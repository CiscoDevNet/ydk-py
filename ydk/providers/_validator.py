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
from ydk.errors import YPYDataValidationError, YPYError
from ydk.types import READ, DELETE
from ydk._core._dm_meta_info import _dm_validate_value
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_ENUM_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST


def validate_entity(entity, optype):
    i_errors = []
    validate_entity_delegate(entity, optype, i_errors)
    if len(i_errors) > 0:
        _i_errors = map((lambda t: ': '.join(t)), i_errors)
        errmsg = '\n'.join(_i_errors)
        raise YPYDataValidationError(errmsg)


def validate_entity_delegate(entity, optype, i_errors):
    """ Validates the given entity.
    
        This function validates the given entity and it's children. If an entity class
        has any errors , the errors will available in the injected member i_errors ,
        which is a list of tuples of form (<name of the class member>, <error messsage>)
        
        Note this method will raise ydk.errors.YPYDataValidationError if validation fails
    """
    for member in entity._meta_info().meta_info_class_members:
        # print member.mtype, member.name
        value = eval('entity.%s' % member.presentation_name)
        if isinstance(value, READ) or isinstance(value, DELETE):
            continue

        if value is None:
            continue

        # bits
        if hasattr(value, '_has_data') and not value._has_data():
            continue

        # if value is not None:
        if  member.mtype in (ATTRIBUTE, REFERENCE_ENUM_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST):
        # if  member.mtype==ATTRIBUTE:
            _dm_validate_value(member, value, entity, optype, i_errors)
