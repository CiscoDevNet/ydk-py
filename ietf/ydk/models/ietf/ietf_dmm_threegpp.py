""" ietf_dmm_threegpp 

This module contains YANG definition for 3GPP Related Mobility
Structures.

Copyright (c) 2016 IETF Trust and the persons identified as the
document authors. All rights reserved.

This document is subject to BCP 78 and the IETF Trust's Legal
Provisions Relating to IETF Documents
(http\://trustee.ietf.org/license\-info) in effect on the date of
publication of this document. Please review these documents
carefully, as they describe your rights and restrictions with
respect to this document. Code Components extracted from this
document must include Simplified BSD License text as described
in Section 4.e of the Trust Legal Provisions and are provided
without warranty as described in the Simplified BSD License.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError


from ydk.models.ietf.ietf_dmm_fpc import FpcAccessTypeIdentity
from ydk.models.ietf.ietf_dmm_fpc import FpcMobilityProfileTypeIdentity
from ydk.models.ietf.ietf_dmm_fpc import FpcQosTypeIdentity

class ComponentTypeEnumEnum(Enum):
    """
    ComponentTypeEnumEnum

    TFT Component Type

    .. data:: ipv4RemoteAddress = 16

    	IPv4 Remote Address

    .. data:: ipv4LocalAddress = 17

    	IPv4 Local Address

    .. data:: ipv6RemoteAddress = 32

    	IPv6 Remote Address

    .. data:: ipv6RemoteAddressPrefix = 33

    	IPv6 Remote Address Prefix

    .. data:: ipv6LocalAddressPrefix = 35

    	IPv6 Local Address Prefix

    .. data:: protocolNextHeader = 48

    	Protocol (IPv4) or NextHeader (IPv6)

    	value

    .. data:: localPort = 64

    	Local Port

    .. data:: localPortRange = 65

    	Local Port Range

    .. data:: reomotePort = 80

    	Remote Port

    .. data:: remotePortRange = 81

    	Remote Port Range

    .. data:: secParamIndex = 96

    	Security Parameter Index (SPI)

    .. data:: tosTraffClass = 112

    	TOS Traffic Class

    .. data:: flowLabel = 128

    	Flow Label

    """

    ipv4RemoteAddress = 16

    ipv4LocalAddress = 17

    ipv6RemoteAddress = 32

    ipv6RemoteAddressPrefix = 33

    ipv6LocalAddressPrefix = 35

    protocolNextHeader = 48

    localPort = 64

    localPortRange = 65

    reomotePort = 80

    remotePortRange = 81

    secParamIndex = 96

    tosTraffClass = 112

    flowLabel = 128


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_dmm_threegpp as meta
        return meta._meta_table['ComponentTypeEnumEnum']


class PacketFilterDirectionEnum(Enum):
    """
    PacketFilterDirectionEnum

    Packet Filter Direction

    .. data:: preRel7Tft = 0

    	Pre-Release 7 TFT

    .. data:: uplink = 1

    	uplink

    .. data:: downlink = 2

    	downlink

    .. data:: bidirectional = 3

    	bi-direcitonal

    """

    preRel7Tft = 0

    uplink = 1

    downlink = 2

    bidirectional = 3


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_dmm_threegpp as meta
        return meta._meta_table['PacketFilterDirectionEnum']


class ThreegppInstr(FixedBitsDict):
    """
    ThreegppInstr

    Instruction Set for 3GPP R11
    Keys are:- assign\-fteid\-ip , assign\-dpn , downlink , assign\-fteid\-teid , session , assign\-ip , uplink

    """

    def __init__(self):
        self._dictionary = { 
            'assign-fteid-ip':False,
            'assign-dpn':False,
            'downlink':False,
            'assign-fteid-teid':False,
            'session':False,
            'assign-ip':False,
            'uplink':False,
        }
        self._pos_map = { 
            'assign-fteid-ip':1,
            'assign-dpn':6,
            'downlink':5,
            'assign-fteid-teid':2,
            'session':3,
            'assign-ip':0,
            'uplink':4,
        }


class ThreegppMobilityIdentity(FpcMobilityProfileTypeIdentity):
    """
    3GPP Mobility Profile
    
    

    """

    _prefix = 'threegpp'
    _revision = '2017-03-08'

    def __init__(self):
        FpcMobilityProfileTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_dmm_threegpp as meta
        return meta._meta_table['ThreegppMobilityIdentity']['meta_info']


class ThreegppQosProfileParametersIdentity(FpcQosTypeIdentity):
    """
    3GPP QoS Profile
    
    

    """

    _prefix = 'threegpp'
    _revision = '2017-03-08'

    def __init__(self):
        FpcQosTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_dmm_threegpp as meta
        return meta._meta_table['ThreegppQosProfileParametersIdentity']['meta_info']


class ThreegppTunnelTypeIdentity(object):
    """
    3GPP Base Tunnel Type
    
    

    """

    _prefix = 'threegpp'
    _revision = '2017-03-08'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_dmm_threegpp as meta
        return meta._meta_table['ThreegppTunnelTypeIdentity']['meta_info']


class ThreegppAccessTypeIdentity(FpcAccessTypeIdentity):
    """
    3GPP Access Type
    
    

    """

    _prefix = 'threegpp'
    _revision = '2017-03-08'

    def __init__(self):
        FpcAccessTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_dmm_threegpp as meta
        return meta._meta_table['ThreegppAccessTypeIdentity']['meta_info']


class Gtpv1Identity(ThreegppTunnelTypeIdentity):
    """
    GTP version 1 Tunnel
    
    

    """

    _prefix = 'threegpp'
    _revision = '2017-03-08'

    def __init__(self):
        ThreegppTunnelTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_dmm_threegpp as meta
        return meta._meta_table['Gtpv1Identity']['meta_info']


class Gtpv2Identity(ThreegppTunnelTypeIdentity):
    """
    GTP version 2 Tunnel
    
    

    """

    _prefix = 'threegpp'
    _revision = '2017-03-08'

    def __init__(self):
        ThreegppTunnelTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_dmm_threegpp as meta
        return meta._meta_table['Gtpv2Identity']['meta_info']


