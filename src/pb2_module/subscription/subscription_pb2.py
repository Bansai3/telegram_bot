# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: subscription.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
import os
import sys

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../user'))

import user_pb2 as user__pb2

_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'subscription.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12subscription.proto\x12\x05proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\nuser.proto\"\x87\x01\n\x0cSubscription\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0f\n\x07user_id\x18\x02 \x01(\x03\x12\x12\n\ncountry_id\x18\x03 \x01(\x03\x12\r\n\x05trial\x18\x04 \x01(\x08\x12\x37\n\x13\x65xpiration_datetime\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\";\n\rSubscriptions\x12*\n\rsubscriptions\x18\x01 \x03(\x0b\x32\x13.proto.Subscription\"N\n\x17GetSubscriptionsRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\x03\x12\x12\n\ncountry_id\x18\x02 \x01(\x03\x12\x0e\n\x06\x61\x63tive\x18\x03 \x01(\x08\"\x88\x01\n\x19\x43reateSubscriptionRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\x03\x12\x12\n\ncountry_id\x18\x02 \x01(\x03\x12\r\n\x05trial\x18\x03 \x01(\x08\x12\x37\n\x13\x65xpiration_datetime\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"8\n\x1d\x44\x65\x61\x63tivateSubscriptionRequest\x12\x17\n\x0fsubscription_id\x18\x01 \x01(\x03\"@\n\x1dHasActiveSubscriptionResponse\x12\x1f\n\x17has_active_subscription\x18\x01 \x01(\x08\x32\xd4\x02\n\x13SubscriptionService\x12H\n\x10GetSubscriptions\x12\x1e.proto.GetSubscriptionsRequest\x1a\x14.proto.Subscriptions\x12M\n\x14\x41\x63tivateSubscription\x12 .proto.CreateSubscriptionRequest\x1a\x13.proto.Subscription\x12L\n\x15HasActiveSubscription\x12\r.proto.UserId\x1a$.proto.HasActiveSubscriptionResponse\x12V\n\x16\x44\x65\x61\x63tivateSubscription\x12$.proto.DeactivateSubscriptionRequest\x1a\x16.google.protobuf.Emptyb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'subscription_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_SUBSCRIPTION']._serialized_start=104
  _globals['_SUBSCRIPTION']._serialized_end=239
  _globals['_SUBSCRIPTIONS']._serialized_start=241
  _globals['_SUBSCRIPTIONS']._serialized_end=300
  _globals['_GETSUBSCRIPTIONSREQUEST']._serialized_start=302
  _globals['_GETSUBSCRIPTIONSREQUEST']._serialized_end=380
  _globals['_CREATESUBSCRIPTIONREQUEST']._serialized_start=383
  _globals['_CREATESUBSCRIPTIONREQUEST']._serialized_end=519
  _globals['_DEACTIVATESUBSCRIPTIONREQUEST']._serialized_start=521
  _globals['_DEACTIVATESUBSCRIPTIONREQUEST']._serialized_end=577
  _globals['_HASACTIVESUBSCRIPTIONRESPONSE']._serialized_start=579
  _globals['_HASACTIVESUBSCRIPTIONRESPONSE']._serialized_end=643
  _globals['_SUBSCRIPTIONSERVICE']._serialized_start=646
  _globals['_SUBSCRIPTIONSERVICE']._serialized_end=986
# @@protoc_insertion_point(module_scope)
