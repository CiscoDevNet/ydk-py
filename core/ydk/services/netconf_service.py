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
from ydk.ext.services import Datastore, NetconfService as _NetconfService
from ydk.errors import YPYServiceError as _YPYServiceError
from ydk.errors.error_handler import handle_runtime_error as _handle_error

class NetconfService(_NetconfService):
    """ Python wrapper for NetconfService
    """
    def __init__(self):
        self._ns = _NetconfService()

    def cancel_commit(self, provider, persist_id=-1):
        if None in (provider, persist_id):
            raise _YPYServiceError("provider and persist_id cannot be None")

        with _handle_error():
            return self._ns.cancel_commit(provider, persist_id)

    def close_session(self, provider):
        if provider is None:
            raise _YPYServiceError("provider cannot be None")

        with _handle_error():
            return self._ns.close_session(provider)

    def commit(self, provider, confirmed=False, confirm_timeout=-1, persist=-1, persist_id=-1):
        if provider is None:
            raise _YPYServiceError("provider cannot be None")

        with _handle_error():
            return self._ns.commit(provider, confirmed, confirm_timeout, persist, persist_id)

    def copy_config(self, provider, target, source=None, url="", source_config=None):
        if None in (provider, target) or (source is None and source_config is None):
            raise _YPYServiceError("provider, target, and source/source_config cannot be None")

        with _handle_error():
            if isinstance(source, Datastore):
                return self._ns.copy_config(provider, target, source, url)
            elif source_config is not None:
                return self._ns.copy_config(provider, target, source_config)
            else:
                return self._ns.copy_config(provider, target, source)

    def delete_config(self, provider, target, url=""):
        if None in (provider, target):
            raise _YPYServiceError("provider and target cannot be None")

        with _handle_error():
            return self._ns.delete_config(provider, target, url)

    def discard_changes(self, provider):
        if provider is None:
            raise _YPYServiceError("provider cannot be None")

        with _handle_error():
            return self._ns.discard_changes(provider)

    def edit_config(self, provider, target, config,
        default_operation="", test_option="", error_option=""):

        if None in (provider, target, config):
            raise _YPYServiceError("provider, target, and config cannot be None")

        with _handle_error():
            return self._ns.edit_config(provider, target, config,
                default_operation, test_option, error_option)

    def get_config(self, provider, source, read_filter):
        if None in (provider, source, read_filter):
            raise _YPYServiceError("provider, source, and filter cannot be None")

        with _handle_error():
            return self._ns.get_config(provider, source, read_filter)

    def get(self, provider, read_filter):
        if None in (provider, read_filter):
            raise _YPYServiceError("provider and filter cannot be None")

        with _handle_error():
            return self._ns.get(provider, read_filter)

    def kill_session(self, provider, session_id):
        if None in (provider, session_id):
            raise _YPYServiceError("provider and session_id cannot be None")

        with _handle_error():
            return self._ns.kill_session(provider, session_id)

    def lock(self, provider, target):
        if None in (provider, target):
            raise _YPYServiceError("provider and target cannot be None")

        with _handle_error():
            return self._ns.lock(provider, target)

    def unlock(self, provider, target):
        if None in (provider, target):
            raise _YPYServiceError("provider and target cannot be None")

        with _handle_error():
            return self._ns.unlock(provider, target)

    def validate(self, provider, source=None, url="", source_config=None):
        if provider is None or (source is None and source_config is None):
            raise _YPYServiceError("provider and source/source_config cannot be None")

        with _handle_error():
            if type(source) == Datastore:
                return self._ns.validate(provider, source, url)
            elif source_config is not None:
                return self._ns.validate(provider, source_config)
            else:
                return self._ns.validate(provider, source)
