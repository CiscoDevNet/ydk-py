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



class MplsLdpDownstreamOnDemand_Enum(Enum):
    """
    MplsLdpDownstreamOnDemand_Enum

    Mpls ldp downstream on demand

    """

    """

    Downstream on Demand peers permitted by ACL

    """
    PEER_ACL = 1


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_ldp_cfg_datatypes as meta
        return meta._meta_table['MplsLdpDownstreamOnDemand_Enum']


class MplsLdpNbrPassword_Enum(Enum):
    """
    MplsLdpNbrPassword_Enum

    Mpls ldp nbr password

    """

    """

    Disable the global default password for this
    neighbor

    """
    DISABLE = 1

    """

    Specify a password for this neighbor

    """
    SPECIFIED = 2


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_ldp_cfg_datatypes as meta
        return meta._meta_table['MplsLdpNbrPassword_Enum']


class MplsLdpRouterId_Enum(Enum):
    """
    MplsLdpRouterId_Enum

    Mpls ldp router id

    """

    """

    Use given IP address as LDP Router ID

    """
    ADDRESS = 1


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_ldp_cfg_datatypes as meta
        return meta._meta_table['MplsLdpRouterId_Enum']


class MplsLdpSessionProtection_Enum(Enum):
    """
    MplsLdpSessionProtection_Enum

    Mpls ldp session protection

    """

    """

    Protect all peer sessions

    """
    ALL = 1

    """

    Protect peer session(s) permitted by peer ACL

    """
    FOR = 2

    """

    Protect all peer sessions and holdup protection
    for given duration

    """
    ALL_WITH_DURATION = 3

    """

    Protect peer session(s) permitted by peer ACL
    and holdup protection for given duration

    """
    FOR_WITH_DURATION = 4

    """

    Protect all peer sessions and holdup protection
    forever

    """
    ALL_WITH_FOREVER = 5

    """

    Protect peer session(s) permitted by peer ACL
    and holdup protection forever

    """
    FOR_WITH_FOREVER = 6


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_ldp_cfg_datatypes as meta
        return meta._meta_table['MplsLdpSessionProtection_Enum']


class MplsLdpafName_Enum(Enum):
    """
    MplsLdpafName_Enum

    Mpls ldpaf name

    """

    """

    IPv4

    """
    IPV4 = 4

    """

    IPv6

    """
    IPV6 = 6


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_ldp_cfg_datatypes as meta
        return meta._meta_table['MplsLdpafName_Enum']



