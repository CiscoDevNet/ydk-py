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

""" types.py 
 
   Contains type definitions.
   
"""

from decimal import Decimal, getcontext
from errors import YPYDataValidationError


class DELETE(object):
    '''Marker class used to mark nodes that are to be deleted '''
    pass

class READ(object):
    '''Marker class used to mark nodes that are to be read '''
    pass

class Empty(object):
    """ 
        .. _ydk_models_types_Empty:
        
        Represents the empty type in YANG. The empty built-in type represents a leaf that does not have any
        value, it conveys information by its presence or absence.
         
    """
    def __eq__(self, rhs):
        if not isinstance(rhs, Empty):
            raise YPYDataValidationError("Empty comparision error, invalid rhs\n")
        return True

    def __ne__(self, rhs):
        return not isinstance(rhs, Empty)



class Decimal64(object):
    """ 
        .. _ydk_models_types_Decimal64:
        
        Represents the decimal64 YANG type. The decimal64 type represents a
        subset of the real numbers, which can
        be represented by decimal numerals.  The value space of decimal64 is
        the set of numbers that can be obtained by multiplying a 64-bit
        signed integer by a negative power of ten, i.e., expressible as
        "i x 10^-n" where i is an integer64 and n is an integer between 1 and
        18, inclusively.
    """
    def __init__(self, str_val):
        self.s = str_val

    def __str__(self):
       
        return self.s

    def __cmp__(self, rhs):
        if not isinstance(rhs, Decimal64):
            raise YPYDataValidationError("Decimal64 comparision error, invalid rhs\n")
        return cmp(self.s, rhs.s)

    def __eq__(self, rhs):
        if not isinstance(rhs, Decimal64):
            raise YPYDataValidationError("Decimal64 comparision error, invalid rhs\n")
        return self.__cmp__(rhs) == 0

    def __ne__(self, rhs):
        if not isinstance(rhs, Decimal64):
            raise YPYDataValidationError("Decimal64 comparision error, invalid rhs\n")
        return self.__cmp__(rhs) != 0

    def __lt__(self, rhs):
        if not isinstance(rhs, Decimal64):
            raise YPYDataValidationError("Decimal64 comparision error, invalid rhs\n")
        if self.s is None:
            return True
        
        if rhs.s is None:
            return False
        
        getcontext().prec = 18
        self_dec = Decimal(self.s)
        rhs_dec = Decimal(rhs.s)
        return self_dec < rhs_dec

    def __le__(self, rhs):
        if not isinstance(rhs, Decimal64):
            raise YPYDataValidationError("Decimal64 comparision error, invalid rhs\n")
        
        if self.s is None:
            return True
        
        if rhs.s is None:
            return False
        
        getcontext().prec = 18
        self_dec = Decimal(self.s)
        rhs_dec = Decimal(rhs.s)
        return self_dec <= rhs_dec

    def __gt__(self, rhs):
        if not isinstance(rhs, Decimal64):
            raise YPYDataValidationError("Decimal64 comparision error, invalid rhs\n")
        
        if self.s is None:
            return False
        
        if rhs.s is None:
            return True
        
        getcontext().prec = 18
        self_dec = Decimal(self.s)
        rhs_dec = Decimal(rhs.s)
        
        return self_dec > rhs_dec

    def __ge__(self, rhs):
        if not isinstance(rhs, Decimal64):
            raise YPYDataValidationError("Decimal64 comparision error, invalid rhs\n")
                
        if self.s is None:
            return False
        
        if rhs.s is None:
            return True
        
        getcontext().prec = 18
        self_dec = Decimal(self.s)
        rhs_dec = Decimal(rhs.s)
        
        return self_dec >= rhs_dec

class FixedBitsDict(object):
    """ Super class of all classes that represents the bits type in YANG
    
        A concrete implementation of this class has a dictionary.

       The bits built-in type represents a bit set.  That is, a bits value
       is a set of flags identified by small integer position numbers
       starting at 0.  Each bit number has an assigned name.
    """
    def __init__(self, dictionary, pos_map):
        self._dictionary = dictionary
        self._pos_map = pos_map
    
    def __eq__(self, other):
        return ( isinstance(other, self.__class__) and self.__dict__ == other.__dict__)
    
    def __setitem__(self, key, item):
        if key not in self._dictionary:
            raise KeyError("The key {} is not defined.". format(key))
        self._dictionary[key] = item
    
    def __getitem__(self, key):
        return self.__dictionary[key]
    
    def __str__(self):
        return " ".join([key for key in self._dictionary if self._dictionary[key] == True])
    

    def __ne__(self, rhs):
        return not self.__eq__(rhs)
    
    def _has_data(self):
        for key in self._dictionary:
            if self._dictionary[key]:
                return True
        return False

class YList(list):
    """ Represents a list with support for hanging a parent 
    
        All YANG based entity classes that have lists or leaf-lists 
        in them use YList to represent the list.

        The "list" statement is used to define an interior data node in the
        schema tree.  A list node may exist in multiple instances in the data
        tree.  Each such instance is known as a list entry.  The "list"
        statement takes one argument, which is an identifier, followed by a
        block of substatements that holds detailed list information.

        A list entry is uniquely identified by the values of the list's keys,
        if defined.

        The "leaf-list" statement is used to define an
        array of a particular type.  The "leaf-list" statement takes one
        argument, which is an identifier, followed by a block of
        substatements that holds detailed leaf-list information.
        
    """
    def __init__(self):
        super(YList, self).__init__()
        self.parent = None
        self.property_name = None


