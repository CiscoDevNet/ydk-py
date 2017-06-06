""" openconfig_rib_bgp_types 

Defines identity and type defintions associated with
the OpenConfig BGP RIB modules

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class Bgp_Not_Selected_BestpathIdentity(object):
    """
    Base identity for indicating reason a route was was not
    selected by BGP route selection algorithm
    
    

    """

    _prefix = 'oc-bgprib-types'
    _revision = '2016-04-11'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_rib_bgp_types as meta
        return meta._meta_table['Bgp_Not_Selected_BestpathIdentity']['meta_info']


class Invalid_Route_ReasonIdentity(object):
    """
    Base identity for reason code for routes that are rejected as
    invalid.  Some derived entities are based on BMP v3
    
    

    """

    _prefix = 'oc-bgprib-types'
    _revision = '2016-04-11'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_rib_bgp_types as meta
        return meta._meta_table['Invalid_Route_ReasonIdentity']['meta_info']


class Bgp_Not_Selected_PolicyIdentity(object):
    """
    Base identity for reason code for routes that are rejected
    due to policy
    
    

    """

    _prefix = 'oc-bgprib-types'
    _revision = '2016-04-11'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_rib_bgp_types as meta
        return meta._meta_table['Bgp_Not_Selected_PolicyIdentity']['meta_info']


class Nexthop_Cost_HigherIdentity(Bgp_Not_Selected_BestpathIdentity):
    """
    Route has a higher interior cost to the next hop.
    
    

    """

    _prefix = 'oc-bgprib-types'
    _revision = '2016-04-11'

    def __init__(self):
        Bgp_Not_Selected_BestpathIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_rib_bgp_types as meta
        return meta._meta_table['Nexthop_Cost_HigherIdentity']['meta_info']


class Invalid_As_LoopIdentity(Invalid_Route_ReasonIdentity):
    """
    Route was invalid due to AS\_PATH loop
    
    

    """

    _prefix = 'oc-bgprib-types'
    _revision = '2016-04-11'

    def __init__(self):
        Invalid_Route_ReasonIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_rib_bgp_types as meta
        return meta._meta_table['Invalid_As_LoopIdentity']['meta_info']


class Invalid_ConfedIdentity(Invalid_Route_ReasonIdentity):
    """
    Route was invalid due to a loop in the AS\_CONFED\_SEQUENCE or
    AS\_CONFED\_SET attributes
    
    

    """

    _prefix = 'oc-bgprib-types'
    _revision = '2016-04-11'

    def __init__(self):
        Invalid_Route_ReasonIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_rib_bgp_types as meta
        return meta._meta_table['Invalid_ConfedIdentity']['meta_info']


class Invalid_OriginatorIdentity(Invalid_Route_ReasonIdentity):
    """
    Route was invalid due to ORIGINATOR\_ID, e.g., update has
    local router as originator
    
    

    """

    _prefix = 'oc-bgprib-types'
    _revision = '2016-04-11'

    def __init__(self):
        Invalid_Route_ReasonIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_rib_bgp_types as meta
        return meta._meta_table['Invalid_OriginatorIdentity']['meta_info']


class Local_Pref_LowerIdentity(Bgp_Not_Selected_BestpathIdentity):
    """
    Route has a lower localpref attribute than current best path
    
    

    """

    _prefix = 'oc-bgprib-types'
    _revision = '2016-04-11'

    def __init__(self):
        Bgp_Not_Selected_BestpathIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_rib_bgp_types as meta
        return meta._meta_table['Local_Pref_LowerIdentity']['meta_info']


class Higher_Router_IdIdentity(Bgp_Not_Selected_BestpathIdentity):
    """
    Route was sent by a peer with a higher BGP Identifier value,
    or router id
    
    

    """

    _prefix = 'oc-bgprib-types'
    _revision = '2016-04-11'

    def __init__(self):
        Bgp_Not_Selected_BestpathIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_rib_bgp_types as meta
        return meta._meta_table['Higher_Router_IdIdentity']['meta_info']


class Origin_Type_HigherIdentity(Bgp_Not_Selected_BestpathIdentity):
    """
    Route has a higher origin type, i.e., IGP origin is preferred
    over EGP or incomplete
    
    

    """

    _prefix = 'oc-bgprib-types'
    _revision = '2016-04-11'

    def __init__(self):
        Bgp_Not_Selected_BestpathIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_rib_bgp_types as meta
        return meta._meta_table['Origin_Type_HigherIdentity']['meta_info']


class Higher_Peer_AddressIdentity(Bgp_Not_Selected_BestpathIdentity):
    """
    Route was sent by a peer with a higher IP address
    
    

    """

    _prefix = 'oc-bgprib-types'
    _revision = '2016-04-11'

    def __init__(self):
        Bgp_Not_Selected_BestpathIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_rib_bgp_types as meta
        return meta._meta_table['Higher_Peer_AddressIdentity']['meta_info']


class Invalid_Cluster_LoopIdentity(Invalid_Route_ReasonIdentity):
    """
    Route was invalid due to CLUSTER\_LIST loop
    
    

    """

    _prefix = 'oc-bgprib-types'
    _revision = '2016-04-11'

    def __init__(self):
        Invalid_Route_ReasonIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_rib_bgp_types as meta
        return meta._meta_table['Invalid_Cluster_LoopIdentity']['meta_info']


class As_Path_LongerIdentity(Bgp_Not_Selected_BestpathIdentity):
    """
    Route has a longer AS path attribute than current best path
    
    

    """

    _prefix = 'oc-bgprib-types'
    _revision = '2016-04-11'

    def __init__(self):
        Bgp_Not_Selected_BestpathIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_rib_bgp_types as meta
        return meta._meta_table['As_Path_LongerIdentity']['meta_info']


class Rejected_Import_PolicyIdentity(Bgp_Not_Selected_PolicyIdentity):
    """
    Route was rejected after apply import policies
    
    

    """

    _prefix = 'oc-bgprib-types'
    _revision = '2016-04-11'

    def __init__(self):
        Bgp_Not_Selected_PolicyIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_rib_bgp_types as meta
        return meta._meta_table['Rejected_Import_PolicyIdentity']['meta_info']


class Med_HigherIdentity(Bgp_Not_Selected_BestpathIdentity):
    """
    Route has a higher MED, or metric, attribute than the current
    best path
    
    

    """

    _prefix = 'oc-bgprib-types'
    _revision = '2016-04-11'

    def __init__(self):
        Bgp_Not_Selected_BestpathIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_rib_bgp_types as meta
        return meta._meta_table['Med_HigherIdentity']['meta_info']


class Prefer_ExternalIdentity(Bgp_Not_Selected_BestpathIdentity):
    """
    Route source is via IGP, rather than EGP.
    
    

    """

    _prefix = 'oc-bgprib-types'
    _revision = '2016-04-11'

    def __init__(self):
        Bgp_Not_Selected_BestpathIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_rib_bgp_types as meta
        return meta._meta_table['Prefer_ExternalIdentity']['meta_info']


