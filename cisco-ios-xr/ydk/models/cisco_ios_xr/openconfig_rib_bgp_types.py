""" openconfig_rib_bgp_types 

Defines identity and type defintions associated with
the OpenConfig BGP RIB modules

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Bgp_Not_Selected_Policy(Identity):
    """
    Base identity for reason code for routes that are rejected
    due to policy
    
    

    """

    _prefix = 'oc-bgprib-types'
    _revision = '2016-04-11'

    def __init__(self):
        super(Bgp_Not_Selected_Policy, self).__init__("http://openconfig.net/yang/rib/bgp-types", "openconfig-rib-bgp-types", "openconfig-rib-bgp-types:BGP_NOT_SELECTED_POLICY")


class Invalid_Route_Reason(Identity):
    """
    Base identity for reason code for routes that are rejected as
    invalid.  Some derived entities are based on BMP v3
    
    

    """

    _prefix = 'oc-bgprib-types'
    _revision = '2016-04-11'

    def __init__(self):
        super(Invalid_Route_Reason, self).__init__("http://openconfig.net/yang/rib/bgp-types", "openconfig-rib-bgp-types", "openconfig-rib-bgp-types:INVALID_ROUTE_REASON")


class Bgp_Not_Selected_Bestpath(Identity):
    """
    Base identity for indicating reason a route was was not
    selected by BGP route selection algorithm
    
    

    """

    _prefix = 'oc-bgprib-types'
    _revision = '2016-04-11'

    def __init__(self):
        super(Bgp_Not_Selected_Bestpath, self).__init__("http://openconfig.net/yang/rib/bgp-types", "openconfig-rib-bgp-types", "openconfig-rib-bgp-types:BGP_NOT_SELECTED_BESTPATH")


class Rejected_Import_Policy(Identity):
    """
    Route was rejected after apply import policies
    
    

    """

    _prefix = 'oc-bgprib-types'
    _revision = '2016-04-11'

    def __init__(self):
        super(Rejected_Import_Policy, self).__init__("http://openconfig.net/yang/rib/bgp-types", "openconfig-rib-bgp-types", "openconfig-rib-bgp-types:REJECTED_IMPORT_POLICY")


class Higher_Peer_Address(Identity):
    """
    Route was sent by a peer with a higher IP address
    
    

    """

    _prefix = 'oc-bgprib-types'
    _revision = '2016-04-11'

    def __init__(self):
        super(Higher_Peer_Address, self).__init__("http://openconfig.net/yang/rib/bgp-types", "openconfig-rib-bgp-types", "openconfig-rib-bgp-types:HIGHER_PEER_ADDRESS")


class Invalid_As_Loop(Identity):
    """
    Route was invalid due to AS\_PATH loop
    
    

    """

    _prefix = 'oc-bgprib-types'
    _revision = '2016-04-11'

    def __init__(self):
        super(Invalid_As_Loop, self).__init__("http://openconfig.net/yang/rib/bgp-types", "openconfig-rib-bgp-types", "openconfig-rib-bgp-types:INVALID_AS_LOOP")


class As_Path_Longer(Identity):
    """
    Route has a longer AS path attribute than current best path
    
    

    """

    _prefix = 'oc-bgprib-types'
    _revision = '2016-04-11'

    def __init__(self):
        super(As_Path_Longer, self).__init__("http://openconfig.net/yang/rib/bgp-types", "openconfig-rib-bgp-types", "openconfig-rib-bgp-types:AS_PATH_LONGER")


class Invalid_Cluster_Loop(Identity):
    """
    Route was invalid due to CLUSTER\_LIST loop
    
    

    """

    _prefix = 'oc-bgprib-types'
    _revision = '2016-04-11'

    def __init__(self):
        super(Invalid_Cluster_Loop, self).__init__("http://openconfig.net/yang/rib/bgp-types", "openconfig-rib-bgp-types", "openconfig-rib-bgp-types:INVALID_CLUSTER_LOOP")


class Invalid_Confed(Identity):
    """
    Route was invalid due to a loop in the AS\_CONFED\_SEQUENCE or
    AS\_CONFED\_SET attributes
    
    

    """

    _prefix = 'oc-bgprib-types'
    _revision = '2016-04-11'

    def __init__(self):
        super(Invalid_Confed, self).__init__("http://openconfig.net/yang/rib/bgp-types", "openconfig-rib-bgp-types", "openconfig-rib-bgp-types:INVALID_CONFED")


class Invalid_Originator(Identity):
    """
    Route was invalid due to ORIGINATOR\_ID, e.g., update has
    local router as originator
    
    

    """

    _prefix = 'oc-bgprib-types'
    _revision = '2016-04-11'

    def __init__(self):
        super(Invalid_Originator, self).__init__("http://openconfig.net/yang/rib/bgp-types", "openconfig-rib-bgp-types", "openconfig-rib-bgp-types:INVALID_ORIGINATOR")


class Local_Pref_Lower(Identity):
    """
    Route has a lower localpref attribute than current best path
    
    

    """

    _prefix = 'oc-bgprib-types'
    _revision = '2016-04-11'

    def __init__(self):
        super(Local_Pref_Lower, self).__init__("http://openconfig.net/yang/rib/bgp-types", "openconfig-rib-bgp-types", "openconfig-rib-bgp-types:LOCAL_PREF_LOWER")


class Prefer_External(Identity):
    """
    Route source is via IGP, rather than EGP.
    
    

    """

    _prefix = 'oc-bgprib-types'
    _revision = '2016-04-11'

    def __init__(self):
        super(Prefer_External, self).__init__("http://openconfig.net/yang/rib/bgp-types", "openconfig-rib-bgp-types", "openconfig-rib-bgp-types:PREFER_EXTERNAL")


class Origin_Type_Higher(Identity):
    """
    Route has a higher origin type, i.e., IGP origin is preferred
    over EGP or incomplete
    
    

    """

    _prefix = 'oc-bgprib-types'
    _revision = '2016-04-11'

    def __init__(self):
        super(Origin_Type_Higher, self).__init__("http://openconfig.net/yang/rib/bgp-types", "openconfig-rib-bgp-types", "openconfig-rib-bgp-types:ORIGIN_TYPE_HIGHER")


class Med_Higher(Identity):
    """
    Route has a higher MED, or metric, attribute than the current
    best path
    
    

    """

    _prefix = 'oc-bgprib-types'
    _revision = '2016-04-11'

    def __init__(self):
        super(Med_Higher, self).__init__("http://openconfig.net/yang/rib/bgp-types", "openconfig-rib-bgp-types", "openconfig-rib-bgp-types:MED_HIGHER")


class Nexthop_Cost_Higher(Identity):
    """
    Route has a higher interior cost to the next hop.
    
    

    """

    _prefix = 'oc-bgprib-types'
    _revision = '2016-04-11'

    def __init__(self):
        super(Nexthop_Cost_Higher, self).__init__("http://openconfig.net/yang/rib/bgp-types", "openconfig-rib-bgp-types", "openconfig-rib-bgp-types:NEXTHOP_COST_HIGHER")


class Higher_Router_Id(Identity):
    """
    Route was sent by a peer with a higher BGP Identifier value,
    or router id
    
    

    """

    _prefix = 'oc-bgprib-types'
    _revision = '2016-04-11'

    def __init__(self):
        super(Higher_Router_Id, self).__init__("http://openconfig.net/yang/rib/bgp-types", "openconfig-rib-bgp-types", "openconfig-rib-bgp-types:HIGHER_ROUTER_ID")


