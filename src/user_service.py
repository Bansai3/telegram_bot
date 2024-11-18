from user_pb2_grpc import *
from errors import *
from commands import *
from server_error_exception import *
from user_not_found_exception import *


class UserService:
    def __init__(self, server_host):
        channel = grpc.insecure_channel(server_host)
        self.stub = UserServiceStub(channel)

    def register_user(self, message) -> str:
        user_id = proto_dot_user__pb2.UserId(id=message.from_user.id)
        if self.get_user(user_id) is None:
            response = self.stub.RegisterUser(user_id)
            if response is None:
                raise ServerErrorException(errors['server_error']())

        username = message.from_user.first_name + ' ' + message.from_user.last_name
        return commands['start'](username)

    def get_user(self, message):
        user_id = proto_dot_user__pb2.UserId(message.from_user.id)
        response = self.stub.GetUserByID(user_id)
        if response is None:
            raise ServerErrorException(errors['server_error']())
        username = message.from_user.first_name + ' ' + message.from_user.last_name
        return commands['start'](username)
