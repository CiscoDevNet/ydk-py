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
""" services.py 
 
   The Services module. 
   
   Supported Services Include
   
     CRUDService: Provide Create/Read/Update/Delete API's 
     
"""
from ydk.errors import YPYError
from ydk.types import YList
from .service import Service
import logging


class CRUDService(Service):
    """ CRUD Service class for supporting CRUD operations on entities """
    def __init__(self):
        self.crud_logger = logging.getLogger('ydk.services.CRUDService')

    def create(self, provider, entity):
        """ Create the entity 
        
            Args:
                provider: An instance of ydk.providers.ServiceProvider
                entity: An instance of an entity class defined under the ydk.models package or subpackages

           Returns:
                 None
        
           Raises:
              `YPYDataValidationError <ydk.errors.html#ydk.errors.YPYDataValidationError>`_ if validation.
              `YPYError <ydk.errors.html#ydk.errors.YPYError>`_ if other error has occurred. Possible errors could be 
                  - a server side error
                  - if there isn't enough information in the entity to prepare the message (missing keys for example)
                  
                  
        """
        self.execute_crud_operation_on_provider(provider, entity, 'CREATE', False)

    def delete(self, provider, entity):
        """ Delete the entity 
        
            Args:
                provider: An instance of ydk.providers.ServiceProvider
                entity: An an entity class defined under the ydk.models package or subpackages
                
           

           Returns:
                 None
        
           Raises:
              `YPYDataValidationError <ydk.errors.html#ydk.errors.YPYDataValidationError>`_ if validation failed. 
              `YPYError <ydk.errors.html#ydk.errors.YPYError>`_ if other error has occurred. Possible errors could be a service side error
              or if there isn't enough information in the entity to prepare the message (missing keys for example)
                  
        """
        self.execute_crud_operation_on_provider(provider, entity, 'DELETE', False)

    def update(self, provider, entity):
        """ Update the entity 

            Args:
               - provider: An instance of ydk.providers.ServiceProvider
               - entity: An an entity class defined under the ydk.models package or subpackages

           Note:
               - A given member of an entity can be deleted by setting its attribute to an instance of ydk.types.Delete class.
               - An entity can only be updated if it exists on the server. Otherwise a YPYError will be raised

           Returns:
                 None

           Raises:
              `YPYDataValidationError <ydk.errors.html#ydk.errors.YPYDataValidationError>`_ if validation failed.
              `YPYError <ydk.errors.html#ydk.errors.YPYError>`_ if other error has occurred. Possible errors could be a service side error
              or if there isn't enough information in the entity to prepare the message (missing keys for example)
                  
        """
        # first read the object
        if self.entity_exists(provider, entity):
            # read has succeeded so do an edit-config
            self.execute_crud_operation_on_provider(provider, entity, 'UPDATE', False)

    def read(self, provider, read_filter, only_config=False):
        """ Read the entity or entities
            
            Args:
                - provider: An instance of ydk.providers.ServiceProvider
                - read_filter: A read_filter is an instance of an entity class.
                
                         An entity class is a class defined under the ydk.models package that is not an Enum , Identity of subclass of FixedBitsDict) .
                         Attributes of this entity class may contain values that act as match expressions or can be explicitly marked as to be read by assigning an instance of ydk.types.READ class to them.
                
                - only_config: Flag that indicates that only data that represents configuration data is to be fetched.
                        
                            Default is set to False i.e. both oper and config data will be fetched.
                
           Returns:
                 The entity or entities as identified by the read_filter.
        
           Raises:
              `YPYDataValidationError <ydk.errors.html#ydk.errors.YPYDataValidationError>`_ if validation failed.
              `YPYError <ydk.errors.html#ydk.errors.YPYError>`_ if other error has occurred. Possible errors could be
                  - a server side error
                  - if there isn't enough information in the entity to prepare the message (missing keys for example)
                  - if the type to be returned cannot be determined.
                  
        """
        self.perform_read_filter_check(read_filter)
        payload = self.execute_crud_operation_on_provider(provider, read_filter, 'READ', only_config)
        # print payload
        return self.create_read_return_value(payload, read_filter)

    def execute_crud_operation_on_provider(self, provider, entity, operation, only_config):


        try:
            return self.execute_payload(
                                        provider,
                                        provider.sp_instance.encode(
                                                                    entity,
                                                                    operation,
                                                                    only_config
                                                                    )
                                        )
        finally:
            self.crud_logger.info('CRUD operation completed')

    def perform_read_filter_check(self, read_filter):
        if read_filter is None:
            self.crudLogger.error('Passed in a none filter')
            raise YPYError('Filter cannot be None')

        if not isinstance(read_filter, YList) and not hasattr(read_filter, '_meta_info'):
            self.crudLogger.error('Illegal filter type passed in for read')
            raise YPYError('Illegal filter')

    def create_read_return_value(self, payload, read_filter):

        from ydk._core._dmtree import DmTree

        # In order to figure out which fields are the
        # ones we are interested find the field list
        entity = self.create_top_level_entity_from_read_filter(read_filter)
        DmTree._bind_to_object(payload, entity)
        # drill down to figure out the field access expression
        # that matches the entity or entities to be returned
        # not the argument passed in as a filter might have
        # incomplete key paths, in which case what is returned
        # will be the entity whose common path can be determined

        suffix_field_names = []
        current_entity = read_filter
        if isinstance(current_entity, YList):
            suffix_field_names.append(current_entity.name)
            current_entity = current_entity.parent

        current = entity
        yang_nodes = []
        yang_nodes.extend([ s for s in current_entity._common_path.split('/') if ':' in s])
        yang_nodes = yang_nodes[1:]

        for seg in yang_nodes:
            if '[' in seg:
                seg = seg.split('[')[0]
            _, yang_node_name = seg.split(':')

            found = False
            for member in current._meta_info().meta_info_class_members:
                if member.name == yang_node_name:
                    found = True
                    current = eval('current.%s' % member.presentation_name)
                    if current is None:
                        return None
                    if isinstance(current, YList):
                        if len(current) == 0:
                            return None
                        if len(current) > 2:
                            return current
                        if len(current) == 1:
                            current = current[0]

                    break

            if not found:
                self.crud_logger.error('Error determing what needs to be returned')
                raise YPYError('Error determining what needs to be returned')

        for field in suffix_field_names:
            current = eval('current.%s' % field)

        return current

    def create_top_level_entity_from_read_filter(self, read_filter):
        non_list_filter = read_filter

        while isinstance(non_list_filter, YList):
            non_list_filter = non_list_filter.parent

        if non_list_filter is None:
            self.crud_logger.error('Cannot determine hierarchy for entity. Please set the parent reference')
            raise YPYError('Cannot determine hierarchy for entity. Please set the parent reference')

        top_entity_meta_info = non_list_filter._meta_info()

        while hasattr(top_entity_meta_info, 'parent') and top_entity_meta_info.parent is not None:
            # need to find the member that has
            top_entity_meta_info = top_entity_meta_info.parent

        exec_import = 'from ' + top_entity_meta_info.pmodule_name + ' import ' + top_entity_meta_info.name.split('.')[0]
        exec exec_import
        entity = eval(top_entity_meta_info.name + '()')
        return entity

    def entity_exists(self, provider, entity):
        read_entity = self.read(provider,
                                self.create_update_entity_filter(entity))

        if not read_entity._has_data():
            self.crud_logger.error('Entity does not exist on remote server. Cannot perform update operations.')
            raise YPYError('Entity does not exist on remote server. Cannot perform update operation.')

        return True

    def create_update_entity_filter(self, entity):
        stmt = 'from ' + entity._meta_info().pmodule_name + ' import ' + entity._meta_info().name.split('.')[0]
        exec(stmt)

        update_filter = eval('%s()' % entity._meta_info().name)
        # copy over the keys
        for key_member in entity._meta_info().key_members():
            key_val = eval('entity.%s' % key_member.presentation_name)
            update_filter.__dict__[key_member.presentation_name] = key_val

        return update_filter
