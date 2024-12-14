import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../utils'))
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../pb2_module/user'))

from commands import *
from user_pb2_grpc import *

from errors import *
from exceptions.server_error_exception import *


class UserService:
    def __init__(self, server_host):
        channel = grpc.insecure_channel(server_host)
        self.stub = UserServiceStub(channel)

    def register_user(self, message) -> str:
        user_id = proto_dot_user__pb2.UserId(id=message.from_user.id)
        response = self.stub.RegisterUser(user_id)
        if response is None:
            raise ServerErrorException(errors['server_error']())

        username = message.from_user.first_name + ' ' + message.from_user.last_name
        return username

    def get_user(self, message):
        user_id = proto_dot_user__pb2.UserId(id=message.from_user.id)
        response = self.stub.GetUserByID(user_id)
        if response is None:
            raise ServerErrorException(errors['server_error']())
        username = message.from_user.first_name + ' ' + message.from_user.last_name
        return username
