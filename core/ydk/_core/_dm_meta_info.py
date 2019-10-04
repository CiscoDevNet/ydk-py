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

import importlib

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

    def __init__(self, name, mtype, ptype, ytype,
                 pmodule_name, clazz_name,
                 prange, pattern, doc,
                 presentation_name, module_name, is_key,
                 members=[], max_elements=None, min_elements=None,
                 default_value=None, is_config=True, is_presence=False,
                 is_mandatory=False, has_when=False, has_must=False):
        self._name = name
        self._mtype = mtype
        self._ptype = ptype
        self._ytype = ytype
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
        if members is None:
            self._members = []
        self._max_elements = max_elements
        self._min_elements = min_elements
        self._default_value = default_value
        self._is_config = is_config
        self._is_presence = is_presence
        self._is_mandatory = is_mandatory
        self.has_when = has_when
        self.has_must = has_must

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
    def ytype(self):
        return self._ytype

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

    @property
    def default_value(self):
        return self._default_value

    @property
    def is_mandatory(self):
        return self._is_mandatory

    @property
    def is_presence(self):
        return self._is_presence

    @property
    def is_config(self):
        return self._is_config

    def union_list(self):
        _list = []
        if self._mtype == REFERENCE_UNION:
            for union_member in self.get_all_union_members():
                if union_member._ptype == 'str':
                    pattern = union_member._pattern
                else:
                    pattern = union_member._range
                _list.append((union_member._ptype, union_member._ytype, pattern))
        return _list

    def get_all_union_members(self):
        union_members = []
        if self._mtype == REFERENCE_UNION:
            for meta in self.members:
                if meta.mtype == REFERENCE_UNION:
                    union_members.extend(meta.get_all_union_members())
                else:
                    union_members.append(meta)
        return union_members

    def ydk_class(self):
        if (self.mtype != REFERENCE_ENUM_CLASS and self.mtype != REFERENCE_CLASS and
            self.mtype != REFERENCE_IDENTITY_CLASS) or \
             len(self._pmodule_name) == 0 or len(self._clazz_name) == 0:
            return None
        m = importlib.import_module(self._pmodule_name)
        cls_list = self._clazz_name.split('.')
        for cls in cls_list:
            m = getattr(m, cls)
        return m

    def enum_dict(self):
        yclass = self.ydk_class()
        enum_meta = yclass._meta_info()
        return enum_meta.enum_dict()


class _MetaInfoClass(object):

    def __init__(
            self,
            name,
            mtype,
            doc,
            is_abstract,
            meta_info_class_members,
            module_name,
            yang_name,
            namespace,
            pmodule_name,
            is_config=True, is_presence=False, is_mandatory=False,
            has_when=False, has_must=False,
            ):
        self.name = name
        self.mtype = mtype
        self.doc = doc
        self.namespace = namespace
        self.meta_info_class_members = meta_info_class_members
        self.module_name = module_name
        self.yang_name = yang_name
        self.is_abstract = is_abstract
        self.pmodule_name = pmodule_name
        self.is_config = is_config
        self.is_presence = is_presence
        self.is_mandatory = is_mandatory
        self.has_when = has_when
        self.has_must = has_must

    def key_members(self):
        return [ member for member in self.meta_info_class_members if member.is_key]

    def member(self, name):
        for m in self.meta_info_class_members:
            if m.name == name:
                return m
        return None

    def ydk_class(self):
        m = importlib.import_module(self.pmodule_name)
        cls_list = self.name.split('.')
        for cls in cls_list:
            m = getattr(m, cls)
        return m


class _MetaInfoEnum(object):
    def __init__(
                 self,
                 name,
                 pmodule_name,
                 clazz_name,
                 doc,
                 literal_map,
                 module_name,
                 namespace):
        self.name = name
        self.pmodule_name = pmodule_name
        self.clazz_name = clazz_name
        self.doc = doc
        self.literal_map = literal_map
        self.module_name = module_name
        self.namespace = namespace

    def ydk_class(self):
        m = importlib.import_module(self.pmodule_name)
        cls_list = self.clazz_name.split('.')
        for cls in cls_list:
            m = getattr(m, cls)
        return m

    def enum_dict(self):
        d = dict()
        yclass = self.ydk_class()
        for k in self.literal_map:
            d[k] = getattr(yclass, k)
        return d


def module_meta(pmodule_name):
    """
        :param pmodule_name - fully qualified name for the module,
                e.g. 'ydk.models.ydktest.ydktest_sanity'
        :return table of top level meta classes (_MetaInfoEnum and _MetaInfoClass)
                for the module
    """
    module_meta_table = {}
    try:
        paths = pmodule_name.rsplit('.', 1)
        meta_module_name = '%s.%s' % (paths[0], '_meta._%s' % paths[1])
        meta_module = importlib.import_module(meta_module_name)
    except ImportError:
        return module_meta_table

    if hasattr(meta_module, '_meta_table'):
        for name, value in meta_module._meta_table.items():
            if isinstance(value, _MetaInfoEnum):
                module_meta_table[name] = value
            else:
                module_meta_table[name] = value['meta_info']
    return module_meta_table


def module_enums(pmodule_name):
    """
        :param pmodule_name - fully qualified name for the module,
                e.g. 'ydk.models.ydktest.ydktest_sanity'
        :return table of _MetaInfoEnum classes for the module
    """
    module_meta_table = module_meta(pmodule_name)
    module_meta_enums = {x: v for x, v in module_meta_table.items() if isinstance(v, _MetaInfoEnum)}
    return module_meta_enums
