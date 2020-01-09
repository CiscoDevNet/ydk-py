""" Cisco_IOS_XR_l2rib_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR l2rib package operational data.

This module contains definitions
for the following management objects\:
  l2rib\: L2RIB operational information

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class L2ribAfi(Enum):
    """
    L2ribAfi (Enum Class)

    L2rib afi

    .. data:: l2rib_address_family_ipv4 = 0

    	l2rib address family ipv4

    .. data:: l2rib_address_family_ipv6 = 1

    	l2rib address family ipv6

    .. data:: l2rib_address_family_invalid = 2

    	l2rib address family invalid

    """

    l2rib_address_family_ipv4 = Enum.YLeaf(0, "l2rib-address-family-ipv4")

    l2rib_address_family_ipv6 = Enum.YLeaf(1, "l2rib-address-family-ipv6")

    l2rib_address_family_invalid = Enum.YLeaf(2, "l2rib-address-family-invalid")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
        return meta._meta_table['L2ribAfi']


class L2ribBagObj(Enum):
    """
    L2ribBagObj (Enum Class)

    L2RIB Object Types

    .. data:: l2rib_bag_obj_type_min = 0

    	Invalid Object Type

    .. data:: l2rib_bag_obj_type_all = 1

    	All

    .. data:: l2rib_bag_obj_type_mac = 2

    	Mac

    .. data:: l2rib_bag_obj_type_ipv4_mcast = 3

    	IPv4 Multicast

    .. data:: l2rib_bag_obj_type_ipv6_mcast = 4

    	IPv6 Multicast

    .. data:: l2rib_bag_obj_type_topology = 5

    	Topology

    .. data:: l2rib_bag_obj_type_ead = 6

    	Ethernet AD

    .. data:: l2rib_bag_obj_type_evpn_pl = 7

    	EVPN Path List

    .. data:: l2rib_bag_obj_type_topo_attribute = 8

    	Topology Attribute

    .. data:: l2rib_bag_obj_type_imet_route = 9

    	IMET

    .. data:: l2rib_bag_obj_type_mac_ip = 13

    	Mac IP

    """

    l2rib_bag_obj_type_min = Enum.YLeaf(0, "l2rib-bag-obj-type-min")

    l2rib_bag_obj_type_all = Enum.YLeaf(1, "l2rib-bag-obj-type-all")

    l2rib_bag_obj_type_mac = Enum.YLeaf(2, "l2rib-bag-obj-type-mac")

    l2rib_bag_obj_type_ipv4_mcast = Enum.YLeaf(3, "l2rib-bag-obj-type-ipv4-mcast")

    l2rib_bag_obj_type_ipv6_mcast = Enum.YLeaf(4, "l2rib-bag-obj-type-ipv6-mcast")

    l2rib_bag_obj_type_topology = Enum.YLeaf(5, "l2rib-bag-obj-type-topology")

    l2rib_bag_obj_type_ead = Enum.YLeaf(6, "l2rib-bag-obj-type-ead")

    l2rib_bag_obj_type_evpn_pl = Enum.YLeaf(7, "l2rib-bag-obj-type-evpn-pl")

    l2rib_bag_obj_type_topo_attribute = Enum.YLeaf(8, "l2rib-bag-obj-type-topo-attribute")

    l2rib_bag_obj_type_imet_route = Enum.YLeaf(9, "l2rib-bag-obj-type-imet-route")

    l2rib_bag_obj_type_mac_ip = Enum.YLeaf(13, "l2rib-bag-obj-type-mac-ip")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
        return meta._meta_table['L2ribBagObj']


class L2ribBagProducerId(Enum):
    """
    L2ribBagProducerId (Enum Class)

    L2RIB Producer Types

    .. data:: l2rib_bag_prod_none = 0

    	None

    .. data:: l2rib_bag_prod_best_route = 1

    	Best Route

    .. data:: l2rib_bag_prod_static = 2

    	Static

    .. data:: l2rib_bag_prod_local = 3

    	Local

    .. data:: l2rib_bag_prod_isis = 4

    	IS IS

    .. data:: l2rib_bag_prod_bgp = 5

    	BGP

    .. data:: l2rib_bag_prod_igmp = 6

    	IGMP

    .. data:: l2rib_bag_prod_prod_mld = 7

    	MLD

    .. data:: l2rib_bag_prod_prod_otv = 8

    	OTV

    .. data:: l2rib_bag_prod_prod_l2vpn = 9

    	L2VPN

    .. data:: l2rib_bag_prod_prod_mac_mgr = 10

    	MAC MGR

    .. data:: l2rib_bag_prod_prod_vxlan = 11

    	VXLAN

    .. data:: l2rib_bag_prod_prod_hmm = 12

    	HMM

    .. data:: l2rib_bag_prod_prod_arp = 13

    	ARP

    .. data:: l2rib_bag_prod_prod_local_proxy = 14

    	Local Proxy

    .. data:: l2rib_bag_prod_prod_all = 255

    	All

    """

    l2rib_bag_prod_none = Enum.YLeaf(0, "l2rib-bag-prod-none")

    l2rib_bag_prod_best_route = Enum.YLeaf(1, "l2rib-bag-prod-best-route")

    l2rib_bag_prod_static = Enum.YLeaf(2, "l2rib-bag-prod-static")

    l2rib_bag_prod_local = Enum.YLeaf(3, "l2rib-bag-prod-local")

    l2rib_bag_prod_isis = Enum.YLeaf(4, "l2rib-bag-prod-isis")

    l2rib_bag_prod_bgp = Enum.YLeaf(5, "l2rib-bag-prod-bgp")

    l2rib_bag_prod_igmp = Enum.YLeaf(6, "l2rib-bag-prod-igmp")

    l2rib_bag_prod_prod_mld = Enum.YLeaf(7, "l2rib-bag-prod-prod-mld")

    l2rib_bag_prod_prod_otv = Enum.YLeaf(8, "l2rib-bag-prod-prod-otv")

    l2rib_bag_prod_prod_l2vpn = Enum.YLeaf(9, "l2rib-bag-prod-prod-l2vpn")

    l2rib_bag_prod_prod_mac_mgr = Enum.YLeaf(10, "l2rib-bag-prod-prod-mac-mgr")

    l2rib_bag_prod_prod_vxlan = Enum.YLeaf(11, "l2rib-bag-prod-prod-vxlan")

    l2rib_bag_prod_prod_hmm = Enum.YLeaf(12, "l2rib-bag-prod-prod-hmm")

    l2rib_bag_prod_prod_arp = Enum.YLeaf(13, "l2rib-bag-prod-prod-arp")

    l2rib_bag_prod_prod_local_proxy = Enum.YLeaf(14, "l2rib-bag-prod-prod-local-proxy")

    l2rib_bag_prod_prod_all = Enum.YLeaf(255, "l2rib-bag-prod-prod-all")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
        return meta._meta_table['L2ribBagProducerId']


class L2ribBagProducerState(Enum):
    """
    L2ribBagProducerState (Enum Class)

    L2RIB Producer States

    .. data:: l2rib_bag_prod_state_initial = 0

    	Initial

    .. data:: l2rib_bag_prod_state_staled = 1

    	Stale

    .. data:: l2rib_bag_prod_state_re_connected = 2

    	Reconnected

    .. data:: l2rib_bag_prod_state_converged = 3

    	Converged

    .. data:: l2rib_bag_prod_state_delete_p_end = 4

    	Delete Pending

    """

    l2rib_bag_prod_state_initial = Enum.YLeaf(0, "l2rib-bag-prod-state-initial")

    l2rib_bag_prod_state_staled = Enum.YLeaf(1, "l2rib-bag-prod-state-staled")

    l2rib_bag_prod_state_re_connected = Enum.YLeaf(2, "l2rib-bag-prod-state-re-connected")

    l2rib_bag_prod_state_converged = Enum.YLeaf(3, "l2rib-bag-prod-state-converged")

    l2rib_bag_prod_state_delete_p_end = Enum.YLeaf(4, "l2rib-bag-prod-state-delete-p-end")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
        return meta._meta_table['L2ribBagProducerState']


class L2ribMacRoute(Enum):
    """
    L2ribMacRoute (Enum Class)

    L2rib mac route

    .. data:: l2rib_mac_route_type_invalid = 0

    	l2rib mac route type invalid

    .. data:: l2rib_mac_route_type_regular = 1

    	l2rib mac route type regular

    .. data:: l2rib_mac_route_type_evpn_esi = 2

    	l2rib mac route type evpn esi

    .. data:: l2rib_mac_route_type_bmac = 3

    	l2rib mac route type bmac

    """

    l2rib_mac_route_type_invalid = Enum.YLeaf(0, "l2rib-mac-route-type-invalid")

    l2rib_mac_route_type_regular = Enum.YLeaf(1, "l2rib-mac-route-type-regular")

    l2rib_mac_route_type_evpn_esi = Enum.YLeaf(2, "l2rib-mac-route-type-evpn-esi")

    l2rib_mac_route_type_bmac = Enum.YLeaf(3, "l2rib-mac-route-type-bmac")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
        return meta._meta_table['L2ribMacRoute']


class L2ribNextHop(Enum):
    """
    L2ribNextHop (Enum Class)

    L2rib next hop

    .. data:: l2rib_next_hop_invalid = 0

    	l2rib next hop invalid

    .. data:: l2rib_next_hop_interface_ordinal = 1

    	l2rib next hop interface ordinal

    .. data:: l2rib_next_hop_interface_index = 2

    	l2rib next hop interface index

    .. data:: l2rib_next_hop_mac = 3

    	l2rib next hop mac

    .. data:: l2rib_next_hop_ipv4 = 4

    	l2rib next hop ipv4

    .. data:: l2rib_next_hop_ipv6 = 5

    	l2rib next hop ipv6

    .. data:: l2rib_next_hop_overlay = 6

    	l2rib next hop overlay

    .. data:: l2rib_next_hop_site_index = 7

    	l2rib next hop site index

    .. data:: l2rib_next_hop_label_ed = 8

    	l2rib next hop label ed

    .. data:: l2rib_next_hop_xid = 9

    	l2rib next hop xid

    """

    l2rib_next_hop_invalid = Enum.YLeaf(0, "l2rib-next-hop-invalid")

    l2rib_next_hop_interface_ordinal = Enum.YLeaf(1, "l2rib-next-hop-interface-ordinal")

    l2rib_next_hop_interface_index = Enum.YLeaf(2, "l2rib-next-hop-interface-index")

    l2rib_next_hop_mac = Enum.YLeaf(3, "l2rib-next-hop-mac")

    l2rib_next_hop_ipv4 = Enum.YLeaf(4, "l2rib-next-hop-ipv4")

    l2rib_next_hop_ipv6 = Enum.YLeaf(5, "l2rib-next-hop-ipv6")

    l2rib_next_hop_overlay = Enum.YLeaf(6, "l2rib-next-hop-overlay")

    l2rib_next_hop_site_index = Enum.YLeaf(7, "l2rib-next-hop-site-index")

    l2rib_next_hop_label_ed = Enum.YLeaf(8, "l2rib-next-hop-label-ed")

    l2rib_next_hop_xid = Enum.YLeaf(9, "l2rib-next-hop-xid")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
        return meta._meta_table['L2ribNextHop']



class L2rib(_Entity_):
    """
    L2RIB operational information 
    
    .. attribute:: producers_details
    
    	L2RIB detailed producer table
    	**type**\:  :py:class:`ProducersDetails <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.ProducersDetails>`
    
    	**config**\: False
    
    .. attribute:: summary
    
    	L2RIB EVPN Summary
    	**type**\:  :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.Summary>`
    
    	**config**\: False
    
    .. attribute:: producers
    
    	L2RIB producer table
    	**type**\:  :py:class:`Producers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.Producers>`
    
    	**config**\: False
    
    .. attribute:: clients
    
    	L2RIB client table
    	**type**\:  :py:class:`Clients <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.Clients>`
    
    	**config**\: False
    
    .. attribute:: evis_xr
    
    	L2RIB EVPN EVI Detail Table
    	**type**\:  :py:class:`EvisXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EvisXr>`
    
    	**config**\: False
    
    .. attribute:: clients_details
    
    	L2RIB detailed client table
    	**type**\:  :py:class:`ClientsDetails <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.ClientsDetails>`
    
    	**config**\: False
    
    .. attribute:: evi_child_tables
    
    	Container for all EVI Child Tables
    	**type**\:  :py:class:`EviChildTables <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables>`
    
    	**config**\: False
    
    .. attribute:: evis
    
    	L2RIB EVPN EVI Table
    	**type**\:  :py:class:`Evis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.Evis>`
    
    	**config**\: False
    
    

    """

    _prefix = 'l2rib-oper'
    _revision = '2015-11-09'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(L2rib, self).__init__()
        self._top_entity = None

        self.yang_name = "l2rib"
        self.yang_parent_name = "Cisco-IOS-XR-l2rib-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("producers-details", ("producers_details", L2rib.ProducersDetails)), ("summary", ("summary", L2rib.Summary)), ("producers", ("producers", L2rib.Producers)), ("clients", ("clients", L2rib.Clients)), ("evis-xr", ("evis_xr", L2rib.EvisXr)), ("clients-details", ("clients_details", L2rib.ClientsDetails)), ("evi-child-tables", ("evi_child_tables", L2rib.EviChildTables)), ("evis", ("evis", L2rib.Evis))])
        self._leafs = OrderedDict()

        self.producers_details = L2rib.ProducersDetails()
        self.producers_details.parent = self
        self._children_name_map["producers_details"] = "producers-details"

        self.summary = L2rib.Summary()
        self.summary.parent = self
        self._children_name_map["summary"] = "summary"

        self.producers = L2rib.Producers()
        self.producers.parent = self
        self._children_name_map["producers"] = "producers"

        self.clients = L2rib.Clients()
        self.clients.parent = self
        self._children_name_map["clients"] = "clients"

        self.evis_xr = L2rib.EvisXr()
        self.evis_xr.parent = self
        self._children_name_map["evis_xr"] = "evis-xr"

        self.clients_details = L2rib.ClientsDetails()
        self.clients_details.parent = self
        self._children_name_map["clients_details"] = "clients-details"

        self.evi_child_tables = L2rib.EviChildTables()
        self.evi_child_tables.parent = self
        self._children_name_map["evi_child_tables"] = "evi-child-tables"

        self.evis = L2rib.Evis()
        self.evis.parent = self
        self._children_name_map["evis"] = "evis"
        self._segment_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(L2rib, [], name, value)


    class ProducersDetails(_Entity_):
        """
        L2RIB detailed producer table
        
        .. attribute:: producers_detail
        
        	L2RIB producers detail information
        	**type**\: list of  		 :py:class:`ProducersDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.ProducersDetails.ProducersDetail>`
        
        	**config**\: False
        
        

        """

        _prefix = 'l2rib-oper'
        _revision = '2015-11-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(L2rib.ProducersDetails, self).__init__()

            self.yang_name = "producers-details"
            self.yang_parent_name = "l2rib"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("producers-detail", ("producers_detail", L2rib.ProducersDetails.ProducersDetail))])
            self._leafs = OrderedDict()

            self.producers_detail = YList(self)
            self._segment_path = lambda: "producers-details"
            self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(L2rib.ProducersDetails, [], name, value)


        class ProducersDetail(_Entity_):
            """
            L2RIB producers detail information
            
            .. attribute:: object_id
            
            	Object ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: product_id
            
            	Product ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: producer
            
            	Non\-detail Producer Bag
            	**type**\:  :py:class:`Producer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.ProducersDetails.ProducersDetail.Producer>`
            
            	**config**\: False
            
            .. attribute:: statistics
            
            	Producer Statistics
            	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.ProducersDetails.ProducersDetail.Statistics>`
            
            	**config**\: False
            
            .. attribute:: last_update_timestamp
            
            	Last Update Timestamp
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            

            """

            _prefix = 'l2rib-oper'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(L2rib.ProducersDetails.ProducersDetail, self).__init__()

                self.yang_name = "producers-detail"
                self.yang_parent_name = "producers-details"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("producer", ("producer", L2rib.ProducersDetails.ProducersDetail.Producer)), ("statistics", ("statistics", L2rib.ProducersDetails.ProducersDetail.Statistics))])
                self._leafs = OrderedDict([
                    ('object_id', (YLeaf(YType.uint32, 'object-id'), ['int'])),
                    ('product_id', (YLeaf(YType.uint32, 'product-id'), ['int'])),
                    ('last_update_timestamp', (YLeaf(YType.uint64, 'last-update-timestamp'), ['int'])),
                ])
                self.object_id = None
                self.product_id = None
                self.last_update_timestamp = None

                self.producer = L2rib.ProducersDetails.ProducersDetail.Producer()
                self.producer.parent = self
                self._children_name_map["producer"] = "producer"

                self.statistics = L2rib.ProducersDetails.ProducersDetail.Statistics()
                self.statistics.parent = self
                self._children_name_map["statistics"] = "statistics"
                self._segment_path = lambda: "producers-detail"
                self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/producers-details/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(L2rib.ProducersDetails.ProducersDetail, ['object_id', 'product_id', 'last_update_timestamp'], name, value)


            class Producer(_Entity_):
                """
                Non\-detail Producer Bag
                
                .. attribute:: client_id
                
                	Client ID
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: object_type
                
                	Object Type
                	**type**\:  :py:class:`L2ribBagObj <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2ribBagObj>`
                
                	**config**\: False
                
                .. attribute:: producer_id
                
                	Producer ID
                	**type**\:  :py:class:`L2ribBagProducerId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2ribBagProducerId>`
                
                	**config**\: False
                
                .. attribute:: producer_name
                
                	Producer Name
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: admin_distance
                
                	Admin Distance
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: purge_time
                
                	Purge Time
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: state
                
                	Producer State
                	**type**\:  :py:class:`L2ribBagProducerState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2ribBagProducerState>`
                
                	**config**\: False
                
                

                """

                _prefix = 'l2rib-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(L2rib.ProducersDetails.ProducersDetail.Producer, self).__init__()

                    self.yang_name = "producer"
                    self.yang_parent_name = "producers-detail"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('client_id', (YLeaf(YType.uint32, 'client-id'), ['int'])),
                        ('object_type', (YLeaf(YType.enumeration, 'object-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper', 'L2ribBagObj', '')])),
                        ('producer_id', (YLeaf(YType.enumeration, 'producer-id'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper', 'L2ribBagProducerId', '')])),
                        ('producer_name', (YLeaf(YType.str, 'producer-name'), ['str'])),
                        ('admin_distance', (YLeaf(YType.uint32, 'admin-distance'), ['int'])),
                        ('purge_time', (YLeaf(YType.uint32, 'purge-time'), ['int'])),
                        ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper', 'L2ribBagProducerState', '')])),
                    ])
                    self.client_id = None
                    self.object_type = None
                    self.producer_id = None
                    self.producer_name = None
                    self.admin_distance = None
                    self.purge_time = None
                    self.state = None
                    self._segment_path = lambda: "producer"
                    self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/producers-details/producers-detail/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(L2rib.ProducersDetails.ProducersDetail.Producer, ['client_id', 'object_type', 'producer_id', 'producer_name', 'admin_distance', 'purge_time', 'state'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                    return meta._meta_table['L2rib.ProducersDetails.ProducersDetail.Producer']['meta_info']


            class Statistics(_Entity_):
                """
                Producer Statistics
                
                .. attribute:: statistics
                
                	Statistics
                	**type**\:  :py:class:`Statistics_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.ProducersDetails.ProducersDetail.Statistics.Statistics_>`
                
                	**config**\: False
                
                .. attribute:: producer_id
                
                	Producer ID
                	**type**\:  :py:class:`L2ribBagProducerId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2ribBagProducerId>`
                
                	**config**\: False
                
                .. attribute:: producer_name
                
                	Producer Name
                	**type**\: str
                
                	**config**\: False
                
                

                """

                _prefix = 'l2rib-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(L2rib.ProducersDetails.ProducersDetail.Statistics, self).__init__()

                    self.yang_name = "statistics"
                    self.yang_parent_name = "producers-detail"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("statistics", ("statistics", L2rib.ProducersDetails.ProducersDetail.Statistics.Statistics_))])
                    self._leafs = OrderedDict([
                        ('producer_id', (YLeaf(YType.enumeration, 'producer-id'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper', 'L2ribBagProducerId', '')])),
                        ('producer_name', (YLeaf(YType.str, 'producer-name'), ['str'])),
                    ])
                    self.producer_id = None
                    self.producer_name = None

                    self.statistics = L2rib.ProducersDetails.ProducersDetail.Statistics.Statistics_()
                    self.statistics.parent = self
                    self._children_name_map["statistics"] = "statistics"
                    self._segment_path = lambda: "statistics"
                    self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/producers-details/producers-detail/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(L2rib.ProducersDetails.ProducersDetail.Statistics, ['producer_id', 'producer_name'], name, value)


                class Statistics_(_Entity_):
                    """
                    Statistics
                    
                    .. attribute:: memory_size
                    
                    	Memory Size
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: object_count
                    
                    	Number of Objects
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: endof_interval_ts
                    
                    	End of Interval Timestamp
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: extended_counter
                    
                    	Extended Counters
                    	**type**\: list of  		 :py:class:`ExtendedCounter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.ProducersDetails.ProducersDetail.Statistics.Statistics_.ExtendedCounter>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'l2rib-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(L2rib.ProducersDetails.ProducersDetail.Statistics.Statistics_, self).__init__()

                        self.yang_name = "statistics"
                        self.yang_parent_name = "statistics"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("extended-counter", ("extended_counter", L2rib.ProducersDetails.ProducersDetail.Statistics.Statistics_.ExtendedCounter))])
                        self._leafs = OrderedDict([
                            ('memory_size', (YLeaf(YType.uint32, 'memory-size'), ['int'])),
                            ('object_count', (YLeaf(YType.uint32, 'object-count'), ['int'])),
                            ('endof_interval_ts', (YLeaf(YType.uint64, 'endof-interval-ts'), ['int'])),
                        ])
                        self.memory_size = None
                        self.object_count = None
                        self.endof_interval_ts = None

                        self.extended_counter = YList(self)
                        self._segment_path = lambda: "statistics"
                        self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/producers-details/producers-detail/statistics/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2rib.ProducersDetails.ProducersDetail.Statistics.Statistics_, ['memory_size', 'object_count', 'endof_interval_ts'], name, value)


                    class ExtendedCounter(_Entity_):
                        """
                        Extended Counters
                        
                        .. attribute:: counter_type
                        
                        	CounterType
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: counter_name
                        
                        	CounterName
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: l2rb_first_event_ts
                        
                        	Real\-clock timestamp in msec of first event
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: l2rb_last_event_ts
                        
                        	Real\-clock timestamp in msec of last event
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: l2rb_interval_event_count
                        
                        	number of events in interval
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: l2rb_total_event_count
                        
                        	total number of events
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'l2rib-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(L2rib.ProducersDetails.ProducersDetail.Statistics.Statistics_.ExtendedCounter, self).__init__()

                            self.yang_name = "extended-counter"
                            self.yang_parent_name = "statistics"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('counter_type', (YLeaf(YType.uint8, 'counter-type'), ['int'])),
                                ('counter_name', (YLeaf(YType.str, 'counter-name'), ['str'])),
                                ('l2rb_first_event_ts', (YLeaf(YType.uint64, 'l2rb-first-event-ts'), ['int'])),
                                ('l2rb_last_event_ts', (YLeaf(YType.uint64, 'l2rb-last-event-ts'), ['int'])),
                                ('l2rb_interval_event_count', (YLeaf(YType.uint32, 'l2rb-interval-event-count'), ['int'])),
                                ('l2rb_total_event_count', (YLeaf(YType.uint32, 'l2rb-total-event-count'), ['int'])),
                            ])
                            self.counter_type = None
                            self.counter_name = None
                            self.l2rb_first_event_ts = None
                            self.l2rb_last_event_ts = None
                            self.l2rb_interval_event_count = None
                            self.l2rb_total_event_count = None
                            self._segment_path = lambda: "extended-counter"
                            self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/producers-details/producers-detail/statistics/statistics/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2rib.ProducersDetails.ProducersDetail.Statistics.Statistics_.ExtendedCounter, ['counter_type', 'counter_name', 'l2rb_first_event_ts', 'l2rb_last_event_ts', 'l2rb_interval_event_count', 'l2rb_total_event_count'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                            return meta._meta_table['L2rib.ProducersDetails.ProducersDetail.Statistics.Statistics_.ExtendedCounter']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                        return meta._meta_table['L2rib.ProducersDetails.ProducersDetail.Statistics.Statistics_']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                    return meta._meta_table['L2rib.ProducersDetails.ProducersDetail.Statistics']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                return meta._meta_table['L2rib.ProducersDetails.ProducersDetail']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
            return meta._meta_table['L2rib.ProducersDetails']['meta_info']


    class Summary(_Entity_):
        """
        L2RIB EVPN Summary
        
        .. attribute:: mac_dd_params
        
        	MAC duplicate detection parameters
        	**type**\:  :py:class:`MacDdParams <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.Summary.MacDdParams>`
        
        	**config**\: False
        
        .. attribute:: ipv4_dd_params
        
        	IPv4 duplicate detection parameters
        	**type**\:  :py:class:`Ipv4DdParams <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.Summary.Ipv4DdParams>`
        
        	**config**\: False
        
        .. attribute:: ipv6_dd_params
        
        	IPv6 duplicate detection parameters
        	**type**\:  :py:class:`Ipv6DdParams <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.Summary.Ipv6DdParams>`
        
        	**config**\: False
        
        .. attribute:: converged_tables_count
        
        	Number of Converged Tables
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: total_memory
        
        	Total Allocated Memory
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: table_summary
        
        	Per Object Table summary
        	**type**\: list of  		 :py:class:`TableSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.Summary.TableSummary>`
        
        	**config**\: False
        
        

        """

        _prefix = 'l2rib-oper'
        _revision = '2015-11-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(L2rib.Summary, self).__init__()

            self.yang_name = "summary"
            self.yang_parent_name = "l2rib"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("mac-dd-params", ("mac_dd_params", L2rib.Summary.MacDdParams)), ("ipv4-dd-params", ("ipv4_dd_params", L2rib.Summary.Ipv4DdParams)), ("ipv6-dd-params", ("ipv6_dd_params", L2rib.Summary.Ipv6DdParams)), ("table-summary", ("table_summary", L2rib.Summary.TableSummary))])
            self._leafs = OrderedDict([
                ('converged_tables_count', (YLeaf(YType.uint32, 'converged-tables-count'), ['int'])),
                ('total_memory', (YLeaf(YType.uint32, 'total-memory'), ['int'])),
            ])
            self.converged_tables_count = None
            self.total_memory = None

            self.mac_dd_params = L2rib.Summary.MacDdParams()
            self.mac_dd_params.parent = self
            self._children_name_map["mac_dd_params"] = "mac-dd-params"

            self.ipv4_dd_params = L2rib.Summary.Ipv4DdParams()
            self.ipv4_dd_params.parent = self
            self._children_name_map["ipv4_dd_params"] = "ipv4-dd-params"

            self.ipv6_dd_params = L2rib.Summary.Ipv6DdParams()
            self.ipv6_dd_params.parent = self
            self._children_name_map["ipv6_dd_params"] = "ipv6-dd-params"

            self.table_summary = YList(self)
            self._segment_path = lambda: "summary"
            self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(L2rib.Summary, ['converged_tables_count', 'total_memory'], name, value)


        class MacDdParams(_Entity_):
            """
            MAC duplicate detection parameters
            
            .. attribute:: dd_params_disable
            
            	Disable duplicate detection for MAC, IPv4 or IPv6 addresses
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: dd_params_freeze_time
            
            	Length of time to freeze the mac after it has been detected as duplicate. Default is 30s
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: dd_params_retry_count
            
            	Number of times to unfreeze a MAC before permanently freezing it. Default is 3 times
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: dd_params_move_count
            
            	Number of moves to occur in move\-interval seconds before freezing the MAC. Default is 5s
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: second
            
            .. attribute:: dd_params_move_interval
            
            	Interval to watch for subsequent moves before freezing the MAC. Default is 180s
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'l2rib-oper'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(L2rib.Summary.MacDdParams, self).__init__()

                self.yang_name = "mac-dd-params"
                self.yang_parent_name = "summary"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('dd_params_disable', (YLeaf(YType.boolean, 'dd-params-disable'), ['bool'])),
                    ('dd_params_freeze_time', (YLeaf(YType.uint16, 'dd-params-freeze-time'), ['int'])),
                    ('dd_params_retry_count', (YLeaf(YType.uint16, 'dd-params-retry-count'), ['int'])),
                    ('dd_params_move_count', (YLeaf(YType.uint32, 'dd-params-move-count'), ['int'])),
                    ('dd_params_move_interval', (YLeaf(YType.uint32, 'dd-params-move-interval'), ['int'])),
                ])
                self.dd_params_disable = None
                self.dd_params_freeze_time = None
                self.dd_params_retry_count = None
                self.dd_params_move_count = None
                self.dd_params_move_interval = None
                self._segment_path = lambda: "mac-dd-params"
                self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/summary/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(L2rib.Summary.MacDdParams, ['dd_params_disable', 'dd_params_freeze_time', 'dd_params_retry_count', 'dd_params_move_count', 'dd_params_move_interval'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                return meta._meta_table['L2rib.Summary.MacDdParams']['meta_info']


        class Ipv4DdParams(_Entity_):
            """
            IPv4 duplicate detection parameters
            
            .. attribute:: dd_params_disable
            
            	Disable duplicate detection for MAC, IPv4 or IPv6 addresses
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: dd_params_freeze_time
            
            	Length of time to freeze the mac after it has been detected as duplicate. Default is 30s
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: dd_params_retry_count
            
            	Number of times to unfreeze a MAC before permanently freezing it. Default is 3 times
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: dd_params_move_count
            
            	Number of moves to occur in move\-interval seconds before freezing the MAC. Default is 5s
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: second
            
            .. attribute:: dd_params_move_interval
            
            	Interval to watch for subsequent moves before freezing the MAC. Default is 180s
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'l2rib-oper'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(L2rib.Summary.Ipv4DdParams, self).__init__()

                self.yang_name = "ipv4-dd-params"
                self.yang_parent_name = "summary"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('dd_params_disable', (YLeaf(YType.boolean, 'dd-params-disable'), ['bool'])),
                    ('dd_params_freeze_time', (YLeaf(YType.uint16, 'dd-params-freeze-time'), ['int'])),
                    ('dd_params_retry_count', (YLeaf(YType.uint16, 'dd-params-retry-count'), ['int'])),
                    ('dd_params_move_count', (YLeaf(YType.uint32, 'dd-params-move-count'), ['int'])),
                    ('dd_params_move_interval', (YLeaf(YType.uint32, 'dd-params-move-interval'), ['int'])),
                ])
                self.dd_params_disable = None
                self.dd_params_freeze_time = None
                self.dd_params_retry_count = None
                self.dd_params_move_count = None
                self.dd_params_move_interval = None
                self._segment_path = lambda: "ipv4-dd-params"
                self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/summary/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(L2rib.Summary.Ipv4DdParams, ['dd_params_disable', 'dd_params_freeze_time', 'dd_params_retry_count', 'dd_params_move_count', 'dd_params_move_interval'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                return meta._meta_table['L2rib.Summary.Ipv4DdParams']['meta_info']


        class Ipv6DdParams(_Entity_):
            """
            IPv6 duplicate detection parameters
            
            .. attribute:: dd_params_disable
            
            	Disable duplicate detection for MAC, IPv4 or IPv6 addresses
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: dd_params_freeze_time
            
            	Length of time to freeze the mac after it has been detected as duplicate. Default is 30s
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: dd_params_retry_count
            
            	Number of times to unfreeze a MAC before permanently freezing it. Default is 3 times
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: dd_params_move_count
            
            	Number of moves to occur in move\-interval seconds before freezing the MAC. Default is 5s
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: second
            
            .. attribute:: dd_params_move_interval
            
            	Interval to watch for subsequent moves before freezing the MAC. Default is 180s
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'l2rib-oper'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(L2rib.Summary.Ipv6DdParams, self).__init__()

                self.yang_name = "ipv6-dd-params"
                self.yang_parent_name = "summary"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('dd_params_disable', (YLeaf(YType.boolean, 'dd-params-disable'), ['bool'])),
                    ('dd_params_freeze_time', (YLeaf(YType.uint16, 'dd-params-freeze-time'), ['int'])),
                    ('dd_params_retry_count', (YLeaf(YType.uint16, 'dd-params-retry-count'), ['int'])),
                    ('dd_params_move_count', (YLeaf(YType.uint32, 'dd-params-move-count'), ['int'])),
                    ('dd_params_move_interval', (YLeaf(YType.uint32, 'dd-params-move-interval'), ['int'])),
                ])
                self.dd_params_disable = None
                self.dd_params_freeze_time = None
                self.dd_params_retry_count = None
                self.dd_params_move_count = None
                self.dd_params_move_interval = None
                self._segment_path = lambda: "ipv6-dd-params"
                self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/summary/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(L2rib.Summary.Ipv6DdParams, ['dd_params_disable', 'dd_params_freeze_time', 'dd_params_retry_count', 'dd_params_move_count', 'dd_params_move_interval'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                return meta._meta_table['L2rib.Summary.Ipv6DdParams']['meta_info']


        class TableSummary(_Entity_):
            """
            Per Object Table summary
            
            .. attribute:: object_type
            
            	Object Type
            	**type**\:  :py:class:`L2ribBagObj <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2ribBagObj>`
            
            	**config**\: False
            
            .. attribute:: object_count
            
            	Number of Objects
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: table_memory
            
            	Allocated Memory
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: producer_stat
            
            	Statistics per producer
            	**type**\: list of  		 :py:class:`ProducerStat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.Summary.TableSummary.ProducerStat>`
            
            	**config**\: False
            
            

            """

            _prefix = 'l2rib-oper'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(L2rib.Summary.TableSummary, self).__init__()

                self.yang_name = "table-summary"
                self.yang_parent_name = "summary"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("producer-stat", ("producer_stat", L2rib.Summary.TableSummary.ProducerStat))])
                self._leafs = OrderedDict([
                    ('object_type', (YLeaf(YType.enumeration, 'object-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper', 'L2ribBagObj', '')])),
                    ('object_count', (YLeaf(YType.uint32, 'object-count'), ['int'])),
                    ('table_memory', (YLeaf(YType.uint32, 'table-memory'), ['int'])),
                ])
                self.object_type = None
                self.object_count = None
                self.table_memory = None

                self.producer_stat = YList(self)
                self._segment_path = lambda: "table-summary"
                self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/summary/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(L2rib.Summary.TableSummary, ['object_type', 'object_count', 'table_memory'], name, value)


            class ProducerStat(_Entity_):
                """
                Statistics per producer
                
                .. attribute:: statistics
                
                	Statistics
                	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.Summary.TableSummary.ProducerStat.Statistics>`
                
                	**config**\: False
                
                .. attribute:: producer_id
                
                	Producer ID
                	**type**\:  :py:class:`L2ribBagProducerId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2ribBagProducerId>`
                
                	**config**\: False
                
                .. attribute:: producer_name
                
                	Producer Name
                	**type**\: str
                
                	**config**\: False
                
                

                """

                _prefix = 'l2rib-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(L2rib.Summary.TableSummary.ProducerStat, self).__init__()

                    self.yang_name = "producer-stat"
                    self.yang_parent_name = "table-summary"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("statistics", ("statistics", L2rib.Summary.TableSummary.ProducerStat.Statistics))])
                    self._leafs = OrderedDict([
                        ('producer_id', (YLeaf(YType.enumeration, 'producer-id'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper', 'L2ribBagProducerId', '')])),
                        ('producer_name', (YLeaf(YType.str, 'producer-name'), ['str'])),
                    ])
                    self.producer_id = None
                    self.producer_name = None

                    self.statistics = L2rib.Summary.TableSummary.ProducerStat.Statistics()
                    self.statistics.parent = self
                    self._children_name_map["statistics"] = "statistics"
                    self._segment_path = lambda: "producer-stat"
                    self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/summary/table-summary/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(L2rib.Summary.TableSummary.ProducerStat, ['producer_id', 'producer_name'], name, value)


                class Statistics(_Entity_):
                    """
                    Statistics
                    
                    .. attribute:: memory_size
                    
                    	Memory Size
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: object_count
                    
                    	Number of Objects
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: endof_interval_ts
                    
                    	End of Interval Timestamp
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: extended_counter
                    
                    	Extended Counters
                    	**type**\: list of  		 :py:class:`ExtendedCounter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.Summary.TableSummary.ProducerStat.Statistics.ExtendedCounter>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'l2rib-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(L2rib.Summary.TableSummary.ProducerStat.Statistics, self).__init__()

                        self.yang_name = "statistics"
                        self.yang_parent_name = "producer-stat"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("extended-counter", ("extended_counter", L2rib.Summary.TableSummary.ProducerStat.Statistics.ExtendedCounter))])
                        self._leafs = OrderedDict([
                            ('memory_size', (YLeaf(YType.uint32, 'memory-size'), ['int'])),
                            ('object_count', (YLeaf(YType.uint32, 'object-count'), ['int'])),
                            ('endof_interval_ts', (YLeaf(YType.uint64, 'endof-interval-ts'), ['int'])),
                        ])
                        self.memory_size = None
                        self.object_count = None
                        self.endof_interval_ts = None

                        self.extended_counter = YList(self)
                        self._segment_path = lambda: "statistics"
                        self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/summary/table-summary/producer-stat/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2rib.Summary.TableSummary.ProducerStat.Statistics, ['memory_size', 'object_count', 'endof_interval_ts'], name, value)


                    class ExtendedCounter(_Entity_):
                        """
                        Extended Counters
                        
                        .. attribute:: counter_type
                        
                        	CounterType
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: counter_name
                        
                        	CounterName
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: l2rb_first_event_ts
                        
                        	Real\-clock timestamp in msec of first event
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: l2rb_last_event_ts
                        
                        	Real\-clock timestamp in msec of last event
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: l2rb_interval_event_count
                        
                        	number of events in interval
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: l2rb_total_event_count
                        
                        	total number of events
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'l2rib-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(L2rib.Summary.TableSummary.ProducerStat.Statistics.ExtendedCounter, self).__init__()

                            self.yang_name = "extended-counter"
                            self.yang_parent_name = "statistics"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('counter_type', (YLeaf(YType.uint8, 'counter-type'), ['int'])),
                                ('counter_name', (YLeaf(YType.str, 'counter-name'), ['str'])),
                                ('l2rb_first_event_ts', (YLeaf(YType.uint64, 'l2rb-first-event-ts'), ['int'])),
                                ('l2rb_last_event_ts', (YLeaf(YType.uint64, 'l2rb-last-event-ts'), ['int'])),
                                ('l2rb_interval_event_count', (YLeaf(YType.uint32, 'l2rb-interval-event-count'), ['int'])),
                                ('l2rb_total_event_count', (YLeaf(YType.uint32, 'l2rb-total-event-count'), ['int'])),
                            ])
                            self.counter_type = None
                            self.counter_name = None
                            self.l2rb_first_event_ts = None
                            self.l2rb_last_event_ts = None
                            self.l2rb_interval_event_count = None
                            self.l2rb_total_event_count = None
                            self._segment_path = lambda: "extended-counter"
                            self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/summary/table-summary/producer-stat/statistics/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2rib.Summary.TableSummary.ProducerStat.Statistics.ExtendedCounter, ['counter_type', 'counter_name', 'l2rb_first_event_ts', 'l2rb_last_event_ts', 'l2rb_interval_event_count', 'l2rb_total_event_count'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                            return meta._meta_table['L2rib.Summary.TableSummary.ProducerStat.Statistics.ExtendedCounter']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                        return meta._meta_table['L2rib.Summary.TableSummary.ProducerStat.Statistics']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                    return meta._meta_table['L2rib.Summary.TableSummary.ProducerStat']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                return meta._meta_table['L2rib.Summary.TableSummary']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
            return meta._meta_table['L2rib.Summary']['meta_info']


    class Producers(_Entity_):
        """
        L2RIB producer table
        
        .. attribute:: producer
        
        	L2RIB producers
        	**type**\: list of  		 :py:class:`Producer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.Producers.Producer>`
        
        	**config**\: False
        
        

        """

        _prefix = 'l2rib-oper'
        _revision = '2015-11-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(L2rib.Producers, self).__init__()

            self.yang_name = "producers"
            self.yang_parent_name = "l2rib"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("producer", ("producer", L2rib.Producers.Producer))])
            self._leafs = OrderedDict()

            self.producer = YList(self)
            self._segment_path = lambda: "producers"
            self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(L2rib.Producers, [], name, value)


        class Producer(_Entity_):
            """
            L2RIB producers
            
            .. attribute:: object_id
            
            	Object ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: product_id
            
            	Product ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: client_id
            
            	Client ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: object_type
            
            	Object Type
            	**type**\:  :py:class:`L2ribBagObj <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2ribBagObj>`
            
            	**config**\: False
            
            .. attribute:: producer_id
            
            	Producer ID
            	**type**\:  :py:class:`L2ribBagProducerId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2ribBagProducerId>`
            
            	**config**\: False
            
            .. attribute:: producer_name
            
            	Producer Name
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: admin_distance
            
            	Admin Distance
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: purge_time
            
            	Purge Time
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: state
            
            	Producer State
            	**type**\:  :py:class:`L2ribBagProducerState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2ribBagProducerState>`
            
            	**config**\: False
            
            

            """

            _prefix = 'l2rib-oper'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(L2rib.Producers.Producer, self).__init__()

                self.yang_name = "producer"
                self.yang_parent_name = "producers"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('object_id', (YLeaf(YType.uint32, 'object-id'), ['int'])),
                    ('product_id', (YLeaf(YType.uint32, 'product-id'), ['int'])),
                    ('client_id', (YLeaf(YType.uint32, 'client-id'), ['int'])),
                    ('object_type', (YLeaf(YType.enumeration, 'object-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper', 'L2ribBagObj', '')])),
                    ('producer_id', (YLeaf(YType.enumeration, 'producer-id'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper', 'L2ribBagProducerId', '')])),
                    ('producer_name', (YLeaf(YType.str, 'producer-name'), ['str'])),
                    ('admin_distance', (YLeaf(YType.uint32, 'admin-distance'), ['int'])),
                    ('purge_time', (YLeaf(YType.uint32, 'purge-time'), ['int'])),
                    ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper', 'L2ribBagProducerState', '')])),
                ])
                self.object_id = None
                self.product_id = None
                self.client_id = None
                self.object_type = None
                self.producer_id = None
                self.producer_name = None
                self.admin_distance = None
                self.purge_time = None
                self.state = None
                self._segment_path = lambda: "producer"
                self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/producers/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(L2rib.Producers.Producer, ['object_id', 'product_id', 'client_id', 'object_type', 'producer_id', 'producer_name', 'admin_distance', 'purge_time', 'state'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                return meta._meta_table['L2rib.Producers.Producer']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
            return meta._meta_table['L2rib.Producers']['meta_info']


    class Clients(_Entity_):
        """
        L2RIB client table
        
        .. attribute:: client
        
        	L2RIB clients
        	**type**\: list of  		 :py:class:`Client <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.Clients.Client>`
        
        	**config**\: False
        
        

        """

        _prefix = 'l2rib-oper'
        _revision = '2015-11-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(L2rib.Clients, self).__init__()

            self.yang_name = "clients"
            self.yang_parent_name = "l2rib"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("client", ("client", L2rib.Clients.Client))])
            self._leafs = OrderedDict()

            self.client = YList(self)
            self._segment_path = lambda: "clients"
            self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(L2rib.Clients, [], name, value)


        class Client(_Entity_):
            """
            L2RIB clients
            
            .. attribute:: client_id  (key)
            
            	Client ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: client_id_xr
            
            	Client ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: process_id
            
            	Process ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: node_id
            
            	Node ID
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            	**config**\: False
            
            .. attribute:: proc_name
            
            	Process Name
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: proc_suffix
            
            	Process Suffix
            	**type**\: str
            
            	**config**\: False
            
            

            """

            _prefix = 'l2rib-oper'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(L2rib.Clients.Client, self).__init__()

                self.yang_name = "client"
                self.yang_parent_name = "clients"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['client_id']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('client_id', (YLeaf(YType.uint32, 'client-id'), ['int'])),
                    ('client_id_xr', (YLeaf(YType.uint32, 'client-id-xr'), ['int'])),
                    ('process_id', (YLeaf(YType.uint32, 'process-id'), ['int'])),
                    ('node_id', (YLeaf(YType.str, 'node-id'), ['str'])),
                    ('proc_name', (YLeaf(YType.str, 'proc-name'), ['str'])),
                    ('proc_suffix', (YLeaf(YType.str, 'proc-suffix'), ['str'])),
                ])
                self.client_id = None
                self.client_id_xr = None
                self.process_id = None
                self.node_id = None
                self.proc_name = None
                self.proc_suffix = None
                self._segment_path = lambda: "client" + "[client-id='" + str(self.client_id) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/clients/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(L2rib.Clients.Client, ['client_id', 'client_id_xr', 'process_id', 'node_id', 'proc_name', 'proc_suffix'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                return meta._meta_table['L2rib.Clients.Client']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
            return meta._meta_table['L2rib.Clients']['meta_info']


    class EvisXr(_Entity_):
        """
        L2RIB EVPN EVI Detail Table
        
        .. attribute:: evi
        
        	L2RIB EVPN EVI Entry
        	**type**\: list of  		 :py:class:`Evi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EvisXr.Evi>`
        
        	**config**\: False
        
        

        """

        _prefix = 'l2rib-oper'
        _revision = '2015-11-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(L2rib.EvisXr, self).__init__()

            self.yang_name = "evis-xr"
            self.yang_parent_name = "l2rib"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("evi", ("evi", L2rib.EvisXr.Evi))])
            self._leafs = OrderedDict()

            self.evi = YList(self)
            self._segment_path = lambda: "evis-xr"
            self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(L2rib.EvisXr, [], name, value)


        class Evi(_Entity_):
            """
            L2RIB EVPN EVI Entry
            
            .. attribute:: evi  (key)
            
            	EVI ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: topology
            
            	Topology
            	**type**\:  :py:class:`Topology <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EvisXr.Evi.Topology>`
            
            	**config**\: False
            
            .. attribute:: l2r_vni
            
            	l2r vni
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: l2r_encap_type
            
            	l2r encap type
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: l2r_nve_iod
            
            	l2r nve iod
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: l2r_nve_ifhandle
            
            	l2r nve ifhandle
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: vtep_ip
            
            	VTEP IP
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: l2r_topo_txid
            
            	l2r topo txid
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: l2r_topo_flags
            
            	Topology Flags
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'l2rib-oper'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(L2rib.EvisXr.Evi, self).__init__()

                self.yang_name = "evi"
                self.yang_parent_name = "evis-xr"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['evi']
                self._child_classes = OrderedDict([("topology", ("topology", L2rib.EvisXr.Evi.Topology))])
                self._leafs = OrderedDict([
                    ('evi', (YLeaf(YType.uint32, 'evi'), ['int'])),
                    ('l2r_vni', (YLeaf(YType.uint32, 'l2r-vni'), ['int'])),
                    ('l2r_encap_type', (YLeaf(YType.uint16, 'l2r-encap-type'), ['int'])),
                    ('l2r_nve_iod', (YLeaf(YType.uint32, 'l2r-nve-iod'), ['int'])),
                    ('l2r_nve_ifhandle', (YLeaf(YType.uint32, 'l2r-nve-ifhandle'), ['int'])),
                    ('vtep_ip', (YLeaf(YType.str, 'vtep-ip'), ['str'])),
                    ('l2r_topo_txid', (YLeaf(YType.uint32, 'l2r-topo-txid'), ['int'])),
                    ('l2r_topo_flags', (YLeaf(YType.uint32, 'l2r-topo-flags'), ['int'])),
                ])
                self.evi = None
                self.l2r_vni = None
                self.l2r_encap_type = None
                self.l2r_nve_iod = None
                self.l2r_nve_ifhandle = None
                self.vtep_ip = None
                self.l2r_topo_txid = None
                self.l2r_topo_flags = None

                self.topology = L2rib.EvisXr.Evi.Topology()
                self.topology.parent = self
                self._children_name_map["topology"] = "topology"
                self._segment_path = lambda: "evi" + "[evi='" + str(self.evi) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evis-xr/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(L2rib.EvisXr.Evi, ['evi', 'l2r_vni', 'l2r_encap_type', 'l2r_nve_iod', 'l2r_nve_ifhandle', 'vtep_ip', 'l2r_topo_txid', 'l2r_topo_flags'], name, value)


            class Topology(_Entity_):
                """
                Topology
                
                .. attribute:: topology_id
                
                	Topology ID
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: topology_name
                
                	Topology Name
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: topology_type
                
                	Topology Type
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                

                """

                _prefix = 'l2rib-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(L2rib.EvisXr.Evi.Topology, self).__init__()

                    self.yang_name = "topology"
                    self.yang_parent_name = "evi"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('topology_id', (YLeaf(YType.uint32, 'topology-id'), ['int'])),
                        ('topology_name', (YLeaf(YType.str, 'topology-name'), ['str'])),
                        ('topology_type', (YLeaf(YType.uint32, 'topology-type'), ['int'])),
                    ])
                    self.topology_id = None
                    self.topology_name = None
                    self.topology_type = None
                    self._segment_path = lambda: "topology"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(L2rib.EvisXr.Evi.Topology, ['topology_id', 'topology_name', 'topology_type'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                    return meta._meta_table['L2rib.EvisXr.Evi.Topology']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                return meta._meta_table['L2rib.EvisXr.Evi']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
            return meta._meta_table['L2rib.EvisXr']['meta_info']


    class ClientsDetails(_Entity_):
        """
        L2RIB detailed client table
        
        .. attribute:: clients_detail
        
        	L2RIB clients detail information
        	**type**\: list of  		 :py:class:`ClientsDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.ClientsDetails.ClientsDetail>`
        
        	**config**\: False
        
        

        """

        _prefix = 'l2rib-oper'
        _revision = '2015-11-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(L2rib.ClientsDetails, self).__init__()

            self.yang_name = "clients-details"
            self.yang_parent_name = "l2rib"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("clients-detail", ("clients_detail", L2rib.ClientsDetails.ClientsDetail))])
            self._leafs = OrderedDict()

            self.clients_detail = YList(self)
            self._segment_path = lambda: "clients-details"
            self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(L2rib.ClientsDetails, [], name, value)


        class ClientsDetail(_Entity_):
            """
            L2RIB clients detail information
            
            .. attribute:: client_id  (key)
            
            	Client ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: client
            
            	Non\-detail Client bag
            	**type**\:  :py:class:`Client <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.ClientsDetails.ClientsDetail.Client>`
            
            	**config**\: False
            
            .. attribute:: registration_table_statistics
            
            	Registration table statistics
            	**type**\:  :py:class:`RegistrationTableStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.ClientsDetails.ClientsDetail.RegistrationTableStatistics>`
            
            	**config**\: False
            
            .. attribute:: producer_count
            
            	Number of Producers
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: last_update_timestamp
            
            	Last Update Timestamp
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            .. attribute:: producer_array
            
            	List of Producers
            	**type**\: list of  		 :py:class:`ProducerArray <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.ClientsDetails.ClientsDetail.ProducerArray>`
            
            	**config**\: False
            
            

            """

            _prefix = 'l2rib-oper'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(L2rib.ClientsDetails.ClientsDetail, self).__init__()

                self.yang_name = "clients-detail"
                self.yang_parent_name = "clients-details"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['client_id']
                self._child_classes = OrderedDict([("client", ("client", L2rib.ClientsDetails.ClientsDetail.Client)), ("registration-table-statistics", ("registration_table_statistics", L2rib.ClientsDetails.ClientsDetail.RegistrationTableStatistics)), ("producer-array", ("producer_array", L2rib.ClientsDetails.ClientsDetail.ProducerArray))])
                self._leafs = OrderedDict([
                    ('client_id', (YLeaf(YType.uint32, 'client-id'), ['int'])),
                    ('producer_count', (YLeaf(YType.uint8, 'producer-count'), ['int'])),
                    ('last_update_timestamp', (YLeaf(YType.uint64, 'last-update-timestamp'), ['int'])),
                ])
                self.client_id = None
                self.producer_count = None
                self.last_update_timestamp = None

                self.client = L2rib.ClientsDetails.ClientsDetail.Client()
                self.client.parent = self
                self._children_name_map["client"] = "client"

                self.registration_table_statistics = L2rib.ClientsDetails.ClientsDetail.RegistrationTableStatistics()
                self.registration_table_statistics.parent = self
                self._children_name_map["registration_table_statistics"] = "registration-table-statistics"

                self.producer_array = YList(self)
                self._segment_path = lambda: "clients-detail" + "[client-id='" + str(self.client_id) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/clients-details/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(L2rib.ClientsDetails.ClientsDetail, ['client_id', 'producer_count', 'last_update_timestamp'], name, value)


            class Client(_Entity_):
                """
                Non\-detail Client bag
                
                .. attribute:: client_id_xr
                
                	Client ID
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: process_id
                
                	Process ID
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: node_id
                
                	Node ID
                	**type**\: str
                
                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                
                	**config**\: False
                
                .. attribute:: proc_name
                
                	Process Name
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: proc_suffix
                
                	Process Suffix
                	**type**\: str
                
                	**config**\: False
                
                

                """

                _prefix = 'l2rib-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(L2rib.ClientsDetails.ClientsDetail.Client, self).__init__()

                    self.yang_name = "client"
                    self.yang_parent_name = "clients-detail"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('client_id_xr', (YLeaf(YType.uint32, 'client-id-xr'), ['int'])),
                        ('process_id', (YLeaf(YType.uint32, 'process-id'), ['int'])),
                        ('node_id', (YLeaf(YType.str, 'node-id'), ['str'])),
                        ('proc_name', (YLeaf(YType.str, 'proc-name'), ['str'])),
                        ('proc_suffix', (YLeaf(YType.str, 'proc-suffix'), ['str'])),
                    ])
                    self.client_id_xr = None
                    self.process_id = None
                    self.node_id = None
                    self.proc_name = None
                    self.proc_suffix = None
                    self._segment_path = lambda: "client"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(L2rib.ClientsDetails.ClientsDetail.Client, ['client_id_xr', 'process_id', 'node_id', 'proc_name', 'proc_suffix'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                    return meta._meta_table['L2rib.ClientsDetails.ClientsDetail.Client']['meta_info']


            class RegistrationTableStatistics(_Entity_):
                """
                Registration table statistics
                
                .. attribute:: statistics
                
                	Statistics
                	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.ClientsDetails.ClientsDetail.RegistrationTableStatistics.Statistics>`
                
                	**config**\: False
                
                .. attribute:: producer_id
                
                	Producer ID
                	**type**\:  :py:class:`L2ribBagProducerId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2ribBagProducerId>`
                
                	**config**\: False
                
                .. attribute:: producer_name
                
                	Producer Name
                	**type**\: str
                
                	**config**\: False
                
                

                """

                _prefix = 'l2rib-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(L2rib.ClientsDetails.ClientsDetail.RegistrationTableStatistics, self).__init__()

                    self.yang_name = "registration-table-statistics"
                    self.yang_parent_name = "clients-detail"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("statistics", ("statistics", L2rib.ClientsDetails.ClientsDetail.RegistrationTableStatistics.Statistics))])
                    self._leafs = OrderedDict([
                        ('producer_id', (YLeaf(YType.enumeration, 'producer-id'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper', 'L2ribBagProducerId', '')])),
                        ('producer_name', (YLeaf(YType.str, 'producer-name'), ['str'])),
                    ])
                    self.producer_id = None
                    self.producer_name = None

                    self.statistics = L2rib.ClientsDetails.ClientsDetail.RegistrationTableStatistics.Statistics()
                    self.statistics.parent = self
                    self._children_name_map["statistics"] = "statistics"
                    self._segment_path = lambda: "registration-table-statistics"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(L2rib.ClientsDetails.ClientsDetail.RegistrationTableStatistics, ['producer_id', 'producer_name'], name, value)


                class Statistics(_Entity_):
                    """
                    Statistics
                    
                    .. attribute:: memory_size
                    
                    	Memory Size
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: object_count
                    
                    	Number of Objects
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: endof_interval_ts
                    
                    	End of Interval Timestamp
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: extended_counter
                    
                    	Extended Counters
                    	**type**\: list of  		 :py:class:`ExtendedCounter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.ClientsDetails.ClientsDetail.RegistrationTableStatistics.Statistics.ExtendedCounter>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'l2rib-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(L2rib.ClientsDetails.ClientsDetail.RegistrationTableStatistics.Statistics, self).__init__()

                        self.yang_name = "statistics"
                        self.yang_parent_name = "registration-table-statistics"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("extended-counter", ("extended_counter", L2rib.ClientsDetails.ClientsDetail.RegistrationTableStatistics.Statistics.ExtendedCounter))])
                        self._leafs = OrderedDict([
                            ('memory_size', (YLeaf(YType.uint32, 'memory-size'), ['int'])),
                            ('object_count', (YLeaf(YType.uint32, 'object-count'), ['int'])),
                            ('endof_interval_ts', (YLeaf(YType.uint64, 'endof-interval-ts'), ['int'])),
                        ])
                        self.memory_size = None
                        self.object_count = None
                        self.endof_interval_ts = None

                        self.extended_counter = YList(self)
                        self._segment_path = lambda: "statistics"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2rib.ClientsDetails.ClientsDetail.RegistrationTableStatistics.Statistics, ['memory_size', 'object_count', 'endof_interval_ts'], name, value)


                    class ExtendedCounter(_Entity_):
                        """
                        Extended Counters
                        
                        .. attribute:: counter_type
                        
                        	CounterType
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: counter_name
                        
                        	CounterName
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: l2rb_first_event_ts
                        
                        	Real\-clock timestamp in msec of first event
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: l2rb_last_event_ts
                        
                        	Real\-clock timestamp in msec of last event
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: l2rb_interval_event_count
                        
                        	number of events in interval
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: l2rb_total_event_count
                        
                        	total number of events
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'l2rib-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(L2rib.ClientsDetails.ClientsDetail.RegistrationTableStatistics.Statistics.ExtendedCounter, self).__init__()

                            self.yang_name = "extended-counter"
                            self.yang_parent_name = "statistics"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('counter_type', (YLeaf(YType.uint8, 'counter-type'), ['int'])),
                                ('counter_name', (YLeaf(YType.str, 'counter-name'), ['str'])),
                                ('l2rb_first_event_ts', (YLeaf(YType.uint64, 'l2rb-first-event-ts'), ['int'])),
                                ('l2rb_last_event_ts', (YLeaf(YType.uint64, 'l2rb-last-event-ts'), ['int'])),
                                ('l2rb_interval_event_count', (YLeaf(YType.uint32, 'l2rb-interval-event-count'), ['int'])),
                                ('l2rb_total_event_count', (YLeaf(YType.uint32, 'l2rb-total-event-count'), ['int'])),
                            ])
                            self.counter_type = None
                            self.counter_name = None
                            self.l2rb_first_event_ts = None
                            self.l2rb_last_event_ts = None
                            self.l2rb_interval_event_count = None
                            self.l2rb_total_event_count = None
                            self._segment_path = lambda: "extended-counter"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2rib.ClientsDetails.ClientsDetail.RegistrationTableStatistics.Statistics.ExtendedCounter, ['counter_type', 'counter_name', 'l2rb_first_event_ts', 'l2rb_last_event_ts', 'l2rb_interval_event_count', 'l2rb_total_event_count'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                            return meta._meta_table['L2rib.ClientsDetails.ClientsDetail.RegistrationTableStatistics.Statistics.ExtendedCounter']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                        return meta._meta_table['L2rib.ClientsDetails.ClientsDetail.RegistrationTableStatistics.Statistics']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                    return meta._meta_table['L2rib.ClientsDetails.ClientsDetail.RegistrationTableStatistics']['meta_info']


            class ProducerArray(_Entity_):
                """
                List of Producers
                
                .. attribute:: object_type
                
                	Object Type
                	**type**\:  :py:class:`L2ribBagObj <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2ribBagObj>`
                
                	**config**\: False
                
                .. attribute:: producer_id
                
                	Producer ID
                	**type**\:  :py:class:`L2ribBagProducerId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2ribBagProducerId>`
                
                	**config**\: False
                
                .. attribute:: producer_name
                
                	Producer Name
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: admin_distance
                
                	Admin Distance
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: purge_time
                
                	Purge Time
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                

                """

                _prefix = 'l2rib-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(L2rib.ClientsDetails.ClientsDetail.ProducerArray, self).__init__()

                    self.yang_name = "producer-array"
                    self.yang_parent_name = "clients-detail"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('object_type', (YLeaf(YType.enumeration, 'object-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper', 'L2ribBagObj', '')])),
                        ('producer_id', (YLeaf(YType.enumeration, 'producer-id'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper', 'L2ribBagProducerId', '')])),
                        ('producer_name', (YLeaf(YType.str, 'producer-name'), ['str'])),
                        ('admin_distance', (YLeaf(YType.uint32, 'admin-distance'), ['int'])),
                        ('purge_time', (YLeaf(YType.uint32, 'purge-time'), ['int'])),
                    ])
                    self.object_type = None
                    self.producer_id = None
                    self.producer_name = None
                    self.admin_distance = None
                    self.purge_time = None
                    self._segment_path = lambda: "producer-array"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(L2rib.ClientsDetails.ClientsDetail.ProducerArray, ['object_type', 'producer_id', 'producer_name', 'admin_distance', 'purge_time'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                    return meta._meta_table['L2rib.ClientsDetails.ClientsDetail.ProducerArray']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                return meta._meta_table['L2rib.ClientsDetails.ClientsDetail']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
            return meta._meta_table['L2rib.ClientsDetails']['meta_info']


    class EviChildTables(_Entity_):
        """
        Container for all EVI Child Tables
        
        .. attribute:: macip_details
        
        	L2RIB EVPN EVI MAC IP Detail table
        	**type**\:  :py:class:`MacipDetails <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.MacipDetails>`
        
        	**config**\: False
        
        .. attribute:: mac_ips
        
        	L2RIB EVPN EVI MAC IP table
        	**type**\:  :py:class:`MacIps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.MacIps>`
        
        	**config**\: False
        
        .. attribute:: macs
        
        	L2RIB EVPN EVI MAC table
        	**type**\:  :py:class:`Macs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.Macs>`
        
        	**config**\: False
        
        .. attribute:: imets
        
        	L2RIB EVPN EVI IMET table
        	**type**\:  :py:class:`Imets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.Imets>`
        
        	**config**\: False
        
        .. attribute:: mac_details
        
        	L2RIB EVPN EVI MAC Detail table
        	**type**\:  :py:class:`MacDetails <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.MacDetails>`
        
        	**config**\: False
        
        .. attribute:: imet_details
        
        	L2RIB EVPN EVI IMET Detail table
        	**type**\:  :py:class:`ImetDetails <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.ImetDetails>`
        
        	**config**\: False
        
        

        """

        _prefix = 'l2rib-oper'
        _revision = '2015-11-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(L2rib.EviChildTables, self).__init__()

            self.yang_name = "evi-child-tables"
            self.yang_parent_name = "l2rib"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("macip-details", ("macip_details", L2rib.EviChildTables.MacipDetails)), ("mac-ips", ("mac_ips", L2rib.EviChildTables.MacIps)), ("macs", ("macs", L2rib.EviChildTables.Macs)), ("imets", ("imets", L2rib.EviChildTables.Imets)), ("mac-details", ("mac_details", L2rib.EviChildTables.MacDetails)), ("imet-details", ("imet_details", L2rib.EviChildTables.ImetDetails))])
            self._leafs = OrderedDict()

            self.macip_details = L2rib.EviChildTables.MacipDetails()
            self.macip_details.parent = self
            self._children_name_map["macip_details"] = "macip-details"

            self.mac_ips = L2rib.EviChildTables.MacIps()
            self.mac_ips.parent = self
            self._children_name_map["mac_ips"] = "mac-ips"

            self.macs = L2rib.EviChildTables.Macs()
            self.macs.parent = self
            self._children_name_map["macs"] = "macs"

            self.imets = L2rib.EviChildTables.Imets()
            self.imets.parent = self
            self._children_name_map["imets"] = "imets"

            self.mac_details = L2rib.EviChildTables.MacDetails()
            self.mac_details.parent = self
            self._children_name_map["mac_details"] = "mac-details"

            self.imet_details = L2rib.EviChildTables.ImetDetails()
            self.imet_details.parent = self
            self._children_name_map["imet_details"] = "imet-details"
            self._segment_path = lambda: "evi-child-tables"
            self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(L2rib.EviChildTables, [], name, value)


        class MacipDetails(_Entity_):
            """
            L2RIB EVPN EVI MAC IP Detail table
            
            .. attribute:: macip_detail
            
            	L2RIB EVPN MAC IP Detail table
            	**type**\: list of  		 :py:class:`MacipDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.MacipDetails.MacipDetail>`
            
            	**config**\: False
            
            

            """

            _prefix = 'l2rib-oper'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(L2rib.EviChildTables.MacipDetails, self).__init__()

                self.yang_name = "macip-details"
                self.yang_parent_name = "evi-child-tables"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("macip-detail", ("macip_detail", L2rib.EviChildTables.MacipDetails.MacipDetail))])
                self._leafs = OrderedDict()

                self.macip_detail = YList(self)
                self._segment_path = lambda: "macip-details"
                self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(L2rib.EviChildTables.MacipDetails, [], name, value)


            class MacipDetail(_Entity_):
                """
                L2RIB EVPN MAC IP Detail table
                
                .. attribute:: evi
                
                	EVPN ID
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: mac_addr
                
                	MAC IP Address
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                	**config**\: False
                
                .. attribute:: ip_addr
                
                	IP Address
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                	**config**\: False
                
                .. attribute:: prod_id
                
                	Producer ID
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: mac_ip_route
                
                	MAC\-IP Route
                	**type**\:  :py:class:`MacIpRoute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.MacipDetails.MacipDetail.MacIpRoute>`
                
                	**config**\: False
                
                .. attribute:: rt_tlv
                
                	Mac\-IP Route Opaque Data TLV
                	**type**\:  :py:class:`RtTlv <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.MacipDetails.MacipDetail.RtTlv>`
                
                	**config**\: False
                
                .. attribute:: nh_tlv
                
                	Mac\-IP Route Opaque NH TLV
                	**type**\:  :py:class:`NhTlv <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.MacipDetails.MacipDetail.NhTlv>`
                
                	**config**\: False
                
                .. attribute:: sequence_number
                
                	MAC\-IP route sequence Number
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: flags
                
                	MAC\-IP route flags
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{1,8}
                
                	**config**\: False
                
                .. attribute:: soo
                
                	SOO
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: last_update_timestamp
                
                	Last Update Timestamp
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                

                """

                _prefix = 'l2rib-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(L2rib.EviChildTables.MacipDetails.MacipDetail, self).__init__()

                    self.yang_name = "macip-detail"
                    self.yang_parent_name = "macip-details"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("mac-ip-route", ("mac_ip_route", L2rib.EviChildTables.MacipDetails.MacipDetail.MacIpRoute)), ("rt-tlv", ("rt_tlv", L2rib.EviChildTables.MacipDetails.MacipDetail.RtTlv)), ("nh-tlv", ("nh_tlv", L2rib.EviChildTables.MacipDetails.MacipDetail.NhTlv))])
                    self._leafs = OrderedDict([
                        ('evi', (YLeaf(YType.uint32, 'evi'), ['int'])),
                        ('mac_addr', (YLeaf(YType.str, 'mac-addr'), ['str'])),
                        ('ip_addr', (YLeaf(YType.str, 'ip-addr'), ['str','str'])),
                        ('prod_id', (YLeaf(YType.uint32, 'prod-id'), ['int'])),
                        ('sequence_number', (YLeaf(YType.uint32, 'sequence-number'), ['int'])),
                        ('flags', (YLeaf(YType.str, 'flags'), ['str'])),
                        ('soo', (YLeaf(YType.uint32, 'soo'), ['int'])),
                        ('last_update_timestamp', (YLeaf(YType.uint64, 'last-update-timestamp'), ['int'])),
                    ])
                    self.evi = None
                    self.mac_addr = None
                    self.ip_addr = None
                    self.prod_id = None
                    self.sequence_number = None
                    self.flags = None
                    self.soo = None
                    self.last_update_timestamp = None

                    self.mac_ip_route = L2rib.EviChildTables.MacipDetails.MacipDetail.MacIpRoute()
                    self.mac_ip_route.parent = self
                    self._children_name_map["mac_ip_route"] = "mac-ip-route"

                    self.rt_tlv = L2rib.EviChildTables.MacipDetails.MacipDetail.RtTlv()
                    self.rt_tlv.parent = self
                    self._children_name_map["rt_tlv"] = "rt-tlv"

                    self.nh_tlv = L2rib.EviChildTables.MacipDetails.MacipDetail.NhTlv()
                    self.nh_tlv.parent = self
                    self._children_name_map["nh_tlv"] = "nh-tlv"
                    self._segment_path = lambda: "macip-detail"
                    self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/macip-details/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(L2rib.EviChildTables.MacipDetails.MacipDetail, ['evi', 'mac_addr', 'ip_addr', 'prod_id', 'sequence_number', 'flags', 'soo', 'last_update_timestamp'], name, value)


                class MacIpRoute(_Entity_):
                    """
                    MAC\-IP Route
                    
                    .. attribute:: next_hop
                    
                    	Next Hop
                    	**type**\:  :py:class:`NextHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.MacipDetails.MacipDetail.MacIpRoute.NextHop>`
                    
                    	**config**\: False
                    
                    .. attribute:: backup_next_hop
                    
                    	Secondary Next Hop
                    	**type**\:  :py:class:`BackupNextHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.MacipDetails.MacipDetail.MacIpRoute.BackupNextHop>`
                    
                    	**config**\: False
                    
                    .. attribute:: mac_address
                    
                    	MAC Address
                    	**type**\: str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    	**config**\: False
                    
                    .. attribute:: ip_address
                    
                    	IP Address
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: admin_distance
                    
                    	Admin Distance
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: producer_id
                    
                    	Producer ID
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: topology_id
                    
                    	Topology ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'l2rib-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(L2rib.EviChildTables.MacipDetails.MacipDetail.MacIpRoute, self).__init__()

                        self.yang_name = "mac-ip-route"
                        self.yang_parent_name = "macip-detail"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("next-hop", ("next_hop", L2rib.EviChildTables.MacipDetails.MacipDetail.MacIpRoute.NextHop)), ("backup-next-hop", ("backup_next_hop", L2rib.EviChildTables.MacipDetails.MacipDetail.MacIpRoute.BackupNextHop))])
                        self._leafs = OrderedDict([
                            ('mac_address', (YLeaf(YType.str, 'mac-address'), ['str'])),
                            ('ip_address', (YLeaf(YType.str, 'ip-address'), ['str'])),
                            ('admin_distance', (YLeaf(YType.uint8, 'admin-distance'), ['int'])),
                            ('producer_id', (YLeaf(YType.uint8, 'producer-id'), ['int'])),
                            ('topology_id', (YLeaf(YType.uint32, 'topology-id'), ['int'])),
                        ])
                        self.mac_address = None
                        self.ip_address = None
                        self.admin_distance = None
                        self.producer_id = None
                        self.topology_id = None

                        self.next_hop = L2rib.EviChildTables.MacipDetails.MacipDetail.MacIpRoute.NextHop()
                        self.next_hop.parent = self
                        self._children_name_map["next_hop"] = "next-hop"

                        self.backup_next_hop = L2rib.EviChildTables.MacipDetails.MacipDetail.MacIpRoute.BackupNextHop()
                        self.backup_next_hop.parent = self
                        self._children_name_map["backup_next_hop"] = "backup-next-hop"
                        self._segment_path = lambda: "mac-ip-route"
                        self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/macip-details/macip-detail/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2rib.EviChildTables.MacipDetails.MacipDetail.MacIpRoute, ['mac_address', 'ip_address', 'admin_distance', 'producer_id', 'topology_id'], name, value)


                    class NextHop(_Entity_):
                        """
                        Next Hop
                        
                        .. attribute:: next_hop
                        
                        	Next hop
                        	**type**\:  :py:class:`NextHop_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.MacipDetails.MacipDetail.MacIpRoute.NextHop.NextHop_>`
                        
                        	**config**\: False
                        
                        .. attribute:: topology_id
                        
                        	Next\-hop TOPOLOGY ID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: flags
                        
                        	Next\-hop flags
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'l2rib-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(L2rib.EviChildTables.MacipDetails.MacipDetail.MacIpRoute.NextHop, self).__init__()

                            self.yang_name = "next-hop"
                            self.yang_parent_name = "mac-ip-route"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("next-hop", ("next_hop", L2rib.EviChildTables.MacipDetails.MacipDetail.MacIpRoute.NextHop.NextHop_))])
                            self._leafs = OrderedDict([
                                ('topology_id', (YLeaf(YType.uint32, 'topology-id'), ['int'])),
                                ('flags', (YLeaf(YType.uint16, 'flags'), ['int'])),
                            ])
                            self.topology_id = None
                            self.flags = None

                            self.next_hop = L2rib.EviChildTables.MacipDetails.MacipDetail.MacIpRoute.NextHop.NextHop_()
                            self.next_hop.parent = self
                            self._children_name_map["next_hop"] = "next-hop"
                            self._segment_path = lambda: "next-hop"
                            self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/macip-details/macip-detail/mac-ip-route/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2rib.EviChildTables.MacipDetails.MacipDetail.MacIpRoute.NextHop, ['topology_id', 'flags'], name, value)


                        class NextHop_(_Entity_):
                            """
                            Next hop
                            
                            .. attribute:: labeled
                            
                            	Labeled Next Hop
                            	**type**\:  :py:class:`Labeled <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.MacipDetails.MacipDetail.MacIpRoute.NextHop.NextHop_.Labeled>`
                            
                            	**config**\: False
                            
                            .. attribute:: type
                            
                            	Type
                            	**type**\:  :py:class:`L2ribNextHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2ribNextHop>`
                            
                            	**config**\: False
                            
                            .. attribute:: ipv4
                            
                            	IPV4 address Next Hop
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            	**config**\: False
                            
                            .. attribute:: ipv6
                            
                            	IPV6 address Next Hop
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            	**config**\: False
                            
                            .. attribute:: mac
                            
                            	MAC address Next Hop
                            	**type**\: str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            	**config**\: False
                            
                            .. attribute:: interface_handle
                            
                            	Intefrace Handle Next Hop
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            	**config**\: False
                            
                            .. attribute:: xid
                            
                            	XID Next Hop
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'l2rib-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(L2rib.EviChildTables.MacipDetails.MacipDetail.MacIpRoute.NextHop.NextHop_, self).__init__()

                                self.yang_name = "next-hop"
                                self.yang_parent_name = "next-hop"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("labeled", ("labeled", L2rib.EviChildTables.MacipDetails.MacipDetail.MacIpRoute.NextHop.NextHop_.Labeled))])
                                self._leafs = OrderedDict([
                                    ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper', 'L2ribNextHop', '')])),
                                    ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                                    ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                                    ('mac', (YLeaf(YType.str, 'mac'), ['str'])),
                                    ('interface_handle', (YLeaf(YType.str, 'interface-handle'), ['str'])),
                                    ('xid', (YLeaf(YType.uint32, 'xid'), ['int'])),
                                ])
                                self.type = None
                                self.ipv4 = None
                                self.ipv6 = None
                                self.mac = None
                                self.interface_handle = None
                                self.xid = None

                                self.labeled = L2rib.EviChildTables.MacipDetails.MacipDetail.MacIpRoute.NextHop.NextHop_.Labeled()
                                self.labeled.parent = self
                                self._children_name_map["labeled"] = "labeled"
                                self._segment_path = lambda: "next-hop"
                                self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/macip-details/macip-detail/mac-ip-route/next-hop/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2rib.EviChildTables.MacipDetails.MacipDetail.MacIpRoute.NextHop.NextHop_, ['type', 'ipv4', 'ipv6', 'mac', 'interface_handle', 'xid'], name, value)


                            class Labeled(_Entity_):
                                """
                                Labeled Next Hop
                                
                                .. attribute:: address_family
                                
                                	L2RIB Address Family
                                	**type**\:  :py:class:`L2ribAfi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2ribAfi>`
                                
                                	**config**\: False
                                
                                .. attribute:: ip_address
                                
                                	IP Address
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: label
                                
                                	Label
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: internal
                                
                                	Internal Label
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'l2rib-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(L2rib.EviChildTables.MacipDetails.MacipDetail.MacIpRoute.NextHop.NextHop_.Labeled, self).__init__()

                                    self.yang_name = "labeled"
                                    self.yang_parent_name = "next-hop"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = False
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('address_family', (YLeaf(YType.enumeration, 'address-family'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper', 'L2ribAfi', '')])),
                                        ('ip_address', (YLeaf(YType.str, 'ip-address'), ['str'])),
                                        ('label', (YLeaf(YType.uint32, 'label'), ['int'])),
                                        ('internal', (YLeaf(YType.boolean, 'internal'), ['bool'])),
                                    ])
                                    self.address_family = None
                                    self.ip_address = None
                                    self.label = None
                                    self.internal = None
                                    self._segment_path = lambda: "labeled"
                                    self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/macip-details/macip-detail/mac-ip-route/next-hop/next-hop/%s" % self._segment_path()
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2rib.EviChildTables.MacipDetails.MacipDetail.MacIpRoute.NextHop.NextHop_.Labeled, ['address_family', 'ip_address', 'label', 'internal'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                                    return meta._meta_table['L2rib.EviChildTables.MacipDetails.MacipDetail.MacIpRoute.NextHop.NextHop_.Labeled']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                                return meta._meta_table['L2rib.EviChildTables.MacipDetails.MacipDetail.MacIpRoute.NextHop.NextHop_']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                            return meta._meta_table['L2rib.EviChildTables.MacipDetails.MacipDetail.MacIpRoute.NextHop']['meta_info']


                    class BackupNextHop(_Entity_):
                        """
                        Secondary Next Hop
                        
                        .. attribute:: next_hop
                        
                        	Next hop
                        	**type**\:  :py:class:`NextHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.MacipDetails.MacipDetail.MacIpRoute.BackupNextHop.NextHop>`
                        
                        	**config**\: False
                        
                        .. attribute:: topology_id
                        
                        	Next\-hop TOPOLOGY ID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: flags
                        
                        	Next\-hop flags
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'l2rib-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(L2rib.EviChildTables.MacipDetails.MacipDetail.MacIpRoute.BackupNextHop, self).__init__()

                            self.yang_name = "backup-next-hop"
                            self.yang_parent_name = "mac-ip-route"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("next-hop", ("next_hop", L2rib.EviChildTables.MacipDetails.MacipDetail.MacIpRoute.BackupNextHop.NextHop))])
                            self._leafs = OrderedDict([
                                ('topology_id', (YLeaf(YType.uint32, 'topology-id'), ['int'])),
                                ('flags', (YLeaf(YType.uint16, 'flags'), ['int'])),
                            ])
                            self.topology_id = None
                            self.flags = None

                            self.next_hop = L2rib.EviChildTables.MacipDetails.MacipDetail.MacIpRoute.BackupNextHop.NextHop()
                            self.next_hop.parent = self
                            self._children_name_map["next_hop"] = "next-hop"
                            self._segment_path = lambda: "backup-next-hop"
                            self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/macip-details/macip-detail/mac-ip-route/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2rib.EviChildTables.MacipDetails.MacipDetail.MacIpRoute.BackupNextHop, ['topology_id', 'flags'], name, value)


                        class NextHop(_Entity_):
                            """
                            Next hop
                            
                            .. attribute:: labeled
                            
                            	Labeled Next Hop
                            	**type**\:  :py:class:`Labeled <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.MacipDetails.MacipDetail.MacIpRoute.BackupNextHop.NextHop.Labeled>`
                            
                            	**config**\: False
                            
                            .. attribute:: type
                            
                            	Type
                            	**type**\:  :py:class:`L2ribNextHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2ribNextHop>`
                            
                            	**config**\: False
                            
                            .. attribute:: ipv4
                            
                            	IPV4 address Next Hop
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            	**config**\: False
                            
                            .. attribute:: ipv6
                            
                            	IPV6 address Next Hop
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            	**config**\: False
                            
                            .. attribute:: mac
                            
                            	MAC address Next Hop
                            	**type**\: str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            	**config**\: False
                            
                            .. attribute:: interface_handle
                            
                            	Intefrace Handle Next Hop
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            	**config**\: False
                            
                            .. attribute:: xid
                            
                            	XID Next Hop
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'l2rib-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(L2rib.EviChildTables.MacipDetails.MacipDetail.MacIpRoute.BackupNextHop.NextHop, self).__init__()

                                self.yang_name = "next-hop"
                                self.yang_parent_name = "backup-next-hop"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("labeled", ("labeled", L2rib.EviChildTables.MacipDetails.MacipDetail.MacIpRoute.BackupNextHop.NextHop.Labeled))])
                                self._leafs = OrderedDict([
                                    ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper', 'L2ribNextHop', '')])),
                                    ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                                    ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                                    ('mac', (YLeaf(YType.str, 'mac'), ['str'])),
                                    ('interface_handle', (YLeaf(YType.str, 'interface-handle'), ['str'])),
                                    ('xid', (YLeaf(YType.uint32, 'xid'), ['int'])),
                                ])
                                self.type = None
                                self.ipv4 = None
                                self.ipv6 = None
                                self.mac = None
                                self.interface_handle = None
                                self.xid = None

                                self.labeled = L2rib.EviChildTables.MacipDetails.MacipDetail.MacIpRoute.BackupNextHop.NextHop.Labeled()
                                self.labeled.parent = self
                                self._children_name_map["labeled"] = "labeled"
                                self._segment_path = lambda: "next-hop"
                                self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/macip-details/macip-detail/mac-ip-route/backup-next-hop/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2rib.EviChildTables.MacipDetails.MacipDetail.MacIpRoute.BackupNextHop.NextHop, ['type', 'ipv4', 'ipv6', 'mac', 'interface_handle', 'xid'], name, value)


                            class Labeled(_Entity_):
                                """
                                Labeled Next Hop
                                
                                .. attribute:: address_family
                                
                                	L2RIB Address Family
                                	**type**\:  :py:class:`L2ribAfi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2ribAfi>`
                                
                                	**config**\: False
                                
                                .. attribute:: ip_address
                                
                                	IP Address
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: label
                                
                                	Label
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: internal
                                
                                	Internal Label
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'l2rib-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(L2rib.EviChildTables.MacipDetails.MacipDetail.MacIpRoute.BackupNextHop.NextHop.Labeled, self).__init__()

                                    self.yang_name = "labeled"
                                    self.yang_parent_name = "next-hop"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = False
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('address_family', (YLeaf(YType.enumeration, 'address-family'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper', 'L2ribAfi', '')])),
                                        ('ip_address', (YLeaf(YType.str, 'ip-address'), ['str'])),
                                        ('label', (YLeaf(YType.uint32, 'label'), ['int'])),
                                        ('internal', (YLeaf(YType.boolean, 'internal'), ['bool'])),
                                    ])
                                    self.address_family = None
                                    self.ip_address = None
                                    self.label = None
                                    self.internal = None
                                    self._segment_path = lambda: "labeled"
                                    self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/macip-details/macip-detail/mac-ip-route/backup-next-hop/next-hop/%s" % self._segment_path()
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2rib.EviChildTables.MacipDetails.MacipDetail.MacIpRoute.BackupNextHop.NextHop.Labeled, ['address_family', 'ip_address', 'label', 'internal'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                                    return meta._meta_table['L2rib.EviChildTables.MacipDetails.MacipDetail.MacIpRoute.BackupNextHop.NextHop.Labeled']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                                return meta._meta_table['L2rib.EviChildTables.MacipDetails.MacipDetail.MacIpRoute.BackupNextHop.NextHop']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                            return meta._meta_table['L2rib.EviChildTables.MacipDetails.MacipDetail.MacIpRoute.BackupNextHop']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                        return meta._meta_table['L2rib.EviChildTables.MacipDetails.MacipDetail.MacIpRoute']['meta_info']


                class RtTlv(_Entity_):
                    """
                    Mac\-IP Route Opaque Data TLV
                    
                    .. attribute:: tlv_type
                    
                    	TLV Type
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**config**\: False
                    
                    .. attribute:: tlv_len
                    
                    	TLV Length
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**config**\: False
                    
                    .. attribute:: tlv_val
                    
                    	TLV Value
                    	**type**\: list of  		 :py:class:`TlvVal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.MacipDetails.MacipDetail.RtTlv.TlvVal>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'l2rib-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(L2rib.EviChildTables.MacipDetails.MacipDetail.RtTlv, self).__init__()

                        self.yang_name = "rt-tlv"
                        self.yang_parent_name = "macip-detail"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("tlv-val", ("tlv_val", L2rib.EviChildTables.MacipDetails.MacipDetail.RtTlv.TlvVal))])
                        self._leafs = OrderedDict([
                            ('tlv_type', (YLeaf(YType.uint16, 'tlv-type'), ['int'])),
                            ('tlv_len', (YLeaf(YType.uint16, 'tlv-len'), ['int'])),
                        ])
                        self.tlv_type = None
                        self.tlv_len = None

                        self.tlv_val = YList(self)
                        self._segment_path = lambda: "rt-tlv"
                        self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/macip-details/macip-detail/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2rib.EviChildTables.MacipDetails.MacipDetail.RtTlv, ['tlv_type', 'tlv_len'], name, value)


                    class TlvVal(_Entity_):
                        """
                        TLV Value
                        
                        .. attribute:: entry
                        
                        	TLV Value
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'l2rib-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(L2rib.EviChildTables.MacipDetails.MacipDetail.RtTlv.TlvVal, self).__init__()

                            self.yang_name = "tlv-val"
                            self.yang_parent_name = "rt-tlv"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('entry', (YLeaf(YType.uint8, 'entry'), ['int'])),
                            ])
                            self.entry = None
                            self._segment_path = lambda: "tlv-val"
                            self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/macip-details/macip-detail/rt-tlv/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2rib.EviChildTables.MacipDetails.MacipDetail.RtTlv.TlvVal, ['entry'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                            return meta._meta_table['L2rib.EviChildTables.MacipDetails.MacipDetail.RtTlv.TlvVal']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                        return meta._meta_table['L2rib.EviChildTables.MacipDetails.MacipDetail.RtTlv']['meta_info']


                class NhTlv(_Entity_):
                    """
                    Mac\-IP Route Opaque NH TLV
                    
                    .. attribute:: tlv_type
                    
                    	TLV Type
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**config**\: False
                    
                    .. attribute:: tlv_len
                    
                    	TLV Length
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**config**\: False
                    
                    .. attribute:: tlv_val
                    
                    	TLV Value
                    	**type**\: list of  		 :py:class:`TlvVal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.MacipDetails.MacipDetail.NhTlv.TlvVal>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'l2rib-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(L2rib.EviChildTables.MacipDetails.MacipDetail.NhTlv, self).__init__()

                        self.yang_name = "nh-tlv"
                        self.yang_parent_name = "macip-detail"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("tlv-val", ("tlv_val", L2rib.EviChildTables.MacipDetails.MacipDetail.NhTlv.TlvVal))])
                        self._leafs = OrderedDict([
                            ('tlv_type', (YLeaf(YType.uint16, 'tlv-type'), ['int'])),
                            ('tlv_len', (YLeaf(YType.uint16, 'tlv-len'), ['int'])),
                        ])
                        self.tlv_type = None
                        self.tlv_len = None

                        self.tlv_val = YList(self)
                        self._segment_path = lambda: "nh-tlv"
                        self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/macip-details/macip-detail/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2rib.EviChildTables.MacipDetails.MacipDetail.NhTlv, ['tlv_type', 'tlv_len'], name, value)


                    class TlvVal(_Entity_):
                        """
                        TLV Value
                        
                        .. attribute:: entry
                        
                        	TLV Value
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'l2rib-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(L2rib.EviChildTables.MacipDetails.MacipDetail.NhTlv.TlvVal, self).__init__()

                            self.yang_name = "tlv-val"
                            self.yang_parent_name = "nh-tlv"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('entry', (YLeaf(YType.uint8, 'entry'), ['int'])),
                            ])
                            self.entry = None
                            self._segment_path = lambda: "tlv-val"
                            self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/macip-details/macip-detail/nh-tlv/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2rib.EviChildTables.MacipDetails.MacipDetail.NhTlv.TlvVal, ['entry'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                            return meta._meta_table['L2rib.EviChildTables.MacipDetails.MacipDetail.NhTlv.TlvVal']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                        return meta._meta_table['L2rib.EviChildTables.MacipDetails.MacipDetail.NhTlv']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                    return meta._meta_table['L2rib.EviChildTables.MacipDetails.MacipDetail']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                return meta._meta_table['L2rib.EviChildTables.MacipDetails']['meta_info']


        class MacIps(_Entity_):
            """
            L2RIB EVPN EVI MAC IP table
            
            .. attribute:: mac_ip
            
            	L2RIB EVPN MAC IP table
            	**type**\: list of  		 :py:class:`MacIp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.MacIps.MacIp>`
            
            	**config**\: False
            
            

            """

            _prefix = 'l2rib-oper'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(L2rib.EviChildTables.MacIps, self).__init__()

                self.yang_name = "mac-ips"
                self.yang_parent_name = "evi-child-tables"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("mac-ip", ("mac_ip", L2rib.EviChildTables.MacIps.MacIp))])
                self._leafs = OrderedDict()

                self.mac_ip = YList(self)
                self._segment_path = lambda: "mac-ips"
                self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(L2rib.EviChildTables.MacIps, [], name, value)


            class MacIp(_Entity_):
                """
                L2RIB EVPN MAC IP table
                
                .. attribute:: evi
                
                	EVPN ID
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: mac_addr
                
                	MAC\-IP Address
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                	**config**\: False
                
                .. attribute:: ip_addr
                
                	IP Address
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                	**config**\: False
                
                .. attribute:: prod_id
                
                	Producer ID
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: next_hop
                
                	Next Hop
                	**type**\:  :py:class:`NextHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.MacIps.MacIp.NextHop>`
                
                	**config**\: False
                
                .. attribute:: backup_next_hop
                
                	Secondary Next Hop
                	**type**\:  :py:class:`BackupNextHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.MacIps.MacIp.BackupNextHop>`
                
                	**config**\: False
                
                .. attribute:: mac_address
                
                	MAC Address
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                	**config**\: False
                
                .. attribute:: ip_address
                
                	IP Address
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: admin_distance
                
                	Admin Distance
                	**type**\: int
                
                	**range:** 0..255
                
                	**config**\: False
                
                .. attribute:: producer_id
                
                	Producer ID
                	**type**\: int
                
                	**range:** 0..255
                
                	**config**\: False
                
                .. attribute:: topology_id
                
                	Topology ID
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                

                """

                _prefix = 'l2rib-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(L2rib.EviChildTables.MacIps.MacIp, self).__init__()

                    self.yang_name = "mac-ip"
                    self.yang_parent_name = "mac-ips"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("next-hop", ("next_hop", L2rib.EviChildTables.MacIps.MacIp.NextHop)), ("backup-next-hop", ("backup_next_hop", L2rib.EviChildTables.MacIps.MacIp.BackupNextHop))])
                    self._leafs = OrderedDict([
                        ('evi', (YLeaf(YType.uint32, 'evi'), ['int'])),
                        ('mac_addr', (YLeaf(YType.str, 'mac-addr'), ['str'])),
                        ('ip_addr', (YLeaf(YType.str, 'ip-addr'), ['str','str'])),
                        ('prod_id', (YLeaf(YType.uint32, 'prod-id'), ['int'])),
                        ('mac_address', (YLeaf(YType.str, 'mac-address'), ['str'])),
                        ('ip_address', (YLeaf(YType.str, 'ip-address'), ['str'])),
                        ('admin_distance', (YLeaf(YType.uint8, 'admin-distance'), ['int'])),
                        ('producer_id', (YLeaf(YType.uint8, 'producer-id'), ['int'])),
                        ('topology_id', (YLeaf(YType.uint32, 'topology-id'), ['int'])),
                    ])
                    self.evi = None
                    self.mac_addr = None
                    self.ip_addr = None
                    self.prod_id = None
                    self.mac_address = None
                    self.ip_address = None
                    self.admin_distance = None
                    self.producer_id = None
                    self.topology_id = None

                    self.next_hop = L2rib.EviChildTables.MacIps.MacIp.NextHop()
                    self.next_hop.parent = self
                    self._children_name_map["next_hop"] = "next-hop"

                    self.backup_next_hop = L2rib.EviChildTables.MacIps.MacIp.BackupNextHop()
                    self.backup_next_hop.parent = self
                    self._children_name_map["backup_next_hop"] = "backup-next-hop"
                    self._segment_path = lambda: "mac-ip"
                    self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/mac-ips/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(L2rib.EviChildTables.MacIps.MacIp, ['evi', 'mac_addr', 'ip_addr', 'prod_id', 'mac_address', 'ip_address', 'admin_distance', 'producer_id', 'topology_id'], name, value)


                class NextHop(_Entity_):
                    """
                    Next Hop
                    
                    .. attribute:: next_hop
                    
                    	Next hop
                    	**type**\:  :py:class:`NextHop_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.MacIps.MacIp.NextHop.NextHop_>`
                    
                    	**config**\: False
                    
                    .. attribute:: topology_id
                    
                    	Next\-hop TOPOLOGY ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: flags
                    
                    	Next\-hop flags
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'l2rib-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(L2rib.EviChildTables.MacIps.MacIp.NextHop, self).__init__()

                        self.yang_name = "next-hop"
                        self.yang_parent_name = "mac-ip"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("next-hop", ("next_hop", L2rib.EviChildTables.MacIps.MacIp.NextHop.NextHop_))])
                        self._leafs = OrderedDict([
                            ('topology_id', (YLeaf(YType.uint32, 'topology-id'), ['int'])),
                            ('flags', (YLeaf(YType.uint16, 'flags'), ['int'])),
                        ])
                        self.topology_id = None
                        self.flags = None

                        self.next_hop = L2rib.EviChildTables.MacIps.MacIp.NextHop.NextHop_()
                        self.next_hop.parent = self
                        self._children_name_map["next_hop"] = "next-hop"
                        self._segment_path = lambda: "next-hop"
                        self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/mac-ips/mac-ip/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2rib.EviChildTables.MacIps.MacIp.NextHop, ['topology_id', 'flags'], name, value)


                    class NextHop_(_Entity_):
                        """
                        Next hop
                        
                        .. attribute:: labeled
                        
                        	Labeled Next Hop
                        	**type**\:  :py:class:`Labeled <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.MacIps.MacIp.NextHop.NextHop_.Labeled>`
                        
                        	**config**\: False
                        
                        .. attribute:: type
                        
                        	Type
                        	**type**\:  :py:class:`L2ribNextHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2ribNextHop>`
                        
                        	**config**\: False
                        
                        .. attribute:: ipv4
                        
                        	IPV4 address Next Hop
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        	**config**\: False
                        
                        .. attribute:: ipv6
                        
                        	IPV6 address Next Hop
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        	**config**\: False
                        
                        .. attribute:: mac
                        
                        	MAC address Next Hop
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        	**config**\: False
                        
                        .. attribute:: interface_handle
                        
                        	Intefrace Handle Next Hop
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        	**config**\: False
                        
                        .. attribute:: xid
                        
                        	XID Next Hop
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'l2rib-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(L2rib.EviChildTables.MacIps.MacIp.NextHop.NextHop_, self).__init__()

                            self.yang_name = "next-hop"
                            self.yang_parent_name = "next-hop"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("labeled", ("labeled", L2rib.EviChildTables.MacIps.MacIp.NextHop.NextHop_.Labeled))])
                            self._leafs = OrderedDict([
                                ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper', 'L2ribNextHop', '')])),
                                ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                                ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                                ('mac', (YLeaf(YType.str, 'mac'), ['str'])),
                                ('interface_handle', (YLeaf(YType.str, 'interface-handle'), ['str'])),
                                ('xid', (YLeaf(YType.uint32, 'xid'), ['int'])),
                            ])
                            self.type = None
                            self.ipv4 = None
                            self.ipv6 = None
                            self.mac = None
                            self.interface_handle = None
                            self.xid = None

                            self.labeled = L2rib.EviChildTables.MacIps.MacIp.NextHop.NextHop_.Labeled()
                            self.labeled.parent = self
                            self._children_name_map["labeled"] = "labeled"
                            self._segment_path = lambda: "next-hop"
                            self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/mac-ips/mac-ip/next-hop/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2rib.EviChildTables.MacIps.MacIp.NextHop.NextHop_, ['type', 'ipv4', 'ipv6', 'mac', 'interface_handle', 'xid'], name, value)


                        class Labeled(_Entity_):
                            """
                            Labeled Next Hop
                            
                            .. attribute:: address_family
                            
                            	L2RIB Address Family
                            	**type**\:  :py:class:`L2ribAfi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2ribAfi>`
                            
                            	**config**\: False
                            
                            .. attribute:: ip_address
                            
                            	IP Address
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: label
                            
                            	Label
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: internal
                            
                            	Internal Label
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'l2rib-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(L2rib.EviChildTables.MacIps.MacIp.NextHop.NextHop_.Labeled, self).__init__()

                                self.yang_name = "labeled"
                                self.yang_parent_name = "next-hop"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('address_family', (YLeaf(YType.enumeration, 'address-family'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper', 'L2ribAfi', '')])),
                                    ('ip_address', (YLeaf(YType.str, 'ip-address'), ['str'])),
                                    ('label', (YLeaf(YType.uint32, 'label'), ['int'])),
                                    ('internal', (YLeaf(YType.boolean, 'internal'), ['bool'])),
                                ])
                                self.address_family = None
                                self.ip_address = None
                                self.label = None
                                self.internal = None
                                self._segment_path = lambda: "labeled"
                                self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/mac-ips/mac-ip/next-hop/next-hop/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2rib.EviChildTables.MacIps.MacIp.NextHop.NextHop_.Labeled, ['address_family', 'ip_address', 'label', 'internal'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                                return meta._meta_table['L2rib.EviChildTables.MacIps.MacIp.NextHop.NextHop_.Labeled']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                            return meta._meta_table['L2rib.EviChildTables.MacIps.MacIp.NextHop.NextHop_']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                        return meta._meta_table['L2rib.EviChildTables.MacIps.MacIp.NextHop']['meta_info']


                class BackupNextHop(_Entity_):
                    """
                    Secondary Next Hop
                    
                    .. attribute:: next_hop
                    
                    	Next hop
                    	**type**\:  :py:class:`NextHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.MacIps.MacIp.BackupNextHop.NextHop>`
                    
                    	**config**\: False
                    
                    .. attribute:: topology_id
                    
                    	Next\-hop TOPOLOGY ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: flags
                    
                    	Next\-hop flags
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'l2rib-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(L2rib.EviChildTables.MacIps.MacIp.BackupNextHop, self).__init__()

                        self.yang_name = "backup-next-hop"
                        self.yang_parent_name = "mac-ip"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("next-hop", ("next_hop", L2rib.EviChildTables.MacIps.MacIp.BackupNextHop.NextHop))])
                        self._leafs = OrderedDict([
                            ('topology_id', (YLeaf(YType.uint32, 'topology-id'), ['int'])),
                            ('flags', (YLeaf(YType.uint16, 'flags'), ['int'])),
                        ])
                        self.topology_id = None
                        self.flags = None

                        self.next_hop = L2rib.EviChildTables.MacIps.MacIp.BackupNextHop.NextHop()
                        self.next_hop.parent = self
                        self._children_name_map["next_hop"] = "next-hop"
                        self._segment_path = lambda: "backup-next-hop"
                        self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/mac-ips/mac-ip/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2rib.EviChildTables.MacIps.MacIp.BackupNextHop, ['topology_id', 'flags'], name, value)


                    class NextHop(_Entity_):
                        """
                        Next hop
                        
                        .. attribute:: labeled
                        
                        	Labeled Next Hop
                        	**type**\:  :py:class:`Labeled <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.MacIps.MacIp.BackupNextHop.NextHop.Labeled>`
                        
                        	**config**\: False
                        
                        .. attribute:: type
                        
                        	Type
                        	**type**\:  :py:class:`L2ribNextHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2ribNextHop>`
                        
                        	**config**\: False
                        
                        .. attribute:: ipv4
                        
                        	IPV4 address Next Hop
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        	**config**\: False
                        
                        .. attribute:: ipv6
                        
                        	IPV6 address Next Hop
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        	**config**\: False
                        
                        .. attribute:: mac
                        
                        	MAC address Next Hop
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        	**config**\: False
                        
                        .. attribute:: interface_handle
                        
                        	Intefrace Handle Next Hop
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        	**config**\: False
                        
                        .. attribute:: xid
                        
                        	XID Next Hop
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'l2rib-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(L2rib.EviChildTables.MacIps.MacIp.BackupNextHop.NextHop, self).__init__()

                            self.yang_name = "next-hop"
                            self.yang_parent_name = "backup-next-hop"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("labeled", ("labeled", L2rib.EviChildTables.MacIps.MacIp.BackupNextHop.NextHop.Labeled))])
                            self._leafs = OrderedDict([
                                ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper', 'L2ribNextHop', '')])),
                                ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                                ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                                ('mac', (YLeaf(YType.str, 'mac'), ['str'])),
                                ('interface_handle', (YLeaf(YType.str, 'interface-handle'), ['str'])),
                                ('xid', (YLeaf(YType.uint32, 'xid'), ['int'])),
                            ])
                            self.type = None
                            self.ipv4 = None
                            self.ipv6 = None
                            self.mac = None
                            self.interface_handle = None
                            self.xid = None

                            self.labeled = L2rib.EviChildTables.MacIps.MacIp.BackupNextHop.NextHop.Labeled()
                            self.labeled.parent = self
                            self._children_name_map["labeled"] = "labeled"
                            self._segment_path = lambda: "next-hop"
                            self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/mac-ips/mac-ip/backup-next-hop/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2rib.EviChildTables.MacIps.MacIp.BackupNextHop.NextHop, ['type', 'ipv4', 'ipv6', 'mac', 'interface_handle', 'xid'], name, value)


                        class Labeled(_Entity_):
                            """
                            Labeled Next Hop
                            
                            .. attribute:: address_family
                            
                            	L2RIB Address Family
                            	**type**\:  :py:class:`L2ribAfi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2ribAfi>`
                            
                            	**config**\: False
                            
                            .. attribute:: ip_address
                            
                            	IP Address
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: label
                            
                            	Label
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: internal
                            
                            	Internal Label
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'l2rib-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(L2rib.EviChildTables.MacIps.MacIp.BackupNextHop.NextHop.Labeled, self).__init__()

                                self.yang_name = "labeled"
                                self.yang_parent_name = "next-hop"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('address_family', (YLeaf(YType.enumeration, 'address-family'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper', 'L2ribAfi', '')])),
                                    ('ip_address', (YLeaf(YType.str, 'ip-address'), ['str'])),
                                    ('label', (YLeaf(YType.uint32, 'label'), ['int'])),
                                    ('internal', (YLeaf(YType.boolean, 'internal'), ['bool'])),
                                ])
                                self.address_family = None
                                self.ip_address = None
                                self.label = None
                                self.internal = None
                                self._segment_path = lambda: "labeled"
                                self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/mac-ips/mac-ip/backup-next-hop/next-hop/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2rib.EviChildTables.MacIps.MacIp.BackupNextHop.NextHop.Labeled, ['address_family', 'ip_address', 'label', 'internal'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                                return meta._meta_table['L2rib.EviChildTables.MacIps.MacIp.BackupNextHop.NextHop.Labeled']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                            return meta._meta_table['L2rib.EviChildTables.MacIps.MacIp.BackupNextHop.NextHop']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                        return meta._meta_table['L2rib.EviChildTables.MacIps.MacIp.BackupNextHop']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                    return meta._meta_table['L2rib.EviChildTables.MacIps.MacIp']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                return meta._meta_table['L2rib.EviChildTables.MacIps']['meta_info']


        class Macs(_Entity_):
            """
            L2RIB EVPN EVI MAC table
            
            .. attribute:: mac
            
            	L2RIB EVPN MAC table
            	**type**\: list of  		 :py:class:`Mac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.Macs.Mac>`
            
            	**config**\: False
            
            

            """

            _prefix = 'l2rib-oper'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(L2rib.EviChildTables.Macs, self).__init__()

                self.yang_name = "macs"
                self.yang_parent_name = "evi-child-tables"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("mac", ("mac", L2rib.EviChildTables.Macs.Mac))])
                self._leafs = OrderedDict()

                self.mac = YList(self)
                self._segment_path = lambda: "macs"
                self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(L2rib.EviChildTables.Macs, [], name, value)


            class Mac(_Entity_):
                """
                L2RIB EVPN MAC table
                
                .. attribute:: evi
                
                	EVPN ID
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: mac_addr
                
                	MAC Address
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                	**config**\: False
                
                .. attribute:: prod_id
                
                	Producer ID
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: route
                
                	MAC route
                	**type**\:  :py:class:`Route <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.Macs.Mac.Route>`
                
                	**config**\: False
                
                .. attribute:: mac_address
                
                	MAC Address
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                	**config**\: False
                
                .. attribute:: admin_distance
                
                	Admin Distance
                	**type**\: int
                
                	**range:** 0..255
                
                	**config**\: False
                
                .. attribute:: producer_id
                
                	Producer ID
                	**type**\: int
                
                	**range:** 0..255
                
                	**config**\: False
                
                .. attribute:: topology_id
                
                	Topology ID
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                

                """

                _prefix = 'l2rib-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(L2rib.EviChildTables.Macs.Mac, self).__init__()

                    self.yang_name = "mac"
                    self.yang_parent_name = "macs"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("route", ("route", L2rib.EviChildTables.Macs.Mac.Route))])
                    self._leafs = OrderedDict([
                        ('evi', (YLeaf(YType.uint32, 'evi'), ['int'])),
                        ('mac_addr', (YLeaf(YType.str, 'mac-addr'), ['str'])),
                        ('prod_id', (YLeaf(YType.uint32, 'prod-id'), ['int'])),
                        ('mac_address', (YLeaf(YType.str, 'mac-address'), ['str'])),
                        ('admin_distance', (YLeaf(YType.uint8, 'admin-distance'), ['int'])),
                        ('producer_id', (YLeaf(YType.uint8, 'producer-id'), ['int'])),
                        ('topology_id', (YLeaf(YType.uint32, 'topology-id'), ['int'])),
                    ])
                    self.evi = None
                    self.mac_addr = None
                    self.prod_id = None
                    self.mac_address = None
                    self.admin_distance = None
                    self.producer_id = None
                    self.topology_id = None

                    self.route = L2rib.EviChildTables.Macs.Mac.Route()
                    self.route.parent = self
                    self._children_name_map["route"] = "route"
                    self._segment_path = lambda: "mac"
                    self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/macs/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(L2rib.EviChildTables.Macs.Mac, ['evi', 'mac_addr', 'prod_id', 'mac_address', 'admin_distance', 'producer_id', 'topology_id'], name, value)


                class Route(_Entity_):
                    """
                    MAC route
                    
                    .. attribute:: regular
                    
                    	Regular MAC route
                    	**type**\:  :py:class:`Regular <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.Macs.Mac.Route.Regular>`
                    
                    	**config**\: False
                    
                    .. attribute:: evpn_esi
                    
                    	EVPN ESI MAC route
                    	**type**\:  :py:class:`EvpnEsi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.Macs.Mac.Route.EvpnEsi>`
                    
                    	**config**\: False
                    
                    .. attribute:: bmac
                    
                    	BMAC route
                    	**type**\:  :py:class:`Bmac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.Macs.Mac.Route.Bmac>`
                    
                    	**config**\: False
                    
                    .. attribute:: type
                    
                    	Type
                    	**type**\:  :py:class:`L2ribMacRoute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2ribMacRoute>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'l2rib-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(L2rib.EviChildTables.Macs.Mac.Route, self).__init__()

                        self.yang_name = "route"
                        self.yang_parent_name = "mac"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("regular", ("regular", L2rib.EviChildTables.Macs.Mac.Route.Regular)), ("evpn-esi", ("evpn_esi", L2rib.EviChildTables.Macs.Mac.Route.EvpnEsi)), ("bmac", ("bmac", L2rib.EviChildTables.Macs.Mac.Route.Bmac))])
                        self._leafs = OrderedDict([
                            ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper', 'L2ribMacRoute', '')])),
                        ])
                        self.type = None

                        self.regular = L2rib.EviChildTables.Macs.Mac.Route.Regular()
                        self.regular.parent = self
                        self._children_name_map["regular"] = "regular"

                        self.evpn_esi = L2rib.EviChildTables.Macs.Mac.Route.EvpnEsi()
                        self.evpn_esi.parent = self
                        self._children_name_map["evpn_esi"] = "evpn-esi"

                        self.bmac = L2rib.EviChildTables.Macs.Mac.Route.Bmac()
                        self.bmac.parent = self
                        self._children_name_map["bmac"] = "bmac"
                        self._segment_path = lambda: "route"
                        self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/macs/mac/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2rib.EviChildTables.Macs.Mac.Route, ['type'], name, value)


                    class Regular(_Entity_):
                        """
                        Regular MAC route
                        
                        .. attribute:: next_hop
                        
                        	Next Hop
                        	**type**\:  :py:class:`NextHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.Macs.Mac.Route.Regular.NextHop>`
                        
                        	**config**\: False
                        
                        .. attribute:: backup_next_hop
                        
                        	Secondary Next Hop
                        	**type**\:  :py:class:`BackupNextHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.Macs.Mac.Route.Regular.BackupNextHop>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'l2rib-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(L2rib.EviChildTables.Macs.Mac.Route.Regular, self).__init__()

                            self.yang_name = "regular"
                            self.yang_parent_name = "route"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("next-hop", ("next_hop", L2rib.EviChildTables.Macs.Mac.Route.Regular.NextHop)), ("backup-next-hop", ("backup_next_hop", L2rib.EviChildTables.Macs.Mac.Route.Regular.BackupNextHop))])
                            self._leafs = OrderedDict()

                            self.next_hop = L2rib.EviChildTables.Macs.Mac.Route.Regular.NextHop()
                            self.next_hop.parent = self
                            self._children_name_map["next_hop"] = "next-hop"

                            self.backup_next_hop = L2rib.EviChildTables.Macs.Mac.Route.Regular.BackupNextHop()
                            self.backup_next_hop.parent = self
                            self._children_name_map["backup_next_hop"] = "backup-next-hop"
                            self._segment_path = lambda: "regular"
                            self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/macs/mac/route/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2rib.EviChildTables.Macs.Mac.Route.Regular, [], name, value)


                        class NextHop(_Entity_):
                            """
                            Next Hop
                            
                            .. attribute:: next_hop
                            
                            	Next hop
                            	**type**\:  :py:class:`NextHop_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.Macs.Mac.Route.Regular.NextHop.NextHop_>`
                            
                            	**config**\: False
                            
                            .. attribute:: topology_id
                            
                            	Next\-hop TOPOLOGY ID
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: flags
                            
                            	Next\-hop flags
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'l2rib-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(L2rib.EviChildTables.Macs.Mac.Route.Regular.NextHop, self).__init__()

                                self.yang_name = "next-hop"
                                self.yang_parent_name = "regular"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("next-hop", ("next_hop", L2rib.EviChildTables.Macs.Mac.Route.Regular.NextHop.NextHop_))])
                                self._leafs = OrderedDict([
                                    ('topology_id', (YLeaf(YType.uint32, 'topology-id'), ['int'])),
                                    ('flags', (YLeaf(YType.uint16, 'flags'), ['int'])),
                                ])
                                self.topology_id = None
                                self.flags = None

                                self.next_hop = L2rib.EviChildTables.Macs.Mac.Route.Regular.NextHop.NextHop_()
                                self.next_hop.parent = self
                                self._children_name_map["next_hop"] = "next-hop"
                                self._segment_path = lambda: "next-hop"
                                self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/macs/mac/route/regular/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2rib.EviChildTables.Macs.Mac.Route.Regular.NextHop, ['topology_id', 'flags'], name, value)


                            class NextHop_(_Entity_):
                                """
                                Next hop
                                
                                .. attribute:: labeled
                                
                                	Labeled Next Hop
                                	**type**\:  :py:class:`Labeled <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.Macs.Mac.Route.Regular.NextHop.NextHop_.Labeled>`
                                
                                	**config**\: False
                                
                                .. attribute:: type
                                
                                	Type
                                	**type**\:  :py:class:`L2ribNextHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2ribNextHop>`
                                
                                	**config**\: False
                                
                                .. attribute:: ipv4
                                
                                	IPV4 address Next Hop
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                	**config**\: False
                                
                                .. attribute:: ipv6
                                
                                	IPV6 address Next Hop
                                	**type**\: str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                	**config**\: False
                                
                                .. attribute:: mac
                                
                                	MAC address Next Hop
                                	**type**\: str
                                
                                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                
                                	**config**\: False
                                
                                .. attribute:: interface_handle
                                
                                	Intefrace Handle Next Hop
                                	**type**\: str
                                
                                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                                
                                	**config**\: False
                                
                                .. attribute:: xid
                                
                                	XID Next Hop
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'l2rib-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(L2rib.EviChildTables.Macs.Mac.Route.Regular.NextHop.NextHop_, self).__init__()

                                    self.yang_name = "next-hop"
                                    self.yang_parent_name = "next-hop"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = False
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("labeled", ("labeled", L2rib.EviChildTables.Macs.Mac.Route.Regular.NextHop.NextHop_.Labeled))])
                                    self._leafs = OrderedDict([
                                        ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper', 'L2ribNextHop', '')])),
                                        ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                                        ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                                        ('mac', (YLeaf(YType.str, 'mac'), ['str'])),
                                        ('interface_handle', (YLeaf(YType.str, 'interface-handle'), ['str'])),
                                        ('xid', (YLeaf(YType.uint32, 'xid'), ['int'])),
                                    ])
                                    self.type = None
                                    self.ipv4 = None
                                    self.ipv6 = None
                                    self.mac = None
                                    self.interface_handle = None
                                    self.xid = None

                                    self.labeled = L2rib.EviChildTables.Macs.Mac.Route.Regular.NextHop.NextHop_.Labeled()
                                    self.labeled.parent = self
                                    self._children_name_map["labeled"] = "labeled"
                                    self._segment_path = lambda: "next-hop"
                                    self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/macs/mac/route/regular/next-hop/%s" % self._segment_path()
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2rib.EviChildTables.Macs.Mac.Route.Regular.NextHop.NextHop_, ['type', 'ipv4', 'ipv6', 'mac', 'interface_handle', 'xid'], name, value)


                                class Labeled(_Entity_):
                                    """
                                    Labeled Next Hop
                                    
                                    .. attribute:: address_family
                                    
                                    	L2RIB Address Family
                                    	**type**\:  :py:class:`L2ribAfi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2ribAfi>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: ip_address
                                    
                                    	IP Address
                                    	**type**\: str
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: label
                                    
                                    	Label
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: internal
                                    
                                    	Internal Label
                                    	**type**\: bool
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'l2rib-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(L2rib.EviChildTables.Macs.Mac.Route.Regular.NextHop.NextHop_.Labeled, self).__init__()

                                        self.yang_name = "labeled"
                                        self.yang_parent_name = "next-hop"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = False
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('address_family', (YLeaf(YType.enumeration, 'address-family'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper', 'L2ribAfi', '')])),
                                            ('ip_address', (YLeaf(YType.str, 'ip-address'), ['str'])),
                                            ('label', (YLeaf(YType.uint32, 'label'), ['int'])),
                                            ('internal', (YLeaf(YType.boolean, 'internal'), ['bool'])),
                                        ])
                                        self.address_family = None
                                        self.ip_address = None
                                        self.label = None
                                        self.internal = None
                                        self._segment_path = lambda: "labeled"
                                        self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/macs/mac/route/regular/next-hop/next-hop/%s" % self._segment_path()
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(L2rib.EviChildTables.Macs.Mac.Route.Regular.NextHop.NextHop_.Labeled, ['address_family', 'ip_address', 'label', 'internal'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                                        return meta._meta_table['L2rib.EviChildTables.Macs.Mac.Route.Regular.NextHop.NextHop_.Labeled']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                                    return meta._meta_table['L2rib.EviChildTables.Macs.Mac.Route.Regular.NextHop.NextHop_']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                                return meta._meta_table['L2rib.EviChildTables.Macs.Mac.Route.Regular.NextHop']['meta_info']


                        class BackupNextHop(_Entity_):
                            """
                            Secondary Next Hop
                            
                            .. attribute:: next_hop
                            
                            	Next hop
                            	**type**\:  :py:class:`NextHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.Macs.Mac.Route.Regular.BackupNextHop.NextHop>`
                            
                            	**config**\: False
                            
                            .. attribute:: topology_id
                            
                            	Next\-hop TOPOLOGY ID
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: flags
                            
                            	Next\-hop flags
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'l2rib-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(L2rib.EviChildTables.Macs.Mac.Route.Regular.BackupNextHop, self).__init__()

                                self.yang_name = "backup-next-hop"
                                self.yang_parent_name = "regular"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("next-hop", ("next_hop", L2rib.EviChildTables.Macs.Mac.Route.Regular.BackupNextHop.NextHop))])
                                self._leafs = OrderedDict([
                                    ('topology_id', (YLeaf(YType.uint32, 'topology-id'), ['int'])),
                                    ('flags', (YLeaf(YType.uint16, 'flags'), ['int'])),
                                ])
                                self.topology_id = None
                                self.flags = None

                                self.next_hop = L2rib.EviChildTables.Macs.Mac.Route.Regular.BackupNextHop.NextHop()
                                self.next_hop.parent = self
                                self._children_name_map["next_hop"] = "next-hop"
                                self._segment_path = lambda: "backup-next-hop"
                                self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/macs/mac/route/regular/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2rib.EviChildTables.Macs.Mac.Route.Regular.BackupNextHop, ['topology_id', 'flags'], name, value)


                            class NextHop(_Entity_):
                                """
                                Next hop
                                
                                .. attribute:: labeled
                                
                                	Labeled Next Hop
                                	**type**\:  :py:class:`Labeled <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.Macs.Mac.Route.Regular.BackupNextHop.NextHop.Labeled>`
                                
                                	**config**\: False
                                
                                .. attribute:: type
                                
                                	Type
                                	**type**\:  :py:class:`L2ribNextHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2ribNextHop>`
                                
                                	**config**\: False
                                
                                .. attribute:: ipv4
                                
                                	IPV4 address Next Hop
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                	**config**\: False
                                
                                .. attribute:: ipv6
                                
                                	IPV6 address Next Hop
                                	**type**\: str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                	**config**\: False
                                
                                .. attribute:: mac
                                
                                	MAC address Next Hop
                                	**type**\: str
                                
                                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                
                                	**config**\: False
                                
                                .. attribute:: interface_handle
                                
                                	Intefrace Handle Next Hop
                                	**type**\: str
                                
                                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                                
                                	**config**\: False
                                
                                .. attribute:: xid
                                
                                	XID Next Hop
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'l2rib-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(L2rib.EviChildTables.Macs.Mac.Route.Regular.BackupNextHop.NextHop, self).__init__()

                                    self.yang_name = "next-hop"
                                    self.yang_parent_name = "backup-next-hop"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = False
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("labeled", ("labeled", L2rib.EviChildTables.Macs.Mac.Route.Regular.BackupNextHop.NextHop.Labeled))])
                                    self._leafs = OrderedDict([
                                        ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper', 'L2ribNextHop', '')])),
                                        ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                                        ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                                        ('mac', (YLeaf(YType.str, 'mac'), ['str'])),
                                        ('interface_handle', (YLeaf(YType.str, 'interface-handle'), ['str'])),
                                        ('xid', (YLeaf(YType.uint32, 'xid'), ['int'])),
                                    ])
                                    self.type = None
                                    self.ipv4 = None
                                    self.ipv6 = None
                                    self.mac = None
                                    self.interface_handle = None
                                    self.xid = None

                                    self.labeled = L2rib.EviChildTables.Macs.Mac.Route.Regular.BackupNextHop.NextHop.Labeled()
                                    self.labeled.parent = self
                                    self._children_name_map["labeled"] = "labeled"
                                    self._segment_path = lambda: "next-hop"
                                    self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/macs/mac/route/regular/backup-next-hop/%s" % self._segment_path()
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2rib.EviChildTables.Macs.Mac.Route.Regular.BackupNextHop.NextHop, ['type', 'ipv4', 'ipv6', 'mac', 'interface_handle', 'xid'], name, value)


                                class Labeled(_Entity_):
                                    """
                                    Labeled Next Hop
                                    
                                    .. attribute:: address_family
                                    
                                    	L2RIB Address Family
                                    	**type**\:  :py:class:`L2ribAfi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2ribAfi>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: ip_address
                                    
                                    	IP Address
                                    	**type**\: str
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: label
                                    
                                    	Label
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: internal
                                    
                                    	Internal Label
                                    	**type**\: bool
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'l2rib-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(L2rib.EviChildTables.Macs.Mac.Route.Regular.BackupNextHop.NextHop.Labeled, self).__init__()

                                        self.yang_name = "labeled"
                                        self.yang_parent_name = "next-hop"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = False
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('address_family', (YLeaf(YType.enumeration, 'address-family'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper', 'L2ribAfi', '')])),
                                            ('ip_address', (YLeaf(YType.str, 'ip-address'), ['str'])),
                                            ('label', (YLeaf(YType.uint32, 'label'), ['int'])),
                                            ('internal', (YLeaf(YType.boolean, 'internal'), ['bool'])),
                                        ])
                                        self.address_family = None
                                        self.ip_address = None
                                        self.label = None
                                        self.internal = None
                                        self._segment_path = lambda: "labeled"
                                        self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/macs/mac/route/regular/backup-next-hop/next-hop/%s" % self._segment_path()
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(L2rib.EviChildTables.Macs.Mac.Route.Regular.BackupNextHop.NextHop.Labeled, ['address_family', 'ip_address', 'label', 'internal'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                                        return meta._meta_table['L2rib.EviChildTables.Macs.Mac.Route.Regular.BackupNextHop.NextHop.Labeled']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                                    return meta._meta_table['L2rib.EviChildTables.Macs.Mac.Route.Regular.BackupNextHop.NextHop']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                                return meta._meta_table['L2rib.EviChildTables.Macs.Mac.Route.Regular.BackupNextHop']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                            return meta._meta_table['L2rib.EviChildTables.Macs.Mac.Route.Regular']['meta_info']


                    class EvpnEsi(_Entity_):
                        """
                        EVPN ESI MAC route
                        
                        .. attribute:: ethernet_segment_id
                        
                        	Ethernet Segment Identifier
                        	**type**\:  :py:class:`EthernetSegmentId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.Macs.Mac.Route.EvpnEsi.EthernetSegmentId>`
                        
                        	**config**\: False
                        
                        .. attribute:: path_list
                        
                        	Path list information. Set for detailed MAC route information
                        	**type**\:  :py:class:`PathList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.Macs.Mac.Route.EvpnEsi.PathList>`
                        
                        	**config**\: False
                        
                        .. attribute:: sequence_number
                        
                        	MAC route sequence number
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: forward_state
                        
                        	Forwarding State. True means forward, False means drop
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'l2rib-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(L2rib.EviChildTables.Macs.Mac.Route.EvpnEsi, self).__init__()

                            self.yang_name = "evpn-esi"
                            self.yang_parent_name = "route"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("ethernet-segment-id", ("ethernet_segment_id", L2rib.EviChildTables.Macs.Mac.Route.EvpnEsi.EthernetSegmentId)), ("path-list", ("path_list", L2rib.EviChildTables.Macs.Mac.Route.EvpnEsi.PathList))])
                            self._leafs = OrderedDict([
                                ('sequence_number', (YLeaf(YType.uint32, 'sequence-number'), ['int'])),
                                ('forward_state', (YLeaf(YType.boolean, 'forward-state'), ['bool'])),
                            ])
                            self.sequence_number = None
                            self.forward_state = None

                            self.ethernet_segment_id = L2rib.EviChildTables.Macs.Mac.Route.EvpnEsi.EthernetSegmentId()
                            self.ethernet_segment_id.parent = self
                            self._children_name_map["ethernet_segment_id"] = "ethernet-segment-id"

                            self.path_list = L2rib.EviChildTables.Macs.Mac.Route.EvpnEsi.PathList()
                            self.path_list.parent = self
                            self._children_name_map["path_list"] = "path-list"
                            self._segment_path = lambda: "evpn-esi"
                            self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/macs/mac/route/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2rib.EviChildTables.Macs.Mac.Route.EvpnEsi, ['sequence_number', 'forward_state'], name, value)


                        class EthernetSegmentId(_Entity_):
                            """
                            Ethernet Segment Identifier
                            
                            .. attribute:: system_priority
                            
                            	LACP System Priority
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            	**config**\: False
                            
                            .. attribute:: system_id
                            
                            	LACP System Id
                            	**type**\: str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            	**config**\: False
                            
                            .. attribute:: port_key
                            
                            	LACP Port Key
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'l2rib-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(L2rib.EviChildTables.Macs.Mac.Route.EvpnEsi.EthernetSegmentId, self).__init__()

                                self.yang_name = "ethernet-segment-id"
                                self.yang_parent_name = "evpn-esi"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('system_priority', (YLeaf(YType.uint16, 'system-priority'), ['int'])),
                                    ('system_id', (YLeaf(YType.str, 'system-id'), ['str'])),
                                    ('port_key', (YLeaf(YType.uint16, 'port-key'), ['int'])),
                                ])
                                self.system_priority = None
                                self.system_id = None
                                self.port_key = None
                                self._segment_path = lambda: "ethernet-segment-id"
                                self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/macs/mac/route/evpn-esi/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2rib.EviChildTables.Macs.Mac.Route.EvpnEsi.EthernetSegmentId, ['system_priority', 'system_id', 'port_key'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                                return meta._meta_table['L2rib.EviChildTables.Macs.Mac.Route.EvpnEsi.EthernetSegmentId']['meta_info']


                        class PathList(_Entity_):
                            """
                            Path list information. Set for detailed MAC
                            route information
                            
                            .. attribute:: path_list_info
                            
                            	Type\-specific Path List info
                            	**type**\:  :py:class:`PathListInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.Macs.Mac.Route.EvpnEsi.PathList.PathListInfo>`
                            
                            	**config**\: False
                            
                            .. attribute:: producer_id
                            
                            	ID of EAD route producer
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            .. attribute:: mac_count
                            
                            	Number of MAC routes bound to this Path list
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: local_label
                            
                            	Path list local Label
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: next_hop_array
                            
                            	Array of Next Hops for MAC Path List
                            	**type**\: list of  		 :py:class:`NextHopArray <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.Macs.Mac.Route.EvpnEsi.PathList.NextHopArray>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'l2rib-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(L2rib.EviChildTables.Macs.Mac.Route.EvpnEsi.PathList, self).__init__()

                                self.yang_name = "path-list"
                                self.yang_parent_name = "evpn-esi"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("path-list-info", ("path_list_info", L2rib.EviChildTables.Macs.Mac.Route.EvpnEsi.PathList.PathListInfo)), ("next-hop-array", ("next_hop_array", L2rib.EviChildTables.Macs.Mac.Route.EvpnEsi.PathList.NextHopArray))])
                                self._leafs = OrderedDict([
                                    ('producer_id', (YLeaf(YType.uint8, 'producer-id'), ['int'])),
                                    ('mac_count', (YLeaf(YType.uint32, 'mac-count'), ['int'])),
                                    ('local_label', (YLeaf(YType.uint32, 'local-label'), ['int'])),
                                ])
                                self.producer_id = None
                                self.mac_count = None
                                self.local_label = None

                                self.path_list_info = L2rib.EviChildTables.Macs.Mac.Route.EvpnEsi.PathList.PathListInfo()
                                self.path_list_info.parent = self
                                self._children_name_map["path_list_info"] = "path-list-info"

                                self.next_hop_array = YList(self)
                                self._segment_path = lambda: "path-list"
                                self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/macs/mac/route/evpn-esi/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2rib.EviChildTables.Macs.Mac.Route.EvpnEsi.PathList, ['producer_id', 'mac_count', 'local_label'], name, value)


                            class PathListInfo(_Entity_):
                                """
                                Type\-specific Path List info
                                
                                .. attribute:: path_list_esi
                                
                                	ESI Path List
                                	**type**\:  :py:class:`PathListEsi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.Macs.Mac.Route.EvpnEsi.PathList.PathListInfo.PathListEsi>`
                                
                                	**config**\: False
                                
                                .. attribute:: path_list_mac
                                
                                	MAC Path List
                                	**type**\:  :py:class:`PathListMac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.Macs.Mac.Route.EvpnEsi.PathList.PathListInfo.PathListMac>`
                                
                                	**config**\: False
                                
                                .. attribute:: type
                                
                                	Type
                                	**type**\:  :py:class:`L2ribMacRoute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2ribMacRoute>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'l2rib-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(L2rib.EviChildTables.Macs.Mac.Route.EvpnEsi.PathList.PathListInfo, self).__init__()

                                    self.yang_name = "path-list-info"
                                    self.yang_parent_name = "path-list"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = False
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("path-list-esi", ("path_list_esi", L2rib.EviChildTables.Macs.Mac.Route.EvpnEsi.PathList.PathListInfo.PathListEsi)), ("path-list-mac", ("path_list_mac", L2rib.EviChildTables.Macs.Mac.Route.EvpnEsi.PathList.PathListInfo.PathListMac))])
                                    self._leafs = OrderedDict([
                                        ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper', 'L2ribMacRoute', '')])),
                                    ])
                                    self.type = None

                                    self.path_list_esi = L2rib.EviChildTables.Macs.Mac.Route.EvpnEsi.PathList.PathListInfo.PathListEsi()
                                    self.path_list_esi.parent = self
                                    self._children_name_map["path_list_esi"] = "path-list-esi"

                                    self.path_list_mac = L2rib.EviChildTables.Macs.Mac.Route.EvpnEsi.PathList.PathListInfo.PathListMac()
                                    self.path_list_mac.parent = self
                                    self._children_name_map["path_list_mac"] = "path-list-mac"
                                    self._segment_path = lambda: "path-list-info"
                                    self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/macs/mac/route/evpn-esi/path-list/%s" % self._segment_path()
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2rib.EviChildTables.Macs.Mac.Route.EvpnEsi.PathList.PathListInfo, ['type'], name, value)


                                class PathListEsi(_Entity_):
                                    """
                                    ESI Path List
                                    
                                    .. attribute:: ethernet_segment_id
                                    
                                    	Ethernet Segment Identifier
                                    	**type**\:  :py:class:`EthernetSegmentId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.Macs.Mac.Route.EvpnEsi.PathList.PathListInfo.PathListEsi.EthernetSegmentId>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: resolved
                                    
                                    	Path list Resolved
                                    	**type**\: bool
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: mac_update_next_hop_array
                                    
                                    	Array of Next Hops from MAC Update
                                    	**type**\: list of  		 :py:class:`MacUpdateNextHopArray <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.Macs.Mac.Route.EvpnEsi.PathList.PathListInfo.PathListEsi.MacUpdateNextHopArray>`
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'l2rib-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(L2rib.EviChildTables.Macs.Mac.Route.EvpnEsi.PathList.PathListInfo.PathListEsi, self).__init__()

                                        self.yang_name = "path-list-esi"
                                        self.yang_parent_name = "path-list-info"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = False
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("ethernet-segment-id", ("ethernet_segment_id", L2rib.EviChildTables.Macs.Mac.Route.EvpnEsi.PathList.PathListInfo.PathListEsi.EthernetSegmentId)), ("mac-update-next-hop-array", ("mac_update_next_hop_array", L2rib.EviChildTables.Macs.Mac.Route.EvpnEsi.PathList.PathListInfo.PathListEsi.MacUpdateNextHopArray))])
                                        self._leafs = OrderedDict([
                                            ('resolved', (YLeaf(YType.boolean, 'resolved'), ['bool'])),
                                        ])
                                        self.resolved = None

                                        self.ethernet_segment_id = L2rib.EviChildTables.Macs.Mac.Route.EvpnEsi.PathList.PathListInfo.PathListEsi.EthernetSegmentId()
                                        self.ethernet_segment_id.parent = self
                                        self._children_name_map["ethernet_segment_id"] = "ethernet-segment-id"

                                        self.mac_update_next_hop_array = YList(self)
                                        self._segment_path = lambda: "path-list-esi"
                                        self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/macs/mac/route/evpn-esi/path-list/path-list-info/%s" % self._segment_path()
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(L2rib.EviChildTables.Macs.Mac.Route.EvpnEsi.PathList.PathListInfo.PathListEsi, ['resolved'], name, value)


                                    class EthernetSegmentId(_Entity_):
                                        """
                                        Ethernet Segment Identifier
                                        
                                        .. attribute:: system_priority
                                        
                                        	LACP System Priority
                                        	**type**\: int
                                        
                                        	**range:** 0..65535
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: system_id
                                        
                                        	LACP System Id
                                        	**type**\: str
                                        
                                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: port_key
                                        
                                        	LACP Port Key
                                        	**type**\: int
                                        
                                        	**range:** 0..65535
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'l2rib-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(L2rib.EviChildTables.Macs.Mac.Route.EvpnEsi.PathList.PathListInfo.PathListEsi.EthernetSegmentId, self).__init__()

                                            self.yang_name = "ethernet-segment-id"
                                            self.yang_parent_name = "path-list-esi"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = False
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('system_priority', (YLeaf(YType.uint16, 'system-priority'), ['int'])),
                                                ('system_id', (YLeaf(YType.str, 'system-id'), ['str'])),
                                                ('port_key', (YLeaf(YType.uint16, 'port-key'), ['int'])),
                                            ])
                                            self.system_priority = None
                                            self.system_id = None
                                            self.port_key = None
                                            self._segment_path = lambda: "ethernet-segment-id"
                                            self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/macs/mac/route/evpn-esi/path-list/path-list-info/path-list-esi/%s" % self._segment_path()
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2rib.EviChildTables.Macs.Mac.Route.EvpnEsi.PathList.PathListInfo.PathListEsi.EthernetSegmentId, ['system_priority', 'system_id', 'port_key'], name, value)

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                                            return meta._meta_table['L2rib.EviChildTables.Macs.Mac.Route.EvpnEsi.PathList.PathListInfo.PathListEsi.EthernetSegmentId']['meta_info']


                                    class MacUpdateNextHopArray(_Entity_):
                                        """
                                        Array of Next Hops from MAC Update
                                        
                                        .. attribute:: next_hop
                                        
                                        	Next hop
                                        	**type**\:  :py:class:`NextHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.Macs.Mac.Route.EvpnEsi.PathList.PathListInfo.PathListEsi.MacUpdateNextHopArray.NextHop>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: topology_id
                                        
                                        	Next\-hop TOPOLOGY ID
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: flags
                                        
                                        	Next\-hop flags
                                        	**type**\: int
                                        
                                        	**range:** 0..65535
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'l2rib-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(L2rib.EviChildTables.Macs.Mac.Route.EvpnEsi.PathList.PathListInfo.PathListEsi.MacUpdateNextHopArray, self).__init__()

                                            self.yang_name = "mac-update-next-hop-array"
                                            self.yang_parent_name = "path-list-esi"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = False
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("next-hop", ("next_hop", L2rib.EviChildTables.Macs.Mac.Route.EvpnEsi.PathList.PathListInfo.PathListEsi.MacUpdateNextHopArray.NextHop))])
                                            self._leafs = OrderedDict([
                                                ('topology_id', (YLeaf(YType.uint32, 'topology-id'), ['int'])),
                                                ('flags', (YLeaf(YType.uint16, 'flags'), ['int'])),
                                            ])
                                            self.topology_id = None
                                            self.flags = None

                                            self.next_hop = L2rib.EviChildTables.Macs.Mac.Route.EvpnEsi.PathList.PathListInfo.PathListEsi.MacUpdateNextHopArray.NextHop()
                                            self.next_hop.parent = self
                                            self._children_name_map["next_hop"] = "next-hop"
                                            self._segment_path = lambda: "mac-update-next-hop-array"
                                            self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/macs/mac/route/evpn-esi/path-list/path-list-info/path-list-esi/%s" % self._segment_path()
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2rib.EviChildTables.Macs.Mac.Route.EvpnEsi.PathList.PathListInfo.PathListEsi.MacUpdateNextHopArray, ['topology_id', 'flags'], name, value)


                                        class NextHop(_Entity_):
                                            """
                                            Next hop
                                            
                                            .. attribute:: labeled
                                            
                                            	Labeled Next Hop
                                            	**type**\:  :py:class:`Labeled <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.Macs.Mac.Route.EvpnEsi.PathList.PathListInfo.PathListEsi.MacUpdateNextHopArray.NextHop.Labeled>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: type
                                            
                                            	Type
                                            	**type**\:  :py:class:`L2ribNextHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2ribNextHop>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: ipv4
                                            
                                            	IPV4 address Next Hop
                                            	**type**\: str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: ipv6
                                            
                                            	IPV6 address Next Hop
                                            	**type**\: str
                                            
                                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: mac
                                            
                                            	MAC address Next Hop
                                            	**type**\: str
                                            
                                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: interface_handle
                                            
                                            	Intefrace Handle Next Hop
                                            	**type**\: str
                                            
                                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: xid
                                            
                                            	XID Next Hop
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'l2rib-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(L2rib.EviChildTables.Macs.Mac.Route.EvpnEsi.PathList.PathListInfo.PathListEsi.MacUpdateNextHopArray.NextHop, self).__init__()

                                                self.yang_name = "next-hop"
                                                self.yang_parent_name = "mac-update-next-hop-array"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = False
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([("labeled", ("labeled", L2rib.EviChildTables.Macs.Mac.Route.EvpnEsi.PathList.PathListInfo.PathListEsi.MacUpdateNextHopArray.NextHop.Labeled))])
                                                self._leafs = OrderedDict([
                                                    ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper', 'L2ribNextHop', '')])),
                                                    ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                                                    ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                                                    ('mac', (YLeaf(YType.str, 'mac'), ['str'])),
                                                    ('interface_handle', (YLeaf(YType.str, 'interface-handle'), ['str'])),
                                                    ('xid', (YLeaf(YType.uint32, 'xid'), ['int'])),
                                                ])
                                                self.type = None
                                                self.ipv4 = None
                                                self.ipv6 = None
                                                self.mac = None
                                                self.interface_handle = None
                                                self.xid = None

                                                self.labeled = L2rib.EviChildTables.Macs.Mac.Route.EvpnEsi.PathList.PathListInfo.PathListEsi.MacUpdateNextHopArray.NextHop.Labeled()
                                                self.labeled.parent = self
                                                self._children_name_map["labeled"] = "labeled"
                                                self._segment_path = lambda: "next-hop"
                                                self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/macs/mac/route/evpn-esi/path-list/path-list-info/path-list-esi/mac-update-next-hop-array/%s" % self._segment_path()
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(L2rib.EviChildTables.Macs.Mac.Route.EvpnEsi.PathList.PathListInfo.PathListEsi.MacUpdateNextHopArray.NextHop, ['type', 'ipv4', 'ipv6', 'mac', 'interface_handle', 'xid'], name, value)


                                            class Labeled(_Entity_):
                                                """
                                                Labeled Next Hop
                                                
                                                .. attribute:: address_family
                                                
                                                	L2RIB Address Family
                                                	**type**\:  :py:class:`L2ribAfi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2ribAfi>`
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: ip_address
                                                
                                                	IP Address
                                                	**type**\: str
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: label
                                                
                                                	Label
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: internal
                                                
                                                	Internal Label
                                                	**type**\: bool
                                                
                                                	**config**\: False
                                                
                                                

                                                """

                                                _prefix = 'l2rib-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    if sys.version_info > (3,):
                                                        super().__init__()
                                                    else:
                                                        super(L2rib.EviChildTables.Macs.Mac.Route.EvpnEsi.PathList.PathListInfo.PathListEsi.MacUpdateNextHopArray.NextHop.Labeled, self).__init__()

                                                    self.yang_name = "labeled"
                                                    self.yang_parent_name = "next-hop"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = False
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('address_family', (YLeaf(YType.enumeration, 'address-family'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper', 'L2ribAfi', '')])),
                                                        ('ip_address', (YLeaf(YType.str, 'ip-address'), ['str'])),
                                                        ('label', (YLeaf(YType.uint32, 'label'), ['int'])),
                                                        ('internal', (YLeaf(YType.boolean, 'internal'), ['bool'])),
                                                    ])
                                                    self.address_family = None
                                                    self.ip_address = None
                                                    self.label = None
                                                    self.internal = None
                                                    self._segment_path = lambda: "labeled"
                                                    self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/macs/mac/route/evpn-esi/path-list/path-list-info/path-list-esi/mac-update-next-hop-array/next-hop/%s" % self._segment_path()
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(L2rib.EviChildTables.Macs.Mac.Route.EvpnEsi.PathList.PathListInfo.PathListEsi.MacUpdateNextHopArray.NextHop.Labeled, ['address_family', 'ip_address', 'label', 'internal'], name, value)

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                                                    return meta._meta_table['L2rib.EviChildTables.Macs.Mac.Route.EvpnEsi.PathList.PathListInfo.PathListEsi.MacUpdateNextHopArray.NextHop.Labeled']['meta_info']

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                                                return meta._meta_table['L2rib.EviChildTables.Macs.Mac.Route.EvpnEsi.PathList.PathListInfo.PathListEsi.MacUpdateNextHopArray.NextHop']['meta_info']

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                                            return meta._meta_table['L2rib.EviChildTables.Macs.Mac.Route.EvpnEsi.PathList.PathListInfo.PathListEsi.MacUpdateNextHopArray']['meta_info']

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                                        return meta._meta_table['L2rib.EviChildTables.Macs.Mac.Route.EvpnEsi.PathList.PathListInfo.PathListEsi']['meta_info']


                                class PathListMac(_Entity_):
                                    """
                                    MAC Path List
                                    
                                    .. attribute:: mac_address
                                    
                                    	MAC Address
                                    	**type**\: str
                                    
                                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'l2rib-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(L2rib.EviChildTables.Macs.Mac.Route.EvpnEsi.PathList.PathListInfo.PathListMac, self).__init__()

                                        self.yang_name = "path-list-mac"
                                        self.yang_parent_name = "path-list-info"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = False
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('mac_address', (YLeaf(YType.str, 'mac-address'), ['str'])),
                                        ])
                                        self.mac_address = None
                                        self._segment_path = lambda: "path-list-mac"
                                        self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/macs/mac/route/evpn-esi/path-list/path-list-info/%s" % self._segment_path()
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(L2rib.EviChildTables.Macs.Mac.Route.EvpnEsi.PathList.PathListInfo.PathListMac, ['mac_address'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                                        return meta._meta_table['L2rib.EviChildTables.Macs.Mac.Route.EvpnEsi.PathList.PathListInfo.PathListMac']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                                    return meta._meta_table['L2rib.EviChildTables.Macs.Mac.Route.EvpnEsi.PathList.PathListInfo']['meta_info']


                            class NextHopArray(_Entity_):
                                """
                                Array of Next Hops for MAC Path List
                                
                                .. attribute:: next_hop
                                
                                	Next hop
                                	**type**\:  :py:class:`NextHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.Macs.Mac.Route.EvpnEsi.PathList.NextHopArray.NextHop>`
                                
                                	**config**\: False
                                
                                .. attribute:: topology_id
                                
                                	Next\-hop TOPOLOGY ID
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: flags
                                
                                	Next\-hop flags
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'l2rib-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(L2rib.EviChildTables.Macs.Mac.Route.EvpnEsi.PathList.NextHopArray, self).__init__()

                                    self.yang_name = "next-hop-array"
                                    self.yang_parent_name = "path-list"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = False
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("next-hop", ("next_hop", L2rib.EviChildTables.Macs.Mac.Route.EvpnEsi.PathList.NextHopArray.NextHop))])
                                    self._leafs = OrderedDict([
                                        ('topology_id', (YLeaf(YType.uint32, 'topology-id'), ['int'])),
                                        ('flags', (YLeaf(YType.uint16, 'flags'), ['int'])),
                                    ])
                                    self.topology_id = None
                                    self.flags = None

                                    self.next_hop = L2rib.EviChildTables.Macs.Mac.Route.EvpnEsi.PathList.NextHopArray.NextHop()
                                    self.next_hop.parent = self
                                    self._children_name_map["next_hop"] = "next-hop"
                                    self._segment_path = lambda: "next-hop-array"
                                    self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/macs/mac/route/evpn-esi/path-list/%s" % self._segment_path()
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2rib.EviChildTables.Macs.Mac.Route.EvpnEsi.PathList.NextHopArray, ['topology_id', 'flags'], name, value)


                                class NextHop(_Entity_):
                                    """
                                    Next hop
                                    
                                    .. attribute:: labeled
                                    
                                    	Labeled Next Hop
                                    	**type**\:  :py:class:`Labeled <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.Macs.Mac.Route.EvpnEsi.PathList.NextHopArray.NextHop.Labeled>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: type
                                    
                                    	Type
                                    	**type**\:  :py:class:`L2ribNextHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2ribNextHop>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: ipv4
                                    
                                    	IPV4 address Next Hop
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: ipv6
                                    
                                    	IPV6 address Next Hop
                                    	**type**\: str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: mac
                                    
                                    	MAC address Next Hop
                                    	**type**\: str
                                    
                                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: interface_handle
                                    
                                    	Intefrace Handle Next Hop
                                    	**type**\: str
                                    
                                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: xid
                                    
                                    	XID Next Hop
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'l2rib-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(L2rib.EviChildTables.Macs.Mac.Route.EvpnEsi.PathList.NextHopArray.NextHop, self).__init__()

                                        self.yang_name = "next-hop"
                                        self.yang_parent_name = "next-hop-array"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = False
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("labeled", ("labeled", L2rib.EviChildTables.Macs.Mac.Route.EvpnEsi.PathList.NextHopArray.NextHop.Labeled))])
                                        self._leafs = OrderedDict([
                                            ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper', 'L2ribNextHop', '')])),
                                            ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                                            ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                                            ('mac', (YLeaf(YType.str, 'mac'), ['str'])),
                                            ('interface_handle', (YLeaf(YType.str, 'interface-handle'), ['str'])),
                                            ('xid', (YLeaf(YType.uint32, 'xid'), ['int'])),
                                        ])
                                        self.type = None
                                        self.ipv4 = None
                                        self.ipv6 = None
                                        self.mac = None
                                        self.interface_handle = None
                                        self.xid = None

                                        self.labeled = L2rib.EviChildTables.Macs.Mac.Route.EvpnEsi.PathList.NextHopArray.NextHop.Labeled()
                                        self.labeled.parent = self
                                        self._children_name_map["labeled"] = "labeled"
                                        self._segment_path = lambda: "next-hop"
                                        self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/macs/mac/route/evpn-esi/path-list/next-hop-array/%s" % self._segment_path()
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(L2rib.EviChildTables.Macs.Mac.Route.EvpnEsi.PathList.NextHopArray.NextHop, ['type', 'ipv4', 'ipv6', 'mac', 'interface_handle', 'xid'], name, value)


                                    class Labeled(_Entity_):
                                        """
                                        Labeled Next Hop
                                        
                                        .. attribute:: address_family
                                        
                                        	L2RIB Address Family
                                        	**type**\:  :py:class:`L2ribAfi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2ribAfi>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: ip_address
                                        
                                        	IP Address
                                        	**type**\: str
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: label
                                        
                                        	Label
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: internal
                                        
                                        	Internal Label
                                        	**type**\: bool
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'l2rib-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(L2rib.EviChildTables.Macs.Mac.Route.EvpnEsi.PathList.NextHopArray.NextHop.Labeled, self).__init__()

                                            self.yang_name = "labeled"
                                            self.yang_parent_name = "next-hop"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = False
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('address_family', (YLeaf(YType.enumeration, 'address-family'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper', 'L2ribAfi', '')])),
                                                ('ip_address', (YLeaf(YType.str, 'ip-address'), ['str'])),
                                                ('label', (YLeaf(YType.uint32, 'label'), ['int'])),
                                                ('internal', (YLeaf(YType.boolean, 'internal'), ['bool'])),
                                            ])
                                            self.address_family = None
                                            self.ip_address = None
                                            self.label = None
                                            self.internal = None
                                            self._segment_path = lambda: "labeled"
                                            self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/macs/mac/route/evpn-esi/path-list/next-hop-array/next-hop/%s" % self._segment_path()
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2rib.EviChildTables.Macs.Mac.Route.EvpnEsi.PathList.NextHopArray.NextHop.Labeled, ['address_family', 'ip_address', 'label', 'internal'], name, value)

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                                            return meta._meta_table['L2rib.EviChildTables.Macs.Mac.Route.EvpnEsi.PathList.NextHopArray.NextHop.Labeled']['meta_info']

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                                        return meta._meta_table['L2rib.EviChildTables.Macs.Mac.Route.EvpnEsi.PathList.NextHopArray.NextHop']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                                    return meta._meta_table['L2rib.EviChildTables.Macs.Mac.Route.EvpnEsi.PathList.NextHopArray']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                                return meta._meta_table['L2rib.EviChildTables.Macs.Mac.Route.EvpnEsi.PathList']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                            return meta._meta_table['L2rib.EviChildTables.Macs.Mac.Route.EvpnEsi']['meta_info']


                    class Bmac(_Entity_):
                        """
                        BMAC route
                        
                        .. attribute:: path_list
                        
                        	Path list information
                        	**type**\:  :py:class:`PathList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.Macs.Mac.Route.Bmac.PathList>`
                        
                        	**config**\: False
                        
                        .. attribute:: bmac_address
                        
                        	BMAC Address
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        	**config**\: False
                        
                        .. attribute:: forward_state
                        
                        	Forwarding State. True means forward, False means drop
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'l2rib-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(L2rib.EviChildTables.Macs.Mac.Route.Bmac, self).__init__()

                            self.yang_name = "bmac"
                            self.yang_parent_name = "route"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("path-list", ("path_list", L2rib.EviChildTables.Macs.Mac.Route.Bmac.PathList))])
                            self._leafs = OrderedDict([
                                ('bmac_address', (YLeaf(YType.str, 'bmac-address'), ['str'])),
                                ('forward_state', (YLeaf(YType.boolean, 'forward-state'), ['bool'])),
                            ])
                            self.bmac_address = None
                            self.forward_state = None

                            self.path_list = L2rib.EviChildTables.Macs.Mac.Route.Bmac.PathList()
                            self.path_list.parent = self
                            self._children_name_map["path_list"] = "path-list"
                            self._segment_path = lambda: "bmac"
                            self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/macs/mac/route/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2rib.EviChildTables.Macs.Mac.Route.Bmac, ['bmac_address', 'forward_state'], name, value)


                        class PathList(_Entity_):
                            """
                            Path list information
                            
                            .. attribute:: path_list_info
                            
                            	Type\-specific Path List info
                            	**type**\:  :py:class:`PathListInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.Macs.Mac.Route.Bmac.PathList.PathListInfo>`
                            
                            	**config**\: False
                            
                            .. attribute:: producer_id
                            
                            	ID of EAD route producer
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            .. attribute:: mac_count
                            
                            	Number of MAC routes bound to this Path list
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: local_label
                            
                            	Path list local Label
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: next_hop_array
                            
                            	Array of Next Hops for MAC Path List
                            	**type**\: list of  		 :py:class:`NextHopArray <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.Macs.Mac.Route.Bmac.PathList.NextHopArray>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'l2rib-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(L2rib.EviChildTables.Macs.Mac.Route.Bmac.PathList, self).__init__()

                                self.yang_name = "path-list"
                                self.yang_parent_name = "bmac"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("path-list-info", ("path_list_info", L2rib.EviChildTables.Macs.Mac.Route.Bmac.PathList.PathListInfo)), ("next-hop-array", ("next_hop_array", L2rib.EviChildTables.Macs.Mac.Route.Bmac.PathList.NextHopArray))])
                                self._leafs = OrderedDict([
                                    ('producer_id', (YLeaf(YType.uint8, 'producer-id'), ['int'])),
                                    ('mac_count', (YLeaf(YType.uint32, 'mac-count'), ['int'])),
                                    ('local_label', (YLeaf(YType.uint32, 'local-label'), ['int'])),
                                ])
                                self.producer_id = None
                                self.mac_count = None
                                self.local_label = None

                                self.path_list_info = L2rib.EviChildTables.Macs.Mac.Route.Bmac.PathList.PathListInfo()
                                self.path_list_info.parent = self
                                self._children_name_map["path_list_info"] = "path-list-info"

                                self.next_hop_array = YList(self)
                                self._segment_path = lambda: "path-list"
                                self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/macs/mac/route/bmac/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2rib.EviChildTables.Macs.Mac.Route.Bmac.PathList, ['producer_id', 'mac_count', 'local_label'], name, value)


                            class PathListInfo(_Entity_):
                                """
                                Type\-specific Path List info
                                
                                .. attribute:: path_list_esi
                                
                                	ESI Path List
                                	**type**\:  :py:class:`PathListEsi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.Macs.Mac.Route.Bmac.PathList.PathListInfo.PathListEsi>`
                                
                                	**config**\: False
                                
                                .. attribute:: path_list_mac
                                
                                	MAC Path List
                                	**type**\:  :py:class:`PathListMac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.Macs.Mac.Route.Bmac.PathList.PathListInfo.PathListMac>`
                                
                                	**config**\: False
                                
                                .. attribute:: type
                                
                                	Type
                                	**type**\:  :py:class:`L2ribMacRoute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2ribMacRoute>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'l2rib-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(L2rib.EviChildTables.Macs.Mac.Route.Bmac.PathList.PathListInfo, self).__init__()

                                    self.yang_name = "path-list-info"
                                    self.yang_parent_name = "path-list"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = False
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("path-list-esi", ("path_list_esi", L2rib.EviChildTables.Macs.Mac.Route.Bmac.PathList.PathListInfo.PathListEsi)), ("path-list-mac", ("path_list_mac", L2rib.EviChildTables.Macs.Mac.Route.Bmac.PathList.PathListInfo.PathListMac))])
                                    self._leafs = OrderedDict([
                                        ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper', 'L2ribMacRoute', '')])),
                                    ])
                                    self.type = None

                                    self.path_list_esi = L2rib.EviChildTables.Macs.Mac.Route.Bmac.PathList.PathListInfo.PathListEsi()
                                    self.path_list_esi.parent = self
                                    self._children_name_map["path_list_esi"] = "path-list-esi"

                                    self.path_list_mac = L2rib.EviChildTables.Macs.Mac.Route.Bmac.PathList.PathListInfo.PathListMac()
                                    self.path_list_mac.parent = self
                                    self._children_name_map["path_list_mac"] = "path-list-mac"
                                    self._segment_path = lambda: "path-list-info"
                                    self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/macs/mac/route/bmac/path-list/%s" % self._segment_path()
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2rib.EviChildTables.Macs.Mac.Route.Bmac.PathList.PathListInfo, ['type'], name, value)


                                class PathListEsi(_Entity_):
                                    """
                                    ESI Path List
                                    
                                    .. attribute:: ethernet_segment_id
                                    
                                    	Ethernet Segment Identifier
                                    	**type**\:  :py:class:`EthernetSegmentId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.Macs.Mac.Route.Bmac.PathList.PathListInfo.PathListEsi.EthernetSegmentId>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: resolved
                                    
                                    	Path list Resolved
                                    	**type**\: bool
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: mac_update_next_hop_array
                                    
                                    	Array of Next Hops from MAC Update
                                    	**type**\: list of  		 :py:class:`MacUpdateNextHopArray <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.Macs.Mac.Route.Bmac.PathList.PathListInfo.PathListEsi.MacUpdateNextHopArray>`
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'l2rib-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(L2rib.EviChildTables.Macs.Mac.Route.Bmac.PathList.PathListInfo.PathListEsi, self).__init__()

                                        self.yang_name = "path-list-esi"
                                        self.yang_parent_name = "path-list-info"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = False
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("ethernet-segment-id", ("ethernet_segment_id", L2rib.EviChildTables.Macs.Mac.Route.Bmac.PathList.PathListInfo.PathListEsi.EthernetSegmentId)), ("mac-update-next-hop-array", ("mac_update_next_hop_array", L2rib.EviChildTables.Macs.Mac.Route.Bmac.PathList.PathListInfo.PathListEsi.MacUpdateNextHopArray))])
                                        self._leafs = OrderedDict([
                                            ('resolved', (YLeaf(YType.boolean, 'resolved'), ['bool'])),
                                        ])
                                        self.resolved = None

                                        self.ethernet_segment_id = L2rib.EviChildTables.Macs.Mac.Route.Bmac.PathList.PathListInfo.PathListEsi.EthernetSegmentId()
                                        self.ethernet_segment_id.parent = self
                                        self._children_name_map["ethernet_segment_id"] = "ethernet-segment-id"

                                        self.mac_update_next_hop_array = YList(self)
                                        self._segment_path = lambda: "path-list-esi"
                                        self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/macs/mac/route/bmac/path-list/path-list-info/%s" % self._segment_path()
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(L2rib.EviChildTables.Macs.Mac.Route.Bmac.PathList.PathListInfo.PathListEsi, ['resolved'], name, value)


                                    class EthernetSegmentId(_Entity_):
                                        """
                                        Ethernet Segment Identifier
                                        
                                        .. attribute:: system_priority
                                        
                                        	LACP System Priority
                                        	**type**\: int
                                        
                                        	**range:** 0..65535
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: system_id
                                        
                                        	LACP System Id
                                        	**type**\: str
                                        
                                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: port_key
                                        
                                        	LACP Port Key
                                        	**type**\: int
                                        
                                        	**range:** 0..65535
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'l2rib-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(L2rib.EviChildTables.Macs.Mac.Route.Bmac.PathList.PathListInfo.PathListEsi.EthernetSegmentId, self).__init__()

                                            self.yang_name = "ethernet-segment-id"
                                            self.yang_parent_name = "path-list-esi"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = False
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('system_priority', (YLeaf(YType.uint16, 'system-priority'), ['int'])),
                                                ('system_id', (YLeaf(YType.str, 'system-id'), ['str'])),
                                                ('port_key', (YLeaf(YType.uint16, 'port-key'), ['int'])),
                                            ])
                                            self.system_priority = None
                                            self.system_id = None
                                            self.port_key = None
                                            self._segment_path = lambda: "ethernet-segment-id"
                                            self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/macs/mac/route/bmac/path-list/path-list-info/path-list-esi/%s" % self._segment_path()
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2rib.EviChildTables.Macs.Mac.Route.Bmac.PathList.PathListInfo.PathListEsi.EthernetSegmentId, ['system_priority', 'system_id', 'port_key'], name, value)

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                                            return meta._meta_table['L2rib.EviChildTables.Macs.Mac.Route.Bmac.PathList.PathListInfo.PathListEsi.EthernetSegmentId']['meta_info']


                                    class MacUpdateNextHopArray(_Entity_):
                                        """
                                        Array of Next Hops from MAC Update
                                        
                                        .. attribute:: next_hop
                                        
                                        	Next hop
                                        	**type**\:  :py:class:`NextHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.Macs.Mac.Route.Bmac.PathList.PathListInfo.PathListEsi.MacUpdateNextHopArray.NextHop>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: topology_id
                                        
                                        	Next\-hop TOPOLOGY ID
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: flags
                                        
                                        	Next\-hop flags
                                        	**type**\: int
                                        
                                        	**range:** 0..65535
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'l2rib-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(L2rib.EviChildTables.Macs.Mac.Route.Bmac.PathList.PathListInfo.PathListEsi.MacUpdateNextHopArray, self).__init__()

                                            self.yang_name = "mac-update-next-hop-array"
                                            self.yang_parent_name = "path-list-esi"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = False
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("next-hop", ("next_hop", L2rib.EviChildTables.Macs.Mac.Route.Bmac.PathList.PathListInfo.PathListEsi.MacUpdateNextHopArray.NextHop))])
                                            self._leafs = OrderedDict([
                                                ('topology_id', (YLeaf(YType.uint32, 'topology-id'), ['int'])),
                                                ('flags', (YLeaf(YType.uint16, 'flags'), ['int'])),
                                            ])
                                            self.topology_id = None
                                            self.flags = None

                                            self.next_hop = L2rib.EviChildTables.Macs.Mac.Route.Bmac.PathList.PathListInfo.PathListEsi.MacUpdateNextHopArray.NextHop()
                                            self.next_hop.parent = self
                                            self._children_name_map["next_hop"] = "next-hop"
                                            self._segment_path = lambda: "mac-update-next-hop-array"
                                            self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/macs/mac/route/bmac/path-list/path-list-info/path-list-esi/%s" % self._segment_path()
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2rib.EviChildTables.Macs.Mac.Route.Bmac.PathList.PathListInfo.PathListEsi.MacUpdateNextHopArray, ['topology_id', 'flags'], name, value)


                                        class NextHop(_Entity_):
                                            """
                                            Next hop
                                            
                                            .. attribute:: labeled
                                            
                                            	Labeled Next Hop
                                            	**type**\:  :py:class:`Labeled <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.Macs.Mac.Route.Bmac.PathList.PathListInfo.PathListEsi.MacUpdateNextHopArray.NextHop.Labeled>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: type
                                            
                                            	Type
                                            	**type**\:  :py:class:`L2ribNextHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2ribNextHop>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: ipv4
                                            
                                            	IPV4 address Next Hop
                                            	**type**\: str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: ipv6
                                            
                                            	IPV6 address Next Hop
                                            	**type**\: str
                                            
                                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: mac
                                            
                                            	MAC address Next Hop
                                            	**type**\: str
                                            
                                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: interface_handle
                                            
                                            	Intefrace Handle Next Hop
                                            	**type**\: str
                                            
                                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: xid
                                            
                                            	XID Next Hop
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'l2rib-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(L2rib.EviChildTables.Macs.Mac.Route.Bmac.PathList.PathListInfo.PathListEsi.MacUpdateNextHopArray.NextHop, self).__init__()

                                                self.yang_name = "next-hop"
                                                self.yang_parent_name = "mac-update-next-hop-array"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = False
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([("labeled", ("labeled", L2rib.EviChildTables.Macs.Mac.Route.Bmac.PathList.PathListInfo.PathListEsi.MacUpdateNextHopArray.NextHop.Labeled))])
                                                self._leafs = OrderedDict([
                                                    ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper', 'L2ribNextHop', '')])),
                                                    ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                                                    ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                                                    ('mac', (YLeaf(YType.str, 'mac'), ['str'])),
                                                    ('interface_handle', (YLeaf(YType.str, 'interface-handle'), ['str'])),
                                                    ('xid', (YLeaf(YType.uint32, 'xid'), ['int'])),
                                                ])
                                                self.type = None
                                                self.ipv4 = None
                                                self.ipv6 = None
                                                self.mac = None
                                                self.interface_handle = None
                                                self.xid = None

                                                self.labeled = L2rib.EviChildTables.Macs.Mac.Route.Bmac.PathList.PathListInfo.PathListEsi.MacUpdateNextHopArray.NextHop.Labeled()
                                                self.labeled.parent = self
                                                self._children_name_map["labeled"] = "labeled"
                                                self._segment_path = lambda: "next-hop"
                                                self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/macs/mac/route/bmac/path-list/path-list-info/path-list-esi/mac-update-next-hop-array/%s" % self._segment_path()
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(L2rib.EviChildTables.Macs.Mac.Route.Bmac.PathList.PathListInfo.PathListEsi.MacUpdateNextHopArray.NextHop, ['type', 'ipv4', 'ipv6', 'mac', 'interface_handle', 'xid'], name, value)


                                            class Labeled(_Entity_):
                                                """
                                                Labeled Next Hop
                                                
                                                .. attribute:: address_family
                                                
                                                	L2RIB Address Family
                                                	**type**\:  :py:class:`L2ribAfi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2ribAfi>`
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: ip_address
                                                
                                                	IP Address
                                                	**type**\: str
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: label
                                                
                                                	Label
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: internal
                                                
                                                	Internal Label
                                                	**type**\: bool
                                                
                                                	**config**\: False
                                                
                                                

                                                """

                                                _prefix = 'l2rib-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    if sys.version_info > (3,):
                                                        super().__init__()
                                                    else:
                                                        super(L2rib.EviChildTables.Macs.Mac.Route.Bmac.PathList.PathListInfo.PathListEsi.MacUpdateNextHopArray.NextHop.Labeled, self).__init__()

                                                    self.yang_name = "labeled"
                                                    self.yang_parent_name = "next-hop"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = False
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('address_family', (YLeaf(YType.enumeration, 'address-family'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper', 'L2ribAfi', '')])),
                                                        ('ip_address', (YLeaf(YType.str, 'ip-address'), ['str'])),
                                                        ('label', (YLeaf(YType.uint32, 'label'), ['int'])),
                                                        ('internal', (YLeaf(YType.boolean, 'internal'), ['bool'])),
                                                    ])
                                                    self.address_family = None
                                                    self.ip_address = None
                                                    self.label = None
                                                    self.internal = None
                                                    self._segment_path = lambda: "labeled"
                                                    self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/macs/mac/route/bmac/path-list/path-list-info/path-list-esi/mac-update-next-hop-array/next-hop/%s" % self._segment_path()
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(L2rib.EviChildTables.Macs.Mac.Route.Bmac.PathList.PathListInfo.PathListEsi.MacUpdateNextHopArray.NextHop.Labeled, ['address_family', 'ip_address', 'label', 'internal'], name, value)

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                                                    return meta._meta_table['L2rib.EviChildTables.Macs.Mac.Route.Bmac.PathList.PathListInfo.PathListEsi.MacUpdateNextHopArray.NextHop.Labeled']['meta_info']

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                                                return meta._meta_table['L2rib.EviChildTables.Macs.Mac.Route.Bmac.PathList.PathListInfo.PathListEsi.MacUpdateNextHopArray.NextHop']['meta_info']

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                                            return meta._meta_table['L2rib.EviChildTables.Macs.Mac.Route.Bmac.PathList.PathListInfo.PathListEsi.MacUpdateNextHopArray']['meta_info']

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                                        return meta._meta_table['L2rib.EviChildTables.Macs.Mac.Route.Bmac.PathList.PathListInfo.PathListEsi']['meta_info']


                                class PathListMac(_Entity_):
                                    """
                                    MAC Path List
                                    
                                    .. attribute:: mac_address
                                    
                                    	MAC Address
                                    	**type**\: str
                                    
                                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'l2rib-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(L2rib.EviChildTables.Macs.Mac.Route.Bmac.PathList.PathListInfo.PathListMac, self).__init__()

                                        self.yang_name = "path-list-mac"
                                        self.yang_parent_name = "path-list-info"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = False
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('mac_address', (YLeaf(YType.str, 'mac-address'), ['str'])),
                                        ])
                                        self.mac_address = None
                                        self._segment_path = lambda: "path-list-mac"
                                        self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/macs/mac/route/bmac/path-list/path-list-info/%s" % self._segment_path()
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(L2rib.EviChildTables.Macs.Mac.Route.Bmac.PathList.PathListInfo.PathListMac, ['mac_address'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                                        return meta._meta_table['L2rib.EviChildTables.Macs.Mac.Route.Bmac.PathList.PathListInfo.PathListMac']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                                    return meta._meta_table['L2rib.EviChildTables.Macs.Mac.Route.Bmac.PathList.PathListInfo']['meta_info']


                            class NextHopArray(_Entity_):
                                """
                                Array of Next Hops for MAC Path List
                                
                                .. attribute:: next_hop
                                
                                	Next hop
                                	**type**\:  :py:class:`NextHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.Macs.Mac.Route.Bmac.PathList.NextHopArray.NextHop>`
                                
                                	**config**\: False
                                
                                .. attribute:: topology_id
                                
                                	Next\-hop TOPOLOGY ID
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: flags
                                
                                	Next\-hop flags
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'l2rib-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(L2rib.EviChildTables.Macs.Mac.Route.Bmac.PathList.NextHopArray, self).__init__()

                                    self.yang_name = "next-hop-array"
                                    self.yang_parent_name = "path-list"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = False
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("next-hop", ("next_hop", L2rib.EviChildTables.Macs.Mac.Route.Bmac.PathList.NextHopArray.NextHop))])
                                    self._leafs = OrderedDict([
                                        ('topology_id', (YLeaf(YType.uint32, 'topology-id'), ['int'])),
                                        ('flags', (YLeaf(YType.uint16, 'flags'), ['int'])),
                                    ])
                                    self.topology_id = None
                                    self.flags = None

                                    self.next_hop = L2rib.EviChildTables.Macs.Mac.Route.Bmac.PathList.NextHopArray.NextHop()
                                    self.next_hop.parent = self
                                    self._children_name_map["next_hop"] = "next-hop"
                                    self._segment_path = lambda: "next-hop-array"
                                    self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/macs/mac/route/bmac/path-list/%s" % self._segment_path()
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2rib.EviChildTables.Macs.Mac.Route.Bmac.PathList.NextHopArray, ['topology_id', 'flags'], name, value)


                                class NextHop(_Entity_):
                                    """
                                    Next hop
                                    
                                    .. attribute:: labeled
                                    
                                    	Labeled Next Hop
                                    	**type**\:  :py:class:`Labeled <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.Macs.Mac.Route.Bmac.PathList.NextHopArray.NextHop.Labeled>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: type
                                    
                                    	Type
                                    	**type**\:  :py:class:`L2ribNextHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2ribNextHop>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: ipv4
                                    
                                    	IPV4 address Next Hop
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: ipv6
                                    
                                    	IPV6 address Next Hop
                                    	**type**\: str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: mac
                                    
                                    	MAC address Next Hop
                                    	**type**\: str
                                    
                                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: interface_handle
                                    
                                    	Intefrace Handle Next Hop
                                    	**type**\: str
                                    
                                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: xid
                                    
                                    	XID Next Hop
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'l2rib-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(L2rib.EviChildTables.Macs.Mac.Route.Bmac.PathList.NextHopArray.NextHop, self).__init__()

                                        self.yang_name = "next-hop"
                                        self.yang_parent_name = "next-hop-array"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = False
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("labeled", ("labeled", L2rib.EviChildTables.Macs.Mac.Route.Bmac.PathList.NextHopArray.NextHop.Labeled))])
                                        self._leafs = OrderedDict([
                                            ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper', 'L2ribNextHop', '')])),
                                            ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                                            ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                                            ('mac', (YLeaf(YType.str, 'mac'), ['str'])),
                                            ('interface_handle', (YLeaf(YType.str, 'interface-handle'), ['str'])),
                                            ('xid', (YLeaf(YType.uint32, 'xid'), ['int'])),
                                        ])
                                        self.type = None
                                        self.ipv4 = None
                                        self.ipv6 = None
                                        self.mac = None
                                        self.interface_handle = None
                                        self.xid = None

                                        self.labeled = L2rib.EviChildTables.Macs.Mac.Route.Bmac.PathList.NextHopArray.NextHop.Labeled()
                                        self.labeled.parent = self
                                        self._children_name_map["labeled"] = "labeled"
                                        self._segment_path = lambda: "next-hop"
                                        self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/macs/mac/route/bmac/path-list/next-hop-array/%s" % self._segment_path()
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(L2rib.EviChildTables.Macs.Mac.Route.Bmac.PathList.NextHopArray.NextHop, ['type', 'ipv4', 'ipv6', 'mac', 'interface_handle', 'xid'], name, value)


                                    class Labeled(_Entity_):
                                        """
                                        Labeled Next Hop
                                        
                                        .. attribute:: address_family
                                        
                                        	L2RIB Address Family
                                        	**type**\:  :py:class:`L2ribAfi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2ribAfi>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: ip_address
                                        
                                        	IP Address
                                        	**type**\: str
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: label
                                        
                                        	Label
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: internal
                                        
                                        	Internal Label
                                        	**type**\: bool
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'l2rib-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(L2rib.EviChildTables.Macs.Mac.Route.Bmac.PathList.NextHopArray.NextHop.Labeled, self).__init__()

                                            self.yang_name = "labeled"
                                            self.yang_parent_name = "next-hop"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = False
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('address_family', (YLeaf(YType.enumeration, 'address-family'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper', 'L2ribAfi', '')])),
                                                ('ip_address', (YLeaf(YType.str, 'ip-address'), ['str'])),
                                                ('label', (YLeaf(YType.uint32, 'label'), ['int'])),
                                                ('internal', (YLeaf(YType.boolean, 'internal'), ['bool'])),
                                            ])
                                            self.address_family = None
                                            self.ip_address = None
                                            self.label = None
                                            self.internal = None
                                            self._segment_path = lambda: "labeled"
                                            self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/macs/mac/route/bmac/path-list/next-hop-array/next-hop/%s" % self._segment_path()
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2rib.EviChildTables.Macs.Mac.Route.Bmac.PathList.NextHopArray.NextHop.Labeled, ['address_family', 'ip_address', 'label', 'internal'], name, value)

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                                            return meta._meta_table['L2rib.EviChildTables.Macs.Mac.Route.Bmac.PathList.NextHopArray.NextHop.Labeled']['meta_info']

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                                        return meta._meta_table['L2rib.EviChildTables.Macs.Mac.Route.Bmac.PathList.NextHopArray.NextHop']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                                    return meta._meta_table['L2rib.EviChildTables.Macs.Mac.Route.Bmac.PathList.NextHopArray']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                                return meta._meta_table['L2rib.EviChildTables.Macs.Mac.Route.Bmac.PathList']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                            return meta._meta_table['L2rib.EviChildTables.Macs.Mac.Route.Bmac']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                        return meta._meta_table['L2rib.EviChildTables.Macs.Mac.Route']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                    return meta._meta_table['L2rib.EviChildTables.Macs.Mac']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                return meta._meta_table['L2rib.EviChildTables.Macs']['meta_info']


        class Imets(_Entity_):
            """
            L2RIB EVPN EVI IMET table
            
            .. attribute:: imet
            
            	L2RIB EVPN IMET table
            	**type**\: list of  		 :py:class:`Imet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.Imets.Imet>`
            
            	**config**\: False
            
            

            """

            _prefix = 'l2rib-oper'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(L2rib.EviChildTables.Imets, self).__init__()

                self.yang_name = "imets"
                self.yang_parent_name = "evi-child-tables"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("imet", ("imet", L2rib.EviChildTables.Imets.Imet))])
                self._leafs = OrderedDict()

                self.imet = YList(self)
                self._segment_path = lambda: "imets"
                self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(L2rib.EviChildTables.Imets, [], name, value)


            class Imet(_Entity_):
                """
                L2RIB EVPN IMET table
                
                .. attribute:: evi
                
                	EVPN ID
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: tag_id
                
                	Tag ID
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: ip_addr
                
                	Originating Router IP Address
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                	**config**\: False
                
                .. attribute:: prod_id
                
                	Producer ID
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: vtepi_paddr
                
                	Originating Router IP Address
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: producer_id
                
                	Producer of Imet route
                	**type**\: int
                
                	**range:** 0..255
                
                	**config**\: False
                
                .. attribute:: topo_id
                
                	Topo ID
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: ethernet_tag_id
                
                	Ethernet Tag ID
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                

                """

                _prefix = 'l2rib-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(L2rib.EviChildTables.Imets.Imet, self).__init__()

                    self.yang_name = "imet"
                    self.yang_parent_name = "imets"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('evi', (YLeaf(YType.uint32, 'evi'), ['int'])),
                        ('tag_id', (YLeaf(YType.uint32, 'tag-id'), ['int'])),
                        ('ip_addr', (YLeaf(YType.str, 'ip-addr'), ['str','str'])),
                        ('prod_id', (YLeaf(YType.uint32, 'prod-id'), ['int'])),
                        ('vtepi_paddr', (YLeaf(YType.str, 'vtepi-paddr'), ['str'])),
                        ('producer_id', (YLeaf(YType.uint8, 'producer-id'), ['int'])),
                        ('topo_id', (YLeaf(YType.uint32, 'topo-id'), ['int'])),
                        ('ethernet_tag_id', (YLeaf(YType.uint32, 'ethernet-tag-id'), ['int'])),
                    ])
                    self.evi = None
                    self.tag_id = None
                    self.ip_addr = None
                    self.prod_id = None
                    self.vtepi_paddr = None
                    self.producer_id = None
                    self.topo_id = None
                    self.ethernet_tag_id = None
                    self._segment_path = lambda: "imet"
                    self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/imets/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(L2rib.EviChildTables.Imets.Imet, ['evi', 'tag_id', 'ip_addr', 'prod_id', 'vtepi_paddr', 'producer_id', 'topo_id', 'ethernet_tag_id'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                    return meta._meta_table['L2rib.EviChildTables.Imets.Imet']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                return meta._meta_table['L2rib.EviChildTables.Imets']['meta_info']


        class MacDetails(_Entity_):
            """
            L2RIB EVPN EVI MAC Detail table
            
            .. attribute:: mac_detail
            
            	L2RIB EVPN MAC Detail table
            	**type**\: list of  		 :py:class:`MacDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.MacDetails.MacDetail>`
            
            	**config**\: False
            
            

            """

            _prefix = 'l2rib-oper'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(L2rib.EviChildTables.MacDetails, self).__init__()

                self.yang_name = "mac-details"
                self.yang_parent_name = "evi-child-tables"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("mac-detail", ("mac_detail", L2rib.EviChildTables.MacDetails.MacDetail))])
                self._leafs = OrderedDict()

                self.mac_detail = YList(self)
                self._segment_path = lambda: "mac-details"
                self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(L2rib.EviChildTables.MacDetails, [], name, value)


            class MacDetail(_Entity_):
                """
                L2RIB EVPN MAC Detail table
                
                .. attribute:: evi
                
                	EVPN ID
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: mac_addr
                
                	MAC Address
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                	**config**\: False
                
                .. attribute:: prod_id
                
                	Producer ID
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: mac_route
                
                	MAC Route
                	**type**\:  :py:class:`MacRoute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.MacDetails.MacDetail.MacRoute>`
                
                	**config**\: False
                
                .. attribute:: rt_tlv
                
                	Mac Route Opaque Data TLV
                	**type**\:  :py:class:`RtTlv <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.MacDetails.MacDetail.RtTlv>`
                
                	**config**\: False
                
                .. attribute:: sequence_number
                
                	MAC route sequence Number
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: flags
                
                	MAC route flags
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{1,8}
                
                	**config**\: False
                
                .. attribute:: baseflags
                
                	BASE flags
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{1,8}
                
                	**config**\: False
                
                .. attribute:: soo
                
                	SOO
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: slot_id
                
                	Slot ID
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: esi
                
                	ESI
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: last_update_timestamp
                
                	Last Update Timestamp
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                

                """

                _prefix = 'l2rib-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(L2rib.EviChildTables.MacDetails.MacDetail, self).__init__()

                    self.yang_name = "mac-detail"
                    self.yang_parent_name = "mac-details"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("mac-route", ("mac_route", L2rib.EviChildTables.MacDetails.MacDetail.MacRoute)), ("rt-tlv", ("rt_tlv", L2rib.EviChildTables.MacDetails.MacDetail.RtTlv))])
                    self._leafs = OrderedDict([
                        ('evi', (YLeaf(YType.uint32, 'evi'), ['int'])),
                        ('mac_addr', (YLeaf(YType.str, 'mac-addr'), ['str'])),
                        ('prod_id', (YLeaf(YType.uint32, 'prod-id'), ['int'])),
                        ('sequence_number', (YLeaf(YType.uint32, 'sequence-number'), ['int'])),
                        ('flags', (YLeaf(YType.str, 'flags'), ['str'])),
                        ('baseflags', (YLeaf(YType.str, 'baseflags'), ['str'])),
                        ('soo', (YLeaf(YType.uint32, 'soo'), ['int'])),
                        ('slot_id', (YLeaf(YType.uint32, 'slot-id'), ['int'])),
                        ('esi', (YLeaf(YType.str, 'esi'), ['str'])),
                        ('last_update_timestamp', (YLeaf(YType.uint64, 'last-update-timestamp'), ['int'])),
                    ])
                    self.evi = None
                    self.mac_addr = None
                    self.prod_id = None
                    self.sequence_number = None
                    self.flags = None
                    self.baseflags = None
                    self.soo = None
                    self.slot_id = None
                    self.esi = None
                    self.last_update_timestamp = None

                    self.mac_route = L2rib.EviChildTables.MacDetails.MacDetail.MacRoute()
                    self.mac_route.parent = self
                    self._children_name_map["mac_route"] = "mac-route"

                    self.rt_tlv = L2rib.EviChildTables.MacDetails.MacDetail.RtTlv()
                    self.rt_tlv.parent = self
                    self._children_name_map["rt_tlv"] = "rt-tlv"
                    self._segment_path = lambda: "mac-detail"
                    self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/mac-details/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(L2rib.EviChildTables.MacDetails.MacDetail, ['evi', 'mac_addr', 'prod_id', 'sequence_number', 'flags', 'baseflags', 'soo', 'slot_id', 'esi', 'last_update_timestamp'], name, value)


                class MacRoute(_Entity_):
                    """
                    MAC Route
                    
                    .. attribute:: route
                    
                    	MAC route
                    	**type**\:  :py:class:`Route <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route>`
                    
                    	**config**\: False
                    
                    .. attribute:: mac_address
                    
                    	MAC Address
                    	**type**\: str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    	**config**\: False
                    
                    .. attribute:: admin_distance
                    
                    	Admin Distance
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: producer_id
                    
                    	Producer ID
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: topology_id
                    
                    	Topology ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'l2rib-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(L2rib.EviChildTables.MacDetails.MacDetail.MacRoute, self).__init__()

                        self.yang_name = "mac-route"
                        self.yang_parent_name = "mac-detail"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("route", ("route", L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route))])
                        self._leafs = OrderedDict([
                            ('mac_address', (YLeaf(YType.str, 'mac-address'), ['str'])),
                            ('admin_distance', (YLeaf(YType.uint8, 'admin-distance'), ['int'])),
                            ('producer_id', (YLeaf(YType.uint8, 'producer-id'), ['int'])),
                            ('topology_id', (YLeaf(YType.uint32, 'topology-id'), ['int'])),
                        ])
                        self.mac_address = None
                        self.admin_distance = None
                        self.producer_id = None
                        self.topology_id = None

                        self.route = L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route()
                        self.route.parent = self
                        self._children_name_map["route"] = "route"
                        self._segment_path = lambda: "mac-route"
                        self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/mac-details/mac-detail/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2rib.EviChildTables.MacDetails.MacDetail.MacRoute, ['mac_address', 'admin_distance', 'producer_id', 'topology_id'], name, value)


                    class Route(_Entity_):
                        """
                        MAC route
                        
                        .. attribute:: regular
                        
                        	Regular MAC route
                        	**type**\:  :py:class:`Regular <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Regular>`
                        
                        	**config**\: False
                        
                        .. attribute:: evpn_esi
                        
                        	EVPN ESI MAC route
                        	**type**\:  :py:class:`EvpnEsi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.EvpnEsi>`
                        
                        	**config**\: False
                        
                        .. attribute:: bmac
                        
                        	BMAC route
                        	**type**\:  :py:class:`Bmac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Bmac>`
                        
                        	**config**\: False
                        
                        .. attribute:: type
                        
                        	Type
                        	**type**\:  :py:class:`L2ribMacRoute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2ribMacRoute>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'l2rib-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route, self).__init__()

                            self.yang_name = "route"
                            self.yang_parent_name = "mac-route"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("regular", ("regular", L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Regular)), ("evpn-esi", ("evpn_esi", L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.EvpnEsi)), ("bmac", ("bmac", L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Bmac))])
                            self._leafs = OrderedDict([
                                ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper', 'L2ribMacRoute', '')])),
                            ])
                            self.type = None

                            self.regular = L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Regular()
                            self.regular.parent = self
                            self._children_name_map["regular"] = "regular"

                            self.evpn_esi = L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.EvpnEsi()
                            self.evpn_esi.parent = self
                            self._children_name_map["evpn_esi"] = "evpn-esi"

                            self.bmac = L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Bmac()
                            self.bmac.parent = self
                            self._children_name_map["bmac"] = "bmac"
                            self._segment_path = lambda: "route"
                            self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/mac-details/mac-detail/mac-route/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route, ['type'], name, value)


                        class Regular(_Entity_):
                            """
                            Regular MAC route
                            
                            .. attribute:: next_hop
                            
                            	Next Hop
                            	**type**\:  :py:class:`NextHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Regular.NextHop>`
                            
                            	**config**\: False
                            
                            .. attribute:: backup_next_hop
                            
                            	Secondary Next Hop
                            	**type**\:  :py:class:`BackupNextHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Regular.BackupNextHop>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'l2rib-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Regular, self).__init__()

                                self.yang_name = "regular"
                                self.yang_parent_name = "route"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("next-hop", ("next_hop", L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Regular.NextHop)), ("backup-next-hop", ("backup_next_hop", L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Regular.BackupNextHop))])
                                self._leafs = OrderedDict()

                                self.next_hop = L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Regular.NextHop()
                                self.next_hop.parent = self
                                self._children_name_map["next_hop"] = "next-hop"

                                self.backup_next_hop = L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Regular.BackupNextHop()
                                self.backup_next_hop.parent = self
                                self._children_name_map["backup_next_hop"] = "backup-next-hop"
                                self._segment_path = lambda: "regular"
                                self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/mac-details/mac-detail/mac-route/route/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Regular, [], name, value)


                            class NextHop(_Entity_):
                                """
                                Next Hop
                                
                                .. attribute:: next_hop
                                
                                	Next hop
                                	**type**\:  :py:class:`NextHop_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Regular.NextHop.NextHop_>`
                                
                                	**config**\: False
                                
                                .. attribute:: topology_id
                                
                                	Next\-hop TOPOLOGY ID
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: flags
                                
                                	Next\-hop flags
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'l2rib-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Regular.NextHop, self).__init__()

                                    self.yang_name = "next-hop"
                                    self.yang_parent_name = "regular"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = False
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("next-hop", ("next_hop", L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Regular.NextHop.NextHop_))])
                                    self._leafs = OrderedDict([
                                        ('topology_id', (YLeaf(YType.uint32, 'topology-id'), ['int'])),
                                        ('flags', (YLeaf(YType.uint16, 'flags'), ['int'])),
                                    ])
                                    self.topology_id = None
                                    self.flags = None

                                    self.next_hop = L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Regular.NextHop.NextHop_()
                                    self.next_hop.parent = self
                                    self._children_name_map["next_hop"] = "next-hop"
                                    self._segment_path = lambda: "next-hop"
                                    self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/mac-details/mac-detail/mac-route/route/regular/%s" % self._segment_path()
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Regular.NextHop, ['topology_id', 'flags'], name, value)


                                class NextHop_(_Entity_):
                                    """
                                    Next hop
                                    
                                    .. attribute:: labeled
                                    
                                    	Labeled Next Hop
                                    	**type**\:  :py:class:`Labeled <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Regular.NextHop.NextHop_.Labeled>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: type
                                    
                                    	Type
                                    	**type**\:  :py:class:`L2ribNextHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2ribNextHop>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: ipv4
                                    
                                    	IPV4 address Next Hop
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: ipv6
                                    
                                    	IPV6 address Next Hop
                                    	**type**\: str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: mac
                                    
                                    	MAC address Next Hop
                                    	**type**\: str
                                    
                                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: interface_handle
                                    
                                    	Intefrace Handle Next Hop
                                    	**type**\: str
                                    
                                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: xid
                                    
                                    	XID Next Hop
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'l2rib-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Regular.NextHop.NextHop_, self).__init__()

                                        self.yang_name = "next-hop"
                                        self.yang_parent_name = "next-hop"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = False
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("labeled", ("labeled", L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Regular.NextHop.NextHop_.Labeled))])
                                        self._leafs = OrderedDict([
                                            ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper', 'L2ribNextHop', '')])),
                                            ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                                            ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                                            ('mac', (YLeaf(YType.str, 'mac'), ['str'])),
                                            ('interface_handle', (YLeaf(YType.str, 'interface-handle'), ['str'])),
                                            ('xid', (YLeaf(YType.uint32, 'xid'), ['int'])),
                                        ])
                                        self.type = None
                                        self.ipv4 = None
                                        self.ipv6 = None
                                        self.mac = None
                                        self.interface_handle = None
                                        self.xid = None

                                        self.labeled = L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Regular.NextHop.NextHop_.Labeled()
                                        self.labeled.parent = self
                                        self._children_name_map["labeled"] = "labeled"
                                        self._segment_path = lambda: "next-hop"
                                        self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/mac-details/mac-detail/mac-route/route/regular/next-hop/%s" % self._segment_path()
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Regular.NextHop.NextHop_, ['type', 'ipv4', 'ipv6', 'mac', 'interface_handle', 'xid'], name, value)


                                    class Labeled(_Entity_):
                                        """
                                        Labeled Next Hop
                                        
                                        .. attribute:: address_family
                                        
                                        	L2RIB Address Family
                                        	**type**\:  :py:class:`L2ribAfi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2ribAfi>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: ip_address
                                        
                                        	IP Address
                                        	**type**\: str
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: label
                                        
                                        	Label
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: internal
                                        
                                        	Internal Label
                                        	**type**\: bool
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'l2rib-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Regular.NextHop.NextHop_.Labeled, self).__init__()

                                            self.yang_name = "labeled"
                                            self.yang_parent_name = "next-hop"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = False
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('address_family', (YLeaf(YType.enumeration, 'address-family'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper', 'L2ribAfi', '')])),
                                                ('ip_address', (YLeaf(YType.str, 'ip-address'), ['str'])),
                                                ('label', (YLeaf(YType.uint32, 'label'), ['int'])),
                                                ('internal', (YLeaf(YType.boolean, 'internal'), ['bool'])),
                                            ])
                                            self.address_family = None
                                            self.ip_address = None
                                            self.label = None
                                            self.internal = None
                                            self._segment_path = lambda: "labeled"
                                            self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/mac-details/mac-detail/mac-route/route/regular/next-hop/next-hop/%s" % self._segment_path()
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Regular.NextHop.NextHop_.Labeled, ['address_family', 'ip_address', 'label', 'internal'], name, value)

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                                            return meta._meta_table['L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Regular.NextHop.NextHop_.Labeled']['meta_info']

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                                        return meta._meta_table['L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Regular.NextHop.NextHop_']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                                    return meta._meta_table['L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Regular.NextHop']['meta_info']


                            class BackupNextHop(_Entity_):
                                """
                                Secondary Next Hop
                                
                                .. attribute:: next_hop
                                
                                	Next hop
                                	**type**\:  :py:class:`NextHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Regular.BackupNextHop.NextHop>`
                                
                                	**config**\: False
                                
                                .. attribute:: topology_id
                                
                                	Next\-hop TOPOLOGY ID
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: flags
                                
                                	Next\-hop flags
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'l2rib-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Regular.BackupNextHop, self).__init__()

                                    self.yang_name = "backup-next-hop"
                                    self.yang_parent_name = "regular"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = False
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("next-hop", ("next_hop", L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Regular.BackupNextHop.NextHop))])
                                    self._leafs = OrderedDict([
                                        ('topology_id', (YLeaf(YType.uint32, 'topology-id'), ['int'])),
                                        ('flags', (YLeaf(YType.uint16, 'flags'), ['int'])),
                                    ])
                                    self.topology_id = None
                                    self.flags = None

                                    self.next_hop = L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Regular.BackupNextHop.NextHop()
                                    self.next_hop.parent = self
                                    self._children_name_map["next_hop"] = "next-hop"
                                    self._segment_path = lambda: "backup-next-hop"
                                    self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/mac-details/mac-detail/mac-route/route/regular/%s" % self._segment_path()
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Regular.BackupNextHop, ['topology_id', 'flags'], name, value)


                                class NextHop(_Entity_):
                                    """
                                    Next hop
                                    
                                    .. attribute:: labeled
                                    
                                    	Labeled Next Hop
                                    	**type**\:  :py:class:`Labeled <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Regular.BackupNextHop.NextHop.Labeled>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: type
                                    
                                    	Type
                                    	**type**\:  :py:class:`L2ribNextHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2ribNextHop>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: ipv4
                                    
                                    	IPV4 address Next Hop
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: ipv6
                                    
                                    	IPV6 address Next Hop
                                    	**type**\: str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: mac
                                    
                                    	MAC address Next Hop
                                    	**type**\: str
                                    
                                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: interface_handle
                                    
                                    	Intefrace Handle Next Hop
                                    	**type**\: str
                                    
                                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: xid
                                    
                                    	XID Next Hop
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'l2rib-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Regular.BackupNextHop.NextHop, self).__init__()

                                        self.yang_name = "next-hop"
                                        self.yang_parent_name = "backup-next-hop"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = False
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("labeled", ("labeled", L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Regular.BackupNextHop.NextHop.Labeled))])
                                        self._leafs = OrderedDict([
                                            ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper', 'L2ribNextHop', '')])),
                                            ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                                            ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                                            ('mac', (YLeaf(YType.str, 'mac'), ['str'])),
                                            ('interface_handle', (YLeaf(YType.str, 'interface-handle'), ['str'])),
                                            ('xid', (YLeaf(YType.uint32, 'xid'), ['int'])),
                                        ])
                                        self.type = None
                                        self.ipv4 = None
                                        self.ipv6 = None
                                        self.mac = None
                                        self.interface_handle = None
                                        self.xid = None

                                        self.labeled = L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Regular.BackupNextHop.NextHop.Labeled()
                                        self.labeled.parent = self
                                        self._children_name_map["labeled"] = "labeled"
                                        self._segment_path = lambda: "next-hop"
                                        self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/mac-details/mac-detail/mac-route/route/regular/backup-next-hop/%s" % self._segment_path()
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Regular.BackupNextHop.NextHop, ['type', 'ipv4', 'ipv6', 'mac', 'interface_handle', 'xid'], name, value)


                                    class Labeled(_Entity_):
                                        """
                                        Labeled Next Hop
                                        
                                        .. attribute:: address_family
                                        
                                        	L2RIB Address Family
                                        	**type**\:  :py:class:`L2ribAfi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2ribAfi>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: ip_address
                                        
                                        	IP Address
                                        	**type**\: str
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: label
                                        
                                        	Label
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: internal
                                        
                                        	Internal Label
                                        	**type**\: bool
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'l2rib-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Regular.BackupNextHop.NextHop.Labeled, self).__init__()

                                            self.yang_name = "labeled"
                                            self.yang_parent_name = "next-hop"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = False
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('address_family', (YLeaf(YType.enumeration, 'address-family'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper', 'L2ribAfi', '')])),
                                                ('ip_address', (YLeaf(YType.str, 'ip-address'), ['str'])),
                                                ('label', (YLeaf(YType.uint32, 'label'), ['int'])),
                                                ('internal', (YLeaf(YType.boolean, 'internal'), ['bool'])),
                                            ])
                                            self.address_family = None
                                            self.ip_address = None
                                            self.label = None
                                            self.internal = None
                                            self._segment_path = lambda: "labeled"
                                            self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/mac-details/mac-detail/mac-route/route/regular/backup-next-hop/next-hop/%s" % self._segment_path()
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Regular.BackupNextHop.NextHop.Labeled, ['address_family', 'ip_address', 'label', 'internal'], name, value)

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                                            return meta._meta_table['L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Regular.BackupNextHop.NextHop.Labeled']['meta_info']

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                                        return meta._meta_table['L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Regular.BackupNextHop.NextHop']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                                    return meta._meta_table['L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Regular.BackupNextHop']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                                return meta._meta_table['L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Regular']['meta_info']


                        class EvpnEsi(_Entity_):
                            """
                            EVPN ESI MAC route
                            
                            .. attribute:: ethernet_segment_id
                            
                            	Ethernet Segment Identifier
                            	**type**\:  :py:class:`EthernetSegmentId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.EvpnEsi.EthernetSegmentId>`
                            
                            	**config**\: False
                            
                            .. attribute:: path_list
                            
                            	Path list information. Set for detailed MAC route information
                            	**type**\:  :py:class:`PathList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.EvpnEsi.PathList>`
                            
                            	**config**\: False
                            
                            .. attribute:: sequence_number
                            
                            	MAC route sequence number
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: forward_state
                            
                            	Forwarding State. True means forward, False means drop
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'l2rib-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.EvpnEsi, self).__init__()

                                self.yang_name = "evpn-esi"
                                self.yang_parent_name = "route"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("ethernet-segment-id", ("ethernet_segment_id", L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.EvpnEsi.EthernetSegmentId)), ("path-list", ("path_list", L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.EvpnEsi.PathList))])
                                self._leafs = OrderedDict([
                                    ('sequence_number', (YLeaf(YType.uint32, 'sequence-number'), ['int'])),
                                    ('forward_state', (YLeaf(YType.boolean, 'forward-state'), ['bool'])),
                                ])
                                self.sequence_number = None
                                self.forward_state = None

                                self.ethernet_segment_id = L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.EvpnEsi.EthernetSegmentId()
                                self.ethernet_segment_id.parent = self
                                self._children_name_map["ethernet_segment_id"] = "ethernet-segment-id"

                                self.path_list = L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.EvpnEsi.PathList()
                                self.path_list.parent = self
                                self._children_name_map["path_list"] = "path-list"
                                self._segment_path = lambda: "evpn-esi"
                                self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/mac-details/mac-detail/mac-route/route/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.EvpnEsi, ['sequence_number', 'forward_state'], name, value)


                            class EthernetSegmentId(_Entity_):
                                """
                                Ethernet Segment Identifier
                                
                                .. attribute:: system_priority
                                
                                	LACP System Priority
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                	**config**\: False
                                
                                .. attribute:: system_id
                                
                                	LACP System Id
                                	**type**\: str
                                
                                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                
                                	**config**\: False
                                
                                .. attribute:: port_key
                                
                                	LACP Port Key
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'l2rib-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.EvpnEsi.EthernetSegmentId, self).__init__()

                                    self.yang_name = "ethernet-segment-id"
                                    self.yang_parent_name = "evpn-esi"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = False
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('system_priority', (YLeaf(YType.uint16, 'system-priority'), ['int'])),
                                        ('system_id', (YLeaf(YType.str, 'system-id'), ['str'])),
                                        ('port_key', (YLeaf(YType.uint16, 'port-key'), ['int'])),
                                    ])
                                    self.system_priority = None
                                    self.system_id = None
                                    self.port_key = None
                                    self._segment_path = lambda: "ethernet-segment-id"
                                    self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/mac-details/mac-detail/mac-route/route/evpn-esi/%s" % self._segment_path()
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.EvpnEsi.EthernetSegmentId, ['system_priority', 'system_id', 'port_key'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                                    return meta._meta_table['L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.EvpnEsi.EthernetSegmentId']['meta_info']


                            class PathList(_Entity_):
                                """
                                Path list information. Set for detailed MAC
                                route information
                                
                                .. attribute:: path_list_info
                                
                                	Type\-specific Path List info
                                	**type**\:  :py:class:`PathListInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.EvpnEsi.PathList.PathListInfo>`
                                
                                	**config**\: False
                                
                                .. attribute:: producer_id
                                
                                	ID of EAD route producer
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                	**config**\: False
                                
                                .. attribute:: mac_count
                                
                                	Number of MAC routes bound to this Path list
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: local_label
                                
                                	Path list local Label
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: next_hop_array
                                
                                	Array of Next Hops for MAC Path List
                                	**type**\: list of  		 :py:class:`NextHopArray <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.EvpnEsi.PathList.NextHopArray>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'l2rib-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.EvpnEsi.PathList, self).__init__()

                                    self.yang_name = "path-list"
                                    self.yang_parent_name = "evpn-esi"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = False
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("path-list-info", ("path_list_info", L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.EvpnEsi.PathList.PathListInfo)), ("next-hop-array", ("next_hop_array", L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.EvpnEsi.PathList.NextHopArray))])
                                    self._leafs = OrderedDict([
                                        ('producer_id', (YLeaf(YType.uint8, 'producer-id'), ['int'])),
                                        ('mac_count', (YLeaf(YType.uint32, 'mac-count'), ['int'])),
                                        ('local_label', (YLeaf(YType.uint32, 'local-label'), ['int'])),
                                    ])
                                    self.producer_id = None
                                    self.mac_count = None
                                    self.local_label = None

                                    self.path_list_info = L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.EvpnEsi.PathList.PathListInfo()
                                    self.path_list_info.parent = self
                                    self._children_name_map["path_list_info"] = "path-list-info"

                                    self.next_hop_array = YList(self)
                                    self._segment_path = lambda: "path-list"
                                    self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/mac-details/mac-detail/mac-route/route/evpn-esi/%s" % self._segment_path()
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.EvpnEsi.PathList, ['producer_id', 'mac_count', 'local_label'], name, value)


                                class PathListInfo(_Entity_):
                                    """
                                    Type\-specific Path List info
                                    
                                    .. attribute:: path_list_esi
                                    
                                    	ESI Path List
                                    	**type**\:  :py:class:`PathListEsi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.EvpnEsi.PathList.PathListInfo.PathListEsi>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: path_list_mac
                                    
                                    	MAC Path List
                                    	**type**\:  :py:class:`PathListMac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.EvpnEsi.PathList.PathListInfo.PathListMac>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: type
                                    
                                    	Type
                                    	**type**\:  :py:class:`L2ribMacRoute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2ribMacRoute>`
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'l2rib-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.EvpnEsi.PathList.PathListInfo, self).__init__()

                                        self.yang_name = "path-list-info"
                                        self.yang_parent_name = "path-list"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = False
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("path-list-esi", ("path_list_esi", L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.EvpnEsi.PathList.PathListInfo.PathListEsi)), ("path-list-mac", ("path_list_mac", L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.EvpnEsi.PathList.PathListInfo.PathListMac))])
                                        self._leafs = OrderedDict([
                                            ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper', 'L2ribMacRoute', '')])),
                                        ])
                                        self.type = None

                                        self.path_list_esi = L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.EvpnEsi.PathList.PathListInfo.PathListEsi()
                                        self.path_list_esi.parent = self
                                        self._children_name_map["path_list_esi"] = "path-list-esi"

                                        self.path_list_mac = L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.EvpnEsi.PathList.PathListInfo.PathListMac()
                                        self.path_list_mac.parent = self
                                        self._children_name_map["path_list_mac"] = "path-list-mac"
                                        self._segment_path = lambda: "path-list-info"
                                        self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/mac-details/mac-detail/mac-route/route/evpn-esi/path-list/%s" % self._segment_path()
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.EvpnEsi.PathList.PathListInfo, ['type'], name, value)


                                    class PathListEsi(_Entity_):
                                        """
                                        ESI Path List
                                        
                                        .. attribute:: ethernet_segment_id
                                        
                                        	Ethernet Segment Identifier
                                        	**type**\:  :py:class:`EthernetSegmentId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.EvpnEsi.PathList.PathListInfo.PathListEsi.EthernetSegmentId>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: resolved
                                        
                                        	Path list Resolved
                                        	**type**\: bool
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: mac_update_next_hop_array
                                        
                                        	Array of Next Hops from MAC Update
                                        	**type**\: list of  		 :py:class:`MacUpdateNextHopArray <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.EvpnEsi.PathList.PathListInfo.PathListEsi.MacUpdateNextHopArray>`
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'l2rib-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.EvpnEsi.PathList.PathListInfo.PathListEsi, self).__init__()

                                            self.yang_name = "path-list-esi"
                                            self.yang_parent_name = "path-list-info"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = False
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("ethernet-segment-id", ("ethernet_segment_id", L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.EvpnEsi.PathList.PathListInfo.PathListEsi.EthernetSegmentId)), ("mac-update-next-hop-array", ("mac_update_next_hop_array", L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.EvpnEsi.PathList.PathListInfo.PathListEsi.MacUpdateNextHopArray))])
                                            self._leafs = OrderedDict([
                                                ('resolved', (YLeaf(YType.boolean, 'resolved'), ['bool'])),
                                            ])
                                            self.resolved = None

                                            self.ethernet_segment_id = L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.EvpnEsi.PathList.PathListInfo.PathListEsi.EthernetSegmentId()
                                            self.ethernet_segment_id.parent = self
                                            self._children_name_map["ethernet_segment_id"] = "ethernet-segment-id"

                                            self.mac_update_next_hop_array = YList(self)
                                            self._segment_path = lambda: "path-list-esi"
                                            self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/mac-details/mac-detail/mac-route/route/evpn-esi/path-list/path-list-info/%s" % self._segment_path()
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.EvpnEsi.PathList.PathListInfo.PathListEsi, ['resolved'], name, value)


                                        class EthernetSegmentId(_Entity_):
                                            """
                                            Ethernet Segment Identifier
                                            
                                            .. attribute:: system_priority
                                            
                                            	LACP System Priority
                                            	**type**\: int
                                            
                                            	**range:** 0..65535
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: system_id
                                            
                                            	LACP System Id
                                            	**type**\: str
                                            
                                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: port_key
                                            
                                            	LACP Port Key
                                            	**type**\: int
                                            
                                            	**range:** 0..65535
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'l2rib-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.EvpnEsi.PathList.PathListInfo.PathListEsi.EthernetSegmentId, self).__init__()

                                                self.yang_name = "ethernet-segment-id"
                                                self.yang_parent_name = "path-list-esi"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = False
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('system_priority', (YLeaf(YType.uint16, 'system-priority'), ['int'])),
                                                    ('system_id', (YLeaf(YType.str, 'system-id'), ['str'])),
                                                    ('port_key', (YLeaf(YType.uint16, 'port-key'), ['int'])),
                                                ])
                                                self.system_priority = None
                                                self.system_id = None
                                                self.port_key = None
                                                self._segment_path = lambda: "ethernet-segment-id"
                                                self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/mac-details/mac-detail/mac-route/route/evpn-esi/path-list/path-list-info/path-list-esi/%s" % self._segment_path()
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.EvpnEsi.PathList.PathListInfo.PathListEsi.EthernetSegmentId, ['system_priority', 'system_id', 'port_key'], name, value)

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                                                return meta._meta_table['L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.EvpnEsi.PathList.PathListInfo.PathListEsi.EthernetSegmentId']['meta_info']


                                        class MacUpdateNextHopArray(_Entity_):
                                            """
                                            Array of Next Hops from MAC Update
                                            
                                            .. attribute:: next_hop
                                            
                                            	Next hop
                                            	**type**\:  :py:class:`NextHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.EvpnEsi.PathList.PathListInfo.PathListEsi.MacUpdateNextHopArray.NextHop>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: topology_id
                                            
                                            	Next\-hop TOPOLOGY ID
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: flags
                                            
                                            	Next\-hop flags
                                            	**type**\: int
                                            
                                            	**range:** 0..65535
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'l2rib-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.EvpnEsi.PathList.PathListInfo.PathListEsi.MacUpdateNextHopArray, self).__init__()

                                                self.yang_name = "mac-update-next-hop-array"
                                                self.yang_parent_name = "path-list-esi"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = False
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([("next-hop", ("next_hop", L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.EvpnEsi.PathList.PathListInfo.PathListEsi.MacUpdateNextHopArray.NextHop))])
                                                self._leafs = OrderedDict([
                                                    ('topology_id', (YLeaf(YType.uint32, 'topology-id'), ['int'])),
                                                    ('flags', (YLeaf(YType.uint16, 'flags'), ['int'])),
                                                ])
                                                self.topology_id = None
                                                self.flags = None

                                                self.next_hop = L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.EvpnEsi.PathList.PathListInfo.PathListEsi.MacUpdateNextHopArray.NextHop()
                                                self.next_hop.parent = self
                                                self._children_name_map["next_hop"] = "next-hop"
                                                self._segment_path = lambda: "mac-update-next-hop-array"
                                                self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/mac-details/mac-detail/mac-route/route/evpn-esi/path-list/path-list-info/path-list-esi/%s" % self._segment_path()
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.EvpnEsi.PathList.PathListInfo.PathListEsi.MacUpdateNextHopArray, ['topology_id', 'flags'], name, value)


                                            class NextHop(_Entity_):
                                                """
                                                Next hop
                                                
                                                .. attribute:: labeled
                                                
                                                	Labeled Next Hop
                                                	**type**\:  :py:class:`Labeled <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.EvpnEsi.PathList.PathListInfo.PathListEsi.MacUpdateNextHopArray.NextHop.Labeled>`
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: type
                                                
                                                	Type
                                                	**type**\:  :py:class:`L2ribNextHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2ribNextHop>`
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: ipv4
                                                
                                                	IPV4 address Next Hop
                                                	**type**\: str
                                                
                                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: ipv6
                                                
                                                	IPV6 address Next Hop
                                                	**type**\: str
                                                
                                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: mac
                                                
                                                	MAC address Next Hop
                                                	**type**\: str
                                                
                                                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: interface_handle
                                                
                                                	Intefrace Handle Next Hop
                                                	**type**\: str
                                                
                                                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: xid
                                                
                                                	XID Next Hop
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                

                                                """

                                                _prefix = 'l2rib-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    if sys.version_info > (3,):
                                                        super().__init__()
                                                    else:
                                                        super(L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.EvpnEsi.PathList.PathListInfo.PathListEsi.MacUpdateNextHopArray.NextHop, self).__init__()

                                                    self.yang_name = "next-hop"
                                                    self.yang_parent_name = "mac-update-next-hop-array"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = False
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([("labeled", ("labeled", L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.EvpnEsi.PathList.PathListInfo.PathListEsi.MacUpdateNextHopArray.NextHop.Labeled))])
                                                    self._leafs = OrderedDict([
                                                        ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper', 'L2ribNextHop', '')])),
                                                        ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                                                        ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                                                        ('mac', (YLeaf(YType.str, 'mac'), ['str'])),
                                                        ('interface_handle', (YLeaf(YType.str, 'interface-handle'), ['str'])),
                                                        ('xid', (YLeaf(YType.uint32, 'xid'), ['int'])),
                                                    ])
                                                    self.type = None
                                                    self.ipv4 = None
                                                    self.ipv6 = None
                                                    self.mac = None
                                                    self.interface_handle = None
                                                    self.xid = None

                                                    self.labeled = L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.EvpnEsi.PathList.PathListInfo.PathListEsi.MacUpdateNextHopArray.NextHop.Labeled()
                                                    self.labeled.parent = self
                                                    self._children_name_map["labeled"] = "labeled"
                                                    self._segment_path = lambda: "next-hop"
                                                    self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/mac-details/mac-detail/mac-route/route/evpn-esi/path-list/path-list-info/path-list-esi/mac-update-next-hop-array/%s" % self._segment_path()
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.EvpnEsi.PathList.PathListInfo.PathListEsi.MacUpdateNextHopArray.NextHop, ['type', 'ipv4', 'ipv6', 'mac', 'interface_handle', 'xid'], name, value)


                                                class Labeled(_Entity_):
                                                    """
                                                    Labeled Next Hop
                                                    
                                                    .. attribute:: address_family
                                                    
                                                    	L2RIB Address Family
                                                    	**type**\:  :py:class:`L2ribAfi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2ribAfi>`
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: ip_address
                                                    
                                                    	IP Address
                                                    	**type**\: str
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: label
                                                    
                                                    	Label
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: internal
                                                    
                                                    	Internal Label
                                                    	**type**\: bool
                                                    
                                                    	**config**\: False
                                                    
                                                    

                                                    """

                                                    _prefix = 'l2rib-oper'
                                                    _revision = '2015-11-09'

                                                    def __init__(self):
                                                        if sys.version_info > (3,):
                                                            super().__init__()
                                                        else:
                                                            super(L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.EvpnEsi.PathList.PathListInfo.PathListEsi.MacUpdateNextHopArray.NextHop.Labeled, self).__init__()

                                                        self.yang_name = "labeled"
                                                        self.yang_parent_name = "next-hop"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = False
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([])
                                                        self._leafs = OrderedDict([
                                                            ('address_family', (YLeaf(YType.enumeration, 'address-family'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper', 'L2ribAfi', '')])),
                                                            ('ip_address', (YLeaf(YType.str, 'ip-address'), ['str'])),
                                                            ('label', (YLeaf(YType.uint32, 'label'), ['int'])),
                                                            ('internal', (YLeaf(YType.boolean, 'internal'), ['bool'])),
                                                        ])
                                                        self.address_family = None
                                                        self.ip_address = None
                                                        self.label = None
                                                        self.internal = None
                                                        self._segment_path = lambda: "labeled"
                                                        self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/mac-details/mac-detail/mac-route/route/evpn-esi/path-list/path-list-info/path-list-esi/mac-update-next-hop-array/next-hop/%s" % self._segment_path()
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.EvpnEsi.PathList.PathListInfo.PathListEsi.MacUpdateNextHopArray.NextHop.Labeled, ['address_family', 'ip_address', 'label', 'internal'], name, value)

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                                                        return meta._meta_table['L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.EvpnEsi.PathList.PathListInfo.PathListEsi.MacUpdateNextHopArray.NextHop.Labeled']['meta_info']

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                                                    return meta._meta_table['L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.EvpnEsi.PathList.PathListInfo.PathListEsi.MacUpdateNextHopArray.NextHop']['meta_info']

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                                                return meta._meta_table['L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.EvpnEsi.PathList.PathListInfo.PathListEsi.MacUpdateNextHopArray']['meta_info']

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                                            return meta._meta_table['L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.EvpnEsi.PathList.PathListInfo.PathListEsi']['meta_info']


                                    class PathListMac(_Entity_):
                                        """
                                        MAC Path List
                                        
                                        .. attribute:: mac_address
                                        
                                        	MAC Address
                                        	**type**\: str
                                        
                                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'l2rib-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.EvpnEsi.PathList.PathListInfo.PathListMac, self).__init__()

                                            self.yang_name = "path-list-mac"
                                            self.yang_parent_name = "path-list-info"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = False
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('mac_address', (YLeaf(YType.str, 'mac-address'), ['str'])),
                                            ])
                                            self.mac_address = None
                                            self._segment_path = lambda: "path-list-mac"
                                            self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/mac-details/mac-detail/mac-route/route/evpn-esi/path-list/path-list-info/%s" % self._segment_path()
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.EvpnEsi.PathList.PathListInfo.PathListMac, ['mac_address'], name, value)

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                                            return meta._meta_table['L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.EvpnEsi.PathList.PathListInfo.PathListMac']['meta_info']

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                                        return meta._meta_table['L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.EvpnEsi.PathList.PathListInfo']['meta_info']


                                class NextHopArray(_Entity_):
                                    """
                                    Array of Next Hops for MAC Path List
                                    
                                    .. attribute:: next_hop
                                    
                                    	Next hop
                                    	**type**\:  :py:class:`NextHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.EvpnEsi.PathList.NextHopArray.NextHop>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: topology_id
                                    
                                    	Next\-hop TOPOLOGY ID
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: flags
                                    
                                    	Next\-hop flags
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'l2rib-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.EvpnEsi.PathList.NextHopArray, self).__init__()

                                        self.yang_name = "next-hop-array"
                                        self.yang_parent_name = "path-list"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = False
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("next-hop", ("next_hop", L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.EvpnEsi.PathList.NextHopArray.NextHop))])
                                        self._leafs = OrderedDict([
                                            ('topology_id', (YLeaf(YType.uint32, 'topology-id'), ['int'])),
                                            ('flags', (YLeaf(YType.uint16, 'flags'), ['int'])),
                                        ])
                                        self.topology_id = None
                                        self.flags = None

                                        self.next_hop = L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.EvpnEsi.PathList.NextHopArray.NextHop()
                                        self.next_hop.parent = self
                                        self._children_name_map["next_hop"] = "next-hop"
                                        self._segment_path = lambda: "next-hop-array"
                                        self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/mac-details/mac-detail/mac-route/route/evpn-esi/path-list/%s" % self._segment_path()
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.EvpnEsi.PathList.NextHopArray, ['topology_id', 'flags'], name, value)


                                    class NextHop(_Entity_):
                                        """
                                        Next hop
                                        
                                        .. attribute:: labeled
                                        
                                        	Labeled Next Hop
                                        	**type**\:  :py:class:`Labeled <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.EvpnEsi.PathList.NextHopArray.NextHop.Labeled>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: type
                                        
                                        	Type
                                        	**type**\:  :py:class:`L2ribNextHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2ribNextHop>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: ipv4
                                        
                                        	IPV4 address Next Hop
                                        	**type**\: str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: ipv6
                                        
                                        	IPV6 address Next Hop
                                        	**type**\: str
                                        
                                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: mac
                                        
                                        	MAC address Next Hop
                                        	**type**\: str
                                        
                                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: interface_handle
                                        
                                        	Intefrace Handle Next Hop
                                        	**type**\: str
                                        
                                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: xid
                                        
                                        	XID Next Hop
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'l2rib-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.EvpnEsi.PathList.NextHopArray.NextHop, self).__init__()

                                            self.yang_name = "next-hop"
                                            self.yang_parent_name = "next-hop-array"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = False
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("labeled", ("labeled", L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.EvpnEsi.PathList.NextHopArray.NextHop.Labeled))])
                                            self._leafs = OrderedDict([
                                                ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper', 'L2ribNextHop', '')])),
                                                ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                                                ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                                                ('mac', (YLeaf(YType.str, 'mac'), ['str'])),
                                                ('interface_handle', (YLeaf(YType.str, 'interface-handle'), ['str'])),
                                                ('xid', (YLeaf(YType.uint32, 'xid'), ['int'])),
                                            ])
                                            self.type = None
                                            self.ipv4 = None
                                            self.ipv6 = None
                                            self.mac = None
                                            self.interface_handle = None
                                            self.xid = None

                                            self.labeled = L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.EvpnEsi.PathList.NextHopArray.NextHop.Labeled()
                                            self.labeled.parent = self
                                            self._children_name_map["labeled"] = "labeled"
                                            self._segment_path = lambda: "next-hop"
                                            self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/mac-details/mac-detail/mac-route/route/evpn-esi/path-list/next-hop-array/%s" % self._segment_path()
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.EvpnEsi.PathList.NextHopArray.NextHop, ['type', 'ipv4', 'ipv6', 'mac', 'interface_handle', 'xid'], name, value)


                                        class Labeled(_Entity_):
                                            """
                                            Labeled Next Hop
                                            
                                            .. attribute:: address_family
                                            
                                            	L2RIB Address Family
                                            	**type**\:  :py:class:`L2ribAfi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2ribAfi>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: ip_address
                                            
                                            	IP Address
                                            	**type**\: str
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: label
                                            
                                            	Label
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: internal
                                            
                                            	Internal Label
                                            	**type**\: bool
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'l2rib-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.EvpnEsi.PathList.NextHopArray.NextHop.Labeled, self).__init__()

                                                self.yang_name = "labeled"
                                                self.yang_parent_name = "next-hop"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = False
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('address_family', (YLeaf(YType.enumeration, 'address-family'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper', 'L2ribAfi', '')])),
                                                    ('ip_address', (YLeaf(YType.str, 'ip-address'), ['str'])),
                                                    ('label', (YLeaf(YType.uint32, 'label'), ['int'])),
                                                    ('internal', (YLeaf(YType.boolean, 'internal'), ['bool'])),
                                                ])
                                                self.address_family = None
                                                self.ip_address = None
                                                self.label = None
                                                self.internal = None
                                                self._segment_path = lambda: "labeled"
                                                self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/mac-details/mac-detail/mac-route/route/evpn-esi/path-list/next-hop-array/next-hop/%s" % self._segment_path()
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.EvpnEsi.PathList.NextHopArray.NextHop.Labeled, ['address_family', 'ip_address', 'label', 'internal'], name, value)

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                                                return meta._meta_table['L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.EvpnEsi.PathList.NextHopArray.NextHop.Labeled']['meta_info']

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                                            return meta._meta_table['L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.EvpnEsi.PathList.NextHopArray.NextHop']['meta_info']

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                                        return meta._meta_table['L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.EvpnEsi.PathList.NextHopArray']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                                    return meta._meta_table['L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.EvpnEsi.PathList']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                                return meta._meta_table['L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.EvpnEsi']['meta_info']


                        class Bmac(_Entity_):
                            """
                            BMAC route
                            
                            .. attribute:: path_list
                            
                            	Path list information
                            	**type**\:  :py:class:`PathList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Bmac.PathList>`
                            
                            	**config**\: False
                            
                            .. attribute:: bmac_address
                            
                            	BMAC Address
                            	**type**\: str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            	**config**\: False
                            
                            .. attribute:: forward_state
                            
                            	Forwarding State. True means forward, False means drop
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'l2rib-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Bmac, self).__init__()

                                self.yang_name = "bmac"
                                self.yang_parent_name = "route"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("path-list", ("path_list", L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Bmac.PathList))])
                                self._leafs = OrderedDict([
                                    ('bmac_address', (YLeaf(YType.str, 'bmac-address'), ['str'])),
                                    ('forward_state', (YLeaf(YType.boolean, 'forward-state'), ['bool'])),
                                ])
                                self.bmac_address = None
                                self.forward_state = None

                                self.path_list = L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Bmac.PathList()
                                self.path_list.parent = self
                                self._children_name_map["path_list"] = "path-list"
                                self._segment_path = lambda: "bmac"
                                self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/mac-details/mac-detail/mac-route/route/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Bmac, ['bmac_address', 'forward_state'], name, value)


                            class PathList(_Entity_):
                                """
                                Path list information
                                
                                .. attribute:: path_list_info
                                
                                	Type\-specific Path List info
                                	**type**\:  :py:class:`PathListInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Bmac.PathList.PathListInfo>`
                                
                                	**config**\: False
                                
                                .. attribute:: producer_id
                                
                                	ID of EAD route producer
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                	**config**\: False
                                
                                .. attribute:: mac_count
                                
                                	Number of MAC routes bound to this Path list
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: local_label
                                
                                	Path list local Label
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: next_hop_array
                                
                                	Array of Next Hops for MAC Path List
                                	**type**\: list of  		 :py:class:`NextHopArray <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Bmac.PathList.NextHopArray>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'l2rib-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Bmac.PathList, self).__init__()

                                    self.yang_name = "path-list"
                                    self.yang_parent_name = "bmac"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = False
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("path-list-info", ("path_list_info", L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Bmac.PathList.PathListInfo)), ("next-hop-array", ("next_hop_array", L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Bmac.PathList.NextHopArray))])
                                    self._leafs = OrderedDict([
                                        ('producer_id', (YLeaf(YType.uint8, 'producer-id'), ['int'])),
                                        ('mac_count', (YLeaf(YType.uint32, 'mac-count'), ['int'])),
                                        ('local_label', (YLeaf(YType.uint32, 'local-label'), ['int'])),
                                    ])
                                    self.producer_id = None
                                    self.mac_count = None
                                    self.local_label = None

                                    self.path_list_info = L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Bmac.PathList.PathListInfo()
                                    self.path_list_info.parent = self
                                    self._children_name_map["path_list_info"] = "path-list-info"

                                    self.next_hop_array = YList(self)
                                    self._segment_path = lambda: "path-list"
                                    self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/mac-details/mac-detail/mac-route/route/bmac/%s" % self._segment_path()
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Bmac.PathList, ['producer_id', 'mac_count', 'local_label'], name, value)


                                class PathListInfo(_Entity_):
                                    """
                                    Type\-specific Path List info
                                    
                                    .. attribute:: path_list_esi
                                    
                                    	ESI Path List
                                    	**type**\:  :py:class:`PathListEsi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Bmac.PathList.PathListInfo.PathListEsi>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: path_list_mac
                                    
                                    	MAC Path List
                                    	**type**\:  :py:class:`PathListMac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Bmac.PathList.PathListInfo.PathListMac>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: type
                                    
                                    	Type
                                    	**type**\:  :py:class:`L2ribMacRoute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2ribMacRoute>`
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'l2rib-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Bmac.PathList.PathListInfo, self).__init__()

                                        self.yang_name = "path-list-info"
                                        self.yang_parent_name = "path-list"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = False
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("path-list-esi", ("path_list_esi", L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Bmac.PathList.PathListInfo.PathListEsi)), ("path-list-mac", ("path_list_mac", L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Bmac.PathList.PathListInfo.PathListMac))])
                                        self._leafs = OrderedDict([
                                            ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper', 'L2ribMacRoute', '')])),
                                        ])
                                        self.type = None

                                        self.path_list_esi = L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Bmac.PathList.PathListInfo.PathListEsi()
                                        self.path_list_esi.parent = self
                                        self._children_name_map["path_list_esi"] = "path-list-esi"

                                        self.path_list_mac = L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Bmac.PathList.PathListInfo.PathListMac()
                                        self.path_list_mac.parent = self
                                        self._children_name_map["path_list_mac"] = "path-list-mac"
                                        self._segment_path = lambda: "path-list-info"
                                        self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/mac-details/mac-detail/mac-route/route/bmac/path-list/%s" % self._segment_path()
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Bmac.PathList.PathListInfo, ['type'], name, value)


                                    class PathListEsi(_Entity_):
                                        """
                                        ESI Path List
                                        
                                        .. attribute:: ethernet_segment_id
                                        
                                        	Ethernet Segment Identifier
                                        	**type**\:  :py:class:`EthernetSegmentId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Bmac.PathList.PathListInfo.PathListEsi.EthernetSegmentId>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: resolved
                                        
                                        	Path list Resolved
                                        	**type**\: bool
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: mac_update_next_hop_array
                                        
                                        	Array of Next Hops from MAC Update
                                        	**type**\: list of  		 :py:class:`MacUpdateNextHopArray <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Bmac.PathList.PathListInfo.PathListEsi.MacUpdateNextHopArray>`
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'l2rib-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Bmac.PathList.PathListInfo.PathListEsi, self).__init__()

                                            self.yang_name = "path-list-esi"
                                            self.yang_parent_name = "path-list-info"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = False
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("ethernet-segment-id", ("ethernet_segment_id", L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Bmac.PathList.PathListInfo.PathListEsi.EthernetSegmentId)), ("mac-update-next-hop-array", ("mac_update_next_hop_array", L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Bmac.PathList.PathListInfo.PathListEsi.MacUpdateNextHopArray))])
                                            self._leafs = OrderedDict([
                                                ('resolved', (YLeaf(YType.boolean, 'resolved'), ['bool'])),
                                            ])
                                            self.resolved = None

                                            self.ethernet_segment_id = L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Bmac.PathList.PathListInfo.PathListEsi.EthernetSegmentId()
                                            self.ethernet_segment_id.parent = self
                                            self._children_name_map["ethernet_segment_id"] = "ethernet-segment-id"

                                            self.mac_update_next_hop_array = YList(self)
                                            self._segment_path = lambda: "path-list-esi"
                                            self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/mac-details/mac-detail/mac-route/route/bmac/path-list/path-list-info/%s" % self._segment_path()
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Bmac.PathList.PathListInfo.PathListEsi, ['resolved'], name, value)


                                        class EthernetSegmentId(_Entity_):
                                            """
                                            Ethernet Segment Identifier
                                            
                                            .. attribute:: system_priority
                                            
                                            	LACP System Priority
                                            	**type**\: int
                                            
                                            	**range:** 0..65535
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: system_id
                                            
                                            	LACP System Id
                                            	**type**\: str
                                            
                                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: port_key
                                            
                                            	LACP Port Key
                                            	**type**\: int
                                            
                                            	**range:** 0..65535
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'l2rib-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Bmac.PathList.PathListInfo.PathListEsi.EthernetSegmentId, self).__init__()

                                                self.yang_name = "ethernet-segment-id"
                                                self.yang_parent_name = "path-list-esi"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = False
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('system_priority', (YLeaf(YType.uint16, 'system-priority'), ['int'])),
                                                    ('system_id', (YLeaf(YType.str, 'system-id'), ['str'])),
                                                    ('port_key', (YLeaf(YType.uint16, 'port-key'), ['int'])),
                                                ])
                                                self.system_priority = None
                                                self.system_id = None
                                                self.port_key = None
                                                self._segment_path = lambda: "ethernet-segment-id"
                                                self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/mac-details/mac-detail/mac-route/route/bmac/path-list/path-list-info/path-list-esi/%s" % self._segment_path()
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Bmac.PathList.PathListInfo.PathListEsi.EthernetSegmentId, ['system_priority', 'system_id', 'port_key'], name, value)

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                                                return meta._meta_table['L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Bmac.PathList.PathListInfo.PathListEsi.EthernetSegmentId']['meta_info']


                                        class MacUpdateNextHopArray(_Entity_):
                                            """
                                            Array of Next Hops from MAC Update
                                            
                                            .. attribute:: next_hop
                                            
                                            	Next hop
                                            	**type**\:  :py:class:`NextHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Bmac.PathList.PathListInfo.PathListEsi.MacUpdateNextHopArray.NextHop>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: topology_id
                                            
                                            	Next\-hop TOPOLOGY ID
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: flags
                                            
                                            	Next\-hop flags
                                            	**type**\: int
                                            
                                            	**range:** 0..65535
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'l2rib-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Bmac.PathList.PathListInfo.PathListEsi.MacUpdateNextHopArray, self).__init__()

                                                self.yang_name = "mac-update-next-hop-array"
                                                self.yang_parent_name = "path-list-esi"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = False
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([("next-hop", ("next_hop", L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Bmac.PathList.PathListInfo.PathListEsi.MacUpdateNextHopArray.NextHop))])
                                                self._leafs = OrderedDict([
                                                    ('topology_id', (YLeaf(YType.uint32, 'topology-id'), ['int'])),
                                                    ('flags', (YLeaf(YType.uint16, 'flags'), ['int'])),
                                                ])
                                                self.topology_id = None
                                                self.flags = None

                                                self.next_hop = L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Bmac.PathList.PathListInfo.PathListEsi.MacUpdateNextHopArray.NextHop()
                                                self.next_hop.parent = self
                                                self._children_name_map["next_hop"] = "next-hop"
                                                self._segment_path = lambda: "mac-update-next-hop-array"
                                                self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/mac-details/mac-detail/mac-route/route/bmac/path-list/path-list-info/path-list-esi/%s" % self._segment_path()
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Bmac.PathList.PathListInfo.PathListEsi.MacUpdateNextHopArray, ['topology_id', 'flags'], name, value)


                                            class NextHop(_Entity_):
                                                """
                                                Next hop
                                                
                                                .. attribute:: labeled
                                                
                                                	Labeled Next Hop
                                                	**type**\:  :py:class:`Labeled <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Bmac.PathList.PathListInfo.PathListEsi.MacUpdateNextHopArray.NextHop.Labeled>`
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: type
                                                
                                                	Type
                                                	**type**\:  :py:class:`L2ribNextHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2ribNextHop>`
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: ipv4
                                                
                                                	IPV4 address Next Hop
                                                	**type**\: str
                                                
                                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: ipv6
                                                
                                                	IPV6 address Next Hop
                                                	**type**\: str
                                                
                                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: mac
                                                
                                                	MAC address Next Hop
                                                	**type**\: str
                                                
                                                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: interface_handle
                                                
                                                	Intefrace Handle Next Hop
                                                	**type**\: str
                                                
                                                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: xid
                                                
                                                	XID Next Hop
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                

                                                """

                                                _prefix = 'l2rib-oper'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    if sys.version_info > (3,):
                                                        super().__init__()
                                                    else:
                                                        super(L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Bmac.PathList.PathListInfo.PathListEsi.MacUpdateNextHopArray.NextHop, self).__init__()

                                                    self.yang_name = "next-hop"
                                                    self.yang_parent_name = "mac-update-next-hop-array"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = False
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([("labeled", ("labeled", L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Bmac.PathList.PathListInfo.PathListEsi.MacUpdateNextHopArray.NextHop.Labeled))])
                                                    self._leafs = OrderedDict([
                                                        ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper', 'L2ribNextHop', '')])),
                                                        ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                                                        ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                                                        ('mac', (YLeaf(YType.str, 'mac'), ['str'])),
                                                        ('interface_handle', (YLeaf(YType.str, 'interface-handle'), ['str'])),
                                                        ('xid', (YLeaf(YType.uint32, 'xid'), ['int'])),
                                                    ])
                                                    self.type = None
                                                    self.ipv4 = None
                                                    self.ipv6 = None
                                                    self.mac = None
                                                    self.interface_handle = None
                                                    self.xid = None

                                                    self.labeled = L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Bmac.PathList.PathListInfo.PathListEsi.MacUpdateNextHopArray.NextHop.Labeled()
                                                    self.labeled.parent = self
                                                    self._children_name_map["labeled"] = "labeled"
                                                    self._segment_path = lambda: "next-hop"
                                                    self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/mac-details/mac-detail/mac-route/route/bmac/path-list/path-list-info/path-list-esi/mac-update-next-hop-array/%s" % self._segment_path()
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Bmac.PathList.PathListInfo.PathListEsi.MacUpdateNextHopArray.NextHop, ['type', 'ipv4', 'ipv6', 'mac', 'interface_handle', 'xid'], name, value)


                                                class Labeled(_Entity_):
                                                    """
                                                    Labeled Next Hop
                                                    
                                                    .. attribute:: address_family
                                                    
                                                    	L2RIB Address Family
                                                    	**type**\:  :py:class:`L2ribAfi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2ribAfi>`
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: ip_address
                                                    
                                                    	IP Address
                                                    	**type**\: str
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: label
                                                    
                                                    	Label
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: internal
                                                    
                                                    	Internal Label
                                                    	**type**\: bool
                                                    
                                                    	**config**\: False
                                                    
                                                    

                                                    """

                                                    _prefix = 'l2rib-oper'
                                                    _revision = '2015-11-09'

                                                    def __init__(self):
                                                        if sys.version_info > (3,):
                                                            super().__init__()
                                                        else:
                                                            super(L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Bmac.PathList.PathListInfo.PathListEsi.MacUpdateNextHopArray.NextHop.Labeled, self).__init__()

                                                        self.yang_name = "labeled"
                                                        self.yang_parent_name = "next-hop"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = False
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([])
                                                        self._leafs = OrderedDict([
                                                            ('address_family', (YLeaf(YType.enumeration, 'address-family'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper', 'L2ribAfi', '')])),
                                                            ('ip_address', (YLeaf(YType.str, 'ip-address'), ['str'])),
                                                            ('label', (YLeaf(YType.uint32, 'label'), ['int'])),
                                                            ('internal', (YLeaf(YType.boolean, 'internal'), ['bool'])),
                                                        ])
                                                        self.address_family = None
                                                        self.ip_address = None
                                                        self.label = None
                                                        self.internal = None
                                                        self._segment_path = lambda: "labeled"
                                                        self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/mac-details/mac-detail/mac-route/route/bmac/path-list/path-list-info/path-list-esi/mac-update-next-hop-array/next-hop/%s" % self._segment_path()
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Bmac.PathList.PathListInfo.PathListEsi.MacUpdateNextHopArray.NextHop.Labeled, ['address_family', 'ip_address', 'label', 'internal'], name, value)

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                                                        return meta._meta_table['L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Bmac.PathList.PathListInfo.PathListEsi.MacUpdateNextHopArray.NextHop.Labeled']['meta_info']

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                                                    return meta._meta_table['L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Bmac.PathList.PathListInfo.PathListEsi.MacUpdateNextHopArray.NextHop']['meta_info']

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                                                return meta._meta_table['L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Bmac.PathList.PathListInfo.PathListEsi.MacUpdateNextHopArray']['meta_info']

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                                            return meta._meta_table['L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Bmac.PathList.PathListInfo.PathListEsi']['meta_info']


                                    class PathListMac(_Entity_):
                                        """
                                        MAC Path List
                                        
                                        .. attribute:: mac_address
                                        
                                        	MAC Address
                                        	**type**\: str
                                        
                                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'l2rib-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Bmac.PathList.PathListInfo.PathListMac, self).__init__()

                                            self.yang_name = "path-list-mac"
                                            self.yang_parent_name = "path-list-info"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = False
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('mac_address', (YLeaf(YType.str, 'mac-address'), ['str'])),
                                            ])
                                            self.mac_address = None
                                            self._segment_path = lambda: "path-list-mac"
                                            self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/mac-details/mac-detail/mac-route/route/bmac/path-list/path-list-info/%s" % self._segment_path()
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Bmac.PathList.PathListInfo.PathListMac, ['mac_address'], name, value)

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                                            return meta._meta_table['L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Bmac.PathList.PathListInfo.PathListMac']['meta_info']

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                                        return meta._meta_table['L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Bmac.PathList.PathListInfo']['meta_info']


                                class NextHopArray(_Entity_):
                                    """
                                    Array of Next Hops for MAC Path List
                                    
                                    .. attribute:: next_hop
                                    
                                    	Next hop
                                    	**type**\:  :py:class:`NextHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Bmac.PathList.NextHopArray.NextHop>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: topology_id
                                    
                                    	Next\-hop TOPOLOGY ID
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: flags
                                    
                                    	Next\-hop flags
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'l2rib-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Bmac.PathList.NextHopArray, self).__init__()

                                        self.yang_name = "next-hop-array"
                                        self.yang_parent_name = "path-list"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = False
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("next-hop", ("next_hop", L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Bmac.PathList.NextHopArray.NextHop))])
                                        self._leafs = OrderedDict([
                                            ('topology_id', (YLeaf(YType.uint32, 'topology-id'), ['int'])),
                                            ('flags', (YLeaf(YType.uint16, 'flags'), ['int'])),
                                        ])
                                        self.topology_id = None
                                        self.flags = None

                                        self.next_hop = L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Bmac.PathList.NextHopArray.NextHop()
                                        self.next_hop.parent = self
                                        self._children_name_map["next_hop"] = "next-hop"
                                        self._segment_path = lambda: "next-hop-array"
                                        self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/mac-details/mac-detail/mac-route/route/bmac/path-list/%s" % self._segment_path()
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Bmac.PathList.NextHopArray, ['topology_id', 'flags'], name, value)


                                    class NextHop(_Entity_):
                                        """
                                        Next hop
                                        
                                        .. attribute:: labeled
                                        
                                        	Labeled Next Hop
                                        	**type**\:  :py:class:`Labeled <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Bmac.PathList.NextHopArray.NextHop.Labeled>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: type
                                        
                                        	Type
                                        	**type**\:  :py:class:`L2ribNextHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2ribNextHop>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: ipv4
                                        
                                        	IPV4 address Next Hop
                                        	**type**\: str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: ipv6
                                        
                                        	IPV6 address Next Hop
                                        	**type**\: str
                                        
                                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: mac
                                        
                                        	MAC address Next Hop
                                        	**type**\: str
                                        
                                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: interface_handle
                                        
                                        	Intefrace Handle Next Hop
                                        	**type**\: str
                                        
                                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: xid
                                        
                                        	XID Next Hop
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'l2rib-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Bmac.PathList.NextHopArray.NextHop, self).__init__()

                                            self.yang_name = "next-hop"
                                            self.yang_parent_name = "next-hop-array"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = False
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("labeled", ("labeled", L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Bmac.PathList.NextHopArray.NextHop.Labeled))])
                                            self._leafs = OrderedDict([
                                                ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper', 'L2ribNextHop', '')])),
                                                ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                                                ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                                                ('mac', (YLeaf(YType.str, 'mac'), ['str'])),
                                                ('interface_handle', (YLeaf(YType.str, 'interface-handle'), ['str'])),
                                                ('xid', (YLeaf(YType.uint32, 'xid'), ['int'])),
                                            ])
                                            self.type = None
                                            self.ipv4 = None
                                            self.ipv6 = None
                                            self.mac = None
                                            self.interface_handle = None
                                            self.xid = None

                                            self.labeled = L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Bmac.PathList.NextHopArray.NextHop.Labeled()
                                            self.labeled.parent = self
                                            self._children_name_map["labeled"] = "labeled"
                                            self._segment_path = lambda: "next-hop"
                                            self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/mac-details/mac-detail/mac-route/route/bmac/path-list/next-hop-array/%s" % self._segment_path()
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Bmac.PathList.NextHopArray.NextHop, ['type', 'ipv4', 'ipv6', 'mac', 'interface_handle', 'xid'], name, value)


                                        class Labeled(_Entity_):
                                            """
                                            Labeled Next Hop
                                            
                                            .. attribute:: address_family
                                            
                                            	L2RIB Address Family
                                            	**type**\:  :py:class:`L2ribAfi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2ribAfi>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: ip_address
                                            
                                            	IP Address
                                            	**type**\: str
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: label
                                            
                                            	Label
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: internal
                                            
                                            	Internal Label
                                            	**type**\: bool
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'l2rib-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Bmac.PathList.NextHopArray.NextHop.Labeled, self).__init__()

                                                self.yang_name = "labeled"
                                                self.yang_parent_name = "next-hop"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = False
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('address_family', (YLeaf(YType.enumeration, 'address-family'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper', 'L2ribAfi', '')])),
                                                    ('ip_address', (YLeaf(YType.str, 'ip-address'), ['str'])),
                                                    ('label', (YLeaf(YType.uint32, 'label'), ['int'])),
                                                    ('internal', (YLeaf(YType.boolean, 'internal'), ['bool'])),
                                                ])
                                                self.address_family = None
                                                self.ip_address = None
                                                self.label = None
                                                self.internal = None
                                                self._segment_path = lambda: "labeled"
                                                self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/mac-details/mac-detail/mac-route/route/bmac/path-list/next-hop-array/next-hop/%s" % self._segment_path()
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Bmac.PathList.NextHopArray.NextHop.Labeled, ['address_family', 'ip_address', 'label', 'internal'], name, value)

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                                                return meta._meta_table['L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Bmac.PathList.NextHopArray.NextHop.Labeled']['meta_info']

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                                            return meta._meta_table['L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Bmac.PathList.NextHopArray.NextHop']['meta_info']

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                                        return meta._meta_table['L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Bmac.PathList.NextHopArray']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                                    return meta._meta_table['L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Bmac.PathList']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                                return meta._meta_table['L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route.Bmac']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                            return meta._meta_table['L2rib.EviChildTables.MacDetails.MacDetail.MacRoute.Route']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                        return meta._meta_table['L2rib.EviChildTables.MacDetails.MacDetail.MacRoute']['meta_info']


                class RtTlv(_Entity_):
                    """
                    Mac Route Opaque Data TLV
                    
                    .. attribute:: tlv_type
                    
                    	TLV Type
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**config**\: False
                    
                    .. attribute:: tlv_len
                    
                    	TLV Length
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**config**\: False
                    
                    .. attribute:: tlv_val
                    
                    	TLV Value
                    	**type**\: list of  		 :py:class:`TlvVal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.MacDetails.MacDetail.RtTlv.TlvVal>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'l2rib-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(L2rib.EviChildTables.MacDetails.MacDetail.RtTlv, self).__init__()

                        self.yang_name = "rt-tlv"
                        self.yang_parent_name = "mac-detail"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("tlv-val", ("tlv_val", L2rib.EviChildTables.MacDetails.MacDetail.RtTlv.TlvVal))])
                        self._leafs = OrderedDict([
                            ('tlv_type', (YLeaf(YType.uint16, 'tlv-type'), ['int'])),
                            ('tlv_len', (YLeaf(YType.uint16, 'tlv-len'), ['int'])),
                        ])
                        self.tlv_type = None
                        self.tlv_len = None

                        self.tlv_val = YList(self)
                        self._segment_path = lambda: "rt-tlv"
                        self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/mac-details/mac-detail/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2rib.EviChildTables.MacDetails.MacDetail.RtTlv, ['tlv_type', 'tlv_len'], name, value)


                    class TlvVal(_Entity_):
                        """
                        TLV Value
                        
                        .. attribute:: entry
                        
                        	TLV Value
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'l2rib-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(L2rib.EviChildTables.MacDetails.MacDetail.RtTlv.TlvVal, self).__init__()

                            self.yang_name = "tlv-val"
                            self.yang_parent_name = "rt-tlv"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('entry', (YLeaf(YType.uint8, 'entry'), ['int'])),
                            ])
                            self.entry = None
                            self._segment_path = lambda: "tlv-val"
                            self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/mac-details/mac-detail/rt-tlv/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2rib.EviChildTables.MacDetails.MacDetail.RtTlv.TlvVal, ['entry'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                            return meta._meta_table['L2rib.EviChildTables.MacDetails.MacDetail.RtTlv.TlvVal']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                        return meta._meta_table['L2rib.EviChildTables.MacDetails.MacDetail.RtTlv']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                    return meta._meta_table['L2rib.EviChildTables.MacDetails.MacDetail']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                return meta._meta_table['L2rib.EviChildTables.MacDetails']['meta_info']


        class ImetDetails(_Entity_):
            """
            L2RIB EVPN EVI IMET Detail table
            
            .. attribute:: imet_detail
            
            	L2RIB EVPN IMET Detail table
            	**type**\: list of  		 :py:class:`ImetDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.ImetDetails.ImetDetail>`
            
            	**config**\: False
            
            

            """

            _prefix = 'l2rib-oper'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(L2rib.EviChildTables.ImetDetails, self).__init__()

                self.yang_name = "imet-details"
                self.yang_parent_name = "evi-child-tables"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("imet-detail", ("imet_detail", L2rib.EviChildTables.ImetDetails.ImetDetail))])
                self._leafs = OrderedDict()

                self.imet_detail = YList(self)
                self._segment_path = lambda: "imet-details"
                self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(L2rib.EviChildTables.ImetDetails, [], name, value)


            class ImetDetail(_Entity_):
                """
                L2RIB EVPN IMET Detail table
                
                .. attribute:: evi
                
                	EVPN ID
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: tag_id
                
                	Tag ID
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: ip_addr
                
                	Originating Router IP Address
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                	**config**\: False
                
                .. attribute:: prod_id
                
                	Producer ID
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: imet_route_base
                
                	Imet Route base information
                	**type**\:  :py:class:`ImetRouteBase <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.EviChildTables.ImetDetails.ImetDetail.ImetRouteBase>`
                
                	**config**\: False
                
                .. attribute:: tunnel_id
                
                	Tunnel Id
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: flags
                
                	IMET route flags
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: tunnel_type
                
                	IMET route tunnel type
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: l2r_label
                
                	Label
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: encap_type
                
                	Encap Type
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: last_update_timestamp
                
                	Last Update Timestamp
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                

                """

                _prefix = 'l2rib-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(L2rib.EviChildTables.ImetDetails.ImetDetail, self).__init__()

                    self.yang_name = "imet-detail"
                    self.yang_parent_name = "imet-details"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("imet-route-base", ("imet_route_base", L2rib.EviChildTables.ImetDetails.ImetDetail.ImetRouteBase))])
                    self._leafs = OrderedDict([
                        ('evi', (YLeaf(YType.uint32, 'evi'), ['int'])),
                        ('tag_id', (YLeaf(YType.uint32, 'tag-id'), ['int'])),
                        ('ip_addr', (YLeaf(YType.str, 'ip-addr'), ['str','str'])),
                        ('prod_id', (YLeaf(YType.uint32, 'prod-id'), ['int'])),
                        ('tunnel_id', (YLeaf(YType.str, 'tunnel-id'), ['str'])),
                        ('flags', (YLeaf(YType.uint32, 'flags'), ['int'])),
                        ('tunnel_type', (YLeaf(YType.uint32, 'tunnel-type'), ['int'])),
                        ('l2r_label', (YLeaf(YType.uint32, 'l2r-label'), ['int'])),
                        ('encap_type', (YLeaf(YType.uint32, 'encap-type'), ['int'])),
                        ('last_update_timestamp', (YLeaf(YType.uint64, 'last-update-timestamp'), ['int'])),
                    ])
                    self.evi = None
                    self.tag_id = None
                    self.ip_addr = None
                    self.prod_id = None
                    self.tunnel_id = None
                    self.flags = None
                    self.tunnel_type = None
                    self.l2r_label = None
                    self.encap_type = None
                    self.last_update_timestamp = None

                    self.imet_route_base = L2rib.EviChildTables.ImetDetails.ImetDetail.ImetRouteBase()
                    self.imet_route_base.parent = self
                    self._children_name_map["imet_route_base"] = "imet-route-base"
                    self._segment_path = lambda: "imet-detail"
                    self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/imet-details/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(L2rib.EviChildTables.ImetDetails.ImetDetail, ['evi', 'tag_id', 'ip_addr', 'prod_id', 'tunnel_id', 'flags', 'tunnel_type', 'l2r_label', 'encap_type', 'last_update_timestamp'], name, value)


                class ImetRouteBase(_Entity_):
                    """
                    Imet Route base information
                    
                    .. attribute:: vtepi_paddr
                    
                    	Originating Router IP Address
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: producer_id
                    
                    	Producer of Imet route
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: topo_id
                    
                    	Topo ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: ethernet_tag_id
                    
                    	Ethernet Tag ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'l2rib-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(L2rib.EviChildTables.ImetDetails.ImetDetail.ImetRouteBase, self).__init__()

                        self.yang_name = "imet-route-base"
                        self.yang_parent_name = "imet-detail"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('vtepi_paddr', (YLeaf(YType.str, 'vtepi-paddr'), ['str'])),
                            ('producer_id', (YLeaf(YType.uint8, 'producer-id'), ['int'])),
                            ('topo_id', (YLeaf(YType.uint32, 'topo-id'), ['int'])),
                            ('ethernet_tag_id', (YLeaf(YType.uint32, 'ethernet-tag-id'), ['int'])),
                        ])
                        self.vtepi_paddr = None
                        self.producer_id = None
                        self.topo_id = None
                        self.ethernet_tag_id = None
                        self._segment_path = lambda: "imet-route-base"
                        self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evi-child-tables/imet-details/imet-detail/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2rib.EviChildTables.ImetDetails.ImetDetail.ImetRouteBase, ['vtepi_paddr', 'producer_id', 'topo_id', 'ethernet_tag_id'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                        return meta._meta_table['L2rib.EviChildTables.ImetDetails.ImetDetail.ImetRouteBase']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                    return meta._meta_table['L2rib.EviChildTables.ImetDetails.ImetDetail']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                return meta._meta_table['L2rib.EviChildTables.ImetDetails']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
            return meta._meta_table['L2rib.EviChildTables']['meta_info']


    class Evis(_Entity_):
        """
        L2RIB EVPN EVI Table
        
        .. attribute:: evi
        
        	L2RIB EVPN EVI Entry
        	**type**\: list of  		 :py:class:`Evi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2rib_oper.L2rib.Evis.Evi>`
        
        	**config**\: False
        
        

        """

        _prefix = 'l2rib-oper'
        _revision = '2015-11-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(L2rib.Evis, self).__init__()

            self.yang_name = "evis"
            self.yang_parent_name = "l2rib"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("evi", ("evi", L2rib.Evis.Evi))])
            self._leafs = OrderedDict()

            self.evi = YList(self)
            self._segment_path = lambda: "evis"
            self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(L2rib.Evis, [], name, value)


        class Evi(_Entity_):
            """
            L2RIB EVPN EVI Entry
            
            .. attribute:: evi  (key)
            
            	EVI ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: topology_id
            
            	Topology ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: topology_name
            
            	Topology Name
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: topology_type
            
            	Topology Type
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'l2rib-oper'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(L2rib.Evis.Evi, self).__init__()

                self.yang_name = "evi"
                self.yang_parent_name = "evis"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['evi']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('evi', (YLeaf(YType.uint32, 'evi'), ['int'])),
                    ('topology_id', (YLeaf(YType.uint32, 'topology-id'), ['int'])),
                    ('topology_name', (YLeaf(YType.str, 'topology-name'), ['str'])),
                    ('topology_type', (YLeaf(YType.uint32, 'topology-type'), ['int'])),
                ])
                self.evi = None
                self.topology_id = None
                self.topology_name = None
                self.topology_type = None
                self._segment_path = lambda: "evi" + "[evi='" + str(self.evi) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-l2rib-oper:l2rib/evis/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(L2rib.Evis.Evi, ['evi', 'topology_id', 'topology_name', 'topology_type'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
                return meta._meta_table['L2rib.Evis.Evi']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
            return meta._meta_table['L2rib.Evis']['meta_info']

    def clone_ptr(self):
        self._top_entity = L2rib()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_l2rib_oper as meta
        return meta._meta_table['L2rib']['meta_info']


