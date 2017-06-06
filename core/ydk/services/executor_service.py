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
""" executor_service.py

   The Executor Service class.

"""
from __future__ import absolute_import
from .service import Service
from ydk.errors import YPYServiceError
from .meta_service import MetaService
import logging


class ExecutorService(Service):
    """ Executor Service class for executing RPCs containing entities """
    def __init__(self):
        self.service_logger = logging.getLogger(__name__)

    def execute_rpc(self, provider, rpc):
        """ Execute the RPC

            Args:
                provider: An instance of ydk.providers.ServiceProvider
                rpc: An instance of an RPC class defined under the ydk.models package or subpackages

           Returns:
                 None

           Raises:
              `YPYModelError <ydk.errors.html#ydk.errors.YPYModelError>`_ if validation.
              `YPYServiceError <ydk.errors.html#ydk.errors.YPYServiceError>`_ if other error has occurred. Possible errors could be
                  - a server side error
                  - if there isn't enough information in the entity to prepare the message (missing keys for example)
        """
        if None in (provider, rpc):
            self.service_logger.error('Passed in a None arg')
            err_msg = "'provider' and 'rpc' cannot be None"
            raise YPYServiceError(error_msg=err_msg)
        try:
            rpc = MetaService.normalize_meta(provider._get_capabilities(), rpc)
            self.service_logger.info('Executor operation initiated')
            result = provider.execute(
                                    provider.sp_instance.encode_rpc(rpc),
                                    ''
                                    )
            return provider.decode(result, rpc)
        finally:
            self.service_logger.info('Executor operation completed')
