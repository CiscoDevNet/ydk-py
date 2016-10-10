#  ----------------------------------------------------------------
# Copyright 2016 Cisco Systems
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ------------------------------------------------------------------
#
# Copied from the bigmuddy collector
#
from google.protobuf.message import Message
from google.protobuf.descriptor import FieldDescriptor


DECODE_FN_MAP = {
    FieldDescriptor.TYPE_DOUBLE: float,
    FieldDescriptor.TYPE_FLOAT: float,
    FieldDescriptor.TYPE_INT32: int,
    FieldDescriptor.TYPE_INT64: int,
    FieldDescriptor.TYPE_UINT32: int,
    FieldDescriptor.TYPE_UINT64: int,
    FieldDescriptor.TYPE_SINT32: int,
    FieldDescriptor.TYPE_SINT64: int,
    FieldDescriptor.TYPE_FIXED32: int,
    FieldDescriptor.TYPE_FIXED64: int,
    FieldDescriptor.TYPE_SFIXED32: int,
    FieldDescriptor.TYPE_SFIXED64: int,
    FieldDescriptor.TYPE_BOOL: bool,
    FieldDescriptor.TYPE_STRING: str,
    FieldDescriptor.TYPE_BYTES: lambda b: bytes_to_string(b),
    FieldDescriptor.TYPE_ENUM: int,
}


def bytes_to_string (bytes):
    """
    Convert a byte array into a string aa:bb:cc
    """
    return ":".join(["{:02x}".format(int(ord(c))) for c in bytes])


def field_type_to_fn(msg, field):
    if field.type == FieldDescriptor.TYPE_MESSAGE:
        # For embedded messages recursively call this function. If it is
        # a repeated field return a list
        result = lambda msg: proto_to_dict(msg)
    elif field.type in DECODE_FN_MAP:
        result = DECODE_FN_MAP[field.type]
    else:
        raise TypeError("Field %s.%s has unrecognised type id %d" % (
                         msg.__class__.__name__, field.name, field.type))
    return result


def proto_to_dict(msg):
    result_dict = {}
    extensions = {}
    for field, value in msg.ListFields():
        conversion_fn = field_type_to_fn(msg, field)
        
        # Skip extensions
        if not field.is_extension:
            # Repeated fields result in an array, otherwise just call the 
            # conversion function to store the value
            if field.label == FieldDescriptor.LABEL_REPEATED:
                result_dict[field.name] = [conversion_fn(v) for v in value]
            else:
                result_dict[field.name] = conversion_fn(value)
    return result_dict


