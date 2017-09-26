""" Cisco_IOS_XR_ipv4_ospf_act 

This module contains a collection of YANG definitions
for Cisco IOS\-XR OSPF action package configuration.

Copyright (c) 2016\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class ClearOspfInstanceVrf(Entity):
    """
    Clear one or more non\-default OSPF VRFs in process
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ClearOspfInstanceVrf.Input>`
    
    

    """

    _prefix = 'ospf-act'
    _revision = '2016-09-14'

    def __init__(self):
        super(ClearOspfInstanceVrf, self).__init__()
        self._top_entity = None

        self.yang_name = "clear-ospf-instance-vrf"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-ospf-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {}
        self._child_list_classes = {}

        self.input = ClearOspfInstanceVrf.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")
        self._segment_path = lambda: "Cisco-IOS-XR-ipv4-ospf-act:clear-ospf-instance-vrf"


    class Input(Entity):
        """
        
        
        .. attribute:: instance
        
        	OSPF instance name
        	**type**\:   :py:class:`Instance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ClearOspfInstanceVrf.Input.Instance>`
        
        

        """

        _prefix = 'ospf-act'
        _revision = '2016-09-14'

        def __init__(self):
            super(ClearOspfInstanceVrf.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "clear-ospf-instance-vrf"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"instance" : ("instance", ClearOspfInstanceVrf.Input.Instance)}
            self._child_list_classes = {}

            self.instance = ClearOspfInstanceVrf.Input.Instance()
            self.instance.parent = self
            self._children_name_map["instance"] = "instance"
            self._children_yang_names.add("instance")
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-ospf-act:clear-ospf-instance-vrf/%s" % self._segment_path()


        class Instance(Entity):
            """
            OSPF instance name
            
            .. attribute:: all
            
            	Clear all non\-default OSPF VRFs
            	**type**\:   :py:class:`All <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ClearOspfInstanceVrf.Input.Instance.All>`
            
            .. attribute:: all_inclusive
            
            	Clear all non\-default and default OSPF VRFs
            	**type**\:   :py:class:`AllInclusive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ClearOspfInstanceVrf.Input.Instance.AllInclusive>`
            
            .. attribute:: instance_identifier
            
            	OSPF process instance identifier
            	**type**\:  str
            
            	**mandatory**\: True
            
            .. attribute:: vrf
            
            	Clear one or more non\-default OSPF VRFs in process
            	**type**\:   :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ClearOspfInstanceVrf.Input.Instance.Vrf>`
            
            

            """

            _prefix = 'ospf-act'
            _revision = '2016-09-14'

            def __init__(self):
                super(ClearOspfInstanceVrf.Input.Instance, self).__init__()

                self.yang_name = "instance"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"all" : ("all", ClearOspfInstanceVrf.Input.Instance.All), "all-inclusive" : ("all_inclusive", ClearOspfInstanceVrf.Input.Instance.AllInclusive), "vrf" : ("vrf", ClearOspfInstanceVrf.Input.Instance.Vrf)}
                self._child_list_classes = {}

                self.instance_identifier = YLeaf(YType.str, "instance-identifier")

                self.all = ClearOspfInstanceVrf.Input.Instance.All()
                self.all.parent = self
                self._children_name_map["all"] = "all"
                self._children_yang_names.add("all")

                self.all_inclusive = ClearOspfInstanceVrf.Input.Instance.AllInclusive()
                self.all_inclusive.parent = self
                self._children_name_map["all_inclusive"] = "all-inclusive"
                self._children_yang_names.add("all-inclusive")

                self.vrf = ClearOspfInstanceVrf.Input.Instance.Vrf()
                self.vrf.parent = self
                self._children_name_map["vrf"] = "vrf"
                self._children_yang_names.add("vrf")
                self._segment_path = lambda: "instance"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-ospf-act:clear-ospf-instance-vrf/input/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(ClearOspfInstanceVrf.Input.Instance, ['instance_identifier'], name, value)


            class All(Entity):
                """
                Clear all non\-default OSPF VRFs
                
                .. attribute:: process
                
                	Reset OSPF process
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: redistribution
                
                	Clear OSPF route redistrbution
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: route
                
                	Clear OSPF route table
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: stats
                
                	OSPF counters and statistics
                	**type**\:   :py:class:`Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ClearOspfInstanceVrf.Input.Instance.All.Stats>`
                
                

                """

                _prefix = 'ospf-act'
                _revision = '2016-09-14'

                def __init__(self):
                    super(ClearOspfInstanceVrf.Input.Instance.All, self).__init__()

                    self.yang_name = "all"
                    self.yang_parent_name = "instance"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"stats" : ("stats", ClearOspfInstanceVrf.Input.Instance.All.Stats)}
                    self._child_list_classes = {}

                    self.process = YLeaf(YType.empty, "process")

                    self.redistribution = YLeaf(YType.empty, "redistribution")

                    self.route = YLeaf(YType.empty, "route")

                    self.stats = ClearOspfInstanceVrf.Input.Instance.All.Stats()
                    self.stats.parent = self
                    self._children_name_map["stats"] = "stats"
                    self._children_yang_names.add("stats")
                    self._segment_path = lambda: "all"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-ospf-act:clear-ospf-instance-vrf/input/instance/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(ClearOspfInstanceVrf.Input.Instance.All, ['process', 'redistribution', 'route'], name, value)


                class Stats(Entity):
                    """
                    OSPF counters and statistics
                    
                    .. attribute:: interface
                    
                    	OSPF interface statistics
                    	**type**\:   :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ClearOspfInstanceVrf.Input.Instance.All.Stats.Interface>`
                    
                    .. attribute:: message_queue
                    
                    	Message\-queue statistics
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: neighbor
                    
                    	Neighbor statistics per interface or neighbor id
                    	**type**\:   :py:class:`Neighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ClearOspfInstanceVrf.Input.Instance.All.Stats.Neighbor>`
                    
                    .. attribute:: spf
                    
                    	SPF statistics
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'ospf-act'
                    _revision = '2016-09-14'

                    def __init__(self):
                        super(ClearOspfInstanceVrf.Input.Instance.All.Stats, self).__init__()

                        self.yang_name = "stats"
                        self.yang_parent_name = "all"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"interface" : ("interface", ClearOspfInstanceVrf.Input.Instance.All.Stats.Interface), "neighbor" : ("neighbor", ClearOspfInstanceVrf.Input.Instance.All.Stats.Neighbor)}
                        self._child_list_classes = {}

                        self.message_queue = YLeaf(YType.empty, "message-queue")

                        self.spf = YLeaf(YType.empty, "spf")

                        self.interface = ClearOspfInstanceVrf.Input.Instance.All.Stats.Interface()
                        self.interface.parent = self
                        self._children_name_map["interface"] = "interface"
                        self._children_yang_names.add("interface")

                        self.neighbor = ClearOspfInstanceVrf.Input.Instance.All.Stats.Neighbor()
                        self.neighbor.parent = self
                        self._children_name_map["neighbor"] = "neighbor"
                        self._children_yang_names.add("neighbor")
                        self._segment_path = lambda: "stats"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-ospf-act:clear-ospf-instance-vrf/input/instance/all/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(ClearOspfInstanceVrf.Input.Instance.All.Stats, ['message_queue', 'spf'], name, value)


                    class Interface(Entity):
                        """
                        OSPF interface statistics
                        
                        .. attribute:: interface_name
                        
                        	
                        	**type**\:  str
                        
                        	**pattern:** [a\-zA\-Z0\-9./\-]+
                        
                        

                        """

                        _prefix = 'ospf-act'
                        _revision = '2016-09-14'

                        def __init__(self):
                            super(ClearOspfInstanceVrf.Input.Instance.All.Stats.Interface, self).__init__()

                            self.yang_name = "interface"
                            self.yang_parent_name = "stats"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.interface_name = YLeaf(YType.str, "interface-name")
                            self._segment_path = lambda: "interface"
                            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-ospf-act:clear-ospf-instance-vrf/input/instance/all/stats/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(ClearOspfInstanceVrf.Input.Instance.All.Stats.Interface, ['interface_name'], name, value)


                    class Neighbor(Entity):
                        """
                        Neighbor statistics per interface or neighbor id
                        
                        .. attribute:: interface
                        
                        	
                        	**type**\:   :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ClearOspfInstanceVrf.Input.Instance.All.Stats.Neighbor.Interface>`
                        
                        .. attribute:: neighbor_id
                        
                        	Neighbor ID
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ospf-act'
                        _revision = '2016-09-14'

                        def __init__(self):
                            super(ClearOspfInstanceVrf.Input.Instance.All.Stats.Neighbor, self).__init__()

                            self.yang_name = "neighbor"
                            self.yang_parent_name = "stats"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self._child_container_classes = {"interface" : ("interface", ClearOspfInstanceVrf.Input.Instance.All.Stats.Neighbor.Interface)}
                            self._child_list_classes = {}

                            self.neighbor_id = YLeaf(YType.str, "neighbor-id")

                            self.interface = ClearOspfInstanceVrf.Input.Instance.All.Stats.Neighbor.Interface()
                            self.interface.parent = self
                            self._children_name_map["interface"] = "interface"
                            self._children_yang_names.add("interface")
                            self._segment_path = lambda: "neighbor"
                            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-ospf-act:clear-ospf-instance-vrf/input/instance/all/stats/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(ClearOspfInstanceVrf.Input.Instance.All.Stats.Neighbor, ['neighbor_id'], name, value)


                        class Interface(Entity):
                            """
                            
                            
                            .. attribute:: interface_name
                            
                            	OSPF interface statistics
                            	**type**\:  str
                            
                            	**pattern:** [a\-zA\-Z0\-9./\-]+
                            
                            

                            """

                            _prefix = 'ospf-act'
                            _revision = '2016-09-14'

                            def __init__(self):
                                super(ClearOspfInstanceVrf.Input.Instance.All.Stats.Neighbor.Interface, self).__init__()

                                self.yang_name = "interface"
                                self.yang_parent_name = "neighbor"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.interface_name = YLeaf(YType.str, "interface-name")
                                self._segment_path = lambda: "interface"
                                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-ospf-act:clear-ospf-instance-vrf/input/instance/all/stats/neighbor/%s" % self._segment_path()

                            def __setattr__(self, name, value):
                                self._perform_setattr(ClearOspfInstanceVrf.Input.Instance.All.Stats.Neighbor.Interface, ['interface_name'], name, value)


            class AllInclusive(Entity):
                """
                Clear all non\-default and default OSPF VRFs
                
                .. attribute:: process
                
                	Reset OSPF process
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: redistribution
                
                	Clear OSPF route redistrbution
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: route
                
                	Clear OSPF route table
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: stats
                
                	OSPF counters and statistics
                	**type**\:   :py:class:`Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ClearOspfInstanceVrf.Input.Instance.AllInclusive.Stats>`
                
                

                """

                _prefix = 'ospf-act'
                _revision = '2016-09-14'

                def __init__(self):
                    super(ClearOspfInstanceVrf.Input.Instance.AllInclusive, self).__init__()

                    self.yang_name = "all-inclusive"
                    self.yang_parent_name = "instance"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"stats" : ("stats", ClearOspfInstanceVrf.Input.Instance.AllInclusive.Stats)}
                    self._child_list_classes = {}

                    self.process = YLeaf(YType.empty, "process")

                    self.redistribution = YLeaf(YType.empty, "redistribution")

                    self.route = YLeaf(YType.empty, "route")

                    self.stats = ClearOspfInstanceVrf.Input.Instance.AllInclusive.Stats()
                    self.stats.parent = self
                    self._children_name_map["stats"] = "stats"
                    self._children_yang_names.add("stats")
                    self._segment_path = lambda: "all-inclusive"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-ospf-act:clear-ospf-instance-vrf/input/instance/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(ClearOspfInstanceVrf.Input.Instance.AllInclusive, ['process', 'redistribution', 'route'], name, value)


                class Stats(Entity):
                    """
                    OSPF counters and statistics
                    
                    .. attribute:: interface
                    
                    	OSPF interface statistics
                    	**type**\:   :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ClearOspfInstanceVrf.Input.Instance.AllInclusive.Stats.Interface>`
                    
                    .. attribute:: message_queue
                    
                    	Message\-queue statistics
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: neighbor
                    
                    	Neighbor statistics per interface or neighbor id
                    	**type**\:   :py:class:`Neighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ClearOspfInstanceVrf.Input.Instance.AllInclusive.Stats.Neighbor>`
                    
                    .. attribute:: spf
                    
                    	SPF statistics
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'ospf-act'
                    _revision = '2016-09-14'

                    def __init__(self):
                        super(ClearOspfInstanceVrf.Input.Instance.AllInclusive.Stats, self).__init__()

                        self.yang_name = "stats"
                        self.yang_parent_name = "all-inclusive"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"interface" : ("interface", ClearOspfInstanceVrf.Input.Instance.AllInclusive.Stats.Interface), "neighbor" : ("neighbor", ClearOspfInstanceVrf.Input.Instance.AllInclusive.Stats.Neighbor)}
                        self._child_list_classes = {}

                        self.message_queue = YLeaf(YType.empty, "message-queue")

                        self.spf = YLeaf(YType.empty, "spf")

                        self.interface = ClearOspfInstanceVrf.Input.Instance.AllInclusive.Stats.Interface()
                        self.interface.parent = self
                        self._children_name_map["interface"] = "interface"
                        self._children_yang_names.add("interface")

                        self.neighbor = ClearOspfInstanceVrf.Input.Instance.AllInclusive.Stats.Neighbor()
                        self.neighbor.parent = self
                        self._children_name_map["neighbor"] = "neighbor"
                        self._children_yang_names.add("neighbor")
                        self._segment_path = lambda: "stats"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-ospf-act:clear-ospf-instance-vrf/input/instance/all-inclusive/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(ClearOspfInstanceVrf.Input.Instance.AllInclusive.Stats, ['message_queue', 'spf'], name, value)


                    class Interface(Entity):
                        """
                        OSPF interface statistics
                        
                        .. attribute:: interface_name
                        
                        	
                        	**type**\:  str
                        
                        	**pattern:** [a\-zA\-Z0\-9./\-]+
                        
                        

                        """

                        _prefix = 'ospf-act'
                        _revision = '2016-09-14'

                        def __init__(self):
                            super(ClearOspfInstanceVrf.Input.Instance.AllInclusive.Stats.Interface, self).__init__()

                            self.yang_name = "interface"
                            self.yang_parent_name = "stats"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.interface_name = YLeaf(YType.str, "interface-name")
                            self._segment_path = lambda: "interface"
                            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-ospf-act:clear-ospf-instance-vrf/input/instance/all-inclusive/stats/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(ClearOspfInstanceVrf.Input.Instance.AllInclusive.Stats.Interface, ['interface_name'], name, value)


                    class Neighbor(Entity):
                        """
                        Neighbor statistics per interface or neighbor id
                        
                        .. attribute:: interface
                        
                        	
                        	**type**\:   :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ClearOspfInstanceVrf.Input.Instance.AllInclusive.Stats.Neighbor.Interface>`
                        
                        .. attribute:: neighbor_id
                        
                        	Neighbor ID
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ospf-act'
                        _revision = '2016-09-14'

                        def __init__(self):
                            super(ClearOspfInstanceVrf.Input.Instance.AllInclusive.Stats.Neighbor, self).__init__()

                            self.yang_name = "neighbor"
                            self.yang_parent_name = "stats"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self._child_container_classes = {"interface" : ("interface", ClearOspfInstanceVrf.Input.Instance.AllInclusive.Stats.Neighbor.Interface)}
                            self._child_list_classes = {}

                            self.neighbor_id = YLeaf(YType.str, "neighbor-id")

                            self.interface = ClearOspfInstanceVrf.Input.Instance.AllInclusive.Stats.Neighbor.Interface()
                            self.interface.parent = self
                            self._children_name_map["interface"] = "interface"
                            self._children_yang_names.add("interface")
                            self._segment_path = lambda: "neighbor"
                            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-ospf-act:clear-ospf-instance-vrf/input/instance/all-inclusive/stats/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(ClearOspfInstanceVrf.Input.Instance.AllInclusive.Stats.Neighbor, ['neighbor_id'], name, value)


                        class Interface(Entity):
                            """
                            
                            
                            .. attribute:: interface_name
                            
                            	OSPF interface statistics
                            	**type**\:  str
                            
                            	**pattern:** [a\-zA\-Z0\-9./\-]+
                            
                            

                            """

                            _prefix = 'ospf-act'
                            _revision = '2016-09-14'

                            def __init__(self):
                                super(ClearOspfInstanceVrf.Input.Instance.AllInclusive.Stats.Neighbor.Interface, self).__init__()

                                self.yang_name = "interface"
                                self.yang_parent_name = "neighbor"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.interface_name = YLeaf(YType.str, "interface-name")
                                self._segment_path = lambda: "interface"
                                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-ospf-act:clear-ospf-instance-vrf/input/instance/all-inclusive/stats/neighbor/%s" % self._segment_path()

                            def __setattr__(self, name, value):
                                self._perform_setattr(ClearOspfInstanceVrf.Input.Instance.AllInclusive.Stats.Neighbor.Interface, ['interface_name'], name, value)


            class Vrf(Entity):
                """
                Clear one or more non\-default OSPF VRFs in process
                
                .. attribute:: process
                
                	Reset OSPF process
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: redistribution
                
                	Clear OSPF route redistrbution
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: route
                
                	Clear OSPF route table
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: stats
                
                	OSPF counters and statistics
                	**type**\:   :py:class:`Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ClearOspfInstanceVrf.Input.Instance.Vrf.Stats>`
                
                .. attribute:: vrf_name
                
                	OSPF VRF name
                	**type**\:  str
                
                

                """

                _prefix = 'ospf-act'
                _revision = '2016-09-14'

                def __init__(self):
                    super(ClearOspfInstanceVrf.Input.Instance.Vrf, self).__init__()

                    self.yang_name = "vrf"
                    self.yang_parent_name = "instance"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"stats" : ("stats", ClearOspfInstanceVrf.Input.Instance.Vrf.Stats)}
                    self._child_list_classes = {}

                    self.process = YLeaf(YType.empty, "process")

                    self.redistribution = YLeaf(YType.empty, "redistribution")

                    self.route = YLeaf(YType.empty, "route")

                    self.vrf_name = YLeaf(YType.str, "vrf-name")

                    self.stats = ClearOspfInstanceVrf.Input.Instance.Vrf.Stats()
                    self.stats.parent = self
                    self._children_name_map["stats"] = "stats"
                    self._children_yang_names.add("stats")
                    self._segment_path = lambda: "vrf"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-ospf-act:clear-ospf-instance-vrf/input/instance/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(ClearOspfInstanceVrf.Input.Instance.Vrf, ['process', 'redistribution', 'route', 'vrf_name'], name, value)


                class Stats(Entity):
                    """
                    OSPF counters and statistics
                    
                    .. attribute:: interface
                    
                    	OSPF interface statistics
                    	**type**\:   :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ClearOspfInstanceVrf.Input.Instance.Vrf.Stats.Interface>`
                    
                    .. attribute:: message_queue
                    
                    	Message\-queue statistics
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: neighbor
                    
                    	Neighbor statistics per interface or neighbor id
                    	**type**\:   :py:class:`Neighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ClearOspfInstanceVrf.Input.Instance.Vrf.Stats.Neighbor>`
                    
                    .. attribute:: spf
                    
                    	SPF statistics
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'ospf-act'
                    _revision = '2016-09-14'

                    def __init__(self):
                        super(ClearOspfInstanceVrf.Input.Instance.Vrf.Stats, self).__init__()

                        self.yang_name = "stats"
                        self.yang_parent_name = "vrf"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"interface" : ("interface", ClearOspfInstanceVrf.Input.Instance.Vrf.Stats.Interface), "neighbor" : ("neighbor", ClearOspfInstanceVrf.Input.Instance.Vrf.Stats.Neighbor)}
                        self._child_list_classes = {}

                        self.message_queue = YLeaf(YType.empty, "message-queue")

                        self.spf = YLeaf(YType.empty, "spf")

                        self.interface = ClearOspfInstanceVrf.Input.Instance.Vrf.Stats.Interface()
                        self.interface.parent = self
                        self._children_name_map["interface"] = "interface"
                        self._children_yang_names.add("interface")

                        self.neighbor = ClearOspfInstanceVrf.Input.Instance.Vrf.Stats.Neighbor()
                        self.neighbor.parent = self
                        self._children_name_map["neighbor"] = "neighbor"
                        self._children_yang_names.add("neighbor")
                        self._segment_path = lambda: "stats"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-ospf-act:clear-ospf-instance-vrf/input/instance/vrf/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(ClearOspfInstanceVrf.Input.Instance.Vrf.Stats, ['message_queue', 'spf'], name, value)


                    class Interface(Entity):
                        """
                        OSPF interface statistics
                        
                        .. attribute:: interface_name
                        
                        	
                        	**type**\:  str
                        
                        	**pattern:** [a\-zA\-Z0\-9./\-]+
                        
                        

                        """

                        _prefix = 'ospf-act'
                        _revision = '2016-09-14'

                        def __init__(self):
                            super(ClearOspfInstanceVrf.Input.Instance.Vrf.Stats.Interface, self).__init__()

                            self.yang_name = "interface"
                            self.yang_parent_name = "stats"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.interface_name = YLeaf(YType.str, "interface-name")
                            self._segment_path = lambda: "interface"
                            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-ospf-act:clear-ospf-instance-vrf/input/instance/vrf/stats/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(ClearOspfInstanceVrf.Input.Instance.Vrf.Stats.Interface, ['interface_name'], name, value)


                    class Neighbor(Entity):
                        """
                        Neighbor statistics per interface or neighbor id
                        
                        .. attribute:: interface
                        
                        	
                        	**type**\:   :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ClearOspfInstanceVrf.Input.Instance.Vrf.Stats.Neighbor.Interface>`
                        
                        .. attribute:: neighbor_id
                        
                        	Neighbor ID
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ospf-act'
                        _revision = '2016-09-14'

                        def __init__(self):
                            super(ClearOspfInstanceVrf.Input.Instance.Vrf.Stats.Neighbor, self).__init__()

                            self.yang_name = "neighbor"
                            self.yang_parent_name = "stats"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self._child_container_classes = {"interface" : ("interface", ClearOspfInstanceVrf.Input.Instance.Vrf.Stats.Neighbor.Interface)}
                            self._child_list_classes = {}

                            self.neighbor_id = YLeaf(YType.str, "neighbor-id")

                            self.interface = ClearOspfInstanceVrf.Input.Instance.Vrf.Stats.Neighbor.Interface()
                            self.interface.parent = self
                            self._children_name_map["interface"] = "interface"
                            self._children_yang_names.add("interface")
                            self._segment_path = lambda: "neighbor"
                            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-ospf-act:clear-ospf-instance-vrf/input/instance/vrf/stats/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(ClearOspfInstanceVrf.Input.Instance.Vrf.Stats.Neighbor, ['neighbor_id'], name, value)


                        class Interface(Entity):
                            """
                            
                            
                            .. attribute:: interface_name
                            
                            	OSPF interface statistics
                            	**type**\:  str
                            
                            	**pattern:** [a\-zA\-Z0\-9./\-]+
                            
                            

                            """

                            _prefix = 'ospf-act'
                            _revision = '2016-09-14'

                            def __init__(self):
                                super(ClearOspfInstanceVrf.Input.Instance.Vrf.Stats.Neighbor.Interface, self).__init__()

                                self.yang_name = "interface"
                                self.yang_parent_name = "neighbor"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.interface_name = YLeaf(YType.str, "interface-name")
                                self._segment_path = lambda: "interface"
                                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-ospf-act:clear-ospf-instance-vrf/input/instance/vrf/stats/neighbor/%s" % self._segment_path()

                            def __setattr__(self, name, value):
                                self._perform_setattr(ClearOspfInstanceVrf.Input.Instance.Vrf.Stats.Neighbor.Interface, ['interface_name'], name, value)

    def clone_ptr(self):
        self._top_entity = ClearOspfInstanceVrf()
        return self._top_entity

class ClearOspfProcess(Entity):
    """
    Clear (reset) OSPF process
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ClearOspfProcess.Input>`
    
    

    """

    _prefix = 'ospf-act'
    _revision = '2016-09-14'

    def __init__(self):
        super(ClearOspfProcess, self).__init__()
        self._top_entity = None

        self.yang_name = "clear-ospf-process"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-ospf-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {}
        self._child_list_classes = {}

        self.input = ClearOspfProcess.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")
        self._segment_path = lambda: "Cisco-IOS-XR-ipv4-ospf-act:clear-ospf-process"


    class Input(Entity):
        """
        
        
        .. attribute:: instance
        
        	Clear data from OSPF instance
        	**type**\:   :py:class:`Instance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ClearOspfProcess.Input.Instance>`
        
        .. attribute:: process
        
        	Reset OSPF process
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'ospf-act'
        _revision = '2016-09-14'

        def __init__(self):
            super(ClearOspfProcess.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "clear-ospf-process"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"instance" : ("instance", ClearOspfProcess.Input.Instance)}
            self._child_list_classes = {}

            self.process = YLeaf(YType.empty, "process")

            self.instance = ClearOspfProcess.Input.Instance()
            self.instance.parent = self
            self._children_name_map["instance"] = "instance"
            self._children_yang_names.add("instance")
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-ospf-act:clear-ospf-process/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(ClearOspfProcess.Input, ['process'], name, value)


        class Instance(Entity):
            """
            Clear data from OSPF instance
            
            .. attribute:: instance_identifier
            
            	OSPF process instance identifier
            	**type**\:  str
            
            

            """

            _prefix = 'ospf-act'
            _revision = '2016-09-14'

            def __init__(self):
                super(ClearOspfProcess.Input.Instance, self).__init__()

                self.yang_name = "instance"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.instance_identifier = YLeaf(YType.str, "instance-identifier")
                self._segment_path = lambda: "instance"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-ospf-act:clear-ospf-process/input/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(ClearOspfProcess.Input.Instance, ['instance_identifier'], name, value)

    def clone_ptr(self):
        self._top_entity = ClearOspfProcess()
        return self._top_entity

class ClearOspfRedistribution(Entity):
    """
    Clear OSPF route redistribution
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ClearOspfRedistribution.Input>`
    
    

    """

    _prefix = 'ospf-act'
    _revision = '2016-09-14'

    def __init__(self):
        super(ClearOspfRedistribution, self).__init__()
        self._top_entity = None

        self.yang_name = "clear-ospf-redistribution"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-ospf-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {}
        self._child_list_classes = {}

        self.input = ClearOspfRedistribution.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")
        self._segment_path = lambda: "Cisco-IOS-XR-ipv4-ospf-act:clear-ospf-redistribution"


    class Input(Entity):
        """
        
        
        .. attribute:: instance
        
        	Clear data from OSPF instance
        	**type**\:   :py:class:`Instance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ClearOspfRedistribution.Input.Instance>`
        
        .. attribute:: redistribution
        
        	Clear OSPF route redistribution
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'ospf-act'
        _revision = '2016-09-14'

        def __init__(self):
            super(ClearOspfRedistribution.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "clear-ospf-redistribution"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"instance" : ("instance", ClearOspfRedistribution.Input.Instance)}
            self._child_list_classes = {}

            self.redistribution = YLeaf(YType.empty, "redistribution")

            self.instance = ClearOspfRedistribution.Input.Instance()
            self.instance.parent = self
            self._children_name_map["instance"] = "instance"
            self._children_yang_names.add("instance")
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-ospf-act:clear-ospf-redistribution/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(ClearOspfRedistribution.Input, ['redistribution'], name, value)


        class Instance(Entity):
            """
            Clear data from OSPF instance
            
            .. attribute:: instance_identifier
            
            	OSPF process instance identifier
            	**type**\:  str
            
            

            """

            _prefix = 'ospf-act'
            _revision = '2016-09-14'

            def __init__(self):
                super(ClearOspfRedistribution.Input.Instance, self).__init__()

                self.yang_name = "instance"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.instance_identifier = YLeaf(YType.str, "instance-identifier")
                self._segment_path = lambda: "instance"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-ospf-act:clear-ospf-redistribution/input/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(ClearOspfRedistribution.Input.Instance, ['instance_identifier'], name, value)

    def clone_ptr(self):
        self._top_entity = ClearOspfRedistribution()
        return self._top_entity

class ClearOspfRoutes(Entity):
    """
    Clear OSPF route table
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ClearOspfRoutes.Input>`
    
    

    """

    _prefix = 'ospf-act'
    _revision = '2016-09-14'

    def __init__(self):
        super(ClearOspfRoutes, self).__init__()
        self._top_entity = None

        self.yang_name = "clear-ospf-routes"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-ospf-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {}
        self._child_list_classes = {}

        self.input = ClearOspfRoutes.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")
        self._segment_path = lambda: "Cisco-IOS-XR-ipv4-ospf-act:clear-ospf-routes"


    class Input(Entity):
        """
        
        
        .. attribute:: instance
        
        	Clear data from OSPF instance
        	**type**\:   :py:class:`Instance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ClearOspfRoutes.Input.Instance>`
        
        .. attribute:: route
        
        	Clear OSPF route table
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'ospf-act'
        _revision = '2016-09-14'

        def __init__(self):
            super(ClearOspfRoutes.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "clear-ospf-routes"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"instance" : ("instance", ClearOspfRoutes.Input.Instance)}
            self._child_list_classes = {}

            self.route = YLeaf(YType.empty, "route")

            self.instance = ClearOspfRoutes.Input.Instance()
            self.instance.parent = self
            self._children_name_map["instance"] = "instance"
            self._children_yang_names.add("instance")
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-ospf-act:clear-ospf-routes/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(ClearOspfRoutes.Input, ['route'], name, value)


        class Instance(Entity):
            """
            Clear data from OSPF instance
            
            .. attribute:: instance_identifier
            
            	OSPF process instance identifier
            	**type**\:  str
            
            

            """

            _prefix = 'ospf-act'
            _revision = '2016-09-14'

            def __init__(self):
                super(ClearOspfRoutes.Input.Instance, self).__init__()

                self.yang_name = "instance"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.instance_identifier = YLeaf(YType.str, "instance-identifier")
                self._segment_path = lambda: "instance"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-ospf-act:clear-ospf-routes/input/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(ClearOspfRoutes.Input.Instance, ['instance_identifier'], name, value)

    def clone_ptr(self):
        self._top_entity = ClearOspfRoutes()
        return self._top_entity

class ClearOspfStatistics(Entity):
    """
    Clear OSPF counters and statistics
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ClearOspfStatistics.Input>`
    
    

    """

    _prefix = 'ospf-act'
    _revision = '2016-09-14'

    def __init__(self):
        super(ClearOspfStatistics, self).__init__()
        self._top_entity = None

        self.yang_name = "clear-ospf-statistics"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-ospf-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {}
        self._child_list_classes = {}

        self.input = ClearOspfStatistics.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")
        self._segment_path = lambda: "Cisco-IOS-XR-ipv4-ospf-act:clear-ospf-statistics"


    class Input(Entity):
        """
        
        
        .. attribute:: all
        
        	All OSPF counters and statistics
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: instance
        
        	Clear data from OSPF instance
        	**type**\:   :py:class:`Instance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ClearOspfStatistics.Input.Instance>`
        
        .. attribute:: interface_name
        
        	OSPF interface statistics
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: message_queue
        
        	Message\-queue statistics
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: neighbor
        
        	Neighbor statistics per neighbor id
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: spf
        
        	SPF statistics
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'ospf-act'
        _revision = '2016-09-14'

        def __init__(self):
            super(ClearOspfStatistics.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "clear-ospf-statistics"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"instance" : ("instance", ClearOspfStatistics.Input.Instance)}
            self._child_list_classes = {}

            self.all = YLeaf(YType.empty, "all")

            self.interface_name = YLeaf(YType.empty, "interface-name")

            self.message_queue = YLeaf(YType.empty, "message-queue")

            self.neighbor = YLeaf(YType.empty, "neighbor")

            self.spf = YLeaf(YType.empty, "spf")

            self.instance = ClearOspfStatistics.Input.Instance()
            self.instance.parent = self
            self._children_name_map["instance"] = "instance"
            self._children_yang_names.add("instance")
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-ospf-act:clear-ospf-statistics/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(ClearOspfStatistics.Input, ['all', 'interface_name', 'message_queue', 'neighbor', 'spf'], name, value)


        class Instance(Entity):
            """
            Clear data from OSPF instance
            
            .. attribute:: instance_identifier
            
            	OSPF process instance identifier
            	**type**\:  str
            
            

            """

            _prefix = 'ospf-act'
            _revision = '2016-09-14'

            def __init__(self):
                super(ClearOspfStatistics.Input.Instance, self).__init__()

                self.yang_name = "instance"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.instance_identifier = YLeaf(YType.str, "instance-identifier")
                self._segment_path = lambda: "instance"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-ospf-act:clear-ospf-statistics/input/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(ClearOspfStatistics.Input.Instance, ['instance_identifier'], name, value)

    def clone_ptr(self):
        self._top_entity = ClearOspfStatistics()
        return self._top_entity

class ClearOspfStatisticsInterface(Entity):
    """
    Clear OSPF interface statistics
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ClearOspfStatisticsInterface.Input>`
    
    

    """

    _prefix = 'ospf-act'
    _revision = '2016-09-14'

    def __init__(self):
        super(ClearOspfStatisticsInterface, self).__init__()
        self._top_entity = None

        self.yang_name = "clear-ospf-statistics-interface"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-ospf-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {}
        self._child_list_classes = {}

        self.input = ClearOspfStatisticsInterface.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")
        self._segment_path = lambda: "Cisco-IOS-XR-ipv4-ospf-act:clear-ospf-statistics-interface"


    class Input(Entity):
        """
        
        
        .. attribute:: instance
        
        	Clear data from OSPF instance
        	**type**\:   :py:class:`Instance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ClearOspfStatisticsInterface.Input.Instance>`
        
        .. attribute:: interface
        
        	
        	**type**\:   :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ClearOspfStatisticsInterface.Input.Interface>`
        
        

        """

        _prefix = 'ospf-act'
        _revision = '2016-09-14'

        def __init__(self):
            super(ClearOspfStatisticsInterface.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "clear-ospf-statistics-interface"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"instance" : ("instance", ClearOspfStatisticsInterface.Input.Instance), "interface" : ("interface", ClearOspfStatisticsInterface.Input.Interface)}
            self._child_list_classes = {}

            self.instance = ClearOspfStatisticsInterface.Input.Instance()
            self.instance.parent = self
            self._children_name_map["instance"] = "instance"
            self._children_yang_names.add("instance")

            self.interface = ClearOspfStatisticsInterface.Input.Interface()
            self.interface.parent = self
            self._children_name_map["interface"] = "interface"
            self._children_yang_names.add("interface")
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-ospf-act:clear-ospf-statistics-interface/%s" % self._segment_path()


        class Instance(Entity):
            """
            Clear data from OSPF instance
            
            .. attribute:: instance_identifier
            
            	OSPF process instance identifier
            	**type**\:  str
            
            

            """

            _prefix = 'ospf-act'
            _revision = '2016-09-14'

            def __init__(self):
                super(ClearOspfStatisticsInterface.Input.Instance, self).__init__()

                self.yang_name = "instance"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.instance_identifier = YLeaf(YType.str, "instance-identifier")
                self._segment_path = lambda: "instance"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-ospf-act:clear-ospf-statistics-interface/input/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(ClearOspfStatisticsInterface.Input.Instance, ['instance_identifier'], name, value)


        class Interface(Entity):
            """
            
            
            .. attribute:: interface_name
            
            	OSPF interface statistics
            	**type**\:  str
            
            	**pattern:** [a\-zA\-Z0\-9./\-]+
            
            

            """

            _prefix = 'ospf-act'
            _revision = '2016-09-14'

            def __init__(self):
                super(ClearOspfStatisticsInterface.Input.Interface, self).__init__()

                self.yang_name = "interface"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.interface_name = YLeaf(YType.str, "interface-name")
                self._segment_path = lambda: "interface"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-ospf-act:clear-ospf-statistics-interface/input/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(ClearOspfStatisticsInterface.Input.Interface, ['interface_name'], name, value)

    def clone_ptr(self):
        self._top_entity = ClearOspfStatisticsInterface()
        return self._top_entity

class ClearOspfStatisticsNeighbor(Entity):
    """
    Clear OSPF neighbor statistics per interface or neighbor id
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ClearOspfStatisticsNeighbor.Input>`
    
    

    """

    _prefix = 'ospf-act'
    _revision = '2016-09-14'

    def __init__(self):
        super(ClearOspfStatisticsNeighbor, self).__init__()
        self._top_entity = None

        self.yang_name = "clear-ospf-statistics-neighbor"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-ospf-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {}
        self._child_list_classes = {}

        self.input = ClearOspfStatisticsNeighbor.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")
        self._segment_path = lambda: "Cisco-IOS-XR-ipv4-ospf-act:clear-ospf-statistics-neighbor"


    class Input(Entity):
        """
        
        
        .. attribute:: instance
        
        	Clear data from OSPF instance
        	**type**\:   :py:class:`Instance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ClearOspfStatisticsNeighbor.Input.Instance>`
        
        .. attribute:: neighbor
        
        	
        	**type**\:   :py:class:`Neighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ClearOspfStatisticsNeighbor.Input.Neighbor>`
        
        

        """

        _prefix = 'ospf-act'
        _revision = '2016-09-14'

        def __init__(self):
            super(ClearOspfStatisticsNeighbor.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "clear-ospf-statistics-neighbor"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"instance" : ("instance", ClearOspfStatisticsNeighbor.Input.Instance), "neighbor" : ("neighbor", ClearOspfStatisticsNeighbor.Input.Neighbor)}
            self._child_list_classes = {}

            self.instance = ClearOspfStatisticsNeighbor.Input.Instance()
            self.instance.parent = self
            self._children_name_map["instance"] = "instance"
            self._children_yang_names.add("instance")

            self.neighbor = ClearOspfStatisticsNeighbor.Input.Neighbor()
            self.neighbor.parent = self
            self._children_name_map["neighbor"] = "neighbor"
            self._children_yang_names.add("neighbor")
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-ospf-act:clear-ospf-statistics-neighbor/%s" % self._segment_path()


        class Instance(Entity):
            """
            Clear data from OSPF instance
            
            .. attribute:: instance_identifier
            
            	OSPF process instance identifier
            	**type**\:  str
            
            

            """

            _prefix = 'ospf-act'
            _revision = '2016-09-14'

            def __init__(self):
                super(ClearOspfStatisticsNeighbor.Input.Instance, self).__init__()

                self.yang_name = "instance"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.instance_identifier = YLeaf(YType.str, "instance-identifier")
                self._segment_path = lambda: "instance"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-ospf-act:clear-ospf-statistics-neighbor/input/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(ClearOspfStatisticsNeighbor.Input.Instance, ['instance_identifier'], name, value)


        class Neighbor(Entity):
            """
            
            
            .. attribute:: interface_name
            
            	Interface
            	**type**\:  str
            
            	**pattern:** [a\-zA\-Z0\-9./\-]+
            
            .. attribute:: neighbor_id
            
            	Neighbor ID
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            

            """

            _prefix = 'ospf-act'
            _revision = '2016-09-14'

            def __init__(self):
                super(ClearOspfStatisticsNeighbor.Input.Neighbor, self).__init__()

                self.yang_name = "neighbor"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.interface_name = YLeaf(YType.str, "interface-name")

                self.neighbor_id = YLeaf(YType.str, "neighbor-id")
                self._segment_path = lambda: "neighbor"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-ospf-act:clear-ospf-statistics-neighbor/input/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(ClearOspfStatisticsNeighbor.Input.Neighbor, ['interface_name', 'neighbor_id'], name, value)

    def clone_ptr(self):
        self._top_entity = ClearOspfStatisticsNeighbor()
        return self._top_entity

