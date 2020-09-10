# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: simple.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='simple.proto',
  package='simple',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0csimple.proto\x12\x06simple\"*\n\rSimpleRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03msg\x18\x02 \x01(\t\"?\n\x11SimpleRequestList\x12*\n\x0bperson_list\x18\x01 \x03(\x0b\x32\x15.simple.SimpleRequest\"#\n\x0eSimpleResponse\x12\x11\n\treply_msg\x18\x01 \x01(\t\"C\n\x12SimpleResponseList\x12-\n\rresponse_list\x18\x01 \x03(\x0b\x32\x16.simple.SimpleResponse2V\n\rSimpleService\x12\x45\n\nSimpleSend\x12\x19.simple.SimpleRequestList\x1a\x1a.simple.SimpleResponseList\"\x00\x62\x06proto3'
)




_SIMPLEREQUEST = _descriptor.Descriptor(
  name='SimpleRequest',
  full_name='simple.SimpleRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='simple.SimpleRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='msg', full_name='simple.SimpleRequest.msg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=24,
  serialized_end=66,
)


_SIMPLEREQUESTLIST = _descriptor.Descriptor(
  name='SimpleRequestList',
  full_name='simple.SimpleRequestList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='person_list', full_name='simple.SimpleRequestList.person_list', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=68,
  serialized_end=131,
)


_SIMPLERESPONSE = _descriptor.Descriptor(
  name='SimpleResponse',
  full_name='simple.SimpleResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='reply_msg', full_name='simple.SimpleResponse.reply_msg', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=133,
  serialized_end=168,
)


_SIMPLERESPONSELIST = _descriptor.Descriptor(
  name='SimpleResponseList',
  full_name='simple.SimpleResponseList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='response_list', full_name='simple.SimpleResponseList.response_list', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=170,
  serialized_end=237,
)

_SIMPLEREQUESTLIST.fields_by_name['person_list'].message_type = _SIMPLEREQUEST
_SIMPLERESPONSELIST.fields_by_name['response_list'].message_type = _SIMPLERESPONSE
DESCRIPTOR.message_types_by_name['SimpleRequest'] = _SIMPLEREQUEST
DESCRIPTOR.message_types_by_name['SimpleRequestList'] = _SIMPLEREQUESTLIST
DESCRIPTOR.message_types_by_name['SimpleResponse'] = _SIMPLERESPONSE
DESCRIPTOR.message_types_by_name['SimpleResponseList'] = _SIMPLERESPONSELIST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SimpleRequest = _reflection.GeneratedProtocolMessageType('SimpleRequest', (_message.Message,), {
  'DESCRIPTOR' : _SIMPLEREQUEST,
  '__module__' : 'simple_pb2'
  # @@protoc_insertion_point(class_scope:simple.SimpleRequest)
  })
_sym_db.RegisterMessage(SimpleRequest)

SimpleRequestList = _reflection.GeneratedProtocolMessageType('SimpleRequestList', (_message.Message,), {
  'DESCRIPTOR' : _SIMPLEREQUESTLIST,
  '__module__' : 'simple_pb2'
  # @@protoc_insertion_point(class_scope:simple.SimpleRequestList)
  })
_sym_db.RegisterMessage(SimpleRequestList)

SimpleResponse = _reflection.GeneratedProtocolMessageType('SimpleResponse', (_message.Message,), {
  'DESCRIPTOR' : _SIMPLERESPONSE,
  '__module__' : 'simple_pb2'
  # @@protoc_insertion_point(class_scope:simple.SimpleResponse)
  })
_sym_db.RegisterMessage(SimpleResponse)

SimpleResponseList = _reflection.GeneratedProtocolMessageType('SimpleResponseList', (_message.Message,), {
  'DESCRIPTOR' : _SIMPLERESPONSELIST,
  '__module__' : 'simple_pb2'
  # @@protoc_insertion_point(class_scope:simple.SimpleResponseList)
  })
_sym_db.RegisterMessage(SimpleResponseList)



_SIMPLESERVICE = _descriptor.ServiceDescriptor(
  name='SimpleService',
  full_name='simple.SimpleService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=239,
  serialized_end=325,
  methods=[
  _descriptor.MethodDescriptor(
    name='SimpleSend',
    full_name='simple.SimpleService.SimpleSend',
    index=0,
    containing_service=None,
    input_type=_SIMPLEREQUESTLIST,
    output_type=_SIMPLERESPONSELIST,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SIMPLESERVICE)

DESCRIPTOR.services_by_name['SimpleService'] = _SIMPLESERVICE

# @@protoc_insertion_point(module_scope)