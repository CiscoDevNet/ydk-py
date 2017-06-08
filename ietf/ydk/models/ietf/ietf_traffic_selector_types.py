""" ietf_traffic_selector_types 

This module contains a collection of YANG definitions for
traffic selectors for flow bindings.

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




class TrafficSelectorFormatIdentity(object):
    """
    The base type for Traffic\-Selector Formats
    
    

    """

    _prefix = 'traffic-selectors'
    _revision = '2016-01-14'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_traffic_selector_types as meta
        return meta._meta_table['TrafficSelectorFormatIdentity']['meta_info']


class Ipv4BinarySelectorFormatIdentity(TrafficSelectorFormatIdentity):
    """
    IPv4 Binary Traffic Selector Format
    
    

    """

    _prefix = 'traffic-selectors'
    _revision = '2016-01-14'

    def __init__(self):
        TrafficSelectorFormatIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_traffic_selector_types as meta
        return meta._meta_table['Ipv4BinarySelectorFormatIdentity']['meta_info']


class Ipv6BinarySelectorFormatIdentity(TrafficSelectorFormatIdentity):
    """
    IPv6 Binary Traffic Selector Format
    
    

    """

    _prefix = 'traffic-selectors'
    _revision = '2016-01-14'

    def __init__(self):
        TrafficSelectorFormatIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_traffic_selector_types as meta
        return meta._meta_table['Ipv6BinarySelectorFormatIdentity']['meta_info']


