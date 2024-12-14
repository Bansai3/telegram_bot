import os
import sys
from datetime import timedelta
from tabnanny import check

import requests

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'services'))

import datetime

import telebot
from dotenv import load_dotenv
from telebot import types

import sys
import os

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../utils'))
from subscription_service import SubscriptionService
from services.user_service import *
from services.vpn_service import *
from logging_config import setup_logging


class TelegramBot:

    def __init__(self):
        self.log = setup_logging()

        load_dotenv()
        self.bot_token = self.__get_bot_token()
        self.server_host = self.__get_server_host()
        self.subscription_link = self.__get_subscription_link()
        self.subscription_group_id = self.__get_subscription_group_id()

        self.__user_service = UserService(self.server_host)
        self.__payment_service = SubscriptionService(self.server_host)
        self.__vpn_service = VPNService(self.server_host)

        self.bot = telebot.TeleBot(self.bot_token)
        self.users_subscription_countries = {}
        self.countries = set()

    def start(self):
        try:
            self.__check_env_variables()
        except EnvironmentVariableErrorException as e:
            self.log.error(str(e))
            return

        self.countries = set(self.__get_countries())
        if self.countries is None:
            self.log.error("No countries configured")
            return
        self.handle_button()
        self.log.info('Bot started successfully: %s', datetime.datetime.now())

    def handle_button(self):
        @self.bot.message_handler(commands=['start'])
        def handle_start_command(message):
            self.handle_start_command(message)

        @self.bot.message_handler(content_types=['text'])
        def handle_commands(message):
            return self.handle_commands(message)

        self.bot.polling(none_stop=True)


    def handle_commands(self, message):
        if message.text == 'Информация о боте':
            self.handle_info_command(message)
        elif message.text == 'Подписка':
            self.handle_subscription_command(message)
        elif message.text == 'Информация о подписке':
            self.handle_subscription_info_command(message)
        elif message.text == 'Вернуться в меню':
            self.handle_get_back_to_menu(message)
        elif message.text == 'Купить подписку':
            self.handle_buy_subscription_command(message)
        elif message.text in self.countries:
            self.users_subscription_countries[message.from_user.id] = message.text
            self.handle_subscription_choices(message)
        elif message.text == "Вернуться к покупке подписки":
            self.handle_get_back_to_buy_subscription_command(message)
        elif message.text == "Вернуться к выбору страны":
            self.handle_buy_subscription_command(message)
        elif message.text == "Платная подписка":
            self.handle_get_subscription(message)
        elif message.text == "Пробная подписка":
            self.handle_get_trial_subscription(message)
        elif message.text == "Я оплатил":
            self.handle_pay_subscription(message)
        elif message.text == "Вернуться к выбору подписики":
            self.handle_subscription_choices(message)


    def handle_get_back_to_menu(self, message):
        markup = self.__get_menu_buttons()
        self.bot.send_message(message.chat.id, "Меню:", reply_markup=markup)


    def handle_info_command(self, message):
        markup = self.__get_menu_buttons()
        self.bot.send_message(message.chat.id, commands['info'](), parse_mode='html', reply_markup=markup)

    def handle_start_command(self, message):
        try:
            user_name = self.__user_service.get_user(message)
            markup = self.__get_menu_buttons()
            self.bot.send_message(message.chat.id, commands['start'](user_name), parse_mode='html', reply_markup=markup)
        except ServerErrorException:
            self.bot.send_message(message.chat.id, commands['server_error'](), parse_mode='html')
        except Exception:
            response_message = self.__user_service.register_user(message)
            markup = self.__get_menu_buttons()
            self.bot.send_message(message.chat.id, commands['start'](response_message), parse_mode='html', reply_markup=markup)


    def handle_subscription_info_command(self, message):
        markup = self.__get_menu_buttons()
        self.bot.send_message(message.chat.id, commands['subscription_info'](), parse_mode='html', reply_markup=markup)

    def handle_subscription_command(self, message):
        markup = self.__get_buy_subscription_buttons()
        self.bot.send_message(message.chat.id,
                              'Нажмите "Купить подписку" если хотите приобрести пробную или платную подписку',
                              reply_markup=markup)


    def handle_buy_subscription_command(self, message):
        markup = self.__get_countries_buttons(self.countries)
        self.bot.send_message(message.chat.id, 'Выберите страну:', reply_markup=markup)

    def handle_get_back_to_buy_subscription_command(self, message):
        markup = self.__get_buy_subscription_buttons()
        self.bot.send_message(message.chat.id,
                              'Нажмите "Купить подписку" если хотите приобрести пробную или платную подписку',
                              reply_markup=markup)


    def handle_subscription_choices(self, message):
        markup = self.__get_subscription_choices_buttons(message)
        self.bot.send_message(message.chat.id, 'Выберите подписку', reply_markup=markup)


    def handle_get_trial_subscription(self, message):
        markup = self.__get_menu_buttons()
        try:
            country_name = self.users_subscription_countries[message.from_user.id]
            key_value = self.__get_key(country_name, message.from_user.id, True)
            self.bot.send_message(message.chat.id, commands['key'](key_value), parse_mode='html', reply_markup=markup)
        except ServerErrorException as e:
            self.bot.send_message(message.chat.id, str(e), reply_markup=markup)
        except TypeError as e:
            self.bot.send_message(message.chat.id, "Надо выбрать страну для покупки подписки!", reply_markup=markup)
        except:
            self.bot.send_message(message.chat.id, errors['trial_subscription_already_bought'](), reply_markup=markup)

    def handle_get_subscription(self, message):
        markup = self.__get_menu_buttons()
        try:
            country_name = self.users_subscription_countries[message.from_user.id]
            subscriptions_ids = self.__get_user_subscriptions(message.from_user.id)
            chat_member = self.bot.get_chat_member(self.subscription_group_id, message.from_user.id)
            if len(subscriptions_ids) == 0 and chat_member.status in ['member', 'administrator', 'creator']:
                self.__delete_chat_member(message.from_user.id)
            elif len(subscriptions_ids) != 0 and chat_member.status in ['member', 'administrator',
                                                                        'creator']:
                self.bot.send_message(message.chat.id, errors['subscription_already_bought'](), reply_markup=markup)
                return
        except ServerErrorException as e:
            self.bot.send_message(message.chat.id, str(e), reply_markup=markup)
            return
        except TypeError as e:
            self.bot.send_message(message.chat.id, "Надо выбрать страну для покупки подписки!", reply_markup=markup)
            return
        except Exception as e:
            self.bot.send_message(message.chat.id, str(e), reply_markup=markup)
            return
        markup = self.__get_subscription_paid_button()
        self.bot.send_message(message.chat.id, 'Для оплаты подписки перейдите по данной ссылке:\n\n' +
                              self.subscription_link + '\n\n' + 'После оплаты нажмите "Я оплатил"',
                              reply_markup=markup)

    def handle_pay_subscription(self, message):
        markup = self.__get_menu_buttons()
        try:
            chat_member = self.bot.get_chat_member(self.subscription_group_id, message.from_user.id)
            country_name = self.users_subscription_countries[message.from_user.id]
            if chat_member.status in ['member', 'administrator', 'creator']:
                self.bot.send_message(message.chat.id, commands['paid_sub_info'](), parse_mode='html', reply_markup=markup)
                self.log.info('User %s paid for subscription', message.from_user.id)
                self.log.debug('User info: %s', chat_member.user)

                key_value = self.__get_key(country_name, message.from_user.id, False)
                self.bot.send_message(message.chat.id, commands['key'](key_value), parse_mode='html', reply_markup=markup)
            else:
                self.log.error('User %s is not a member of the subscription group', message.from_user.id)
                self.bot.send_message(message.chat.id, errors['not_found_after_payment_error'](),
                                      parse_mode='html', reply_markup=markup)
        except ServerErrorException as e:
            self.log.error('Error occurred while checking user membership in the subscription group: %s', e)
            self.bot.send_message(message.chat.id, str(e), parse_mode='html', reply_markup=markup)
        except TypeError as e:
            self.log.error('User did not indicate the country for subscription: %s', e)
            self.bot.send_message(message.chat.id, "Надо выбрать страну для покупки подписки!", reply_markup=markup)
        except Exception as e:
            self.log.error('Error occurred while checking user membership in the subscription group: %s', e)
            self.bot.send_message(message.chat.id, errors['server_connection_error'](), parse_mode='html', reply_markup=markup)


    @staticmethod
    def __get_bot_token() -> str:
        return os.getenv("BOT_TOKEN")

    @staticmethod
    def __get_server_host() -> str:
        return os.getenv("SERVER_HOST")

    @staticmethod
    def __get_subscription_link() -> str:
        return os.getenv("SUBSCRIPTION_LINK")

    @staticmethod
    def __get_subscription_group_id() -> str:
        return os.getenv("SUBSCRIPTION_GROUP_ID")


    @staticmethod
    def __get_menu_buttons():
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Информация о боте")
        btn2 = types.KeyboardButton("Подписка")
        btn3 = types.KeyboardButton("Информация о подписке")
        markup.add(btn1, btn2, btn3)
        return markup


    @staticmethod
    def __get_buy_subscription_buttons():
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Вернуться в меню")
        btn2 = types.KeyboardButton("Купить подписку")
        markup.add(btn1, btn2)
        return markup

    @staticmethod
    def __get_countries_buttons(countries):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for country in countries:
            markup.add(types.KeyboardButton(text=country))
        btn = types.KeyboardButton("Вернуться к покупке подписки")
        markup.add(btn)
        return markup

    @staticmethod
    def __get_subscription_choices_buttons(countries):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Платная подписка")
        btn2 = types.KeyboardButton("Пробная подписка")
        btn3 = types.KeyboardButton("Вернуться к выбору страны")
        markup.add(btn1, btn2, btn3)
        return markup

    @staticmethod
    def __get_subscription_paid_button():
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Я оплатил")
        btn2 = types.KeyboardButton("Вернуться к выбору подписки")
        markup.add(btn1, btn2)
        return markup

    def __get_countries(self):
        try:
            countries = self.__vpn_service.get_countries()
        except Exception as e:
            return None
        return [country.name for country in countries]


    def __get_key(self, country_name, user_id, is_trial):
        country = self.__vpn_service.get_country_by_name(country_name)
        subscription = self.__payment_service.buy_subscription(country.id, user_id, is_trial)
        key_value = self.__vpn_service.get_key(subscription.id)
        return key_value

    def __get_user_subscriptions(self, user_id):
        subscriptions_ids = self.__payment_service.get_all_user_subscriptions(user_id)
        return subscriptions_ids

    def __check_env_variables(self):
        if self.bot_token is None or \
           self.subscription_group_id is None or \
           self.server_host is None or \
           self.subscription_link is None:
            raise EnvironmentVariableErrorException(errors['environment_variables_error'])

    def __delete_chat_member(self, user_id):
        payload = {
            "chat_id": self.subscription_group_id,
            "user_id": user_id
        }

        url = f"https://api.telegram.org/bot{self.bot_token}/banChatMember"

        response = requests.post(url, json=payload)

        if response.status_code != 200:
            self.log.info(f'Error deleting chat member! {response.text}')
            raise Exception(f"{response.text}")
