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
from ydk_gnmi_.services import gNMIService as _gNMIService
from ydk_gnmi_.services import gNMISubscription
from ydk.errors import YServiceError as _YServiceError
from ydk.errors.error_handler import handle_runtime_error as _handle_error

from ydk.types import EntityCollection, Config
from ydk.entity_utils import _get_top_level_entity, _get_child_entity_from_top

class gNMIService(_gNMIService):
    """ Python wrapper for gNMIService
    """
    def __init__(self):
        self._gs = _gNMIService()

    def capabilities(self, provider):
        if provider is None:
            raise _YServiceError("Service Provider cannot be None")
        return self._gs.capabilities(provider)

    def get(self, provider, read_filter, operation='CONFIG'):
        if provider is None:
            raise _YServiceError("Service Provider cannot be None")

        if read_filter is None:
            raise _YServiceError("Get filter cannot be None")

        filters = read_filter
        if isinstance(read_filter, EntityCollection):
            filters = read_filter.entities()

        top_filters = _get_top_level_entity(filters, provider.get_session().get_root_schema())
        with _handle_error():
            top_result = self._gs.get(provider, top_filters, operation)
        result = _get_child_entity_from_top(top_result, filters)

        if isinstance(read_filter, EntityCollection):
            result = Config(result)
        return result

    def set(self, provider, entity):
        if provider is None:
            raise _YServiceError("Provider cannot be None")

        if entity is None:
            raise _YServiceError("Set entiy cannot be None")

        entities = entity
        if isinstance(entity, EntityCollection):
            entities = entity.entities()

        with _handle_error():
            result = self._gs.set(provider, entities)
        return result

    def subscribe(self, provider, subscription, qos=0, mode='ONCE', encoding='PROTO', gnmi_subscribe_callback=None):
        if provider is None:
            raise _YServiceError("Provider cannot be None")

#         if (subscription is None or (not isinstance(subscription, gNMISubscription)) or
#              (not (isinstance(subscription, list) and isinstance(subscription[0], gNMISubscription)))):
#             raise _YServiceError("Subscription is not properly defined")

        self._gs.subscribe(provider, subscription, qos, mode, encoding, gnmi_subscribe_callback)
        
