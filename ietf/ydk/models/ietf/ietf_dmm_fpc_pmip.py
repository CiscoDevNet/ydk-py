""" ietf_dmm_fpc_pmip 

This module contains YANG definition for Forwarding Policy
Configuration Protocol (FPCP).

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
from ydk.models.ietf.ietf_dmm_fpc import FpcDescriptorTypeIdentity
from ydk.models.ietf.ietf_dmm_fpc import FpcMobilityProfileTypeIdentity
from ydk.models.ietf.ietf_dmm_fpc import FpcQosTypeIdentity

class PmipInstr(FixedBitsDict):
    """
    PmipInstr

    Instruction Set for PMIP
    Keys are:- downlink , session , assign\-dpn , uplink , assign\-ip

    """

    def __init__(self):
        self._dictionary = { 
            'downlink':False,
            'session':False,
            'assign-dpn':False,
            'uplink':False,
            'assign-ip':False,
        }
        self._pos_map = { 
            'downlink':4,
            'session':2,
            'assign-dpn':1,
            'uplink':3,
            'assign-ip':0,
        }


class FpcpQosIndexPmipIdentity(FpcQosTypeIdentity):
    """
    PMIP QoS
    
    

    """

    _prefix = 'fpc-pmip'
    _revision = '2017-03-08'

    def __init__(self):
        FpcQosTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_dmm_fpc_pmip as meta
        return meta._meta_table['FpcpQosIndexPmipIdentity']['meta_info']


class PmipTunnelTypeIdentity(object):
    """
    PMIP Tunnel Type
    
    

    """

    _prefix = 'fpc-pmip'
    _revision = '2017-03-08'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_dmm_fpc_pmip as meta
        return meta._meta_table['PmipTunnelTypeIdentity']['meta_info']


class TrafficSelectorMip6Identity(FpcDescriptorTypeIdentity):
    """
    MIP6 Traffic Selector
    
    

    """

    _prefix = 'fpc-pmip'
    _revision = '2017-03-08'

    def __init__(self):
        FpcDescriptorTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_dmm_fpc_pmip as meta
        return meta._meta_table['TrafficSelectorMip6Identity']['meta_info']


class IetfPmipAccessTypeIdentity(FpcAccessTypeIdentity):
    """
    PMIP Access
    
    

    """

    _prefix = 'fpc-pmip'
    _revision = '2017-03-08'

    def __init__(self):
        FpcAccessTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_dmm_fpc_pmip as meta
        return meta._meta_table['IetfPmipAccessTypeIdentity']['meta_info']


class IetfPmipIdentity(FpcMobilityProfileTypeIdentity):
    """
    PMIP Mobility
    
    

    """

    _prefix = 'fpc-pmip'
    _revision = '2017-03-08'

    def __init__(self):
        FpcMobilityProfileTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_dmm_fpc_pmip as meta
        return meta._meta_table['IetfPmipIdentity']['meta_info']


class Grev2Identity(PmipTunnelTypeIdentity):
    """
    GRE v2
    
    

    """

    _prefix = 'fpc-pmip'
    _revision = '2017-03-08'

    def __init__(self):
        PmipTunnelTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_dmm_fpc_pmip as meta
        return meta._meta_table['Grev2Identity']['meta_info']


class Grev1Identity(PmipTunnelTypeIdentity):
    """
    GRE v1
    
    

    """

    _prefix = 'fpc-pmip'
    _revision = '2017-03-08'

    def __init__(self):
        PmipTunnelTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_dmm_fpc_pmip as meta
        return meta._meta_table['Grev1Identity']['meta_info']


class IpinipIdentity(PmipTunnelTypeIdentity):
    """
    IP in IP
    
    

    """

    _prefix = 'fpc-pmip'
    _revision = '2017-03-08'

    def __init__(self):
        PmipTunnelTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_dmm_fpc_pmip as meta
        return meta._meta_table['IpinipIdentity']['meta_info']


