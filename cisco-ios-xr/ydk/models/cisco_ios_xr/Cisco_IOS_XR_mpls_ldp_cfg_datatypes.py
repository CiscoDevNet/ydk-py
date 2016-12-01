""" Cisco_IOS_XR_mpls_ldp_cfg_datatypes 

This module contains a collection of YANG definitions
for Cisco IOS\-XR mpls\-ldp\-cfg\-datat package configuration.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class MplsLdpDownstreamOnDemandEnum(Enum):
    """
    MplsLdpDownstreamOnDemandEnum

    Mpls ldp downstream on demand

    .. data:: peer_acl = 1

    	Downstream on Demand peers permitted by ACL

    """

    peer_acl = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg_datatypes as meta
        return meta._meta_table['MplsLdpDownstreamOnDemandEnum']


class MplsLdpNbrPasswordEnum(Enum):
    """
    MplsLdpNbrPasswordEnum

    Mpls ldp nbr password

    .. data:: disable = 1

    	Disable the global default password for this

    	neighbor

    .. data:: specified = 2

    	Specify a password for this neighbor

    """

    disable = 1

    specified = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg_datatypes as meta
        return meta._meta_table['MplsLdpNbrPasswordEnum']


class MplsLdpRouterIdEnum(Enum):
    """
    MplsLdpRouterIdEnum

    Mpls ldp router id

    .. data:: address = 1

    	Use given IP address as LDP Router ID

    """

    address = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg_datatypes as meta
        return meta._meta_table['MplsLdpRouterIdEnum']


class MplsLdpSessionProtectionEnum(Enum):
    """
    MplsLdpSessionProtectionEnum

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

    all = 1

    for_ = 2

    all_with_duration = 3

    for_with_duration = 4

    all_with_forever = 5

    for_with_forever = 6


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg_datatypes as meta
        return meta._meta_table['MplsLdpSessionProtectionEnum']


class MplsLdpafNameEnum(Enum):
    """
    MplsLdpafNameEnum

    Mpls ldpaf name

    .. data:: ipv4 = 4

    	IPv4

    .. data:: ipv6 = 6

    	IPv6

    """

    ipv4 = 4

    ipv6 = 6


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg_datatypes as meta
        return meta._meta_table['MplsLdpafNameEnum']



