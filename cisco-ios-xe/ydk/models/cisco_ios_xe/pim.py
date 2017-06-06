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


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class MrouteProtocolTypeEnum(Enum):
    """
    MrouteProtocolTypeEnum

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

    other = 1

    local = 2

    netmgmt = 3

    dvmrp = 4

    mospf = 5

    pimSparseDense = 6

    cbt = 7

    pimSparseMode = 8

    pimDenseMode = 9

    igmpOnly = 10

    bgmp = 11

    msdp = 12


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _pim as meta
        return meta._meta_table['MrouteProtocolTypeEnum']


class OriginEnum(Enum):
    """
    OriginEnum

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

    other_origin = 1

    pim_request = 2

    ssm_request = 3

    fixed = 4

    embedded = 5

    static = 6

    config_ssm = 7

    auto_rp = 8

    bsr = 9

    msdp = 10


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _pim as meta
        return meta._meta_table['OriginEnum']


class PimModeEnum(Enum):
    """
    PimModeEnum

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

    sparse = 1

    dense = 2

    sparse_dense = 3

    dm_proxy = 4

    none = 5


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _pim as meta
        return meta._meta_table['PimModeEnum']


class RouteProtocolTypeEnum(Enum):
    """
    RouteProtocolTypeEnum

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

    other = 1

    local = 2

    netmgmt = 3

    icmp = 4

    egp = 5

    ggp = 6

    hello = 7

    rip = 8

    isIs = 9

    esIs = 10

    ciscoIgrp = 11

    bbnSpfIgp = 12

    ospf = 13

    bgp = 14

    idpr = 15

    ciscoEigrp = 16

    dvmrp = 17


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _pim as meta
        return meta._meta_table['RouteProtocolTypeEnum']



class GroupToRpMappingModeIdentity(object):
    """
    The base\-type for a PIM\-mode giving context to a group\-to\-rp\-mapping.
    
    

    """

    _prefix = 'pim'
    _revision = '2014-06-27'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _pim as meta
        return meta._meta_table['GroupToRpMappingModeIdentity']['meta_info']


class SmMappingModeIdentity(GroupToRpMappingModeIdentity):
    """
    The mapping is for Sparse Mode.
    
    

    """

    _prefix = 'pim'
    _revision = '2014-06-27'

    def __init__(self):
        GroupToRpMappingModeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _pim as meta
        return meta._meta_table['SmMappingModeIdentity']['meta_info']


class DmMappingModeIdentity(GroupToRpMappingModeIdentity):
    """
    The mapping is for Dense Mode.
    
    

    """

    _prefix = 'pim'
    _revision = '2014-06-27'

    def __init__(self):
        GroupToRpMappingModeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _pim as meta
        return meta._meta_table['DmMappingModeIdentity']['meta_info']


class PimBidirMappingModeIdentity(GroupToRpMappingModeIdentity):
    """
    The mapping is for Bidirectional PIM.
    
    

    """

    _prefix = 'pim'
    _revision = '2014-06-27'

    def __init__(self):
        GroupToRpMappingModeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _pim as meta
        return meta._meta_table['PimBidirMappingModeIdentity']['meta_info']


class SsmMappingModeIdentity(GroupToRpMappingModeIdentity):
    """
    The mapping is for Source Specific Mode.
    
    

    """

    _prefix = 'pim'
    _revision = '2014-06-27'

    def __init__(self):
        GroupToRpMappingModeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _pim as meta
        return meta._meta_table['SsmMappingModeIdentity']['meta_info']


class OtherMappingModeIdentity(GroupToRpMappingModeIdentity):
    """
    None of the available modes.
    
    

    """

    _prefix = 'pim'
    _revision = '2014-06-27'

    def __init__(self):
        GroupToRpMappingModeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _pim as meta
        return meta._meta_table['OtherMappingModeIdentity']['meta_info']


class AsmMappingModeIdentity(GroupToRpMappingModeIdentity):
    """
    The mapping is for Any\-Source Multicast (ASM) with PIM Sparse Mode.
    
    

    """

    _prefix = 'pim'
    _revision = '2014-06-27'

    def __init__(self):
        GroupToRpMappingModeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _pim as meta
        return meta._meta_table['AsmMappingModeIdentity']['meta_info']


