""" Cisco_IOS_XR_ipv6_ospfv3_act 

This module contains a collection of YANG definitions
for Cisco IOS\-XR IPv6 OSPFv3 action package configuration.

Copyright (c) 2016\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class ClearOspfv3Routes(Entity):
    """
    Clear OSPFv3 route table
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act.ClearOspfv3Routes.Input>`
    
    

    """

    _prefix = 'ospfv3-act'
    _revision = '2016-09-14'

    def __init__(self):
        super(ClearOspfv3Routes, self).__init__()
        self._top_entity = None

        self.yang_name = "clear-ospfv3-routes"
        self.yang_parent_name = "Cisco-IOS-XR-ipv6-ospfv3-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = ClearOspfv3Routes.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._segment_path = lambda: "Cisco-IOS-XR-ipv6-ospfv3-act:clear-ospfv3-routes"
        self._is_frozen = True


    class Input(Entity):
        """
        
        
        .. attribute:: instance
        
        	Clear data from OSPFv3 instance
        	**type**\:  :py:class:`Instance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act.ClearOspfv3Routes.Input.Instance>`
        
        .. attribute:: route
        
        	Clear OSPFv3 route table
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'ospfv3-act'
        _revision = '2016-09-14'

        def __init__(self):
            super(ClearOspfv3Routes.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "clear-ospfv3-routes"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("instance", ("instance", ClearOspfv3Routes.Input.Instance))])
            self._leafs = OrderedDict([
                ('route', (YLeaf(YType.empty, 'route'), ['Empty'])),
            ])
            self.route = None

            self.instance = ClearOspfv3Routes.Input.Instance()
            self.instance.parent = self
            self._children_name_map["instance"] = "instance"
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-ospfv3-act:clear-ospfv3-routes/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(ClearOspfv3Routes.Input, ['route'], name, value)


        class Instance(Entity):
            """
            Clear data from OSPFv3 instance
            
            .. attribute:: instance_identifier
            
            	OSPFv3 process instance identifier
            	**type**\: str
            
            

            """

            _prefix = 'ospfv3-act'
            _revision = '2016-09-14'

            def __init__(self):
                super(ClearOspfv3Routes.Input.Instance, self).__init__()

                self.yang_name = "instance"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('instance_identifier', (YLeaf(YType.str, 'instance-identifier'), ['str'])),
                ])
                self.instance_identifier = None
                self._segment_path = lambda: "instance"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-ospfv3-act:clear-ospfv3-routes/input/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ClearOspfv3Routes.Input.Instance, ['instance_identifier'], name, value)

    def clone_ptr(self):
        self._top_entity = ClearOspfv3Routes()
        return self._top_entity

class ClearOspfv3Redistribution(Entity):
    """
    Clear OSPFv3 route redistribution
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act.ClearOspfv3Redistribution.Input>`
    
    

    """

    _prefix = 'ospfv3-act'
    _revision = '2016-09-14'

    def __init__(self):
        super(ClearOspfv3Redistribution, self).__init__()
        self._top_entity = None

        self.yang_name = "clear-ospfv3-redistribution"
        self.yang_parent_name = "Cisco-IOS-XR-ipv6-ospfv3-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = ClearOspfv3Redistribution.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._segment_path = lambda: "Cisco-IOS-XR-ipv6-ospfv3-act:clear-ospfv3-redistribution"
        self._is_frozen = True


    class Input(Entity):
        """
        
        
        .. attribute:: instance
        
        	Clear data from OSPFv3 instance
        	**type**\:  :py:class:`Instance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act.ClearOspfv3Redistribution.Input.Instance>`
        
        .. attribute:: redistribution
        
        	Clear OSPFv3 route redistribution
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'ospfv3-act'
        _revision = '2016-09-14'

        def __init__(self):
            super(ClearOspfv3Redistribution.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "clear-ospfv3-redistribution"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("instance", ("instance", ClearOspfv3Redistribution.Input.Instance))])
            self._leafs = OrderedDict([
                ('redistribution', (YLeaf(YType.empty, 'redistribution'), ['Empty'])),
            ])
            self.redistribution = None

            self.instance = ClearOspfv3Redistribution.Input.Instance()
            self.instance.parent = self
            self._children_name_map["instance"] = "instance"
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-ospfv3-act:clear-ospfv3-redistribution/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(ClearOspfv3Redistribution.Input, ['redistribution'], name, value)


        class Instance(Entity):
            """
            Clear data from OSPFv3 instance
            
            .. attribute:: instance_identifier
            
            	OSPFv3 process instance identifier
            	**type**\: str
            
            

            """

            _prefix = 'ospfv3-act'
            _revision = '2016-09-14'

            def __init__(self):
                super(ClearOspfv3Redistribution.Input.Instance, self).__init__()

                self.yang_name = "instance"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('instance_identifier', (YLeaf(YType.str, 'instance-identifier'), ['str'])),
                ])
                self.instance_identifier = None
                self._segment_path = lambda: "instance"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-ospfv3-act:clear-ospfv3-redistribution/input/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ClearOspfv3Redistribution.Input.Instance, ['instance_identifier'], name, value)

    def clone_ptr(self):
        self._top_entity = ClearOspfv3Redistribution()
        return self._top_entity

class ClearOspfv3Process(Entity):
    """
    Clear (reset) OSPFv3 Process
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act.ClearOspfv3Process.Input>`
    
    

    """

    _prefix = 'ospfv3-act'
    _revision = '2016-09-14'

    def __init__(self):
        super(ClearOspfv3Process, self).__init__()
        self._top_entity = None

        self.yang_name = "clear-ospfv3-process"
        self.yang_parent_name = "Cisco-IOS-XR-ipv6-ospfv3-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = ClearOspfv3Process.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._segment_path = lambda: "Cisco-IOS-XR-ipv6-ospfv3-act:clear-ospfv3-process"
        self._is_frozen = True


    class Input(Entity):
        """
        
        
        .. attribute:: instance
        
        	Clear data from OSPFv3 instance
        	**type**\:  :py:class:`Instance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act.ClearOspfv3Process.Input.Instance>`
        
        .. attribute:: process
        
        	Reset OSPFv3 process
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'ospfv3-act'
        _revision = '2016-09-14'

        def __init__(self):
            super(ClearOspfv3Process.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "clear-ospfv3-process"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("instance", ("instance", ClearOspfv3Process.Input.Instance))])
            self._leafs = OrderedDict([
                ('process', (YLeaf(YType.empty, 'process'), ['Empty'])),
            ])
            self.process = None

            self.instance = ClearOspfv3Process.Input.Instance()
            self.instance.parent = self
            self._children_name_map["instance"] = "instance"
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-ospfv3-act:clear-ospfv3-process/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(ClearOspfv3Process.Input, ['process'], name, value)


        class Instance(Entity):
            """
            Clear data from OSPFv3 instance
            
            .. attribute:: instance_identifier
            
            	OSPFv3 process instance identifier
            	**type**\: str
            
            

            """

            _prefix = 'ospfv3-act'
            _revision = '2016-09-14'

            def __init__(self):
                super(ClearOspfv3Process.Input.Instance, self).__init__()

                self.yang_name = "instance"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('instance_identifier', (YLeaf(YType.str, 'instance-identifier'), ['str'])),
                ])
                self.instance_identifier = None
                self._segment_path = lambda: "instance"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-ospfv3-act:clear-ospfv3-process/input/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ClearOspfv3Process.Input.Instance, ['instance_identifier'], name, value)

    def clone_ptr(self):
        self._top_entity = ClearOspfv3Process()
        return self._top_entity

class ClearOspfv3StatisticsNeighbor(Entity):
    """
    Clear OSPFv3 neighbor statistics per interface or neighbor id
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act.ClearOspfv3StatisticsNeighbor.Input>`
    
    

    """

    _prefix = 'ospfv3-act'
    _revision = '2016-09-14'

    def __init__(self):
        super(ClearOspfv3StatisticsNeighbor, self).__init__()
        self._top_entity = None

        self.yang_name = "clear-ospfv3-statistics-neighbor"
        self.yang_parent_name = "Cisco-IOS-XR-ipv6-ospfv3-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = ClearOspfv3StatisticsNeighbor.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._segment_path = lambda: "Cisco-IOS-XR-ipv6-ospfv3-act:clear-ospfv3-statistics-neighbor"
        self._is_frozen = True


    class Input(Entity):
        """
        
        
        .. attribute:: instance
        
        	Clear data from OSPFv3 instance
        	**type**\:  :py:class:`Instance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act.ClearOspfv3StatisticsNeighbor.Input.Instance>`
        
        .. attribute:: neighbor
        
        	
        	**type**\:  :py:class:`Neighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act.ClearOspfv3StatisticsNeighbor.Input.Neighbor>`
        
        

        """

        _prefix = 'ospfv3-act'
        _revision = '2016-09-14'

        def __init__(self):
            super(ClearOspfv3StatisticsNeighbor.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "clear-ospfv3-statistics-neighbor"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("instance", ("instance", ClearOspfv3StatisticsNeighbor.Input.Instance)), ("neighbor", ("neighbor", ClearOspfv3StatisticsNeighbor.Input.Neighbor))])
            self._leafs = OrderedDict()

            self.instance = ClearOspfv3StatisticsNeighbor.Input.Instance()
            self.instance.parent = self
            self._children_name_map["instance"] = "instance"

            self.neighbor = ClearOspfv3StatisticsNeighbor.Input.Neighbor()
            self.neighbor.parent = self
            self._children_name_map["neighbor"] = "neighbor"
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-ospfv3-act:clear-ospfv3-statistics-neighbor/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(ClearOspfv3StatisticsNeighbor.Input, [], name, value)


        class Instance(Entity):
            """
            Clear data from OSPFv3 instance
            
            .. attribute:: instance_identifier
            
            	OSPFv3 process instance identifier
            	**type**\: str
            
            

            """

            _prefix = 'ospfv3-act'
            _revision = '2016-09-14'

            def __init__(self):
                super(ClearOspfv3StatisticsNeighbor.Input.Instance, self).__init__()

                self.yang_name = "instance"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('instance_identifier', (YLeaf(YType.str, 'instance-identifier'), ['str'])),
                ])
                self.instance_identifier = None
                self._segment_path = lambda: "instance"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-ospfv3-act:clear-ospfv3-statistics-neighbor/input/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ClearOspfv3StatisticsNeighbor.Input.Instance, ['instance_identifier'], name, value)


        class Neighbor(Entity):
            """
            
            
            .. attribute:: neighbor_id
            
            	Neighbor ID
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: interface_name
            
            	Interface
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
            
            

            """

            _prefix = 'ospfv3-act'
            _revision = '2016-09-14'

            def __init__(self):
                super(ClearOspfv3StatisticsNeighbor.Input.Neighbor, self).__init__()

                self.yang_name = "neighbor"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('neighbor_id', (YLeaf(YType.str, 'neighbor-id'), ['str'])),
                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                ])
                self.neighbor_id = None
                self.interface_name = None
                self._segment_path = lambda: "neighbor"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-ospfv3-act:clear-ospfv3-statistics-neighbor/input/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ClearOspfv3StatisticsNeighbor.Input.Neighbor, ['neighbor_id', 'interface_name'], name, value)

    def clone_ptr(self):
        self._top_entity = ClearOspfv3StatisticsNeighbor()
        return self._top_entity

class ClearOspfv3Statistics(Entity):
    """
    Clear OSPFv3 counters and statistics
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act.ClearOspfv3Statistics.Input>`
    
    

    """

    _prefix = 'ospfv3-act'
    _revision = '2016-09-14'

    def __init__(self):
        super(ClearOspfv3Statistics, self).__init__()
        self._top_entity = None

        self.yang_name = "clear-ospfv3-statistics"
        self.yang_parent_name = "Cisco-IOS-XR-ipv6-ospfv3-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = ClearOspfv3Statistics.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._segment_path = lambda: "Cisco-IOS-XR-ipv6-ospfv3-act:clear-ospfv3-statistics"
        self._is_frozen = True


    class Input(Entity):
        """
        
        
        .. attribute:: instance
        
        	Clear data from OSPFv3 instance
        	**type**\:  :py:class:`Instance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act.ClearOspfv3Statistics.Input.Instance>`
        
        .. attribute:: prefix_priority
        
        	All OSPFv3 counters and statistics
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: spf
        
        	SPF statistics
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: neighbor
        
        	Neighbor statistics per neighbor id
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'ospfv3-act'
        _revision = '2016-09-14'

        def __init__(self):
            super(ClearOspfv3Statistics.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "clear-ospfv3-statistics"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("instance", ("instance", ClearOspfv3Statistics.Input.Instance))])
            self._leafs = OrderedDict([
                ('prefix_priority', (YLeaf(YType.empty, 'prefix-priority'), ['Empty'])),
                ('spf', (YLeaf(YType.empty, 'spf'), ['Empty'])),
                ('neighbor', (YLeaf(YType.empty, 'neighbor'), ['Empty'])),
            ])
            self.prefix_priority = None
            self.spf = None
            self.neighbor = None

            self.instance = ClearOspfv3Statistics.Input.Instance()
            self.instance.parent = self
            self._children_name_map["instance"] = "instance"
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-ospfv3-act:clear-ospfv3-statistics/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(ClearOspfv3Statistics.Input, ['prefix_priority', 'spf', 'neighbor'], name, value)


        class Instance(Entity):
            """
            Clear data from OSPFv3 instance
            
            .. attribute:: instance_identifier
            
            	OSPFv3 process instance identifier
            	**type**\: str
            
            

            """

            _prefix = 'ospfv3-act'
            _revision = '2016-09-14'

            def __init__(self):
                super(ClearOspfv3Statistics.Input.Instance, self).__init__()

                self.yang_name = "instance"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('instance_identifier', (YLeaf(YType.str, 'instance-identifier'), ['str'])),
                ])
                self.instance_identifier = None
                self._segment_path = lambda: "instance"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-ospfv3-act:clear-ospfv3-statistics/input/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ClearOspfv3Statistics.Input.Instance, ['instance_identifier'], name, value)

    def clone_ptr(self):
        self._top_entity = ClearOspfv3Statistics()
        return self._top_entity

class ClearOspfv3InstanceVrf(Entity):
    """
    Clear one or more non\-default OSPFv3 VRFs in process
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act.ClearOspfv3InstanceVrf.Input>`
    
    

    """

    _prefix = 'ospfv3-act'
    _revision = '2016-09-14'

    def __init__(self):
        super(ClearOspfv3InstanceVrf, self).__init__()
        self._top_entity = None

        self.yang_name = "clear-ospfv3-instance-vrf"
        self.yang_parent_name = "Cisco-IOS-XR-ipv6-ospfv3-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = ClearOspfv3InstanceVrf.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._segment_path = lambda: "Cisco-IOS-XR-ipv6-ospfv3-act:clear-ospfv3-instance-vrf"
        self._is_frozen = True


    class Input(Entity):
        """
        
        
        .. attribute:: instance
        
        	OSPFv3 instance name
        	**type**\:  :py:class:`Instance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act.ClearOspfv3InstanceVrf.Input.Instance>`
        
        

        """

        _prefix = 'ospfv3-act'
        _revision = '2016-09-14'

        def __init__(self):
            super(ClearOspfv3InstanceVrf.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "clear-ospfv3-instance-vrf"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("instance", ("instance", ClearOspfv3InstanceVrf.Input.Instance))])
            self._leafs = OrderedDict()

            self.instance = ClearOspfv3InstanceVrf.Input.Instance()
            self.instance.parent = self
            self._children_name_map["instance"] = "instance"
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-ospfv3-act:clear-ospfv3-instance-vrf/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(ClearOspfv3InstanceVrf.Input, [], name, value)


        class Instance(Entity):
            """
            OSPFv3 instance name
            
            .. attribute:: instance_identifier
            
            	OSPFv3 process instance identifier
            	**type**\: str
            
            	**mandatory**\: True
            
            .. attribute:: vrf
            
            	Clear one or more non\-default OSPFv3 VRFs in process
            	**type**\:  :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act.ClearOspfv3InstanceVrf.Input.Instance.Vrf>`
            
            .. attribute:: all
            
            	Clear all non\-default OSPFv3 VRFs
            	**type**\:  :py:class:`All <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act.ClearOspfv3InstanceVrf.Input.Instance.All>`
            
            .. attribute:: all_inclusive
            
            	Clear all non\-default and default OSPFv3 VRFs
            	**type**\:  :py:class:`AllInclusive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act.ClearOspfv3InstanceVrf.Input.Instance.AllInclusive>`
            
            

            """

            _prefix = 'ospfv3-act'
            _revision = '2016-09-14'

            def __init__(self):
                super(ClearOspfv3InstanceVrf.Input.Instance, self).__init__()

                self.yang_name = "instance"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("vrf", ("vrf", ClearOspfv3InstanceVrf.Input.Instance.Vrf)), ("all", ("all", ClearOspfv3InstanceVrf.Input.Instance.All)), ("all-inclusive", ("all_inclusive", ClearOspfv3InstanceVrf.Input.Instance.AllInclusive))])
                self._leafs = OrderedDict([
                    ('instance_identifier', (YLeaf(YType.str, 'instance-identifier'), ['str'])),
                ])
                self.instance_identifier = None

                self.vrf = ClearOspfv3InstanceVrf.Input.Instance.Vrf()
                self.vrf.parent = self
                self._children_name_map["vrf"] = "vrf"

                self.all = ClearOspfv3InstanceVrf.Input.Instance.All()
                self.all.parent = self
                self._children_name_map["all"] = "all"

                self.all_inclusive = ClearOspfv3InstanceVrf.Input.Instance.AllInclusive()
                self.all_inclusive.parent = self
                self._children_name_map["all_inclusive"] = "all-inclusive"
                self._segment_path = lambda: "instance"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-ospfv3-act:clear-ospfv3-instance-vrf/input/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ClearOspfv3InstanceVrf.Input.Instance, ['instance_identifier'], name, value)


            class Vrf(Entity):
                """
                Clear one or more non\-default OSPFv3 VRFs in process
                
                .. attribute:: vrf_name
                
                	OSPFv3 VRF name
                	**type**\: str
                
                	**mandatory**\: True
                
                .. attribute:: process
                
                	Reset OSPFv3 process
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: redistribution
                
                	Clear OSPFv3 route redistrbution
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: route
                
                	Clear OSPFv3 route table
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: stats
                
                	OSPFv3 counters and statistics
                	**type**\:  :py:class:`Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act.ClearOspfv3InstanceVrf.Input.Instance.Vrf.Stats>`
                
                

                """

                _prefix = 'ospfv3-act'
                _revision = '2016-09-14'

                def __init__(self):
                    super(ClearOspfv3InstanceVrf.Input.Instance.Vrf, self).__init__()

                    self.yang_name = "vrf"
                    self.yang_parent_name = "instance"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("stats", ("stats", ClearOspfv3InstanceVrf.Input.Instance.Vrf.Stats))])
                    self._leafs = OrderedDict([
                        ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                        ('process', (YLeaf(YType.empty, 'process'), ['Empty'])),
                        ('redistribution', (YLeaf(YType.empty, 'redistribution'), ['Empty'])),
                        ('route', (YLeaf(YType.empty, 'route'), ['Empty'])),
                    ])
                    self.vrf_name = None
                    self.process = None
                    self.redistribution = None
                    self.route = None

                    self.stats = ClearOspfv3InstanceVrf.Input.Instance.Vrf.Stats()
                    self.stats.parent = self
                    self._children_name_map["stats"] = "stats"
                    self._segment_path = lambda: "vrf"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-ospfv3-act:clear-ospfv3-instance-vrf/input/instance/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(ClearOspfv3InstanceVrf.Input.Instance.Vrf, ['vrf_name', 'process', 'redistribution', 'route'], name, value)


                class Stats(Entity):
                    """
                    OSPFv3 counters and statistics
                    
                    .. attribute:: spf
                    
                    	SPF statistics
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: prefix_priority
                    
                    	SPF Prefix Priority statistics
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: neighbor
                    
                    	Neighbor statistics per interface or neighbor id
                    	**type**\:  :py:class:`Neighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act.ClearOspfv3InstanceVrf.Input.Instance.Vrf.Stats.Neighbor>`
                    
                    

                    """

                    _prefix = 'ospfv3-act'
                    _revision = '2016-09-14'

                    def __init__(self):
                        super(ClearOspfv3InstanceVrf.Input.Instance.Vrf.Stats, self).__init__()

                        self.yang_name = "stats"
                        self.yang_parent_name = "vrf"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("neighbor", ("neighbor", ClearOspfv3InstanceVrf.Input.Instance.Vrf.Stats.Neighbor))])
                        self._leafs = OrderedDict([
                            ('spf', (YLeaf(YType.empty, 'spf'), ['Empty'])),
                            ('prefix_priority', (YLeaf(YType.empty, 'prefix-priority'), ['Empty'])),
                        ])
                        self.spf = None
                        self.prefix_priority = None

                        self.neighbor = ClearOspfv3InstanceVrf.Input.Instance.Vrf.Stats.Neighbor()
                        self.neighbor.parent = self
                        self._children_name_map["neighbor"] = "neighbor"
                        self._segment_path = lambda: "stats"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-ospfv3-act:clear-ospfv3-instance-vrf/input/instance/vrf/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ClearOspfv3InstanceVrf.Input.Instance.Vrf.Stats, ['spf', 'prefix_priority'], name, value)


                    class Neighbor(Entity):
                        """
                        Neighbor statistics per interface or neighbor id
                        
                        .. attribute:: neighbor_id
                        
                        	Neighbor ID
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: interface
                        
                        	
                        	**type**\:  :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act.ClearOspfv3InstanceVrf.Input.Instance.Vrf.Stats.Neighbor.Interface>`
                        
                        

                        """

                        _prefix = 'ospfv3-act'
                        _revision = '2016-09-14'

                        def __init__(self):
                            super(ClearOspfv3InstanceVrf.Input.Instance.Vrf.Stats.Neighbor, self).__init__()

                            self.yang_name = "neighbor"
                            self.yang_parent_name = "stats"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("interface", ("interface", ClearOspfv3InstanceVrf.Input.Instance.Vrf.Stats.Neighbor.Interface))])
                            self._leafs = OrderedDict([
                                ('neighbor_id', (YLeaf(YType.str, 'neighbor-id'), ['str'])),
                            ])
                            self.neighbor_id = None

                            self.interface = ClearOspfv3InstanceVrf.Input.Instance.Vrf.Stats.Neighbor.Interface()
                            self.interface.parent = self
                            self._children_name_map["interface"] = "interface"
                            self._segment_path = lambda: "neighbor"
                            self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-ospfv3-act:clear-ospfv3-instance-vrf/input/instance/vrf/stats/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(ClearOspfv3InstanceVrf.Input.Instance.Vrf.Stats.Neighbor, ['neighbor_id'], name, value)


                        class Interface(Entity):
                            """
                            
                            
                            .. attribute:: interface_name
                            
                            	OSPFv3 interface statistics
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            

                            """

                            _prefix = 'ospfv3-act'
                            _revision = '2016-09-14'

                            def __init__(self):
                                super(ClearOspfv3InstanceVrf.Input.Instance.Vrf.Stats.Neighbor.Interface, self).__init__()

                                self.yang_name = "interface"
                                self.yang_parent_name = "neighbor"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                ])
                                self.interface_name = None
                                self._segment_path = lambda: "interface"
                                self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-ospfv3-act:clear-ospfv3-instance-vrf/input/instance/vrf/stats/neighbor/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(ClearOspfv3InstanceVrf.Input.Instance.Vrf.Stats.Neighbor.Interface, ['interface_name'], name, value)


            class All(Entity):
                """
                Clear all non\-default OSPFv3 VRFs
                
                .. attribute:: process
                
                	Reset OSPFv3 process
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: redistribution
                
                	Clear OSPFv3 route redistrbution
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: route
                
                	Clear OSPFv3 route table
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: stats
                
                	OSPFv3 counters and statistics
                	**type**\:  :py:class:`Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act.ClearOspfv3InstanceVrf.Input.Instance.All.Stats>`
                
                

                """

                _prefix = 'ospfv3-act'
                _revision = '2016-09-14'

                def __init__(self):
                    super(ClearOspfv3InstanceVrf.Input.Instance.All, self).__init__()

                    self.yang_name = "all"
                    self.yang_parent_name = "instance"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("stats", ("stats", ClearOspfv3InstanceVrf.Input.Instance.All.Stats))])
                    self._leafs = OrderedDict([
                        ('process', (YLeaf(YType.empty, 'process'), ['Empty'])),
                        ('redistribution', (YLeaf(YType.empty, 'redistribution'), ['Empty'])),
                        ('route', (YLeaf(YType.empty, 'route'), ['Empty'])),
                    ])
                    self.process = None
                    self.redistribution = None
                    self.route = None

                    self.stats = ClearOspfv3InstanceVrf.Input.Instance.All.Stats()
                    self.stats.parent = self
                    self._children_name_map["stats"] = "stats"
                    self._segment_path = lambda: "all"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-ospfv3-act:clear-ospfv3-instance-vrf/input/instance/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(ClearOspfv3InstanceVrf.Input.Instance.All, ['process', 'redistribution', 'route'], name, value)


                class Stats(Entity):
                    """
                    OSPFv3 counters and statistics
                    
                    .. attribute:: spf
                    
                    	SPF statistics
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: prefix_priority
                    
                    	SPF Prefix Priority statistics
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: neighbor
                    
                    	Neighbor statistics per interface or neighbor id
                    	**type**\:  :py:class:`Neighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act.ClearOspfv3InstanceVrf.Input.Instance.All.Stats.Neighbor>`
                    
                    

                    """

                    _prefix = 'ospfv3-act'
                    _revision = '2016-09-14'

                    def __init__(self):
                        super(ClearOspfv3InstanceVrf.Input.Instance.All.Stats, self).__init__()

                        self.yang_name = "stats"
                        self.yang_parent_name = "all"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("neighbor", ("neighbor", ClearOspfv3InstanceVrf.Input.Instance.All.Stats.Neighbor))])
                        self._leafs = OrderedDict([
                            ('spf', (YLeaf(YType.empty, 'spf'), ['Empty'])),
                            ('prefix_priority', (YLeaf(YType.empty, 'prefix-priority'), ['Empty'])),
                        ])
                        self.spf = None
                        self.prefix_priority = None

                        self.neighbor = ClearOspfv3InstanceVrf.Input.Instance.All.Stats.Neighbor()
                        self.neighbor.parent = self
                        self._children_name_map["neighbor"] = "neighbor"
                        self._segment_path = lambda: "stats"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-ospfv3-act:clear-ospfv3-instance-vrf/input/instance/all/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ClearOspfv3InstanceVrf.Input.Instance.All.Stats, ['spf', 'prefix_priority'], name, value)


                    class Neighbor(Entity):
                        """
                        Neighbor statistics per interface or neighbor id
                        
                        .. attribute:: neighbor_id
                        
                        	Neighbor ID
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: interface
                        
                        	
                        	**type**\:  :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act.ClearOspfv3InstanceVrf.Input.Instance.All.Stats.Neighbor.Interface>`
                        
                        

                        """

                        _prefix = 'ospfv3-act'
                        _revision = '2016-09-14'

                        def __init__(self):
                            super(ClearOspfv3InstanceVrf.Input.Instance.All.Stats.Neighbor, self).__init__()

                            self.yang_name = "neighbor"
                            self.yang_parent_name = "stats"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("interface", ("interface", ClearOspfv3InstanceVrf.Input.Instance.All.Stats.Neighbor.Interface))])
                            self._leafs = OrderedDict([
                                ('neighbor_id', (YLeaf(YType.str, 'neighbor-id'), ['str'])),
                            ])
                            self.neighbor_id = None

                            self.interface = ClearOspfv3InstanceVrf.Input.Instance.All.Stats.Neighbor.Interface()
                            self.interface.parent = self
                            self._children_name_map["interface"] = "interface"
                            self._segment_path = lambda: "neighbor"
                            self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-ospfv3-act:clear-ospfv3-instance-vrf/input/instance/all/stats/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(ClearOspfv3InstanceVrf.Input.Instance.All.Stats.Neighbor, ['neighbor_id'], name, value)


                        class Interface(Entity):
                            """
                            
                            
                            .. attribute:: interface_name
                            
                            	OSPFv3 interface statistics
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            

                            """

                            _prefix = 'ospfv3-act'
                            _revision = '2016-09-14'

                            def __init__(self):
                                super(ClearOspfv3InstanceVrf.Input.Instance.All.Stats.Neighbor.Interface, self).__init__()

                                self.yang_name = "interface"
                                self.yang_parent_name = "neighbor"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                ])
                                self.interface_name = None
                                self._segment_path = lambda: "interface"
                                self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-ospfv3-act:clear-ospfv3-instance-vrf/input/instance/all/stats/neighbor/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(ClearOspfv3InstanceVrf.Input.Instance.All.Stats.Neighbor.Interface, ['interface_name'], name, value)


            class AllInclusive(Entity):
                """
                Clear all non\-default and default OSPFv3 VRFs
                
                .. attribute:: process
                
                	Reset OSPFv3 process
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: redistribution
                
                	Clear OSPFv3 route redistrbution
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: route
                
                	Clear OSPFv3 route table
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: stats
                
                	OSPFv3 counters and statistics
                	**type**\:  :py:class:`Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act.ClearOspfv3InstanceVrf.Input.Instance.AllInclusive.Stats>`
                
                

                """

                _prefix = 'ospfv3-act'
                _revision = '2016-09-14'

                def __init__(self):
                    super(ClearOspfv3InstanceVrf.Input.Instance.AllInclusive, self).__init__()

                    self.yang_name = "all-inclusive"
                    self.yang_parent_name = "instance"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("stats", ("stats", ClearOspfv3InstanceVrf.Input.Instance.AllInclusive.Stats))])
                    self._leafs = OrderedDict([
                        ('process', (YLeaf(YType.empty, 'process'), ['Empty'])),
                        ('redistribution', (YLeaf(YType.empty, 'redistribution'), ['Empty'])),
                        ('route', (YLeaf(YType.empty, 'route'), ['Empty'])),
                    ])
                    self.process = None
                    self.redistribution = None
                    self.route = None

                    self.stats = ClearOspfv3InstanceVrf.Input.Instance.AllInclusive.Stats()
                    self.stats.parent = self
                    self._children_name_map["stats"] = "stats"
                    self._segment_path = lambda: "all-inclusive"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-ospfv3-act:clear-ospfv3-instance-vrf/input/instance/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(ClearOspfv3InstanceVrf.Input.Instance.AllInclusive, ['process', 'redistribution', 'route'], name, value)


                class Stats(Entity):
                    """
                    OSPFv3 counters and statistics
                    
                    .. attribute:: spf
                    
                    	SPF statistics
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: prefix_priority
                    
                    	SPF Prefix Priority statistics
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: neighbor
                    
                    	Neighbor statistics per interface or neighbor id
                    	**type**\:  :py:class:`Neighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act.ClearOspfv3InstanceVrf.Input.Instance.AllInclusive.Stats.Neighbor>`
                    
                    

                    """

                    _prefix = 'ospfv3-act'
                    _revision = '2016-09-14'

                    def __init__(self):
                        super(ClearOspfv3InstanceVrf.Input.Instance.AllInclusive.Stats, self).__init__()

                        self.yang_name = "stats"
                        self.yang_parent_name = "all-inclusive"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("neighbor", ("neighbor", ClearOspfv3InstanceVrf.Input.Instance.AllInclusive.Stats.Neighbor))])
                        self._leafs = OrderedDict([
                            ('spf', (YLeaf(YType.empty, 'spf'), ['Empty'])),
                            ('prefix_priority', (YLeaf(YType.empty, 'prefix-priority'), ['Empty'])),
                        ])
                        self.spf = None
                        self.prefix_priority = None

                        self.neighbor = ClearOspfv3InstanceVrf.Input.Instance.AllInclusive.Stats.Neighbor()
                        self.neighbor.parent = self
                        self._children_name_map["neighbor"] = "neighbor"
                        self._segment_path = lambda: "stats"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-ospfv3-act:clear-ospfv3-instance-vrf/input/instance/all-inclusive/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ClearOspfv3InstanceVrf.Input.Instance.AllInclusive.Stats, ['spf', 'prefix_priority'], name, value)


                    class Neighbor(Entity):
                        """
                        Neighbor statistics per interface or neighbor id
                        
                        .. attribute:: neighbor_id
                        
                        	Neighbor ID
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: interface
                        
                        	
                        	**type**\:  :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act.ClearOspfv3InstanceVrf.Input.Instance.AllInclusive.Stats.Neighbor.Interface>`
                        
                        

                        """

                        _prefix = 'ospfv3-act'
                        _revision = '2016-09-14'

                        def __init__(self):
                            super(ClearOspfv3InstanceVrf.Input.Instance.AllInclusive.Stats.Neighbor, self).__init__()

                            self.yang_name = "neighbor"
                            self.yang_parent_name = "stats"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("interface", ("interface", ClearOspfv3InstanceVrf.Input.Instance.AllInclusive.Stats.Neighbor.Interface))])
                            self._leafs = OrderedDict([
                                ('neighbor_id', (YLeaf(YType.str, 'neighbor-id'), ['str'])),
                            ])
                            self.neighbor_id = None

                            self.interface = ClearOspfv3InstanceVrf.Input.Instance.AllInclusive.Stats.Neighbor.Interface()
                            self.interface.parent = self
                            self._children_name_map["interface"] = "interface"
                            self._segment_path = lambda: "neighbor"
                            self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-ospfv3-act:clear-ospfv3-instance-vrf/input/instance/all-inclusive/stats/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(ClearOspfv3InstanceVrf.Input.Instance.AllInclusive.Stats.Neighbor, ['neighbor_id'], name, value)


                        class Interface(Entity):
                            """
                            
                            
                            .. attribute:: interface_name
                            
                            	OSPFv3 interface statistics
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            

                            """

                            _prefix = 'ospfv3-act'
                            _revision = '2016-09-14'

                            def __init__(self):
                                super(ClearOspfv3InstanceVrf.Input.Instance.AllInclusive.Stats.Neighbor.Interface, self).__init__()

                                self.yang_name = "interface"
                                self.yang_parent_name = "neighbor"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                ])
                                self.interface_name = None
                                self._segment_path = lambda: "interface"
                                self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-ospfv3-act:clear-ospfv3-instance-vrf/input/instance/all-inclusive/stats/neighbor/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(ClearOspfv3InstanceVrf.Input.Instance.AllInclusive.Stats.Neighbor.Interface, ['interface_name'], name, value)

    def clone_ptr(self):
        self._top_entity = ClearOspfv3InstanceVrf()
        return self._top_entity

