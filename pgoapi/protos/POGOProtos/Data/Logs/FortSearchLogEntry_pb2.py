# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: POGOProtos/Data/Logs/FortSearchLogEntry.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from POGOProtos.Inventory.Item import ItemData_pb2 as POGOProtos_dot_Inventory_dot_Item_dot_ItemData__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='POGOProtos/Data/Logs/FortSearchLogEntry.proto',
  package='POGOProtos.Data.Logs',
  syntax='proto3',
  serialized_pb=_b('\n-POGOProtos/Data/Logs/FortSearchLogEntry.proto\x12\x14POGOProtos.Data.Logs\x1a(POGOProtos/Inventory/Item/ItemData.proto\"\xca\x01\n\x12\x46ortSearchLogEntry\x12?\n\x06result\x18\x01 \x01(\x0e\x32/.POGOProtos.Data.Logs.FortSearchLogEntry.Result\x12\x0f\n\x07\x66ort_id\x18\x02 \x01(\t\x12\x32\n\x05items\x18\x03 \x03(\x0b\x32#.POGOProtos.Inventory.Item.ItemData\x12\x0c\n\x04\x65ggs\x18\x04 \x01(\x05\" \n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x62\x06proto3')
  ,
  dependencies=[POGOProtos_dot_Inventory_dot_Item_dot_ItemData__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_FORTSEARCHLOGENTRY_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='POGOProtos.Data.Logs.FortSearchLogEntry.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=284,
  serialized_end=316,
)
_sym_db.RegisterEnumDescriptor(_FORTSEARCHLOGENTRY_RESULT)


_FORTSEARCHLOGENTRY = _descriptor.Descriptor(
  name='FortSearchLogEntry',
  full_name='POGOProtos.Data.Logs.FortSearchLogEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='POGOProtos.Data.Logs.FortSearchLogEntry.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fort_id', full_name='POGOProtos.Data.Logs.FortSearchLogEntry.fort_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='items', full_name='POGOProtos.Data.Logs.FortSearchLogEntry.items', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='eggs', full_name='POGOProtos.Data.Logs.FortSearchLogEntry.eggs', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _FORTSEARCHLOGENTRY_RESULT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=114,
  serialized_end=316,
)

_FORTSEARCHLOGENTRY.fields_by_name['result'].enum_type = _FORTSEARCHLOGENTRY_RESULT
_FORTSEARCHLOGENTRY.fields_by_name['items'].message_type = POGOProtos_dot_Inventory_dot_Item_dot_ItemData__pb2._ITEMDATA
_FORTSEARCHLOGENTRY_RESULT.containing_type = _FORTSEARCHLOGENTRY
DESCRIPTOR.message_types_by_name['FortSearchLogEntry'] = _FORTSEARCHLOGENTRY

FortSearchLogEntry = _reflection.GeneratedProtocolMessageType('FortSearchLogEntry', (_message.Message,), dict(
  DESCRIPTOR = _FORTSEARCHLOGENTRY,
  __module__ = 'POGOProtos.Data.Logs.FortSearchLogEntry_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Data.Logs.FortSearchLogEntry)
  ))
_sym_db.RegisterMessage(FortSearchLogEntry)


# @@protoc_insertion_point(module_scope)
