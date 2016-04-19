""" Cisco_IOS_XR_mpls_ldp_cfg_datatypes 

This module contains a collection of YANG definitions
for Cisco IOS\-XR mpls\-ldp\-cfg\-datat package configuration.

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class MplsLdpDownstreamOnDemandEnum(Enum):
    """
    MplsLdpDownstreamOnDemandEnum

    Mpls ldp downstream on demand

    .. data:: PEER_ACL = 1

    	Downstream on Demand peers permitted by ACL

    """

    PEER_ACL = 1


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_ldp_cfg_datatypes as meta
        return meta._meta_table['MplsLdpDownstreamOnDemandEnum']


class MplsLdpNbrPasswordEnum(Enum):
    """
    MplsLdpNbrPasswordEnum

    Mpls ldp nbr password

    .. data:: DISABLE = 1

    	Disable the global default password for this

    	neighbor

    .. data:: SPECIFIED = 2

    	Specify a password for this neighbor

    """

    DISABLE = 1

    SPECIFIED = 2


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_ldp_cfg_datatypes as meta
        return meta._meta_table['MplsLdpNbrPasswordEnum']


class MplsLdpRouterIdEnum(Enum):
    """
    MplsLdpRouterIdEnum

    Mpls ldp router id

    .. data:: ADDRESS = 1

    	Use given IP address as LDP Router ID

    """

    ADDRESS = 1


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_ldp_cfg_datatypes as meta
        return meta._meta_table['MplsLdpRouterIdEnum']


class MplsLdpSessionProtectionEnum(Enum):
    """
    MplsLdpSessionProtectionEnum

    Mpls ldp session protection

    .. data:: ALL = 1

    	Protect all peer sessions

    .. data:: FOR = 2

    	Protect peer session(s) permitted by peer ACL

    .. data:: ALL_WITH_DURATION = 3

    	Protect all peer sessions and holdup protection

    	for given duration

    .. data:: FOR_WITH_DURATION = 4

    	Protect peer session(s) permitted by peer ACL

    	and holdup protection for given duration

    .. data:: ALL_WITH_FOREVER = 5

    	Protect all peer sessions and holdup protection

    	forever

    .. data:: FOR_WITH_FOREVER = 6

    	Protect peer session(s) permitted by peer ACL

    	and holdup protection forever

    """

    ALL = 1

    FOR = 2

    ALL_WITH_DURATION = 3

    FOR_WITH_DURATION = 4

    ALL_WITH_FOREVER = 5

    FOR_WITH_FOREVER = 6


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_ldp_cfg_datatypes as meta
        return meta._meta_table['MplsLdpSessionProtectionEnum']


class MplsLdpafNameEnum(Enum):
    """
    MplsLdpafNameEnum

    Mpls ldpaf name

    .. data:: IPV4 = 4

    	IPv4

    .. data:: IPV6 = 6

    	IPv6

    """

    IPV4 = 4

    IPV6 = 6


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_ldp_cfg_datatypes as meta
        return meta._meta_table['MplsLdpafNameEnum']



