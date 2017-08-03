""" pim 


The YANG\-module for Protocol Independent Multicast (PIM). 
The module defines configuration and operational data 
for the following features\:
PIM Sparse Mode (PIM\-SM)
PIM Source\-Specific Multicast (PIM\-SSM)
Bidirectional PIM (Bidir\-PIM)
Anycast\-RP for PIM
Bootstrap Router (BSR)  for PIM
PIM Dense Mode (PIM\-DM)
Auto\-RP \- Cisco\-propriatary

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class MrouteProtocolType(Enum):
    """
    MrouteProtocolType

    The multicast routing protocol.  Inclusion of values for

    multicast routing protocols is not intended to imply that

    those protocols need be supported.

    .. data:: other = 1

    .. data:: local = 2

    .. data:: netmgmt = 3

    .. data:: dvmrp = 4

    .. data:: mospf = 5

    .. data:: pimSparseDense = 6

    .. data:: cbt = 7

    .. data:: pimSparseMode = 8

    .. data:: pimDenseMode = 9

    .. data:: igmpOnly = 10

    .. data:: bgmp = 11

    .. data:: msdp = 12

    """

    other = Enum.YLeaf(1, "other")

    local = Enum.YLeaf(2, "local")

    netmgmt = Enum.YLeaf(3, "netmgmt")

    dvmrp = Enum.YLeaf(4, "dvmrp")

    mospf = Enum.YLeaf(5, "mospf")

    pimSparseDense = Enum.YLeaf(6, "pimSparseDense")

    cbt = Enum.YLeaf(7, "cbt")

    pimSparseMode = Enum.YLeaf(8, "pimSparseMode")

    pimDenseMode = Enum.YLeaf(9, "pimDenseMode")

    igmpOnly = Enum.YLeaf(10, "igmpOnly")

    bgmp = Enum.YLeaf(11, "bgmp")

    msdp = Enum.YLeaf(12, "msdp")


class Origin(Enum):
    """
    Origin

    This type  verify all uses of origin in model describes where a state was learned.

    .. data:: other_origin = 1

    	The state's origin is none of the available sources or it is unknown.

    .. data:: pim_request = 2

    	PIM-request-states are learned by PIM joins (between PIM-routers).

    .. data:: ssm_request = 3

    	SSM-Request-states are learned by SSM channel subscription, e.g., through 

    	IGMP3 (primarily only on last-hop-routers, although routers within the domain can keep 

    	this origin-type

    	).

    .. data:: fixed = 4

    	Fixed states are created automatically by the router at startup, to 

    	correspond to the well-defined prefixes of link-local and unroutable group addresses. 

    	These states are never destroyed.

    .. data:: embedded = 5

    	Embedded states are created by the router to correspond to group 

    	prefixes that are to be treated as being in Embedded-RP format.

    .. data:: static = 6

    	Static states are created and destroyed as a result of static configuration.

    .. data:: config_ssm = 7

    	Config-SSM states are created and destroyed as a result of configuration 

    	of SSM address ranges to the local router.

    .. data:: auto_rp = 8

    	Auto-RP states are created as a result of running Cisco's Auto-RP mechanism.

    .. data:: bsr = 9

    	BSR states are created as a result of running the PIM Bootstrap Router 

    	(BSR) mechanism.

    .. data:: msdp = 10

    	MSDP states are (*, G)-entries learned through a Multicast Source Discovery 

    	Protocol (MSDP) peer. This origin is applicable only for an RP running MSDP. 

    """

    other_origin = Enum.YLeaf(1, "other-origin")

    pim_request = Enum.YLeaf(2, "pim-request")

    ssm_request = Enum.YLeaf(3, "ssm-request")

    fixed = Enum.YLeaf(4, "fixed")

    embedded = Enum.YLeaf(5, "embedded")

    static = Enum.YLeaf(6, "static")

    config_ssm = Enum.YLeaf(7, "config-ssm")

    auto_rp = Enum.YLeaf(8, "auto-rp")

    bsr = Enum.YLeaf(9, "bsr")

    msdp = Enum.YLeaf(10, "msdp")


class PimMode(Enum):
    """
    PimMode

    PIM mode active on an interface.

    .. data:: sparse = 1

    	PIM sparse mode enabled on interface

    .. data:: dense = 2

    	PIM dense mode enable on interface.

    .. data:: sparse_dense = 3

    	PIM dense mode enable on interface.

    .. data:: dm_proxy = 4

    	PIM dense mode enable on interface.

    .. data:: none = 5

    	PIM dense mode enable on interface.

    """

    sparse = Enum.YLeaf(1, "sparse")

    dense = Enum.YLeaf(2, "dense")

    sparse_dense = Enum.YLeaf(3, "sparse-dense")

    dm_proxy = Enum.YLeaf(4, "dm-proxy")

    none = Enum.YLeaf(5, "none")


class RouteProtocolType(Enum):
    """
    RouteProtocolType

    A mechanism for learning routes.  Inclusion of values for

    routing protocols is not intended to imply that those

    protocols need be supported.

    .. data:: other = 1

    .. data:: local = 2

    .. data:: netmgmt = 3

    .. data:: icmp = 4

    .. data:: egp = 5

    .. data:: ggp = 6

    .. data:: hello = 7

    .. data:: rip = 8

    .. data:: isIs = 9

    .. data:: esIs = 10

    .. data:: ciscoIgrp = 11

    .. data:: bbnSpfIgp = 12

    .. data:: ospf = 13

    .. data:: bgp = 14

    .. data:: idpr = 15

    .. data:: ciscoEigrp = 16

    .. data:: dvmrp = 17

    """

    other = Enum.YLeaf(1, "other")

    local = Enum.YLeaf(2, "local")

    netmgmt = Enum.YLeaf(3, "netmgmt")

    icmp = Enum.YLeaf(4, "icmp")

    egp = Enum.YLeaf(5, "egp")

    ggp = Enum.YLeaf(6, "ggp")

    hello = Enum.YLeaf(7, "hello")

    rip = Enum.YLeaf(8, "rip")

    isIs = Enum.YLeaf(9, "isIs")

    esIs = Enum.YLeaf(10, "esIs")

    ciscoIgrp = Enum.YLeaf(11, "ciscoIgrp")

    bbnSpfIgp = Enum.YLeaf(12, "bbnSpfIgp")

    ospf = Enum.YLeaf(13, "ospf")

    bgp = Enum.YLeaf(14, "bgp")

    idpr = Enum.YLeaf(15, "idpr")

    ciscoEigrp = Enum.YLeaf(16, "ciscoEigrp")

    dvmrp = Enum.YLeaf(17, "dvmrp")



class GroupToRpMappingMode(Identity):
    """
    The base\-type for a PIM\-mode giving context to a group\-to\-rp\-mapping.
    
    

    """

    _prefix = 'pim'
    _revision = '2014-06-27'

    def __init__(self):
        super(GroupToRpMappingMode, self).__init__("urn:cisco:params:xml:ns:yang:pim", "pim", "pim:group-to-rp-mapping-mode")


class SmMappingMode(Identity):
    """
    The mapping is for Sparse Mode.
    
    

    """

    _prefix = 'pim'
    _revision = '2014-06-27'

    def __init__(self):
        super(SmMappingMode, self).__init__("urn:cisco:params:xml:ns:yang:pim", "pim", "pim:sm-mapping-mode")


class DmMappingMode(Identity):
    """
    The mapping is for Dense Mode.
    
    

    """

    _prefix = 'pim'
    _revision = '2014-06-27'

    def __init__(self):
        super(DmMappingMode, self).__init__("urn:cisco:params:xml:ns:yang:pim", "pim", "pim:dm-mapping-mode")


class SsmMappingMode(Identity):
    """
    The mapping is for Source Specific Mode.
    
    

    """

    _prefix = 'pim'
    _revision = '2014-06-27'

    def __init__(self):
        super(SsmMappingMode, self).__init__("urn:cisco:params:xml:ns:yang:pim", "pim", "pim:ssm-mapping-mode")


class PimBidirMappingMode(Identity):
    """
    The mapping is for Bidirectional PIM.
    
    

    """

    _prefix = 'pim'
    _revision = '2014-06-27'

    def __init__(self):
        super(PimBidirMappingMode, self).__init__("urn:cisco:params:xml:ns:yang:pim", "pim", "pim:pim-bidir-mapping-mode")


class OtherMappingMode(Identity):
    """
    None of the available modes.
    
    

    """

    _prefix = 'pim'
    _revision = '2014-06-27'

    def __init__(self):
        super(OtherMappingMode, self).__init__("urn:cisco:params:xml:ns:yang:pim", "pim", "pim:other-mapping-mode")


class AsmMappingMode(Identity):
    """
    The mapping is for Any\-Source Multicast (ASM) with PIM Sparse Mode.
    
    

    """

    _prefix = 'pim'
    _revision = '2014-06-27'

    def __init__(self):
        super(AsmMappingMode, self).__init__("urn:cisco:params:xml:ns:yang:pim", "pim", "pim:asm-mapping-mode")


