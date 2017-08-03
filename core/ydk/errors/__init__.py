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

""" errors
   Contains types representing the Exception hierarchy in YDK
"""


class YPYError(Exception):
    """Base class for YPY Errors.
    The subclasses give a specialized view of the error that has occurred.
    """
    def __init__(self, error_msg):
        self.message = error_msg

    def __repr__(self):
        return self.message

    def __str__(self):
        return self.__repr__()

class YPYCoreError(YPYError):
    """
    Exception for core error
    """
    def __init__(self, error_msg):
        super(YPYCoreError, self).__init__(error_msg)


class YPYCodecError(YPYError):
    """
    Exception for Codec Error
    """
    def __init__(self, error_msg):
        super(YPYCodecError, self).__init__(error_msg)

class YPYClientError(YPYError):
    """
    Exception for Client Side Validation
    """
    def __init__(self, error_msg):
        super(YPYClientError, self).__init__(error_msg)


class YPYServiceProviderError(YPYError):
    """
    Exception for Provider Side Validation
    """
    def __init__(self, error_msg):
        super(YPYServiceProviderError, self).__init__(error_msg)


class YPYServiceError(YPYError):
    """
    Exception for Service Side Validation
    """
    def __init__(self, error_msg):
        super(YPYServiceError, self).__init__(error_msg)


class YPYIllegalStateError(YPYError):
    """Illegal State Error.
    Thrown when an operation/service is invoked on an object that is not
    in the right state. Use the error_msg for the error.
    """
    def __init__(self, error_msg):
        super(YPYIllegalStateError, self).__init__(error_msg)


class YPYInvalidArgumentError(YPYError):
    """Invalid Argument.
    Use the error_msg for the error.
    """
    def __init__(self, error_msg):
        super(YPYInvalidArgumentError, self).__init__(error_msg)


class YPYOperationNotSupportedError(YPYError):
    """Operation Not Supported Error.
    Thrown when an yfilter is not supported.
    """
    def __init__(self, error_msg):
        super(YPYOperationNotSupportedError, self).__init__(error_msg)


class YPYModelError(YPYError):
    """Model Error.
    Thrown when a model constraint is violated.
    """
    def __init__(self, error_msg):
        super(YPYModelError, self).__init__(error_msg)
