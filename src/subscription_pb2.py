# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: proto/subscription.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'proto/subscription.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18proto/subscription.proto\x12\x05proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x87\x01\n\x0cSubscription\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0f\n\x07user_id\x18\x02 \x01(\x03\x12\x12\n\ncountry_id\x18\x03 \x01(\x03\x12\r\n\x05trial\x18\x04 \x01(\x08\x12\x37\n\x13\x65xpiration_datetime\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\";\n\rSubscriptions\x12*\n\rsubscriptions\x18\x01 \x03(\x0b\x32\x13.proto.Subscription\"N\n\x17GetSubscriptionsRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\x03\x12\x12\n\ncountry_id\x18\x02 \x01(\x03\x12\x0e\n\x06\x61\x63tive\x18\x03 \x01(\x08\"\x88\x01\n\x19\x43reateSubscriptionRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\x03\x12\x12\n\ncountry_id\x18\x02 \x01(\x03\x12\r\n\x05trial\x18\x03 \x01(\x08\x12\x37\n\x13\x65xpiration_datetime\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp2\xae\x01\n\x13SubscriptionService\x12H\n\x10GetSubscriptions\x12\x1e.proto.GetSubscriptionsRequest\x1a\x14.proto.Subscriptions\x12M\n\x14\x41\x63tivateSubscription\x12 .proto.CreateSubscriptionRequest\x1a\x13.proto.Subscriptionb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.subscription_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_SUBSCRIPTION']._serialized_start=69
  _globals['_SUBSCRIPTION']._serialized_end=204
  _globals['_SUBSCRIPTIONS']._serialized_start=206
  _globals['_SUBSCRIPTIONS']._serialized_end=265
  _globals['_GETSUBSCRIPTIONSREQUEST']._serialized_start=267
  _globals['_GETSUBSCRIPTIONSREQUEST']._serialized_end=345
  _globals['_CREATESUBSCRIPTIONREQUEST']._serialized_start=348
  _globals['_CREATESUBSCRIPTIONREQUEST']._serialized_end=484
  _globals['_SUBSCRIPTIONSERVICE']._serialized_start=487
  _globals['_SUBSCRIPTIONSERVICE']._serialized_end=661
# @@protoc_insertion_point(module_scope)
