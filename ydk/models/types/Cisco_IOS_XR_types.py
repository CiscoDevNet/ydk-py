""" Cisco_IOS_XR_types 

This module contains a collection of IOS\-XR derived YANG data 
types.
    
Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class EncryptionTypeEnum(Enum):
    """
    EncryptionTypeEnum

    The type of encryption used on a password string.

    .. data:: NONE = 0

    	The password string is clear text.

    .. data:: MD5 = 1

    	The password is encrypted to an MD5 digest.

    .. data:: PROPRIETARY = 2

    	The password is encrypted using Cisco type 7 

    	password encryption.

    """

    NONE = 0

    MD5 = 1

    PROPRIETARY = 2


    @staticmethod
    def _meta_info():
        from ydk.models.types._meta import _Cisco_IOS_XR_types as meta
        return meta._meta_table['EncryptionTypeEnum']



