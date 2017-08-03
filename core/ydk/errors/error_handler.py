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
import sys
import inspect
import contextlib

from ydk.errors import YPYError as _YPYError
from ydk.errors import YPYCoreError as _YPYCoreError
from ydk.errors import YPYCodecError as _YPYCodecError
from ydk.errors import YPYClientError as _YPYClientError
from ydk.errors import YPYIllegalStateError as _YPYIllegalStateError
from ydk.errors import YPYInvalidArgumentError as _YPYInvalidArgumentError
from ydk.errors import YPYModelError as _YPYModelError
from ydk.errors import YPYOperationNotSupportedError as _YPYOperationNotSupportedError
from ydk.errors import YPYServiceError as _YPYServiceError
from ydk.errors import YPYServiceProviderError as _YPYServiceProviderError


if sys.version_info > (3, 0):
    inspect.getargspec = inspect.getfullargspec


_ERRORS = {"YCPPError": _YPYError,
           "YCPPCoreError": _YPYCoreError,
           "YCPPCodecError": _YPYCodecError,
           "YCPPClientError": _YPYClientError,
           "YCPPIllegalStateError": _YPYIllegalStateError,
           "YCPPInvalidArgumentError": _YPYInvalidArgumentError,
           "YCPPModelError": _YPYModelError,
           "YCPPOperationNotSupportedError": _YPYOperationNotSupportedError,
           "YCPPServiceError": _YPYServiceError,
           "YCPPServiceProviderError": _YPYServiceProviderError,
}


def _raise(exc):
    """Suppress old exception context for Python > 3.3,
    Use exec to avoid SyntaxError under Python 2 environment.
    """
    if sys.version_info >= (3,3):
        exec("raise exc from None")
    else:
        raise exc


@contextlib.contextmanager
def handle_runtime_error():
    _exc = None
    try:
        yield
    except RuntimeError as err:
        msg = str(err)
        if ":" in msg:
            etype_str, msg = msg.split(":", 1)
            etype = _ERRORS.get(etype_str, _YPYError)
        else:
            etype = _YPYError
            msg = msg
        _exc = etype(msg)
    except TypeError as err:
        msg = str(err)
        if ':' in msg:
            etype_str, msg = msg.split(':', 1)
            _exc = _YPYServiceError(msg)
        else:
            _exc = _YPYError(msg)
    finally:
        if _exc:
            _raise(_exc)


@contextlib.contextmanager
def handle_type_error():
    """Rethrow TypeError as YPYModelError"""
    _exc = None
    try:
        yield
    except TypeError as err:
        _exc = _YPYModelError(str(err))
    finally:
        if _exc:
            _raise(_exc)


@contextlib.contextmanager
def handle_import_error(logger, level):
    try:
        yield
    except ImportError as err:
        logger.log(level, str(err))


def check_argument(func):
    def helper(self, provider, entity, *args, **kwargs):
        _, pname, ename = inspect.getargspec(func).args[:3]
        if provider is None or entity is None:
            err_msg = "'{0}' and '{1}' cannot be None".format(pname, ename)
            raise _YPYServiceError(error_msg=err_msg)
        return func(self, provider, entity, *args, **kwargs)
    return helper
