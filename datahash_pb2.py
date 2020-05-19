# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: datahash.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='datahash.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x0e\x64\x61tahash.proto\"\x14\n\x04Text\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\t2-\n\x08\x44\x61taHash\x12!\n\x0freceive_message\x12\x05.Text\x1a\x05.Text\"\x00\x62\x06proto3'
)




_TEXT = _descriptor.Descriptor(
  name='Text',
  full_name='Text',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='Text.data', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=18,
  serialized_end=38,
)

DESCRIPTOR.message_types_by_name['Text'] = _TEXT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Text = _reflection.GeneratedProtocolMessageType('Text', (_message.Message,), {
  'DESCRIPTOR' : _TEXT,
  '__module__' : 'datahash_pb2'
  # @@protoc_insertion_point(class_scope:Text)
  })
_sym_db.RegisterMessage(Text)



_DATAHASH = _descriptor.ServiceDescriptor(
  name='DataHash',
  full_name='DataHash',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=40,
  serialized_end=85,
  methods=[
  _descriptor.MethodDescriptor(
    name='receive_message',
    full_name='DataHash.receive_message',
    index=0,
    containing_service=None,
    input_type=_TEXT,
    output_type=_TEXT,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_DATAHASH)

DESCRIPTOR.services_by_name['DataHash'] = _DATAHASH

# @@protoc_insertion_point(module_scope)