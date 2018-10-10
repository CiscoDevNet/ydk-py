""" Cisco_IOS_XR_aaa_locald_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR aaa\-locald package configuration.

This YANG module augments the
  Cisco\-IOS\-XR\-aaa\-lib\-cfg
module with configuration data.

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class AaaLocaldTaskClass(Enum):
    """
    AaaLocaldTaskClass (Enum Class)

    Aaa locald task class

    .. data:: read = 0

    	Permits read operation for a Task ID

    .. data:: write = 1

    	Permits write operation for a Task ID

    .. data:: execute = 2

    	Permits execute operation for a Task ID

    .. data:: debug = 3

    	Permits debug operation for a Task ID

    """

    read = Enum.YLeaf(0, "read")

    write = Enum.YLeaf(1, "write")

    execute = Enum.YLeaf(2, "execute")

    debug = Enum.YLeaf(3, "debug")



