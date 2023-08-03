# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: clusterfuzz/_internal/protos/process_state.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='clusterfuzz/_internal/protos/process_state.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n0clusterfuzz/_internal/protos/process_state.proto\"\x9f\x03\n\x11ProcessStateProto\x12\x17\n\x0ftime_date_stamp\x18\x01 \x01(\x03\x12\x1b\n\x13process_create_time\x18\r \x01(\x03\x12\'\n\x05\x63rash\x18\x02 \x01(\x0b\x32\x18.ProcessStateProto.Crash\x12\x11\n\tassertion\x18\x03 \x01(\t\x12\x19\n\x11requesting_thread\x18\x04 \x01(\x05\x12*\n\x07threads\x18\x05 \x03(\x0b\x32\x19.ProcessStateProto.Thread\x12\x1c\n\x07modules\x18\x06 \x03(\x0b\x32\x0b.CodeModule\x12\n\n\x02os\x18\x07 \x01(\t\x12\x10\n\x08os_short\x18\x08 \x01(\t\x12\x12\n\nos_version\x18\t \x01(\t\x12\x0b\n\x03\x63pu\x18\n \x01(\t\x12\x10\n\x08\x63pu_info\x18\x0b \x01(\t\x12\x11\n\tcpu_count\x18\x0c \x01(\x05\x1a(\n\x05\x43rash\x12\x0e\n\x06reason\x18\x01 \x02(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x02(\x03\x1a%\n\x06Thread\x12\x1b\n\x06\x66rames\x18\x01 \x03(\x0b\x32\x0b.StackFrame\"\x8e\x03\n\nStackFrame\x12\x13\n\x0binstruction\x18\x01 \x02(\x03\x12\x1b\n\x06module\x18\x02 \x01(\x0b\x32\x0b.CodeModule\x12\x15\n\rfunction_name\x18\x03 \x01(\t\x12\x15\n\rfunction_base\x18\x04 \x01(\x03\x12\x18\n\x10source_file_name\x18\x05 \x01(\t\x12\x13\n\x0bsource_line\x18\x06 \x01(\x05\x12\x18\n\x10source_line_base\x18\x07 \x01(\x03\x12%\n\x05trust\x18\x08 \x01(\x0e\x32\x16.StackFrame.FrameTrust\"\xaf\x01\n\nFrameTrust\x12\x14\n\x10\x46RAME_TRUST_NONE\x10\x00\x12\x14\n\x10\x46RAME_TRUST_SCAN\x10\x01\x12\x18\n\x14\x46RAME_TRUST_CFI_SCAN\x10\x02\x12\x12\n\x0e\x46RAME_TRUST_FP\x10\x03\x12\x13\n\x0f\x46RAME_TRUST_CFI\x10\x04\x12\x19\n\x15\x46RAME_TRUST_PREWALKED\x10\x05\x12\x17\n\x13\x46RAME_TRUST_CONTEXT\x10\x06\"\x9b\x01\n\nCodeModule\x12\x14\n\x0c\x62\x61se_address\x18\x01 \x01(\x03\x12\x0c\n\x04size\x18\x02 \x01(\x03\x12\x11\n\tcode_file\x18\x03 \x01(\t\x12\x17\n\x0f\x63ode_identifier\x18\x04 \x01(\t\x12\x12\n\ndebug_file\x18\x05 \x01(\t\x12\x18\n\x10\x64\x65\x62ug_identifier\x18\x06 \x01(\t\x12\x0f\n\x07version\x18\x07 \x01(\t'
)



_STACKFRAME_FRAMETRUST = _descriptor.EnumDescriptor(
  name='FrameTrust',
  full_name='StackFrame.FrameTrust',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FRAME_TRUST_NONE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FRAME_TRUST_SCAN', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FRAME_TRUST_CFI_SCAN', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FRAME_TRUST_FP', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FRAME_TRUST_CFI', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FRAME_TRUST_PREWALKED', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FRAME_TRUST_CONTEXT', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=694,
  serialized_end=869,
)
_sym_db.RegisterEnumDescriptor(_STACKFRAME_FRAMETRUST)


_PROCESSSTATEPROTO_CRASH = _descriptor.Descriptor(
  name='Crash',
  full_name='ProcessStateProto.Crash',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='reason', full_name='ProcessStateProto.Crash.reason', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='address', full_name='ProcessStateProto.Crash.address', index=1,
      number=2, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=389,
  serialized_end=429,
)

_PROCESSSTATEPROTO_THREAD = _descriptor.Descriptor(
  name='Thread',
  full_name='ProcessStateProto.Thread',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='frames', full_name='ProcessStateProto.Thread.frames', index=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=431,
  serialized_end=468,
)

_PROCESSSTATEPROTO = _descriptor.Descriptor(
  name='ProcessStateProto',
  full_name='ProcessStateProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='time_date_stamp', full_name='ProcessStateProto.time_date_stamp', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='process_create_time', full_name='ProcessStateProto.process_create_time', index=1,
      number=13, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='crash', full_name='ProcessStateProto.crash', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='assertion', full_name='ProcessStateProto.assertion', index=3,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='requesting_thread', full_name='ProcessStateProto.requesting_thread', index=4,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='threads', full_name='ProcessStateProto.threads', index=5,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='modules', full_name='ProcessStateProto.modules', index=6,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='os', full_name='ProcessStateProto.os', index=7,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='os_short', full_name='ProcessStateProto.os_short', index=8,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='os_version', full_name='ProcessStateProto.os_version', index=9,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cpu', full_name='ProcessStateProto.cpu', index=10,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cpu_info', full_name='ProcessStateProto.cpu_info', index=11,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cpu_count', full_name='ProcessStateProto.cpu_count', index=12,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_PROCESSSTATEPROTO_CRASH, _PROCESSSTATEPROTO_THREAD, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=53,
  serialized_end=468,
)


_STACKFRAME = _descriptor.Descriptor(
  name='StackFrame',
  full_name='StackFrame',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='instruction', full_name='StackFrame.instruction', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='module', full_name='StackFrame.module', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='function_name', full_name='StackFrame.function_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='function_base', full_name='StackFrame.function_base', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='source_file_name', full_name='StackFrame.source_file_name', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='source_line', full_name='StackFrame.source_line', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='source_line_base', full_name='StackFrame.source_line_base', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='trust', full_name='StackFrame.trust', index=7,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _STACKFRAME_FRAMETRUST,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=471,
  serialized_end=869,
)


_CODEMODULE = _descriptor.Descriptor(
  name='CodeModule',
  full_name='CodeModule',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='base_address', full_name='CodeModule.base_address', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='size', full_name='CodeModule.size', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='code_file', full_name='CodeModule.code_file', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='code_identifier', full_name='CodeModule.code_identifier', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='debug_file', full_name='CodeModule.debug_file', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='debug_identifier', full_name='CodeModule.debug_identifier', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='version', full_name='CodeModule.version', index=6,
      number=7, type=9, cpp_type=9, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=872,
  serialized_end=1027,
)

_PROCESSSTATEPROTO_CRASH.containing_type = _PROCESSSTATEPROTO
_PROCESSSTATEPROTO_THREAD.fields_by_name['frames'].message_type = _STACKFRAME
_PROCESSSTATEPROTO_THREAD.containing_type = _PROCESSSTATEPROTO
_PROCESSSTATEPROTO.fields_by_name['crash'].message_type = _PROCESSSTATEPROTO_CRASH
_PROCESSSTATEPROTO.fields_by_name['threads'].message_type = _PROCESSSTATEPROTO_THREAD
_PROCESSSTATEPROTO.fields_by_name['modules'].message_type = _CODEMODULE
_STACKFRAME.fields_by_name['module'].message_type = _CODEMODULE
_STACKFRAME.fields_by_name['trust'].enum_type = _STACKFRAME_FRAMETRUST
_STACKFRAME_FRAMETRUST.containing_type = _STACKFRAME
DESCRIPTOR.message_types_by_name['ProcessStateProto'] = _PROCESSSTATEPROTO
DESCRIPTOR.message_types_by_name['StackFrame'] = _STACKFRAME
DESCRIPTOR.message_types_by_name['CodeModule'] = _CODEMODULE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ProcessStateProto = _reflection.GeneratedProtocolMessageType('ProcessStateProto', (_message.Message,), {

  'Crash' : _reflection.GeneratedProtocolMessageType('Crash', (_message.Message,), {
    'DESCRIPTOR' : _PROCESSSTATEPROTO_CRASH,
    '__module__' : 'clusterfuzz._internal.protos.process_state_pb2'
    # @@protoc_insertion_point(class_scope:ProcessStateProto.Crash)
    })
  ,

  'Thread' : _reflection.GeneratedProtocolMessageType('Thread', (_message.Message,), {
    'DESCRIPTOR' : _PROCESSSTATEPROTO_THREAD,
    '__module__' : 'clusterfuzz._internal.protos.process_state_pb2'
    # @@protoc_insertion_point(class_scope:ProcessStateProto.Thread)
    })
  ,
  'DESCRIPTOR' : _PROCESSSTATEPROTO,
  '__module__' : 'clusterfuzz._internal.protos.process_state_pb2'
  # @@protoc_insertion_point(class_scope:ProcessStateProto)
  })
_sym_db.RegisterMessage(ProcessStateProto)
_sym_db.RegisterMessage(ProcessStateProto.Crash)
_sym_db.RegisterMessage(ProcessStateProto.Thread)

StackFrame = _reflection.GeneratedProtocolMessageType('StackFrame', (_message.Message,), {
  'DESCRIPTOR' : _STACKFRAME,
  '__module__' : 'clusterfuzz._internal.protos.process_state_pb2'
  # @@protoc_insertion_point(class_scope:StackFrame)
  })
_sym_db.RegisterMessage(StackFrame)

CodeModule = _reflection.GeneratedProtocolMessageType('CodeModule', (_message.Message,), {
  'DESCRIPTOR' : _CODEMODULE,
  '__module__' : 'clusterfuzz._internal.protos.process_state_pb2'
  # @@protoc_insertion_point(class_scope:CodeModule)
  })
_sym_db.RegisterMessage(CodeModule)


# @@protoc_insertion_point(module_scope)
