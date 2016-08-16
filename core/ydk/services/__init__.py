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

""" services
 
   The Services module. 
   
   Supported Services Include
   
     - CRUDService: Provide Create/Read/Update/Delete API's
     - ExecutorService: Provide API to execute RPC 
     
"""
from .service import Service
from .crud_service import CRUDService
from .executor_service import ExecutorService
from .netconf_service import Datastore
from .netconf_service import NetconfService
from .codec_service import CodecService
import logging


logging.getLogger('ydk').addHandler(logging.NullHandler())
