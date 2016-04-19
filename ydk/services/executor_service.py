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
from .service import Service
from meta_service import MetaService
import logging


class ExecutorService(Service):
    """ Executor Service class for executing RPCs containing entities """
    def __init__(self):
        self.executor_logger = logging.getLogger('ydk.services.ExecutorService')

    def execute_rpc(self, provider, rpc):
        """ Execute the RPC
        
            Args:
                provider: An instance of ydk.providers.ServiceProvider
                rpc: An instance of an RPC class defined under the ydk.models package or subpackages

           Returns:
                 None
        
           Raises:
              `YPYDataValidationError <ydk.errors.html#ydk.errors.YPYDataValidationError>`_ if validation.
              `YPYError <ydk.errors.html#ydk.errors.YPYError>`_ if other error has occurred. Possible errors could be 
                  - a server side error
                  - if there isn't enough information in the entity to prepare the message (missing keys for example)
        """
        try:
            rpc = MetaService.normalize_meta(provider.get_capabilities(), rpc)
            return self.execute_payload(
                                        provider,
                                        '',
                                        provider.sp_instance.encode_rpc(rpc)
                                        )
        finally:
            self.executor_logger.info('Netconf operation completed')

