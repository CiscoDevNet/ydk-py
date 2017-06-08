""" ietf_nvo_vpn_types 

ietf\-nvo\-vpn\-types

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class ProtectionroleEnum(Enum):
    """
    ProtectionroleEnum

    ProtectionRole

    .. data:: NOP = 0

    	NOP

    .. data:: MAIN = 1

    	MAIN

    """

    NOP = 0

    MAIN = 1


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_nvo_vpn_types as meta
        return meta._meta_table['ProtectionroleEnum']


class ServicetypeEnum(Enum):
    """
    ServicetypeEnum

    ServiceType

    .. data:: l3vpn = 0

    	l3vpn

    .. data:: l2vpn = 1

    	l2vpn

    """

    l3vpn = 0

    l2vpn = 1


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_nvo_vpn_types as meta
        return meta._meta_table['ServicetypeEnum']


class VpntunneltypeEnum(Enum):
    """
    VpntunneltypeEnum

    VPNTunnelType

    .. data:: NOP = 0

    	NOP

    .. data:: MPLS = 1

    	MPLS

    .. data:: MPLS_TP = 2

    	MPLS-TP

    """

    NOP = 0

    MPLS = 1

    MPLS_TP = 2


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_nvo_vpn_types as meta
        return meta._meta_table['VpntunneltypeEnum']



