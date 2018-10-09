""" Cisco_IOS_XR_infra_rmf_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-rmf package operational data.

This module contains definitions
for the following management objects\:
  redundancy\: Redundancy show information

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class Redundancy(Entity):
    """
    Redundancy show information
    
    .. attribute:: nodes
    
    	Location show information
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rmf_oper.Redundancy.Nodes>`
    
    .. attribute:: summary
    
    	Redundancy Summary of Nodes
    	**type**\:  :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rmf_oper.Redundancy.Summary>`
    
    

    """

    _prefix = 'infra-rmf-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Redundancy, self).__init__()
        self._top_entity = None

        self.yang_name = "redundancy"
        self.yang_parent_name = "Cisco-IOS-XR-infra-rmf-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("nodes", ("nodes", Redundancy.Nodes)), ("summary", ("summary", Redundancy.Summary))])
        self._leafs = OrderedDict()

        self.nodes = Redundancy.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"

        self.summary = Redundancy.Summary()
        self.summary.parent = self
        self._children_name_map["summary"] = "summary"
        self._segment_path = lambda: "Cisco-IOS-XR-infra-rmf-oper:redundancy"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Redundancy, [], name, value)


    class Nodes(Entity):
        """
        Location show information
        
        .. attribute:: node
        
        	Redundancy Node Information
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rmf_oper.Redundancy.Nodes.Node>`
        
        

        """

        _prefix = 'infra-rmf-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Redundancy.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "redundancy"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("node", ("node", Redundancy.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-rmf-oper:redundancy/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Redundancy.Nodes, [], name, value)


        class Node(Entity):
            """
            Redundancy Node Information
            
            .. attribute:: node_id  (key)
            
            	Node Location
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: redundancy
            
            	Row information
            	**type**\:  :py:class:`Redundancy_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rmf_oper.Redundancy.Nodes.Node.Redundancy_>`
            
            .. attribute:: log
            
            	Reload and boot logs
            	**type**\: str
            
            .. attribute:: active_reboot_reason
            
            	Active node reload
            	**type**\: str
            
            .. attribute:: standby_reboot_reason
            
            	Standby node reload
            	**type**\: str
            
            .. attribute:: err_log
            
            	Error Log
            	**type**\: str
            
            

            """

            _prefix = 'infra-rmf-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Redundancy.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_id']
                self._child_classes = OrderedDict([("redundancy", ("redundancy", Redundancy.Nodes.Node.Redundancy_))])
                self._leafs = OrderedDict([
                    ('node_id', (YLeaf(YType.str, 'node-id'), ['str'])),
                    ('log', (YLeaf(YType.str, 'log'), ['str'])),
                    ('active_reboot_reason', (YLeaf(YType.str, 'active-reboot-reason'), ['str'])),
                    ('standby_reboot_reason', (YLeaf(YType.str, 'standby-reboot-reason'), ['str'])),
                    ('err_log', (YLeaf(YType.str, 'err-log'), ['str'])),
                ])
                self.node_id = None
                self.log = None
                self.active_reboot_reason = None
                self.standby_reboot_reason = None
                self.err_log = None

                self.redundancy = Redundancy.Nodes.Node.Redundancy_()
                self.redundancy.parent = self
                self._children_name_map["redundancy"] = "redundancy"
                self._segment_path = lambda: "node" + "[node-id='" + str(self.node_id) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-rmf-oper:redundancy/nodes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Redundancy.Nodes.Node, ['node_id', u'log', u'active_reboot_reason', u'standby_reboot_reason', u'err_log'], name, value)


            class Redundancy_(Entity):
                """
                Row information
                
                .. attribute:: active
                
                	Active node name R/S/I
                	**type**\: str
                
                .. attribute:: standby
                
                	Standby node name R/S/I
                	**type**\: str
                
                .. attribute:: ha_state
                
                	High Availability state Ready/Not Ready
                	**type**\: str
                
                .. attribute:: nsr_state
                
                	NSR state Configured/Not Configured
                	**type**\: str
                
                .. attribute:: groupinfo
                
                	groupinfo
                	**type**\: list of  		 :py:class:`Groupinfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rmf_oper.Redundancy.Nodes.Node.Redundancy_.Groupinfo>`
                
                

                """

                _prefix = 'infra-rmf-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Redundancy.Nodes.Node.Redundancy_, self).__init__()

                    self.yang_name = "redundancy"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("groupinfo", ("groupinfo", Redundancy.Nodes.Node.Redundancy_.Groupinfo))])
                    self._leafs = OrderedDict([
                        ('active', (YLeaf(YType.str, 'active'), ['str'])),
                        ('standby', (YLeaf(YType.str, 'standby'), ['str'])),
                        ('ha_state', (YLeaf(YType.str, 'ha-state'), ['str'])),
                        ('nsr_state', (YLeaf(YType.str, 'nsr-state'), ['str'])),
                    ])
                    self.active = None
                    self.standby = None
                    self.ha_state = None
                    self.nsr_state = None

                    self.groupinfo = YList(self)
                    self._segment_path = lambda: "redundancy"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Redundancy.Nodes.Node.Redundancy_, [u'active', u'standby', u'ha_state', u'nsr_state'], name, value)


                class Groupinfo(Entity):
                    """
                    groupinfo
                    
                    .. attribute:: active
                    
                    	Active
                    	**type**\: str
                    
                    .. attribute:: standby
                    
                    	Standby
                    	**type**\: str
                    
                    .. attribute:: ha_state
                    
                    	HAState
                    	**type**\: str
                    
                    .. attribute:: nsr_state
                    
                    	NSRState
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'infra-rmf-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Redundancy.Nodes.Node.Redundancy_.Groupinfo, self).__init__()

                        self.yang_name = "groupinfo"
                        self.yang_parent_name = "redundancy"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('active', (YLeaf(YType.str, 'active'), ['str'])),
                            ('standby', (YLeaf(YType.str, 'standby'), ['str'])),
                            ('ha_state', (YLeaf(YType.str, 'ha-state'), ['str'])),
                            ('nsr_state', (YLeaf(YType.str, 'nsr-state'), ['str'])),
                        ])
                        self.active = None
                        self.standby = None
                        self.ha_state = None
                        self.nsr_state = None
                        self._segment_path = lambda: "groupinfo"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Redundancy.Nodes.Node.Redundancy_.Groupinfo, [u'active', u'standby', u'ha_state', u'nsr_state'], name, value)


    class Summary(Entity):
        """
        Redundancy Summary of Nodes
        
        .. attribute:: err_log
        
        	Error Log
        	**type**\: str
        
        .. attribute:: red_pair
        
        	Redundancy Pair
        	**type**\: list of  		 :py:class:`RedPair <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rmf_oper.Redundancy.Summary.RedPair>`
        
        

        """

        _prefix = 'infra-rmf-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Redundancy.Summary, self).__init__()

            self.yang_name = "summary"
            self.yang_parent_name = "redundancy"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("red-pair", ("red_pair", Redundancy.Summary.RedPair))])
            self._leafs = OrderedDict([
                ('err_log', (YLeaf(YType.str, 'err-log'), ['str'])),
            ])
            self.err_log = None

            self.red_pair = YList(self)
            self._segment_path = lambda: "summary"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-rmf-oper:redundancy/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Redundancy.Summary, [u'err_log'], name, value)


        class RedPair(Entity):
            """
            Redundancy Pair
            
            .. attribute:: active
            
            	Active node name R/S/I
            	**type**\: str
            
            .. attribute:: standby
            
            	Standby node name R/S/I
            	**type**\: str
            
            .. attribute:: ha_state
            
            	High Availability state Ready/Not Ready
            	**type**\: str
            
            .. attribute:: nsr_state
            
            	NSR state Configured/Not Configured
            	**type**\: str
            
            .. attribute:: groupinfo
            
            	groupinfo
            	**type**\: list of  		 :py:class:`Groupinfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rmf_oper.Redundancy.Summary.RedPair.Groupinfo>`
            
            

            """

            _prefix = 'infra-rmf-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Redundancy.Summary.RedPair, self).__init__()

                self.yang_name = "red-pair"
                self.yang_parent_name = "summary"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("groupinfo", ("groupinfo", Redundancy.Summary.RedPair.Groupinfo))])
                self._leafs = OrderedDict([
                    ('active', (YLeaf(YType.str, 'active'), ['str'])),
                    ('standby', (YLeaf(YType.str, 'standby'), ['str'])),
                    ('ha_state', (YLeaf(YType.str, 'ha-state'), ['str'])),
                    ('nsr_state', (YLeaf(YType.str, 'nsr-state'), ['str'])),
                ])
                self.active = None
                self.standby = None
                self.ha_state = None
                self.nsr_state = None

                self.groupinfo = YList(self)
                self._segment_path = lambda: "red-pair"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-rmf-oper:redundancy/summary/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Redundancy.Summary.RedPair, [u'active', u'standby', u'ha_state', u'nsr_state'], name, value)


            class Groupinfo(Entity):
                """
                groupinfo
                
                .. attribute:: active
                
                	Active
                	**type**\: str
                
                .. attribute:: standby
                
                	Standby
                	**type**\: str
                
                .. attribute:: ha_state
                
                	HAState
                	**type**\: str
                
                .. attribute:: nsr_state
                
                	NSRState
                	**type**\: str
                
                

                """

                _prefix = 'infra-rmf-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Redundancy.Summary.RedPair.Groupinfo, self).__init__()

                    self.yang_name = "groupinfo"
                    self.yang_parent_name = "red-pair"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('active', (YLeaf(YType.str, 'active'), ['str'])),
                        ('standby', (YLeaf(YType.str, 'standby'), ['str'])),
                        ('ha_state', (YLeaf(YType.str, 'ha-state'), ['str'])),
                        ('nsr_state', (YLeaf(YType.str, 'nsr-state'), ['str'])),
                    ])
                    self.active = None
                    self.standby = None
                    self.ha_state = None
                    self.nsr_state = None
                    self._segment_path = lambda: "groupinfo"
                    self._absolute_path = lambda: "Cisco-IOS-XR-infra-rmf-oper:redundancy/summary/red-pair/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Redundancy.Summary.RedPair.Groupinfo, [u'active', u'standby', u'ha_state', u'nsr_state'], name, value)

    def clone_ptr(self):
        self._top_entity = Redundancy()
        return self._top_entity

