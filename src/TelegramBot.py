import datetime

import telebot
from dotenv import load_dotenv
import os
from telebot import types

from subscription_service import SubscriptionService
from user_service import *
from vpn_service import *
from logging_config import setup_logging


class TelegramBot:

    def __init__(self):
        host = self.__get_server_host()
        self.__user_service = UserService(host)
        self.__payment_service = SubscriptionService(host)
        self.__vpn_service = VPNService(host)
        self.log = setup_logging()

    def start(self):
        self.handle_button()
        self.log.info('Bot started successfully: %s', datetime.datetime.now())

    def handle_button(self):
        bot_token = self.__get_bot_token()
        bot = telebot.TeleBot(bot_token)

        @bot.message_handler(commands=['start'])
        def handle_start_command(message):
            try:
                user_name = self.__user_service.get_user(message)
                bot.send_message(message.chat.id, commands['start'](user_name), parse_mode='html')
            except ServerErrorException as e:
                bot.send_message(message.chat.id, commands['server_error'](), parse_mode='html')
            except Exception as e:
                print(str(e))
                response_message = self.__user_service.register_user(message)
                bot.send_message(message.chat.id, commands['start'](response_message), parse_mode='html')
            # bot.send_message(message.chat.id, commands['start'](message.from_user.first_name + ' ' + message.from_user.last_name), parse_mode='html')

        @bot.message_handler(commands=['info'])
        def handle_info_command(message):
            bot.send_message(message.chat.id, commands['info'](), parse_mode='html')

        @bot.message_handler(commands=['subscription_info'])
        def handle_subscription_info_command(message):
            bot.send_message(message.chat.id, commands['subscription_info'](), parse_mode='html')

        @bot.message_handler(commands=['subscription'])
        def handle_payment_command(message):
            markup_inline = types.InlineKeyboardMarkup()
            item_subscription = types.InlineKeyboardButton(text='Купить подписку', callback_data='buy_sub')
            markup_inline.add(item_subscription)
            bot.send_message(message.chat.id,
                             'Нажжмите "Купить подписку" если хотите приобрести пробную или платную подписку',
                             reply_markup=markup_inline)

        @bot.callback_query_handler(func=lambda call: True)
        def subscription_handler(call):
            if call.data == 'buy_sub':
                try:
                    countries = self.__vpn_service.get_countries()
                except ServerErrorException as e:
                    bot.send_message(call.message.chat.id, str(e))
                    return
                except Exception as e:
                    bot.send_message(call.message.chat.id, str(e))
                    return
                markup_inline = types.InlineKeyboardMarkup()
                for country in countries:
                    markup_inline.add(
                        types.InlineKeyboardButton(text=country.name, callback_data=f'country_{country.name}'))
                bot.send_message(call.message.chat.id, 'Выберите страну', reply_markup=markup_inline)
            else:
                command_parts = call.data.split('_')
                if command_parts[0] == 'country':
                    markup_inline = types.InlineKeyboardMarkup()
                    item_trial_subscription = types.InlineKeyboardButton(text='Пробная подписка',
                                                                         callback_data=f'trial_sub_{call.data}')
                    item_subscription = types.InlineKeyboardButton(text='Платная подписка',
                                                                   callback_data=f'sub_{call.data}')
                    markup_inline.add(item_trial_subscription, item_subscription)
                    bot.send_message(call.message.chat.id, 'Выберите подписку', reply_markup=markup_inline)
                elif command_parts[0] == 'trial':
                    try:
                        key_value = self.__get_key(call.data, call.from_user.id, True)
                        bot.send_message(call.message.chat.id, commands['key'](key_value), parse_mode='html')
                    except ServerErrorException as e:
                        bot.send_message(call.message.chat.id, str(e))
                    except:
                        bot.send_message(call.message.chat.id, errors['trial_subscription_already_bought']())
                elif command_parts[0] == 'sub':
                    try:
                        subscriptions_ids = self.__get_user_subscriptions(call.from_user.id)
                        chat_member = bot.get_chat_member(self.__get_subscription_group_id(), call.from_user.id)
                        if len(subscriptions_ids) == 0 and chat_member.status in ['member', 'administrator', 'creator']:
                            bot.ban_chat_member(call.message.chat.id, call.from_user.id)
                            bot.unban_chat_member(call.message.chat.id, call.from_user.id)
                        elif len(subscriptions_ids) != 0 and chat_member.status in ['member', 'administrator', 'creator']:
                            bot.send_message(call.message.chat.id, errors['subscription_already_bought']())
                            return
                    except ServerErrorException as e:
                        bot.send_message(call.message.chat.id, str(e))
                        return
                    bot.send_message(call.message.chat.id, 'Для оплаты подписки перейдите по данной ссылке:\n\n' +
                                     self.__get_subscription_link())
                    markup_inline = types.InlineKeyboardMarkup()
                    user_paid_sub = types.InlineKeyboardButton(text='Я оплатил',
                                                               callback_data=f'paid_{call.data}')
                    markup_inline.add(user_paid_sub)
                    bot.send_message(call.message.chat.id, 'После оплаты нажмите "Я оплатил"',
                                     reply_markup=markup_inline)
                elif command_parts[0] == 'paid':
                    try:
                        chat_member = bot.get_chat_member(self.__get_subscription_group_id(), call.from_user.id)
                        if chat_member.status in ['member', 'administrator', 'creator']:
                            bot.send_message(call.message.chat.id, commands['paid_sub_info'](), parse_mode='html')
                            self.log.info('User %s paid for subscription', call.from_user.id)
                            self.log.debug('User info: %s', chat_member.user)

                            key_value = self.__get_key(call.data, call.from_user.id, False)
                            bot.send_message(call.message.chat.id, commands['key'](key_value), parse_mode='html')
                        else:
                            self.log.error('User %s is not a member of the subscription group', call.from_user.id)
                            bot.send_message(call.message.chat.id, errors['not_found_after_payment_error'](),
                                             parse_mode='html')
                    except ServerErrorException as e:
                        self.log.error('Error occurred while checking user membership in the subscription group: %s', e)
                        bot.send_message(call.message.chat.id, str(e), parse_mode='html')
                    except Exception as e:
                        self.log.error('Error occurred while checking user membership in the subscription group: %s', e)
                        bot.send_message(call.message.chat.id, errors['server_connection_error'], parse_mode='html')

        bot.polling(none_stop=True)

    @staticmethod
    def __get_bot_token() -> str:
        load_dotenv()
        return os.getenv("BOT_TOKEN")

    @staticmethod
    def __get_server_host() -> str:
        load_dotenv()
        return os.getenv("SERVER_HOST")

    @staticmethod
    def __get_subscription_link() -> str:
        load_dotenv()
        return os.getenv("SUBSCRIPTION_LINK")

    @staticmethod
    def __get_subscription_group_id() -> str:
        load_dotenv()
        return os.getenv("SUBSCRIPTION_GROUP_ID")

    def __get_key(self, subscription_info, user_id, is_trial):
        subscription_parts = subscription_info.split('_')
        country_name = subscription_parts[-1]
        country = self.__vpn_service.get_country_by_name(country_name)
        subscription = self.__payment_service.buy_subscription(country.id, user_id, is_trial)
        key_value = self.__vpn_service.get_key(subscription.id)
        return key_value

    def __get_user_subscriptions(self, user_id):
        subscriptions_ids = self.__payment_service.get_all_user_subscriptions(user_id)
        return subscriptions_ids
