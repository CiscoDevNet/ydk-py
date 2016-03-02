""" Cisco_IOS_XR_types 

This module contains a collection of IOS\-XR derived YANG data 
types.
    
Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class EncryptionType_Enum(Enum):
    """
    EncryptionType_Enum

    The type of encryption used on a password string.

    """

    """

    The password string is clear text.

    """
    NONE = 0

    """

    The password is encrypted to an MD5 digest.

    """
    MD5 = 1

    """

    The password is encrypted using Cisco type 7 
    password encryption.

    """
    PROPRIETARY = 2


    @staticmethod
    def _meta_info():
        from ydk.models.types._meta import _Cisco_IOS_XR_types as meta
        return meta._meta_table['EncryptionType_Enum']



