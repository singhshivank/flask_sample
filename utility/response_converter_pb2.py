# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: response_converter.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='response_converter.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x18response_converter.proto\"\xd7\x05\n\x04\x64\x61ta\x12\x18\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\n.data.DATA\x1a\xb4\x05\n\x04\x44\x41TA\x12#\n\x07\x63ontent\x18\x01 \x03(\x0b\x32\x12.data.DATA.CONTENT\x12%\n\x08pageInfo\x18\x02 \x01(\x0b\x32\x13.data.DATA.PAGEINFO\x1a\xf0\x03\n\x07\x43ONTENT\x12\x12\n\nresetEmail\x18\x01 \x01(\x08\x12\x11\n\tadminName\x18\x02 \x01(\t\x12\x15\n\rlastUpdatedOn\x18\x03 \x01(\x01\x12\x11\n\taccountId\x18\x04 \x01(\t\x12\x15\n\raccountStatus\x18\x05 \x01(\t\x12\x11\n\tworkOrder\x18\x06 \x01(\t\x12\x11\n\tcreatedOn\x18\x07 \x01(\x01\x12\x14\n\x0c\x61\x64minChanged\x18\x08 \x01(\x08\x12\n\n\x02id\x18\t \x01(\t\x12\x13\n\x0b\x61\x63\x63ountName\x18\n \x01(\t\x12\x12\n\nlicenseKey\x18\x0b \x01(\t\x12\x0e\n\x06\x64omain\x18\x0c \x01(\t\x12/\n\tsiteInfos\x18\r \x03(\x0b\x32\x1c.data.DATA.CONTENT.SITEINFOS\x12\x13\n\x0b\x63ontactName\x18\x0e \x01(\t\x12\x11\n\townerRole\x18\x0f \x01(\t\x12\x0f\n\x07\x63ompany\x18\x10 \x01(\t\x12\x14\n\x0c\x63ontactPhone\x18\x11 \x01(\t\x12\x12\n\nadminEmail\x18\x12 \x01(\t\x12\x19\n\x11\x62lueReaderEnabled\x18\x13 \x01(\x08\x1aM\n\tSITEINFOS\x12\x0e\n\x06\x61wsArn\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x12\n\ndeleteFlag\x18\x03 \x01(\x08\x12\x0e\n\x06siteId\x18\x04 \x01(\t\x1am\n\x08PAGEINFO\x12\x0c\n\x04size\x18\x01 \x01(\t\x12\x18\n\x10numberOfElements\x18\x02 \x01(\t\x12\x15\n\rtotalElements\x18\x03 \x01(\t\x12\x0e\n\x06number\x18\x04 \x01(\t\x12\x12\n\ntotalPages\x18\x05 \x01(\tb\x06proto3'
)




_DATA_DATA_CONTENT_SITEINFOS = _descriptor.Descriptor(
  name='SITEINFOS',
  full_name='data.DATA.CONTENT.SITEINFOS',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='awsArn', full_name='data.DATA.CONTENT.SITEINFOS.awsArn', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='data.DATA.CONTENT.SITEINFOS.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='deleteFlag', full_name='data.DATA.CONTENT.SITEINFOS.deleteFlag', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='siteId', full_name='data.DATA.CONTENT.SITEINFOS.siteId', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=568,
  serialized_end=645,
)

_DATA_DATA_CONTENT = _descriptor.Descriptor(
  name='CONTENT',
  full_name='data.DATA.CONTENT',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resetEmail', full_name='data.DATA.CONTENT.resetEmail', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='adminName', full_name='data.DATA.CONTENT.adminName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lastUpdatedOn', full_name='data.DATA.CONTENT.lastUpdatedOn', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='accountId', full_name='data.DATA.CONTENT.accountId', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='accountStatus', full_name='data.DATA.CONTENT.accountStatus', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='workOrder', full_name='data.DATA.CONTENT.workOrder', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='createdOn', full_name='data.DATA.CONTENT.createdOn', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='adminChanged', full_name='data.DATA.CONTENT.adminChanged', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='data.DATA.CONTENT.id', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='accountName', full_name='data.DATA.CONTENT.accountName', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='licenseKey', full_name='data.DATA.CONTENT.licenseKey', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='domain', full_name='data.DATA.CONTENT.domain', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='siteInfos', full_name='data.DATA.CONTENT.siteInfos', index=12,
      number=13, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='contactName', full_name='data.DATA.CONTENT.contactName', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ownerRole', full_name='data.DATA.CONTENT.ownerRole', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='company', full_name='data.DATA.CONTENT.company', index=15,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='contactPhone', full_name='data.DATA.CONTENT.contactPhone', index=16,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='adminEmail', full_name='data.DATA.CONTENT.adminEmail', index=17,
      number=18, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='blueReaderEnabled', full_name='data.DATA.CONTENT.blueReaderEnabled', index=18,
      number=19, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_DATA_DATA_CONTENT_SITEINFOS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=149,
  serialized_end=645,
)

_DATA_DATA_PAGEINFO = _descriptor.Descriptor(
  name='PAGEINFO',
  full_name='data.DATA.PAGEINFO',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='size', full_name='data.DATA.PAGEINFO.size', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='numberOfElements', full_name='data.DATA.PAGEINFO.numberOfElements', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='totalElements', full_name='data.DATA.PAGEINFO.totalElements', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='number', full_name='data.DATA.PAGEINFO.number', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='totalPages', full_name='data.DATA.PAGEINFO.totalPages', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=647,
  serialized_end=756,
)

_DATA_DATA = _descriptor.Descriptor(
  name='DATA',
  full_name='data.DATA',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='content', full_name='data.DATA.content', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pageInfo', full_name='data.DATA.pageInfo', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_DATA_DATA_CONTENT, _DATA_DATA_PAGEINFO, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=64,
  serialized_end=756,
)

_DATA = _descriptor.Descriptor(
  name='data',
  full_name='data',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='data.data', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_DATA_DATA, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=29,
  serialized_end=756,
)

_DATA_DATA_CONTENT_SITEINFOS.containing_type = _DATA_DATA_CONTENT
_DATA_DATA_CONTENT.fields_by_name['siteInfos'].message_type = _DATA_DATA_CONTENT_SITEINFOS
_DATA_DATA_CONTENT.containing_type = _DATA_DATA
_DATA_DATA_PAGEINFO.containing_type = _DATA_DATA
_DATA_DATA.fields_by_name['content'].message_type = _DATA_DATA_CONTENT
_DATA_DATA.fields_by_name['pageInfo'].message_type = _DATA_DATA_PAGEINFO
_DATA_DATA.containing_type = _DATA
_DATA.fields_by_name['data'].message_type = _DATA_DATA
DESCRIPTOR.message_types_by_name['data'] = _DATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

data = _reflection.GeneratedProtocolMessageType('data', (_message.Message,), {

  'DATA' : _reflection.GeneratedProtocolMessageType('DATA', (_message.Message,), {

    'CONTENT' : _reflection.GeneratedProtocolMessageType('CONTENT', (_message.Message,), {

      'SITEINFOS' : _reflection.GeneratedProtocolMessageType('SITEINFOS', (_message.Message,), {
        'DESCRIPTOR' : _DATA_DATA_CONTENT_SITEINFOS,
        '__module__' : 'response_converter_pb2'
        # @@protoc_insertion_point(class_scope:data.DATA.CONTENT.SITEINFOS)
        })
      ,
      'DESCRIPTOR' : _DATA_DATA_CONTENT,
      '__module__' : 'response_converter_pb2'
      # @@protoc_insertion_point(class_scope:data.DATA.CONTENT)
      })
    ,

    'PAGEINFO' : _reflection.GeneratedProtocolMessageType('PAGEINFO', (_message.Message,), {
      'DESCRIPTOR' : _DATA_DATA_PAGEINFO,
      '__module__' : 'response_converter_pb2'
      # @@protoc_insertion_point(class_scope:data.DATA.PAGEINFO)
      })
    ,
    'DESCRIPTOR' : _DATA_DATA,
    '__module__' : 'response_converter_pb2'
    # @@protoc_insertion_point(class_scope:data.DATA)
    })
  ,
  'DESCRIPTOR' : _DATA,
  '__module__' : 'response_converter_pb2'
  # @@protoc_insertion_point(class_scope:data)
  })
_sym_db.RegisterMessage(data)
_sym_db.RegisterMessage(data.DATA)
_sym_db.RegisterMessage(data.DATA.CONTENT)
_sym_db.RegisterMessage(data.DATA.CONTENT.SITEINFOS)
_sym_db.RegisterMessage(data.DATA.PAGEINFO)


# @@protoc_insertion_point(module_scope)
