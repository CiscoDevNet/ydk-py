""" Cisco_IOS_XR_infra_rmf_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-rmf package operational data.

This module contains definitions
for the following management objects\:
  redundancy\: Redundancy show information

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




class Redundancy(_Entity_):
    """
    Redundancy show information
    
    .. attribute:: nodes
    
    	Location show information
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rmf_oper.Redundancy.Nodes>`
    
    	**config**\: False
    
    .. attribute:: summary
    
    	Redundancy Summary of Nodes
    	**type**\:  :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rmf_oper.Redundancy.Summary>`
    
    	**config**\: False
    
    

    """

    _prefix = 'infra-rmf-oper'
    _revision = '2015-11-09'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
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


    class Nodes(_Entity_):
        """
        Location show information
        
        .. attribute:: node
        
        	Redundancy Node Information
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rmf_oper.Redundancy.Nodes.Node>`
        
        	**config**\: False
        
        

        """

        _prefix = 'infra-rmf-oper'
        _revision = '2015-11-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
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


        class Node(_Entity_):
            """
            Redundancy Node Information
            
            .. attribute:: node_id  (key)
            
            	Node Location
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            	**config**\: False
            
            .. attribute:: redundancy
            
            	Row information
            	**type**\:  :py:class:`Redundancy_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rmf_oper.Redundancy.Nodes.Node.Redundancy_>`
            
            	**config**\: False
            
            .. attribute:: log
            
            	Reload and boot logs
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: active_reboot_reason
            
            	Active node reload
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: standby_reboot_reason
            
            	Standby node reload
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: err_log
            
            	Error Log
            	**type**\: str
            
            	**config**\: False
            
            

            """

            _prefix = 'infra-rmf-oper'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
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
                self._perform_setattr(Redundancy.Nodes.Node, ['node_id', 'log', 'active_reboot_reason', 'standby_reboot_reason', 'err_log'], name, value)


            class Redundancy_(_Entity_):
                """
                Row information
                
                .. attribute:: active
                
                	Active node name R/S/I
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: standby
                
                	Standby node name R/S/I
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: ha_state
                
                	High Availability state Ready/Not Ready
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: nsr_state
                
                	NSR state Configured/Not Configured
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: groupinfo
                
                	groupinfo
                	**type**\: list of  		 :py:class:`Groupinfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rmf_oper.Redundancy.Nodes.Node.Redundancy_.Groupinfo>`
                
                	**config**\: False
                
                

                """

                _prefix = 'infra-rmf-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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
                    self._perform_setattr(Redundancy.Nodes.Node.Redundancy_, ['active', 'standby', 'ha_state', 'nsr_state'], name, value)


                class Groupinfo(_Entity_):
                    """
                    groupinfo
                    
                    .. attribute:: active
                    
                    	Active
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: standby
                    
                    	Standby
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: ha_state
                    
                    	HAState
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: nsr_state
                    
                    	NSRState
                    	**type**\: str
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'infra-rmf-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
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
                        self._perform_setattr(Redundancy.Nodes.Node.Redundancy_.Groupinfo, ['active', 'standby', 'ha_state', 'nsr_state'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rmf_oper as meta
                        return meta._meta_table['Redundancy.Nodes.Node.Redundancy_.Groupinfo']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rmf_oper as meta
                    return meta._meta_table['Redundancy.Nodes.Node.Redundancy_']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rmf_oper as meta
                return meta._meta_table['Redundancy.Nodes.Node']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rmf_oper as meta
            return meta._meta_table['Redundancy.Nodes']['meta_info']


    class Summary(_Entity_):
        """
        Redundancy Summary of Nodes
        
        .. attribute:: err_log
        
        	Error Log
        	**type**\: str
        
        	**config**\: False
        
        .. attribute:: red_pair
        
        	Redundancy Pair
        	**type**\: list of  		 :py:class:`RedPair <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rmf_oper.Redundancy.Summary.RedPair>`
        
        	**config**\: False
        
        

        """

        _prefix = 'infra-rmf-oper'
        _revision = '2015-11-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
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
            self._perform_setattr(Redundancy.Summary, ['err_log'], name, value)


        class RedPair(_Entity_):
            """
            Redundancy Pair
            
            .. attribute:: active
            
            	Active node name R/S/I
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: standby
            
            	Standby node name R/S/I
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: ha_state
            
            	High Availability state Ready/Not Ready
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: nsr_state
            
            	NSR state Configured/Not Configured
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: groupinfo
            
            	groupinfo
            	**type**\: list of  		 :py:class:`Groupinfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rmf_oper.Redundancy.Summary.RedPair.Groupinfo>`
            
            	**config**\: False
            
            

            """

            _prefix = 'infra-rmf-oper'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
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
                self._perform_setattr(Redundancy.Summary.RedPair, ['active', 'standby', 'ha_state', 'nsr_state'], name, value)


            class Groupinfo(_Entity_):
                """
                groupinfo
                
                .. attribute:: active
                
                	Active
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: standby
                
                	Standby
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: ha_state
                
                	HAState
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: nsr_state
                
                	NSRState
                	**type**\: str
                
                	**config**\: False
                
                

                """

                _prefix = 'infra-rmf-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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
                    self._perform_setattr(Redundancy.Summary.RedPair.Groupinfo, ['active', 'standby', 'ha_state', 'nsr_state'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rmf_oper as meta
                    return meta._meta_table['Redundancy.Summary.RedPair.Groupinfo']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rmf_oper as meta
                return meta._meta_table['Redundancy.Summary.RedPair']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rmf_oper as meta
            return meta._meta_table['Redundancy.Summary']['meta_info']

    def clone_ptr(self):
        self._top_entity = Redundancy()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rmf_oper as meta
        return meta._meta_table['Redundancy']['meta_info']


