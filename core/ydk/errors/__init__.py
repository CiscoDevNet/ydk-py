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


class YError(Exception):
    """Base class for Y Errors.
    The subclasses give a specialized view of the error that has occurred.
    """
    def __init__(self, error_msg):
        self.message = error_msg

    def __repr__(self):
        return self.message

    def __str__(self):
        return self.__repr__()

class YCoreError(YError):
    """
    Exception for core error
    """
    def __init__(self, error_msg):
        super(YCoreError, self).__init__(error_msg)


class YCodecError(YError):
    """
    Exception for Codec Error
    """
    def __init__(self, error_msg):
        super(YCodecError, self).__init__(error_msg)

class YClientError(YError):
    """
    Exception for Client Side Validation
    """
    def __init__(self, error_msg):
        super(YClientError, self).__init__(error_msg)


class YServiceProviderError(YError):
    """
    Exception for Provider Side Validation
    """
    def __init__(self, error_msg):
        super(YServiceProviderError, self).__init__(error_msg)


class YServiceError(YError):
    """
    Exception for Service Side Validation
    """
    def __init__(self, error_msg):
        super(YServiceError, self).__init__(error_msg)


class YIllegalStateError(YError):
    """Illegal State Error.
    Thrown when an operation/service is invoked on an object that is not
    in the right state. Use the error_msg for the error.
    """
    def __init__(self, error_msg):
        super(YIllegalStateError, self).__init__(error_msg)


class YInvalidArgumentError(YError):
    """Invalid Argument.
    Use the error_msg for the error.
    """
    def __init__(self, error_msg):
        super(YInvalidArgumentError, self).__init__(error_msg)


class YOperationNotSupportedError(YError):
    """Operation Not Supported Error.
    Thrown when an yfilter is not supported.
    """
    def __init__(self, error_msg):
        super(YOperationNotSupportedError, self).__init__(error_msg)


class YModelError(YError):
    """Model Error.
    Thrown when a model constraint is violated.
    """
    def __init__(self, error_msg):
        super(YModelError, self).__init__(error_msg)
