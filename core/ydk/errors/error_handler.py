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

from ydk.errors import YError as _YError
from ydk.errors import YCoreError as _YCoreError
from ydk.errors import YCodecError as _YCodecError
from ydk.errors import YClientError as _YClientError
from ydk.errors import YIllegalStateError as _YIllegalStateError
from ydk.errors import YInvalidArgumentError as _YInvalidArgumentError
from ydk.errors import YModelError as _YModelError
from ydk.errors import YOperationNotSupportedError as _YOperationNotSupportedError
from ydk.errors import YServiceError as _YServiceError
from ydk.errors import YServiceProviderError as _YServiceProviderError


if sys.version_info > (3, 0):
    inspect.getargspec = inspect.getfullargspec


_ERRORS = {"YError": _YError,
           "YCoreError": _YCoreError,
           "YCodecError": _YCodecError,
           "YClientError": _YClientError,
           "YIllegalStateError": _YIllegalStateError,
           "YInvalidArgumentError": _YInvalidArgumentError,
           "YModelError": _YModelError,
           "YOperationNotSupportedError": _YOperationNotSupportedError,
           "YServiceError": _YServiceError,
           "YServiceProviderError": _YServiceProviderError,
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
            etype = _ERRORS.get(etype_str, _YError)
        else:
            etype = _YError
            msg = msg
        _exc = etype(msg)
    except TypeError as err:
        msg = str(err)
        if ':' in msg:
            etype_str, msg = msg.split(':', 1)
            _exc = _YServiceError(msg)
        else:
            _exc = _YError(msg)
    finally:
        if _exc:
            _raise(_exc)


@contextlib.contextmanager
def handle_type_error():
    """Rethrow TypeError as YModelError"""
    _exc = None
    try:
        yield
    except TypeError as err:
        _exc = _YModelError(str(err))
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
            raise _YServiceError(error_msg=err_msg)
        return func(self, provider, entity, *args, **kwargs)
    return helper
