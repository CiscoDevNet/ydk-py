""" Cisco_IOS_XR_pbr_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR pbr package operational data.

This module contains definitions
for the following management objects\:
  pbr\: PBR operational data

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



class PolicyState(Enum):
    """
    PolicyState (Enum Class)

    Different Interface states

    .. data:: active = 0

    	active

    .. data:: suspended = 1

    	suspended

    """

    active = Enum.YLeaf(0, "active")

    suspended = Enum.YLeaf(1, "suspended")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_oper as meta
        return meta._meta_table['PolicyState']



class Pbr(_Entity_):
    """
    PBR operational data
    
    .. attribute:: nodes
    
    	Node\-specific PBR operational data
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper.Pbr.Nodes>`
    
    	**config**\: False
    
    

    """

    _prefix = 'pbr-oper'
    _revision = '2015-11-09'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(Pbr, self).__init__()
        self._top_entity = None

        self.yang_name = "pbr"
        self.yang_parent_name = "Cisco-IOS-XR-pbr-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("nodes", ("nodes", Pbr.Nodes))])
        self._leafs = OrderedDict()

        self.nodes = Pbr.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._segment_path = lambda: "Cisco-IOS-XR-pbr-oper:pbr"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Pbr, [], name, value)


    class Nodes(_Entity_):
        """
        Node\-specific PBR operational data
        
        .. attribute:: node
        
        	PBR operational data for a particular node
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper.Pbr.Nodes.Node>`
        
        	**config**\: False
        
        

        """

        _prefix = 'pbr-oper'
        _revision = '2015-11-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Pbr.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "pbr"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("node", ("node", Pbr.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-pbr-oper:pbr/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Pbr.Nodes, [], name, value)


        class Node(_Entity_):
            """
            PBR operational data for a particular node
            
            .. attribute:: node_name  (key)
            
            	The node
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            	**config**\: False
            
            .. attribute:: policy_map
            
            	Operational data for policymaps
            	**type**\:  :py:class:`PolicyMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper.Pbr.Nodes.Node.PolicyMap>`
            
            	**config**\: False
            
            

            """

            _prefix = 'pbr-oper'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Pbr.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_classes = OrderedDict([("policy-map", ("policy_map", Pbr.Nodes.Node.PolicyMap))])
                self._leafs = OrderedDict([
                    ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                ])
                self.node_name = None

                self.policy_map = Pbr.Nodes.Node.PolicyMap()
                self.policy_map.parent = self
                self._children_name_map["policy_map"] = "policy-map"
                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-pbr-oper:pbr/nodes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Pbr.Nodes.Node, ['node_name'], name, value)


            class PolicyMap(_Entity_):
                """
                Operational data for policymaps
                
                .. attribute:: interfaces
                
                	Operational data for all interfaces
                	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper.Pbr.Nodes.Node.PolicyMap.Interfaces>`
                
                	**config**\: False
                
                

                """

                _prefix = 'pbr-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Pbr.Nodes.Node.PolicyMap, self).__init__()

                    self.yang_name = "policy-map"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("interfaces", ("interfaces", Pbr.Nodes.Node.PolicyMap.Interfaces))])
                    self._leafs = OrderedDict()

                    self.interfaces = Pbr.Nodes.Node.PolicyMap.Interfaces()
                    self.interfaces.parent = self
                    self._children_name_map["interfaces"] = "interfaces"
                    self._segment_path = lambda: "policy-map"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Pbr.Nodes.Node.PolicyMap, [], name, value)


                class Interfaces(_Entity_):
                    """
                    Operational data for all interfaces
                    
                    .. attribute:: interface
                    
                    	PBR action data for a particular interface
                    	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper.Pbr.Nodes.Node.PolicyMap.Interfaces.Interface>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'pbr-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Pbr.Nodes.Node.PolicyMap.Interfaces, self).__init__()

                        self.yang_name = "interfaces"
                        self.yang_parent_name = "policy-map"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("interface", ("interface", Pbr.Nodes.Node.PolicyMap.Interfaces.Interface))])
                        self._leafs = OrderedDict()

                        self.interface = YList(self)
                        self._segment_path = lambda: "interfaces"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pbr.Nodes.Node.PolicyMap.Interfaces, [], name, value)


                    class Interface(_Entity_):
                        """
                        PBR action data for a particular interface
                        
                        .. attribute:: interface_name  (key)
                        
                        	Name of the interface
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        	**config**\: False
                        
                        .. attribute:: direction
                        
                        	PBR direction
                        	**type**\:  :py:class:`Direction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper.Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'pbr-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Pbr.Nodes.Node.PolicyMap.Interfaces.Interface, self).__init__()

                            self.yang_name = "interface"
                            self.yang_parent_name = "interfaces"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['interface_name']
                            self._child_classes = OrderedDict([("direction", ("direction", Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction))])
                            self._leafs = OrderedDict([
                                ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                            ])
                            self.interface_name = None

                            self.direction = Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction()
                            self.direction.parent = self
                            self._children_name_map["direction"] = "direction"
                            self._segment_path = lambda: "interface" + "[interface-name='" + str(self.interface_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pbr.Nodes.Node.PolicyMap.Interfaces.Interface, ['interface_name'], name, value)


                        class Direction(_Entity_):
                            """
                            PBR direction
                            
                            .. attribute:: input
                            
                            	PBR policy statistics
                            	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper.Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'pbr-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction, self).__init__()

                                self.yang_name = "direction"
                                self.yang_parent_name = "interface"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("input", ("input", Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input))])
                                self._leafs = OrderedDict()

                                self.input = Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input()
                                self.input.parent = self
                                self._children_name_map["input"] = "input"
                                self._segment_path = lambda: "direction"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction, [], name, value)


                            class Input(_Entity_):
                                """
                                PBR policy statistics
                                
                                .. attribute:: node_name
                                
                                	NodeName
                                	**type**\: str
                                
                                	**length:** 0..42
                                
                                	**config**\: False
                                
                                .. attribute:: policy_name
                                
                                	PolicyName
                                	**type**\: str
                                
                                	**length:** 0..65
                                
                                	**config**\: False
                                
                                .. attribute:: state
                                
                                	State
                                	**type**\:  :py:class:`PolicyState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper.PolicyState>`
                                
                                	**config**\: False
                                
                                .. attribute:: state_description
                                
                                	StateDescription
                                	**type**\: str
                                
                                	**length:** 0..128
                                
                                	**config**\: False
                                
                                .. attribute:: class_stat
                                
                                	Array of classes contained in policy
                                	**type**\: list of  		 :py:class:`ClassStat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper.Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'pbr-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input, self).__init__()

                                    self.yang_name = "input"
                                    self.yang_parent_name = "direction"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("class-stat", ("class_stat", Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat))])
                                    self._leafs = OrderedDict([
                                        ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                                        ('policy_name', (YLeaf(YType.str, 'policy-name'), ['str'])),
                                        ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper', 'PolicyState', '')])),
                                        ('state_description', (YLeaf(YType.str, 'state-description'), ['str'])),
                                    ])
                                    self.node_name = None
                                    self.policy_name = None
                                    self.state = None
                                    self.state_description = None

                                    self.class_stat = YList(self)
                                    self._segment_path = lambda: "input"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input, ['node_name', 'policy_name', 'state', 'state_description'], name, value)


                                class ClassStat(_Entity_):
                                    """
                                    Array of classes contained in policy
                                    
                                    .. attribute:: general_stats
                                    
                                    	general stats
                                    	**type**\:  :py:class:`GeneralStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper.Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat.GeneralStats>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: httpr_stats
                                    
                                    	HTTPR stats
                                    	**type**\:  :py:class:`HttprStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper.Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat.HttprStats>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: http_enrich_stats
                                    
                                    	HTTP Enrichment stats
                                    	**type**\:  :py:class:`HttpEnrichStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper.Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat.HttpEnrichStats>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: counter_validity_bitmask
                                    
                                    	 Bitmask to indicate which counter or counters are undetermined. Counters will be marked undetermined when one or more classes share queues with class\-default because in such cases the value of counters for each class is invalid. Based on the flag(s) set, the following counters will be marked undetermined. For example, if value of this object returned is 0x00000101, counters TransmitPackets/TransmitBytes/TotalTransmitRate and DropPackets/DropBytes are undetermined .0x00000001 \- Transmit (TransmitPackets/TransmitBytes/TotalTransmitRate ), 0x00000002 \- Drop (TotalDropPackets/TotalDropBytes/TotalDropRate), 0x00000004 \- Httpr (HttprTransmitPackets/HttprTransmitBytes), 0x00000020 \- HttpErich (HttpErichTransmitPackets /HttpEnrichTransmitBytes), 
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: class_name
                                    
                                    	ClassName
                                    	**type**\: str
                                    
                                    	**length:** 0..65
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: class_id
                                    
                                    	ClassId
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'pbr-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat, self).__init__()

                                        self.yang_name = "class-stat"
                                        self.yang_parent_name = "input"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("general-stats", ("general_stats", Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat.GeneralStats)), ("httpr-stats", ("httpr_stats", Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat.HttprStats)), ("http-enrich-stats", ("http_enrich_stats", Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat.HttpEnrichStats))])
                                        self._leafs = OrderedDict([
                                            ('counter_validity_bitmask', (YLeaf(YType.uint64, 'counter-validity-bitmask'), ['int'])),
                                            ('class_name', (YLeaf(YType.str, 'class-name'), ['str'])),
                                            ('class_id', (YLeaf(YType.uint32, 'class-id'), ['int'])),
                                        ])
                                        self.counter_validity_bitmask = None
                                        self.class_name = None
                                        self.class_id = None

                                        self.general_stats = Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat.GeneralStats()
                                        self.general_stats.parent = self
                                        self._children_name_map["general_stats"] = "general-stats"

                                        self.httpr_stats = Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat.HttprStats()
                                        self.httpr_stats.parent = self
                                        self._children_name_map["httpr_stats"] = "httpr-stats"

                                        self.http_enrich_stats = Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat.HttpEnrichStats()
                                        self.http_enrich_stats.parent = self
                                        self._children_name_map["http_enrich_stats"] = "http-enrich-stats"
                                        self._segment_path = lambda: "class-stat"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat, ['counter_validity_bitmask', 'class_name', 'class_id'], name, value)


                                    class GeneralStats(_Entity_):
                                        """
                                        general stats
                                        
                                        .. attribute:: transmit_packets
                                        
                                        	Transmitted packets (packets/bytes)
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**config**\: False
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: transmit_bytes
                                        
                                        	Transmitted bytes (packets/bytes)
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**config**\: False
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: total_drop_packets
                                        
                                        	Dropped packets (packets/bytes)
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**config**\: False
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: total_drop_bytes
                                        
                                        	Dropped bytes (packets/bytes)
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**config**\: False
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: total_drop_rate
                                        
                                        	Total drop rate (packets/bytes)
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: match_data_rate
                                        
                                        	Incoming matched data rate in kbps
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        	**units**\: kbit/s
                                        
                                        .. attribute:: total_transmit_rate
                                        
                                        	Total transmit rate in kbps
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        	**units**\: kbit/s
                                        
                                        .. attribute:: pre_policy_matched_packets
                                        
                                        	Matched pkts before applying policy
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: pre_policy_matched_bytes
                                        
                                        	Matched bytes before applying policy
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**config**\: False
                                        
                                        	**units**\: byte
                                        
                                        

                                        """

                                        _prefix = 'pbr-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat.GeneralStats, self).__init__()

                                            self.yang_name = "general-stats"
                                            self.yang_parent_name = "class-stat"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('transmit_packets', (YLeaf(YType.uint64, 'transmit-packets'), ['int'])),
                                                ('transmit_bytes', (YLeaf(YType.uint64, 'transmit-bytes'), ['int'])),
                                                ('total_drop_packets', (YLeaf(YType.uint64, 'total-drop-packets'), ['int'])),
                                                ('total_drop_bytes', (YLeaf(YType.uint64, 'total-drop-bytes'), ['int'])),
                                                ('total_drop_rate', (YLeaf(YType.uint32, 'total-drop-rate'), ['int'])),
                                                ('match_data_rate', (YLeaf(YType.uint32, 'match-data-rate'), ['int'])),
                                                ('total_transmit_rate', (YLeaf(YType.uint32, 'total-transmit-rate'), ['int'])),
                                                ('pre_policy_matched_packets', (YLeaf(YType.uint64, 'pre-policy-matched-packets'), ['int'])),
                                                ('pre_policy_matched_bytes', (YLeaf(YType.uint64, 'pre-policy-matched-bytes'), ['int'])),
                                            ])
                                            self.transmit_packets = None
                                            self.transmit_bytes = None
                                            self.total_drop_packets = None
                                            self.total_drop_bytes = None
                                            self.total_drop_rate = None
                                            self.match_data_rate = None
                                            self.total_transmit_rate = None
                                            self.pre_policy_matched_packets = None
                                            self.pre_policy_matched_bytes = None
                                            self._segment_path = lambda: "general-stats"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat.GeneralStats, ['transmit_packets', 'transmit_bytes', 'total_drop_packets', 'total_drop_bytes', 'total_drop_rate', 'match_data_rate', 'total_transmit_rate', 'pre_policy_matched_packets', 'pre_policy_matched_bytes'], name, value)

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_oper as meta
                                            return meta._meta_table['Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat.GeneralStats']['meta_info']


                                    class HttprStats(_Entity_):
                                        """
                                        HTTPR stats
                                        
                                        .. attribute:: rqst_rcvd_packets
                                        
                                        	TotalNum of pkts HTTP request received
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: rqst_rcvd_bytes
                                        
                                        	TotalNum of Bytes HTTP request received
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**config**\: False
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: drop_packets
                                        
                                        	Dropped  packets
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: drop_bytes
                                        
                                        	Dropped bytes
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**config**\: False
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: resp_sent_packets
                                        
                                        	TotalNum of pkts HTTPR response sent
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: resp_sent_bytes
                                        
                                        	TotalNum of Bytes HTTPR response sent
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**config**\: False
                                        
                                        	**units**\: byte
                                        
                                        

                                        """

                                        _prefix = 'pbr-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat.HttprStats, self).__init__()

                                            self.yang_name = "httpr-stats"
                                            self.yang_parent_name = "class-stat"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('rqst_rcvd_packets', (YLeaf(YType.uint64, 'rqst-rcvd-packets'), ['int'])),
                                                ('rqst_rcvd_bytes', (YLeaf(YType.uint64, 'rqst-rcvd-bytes'), ['int'])),
                                                ('drop_packets', (YLeaf(YType.uint64, 'drop-packets'), ['int'])),
                                                ('drop_bytes', (YLeaf(YType.uint64, 'drop-bytes'), ['int'])),
                                                ('resp_sent_packets', (YLeaf(YType.uint64, 'resp-sent-packets'), ['int'])),
                                                ('resp_sent_bytes', (YLeaf(YType.uint64, 'resp-sent-bytes'), ['int'])),
                                            ])
                                            self.rqst_rcvd_packets = None
                                            self.rqst_rcvd_bytes = None
                                            self.drop_packets = None
                                            self.drop_bytes = None
                                            self.resp_sent_packets = None
                                            self.resp_sent_bytes = None
                                            self._segment_path = lambda: "httpr-stats"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat.HttprStats, ['rqst_rcvd_packets', 'rqst_rcvd_bytes', 'drop_packets', 'drop_bytes', 'resp_sent_packets', 'resp_sent_bytes'], name, value)

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_oper as meta
                                            return meta._meta_table['Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat.HttprStats']['meta_info']


                                    class HttpEnrichStats(_Entity_):
                                        """
                                        HTTP Enrichment stats
                                        
                                        .. attribute:: rqst_rcvd_packets
                                        
                                        	TotalNum of pkts HTTP request received
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: rqst_rcvd_bytes
                                        
                                        	TotalNum of Bytes HTTP request received
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**config**\: False
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: drop_packets
                                        
                                        	Dropped  packets
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: drop_bytes
                                        
                                        	Dropped bytes
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**config**\: False
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: resp_sent_packets
                                        
                                        	TotalNum of pkts HTTP Enrichment response sent
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: resp_sent_bytes
                                        
                                        	TotalNum of Bytes HTTP Enrichment response sent
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**config**\: False
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: req_sent_packets
                                        
                                        	TotalNum of pkts HTTP Enrichment request sent
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: tcp_sent_packets
                                        
                                        	TotalNum of pkts HTTP Enrichment TCP packet sent
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'pbr-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat.HttpEnrichStats, self).__init__()

                                            self.yang_name = "http-enrich-stats"
                                            self.yang_parent_name = "class-stat"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('rqst_rcvd_packets', (YLeaf(YType.uint64, 'rqst-rcvd-packets'), ['int'])),
                                                ('rqst_rcvd_bytes', (YLeaf(YType.uint64, 'rqst-rcvd-bytes'), ['int'])),
                                                ('drop_packets', (YLeaf(YType.uint64, 'drop-packets'), ['int'])),
                                                ('drop_bytes', (YLeaf(YType.uint64, 'drop-bytes'), ['int'])),
                                                ('resp_sent_packets', (YLeaf(YType.uint64, 'resp-sent-packets'), ['int'])),
                                                ('resp_sent_bytes', (YLeaf(YType.uint64, 'resp-sent-bytes'), ['int'])),
                                                ('req_sent_packets', (YLeaf(YType.uint64, 'req-sent-packets'), ['int'])),
                                                ('tcp_sent_packets', (YLeaf(YType.uint64, 'tcp-sent-packets'), ['int'])),
                                            ])
                                            self.rqst_rcvd_packets = None
                                            self.rqst_rcvd_bytes = None
                                            self.drop_packets = None
                                            self.drop_bytes = None
                                            self.resp_sent_packets = None
                                            self.resp_sent_bytes = None
                                            self.req_sent_packets = None
                                            self.tcp_sent_packets = None
                                            self._segment_path = lambda: "http-enrich-stats"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat.HttpEnrichStats, ['rqst_rcvd_packets', 'rqst_rcvd_bytes', 'drop_packets', 'drop_bytes', 'resp_sent_packets', 'resp_sent_bytes', 'req_sent_packets', 'tcp_sent_packets'], name, value)

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_oper as meta
                                            return meta._meta_table['Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat.HttpEnrichStats']['meta_info']

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_oper as meta
                                        return meta._meta_table['Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_oper as meta
                                    return meta._meta_table['Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_oper as meta
                                return meta._meta_table['Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_oper as meta
                            return meta._meta_table['Pbr.Nodes.Node.PolicyMap.Interfaces.Interface']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_oper as meta
                        return meta._meta_table['Pbr.Nodes.Node.PolicyMap.Interfaces']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_oper as meta
                    return meta._meta_table['Pbr.Nodes.Node.PolicyMap']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_oper as meta
                return meta._meta_table['Pbr.Nodes.Node']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_oper as meta
            return meta._meta_table['Pbr.Nodes']['meta_info']

    def clone_ptr(self):
        self._top_entity = Pbr()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pbr_oper as meta
        return meta._meta_table['Pbr']['meta_info']


