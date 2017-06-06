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
from __future__ import absolute_import
from ydk.errors import YPYServiceError
from ydk.types import YList
from .service import Service
from .meta_service import MetaService
import logging
import importlib


class CRUDService(Service):
    """ CRUD Service class for supporting CRUD operations on entities """
    def __init__(self):
        self.service_logger = logging.getLogger(__name__)

    def create(self, provider, entity):
        """ Create the entity

            Args:
                provider: An instance of ydk.providers.ServiceProvider
                entity: An instance of an entity class defined under the ydk.models package or subpackages

           Returns:
                 None

           Raises:
              `YPYModelError <ydk.errors.html#ydk.errors.YPYModelError>`_ if validation.
              `YPYServiceError <ydk.errors.html#ydk.errors.YPYServiceError>`_ if other error has occurred. Possible errors could be
                  - a server side error
                  - if there isn't enough information in the entity to prepare the message (missing keys for example)


        """
        if None in (provider, entity):
            self.service_logger.error('Passed in a None arg')
            err_msg = "'provider' and 'entity' cannot be None"
            raise YPYServiceError(error_msg=err_msg)
        MetaService.normalize_meta(provider._get_capabilities(), entity)
        self._execute_crud_operation_on_provider(provider, entity, 'CREATE', False)

    def delete(self, provider, entity):
        """ Delete the entity

            Args:
                provider: An instance of ydk.providers.ServiceProvider
                entity: An an entity class defined under the ydk.models package or subpackages



           Returns:
                 None

           Raises:
              `YPYModelError <ydk.errors.html#ydk.errors.YPYModelError>`_ if validation failed.
              `YPYServiceError <ydk.errors.html#ydk.errors.YPYServiceError>`_ if other error has occurred. Possible errors could be a service side error
              or if there isn't enough information in the entity to prepare the message (missing keys for example)

        """
        if None in (provider, entity):
            self.service_logger.error('Passed in a None arg')
            err_msg = "'provider' and 'entity' cannot be None"
            raise YPYServiceError(error_msg=err_msg)
        MetaService.normalize_meta(provider._get_capabilities(), entity)
        self._execute_crud_operation_on_provider(provider, entity, 'DELETE', False)

    def update(self, provider, entity):
        """ Update the entity

            Args:
               - provider: An instance of ydk.providers.ServiceProvider
               - entity: An an entity class defined under the ydk.models package or subpackages

           Note:
               - A given member of an entity can be deleted by setting its attribute to an instance of ydk.types.Delete class.
               - An entity can only be updated if it exists on the server. Otherwise a YPYServiceError will be raised

           Returns:
                 None

           Raises:
              `YPYModelError <ydk.errors.html#ydk.errors.YPYModelError>`_ if validation failed.
              `YPYServiceError <ydk.errors.html#ydk.errors.YPYServiceError>`_ if other error has occurred. Possible errors could be a service side error
              or if there isn't enough information in the entity to prepare the message (missing keys for example)

        """
        # first read the object
        if None in (provider, entity):
            self.service_logger.error('Passed in a None arg')
            err_msg = "'provider' and 'entity' cannot be None"
            raise YPYServiceError(error_msg=err_msg)
        if self._entity_exists(provider, entity):
            # read has succeeded so do an edit-config
            MetaService.normalize_meta(provider._get_capabilities(), entity)
            self._execute_crud_operation_on_provider(provider, entity, 'UPDATE', False)

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
              `YPYModelError <ydk.errors.html#ydk.errors.YPYModelError>`_ if validation failed.
              `YPYServiceError <ydk.errors.html#ydk.errors.YPYServiceError>`_ if other error has occurred. Possible errors could be
                  - a server side error
                  - if there isn't enough information in the entity to prepare the message (missing keys for example)
                  - if the type to be returned cannot be determined.

        """
        if None in (provider, read_filter):
            self.service_logger.error('Passed in a None arg')
            err_msg = "'provider' and 'read_filter' cannot be None"
            raise YPYServiceError(error_msg=err_msg)
        MetaService.normalize_meta(provider._get_capabilities(), read_filter)
        self._perform_read_filter_check(read_filter)
        payload = self._execute_crud_operation_on_provider(provider, read_filter, 'READ', only_config)

        return provider.decode(payload, read_filter)

    def _execute_crud_operation_on_provider(self, provider, entity, operation, only_config):
        if None in (provider, entity, operation, only_config):
            self.service_logger.error('Passed in a None arg')
            err_msg = "'provider', 'entity', 'operation', and 'only_config' cannot be None"
            raise YPYServiceError(error_msg=err_msg)
        try:
            self.service_logger.info('{0} operation initiated'.format(operation))
            return self.execute_payload(
                                        provider,
                                        provider.encode(
                                                        entity,
                                                        operation,
                                                        only_config
                                                        ),
                                        operation
                                        )
        finally:
            self.service_logger.info('{0} operation completed'.format(operation))

    def _perform_read_filter_check(self, read_filter):
        if read_filter is None:
            self.service_logger.error('Passed in a None filter')
            err_msg = "'filter' cannot be None"
            raise YPYServiceError(error_msg=err_msg)

        if not isinstance(read_filter, YList) and not hasattr(read_filter, '_meta_info'):
            err_msg = "Illegal 'filter' type passed in for read"
            self.service_logger.error(err_msg)
            raise YPYServiceError(error_msg=err_msg)

    def _entity_exists(self, provider, entity):
        if None in (provider, entity):
            self.service_logger.error('Passed in a None arg')
            err_msg = "'provider' and 'entity' cannot be None"
            raise YPYServiceError(error_msg=err_msg)

        read_entity = self.read(
            provider,
            self._create_update_entity_filter(entity)
        )

        if not read_entity._has_data():
            err_msg = "'entity' does not exist on remote server - cannot perform update operation"
            self.service_logger.error(err_msg)
            raise YPYServiceError(error_msg=err_msg)

        return True

    def _create_update_entity_filter(self, entity):
        if entity is None:
            self.service_logger.error('Passed in a None entity')
            err_msg = "'entity' cannot be None"
            raise YPYServiceError(error_msg=err_msg)

        module = importlib.import_module(entity._meta_info().pmodule_name)
        update_filter = getattr(module, entity._meta_info().name)()

        # copy over the keys
        for key_member in entity._meta_info().key_members():
            key_val = getattr(entity, key_member.presentation_name)
            update_filter.__dict__[key_member.presentation_name] = key_val

        return update_filter
