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
""" _value_encoder.py

   Value encoder.

"""
from __future__ import unicode_literals
from enum import Enum
import logging
import importlib

from ydk._core._dm_meta_info import REFERENCE_BITS, \
    REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_LEAFLIST
from ydk.types import Empty, Decimal64, YListItem

from ._importer import _yang_ns
from functools import reduce

import sys
if sys.version_info > (3,):
    long = int


class ValueEncoder(object):
    def encode(self, member, NSMAP, value):
        text = ''
        if member.mtype == REFERENCE_IDENTITY_CLASS or member.ptype.endswith('Identity'):
            module = importlib.import_module(member.pmodule_name)
            clazz = reduce(getattr, member.clazz_name.split('.'), module)

            if issubclass(type(value), clazz):
                identity_inst = value
                if _yang_ns._namespaces[member.module_name] == _yang_ns._namespaces[identity_inst._meta_info().module_name]:
                    # no need for prefix in this case
                    text = identity_inst._meta_info().yang_name
                else:
                    NSMAP['idx'] = _yang_ns._namespaces[identity_inst._meta_info().module_name]
                    text = 'idx:%s' % identity_inst._meta_info().yang_name
        elif member.mtype == REFERENCE_BITS or member.ptype.endswith('Bits'):
            module = importlib.import_module(member.pmodule_name)
            clazz = reduce(getattr, member.clazz_name.split('.'), module)
            if isinstance(value, clazz):
                bits_value = value
                value = " ".join([k for k in bits_value._dictionary if bits_value._dictionary[k] == True])
                if (len(value) > 1):
                    text = value
        elif member.mtype == REFERENCE_ENUM_CLASS or member.ptype.endswith('Enum'):
            enum_value = value
            if isinstance(enum_value, Enum):
                enum_value = value.name
            module = importlib.import_module(member.pmodule_name)
            enum_clazz = reduce(getattr, member.clazz_name.split('.'), module)
            literal_map = enum_clazz._meta_info().literal_map
            for yang_enum_name in literal_map:
                literal = literal_map[yang_enum_name]
                if enum_value == getattr(enum_clazz, literal) \
                    or enum_value == literal:
                    text = yang_enum_name
                    break
        elif member.ptype == 'bool' and isinstance(value, bool):
            if value is True:
                text = 'true'
            else:
                text = 'false'
        elif member.ptype == 'Empty' and isinstance(value, Empty):
            pass
        elif member.ptype == 'Decimal64' and isinstance(value, Decimal64):
            text = value.s
        elif member.ptype == 'str' and isinstance(value, str):
            text = str(value)
        elif member.ptype == 'int' and isinstance(value, (int, long)):
            text = str(value)
        else:
            ydk_logger = logging.getLogger(__name__)
            ydk_logger.info('Could not encode leaf {0}, type: {1}, {2} value: {3}'.format(member.name, member.mtype, member.ptype, value))
        return text
