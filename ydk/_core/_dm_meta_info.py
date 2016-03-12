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

import re
from ydk.types import Decimal64, Empty, YList
import logging


ATTRIBUTE = 0
REFERENCE_CLASS = 1
REFERENCE_LIST = 2
REFERENCE_LEAFLIST = 3
REFERENCE_IDENTITY_CLASS = 4
REFERENCE_ENUM_CLASS = 5
REFERENCE_BITS = 6
REFERENCE_UNION = 7


class _MetaInfoClassMember(object):

    def __init__(self, name, mtype, ptype,
                 pmodule_name, clazz_name,
                 prange, pattern, doc,
                 presentation_name, module_name, is_key,
                 members=None, max_elements=None, min_elements=None):
        self._name = name
        self._mtype = mtype
        self._ptype = ptype
        self._pmodule_name = pmodule_name
        self._clazz_name = clazz_name
        self._range = prange
        self._pattern = pattern
        self._doc = doc
        if presentation_name is None:
            presentation_name = name
        self._presentation_name = presentation_name
        self._module_name = module_name
        self._is_key = is_key
        self._members = members
        self._max_elements = max_elements
        self._min_elements = min_elements
    
    @property
    def members(self):
        return self._members
    
    @property
    def clazz_name(self):
        return self._clazz_name
    
    @property
    def ptype(self):
        return self._ptype

    @property
    def pmodule_name(self):
        return self._pmodule_name
    
    @property
    def is_key(self):
        return self._is_key
    
    @property
    def name(self):
        return self._name

    @property
    def mtype(self):
        return self._mtype

    @property
    def presentation_name(self):
        return self._presentation_name

    @property
    def module_name(self):
        return self._module_name

    @property
    def max_elements(self):
        return self._max_elements

    @property
    def min_elements(self):
        return self._min_elements


class _MetaInfoClass(object):

    def __init__(
            self,
            name,
            is_abstract,
            meta_info_class_members,
            module_name,
            yang_name,
            namespace,
            pmodule_name):
        self.name = name
        self.namespace = namespace
        self.meta_info_class_members = meta_info_class_members
        self.module_name = module_name
        self.yang_name = yang_name
        self.is_abstract = is_abstract
        self.pmodule_name = pmodule_name
        
    def key_members(self):
        return [ member for member in self.meta_info_class_members if member.is_key]


class _MetaInfoEnum(object):
    def __init__(
                 self,
                 name,
                 pmodule_name,
                 literal_map,
                 module_name,
                 namespace):
        self.name = name
        self.pmodule_name = pmodule_name
        self.literal_map = literal_map
        self.module_name = module_name
        self.namespace = namespace
       
def _handle_error(meta, parent, errmsg, i_errors):
    services_logger = logging.getLogger('ydk.services')
    entry = (meta.presentation_name, errmsg)
    services_logger.error('Validation error for property %s . Error message %s.' % entry) 
    i_errors.append(entry)

    if not hasattr(parent, 'i_errors'):
        parent.i_errors = []
    parent.i_errors.append(entry)

def _encode_value(member, value):
    encoded = True
    if member.mtype == REFERENCE_IDENTITY_CLASS:
        exec 'from %s import %s'%(member.pmodule_name, member.clazz_name.split('.')[0])
        
        if not issubclass(type(value), eval(member.clazz_name)):
            encoded = False

    elif member.mtype == REFERENCE_BITS:
        exec 'from %s import %s'%(member.pmodule_name, member.clazz_name.split('.')[0])
        
        if isinstance(value, eval(member.clazz_name)):
            bits_value = value
            value = " ".join([k for k in bits_value._dictionary if bits_value._dictionary[k] == True])
            if not (len(value)  > 1):
                encoded = False
        else:
            encoded = False     
    elif member.mtype == REFERENCE_ENUM_CLASS:
        enum_value = value
        exec_import = 'from %s import %s' \
            % (member.pmodule_name, member.clazz_name.split('.')[0])
        exec exec_import
        enum_clazz = eval(member.clazz_name)
        literal_map = enum_clazz._meta_info().literal_map
        enum_found = False
        for yang_enum_name in literal_map:
            literal = literal_map[yang_enum_name]
            if enum_value == getattr(enum_clazz, literal) \
                or enum_value == literal:
                enum_found = True
                break
        if not enum_found:
            encoded = False
    elif member.ptype == 'bool' and isinstance(value, bool):
        pass
    elif member.ptype == 'Empty' and isinstance(value, Empty):
        pass
    elif member.ptype == 'Decimal64' and isinstance(value, Decimal64):
        pass
    elif member.ptype == 'str' and isinstance(value, str):
        pass
    elif member.ptype == 'int' and isinstance(value, int):
        pass
    elif member.ptype == 'long' and isinstance(value, long):
        pass
    else:
        encoded = False
    
    return encoded

def _dm_validate_value(meta, value, parent, optype, i_errors):
    #return value#pass
    if value is None:
        return value
    
    if meta._ptype == 'Empty':
        exec 'from ydk.types import Empty'
    elif meta._ptype == 'Decimal64':
        exec 'from ydk.types import Decimal64'

    if meta.mtype in (REFERENCE_IDENTITY_CLASS, 
        REFERENCE_BITS, REFERENCE_ENUM_CLASS, REFERENCE_LIST):
        exec_import = 'from %s import %s' \
            % (meta.pmodule_name, meta.clazz_name.split('.')[0])
        exec exec_import


    if isinstance(value, YList) and meta.mtype == REFERENCE_LIST:
        if optype == 'READ' or meta.max_elements is None:
            max_elements = float('inf')
        else:
            max_elements = meta.max_elements

        if len(value) <= max_elements:
            for v in value:
                _dm_validate_value(meta, v, parent, optype, i_errors)
        else:
            errmsg = "Invalid list length, length = %d" % len(value)
            _handle_error(meta, parent, errmsg, i_errors)
        return value

    elif meta.mtype == REFERENCE_LIST:
        if not isinstance(value, eval(meta.clazz_name)):
            errmsg = "Invalid list element type, type = %s" % value
            _handle_error(meta, parent, errmsg, i_errors)
        return value            

    elif isinstance(value, eval(meta._ptype)):
        if isinstance(value, int):
            if len(meta._range) > 0:
                valid = False
                for prange in meta._range:
                    if type(prange) == tuple:
                        pmin, pmax = prange
                        if value >= pmin and value <= pmax:
                            valid = True
                            break
                    else:
                        if value == prange:
                            valid = True
                            break
                if not valid:
                    errmsg = "Invalid data or data range, value = %d" % value
                    _handle_error(meta, parent, errmsg, i_errors)

            return value
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
                    _handle_error(meta, parent, errmsg, i_errors)

            if len(meta._pattern) > 0:
                pat_valid = False
                for p in meta._pattern:
                    pat = re.compile(p)
                    if pat.match(value) is not None:
                        pat_valid = True
                        break
                if not pat_valid:
                    errmsg = "Invalid data or data range, value = %d" % value
                    _handle_error(meta, parent, errmsg, i_errors)

            return value
        else:
            # enum, etc.
            return value
    #check for type(Empty.SET), type(Empty.UNSET). Needs to be refined
    elif meta._ptype is 'int': 
        return value

    elif type(value) == list and meta.mtype == REFERENCE_LEAFLIST:
        # A leaf list.
        min_elements = meta.min_elements if meta.min_elements else 0
        max_elements = meta.max_elements if meta.max_elements else float('inf')

        value_len = len([v for v in value if v is not None])

        if min_elements <= value_len <= max_elements and value_len == len(value):
            for v in value:
                _dm_validate_value(meta, v, parent, optype, i_errors)
        else:
            errmsg = "Invalid leaflist length, length = %d" % value_len
            _handle_error(meta, parent, errmsg, i_errors)
        return value

    elif meta.mtype == REFERENCE_UNION:
        encoded = False
        for contained_member in meta.members:
            #determine what kind of encoding is needed here
            if _encode_value(contained_member, value):
                encoded = True
                break
        if not encoded:
            errmsg = "Cannot translate union value"
            _handle_error(meta, parent, errmsg, i_errors)

    else:
        if not _encode_value(meta, value):
            errmsg = "Cannot encode value"
            _handle_error(meta, parent, errmsg, i_errors)
