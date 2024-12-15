# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import country_pb2 as country__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2

GRPC_GENERATED_VERSION = '1.67.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in country_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class CountryServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetAllCountries = channel.unary_unary(
                '/proto.CountryService/GetAllCountries',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=country__pb2.Countries.FromString,
                _registered_method=True)
        self.GetCountryByName = channel.unary_unary(
                '/proto.CountryService/GetCountryByName',
                request_serializer=country__pb2.CountryName.SerializeToString,
                response_deserializer=country__pb2.Country.FromString,
                _registered_method=True)
        self.CreateCountry = channel.unary_unary(
                '/proto.CountryService/CreateCountry',
                request_serializer=country__pb2.CountryCreateRequest.SerializeToString,
                response_deserializer=country__pb2.Country.FromString,
                _registered_method=True)


class CountryServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetAllCountries(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCountryByName(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateCountry(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CountryServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetAllCountries': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAllCountries,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=country__pb2.Countries.SerializeToString,
            ),
            'GetCountryByName': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCountryByName,
                    request_deserializer=country__pb2.CountryName.FromString,
                    response_serializer=country__pb2.Country.SerializeToString,
            ),
            'CreateCountry': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateCountry,
                    request_deserializer=country__pb2.CountryCreateRequest.FromString,
                    response_serializer=country__pb2.Country.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'proto.CountryService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('proto.CountryService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class CountryService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetAllCountries(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/proto.CountryService/GetAllCountries',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            country__pb2.Countries.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetCountryByName(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/proto.CountryService/GetCountryByName',
            country__pb2.CountryName.SerializeToString,
            country__pb2.Country.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def CreateCountry(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/proto.CountryService/CreateCountry',
            country__pb2.CountryCreateRequest.SerializeToString,
            country__pb2.Country.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
