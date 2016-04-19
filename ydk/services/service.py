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

""" service.py 
 
   The base Service class.
     
"""

class Service(object):
    """ Base service class which can be extended for different ways of communicating to remote server """

    def execute_payload(self, provider, operation, payload):
        # print payload
        reply = provider.sp_instance.execute_operation(
                                            provider.sp_instance._nc_manager,
                                            operation,
                                            payload)

        # print reply
        return reply
