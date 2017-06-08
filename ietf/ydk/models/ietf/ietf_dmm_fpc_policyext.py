""" ietf_dmm_fpc_policyext 

This module contains YANG definition for Forwarding Policy
Configuration Protocol (FPCP) common Policy Action and
Descriptor extensions.

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


from ydk.models.ietf.ietf_dmm_fpc import FpcDescriptorTypeIdentity


class ServiceFunctionIdentity(FpcDescriptorTypeIdentity):
    """
    Base Identifier for Service Functions.
    
    

    """

    _prefix = 'fpcpolicyext'
    _revision = '2017-03-08'

    def __init__(self):
        FpcDescriptorTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_dmm_fpc_policyext as meta
        return meta._meta_table['ServiceFunctionIdentity']['meta_info']


class CopyForwardIdentity(FpcDescriptorTypeIdentity):
    """
    Copies a packet then forwards to a specific
    destination
    
    

    """

    _prefix = 'fpcpolicyext'
    _revision = '2017-03-08'

    def __init__(self):
        FpcDescriptorTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_dmm_fpc_policyext as meta
        return meta._meta_table['CopyForwardIdentity']['meta_info']


class NatServiceIdentity(ServiceFunctionIdentity):
    """
    NAT Service
    
    

    """

    _prefix = 'fpcpolicyext'
    _revision = '2017-03-08'

    def __init__(self):
        ServiceFunctionIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_dmm_fpc_policyext as meta
        return meta._meta_table['NatServiceIdentity']['meta_info']


class NaptServiceIdentity(ServiceFunctionIdentity):
    """
    NAPT Service
    
    

    """

    _prefix = 'fpcpolicyext'
    _revision = '2017-03-08'

    def __init__(self):
        ServiceFunctionIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_dmm_fpc_policyext as meta
        return meta._meta_table['NaptServiceIdentity']['meta_info']


