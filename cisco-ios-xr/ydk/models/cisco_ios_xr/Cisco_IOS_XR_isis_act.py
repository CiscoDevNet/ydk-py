""" Cisco_IOS_XR_isis_act 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ISIS action package configuration.

Copyright (c) 2016\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class ClearIsisProcess(Entity):
    """
    Clear all IS\-IS data structures
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_isis_act.ClearIsisProcess.Input>`
    
    

    """

    _prefix = 'isis-act'
    _revision = '2016-06-30'

    def __init__(self):
        super(ClearIsisProcess, self).__init__()
        self._top_entity = None

        self.yang_name = "clear-isis-process"
        self.yang_parent_name = "Cisco-IOS-XR-isis-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = ClearIsisProcess.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._segment_path = lambda: "Cisco-IOS-XR-isis-act:clear-isis-process"
        self._is_frozen = True


    class Input(Entity):
        """
        
        
        .. attribute:: instance
        
        	Clear data from single IS\-IS instance
        	**type**\:  :py:class:`Instance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_isis_act.ClearIsisProcess.Input.Instance>`
        
        .. attribute:: process
        
        	Clear all IS\-IS data structures
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'isis-act'
        _revision = '2016-06-30'

        def __init__(self):
            super(ClearIsisProcess.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "clear-isis-process"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("instance", ("instance", ClearIsisProcess.Input.Instance))])
            self._leafs = OrderedDict([
                ('process', (YLeaf(YType.empty, 'process'), ['Empty'])),
            ])
            self.process = None

            self.instance = ClearIsisProcess.Input.Instance()
            self.instance.parent = self
            self._children_name_map["instance"] = "instance"
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-isis-act:clear-isis-process/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(ClearIsisProcess.Input, ['process'], name, value)


        class Instance(Entity):
            """
            Clear data from single IS\-IS instance
            
            .. attribute:: instance_identifier
            
            	IS\-IS process instance identifier
            	**type**\: str
            
            

            """

            _prefix = 'isis-act'
            _revision = '2016-06-30'

            def __init__(self):
                super(ClearIsisProcess.Input.Instance, self).__init__()

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
                self._absolute_path = lambda: "Cisco-IOS-XR-isis-act:clear-isis-process/input/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ClearIsisProcess.Input.Instance, ['instance_identifier'], name, value)

    def clone_ptr(self):
        self._top_entity = ClearIsisProcess()
        return self._top_entity

class ClearIsisRoute(Entity):
    """
    Clear IS\-IS routes
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_isis_act.ClearIsisRoute.Input>`
    
    

    """

    _prefix = 'isis-act'
    _revision = '2016-06-30'

    def __init__(self):
        super(ClearIsisRoute, self).__init__()
        self._top_entity = None

        self.yang_name = "clear-isis-route"
        self.yang_parent_name = "Cisco-IOS-XR-isis-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = ClearIsisRoute.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._segment_path = lambda: "Cisco-IOS-XR-isis-act:clear-isis-route"
        self._is_frozen = True


    class Input(Entity):
        """
        
        
        .. attribute:: instance
        
        	Clear data from single IS\-IS instance
        	**type**\:  :py:class:`Instance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_isis_act.ClearIsisRoute.Input.Instance>`
        
        .. attribute:: route
        
        	Clear IS\-IS routes
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'isis-act'
        _revision = '2016-06-30'

        def __init__(self):
            super(ClearIsisRoute.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "clear-isis-route"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("instance", ("instance", ClearIsisRoute.Input.Instance))])
            self._leafs = OrderedDict([
                ('route', (YLeaf(YType.empty, 'route'), ['Empty'])),
            ])
            self.route = None

            self.instance = ClearIsisRoute.Input.Instance()
            self.instance.parent = self
            self._children_name_map["instance"] = "instance"
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-isis-act:clear-isis-route/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(ClearIsisRoute.Input, ['route'], name, value)


        class Instance(Entity):
            """
            Clear data from single IS\-IS instance
            
            .. attribute:: instance_identifier
            
            	IS\-IS process instance identifier
            	**type**\: str
            
            

            """

            _prefix = 'isis-act'
            _revision = '2016-06-30'

            def __init__(self):
                super(ClearIsisRoute.Input.Instance, self).__init__()

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
                self._absolute_path = lambda: "Cisco-IOS-XR-isis-act:clear-isis-route/input/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ClearIsisRoute.Input.Instance, ['instance_identifier'], name, value)

    def clone_ptr(self):
        self._top_entity = ClearIsisRoute()
        return self._top_entity

class ClearIsisStat(Entity):
    """
    Clear IS\-IS protocol statistics
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_isis_act.ClearIsisStat.Input>`
    
    

    """

    _prefix = 'isis-act'
    _revision = '2016-06-30'

    def __init__(self):
        super(ClearIsisStat, self).__init__()
        self._top_entity = None

        self.yang_name = "clear-isis-stat"
        self.yang_parent_name = "Cisco-IOS-XR-isis-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = ClearIsisStat.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._segment_path = lambda: "Cisco-IOS-XR-isis-act:clear-isis-stat"
        self._is_frozen = True


    class Input(Entity):
        """
        
        
        .. attribute:: instance
        
        	Clear data from single IS\-IS instance
        	**type**\:  :py:class:`Instance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_isis_act.ClearIsisStat.Input.Instance>`
        
        .. attribute:: statistics
        
        	Clear IS\-IS protocol statistics
        	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_isis_act.ClearIsisStat.Input.Statistics>`
        
        

        """

        _prefix = 'isis-act'
        _revision = '2016-06-30'

        def __init__(self):
            super(ClearIsisStat.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "clear-isis-stat"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("instance", ("instance", ClearIsisStat.Input.Instance)), ("statistics", ("statistics", ClearIsisStat.Input.Statistics))])
            self._leafs = OrderedDict()

            self.instance = ClearIsisStat.Input.Instance()
            self.instance.parent = self
            self._children_name_map["instance"] = "instance"

            self.statistics = ClearIsisStat.Input.Statistics()
            self.statistics.parent = self
            self._children_name_map["statistics"] = "statistics"
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-isis-act:clear-isis-stat/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(ClearIsisStat.Input, [], name, value)


        class Instance(Entity):
            """
            Clear data from single IS\-IS instance
            
            .. attribute:: instance_identifier
            
            	IS\-IS process instance identifier
            	**type**\: str
            
            

            """

            _prefix = 'isis-act'
            _revision = '2016-06-30'

            def __init__(self):
                super(ClearIsisStat.Input.Instance, self).__init__()

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
                self._absolute_path = lambda: "Cisco-IOS-XR-isis-act:clear-isis-stat/input/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ClearIsisStat.Input.Instance, ['instance_identifier'], name, value)


        class Statistics(Entity):
            """
            Clear IS\-IS protocol statistics
            
            .. attribute:: interface_name
            
            	Interface name
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
            
            	**mandatory**\: True
            
            

            """

            _prefix = 'isis-act'
            _revision = '2016-06-30'

            def __init__(self):
                super(ClearIsisStat.Input.Statistics, self).__init__()

                self.yang_name = "statistics"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                ])
                self.interface_name = None
                self._segment_path = lambda: "statistics"
                self._absolute_path = lambda: "Cisco-IOS-XR-isis-act:clear-isis-stat/input/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ClearIsisStat.Input.Statistics, ['interface_name'], name, value)

    def clone_ptr(self):
        self._top_entity = ClearIsisStat()
        return self._top_entity

class ClearIsisDist(Entity):
    """
    Reset BGP\-LS topology distribution
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_isis_act.ClearIsisDist.Input>`
    
    

    """

    _prefix = 'isis-act'
    _revision = '2016-06-30'

    def __init__(self):
        super(ClearIsisDist, self).__init__()
        self._top_entity = None

        self.yang_name = "clear-isis-dist"
        self.yang_parent_name = "Cisco-IOS-XR-isis-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = ClearIsisDist.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._segment_path = lambda: "Cisco-IOS-XR-isis-act:clear-isis-dist"
        self._is_frozen = True


    class Input(Entity):
        """
        
        
        .. attribute:: instance
        
        	Reset BGP\-LS topology from single IS\-IS instance
        	**type**\:  :py:class:`Instance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_isis_act.ClearIsisDist.Input.Instance>`
        
        .. attribute:: distribution
        
        	Reset BGP\-LS topology distribution
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'isis-act'
        _revision = '2016-06-30'

        def __init__(self):
            super(ClearIsisDist.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "clear-isis-dist"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("instance", ("instance", ClearIsisDist.Input.Instance))])
            self._leafs = OrderedDict([
                ('distribution', (YLeaf(YType.empty, 'distribution'), ['Empty'])),
            ])
            self.distribution = None

            self.instance = ClearIsisDist.Input.Instance()
            self.instance.parent = self
            self._children_name_map["instance"] = "instance"
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-isis-act:clear-isis-dist/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(ClearIsisDist.Input, ['distribution'], name, value)


        class Instance(Entity):
            """
            Reset BGP\-LS topology from single IS\-IS instance
            
            .. attribute:: instance_identifier
            
            	IS\-IS process instance identifier
            	**type**\: str
            
            

            """

            _prefix = 'isis-act'
            _revision = '2016-06-30'

            def __init__(self):
                super(ClearIsisDist.Input.Instance, self).__init__()

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
                self._absolute_path = lambda: "Cisco-IOS-XR-isis-act:clear-isis-dist/input/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ClearIsisDist.Input.Instance, ['instance_identifier'], name, value)

    def clone_ptr(self):
        self._top_entity = ClearIsisDist()
        return self._top_entity

class ClearIsisLocalLsp(Entity):
    """
    Clean and regenerate local LSPs
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_isis_act.ClearIsisLocalLsp.Input>`
    
    

    """

    _prefix = 'isis-act'
    _revision = '2016-06-30'

    def __init__(self):
        super(ClearIsisLocalLsp, self).__init__()
        self._top_entity = None

        self.yang_name = "clear-isis-local-lsp"
        self.yang_parent_name = "Cisco-IOS-XR-isis-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = ClearIsisLocalLsp.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._segment_path = lambda: "Cisco-IOS-XR-isis-act:clear-isis-local-lsp"
        self._is_frozen = True


    class Input(Entity):
        """
        
        
        .. attribute:: instance
        
        	Clean and regenerate local LSPs from single IS\-IS instance
        	**type**\:  :py:class:`Instance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_isis_act.ClearIsisLocalLsp.Input.Instance>`
        
        .. attribute:: local_lsp
        
        	Clean and regenerate local LSPs
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'isis-act'
        _revision = '2016-06-30'

        def __init__(self):
            super(ClearIsisLocalLsp.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "clear-isis-local-lsp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("instance", ("instance", ClearIsisLocalLsp.Input.Instance))])
            self._leafs = OrderedDict([
                ('local_lsp', (YLeaf(YType.empty, 'local-lsp'), ['Empty'])),
            ])
            self.local_lsp = None

            self.instance = ClearIsisLocalLsp.Input.Instance()
            self.instance.parent = self
            self._children_name_map["instance"] = "instance"
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-isis-act:clear-isis-local-lsp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(ClearIsisLocalLsp.Input, ['local_lsp'], name, value)


        class Instance(Entity):
            """
            Clean and regenerate local LSPs from single IS\-IS instance
            
            .. attribute:: instance_identifier
            
            	IS\-IS process instance identifier
            	**type**\: str
            
            

            """

            _prefix = 'isis-act'
            _revision = '2016-06-30'

            def __init__(self):
                super(ClearIsisLocalLsp.Input.Instance, self).__init__()

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
                self._absolute_path = lambda: "Cisco-IOS-XR-isis-act:clear-isis-local-lsp/input/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ClearIsisLocalLsp.Input.Instance, ['instance_identifier'], name, value)

    def clone_ptr(self):
        self._top_entity = ClearIsisLocalLsp()
        return self._top_entity

class ClearIsis(Entity):
    """
    Clear IS\-IS data structures
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_isis_act.ClearIsis.Input>`
    
    

    """

    _prefix = 'isis-act'
    _revision = '2016-06-30'

    def __init__(self):
        super(ClearIsis, self).__init__()
        self._top_entity = None

        self.yang_name = "clear-isis"
        self.yang_parent_name = "Cisco-IOS-XR-isis-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = ClearIsis.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._segment_path = lambda: "Cisco-IOS-XR-isis-act:clear-isis"
        self._is_frozen = True


    class Input(Entity):
        """
        
        
        .. attribute:: instance
        
        	Clear data from single IS\-IS instance
        	**type**\:  :py:class:`Instance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_isis_act.ClearIsis.Input.Instance>`
        
        .. attribute:: rt_type
        
        	Clear data for these route types
        	**type**\:  :py:class:`RtType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_isis_act.ClearIsis.Input.RtType>`
        
        .. attribute:: route
        
        	Clear IS\-IS routes
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: topology
        
        	Topology table information
        	**type**\: str
        
        

        """

        _prefix = 'isis-act'
        _revision = '2016-06-30'

        def __init__(self):
            super(ClearIsis.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "clear-isis"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("instance", ("instance", ClearIsis.Input.Instance))])
            self._leafs = OrderedDict([
                ('rt_type', (YLeaf(YType.enumeration, 'rt-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_isis_act', 'ClearIsis', 'Input.RtType')])),
                ('route', (YLeaf(YType.empty, 'route'), ['Empty'])),
                ('topology', (YLeaf(YType.str, 'topology'), ['str'])),
            ])
            self.rt_type = None
            self.route = None
            self.topology = None

            self.instance = ClearIsis.Input.Instance()
            self.instance.parent = self
            self._children_name_map["instance"] = "instance"
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-isis-act:clear-isis/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(ClearIsis.Input, ['rt_type', 'route', 'topology'], name, value)

        class RtType(Enum):
            """
            RtType (Enum Class)

            Clear data for these route types

            .. data:: AFI_ALL_MULTICAST = 0

            .. data:: AFI_ALL_SAFI_ALL = 1

            .. data:: AFI_ALL_UNICAST = 2

            .. data:: IPv4_MULTICAST = 3

            .. data:: IPv4_SAFI_ALL = 4

            .. data:: IPv4_UNICAST = 5

            .. data:: IPv6_MULTICAST = 6

            .. data:: IPv6_SAFI_ALL = 7

            .. data:: IPv6_UNICAST = 8

            """

            AFI_ALL_MULTICAST = Enum.YLeaf(0, "AFI-ALL-MULTICAST")

            AFI_ALL_SAFI_ALL = Enum.YLeaf(1, "AFI-ALL-SAFI-ALL")

            AFI_ALL_UNICAST = Enum.YLeaf(2, "AFI-ALL-UNICAST")

            IPv4_MULTICAST = Enum.YLeaf(3, "IPv4-MULTICAST")

            IPv4_SAFI_ALL = Enum.YLeaf(4, "IPv4-SAFI-ALL")

            IPv4_UNICAST = Enum.YLeaf(5, "IPv4-UNICAST")

            IPv6_MULTICAST = Enum.YLeaf(6, "IPv6-MULTICAST")

            IPv6_SAFI_ALL = Enum.YLeaf(7, "IPv6-SAFI-ALL")

            IPv6_UNICAST = Enum.YLeaf(8, "IPv6-UNICAST")



        class Instance(Entity):
            """
            Clear data from single IS\-IS instance
            
            .. attribute:: instance_identifier
            
            	IS\-IS process instance identifier
            	**type**\: str
            
            

            """

            _prefix = 'isis-act'
            _revision = '2016-06-30'

            def __init__(self):
                super(ClearIsis.Input.Instance, self).__init__()

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
                self._absolute_path = lambda: "Cisco-IOS-XR-isis-act:clear-isis/input/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ClearIsis.Input.Instance, ['instance_identifier'], name, value)

    def clone_ptr(self):
        self._top_entity = ClearIsis()
        return self._top_entity

