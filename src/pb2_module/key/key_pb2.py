# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: key.proto
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
    'key.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import user_pb2 as user__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tkey.proto\x12\x05proto\x1a\nuser.proto\"l\n\x03Key\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\x12 \n\x08key_type\x18\x03 \x01(\x0e\x32\x0e.proto.KeyType\x12\x17\n\x0fsubscription_id\x18\x04 \x01(\x03\x12\x10\n\x08proxy_id\x18\x05 \x01(\x03\"v\n\rCountriesKeys\x12,\n\x04keys\x18\x01 \x03(\x0b\x32\x1e.proto.CountriesKeys.KeysEntry\x1a\x37\n\tKeysEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x19\n\x05value\x18\x02 \x01(\x0b\x32\n.proto.Key:\x02\x38\x01\"%\n\nKeyRequest\x12\x17\n\x0fsubscription_id\x18\x01 \x01(\x03*(\n\x07KeyType\x12\x08\n\x04Text\x10\x00\x12\x08\n\x04\x46ile\x10\x01\x12\t\n\x05Photo\x10\x02\x32q\n\nKeyService\x12\'\n\x06GetKey\x12\x11.proto.KeyRequest\x1a\n.proto.Key\x12:\n\x13GetActiveKeysByUser\x12\r.proto.UserId\x1a\x14.proto.CountriesKeysb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'key_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_COUNTRIESKEYS_KEYSENTRY']._loaded_options = None
  _globals['_COUNTRIESKEYS_KEYSENTRY']._serialized_options = b'8\001'
  _globals['_KEYTYPE']._serialized_start=301
  _globals['_KEYTYPE']._serialized_end=341
  _globals['_KEY']._serialized_start=32
  _globals['_KEY']._serialized_end=140
  _globals['_COUNTRIESKEYS']._serialized_start=142
  _globals['_COUNTRIESKEYS']._serialized_end=260
  _globals['_COUNTRIESKEYS_KEYSENTRY']._serialized_start=205
  _globals['_COUNTRIESKEYS_KEYSENTRY']._serialized_end=260
  _globals['_KEYREQUEST']._serialized_start=262
  _globals['_KEYREQUEST']._serialized_end=299
  _globals['_KEYSERVICE']._serialized_start=343
  _globals['_KEYSERVICE']._serialized_end=456
# @@protoc_insertion_point(module_scope)
