""" Cisco_IOS_XR_types 

This module contains a collection of IOS\-XR derived YANG data 
types.
    
Copyright (c) 2013\-2016 by Cisco Systems, Inc.
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

    .. data:: none = 0

    	The password string is clear text.

    .. data:: md5 = 1

    	The password is encrypted to an MD5 digest.

    .. data:: proprietary = 2

    	The password is encrypted using Cisco type 7 

    	password encryption.

    """

    none = 0

    md5 = 1

    proprietary = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_types as meta
        return meta._meta_table['EncryptionTypeEnum']



