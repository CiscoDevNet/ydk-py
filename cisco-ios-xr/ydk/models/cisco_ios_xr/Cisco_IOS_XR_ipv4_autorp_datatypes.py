""" Cisco_IOS_XR_ipv4_autorp_datatypes 

This module contains a collection of generally useful
derived YANG data types.

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class AutoRpProtocolMode(Enum):
    """
    AutoRpProtocolMode (Enum Class)

    Auto rp protocol mode

    .. data:: sparse = 0

    	Sparse Mode

    .. data:: bidirectional = 1

    	Bidirectional Mode

    """

    sparse = Enum.YLeaf(0, "sparse")

    bidirectional = Enum.YLeaf(1, "bidirectional")



