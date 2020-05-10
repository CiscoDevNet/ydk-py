""" openconfig_rib_bgp_types 

Defines identity and type defintions associated with
the OpenConfig BGP RIB modules

"""
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class INVALIDROUTEREASON(Identity):
    """
    Base identity for reason code for routes that are rejected as
    invalid.  Some derived entities are based on BMP v3
    
    

    """

    _prefix = 'oc-bgprib-types'
    _revision = '2016-04-11'

    def __init__(self, ns="http://openconfig.net/yang/rib/bgp-types", pref="openconfig-rib-bgp-types", tag="openconfig-rib-bgp-types:INVALID_ROUTE_REASON"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(INVALIDROUTEREASON, self).__init__(ns, pref, tag)



class BGPNOTSELECTEDBESTPATH(Identity):
    """
    Base identity for indicating reason a route was was not
    selected by BGP route selection algorithm
    
    

    """

    _prefix = 'oc-bgprib-types'
    _revision = '2016-04-11'

    def __init__(self, ns="http://openconfig.net/yang/rib/bgp-types", pref="openconfig-rib-bgp-types", tag="openconfig-rib-bgp-types:BGP_NOT_SELECTED_BESTPATH"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(BGPNOTSELECTEDBESTPATH, self).__init__(ns, pref, tag)



class BGPNOTSELECTEDPOLICY(Identity):
    """
    Base identity for reason code for routes that are rejected
    due to policy
    
    

    """

    _prefix = 'oc-bgprib-types'
    _revision = '2016-04-11'

    def __init__(self, ns="http://openconfig.net/yang/rib/bgp-types", pref="openconfig-rib-bgp-types", tag="openconfig-rib-bgp-types:BGP_NOT_SELECTED_POLICY"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(BGPNOTSELECTEDPOLICY, self).__init__(ns, pref, tag)



class INVALIDCLUSTERLOOP(INVALIDROUTEREASON):
    """
    Route was invalid due to CLUSTER\_LIST loop
    
    

    """

    _prefix = 'oc-bgprib-types'
    _revision = '2016-04-11'

    def __init__(self, ns="http://openconfig.net/yang/rib/bgp-types", pref="openconfig-rib-bgp-types", tag="openconfig-rib-bgp-types:INVALID_CLUSTER_LOOP"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(INVALIDCLUSTERLOOP, self).__init__(ns, pref, tag)



class INVALIDASLOOP(INVALIDROUTEREASON):
    """
    Route was invalid due to AS\_PATH loop
    
    

    """

    _prefix = 'oc-bgprib-types'
    _revision = '2016-04-11'

    def __init__(self, ns="http://openconfig.net/yang/rib/bgp-types", pref="openconfig-rib-bgp-types", tag="openconfig-rib-bgp-types:INVALID_AS_LOOP"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(INVALIDASLOOP, self).__init__(ns, pref, tag)



class INVALIDORIGINATOR(INVALIDROUTEREASON):
    """
    Route was invalid due to ORIGINATOR\_ID, e.g., update has
    local router as originator
    
    

    """

    _prefix = 'oc-bgprib-types'
    _revision = '2016-04-11'

    def __init__(self, ns="http://openconfig.net/yang/rib/bgp-types", pref="openconfig-rib-bgp-types", tag="openconfig-rib-bgp-types:INVALID_ORIGINATOR"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(INVALIDORIGINATOR, self).__init__(ns, pref, tag)



class INVALIDCONFED(INVALIDROUTEREASON):
    """
    Route was invalid due to a loop in the AS\_CONFED\_SEQUENCE or
    AS\_CONFED\_SET attributes
    
    

    """

    _prefix = 'oc-bgprib-types'
    _revision = '2016-04-11'

    def __init__(self, ns="http://openconfig.net/yang/rib/bgp-types", pref="openconfig-rib-bgp-types", tag="openconfig-rib-bgp-types:INVALID_CONFED"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(INVALIDCONFED, self).__init__(ns, pref, tag)



class LOCALPREFLOWER(BGPNOTSELECTEDBESTPATH):
    """
    Route has a lower localpref attribute than current best path
    
    

    """

    _prefix = 'oc-bgprib-types'
    _revision = '2016-04-11'

    def __init__(self, ns="http://openconfig.net/yang/rib/bgp-types", pref="openconfig-rib-bgp-types", tag="openconfig-rib-bgp-types:LOCAL_PREF_LOWER"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(LOCALPREFLOWER, self).__init__(ns, pref, tag)



class ASPATHLONGER(BGPNOTSELECTEDBESTPATH):
    """
    Route has a longer AS path attribute than current best path
    
    

    """

    _prefix = 'oc-bgprib-types'
    _revision = '2016-04-11'

    def __init__(self, ns="http://openconfig.net/yang/rib/bgp-types", pref="openconfig-rib-bgp-types", tag="openconfig-rib-bgp-types:AS_PATH_LONGER"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(ASPATHLONGER, self).__init__(ns, pref, tag)



class ORIGINTYPEHIGHER(BGPNOTSELECTEDBESTPATH):
    """
    Route has a higher origin type, i.e., IGP origin is preferred
    over EGP or incomplete
    
    

    """

    _prefix = 'oc-bgprib-types'
    _revision = '2016-04-11'

    def __init__(self, ns="http://openconfig.net/yang/rib/bgp-types", pref="openconfig-rib-bgp-types", tag="openconfig-rib-bgp-types:ORIGIN_TYPE_HIGHER"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(ORIGINTYPEHIGHER, self).__init__(ns, pref, tag)



class MEDHIGHER(BGPNOTSELECTEDBESTPATH):
    """
    Route has a higher MED, or metric, attribute than the current
    best path
    
    

    """

    _prefix = 'oc-bgprib-types'
    _revision = '2016-04-11'

    def __init__(self, ns="http://openconfig.net/yang/rib/bgp-types", pref="openconfig-rib-bgp-types", tag="openconfig-rib-bgp-types:MED_HIGHER"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(MEDHIGHER, self).__init__(ns, pref, tag)



class PREFEREXTERNAL(BGPNOTSELECTEDBESTPATH):
    """
    Route source is via IGP, rather than EGP.
    
    

    """

    _prefix = 'oc-bgprib-types'
    _revision = '2016-04-11'

    def __init__(self, ns="http://openconfig.net/yang/rib/bgp-types", pref="openconfig-rib-bgp-types", tag="openconfig-rib-bgp-types:PREFER_EXTERNAL"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(PREFEREXTERNAL, self).__init__(ns, pref, tag)



class NEXTHOPCOSTHIGHER(BGPNOTSELECTEDBESTPATH):
    """
    Route has a higher interior cost to the next hop.
    
    

    """

    _prefix = 'oc-bgprib-types'
    _revision = '2016-04-11'

    def __init__(self, ns="http://openconfig.net/yang/rib/bgp-types", pref="openconfig-rib-bgp-types", tag="openconfig-rib-bgp-types:NEXTHOP_COST_HIGHER"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(NEXTHOPCOSTHIGHER, self).__init__(ns, pref, tag)



class HIGHERROUTERID(BGPNOTSELECTEDBESTPATH):
    """
    Route was sent by a peer with a higher BGP Identifier value,
    or router id
    
    

    """

    _prefix = 'oc-bgprib-types'
    _revision = '2016-04-11'

    def __init__(self, ns="http://openconfig.net/yang/rib/bgp-types", pref="openconfig-rib-bgp-types", tag="openconfig-rib-bgp-types:HIGHER_ROUTER_ID"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(HIGHERROUTERID, self).__init__(ns, pref, tag)



class HIGHERPEERADDRESS(BGPNOTSELECTEDBESTPATH):
    """
    Route was sent by a peer with a higher IP address
    
    

    """

    _prefix = 'oc-bgprib-types'
    _revision = '2016-04-11'

    def __init__(self, ns="http://openconfig.net/yang/rib/bgp-types", pref="openconfig-rib-bgp-types", tag="openconfig-rib-bgp-types:HIGHER_PEER_ADDRESS"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(HIGHERPEERADDRESS, self).__init__(ns, pref, tag)



class REJECTEDIMPORTPOLICY(BGPNOTSELECTEDPOLICY):
    """
    Route was rejected after apply import policies
    
    

    """

    _prefix = 'oc-bgprib-types'
    _revision = '2016-04-11'

    def __init__(self, ns="http://openconfig.net/yang/rib/bgp-types", pref="openconfig-rib-bgp-types", tag="openconfig-rib-bgp-types:REJECTED_IMPORT_POLICY"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(REJECTEDIMPORTPOLICY, self).__init__(ns, pref, tag)



