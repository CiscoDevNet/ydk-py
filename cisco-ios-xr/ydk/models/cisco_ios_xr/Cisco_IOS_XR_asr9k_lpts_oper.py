""" Cisco_IOS_XR_asr9k_lpts_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR asr9k\-lpts package operational data.

This module contains definitions
for the following management objects\:
  platform\-lptsp\-ifib\-static\: ASR9K platform ifib operational
    data
  platform\-lptsp\-ifib\: platform lptsp ifib
  platform\-lptsp\-ifib\-np\-stats\: platform lptsp ifib np stats

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




class PlatformLptspIfibStatic(_Entity_):
    """
    ASR9K platform ifib operational data 
    
    .. attribute:: node_statics
    
    	List of nodes with platform specific lpts operation data
    	**type**\:  :py:class:`NodeStatics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lpts_oper.PlatformLptspIfibStatic.NodeStatics>`
    
    	**config**\: False
    
    

    """

    _prefix = 'asr9k-lpts-oper'
    _revision = '2015-11-09'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(PlatformLptspIfibStatic, self).__init__()
        self._top_entity = None

        self.yang_name = "platform-lptsp-ifib-static"
        self.yang_parent_name = "Cisco-IOS-XR-asr9k-lpts-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("node-statics", ("node_statics", PlatformLptspIfibStatic.NodeStatics))])
        self._leafs = OrderedDict()

        self.node_statics = PlatformLptspIfibStatic.NodeStatics()
        self.node_statics.parent = self
        self._children_name_map["node_statics"] = "node-statics"
        self._segment_path = lambda: "Cisco-IOS-XR-asr9k-lpts-oper:platform-lptsp-ifib-static"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(PlatformLptspIfibStatic, [], name, value)


    class NodeStatics(_Entity_):
        """
        List of nodes with platform specific lpts
        operation data
        
        .. attribute:: node_static
        
        	Node with platform specific lpts data
        	**type**\: list of  		 :py:class:`NodeStatic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lpts_oper.PlatformLptspIfibStatic.NodeStatics.NodeStatic>`
        
        	**config**\: False
        
        

        """

        _prefix = 'asr9k-lpts-oper'
        _revision = '2015-11-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(PlatformLptspIfibStatic.NodeStatics, self).__init__()

            self.yang_name = "node-statics"
            self.yang_parent_name = "platform-lptsp-ifib-static"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("node-static", ("node_static", PlatformLptspIfibStatic.NodeStatics.NodeStatic))])
            self._leafs = OrderedDict()

            self.node_static = YList(self)
            self._segment_path = lambda: "node-statics"
            self._absolute_path = lambda: "Cisco-IOS-XR-asr9k-lpts-oper:platform-lptsp-ifib-static/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(PlatformLptspIfibStatic.NodeStatics, [], name, value)


        class NodeStatic(_Entity_):
            """
            Node with platform specific lpts data
            
            .. attribute:: node_name  (key)
            
            	Node name
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            	**config**\: False
            
            .. attribute:: police
            
            	pl\_pifib police data
            	**type**\:  :py:class:`Police <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lpts_oper.PlatformLptspIfibStatic.NodeStatics.NodeStatic.Police>`
            
            	**config**\: False
            
            .. attribute:: stats
            
            	pl\_pifib stats
            	**type**\:  :py:class:`Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lpts_oper.PlatformLptspIfibStatic.NodeStatics.NodeStatic.Stats>`
            
            	**config**\: False
            
            

            """

            _prefix = 'asr9k-lpts-oper'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(PlatformLptspIfibStatic.NodeStatics.NodeStatic, self).__init__()

                self.yang_name = "node-static"
                self.yang_parent_name = "node-statics"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_classes = OrderedDict([("police", ("police", PlatformLptspIfibStatic.NodeStatics.NodeStatic.Police)), ("stats", ("stats", PlatformLptspIfibStatic.NodeStatics.NodeStatic.Stats))])
                self._leafs = OrderedDict([
                    ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                ])
                self.node_name = None

                self.police = PlatformLptspIfibStatic.NodeStatics.NodeStatic.Police()
                self.police.parent = self
                self._children_name_map["police"] = "police"

                self.stats = PlatformLptspIfibStatic.NodeStatics.NodeStatic.Stats()
                self.stats.parent = self
                self._children_name_map["stats"] = "stats"
                self._segment_path = lambda: "node-static" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-asr9k-lpts-oper:platform-lptsp-ifib-static/node-statics/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PlatformLptspIfibStatic.NodeStatics.NodeStatic, ['node_name'], name, value)


            class Police(_Entity_):
                """
                pl\_pifib police data
                
                .. attribute:: static_info
                
                	Per punt reason info
                	**type**\: list of  		 :py:class:`StaticInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lpts_oper.PlatformLptspIfibStatic.NodeStatics.NodeStatic.Police.StaticInfo>`
                
                	**config**\: False
                
                

                """

                _prefix = 'asr9k-lpts-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(PlatformLptspIfibStatic.NodeStatics.NodeStatic.Police, self).__init__()

                    self.yang_name = "police"
                    self.yang_parent_name = "node-static"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("static-info", ("static_info", PlatformLptspIfibStatic.NodeStatics.NodeStatic.Police.StaticInfo))])
                    self._leafs = OrderedDict()

                    self.static_info = YList(self)
                    self._segment_path = lambda: "police"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PlatformLptspIfibStatic.NodeStatics.NodeStatic.Police, [], name, value)


                class StaticInfo(_Entity_):
                    """
                    Per punt reason info
                    
                    .. attribute:: punt_reason
                    
                    	punt reason
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: sid
                    
                    	sid
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: flow_rate
                    
                    	flow rate
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: burst_rate
                    
                    	burst rate
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: accepted
                    
                    	accepted
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: dropped
                    
                    	dropped
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: punt_reason_string
                    
                    	punt reason string
                    	**type**\: str
                    
                    	**length:** 0..50
                    
                    	**config**\: False
                    
                    .. attribute:: change_type
                    
                    	change type
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'asr9k-lpts-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(PlatformLptspIfibStatic.NodeStatics.NodeStatic.Police.StaticInfo, self).__init__()

                        self.yang_name = "static-info"
                        self.yang_parent_name = "police"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('punt_reason', (YLeaf(YType.uint32, 'punt-reason'), ['int'])),
                            ('sid', (YLeaf(YType.uint32, 'sid'), ['int'])),
                            ('flow_rate', (YLeaf(YType.uint32, 'flow-rate'), ['int'])),
                            ('burst_rate', (YLeaf(YType.uint32, 'burst-rate'), ['int'])),
                            ('accepted', (YLeaf(YType.uint64, 'accepted'), ['int'])),
                            ('dropped', (YLeaf(YType.uint64, 'dropped'), ['int'])),
                            ('punt_reason_string', (YLeaf(YType.str, 'punt-reason-string'), ['str'])),
                            ('change_type', (YLeaf(YType.uint8, 'change-type'), ['int'])),
                        ])
                        self.punt_reason = None
                        self.sid = None
                        self.flow_rate = None
                        self.burst_rate = None
                        self.accepted = None
                        self.dropped = None
                        self.punt_reason_string = None
                        self.change_type = None
                        self._segment_path = lambda: "static-info"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PlatformLptspIfibStatic.NodeStatics.NodeStatic.Police.StaticInfo, ['punt_reason', 'sid', 'flow_rate', 'burst_rate', 'accepted', 'dropped', 'punt_reason_string', 'change_type'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_lpts_oper as meta
                        return meta._meta_table['PlatformLptspIfibStatic.NodeStatics.NodeStatic.Police.StaticInfo']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_lpts_oper as meta
                    return meta._meta_table['PlatformLptspIfibStatic.NodeStatics.NodeStatic.Police']['meta_info']


            class Stats(_Entity_):
                """
                pl\_pifib stats
                
                .. attribute:: accepted
                
                	Deleted\-entry accepted packets counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: dropped
                
                	Deleted\-entry dropped packets counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: clear_ts
                
                	Statistics clear timestamp
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: no_stats_mem_err
                
                	No statistics memory error
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                

                """

                _prefix = 'asr9k-lpts-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(PlatformLptspIfibStatic.NodeStatics.NodeStatic.Stats, self).__init__()

                    self.yang_name = "stats"
                    self.yang_parent_name = "node-static"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('accepted', (YLeaf(YType.uint64, 'accepted'), ['int'])),
                        ('dropped', (YLeaf(YType.uint64, 'dropped'), ['int'])),
                        ('clear_ts', (YLeaf(YType.uint64, 'clear-ts'), ['int'])),
                        ('no_stats_mem_err', (YLeaf(YType.uint64, 'no-stats-mem-err'), ['int'])),
                    ])
                    self.accepted = None
                    self.dropped = None
                    self.clear_ts = None
                    self.no_stats_mem_err = None
                    self._segment_path = lambda: "stats"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PlatformLptspIfibStatic.NodeStatics.NodeStatic.Stats, ['accepted', 'dropped', 'clear_ts', 'no_stats_mem_err'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_lpts_oper as meta
                    return meta._meta_table['PlatformLptspIfibStatic.NodeStatics.NodeStatic.Stats']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_lpts_oper as meta
                return meta._meta_table['PlatformLptspIfibStatic.NodeStatics.NodeStatic']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_lpts_oper as meta
            return meta._meta_table['PlatformLptspIfibStatic.NodeStatics']['meta_info']

    def clone_ptr(self):
        self._top_entity = PlatformLptspIfibStatic()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_lpts_oper as meta
        return meta._meta_table['PlatformLptspIfibStatic']['meta_info']


class PlatformLptspIfib(_Entity_):
    """
    platform lptsp ifib
    
    .. attribute:: nodes
    
    	List of nodes with platform specific lpts operation data
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lpts_oper.PlatformLptspIfib.Nodes>`
    
    	**config**\: False
    
    

    """

    _prefix = 'asr9k-lpts-oper'
    _revision = '2015-11-09'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(PlatformLptspIfib, self).__init__()
        self._top_entity = None

        self.yang_name = "platform-lptsp-ifib"
        self.yang_parent_name = "Cisco-IOS-XR-asr9k-lpts-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("nodes", ("nodes", PlatformLptspIfib.Nodes))])
        self._leafs = OrderedDict()

        self.nodes = PlatformLptspIfib.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._segment_path = lambda: "Cisco-IOS-XR-asr9k-lpts-oper:platform-lptsp-ifib"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(PlatformLptspIfib, [], name, value)


    class Nodes(_Entity_):
        """
        List of nodes with platform specific lpts
        operation data
        
        .. attribute:: node
        
        	Node with platform specific lpts data
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lpts_oper.PlatformLptspIfib.Nodes.Node>`
        
        	**config**\: False
        
        

        """

        _prefix = 'asr9k-lpts-oper'
        _revision = '2015-11-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(PlatformLptspIfib.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "platform-lptsp-ifib"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("node", ("node", PlatformLptspIfib.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-asr9k-lpts-oper:platform-lptsp-ifib/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(PlatformLptspIfib.Nodes, [], name, value)


        class Node(_Entity_):
            """
            Node with platform specific lpts data
            
            .. attribute:: node_name  (key)
            
            	Node name
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            	**config**\: False
            
            .. attribute:: police
            
            	pl\_pifib police data
            	**type**\:  :py:class:`Police <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lpts_oper.PlatformLptspIfib.Nodes.Node.Police>`
            
            	**config**\: False
            
            .. attribute:: stats
            
            	pl\_pifib stats
            	**type**\:  :py:class:`Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lpts_oper.PlatformLptspIfib.Nodes.Node.Stats>`
            
            	**config**\: False
            
            

            """

            _prefix = 'asr9k-lpts-oper'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(PlatformLptspIfib.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_classes = OrderedDict([("police", ("police", PlatformLptspIfib.Nodes.Node.Police)), ("stats", ("stats", PlatformLptspIfib.Nodes.Node.Stats))])
                self._leafs = OrderedDict([
                    ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                ])
                self.node_name = None

                self.police = PlatformLptspIfib.Nodes.Node.Police()
                self.police.parent = self
                self._children_name_map["police"] = "police"

                self.stats = PlatformLptspIfib.Nodes.Node.Stats()
                self.stats.parent = self
                self._children_name_map["stats"] = "stats"
                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-asr9k-lpts-oper:platform-lptsp-ifib/nodes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PlatformLptspIfib.Nodes.Node, ['node_name'], name, value)


            class Police(_Entity_):
                """
                pl\_pifib police data
                
                .. attribute:: police_info
                
                	Per flow type police info
                	**type**\: list of  		 :py:class:`PoliceInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lpts_oper.PlatformLptspIfib.Nodes.Node.Police.PoliceInfo>`
                
                	**config**\: False
                
                

                """

                _prefix = 'asr9k-lpts-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(PlatformLptspIfib.Nodes.Node.Police, self).__init__()

                    self.yang_name = "police"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("police-info", ("police_info", PlatformLptspIfib.Nodes.Node.Police.PoliceInfo))])
                    self._leafs = OrderedDict()

                    self.police_info = YList(self)
                    self._segment_path = lambda: "police"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PlatformLptspIfib.Nodes.Node.Police, [], name, value)


                class PoliceInfo(_Entity_):
                    """
                    Per flow type police info
                    
                    .. attribute:: avgrate
                    
                    	avgrate
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: burst
                    
                    	burst
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: static_avgrate
                    
                    	static avgrate
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: avgrate_type
                    
                    	avgrate type
                    	**type**\: str
                    
                    	**length:** 0..50
                    
                    	**config**\: False
                    
                    .. attribute:: flow_type
                    
                    	flow type
                    	**type**\: str
                    
                    	**length:** 0..50
                    
                    	**config**\: False
                    
                    .. attribute:: accepted_stats
                    
                    	accepted stats
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: dropped_stats
                    
                    	dropped stats
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: policer
                    
                    	policer
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: str_iptos_val
                    
                    	str iptos val
                    	**type**\: str
                    
                    	**length:** 0..8
                    
                    	**config**\: False
                    
                    .. attribute:: change_type
                    
                    	change type
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: acl_config
                    
                    	acl config
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: acl_str
                    
                    	acl str
                    	**type**\: str
                    
                    	**length:** 0..50
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'asr9k-lpts-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(PlatformLptspIfib.Nodes.Node.Police.PoliceInfo, self).__init__()

                        self.yang_name = "police-info"
                        self.yang_parent_name = "police"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('avgrate', (YLeaf(YType.uint32, 'avgrate'), ['int'])),
                            ('burst', (YLeaf(YType.uint32, 'burst'), ['int'])),
                            ('static_avgrate', (YLeaf(YType.uint32, 'static-avgrate'), ['int'])),
                            ('avgrate_type', (YLeaf(YType.str, 'avgrate-type'), ['str'])),
                            ('flow_type', (YLeaf(YType.str, 'flow-type'), ['str'])),
                            ('accepted_stats', (YLeaf(YType.uint64, 'accepted-stats'), ['int'])),
                            ('dropped_stats', (YLeaf(YType.uint64, 'dropped-stats'), ['int'])),
                            ('policer', (YLeaf(YType.uint32, 'policer'), ['int'])),
                            ('str_iptos_val', (YLeaf(YType.str, 'str-iptos-val'), ['str'])),
                            ('change_type', (YLeaf(YType.uint8, 'change-type'), ['int'])),
                            ('acl_config', (YLeaf(YType.uint8, 'acl-config'), ['int'])),
                            ('acl_str', (YLeaf(YType.str, 'acl-str'), ['str'])),
                        ])
                        self.avgrate = None
                        self.burst = None
                        self.static_avgrate = None
                        self.avgrate_type = None
                        self.flow_type = None
                        self.accepted_stats = None
                        self.dropped_stats = None
                        self.policer = None
                        self.str_iptos_val = None
                        self.change_type = None
                        self.acl_config = None
                        self.acl_str = None
                        self._segment_path = lambda: "police-info"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PlatformLptspIfib.Nodes.Node.Police.PoliceInfo, ['avgrate', 'burst', 'static_avgrate', 'avgrate_type', 'flow_type', 'accepted_stats', 'dropped_stats', 'policer', 'str_iptos_val', 'change_type', 'acl_config', 'acl_str'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_lpts_oper as meta
                        return meta._meta_table['PlatformLptspIfib.Nodes.Node.Police.PoliceInfo']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_lpts_oper as meta
                    return meta._meta_table['PlatformLptspIfib.Nodes.Node.Police']['meta_info']


            class Stats(_Entity_):
                """
                pl\_pifib stats
                
                .. attribute:: accepted
                
                	Deleted\-entry accepted packets counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: dropped
                
                	Deleted\-entry dropped packets counter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: clear_ts
                
                	Statistics clear timestamp
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: no_stats_mem_err
                
                	No statistics memory error
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                

                """

                _prefix = 'asr9k-lpts-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(PlatformLptspIfib.Nodes.Node.Stats, self).__init__()

                    self.yang_name = "stats"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('accepted', (YLeaf(YType.uint64, 'accepted'), ['int'])),
                        ('dropped', (YLeaf(YType.uint64, 'dropped'), ['int'])),
                        ('clear_ts', (YLeaf(YType.uint64, 'clear-ts'), ['int'])),
                        ('no_stats_mem_err', (YLeaf(YType.uint64, 'no-stats-mem-err'), ['int'])),
                    ])
                    self.accepted = None
                    self.dropped = None
                    self.clear_ts = None
                    self.no_stats_mem_err = None
                    self._segment_path = lambda: "stats"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PlatformLptspIfib.Nodes.Node.Stats, ['accepted', 'dropped', 'clear_ts', 'no_stats_mem_err'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_lpts_oper as meta
                    return meta._meta_table['PlatformLptspIfib.Nodes.Node.Stats']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_lpts_oper as meta
                return meta._meta_table['PlatformLptspIfib.Nodes.Node']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_lpts_oper as meta
            return meta._meta_table['PlatformLptspIfib.Nodes']['meta_info']

    def clone_ptr(self):
        self._top_entity = PlatformLptspIfib()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_lpts_oper as meta
        return meta._meta_table['PlatformLptspIfib']['meta_info']


class PlatformLptspIfibNpStats(_Entity_):
    """
    platform lptsp ifib np stats
    
    .. attribute:: node_np_stats
    
    	List of nodes with platform specific lpts operation data
    	**type**\:  :py:class:`NodeNpStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lpts_oper.PlatformLptspIfibNpStats.NodeNpStats>`
    
    	**config**\: False
    
    

    """

    _prefix = 'asr9k-lpts-oper'
    _revision = '2015-11-09'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(PlatformLptspIfibNpStats, self).__init__()
        self._top_entity = None

        self.yang_name = "platform-lptsp-ifib-np-stats"
        self.yang_parent_name = "Cisco-IOS-XR-asr9k-lpts-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("node-np-stats", ("node_np_stats", PlatformLptspIfibNpStats.NodeNpStats))])
        self._leafs = OrderedDict()

        self.node_np_stats = PlatformLptspIfibNpStats.NodeNpStats()
        self.node_np_stats.parent = self
        self._children_name_map["node_np_stats"] = "node-np-stats"
        self._segment_path = lambda: "Cisco-IOS-XR-asr9k-lpts-oper:platform-lptsp-ifib-np-stats"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(PlatformLptspIfibNpStats, [], name, value)


    class NodeNpStats(_Entity_):
        """
        List of nodes with platform specific lpts
        operation data
        
        .. attribute:: node_np_stat
        
        	Node with platform specific lpts data
        	**type**\: list of  		 :py:class:`NodeNpStat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lpts_oper.PlatformLptspIfibNpStats.NodeNpStats.NodeNpStat>`
        
        	**config**\: False
        
        

        """

        _prefix = 'asr9k-lpts-oper'
        _revision = '2015-11-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(PlatformLptspIfibNpStats.NodeNpStats, self).__init__()

            self.yang_name = "node-np-stats"
            self.yang_parent_name = "platform-lptsp-ifib-np-stats"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("node-np-stat", ("node_np_stat", PlatformLptspIfibNpStats.NodeNpStats.NodeNpStat))])
            self._leafs = OrderedDict()

            self.node_np_stat = YList(self)
            self._segment_path = lambda: "node-np-stats"
            self._absolute_path = lambda: "Cisco-IOS-XR-asr9k-lpts-oper:platform-lptsp-ifib-np-stats/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(PlatformLptspIfibNpStats.NodeNpStats, [], name, value)


        class NodeNpStat(_Entity_):
            """
            Node with platform specific lpts data
            
            .. attribute:: node_name  (key)
            
            	Node name
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            	**config**\: False
            
            .. attribute:: nps
            
            	List of all NP
            	**type**\:  :py:class:`Nps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lpts_oper.PlatformLptspIfibNpStats.NodeNpStats.NodeNpStat.Nps>`
            
            	**config**\: False
            
            

            """

            _prefix = 'asr9k-lpts-oper'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(PlatformLptspIfibNpStats.NodeNpStats.NodeNpStat, self).__init__()

                self.yang_name = "node-np-stat"
                self.yang_parent_name = "node-np-stats"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_classes = OrderedDict([("nps", ("nps", PlatformLptspIfibNpStats.NodeNpStats.NodeNpStat.Nps))])
                self._leafs = OrderedDict([
                    ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                ])
                self.node_name = None

                self.nps = PlatformLptspIfibNpStats.NodeNpStats.NodeNpStat.Nps()
                self.nps.parent = self
                self._children_name_map["nps"] = "nps"
                self._segment_path = lambda: "node-np-stat" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-asr9k-lpts-oper:platform-lptsp-ifib-np-stats/node-np-stats/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PlatformLptspIfibNpStats.NodeNpStats.NodeNpStat, ['node_name'], name, value)


            class Nps(_Entity_):
                """
                List of all NP
                
                .. attribute:: np
                
                	np0 to np7
                	**type**\: list of  		 :py:class:`Np <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lpts_oper.PlatformLptspIfibNpStats.NodeNpStats.NodeNpStat.Nps.Np>`
                
                	**config**\: False
                
                

                """

                _prefix = 'asr9k-lpts-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(PlatformLptspIfibNpStats.NodeNpStats.NodeNpStat.Nps, self).__init__()

                    self.yang_name = "nps"
                    self.yang_parent_name = "node-np-stat"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("np", ("np", PlatformLptspIfibNpStats.NodeNpStats.NodeNpStat.Nps.Np))])
                    self._leafs = OrderedDict()

                    self.np = YList(self)
                    self._segment_path = lambda: "nps"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PlatformLptspIfibNpStats.NodeNpStats.NodeNpStat.Nps, [], name, value)


                class Np(_Entity_):
                    """
                    np0 to np7
                    
                    .. attribute:: np_name  (key)
                    
                    	NP name
                    	**type**\: str
                    
                    	**pattern:** (np0)\|(np1)\|(np2)\|(np3)\|(np4)\|(np5)\|(np6)\|(np7)
                    
                    	**config**\: False
                    
                    .. attribute:: np_police
                    
                    	pl\_pifib police data
                    	**type**\:  :py:class:`NpPolice <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lpts_oper.PlatformLptspIfibNpStats.NodeNpStats.NodeNpStat.Nps.Np.NpPolice>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'asr9k-lpts-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(PlatformLptspIfibNpStats.NodeNpStats.NodeNpStat.Nps.Np, self).__init__()

                        self.yang_name = "np"
                        self.yang_parent_name = "nps"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['np_name']
                        self._child_classes = OrderedDict([("np-police", ("np_police", PlatformLptspIfibNpStats.NodeNpStats.NodeNpStat.Nps.Np.NpPolice))])
                        self._leafs = OrderedDict([
                            ('np_name', (YLeaf(YType.str, 'np-name'), ['str'])),
                        ])
                        self.np_name = None

                        self.np_police = PlatformLptspIfibNpStats.NodeNpStats.NodeNpStat.Nps.Np.NpPolice()
                        self.np_police.parent = self
                        self._children_name_map["np_police"] = "np-police"
                        self._segment_path = lambda: "np" + "[np-name='" + str(self.np_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PlatformLptspIfibNpStats.NodeNpStats.NodeNpStat.Nps.Np, ['np_name'], name, value)


                    class NpPolice(_Entity_):
                        """
                        pl\_pifib police data
                        
                        .. attribute:: police_info
                        
                        	Per flow type police info
                        	**type**\: list of  		 :py:class:`PoliceInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lpts_oper.PlatformLptspIfibNpStats.NodeNpStats.NodeNpStat.Nps.Np.NpPolice.PoliceInfo>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'asr9k-lpts-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(PlatformLptspIfibNpStats.NodeNpStats.NodeNpStat.Nps.Np.NpPolice, self).__init__()

                            self.yang_name = "np-police"
                            self.yang_parent_name = "np"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("police-info", ("police_info", PlatformLptspIfibNpStats.NodeNpStats.NodeNpStat.Nps.Np.NpPolice.PoliceInfo))])
                            self._leafs = OrderedDict()

                            self.police_info = YList(self)
                            self._segment_path = lambda: "np-police"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PlatformLptspIfibNpStats.NodeNpStats.NodeNpStat.Nps.Np.NpPolice, [], name, value)


                        class PoliceInfo(_Entity_):
                            """
                            Per flow type police info
                            
                            .. attribute:: avgrate
                            
                            	avgrate
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: burst
                            
                            	burst
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: static_avgrate
                            
                            	static avgrate
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: avgrate_type
                            
                            	avgrate type
                            	**type**\: str
                            
                            	**length:** 0..50
                            
                            	**config**\: False
                            
                            .. attribute:: flow_type
                            
                            	flow type
                            	**type**\: str
                            
                            	**length:** 0..50
                            
                            	**config**\: False
                            
                            .. attribute:: accepted_stats
                            
                            	accepted stats
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: dropped_stats
                            
                            	dropped stats
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: policer
                            
                            	policer
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: str_iptos_val
                            
                            	str iptos val
                            	**type**\: str
                            
                            	**length:** 0..8
                            
                            	**config**\: False
                            
                            .. attribute:: change_type
                            
                            	change type
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            .. attribute:: acl_config
                            
                            	acl config
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            .. attribute:: acl_str
                            
                            	acl str
                            	**type**\: str
                            
                            	**length:** 0..50
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'asr9k-lpts-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(PlatformLptspIfibNpStats.NodeNpStats.NodeNpStat.Nps.Np.NpPolice.PoliceInfo, self).__init__()

                                self.yang_name = "police-info"
                                self.yang_parent_name = "np-police"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('avgrate', (YLeaf(YType.uint32, 'avgrate'), ['int'])),
                                    ('burst', (YLeaf(YType.uint32, 'burst'), ['int'])),
                                    ('static_avgrate', (YLeaf(YType.uint32, 'static-avgrate'), ['int'])),
                                    ('avgrate_type', (YLeaf(YType.str, 'avgrate-type'), ['str'])),
                                    ('flow_type', (YLeaf(YType.str, 'flow-type'), ['str'])),
                                    ('accepted_stats', (YLeaf(YType.uint64, 'accepted-stats'), ['int'])),
                                    ('dropped_stats', (YLeaf(YType.uint64, 'dropped-stats'), ['int'])),
                                    ('policer', (YLeaf(YType.uint32, 'policer'), ['int'])),
                                    ('str_iptos_val', (YLeaf(YType.str, 'str-iptos-val'), ['str'])),
                                    ('change_type', (YLeaf(YType.uint8, 'change-type'), ['int'])),
                                    ('acl_config', (YLeaf(YType.uint8, 'acl-config'), ['int'])),
                                    ('acl_str', (YLeaf(YType.str, 'acl-str'), ['str'])),
                                ])
                                self.avgrate = None
                                self.burst = None
                                self.static_avgrate = None
                                self.avgrate_type = None
                                self.flow_type = None
                                self.accepted_stats = None
                                self.dropped_stats = None
                                self.policer = None
                                self.str_iptos_val = None
                                self.change_type = None
                                self.acl_config = None
                                self.acl_str = None
                                self._segment_path = lambda: "police-info"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PlatformLptspIfibNpStats.NodeNpStats.NodeNpStat.Nps.Np.NpPolice.PoliceInfo, ['avgrate', 'burst', 'static_avgrate', 'avgrate_type', 'flow_type', 'accepted_stats', 'dropped_stats', 'policer', 'str_iptos_val', 'change_type', 'acl_config', 'acl_str'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_lpts_oper as meta
                                return meta._meta_table['PlatformLptspIfibNpStats.NodeNpStats.NodeNpStat.Nps.Np.NpPolice.PoliceInfo']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_lpts_oper as meta
                            return meta._meta_table['PlatformLptspIfibNpStats.NodeNpStats.NodeNpStat.Nps.Np.NpPolice']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_lpts_oper as meta
                        return meta._meta_table['PlatformLptspIfibNpStats.NodeNpStats.NodeNpStat.Nps.Np']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_lpts_oper as meta
                    return meta._meta_table['PlatformLptspIfibNpStats.NodeNpStats.NodeNpStat.Nps']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_lpts_oper as meta
                return meta._meta_table['PlatformLptspIfibNpStats.NodeNpStats.NodeNpStat']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_lpts_oper as meta
            return meta._meta_table['PlatformLptspIfibNpStats.NodeNpStats']['meta_info']

    def clone_ptr(self):
        self._top_entity = PlatformLptspIfibNpStats()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_lpts_oper as meta
        return meta._meta_table['PlatformLptspIfibNpStats']['meta_info']


