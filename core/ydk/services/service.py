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
    def operate_on_object_or_dictionary(self, entity, function, args):
        result=None
        if isinstance(entity, dict):
            result = {}
            for module, child in entity.items():
                result[module] = function(child, *args)
        else:
            result = function(entity, *args)
        return result

    def execute_payload(self, provider, payload, operation):
        reply = provider.execute(payload, operation)
        return reply
