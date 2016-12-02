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


ATTRIBUTE = 0
REFERENCE_CLASS = 1
REFERENCE_LIST = 2
REFERENCE_LEAFLIST = 3
REFERENCE_IDENTITY_CLASS = 4
REFERENCE_ENUM_CLASS = 5
REFERENCE_BITS = 6
REFERENCE_UNION = 7
ANYXML_CLASS = 8

class _MetaInfoClassMember(object):

    def __init__(self, name, mtype, ptype,
                 pmodule_name, clazz_name,
                 prange, pattern, doc,
                 presentation_name, module_name, is_key,
                 members=[], max_elements=None, min_elements=None):
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
