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
from .meta_service import MetaService
from enum import Enum
from ydk.errors import YPYModelError, YPYServiceError
from . import ietf_netconf
from . import ietf_netconf_with_defaults

from ydk.types import Empty
import logging


class Datastore(Enum):
    """Type of datastore."""
    candidate = 1
    running = 2
    startup = 3


class NetconfService(Service):
    """Netconf Service class for executing netconf operations."""

    def __init__(self):
        self.executor = ExecutorService()
        self.service_logger = logging.getLogger(__name__)

    def cancel_commit(self, provider, persist_id=None):
        """Execute an cancel-commit operation to cancel an ongoing confirmed commit.

        Args:
            provider (ydk.providers.ServiceProvider): A provider instance.
            persist_id (str): Cancels a persistent confirmed commit. The value
                MUST be equal to the value given in the <persist> parameter to
                the <commit> operation. If the value does not match, the
                operation fails with an "invalid-value" error.

        Returns:
            An ok reply string if operation succeeds.

        Raises:
            YPYModelError: If validation error occurs.
            YPYServiceError: If other error has occurred.
                Possible errors could be:
                    - A server side error
                    - If there isn't enough information in the entity to
                      prepare the message (missing keys for example).
        """
        self.service_logger.info('Executing cancel-commit RPC')

        rpc = ietf_netconf.CancelCommitRpc()
        rpc.input.persist_id = persist_id

        return self.executor.execute_rpc(provider, rpc)

    def close_session(self, provider):
        """Execute a close-session operation to cancel an ongoing confirmed commit.

        Args:
            provider (ydk.providers.ServiceProvider): A provider instance.

        Returns:
            An ok reply string if operation succeeds.

        Raises:
            YPYModelError: If validation error occurs.
            YPYServiceError: If other error has occurred.
                Possible errors could be:
                    - A server side error
                    - If there isn't enough information in the entity to
                      prepare the message (missing keys for example).
        """
        self.service_logger.info('Executing close-session RPC')
        return self.executor.execute_rpc(provider, ietf_netconf.CloseSessionRpc())

    def commit(self, provider, confirmed=False, confirm_timeout=None, persist=False, persist_id=None):
        """Execute a commit operation to commit the candidate configuration as the
           device's new current configuration.

        Args:
            provider (ydk.providers.ServiceProvider): A provider instance.
            confirmed (bool): Perform a confirmed commit operation.
            confirm_timeout (int): The timeout interval for a confirmed commit.
            persist (str): Make a confirmed commit persistent. A persistent
                confirmed commit is not aborted if the NETCONF session
                terminates. The only way to abort a persistent confirmed commit
                is to let the timer expire, or to use the <cancel-commit>
                operation. The value of this parameter is a token that must be
                given in the 'persist-id' parameter of <commit> or
                <cancel-commit> operations in order to confirm or cancel the
                persistent confirmed commit.
                The token should be a random string.
            persist_id (str): This parameter is given in order to commit a
                persistent confirmed commit. The value must be equal to the
                value given in the 'persist' parameter to the <commit>
                operation. If it does not match, the operation fails with an
                'invalid-value' error.

        Returns:
            An ok reply string if operation succeeds.

        Raises:
            YPYModelError: If validation error occurs.
            YPYServiceError: If other error has occurred.
                Possible errors could be:
                    - A server side error
                    - If there isn't enough information in the entity to
                      prepare the message (missing keys for example).
        """
        self.service_logger.info('Executing commit RPC')
        rpc = ietf_netconf.CommitRpc()
        rpc.input.confirm_timeout = confirm_timeout
        rpc.input.persist_id = persist_id
        if confirmed:
            rpc.input.confirmed = Empty()
        if persist:
            rpc.input.persist = Empty()

        return self.executor.execute_rpc(provider, rpc)

    def copy_config(self, provider, target, source, with_defaults_option=None):
        """ Execute a copy-config operation to create or replace an entire
            configuration datastore with the contents of another complete
            configuration datastore.

        Args:
            provider (ydk.providers.ServiceProvider): A provider instance.
            target (Datastore | str): Particular configuration to copy to.
                Valid options are Datastore.candidate, Datastore.running,
                Datastore.startup and url(str) if the device has such feature
                advertised in device capability.
            source (Datastore | str | object): Particular configuration to copy
                from. Valid options are Datastore.candidate, Datastore.running,
                Datastore.startup and url(str) if the deivce has such feature
                advertised in capability. YDK entity object could also be used
                as a config block for this parameter.
            with_defaults (WithDefaultsModeEnum): The explicit defaults
                processing mode requested.

        Returns:
            An ok reply string if operation succeeds.

        Raises:
            YPYModelError: If validation error occurs.
            YPYServiceError: If other error has occurred.
                Possible errors could be:
                    - A server side error
                    - If there isn't enough information in the entity to
                      prepare the message (missing keys for example).
        """
        if None in (target, source):
            self.service_logger.error('Passed in a None arg')
            err_msg = "'target' and 'source' cannot be None"
            raise YPYServiceError(error_msg=err_msg)

        if with_defaults_option is not None and not isinstance(with_defaults_option, ietf_netconf_with_defaults.WithDefaultsModeEnum):
            err_msg = "optional arg 'with_defaults_option' must be of type ietf_netconf_with_defaults.WithDefaultsModeEnum"
            raise YPYServiceError(error_msg=err_msg)

        self.service_logger.info('Executing copy-config RPC')

        rpc = ietf_netconf.CopyConfigRpc()
        _validate_datastore_options(source, 'copy-config:source')
        _validate_datastore_options(target, 'copy-config:target')
        rpc.input.source = _get_rpc_datastore_object(source, rpc.input.source)
        rpc.input.target = _get_rpc_datastore_object(target, rpc.input.target)
        rpc.input.with_defaults = with_defaults_option

        return self.executor.execute_rpc(provider, rpc)

    def delete_config(self, provider, target):
        """Execute an delete-config operation to delete a configuration datastore.

        Args:
            provider (ydk.providers.ServiceProvider): A provider instance.
            target (Datastore.startup | str): Particular configuration to
                delete. Valid options are Datastore.startup or url(str).

        Returns:
            An ok reply string if operation succeeds.

        Raises:
            YPYModelError: If validation error occurs.
            YPYServiceError: If other error has occurred.
                Possible errors could be:
                    - A server side error
                    - If there isn't enough information in the entity to
                      prepare the message (missing keys for example).
        """
        if target is None:
            err_msg = "'target' cannot be None"
            raise YPYServiceError(error_msg=err_msg)
        self.service_logger.info('Executing delete-config RPC')

        rpc = ietf_netconf.DeleteConfigRpc()
        _validate_datastore_options(target, 'delete-config:target')
        rpc.input.target = _get_rpc_datastore_object(target, rpc.input.target)

        return self.executor.execute_rpc(provider, rpc)

    def discard_changes(self, provider):
        """Execute a discard-changes operation to revert the candidate
        configuration to the current running configuration.

        Args:
            provider (ydk.providers.ServiceProvider): A provider instance.

        Returns:
            An ok reply string if operation succeeds.

        Raises:
            YPYModelError: If validation error occurs.
            YPYServiceError: If other error has occurred.
                Possible errors could be:
                    - A server side error
                    - If there isn't enough information in the entity to
                      prepare the message (missing keys for example).
        """
        self.service_logger.info('Executing discard-changes RPC')
        return self.executor.execute_rpc(provider, ietf_netconf.DiscardChangesRpc())

    def edit_config(self, provider, target, config, default_operation=None, error_option=None, test_option=None):
        """Execute an edit-config operation to load all or part of a specified
           configuration to the specified target configuration.

        Args:
            provider (ydk.providers.ServiceProvider): A provider instance.
            target (Datastore): Particular configuration to copy from. Valid
                options are Datastore.candidate, Datastore.running.
            config (object): A YDK entity object used as a config block.
            default_operation (EditConfigRpc.Input.DefaultOperationEnum):
                Selects the default operation for this edit-config request.
            error_option (EditConfigRpc.Input.ErrorOptionEnum): Selects the
                error option for this edit-config request.
            test_option (EditConfigRpc.Input.TestOptionEnum): Selects the
                test option for this edit-config request.

        Returns:
            An ok reply string if operation succeeds.

        Raises:
            YPYModelError: If validation error occurs.
            YPYServiceError: If other error has occurred.
                Possible errors could be:
                    - A server side error
                    - If there isn't enough information in the entity to
                      prepare the message (missing keys for example).
        """
        if None in (target, config):
            self.service_logger.error('Passed in a None arg')
            err_msg = "'target' and 'config' cannot be None"
            raise YPYServiceError(error_msg=err_msg)

        if default_operation is not None and not isinstance(default_operation, ietf_netconf.EditConfigRpc.Input.DefaultOperationEnum):
            err_msg = "optional arg 'default_operation' must be of type ietf_netconf.EditConfigRpc.Input.DefaultOperationEnum"
            raise YPYServiceError(error_msg=err_msg)
        if error_option is not None and not isinstance(error_option, ietf_netconf.EditConfigRpc.Input.ErrorOptionEnum):
            err_msg = "optional arg 'error_option' must be of type ietf_netconf.EditConfigRpc.Input.ErrorOptionEnum"
            raise YPYServiceError(error_msg=err_msg)
        if test_option is not None and not isinstance(test_option, ietf_netconf.EditConfigRpc.Input.TestOptionEnum):
            err_msg = "optional arg 'test_option' must be of type ietf_netconf.EditConfigRpc.Input.TestOptionEnum"
            raise YPYServiceError(error_msg=err_msg)

        self.service_logger.info('Executing edit-config RPC')

        rpc = ietf_netconf.EditConfigRpc()
        _validate_datastore_options(target, 'edit-config:target')
        rpc.input.target = _get_rpc_datastore_object(target, rpc.input.target)
        rpc.input.config = config
        rpc.input.default_operation = default_operation
        rpc.input.error_option = error_option
        rpc.input.test_option = test_option
        return self.executor.execute_rpc(provider, rpc)

    def get_config(self, provider, source, get_filter, with_defaults_option=None):
        """Execute a get-config operation to retrieve all or part of a
        specified configuration.

        Args:
            provider (ydk.providers.ServiceProvider): A provider instance.
            source (Datastore): Particular configuration to retrieve. Valid
                options are Datastore.candidate, Datastore.running,
                and Datastore.startup.
            get_filter (object): A YDK entity object used as a subtree filter
                or XPath filter.
            with_defaults (WithDefaultsModeEnum): The explicit defaults
                processing mode requested.

        Returns:
            A YDK entity object represents copy of the running datastore subset
            and/or state data that matched the filter criteria (if any). An
            empty data container indicates that the request did not produce
            any results.

        Raises:
            YPYModelError: If validation error occurs.
            YPYServiceError: If other error has occurred.
                Possible errors could be:
                    - A server side error
                    - If there isn't enough information in the entity to
                      prepare the message (missing keys for example).
        """
        if source is None:
            err_msg = "'source' cannot be None"
            raise YPYServiceError(error_msg=err_msg)

        if with_defaults_option is not None and not isinstance(with_defaults_option, ietf_netconf_with_defaults.WithDefaultsModeEnum):
            err_msg = "optional arg 'with_defaults_option' must be of type ietf_netconf_with_defaults.WithDefaultsModeEnum"
            raise YPYServiceError(error_msg=err_msg)

        self.service_logger.info('Executing get-config RPC')

        rpc = ietf_netconf.GetConfigRpc()
        rpc.input.filter = get_filter
        _validate_datastore_options(source, 'get-config:source')
        rpc.input.source = _get_rpc_datastore_object(source, rpc.input.source)
        rpc.input.with_defaults = with_defaults_option
        rpc = MetaService.normalize_meta(provider._get_capabilities(), rpc)

        result = provider.execute(
                                    provider.sp_instance.encode_rpc(rpc),
                                    ''
                                    )
        result = payload_convert(result)
        if len(result) == 0:
            return None
        return provider.decode(result, None)

    def get(self, provider, get_filter, with_defaults_option=None):
        """Execute a get operation to retrieve running configuration and device
        state information.

        Args:
            provider (ydk.providers.ServiceProvider): A provider instance.
            get_filter (object): A YDK entity object specifies the portion of
                the system configuration and state data to retrieve.
            with_defaults (WithDefaultsModeEnum): The explicit defaults
                processing mode requested.

        Returns:
            A YDK entity object represents copy of the running datastore subset
            and/or state data that matched the filter criteria (if any). An
            empty data container indicates that the request did not produce
            any results

        Raises:
            YPYModelError: If validation error occurs.
            YPYServiceError: If other error has occurred.
                Possible errors could be:
                    - A server side error
                    - If there isn't enough information in the entity to
                      prepare the message (missing keys for example).
        """
        if with_defaults_option is not None and not isinstance(with_defaults_option, ietf_netconf_with_defaults.WithDefaultsModeEnum):
            err_msg = "optional arg 'with_defaults_option' must be of type ietf_netconf_with_defaults.WithDefaultsModeEnum"
            raise YPYServiceError(error_msg=err_msg)
        self.service_logger.info('Executing get RPC')

        rpc = ietf_netconf.GetRpc()
        rpc.input.filter = get_filter
        rpc.input.with_defaults = with_defaults_option
        rpc = MetaService.normalize_meta(provider._get_capabilities(), rpc)

        result = provider.execute(
                                    provider.sp_instance.encode_rpc(rpc),
                                    ''
                                    )
        result = payload_convert(result)
        if len(result) == 0:
            return None
        return provider.decode(result, None)

    def kill_session(self, provider, session_id):
        """Execute a kill-session operation to force the termination of a
        NETCONF session.

        Args:
            provider (ydk.providers.ServiceProvider): A provider instance.
            session_id (int): Particular session to kill.

        Returns:
            An ok reply string if operation succeeds.

        Raises:
            YPYModelError: If validation error occurs.
            YPYServiceError: If other error has occurred.
                Possible errors could be:
                    - A server side error
                    - If there isn't enough information in the entity to
                      prepare the message (missing keys for example).
        """
        self.service_logger.info('Executing kill-session RPC')
        rpc = ietf_netconf.KillSessionRpc()
        rpc.input.session_id = session_id

        return self.executor.execute_rpc(provider, rpc)

    def lock(self, provider, target):
        """Execute a lock operation to allow the client to lock the
        configuration system of a device.

        Args:
            provider (ydk.providers.ServiceProvider): A provider instance.
            target (Datastore): Particular configuration to lock. Valid options
            are Datastore.candidate, Datastore.running, and Datastore.startup
            if the device has such feature advertised.

        Returns:
            An ok reply string if operation succeeds.

        Raises:
            YPYModelError: If validation error occurs.
            YPYServiceError: If other error has occurred.
                Possible errors could be:
                    - A server side error
                    - If there isn't enough information in the entity to
                      prepare the message (missing keys for example).
        """
        if target is None:
            err_msg = "'target' cannot be None"
            raise YPYServiceError(error_msg=err_msg)
        self.service_logger.info('Executing lock RPC')

        rpc = ietf_netconf.LockRpc()
        _validate_datastore_options(target, 'lock:target')
        rpc.input.target = _get_rpc_datastore_object(target, rpc.input.target)

        return self.executor.execute_rpc(provider, rpc)

    def unlock(self, provider, target):
        """Execute an unlock operation to  release a configuration lock,
        previously obtained with the 'lock' operation.

        Args:
            provider (ydk.providers.ServiceProvider): A provider instance.
            target (Datastore): Particular configuration to unlock. Valid
            options are Datastore.candidate, Datastore.running, and
            Datastore.startup if the device has such feature advertised.

        Returns:
            An ok reply string if operation succeeds.

        Raises:
            YPYModelError: If validation error occurs.
            YPYServiceError: If other error has occurred.
                Possible errors could be:
                    - A server side error
                    - If there isn't enough information in the entity to
                      prepare the message (missing keys for example).
        """
        if target is None:
            err_msg = "'target' cannot be None"
            raise YPYServiceError(error_msg=err_msg)
        self.service_logger.info('Executing unlock RPC')

        rpc = ietf_netconf.UnlockRpc()
        _validate_datastore_options(target, 'unlock:target')
        rpc.input.target = _get_rpc_datastore_object(target, rpc.input.target)

        return self.executor.execute_rpc(provider, rpc)

    def validate(self, provider, source=None):
        """Execute a validate operation to validate the contents of the
        specified configuration.

        Args:
            provider (ydk.providers.ServiceProvider): A provider instance.
            source (Datastore | str | object): Particular configuration to
                validate. Valid options are Datastore.candidate,
                Datastore.running, Datastore.startup and url(str) if the deivce
                has such feature advertised in device capability. YDK entity
                object could also be used as a config block for this parameter.

        Returns:
            An ok reply string if operation succeeds.

        Raises:
            YPYModelError: If validation error occurs.
            YPYServiceError: If other error has occurred.
                Possible errors could be:
                    - A server side error
                    - If there isn't enough information in the entity to
                      prepare the message (missing keys for example).
        """
        if source is None:
            err_msg = "'source' cannot be None"
            raise YPYServiceError(error_msg=err_msg)
        self.service_logger.info('Executing validate RPC')

        rpc = ietf_netconf.ValidateRpc()
        if source is not None:
            _validate_datastore_options(source, 'validate:source')
            rpc.input.source = _get_rpc_datastore_object(source, rpc.input.source)

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
    elif isinstance(datastore, object):
        rpc_datastore_type.config = datastore
        return rpc_datastore_type
    raise YPYModelError('Invalid datastore specified')


def _validate_datastore_options(datastore, option):
    res = True
    if option == 'copy-config:target':
        res = isinstance(datastore, (str, Datastore))
    elif option == 'copy-config:source':
        res = isinstance(datastore, (str, object, Datastore))
    elif option == 'delete-config:target':
        res = isinstance(datastore, str) or datastore == Datastore.startup
    elif option == 'edit-config:target':
        res = datastore in (Datastore.candidate, Datastore.running)
    elif option == 'get-config:source':
        res = isinstance(datastore, Datastore)
    elif option == 'lock:target':
        res = isinstance(datastore, Datastore)
    elif option == 'unlock:target':
        res = isinstance(datastore, Datastore)
    elif option == 'validate:source':
        res = isinstance(datastore, (str, object, Datastore))

    if not res:
        err_msg = _get_datastore_errmsg(option, datastore)
        raise YPYServiceError(error_msg=err_msg)


def _get_datastore_errmsg(option, datastore):
    if isinstance(datastore, str):
        datastore = 'url'
    if ':' in option:
        option = option[:option.find(':')]
    return ("%s datastore is not supported by Netconf %s operation" % (datastore, option))


def payload_convert(payload):
    from lxml import etree

    rt = etree.fromstring(payload.encode('utf-8'))
    chchs = rt.getchildren()[0].getchildren()
    if len(chchs) == 0:
        return ''
    return etree.tostring(chchs[0], pretty_print=True, encoding='utf-8').decode('utf-8')
