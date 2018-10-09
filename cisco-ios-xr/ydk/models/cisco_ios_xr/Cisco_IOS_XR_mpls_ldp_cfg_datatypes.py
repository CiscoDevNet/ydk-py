""" Cisco_IOS_XR_mpls_ldp_cfg_datatypes 

This module contains a collection of YANG definitions
for Cisco IOS\-XR mpls\-ldp\-cfg\-datat package configuration.

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class MplsLdpDownstreamOnDemand(Enum):
    """
    MplsLdpDownstreamOnDemand (Enum Class)

    Mpls ldp downstream on demand

    .. data:: peer_acl = 1

    	Downstream on Demand peers permitted by ACL

    """

    peer_acl = Enum.YLeaf(1, "peer-acl")


class MplsLdpNbrPassword(Enum):
    """
    MplsLdpNbrPassword (Enum Class)

    Mpls ldp nbr password

    .. data:: disable = 1

    	Disable the global default password for this

    	neighbor

    .. data:: specified = 2

    	Specify a password for this neighbor

    """

    disable = Enum.YLeaf(1, "disable")

    specified = Enum.YLeaf(2, "specified")


class MplsLdpRouterId(Enum):
    """
    MplsLdpRouterId (Enum Class)

    Mpls ldp router id

    .. data:: address = 1

    	Use given IP address as LDP Router ID

    """

    address = Enum.YLeaf(1, "address")


class MplsLdpSessionProtection(Enum):
    """
    MplsLdpSessionProtection (Enum Class)

    Mpls ldp session protection

    .. data:: all = 1

    	Protect all peer sessions

    .. data:: for_ = 2

    	Protect peer session(s) permitted by peer ACL

    .. data:: all_with_duration = 3

    	Protect all peer sessions and holdup protection

    	for given duration

    .. data:: for_with_duration = 4

    	Protect peer session(s) permitted by peer ACL

    	and holdup protection for given duration

    .. data:: all_with_forever = 5

    	Protect all peer sessions and holdup protection

    	forever

    .. data:: for_with_forever = 6

    	Protect peer session(s) permitted by peer ACL

    	and holdup protection forever

    """

    all = Enum.YLeaf(1, "all")

    for_ = Enum.YLeaf(2, "for")

    all_with_duration = Enum.YLeaf(3, "all-with-duration")

    for_with_duration = Enum.YLeaf(4, "for-with-duration")

    all_with_forever = Enum.YLeaf(5, "all-with-forever")

    for_with_forever = Enum.YLeaf(6, "for-with-forever")


class MplsLdpafName(Enum):
    """
    MplsLdpafName (Enum Class)

    Mpls ldpaf name

    .. data:: ipv4 = 4

    	IPv4

    .. data:: ipv6 = 6

    	IPv6

    """

    ipv4 = Enum.YLeaf(4, "ipv4")

    ipv6 = Enum.YLeaf(6, "ipv6")



