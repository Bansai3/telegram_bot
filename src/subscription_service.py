from subscription_pb2_grpc import *
from errors import *
from server_error_exception import *
import datetime
from google.protobuf.timestamp_pb2 import Timestamp


class SubscriptionService:

    def __init__(self, server_host):
        channel = grpc.insecure_channel(server_host)
        self.stub = SubscriptionServiceStub(channel)

    def buy_subscription(self, country_id, user_id, is_trial):
        if is_trial:
            now = datetime.datetime.now()
            two_days_later = now + datetime.timedelta(days=2)
            expiration_timestamp = Timestamp()
            expiration_timestamp.FromDatetime(two_days_later)
        else:
            now = datetime.datetime.now()
            two_days_later = now + datetime.timedelta(days=30)
            expiration_timestamp = Timestamp()
            expiration_timestamp.FromDatetime(two_days_later)

        sub_request = proto_dot_subscription__pb2.CreateSubscriptionRequest(user_id, country_id, is_trial,
                                                                            expiration_timestamp)

        response = self.stub.ActivateSubscription(sub_request)

        if response is None:
            raise ServerErrorException(errors['server_error']())

        return response