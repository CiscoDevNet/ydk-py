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
from ydk_.services import CRUDService as _CrudService
from ydk.errors.error_handler import handle_runtime_error as _handle_error
from ydk.errors.error_handler import check_argument as _check_argument
from ydk.errors import YServiceError
from ydk.types import EntityCollection, Config
from ydk.entity_utils import _read_entities, _get_top_level_entity, _get_child_entity_from_top
from ydk.entity_utils import _set_nontop_entity_filter
from ydk.filters import YFilter


class CRUDService(_CrudService):
    """
    Python wrapper for CrudService

    Provides API to Create, Read, Update, and Delete configuration on device.

    Args:
        provider (ydk.ServiceProvider): NetconfServiceProvider.
        entity_holder (ydk.types.Entity or a list(ydk.types.Entity)): Encoding target(s).
        pretty (bool, optional): Pretty formatting. Default value is True.

    Returns:
        Functions read and read-config return, ydk.types.Entity or a list(ydk.types.Entity), depending on provided input
        Other functions return boolean value: true - for success; false - failure.

    Raises:
        Instance of YError in case of operation failure fails.
    """
    def __init__(self):
        self._crud = _CrudService()

    @_check_argument
    def create(self, provider, entity):
        return _crud_update(provider, entity, self._crud.create)

    @_check_argument
    def delete(self, provider, entity):
        return _crud_update(provider, entity, self._crud.delete)

    @_check_argument
    def update(self, provider, entity):
        return _crud_update(provider, entity, self._crud.update)

    def read(self, provider, read_filter=None):
        return _crud_read(provider, read_filter, False, self._crud.read)

    def read_config(self, provider, read_filter=None):
        return _crud_read(provider, read_filter, True, self._crud.read_config)


def _crud_update(provider, entity, crud_call):
    if isinstance(entity, EntityCollection):
        entity = entity.entities()
    with _handle_error():
        return crud_call(provider, entity)


def _crud_read(provider, read_filter, is_config, crud_call):
    if provider is None:
        raise YServiceError("provider cannot be None")

    if read_filter is None:
        with _handle_error():
            return _read_entities(provider, get_config=is_config)

    filters = read_filter
    if isinstance(read_filter, EntityCollection):
        filters = read_filter.entities()

    _set_nontop_entity_filter(filters, YFilter.read)
    top_filters = _get_top_level_entity(filters, provider.get_session().get_root_schema())
    with _handle_error():
        read_top_entity = crud_call(provider, top_filters)
    read_entity = _get_child_entity_from_top(read_top_entity, filters)

    if isinstance(read_filter, EntityCollection):
        read_entity = Config(read_entity)
    return read_entity
