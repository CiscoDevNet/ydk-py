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

""" errors.py

   Contains types representing the Exception hierarchy in YDK

"""
from lxml import etree
from enum import Enum


class YPYErrorCode(Enum):
    ''' Exception Enum for YDK errors '''
    INVALID_UNION_VALUE = 'Cannot translate union value'
    INVALID_ENCODE_VALUE = 'Cannot encode value'
    INVALID_DECODE_RPC = 'Cannout decode value'

    INVALID_HIERARCHY_PARENT = 'Parent is not set. \
                    Parent Hierarchy cannot be determined'
    INVALID_HIERARCHY_KEY = 'Key value is not set. \
                    Parent hierarchy cannot be constructed'
    INVALID_RPC = 'Object is not an RPC, cannot execute non-RPC object.'
    INVALID_MODIFY = 'Entity is read-only, cannot modify a read-only entity.'
    SERVER_REJ = 'Server rejected request.'
    SERVER_COMMIT_ERR = 'Server reported an error while committing change.'

    INVALID_TYPE = 'Type is invalid'
    INVALID_VALUE = 'Value is invalid'


class YPYError(Exception):
    ''' Base Exception for YDK Errors '''
    def __init__(self, error_code=None, error_msg=None):
        self.code = error_code
        self.message = error_msg

    def __str__(self):
        ret = None
        if self.code is None:
            ret = self.message
            return ret
        else:
            ret = self.code.value
            if self.message is not None:
                ret = [ret]
                parser = etree.XMLParser(remove_blank_text=True)
                root = etree.XML(self.message.encode('utf-8'), parser)
                for r in root.iter():
                    tag = r.tag[r.tag.rfind('}') + 1:]
                    if r.text is not None:
                        ret.append('\t{}: {}'.format(tag, r.text.strip()))
                ret = '\n'.join(ret)
            return ret


class YPYModelError(YPYError):
    '''
    Exception for Client Side Data Validation

    Type Validation\n
    --------
    Any data validation error encountered that is related to type \
    validation encountered does not raise an Exception right away.

    To uncover as many client side issues as possible, \
    an i_errors list is injected in the parent entity of any entity \
    with issues. The items added to this i_errors list captures the \
    object type that caused the error as well as an error message.

    '''
    def __init__(self, error_msg):
        super(YPYModelError, self).__init__(error_msg=error_msg)


class YPYServiceError(YPYError):
    '''
    Exception for Service Side Validation
    '''
    def __init__(self, error_code=None, error_msg=None):
        super(YPYServiceError, self).__init__(
            error_code=error_code, error_msg=error_msg)


class YPYServiceProviderError(YPYError):
    '''
    Exception for Provider Side Validation
    '''
    def __init__(self, error_code=None, error_msg=None):
        super(YPYServiceProviderError, self).__init__(
            error_code=error_code, error_msg=error_msg)
