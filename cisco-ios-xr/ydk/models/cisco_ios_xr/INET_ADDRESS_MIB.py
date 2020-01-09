""" INET_ADDRESS_MIB 

This module contains definitions
for the Calvados model objects.

Copyright (c) 2012\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class InetAddressType(Enum):
    """
    InetAddressType (Enum Class)

    .. data:: unknown = 0

    .. data:: ipv4 = 1

    .. data:: ipv6 = 2

    .. data:: ipv4z = 3

    .. data:: ipv6z = 4

    .. data:: dns = 16

    """

    unknown = Enum.YLeaf(0, "unknown")

    ipv4 = Enum.YLeaf(1, "ipv4")

    ipv6 = Enum.YLeaf(2, "ipv6")

    ipv4z = Enum.YLeaf(3, "ipv4z")

    ipv6z = Enum.YLeaf(4, "ipv6z")

    dns = Enum.YLeaf(16, "dns")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _INET_ADDRESS_MIB as meta
        return meta._meta_table['InetAddressType']


class InetScopeType(Enum):
    """
    InetScopeType (Enum Class)

    .. data:: interfaceLocal = 1

    .. data:: linkLocal = 2

    .. data:: subnetLocal = 3

    .. data:: adminLocal = 4

    .. data:: siteLocal = 5

    .. data:: organizationLocal = 8

    .. data:: global_ = 14

    """

    interfaceLocal = Enum.YLeaf(1, "interfaceLocal")

    linkLocal = Enum.YLeaf(2, "linkLocal")

    subnetLocal = Enum.YLeaf(3, "subnetLocal")

    adminLocal = Enum.YLeaf(4, "adminLocal")

    siteLocal = Enum.YLeaf(5, "siteLocal")

    organizationLocal = Enum.YLeaf(8, "organizationLocal")

    global_ = Enum.YLeaf(14, "global")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _INET_ADDRESS_MIB as meta
        return meta._meta_table['InetScopeType']


class InetVersion(Enum):
    """
    InetVersion (Enum Class)

    .. data:: unknown = 0

    .. data:: ipv4 = 1

    .. data:: ipv6 = 2

    """

    unknown = Enum.YLeaf(0, "unknown")

    ipv4 = Enum.YLeaf(1, "ipv4")

    ipv6 = Enum.YLeaf(2, "ipv6")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _INET_ADDRESS_MIB as meta
        return meta._meta_table['InetVersion']



