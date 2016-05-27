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
""" netconf_service.py

   The Netconf Service class.

"""
from .executor_service import ExecutorService
from .service import Service
from enum import Enum
from ydk.errors import YPYDataValidationError
try:
    from ydk.models.ietf import ietf_netconf
    from ydk.models.ietf import ietf_netconf_with_defaults
except:
    pass 
from ydk.types import Empty


class Datastore(Enum):
    '''
    Type of datastore
    '''
    candidate = 1
    running = 2
    startup = 3


class NetconfService(Service):
    """ Netconf Service class for executing netconf operations """

    def __init__(self):
        self.executor = ExecutorService()

    def cancel_commit(self, provider, persist_id=None):
        """ Execute an cancel-commit operation to cancel an ongoing confirmed commit.

            Args:
                - provider: An instance of ydk.providers.ServiceProvider
                - persist_id: This parameter is given in order to cancel a persistent confirmed commit.
                    The value must be equal to the value given in the 'persist' parameter to the <commit>
                    operation. If it does not match, the operation fails with an 'invalid-value' error

           Returns:
                 - ok reply if operation succeeds else, raises an exception

           Raises:
              `YPYDataValidationError <ydk.errors.html#ydk.errors.YPYDataValidationError>`_ if validation error occurs.
              `YPYError <ydk.errors.html#ydk.errors.YPYError>`_ if other error has occurred. Possible errors could be
                  - a server side error
                  - if there isn't enough information in the entity to prepare the message (missing keys for example)
        """
        rpc = ietf_netconf.CancelCommitRpc()
        rpc.input.persist_id = persist_id

        return self.executor.execute_rpc(provider, rpc)

    def close_session(self, provider):
        """ Execute a close-session operation to cancel an ongoing confirmed commit.

            Args:
                - provider: An instance of ydk.providers.ServiceProvider

           Returns:
                 - ok reply if operation succeeds else, raises an exception

           Raises:
              `YPYDataValidationError <ydk.errors.html#ydk.errors.YPYDataValidationError>`_ if validation error occurs.
              `YPYError <ydk.errors.html#ydk.errors.YPYError>`_ if other error has occurred. Possible errors could be
                  - a server side error
                  - if there isn't enough information in the entity to prepare the message (missing keys for example)
        """
        return self.executor.execute_rpc(provider, ietf_netconf.CloseSessionRpc())

    def commit(self, provider):
        """ Execute a commit operation to commit the candidate configuration as the device's new
            current configuration.

            Args:
                - provider: An instance of ydk.providers.ServiceProvider

           Returns:
                 - ok reply if operation succeeds else, raises an exception

           Raises:
              `YPYDataValidationError <ydk.errors.html#ydk.errors.YPYDataValidationError>`_ if validation error occurs.
              `YPYError <ydk.errors.html#ydk.errors.YPYError>`_ if other error has occurred. Possible errors could be
                  - a server side error
                  - if there isn't enough information in the entity to prepare the message (missing keys for example)
        """
        return self.executor.execute_rpc(provider, ietf_netconf.CommitRpc())

    def commit_confirmed(self, provider, confirm_timeout=None, persist=False, persist_id=None):
        """ Execute a commit operation to commit the candidate configuration with a confirmed option.

            Args:
                - provider: An instance of ydk.providers.ServiceProvider
                - confirm_timeout: The timeout interval for a confirmed commit
                - persist: This parameter is used to make a confirmed commit persistent. A persistent confirmed commit
                 is not aborted if the NETCONF session terminates.  The only way to abort a persistent confirmed commit
                 is to let the timer expire, or to use the <cancel-commit> operation. The value of this parameter is
                 a token that must be given in the 'persist-id' parameter of <commit> or <cancel-commit> operations
                 in order to confirm or cancel the persistent confirmed commit.  The token should be a random string
                - persist_id: This parameter is given in order to commit a persistent confirmed commit. The value must
                 be equal to the value given in the 'persist' parameter to the <commit> operation. If it does not match,
                 the operation fails with an 'invalid-value' error

           Returns:
                 - ok reply if operation succeeds else, raises an exception

           Raises:
              `YPYDataValidationError <ydk.errors.html#ydk.errors.YPYDataValidationError>`_ if validation error occurs.
              `YPYError <ydk.errors.html#ydk.errors.YPYError>`_ if other error has occurred. Possible errors could be
                  - a server side error
                  - if there isn't enough information in the entity to prepare the message (missing keys for example)
        """
        rpc = ietf_netconf.CommitRpc()
        rpc.input.confirm_timeout = confirm_timeout
        rpc.input.persist_id = persist_id
        if persist:
            rpc.input.persist = Empty()

        return self.executor.execute_rpc(provider, rpc)

    def copy_config(self, provider, target, source, with_defaults_option=None):
        """ Execute a copy-config operation to create or replace an entire configuration datastore with the
            contents of another complete configuration datastore.

            Args:
                - target: Particular configuration to copy to
                - source: Particular configuration to copy from
                - with_defaults: The explicit defaults processing mode requested

           Returns:
                 - ok reply if operation succeeds else, raises an exception

           Raises:
              `YPYDataValidationError <ydk.errors.html#ydk.errors.YPYDataValidationError>`_ if validation error occurs.
              `YPYError <ydk.errors.html#ydk.errors.YPYError>`_ if other error has occurred. Possible errors could be
                  - a server side error
                  - if there isn't enough information in the entity to prepare the message (missing keys for example)
        """
        assert target is not None
        assert source is not None

        if with_defaults_option is not None:
            assert isinstance(with_defaults_option, ietf_netconf_with_defaults.WithDefaultsMode_Enum)

        rpc = ietf_netconf.CopyConfigRpc()
        rpc.input.source = _get_rpc_datastore_object(source, rpc.input.source)
        rpc.input.target = _get_rpc_datastore_object(target, rpc.input.target)
        rpc.input.with_defaults_option = with_defaults_option

        return self.executor.execute_rpc(provider, rpc)

    def delete_config(self, provider, target):
        """ Execute an delete-config operation to delete a configuration datastore.

            Args:
                - target: Particular configuration to delete

           Returns:
                 - ok reply if operation succeeds else, raises an exception

           Raises:
              `YPYDataValidationError <ydk.errors.html#ydk.errors.YPYDataValidationError>`_ if validation error occurs.
              `YPYError <ydk.errors.html#ydk.errors.YPYError>`_ if other error has occurred. Possible errors could be
                  - a server side error
                  - if there isn't enough information in the entity to prepare the message (missing keys for example)
        """
        assert target is not None

        rpc = ietf_netconf.DeleteConfigRpc()
        rpc.input.target = _get_rpc_datastore_object(target, rpc.input.target)

        return self.executor.execute_rpc(provider, rpc)

    def discard_changes(self, provider):
        """ Execute a discard-changes operation to revert the candidate configuration to the current
            running configuration.

            Args:
                - provider: An instance of ydk.providers.ServiceProvider

           Returns:
                 - ok reply if operation succeeds else, raises an exception

           Raises:
              `YPYDataValidationError <ydk.errors.html#ydk.errors.YPYDataValidationError>`_ if validation error occurs.
              `YPYError <ydk.errors.html#ydk.errors.YPYError>`_ if other error has occurred. Possible errors could be
                  - a server side error
                  - if there isn't enough information in the entity to prepare the message (missing keys for example)
        """
        return self.executor.execute_rpc(provider, ietf_netconf.DiscardChangesRpc())

    def edit_config(self, provider, target, config, default_operation=None, error_option=None, test_option=None):
        """ Execute an edit-config operation to load all or part of a specified
            configuration to the specified target configuration.

            Args:
                - provider: An instance of ydk.providers.ServiceProvider
                - target: Particular configuration to edit
                - config: Inline Config content
                - default_operation: The default operation to use
                - error_option: The error option to use
                - test_option: The test option to use

           Returns:
                 - ok reply if operation succeeds else, raises an exception

           Raises:
              `YPYDataValidationError <ydk.errors.html#ydk.errors.YPYDataValidationError>`_ if validation error occurs.
              `YPYError <ydk.errors.html#ydk.errors.YPYError>`_ if other error has occurred. Possible errors could be
                  - a server side error
                  - if there isn't enough information in the entity to prepare the message (missing keys for example)
        """
        assert target is not None
        assert config is not None

        if default_operation is not None:
            assert isinstance(default_operation, ietf_netconf.EditConfigRpc.Input.DefaultOperation_Enum)
        if error_option is not None:
            assert isinstance(error_option, ietf_netconf.EditConfigRpc.Input.ErrorOption_Enum)
        if test_option is not None:
            assert isinstance(test_option, ietf_netconf.EditConfigRpc.Input.TestOption_Enum)

        rpc = ietf_netconf.EditConfigRpc()
        rpc.input.target = _get_rpc_datastore_object(target, rpc.input.target)
        rpc.input.config = config
        rpc.input.default_operation = default_operation
        rpc.input.error_option = error_option
        rpc.input.test_option = test_option
        return self.executor.execute_rpc(provider, rpc)

    def get_config(self, provider, source, get_filter, with_defaults_option=None):
        """ Execute a get-config operation to retrieve all or part of a specified configuration.

            Args:
                - get_filter: Subtree or XPath filter to use
                - source: Particular configuration to retrieve
                - with_defaults: The explicit defaults processing mode requested

           Returns:
                 - Copy of the running datastore subset and/or state data that matched the filter criteria (if any).
                   An empty data container indicates that the request did not produce any results

           Raises:
              `YPYDataValidationError <ydk.errors.html#ydk.errors.YPYDataValidationError>`_ if validation error occurs.
              `YPYError <ydk.errors.html#ydk.errors.YPYError>`_ if other error has occurred. Possible errors could be
                  - a server side error
                  - if there isn't enough information in the entity to prepare the message (missing keys for example)
        """
        assert source is not None


        if with_defaults_option is not None:
            assert isinstance(with_defaults_option, ietf_netconf_with_defaults.WithDefaultsMode_Enum)

        rpc = ietf_netconf.GetConfigRpc()
        rpc.input.filter = get_filter
        rpc.input.source = _get_rpc_datastore_object(source, rpc.input.source)
        rpc.input.with_defaults_option = with_defaults_option

        return self.executor.execute_rpc(provider, rpc)

    def get(self, provider, get_filter, with_defaults_option=None):
        """ Execute a get operation to retrieve running configuration and device state information.

            Args:
                - get_filter: This parameter specifies the portion of the system configuration and state data to retrieve
                - with_defaults: The explicit defaults processing mode requested

           Returns:
                 - Copy of the running datastore subset and/or state data that matched the filter criteria (if any).
                   An empty data container indicates that the request did not produce any results

           Raises:
              `YPYDataValidationError <ydk.errors.html#ydk.errors.YPYDataValidationError>`_ if validation error occurs.
              `YPYError <ydk.errors.html#ydk.errors.YPYError>`_ if other error has occurred. Possible errors could be
                  - a server side error
                  - if there isn't enough information in the entity to prepare the message (missing keys for example)
        """

        if with_defaults_option is not None:
            assert isinstance(with_defaults_option, ietf_netconf_with_defaults.WithDefaultsMode_Enum)

        rpc = ietf_netconf.GetRpc()
        rpc.input.filter = get_filter
        rpc.input.with_defaults_option = with_defaults_option

        return self.executor.execute_rpc(provider, rpc)

    def kill_session(self, provider, session_id):
        """ Execute a kill-session operation to force the termination of a NETCONF session.

            Args:
                - session_id: Particular session to kill


           Returns:
                 - ok reply if operation succeeds else, raises an exception

           Raises:
              `YPYDataValidationError <ydk.errors.html#ydk.errors.YPYDataValidationError>`_ if validation error occurs.
              `YPYError <ydk.errors.html#ydk.errors.YPYError>`_ if other error has occurred. Possible errors could be
                  - a server side error
                  - if there isn't enough information in the entity to prepare the message (missing keys for example)
        """
        rpc = ietf_netconf.KillSessionRpc()
        rpc.input.session_id = session_id

        return self.executor.execute_rpc(provider, rpc)

    def lock(self, provider, target):
        """ Execute a lock operation to allow the client to lock the configuration
            system of a device.

            Args:
                - target: Particular configuration to lock

           Returns:
                 - ok reply if operation succeeds else, raises an exception

           Raises:
              `YPYDataValidationError <ydk.errors.html#ydk.errors.YPYDataValidationError>`_ if validation error occurs.
              `YPYError <ydk.errors.html#ydk.errors.YPYError>`_ if other error has occurred. Possible errors could be
                  - a server side error
                  - if there isn't enough information in the entity to prepare the message (missing keys for example)
        """
        assert target is not None

        rpc = ietf_netconf.LockRpc()
        rpc.input.target = _get_rpc_datastore_object(target, rpc.input.target)

        return self.executor.execute_rpc(provider, rpc)

    def unlock(self, provider, target):
        """ Execute an unlock operation to  release a configuration lock,
            previously obtained with the 'lock' operation.

            Args:
                - target: Particular configuration to unlock

           Returns:
                 - ok reply if operation succeeds else, raises an exception

           Raises:
              `YPYDataValidationError <ydk.errors.html#ydk.errors.YPYDataValidationError>`_ if validation error occurs.
              `YPYError <ydk.errors.html#ydk.errors.YPYError>`_ if other error has occurred. Possible errors could be
                  - a server side error
                  - if there isn't enough information in the entity to prepare the message (missing keys for example)
        """
        assert target is not None

        rpc = ietf_netconf.UnlockRpc()
        rpc.input.target = _get_rpc_datastore_object(target, rpc.input.target)

        return self.executor.execute_rpc(provider, rpc)

    def validate(self, provider, source=None, config=None):
        """ Execute a validate operation to validate the contents of the specified configuration.

            Args:
                - source: Particular configuration to validate
                - with_defaults: The explicit defaults processing mode requested

           Returns:
                 - ok reply if operation succeeds else, raises an exception

           Raises:
              `YPYDataValidationError <ydk.errors.html#ydk.errors.YPYDataValidationError>`_ if validation error occurs.
              `YPYError <ydk.errors.html#ydk.errors.YPYError>`_ if other error has occurred. Possible errors could be
                  - a server side error
                  - if there isn't enough information in the entity to prepare the message (missing keys for example)
        """
        assert source is not None or config is not None

        rpc = ietf_netconf.ValidateRpc()
        if source is not None:
            rpc.input.source = _get_rpc_datastore_object(source, rpc.input.source)
        if config is not None:
            rpc.input.source.config = config

        return self.executor.execute_rpc(provider, rpc)


def _get_rpc_datastore_object(datastore, rpc_datastore_type):
    if isinstance(datastore, str):
        rpc_datastore_type.url = datastore
        return rpc_datastore_type
    elif datastore == Datastore.candidate:
        rpc_datastore_type.candidate = Empty()
        return rpc_datastore_type
    elif datastore == Datastore.running:
        rpc_datastore_type.running = Empty()
        return rpc_datastore_type
    elif datastore == Datastore.startup:
        rpc_datastore_type.startup = Empty()
        return rpc_datastore_type
    else:
        raise YPYDataValidationError('Invalid datastore specified')
