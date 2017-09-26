""" Cisco_IOS_XR_tunnel_nve_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR tunnel\-nve package operational data.

This module contains definitions
for the following management objects\:
  nve\: NVE operational data

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Nve(Entity):
    """
    NVE operational data
    
    .. attribute:: interfaces
    
    	Table for NVE interface attributes
    	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_nve_oper.Nve.Interfaces>`
    
    .. attribute:: vnis
    
    	Table for VNIs
    	**type**\:   :py:class:`Vnis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_nve_oper.Nve.Vnis>`
    
    

    """

    _prefix = 'tunnel-nve-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Nve, self).__init__()
        self._top_entity = None

        self.yang_name = "nve"
        self.yang_parent_name = "Cisco-IOS-XR-tunnel-nve-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"interfaces" : ("interfaces", Nve.Interfaces), "vnis" : ("vnis", Nve.Vnis)}
        self._child_list_classes = {}

        self.interfaces = Nve.Interfaces()
        self.interfaces.parent = self
        self._children_name_map["interfaces"] = "interfaces"
        self._children_yang_names.add("interfaces")

        self.vnis = Nve.Vnis()
        self.vnis.parent = self
        self._children_name_map["vnis"] = "vnis"
        self._children_yang_names.add("vnis")
        self._segment_path = lambda: "Cisco-IOS-XR-tunnel-nve-oper:nve"


    class Interfaces(Entity):
        """
        Table for NVE interface attributes
        
        .. attribute:: interface
        
        	The attributes for a particular interface
        	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_nve_oper.Nve.Interfaces.Interface>`
        
        

        """

        _prefix = 'tunnel-nve-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Nve.Interfaces, self).__init__()

            self.yang_name = "interfaces"
            self.yang_parent_name = "nve"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"interface" : ("interface", Nve.Interfaces.Interface)}

            self.interface = YList(self)
            self._segment_path = lambda: "interfaces"
            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-nve-oper:nve/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Nve.Interfaces, [], name, value)


        class Interface(Entity):
            """
            The attributes for a particular interface
            
            .. attribute:: interface_name  <key>
            
            	Interface Name
            	**type**\:  str
            
            	**pattern:** [a\-zA\-Z0\-9./\-]+
            
            .. attribute:: admin_state
            
            	Admin State
            	**type**\:  int
            
            	**range:** \-128..127
            
            .. attribute:: any_cast_source_interface_name
            
            	Anycast Source Interface name
            	**type**\:  str
            
            .. attribute:: any_cast_source_ipv4_address
            
            	Anycast Source IPv4 Address
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: any_cast_source_state
            
            	Anycast Source Interface State
            	**type**\:  int
            
            	**range:** \-128..127
            
            .. attribute:: encap
            
            	Encap
            	**type**\:  int
            
            	**range:** \-128..127
            
            .. attribute:: flags
            
            	Flags
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: if_handle
            
            	NVE IfHandle
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: interface_name_xr
            
            	Interface name
            	**type**\:  str
            
            .. attribute:: source_interface_name
            
            	Source Interface name
            	**type**\:  str
            
            .. attribute:: source_ipv4_address
            
            	Source IPv4 Address
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: source_state
            
            	Source Intf State
            	**type**\:  int
            
            	**range:** \-128..127
            
            .. attribute:: state
            
            	State
            	**type**\:  int
            
            	**range:** \-128..127
            
            .. attribute:: sync_mcast_flags
            
            	Sync McastFlags
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sync_mcast_ipv4_address
            
            	MCAST sync group IPv4 Address
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: udp_port
            
            	UDP Port
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'tunnel-nve-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Nve.Interfaces.Interface, self).__init__()

                self.yang_name = "interface"
                self.yang_parent_name = "interfaces"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.interface_name = YLeaf(YType.str, "interface-name")

                self.admin_state = YLeaf(YType.int8, "admin-state")

                self.any_cast_source_interface_name = YLeaf(YType.str, "any-cast-source-interface-name")

                self.any_cast_source_ipv4_address = YLeaf(YType.str, "any-cast-source-ipv4-address")

                self.any_cast_source_state = YLeaf(YType.int8, "any-cast-source-state")

                self.encap = YLeaf(YType.int8, "encap")

                self.flags = YLeaf(YType.uint32, "flags")

                self.if_handle = YLeaf(YType.uint64, "if-handle")

                self.interface_name_xr = YLeaf(YType.str, "interface-name-xr")

                self.source_interface_name = YLeaf(YType.str, "source-interface-name")

                self.source_ipv4_address = YLeaf(YType.str, "source-ipv4-address")

                self.source_state = YLeaf(YType.int8, "source-state")

                self.state = YLeaf(YType.int8, "state")

                self.sync_mcast_flags = YLeaf(YType.uint32, "sync-mcast-flags")

                self.sync_mcast_ipv4_address = YLeaf(YType.str, "sync-mcast-ipv4-address")

                self.udp_port = YLeaf(YType.uint32, "udp-port")
                self._segment_path = lambda: "interface" + "[interface-name='" + self.interface_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-nve-oper:nve/interfaces/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Nve.Interfaces.Interface, ['interface_name', 'admin_state', 'any_cast_source_interface_name', 'any_cast_source_ipv4_address', 'any_cast_source_state', 'encap', 'flags', 'if_handle', 'interface_name_xr', 'source_interface_name', 'source_ipv4_address', 'source_state', 'state', 'sync_mcast_flags', 'sync_mcast_ipv4_address', 'udp_port'], name, value)


    class Vnis(Entity):
        """
        Table for VNIs
        
        .. attribute:: vni
        
        	The attributes for a particular VNI
        	**type**\: list of    :py:class:`Vni <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_nve_oper.Nve.Vnis.Vni>`
        
        

        """

        _prefix = 'tunnel-nve-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Nve.Vnis, self).__init__()

            self.yang_name = "vnis"
            self.yang_parent_name = "nve"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"vni" : ("vni", Nve.Vnis.Vni)}

            self.vni = YList(self)
            self._segment_path = lambda: "vnis"
            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-nve-oper:nve/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Nve.Vnis, [], name, value)


        class Vni(Entity):
            """
            The attributes for a particular VNI
            
            .. attribute:: vni  <key>
            
            	VNI ID
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: bvi_ifh
            
            	BVI Interface Handle
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: bvi_mac
            
            	BVI MAC address
            	**type**\:  str
            
            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
            
            .. attribute:: bvi_state
            
            	BVI Interface Oper State
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: flags
            
            	Flags
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: interface_name
            
            	NVE Interface name
            	**type**\:  str
            
            .. attribute:: ipv4_tbl_id
            
            	IPv4 Table ID
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipv6_tbl_id
            
            	IPv6 Table ID
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mcast_flags
            
            	McastFlags
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mcast_ipv4_address
            
            	MCAST IPv4 Address
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: state
            
            	State
            	**type**\:  int
            
            	**range:** \-128..127
            
            .. attribute:: topo_id
            
            	L2RIB Topology ID
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: topo_name
            
            	L2RIB Topology Name
            	**type**\:  str
            
            	**length:** 0..50
            
            .. attribute:: topo_valid
            
            	TOPO ID valid flag
            	**type**\:  bool
            
            .. attribute:: udp_port
            
            	UDP Port
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: vni_max
            
            	VNI Max in Range
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: vni_min
            
            	VNI Min in Range
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: vni_xr
            
            	VNI Number
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: vrf_id
            
            	L3 VRF ID
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: vrf_name
            
            	L3 VRF Name
            	**type**\:  str
            
            .. attribute:: vrf_vni
            
            	VRF VNI
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'tunnel-nve-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Nve.Vnis.Vni, self).__init__()

                self.yang_name = "vni"
                self.yang_parent_name = "vnis"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.vni = YLeaf(YType.str, "vni")

                self.bvi_ifh = YLeaf(YType.uint32, "bvi-ifh")

                self.bvi_mac = YLeaf(YType.str, "bvi-mac")

                self.bvi_state = YLeaf(YType.uint8, "bvi-state")

                self.flags = YLeaf(YType.uint32, "flags")

                self.interface_name = YLeaf(YType.str, "interface-name")

                self.ipv4_tbl_id = YLeaf(YType.uint32, "ipv4-tbl-id")

                self.ipv6_tbl_id = YLeaf(YType.uint32, "ipv6-tbl-id")

                self.mcast_flags = YLeaf(YType.uint32, "mcast-flags")

                self.mcast_ipv4_address = YLeaf(YType.str, "mcast-ipv4-address")

                self.state = YLeaf(YType.int8, "state")

                self.topo_id = YLeaf(YType.uint32, "topo-id")

                self.topo_name = YLeaf(YType.str, "topo-name")

                self.topo_valid = YLeaf(YType.boolean, "topo-valid")

                self.udp_port = YLeaf(YType.uint32, "udp-port")

                self.vni_max = YLeaf(YType.uint32, "vni-max")

                self.vni_min = YLeaf(YType.uint32, "vni-min")

                self.vni_xr = YLeaf(YType.uint32, "vni-xr")

                self.vrf_id = YLeaf(YType.uint32, "vrf-id")

                self.vrf_name = YLeaf(YType.str, "vrf-name")

                self.vrf_vni = YLeaf(YType.uint32, "vrf-vni")
                self._segment_path = lambda: "vni" + "[vni='" + self.vni.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-nve-oper:nve/vnis/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Nve.Vnis.Vni, ['vni', 'bvi_ifh', 'bvi_mac', 'bvi_state', 'flags', 'interface_name', 'ipv4_tbl_id', 'ipv6_tbl_id', 'mcast_flags', 'mcast_ipv4_address', 'state', 'topo_id', 'topo_name', 'topo_valid', 'udp_port', 'vni_max', 'vni_min', 'vni_xr', 'vrf_id', 'vrf_name', 'vrf_vni'], name, value)

    def clone_ptr(self):
        self._top_entity = Nve()
        return self._top_entity

