# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: a_e.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='a_e.proto',
  package='bayouapp',
  syntax='proto3',
  serialized_pb=_b('\n\ta_e.proto\x12\x08\x62\x61youapp\"\x88\x01\n\rcalendarEntry\x12\x11\n\tmessageid\x18\x01 \x01(\t\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x0f\n\x07romm_no\x18\x03 \x01(\t\x12\x0e\n\x06\x62_date\x18\x04 \x01(\t\x12\x0e\n\x06\x62_time\x18\x05 \x01(\t\x12\x11\n\ttimestamp\x18\x06 \x01(\x01\x12\x0e\n\x06status\x18\x07 \x01(\t\"\x13\n\x04test\x12\x0b\n\x03num\x18\x01 \x01(\x05\x32~\n\x05\x42\x61you\x12\x44\n\x0c\x61nti_entropy\x12\x17.bayouapp.calendarEntry\x1a\x17.bayouapp.calendarEntry(\x01\x30\x01\x12/\n\tchecktest\x12\x0e.bayouapp.test\x1a\x0e.bayouapp.test(\x01\x30\x01\x42/\n\x16io.grpc.examples.bayouB\rBayouAPPProtoP\x01\xa2\x02\x03\x42\x41Pb\x06proto3')
)




_CALENDARENTRY = _descriptor.Descriptor(
  name='calendarEntry',
  full_name='bayouapp.calendarEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='messageid', full_name='bayouapp.calendarEntry.messageid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='username', full_name='bayouapp.calendarEntry.username', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='romm_no', full_name='bayouapp.calendarEntry.romm_no', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='b_date', full_name='bayouapp.calendarEntry.b_date', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='b_time', full_name='bayouapp.calendarEntry.b_time', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='bayouapp.calendarEntry.timestamp', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='bayouapp.calendarEntry.status', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=24,
  serialized_end=160,
)


_TEST = _descriptor.Descriptor(
  name='test',
  full_name='bayouapp.test',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='num', full_name='bayouapp.test.num', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=162,
  serialized_end=181,
)

DESCRIPTOR.message_types_by_name['calendarEntry'] = _CALENDARENTRY
DESCRIPTOR.message_types_by_name['test'] = _TEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

calendarEntry = _reflection.GeneratedProtocolMessageType('calendarEntry', (_message.Message,), dict(
  DESCRIPTOR = _CALENDARENTRY,
  __module__ = 'a_e_pb2'
  # @@protoc_insertion_point(class_scope:bayouapp.calendarEntry)
  ))
_sym_db.RegisterMessage(calendarEntry)

test = _reflection.GeneratedProtocolMessageType('test', (_message.Message,), dict(
  DESCRIPTOR = _TEST,
  __module__ = 'a_e_pb2'
  # @@protoc_insertion_point(class_scope:bayouapp.test)
  ))
_sym_db.RegisterMessage(test)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\026io.grpc.examples.bayouB\rBayouAPPProtoP\001\242\002\003BAP'))

_BAYOU = _descriptor.ServiceDescriptor(
  name='Bayou',
  full_name='bayouapp.Bayou',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=183,
  serialized_end=309,
  methods=[
  _descriptor.MethodDescriptor(
    name='anti_entropy',
    full_name='bayouapp.Bayou.anti_entropy',
    index=0,
    containing_service=None,
    input_type=_CALENDARENTRY,
    output_type=_CALENDARENTRY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='checktest',
    full_name='bayouapp.Bayou.checktest',
    index=1,
    containing_service=None,
    input_type=_TEST,
    output_type=_TEST,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_BAYOU)

DESCRIPTOR.services_by_name['Bayou'] = _BAYOU

# @@protoc_insertion_point(module_scope)
