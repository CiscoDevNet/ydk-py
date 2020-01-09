""" Cisco_IOS_XR_tunnel_nve_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR tunnel\-nve package operational data.

This module contains definitions
for the following management objects\:
  nve\: NVE operational data

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




class Nve(_Entity_):
    """
    NVE operational data
    
    .. attribute:: vnis
    
    	Table for VNIs
    	**type**\:  :py:class:`Vnis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_nve_oper.Nve.Vnis>`
    
    	**config**\: False
    
    .. attribute:: interfaces
    
    	Table for NVE interface attributes
    	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_nve_oper.Nve.Interfaces>`
    
    	**config**\: False
    
    

    """

    _prefix = 'tunnel-nve-oper'
    _revision = '2015-11-09'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(Nve, self).__init__()
        self._top_entity = None

        self.yang_name = "nve"
        self.yang_parent_name = "Cisco-IOS-XR-tunnel-nve-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("vnis", ("vnis", Nve.Vnis)), ("interfaces", ("interfaces", Nve.Interfaces))])
        self._leafs = OrderedDict()

        self.vnis = Nve.Vnis()
        self.vnis.parent = self
        self._children_name_map["vnis"] = "vnis"

        self.interfaces = Nve.Interfaces()
        self.interfaces.parent = self
        self._children_name_map["interfaces"] = "interfaces"
        self._segment_path = lambda: "Cisco-IOS-XR-tunnel-nve-oper:nve"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Nve, [], name, value)


    class Vnis(_Entity_):
        """
        Table for VNIs
        
        .. attribute:: vni
        
        	The attributes for a particular VNI
        	**type**\: list of  		 :py:class:`Vni <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_nve_oper.Nve.Vnis.Vni>`
        
        	**config**\: False
        
        

        """

        _prefix = 'tunnel-nve-oper'
        _revision = '2015-11-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Nve.Vnis, self).__init__()

            self.yang_name = "vnis"
            self.yang_parent_name = "nve"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("vni", ("vni", Nve.Vnis.Vni))])
            self._leafs = OrderedDict()

            self.vni = YList(self)
            self._segment_path = lambda: "vnis"
            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-nve-oper:nve/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Nve.Vnis, [], name, value)


        class Vni(_Entity_):
            """
            The attributes for a particular VNI
            
            .. attribute:: vni  (key)
            
            	VNI ID
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            	**config**\: False
            
            .. attribute:: interface_name
            
            	NVE Interface name
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: vni_xr
            
            	VNI Number
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: state
            
            	State
            	**type**\: int
            
            	**range:** \-128..127
            
            	**config**\: False
            
            .. attribute:: mcast_ipv4_address
            
            	MCAST IPv4 Address
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**config**\: False
            
            .. attribute:: flags
            
            	Flags
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: vni_min
            
            	VNI Min in Range
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: vni_max
            
            	VNI Max in Range
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: mcast_flags
            
            	McastFlags
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: udp_port
            
            	UDP Port
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: bvi_ifh
            
            	BVI Interface Handle
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: bvi_state
            
            	BVI Interface Oper State
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: bvi_mac
            
            	BVI MAC address
            	**type**\: str
            
            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
            
            	**config**\: False
            
            .. attribute:: vrf_name
            
            	L3 VRF Name
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: vrf_id
            
            	L3 VRF ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: ipv4_tbl_id
            
            	IPv4 Table ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: ipv6_tbl_id
            
            	IPv6 Table ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: vrf_vni
            
            	VRF VNI
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: topo_valid
            
            	TOPO ID valid flag
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: topo_id
            
            	L2RIB Topology ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: topo_name
            
            	L2RIB Topology Name
            	**type**\: str
            
            	**length:** 0..50
            
            	**config**\: False
            
            

            """

            _prefix = 'tunnel-nve-oper'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Nve.Vnis.Vni, self).__init__()

                self.yang_name = "vni"
                self.yang_parent_name = "vnis"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['vni']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('vni', (YLeaf(YType.str, 'vni'), ['str'])),
                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                    ('vni_xr', (YLeaf(YType.uint32, 'vni-xr'), ['int'])),
                    ('state', (YLeaf(YType.int8, 'state'), ['int'])),
                    ('mcast_ipv4_address', (YLeaf(YType.str, 'mcast-ipv4-address'), ['str'])),
                    ('flags', (YLeaf(YType.uint32, 'flags'), ['int'])),
                    ('vni_min', (YLeaf(YType.uint32, 'vni-min'), ['int'])),
                    ('vni_max', (YLeaf(YType.uint32, 'vni-max'), ['int'])),
                    ('mcast_flags', (YLeaf(YType.uint32, 'mcast-flags'), ['int'])),
                    ('udp_port', (YLeaf(YType.uint32, 'udp-port'), ['int'])),
                    ('bvi_ifh', (YLeaf(YType.uint32, 'bvi-ifh'), ['int'])),
                    ('bvi_state', (YLeaf(YType.uint8, 'bvi-state'), ['int'])),
                    ('bvi_mac', (YLeaf(YType.str, 'bvi-mac'), ['str'])),
                    ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                    ('vrf_id', (YLeaf(YType.uint32, 'vrf-id'), ['int'])),
                    ('ipv4_tbl_id', (YLeaf(YType.uint32, 'ipv4-tbl-id'), ['int'])),
                    ('ipv6_tbl_id', (YLeaf(YType.uint32, 'ipv6-tbl-id'), ['int'])),
                    ('vrf_vni', (YLeaf(YType.uint32, 'vrf-vni'), ['int'])),
                    ('topo_valid', (YLeaf(YType.boolean, 'topo-valid'), ['bool'])),
                    ('topo_id', (YLeaf(YType.uint32, 'topo-id'), ['int'])),
                    ('topo_name', (YLeaf(YType.str, 'topo-name'), ['str'])),
                ])
                self.vni = None
                self.interface_name = None
                self.vni_xr = None
                self.state = None
                self.mcast_ipv4_address = None
                self.flags = None
                self.vni_min = None
                self.vni_max = None
                self.mcast_flags = None
                self.udp_port = None
                self.bvi_ifh = None
                self.bvi_state = None
                self.bvi_mac = None
                self.vrf_name = None
                self.vrf_id = None
                self.ipv4_tbl_id = None
                self.ipv6_tbl_id = None
                self.vrf_vni = None
                self.topo_valid = None
                self.topo_id = None
                self.topo_name = None
                self._segment_path = lambda: "vni" + "[vni='" + str(self.vni) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-nve-oper:nve/vnis/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Nve.Vnis.Vni, ['vni', 'interface_name', 'vni_xr', 'state', 'mcast_ipv4_address', 'flags', 'vni_min', 'vni_max', 'mcast_flags', 'udp_port', 'bvi_ifh', 'bvi_state', 'bvi_mac', 'vrf_name', 'vrf_id', 'ipv4_tbl_id', 'ipv6_tbl_id', 'vrf_vni', 'topo_valid', 'topo_id', 'topo_name'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_nve_oper as meta
                return meta._meta_table['Nve.Vnis.Vni']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_nve_oper as meta
            return meta._meta_table['Nve.Vnis']['meta_info']


    class Interfaces(_Entity_):
        """
        Table for NVE interface attributes
        
        .. attribute:: interface
        
        	The attributes for a particular interface
        	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_nve_oper.Nve.Interfaces.Interface>`
        
        	**config**\: False
        
        

        """

        _prefix = 'tunnel-nve-oper'
        _revision = '2015-11-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Nve.Interfaces, self).__init__()

            self.yang_name = "interfaces"
            self.yang_parent_name = "nve"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("interface", ("interface", Nve.Interfaces.Interface))])
            self._leafs = OrderedDict()

            self.interface = YList(self)
            self._segment_path = lambda: "interfaces"
            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-nve-oper:nve/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Nve.Interfaces, [], name, value)


        class Interface(_Entity_):
            """
            The attributes for a particular interface
            
            .. attribute:: interface_name  (key)
            
            	Interface Name
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
            
            	**config**\: False
            
            .. attribute:: interface_name_xr
            
            	Interface name
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: state
            
            	State
            	**type**\: int
            
            	**range:** \-128..127
            
            	**config**\: False
            
            .. attribute:: admin_state
            
            	Admin State
            	**type**\: int
            
            	**range:** \-128..127
            
            	**config**\: False
            
            .. attribute:: flags
            
            	Flags
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: encap
            
            	Encap
            	**type**\: int
            
            	**range:** \-128..127
            
            	**config**\: False
            
            .. attribute:: source_interface_name
            
            	Source Interface name
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: source_ipv4_address
            
            	Source IPv4 Address
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**config**\: False
            
            .. attribute:: if_handle
            
            	NVE IfHandle
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            .. attribute:: source_state
            
            	Source Intf State
            	**type**\: int
            
            	**range:** \-128..127
            
            	**config**\: False
            
            .. attribute:: udp_port
            
            	UDP Port
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: any_cast_source_interface_name
            
            	Anycast Source Interface name
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: any_cast_source_ipv4_address
            
            	Anycast Source IPv4 Address
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**config**\: False
            
            .. attribute:: any_cast_source_state
            
            	Anycast Source Interface State
            	**type**\: int
            
            	**range:** \-128..127
            
            	**config**\: False
            
            .. attribute:: sync_mcast_ipv4_address
            
            	MCAST sync group IPv4 Address
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**config**\: False
            
            .. attribute:: sync_mcast_flags
            
            	Sync McastFlags
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'tunnel-nve-oper'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Nve.Interfaces.Interface, self).__init__()

                self.yang_name = "interface"
                self.yang_parent_name = "interfaces"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['interface_name']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                    ('interface_name_xr', (YLeaf(YType.str, 'interface-name-xr'), ['str'])),
                    ('state', (YLeaf(YType.int8, 'state'), ['int'])),
                    ('admin_state', (YLeaf(YType.int8, 'admin-state'), ['int'])),
                    ('flags', (YLeaf(YType.uint32, 'flags'), ['int'])),
                    ('encap', (YLeaf(YType.int8, 'encap'), ['int'])),
                    ('source_interface_name', (YLeaf(YType.str, 'source-interface-name'), ['str'])),
                    ('source_ipv4_address', (YLeaf(YType.str, 'source-ipv4-address'), ['str'])),
                    ('if_handle', (YLeaf(YType.uint64, 'if-handle'), ['int'])),
                    ('source_state', (YLeaf(YType.int8, 'source-state'), ['int'])),
                    ('udp_port', (YLeaf(YType.uint32, 'udp-port'), ['int'])),
                    ('any_cast_source_interface_name', (YLeaf(YType.str, 'any-cast-source-interface-name'), ['str'])),
                    ('any_cast_source_ipv4_address', (YLeaf(YType.str, 'any-cast-source-ipv4-address'), ['str'])),
                    ('any_cast_source_state', (YLeaf(YType.int8, 'any-cast-source-state'), ['int'])),
                    ('sync_mcast_ipv4_address', (YLeaf(YType.str, 'sync-mcast-ipv4-address'), ['str'])),
                    ('sync_mcast_flags', (YLeaf(YType.uint32, 'sync-mcast-flags'), ['int'])),
                ])
                self.interface_name = None
                self.interface_name_xr = None
                self.state = None
                self.admin_state = None
                self.flags = None
                self.encap = None
                self.source_interface_name = None
                self.source_ipv4_address = None
                self.if_handle = None
                self.source_state = None
                self.udp_port = None
                self.any_cast_source_interface_name = None
                self.any_cast_source_ipv4_address = None
                self.any_cast_source_state = None
                self.sync_mcast_ipv4_address = None
                self.sync_mcast_flags = None
                self._segment_path = lambda: "interface" + "[interface-name='" + str(self.interface_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-nve-oper:nve/interfaces/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Nve.Interfaces.Interface, ['interface_name', 'interface_name_xr', 'state', 'admin_state', 'flags', 'encap', 'source_interface_name', 'source_ipv4_address', 'if_handle', 'source_state', 'udp_port', 'any_cast_source_interface_name', 'any_cast_source_ipv4_address', 'any_cast_source_state', 'sync_mcast_ipv4_address', 'sync_mcast_flags'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_nve_oper as meta
                return meta._meta_table['Nve.Interfaces.Interface']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_nve_oper as meta
            return meta._meta_table['Nve.Interfaces']['meta_info']

    def clone_ptr(self):
        self._top_entity = Nve()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_nve_oper as meta
        return meta._meta_table['Nve']['meta_info']


