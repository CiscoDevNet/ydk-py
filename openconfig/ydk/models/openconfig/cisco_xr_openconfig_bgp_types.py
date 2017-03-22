""" cisco_xr_openconfig_bgp_types 

This model maintains data items defined in the Openconfig 
bgp types yang file revision 2.1.1 untill it is 
supported by Cisco, as these data items are needed by 
openconfig\-local\-routing YANG model

Copyright (c) 2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class BgpOriginAttrTypeEnum(Enum):
    """
    BgpOriginAttrTypeEnum

    Type definition for standard BGP origin attribute

    .. data:: IGP = 0

    	Origin of the NLRI is internal

    .. data:: EGP = 1

    	Origin of the NLRI is EGP

    .. data:: INCOMPLETE = 2

    	Origin of the NLRI is neither IGP or EGP

    """

    IGP = 0

    EGP = 1

    INCOMPLETE = 2


    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _cisco_xr_openconfig_bgp_types as meta
        return meta._meta_table['BgpOriginAttrTypeEnum']



class Afi_Safi_TypeIdentity(object):
    """
    Base identity type for AFI,SAFI tuples for BGP\-4
    
    

    """

    _prefix = 'cisco-oc-bgp-types'
    _revision = '2016-11-01'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _cisco_xr_openconfig_bgp_types as meta
        return meta._meta_table['Afi_Safi_TypeIdentity']['meta_info']


class Ipv6_UnicastIdentity(Afi_Safi_TypeIdentity):
    """
    IPv6 unicast (AFI,SAFI = 2,1)
    
    

    """

    _prefix = 'cisco-oc-bgp-types'
    _revision = '2016-11-01'

    def __init__(self):
        Afi_Safi_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _cisco_xr_openconfig_bgp_types as meta
        return meta._meta_table['Ipv6_UnicastIdentity']['meta_info']


class Ipv4_UnicastIdentity(Afi_Safi_TypeIdentity):
    """
    IPv4 unicast (AFI,SAFI = 1,1)
    
    

    """

    _prefix = 'cisco-oc-bgp-types'
    _revision = '2016-11-01'

    def __init__(self):
        Afi_Safi_TypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _cisco_xr_openconfig_bgp_types as meta
        return meta._meta_table['Ipv4_UnicastIdentity']['meta_info']


