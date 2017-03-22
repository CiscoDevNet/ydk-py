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
""" providers.py

   Service Providers module. Current implementation supports the NetconfServiceProvider which
   uses ncclient (a Netconf client library) to provide CRUD services.

"""
from ._value_encoder import ValueEncoder
from ydk.errors import YPYModelError, YPYErrorCode
from ydk.types import READ, DELETE, Decimal64, Empty, YList, YLeafList, YListItem
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_ENUM_CLASS, REFERENCE_LIST, \
            REFERENCE_LEAFLIST, REFERENCE_IDENTITY_CLASS, REFERENCE_BITS, REFERENCE_UNION

from enum import Enum
import logging
import importlib
from functools import reduce

import sys
if sys.version_info > (3,):
    long = int


def validate_entity(entity, optype):
    errors = []
    validate_entity_delegate(entity, optype, errors)
    if len(errors) > 0:
        _errors = list(map((lambda t: '%s: (%s, %s)' % t), errors))
        _errors.insert(0, '')
        errmsg = '\n  '.join(_errors)
        raise YPYModelError(errmsg)


def validate_entity_delegate(entity, optype, errors):
    """ Validates the given entity.

        This function validates the given entity and it's children. If an entity class
        has any errors , the errors will available in the injected member errors ,
        which is a list of tuples of form (<name of the class member>, <error messsage>)

        Note this method will raise ydk.errors.YPYModelError if validation fails
    """
    for member in entity.i_meta.meta_info_class_members:
        value = getattr(entity, member.presentation_name)
        if isinstance(value, READ) or isinstance(value, DELETE):
            continue

        if value is None:
            continue

        # bits
        if hasattr(value, '_has_data') and not value._has_data():
            continue

        if  member.mtype in (ATTRIBUTE, REFERENCE_ENUM_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST):
            _dm_validate_value(member, value, entity, optype, errors)

def _dm_validate_value(meta, value, parent, optype, errors):
    if value is None:
        return value
    elif isinstance(value, YListItem):
        value = value.item

    if meta._ptype == 'Empty':
        exec('from ydk.types import Empty')
    elif meta._ptype == 'Decimal64':
        exec('from ydk.types import Decimal64')
    elif 'Enum' in meta._ptype:
        exec_import = 'from %s import %s' \
            % (meta.pmodule_name, meta.clazz_name.split('.')[0])
        exec(exec_import)
    elif meta._ptype == 'str' and meta.mtype != REFERENCE_LEAFLIST and isinstance(value, bytes):
        new_value = str(value.decode())
        setattr(parent, meta.presentation_name, new_value)
        value = new_value

    isNumber = False
    path = '%s.%s' % (parent.i_meta.name, meta.presentation_name)

    if meta.mtype in (REFERENCE_IDENTITY_CLASS,
        REFERENCE_BITS, REFERENCE_ENUM_CLASS, REFERENCE_LIST):
        module = importlib.import_module(meta.pmodule_name)

    if isinstance(value, YList) and meta.mtype == REFERENCE_LIST:
        if optype == 'READ' or meta.max_elements is None:
            max_elements = float('inf')
        else:
            max_elements = meta.max_elements

        if len(value) <= max_elements:
            for v in value:
                _dm_validate_value(meta, v, parent, optype, errors)
        else:
            errmsg = "Invalid list length, length = %d" % len(value)
            _handle_error(meta, parent, errors, errmsg)
        return value

    elif meta.mtype == REFERENCE_ENUM_CLASS:
        enum_value = value
        if isinstance(enum_value, Enum):
            enum_value = enum_value.name
        module = importlib.import_module(meta.pmodule_name)
        enum_clazz = reduce(getattr, meta.clazz_name.split('.'), module)
        literal_map = enum_clazz._meta_info().literal_map
        enum_found = False
        for yang_enum_name in literal_map:
            literal = literal_map[yang_enum_name]
            if enum_value == getattr(enum_clazz, literal) \
                or enum_value == literal:
                enum_found = True
                break
        if not enum_found:
            errmsg = "Invalid type: '%s'. Expected type: Enum" % (type(value).__name__)
            _handle_error(meta, parent, errors, errmsg)
        return value

    elif meta.mtype == REFERENCE_LIST:
        clazz = reduce(getattr, meta.clazz_name.split('.'), module)
        if not isinstance(value, clazz):
            errmsg = "Invalid list element type, type = %s" % value
            _handle_error(meta, parent, errors, errmsg)
        return value

    elif value.__class__.__name__ == meta._ptype:
        if isinstance(value, (int, long)):
            return _validate_number(meta, value, parent, errors)
        elif isinstance(value, str):
            if len(meta._range) > 0:
                valid = False
                for prange in meta._range:
                    if type(prange) == tuple:
                        pmin, pmax = prange
                        if len(value) >= pmin and len(value) <= pmax:
                            valid = True
                            break
                    else:
                        if len(value) == prange:
                            valid = True
                            break
                if not valid:
                    errmsg = "Invalid data or data range, value = %d" % value
                    _handle_error(meta, parent, errors, errmsg)

            '''TODO
                if len(meta._pattern) > 0:
                pat_valid = False
                for p in meta._pattern:
                    pat = re.compile(p)
                    if pat.match(value) is not None:
                        pat_valid = True
                        break
                if not pat_valid:
                    errmsg = "Invalid data or data range, value = %s" % value
                    _handle_error(meta, parent, errors, errmsg)'''

            return value
        else:
            # enum, etc.
            return value

    elif isinstance(value, (int, long)) and meta._ptype == 'int':
        return _validate_number(meta, value, parent, errors)

    elif isinstance(value, YLeafList) and meta.mtype == REFERENCE_LEAFLIST:
        # A leaf list.
        min_elements = meta.min_elements if meta.min_elements else 0
        max_elements = meta.max_elements if meta.max_elements else float('inf')

        value_len = len([v for v in value if v is not None])

        if min_elements <= value_len <= max_elements and value_len == len(value):
            for i in range(len(value)):
                v = value [i]
                if meta.ptype == 'str' and isinstance(value[i], bytes):
                    v = str(value[i].decode())
                    value[i] = v
                _dm_validate_value(meta, v, parent, optype, errors)
            setattr(parent, meta.presentation_name, value)
        else:
            errmsg = "Invalid leaflist length, length = %d" % value_len
            _handle_error(meta, parent, errors, errmsg)
        return value

    elif meta.mtype == REFERENCE_UNION:
        encoded = False
        for contained_member in meta.members:
            # determine what kind of encoding is needed here
            if '' == ValueEncoder().encode(contained_member, {}, value):
                encoded = True
                break
        if not encoded:
            _handle_error(meta, parent, errors, error_code=YPYErrorCode.INVALID_UNION_VALUE)

    else:
        if '' == ValueEncoder().encode(meta, {}, value):
            errmsg = "Invalid type: '%s'. Expected type: '%s'" % (type(value).__name__, meta._ptype)
            _handle_error(meta, parent, errors, errmsg)

def _validate_number(meta, value, parent, errors):
    if len(meta._range) > 0:
        valid = False
        for prange in meta._range:
            if type(prange) == tuple:
                pmin, pmax = prange
                if meta.ptype == 'int':
                    pmin, pmax = int(pmin), int(pmax)
                if value >= pmin and value <= pmax:
                    valid = True
                    break
            else:
                if value == prange:
                    valid = True
                    break
        if not valid:
            errcode = YPYErrorCode.INVALID_VALUE
            _range = None
            size = len(meta._range)
            if size > 1:
                _range = str(meta._range)
            else:
                lower, upper = meta._range[0]
                _range = '(%s, %s)' % (lower, upper)
            errmsg = '{}: {} not in range {}'.format(errcode.value, value, _range)
            _handle_error(meta, parent, errors, errmsg, errcode)
    return value

def _handle_error(meta, parent, errors, errmsg=None, errcode=None):
    services_logger = logging.getLogger(__name__)
    path = '%s.%s' % (parent.i_meta.name, meta.presentation_name)

    if errcode is None:
        errcode = YPYErrorCode.INVALID_TYPE
    if errmsg is None:
        errmsg = errcode.value
    entry = (path, errcode.name, errmsg)

    services_logger.error('Validation error for property %s . Error message (%s, %s).' % entry)
    errors.append(entry)
