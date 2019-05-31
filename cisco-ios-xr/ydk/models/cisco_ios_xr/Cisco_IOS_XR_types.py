""" Cisco_IOS_XR_types 

This module contains a collection of IOS\-XR derived YANG data 
types.
    
Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class EncryptionType(Enum):
    """
    EncryptionType (Enum Class)

    The type of encryption used on a password string.

    .. data:: none = 0

    	The password string is clear text.

    .. data:: md5 = 1

    	The password is encrypted to an MD5 digest.

    .. data:: proprietary = 2

    	The password is encrypted using Cisco type 7 

    	password encryption.

    .. data:: type6 = 3

    	The password is encrypted using Cisco type 6 

    	password encryption.

    """

    none = Enum.YLeaf(0, "none")

    md5 = Enum.YLeaf(1, "md5")

    proprietary = Enum.YLeaf(2, "proprietary")

    type6 = Enum.YLeaf(3, "type6")



