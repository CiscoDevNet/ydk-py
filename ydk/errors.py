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

class YPYError(Exception):
    ''' Base Exception for YDK Errors '''
    pass

class YPYDataValidationError(YPYError):
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
    pass
