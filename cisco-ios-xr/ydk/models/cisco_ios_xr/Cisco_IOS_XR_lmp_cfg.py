""" Cisco_IOS_XR_lmp_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR lmp package configuration.

This module contains definitions
for the following management objects\:
  lmp\: Main common OLM/LMP configuration container

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class OlmAddr(Enum):
    """
    OlmAddr (Enum Class)

    Olm addr

    .. data:: ipv4 = 101

    	IPv4 address

    .. data:: ipv6 = 102

    	IPv6 address

    .. data:: unnumbered = 103

    	Unnumbered address

    .. data:: nsap = 104

    	NSAP address

    """

    ipv4 = Enum.YLeaf(101, "ipv4")

    ipv6 = Enum.YLeaf(102, "ipv6")

    unnumbered = Enum.YLeaf(103, "unnumbered")

    nsap = Enum.YLeaf(104, "nsap")


class OlmSwitchingCap(Enum):
    """
    OlmSwitchingCap (Enum Class)

    Olm switching cap

    .. data:: lsc = 150

    	Lambda switch capable

    .. data:: fsc = 200

    	Fiber switch capable

    """

    lsc = Enum.YLeaf(150, "lsc")

    fsc = Enum.YLeaf(200, "fsc")



class Lmp(Entity):
    """
    Main common OLM/LMP configuration container
    
    .. attribute:: gmpls_uni
    
    	GMPLS UNI specific OLM/LMP configuration
    	**type**\:  :py:class:`GmplsUni <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_cfg.Lmp.GmplsUni>`
    
    .. attribute:: enable
    
    	Enable the OLM/LMP application
    	**type**\: :py:class:`Empty<ydk.types.Empty>`
    
    

    """

    _prefix = 'lmp-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(Lmp, self).__init__()
        self._top_entity = None

        self.yang_name = "lmp"
        self.yang_parent_name = "Cisco-IOS-XR-lmp-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("gmpls-uni", ("gmpls_uni", Lmp.GmplsUni))])
        self._leafs = OrderedDict([
            ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
        ])
        self.enable = None

        self.gmpls_uni = Lmp.GmplsUni()
        self.gmpls_uni.parent = self
        self._children_name_map["gmpls_uni"] = "gmpls-uni"
        self._segment_path = lambda: "Cisco-IOS-XR-lmp-cfg:lmp"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Lmp, ['enable'], name, value)


    class GmplsUni(Entity):
        """
        GMPLS UNI specific OLM/LMP configuration
        
        .. attribute:: neighbors
        
        	Neighbor configuration
        	**type**\:  :py:class:`Neighbors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_cfg.Lmp.GmplsUni.Neighbors>`
        
        .. attribute:: router_id
        
        	Local GMPLS UNI router ID
        	**type**\:  :py:class:`RouterId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_cfg.Lmp.GmplsUni.RouterId>`
        
        	**presence node**\: True
        
        .. attribute:: controllers
        
        	Configure GMPLS UNI OLM/LMP controllers
        	**type**\:  :py:class:`Controllers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_cfg.Lmp.GmplsUni.Controllers>`
        
        

        """

        _prefix = 'lmp-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Lmp.GmplsUni, self).__init__()

            self.yang_name = "gmpls-uni"
            self.yang_parent_name = "lmp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("neighbors", ("neighbors", Lmp.GmplsUni.Neighbors)), ("router-id", ("router_id", Lmp.GmplsUni.RouterId)), ("controllers", ("controllers", Lmp.GmplsUni.Controllers))])
            self._leafs = OrderedDict()

            self.neighbors = Lmp.GmplsUni.Neighbors()
            self.neighbors.parent = self
            self._children_name_map["neighbors"] = "neighbors"

            self.router_id = None
            self._children_name_map["router_id"] = "router-id"

            self.controllers = Lmp.GmplsUni.Controllers()
            self.controllers.parent = self
            self._children_name_map["controllers"] = "controllers"
            self._segment_path = lambda: "gmpls-uni"
            self._absolute_path = lambda: "Cisco-IOS-XR-lmp-cfg:lmp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Lmp.GmplsUni, [], name, value)


        class Neighbors(Entity):
            """
            Neighbor configuration
            
            .. attribute:: neighbor
            
            	Neighbor configuration
            	**type**\: list of  		 :py:class:`Neighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_cfg.Lmp.GmplsUni.Neighbors.Neighbor>`
            
            

            """

            _prefix = 'lmp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Lmp.GmplsUni.Neighbors, self).__init__()

                self.yang_name = "neighbors"
                self.yang_parent_name = "gmpls-uni"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("neighbor", ("neighbor", Lmp.GmplsUni.Neighbors.Neighbor))])
                self._leafs = OrderedDict()

                self.neighbor = YList(self)
                self._segment_path = lambda: "neighbors"
                self._absolute_path = lambda: "Cisco-IOS-XR-lmp-cfg:lmp/gmpls-uni/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Lmp.GmplsUni.Neighbors, [], name, value)


            class Neighbor(Entity):
                """
                Neighbor configuration
                
                .. attribute:: neighbor_name  (key)
                
                	Neighbor name
                	**type**\: str
                
                	**length:** 1..64
                
                .. attribute:: ipcc
                
                	IPCC configuration
                	**type**\:  :py:class:`Ipcc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_cfg.Lmp.GmplsUni.Neighbors.Neighbor.Ipcc>`
                
                .. attribute:: enable
                
                	Neighbor creation
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: neighbor_router_id
                
                	Neighbor router ID (IPv4 Address)
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                

                """

                _prefix = 'lmp-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Lmp.GmplsUni.Neighbors.Neighbor, self).__init__()

                    self.yang_name = "neighbor"
                    self.yang_parent_name = "neighbors"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['neighbor_name']
                    self._child_classes = OrderedDict([("ipcc", ("ipcc", Lmp.GmplsUni.Neighbors.Neighbor.Ipcc))])
                    self._leafs = OrderedDict([
                        ('neighbor_name', (YLeaf(YType.str, 'neighbor-name'), ['str'])),
                        ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                        ('neighbor_router_id', (YLeaf(YType.str, 'neighbor-router-id'), ['str'])),
                    ])
                    self.neighbor_name = None
                    self.enable = None
                    self.neighbor_router_id = None

                    self.ipcc = Lmp.GmplsUni.Neighbors.Neighbor.Ipcc()
                    self.ipcc.parent = self
                    self._children_name_map["ipcc"] = "ipcc"
                    self._segment_path = lambda: "neighbor" + "[neighbor-name='" + str(self.neighbor_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-lmp-cfg:lmp/gmpls-uni/neighbors/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Lmp.GmplsUni.Neighbors.Neighbor, ['neighbor_name', 'enable', 'neighbor_router_id'], name, value)


                class Ipcc(Entity):
                    """
                    IPCC configuration
                    
                    .. attribute:: routed
                    
                    	Routed IPCC configuration
                    	**type**\:  :py:class:`Routed <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_cfg.Lmp.GmplsUni.Neighbors.Neighbor.Ipcc.Routed>`
                    
                    

                    """

                    _prefix = 'lmp-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Lmp.GmplsUni.Neighbors.Neighbor.Ipcc, self).__init__()

                        self.yang_name = "ipcc"
                        self.yang_parent_name = "neighbor"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("routed", ("routed", Lmp.GmplsUni.Neighbors.Neighbor.Ipcc.Routed))])
                        self._leafs = OrderedDict()

                        self.routed = Lmp.GmplsUni.Neighbors.Neighbor.Ipcc.Routed()
                        self.routed.parent = self
                        self._children_name_map["routed"] = "routed"
                        self._segment_path = lambda: "ipcc"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Lmp.GmplsUni.Neighbors.Neighbor.Ipcc, [], name, value)


                    class Routed(Entity):
                        """
                        Routed IPCC configuration
                        
                        .. attribute:: enable
                        
                        	Routed IPCC creation
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'lmp-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Lmp.GmplsUni.Neighbors.Neighbor.Ipcc.Routed, self).__init__()

                            self.yang_name = "routed"
                            self.yang_parent_name = "ipcc"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                            ])
                            self.enable = None
                            self._segment_path = lambda: "routed"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Lmp.GmplsUni.Neighbors.Neighbor.Ipcc.Routed, ['enable'], name, value)


        class RouterId(Entity):
            """
            Local GMPLS UNI router ID
            
            .. attribute:: interface_name
            
            	Name of interface
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
            
            .. attribute:: address
            
            	Local router ID (IPv4 Address)
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'lmp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Lmp.GmplsUni.RouterId, self).__init__()

                self.yang_name = "router-id"
                self.yang_parent_name = "gmpls-uni"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self.is_presence_container = True
                self._leafs = OrderedDict([
                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                    ('address', (YLeaf(YType.str, 'address'), ['str'])),
                ])
                self.interface_name = None
                self.address = None
                self._segment_path = lambda: "router-id"
                self._absolute_path = lambda: "Cisco-IOS-XR-lmp-cfg:lmp/gmpls-uni/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Lmp.GmplsUni.RouterId, ['interface_name', 'address'], name, value)


        class Controllers(Entity):
            """
            Configure GMPLS UNI OLM/LMP controllers
            
            .. attribute:: controller
            
            	Configure an GMPLS UNI OLM/LMP contoller
            	**type**\: list of  		 :py:class:`Controller <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_cfg.Lmp.GmplsUni.Controllers.Controller>`
            
            

            """

            _prefix = 'lmp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Lmp.GmplsUni.Controllers, self).__init__()

                self.yang_name = "controllers"
                self.yang_parent_name = "gmpls-uni"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("controller", ("controller", Lmp.GmplsUni.Controllers.Controller))])
                self._leafs = OrderedDict()

                self.controller = YList(self)
                self._segment_path = lambda: "controllers"
                self._absolute_path = lambda: "Cisco-IOS-XR-lmp-cfg:lmp/gmpls-uni/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Lmp.GmplsUni.Controllers, [], name, value)


            class Controller(Entity):
                """
                Configure an GMPLS UNI OLM/LMP contoller
                
                .. attribute:: controller_name  (key)
                
                	Controller name
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                .. attribute:: local_link_id
                
                	Local Link ID configuration
                	**type**\:  :py:class:`LocalLinkId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_cfg.Lmp.GmplsUni.Controllers.Controller.LocalLinkId>`
                
                .. attribute:: adjacency
                
                	Neighbor controller adjacency configuration
                	**type**\:  :py:class:`Adjacency <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_cfg.Lmp.GmplsUni.Controllers.Controller.Adjacency>`
                
                .. attribute:: enable
                
                	Enable the OLM/LMP application on this controller
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'lmp-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Lmp.GmplsUni.Controllers.Controller, self).__init__()

                    self.yang_name = "controller"
                    self.yang_parent_name = "controllers"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['controller_name']
                    self._child_classes = OrderedDict([("local-link-id", ("local_link_id", Lmp.GmplsUni.Controllers.Controller.LocalLinkId)), ("adjacency", ("adjacency", Lmp.GmplsUni.Controllers.Controller.Adjacency))])
                    self._leafs = OrderedDict([
                        ('controller_name', (YLeaf(YType.str, 'controller-name'), ['str'])),
                        ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                    ])
                    self.controller_name = None
                    self.enable = None

                    self.local_link_id = Lmp.GmplsUni.Controllers.Controller.LocalLinkId()
                    self.local_link_id.parent = self
                    self._children_name_map["local_link_id"] = "local-link-id"

                    self.adjacency = Lmp.GmplsUni.Controllers.Controller.Adjacency()
                    self.adjacency.parent = self
                    self._children_name_map["adjacency"] = "adjacency"
                    self._segment_path = lambda: "controller" + "[controller-name='" + str(self.controller_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-lmp-cfg:lmp/gmpls-uni/controllers/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Lmp.GmplsUni.Controllers.Controller, ['controller_name', 'enable'], name, value)


                class LocalLinkId(Entity):
                    """
                    Local Link ID configuration
                    
                    .. attribute:: address_type
                    
                    	Local link ID address type
                    	**type**\:  :py:class:`OlmAddr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_cfg.OlmAddr>`
                    
                    .. attribute:: unnumbered
                    
                    	Local address unnumbered 
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: address
                    
                    	Local link ID address IPv4
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'lmp-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Lmp.GmplsUni.Controllers.Controller.LocalLinkId, self).__init__()

                        self.yang_name = "local-link-id"
                        self.yang_parent_name = "controller"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('address_type', (YLeaf(YType.enumeration, 'address-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_cfg', 'OlmAddr', '')])),
                            ('unnumbered', (YLeaf(YType.uint32, 'unnumbered'), ['int'])),
                            ('address', (YLeaf(YType.str, 'address'), ['str'])),
                        ])
                        self.address_type = None
                        self.unnumbered = None
                        self.address = None
                        self._segment_path = lambda: "local-link-id"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Lmp.GmplsUni.Controllers.Controller.LocalLinkId, ['address_type', 'unnumbered', 'address'], name, value)


                class Adjacency(Entity):
                    """
                    Neighbor controller adjacency configuration
                    
                    .. attribute:: remote_neighbor
                    
                    	Neighbor data
                    	**type**\:  :py:class:`RemoteNeighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_cfg.Lmp.GmplsUni.Controllers.Controller.Adjacency.RemoteNeighbor>`
                    
                    

                    """

                    _prefix = 'lmp-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Lmp.GmplsUni.Controllers.Controller.Adjacency, self).__init__()

                        self.yang_name = "adjacency"
                        self.yang_parent_name = "controller"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("remote-neighbor", ("remote_neighbor", Lmp.GmplsUni.Controllers.Controller.Adjacency.RemoteNeighbor))])
                        self._leafs = OrderedDict()

                        self.remote_neighbor = Lmp.GmplsUni.Controllers.Controller.Adjacency.RemoteNeighbor()
                        self.remote_neighbor.parent = self
                        self._children_name_map["remote_neighbor"] = "remote-neighbor"
                        self._segment_path = lambda: "adjacency"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Lmp.GmplsUni.Controllers.Controller.Adjacency, [], name, value)


                    class RemoteNeighbor(Entity):
                        """
                        Neighbor data
                        
                        .. attribute:: interface_id
                        
                        	Neighbor Interface ID configuration
                        	**type**\:  :py:class:`InterfaceId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_cfg.Lmp.GmplsUni.Controllers.Controller.Adjacency.RemoteNeighbor.InterfaceId>`
                        
                        .. attribute:: link_id
                        
                        	Neighbor Link ID configuration
                        	**type**\:  :py:class:`LinkId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_cfg.Lmp.GmplsUni.Controllers.Controller.Adjacency.RemoteNeighbor.LinkId>`
                        
                        .. attribute:: neighbor_association
                        
                        	Create LMP controller to neighbor association
                        	**type**\: str
                        
                        	**length:** 1..64
                        
                        .. attribute:: link_switching_capability
                        
                        	Neighbor link switching capability configuration
                        	**type**\:  :py:class:`OlmSwitchingCap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_cfg.OlmSwitchingCap>`
                        
                        	**default value**\: lsc
                        
                        .. attribute:: flexi_grid_capable
                        
                        	Remote node flexi grid capability 
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'lmp-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Lmp.GmplsUni.Controllers.Controller.Adjacency.RemoteNeighbor, self).__init__()

                            self.yang_name = "remote-neighbor"
                            self.yang_parent_name = "adjacency"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("interface-id", ("interface_id", Lmp.GmplsUni.Controllers.Controller.Adjacency.RemoteNeighbor.InterfaceId)), ("link-id", ("link_id", Lmp.GmplsUni.Controllers.Controller.Adjacency.RemoteNeighbor.LinkId))])
                            self._leafs = OrderedDict([
                                ('neighbor_association', (YLeaf(YType.str, 'neighbor-association'), ['str'])),
                                ('link_switching_capability', (YLeaf(YType.enumeration, 'link-switching-capability'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_cfg', 'OlmSwitchingCap', '')])),
                                ('flexi_grid_capable', (YLeaf(YType.uint32, 'flexi-grid-capable'), ['int'])),
                            ])
                            self.neighbor_association = None
                            self.link_switching_capability = None
                            self.flexi_grid_capable = None

                            self.interface_id = Lmp.GmplsUni.Controllers.Controller.Adjacency.RemoteNeighbor.InterfaceId()
                            self.interface_id.parent = self
                            self._children_name_map["interface_id"] = "interface-id"

                            self.link_id = Lmp.GmplsUni.Controllers.Controller.Adjacency.RemoteNeighbor.LinkId()
                            self.link_id.parent = self
                            self._children_name_map["link_id"] = "link-id"
                            self._segment_path = lambda: "remote-neighbor"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Lmp.GmplsUni.Controllers.Controller.Adjacency.RemoteNeighbor, ['neighbor_association', 'link_switching_capability', 'flexi_grid_capable'], name, value)


                        class InterfaceId(Entity):
                            """
                            Neighbor Interface ID configuration
                            
                            .. attribute:: address_type
                            
                            	Local link ID address type
                            	**type**\:  :py:class:`OlmAddr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_cfg.OlmAddr>`
                            
                            .. attribute:: unnumbered
                            
                            	Local address unnumbered 
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: address
                            
                            	Local link ID address IPv4
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'lmp-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Lmp.GmplsUni.Controllers.Controller.Adjacency.RemoteNeighbor.InterfaceId, self).__init__()

                                self.yang_name = "interface-id"
                                self.yang_parent_name = "remote-neighbor"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('address_type', (YLeaf(YType.enumeration, 'address-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_cfg', 'OlmAddr', '')])),
                                    ('unnumbered', (YLeaf(YType.uint32, 'unnumbered'), ['int'])),
                                    ('address', (YLeaf(YType.str, 'address'), ['str'])),
                                ])
                                self.address_type = None
                                self.unnumbered = None
                                self.address = None
                                self._segment_path = lambda: "interface-id"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Lmp.GmplsUni.Controllers.Controller.Adjacency.RemoteNeighbor.InterfaceId, ['address_type', 'unnumbered', 'address'], name, value)


                        class LinkId(Entity):
                            """
                            Neighbor Link ID configuration
                            
                            .. attribute:: address_type
                            
                            	Neighbor link ID address type
                            	**type**\:  :py:class:`OlmAddr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_cfg.OlmAddr>`
                            
                            .. attribute:: unnumbered
                            
                            	Neighbor address unnumbered [Not supported]
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: address
                            
                            	Neighbor ID address IPv4
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'lmp-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Lmp.GmplsUni.Controllers.Controller.Adjacency.RemoteNeighbor.LinkId, self).__init__()

                                self.yang_name = "link-id"
                                self.yang_parent_name = "remote-neighbor"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('address_type', (YLeaf(YType.enumeration, 'address-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_cfg', 'OlmAddr', '')])),
                                    ('unnumbered', (YLeaf(YType.uint32, 'unnumbered'), ['int'])),
                                    ('address', (YLeaf(YType.str, 'address'), ['str'])),
                                ])
                                self.address_type = None
                                self.unnumbered = None
                                self.address = None
                                self._segment_path = lambda: "link-id"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Lmp.GmplsUni.Controllers.Controller.Adjacency.RemoteNeighbor.LinkId, ['address_type', 'unnumbered', 'address'], name, value)

    def clone_ptr(self):
        self._top_entity = Lmp()
        return self._top_entity

