""" Cisco_IOS_XR_evpn_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR evpn package operational data.

This module contains definitions
for the following management objects\:
  evpn\: EVPN Operational Table

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class BgpRouteTargetEnum(Enum):
    """
    BgpRouteTargetEnum

    Bgp route target

    .. data:: no_stitching = 0

    	RT is default type

    .. data:: stitching = 1

    	RT is for stitching (Golf-L2)

    """

    no_stitching = 0

    stitching = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
        return meta._meta_table['BgpRouteTargetEnum']


class BgpRouteTargetFormatEnum(Enum):
    """
    BgpRouteTargetFormatEnum

    Bgp route target format

    .. data:: none = 0

    	No route target

    .. data:: two_byte_as = 1

    	2 Byte AS:nn format

    .. data:: four_byte_as = 2

    	4 byte AS:nn format

    .. data:: ipv4_address = 3

    	IP:nn format

    """

    none = 0

    two_byte_as = 1

    four_byte_as = 2

    ipv4_address = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
        return meta._meta_table['BgpRouteTargetFormatEnum']


class BgpRouteTargetRoleEnum(Enum):
    """
    BgpRouteTargetRoleEnum

    Bgp route target role

    .. data:: both = 0

    	Both Import and export roles

    .. data:: import_ = 1

    	Import role

    .. data:: export = 2

    	Export role

    """

    both = 0

    import_ = 1

    export = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
        return meta._meta_table['BgpRouteTargetRoleEnum']


class EvpnEnum(Enum):
    """
    EvpnEnum

    Evpn

    .. data:: evpn_type_invalid = 0

    	Unspecify type for that EVI entry

    .. data:: evpn_type_evpn = 1

    	EVPN service type

    .. data:: evpn_type_pbb_evpn = 2

    	PBB EVPN service type

    .. data:: evpn_type_evpn_vpws_vlan_unaware = 3

    	EVPN VPWS vlan-unaware service type

    .. data:: evpn_type_evpn_vpws_vlan_aware = 4

    	EVPN VPWS vlan-aware service type

    .. data:: evpn_type_max = 5

    	Max EVPN type

    """

    evpn_type_invalid = 0

    evpn_type_evpn = 1

    evpn_type_pbb_evpn = 2

    evpn_type_evpn_vpws_vlan_unaware = 3

    evpn_type_evpn_vpws_vlan_aware = 4

    evpn_type_max = 5


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
        return meta._meta_table['EvpnEnum']


class L2VpnAdRdEnum(Enum):
    """
    L2VpnAdRdEnum

    L2vpn ad rd

    .. data:: l2vpn_ad_rd_none = 0

    	Route Distinguisher not set

    .. data:: l2vpn_ad_rd_auto = 1

    	Route Distinguisher auto-generated

    .. data:: l2vpn_ad_rd_as = 2

    	Route Distinguisher with 2 Byte AS number

    .. data:: l2vpn_ad_rd_4byte_as = 3

    	Route Distinguisher with 4 Byte AS number

    .. data:: l2vpn_ad_rd_v4_addr = 4

    	Route Distinguisher with IPv4 Address

    """

    l2vpn_ad_rd_none = 0

    l2vpn_ad_rd_auto = 1

    l2vpn_ad_rd_as = 2

    l2vpn_ad_rd_4byte_as = 3

    l2vpn_ad_rd_v4_addr = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
        return meta._meta_table['L2VpnAdRdEnum']


class L2VpnAdRtEnum(Enum):
    """
    L2VpnAdRtEnum

    L2vpn ad rt

    .. data:: l2vpn_ad_rt_none = 0

    	Route target not set

    .. data:: l2vpn_ad_rt_as = 1

    	Route Target with 2 Byte AS number

    .. data:: l2vpn_ad_rt_4byte_as = 2

    	Route Target with 4 Byte AS number

    .. data:: l2vpn_ad_rt_v4_addr = 3

    	Route Target with IPv4 Address

    .. data:: es_import = 1538

    	Ethernet Segment Route Target from BGP

    """

    l2vpn_ad_rt_none = 0

    l2vpn_ad_rt_as = 1

    l2vpn_ad_rt_4byte_as = 2

    l2vpn_ad_rt_v4_addr = 3

    es_import = 1538


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
        return meta._meta_table['L2VpnAdRtEnum']


class L2VpnAdRtRoleEnum(Enum):
    """
    L2VpnAdRtRoleEnum

    L2vpn ad rt role

    .. data:: both = 0

    	Both

    .. data:: import_ = 1

    	Import

    .. data:: export = 2

    	Export

    """

    both = 0

    import_ = 1

    export = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
        return meta._meta_table['L2VpnAdRtRoleEnum']


class L2VpnEvpnEsiEnum(Enum):
    """
    L2VpnEvpnEsiEnum

    EVPN ESI types

    .. data:: esi_type0 = 0

    	ESI type zero

    .. data:: esi_type1 = 1

    	ESI type one

    .. data:: esi_type2 = 2

    	ESI type two

    .. data:: esi_type3 = 3

    	ESI type three

    .. data:: esi_type4 = 4

    	ESI type four

    .. data:: esi_type5 = 5

    	ESI type five

    .. data:: l2vpn_evpn_esi_type_legacy = 128

    	ESI type legacy

    .. data:: l2vpn_evpn_esi_type_override = 129

    	ESI type override (10-octet value)

    .. data:: esi_type_invalid = 255

    	ESI type invalid

    """

    esi_type0 = 0

    esi_type1 = 1

    esi_type2 = 2

    esi_type3 = 3

    esi_type4 = 4

    esi_type5 = 5

    l2vpn_evpn_esi_type_legacy = 128

    l2vpn_evpn_esi_type_override = 129

    esi_type_invalid = 255


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
        return meta._meta_table['L2VpnEvpnEsiEnum']


class L2VpnEvpnLbModeEnum(Enum):
    """
    L2VpnEvpnLbModeEnum

    L2VPN EVPN load balancing mode

    .. data:: invalid_load_balancing = 0

    	Invalid load balancing

    .. data:: single_homed = 1

    	Single-homed site or network

    .. data:: multi_homed_aa_per_flow = 2

    	Multi-homed access network active/active per

    	flow

    .. data:: multi_homed_aa_per_service = 3

    	Multi-homed access network active/active per

    	service

    """

    invalid_load_balancing = 0

    single_homed = 1

    multi_homed_aa_per_flow = 2

    multi_homed_aa_per_service = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
        return meta._meta_table['L2VpnEvpnLbModeEnum']


class L2VpnEvpnMfModeEnum(Enum):
    """
    L2VpnEvpnMfModeEnum

    L2VPN EVPN MAC flushing mode

    .. data:: invalid = 0

    	Invalid MAC Flushing mode

    .. data:: tcn_stp = 1

    	TCN STP MAC Flushing mode

    .. data:: mvrp = 2

    	MVRP MAC Flushing mode

    """

    invalid = 0

    tcn_stp = 1

    mvrp = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
        return meta._meta_table['L2VpnEvpnMfModeEnum']


class L2VpnEvpnRtOriginEnum(Enum):
    """
    L2VpnEvpnRtOriginEnum

    L2vpn evpn rt origin

    .. data:: invalid = 0

    	Incomplete Configuration

    .. data:: extracted = 1

    	From ESI

    .. data:: configured = 2

    	Locally configured

    """

    invalid = 0

    extracted = 1

    configured = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
        return meta._meta_table['L2VpnEvpnRtOriginEnum']


class L2VpnEvpnScEnum(Enum):
    """
    L2VpnEvpnScEnum

    EVPN Ethernet\-Segment service carving type

    .. data:: not_applicable = 0

    	Service Carving does not apply

    .. data:: evi = 1

    	Service Carving by EVI

    .. data:: isid = 2

    	Service Carving by ISID

    .. data:: evpn_bag_sc_type_max = 3

    	evpn bag sc type max

    """

    not_applicable = 0

    evi = 1

    isid = 2

    evpn_bag_sc_type_max = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
        return meta._meta_table['L2VpnEvpnScEnum']


class L2VpnEvpnScModeEnum(Enum):
    """
    L2VpnEvpnScModeEnum

    EVPN Ethernet\-Segment service carving mode

    .. data:: invalid = 0

    	Invalid service carving mode

    .. data:: auto = 1

    	Auto service carving mode

    .. data:: manual = 2

    	Manual service carving

    """

    invalid = 0

    auto = 1

    manual = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
        return meta._meta_table['L2VpnEvpnScModeEnum']


class L2VpnEvpnSmacSrcEnum(Enum):
    """
    L2VpnEvpnSmacSrcEnum

    L2vpn evpn smac src

    .. data:: invalid = 0

    	Incomplete Configuration

    .. data:: not_applicable = 1

    	Source MAC Not Applicable (EVPN)

    .. data:: local = 2

    	Local

    .. data:: pbb_bsa = 3

    	PBB BSA

    .. data:: esi = 4

    	From ESI

    .. data:: esi_invalid = 5

    	From ESI, Error

    .. data:: pbb_bsa_overrride = 6

    	PBB BSA, no ESI

    """

    invalid = 0

    not_applicable = 1

    local = 2

    pbb_bsa = 3

    esi = 4

    esi_invalid = 5

    pbb_bsa_overrride = 6


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
        return meta._meta_table['L2VpnEvpnSmacSrcEnum']


class L2VpnRgStateEnum(Enum):
    """
    L2VpnRgStateEnum

    L2vpn rg state

    .. data:: unknown = 0

    	Not defined

    .. data:: active = 1

    	Active

    .. data:: standby = 2

    	Standby

    """

    unknown = 0

    active = 1

    standby = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
        return meta._meta_table['L2VpnRgStateEnum']



class Evpn(object):
    """
    EVPN Operational Table
    
    .. attribute:: active
    
    	Active EVPN operational data
    	**type**\:   :py:class:`Active <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active>`
    
    .. attribute:: nodes
    
    	Table of EVPN operational data for a particular node
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes>`
    
    .. attribute:: standby
    
    	Standby EVPN operational data
    	**type**\:   :py:class:`Standby <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby>`
    
    

    """

    _prefix = 'evpn-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.active = Evpn.Active()
        self.active.parent = self
        self.nodes = Evpn.Nodes()
        self.nodes.parent = self
        self.standby = Evpn.Standby()
        self.standby.parent = self


    class Nodes(object):
        """
        Table of EVPN operational data for a particular
        node
        
        .. attribute:: node
        
        	EVPN operational data for a particular node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node>`
        
        

        """

        _prefix = 'evpn-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.node = YList()
            self.node.parent = self
            self.node.name = 'node'


        class Node(object):
            """
            EVPN operational data for a particular node
            
            .. attribute:: node_id  <key>
            
            	Location
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: ac_ids
            
            	EVPN AC ID table
            	**type**\:   :py:class:`AcIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.AcIds>`
            
            .. attribute:: ethernet_segments
            
            	EVPN Ethernet\-Segment Table
            	**type**\:   :py:class:`EthernetSegments <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EthernetSegments>`
            
            .. attribute:: evi_detail
            
            	L2VPN EVI Detail Table
            	**type**\:   :py:class:`EviDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail>`
            
            .. attribute:: evis
            
            	L2VPN EVPN EVI Table
            	**type**\:   :py:class:`Evis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.Evis>`
            
            .. attribute:: summary
            
            	L2VPN EVPN Summary
            	**type**\:   :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.Summary>`
            
            

            """

            _prefix = 'evpn-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.node_id = None
                self.ac_ids = Evpn.Nodes.Node.AcIds()
                self.ac_ids.parent = self
                self.ethernet_segments = Evpn.Nodes.Node.EthernetSegments()
                self.ethernet_segments.parent = self
                self.evi_detail = Evpn.Nodes.Node.EviDetail()
                self.evi_detail.parent = self
                self.evis = Evpn.Nodes.Node.Evis()
                self.evis.parent = self
                self.summary = Evpn.Nodes.Node.Summary()
                self.summary.parent = self


            class Evis(object):
                """
                L2VPN EVPN EVI Table
                
                .. attribute:: evi
                
                	L2VPN EVPN EVI Entry
                	**type**\: list of    :py:class:`Evi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.Evis.Evi>`
                
                

                """

                _prefix = 'evpn-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.evi = YList()
                    self.evi.parent = self
                    self.evi.name = 'evi'


                class Evi(object):
                    """
                    L2VPN EVPN EVI Entry
                    
                    .. attribute:: evi  <key>
                    
                    	EVPN id
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: bd_name
                    
                    	Bridge domain name
                    	**type**\:  str
                    
                    .. attribute:: evi_xr
                    
                    	E\-VPN id
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: type
                    
                    	Service Type
                    	**type**\:   :py:class:`EvpnEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.EvpnEnum>`
                    
                    

                    """

                    _prefix = 'evpn-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.evi = None
                        self.bd_name = None
                        self.evi_xr = None
                        self.type = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.evi is None:
                            raise YPYModelError('Key property evi is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:evi[Cisco-IOS-XR-evpn-oper:evi = ' + str(self.evi) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.evi is not None:
                            return True

                        if self.bd_name is not None:
                            return True

                        if self.evi_xr is not None:
                            return True

                        if self.type is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                        return meta._meta_table['Evpn.Nodes.Node.Evis.Evi']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:evis'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.evi is not None:
                        for child_ref in self.evi:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                    return meta._meta_table['Evpn.Nodes.Node.Evis']['meta_info']


            class Summary(object):
                """
                L2VPN EVPN Summary
                
                .. attribute:: as_
                
                	BGP AS number
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: es_entries
                
                	Number of ES Entries in DB
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: es_global_mac_routes
                
                	Number of ES\:Global MAC Routes
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: ev_is
                
                	Number of EVI DB Entries
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: global_source_mac
                
                	Global Source MAC Address
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: l2rib_throttle
                
                	Send to L2RIB Throttled
                	**type**\:  bool
                
                .. attribute:: labels
                
                	Number of Internal Labels
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: local_ead_routes
                
                	Number of Local EAD Entries in DB
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: local_imcast_routes
                
                	Number of Local IMCAST Routes
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: local_ipv4_mac_routes
                
                	Number of Local IPv4 MAC\-IP Routes
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: local_ipv6_mac_routes
                
                	Number of Local IPv6 MAC\-IP Routes
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: local_mac_routes
                
                	Number of Local MAC Routes
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: logging_df_election_enabled
                
                	Logging EVPN Designated Forwarder changes enabled
                	**type**\:  bool
                
                .. attribute:: neighbor_entries
                
                	Number of neighbor Entries in DB
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: peering_time
                
                	EVPN ES Peering Time (seconds)
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: recovery_time
                
                	EVPN ES Recovery Time (seconds)
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: remote_ead_routes
                
                	Number of Remote EAD Entries in DB
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: remote_imcast_routes
                
                	Number of Remote IMCAST Routes
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: remote_ipv4_mac_routes
                
                	Number of Remote IPv4 MAC\-IP Routes
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: remote_ipv6_mac_routes
                
                	Number of Remote IPv6 MAC\-IP Routes
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: remote_mac_routes
                
                	Number of Remote MAC Routes
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: remote_soo_mac_routes
                
                	Number of Remote Soo MAC Routes
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: router_id
                
                	EVPN Router ID
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                

                """

                _prefix = 'evpn-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.as_ = None
                    self.es_entries = None
                    self.es_global_mac_routes = None
                    self.ev_is = None
                    self.global_source_mac = None
                    self.l2rib_throttle = None
                    self.labels = None
                    self.local_ead_routes = None
                    self.local_imcast_routes = None
                    self.local_ipv4_mac_routes = None
                    self.local_ipv6_mac_routes = None
                    self.local_mac_routes = None
                    self.logging_df_election_enabled = None
                    self.neighbor_entries = None
                    self.peering_time = None
                    self.recovery_time = None
                    self.remote_ead_routes = None
                    self.remote_imcast_routes = None
                    self.remote_ipv4_mac_routes = None
                    self.remote_ipv6_mac_routes = None
                    self.remote_mac_routes = None
                    self.remote_soo_mac_routes = None
                    self.router_id = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:summary'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.as_ is not None:
                        return True

                    if self.es_entries is not None:
                        return True

                    if self.es_global_mac_routes is not None:
                        return True

                    if self.ev_is is not None:
                        return True

                    if self.global_source_mac is not None:
                        return True

                    if self.l2rib_throttle is not None:
                        return True

                    if self.labels is not None:
                        return True

                    if self.local_ead_routes is not None:
                        return True

                    if self.local_imcast_routes is not None:
                        return True

                    if self.local_ipv4_mac_routes is not None:
                        return True

                    if self.local_ipv6_mac_routes is not None:
                        return True

                    if self.local_mac_routes is not None:
                        return True

                    if self.logging_df_election_enabled is not None:
                        return True

                    if self.neighbor_entries is not None:
                        return True

                    if self.peering_time is not None:
                        return True

                    if self.recovery_time is not None:
                        return True

                    if self.remote_ead_routes is not None:
                        return True

                    if self.remote_imcast_routes is not None:
                        return True

                    if self.remote_ipv4_mac_routes is not None:
                        return True

                    if self.remote_ipv6_mac_routes is not None:
                        return True

                    if self.remote_mac_routes is not None:
                        return True

                    if self.remote_soo_mac_routes is not None:
                        return True

                    if self.router_id is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                    return meta._meta_table['Evpn.Nodes.Node.Summary']['meta_info']


            class EviDetail(object):
                """
                L2VPN EVI Detail Table
                
                .. attribute:: elements
                
                	EVI BGP RT Detail Info Elements
                	**type**\:   :py:class:`Elements <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.Elements>`
                
                .. attribute:: evi_children
                
                	Container for all EVI detail info
                	**type**\:   :py:class:`EviChildren <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.EviChildren>`
                
                

                """

                _prefix = 'evpn-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.elements = Evpn.Nodes.Node.EviDetail.Elements()
                    self.elements.parent = self
                    self.evi_children = Evpn.Nodes.Node.EviDetail.EviChildren()
                    self.evi_children.parent = self


                class Elements(object):
                    """
                    EVI BGP RT Detail Info Elements
                    
                    .. attribute:: element
                    
                    	EVI BGP RT Detail Info
                    	**type**\: list of    :py:class:`Element <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.Elements.Element>`
                    
                    

                    """

                    _prefix = 'evpn-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.element = YList()
                        self.element.parent = self
                        self.element.name = 'element'


                    class Element(object):
                        """
                        EVI BGP RT Detail Info
                        
                        .. attribute:: evi  <key>
                        
                        	EVPN id
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: advertise_mac
                        
                        	Advertise MAC\-only routes on this EVI
                        	**type**\:  bool
                        
                        .. attribute:: aliasing_disabled
                        
                        	Route Aliasing is disabled
                        	**type**\:  bool
                        
                        .. attribute:: bd_name
                        
                        	Bridge domain name
                        	**type**\:  str
                        
                        .. attribute:: cw_disable
                        
                        	Control\-Word Disable
                        	**type**\:  bool
                        
                        .. attribute:: description
                        
                        	EVI description
                        	**type**\:  str
                        
                        .. attribute:: evi_xr
                        
                        	E\-VPN id
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: flow_label
                        
                        	Flow Label Information
                        	**type**\:   :py:class:`FlowLabel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.Elements.Element.FlowLabel>`
                        
                        .. attribute:: forward_class
                        
                        	Forward Class attribute
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: multicast_label
                        
                        	Multicast Label
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: rd_auto
                        
                        	Automatic Route Distingtuisher
                        	**type**\:   :py:class:`RdAuto <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.Elements.Element.RdAuto>`
                        
                        .. attribute:: rd_configured
                        
                        	Configured Route Distinguisher
                        	**type**\:   :py:class:`RdConfigured <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.Elements.Element.RdConfigured>`
                        
                        .. attribute:: reoriginate_disabled
                        
                        	Route Re\-origination is disabled
                        	**type**\:  bool
                        
                        .. attribute:: rt_auto
                        
                        	Automatic Route Target
                        	**type**\:   :py:class:`RtAuto <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.Elements.Element.RtAuto>`
                        
                        .. attribute:: rt_auto_stitching
                        
                        	Automatic Route Target Stitching
                        	**type**\:   :py:class:`RtAutoStitching <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.Elements.Element.RtAutoStitching>`
                        
                        .. attribute:: rt_export_block_set
                        
                        	Is Export RT None set
                        	**type**\:  bool
                        
                        .. attribute:: rt_import_block_set
                        
                        	Is Import RT None set
                        	**type**\:  bool
                        
                        .. attribute:: stitching
                        
                        	RT Stitching for MPLS Fabric is enabled
                        	**type**\:  bool
                        
                        .. attribute:: table_policy_name
                        
                        	Table\-policy Name
                        	**type**\:  str
                        
                        .. attribute:: type
                        
                        	Service Type
                        	**type**\:   :py:class:`EvpnEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.EvpnEnum>`
                        
                        .. attribute:: unicast_label
                        
                        	Unicast Label
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unknown_unicast_flooding_disabled
                        
                        	Unknown\-unicast flooding is disabled
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'evpn-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.evi = None
                            self.advertise_mac = None
                            self.aliasing_disabled = None
                            self.bd_name = None
                            self.cw_disable = None
                            self.description = None
                            self.evi_xr = None
                            self.flow_label = Evpn.Nodes.Node.EviDetail.Elements.Element.FlowLabel()
                            self.flow_label.parent = self
                            self.forward_class = None
                            self.multicast_label = None
                            self.rd_auto = Evpn.Nodes.Node.EviDetail.Elements.Element.RdAuto()
                            self.rd_auto.parent = self
                            self.rd_configured = Evpn.Nodes.Node.EviDetail.Elements.Element.RdConfigured()
                            self.rd_configured.parent = self
                            self.reoriginate_disabled = None
                            self.rt_auto = Evpn.Nodes.Node.EviDetail.Elements.Element.RtAuto()
                            self.rt_auto.parent = self
                            self.rt_auto_stitching = Evpn.Nodes.Node.EviDetail.Elements.Element.RtAutoStitching()
                            self.rt_auto_stitching.parent = self
                            self.rt_export_block_set = None
                            self.rt_import_block_set = None
                            self.stitching = None
                            self.table_policy_name = None
                            self.type = None
                            self.unicast_label = None
                            self.unknown_unicast_flooding_disabled = None


                        class FlowLabel(object):
                            """
                            Flow Label Information
                            
                            .. attribute:: global_flow_label
                            
                            	Globally configured flow label
                            	**type**\:  bool
                            
                            .. attribute:: static_flow_label
                            
                            	Static flow label
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.global_flow_label = None
                                self.static_flow_label = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:flow-label'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.global_flow_label is not None:
                                    return True

                                if self.static_flow_label is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                                return meta._meta_table['Evpn.Nodes.Node.EviDetail.Elements.Element.FlowLabel']['meta_info']


                        class RdAuto(object):
                            """
                            Automatic Route Distingtuisher
                            
                            .. attribute:: auto
                            
                            	auto
                            	**type**\:   :py:class:`Auto <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.Elements.Element.RdAuto.Auto>`
                            
                            .. attribute:: four_byte_as
                            
                            	four byte as
                            	**type**\:   :py:class:`FourByteAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.Elements.Element.RdAuto.FourByteAs>`
                            
                            .. attribute:: rd
                            
                            	RD
                            	**type**\:   :py:class:`L2VpnAdRdEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2VpnAdRdEnum>`
                            
                            .. attribute:: two_byte_as
                            
                            	two byte as
                            	**type**\:   :py:class:`TwoByteAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.Elements.Element.RdAuto.TwoByteAs>`
                            
                            .. attribute:: v4_addr
                            
                            	v4 addr
                            	**type**\:   :py:class:`V4Addr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.Elements.Element.RdAuto.V4Addr>`
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.auto = Evpn.Nodes.Node.EviDetail.Elements.Element.RdAuto.Auto()
                                self.auto.parent = self
                                self.four_byte_as = Evpn.Nodes.Node.EviDetail.Elements.Element.RdAuto.FourByteAs()
                                self.four_byte_as.parent = self
                                self.rd = None
                                self.two_byte_as = Evpn.Nodes.Node.EviDetail.Elements.Element.RdAuto.TwoByteAs()
                                self.two_byte_as.parent = self
                                self.v4_addr = Evpn.Nodes.Node.EviDetail.Elements.Element.RdAuto.V4Addr()
                                self.v4_addr.parent = self


                            class Auto(object):
                                """
                                auto
                                
                                .. attribute:: auto_index
                                
                                	Auto\-generated Index
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: router_id
                                
                                	BGP Router ID
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'evpn-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.auto_index = None
                                    self.router_id = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:auto'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.auto_index is not None:
                                        return True

                                    if self.router_id is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                                    return meta._meta_table['Evpn.Nodes.Node.EviDetail.Elements.Element.RdAuto.Auto']['meta_info']


                            class TwoByteAs(object):
                                """
                                two byte as
                                
                                .. attribute:: four_byte_index
                                
                                	4 Byte Index
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: two_byte_as
                                
                                	2 Byte AS Number
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'evpn-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.four_byte_index = None
                                    self.two_byte_as = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:two-byte-as'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.four_byte_index is not None:
                                        return True

                                    if self.two_byte_as is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                                    return meta._meta_table['Evpn.Nodes.Node.EviDetail.Elements.Element.RdAuto.TwoByteAs']['meta_info']


                            class FourByteAs(object):
                                """
                                four byte as
                                
                                .. attribute:: four_byte_as
                                
                                	4 Byte AS Number
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: two_byte_index
                                
                                	2 Byte Index
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'evpn-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.four_byte_as = None
                                    self.two_byte_index = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:four-byte-as'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.four_byte_as is not None:
                                        return True

                                    if self.two_byte_index is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                                    return meta._meta_table['Evpn.Nodes.Node.EviDetail.Elements.Element.RdAuto.FourByteAs']['meta_info']


                            class V4Addr(object):
                                """
                                v4 addr
                                
                                .. attribute:: ipv4_address
                                
                                	IPv4 Address
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: two_byte_index
                                
                                	2 Byte Index
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'evpn-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.ipv4_address = None
                                    self.two_byte_index = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:v4-addr'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.ipv4_address is not None:
                                        return True

                                    if self.two_byte_index is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                                    return meta._meta_table['Evpn.Nodes.Node.EviDetail.Elements.Element.RdAuto.V4Addr']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:rd-auto'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.auto is not None and self.auto._has_data():
                                    return True

                                if self.four_byte_as is not None and self.four_byte_as._has_data():
                                    return True

                                if self.rd is not None:
                                    return True

                                if self.two_byte_as is not None and self.two_byte_as._has_data():
                                    return True

                                if self.v4_addr is not None and self.v4_addr._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                                return meta._meta_table['Evpn.Nodes.Node.EviDetail.Elements.Element.RdAuto']['meta_info']


                        class RdConfigured(object):
                            """
                            Configured Route Distinguisher
                            
                            .. attribute:: auto
                            
                            	auto
                            	**type**\:   :py:class:`Auto <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.Elements.Element.RdConfigured.Auto>`
                            
                            .. attribute:: four_byte_as
                            
                            	four byte as
                            	**type**\:   :py:class:`FourByteAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.Elements.Element.RdConfigured.FourByteAs>`
                            
                            .. attribute:: rd
                            
                            	RD
                            	**type**\:   :py:class:`L2VpnAdRdEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2VpnAdRdEnum>`
                            
                            .. attribute:: two_byte_as
                            
                            	two byte as
                            	**type**\:   :py:class:`TwoByteAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.Elements.Element.RdConfigured.TwoByteAs>`
                            
                            .. attribute:: v4_addr
                            
                            	v4 addr
                            	**type**\:   :py:class:`V4Addr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.Elements.Element.RdConfigured.V4Addr>`
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.auto = Evpn.Nodes.Node.EviDetail.Elements.Element.RdConfigured.Auto()
                                self.auto.parent = self
                                self.four_byte_as = Evpn.Nodes.Node.EviDetail.Elements.Element.RdConfigured.FourByteAs()
                                self.four_byte_as.parent = self
                                self.rd = None
                                self.two_byte_as = Evpn.Nodes.Node.EviDetail.Elements.Element.RdConfigured.TwoByteAs()
                                self.two_byte_as.parent = self
                                self.v4_addr = Evpn.Nodes.Node.EviDetail.Elements.Element.RdConfigured.V4Addr()
                                self.v4_addr.parent = self


                            class Auto(object):
                                """
                                auto
                                
                                .. attribute:: auto_index
                                
                                	Auto\-generated Index
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: router_id
                                
                                	BGP Router ID
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'evpn-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.auto_index = None
                                    self.router_id = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:auto'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.auto_index is not None:
                                        return True

                                    if self.router_id is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                                    return meta._meta_table['Evpn.Nodes.Node.EviDetail.Elements.Element.RdConfigured.Auto']['meta_info']


                            class TwoByteAs(object):
                                """
                                two byte as
                                
                                .. attribute:: four_byte_index
                                
                                	4 Byte Index
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: two_byte_as
                                
                                	2 Byte AS Number
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'evpn-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.four_byte_index = None
                                    self.two_byte_as = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:two-byte-as'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.four_byte_index is not None:
                                        return True

                                    if self.two_byte_as is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                                    return meta._meta_table['Evpn.Nodes.Node.EviDetail.Elements.Element.RdConfigured.TwoByteAs']['meta_info']


                            class FourByteAs(object):
                                """
                                four byte as
                                
                                .. attribute:: four_byte_as
                                
                                	4 Byte AS Number
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: two_byte_index
                                
                                	2 Byte Index
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'evpn-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.four_byte_as = None
                                    self.two_byte_index = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:four-byte-as'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.four_byte_as is not None:
                                        return True

                                    if self.two_byte_index is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                                    return meta._meta_table['Evpn.Nodes.Node.EviDetail.Elements.Element.RdConfigured.FourByteAs']['meta_info']


                            class V4Addr(object):
                                """
                                v4 addr
                                
                                .. attribute:: ipv4_address
                                
                                	IPv4 Address
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: two_byte_index
                                
                                	2 Byte Index
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'evpn-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.ipv4_address = None
                                    self.two_byte_index = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:v4-addr'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.ipv4_address is not None:
                                        return True

                                    if self.two_byte_index is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                                    return meta._meta_table['Evpn.Nodes.Node.EviDetail.Elements.Element.RdConfigured.V4Addr']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:rd-configured'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.auto is not None and self.auto._has_data():
                                    return True

                                if self.four_byte_as is not None and self.four_byte_as._has_data():
                                    return True

                                if self.rd is not None:
                                    return True

                                if self.two_byte_as is not None and self.two_byte_as._has_data():
                                    return True

                                if self.v4_addr is not None and self.v4_addr._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                                return meta._meta_table['Evpn.Nodes.Node.EviDetail.Elements.Element.RdConfigured']['meta_info']


                        class RtAuto(object):
                            """
                            Automatic Route Target
                            
                            .. attribute:: es_import
                            
                            	es import
                            	**type**\:   :py:class:`EsImport <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.Elements.Element.RtAuto.EsImport>`
                            
                            .. attribute:: four_byte_as
                            
                            	four byte as
                            	**type**\:   :py:class:`FourByteAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.Elements.Element.RtAuto.FourByteAs>`
                            
                            .. attribute:: rt
                            
                            	RT
                            	**type**\:   :py:class:`L2VpnAdRtEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2VpnAdRtEnum>`
                            
                            .. attribute:: two_byte_as
                            
                            	two byte as
                            	**type**\:   :py:class:`TwoByteAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.Elements.Element.RtAuto.TwoByteAs>`
                            
                            .. attribute:: v4_addr
                            
                            	v4 addr
                            	**type**\:   :py:class:`V4Addr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.Elements.Element.RtAuto.V4Addr>`
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.es_import = Evpn.Nodes.Node.EviDetail.Elements.Element.RtAuto.EsImport()
                                self.es_import.parent = self
                                self.four_byte_as = Evpn.Nodes.Node.EviDetail.Elements.Element.RtAuto.FourByteAs()
                                self.four_byte_as.parent = self
                                self.rt = None
                                self.two_byte_as = Evpn.Nodes.Node.EviDetail.Elements.Element.RtAuto.TwoByteAs()
                                self.two_byte_as.parent = self
                                self.v4_addr = Evpn.Nodes.Node.EviDetail.Elements.Element.RtAuto.V4Addr()
                                self.v4_addr.parent = self


                            class TwoByteAs(object):
                                """
                                two byte as
                                
                                .. attribute:: four_byte_index
                                
                                	4 Byte Index
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: two_byte_as
                                
                                	2 Byte AS Number
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'evpn-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.four_byte_index = None
                                    self.two_byte_as = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:two-byte-as'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.four_byte_index is not None:
                                        return True

                                    if self.two_byte_as is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                                    return meta._meta_table['Evpn.Nodes.Node.EviDetail.Elements.Element.RtAuto.TwoByteAs']['meta_info']


                            class FourByteAs(object):
                                """
                                four byte as
                                
                                .. attribute:: four_byte_as
                                
                                	4 Byte AS Number
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: two_byte_index
                                
                                	2 Byte Index
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'evpn-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.four_byte_as = None
                                    self.two_byte_index = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:four-byte-as'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.four_byte_as is not None:
                                        return True

                                    if self.two_byte_index is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                                    return meta._meta_table['Evpn.Nodes.Node.EviDetail.Elements.Element.RtAuto.FourByteAs']['meta_info']


                            class V4Addr(object):
                                """
                                v4 addr
                                
                                .. attribute:: ipv4_address
                                
                                	IPv4 Address
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: two_byte_index
                                
                                	2 Byte Index
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'evpn-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.ipv4_address = None
                                    self.two_byte_index = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:v4-addr'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.ipv4_address is not None:
                                        return True

                                    if self.two_byte_index is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                                    return meta._meta_table['Evpn.Nodes.Node.EviDetail.Elements.Element.RtAuto.V4Addr']['meta_info']


                            class EsImport(object):
                                """
                                es import
                                
                                .. attribute:: high_bytes
                                
                                	Top 4 bytes of ES Import
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: low_bytes
                                
                                	Low 2 bytes of ES Import
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'evpn-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.high_bytes = None
                                    self.low_bytes = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:es-import'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.high_bytes is not None:
                                        return True

                                    if self.low_bytes is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                                    return meta._meta_table['Evpn.Nodes.Node.EviDetail.Elements.Element.RtAuto.EsImport']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:rt-auto'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.es_import is not None and self.es_import._has_data():
                                    return True

                                if self.four_byte_as is not None and self.four_byte_as._has_data():
                                    return True

                                if self.rt is not None:
                                    return True

                                if self.two_byte_as is not None and self.two_byte_as._has_data():
                                    return True

                                if self.v4_addr is not None and self.v4_addr._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                                return meta._meta_table['Evpn.Nodes.Node.EviDetail.Elements.Element.RtAuto']['meta_info']


                        class RtAutoStitching(object):
                            """
                            Automatic Route Target Stitching
                            
                            .. attribute:: es_import
                            
                            	es import
                            	**type**\:   :py:class:`EsImport <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.Elements.Element.RtAutoStitching.EsImport>`
                            
                            .. attribute:: four_byte_as
                            
                            	four byte as
                            	**type**\:   :py:class:`FourByteAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.Elements.Element.RtAutoStitching.FourByteAs>`
                            
                            .. attribute:: rt
                            
                            	RT
                            	**type**\:   :py:class:`L2VpnAdRtEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2VpnAdRtEnum>`
                            
                            .. attribute:: two_byte_as
                            
                            	two byte as
                            	**type**\:   :py:class:`TwoByteAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.Elements.Element.RtAutoStitching.TwoByteAs>`
                            
                            .. attribute:: v4_addr
                            
                            	v4 addr
                            	**type**\:   :py:class:`V4Addr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.Elements.Element.RtAutoStitching.V4Addr>`
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.es_import = Evpn.Nodes.Node.EviDetail.Elements.Element.RtAutoStitching.EsImport()
                                self.es_import.parent = self
                                self.four_byte_as = Evpn.Nodes.Node.EviDetail.Elements.Element.RtAutoStitching.FourByteAs()
                                self.four_byte_as.parent = self
                                self.rt = None
                                self.two_byte_as = Evpn.Nodes.Node.EviDetail.Elements.Element.RtAutoStitching.TwoByteAs()
                                self.two_byte_as.parent = self
                                self.v4_addr = Evpn.Nodes.Node.EviDetail.Elements.Element.RtAutoStitching.V4Addr()
                                self.v4_addr.parent = self


                            class TwoByteAs(object):
                                """
                                two byte as
                                
                                .. attribute:: four_byte_index
                                
                                	4 Byte Index
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: two_byte_as
                                
                                	2 Byte AS Number
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'evpn-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.four_byte_index = None
                                    self.two_byte_as = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:two-byte-as'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.four_byte_index is not None:
                                        return True

                                    if self.two_byte_as is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                                    return meta._meta_table['Evpn.Nodes.Node.EviDetail.Elements.Element.RtAutoStitching.TwoByteAs']['meta_info']


                            class FourByteAs(object):
                                """
                                four byte as
                                
                                .. attribute:: four_byte_as
                                
                                	4 Byte AS Number
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: two_byte_index
                                
                                	2 Byte Index
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'evpn-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.four_byte_as = None
                                    self.two_byte_index = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:four-byte-as'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.four_byte_as is not None:
                                        return True

                                    if self.two_byte_index is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                                    return meta._meta_table['Evpn.Nodes.Node.EviDetail.Elements.Element.RtAutoStitching.FourByteAs']['meta_info']


                            class V4Addr(object):
                                """
                                v4 addr
                                
                                .. attribute:: ipv4_address
                                
                                	IPv4 Address
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: two_byte_index
                                
                                	2 Byte Index
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'evpn-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.ipv4_address = None
                                    self.two_byte_index = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:v4-addr'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.ipv4_address is not None:
                                        return True

                                    if self.two_byte_index is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                                    return meta._meta_table['Evpn.Nodes.Node.EviDetail.Elements.Element.RtAutoStitching.V4Addr']['meta_info']


                            class EsImport(object):
                                """
                                es import
                                
                                .. attribute:: high_bytes
                                
                                	Top 4 bytes of ES Import
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: low_bytes
                                
                                	Low 2 bytes of ES Import
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'evpn-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.high_bytes = None
                                    self.low_bytes = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:es-import'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.high_bytes is not None:
                                        return True

                                    if self.low_bytes is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                                    return meta._meta_table['Evpn.Nodes.Node.EviDetail.Elements.Element.RtAutoStitching.EsImport']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:rt-auto-stitching'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.es_import is not None and self.es_import._has_data():
                                    return True

                                if self.four_byte_as is not None and self.four_byte_as._has_data():
                                    return True

                                if self.rt is not None:
                                    return True

                                if self.two_byte_as is not None and self.two_byte_as._has_data():
                                    return True

                                if self.v4_addr is not None and self.v4_addr._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                                return meta._meta_table['Evpn.Nodes.Node.EviDetail.Elements.Element.RtAutoStitching']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.evi is None:
                                raise YPYModelError('Key property evi is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:element[Cisco-IOS-XR-evpn-oper:evi = ' + str(self.evi) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.evi is not None:
                                return True

                            if self.advertise_mac is not None:
                                return True

                            if self.aliasing_disabled is not None:
                                return True

                            if self.bd_name is not None:
                                return True

                            if self.cw_disable is not None:
                                return True

                            if self.description is not None:
                                return True

                            if self.evi_xr is not None:
                                return True

                            if self.flow_label is not None and self.flow_label._has_data():
                                return True

                            if self.forward_class is not None:
                                return True

                            if self.multicast_label is not None:
                                return True

                            if self.rd_auto is not None and self.rd_auto._has_data():
                                return True

                            if self.rd_configured is not None and self.rd_configured._has_data():
                                return True

                            if self.reoriginate_disabled is not None:
                                return True

                            if self.rt_auto is not None and self.rt_auto._has_data():
                                return True

                            if self.rt_auto_stitching is not None and self.rt_auto_stitching._has_data():
                                return True

                            if self.rt_export_block_set is not None:
                                return True

                            if self.rt_import_block_set is not None:
                                return True

                            if self.stitching is not None:
                                return True

                            if self.table_policy_name is not None:
                                return True

                            if self.type is not None:
                                return True

                            if self.unicast_label is not None:
                                return True

                            if self.unknown_unicast_flooding_disabled is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                            return meta._meta_table['Evpn.Nodes.Node.EviDetail.Elements.Element']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:elements'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.element is not None:
                            for child_ref in self.element:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                        return meta._meta_table['Evpn.Nodes.Node.EviDetail.Elements']['meta_info']


                class EviChildren(object):
                    """
                    Container for all EVI detail info
                    
                    .. attribute:: ethernet_auto_discoveries
                    
                    	EVPN Ethernet Auto\-Discovery table
                    	**type**\:   :py:class:`EthernetAutoDiscoveries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.EviChildren.EthernetAutoDiscoveries>`
                    
                    .. attribute:: inclusive_multicasts
                    
                    	L2VPN EVPN IMCAST table
                    	**type**\:   :py:class:`InclusiveMulticasts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.EviChildren.InclusiveMulticasts>`
                    
                    .. attribute:: macs
                    
                    	L2VPN EVPN EVI MAC table
                    	**type**\:   :py:class:`Macs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.EviChildren.Macs>`
                    
                    .. attribute:: neighbors
                    
                    	EVPN Neighbor table
                    	**type**\:   :py:class:`Neighbors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.EviChildren.Neighbors>`
                    
                    .. attribute:: route_targets
                    
                    	L2VPN EVPN EVI RT Child Table
                    	**type**\:   :py:class:`RouteTargets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets>`
                    
                    

                    """

                    _prefix = 'evpn-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.ethernet_auto_discoveries = Evpn.Nodes.Node.EviDetail.EviChildren.EthernetAutoDiscoveries()
                        self.ethernet_auto_discoveries.parent = self
                        self.inclusive_multicasts = Evpn.Nodes.Node.EviDetail.EviChildren.InclusiveMulticasts()
                        self.inclusive_multicasts.parent = self
                        self.macs = Evpn.Nodes.Node.EviDetail.EviChildren.Macs()
                        self.macs.parent = self
                        self.neighbors = Evpn.Nodes.Node.EviDetail.EviChildren.Neighbors()
                        self.neighbors.parent = self
                        self.route_targets = Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets()
                        self.route_targets.parent = self


                    class Neighbors(object):
                        """
                        EVPN Neighbor table
                        
                        .. attribute:: neighbor
                        
                        	EVPN Neighbor table
                        	**type**\: list of    :py:class:`Neighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.EviChildren.Neighbors.Neighbor>`
                        
                        

                        """

                        _prefix = 'evpn-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.neighbor = YList()
                            self.neighbor.parent = self
                            self.neighbor.name = 'neighbor'


                        class Neighbor(object):
                            """
                            EVPN Neighbor table
                            
                            .. attribute:: evi
                            
                            	EVPN id
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: evi_xr
                            
                            	E\-VPN id
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: neighbor
                            
                            	Neighbor IP
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: neighbor_ip
                            
                            	Neighbor IP
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.evi = None
                                self.evi_xr = None
                                self.neighbor = None
                                self.neighbor_ip = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:neighbor'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.evi is not None:
                                    return True

                                if self.evi_xr is not None:
                                    return True

                                if self.neighbor is not None:
                                    return True

                                if self.neighbor_ip is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                                return meta._meta_table['Evpn.Nodes.Node.EviDetail.EviChildren.Neighbors.Neighbor']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:neighbors'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.neighbor is not None:
                                for child_ref in self.neighbor:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                            return meta._meta_table['Evpn.Nodes.Node.EviDetail.EviChildren.Neighbors']['meta_info']


                    class EthernetAutoDiscoveries(object):
                        """
                        EVPN Ethernet Auto\-Discovery table
                        
                        .. attribute:: ethernet_auto_discovery
                        
                        	EVPN Ethernet Auto\-Discovery Entry
                        	**type**\: list of    :py:class:`EthernetAutoDiscovery <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.EviChildren.EthernetAutoDiscoveries.EthernetAutoDiscovery>`
                        
                        

                        """

                        _prefix = 'evpn-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.ethernet_auto_discovery = YList()
                            self.ethernet_auto_discovery.parent = self
                            self.ethernet_auto_discovery.name = 'ethernet_auto_discovery'


                        class EthernetAutoDiscovery(object):
                            """
                            EVPN Ethernet Auto\-Discovery Entry
                            
                            .. attribute:: encap
                            
                            	Encap type of local or remote EAD
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: esi1
                            
                            	ES id (part 1/5)
                            	**type**\:  str
                            
                            	**pattern:** [0\-9a\-fA\-F]{1,8}
                            
                            .. attribute:: esi2
                            
                            	ES id (part 2/5)
                            	**type**\:  str
                            
                            	**pattern:** [0\-9a\-fA\-F]{1,8}
                            
                            .. attribute:: esi3
                            
                            	ES id (part 3/5)
                            	**type**\:  str
                            
                            	**pattern:** [0\-9a\-fA\-F]{1,8}
                            
                            .. attribute:: esi4
                            
                            	ES id (part 4/5)
                            	**type**\:  str
                            
                            	**pattern:** [0\-9a\-fA\-F]{1,8}
                            
                            .. attribute:: esi5
                            
                            	ES id (part 5/5)
                            	**type**\:  str
                            
                            	**pattern:** [0\-9a\-fA\-F]{1,8}
                            
                            .. attribute:: ethernet_segment_identifier
                            
                            	Ethernet Segment id
                            	**type**\:  list of int
                            
                            	**range:** 0..255
                            
                            .. attribute:: ethernet_tag
                            
                            	Ethernet Tag ID
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: ethernet_tag_xr
                            
                            	Ethernet Tag
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: ethernet_vpnid
                            
                            	E\-VPN id
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: evi
                            
                            	EVPN id
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: is_local_ead
                            
                            	Indication of EthernetAutoDiscovery Route is local
                            	**type**\:  bool
                            
                            .. attribute:: local_label
                            
                            	Associated local label
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: local_next_hop
                            
                            	Local nexthop IP
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: num_paths
                            
                            	 Number of items in path list buffer
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: path_buffer
                            
                            	Path List Buffer
                            	**type**\: list of    :py:class:`PathBuffer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.EviChildren.EthernetAutoDiscoveries.EthernetAutoDiscovery.PathBuffer>`
                            
                            .. attribute:: redundancy_single_active
                            
                            	Single\-active redundancy configured at remote EAD
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.encap = None
                                self.esi1 = None
                                self.esi2 = None
                                self.esi3 = None
                                self.esi4 = None
                                self.esi5 = None
                                self.ethernet_segment_identifier = YLeafList()
                                self.ethernet_segment_identifier.parent = self
                                self.ethernet_segment_identifier.name = 'ethernet_segment_identifier'
                                self.ethernet_tag = None
                                self.ethernet_tag_xr = None
                                self.ethernet_vpnid = None
                                self.evi = None
                                self.is_local_ead = None
                                self.local_label = None
                                self.local_next_hop = None
                                self.num_paths = None
                                self.path_buffer = YList()
                                self.path_buffer.parent = self
                                self.path_buffer.name = 'path_buffer'
                                self.redundancy_single_active = None


                            class PathBuffer(object):
                                """
                                Path List Buffer
                                
                                .. attribute:: next_hop
                                
                                	Next\-hop IP address (v6 format)
                                	**type**\:  str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: output_label
                                
                                	Output Label
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'evpn-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.next_hop = None
                                    self.output_label = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:path-buffer'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.next_hop is not None:
                                        return True

                                    if self.output_label is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                                    return meta._meta_table['Evpn.Nodes.Node.EviDetail.EviChildren.EthernetAutoDiscoveries.EthernetAutoDiscovery.PathBuffer']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:ethernet-auto-discovery'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.encap is not None:
                                    return True

                                if self.esi1 is not None:
                                    return True

                                if self.esi2 is not None:
                                    return True

                                if self.esi3 is not None:
                                    return True

                                if self.esi4 is not None:
                                    return True

                                if self.esi5 is not None:
                                    return True

                                if self.ethernet_segment_identifier is not None:
                                    for child in self.ethernet_segment_identifier:
                                        if child is not None:
                                            return True

                                if self.ethernet_tag is not None:
                                    return True

                                if self.ethernet_tag_xr is not None:
                                    return True

                                if self.ethernet_vpnid is not None:
                                    return True

                                if self.evi is not None:
                                    return True

                                if self.is_local_ead is not None:
                                    return True

                                if self.local_label is not None:
                                    return True

                                if self.local_next_hop is not None:
                                    return True

                                if self.num_paths is not None:
                                    return True

                                if self.path_buffer is not None:
                                    for child_ref in self.path_buffer:
                                        if child_ref._has_data():
                                            return True

                                if self.redundancy_single_active is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                                return meta._meta_table['Evpn.Nodes.Node.EviDetail.EviChildren.EthernetAutoDiscoveries.EthernetAutoDiscovery']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:ethernet-auto-discoveries'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.ethernet_auto_discovery is not None:
                                for child_ref in self.ethernet_auto_discovery:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                            return meta._meta_table['Evpn.Nodes.Node.EviDetail.EviChildren.EthernetAutoDiscoveries']['meta_info']


                    class InclusiveMulticasts(object):
                        """
                        L2VPN EVPN IMCAST table
                        
                        .. attribute:: inclusive_multicast
                        
                        	L2VPN EVPN IMCAST table
                        	**type**\: list of    :py:class:`InclusiveMulticast <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.EviChildren.InclusiveMulticasts.InclusiveMulticast>`
                        
                        

                        """

                        _prefix = 'evpn-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.inclusive_multicast = YList()
                            self.inclusive_multicast.parent = self
                            self.inclusive_multicast.name = 'inclusive_multicast'


                        class InclusiveMulticast(object):
                            """
                            L2VPN EVPN IMCAST table
                            
                            .. attribute:: ethernet_tag
                            
                            	Ethernet Tag
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: ethernet_tag_xr
                            
                            	Ethernet Tag
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: evi
                            
                            	EVPN id
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: evi_xr
                            
                            	E\-VPN id
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: is_local_entry
                            
                            	Local entry
                            	**type**\:  bool
                            
                            .. attribute:: next_hop
                            
                            	IP of nexthop
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: originating_ip
                            
                            	Originating IP
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: originating_ip_xr
                            
                            	Originating IP
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: output_label
                            
                            	Output label
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.ethernet_tag = None
                                self.ethernet_tag_xr = None
                                self.evi = None
                                self.evi_xr = None
                                self.is_local_entry = None
                                self.next_hop = None
                                self.originating_ip = None
                                self.originating_ip_xr = None
                                self.output_label = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:inclusive-multicast'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.ethernet_tag is not None:
                                    return True

                                if self.ethernet_tag_xr is not None:
                                    return True

                                if self.evi is not None:
                                    return True

                                if self.evi_xr is not None:
                                    return True

                                if self.is_local_entry is not None:
                                    return True

                                if self.next_hop is not None:
                                    return True

                                if self.originating_ip is not None:
                                    return True

                                if self.originating_ip_xr is not None:
                                    return True

                                if self.output_label is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                                return meta._meta_table['Evpn.Nodes.Node.EviDetail.EviChildren.InclusiveMulticasts.InclusiveMulticast']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:inclusive-multicasts'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.inclusive_multicast is not None:
                                for child_ref in self.inclusive_multicast:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                            return meta._meta_table['Evpn.Nodes.Node.EviDetail.EviChildren.InclusiveMulticasts']['meta_info']


                    class RouteTargets(object):
                        """
                        L2VPN EVPN EVI RT Child Table
                        
                        .. attribute:: route_target
                        
                        	L2VPN EVPN EVI RT Table
                        	**type**\: list of    :py:class:`RouteTarget <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets.RouteTarget>`
                        
                        

                        """

                        _prefix = 'evpn-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.route_target = YList()
                            self.route_target.parent = self
                            self.route_target.name = 'route_target'


                        class RouteTarget(object):
                            """
                            L2VPN EVPN EVI RT Table
                            
                            .. attribute:: addr_index
                            
                            	RT IP Index
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: address
                            
                            	RT IPv4 Address
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: as_
                            
                            	Two or Four byte AS Number
                            	**type**\:  int
                            
                            	**range:** 1..4294967295
                            
                            .. attribute:: as_index
                            
                            	RT AS Index
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: bd_name
                            
                            	Bridge Domain Name
                            	**type**\:  str
                            
                            .. attribute:: evi
                            
                            	EVPN id
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: evi_xr
                            
                            	VPN ID
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: format
                            
                            	Format of the route target
                            	**type**\:   :py:class:`BgpRouteTargetFormatEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.BgpRouteTargetFormatEnum>`
                            
                            .. attribute:: role
                            
                            	Role of the route target
                            	**type**\:   :py:class:`BgpRouteTargetRoleEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.BgpRouteTargetRoleEnum>`
                            
                            .. attribute:: route_target
                            
                            	Route Target
                            	**type**\:   :py:class:`RouteTarget_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_>`
                            
                            .. attribute:: route_target_role
                            
                            	RT Role
                            	**type**\:   :py:class:`L2VpnAdRtRoleEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2VpnAdRtRoleEnum>`
                            
                            .. attribute:: route_target_stitching
                            
                            	RT Stitching
                            	**type**\:  bool
                            
                            .. attribute:: type
                            
                            	Type of the route target
                            	**type**\:   :py:class:`BgpRouteTargetEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.BgpRouteTargetEnum>`
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.addr_index = None
                                self.address = None
                                self.as_ = None
                                self.as_index = None
                                self.bd_name = None
                                self.evi = None
                                self.evi_xr = None
                                self.format = None
                                self.role = None
                                self.route_target = Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_()
                                self.route_target.parent = self
                                self.route_target_role = None
                                self.route_target_stitching = None
                                self.type = None


                            class RouteTarget_(object):
                                """
                                Route Target
                                
                                .. attribute:: es_import
                                
                                	es import
                                	**type**\:   :py:class:`EsImport <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.EsImport>`
                                
                                .. attribute:: four_byte_as
                                
                                	four byte as
                                	**type**\:   :py:class:`FourByteAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.FourByteAs>`
                                
                                .. attribute:: rt
                                
                                	RT
                                	**type**\:   :py:class:`L2VpnAdRtEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2VpnAdRtEnum>`
                                
                                .. attribute:: two_byte_as
                                
                                	two byte as
                                	**type**\:   :py:class:`TwoByteAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.TwoByteAs>`
                                
                                .. attribute:: v4_addr
                                
                                	v4 addr
                                	**type**\:   :py:class:`V4Addr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.V4Addr>`
                                
                                

                                """

                                _prefix = 'evpn-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.es_import = Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.EsImport()
                                    self.es_import.parent = self
                                    self.four_byte_as = Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.FourByteAs()
                                    self.four_byte_as.parent = self
                                    self.rt = None
                                    self.two_byte_as = Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.TwoByteAs()
                                    self.two_byte_as.parent = self
                                    self.v4_addr = Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.V4Addr()
                                    self.v4_addr.parent = self


                                class TwoByteAs(object):
                                    """
                                    two byte as
                                    
                                    .. attribute:: four_byte_index
                                    
                                    	4 Byte Index
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: two_byte_as
                                    
                                    	2 Byte AS Number
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    

                                    """

                                    _prefix = 'evpn-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.four_byte_index = None
                                        self.two_byte_as = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:two-byte-as'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.four_byte_index is not None:
                                            return True

                                        if self.two_byte_as is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                                        return meta._meta_table['Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.TwoByteAs']['meta_info']


                                class FourByteAs(object):
                                    """
                                    four byte as
                                    
                                    .. attribute:: four_byte_as
                                    
                                    	4 Byte AS Number
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: two_byte_index
                                    
                                    	2 Byte Index
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    

                                    """

                                    _prefix = 'evpn-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.four_byte_as = None
                                        self.two_byte_index = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:four-byte-as'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.four_byte_as is not None:
                                            return True

                                        if self.two_byte_index is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                                        return meta._meta_table['Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.FourByteAs']['meta_info']


                                class V4Addr(object):
                                    """
                                    v4 addr
                                    
                                    .. attribute:: ipv4_address
                                    
                                    	IPv4 Address
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: two_byte_index
                                    
                                    	2 Byte Index
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    

                                    """

                                    _prefix = 'evpn-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.ipv4_address = None
                                        self.two_byte_index = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:v4-addr'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.ipv4_address is not None:
                                            return True

                                        if self.two_byte_index is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                                        return meta._meta_table['Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.V4Addr']['meta_info']


                                class EsImport(object):
                                    """
                                    es import
                                    
                                    .. attribute:: high_bytes
                                    
                                    	Top 4 bytes of ES Import
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: low_bytes
                                    
                                    	Low 2 bytes of ES Import
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    

                                    """

                                    _prefix = 'evpn-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.high_bytes = None
                                        self.low_bytes = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:es-import'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.high_bytes is not None:
                                            return True

                                        if self.low_bytes is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                                        return meta._meta_table['Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.EsImport']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:route-target'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.es_import is not None and self.es_import._has_data():
                                        return True

                                    if self.four_byte_as is not None and self.four_byte_as._has_data():
                                        return True

                                    if self.rt is not None:
                                        return True

                                    if self.two_byte_as is not None and self.two_byte_as._has_data():
                                        return True

                                    if self.v4_addr is not None and self.v4_addr._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                                    return meta._meta_table['Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:route-target'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.addr_index is not None:
                                    return True

                                if self.address is not None:
                                    return True

                                if self.as_ is not None:
                                    return True

                                if self.as_index is not None:
                                    return True

                                if self.bd_name is not None:
                                    return True

                                if self.evi is not None:
                                    return True

                                if self.evi_xr is not None:
                                    return True

                                if self.format is not None:
                                    return True

                                if self.role is not None:
                                    return True

                                if self.route_target is not None and self.route_target._has_data():
                                    return True

                                if self.route_target_role is not None:
                                    return True

                                if self.route_target_stitching is not None:
                                    return True

                                if self.type is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                                return meta._meta_table['Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets.RouteTarget']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:route-targets'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.route_target is not None:
                                for child_ref in self.route_target:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                            return meta._meta_table['Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets']['meta_info']


                    class Macs(object):
                        """
                        L2VPN EVPN EVI MAC table
                        
                        .. attribute:: mac
                        
                        	L2VPN EVPN MAC table
                        	**type**\: list of    :py:class:`Mac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.EviChildren.Macs.Mac>`
                        
                        

                        """

                        _prefix = 'evpn-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.mac = YList()
                            self.mac.parent = self
                            self.mac.name = 'mac'


                        class Mac(object):
                            """
                            L2VPN EVPN MAC table
                            
                            .. attribute:: esi_port_key
                            
                            	ESI port key
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: ethernet_tag
                            
                            	Ethernet Tag ID
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: ethernet_tag_xr
                            
                            	Ethernet Tag
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: evi
                            
                            	EVPN id
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: internal_label
                            
                            	MPLS Internal Label
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: ip_address
                            
                            	IP Address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: ip_address_xr
                            
                            	IP address (v6 format)
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: is_local_mac
                            
                            	Indication of MAC being locally generated
                            	**type**\:  bool
                            
                            .. attribute:: is_remote_mac
                            
                            	Indication of MAC being remotely generated
                            	**type**\:  bool
                            
                            .. attribute:: is_static
                            
                            	Indication if MAC is statically configured
                            	**type**\:  bool
                            
                            .. attribute:: learned_bridge_port_name
                            
                            	Port the MAC was learned on
                            	**type**\:  str
                            
                            .. attribute:: local_encap_type
                            
                            	Encap type of local MAC
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: local_ethernet_segment_identifier
                            
                            	Local Ethernet Segment id
                            	**type**\:  list of int
                            
                            	**range:** 0..255
                            
                            .. attribute:: local_label
                            
                            	Associated local label
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: local_seq_id
                            
                            	local seq id
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mac_address
                            
                            	MAC address
                            	**type**\:  str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            .. attribute:: mac_address_xr
                            
                            	MAC address
                            	**type**\:  str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            .. attribute:: mac_flush_received
                            
                            	Number of flushes received 
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: mac_flush_requested
                            
                            	Number of flushes requested 
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: num_paths
                            
                            	 Number of items in path list buffer
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: path_buffer
                            
                            	Path List Buffer
                            	**type**\: list of    :py:class:`PathBuffer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.EviChildren.Macs.Mac.PathBuffer>`
                            
                            .. attribute:: remote_encap_type
                            
                            	Encap type of remote MAC
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: remote_ethernet_segment_identifier
                            
                            	Remote Ethernet Segment id
                            	**type**\:  list of int
                            
                            	**range:** 0..255
                            
                            .. attribute:: remote_seq_id
                            
                            	remote seq id
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: resolved
                            
                            	Internal Label has resolved per\-ES EAD and per\-EVI EAD or MAC routes
                            	**type**\:  bool
                            
                            .. attribute:: soo_nexthop
                            
                            	SOO nexthop (v6 format)
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.esi_port_key = None
                                self.ethernet_tag = None
                                self.ethernet_tag_xr = None
                                self.evi = None
                                self.internal_label = None
                                self.ip_address = None
                                self.ip_address_xr = None
                                self.is_local_mac = None
                                self.is_remote_mac = None
                                self.is_static = None
                                self.learned_bridge_port_name = None
                                self.local_encap_type = None
                                self.local_ethernet_segment_identifier = YLeafList()
                                self.local_ethernet_segment_identifier.parent = self
                                self.local_ethernet_segment_identifier.name = 'local_ethernet_segment_identifier'
                                self.local_label = None
                                self.local_seq_id = None
                                self.mac_address = None
                                self.mac_address_xr = None
                                self.mac_flush_received = None
                                self.mac_flush_requested = None
                                self.num_paths = None
                                self.path_buffer = YList()
                                self.path_buffer.parent = self
                                self.path_buffer.name = 'path_buffer'
                                self.remote_encap_type = None
                                self.remote_ethernet_segment_identifier = YLeafList()
                                self.remote_ethernet_segment_identifier.parent = self
                                self.remote_ethernet_segment_identifier.name = 'remote_ethernet_segment_identifier'
                                self.remote_seq_id = None
                                self.resolved = None
                                self.soo_nexthop = None


                            class PathBuffer(object):
                                """
                                Path List Buffer
                                
                                .. attribute:: next_hop
                                
                                	Next\-hop IP address (v6 format)
                                	**type**\:  str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: output_label
                                
                                	Output Label
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'evpn-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.next_hop = None
                                    self.output_label = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:path-buffer'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.next_hop is not None:
                                        return True

                                    if self.output_label is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                                    return meta._meta_table['Evpn.Nodes.Node.EviDetail.EviChildren.Macs.Mac.PathBuffer']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:mac'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.esi_port_key is not None:
                                    return True

                                if self.ethernet_tag is not None:
                                    return True

                                if self.ethernet_tag_xr is not None:
                                    return True

                                if self.evi is not None:
                                    return True

                                if self.internal_label is not None:
                                    return True

                                if self.ip_address is not None:
                                    return True

                                if self.ip_address_xr is not None:
                                    return True

                                if self.is_local_mac is not None:
                                    return True

                                if self.is_remote_mac is not None:
                                    return True

                                if self.is_static is not None:
                                    return True

                                if self.learned_bridge_port_name is not None:
                                    return True

                                if self.local_encap_type is not None:
                                    return True

                                if self.local_ethernet_segment_identifier is not None:
                                    for child in self.local_ethernet_segment_identifier:
                                        if child is not None:
                                            return True

                                if self.local_label is not None:
                                    return True

                                if self.local_seq_id is not None:
                                    return True

                                if self.mac_address is not None:
                                    return True

                                if self.mac_address_xr is not None:
                                    return True

                                if self.mac_flush_received is not None:
                                    return True

                                if self.mac_flush_requested is not None:
                                    return True

                                if self.num_paths is not None:
                                    return True

                                if self.path_buffer is not None:
                                    for child_ref in self.path_buffer:
                                        if child_ref._has_data():
                                            return True

                                if self.remote_encap_type is not None:
                                    return True

                                if self.remote_ethernet_segment_identifier is not None:
                                    for child in self.remote_ethernet_segment_identifier:
                                        if child is not None:
                                            return True

                                if self.remote_seq_id is not None:
                                    return True

                                if self.resolved is not None:
                                    return True

                                if self.soo_nexthop is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                                return meta._meta_table['Evpn.Nodes.Node.EviDetail.EviChildren.Macs.Mac']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:macs'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.mac is not None:
                                for child_ref in self.mac:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                            return meta._meta_table['Evpn.Nodes.Node.EviDetail.EviChildren.Macs']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:evi-children'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.ethernet_auto_discoveries is not None and self.ethernet_auto_discoveries._has_data():
                            return True

                        if self.inclusive_multicasts is not None and self.inclusive_multicasts._has_data():
                            return True

                        if self.macs is not None and self.macs._has_data():
                            return True

                        if self.neighbors is not None and self.neighbors._has_data():
                            return True

                        if self.route_targets is not None and self.route_targets._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                        return meta._meta_table['Evpn.Nodes.Node.EviDetail.EviChildren']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:evi-detail'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.elements is not None and self.elements._has_data():
                        return True

                    if self.evi_children is not None and self.evi_children._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                    return meta._meta_table['Evpn.Nodes.Node.EviDetail']['meta_info']


            class EthernetSegments(object):
                """
                EVPN Ethernet\-Segment Table
                
                .. attribute:: ethernet_segment
                
                	EVPN Ethernet\-Segment Entry
                	**type**\: list of    :py:class:`EthernetSegment <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EthernetSegments.EthernetSegment>`
                
                

                """

                _prefix = 'evpn-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.ethernet_segment = YList()
                    self.ethernet_segment.parent = self
                    self.ethernet_segment.name = 'ethernet_segment'


                class EthernetSegment(object):
                    """
                    EVPN Ethernet\-Segment Entry
                    
                    .. attribute:: elected_d_fs
                    
                    	Count of service carving results \- elected
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: es_bgp_gates
                    
                    	ES BGP Gates
                    	**type**\:  str
                    
                    .. attribute:: es_l2fib_gates
                    
                    	ES L2FIB Gates
                    	**type**\:  str
                    
                    .. attribute:: esi1
                    
                    	ES id (part 1/5)
                    	**type**\:  str
                    
                    	**pattern:** [0\-9a\-fA\-F]{1,8}
                    
                    .. attribute:: esi2
                    
                    	ES id (part 2/5)
                    	**type**\:  str
                    
                    	**pattern:** [0\-9a\-fA\-F]{1,8}
                    
                    .. attribute:: esi3
                    
                    	ES id (part 3/5)
                    	**type**\:  str
                    
                    	**pattern:** [0\-9a\-fA\-F]{1,8}
                    
                    .. attribute:: esi4
                    
                    	ES id (part 4/5)
                    	**type**\:  str
                    
                    	**pattern:** [0\-9a\-fA\-F]{1,8}
                    
                    .. attribute:: esi5
                    
                    	ES id (part 5/5)
                    	**type**\:  str
                    
                    	**pattern:** [0\-9a\-fA\-F]{1,8}
                    
                    .. attribute:: esi_type
                    
                    	ESI Type
                    	**type**\:   :py:class:`L2VpnEvpnEsiEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2VpnEvpnEsiEnum>`
                    
                    .. attribute:: ethernet_segment_identifier
                    
                    	Ethernet Segment id
                    	**type**\:  list of int
                    
                    	**range:** 0..255
                    
                    .. attribute:: ethernet_segment_name
                    
                    	Ethernet Segment Name
                    	**type**\:  str
                    
                    .. attribute:: ethernet_segment_state
                    
                    	State of the ethernet segment
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: force_single_home
                    
                    	Ethernet\-Segment forced to single home
                    	**type**\:  bool
                    
                    .. attribute:: forwarder_ports
                    
                    	Count of Forwarders (AC, AC PW, VFI PW)
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: if_handle
                    
                    	Main port ifhandle
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: interface_name
                    
                    	Interface
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: load_balance_mode_config
                    
                    	Configured load balancing mode
                    	**type**\:   :py:class:`L2VpnEvpnLbModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2VpnEvpnLbModeEnum>`
                    
                    .. attribute:: load_balance_mode_is_default
                    
                    	Load balancing mode is default
                    	**type**\:  bool
                    
                    .. attribute:: load_balance_mode_oper
                    
                    	Operational load balancing mode
                    	**type**\:   :py:class:`L2VpnEvpnLbModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2VpnEvpnLbModeEnum>`
                    
                    .. attribute:: local_split_horizon_group_label
                    
                    	Local split horizon group label
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: mac_flushing_mode_config
                    
                    	Configured MAC Flushing mode
                    	**type**\:   :py:class:`L2VpnEvpnMfModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2VpnEvpnMfModeEnum>`
                    
                    .. attribute:: main_port_mac
                    
                    	Main Port MAC Address
                    	**type**\:  str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: main_port_role
                    
                    	Main port redundancy group role
                    	**type**\:   :py:class:`L2VpnRgStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2VpnRgStateEnum>`
                    
                    .. attribute:: mp_protected
                    
                    	MP is protected and not under EVPN control
                    	**type**\:  bool
                    
                    .. attribute:: next_hop
                    
                    	List of nexthop IPv6 addresses
                    	**type**\: list of    :py:class:`NextHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EthernetSegments.EthernetSegment.NextHop>`
                    
                    .. attribute:: not_config_d_fs
                    
                    	Count of service carving results \- missing config detected
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: not_elected_d_fs
                    
                    	Count of service carving results \- not elected
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_up_p_ws
                    
                    	Number of PWs in Up state
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: peering_timer
                    
                    	Configured timer for triggering DF election (seconds)
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: peering_timer_left
                    
                    	Milliseconds left on DF election timer
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: millisecond
                    
                    .. attribute:: primary_service
                    
                    	List of Primary services ESI/I\-SIDs
                    	**type**\:  list of int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: primary_services_input
                    
                    	Input string of Primary services ESI/I\-SIDs
                    	**type**\:  str
                    
                    .. attribute:: recovery_timer
                    
                    	Configured timer for (STP) recovery (seconds)
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: recovery_timer_left
                    
                    	Milliseconds left on (STP) recovery timer
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: millisecond
                    
                    .. attribute:: remote_split_horizon_group_label
                    
                    	Remote split horizon group labels
                    	**type**\: list of    :py:class:`RemoteSplitHorizonGroupLabel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EthernetSegments.EthernetSegment.RemoteSplitHorizonGroupLabel>`
                    
                    .. attribute:: route_target
                    
                    	ES\-Import Route Target
                    	**type**\:  str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: rt_origin
                    
                    	Origin of operational ES\-Import RT
                    	**type**\:   :py:class:`L2VpnEvpnRtOriginEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2VpnEvpnRtOriginEnum>`
                    
                    .. attribute:: secondary_service
                    
                    	List of Secondary services ESI/I\-SIDs
                    	**type**\:  list of int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: secondary_services_input
                    
                    	Input string of Secondary services ESI/I\-SIDs
                    	**type**\:  str
                    
                    .. attribute:: service_carving_mode
                    
                    	Service carving mode
                    	**type**\:   :py:class:`L2VpnEvpnScModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2VpnEvpnScModeEnum>`
                    
                    .. attribute:: service_carving_result
                    
                    	Service carving results
                    	**type**\:  list of int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: service_carving_type
                    
                    	Service Carving Type
                    	**type**\:   :py:class:`L2VpnEvpnScEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2VpnEvpnScEnum>`
                    
                    .. attribute:: source_mac_oper
                    
                    	Operational Source MAC address
                    	**type**\:  str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: source_mac_origin
                    
                    	Origin of operational source MAC address
                    	**type**\:   :py:class:`L2VpnEvpnSmacSrcEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2VpnEvpnSmacSrcEnum>`
                    
                    

                    """

                    _prefix = 'evpn-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.elected_d_fs = None
                        self.es_bgp_gates = None
                        self.es_l2fib_gates = None
                        self.esi1 = None
                        self.esi2 = None
                        self.esi3 = None
                        self.esi4 = None
                        self.esi5 = None
                        self.esi_type = None
                        self.ethernet_segment_identifier = YLeafList()
                        self.ethernet_segment_identifier.parent = self
                        self.ethernet_segment_identifier.name = 'ethernet_segment_identifier'
                        self.ethernet_segment_name = None
                        self.ethernet_segment_state = None
                        self.force_single_home = None
                        self.forwarder_ports = None
                        self.if_handle = None
                        self.interface_name = None
                        self.load_balance_mode_config = None
                        self.load_balance_mode_is_default = None
                        self.load_balance_mode_oper = None
                        self.local_split_horizon_group_label = None
                        self.mac_flushing_mode_config = None
                        self.main_port_mac = None
                        self.main_port_role = None
                        self.mp_protected = None
                        self.next_hop = YList()
                        self.next_hop.parent = self
                        self.next_hop.name = 'next_hop'
                        self.not_config_d_fs = None
                        self.not_elected_d_fs = None
                        self.num_up_p_ws = None
                        self.peering_timer = None
                        self.peering_timer_left = None
                        self.primary_service = YLeafList()
                        self.primary_service.parent = self
                        self.primary_service.name = 'primary_service'
                        self.primary_services_input = None
                        self.recovery_timer = None
                        self.recovery_timer_left = None
                        self.remote_split_horizon_group_label = YList()
                        self.remote_split_horizon_group_label.parent = self
                        self.remote_split_horizon_group_label.name = 'remote_split_horizon_group_label'
                        self.route_target = None
                        self.rt_origin = None
                        self.secondary_service = YLeafList()
                        self.secondary_service.parent = self
                        self.secondary_service.name = 'secondary_service'
                        self.secondary_services_input = None
                        self.service_carving_mode = None
                        self.service_carving_result = YLeafList()
                        self.service_carving_result.parent = self
                        self.service_carving_result.name = 'service_carving_result'
                        self.service_carving_type = None
                        self.source_mac_oper = None
                        self.source_mac_origin = None


                    class NextHop(object):
                        """
                        List of nexthop IPv6 addresses
                        
                        .. attribute:: next_hop
                        
                        	Next\-hop IP address (v6 format)
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'evpn-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.next_hop = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:next-hop'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.next_hop is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                            return meta._meta_table['Evpn.Nodes.Node.EthernetSegments.EthernetSegment.NextHop']['meta_info']


                    class RemoteSplitHorizonGroupLabel(object):
                        """
                        Remote split horizon group labels
                        
                        .. attribute:: label
                        
                        	Split horizon label associated with next\-hop address
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: next_hop
                        
                        	Next\-hop IP address (v6 format)
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'evpn-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.label = None
                            self.next_hop = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:remote-split-horizon-group-label'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.label is not None:
                                return True

                            if self.next_hop is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                            return meta._meta_table['Evpn.Nodes.Node.EthernetSegments.EthernetSegment.RemoteSplitHorizonGroupLabel']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:ethernet-segment'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.elected_d_fs is not None:
                            return True

                        if self.es_bgp_gates is not None:
                            return True

                        if self.es_l2fib_gates is not None:
                            return True

                        if self.esi1 is not None:
                            return True

                        if self.esi2 is not None:
                            return True

                        if self.esi3 is not None:
                            return True

                        if self.esi4 is not None:
                            return True

                        if self.esi5 is not None:
                            return True

                        if self.esi_type is not None:
                            return True

                        if self.ethernet_segment_identifier is not None:
                            for child in self.ethernet_segment_identifier:
                                if child is not None:
                                    return True

                        if self.ethernet_segment_name is not None:
                            return True

                        if self.ethernet_segment_state is not None:
                            return True

                        if self.force_single_home is not None:
                            return True

                        if self.forwarder_ports is not None:
                            return True

                        if self.if_handle is not None:
                            return True

                        if self.interface_name is not None:
                            return True

                        if self.load_balance_mode_config is not None:
                            return True

                        if self.load_balance_mode_is_default is not None:
                            return True

                        if self.load_balance_mode_oper is not None:
                            return True

                        if self.local_split_horizon_group_label is not None:
                            return True

                        if self.mac_flushing_mode_config is not None:
                            return True

                        if self.main_port_mac is not None:
                            return True

                        if self.main_port_role is not None:
                            return True

                        if self.mp_protected is not None:
                            return True

                        if self.next_hop is not None:
                            for child_ref in self.next_hop:
                                if child_ref._has_data():
                                    return True

                        if self.not_config_d_fs is not None:
                            return True

                        if self.not_elected_d_fs is not None:
                            return True

                        if self.num_up_p_ws is not None:
                            return True

                        if self.peering_timer is not None:
                            return True

                        if self.peering_timer_left is not None:
                            return True

                        if self.primary_service is not None:
                            for child in self.primary_service:
                                if child is not None:
                                    return True

                        if self.primary_services_input is not None:
                            return True

                        if self.recovery_timer is not None:
                            return True

                        if self.recovery_timer_left is not None:
                            return True

                        if self.remote_split_horizon_group_label is not None:
                            for child_ref in self.remote_split_horizon_group_label:
                                if child_ref._has_data():
                                    return True

                        if self.route_target is not None:
                            return True

                        if self.rt_origin is not None:
                            return True

                        if self.secondary_service is not None:
                            for child in self.secondary_service:
                                if child is not None:
                                    return True

                        if self.secondary_services_input is not None:
                            return True

                        if self.service_carving_mode is not None:
                            return True

                        if self.service_carving_result is not None:
                            for child in self.service_carving_result:
                                if child is not None:
                                    return True

                        if self.service_carving_type is not None:
                            return True

                        if self.source_mac_oper is not None:
                            return True

                        if self.source_mac_origin is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                        return meta._meta_table['Evpn.Nodes.Node.EthernetSegments.EthernetSegment']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:ethernet-segments'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.ethernet_segment is not None:
                        for child_ref in self.ethernet_segment:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                    return meta._meta_table['Evpn.Nodes.Node.EthernetSegments']['meta_info']


            class AcIds(object):
                """
                EVPN AC ID table
                
                .. attribute:: ac_id
                
                	EVPN AC ID table
                	**type**\: list of    :py:class:`AcId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.AcIds.AcId>`
                
                

                """

                _prefix = 'evpn-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.ac_id = YList()
                    self.ac_id.parent = self
                    self.ac_id.name = 'ac_id'


                class AcId(object):
                    """
                    EVPN AC ID table
                    
                    .. attribute:: ac_id
                    
                    	AC ID
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: evi
                    
                    	EVPN id
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: evi_xr
                    
                    	E\-VPN id
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: neighbor
                    
                    	Neighbor IP
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'evpn-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.ac_id = None
                        self.evi = None
                        self.evi_xr = None
                        self.neighbor = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:ac-id'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.ac_id is not None:
                            return True

                        if self.evi is not None:
                            return True

                        if self.evi_xr is not None:
                            return True

                        if self.neighbor is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                        return meta._meta_table['Evpn.Nodes.Node.AcIds.AcId']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:ac-ids'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.ac_id is not None:
                        for child_ref in self.ac_id:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                    return meta._meta_table['Evpn.Nodes.Node.AcIds']['meta_info']

            @property
            def _common_path(self):
                if self.node_id is None:
                    raise YPYModelError('Key property node_id is None')

                return '/Cisco-IOS-XR-evpn-oper:evpn/Cisco-IOS-XR-evpn-oper:nodes/Cisco-IOS-XR-evpn-oper:node[Cisco-IOS-XR-evpn-oper:node-id = ' + str(self.node_id) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.node_id is not None:
                    return True

                if self.ac_ids is not None and self.ac_ids._has_data():
                    return True

                if self.ethernet_segments is not None and self.ethernet_segments._has_data():
                    return True

                if self.evi_detail is not None and self.evi_detail._has_data():
                    return True

                if self.evis is not None and self.evis._has_data():
                    return True

                if self.summary is not None and self.summary._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                return meta._meta_table['Evpn.Nodes.Node']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-evpn-oper:evpn/Cisco-IOS-XR-evpn-oper:nodes'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.node is not None:
                for child_ref in self.node:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
            return meta._meta_table['Evpn.Nodes']['meta_info']


    class Active(object):
        """
        Active EVPN operational data
        
        .. attribute:: ac_ids
        
        	EVPN AC ID table
        	**type**\:   :py:class:`AcIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.AcIds>`
        
        .. attribute:: ethernet_segments
        
        	EVPN Ethernet\-Segment Table
        	**type**\:   :py:class:`EthernetSegments <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EthernetSegments>`
        
        .. attribute:: evi_detail
        
        	L2VPN EVI Detail Table
        	**type**\:   :py:class:`EviDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail>`
        
        .. attribute:: evis
        
        	L2VPN EVPN EVI Table
        	**type**\:   :py:class:`Evis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.Evis>`
        
        .. attribute:: summary
        
        	L2VPN EVPN Summary
        	**type**\:   :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.Summary>`
        
        

        """

        _prefix = 'evpn-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.ac_ids = Evpn.Active.AcIds()
            self.ac_ids.parent = self
            self.ethernet_segments = Evpn.Active.EthernetSegments()
            self.ethernet_segments.parent = self
            self.evi_detail = Evpn.Active.EviDetail()
            self.evi_detail.parent = self
            self.evis = Evpn.Active.Evis()
            self.evis.parent = self
            self.summary = Evpn.Active.Summary()
            self.summary.parent = self


        class Evis(object):
            """
            L2VPN EVPN EVI Table
            
            .. attribute:: evi
            
            	L2VPN EVPN EVI Entry
            	**type**\: list of    :py:class:`Evi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.Evis.Evi>`
            
            

            """

            _prefix = 'evpn-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.evi = YList()
                self.evi.parent = self
                self.evi.name = 'evi'


            class Evi(object):
                """
                L2VPN EVPN EVI Entry
                
                .. attribute:: evi  <key>
                
                	EVPN id
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: bd_name
                
                	Bridge domain name
                	**type**\:  str
                
                .. attribute:: evi_xr
                
                	E\-VPN id
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: type
                
                	Service Type
                	**type**\:   :py:class:`EvpnEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.EvpnEnum>`
                
                

                """

                _prefix = 'evpn-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.evi = None
                    self.bd_name = None
                    self.evi_xr = None
                    self.type = None

                @property
                def _common_path(self):
                    if self.evi is None:
                        raise YPYModelError('Key property evi is None')

                    return '/Cisco-IOS-XR-evpn-oper:evpn/Cisco-IOS-XR-evpn-oper:active/Cisco-IOS-XR-evpn-oper:evis/Cisco-IOS-XR-evpn-oper:evi[Cisco-IOS-XR-evpn-oper:evi = ' + str(self.evi) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.evi is not None:
                        return True

                    if self.bd_name is not None:
                        return True

                    if self.evi_xr is not None:
                        return True

                    if self.type is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                    return meta._meta_table['Evpn.Active.Evis.Evi']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-evpn-oper:evpn/Cisco-IOS-XR-evpn-oper:active/Cisco-IOS-XR-evpn-oper:evis'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.evi is not None:
                    for child_ref in self.evi:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                return meta._meta_table['Evpn.Active.Evis']['meta_info']


        class Summary(object):
            """
            L2VPN EVPN Summary
            
            .. attribute:: as_
            
            	BGP AS number
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: es_entries
            
            	Number of ES Entries in DB
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: es_global_mac_routes
            
            	Number of ES\:Global MAC Routes
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ev_is
            
            	Number of EVI DB Entries
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: global_source_mac
            
            	Global Source MAC Address
            	**type**\:  str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: l2rib_throttle
            
            	Send to L2RIB Throttled
            	**type**\:  bool
            
            .. attribute:: labels
            
            	Number of Internal Labels
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: local_ead_routes
            
            	Number of Local EAD Entries in DB
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: local_imcast_routes
            
            	Number of Local IMCAST Routes
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: local_ipv4_mac_routes
            
            	Number of Local IPv4 MAC\-IP Routes
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: local_ipv6_mac_routes
            
            	Number of Local IPv6 MAC\-IP Routes
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: local_mac_routes
            
            	Number of Local MAC Routes
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: logging_df_election_enabled
            
            	Logging EVPN Designated Forwarder changes enabled
            	**type**\:  bool
            
            .. attribute:: neighbor_entries
            
            	Number of neighbor Entries in DB
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: peering_time
            
            	EVPN ES Peering Time (seconds)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: second
            
            .. attribute:: recovery_time
            
            	EVPN ES Recovery Time (seconds)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: second
            
            .. attribute:: remote_ead_routes
            
            	Number of Remote EAD Entries in DB
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: remote_imcast_routes
            
            	Number of Remote IMCAST Routes
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: remote_ipv4_mac_routes
            
            	Number of Remote IPv4 MAC\-IP Routes
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: remote_ipv6_mac_routes
            
            	Number of Remote IPv6 MAC\-IP Routes
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: remote_mac_routes
            
            	Number of Remote MAC Routes
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: remote_soo_mac_routes
            
            	Number of Remote Soo MAC Routes
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: router_id
            
            	EVPN Router ID
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            

            """

            _prefix = 'evpn-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.as_ = None
                self.es_entries = None
                self.es_global_mac_routes = None
                self.ev_is = None
                self.global_source_mac = None
                self.l2rib_throttle = None
                self.labels = None
                self.local_ead_routes = None
                self.local_imcast_routes = None
                self.local_ipv4_mac_routes = None
                self.local_ipv6_mac_routes = None
                self.local_mac_routes = None
                self.logging_df_election_enabled = None
                self.neighbor_entries = None
                self.peering_time = None
                self.recovery_time = None
                self.remote_ead_routes = None
                self.remote_imcast_routes = None
                self.remote_ipv4_mac_routes = None
                self.remote_ipv6_mac_routes = None
                self.remote_mac_routes = None
                self.remote_soo_mac_routes = None
                self.router_id = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-evpn-oper:evpn/Cisco-IOS-XR-evpn-oper:active/Cisco-IOS-XR-evpn-oper:summary'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.as_ is not None:
                    return True

                if self.es_entries is not None:
                    return True

                if self.es_global_mac_routes is not None:
                    return True

                if self.ev_is is not None:
                    return True

                if self.global_source_mac is not None:
                    return True

                if self.l2rib_throttle is not None:
                    return True

                if self.labels is not None:
                    return True

                if self.local_ead_routes is not None:
                    return True

                if self.local_imcast_routes is not None:
                    return True

                if self.local_ipv4_mac_routes is not None:
                    return True

                if self.local_ipv6_mac_routes is not None:
                    return True

                if self.local_mac_routes is not None:
                    return True

                if self.logging_df_election_enabled is not None:
                    return True

                if self.neighbor_entries is not None:
                    return True

                if self.peering_time is not None:
                    return True

                if self.recovery_time is not None:
                    return True

                if self.remote_ead_routes is not None:
                    return True

                if self.remote_imcast_routes is not None:
                    return True

                if self.remote_ipv4_mac_routes is not None:
                    return True

                if self.remote_ipv6_mac_routes is not None:
                    return True

                if self.remote_mac_routes is not None:
                    return True

                if self.remote_soo_mac_routes is not None:
                    return True

                if self.router_id is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                return meta._meta_table['Evpn.Active.Summary']['meta_info']


        class EviDetail(object):
            """
            L2VPN EVI Detail Table
            
            .. attribute:: elements
            
            	EVI BGP RT Detail Info Elements
            	**type**\:   :py:class:`Elements <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.Elements>`
            
            .. attribute:: evi_children
            
            	Container for all EVI detail info
            	**type**\:   :py:class:`EviChildren <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.EviChildren>`
            
            

            """

            _prefix = 'evpn-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.elements = Evpn.Active.EviDetail.Elements()
                self.elements.parent = self
                self.evi_children = Evpn.Active.EviDetail.EviChildren()
                self.evi_children.parent = self


            class Elements(object):
                """
                EVI BGP RT Detail Info Elements
                
                .. attribute:: element
                
                	EVI BGP RT Detail Info
                	**type**\: list of    :py:class:`Element <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.Elements.Element>`
                
                

                """

                _prefix = 'evpn-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.element = YList()
                    self.element.parent = self
                    self.element.name = 'element'


                class Element(object):
                    """
                    EVI BGP RT Detail Info
                    
                    .. attribute:: evi  <key>
                    
                    	EVPN id
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: advertise_mac
                    
                    	Advertise MAC\-only routes on this EVI
                    	**type**\:  bool
                    
                    .. attribute:: aliasing_disabled
                    
                    	Route Aliasing is disabled
                    	**type**\:  bool
                    
                    .. attribute:: bd_name
                    
                    	Bridge domain name
                    	**type**\:  str
                    
                    .. attribute:: cw_disable
                    
                    	Control\-Word Disable
                    	**type**\:  bool
                    
                    .. attribute:: description
                    
                    	EVI description
                    	**type**\:  str
                    
                    .. attribute:: evi_xr
                    
                    	E\-VPN id
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: flow_label
                    
                    	Flow Label Information
                    	**type**\:   :py:class:`FlowLabel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.Elements.Element.FlowLabel>`
                    
                    .. attribute:: forward_class
                    
                    	Forward Class attribute
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: multicast_label
                    
                    	Multicast Label
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rd_auto
                    
                    	Automatic Route Distingtuisher
                    	**type**\:   :py:class:`RdAuto <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.Elements.Element.RdAuto>`
                    
                    .. attribute:: rd_configured
                    
                    	Configured Route Distinguisher
                    	**type**\:   :py:class:`RdConfigured <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.Elements.Element.RdConfigured>`
                    
                    .. attribute:: reoriginate_disabled
                    
                    	Route Re\-origination is disabled
                    	**type**\:  bool
                    
                    .. attribute:: rt_auto
                    
                    	Automatic Route Target
                    	**type**\:   :py:class:`RtAuto <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.Elements.Element.RtAuto>`
                    
                    .. attribute:: rt_auto_stitching
                    
                    	Automatic Route Target Stitching
                    	**type**\:   :py:class:`RtAutoStitching <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.Elements.Element.RtAutoStitching>`
                    
                    .. attribute:: rt_export_block_set
                    
                    	Is Export RT None set
                    	**type**\:  bool
                    
                    .. attribute:: rt_import_block_set
                    
                    	Is Import RT None set
                    	**type**\:  bool
                    
                    .. attribute:: stitching
                    
                    	RT Stitching for MPLS Fabric is enabled
                    	**type**\:  bool
                    
                    .. attribute:: table_policy_name
                    
                    	Table\-policy Name
                    	**type**\:  str
                    
                    .. attribute:: type
                    
                    	Service Type
                    	**type**\:   :py:class:`EvpnEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.EvpnEnum>`
                    
                    .. attribute:: unicast_label
                    
                    	Unicast Label
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: unknown_unicast_flooding_disabled
                    
                    	Unknown\-unicast flooding is disabled
                    	**type**\:  bool
                    
                    

                    """

                    _prefix = 'evpn-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.evi = None
                        self.advertise_mac = None
                        self.aliasing_disabled = None
                        self.bd_name = None
                        self.cw_disable = None
                        self.description = None
                        self.evi_xr = None
                        self.flow_label = Evpn.Active.EviDetail.Elements.Element.FlowLabel()
                        self.flow_label.parent = self
                        self.forward_class = None
                        self.multicast_label = None
                        self.rd_auto = Evpn.Active.EviDetail.Elements.Element.RdAuto()
                        self.rd_auto.parent = self
                        self.rd_configured = Evpn.Active.EviDetail.Elements.Element.RdConfigured()
                        self.rd_configured.parent = self
                        self.reoriginate_disabled = None
                        self.rt_auto = Evpn.Active.EviDetail.Elements.Element.RtAuto()
                        self.rt_auto.parent = self
                        self.rt_auto_stitching = Evpn.Active.EviDetail.Elements.Element.RtAutoStitching()
                        self.rt_auto_stitching.parent = self
                        self.rt_export_block_set = None
                        self.rt_import_block_set = None
                        self.stitching = None
                        self.table_policy_name = None
                        self.type = None
                        self.unicast_label = None
                        self.unknown_unicast_flooding_disabled = None


                    class FlowLabel(object):
                        """
                        Flow Label Information
                        
                        .. attribute:: global_flow_label
                        
                        	Globally configured flow label
                        	**type**\:  bool
                        
                        .. attribute:: static_flow_label
                        
                        	Static flow label
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'evpn-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.global_flow_label = None
                            self.static_flow_label = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:flow-label'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.global_flow_label is not None:
                                return True

                            if self.static_flow_label is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                            return meta._meta_table['Evpn.Active.EviDetail.Elements.Element.FlowLabel']['meta_info']


                    class RdAuto(object):
                        """
                        Automatic Route Distingtuisher
                        
                        .. attribute:: auto
                        
                        	auto
                        	**type**\:   :py:class:`Auto <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.Elements.Element.RdAuto.Auto>`
                        
                        .. attribute:: four_byte_as
                        
                        	four byte as
                        	**type**\:   :py:class:`FourByteAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.Elements.Element.RdAuto.FourByteAs>`
                        
                        .. attribute:: rd
                        
                        	RD
                        	**type**\:   :py:class:`L2VpnAdRdEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2VpnAdRdEnum>`
                        
                        .. attribute:: two_byte_as
                        
                        	two byte as
                        	**type**\:   :py:class:`TwoByteAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.Elements.Element.RdAuto.TwoByteAs>`
                        
                        .. attribute:: v4_addr
                        
                        	v4 addr
                        	**type**\:   :py:class:`V4Addr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.Elements.Element.RdAuto.V4Addr>`
                        
                        

                        """

                        _prefix = 'evpn-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.auto = Evpn.Active.EviDetail.Elements.Element.RdAuto.Auto()
                            self.auto.parent = self
                            self.four_byte_as = Evpn.Active.EviDetail.Elements.Element.RdAuto.FourByteAs()
                            self.four_byte_as.parent = self
                            self.rd = None
                            self.two_byte_as = Evpn.Active.EviDetail.Elements.Element.RdAuto.TwoByteAs()
                            self.two_byte_as.parent = self
                            self.v4_addr = Evpn.Active.EviDetail.Elements.Element.RdAuto.V4Addr()
                            self.v4_addr.parent = self


                        class Auto(object):
                            """
                            auto
                            
                            .. attribute:: auto_index
                            
                            	Auto\-generated Index
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: router_id
                            
                            	BGP Router ID
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.auto_index = None
                                self.router_id = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:auto'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.auto_index is not None:
                                    return True

                                if self.router_id is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                                return meta._meta_table['Evpn.Active.EviDetail.Elements.Element.RdAuto.Auto']['meta_info']


                        class TwoByteAs(object):
                            """
                            two byte as
                            
                            .. attribute:: four_byte_index
                            
                            	4 Byte Index
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: two_byte_as
                            
                            	2 Byte AS Number
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.four_byte_index = None
                                self.two_byte_as = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:two-byte-as'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.four_byte_index is not None:
                                    return True

                                if self.two_byte_as is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                                return meta._meta_table['Evpn.Active.EviDetail.Elements.Element.RdAuto.TwoByteAs']['meta_info']


                        class FourByteAs(object):
                            """
                            four byte as
                            
                            .. attribute:: four_byte_as
                            
                            	4 Byte AS Number
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: two_byte_index
                            
                            	2 Byte Index
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.four_byte_as = None
                                self.two_byte_index = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:four-byte-as'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.four_byte_as is not None:
                                    return True

                                if self.two_byte_index is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                                return meta._meta_table['Evpn.Active.EviDetail.Elements.Element.RdAuto.FourByteAs']['meta_info']


                        class V4Addr(object):
                            """
                            v4 addr
                            
                            .. attribute:: ipv4_address
                            
                            	IPv4 Address
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: two_byte_index
                            
                            	2 Byte Index
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.ipv4_address = None
                                self.two_byte_index = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:v4-addr'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.ipv4_address is not None:
                                    return True

                                if self.two_byte_index is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                                return meta._meta_table['Evpn.Active.EviDetail.Elements.Element.RdAuto.V4Addr']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:rd-auto'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.auto is not None and self.auto._has_data():
                                return True

                            if self.four_byte_as is not None and self.four_byte_as._has_data():
                                return True

                            if self.rd is not None:
                                return True

                            if self.two_byte_as is not None and self.two_byte_as._has_data():
                                return True

                            if self.v4_addr is not None and self.v4_addr._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                            return meta._meta_table['Evpn.Active.EviDetail.Elements.Element.RdAuto']['meta_info']


                    class RdConfigured(object):
                        """
                        Configured Route Distinguisher
                        
                        .. attribute:: auto
                        
                        	auto
                        	**type**\:   :py:class:`Auto <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.Elements.Element.RdConfigured.Auto>`
                        
                        .. attribute:: four_byte_as
                        
                        	four byte as
                        	**type**\:   :py:class:`FourByteAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.Elements.Element.RdConfigured.FourByteAs>`
                        
                        .. attribute:: rd
                        
                        	RD
                        	**type**\:   :py:class:`L2VpnAdRdEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2VpnAdRdEnum>`
                        
                        .. attribute:: two_byte_as
                        
                        	two byte as
                        	**type**\:   :py:class:`TwoByteAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.Elements.Element.RdConfigured.TwoByteAs>`
                        
                        .. attribute:: v4_addr
                        
                        	v4 addr
                        	**type**\:   :py:class:`V4Addr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.Elements.Element.RdConfigured.V4Addr>`
                        
                        

                        """

                        _prefix = 'evpn-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.auto = Evpn.Active.EviDetail.Elements.Element.RdConfigured.Auto()
                            self.auto.parent = self
                            self.four_byte_as = Evpn.Active.EviDetail.Elements.Element.RdConfigured.FourByteAs()
                            self.four_byte_as.parent = self
                            self.rd = None
                            self.two_byte_as = Evpn.Active.EviDetail.Elements.Element.RdConfigured.TwoByteAs()
                            self.two_byte_as.parent = self
                            self.v4_addr = Evpn.Active.EviDetail.Elements.Element.RdConfigured.V4Addr()
                            self.v4_addr.parent = self


                        class Auto(object):
                            """
                            auto
                            
                            .. attribute:: auto_index
                            
                            	Auto\-generated Index
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: router_id
                            
                            	BGP Router ID
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.auto_index = None
                                self.router_id = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:auto'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.auto_index is not None:
                                    return True

                                if self.router_id is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                                return meta._meta_table['Evpn.Active.EviDetail.Elements.Element.RdConfigured.Auto']['meta_info']


                        class TwoByteAs(object):
                            """
                            two byte as
                            
                            .. attribute:: four_byte_index
                            
                            	4 Byte Index
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: two_byte_as
                            
                            	2 Byte AS Number
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.four_byte_index = None
                                self.two_byte_as = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:two-byte-as'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.four_byte_index is not None:
                                    return True

                                if self.two_byte_as is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                                return meta._meta_table['Evpn.Active.EviDetail.Elements.Element.RdConfigured.TwoByteAs']['meta_info']


                        class FourByteAs(object):
                            """
                            four byte as
                            
                            .. attribute:: four_byte_as
                            
                            	4 Byte AS Number
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: two_byte_index
                            
                            	2 Byte Index
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.four_byte_as = None
                                self.two_byte_index = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:four-byte-as'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.four_byte_as is not None:
                                    return True

                                if self.two_byte_index is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                                return meta._meta_table['Evpn.Active.EviDetail.Elements.Element.RdConfigured.FourByteAs']['meta_info']


                        class V4Addr(object):
                            """
                            v4 addr
                            
                            .. attribute:: ipv4_address
                            
                            	IPv4 Address
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: two_byte_index
                            
                            	2 Byte Index
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.ipv4_address = None
                                self.two_byte_index = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:v4-addr'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.ipv4_address is not None:
                                    return True

                                if self.two_byte_index is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                                return meta._meta_table['Evpn.Active.EviDetail.Elements.Element.RdConfigured.V4Addr']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:rd-configured'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.auto is not None and self.auto._has_data():
                                return True

                            if self.four_byte_as is not None and self.four_byte_as._has_data():
                                return True

                            if self.rd is not None:
                                return True

                            if self.two_byte_as is not None and self.two_byte_as._has_data():
                                return True

                            if self.v4_addr is not None and self.v4_addr._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                            return meta._meta_table['Evpn.Active.EviDetail.Elements.Element.RdConfigured']['meta_info']


                    class RtAuto(object):
                        """
                        Automatic Route Target
                        
                        .. attribute:: es_import
                        
                        	es import
                        	**type**\:   :py:class:`EsImport <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.Elements.Element.RtAuto.EsImport>`
                        
                        .. attribute:: four_byte_as
                        
                        	four byte as
                        	**type**\:   :py:class:`FourByteAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.Elements.Element.RtAuto.FourByteAs>`
                        
                        .. attribute:: rt
                        
                        	RT
                        	**type**\:   :py:class:`L2VpnAdRtEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2VpnAdRtEnum>`
                        
                        .. attribute:: two_byte_as
                        
                        	two byte as
                        	**type**\:   :py:class:`TwoByteAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.Elements.Element.RtAuto.TwoByteAs>`
                        
                        .. attribute:: v4_addr
                        
                        	v4 addr
                        	**type**\:   :py:class:`V4Addr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.Elements.Element.RtAuto.V4Addr>`
                        
                        

                        """

                        _prefix = 'evpn-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.es_import = Evpn.Active.EviDetail.Elements.Element.RtAuto.EsImport()
                            self.es_import.parent = self
                            self.four_byte_as = Evpn.Active.EviDetail.Elements.Element.RtAuto.FourByteAs()
                            self.four_byte_as.parent = self
                            self.rt = None
                            self.two_byte_as = Evpn.Active.EviDetail.Elements.Element.RtAuto.TwoByteAs()
                            self.two_byte_as.parent = self
                            self.v4_addr = Evpn.Active.EviDetail.Elements.Element.RtAuto.V4Addr()
                            self.v4_addr.parent = self


                        class TwoByteAs(object):
                            """
                            two byte as
                            
                            .. attribute:: four_byte_index
                            
                            	4 Byte Index
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: two_byte_as
                            
                            	2 Byte AS Number
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.four_byte_index = None
                                self.two_byte_as = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:two-byte-as'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.four_byte_index is not None:
                                    return True

                                if self.two_byte_as is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                                return meta._meta_table['Evpn.Active.EviDetail.Elements.Element.RtAuto.TwoByteAs']['meta_info']


                        class FourByteAs(object):
                            """
                            four byte as
                            
                            .. attribute:: four_byte_as
                            
                            	4 Byte AS Number
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: two_byte_index
                            
                            	2 Byte Index
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.four_byte_as = None
                                self.two_byte_index = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:four-byte-as'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.four_byte_as is not None:
                                    return True

                                if self.two_byte_index is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                                return meta._meta_table['Evpn.Active.EviDetail.Elements.Element.RtAuto.FourByteAs']['meta_info']


                        class V4Addr(object):
                            """
                            v4 addr
                            
                            .. attribute:: ipv4_address
                            
                            	IPv4 Address
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: two_byte_index
                            
                            	2 Byte Index
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.ipv4_address = None
                                self.two_byte_index = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:v4-addr'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.ipv4_address is not None:
                                    return True

                                if self.two_byte_index is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                                return meta._meta_table['Evpn.Active.EviDetail.Elements.Element.RtAuto.V4Addr']['meta_info']


                        class EsImport(object):
                            """
                            es import
                            
                            .. attribute:: high_bytes
                            
                            	Top 4 bytes of ES Import
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: low_bytes
                            
                            	Low 2 bytes of ES Import
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.high_bytes = None
                                self.low_bytes = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:es-import'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.high_bytes is not None:
                                    return True

                                if self.low_bytes is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                                return meta._meta_table['Evpn.Active.EviDetail.Elements.Element.RtAuto.EsImport']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:rt-auto'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.es_import is not None and self.es_import._has_data():
                                return True

                            if self.four_byte_as is not None and self.four_byte_as._has_data():
                                return True

                            if self.rt is not None:
                                return True

                            if self.two_byte_as is not None and self.two_byte_as._has_data():
                                return True

                            if self.v4_addr is not None and self.v4_addr._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                            return meta._meta_table['Evpn.Active.EviDetail.Elements.Element.RtAuto']['meta_info']


                    class RtAutoStitching(object):
                        """
                        Automatic Route Target Stitching
                        
                        .. attribute:: es_import
                        
                        	es import
                        	**type**\:   :py:class:`EsImport <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.Elements.Element.RtAutoStitching.EsImport>`
                        
                        .. attribute:: four_byte_as
                        
                        	four byte as
                        	**type**\:   :py:class:`FourByteAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.Elements.Element.RtAutoStitching.FourByteAs>`
                        
                        .. attribute:: rt
                        
                        	RT
                        	**type**\:   :py:class:`L2VpnAdRtEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2VpnAdRtEnum>`
                        
                        .. attribute:: two_byte_as
                        
                        	two byte as
                        	**type**\:   :py:class:`TwoByteAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.Elements.Element.RtAutoStitching.TwoByteAs>`
                        
                        .. attribute:: v4_addr
                        
                        	v4 addr
                        	**type**\:   :py:class:`V4Addr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.Elements.Element.RtAutoStitching.V4Addr>`
                        
                        

                        """

                        _prefix = 'evpn-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.es_import = Evpn.Active.EviDetail.Elements.Element.RtAutoStitching.EsImport()
                            self.es_import.parent = self
                            self.four_byte_as = Evpn.Active.EviDetail.Elements.Element.RtAutoStitching.FourByteAs()
                            self.four_byte_as.parent = self
                            self.rt = None
                            self.two_byte_as = Evpn.Active.EviDetail.Elements.Element.RtAutoStitching.TwoByteAs()
                            self.two_byte_as.parent = self
                            self.v4_addr = Evpn.Active.EviDetail.Elements.Element.RtAutoStitching.V4Addr()
                            self.v4_addr.parent = self


                        class TwoByteAs(object):
                            """
                            two byte as
                            
                            .. attribute:: four_byte_index
                            
                            	4 Byte Index
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: two_byte_as
                            
                            	2 Byte AS Number
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.four_byte_index = None
                                self.two_byte_as = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:two-byte-as'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.four_byte_index is not None:
                                    return True

                                if self.two_byte_as is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                                return meta._meta_table['Evpn.Active.EviDetail.Elements.Element.RtAutoStitching.TwoByteAs']['meta_info']


                        class FourByteAs(object):
                            """
                            four byte as
                            
                            .. attribute:: four_byte_as
                            
                            	4 Byte AS Number
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: two_byte_index
                            
                            	2 Byte Index
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.four_byte_as = None
                                self.two_byte_index = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:four-byte-as'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.four_byte_as is not None:
                                    return True

                                if self.two_byte_index is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                                return meta._meta_table['Evpn.Active.EviDetail.Elements.Element.RtAutoStitching.FourByteAs']['meta_info']


                        class V4Addr(object):
                            """
                            v4 addr
                            
                            .. attribute:: ipv4_address
                            
                            	IPv4 Address
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: two_byte_index
                            
                            	2 Byte Index
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.ipv4_address = None
                                self.two_byte_index = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:v4-addr'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.ipv4_address is not None:
                                    return True

                                if self.two_byte_index is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                                return meta._meta_table['Evpn.Active.EviDetail.Elements.Element.RtAutoStitching.V4Addr']['meta_info']


                        class EsImport(object):
                            """
                            es import
                            
                            .. attribute:: high_bytes
                            
                            	Top 4 bytes of ES Import
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: low_bytes
                            
                            	Low 2 bytes of ES Import
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.high_bytes = None
                                self.low_bytes = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:es-import'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.high_bytes is not None:
                                    return True

                                if self.low_bytes is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                                return meta._meta_table['Evpn.Active.EviDetail.Elements.Element.RtAutoStitching.EsImport']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:rt-auto-stitching'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.es_import is not None and self.es_import._has_data():
                                return True

                            if self.four_byte_as is not None and self.four_byte_as._has_data():
                                return True

                            if self.rt is not None:
                                return True

                            if self.two_byte_as is not None and self.two_byte_as._has_data():
                                return True

                            if self.v4_addr is not None and self.v4_addr._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                            return meta._meta_table['Evpn.Active.EviDetail.Elements.Element.RtAutoStitching']['meta_info']

                    @property
                    def _common_path(self):
                        if self.evi is None:
                            raise YPYModelError('Key property evi is None')

                        return '/Cisco-IOS-XR-evpn-oper:evpn/Cisco-IOS-XR-evpn-oper:active/Cisco-IOS-XR-evpn-oper:evi-detail/Cisco-IOS-XR-evpn-oper:elements/Cisco-IOS-XR-evpn-oper:element[Cisco-IOS-XR-evpn-oper:evi = ' + str(self.evi) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.evi is not None:
                            return True

                        if self.advertise_mac is not None:
                            return True

                        if self.aliasing_disabled is not None:
                            return True

                        if self.bd_name is not None:
                            return True

                        if self.cw_disable is not None:
                            return True

                        if self.description is not None:
                            return True

                        if self.evi_xr is not None:
                            return True

                        if self.flow_label is not None and self.flow_label._has_data():
                            return True

                        if self.forward_class is not None:
                            return True

                        if self.multicast_label is not None:
                            return True

                        if self.rd_auto is not None and self.rd_auto._has_data():
                            return True

                        if self.rd_configured is not None and self.rd_configured._has_data():
                            return True

                        if self.reoriginate_disabled is not None:
                            return True

                        if self.rt_auto is not None and self.rt_auto._has_data():
                            return True

                        if self.rt_auto_stitching is not None and self.rt_auto_stitching._has_data():
                            return True

                        if self.rt_export_block_set is not None:
                            return True

                        if self.rt_import_block_set is not None:
                            return True

                        if self.stitching is not None:
                            return True

                        if self.table_policy_name is not None:
                            return True

                        if self.type is not None:
                            return True

                        if self.unicast_label is not None:
                            return True

                        if self.unknown_unicast_flooding_disabled is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                        return meta._meta_table['Evpn.Active.EviDetail.Elements.Element']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-evpn-oper:evpn/Cisco-IOS-XR-evpn-oper:active/Cisco-IOS-XR-evpn-oper:evi-detail/Cisco-IOS-XR-evpn-oper:elements'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.element is not None:
                        for child_ref in self.element:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                    return meta._meta_table['Evpn.Active.EviDetail.Elements']['meta_info']


            class EviChildren(object):
                """
                Container for all EVI detail info
                
                .. attribute:: ethernet_auto_discoveries
                
                	EVPN Ethernet Auto\-Discovery table
                	**type**\:   :py:class:`EthernetAutoDiscoveries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.EviChildren.EthernetAutoDiscoveries>`
                
                .. attribute:: inclusive_multicasts
                
                	L2VPN EVPN IMCAST table
                	**type**\:   :py:class:`InclusiveMulticasts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.EviChildren.InclusiveMulticasts>`
                
                .. attribute:: macs
                
                	L2VPN EVPN EVI MAC table
                	**type**\:   :py:class:`Macs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.EviChildren.Macs>`
                
                .. attribute:: neighbors
                
                	EVPN Neighbor table
                	**type**\:   :py:class:`Neighbors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.EviChildren.Neighbors>`
                
                .. attribute:: route_targets
                
                	L2VPN EVPN EVI RT Child Table
                	**type**\:   :py:class:`RouteTargets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.EviChildren.RouteTargets>`
                
                

                """

                _prefix = 'evpn-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.ethernet_auto_discoveries = Evpn.Active.EviDetail.EviChildren.EthernetAutoDiscoveries()
                    self.ethernet_auto_discoveries.parent = self
                    self.inclusive_multicasts = Evpn.Active.EviDetail.EviChildren.InclusiveMulticasts()
                    self.inclusive_multicasts.parent = self
                    self.macs = Evpn.Active.EviDetail.EviChildren.Macs()
                    self.macs.parent = self
                    self.neighbors = Evpn.Active.EviDetail.EviChildren.Neighbors()
                    self.neighbors.parent = self
                    self.route_targets = Evpn.Active.EviDetail.EviChildren.RouteTargets()
                    self.route_targets.parent = self


                class Neighbors(object):
                    """
                    EVPN Neighbor table
                    
                    .. attribute:: neighbor
                    
                    	EVPN Neighbor table
                    	**type**\: list of    :py:class:`Neighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.EviChildren.Neighbors.Neighbor>`
                    
                    

                    """

                    _prefix = 'evpn-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.neighbor = YList()
                        self.neighbor.parent = self
                        self.neighbor.name = 'neighbor'


                    class Neighbor(object):
                        """
                        EVPN Neighbor table
                        
                        .. attribute:: evi
                        
                        	EVPN id
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: evi_xr
                        
                        	E\-VPN id
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: neighbor
                        
                        	Neighbor IP
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: neighbor_ip
                        
                        	Neighbor IP
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        

                        """

                        _prefix = 'evpn-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.evi = None
                            self.evi_xr = None
                            self.neighbor = None
                            self.neighbor_ip = None

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-evpn-oper:evpn/Cisco-IOS-XR-evpn-oper:active/Cisco-IOS-XR-evpn-oper:evi-detail/Cisco-IOS-XR-evpn-oper:evi-children/Cisco-IOS-XR-evpn-oper:neighbors/Cisco-IOS-XR-evpn-oper:neighbor'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.evi is not None:
                                return True

                            if self.evi_xr is not None:
                                return True

                            if self.neighbor is not None:
                                return True

                            if self.neighbor_ip is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                            return meta._meta_table['Evpn.Active.EviDetail.EviChildren.Neighbors.Neighbor']['meta_info']

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-evpn-oper:evpn/Cisco-IOS-XR-evpn-oper:active/Cisco-IOS-XR-evpn-oper:evi-detail/Cisco-IOS-XR-evpn-oper:evi-children/Cisco-IOS-XR-evpn-oper:neighbors'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.neighbor is not None:
                            for child_ref in self.neighbor:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                        return meta._meta_table['Evpn.Active.EviDetail.EviChildren.Neighbors']['meta_info']


                class EthernetAutoDiscoveries(object):
                    """
                    EVPN Ethernet Auto\-Discovery table
                    
                    .. attribute:: ethernet_auto_discovery
                    
                    	EVPN Ethernet Auto\-Discovery Entry
                    	**type**\: list of    :py:class:`EthernetAutoDiscovery <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.EviChildren.EthernetAutoDiscoveries.EthernetAutoDiscovery>`
                    
                    

                    """

                    _prefix = 'evpn-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.ethernet_auto_discovery = YList()
                        self.ethernet_auto_discovery.parent = self
                        self.ethernet_auto_discovery.name = 'ethernet_auto_discovery'


                    class EthernetAutoDiscovery(object):
                        """
                        EVPN Ethernet Auto\-Discovery Entry
                        
                        .. attribute:: encap
                        
                        	Encap type of local or remote EAD
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: esi1
                        
                        	ES id (part 1/5)
                        	**type**\:  str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        .. attribute:: esi2
                        
                        	ES id (part 2/5)
                        	**type**\:  str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        .. attribute:: esi3
                        
                        	ES id (part 3/5)
                        	**type**\:  str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        .. attribute:: esi4
                        
                        	ES id (part 4/5)
                        	**type**\:  str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        .. attribute:: esi5
                        
                        	ES id (part 5/5)
                        	**type**\:  str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        .. attribute:: ethernet_segment_identifier
                        
                        	Ethernet Segment id
                        	**type**\:  list of int
                        
                        	**range:** 0..255
                        
                        .. attribute:: ethernet_tag
                        
                        	Ethernet Tag ID
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: ethernet_tag_xr
                        
                        	Ethernet Tag
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ethernet_vpnid
                        
                        	E\-VPN id
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: evi
                        
                        	EVPN id
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: is_local_ead
                        
                        	Indication of EthernetAutoDiscovery Route is local
                        	**type**\:  bool
                        
                        .. attribute:: local_label
                        
                        	Associated local label
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: local_next_hop
                        
                        	Local nexthop IP
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: num_paths
                        
                        	 Number of items in path list buffer
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: path_buffer
                        
                        	Path List Buffer
                        	**type**\: list of    :py:class:`PathBuffer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.EviChildren.EthernetAutoDiscoveries.EthernetAutoDiscovery.PathBuffer>`
                        
                        .. attribute:: redundancy_single_active
                        
                        	Single\-active redundancy configured at remote EAD
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'evpn-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.encap = None
                            self.esi1 = None
                            self.esi2 = None
                            self.esi3 = None
                            self.esi4 = None
                            self.esi5 = None
                            self.ethernet_segment_identifier = YLeafList()
                            self.ethernet_segment_identifier.parent = self
                            self.ethernet_segment_identifier.name = 'ethernet_segment_identifier'
                            self.ethernet_tag = None
                            self.ethernet_tag_xr = None
                            self.ethernet_vpnid = None
                            self.evi = None
                            self.is_local_ead = None
                            self.local_label = None
                            self.local_next_hop = None
                            self.num_paths = None
                            self.path_buffer = YList()
                            self.path_buffer.parent = self
                            self.path_buffer.name = 'path_buffer'
                            self.redundancy_single_active = None


                        class PathBuffer(object):
                            """
                            Path List Buffer
                            
                            .. attribute:: next_hop
                            
                            	Next\-hop IP address (v6 format)
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: output_label
                            
                            	Output Label
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.next_hop = None
                                self.output_label = None

                            @property
                            def _common_path(self):

                                return '/Cisco-IOS-XR-evpn-oper:evpn/Cisco-IOS-XR-evpn-oper:active/Cisco-IOS-XR-evpn-oper:evi-detail/Cisco-IOS-XR-evpn-oper:evi-children/Cisco-IOS-XR-evpn-oper:ethernet-auto-discoveries/Cisco-IOS-XR-evpn-oper:ethernet-auto-discovery/Cisco-IOS-XR-evpn-oper:path-buffer'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.next_hop is not None:
                                    return True

                                if self.output_label is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                                return meta._meta_table['Evpn.Active.EviDetail.EviChildren.EthernetAutoDiscoveries.EthernetAutoDiscovery.PathBuffer']['meta_info']

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-evpn-oper:evpn/Cisco-IOS-XR-evpn-oper:active/Cisco-IOS-XR-evpn-oper:evi-detail/Cisco-IOS-XR-evpn-oper:evi-children/Cisco-IOS-XR-evpn-oper:ethernet-auto-discoveries/Cisco-IOS-XR-evpn-oper:ethernet-auto-discovery'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.encap is not None:
                                return True

                            if self.esi1 is not None:
                                return True

                            if self.esi2 is not None:
                                return True

                            if self.esi3 is not None:
                                return True

                            if self.esi4 is not None:
                                return True

                            if self.esi5 is not None:
                                return True

                            if self.ethernet_segment_identifier is not None:
                                for child in self.ethernet_segment_identifier:
                                    if child is not None:
                                        return True

                            if self.ethernet_tag is not None:
                                return True

                            if self.ethernet_tag_xr is not None:
                                return True

                            if self.ethernet_vpnid is not None:
                                return True

                            if self.evi is not None:
                                return True

                            if self.is_local_ead is not None:
                                return True

                            if self.local_label is not None:
                                return True

                            if self.local_next_hop is not None:
                                return True

                            if self.num_paths is not None:
                                return True

                            if self.path_buffer is not None:
                                for child_ref in self.path_buffer:
                                    if child_ref._has_data():
                                        return True

                            if self.redundancy_single_active is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                            return meta._meta_table['Evpn.Active.EviDetail.EviChildren.EthernetAutoDiscoveries.EthernetAutoDiscovery']['meta_info']

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-evpn-oper:evpn/Cisco-IOS-XR-evpn-oper:active/Cisco-IOS-XR-evpn-oper:evi-detail/Cisco-IOS-XR-evpn-oper:evi-children/Cisco-IOS-XR-evpn-oper:ethernet-auto-discoveries'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.ethernet_auto_discovery is not None:
                            for child_ref in self.ethernet_auto_discovery:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                        return meta._meta_table['Evpn.Active.EviDetail.EviChildren.EthernetAutoDiscoveries']['meta_info']


                class InclusiveMulticasts(object):
                    """
                    L2VPN EVPN IMCAST table
                    
                    .. attribute:: inclusive_multicast
                    
                    	L2VPN EVPN IMCAST table
                    	**type**\: list of    :py:class:`InclusiveMulticast <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.EviChildren.InclusiveMulticasts.InclusiveMulticast>`
                    
                    

                    """

                    _prefix = 'evpn-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.inclusive_multicast = YList()
                        self.inclusive_multicast.parent = self
                        self.inclusive_multicast.name = 'inclusive_multicast'


                    class InclusiveMulticast(object):
                        """
                        L2VPN EVPN IMCAST table
                        
                        .. attribute:: ethernet_tag
                        
                        	Ethernet Tag
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: ethernet_tag_xr
                        
                        	Ethernet Tag
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: evi
                        
                        	EVPN id
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: evi_xr
                        
                        	E\-VPN id
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_local_entry
                        
                        	Local entry
                        	**type**\:  bool
                        
                        .. attribute:: next_hop
                        
                        	IP of nexthop
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: originating_ip
                        
                        	Originating IP
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: originating_ip_xr
                        
                        	Originating IP
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: output_label
                        
                        	Output label
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'evpn-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.ethernet_tag = None
                            self.ethernet_tag_xr = None
                            self.evi = None
                            self.evi_xr = None
                            self.is_local_entry = None
                            self.next_hop = None
                            self.originating_ip = None
                            self.originating_ip_xr = None
                            self.output_label = None

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-evpn-oper:evpn/Cisco-IOS-XR-evpn-oper:active/Cisco-IOS-XR-evpn-oper:evi-detail/Cisco-IOS-XR-evpn-oper:evi-children/Cisco-IOS-XR-evpn-oper:inclusive-multicasts/Cisco-IOS-XR-evpn-oper:inclusive-multicast'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.ethernet_tag is not None:
                                return True

                            if self.ethernet_tag_xr is not None:
                                return True

                            if self.evi is not None:
                                return True

                            if self.evi_xr is not None:
                                return True

                            if self.is_local_entry is not None:
                                return True

                            if self.next_hop is not None:
                                return True

                            if self.originating_ip is not None:
                                return True

                            if self.originating_ip_xr is not None:
                                return True

                            if self.output_label is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                            return meta._meta_table['Evpn.Active.EviDetail.EviChildren.InclusiveMulticasts.InclusiveMulticast']['meta_info']

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-evpn-oper:evpn/Cisco-IOS-XR-evpn-oper:active/Cisco-IOS-XR-evpn-oper:evi-detail/Cisco-IOS-XR-evpn-oper:evi-children/Cisco-IOS-XR-evpn-oper:inclusive-multicasts'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.inclusive_multicast is not None:
                            for child_ref in self.inclusive_multicast:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                        return meta._meta_table['Evpn.Active.EviDetail.EviChildren.InclusiveMulticasts']['meta_info']


                class RouteTargets(object):
                    """
                    L2VPN EVPN EVI RT Child Table
                    
                    .. attribute:: route_target
                    
                    	L2VPN EVPN EVI RT Table
                    	**type**\: list of    :py:class:`RouteTarget <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.EviChildren.RouteTargets.RouteTarget>`
                    
                    

                    """

                    _prefix = 'evpn-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.route_target = YList()
                        self.route_target.parent = self
                        self.route_target.name = 'route_target'


                    class RouteTarget(object):
                        """
                        L2VPN EVPN EVI RT Table
                        
                        .. attribute:: addr_index
                        
                        	RT IP Index
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: address
                        
                        	RT IPv4 Address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: as_
                        
                        	Two or Four byte AS Number
                        	**type**\:  int
                        
                        	**range:** 1..4294967295
                        
                        .. attribute:: as_index
                        
                        	RT AS Index
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bd_name
                        
                        	Bridge Domain Name
                        	**type**\:  str
                        
                        .. attribute:: evi
                        
                        	EVPN id
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: evi_xr
                        
                        	VPN ID
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: format
                        
                        	Format of the route target
                        	**type**\:   :py:class:`BgpRouteTargetFormatEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.BgpRouteTargetFormatEnum>`
                        
                        .. attribute:: role
                        
                        	Role of the route target
                        	**type**\:   :py:class:`BgpRouteTargetRoleEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.BgpRouteTargetRoleEnum>`
                        
                        .. attribute:: route_target
                        
                        	Route Target
                        	**type**\:   :py:class:`RouteTarget_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_>`
                        
                        .. attribute:: route_target_role
                        
                        	RT Role
                        	**type**\:   :py:class:`L2VpnAdRtRoleEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2VpnAdRtRoleEnum>`
                        
                        .. attribute:: route_target_stitching
                        
                        	RT Stitching
                        	**type**\:  bool
                        
                        .. attribute:: type
                        
                        	Type of the route target
                        	**type**\:   :py:class:`BgpRouteTargetEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.BgpRouteTargetEnum>`
                        
                        

                        """

                        _prefix = 'evpn-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.addr_index = None
                            self.address = None
                            self.as_ = None
                            self.as_index = None
                            self.bd_name = None
                            self.evi = None
                            self.evi_xr = None
                            self.format = None
                            self.role = None
                            self.route_target = Evpn.Active.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_()
                            self.route_target.parent = self
                            self.route_target_role = None
                            self.route_target_stitching = None
                            self.type = None


                        class RouteTarget_(object):
                            """
                            Route Target
                            
                            .. attribute:: es_import
                            
                            	es import
                            	**type**\:   :py:class:`EsImport <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.EsImport>`
                            
                            .. attribute:: four_byte_as
                            
                            	four byte as
                            	**type**\:   :py:class:`FourByteAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.FourByteAs>`
                            
                            .. attribute:: rt
                            
                            	RT
                            	**type**\:   :py:class:`L2VpnAdRtEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2VpnAdRtEnum>`
                            
                            .. attribute:: two_byte_as
                            
                            	two byte as
                            	**type**\:   :py:class:`TwoByteAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.TwoByteAs>`
                            
                            .. attribute:: v4_addr
                            
                            	v4 addr
                            	**type**\:   :py:class:`V4Addr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.V4Addr>`
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.es_import = Evpn.Active.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.EsImport()
                                self.es_import.parent = self
                                self.four_byte_as = Evpn.Active.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.FourByteAs()
                                self.four_byte_as.parent = self
                                self.rt = None
                                self.two_byte_as = Evpn.Active.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.TwoByteAs()
                                self.two_byte_as.parent = self
                                self.v4_addr = Evpn.Active.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.V4Addr()
                                self.v4_addr.parent = self


                            class TwoByteAs(object):
                                """
                                two byte as
                                
                                .. attribute:: four_byte_index
                                
                                	4 Byte Index
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: two_byte_as
                                
                                	2 Byte AS Number
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'evpn-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.four_byte_index = None
                                    self.two_byte_as = None

                                @property
                                def _common_path(self):

                                    return '/Cisco-IOS-XR-evpn-oper:evpn/Cisco-IOS-XR-evpn-oper:active/Cisco-IOS-XR-evpn-oper:evi-detail/Cisco-IOS-XR-evpn-oper:evi-children/Cisco-IOS-XR-evpn-oper:route-targets/Cisco-IOS-XR-evpn-oper:route-target/Cisco-IOS-XR-evpn-oper:route-target/Cisco-IOS-XR-evpn-oper:two-byte-as'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.four_byte_index is not None:
                                        return True

                                    if self.two_byte_as is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                                    return meta._meta_table['Evpn.Active.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.TwoByteAs']['meta_info']


                            class FourByteAs(object):
                                """
                                four byte as
                                
                                .. attribute:: four_byte_as
                                
                                	4 Byte AS Number
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: two_byte_index
                                
                                	2 Byte Index
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'evpn-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.four_byte_as = None
                                    self.two_byte_index = None

                                @property
                                def _common_path(self):

                                    return '/Cisco-IOS-XR-evpn-oper:evpn/Cisco-IOS-XR-evpn-oper:active/Cisco-IOS-XR-evpn-oper:evi-detail/Cisco-IOS-XR-evpn-oper:evi-children/Cisco-IOS-XR-evpn-oper:route-targets/Cisco-IOS-XR-evpn-oper:route-target/Cisco-IOS-XR-evpn-oper:route-target/Cisco-IOS-XR-evpn-oper:four-byte-as'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.four_byte_as is not None:
                                        return True

                                    if self.two_byte_index is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                                    return meta._meta_table['Evpn.Active.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.FourByteAs']['meta_info']


                            class V4Addr(object):
                                """
                                v4 addr
                                
                                .. attribute:: ipv4_address
                                
                                	IPv4 Address
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: two_byte_index
                                
                                	2 Byte Index
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'evpn-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.ipv4_address = None
                                    self.two_byte_index = None

                                @property
                                def _common_path(self):

                                    return '/Cisco-IOS-XR-evpn-oper:evpn/Cisco-IOS-XR-evpn-oper:active/Cisco-IOS-XR-evpn-oper:evi-detail/Cisco-IOS-XR-evpn-oper:evi-children/Cisco-IOS-XR-evpn-oper:route-targets/Cisco-IOS-XR-evpn-oper:route-target/Cisco-IOS-XR-evpn-oper:route-target/Cisco-IOS-XR-evpn-oper:v4-addr'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.ipv4_address is not None:
                                        return True

                                    if self.two_byte_index is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                                    return meta._meta_table['Evpn.Active.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.V4Addr']['meta_info']


                            class EsImport(object):
                                """
                                es import
                                
                                .. attribute:: high_bytes
                                
                                	Top 4 bytes of ES Import
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: low_bytes
                                
                                	Low 2 bytes of ES Import
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'evpn-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.high_bytes = None
                                    self.low_bytes = None

                                @property
                                def _common_path(self):

                                    return '/Cisco-IOS-XR-evpn-oper:evpn/Cisco-IOS-XR-evpn-oper:active/Cisco-IOS-XR-evpn-oper:evi-detail/Cisco-IOS-XR-evpn-oper:evi-children/Cisco-IOS-XR-evpn-oper:route-targets/Cisco-IOS-XR-evpn-oper:route-target/Cisco-IOS-XR-evpn-oper:route-target/Cisco-IOS-XR-evpn-oper:es-import'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.high_bytes is not None:
                                        return True

                                    if self.low_bytes is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                                    return meta._meta_table['Evpn.Active.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.EsImport']['meta_info']

                            @property
                            def _common_path(self):

                                return '/Cisco-IOS-XR-evpn-oper:evpn/Cisco-IOS-XR-evpn-oper:active/Cisco-IOS-XR-evpn-oper:evi-detail/Cisco-IOS-XR-evpn-oper:evi-children/Cisco-IOS-XR-evpn-oper:route-targets/Cisco-IOS-XR-evpn-oper:route-target/Cisco-IOS-XR-evpn-oper:route-target'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.es_import is not None and self.es_import._has_data():
                                    return True

                                if self.four_byte_as is not None and self.four_byte_as._has_data():
                                    return True

                                if self.rt is not None:
                                    return True

                                if self.two_byte_as is not None and self.two_byte_as._has_data():
                                    return True

                                if self.v4_addr is not None and self.v4_addr._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                                return meta._meta_table['Evpn.Active.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_']['meta_info']

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-evpn-oper:evpn/Cisco-IOS-XR-evpn-oper:active/Cisco-IOS-XR-evpn-oper:evi-detail/Cisco-IOS-XR-evpn-oper:evi-children/Cisco-IOS-XR-evpn-oper:route-targets/Cisco-IOS-XR-evpn-oper:route-target'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.addr_index is not None:
                                return True

                            if self.address is not None:
                                return True

                            if self.as_ is not None:
                                return True

                            if self.as_index is not None:
                                return True

                            if self.bd_name is not None:
                                return True

                            if self.evi is not None:
                                return True

                            if self.evi_xr is not None:
                                return True

                            if self.format is not None:
                                return True

                            if self.role is not None:
                                return True

                            if self.route_target is not None and self.route_target._has_data():
                                return True

                            if self.route_target_role is not None:
                                return True

                            if self.route_target_stitching is not None:
                                return True

                            if self.type is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                            return meta._meta_table['Evpn.Active.EviDetail.EviChildren.RouteTargets.RouteTarget']['meta_info']

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-evpn-oper:evpn/Cisco-IOS-XR-evpn-oper:active/Cisco-IOS-XR-evpn-oper:evi-detail/Cisco-IOS-XR-evpn-oper:evi-children/Cisco-IOS-XR-evpn-oper:route-targets'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.route_target is not None:
                            for child_ref in self.route_target:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                        return meta._meta_table['Evpn.Active.EviDetail.EviChildren.RouteTargets']['meta_info']


                class Macs(object):
                    """
                    L2VPN EVPN EVI MAC table
                    
                    .. attribute:: mac
                    
                    	L2VPN EVPN MAC table
                    	**type**\: list of    :py:class:`Mac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.EviChildren.Macs.Mac>`
                    
                    

                    """

                    _prefix = 'evpn-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.mac = YList()
                        self.mac.parent = self
                        self.mac.name = 'mac'


                    class Mac(object):
                        """
                        L2VPN EVPN MAC table
                        
                        .. attribute:: esi_port_key
                        
                        	ESI port key
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: ethernet_tag
                        
                        	Ethernet Tag ID
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: ethernet_tag_xr
                        
                        	Ethernet Tag
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: evi
                        
                        	EVPN id
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: internal_label
                        
                        	MPLS Internal Label
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ip_address
                        
                        	IP Address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: ip_address_xr
                        
                        	IP address (v6 format)
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: is_local_mac
                        
                        	Indication of MAC being locally generated
                        	**type**\:  bool
                        
                        .. attribute:: is_remote_mac
                        
                        	Indication of MAC being remotely generated
                        	**type**\:  bool
                        
                        .. attribute:: is_static
                        
                        	Indication if MAC is statically configured
                        	**type**\:  bool
                        
                        .. attribute:: learned_bridge_port_name
                        
                        	Port the MAC was learned on
                        	**type**\:  str
                        
                        .. attribute:: local_encap_type
                        
                        	Encap type of local MAC
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: local_ethernet_segment_identifier
                        
                        	Local Ethernet Segment id
                        	**type**\:  list of int
                        
                        	**range:** 0..255
                        
                        .. attribute:: local_label
                        
                        	Associated local label
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: local_seq_id
                        
                        	local seq id
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: mac_address
                        
                        	MAC address
                        	**type**\:  str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        .. attribute:: mac_address_xr
                        
                        	MAC address
                        	**type**\:  str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        .. attribute:: mac_flush_received
                        
                        	Number of flushes received 
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: mac_flush_requested
                        
                        	Number of flushes requested 
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: num_paths
                        
                        	 Number of items in path list buffer
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: path_buffer
                        
                        	Path List Buffer
                        	**type**\: list of    :py:class:`PathBuffer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.EviChildren.Macs.Mac.PathBuffer>`
                        
                        .. attribute:: remote_encap_type
                        
                        	Encap type of remote MAC
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: remote_ethernet_segment_identifier
                        
                        	Remote Ethernet Segment id
                        	**type**\:  list of int
                        
                        	**range:** 0..255
                        
                        .. attribute:: remote_seq_id
                        
                        	remote seq id
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: resolved
                        
                        	Internal Label has resolved per\-ES EAD and per\-EVI EAD or MAC routes
                        	**type**\:  bool
                        
                        .. attribute:: soo_nexthop
                        
                        	SOO nexthop (v6 format)
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'evpn-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.esi_port_key = None
                            self.ethernet_tag = None
                            self.ethernet_tag_xr = None
                            self.evi = None
                            self.internal_label = None
                            self.ip_address = None
                            self.ip_address_xr = None
                            self.is_local_mac = None
                            self.is_remote_mac = None
                            self.is_static = None
                            self.learned_bridge_port_name = None
                            self.local_encap_type = None
                            self.local_ethernet_segment_identifier = YLeafList()
                            self.local_ethernet_segment_identifier.parent = self
                            self.local_ethernet_segment_identifier.name = 'local_ethernet_segment_identifier'
                            self.local_label = None
                            self.local_seq_id = None
                            self.mac_address = None
                            self.mac_address_xr = None
                            self.mac_flush_received = None
                            self.mac_flush_requested = None
                            self.num_paths = None
                            self.path_buffer = YList()
                            self.path_buffer.parent = self
                            self.path_buffer.name = 'path_buffer'
                            self.remote_encap_type = None
                            self.remote_ethernet_segment_identifier = YLeafList()
                            self.remote_ethernet_segment_identifier.parent = self
                            self.remote_ethernet_segment_identifier.name = 'remote_ethernet_segment_identifier'
                            self.remote_seq_id = None
                            self.resolved = None
                            self.soo_nexthop = None


                        class PathBuffer(object):
                            """
                            Path List Buffer
                            
                            .. attribute:: next_hop
                            
                            	Next\-hop IP address (v6 format)
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: output_label
                            
                            	Output Label
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.next_hop = None
                                self.output_label = None

                            @property
                            def _common_path(self):

                                return '/Cisco-IOS-XR-evpn-oper:evpn/Cisco-IOS-XR-evpn-oper:active/Cisco-IOS-XR-evpn-oper:evi-detail/Cisco-IOS-XR-evpn-oper:evi-children/Cisco-IOS-XR-evpn-oper:macs/Cisco-IOS-XR-evpn-oper:mac/Cisco-IOS-XR-evpn-oper:path-buffer'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.next_hop is not None:
                                    return True

                                if self.output_label is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                                return meta._meta_table['Evpn.Active.EviDetail.EviChildren.Macs.Mac.PathBuffer']['meta_info']

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-evpn-oper:evpn/Cisco-IOS-XR-evpn-oper:active/Cisco-IOS-XR-evpn-oper:evi-detail/Cisco-IOS-XR-evpn-oper:evi-children/Cisco-IOS-XR-evpn-oper:macs/Cisco-IOS-XR-evpn-oper:mac'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.esi_port_key is not None:
                                return True

                            if self.ethernet_tag is not None:
                                return True

                            if self.ethernet_tag_xr is not None:
                                return True

                            if self.evi is not None:
                                return True

                            if self.internal_label is not None:
                                return True

                            if self.ip_address is not None:
                                return True

                            if self.ip_address_xr is not None:
                                return True

                            if self.is_local_mac is not None:
                                return True

                            if self.is_remote_mac is not None:
                                return True

                            if self.is_static is not None:
                                return True

                            if self.learned_bridge_port_name is not None:
                                return True

                            if self.local_encap_type is not None:
                                return True

                            if self.local_ethernet_segment_identifier is not None:
                                for child in self.local_ethernet_segment_identifier:
                                    if child is not None:
                                        return True

                            if self.local_label is not None:
                                return True

                            if self.local_seq_id is not None:
                                return True

                            if self.mac_address is not None:
                                return True

                            if self.mac_address_xr is not None:
                                return True

                            if self.mac_flush_received is not None:
                                return True

                            if self.mac_flush_requested is not None:
                                return True

                            if self.num_paths is not None:
                                return True

                            if self.path_buffer is not None:
                                for child_ref in self.path_buffer:
                                    if child_ref._has_data():
                                        return True

                            if self.remote_encap_type is not None:
                                return True

                            if self.remote_ethernet_segment_identifier is not None:
                                for child in self.remote_ethernet_segment_identifier:
                                    if child is not None:
                                        return True

                            if self.remote_seq_id is not None:
                                return True

                            if self.resolved is not None:
                                return True

                            if self.soo_nexthop is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                            return meta._meta_table['Evpn.Active.EviDetail.EviChildren.Macs.Mac']['meta_info']

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-evpn-oper:evpn/Cisco-IOS-XR-evpn-oper:active/Cisco-IOS-XR-evpn-oper:evi-detail/Cisco-IOS-XR-evpn-oper:evi-children/Cisco-IOS-XR-evpn-oper:macs'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.mac is not None:
                            for child_ref in self.mac:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                        return meta._meta_table['Evpn.Active.EviDetail.EviChildren.Macs']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-evpn-oper:evpn/Cisco-IOS-XR-evpn-oper:active/Cisco-IOS-XR-evpn-oper:evi-detail/Cisco-IOS-XR-evpn-oper:evi-children'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.ethernet_auto_discoveries is not None and self.ethernet_auto_discoveries._has_data():
                        return True

                    if self.inclusive_multicasts is not None and self.inclusive_multicasts._has_data():
                        return True

                    if self.macs is not None and self.macs._has_data():
                        return True

                    if self.neighbors is not None and self.neighbors._has_data():
                        return True

                    if self.route_targets is not None and self.route_targets._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                    return meta._meta_table['Evpn.Active.EviDetail.EviChildren']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-evpn-oper:evpn/Cisco-IOS-XR-evpn-oper:active/Cisco-IOS-XR-evpn-oper:evi-detail'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.elements is not None and self.elements._has_data():
                    return True

                if self.evi_children is not None and self.evi_children._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                return meta._meta_table['Evpn.Active.EviDetail']['meta_info']


        class EthernetSegments(object):
            """
            EVPN Ethernet\-Segment Table
            
            .. attribute:: ethernet_segment
            
            	EVPN Ethernet\-Segment Entry
            	**type**\: list of    :py:class:`EthernetSegment <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EthernetSegments.EthernetSegment>`
            
            

            """

            _prefix = 'evpn-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.ethernet_segment = YList()
                self.ethernet_segment.parent = self
                self.ethernet_segment.name = 'ethernet_segment'


            class EthernetSegment(object):
                """
                EVPN Ethernet\-Segment Entry
                
                .. attribute:: elected_d_fs
                
                	Count of service carving results \- elected
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: es_bgp_gates
                
                	ES BGP Gates
                	**type**\:  str
                
                .. attribute:: es_l2fib_gates
                
                	ES L2FIB Gates
                	**type**\:  str
                
                .. attribute:: esi1
                
                	ES id (part 1/5)
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{1,8}
                
                .. attribute:: esi2
                
                	ES id (part 2/5)
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{1,8}
                
                .. attribute:: esi3
                
                	ES id (part 3/5)
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{1,8}
                
                .. attribute:: esi4
                
                	ES id (part 4/5)
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{1,8}
                
                .. attribute:: esi5
                
                	ES id (part 5/5)
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{1,8}
                
                .. attribute:: esi_type
                
                	ESI Type
                	**type**\:   :py:class:`L2VpnEvpnEsiEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2VpnEvpnEsiEnum>`
                
                .. attribute:: ethernet_segment_identifier
                
                	Ethernet Segment id
                	**type**\:  list of int
                
                	**range:** 0..255
                
                .. attribute:: ethernet_segment_name
                
                	Ethernet Segment Name
                	**type**\:  str
                
                .. attribute:: ethernet_segment_state
                
                	State of the ethernet segment
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: force_single_home
                
                	Ethernet\-Segment forced to single home
                	**type**\:  bool
                
                .. attribute:: forwarder_ports
                
                	Count of Forwarders (AC, AC PW, VFI PW)
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: if_handle
                
                	Main port ifhandle
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: interface_name
                
                	Interface
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: load_balance_mode_config
                
                	Configured load balancing mode
                	**type**\:   :py:class:`L2VpnEvpnLbModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2VpnEvpnLbModeEnum>`
                
                .. attribute:: load_balance_mode_is_default
                
                	Load balancing mode is default
                	**type**\:  bool
                
                .. attribute:: load_balance_mode_oper
                
                	Operational load balancing mode
                	**type**\:   :py:class:`L2VpnEvpnLbModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2VpnEvpnLbModeEnum>`
                
                .. attribute:: local_split_horizon_group_label
                
                	Local split horizon group label
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: mac_flushing_mode_config
                
                	Configured MAC Flushing mode
                	**type**\:   :py:class:`L2VpnEvpnMfModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2VpnEvpnMfModeEnum>`
                
                .. attribute:: main_port_mac
                
                	Main Port MAC Address
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: main_port_role
                
                	Main port redundancy group role
                	**type**\:   :py:class:`L2VpnRgStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2VpnRgStateEnum>`
                
                .. attribute:: mp_protected
                
                	MP is protected and not under EVPN control
                	**type**\:  bool
                
                .. attribute:: next_hop
                
                	List of nexthop IPv6 addresses
                	**type**\: list of    :py:class:`NextHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EthernetSegments.EthernetSegment.NextHop>`
                
                .. attribute:: not_config_d_fs
                
                	Count of service carving results \- missing config detected
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: not_elected_d_fs
                
                	Count of service carving results \- not elected
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: num_up_p_ws
                
                	Number of PWs in Up state
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: peering_timer
                
                	Configured timer for triggering DF election (seconds)
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: peering_timer_left
                
                	Milliseconds left on DF election timer
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: millisecond
                
                .. attribute:: primary_service
                
                	List of Primary services ESI/I\-SIDs
                	**type**\:  list of int
                
                	**range:** 0..4294967295
                
                .. attribute:: primary_services_input
                
                	Input string of Primary services ESI/I\-SIDs
                	**type**\:  str
                
                .. attribute:: recovery_timer
                
                	Configured timer for (STP) recovery (seconds)
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: recovery_timer_left
                
                	Milliseconds left on (STP) recovery timer
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: millisecond
                
                .. attribute:: remote_split_horizon_group_label
                
                	Remote split horizon group labels
                	**type**\: list of    :py:class:`RemoteSplitHorizonGroupLabel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EthernetSegments.EthernetSegment.RemoteSplitHorizonGroupLabel>`
                
                .. attribute:: route_target
                
                	ES\-Import Route Target
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: rt_origin
                
                	Origin of operational ES\-Import RT
                	**type**\:   :py:class:`L2VpnEvpnRtOriginEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2VpnEvpnRtOriginEnum>`
                
                .. attribute:: secondary_service
                
                	List of Secondary services ESI/I\-SIDs
                	**type**\:  list of int
                
                	**range:** 0..4294967295
                
                .. attribute:: secondary_services_input
                
                	Input string of Secondary services ESI/I\-SIDs
                	**type**\:  str
                
                .. attribute:: service_carving_mode
                
                	Service carving mode
                	**type**\:   :py:class:`L2VpnEvpnScModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2VpnEvpnScModeEnum>`
                
                .. attribute:: service_carving_result
                
                	Service carving results
                	**type**\:  list of int
                
                	**range:** 0..4294967295
                
                .. attribute:: service_carving_type
                
                	Service Carving Type
                	**type**\:   :py:class:`L2VpnEvpnScEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2VpnEvpnScEnum>`
                
                .. attribute:: source_mac_oper
                
                	Operational Source MAC address
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: source_mac_origin
                
                	Origin of operational source MAC address
                	**type**\:   :py:class:`L2VpnEvpnSmacSrcEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2VpnEvpnSmacSrcEnum>`
                
                

                """

                _prefix = 'evpn-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.elected_d_fs = None
                    self.es_bgp_gates = None
                    self.es_l2fib_gates = None
                    self.esi1 = None
                    self.esi2 = None
                    self.esi3 = None
                    self.esi4 = None
                    self.esi5 = None
                    self.esi_type = None
                    self.ethernet_segment_identifier = YLeafList()
                    self.ethernet_segment_identifier.parent = self
                    self.ethernet_segment_identifier.name = 'ethernet_segment_identifier'
                    self.ethernet_segment_name = None
                    self.ethernet_segment_state = None
                    self.force_single_home = None
                    self.forwarder_ports = None
                    self.if_handle = None
                    self.interface_name = None
                    self.load_balance_mode_config = None
                    self.load_balance_mode_is_default = None
                    self.load_balance_mode_oper = None
                    self.local_split_horizon_group_label = None
                    self.mac_flushing_mode_config = None
                    self.main_port_mac = None
                    self.main_port_role = None
                    self.mp_protected = None
                    self.next_hop = YList()
                    self.next_hop.parent = self
                    self.next_hop.name = 'next_hop'
                    self.not_config_d_fs = None
                    self.not_elected_d_fs = None
                    self.num_up_p_ws = None
                    self.peering_timer = None
                    self.peering_timer_left = None
                    self.primary_service = YLeafList()
                    self.primary_service.parent = self
                    self.primary_service.name = 'primary_service'
                    self.primary_services_input = None
                    self.recovery_timer = None
                    self.recovery_timer_left = None
                    self.remote_split_horizon_group_label = YList()
                    self.remote_split_horizon_group_label.parent = self
                    self.remote_split_horizon_group_label.name = 'remote_split_horizon_group_label'
                    self.route_target = None
                    self.rt_origin = None
                    self.secondary_service = YLeafList()
                    self.secondary_service.parent = self
                    self.secondary_service.name = 'secondary_service'
                    self.secondary_services_input = None
                    self.service_carving_mode = None
                    self.service_carving_result = YLeafList()
                    self.service_carving_result.parent = self
                    self.service_carving_result.name = 'service_carving_result'
                    self.service_carving_type = None
                    self.source_mac_oper = None
                    self.source_mac_origin = None


                class NextHop(object):
                    """
                    List of nexthop IPv6 addresses
                    
                    .. attribute:: next_hop
                    
                    	Next\-hop IP address (v6 format)
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'evpn-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.next_hop = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-evpn-oper:evpn/Cisco-IOS-XR-evpn-oper:active/Cisco-IOS-XR-evpn-oper:ethernet-segments/Cisco-IOS-XR-evpn-oper:ethernet-segment/Cisco-IOS-XR-evpn-oper:next-hop'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.next_hop is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                        return meta._meta_table['Evpn.Active.EthernetSegments.EthernetSegment.NextHop']['meta_info']


                class RemoteSplitHorizonGroupLabel(object):
                    """
                    Remote split horizon group labels
                    
                    .. attribute:: label
                    
                    	Split horizon label associated with next\-hop address
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: next_hop
                    
                    	Next\-hop IP address (v6 format)
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'evpn-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.label = None
                        self.next_hop = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-evpn-oper:evpn/Cisco-IOS-XR-evpn-oper:active/Cisco-IOS-XR-evpn-oper:ethernet-segments/Cisco-IOS-XR-evpn-oper:ethernet-segment/Cisco-IOS-XR-evpn-oper:remote-split-horizon-group-label'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.label is not None:
                            return True

                        if self.next_hop is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                        return meta._meta_table['Evpn.Active.EthernetSegments.EthernetSegment.RemoteSplitHorizonGroupLabel']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-evpn-oper:evpn/Cisco-IOS-XR-evpn-oper:active/Cisco-IOS-XR-evpn-oper:ethernet-segments/Cisco-IOS-XR-evpn-oper:ethernet-segment'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.elected_d_fs is not None:
                        return True

                    if self.es_bgp_gates is not None:
                        return True

                    if self.es_l2fib_gates is not None:
                        return True

                    if self.esi1 is not None:
                        return True

                    if self.esi2 is not None:
                        return True

                    if self.esi3 is not None:
                        return True

                    if self.esi4 is not None:
                        return True

                    if self.esi5 is not None:
                        return True

                    if self.esi_type is not None:
                        return True

                    if self.ethernet_segment_identifier is not None:
                        for child in self.ethernet_segment_identifier:
                            if child is not None:
                                return True

                    if self.ethernet_segment_name is not None:
                        return True

                    if self.ethernet_segment_state is not None:
                        return True

                    if self.force_single_home is not None:
                        return True

                    if self.forwarder_ports is not None:
                        return True

                    if self.if_handle is not None:
                        return True

                    if self.interface_name is not None:
                        return True

                    if self.load_balance_mode_config is not None:
                        return True

                    if self.load_balance_mode_is_default is not None:
                        return True

                    if self.load_balance_mode_oper is not None:
                        return True

                    if self.local_split_horizon_group_label is not None:
                        return True

                    if self.mac_flushing_mode_config is not None:
                        return True

                    if self.main_port_mac is not None:
                        return True

                    if self.main_port_role is not None:
                        return True

                    if self.mp_protected is not None:
                        return True

                    if self.next_hop is not None:
                        for child_ref in self.next_hop:
                            if child_ref._has_data():
                                return True

                    if self.not_config_d_fs is not None:
                        return True

                    if self.not_elected_d_fs is not None:
                        return True

                    if self.num_up_p_ws is not None:
                        return True

                    if self.peering_timer is not None:
                        return True

                    if self.peering_timer_left is not None:
                        return True

                    if self.primary_service is not None:
                        for child in self.primary_service:
                            if child is not None:
                                return True

                    if self.primary_services_input is not None:
                        return True

                    if self.recovery_timer is not None:
                        return True

                    if self.recovery_timer_left is not None:
                        return True

                    if self.remote_split_horizon_group_label is not None:
                        for child_ref in self.remote_split_horizon_group_label:
                            if child_ref._has_data():
                                return True

                    if self.route_target is not None:
                        return True

                    if self.rt_origin is not None:
                        return True

                    if self.secondary_service is not None:
                        for child in self.secondary_service:
                            if child is not None:
                                return True

                    if self.secondary_services_input is not None:
                        return True

                    if self.service_carving_mode is not None:
                        return True

                    if self.service_carving_result is not None:
                        for child in self.service_carving_result:
                            if child is not None:
                                return True

                    if self.service_carving_type is not None:
                        return True

                    if self.source_mac_oper is not None:
                        return True

                    if self.source_mac_origin is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                    return meta._meta_table['Evpn.Active.EthernetSegments.EthernetSegment']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-evpn-oper:evpn/Cisco-IOS-XR-evpn-oper:active/Cisco-IOS-XR-evpn-oper:ethernet-segments'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ethernet_segment is not None:
                    for child_ref in self.ethernet_segment:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                return meta._meta_table['Evpn.Active.EthernetSegments']['meta_info']


        class AcIds(object):
            """
            EVPN AC ID table
            
            .. attribute:: ac_id
            
            	EVPN AC ID table
            	**type**\: list of    :py:class:`AcId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.AcIds.AcId>`
            
            

            """

            _prefix = 'evpn-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.ac_id = YList()
                self.ac_id.parent = self
                self.ac_id.name = 'ac_id'


            class AcId(object):
                """
                EVPN AC ID table
                
                .. attribute:: ac_id
                
                	AC ID
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: evi
                
                	EVPN id
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: evi_xr
                
                	E\-VPN id
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: neighbor
                
                	Neighbor IP
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                

                """

                _prefix = 'evpn-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.ac_id = None
                    self.evi = None
                    self.evi_xr = None
                    self.neighbor = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-evpn-oper:evpn/Cisco-IOS-XR-evpn-oper:active/Cisco-IOS-XR-evpn-oper:ac-ids/Cisco-IOS-XR-evpn-oper:ac-id'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.ac_id is not None:
                        return True

                    if self.evi is not None:
                        return True

                    if self.evi_xr is not None:
                        return True

                    if self.neighbor is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                    return meta._meta_table['Evpn.Active.AcIds.AcId']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-evpn-oper:evpn/Cisco-IOS-XR-evpn-oper:active/Cisco-IOS-XR-evpn-oper:ac-ids'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ac_id is not None:
                    for child_ref in self.ac_id:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                return meta._meta_table['Evpn.Active.AcIds']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-evpn-oper:evpn/Cisco-IOS-XR-evpn-oper:active'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ac_ids is not None and self.ac_ids._has_data():
                return True

            if self.ethernet_segments is not None and self.ethernet_segments._has_data():
                return True

            if self.evi_detail is not None and self.evi_detail._has_data():
                return True

            if self.evis is not None and self.evis._has_data():
                return True

            if self.summary is not None and self.summary._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
            return meta._meta_table['Evpn.Active']['meta_info']


    class Standby(object):
        """
        Standby EVPN operational data
        
        .. attribute:: ac_ids
        
        	EVPN AC ID table
        	**type**\:   :py:class:`AcIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.AcIds>`
        
        .. attribute:: ethernet_segments
        
        	EVPN Ethernet\-Segment Table
        	**type**\:   :py:class:`EthernetSegments <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EthernetSegments>`
        
        .. attribute:: evi_detail
        
        	L2VPN EVI Detail Table
        	**type**\:   :py:class:`EviDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail>`
        
        .. attribute:: evis
        
        	L2VPN EVPN EVI Table
        	**type**\:   :py:class:`Evis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.Evis>`
        
        .. attribute:: summary
        
        	L2VPN EVPN Summary
        	**type**\:   :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.Summary>`
        
        

        """

        _prefix = 'evpn-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.ac_ids = Evpn.Standby.AcIds()
            self.ac_ids.parent = self
            self.ethernet_segments = Evpn.Standby.EthernetSegments()
            self.ethernet_segments.parent = self
            self.evi_detail = Evpn.Standby.EviDetail()
            self.evi_detail.parent = self
            self.evis = Evpn.Standby.Evis()
            self.evis.parent = self
            self.summary = Evpn.Standby.Summary()
            self.summary.parent = self


        class Evis(object):
            """
            L2VPN EVPN EVI Table
            
            .. attribute:: evi
            
            	L2VPN EVPN EVI Entry
            	**type**\: list of    :py:class:`Evi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.Evis.Evi>`
            
            

            """

            _prefix = 'evpn-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.evi = YList()
                self.evi.parent = self
                self.evi.name = 'evi'


            class Evi(object):
                """
                L2VPN EVPN EVI Entry
                
                .. attribute:: evi  <key>
                
                	EVPN id
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: bd_name
                
                	Bridge domain name
                	**type**\:  str
                
                .. attribute:: evi_xr
                
                	E\-VPN id
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: type
                
                	Service Type
                	**type**\:   :py:class:`EvpnEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.EvpnEnum>`
                
                

                """

                _prefix = 'evpn-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.evi = None
                    self.bd_name = None
                    self.evi_xr = None
                    self.type = None

                @property
                def _common_path(self):
                    if self.evi is None:
                        raise YPYModelError('Key property evi is None')

                    return '/Cisco-IOS-XR-evpn-oper:evpn/Cisco-IOS-XR-evpn-oper:standby/Cisco-IOS-XR-evpn-oper:evis/Cisco-IOS-XR-evpn-oper:evi[Cisco-IOS-XR-evpn-oper:evi = ' + str(self.evi) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.evi is not None:
                        return True

                    if self.bd_name is not None:
                        return True

                    if self.evi_xr is not None:
                        return True

                    if self.type is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                    return meta._meta_table['Evpn.Standby.Evis.Evi']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-evpn-oper:evpn/Cisco-IOS-XR-evpn-oper:standby/Cisco-IOS-XR-evpn-oper:evis'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.evi is not None:
                    for child_ref in self.evi:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                return meta._meta_table['Evpn.Standby.Evis']['meta_info']


        class Summary(object):
            """
            L2VPN EVPN Summary
            
            .. attribute:: as_
            
            	BGP AS number
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: es_entries
            
            	Number of ES Entries in DB
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: es_global_mac_routes
            
            	Number of ES\:Global MAC Routes
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ev_is
            
            	Number of EVI DB Entries
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: global_source_mac
            
            	Global Source MAC Address
            	**type**\:  str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: l2rib_throttle
            
            	Send to L2RIB Throttled
            	**type**\:  bool
            
            .. attribute:: labels
            
            	Number of Internal Labels
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: local_ead_routes
            
            	Number of Local EAD Entries in DB
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: local_imcast_routes
            
            	Number of Local IMCAST Routes
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: local_ipv4_mac_routes
            
            	Number of Local IPv4 MAC\-IP Routes
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: local_ipv6_mac_routes
            
            	Number of Local IPv6 MAC\-IP Routes
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: local_mac_routes
            
            	Number of Local MAC Routes
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: logging_df_election_enabled
            
            	Logging EVPN Designated Forwarder changes enabled
            	**type**\:  bool
            
            .. attribute:: neighbor_entries
            
            	Number of neighbor Entries in DB
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: peering_time
            
            	EVPN ES Peering Time (seconds)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: second
            
            .. attribute:: recovery_time
            
            	EVPN ES Recovery Time (seconds)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: second
            
            .. attribute:: remote_ead_routes
            
            	Number of Remote EAD Entries in DB
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: remote_imcast_routes
            
            	Number of Remote IMCAST Routes
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: remote_ipv4_mac_routes
            
            	Number of Remote IPv4 MAC\-IP Routes
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: remote_ipv6_mac_routes
            
            	Number of Remote IPv6 MAC\-IP Routes
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: remote_mac_routes
            
            	Number of Remote MAC Routes
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: remote_soo_mac_routes
            
            	Number of Remote Soo MAC Routes
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: router_id
            
            	EVPN Router ID
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            

            """

            _prefix = 'evpn-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.as_ = None
                self.es_entries = None
                self.es_global_mac_routes = None
                self.ev_is = None
                self.global_source_mac = None
                self.l2rib_throttle = None
                self.labels = None
                self.local_ead_routes = None
                self.local_imcast_routes = None
                self.local_ipv4_mac_routes = None
                self.local_ipv6_mac_routes = None
                self.local_mac_routes = None
                self.logging_df_election_enabled = None
                self.neighbor_entries = None
                self.peering_time = None
                self.recovery_time = None
                self.remote_ead_routes = None
                self.remote_imcast_routes = None
                self.remote_ipv4_mac_routes = None
                self.remote_ipv6_mac_routes = None
                self.remote_mac_routes = None
                self.remote_soo_mac_routes = None
                self.router_id = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-evpn-oper:evpn/Cisco-IOS-XR-evpn-oper:standby/Cisco-IOS-XR-evpn-oper:summary'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.as_ is not None:
                    return True

                if self.es_entries is not None:
                    return True

                if self.es_global_mac_routes is not None:
                    return True

                if self.ev_is is not None:
                    return True

                if self.global_source_mac is not None:
                    return True

                if self.l2rib_throttle is not None:
                    return True

                if self.labels is not None:
                    return True

                if self.local_ead_routes is not None:
                    return True

                if self.local_imcast_routes is not None:
                    return True

                if self.local_ipv4_mac_routes is not None:
                    return True

                if self.local_ipv6_mac_routes is not None:
                    return True

                if self.local_mac_routes is not None:
                    return True

                if self.logging_df_election_enabled is not None:
                    return True

                if self.neighbor_entries is not None:
                    return True

                if self.peering_time is not None:
                    return True

                if self.recovery_time is not None:
                    return True

                if self.remote_ead_routes is not None:
                    return True

                if self.remote_imcast_routes is not None:
                    return True

                if self.remote_ipv4_mac_routes is not None:
                    return True

                if self.remote_ipv6_mac_routes is not None:
                    return True

                if self.remote_mac_routes is not None:
                    return True

                if self.remote_soo_mac_routes is not None:
                    return True

                if self.router_id is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                return meta._meta_table['Evpn.Standby.Summary']['meta_info']


        class EviDetail(object):
            """
            L2VPN EVI Detail Table
            
            .. attribute:: elements
            
            	EVI BGP RT Detail Info Elements
            	**type**\:   :py:class:`Elements <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.Elements>`
            
            .. attribute:: evi_children
            
            	Container for all EVI detail info
            	**type**\:   :py:class:`EviChildren <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.EviChildren>`
            
            

            """

            _prefix = 'evpn-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.elements = Evpn.Standby.EviDetail.Elements()
                self.elements.parent = self
                self.evi_children = Evpn.Standby.EviDetail.EviChildren()
                self.evi_children.parent = self


            class Elements(object):
                """
                EVI BGP RT Detail Info Elements
                
                .. attribute:: element
                
                	EVI BGP RT Detail Info
                	**type**\: list of    :py:class:`Element <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.Elements.Element>`
                
                

                """

                _prefix = 'evpn-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.element = YList()
                    self.element.parent = self
                    self.element.name = 'element'


                class Element(object):
                    """
                    EVI BGP RT Detail Info
                    
                    .. attribute:: evi  <key>
                    
                    	EVPN id
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: advertise_mac
                    
                    	Advertise MAC\-only routes on this EVI
                    	**type**\:  bool
                    
                    .. attribute:: aliasing_disabled
                    
                    	Route Aliasing is disabled
                    	**type**\:  bool
                    
                    .. attribute:: bd_name
                    
                    	Bridge domain name
                    	**type**\:  str
                    
                    .. attribute:: cw_disable
                    
                    	Control\-Word Disable
                    	**type**\:  bool
                    
                    .. attribute:: description
                    
                    	EVI description
                    	**type**\:  str
                    
                    .. attribute:: evi_xr
                    
                    	E\-VPN id
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: flow_label
                    
                    	Flow Label Information
                    	**type**\:   :py:class:`FlowLabel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.Elements.Element.FlowLabel>`
                    
                    .. attribute:: forward_class
                    
                    	Forward Class attribute
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: multicast_label
                    
                    	Multicast Label
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rd_auto
                    
                    	Automatic Route Distingtuisher
                    	**type**\:   :py:class:`RdAuto <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.Elements.Element.RdAuto>`
                    
                    .. attribute:: rd_configured
                    
                    	Configured Route Distinguisher
                    	**type**\:   :py:class:`RdConfigured <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.Elements.Element.RdConfigured>`
                    
                    .. attribute:: reoriginate_disabled
                    
                    	Route Re\-origination is disabled
                    	**type**\:  bool
                    
                    .. attribute:: rt_auto
                    
                    	Automatic Route Target
                    	**type**\:   :py:class:`RtAuto <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.Elements.Element.RtAuto>`
                    
                    .. attribute:: rt_auto_stitching
                    
                    	Automatic Route Target Stitching
                    	**type**\:   :py:class:`RtAutoStitching <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.Elements.Element.RtAutoStitching>`
                    
                    .. attribute:: rt_export_block_set
                    
                    	Is Export RT None set
                    	**type**\:  bool
                    
                    .. attribute:: rt_import_block_set
                    
                    	Is Import RT None set
                    	**type**\:  bool
                    
                    .. attribute:: stitching
                    
                    	RT Stitching for MPLS Fabric is enabled
                    	**type**\:  bool
                    
                    .. attribute:: table_policy_name
                    
                    	Table\-policy Name
                    	**type**\:  str
                    
                    .. attribute:: type
                    
                    	Service Type
                    	**type**\:   :py:class:`EvpnEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.EvpnEnum>`
                    
                    .. attribute:: unicast_label
                    
                    	Unicast Label
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: unknown_unicast_flooding_disabled
                    
                    	Unknown\-unicast flooding is disabled
                    	**type**\:  bool
                    
                    

                    """

                    _prefix = 'evpn-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.evi = None
                        self.advertise_mac = None
                        self.aliasing_disabled = None
                        self.bd_name = None
                        self.cw_disable = None
                        self.description = None
                        self.evi_xr = None
                        self.flow_label = Evpn.Standby.EviDetail.Elements.Element.FlowLabel()
                        self.flow_label.parent = self
                        self.forward_class = None
                        self.multicast_label = None
                        self.rd_auto = Evpn.Standby.EviDetail.Elements.Element.RdAuto()
                        self.rd_auto.parent = self
                        self.rd_configured = Evpn.Standby.EviDetail.Elements.Element.RdConfigured()
                        self.rd_configured.parent = self
                        self.reoriginate_disabled = None
                        self.rt_auto = Evpn.Standby.EviDetail.Elements.Element.RtAuto()
                        self.rt_auto.parent = self
                        self.rt_auto_stitching = Evpn.Standby.EviDetail.Elements.Element.RtAutoStitching()
                        self.rt_auto_stitching.parent = self
                        self.rt_export_block_set = None
                        self.rt_import_block_set = None
                        self.stitching = None
                        self.table_policy_name = None
                        self.type = None
                        self.unicast_label = None
                        self.unknown_unicast_flooding_disabled = None


                    class FlowLabel(object):
                        """
                        Flow Label Information
                        
                        .. attribute:: global_flow_label
                        
                        	Globally configured flow label
                        	**type**\:  bool
                        
                        .. attribute:: static_flow_label
                        
                        	Static flow label
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'evpn-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.global_flow_label = None
                            self.static_flow_label = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:flow-label'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.global_flow_label is not None:
                                return True

                            if self.static_flow_label is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                            return meta._meta_table['Evpn.Standby.EviDetail.Elements.Element.FlowLabel']['meta_info']


                    class RdAuto(object):
                        """
                        Automatic Route Distingtuisher
                        
                        .. attribute:: auto
                        
                        	auto
                        	**type**\:   :py:class:`Auto <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.Elements.Element.RdAuto.Auto>`
                        
                        .. attribute:: four_byte_as
                        
                        	four byte as
                        	**type**\:   :py:class:`FourByteAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.Elements.Element.RdAuto.FourByteAs>`
                        
                        .. attribute:: rd
                        
                        	RD
                        	**type**\:   :py:class:`L2VpnAdRdEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2VpnAdRdEnum>`
                        
                        .. attribute:: two_byte_as
                        
                        	two byte as
                        	**type**\:   :py:class:`TwoByteAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.Elements.Element.RdAuto.TwoByteAs>`
                        
                        .. attribute:: v4_addr
                        
                        	v4 addr
                        	**type**\:   :py:class:`V4Addr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.Elements.Element.RdAuto.V4Addr>`
                        
                        

                        """

                        _prefix = 'evpn-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.auto = Evpn.Standby.EviDetail.Elements.Element.RdAuto.Auto()
                            self.auto.parent = self
                            self.four_byte_as = Evpn.Standby.EviDetail.Elements.Element.RdAuto.FourByteAs()
                            self.four_byte_as.parent = self
                            self.rd = None
                            self.two_byte_as = Evpn.Standby.EviDetail.Elements.Element.RdAuto.TwoByteAs()
                            self.two_byte_as.parent = self
                            self.v4_addr = Evpn.Standby.EviDetail.Elements.Element.RdAuto.V4Addr()
                            self.v4_addr.parent = self


                        class Auto(object):
                            """
                            auto
                            
                            .. attribute:: auto_index
                            
                            	Auto\-generated Index
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: router_id
                            
                            	BGP Router ID
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.auto_index = None
                                self.router_id = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:auto'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.auto_index is not None:
                                    return True

                                if self.router_id is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                                return meta._meta_table['Evpn.Standby.EviDetail.Elements.Element.RdAuto.Auto']['meta_info']


                        class TwoByteAs(object):
                            """
                            two byte as
                            
                            .. attribute:: four_byte_index
                            
                            	4 Byte Index
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: two_byte_as
                            
                            	2 Byte AS Number
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.four_byte_index = None
                                self.two_byte_as = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:two-byte-as'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.four_byte_index is not None:
                                    return True

                                if self.two_byte_as is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                                return meta._meta_table['Evpn.Standby.EviDetail.Elements.Element.RdAuto.TwoByteAs']['meta_info']


                        class FourByteAs(object):
                            """
                            four byte as
                            
                            .. attribute:: four_byte_as
                            
                            	4 Byte AS Number
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: two_byte_index
                            
                            	2 Byte Index
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.four_byte_as = None
                                self.two_byte_index = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:four-byte-as'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.four_byte_as is not None:
                                    return True

                                if self.two_byte_index is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                                return meta._meta_table['Evpn.Standby.EviDetail.Elements.Element.RdAuto.FourByteAs']['meta_info']


                        class V4Addr(object):
                            """
                            v4 addr
                            
                            .. attribute:: ipv4_address
                            
                            	IPv4 Address
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: two_byte_index
                            
                            	2 Byte Index
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.ipv4_address = None
                                self.two_byte_index = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:v4-addr'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.ipv4_address is not None:
                                    return True

                                if self.two_byte_index is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                                return meta._meta_table['Evpn.Standby.EviDetail.Elements.Element.RdAuto.V4Addr']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:rd-auto'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.auto is not None and self.auto._has_data():
                                return True

                            if self.four_byte_as is not None and self.four_byte_as._has_data():
                                return True

                            if self.rd is not None:
                                return True

                            if self.two_byte_as is not None and self.two_byte_as._has_data():
                                return True

                            if self.v4_addr is not None and self.v4_addr._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                            return meta._meta_table['Evpn.Standby.EviDetail.Elements.Element.RdAuto']['meta_info']


                    class RdConfigured(object):
                        """
                        Configured Route Distinguisher
                        
                        .. attribute:: auto
                        
                        	auto
                        	**type**\:   :py:class:`Auto <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.Elements.Element.RdConfigured.Auto>`
                        
                        .. attribute:: four_byte_as
                        
                        	four byte as
                        	**type**\:   :py:class:`FourByteAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.Elements.Element.RdConfigured.FourByteAs>`
                        
                        .. attribute:: rd
                        
                        	RD
                        	**type**\:   :py:class:`L2VpnAdRdEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2VpnAdRdEnum>`
                        
                        .. attribute:: two_byte_as
                        
                        	two byte as
                        	**type**\:   :py:class:`TwoByteAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.Elements.Element.RdConfigured.TwoByteAs>`
                        
                        .. attribute:: v4_addr
                        
                        	v4 addr
                        	**type**\:   :py:class:`V4Addr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.Elements.Element.RdConfigured.V4Addr>`
                        
                        

                        """

                        _prefix = 'evpn-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.auto = Evpn.Standby.EviDetail.Elements.Element.RdConfigured.Auto()
                            self.auto.parent = self
                            self.four_byte_as = Evpn.Standby.EviDetail.Elements.Element.RdConfigured.FourByteAs()
                            self.four_byte_as.parent = self
                            self.rd = None
                            self.two_byte_as = Evpn.Standby.EviDetail.Elements.Element.RdConfigured.TwoByteAs()
                            self.two_byte_as.parent = self
                            self.v4_addr = Evpn.Standby.EviDetail.Elements.Element.RdConfigured.V4Addr()
                            self.v4_addr.parent = self


                        class Auto(object):
                            """
                            auto
                            
                            .. attribute:: auto_index
                            
                            	Auto\-generated Index
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: router_id
                            
                            	BGP Router ID
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.auto_index = None
                                self.router_id = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:auto'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.auto_index is not None:
                                    return True

                                if self.router_id is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                                return meta._meta_table['Evpn.Standby.EviDetail.Elements.Element.RdConfigured.Auto']['meta_info']


                        class TwoByteAs(object):
                            """
                            two byte as
                            
                            .. attribute:: four_byte_index
                            
                            	4 Byte Index
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: two_byte_as
                            
                            	2 Byte AS Number
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.four_byte_index = None
                                self.two_byte_as = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:two-byte-as'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.four_byte_index is not None:
                                    return True

                                if self.two_byte_as is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                                return meta._meta_table['Evpn.Standby.EviDetail.Elements.Element.RdConfigured.TwoByteAs']['meta_info']


                        class FourByteAs(object):
                            """
                            four byte as
                            
                            .. attribute:: four_byte_as
                            
                            	4 Byte AS Number
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: two_byte_index
                            
                            	2 Byte Index
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.four_byte_as = None
                                self.two_byte_index = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:four-byte-as'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.four_byte_as is not None:
                                    return True

                                if self.two_byte_index is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                                return meta._meta_table['Evpn.Standby.EviDetail.Elements.Element.RdConfigured.FourByteAs']['meta_info']


                        class V4Addr(object):
                            """
                            v4 addr
                            
                            .. attribute:: ipv4_address
                            
                            	IPv4 Address
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: two_byte_index
                            
                            	2 Byte Index
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.ipv4_address = None
                                self.two_byte_index = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:v4-addr'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.ipv4_address is not None:
                                    return True

                                if self.two_byte_index is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                                return meta._meta_table['Evpn.Standby.EviDetail.Elements.Element.RdConfigured.V4Addr']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:rd-configured'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.auto is not None and self.auto._has_data():
                                return True

                            if self.four_byte_as is not None and self.four_byte_as._has_data():
                                return True

                            if self.rd is not None:
                                return True

                            if self.two_byte_as is not None and self.two_byte_as._has_data():
                                return True

                            if self.v4_addr is not None and self.v4_addr._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                            return meta._meta_table['Evpn.Standby.EviDetail.Elements.Element.RdConfigured']['meta_info']


                    class RtAuto(object):
                        """
                        Automatic Route Target
                        
                        .. attribute:: es_import
                        
                        	es import
                        	**type**\:   :py:class:`EsImport <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.Elements.Element.RtAuto.EsImport>`
                        
                        .. attribute:: four_byte_as
                        
                        	four byte as
                        	**type**\:   :py:class:`FourByteAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.Elements.Element.RtAuto.FourByteAs>`
                        
                        .. attribute:: rt
                        
                        	RT
                        	**type**\:   :py:class:`L2VpnAdRtEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2VpnAdRtEnum>`
                        
                        .. attribute:: two_byte_as
                        
                        	two byte as
                        	**type**\:   :py:class:`TwoByteAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.Elements.Element.RtAuto.TwoByteAs>`
                        
                        .. attribute:: v4_addr
                        
                        	v4 addr
                        	**type**\:   :py:class:`V4Addr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.Elements.Element.RtAuto.V4Addr>`
                        
                        

                        """

                        _prefix = 'evpn-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.es_import = Evpn.Standby.EviDetail.Elements.Element.RtAuto.EsImport()
                            self.es_import.parent = self
                            self.four_byte_as = Evpn.Standby.EviDetail.Elements.Element.RtAuto.FourByteAs()
                            self.four_byte_as.parent = self
                            self.rt = None
                            self.two_byte_as = Evpn.Standby.EviDetail.Elements.Element.RtAuto.TwoByteAs()
                            self.two_byte_as.parent = self
                            self.v4_addr = Evpn.Standby.EviDetail.Elements.Element.RtAuto.V4Addr()
                            self.v4_addr.parent = self


                        class TwoByteAs(object):
                            """
                            two byte as
                            
                            .. attribute:: four_byte_index
                            
                            	4 Byte Index
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: two_byte_as
                            
                            	2 Byte AS Number
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.four_byte_index = None
                                self.two_byte_as = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:two-byte-as'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.four_byte_index is not None:
                                    return True

                                if self.two_byte_as is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                                return meta._meta_table['Evpn.Standby.EviDetail.Elements.Element.RtAuto.TwoByteAs']['meta_info']


                        class FourByteAs(object):
                            """
                            four byte as
                            
                            .. attribute:: four_byte_as
                            
                            	4 Byte AS Number
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: two_byte_index
                            
                            	2 Byte Index
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.four_byte_as = None
                                self.two_byte_index = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:four-byte-as'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.four_byte_as is not None:
                                    return True

                                if self.two_byte_index is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                                return meta._meta_table['Evpn.Standby.EviDetail.Elements.Element.RtAuto.FourByteAs']['meta_info']


                        class V4Addr(object):
                            """
                            v4 addr
                            
                            .. attribute:: ipv4_address
                            
                            	IPv4 Address
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: two_byte_index
                            
                            	2 Byte Index
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.ipv4_address = None
                                self.two_byte_index = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:v4-addr'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.ipv4_address is not None:
                                    return True

                                if self.two_byte_index is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                                return meta._meta_table['Evpn.Standby.EviDetail.Elements.Element.RtAuto.V4Addr']['meta_info']


                        class EsImport(object):
                            """
                            es import
                            
                            .. attribute:: high_bytes
                            
                            	Top 4 bytes of ES Import
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: low_bytes
                            
                            	Low 2 bytes of ES Import
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.high_bytes = None
                                self.low_bytes = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:es-import'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.high_bytes is not None:
                                    return True

                                if self.low_bytes is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                                return meta._meta_table['Evpn.Standby.EviDetail.Elements.Element.RtAuto.EsImport']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:rt-auto'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.es_import is not None and self.es_import._has_data():
                                return True

                            if self.four_byte_as is not None and self.four_byte_as._has_data():
                                return True

                            if self.rt is not None:
                                return True

                            if self.two_byte_as is not None and self.two_byte_as._has_data():
                                return True

                            if self.v4_addr is not None and self.v4_addr._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                            return meta._meta_table['Evpn.Standby.EviDetail.Elements.Element.RtAuto']['meta_info']


                    class RtAutoStitching(object):
                        """
                        Automatic Route Target Stitching
                        
                        .. attribute:: es_import
                        
                        	es import
                        	**type**\:   :py:class:`EsImport <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.Elements.Element.RtAutoStitching.EsImport>`
                        
                        .. attribute:: four_byte_as
                        
                        	four byte as
                        	**type**\:   :py:class:`FourByteAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.Elements.Element.RtAutoStitching.FourByteAs>`
                        
                        .. attribute:: rt
                        
                        	RT
                        	**type**\:   :py:class:`L2VpnAdRtEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2VpnAdRtEnum>`
                        
                        .. attribute:: two_byte_as
                        
                        	two byte as
                        	**type**\:   :py:class:`TwoByteAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.Elements.Element.RtAutoStitching.TwoByteAs>`
                        
                        .. attribute:: v4_addr
                        
                        	v4 addr
                        	**type**\:   :py:class:`V4Addr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.Elements.Element.RtAutoStitching.V4Addr>`
                        
                        

                        """

                        _prefix = 'evpn-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.es_import = Evpn.Standby.EviDetail.Elements.Element.RtAutoStitching.EsImport()
                            self.es_import.parent = self
                            self.four_byte_as = Evpn.Standby.EviDetail.Elements.Element.RtAutoStitching.FourByteAs()
                            self.four_byte_as.parent = self
                            self.rt = None
                            self.two_byte_as = Evpn.Standby.EviDetail.Elements.Element.RtAutoStitching.TwoByteAs()
                            self.two_byte_as.parent = self
                            self.v4_addr = Evpn.Standby.EviDetail.Elements.Element.RtAutoStitching.V4Addr()
                            self.v4_addr.parent = self


                        class TwoByteAs(object):
                            """
                            two byte as
                            
                            .. attribute:: four_byte_index
                            
                            	4 Byte Index
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: two_byte_as
                            
                            	2 Byte AS Number
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.four_byte_index = None
                                self.two_byte_as = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:two-byte-as'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.four_byte_index is not None:
                                    return True

                                if self.two_byte_as is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                                return meta._meta_table['Evpn.Standby.EviDetail.Elements.Element.RtAutoStitching.TwoByteAs']['meta_info']


                        class FourByteAs(object):
                            """
                            four byte as
                            
                            .. attribute:: four_byte_as
                            
                            	4 Byte AS Number
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: two_byte_index
                            
                            	2 Byte Index
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.four_byte_as = None
                                self.two_byte_index = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:four-byte-as'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.four_byte_as is not None:
                                    return True

                                if self.two_byte_index is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                                return meta._meta_table['Evpn.Standby.EviDetail.Elements.Element.RtAutoStitching.FourByteAs']['meta_info']


                        class V4Addr(object):
                            """
                            v4 addr
                            
                            .. attribute:: ipv4_address
                            
                            	IPv4 Address
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: two_byte_index
                            
                            	2 Byte Index
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.ipv4_address = None
                                self.two_byte_index = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:v4-addr'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.ipv4_address is not None:
                                    return True

                                if self.two_byte_index is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                                return meta._meta_table['Evpn.Standby.EviDetail.Elements.Element.RtAutoStitching.V4Addr']['meta_info']


                        class EsImport(object):
                            """
                            es import
                            
                            .. attribute:: high_bytes
                            
                            	Top 4 bytes of ES Import
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: low_bytes
                            
                            	Low 2 bytes of ES Import
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.high_bytes = None
                                self.low_bytes = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:es-import'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.high_bytes is not None:
                                    return True

                                if self.low_bytes is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                                return meta._meta_table['Evpn.Standby.EviDetail.Elements.Element.RtAutoStitching.EsImport']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-evpn-oper:rt-auto-stitching'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.es_import is not None and self.es_import._has_data():
                                return True

                            if self.four_byte_as is not None and self.four_byte_as._has_data():
                                return True

                            if self.rt is not None:
                                return True

                            if self.two_byte_as is not None and self.two_byte_as._has_data():
                                return True

                            if self.v4_addr is not None and self.v4_addr._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                            return meta._meta_table['Evpn.Standby.EviDetail.Elements.Element.RtAutoStitching']['meta_info']

                    @property
                    def _common_path(self):
                        if self.evi is None:
                            raise YPYModelError('Key property evi is None')

                        return '/Cisco-IOS-XR-evpn-oper:evpn/Cisco-IOS-XR-evpn-oper:standby/Cisco-IOS-XR-evpn-oper:evi-detail/Cisco-IOS-XR-evpn-oper:elements/Cisco-IOS-XR-evpn-oper:element[Cisco-IOS-XR-evpn-oper:evi = ' + str(self.evi) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.evi is not None:
                            return True

                        if self.advertise_mac is not None:
                            return True

                        if self.aliasing_disabled is not None:
                            return True

                        if self.bd_name is not None:
                            return True

                        if self.cw_disable is not None:
                            return True

                        if self.description is not None:
                            return True

                        if self.evi_xr is not None:
                            return True

                        if self.flow_label is not None and self.flow_label._has_data():
                            return True

                        if self.forward_class is not None:
                            return True

                        if self.multicast_label is not None:
                            return True

                        if self.rd_auto is not None and self.rd_auto._has_data():
                            return True

                        if self.rd_configured is not None and self.rd_configured._has_data():
                            return True

                        if self.reoriginate_disabled is not None:
                            return True

                        if self.rt_auto is not None and self.rt_auto._has_data():
                            return True

                        if self.rt_auto_stitching is not None and self.rt_auto_stitching._has_data():
                            return True

                        if self.rt_export_block_set is not None:
                            return True

                        if self.rt_import_block_set is not None:
                            return True

                        if self.stitching is not None:
                            return True

                        if self.table_policy_name is not None:
                            return True

                        if self.type is not None:
                            return True

                        if self.unicast_label is not None:
                            return True

                        if self.unknown_unicast_flooding_disabled is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                        return meta._meta_table['Evpn.Standby.EviDetail.Elements.Element']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-evpn-oper:evpn/Cisco-IOS-XR-evpn-oper:standby/Cisco-IOS-XR-evpn-oper:evi-detail/Cisco-IOS-XR-evpn-oper:elements'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.element is not None:
                        for child_ref in self.element:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                    return meta._meta_table['Evpn.Standby.EviDetail.Elements']['meta_info']


            class EviChildren(object):
                """
                Container for all EVI detail info
                
                .. attribute:: ethernet_auto_discoveries
                
                	EVPN Ethernet Auto\-Discovery table
                	**type**\:   :py:class:`EthernetAutoDiscoveries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.EviChildren.EthernetAutoDiscoveries>`
                
                .. attribute:: inclusive_multicasts
                
                	L2VPN EVPN IMCAST table
                	**type**\:   :py:class:`InclusiveMulticasts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.EviChildren.InclusiveMulticasts>`
                
                .. attribute:: macs
                
                	L2VPN EVPN EVI MAC table
                	**type**\:   :py:class:`Macs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.EviChildren.Macs>`
                
                .. attribute:: neighbors
                
                	EVPN Neighbor table
                	**type**\:   :py:class:`Neighbors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.EviChildren.Neighbors>`
                
                .. attribute:: route_targets
                
                	L2VPN EVPN EVI RT Child Table
                	**type**\:   :py:class:`RouteTargets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.EviChildren.RouteTargets>`
                
                

                """

                _prefix = 'evpn-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.ethernet_auto_discoveries = Evpn.Standby.EviDetail.EviChildren.EthernetAutoDiscoveries()
                    self.ethernet_auto_discoveries.parent = self
                    self.inclusive_multicasts = Evpn.Standby.EviDetail.EviChildren.InclusiveMulticasts()
                    self.inclusive_multicasts.parent = self
                    self.macs = Evpn.Standby.EviDetail.EviChildren.Macs()
                    self.macs.parent = self
                    self.neighbors = Evpn.Standby.EviDetail.EviChildren.Neighbors()
                    self.neighbors.parent = self
                    self.route_targets = Evpn.Standby.EviDetail.EviChildren.RouteTargets()
                    self.route_targets.parent = self


                class Neighbors(object):
                    """
                    EVPN Neighbor table
                    
                    .. attribute:: neighbor
                    
                    	EVPN Neighbor table
                    	**type**\: list of    :py:class:`Neighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.EviChildren.Neighbors.Neighbor>`
                    
                    

                    """

                    _prefix = 'evpn-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.neighbor = YList()
                        self.neighbor.parent = self
                        self.neighbor.name = 'neighbor'


                    class Neighbor(object):
                        """
                        EVPN Neighbor table
                        
                        .. attribute:: evi
                        
                        	EVPN id
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: evi_xr
                        
                        	E\-VPN id
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: neighbor
                        
                        	Neighbor IP
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: neighbor_ip
                        
                        	Neighbor IP
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        

                        """

                        _prefix = 'evpn-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.evi = None
                            self.evi_xr = None
                            self.neighbor = None
                            self.neighbor_ip = None

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-evpn-oper:evpn/Cisco-IOS-XR-evpn-oper:standby/Cisco-IOS-XR-evpn-oper:evi-detail/Cisco-IOS-XR-evpn-oper:evi-children/Cisco-IOS-XR-evpn-oper:neighbors/Cisco-IOS-XR-evpn-oper:neighbor'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.evi is not None:
                                return True

                            if self.evi_xr is not None:
                                return True

                            if self.neighbor is not None:
                                return True

                            if self.neighbor_ip is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                            return meta._meta_table['Evpn.Standby.EviDetail.EviChildren.Neighbors.Neighbor']['meta_info']

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-evpn-oper:evpn/Cisco-IOS-XR-evpn-oper:standby/Cisco-IOS-XR-evpn-oper:evi-detail/Cisco-IOS-XR-evpn-oper:evi-children/Cisco-IOS-XR-evpn-oper:neighbors'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.neighbor is not None:
                            for child_ref in self.neighbor:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                        return meta._meta_table['Evpn.Standby.EviDetail.EviChildren.Neighbors']['meta_info']


                class EthernetAutoDiscoveries(object):
                    """
                    EVPN Ethernet Auto\-Discovery table
                    
                    .. attribute:: ethernet_auto_discovery
                    
                    	EVPN Ethernet Auto\-Discovery Entry
                    	**type**\: list of    :py:class:`EthernetAutoDiscovery <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.EviChildren.EthernetAutoDiscoveries.EthernetAutoDiscovery>`
                    
                    

                    """

                    _prefix = 'evpn-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.ethernet_auto_discovery = YList()
                        self.ethernet_auto_discovery.parent = self
                        self.ethernet_auto_discovery.name = 'ethernet_auto_discovery'


                    class EthernetAutoDiscovery(object):
                        """
                        EVPN Ethernet Auto\-Discovery Entry
                        
                        .. attribute:: encap
                        
                        	Encap type of local or remote EAD
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: esi1
                        
                        	ES id (part 1/5)
                        	**type**\:  str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        .. attribute:: esi2
                        
                        	ES id (part 2/5)
                        	**type**\:  str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        .. attribute:: esi3
                        
                        	ES id (part 3/5)
                        	**type**\:  str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        .. attribute:: esi4
                        
                        	ES id (part 4/5)
                        	**type**\:  str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        .. attribute:: esi5
                        
                        	ES id (part 5/5)
                        	**type**\:  str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        .. attribute:: ethernet_segment_identifier
                        
                        	Ethernet Segment id
                        	**type**\:  list of int
                        
                        	**range:** 0..255
                        
                        .. attribute:: ethernet_tag
                        
                        	Ethernet Tag ID
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: ethernet_tag_xr
                        
                        	Ethernet Tag
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ethernet_vpnid
                        
                        	E\-VPN id
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: evi
                        
                        	EVPN id
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: is_local_ead
                        
                        	Indication of EthernetAutoDiscovery Route is local
                        	**type**\:  bool
                        
                        .. attribute:: local_label
                        
                        	Associated local label
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: local_next_hop
                        
                        	Local nexthop IP
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: num_paths
                        
                        	 Number of items in path list buffer
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: path_buffer
                        
                        	Path List Buffer
                        	**type**\: list of    :py:class:`PathBuffer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.EviChildren.EthernetAutoDiscoveries.EthernetAutoDiscovery.PathBuffer>`
                        
                        .. attribute:: redundancy_single_active
                        
                        	Single\-active redundancy configured at remote EAD
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'evpn-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.encap = None
                            self.esi1 = None
                            self.esi2 = None
                            self.esi3 = None
                            self.esi4 = None
                            self.esi5 = None
                            self.ethernet_segment_identifier = YLeafList()
                            self.ethernet_segment_identifier.parent = self
                            self.ethernet_segment_identifier.name = 'ethernet_segment_identifier'
                            self.ethernet_tag = None
                            self.ethernet_tag_xr = None
                            self.ethernet_vpnid = None
                            self.evi = None
                            self.is_local_ead = None
                            self.local_label = None
                            self.local_next_hop = None
                            self.num_paths = None
                            self.path_buffer = YList()
                            self.path_buffer.parent = self
                            self.path_buffer.name = 'path_buffer'
                            self.redundancy_single_active = None


                        class PathBuffer(object):
                            """
                            Path List Buffer
                            
                            .. attribute:: next_hop
                            
                            	Next\-hop IP address (v6 format)
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: output_label
                            
                            	Output Label
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.next_hop = None
                                self.output_label = None

                            @property
                            def _common_path(self):

                                return '/Cisco-IOS-XR-evpn-oper:evpn/Cisco-IOS-XR-evpn-oper:standby/Cisco-IOS-XR-evpn-oper:evi-detail/Cisco-IOS-XR-evpn-oper:evi-children/Cisco-IOS-XR-evpn-oper:ethernet-auto-discoveries/Cisco-IOS-XR-evpn-oper:ethernet-auto-discovery/Cisco-IOS-XR-evpn-oper:path-buffer'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.next_hop is not None:
                                    return True

                                if self.output_label is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                                return meta._meta_table['Evpn.Standby.EviDetail.EviChildren.EthernetAutoDiscoveries.EthernetAutoDiscovery.PathBuffer']['meta_info']

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-evpn-oper:evpn/Cisco-IOS-XR-evpn-oper:standby/Cisco-IOS-XR-evpn-oper:evi-detail/Cisco-IOS-XR-evpn-oper:evi-children/Cisco-IOS-XR-evpn-oper:ethernet-auto-discoveries/Cisco-IOS-XR-evpn-oper:ethernet-auto-discovery'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.encap is not None:
                                return True

                            if self.esi1 is not None:
                                return True

                            if self.esi2 is not None:
                                return True

                            if self.esi3 is not None:
                                return True

                            if self.esi4 is not None:
                                return True

                            if self.esi5 is not None:
                                return True

                            if self.ethernet_segment_identifier is not None:
                                for child in self.ethernet_segment_identifier:
                                    if child is not None:
                                        return True

                            if self.ethernet_tag is not None:
                                return True

                            if self.ethernet_tag_xr is not None:
                                return True

                            if self.ethernet_vpnid is not None:
                                return True

                            if self.evi is not None:
                                return True

                            if self.is_local_ead is not None:
                                return True

                            if self.local_label is not None:
                                return True

                            if self.local_next_hop is not None:
                                return True

                            if self.num_paths is not None:
                                return True

                            if self.path_buffer is not None:
                                for child_ref in self.path_buffer:
                                    if child_ref._has_data():
                                        return True

                            if self.redundancy_single_active is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                            return meta._meta_table['Evpn.Standby.EviDetail.EviChildren.EthernetAutoDiscoveries.EthernetAutoDiscovery']['meta_info']

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-evpn-oper:evpn/Cisco-IOS-XR-evpn-oper:standby/Cisco-IOS-XR-evpn-oper:evi-detail/Cisco-IOS-XR-evpn-oper:evi-children/Cisco-IOS-XR-evpn-oper:ethernet-auto-discoveries'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.ethernet_auto_discovery is not None:
                            for child_ref in self.ethernet_auto_discovery:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                        return meta._meta_table['Evpn.Standby.EviDetail.EviChildren.EthernetAutoDiscoveries']['meta_info']


                class InclusiveMulticasts(object):
                    """
                    L2VPN EVPN IMCAST table
                    
                    .. attribute:: inclusive_multicast
                    
                    	L2VPN EVPN IMCAST table
                    	**type**\: list of    :py:class:`InclusiveMulticast <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.EviChildren.InclusiveMulticasts.InclusiveMulticast>`
                    
                    

                    """

                    _prefix = 'evpn-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.inclusive_multicast = YList()
                        self.inclusive_multicast.parent = self
                        self.inclusive_multicast.name = 'inclusive_multicast'


                    class InclusiveMulticast(object):
                        """
                        L2VPN EVPN IMCAST table
                        
                        .. attribute:: ethernet_tag
                        
                        	Ethernet Tag
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: ethernet_tag_xr
                        
                        	Ethernet Tag
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: evi
                        
                        	EVPN id
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: evi_xr
                        
                        	E\-VPN id
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_local_entry
                        
                        	Local entry
                        	**type**\:  bool
                        
                        .. attribute:: next_hop
                        
                        	IP of nexthop
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: originating_ip
                        
                        	Originating IP
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: originating_ip_xr
                        
                        	Originating IP
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: output_label
                        
                        	Output label
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'evpn-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.ethernet_tag = None
                            self.ethernet_tag_xr = None
                            self.evi = None
                            self.evi_xr = None
                            self.is_local_entry = None
                            self.next_hop = None
                            self.originating_ip = None
                            self.originating_ip_xr = None
                            self.output_label = None

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-evpn-oper:evpn/Cisco-IOS-XR-evpn-oper:standby/Cisco-IOS-XR-evpn-oper:evi-detail/Cisco-IOS-XR-evpn-oper:evi-children/Cisco-IOS-XR-evpn-oper:inclusive-multicasts/Cisco-IOS-XR-evpn-oper:inclusive-multicast'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.ethernet_tag is not None:
                                return True

                            if self.ethernet_tag_xr is not None:
                                return True

                            if self.evi is not None:
                                return True

                            if self.evi_xr is not None:
                                return True

                            if self.is_local_entry is not None:
                                return True

                            if self.next_hop is not None:
                                return True

                            if self.originating_ip is not None:
                                return True

                            if self.originating_ip_xr is not None:
                                return True

                            if self.output_label is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                            return meta._meta_table['Evpn.Standby.EviDetail.EviChildren.InclusiveMulticasts.InclusiveMulticast']['meta_info']

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-evpn-oper:evpn/Cisco-IOS-XR-evpn-oper:standby/Cisco-IOS-XR-evpn-oper:evi-detail/Cisco-IOS-XR-evpn-oper:evi-children/Cisco-IOS-XR-evpn-oper:inclusive-multicasts'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.inclusive_multicast is not None:
                            for child_ref in self.inclusive_multicast:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                        return meta._meta_table['Evpn.Standby.EviDetail.EviChildren.InclusiveMulticasts']['meta_info']


                class RouteTargets(object):
                    """
                    L2VPN EVPN EVI RT Child Table
                    
                    .. attribute:: route_target
                    
                    	L2VPN EVPN EVI RT Table
                    	**type**\: list of    :py:class:`RouteTarget <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.EviChildren.RouteTargets.RouteTarget>`
                    
                    

                    """

                    _prefix = 'evpn-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.route_target = YList()
                        self.route_target.parent = self
                        self.route_target.name = 'route_target'


                    class RouteTarget(object):
                        """
                        L2VPN EVPN EVI RT Table
                        
                        .. attribute:: addr_index
                        
                        	RT IP Index
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: address
                        
                        	RT IPv4 Address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: as_
                        
                        	Two or Four byte AS Number
                        	**type**\:  int
                        
                        	**range:** 1..4294967295
                        
                        .. attribute:: as_index
                        
                        	RT AS Index
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bd_name
                        
                        	Bridge Domain Name
                        	**type**\:  str
                        
                        .. attribute:: evi
                        
                        	EVPN id
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: evi_xr
                        
                        	VPN ID
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: format
                        
                        	Format of the route target
                        	**type**\:   :py:class:`BgpRouteTargetFormatEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.BgpRouteTargetFormatEnum>`
                        
                        .. attribute:: role
                        
                        	Role of the route target
                        	**type**\:   :py:class:`BgpRouteTargetRoleEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.BgpRouteTargetRoleEnum>`
                        
                        .. attribute:: route_target
                        
                        	Route Target
                        	**type**\:   :py:class:`RouteTarget_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_>`
                        
                        .. attribute:: route_target_role
                        
                        	RT Role
                        	**type**\:   :py:class:`L2VpnAdRtRoleEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2VpnAdRtRoleEnum>`
                        
                        .. attribute:: route_target_stitching
                        
                        	RT Stitching
                        	**type**\:  bool
                        
                        .. attribute:: type
                        
                        	Type of the route target
                        	**type**\:   :py:class:`BgpRouteTargetEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.BgpRouteTargetEnum>`
                        
                        

                        """

                        _prefix = 'evpn-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.addr_index = None
                            self.address = None
                            self.as_ = None
                            self.as_index = None
                            self.bd_name = None
                            self.evi = None
                            self.evi_xr = None
                            self.format = None
                            self.role = None
                            self.route_target = Evpn.Standby.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_()
                            self.route_target.parent = self
                            self.route_target_role = None
                            self.route_target_stitching = None
                            self.type = None


                        class RouteTarget_(object):
                            """
                            Route Target
                            
                            .. attribute:: es_import
                            
                            	es import
                            	**type**\:   :py:class:`EsImport <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.EsImport>`
                            
                            .. attribute:: four_byte_as
                            
                            	four byte as
                            	**type**\:   :py:class:`FourByteAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.FourByteAs>`
                            
                            .. attribute:: rt
                            
                            	RT
                            	**type**\:   :py:class:`L2VpnAdRtEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2VpnAdRtEnum>`
                            
                            .. attribute:: two_byte_as
                            
                            	two byte as
                            	**type**\:   :py:class:`TwoByteAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.TwoByteAs>`
                            
                            .. attribute:: v4_addr
                            
                            	v4 addr
                            	**type**\:   :py:class:`V4Addr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.V4Addr>`
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.es_import = Evpn.Standby.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.EsImport()
                                self.es_import.parent = self
                                self.four_byte_as = Evpn.Standby.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.FourByteAs()
                                self.four_byte_as.parent = self
                                self.rt = None
                                self.two_byte_as = Evpn.Standby.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.TwoByteAs()
                                self.two_byte_as.parent = self
                                self.v4_addr = Evpn.Standby.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.V4Addr()
                                self.v4_addr.parent = self


                            class TwoByteAs(object):
                                """
                                two byte as
                                
                                .. attribute:: four_byte_index
                                
                                	4 Byte Index
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: two_byte_as
                                
                                	2 Byte AS Number
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'evpn-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.four_byte_index = None
                                    self.two_byte_as = None

                                @property
                                def _common_path(self):

                                    return '/Cisco-IOS-XR-evpn-oper:evpn/Cisco-IOS-XR-evpn-oper:standby/Cisco-IOS-XR-evpn-oper:evi-detail/Cisco-IOS-XR-evpn-oper:evi-children/Cisco-IOS-XR-evpn-oper:route-targets/Cisco-IOS-XR-evpn-oper:route-target/Cisco-IOS-XR-evpn-oper:route-target/Cisco-IOS-XR-evpn-oper:two-byte-as'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.four_byte_index is not None:
                                        return True

                                    if self.two_byte_as is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                                    return meta._meta_table['Evpn.Standby.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.TwoByteAs']['meta_info']


                            class FourByteAs(object):
                                """
                                four byte as
                                
                                .. attribute:: four_byte_as
                                
                                	4 Byte AS Number
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: two_byte_index
                                
                                	2 Byte Index
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'evpn-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.four_byte_as = None
                                    self.two_byte_index = None

                                @property
                                def _common_path(self):

                                    return '/Cisco-IOS-XR-evpn-oper:evpn/Cisco-IOS-XR-evpn-oper:standby/Cisco-IOS-XR-evpn-oper:evi-detail/Cisco-IOS-XR-evpn-oper:evi-children/Cisco-IOS-XR-evpn-oper:route-targets/Cisco-IOS-XR-evpn-oper:route-target/Cisco-IOS-XR-evpn-oper:route-target/Cisco-IOS-XR-evpn-oper:four-byte-as'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.four_byte_as is not None:
                                        return True

                                    if self.two_byte_index is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                                    return meta._meta_table['Evpn.Standby.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.FourByteAs']['meta_info']


                            class V4Addr(object):
                                """
                                v4 addr
                                
                                .. attribute:: ipv4_address
                                
                                	IPv4 Address
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: two_byte_index
                                
                                	2 Byte Index
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'evpn-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.ipv4_address = None
                                    self.two_byte_index = None

                                @property
                                def _common_path(self):

                                    return '/Cisco-IOS-XR-evpn-oper:evpn/Cisco-IOS-XR-evpn-oper:standby/Cisco-IOS-XR-evpn-oper:evi-detail/Cisco-IOS-XR-evpn-oper:evi-children/Cisco-IOS-XR-evpn-oper:route-targets/Cisco-IOS-XR-evpn-oper:route-target/Cisco-IOS-XR-evpn-oper:route-target/Cisco-IOS-XR-evpn-oper:v4-addr'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.ipv4_address is not None:
                                        return True

                                    if self.two_byte_index is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                                    return meta._meta_table['Evpn.Standby.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.V4Addr']['meta_info']


                            class EsImport(object):
                                """
                                es import
                                
                                .. attribute:: high_bytes
                                
                                	Top 4 bytes of ES Import
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: low_bytes
                                
                                	Low 2 bytes of ES Import
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'evpn-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.high_bytes = None
                                    self.low_bytes = None

                                @property
                                def _common_path(self):

                                    return '/Cisco-IOS-XR-evpn-oper:evpn/Cisco-IOS-XR-evpn-oper:standby/Cisco-IOS-XR-evpn-oper:evi-detail/Cisco-IOS-XR-evpn-oper:evi-children/Cisco-IOS-XR-evpn-oper:route-targets/Cisco-IOS-XR-evpn-oper:route-target/Cisco-IOS-XR-evpn-oper:route-target/Cisco-IOS-XR-evpn-oper:es-import'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.high_bytes is not None:
                                        return True

                                    if self.low_bytes is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                                    return meta._meta_table['Evpn.Standby.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.EsImport']['meta_info']

                            @property
                            def _common_path(self):

                                return '/Cisco-IOS-XR-evpn-oper:evpn/Cisco-IOS-XR-evpn-oper:standby/Cisco-IOS-XR-evpn-oper:evi-detail/Cisco-IOS-XR-evpn-oper:evi-children/Cisco-IOS-XR-evpn-oper:route-targets/Cisco-IOS-XR-evpn-oper:route-target/Cisco-IOS-XR-evpn-oper:route-target'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.es_import is not None and self.es_import._has_data():
                                    return True

                                if self.four_byte_as is not None and self.four_byte_as._has_data():
                                    return True

                                if self.rt is not None:
                                    return True

                                if self.two_byte_as is not None and self.two_byte_as._has_data():
                                    return True

                                if self.v4_addr is not None and self.v4_addr._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                                return meta._meta_table['Evpn.Standby.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_']['meta_info']

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-evpn-oper:evpn/Cisco-IOS-XR-evpn-oper:standby/Cisco-IOS-XR-evpn-oper:evi-detail/Cisco-IOS-XR-evpn-oper:evi-children/Cisco-IOS-XR-evpn-oper:route-targets/Cisco-IOS-XR-evpn-oper:route-target'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.addr_index is not None:
                                return True

                            if self.address is not None:
                                return True

                            if self.as_ is not None:
                                return True

                            if self.as_index is not None:
                                return True

                            if self.bd_name is not None:
                                return True

                            if self.evi is not None:
                                return True

                            if self.evi_xr is not None:
                                return True

                            if self.format is not None:
                                return True

                            if self.role is not None:
                                return True

                            if self.route_target is not None and self.route_target._has_data():
                                return True

                            if self.route_target_role is not None:
                                return True

                            if self.route_target_stitching is not None:
                                return True

                            if self.type is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                            return meta._meta_table['Evpn.Standby.EviDetail.EviChildren.RouteTargets.RouteTarget']['meta_info']

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-evpn-oper:evpn/Cisco-IOS-XR-evpn-oper:standby/Cisco-IOS-XR-evpn-oper:evi-detail/Cisco-IOS-XR-evpn-oper:evi-children/Cisco-IOS-XR-evpn-oper:route-targets'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.route_target is not None:
                            for child_ref in self.route_target:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                        return meta._meta_table['Evpn.Standby.EviDetail.EviChildren.RouteTargets']['meta_info']


                class Macs(object):
                    """
                    L2VPN EVPN EVI MAC table
                    
                    .. attribute:: mac
                    
                    	L2VPN EVPN MAC table
                    	**type**\: list of    :py:class:`Mac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.EviChildren.Macs.Mac>`
                    
                    

                    """

                    _prefix = 'evpn-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.mac = YList()
                        self.mac.parent = self
                        self.mac.name = 'mac'


                    class Mac(object):
                        """
                        L2VPN EVPN MAC table
                        
                        .. attribute:: esi_port_key
                        
                        	ESI port key
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: ethernet_tag
                        
                        	Ethernet Tag ID
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: ethernet_tag_xr
                        
                        	Ethernet Tag
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: evi
                        
                        	EVPN id
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: internal_label
                        
                        	MPLS Internal Label
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ip_address
                        
                        	IP Address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: ip_address_xr
                        
                        	IP address (v6 format)
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: is_local_mac
                        
                        	Indication of MAC being locally generated
                        	**type**\:  bool
                        
                        .. attribute:: is_remote_mac
                        
                        	Indication of MAC being remotely generated
                        	**type**\:  bool
                        
                        .. attribute:: is_static
                        
                        	Indication if MAC is statically configured
                        	**type**\:  bool
                        
                        .. attribute:: learned_bridge_port_name
                        
                        	Port the MAC was learned on
                        	**type**\:  str
                        
                        .. attribute:: local_encap_type
                        
                        	Encap type of local MAC
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: local_ethernet_segment_identifier
                        
                        	Local Ethernet Segment id
                        	**type**\:  list of int
                        
                        	**range:** 0..255
                        
                        .. attribute:: local_label
                        
                        	Associated local label
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: local_seq_id
                        
                        	local seq id
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: mac_address
                        
                        	MAC address
                        	**type**\:  str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        .. attribute:: mac_address_xr
                        
                        	MAC address
                        	**type**\:  str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        .. attribute:: mac_flush_received
                        
                        	Number of flushes received 
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: mac_flush_requested
                        
                        	Number of flushes requested 
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: num_paths
                        
                        	 Number of items in path list buffer
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: path_buffer
                        
                        	Path List Buffer
                        	**type**\: list of    :py:class:`PathBuffer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.EviChildren.Macs.Mac.PathBuffer>`
                        
                        .. attribute:: remote_encap_type
                        
                        	Encap type of remote MAC
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: remote_ethernet_segment_identifier
                        
                        	Remote Ethernet Segment id
                        	**type**\:  list of int
                        
                        	**range:** 0..255
                        
                        .. attribute:: remote_seq_id
                        
                        	remote seq id
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: resolved
                        
                        	Internal Label has resolved per\-ES EAD and per\-EVI EAD or MAC routes
                        	**type**\:  bool
                        
                        .. attribute:: soo_nexthop
                        
                        	SOO nexthop (v6 format)
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'evpn-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.esi_port_key = None
                            self.ethernet_tag = None
                            self.ethernet_tag_xr = None
                            self.evi = None
                            self.internal_label = None
                            self.ip_address = None
                            self.ip_address_xr = None
                            self.is_local_mac = None
                            self.is_remote_mac = None
                            self.is_static = None
                            self.learned_bridge_port_name = None
                            self.local_encap_type = None
                            self.local_ethernet_segment_identifier = YLeafList()
                            self.local_ethernet_segment_identifier.parent = self
                            self.local_ethernet_segment_identifier.name = 'local_ethernet_segment_identifier'
                            self.local_label = None
                            self.local_seq_id = None
                            self.mac_address = None
                            self.mac_address_xr = None
                            self.mac_flush_received = None
                            self.mac_flush_requested = None
                            self.num_paths = None
                            self.path_buffer = YList()
                            self.path_buffer.parent = self
                            self.path_buffer.name = 'path_buffer'
                            self.remote_encap_type = None
                            self.remote_ethernet_segment_identifier = YLeafList()
                            self.remote_ethernet_segment_identifier.parent = self
                            self.remote_ethernet_segment_identifier.name = 'remote_ethernet_segment_identifier'
                            self.remote_seq_id = None
                            self.resolved = None
                            self.soo_nexthop = None


                        class PathBuffer(object):
                            """
                            Path List Buffer
                            
                            .. attribute:: next_hop
                            
                            	Next\-hop IP address (v6 format)
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: output_label
                            
                            	Output Label
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.next_hop = None
                                self.output_label = None

                            @property
                            def _common_path(self):

                                return '/Cisco-IOS-XR-evpn-oper:evpn/Cisco-IOS-XR-evpn-oper:standby/Cisco-IOS-XR-evpn-oper:evi-detail/Cisco-IOS-XR-evpn-oper:evi-children/Cisco-IOS-XR-evpn-oper:macs/Cisco-IOS-XR-evpn-oper:mac/Cisco-IOS-XR-evpn-oper:path-buffer'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.next_hop is not None:
                                    return True

                                if self.output_label is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                                return meta._meta_table['Evpn.Standby.EviDetail.EviChildren.Macs.Mac.PathBuffer']['meta_info']

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-evpn-oper:evpn/Cisco-IOS-XR-evpn-oper:standby/Cisco-IOS-XR-evpn-oper:evi-detail/Cisco-IOS-XR-evpn-oper:evi-children/Cisco-IOS-XR-evpn-oper:macs/Cisco-IOS-XR-evpn-oper:mac'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.esi_port_key is not None:
                                return True

                            if self.ethernet_tag is not None:
                                return True

                            if self.ethernet_tag_xr is not None:
                                return True

                            if self.evi is not None:
                                return True

                            if self.internal_label is not None:
                                return True

                            if self.ip_address is not None:
                                return True

                            if self.ip_address_xr is not None:
                                return True

                            if self.is_local_mac is not None:
                                return True

                            if self.is_remote_mac is not None:
                                return True

                            if self.is_static is not None:
                                return True

                            if self.learned_bridge_port_name is not None:
                                return True

                            if self.local_encap_type is not None:
                                return True

                            if self.local_ethernet_segment_identifier is not None:
                                for child in self.local_ethernet_segment_identifier:
                                    if child is not None:
                                        return True

                            if self.local_label is not None:
                                return True

                            if self.local_seq_id is not None:
                                return True

                            if self.mac_address is not None:
                                return True

                            if self.mac_address_xr is not None:
                                return True

                            if self.mac_flush_received is not None:
                                return True

                            if self.mac_flush_requested is not None:
                                return True

                            if self.num_paths is not None:
                                return True

                            if self.path_buffer is not None:
                                for child_ref in self.path_buffer:
                                    if child_ref._has_data():
                                        return True

                            if self.remote_encap_type is not None:
                                return True

                            if self.remote_ethernet_segment_identifier is not None:
                                for child in self.remote_ethernet_segment_identifier:
                                    if child is not None:
                                        return True

                            if self.remote_seq_id is not None:
                                return True

                            if self.resolved is not None:
                                return True

                            if self.soo_nexthop is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                            return meta._meta_table['Evpn.Standby.EviDetail.EviChildren.Macs.Mac']['meta_info']

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-evpn-oper:evpn/Cisco-IOS-XR-evpn-oper:standby/Cisco-IOS-XR-evpn-oper:evi-detail/Cisco-IOS-XR-evpn-oper:evi-children/Cisco-IOS-XR-evpn-oper:macs'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.mac is not None:
                            for child_ref in self.mac:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                        return meta._meta_table['Evpn.Standby.EviDetail.EviChildren.Macs']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-evpn-oper:evpn/Cisco-IOS-XR-evpn-oper:standby/Cisco-IOS-XR-evpn-oper:evi-detail/Cisco-IOS-XR-evpn-oper:evi-children'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.ethernet_auto_discoveries is not None and self.ethernet_auto_discoveries._has_data():
                        return True

                    if self.inclusive_multicasts is not None and self.inclusive_multicasts._has_data():
                        return True

                    if self.macs is not None and self.macs._has_data():
                        return True

                    if self.neighbors is not None and self.neighbors._has_data():
                        return True

                    if self.route_targets is not None and self.route_targets._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                    return meta._meta_table['Evpn.Standby.EviDetail.EviChildren']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-evpn-oper:evpn/Cisco-IOS-XR-evpn-oper:standby/Cisco-IOS-XR-evpn-oper:evi-detail'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.elements is not None and self.elements._has_data():
                    return True

                if self.evi_children is not None and self.evi_children._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                return meta._meta_table['Evpn.Standby.EviDetail']['meta_info']


        class EthernetSegments(object):
            """
            EVPN Ethernet\-Segment Table
            
            .. attribute:: ethernet_segment
            
            	EVPN Ethernet\-Segment Entry
            	**type**\: list of    :py:class:`EthernetSegment <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EthernetSegments.EthernetSegment>`
            
            

            """

            _prefix = 'evpn-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.ethernet_segment = YList()
                self.ethernet_segment.parent = self
                self.ethernet_segment.name = 'ethernet_segment'


            class EthernetSegment(object):
                """
                EVPN Ethernet\-Segment Entry
                
                .. attribute:: elected_d_fs
                
                	Count of service carving results \- elected
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: es_bgp_gates
                
                	ES BGP Gates
                	**type**\:  str
                
                .. attribute:: es_l2fib_gates
                
                	ES L2FIB Gates
                	**type**\:  str
                
                .. attribute:: esi1
                
                	ES id (part 1/5)
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{1,8}
                
                .. attribute:: esi2
                
                	ES id (part 2/5)
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{1,8}
                
                .. attribute:: esi3
                
                	ES id (part 3/5)
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{1,8}
                
                .. attribute:: esi4
                
                	ES id (part 4/5)
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{1,8}
                
                .. attribute:: esi5
                
                	ES id (part 5/5)
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{1,8}
                
                .. attribute:: esi_type
                
                	ESI Type
                	**type**\:   :py:class:`L2VpnEvpnEsiEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2VpnEvpnEsiEnum>`
                
                .. attribute:: ethernet_segment_identifier
                
                	Ethernet Segment id
                	**type**\:  list of int
                
                	**range:** 0..255
                
                .. attribute:: ethernet_segment_name
                
                	Ethernet Segment Name
                	**type**\:  str
                
                .. attribute:: ethernet_segment_state
                
                	State of the ethernet segment
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: force_single_home
                
                	Ethernet\-Segment forced to single home
                	**type**\:  bool
                
                .. attribute:: forwarder_ports
                
                	Count of Forwarders (AC, AC PW, VFI PW)
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: if_handle
                
                	Main port ifhandle
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: interface_name
                
                	Interface
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: load_balance_mode_config
                
                	Configured load balancing mode
                	**type**\:   :py:class:`L2VpnEvpnLbModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2VpnEvpnLbModeEnum>`
                
                .. attribute:: load_balance_mode_is_default
                
                	Load balancing mode is default
                	**type**\:  bool
                
                .. attribute:: load_balance_mode_oper
                
                	Operational load balancing mode
                	**type**\:   :py:class:`L2VpnEvpnLbModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2VpnEvpnLbModeEnum>`
                
                .. attribute:: local_split_horizon_group_label
                
                	Local split horizon group label
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: mac_flushing_mode_config
                
                	Configured MAC Flushing mode
                	**type**\:   :py:class:`L2VpnEvpnMfModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2VpnEvpnMfModeEnum>`
                
                .. attribute:: main_port_mac
                
                	Main Port MAC Address
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: main_port_role
                
                	Main port redundancy group role
                	**type**\:   :py:class:`L2VpnRgStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2VpnRgStateEnum>`
                
                .. attribute:: mp_protected
                
                	MP is protected and not under EVPN control
                	**type**\:  bool
                
                .. attribute:: next_hop
                
                	List of nexthop IPv6 addresses
                	**type**\: list of    :py:class:`NextHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EthernetSegments.EthernetSegment.NextHop>`
                
                .. attribute:: not_config_d_fs
                
                	Count of service carving results \- missing config detected
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: not_elected_d_fs
                
                	Count of service carving results \- not elected
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: num_up_p_ws
                
                	Number of PWs in Up state
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: peering_timer
                
                	Configured timer for triggering DF election (seconds)
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: peering_timer_left
                
                	Milliseconds left on DF election timer
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: millisecond
                
                .. attribute:: primary_service
                
                	List of Primary services ESI/I\-SIDs
                	**type**\:  list of int
                
                	**range:** 0..4294967295
                
                .. attribute:: primary_services_input
                
                	Input string of Primary services ESI/I\-SIDs
                	**type**\:  str
                
                .. attribute:: recovery_timer
                
                	Configured timer for (STP) recovery (seconds)
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: recovery_timer_left
                
                	Milliseconds left on (STP) recovery timer
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: millisecond
                
                .. attribute:: remote_split_horizon_group_label
                
                	Remote split horizon group labels
                	**type**\: list of    :py:class:`RemoteSplitHorizonGroupLabel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EthernetSegments.EthernetSegment.RemoteSplitHorizonGroupLabel>`
                
                .. attribute:: route_target
                
                	ES\-Import Route Target
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: rt_origin
                
                	Origin of operational ES\-Import RT
                	**type**\:   :py:class:`L2VpnEvpnRtOriginEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2VpnEvpnRtOriginEnum>`
                
                .. attribute:: secondary_service
                
                	List of Secondary services ESI/I\-SIDs
                	**type**\:  list of int
                
                	**range:** 0..4294967295
                
                .. attribute:: secondary_services_input
                
                	Input string of Secondary services ESI/I\-SIDs
                	**type**\:  str
                
                .. attribute:: service_carving_mode
                
                	Service carving mode
                	**type**\:   :py:class:`L2VpnEvpnScModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2VpnEvpnScModeEnum>`
                
                .. attribute:: service_carving_result
                
                	Service carving results
                	**type**\:  list of int
                
                	**range:** 0..4294967295
                
                .. attribute:: service_carving_type
                
                	Service Carving Type
                	**type**\:   :py:class:`L2VpnEvpnScEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2VpnEvpnScEnum>`
                
                .. attribute:: source_mac_oper
                
                	Operational Source MAC address
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: source_mac_origin
                
                	Origin of operational source MAC address
                	**type**\:   :py:class:`L2VpnEvpnSmacSrcEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2VpnEvpnSmacSrcEnum>`
                
                

                """

                _prefix = 'evpn-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.elected_d_fs = None
                    self.es_bgp_gates = None
                    self.es_l2fib_gates = None
                    self.esi1 = None
                    self.esi2 = None
                    self.esi3 = None
                    self.esi4 = None
                    self.esi5 = None
                    self.esi_type = None
                    self.ethernet_segment_identifier = YLeafList()
                    self.ethernet_segment_identifier.parent = self
                    self.ethernet_segment_identifier.name = 'ethernet_segment_identifier'
                    self.ethernet_segment_name = None
                    self.ethernet_segment_state = None
                    self.force_single_home = None
                    self.forwarder_ports = None
                    self.if_handle = None
                    self.interface_name = None
                    self.load_balance_mode_config = None
                    self.load_balance_mode_is_default = None
                    self.load_balance_mode_oper = None
                    self.local_split_horizon_group_label = None
                    self.mac_flushing_mode_config = None
                    self.main_port_mac = None
                    self.main_port_role = None
                    self.mp_protected = None
                    self.next_hop = YList()
                    self.next_hop.parent = self
                    self.next_hop.name = 'next_hop'
                    self.not_config_d_fs = None
                    self.not_elected_d_fs = None
                    self.num_up_p_ws = None
                    self.peering_timer = None
                    self.peering_timer_left = None
                    self.primary_service = YLeafList()
                    self.primary_service.parent = self
                    self.primary_service.name = 'primary_service'
                    self.primary_services_input = None
                    self.recovery_timer = None
                    self.recovery_timer_left = None
                    self.remote_split_horizon_group_label = YList()
                    self.remote_split_horizon_group_label.parent = self
                    self.remote_split_horizon_group_label.name = 'remote_split_horizon_group_label'
                    self.route_target = None
                    self.rt_origin = None
                    self.secondary_service = YLeafList()
                    self.secondary_service.parent = self
                    self.secondary_service.name = 'secondary_service'
                    self.secondary_services_input = None
                    self.service_carving_mode = None
                    self.service_carving_result = YLeafList()
                    self.service_carving_result.parent = self
                    self.service_carving_result.name = 'service_carving_result'
                    self.service_carving_type = None
                    self.source_mac_oper = None
                    self.source_mac_origin = None


                class NextHop(object):
                    """
                    List of nexthop IPv6 addresses
                    
                    .. attribute:: next_hop
                    
                    	Next\-hop IP address (v6 format)
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'evpn-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.next_hop = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-evpn-oper:evpn/Cisco-IOS-XR-evpn-oper:standby/Cisco-IOS-XR-evpn-oper:ethernet-segments/Cisco-IOS-XR-evpn-oper:ethernet-segment/Cisco-IOS-XR-evpn-oper:next-hop'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.next_hop is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                        return meta._meta_table['Evpn.Standby.EthernetSegments.EthernetSegment.NextHop']['meta_info']


                class RemoteSplitHorizonGroupLabel(object):
                    """
                    Remote split horizon group labels
                    
                    .. attribute:: label
                    
                    	Split horizon label associated with next\-hop address
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: next_hop
                    
                    	Next\-hop IP address (v6 format)
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'evpn-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.label = None
                        self.next_hop = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-evpn-oper:evpn/Cisco-IOS-XR-evpn-oper:standby/Cisco-IOS-XR-evpn-oper:ethernet-segments/Cisco-IOS-XR-evpn-oper:ethernet-segment/Cisco-IOS-XR-evpn-oper:remote-split-horizon-group-label'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.label is not None:
                            return True

                        if self.next_hop is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                        return meta._meta_table['Evpn.Standby.EthernetSegments.EthernetSegment.RemoteSplitHorizonGroupLabel']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-evpn-oper:evpn/Cisco-IOS-XR-evpn-oper:standby/Cisco-IOS-XR-evpn-oper:ethernet-segments/Cisco-IOS-XR-evpn-oper:ethernet-segment'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.elected_d_fs is not None:
                        return True

                    if self.es_bgp_gates is not None:
                        return True

                    if self.es_l2fib_gates is not None:
                        return True

                    if self.esi1 is not None:
                        return True

                    if self.esi2 is not None:
                        return True

                    if self.esi3 is not None:
                        return True

                    if self.esi4 is not None:
                        return True

                    if self.esi5 is not None:
                        return True

                    if self.esi_type is not None:
                        return True

                    if self.ethernet_segment_identifier is not None:
                        for child in self.ethernet_segment_identifier:
                            if child is not None:
                                return True

                    if self.ethernet_segment_name is not None:
                        return True

                    if self.ethernet_segment_state is not None:
                        return True

                    if self.force_single_home is not None:
                        return True

                    if self.forwarder_ports is not None:
                        return True

                    if self.if_handle is not None:
                        return True

                    if self.interface_name is not None:
                        return True

                    if self.load_balance_mode_config is not None:
                        return True

                    if self.load_balance_mode_is_default is not None:
                        return True

                    if self.load_balance_mode_oper is not None:
                        return True

                    if self.local_split_horizon_group_label is not None:
                        return True

                    if self.mac_flushing_mode_config is not None:
                        return True

                    if self.main_port_mac is not None:
                        return True

                    if self.main_port_role is not None:
                        return True

                    if self.mp_protected is not None:
                        return True

                    if self.next_hop is not None:
                        for child_ref in self.next_hop:
                            if child_ref._has_data():
                                return True

                    if self.not_config_d_fs is not None:
                        return True

                    if self.not_elected_d_fs is not None:
                        return True

                    if self.num_up_p_ws is not None:
                        return True

                    if self.peering_timer is not None:
                        return True

                    if self.peering_timer_left is not None:
                        return True

                    if self.primary_service is not None:
                        for child in self.primary_service:
                            if child is not None:
                                return True

                    if self.primary_services_input is not None:
                        return True

                    if self.recovery_timer is not None:
                        return True

                    if self.recovery_timer_left is not None:
                        return True

                    if self.remote_split_horizon_group_label is not None:
                        for child_ref in self.remote_split_horizon_group_label:
                            if child_ref._has_data():
                                return True

                    if self.route_target is not None:
                        return True

                    if self.rt_origin is not None:
                        return True

                    if self.secondary_service is not None:
                        for child in self.secondary_service:
                            if child is not None:
                                return True

                    if self.secondary_services_input is not None:
                        return True

                    if self.service_carving_mode is not None:
                        return True

                    if self.service_carving_result is not None:
                        for child in self.service_carving_result:
                            if child is not None:
                                return True

                    if self.service_carving_type is not None:
                        return True

                    if self.source_mac_oper is not None:
                        return True

                    if self.source_mac_origin is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                    return meta._meta_table['Evpn.Standby.EthernetSegments.EthernetSegment']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-evpn-oper:evpn/Cisco-IOS-XR-evpn-oper:standby/Cisco-IOS-XR-evpn-oper:ethernet-segments'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ethernet_segment is not None:
                    for child_ref in self.ethernet_segment:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                return meta._meta_table['Evpn.Standby.EthernetSegments']['meta_info']


        class AcIds(object):
            """
            EVPN AC ID table
            
            .. attribute:: ac_id
            
            	EVPN AC ID table
            	**type**\: list of    :py:class:`AcId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.AcIds.AcId>`
            
            

            """

            _prefix = 'evpn-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.ac_id = YList()
                self.ac_id.parent = self
                self.ac_id.name = 'ac_id'


            class AcId(object):
                """
                EVPN AC ID table
                
                .. attribute:: ac_id
                
                	AC ID
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: evi
                
                	EVPN id
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: evi_xr
                
                	E\-VPN id
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: neighbor
                
                	Neighbor IP
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                

                """

                _prefix = 'evpn-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.ac_id = None
                    self.evi = None
                    self.evi_xr = None
                    self.neighbor = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-evpn-oper:evpn/Cisco-IOS-XR-evpn-oper:standby/Cisco-IOS-XR-evpn-oper:ac-ids/Cisco-IOS-XR-evpn-oper:ac-id'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.ac_id is not None:
                        return True

                    if self.evi is not None:
                        return True

                    if self.evi_xr is not None:
                        return True

                    if self.neighbor is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                    return meta._meta_table['Evpn.Standby.AcIds.AcId']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-evpn-oper:evpn/Cisco-IOS-XR-evpn-oper:standby/Cisco-IOS-XR-evpn-oper:ac-ids'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ac_id is not None:
                    for child_ref in self.ac_id:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
                return meta._meta_table['Evpn.Standby.AcIds']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-evpn-oper:evpn/Cisco-IOS-XR-evpn-oper:standby'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ac_ids is not None and self.ac_ids._has_data():
                return True

            if self.ethernet_segments is not None and self.ethernet_segments._has_data():
                return True

            if self.evi_detail is not None and self.evi_detail._has_data():
                return True

            if self.evis is not None and self.evis._has_data():
                return True

            if self.summary is not None and self.summary._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
            return meta._meta_table['Evpn.Standby']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-evpn-oper:evpn'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.active is not None and self.active._has_data():
            return True

        if self.nodes is not None and self.nodes._has_data():
            return True

        if self.standby is not None and self.standby._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_evpn_oper as meta
        return meta._meta_table['Evpn']['meta_info']


