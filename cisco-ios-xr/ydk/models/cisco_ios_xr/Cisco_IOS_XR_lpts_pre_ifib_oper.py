""" Cisco_IOS_XR_lpts_pre_ifib_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR lpts\-pre\-ifib package operational data.

This module contains definitions
for the following management objects\:
  lpts\-pifib\: lpts pre\-ifib data

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



class LptsPifib(Enum):
    """
    LptsPifib (Enum Class)

    Lpts pifib

    .. data:: isis = 0

    	ISIS packets

    .. data:: ipv4_frag = 1

    	IPv4 fragmented packets

    .. data:: ipv4_echo = 2

    	IPv4 ICMP Echo packets

    .. data:: ipv4_any = 3

    	All IPv4 packets

    .. data:: ipv6_frag = 4

    	IPv6 fragmented packets

    .. data:: ipv6_echo = 5

    	IPv6 ICMP Echo packets

    .. data:: ipv6_nd = 6

    	IPv6 ND packets

    .. data:: ipv6_any = 7

    	All IPv6 packets

    .. data:: bfd_any = 8

    	BFD packets

    .. data:: all = 9

    	All packets

    """

    isis = Enum.YLeaf(0, "isis")

    ipv4_frag = Enum.YLeaf(1, "ipv4-frag")

    ipv4_echo = Enum.YLeaf(2, "ipv4-echo")

    ipv4_any = Enum.YLeaf(3, "ipv4-any")

    ipv6_frag = Enum.YLeaf(4, "ipv6-frag")

    ipv6_echo = Enum.YLeaf(5, "ipv6-echo")

    ipv6_nd = Enum.YLeaf(6, "ipv6-nd")

    ipv6_any = Enum.YLeaf(7, "ipv6-any")

    bfd_any = Enum.YLeaf(8, "bfd-any")

    all = Enum.YLeaf(9, "all")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_pre_ifib_oper as meta
        return meta._meta_table['LptsPifib']



class LptsPifib_(_Entity_):
    """
    lpts pre\-ifib data
    
    .. attribute:: nodes
    
    	List of Pre\-ifib Nodes
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib_.Nodes>`
    
    	**config**\: False
    
    

    """

    _prefix = 'lpts-pre-ifib-oper'
    _revision = '2019-11-06'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(LptsPifib_, self).__init__()
        self._top_entity = None

        self.yang_name = "lpts-pifib"
        self.yang_parent_name = "Cisco-IOS-XR-lpts-pre-ifib-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("nodes", ("nodes", LptsPifib_.Nodes))])
        self._leafs = OrderedDict()

        self.nodes = LptsPifib_.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._segment_path = lambda: "Cisco-IOS-XR-lpts-pre-ifib-oper:lpts-pifib"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(LptsPifib_, [], name, value)


    class Nodes(_Entity_):
        """
        List of Pre\-ifib Nodes
        
        .. attribute:: node
        
        	Pre\-ifib data for particular node
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib_.Nodes.Node>`
        
        	**config**\: False
        
        

        """

        _prefix = 'lpts-pre-ifib-oper'
        _revision = '2019-11-06'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(LptsPifib_.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "lpts-pifib"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("node", ("node", LptsPifib_.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-lpts-pre-ifib-oper:lpts-pifib/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(LptsPifib_.Nodes, [], name, value)


        class Node(_Entity_):
            """
            Pre\-ifib data for particular node
            
            .. attribute:: node_name  (key)
            
            	The node name
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            	**config**\: False
            
            .. attribute:: shadow_entries
            
            	Pre\-IFIB Shadow Entries (PI)
            	**type**\:  :py:class:`ShadowEntries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib_.Nodes.Node.ShadowEntries>`
            
            	**config**\: False
            
            .. attribute:: type_values
            
            	Type specific
            	**type**\:  :py:class:`TypeValues <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib_.Nodes.Node.TypeValues>`
            
            	**config**\: False
            
            .. attribute:: domains
            
            	data for pre\-ifib domains
            	**type**\:  :py:class:`Domains <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib_.Nodes.Node.Domains>`
            
            	**config**\: False
            
            .. attribute:: dynamic_flows_stats
            
            	Dynamic Flows Statistics
            	**type**\:  :py:class:`DynamicFlowsStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib_.Nodes.Node.DynamicFlowsStats>`
            
            	**config**\: False
            
            .. attribute:: punt_policer_stats
            
            	Punt Policer Statistics
            	**type**\:  :py:class:`PuntPolicerStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib_.Nodes.Node.PuntPolicerStats>`
            
            	**config**\: False
            
            .. attribute:: hardware
            
            	Hardware specific
            	**type**\:  :py:class:`Hardware <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib_.Nodes.Node.Hardware>`
            
            	**config**\: False
            
            

            """

            _prefix = 'lpts-pre-ifib-oper'
            _revision = '2019-11-06'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(LptsPifib_.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_classes = OrderedDict([("shadow-entries", ("shadow_entries", LptsPifib_.Nodes.Node.ShadowEntries)), ("type-values", ("type_values", LptsPifib_.Nodes.Node.TypeValues)), ("domains", ("domains", LptsPifib_.Nodes.Node.Domains)), ("dynamic-flows-stats", ("dynamic_flows_stats", LptsPifib_.Nodes.Node.DynamicFlowsStats)), ("punt-policer-stats", ("punt_policer_stats", LptsPifib_.Nodes.Node.PuntPolicerStats)), ("Cisco-IOS-XR-platform-pifib-oper:hardware", ("hardware", LptsPifib_.Nodes.Node.Hardware))])
                self._leafs = OrderedDict([
                    ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                ])
                self.node_name = None

                self.shadow_entries = LptsPifib_.Nodes.Node.ShadowEntries()
                self.shadow_entries.parent = self
                self._children_name_map["shadow_entries"] = "shadow-entries"

                self.type_values = LptsPifib_.Nodes.Node.TypeValues()
                self.type_values.parent = self
                self._children_name_map["type_values"] = "type-values"

                self.domains = LptsPifib_.Nodes.Node.Domains()
                self.domains.parent = self
                self._children_name_map["domains"] = "domains"

                self.dynamic_flows_stats = LptsPifib_.Nodes.Node.DynamicFlowsStats()
                self.dynamic_flows_stats.parent = self
                self._children_name_map["dynamic_flows_stats"] = "dynamic-flows-stats"

                self.punt_policer_stats = LptsPifib_.Nodes.Node.PuntPolicerStats()
                self.punt_policer_stats.parent = self
                self._children_name_map["punt_policer_stats"] = "punt-policer-stats"

                self.hardware = LptsPifib_.Nodes.Node.Hardware()
                self.hardware.parent = self
                self._children_name_map["hardware"] = "Cisco-IOS-XR-platform-pifib-oper:hardware"
                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-lpts-pre-ifib-oper:lpts-pifib/nodes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(LptsPifib_.Nodes.Node, ['node_name'], name, value)


            class ShadowEntries(_Entity_):
                """
                Pre\-IFIB Shadow Entries (PI)
                
                .. attribute:: entry
                
                	Data for single pre\-ifib entry
                	**type**\: list of  		 :py:class:`Entry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib_.Nodes.Node.ShadowEntries.Entry>`
                
                	**config**\: False
                
                

                """

                _prefix = 'lpts-pre-ifib-oper'
                _revision = '2019-11-06'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(LptsPifib_.Nodes.Node.ShadowEntries, self).__init__()

                    self.yang_name = "shadow-entries"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("entry", ("entry", LptsPifib_.Nodes.Node.ShadowEntries.Entry))])
                    self._leafs = OrderedDict()

                    self.entry = YList(self)
                    self._segment_path = lambda: "shadow-entries"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(LptsPifib_.Nodes.Node.ShadowEntries, [], name, value)


                class Entry(_Entity_):
                    """
                    Data for single pre\-ifib entry
                    
                    .. attribute:: entry  (key)
                    
                    	Single Pre\-ifib entry
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    	**config**\: False
                    
                    .. attribute:: vrf_name
                    
                    	VRF Name
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: vid
                    
                    	VRF ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l3protocol
                    
                    	Layer 3 Protocol
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l4protocol
                    
                    	Layer 4 Protocol
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: intf_name
                    
                    	Interface Name
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: intf_handle
                    
                    	Interface Handle
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: destination_addr
                    
                    	Destination IP Address
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: source_addr
                    
                    	Source IP Address
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: destination_type
                    
                    	Destination Key Type
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: destination_value
                    
                    	Destination Port/ICMP Type/IGMP Type
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: source_port
                    
                    	Source port
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: is_frag
                    
                    	Is Fragment
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: is_syn
                    
                    	Is SYN
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: opcode
                    
                    	Opcode
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: flow_type
                    
                    	Flow type
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: listener_tag
                    
                    	Listener Tag
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: local_flag
                    
                    	Local Flag
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: is_fgid
                    
                    	Is FGID or not
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: deliver_list_short
                    
                    	Deliver List Short Format
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: deliver_list_long
                    
                    	Deliver List Long Format
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: min_ttl
                    
                    	Minimum TTL
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: accepts
                    
                    	Packets matched to accept
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: drops
                    
                    	Packets matched for drop
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: stale
                    
                    	Is Stale
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: pifib_type
                    
                    	sub Pre\-IFIB type
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: pifib_program_time
                    
                    	Creation or Update Time
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: domain_idx
                    
                    	Domain Index
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: domain_name
                    
                    	Domain Name
                    	**type**\: str
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'lpts-pre-ifib-oper'
                    _revision = '2019-11-06'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(LptsPifib_.Nodes.Node.ShadowEntries.Entry, self).__init__()

                        self.yang_name = "entry"
                        self.yang_parent_name = "shadow-entries"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['entry']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('entry', (YLeaf(YType.str, 'entry'), ['str'])),
                            ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                            ('vid', (YLeaf(YType.uint32, 'vid'), ['int'])),
                            ('l3protocol', (YLeaf(YType.uint32, 'l3protocol'), ['int'])),
                            ('l4protocol', (YLeaf(YType.uint32, 'l4protocol'), ['int'])),
                            ('intf_name', (YLeaf(YType.str, 'intf-name'), ['str'])),
                            ('intf_handle', (YLeaf(YType.uint32, 'intf-handle'), ['int'])),
                            ('destination_addr', (YLeaf(YType.str, 'destination-addr'), ['str'])),
                            ('source_addr', (YLeaf(YType.str, 'source-addr'), ['str'])),
                            ('destination_type', (YLeaf(YType.str, 'destination-type'), ['str'])),
                            ('destination_value', (YLeaf(YType.str, 'destination-value'), ['str'])),
                            ('source_port', (YLeaf(YType.str, 'source-port'), ['str'])),
                            ('is_frag', (YLeaf(YType.uint8, 'is-frag'), ['int'])),
                            ('is_syn', (YLeaf(YType.uint8, 'is-syn'), ['int'])),
                            ('opcode', (YLeaf(YType.str, 'opcode'), ['str'])),
                            ('flow_type', (YLeaf(YType.str, 'flow-type'), ['str'])),
                            ('listener_tag', (YLeaf(YType.str, 'listener-tag'), ['str'])),
                            ('local_flag', (YLeaf(YType.uint8, 'local-flag'), ['int'])),
                            ('is_fgid', (YLeaf(YType.uint8, 'is-fgid'), ['int'])),
                            ('deliver_list_short', (YLeaf(YType.str, 'deliver-list-short'), ['str'])),
                            ('deliver_list_long', (YLeaf(YType.str, 'deliver-list-long'), ['str'])),
                            ('min_ttl', (YLeaf(YType.uint8, 'min-ttl'), ['int'])),
                            ('accepts', (YLeaf(YType.uint64, 'accepts'), ['int'])),
                            ('drops', (YLeaf(YType.uint64, 'drops'), ['int'])),
                            ('stale', (YLeaf(YType.uint8, 'stale'), ['int'])),
                            ('pifib_type', (YLeaf(YType.uint8, 'pifib-type'), ['int'])),
                            ('pifib_program_time', (YLeaf(YType.str, 'pifib-program-time'), ['str'])),
                            ('domain_idx', (YLeaf(YType.uint8, 'domain-idx'), ['int'])),
                            ('domain_name', (YLeaf(YType.str, 'domain-name'), ['str'])),
                        ])
                        self.entry = None
                        self.vrf_name = None
                        self.vid = None
                        self.l3protocol = None
                        self.l4protocol = None
                        self.intf_name = None
                        self.intf_handle = None
                        self.destination_addr = None
                        self.source_addr = None
                        self.destination_type = None
                        self.destination_value = None
                        self.source_port = None
                        self.is_frag = None
                        self.is_syn = None
                        self.opcode = None
                        self.flow_type = None
                        self.listener_tag = None
                        self.local_flag = None
                        self.is_fgid = None
                        self.deliver_list_short = None
                        self.deliver_list_long = None
                        self.min_ttl = None
                        self.accepts = None
                        self.drops = None
                        self.stale = None
                        self.pifib_type = None
                        self.pifib_program_time = None
                        self.domain_idx = None
                        self.domain_name = None
                        self._segment_path = lambda: "entry" + "[entry='" + str(self.entry) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(LptsPifib_.Nodes.Node.ShadowEntries.Entry, ['entry', 'vrf_name', 'vid', 'l3protocol', 'l4protocol', 'intf_name', 'intf_handle', 'destination_addr', 'source_addr', 'destination_type', 'destination_value', 'source_port', 'is_frag', 'is_syn', 'opcode', 'flow_type', 'listener_tag', 'local_flag', 'is_fgid', 'deliver_list_short', 'deliver_list_long', 'min_ttl', 'accepts', 'drops', 'stale', 'pifib_type', 'pifib_program_time', 'domain_idx', 'domain_name'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_pre_ifib_oper as meta
                        return meta._meta_table['LptsPifib_.Nodes.Node.ShadowEntries.Entry']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_pre_ifib_oper as meta
                    return meta._meta_table['LptsPifib_.Nodes.Node.ShadowEntries']['meta_info']


            class TypeValues(_Entity_):
                """
                Type specific
                
                .. attribute:: type_value
                
                	pifib types
                	**type**\: list of  		 :py:class:`TypeValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib_.Nodes.Node.TypeValues.TypeValue>`
                
                	**config**\: False
                
                

                """

                _prefix = 'lpts-pre-ifib-oper'
                _revision = '2019-11-06'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(LptsPifib_.Nodes.Node.TypeValues, self).__init__()

                    self.yang_name = "type-values"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("type-value", ("type_value", LptsPifib_.Nodes.Node.TypeValues.TypeValue))])
                    self._leafs = OrderedDict()

                    self.type_value = YList(self)
                    self._segment_path = lambda: "type-values"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(LptsPifib_.Nodes.Node.TypeValues, [], name, value)


                class TypeValue(_Entity_):
                    """
                    pifib types
                    
                    .. attribute:: pifib_type  (key)
                    
                    	Type value
                    	**type**\:  :py:class:`LptsPifib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib>`
                    
                    	**config**\: False
                    
                    .. attribute:: entry
                    
                    	Data for single pre\-ifib entry
                    	**type**\: list of  		 :py:class:`Entry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib_.Nodes.Node.TypeValues.TypeValue.Entry>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'lpts-pre-ifib-oper'
                    _revision = '2019-11-06'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(LptsPifib_.Nodes.Node.TypeValues.TypeValue, self).__init__()

                        self.yang_name = "type-value"
                        self.yang_parent_name = "type-values"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['pifib_type']
                        self._child_classes = OrderedDict([("entry", ("entry", LptsPifib_.Nodes.Node.TypeValues.TypeValue.Entry))])
                        self._leafs = OrderedDict([
                            ('pifib_type', (YLeaf(YType.enumeration, 'pifib-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper', 'LptsPifib', '')])),
                        ])
                        self.pifib_type = None

                        self.entry = YList(self)
                        self._segment_path = lambda: "type-value" + "[pifib-type='" + str(self.pifib_type) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(LptsPifib_.Nodes.Node.TypeValues.TypeValue, ['pifib_type'], name, value)


                    class Entry(_Entity_):
                        """
                        Data for single pre\-ifib entry
                        
                        .. attribute:: entry  (key)
                        
                        	Single Pre\-ifib entry
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        	**config**\: False
                        
                        .. attribute:: vrf_name
                        
                        	VRF Name
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: vid
                        
                        	VRF ID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: l3protocol
                        
                        	Layer 3 Protocol
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: l4protocol
                        
                        	Layer 4 Protocol
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: intf_name
                        
                        	Interface Name
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: intf_handle
                        
                        	Interface Handle
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: destination_addr
                        
                        	Destination IP Address
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: source_addr
                        
                        	Source IP Address
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: destination_type
                        
                        	Destination Key Type
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: destination_value
                        
                        	Destination Port/ICMP Type/IGMP Type
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: source_port
                        
                        	Source port
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: is_frag
                        
                        	Is Fragment
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: is_syn
                        
                        	Is SYN
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: opcode
                        
                        	Opcode
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: flow_type
                        
                        	Flow type
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: listener_tag
                        
                        	Listener Tag
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: local_flag
                        
                        	Local Flag
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: is_fgid
                        
                        	Is FGID or not
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: deliver_list_short
                        
                        	Deliver List Short Format
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: deliver_list_long
                        
                        	Deliver List Long Format
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: min_ttl
                        
                        	Minimum TTL
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: accepts
                        
                        	Packets matched to accept
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: drops
                        
                        	Packets matched for drop
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: stale
                        
                        	Is Stale
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: pifib_type
                        
                        	sub Pre\-IFIB type
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: pifib_program_time
                        
                        	Creation or Update Time
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: domain_idx
                        
                        	Domain Index
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: domain_name
                        
                        	Domain Name
                        	**type**\: str
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'lpts-pre-ifib-oper'
                        _revision = '2019-11-06'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(LptsPifib_.Nodes.Node.TypeValues.TypeValue.Entry, self).__init__()

                            self.yang_name = "entry"
                            self.yang_parent_name = "type-value"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['entry']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('entry', (YLeaf(YType.str, 'entry'), ['str'])),
                                ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                                ('vid', (YLeaf(YType.uint32, 'vid'), ['int'])),
                                ('l3protocol', (YLeaf(YType.uint32, 'l3protocol'), ['int'])),
                                ('l4protocol', (YLeaf(YType.uint32, 'l4protocol'), ['int'])),
                                ('intf_name', (YLeaf(YType.str, 'intf-name'), ['str'])),
                                ('intf_handle', (YLeaf(YType.uint32, 'intf-handle'), ['int'])),
                                ('destination_addr', (YLeaf(YType.str, 'destination-addr'), ['str'])),
                                ('source_addr', (YLeaf(YType.str, 'source-addr'), ['str'])),
                                ('destination_type', (YLeaf(YType.str, 'destination-type'), ['str'])),
                                ('destination_value', (YLeaf(YType.str, 'destination-value'), ['str'])),
                                ('source_port', (YLeaf(YType.str, 'source-port'), ['str'])),
                                ('is_frag', (YLeaf(YType.uint8, 'is-frag'), ['int'])),
                                ('is_syn', (YLeaf(YType.uint8, 'is-syn'), ['int'])),
                                ('opcode', (YLeaf(YType.str, 'opcode'), ['str'])),
                                ('flow_type', (YLeaf(YType.str, 'flow-type'), ['str'])),
                                ('listener_tag', (YLeaf(YType.str, 'listener-tag'), ['str'])),
                                ('local_flag', (YLeaf(YType.uint8, 'local-flag'), ['int'])),
                                ('is_fgid', (YLeaf(YType.uint8, 'is-fgid'), ['int'])),
                                ('deliver_list_short', (YLeaf(YType.str, 'deliver-list-short'), ['str'])),
                                ('deliver_list_long', (YLeaf(YType.str, 'deliver-list-long'), ['str'])),
                                ('min_ttl', (YLeaf(YType.uint8, 'min-ttl'), ['int'])),
                                ('accepts', (YLeaf(YType.uint64, 'accepts'), ['int'])),
                                ('drops', (YLeaf(YType.uint64, 'drops'), ['int'])),
                                ('stale', (YLeaf(YType.uint8, 'stale'), ['int'])),
                                ('pifib_type', (YLeaf(YType.uint8, 'pifib-type'), ['int'])),
                                ('pifib_program_time', (YLeaf(YType.str, 'pifib-program-time'), ['str'])),
                                ('domain_idx', (YLeaf(YType.uint8, 'domain-idx'), ['int'])),
                                ('domain_name', (YLeaf(YType.str, 'domain-name'), ['str'])),
                            ])
                            self.entry = None
                            self.vrf_name = None
                            self.vid = None
                            self.l3protocol = None
                            self.l4protocol = None
                            self.intf_name = None
                            self.intf_handle = None
                            self.destination_addr = None
                            self.source_addr = None
                            self.destination_type = None
                            self.destination_value = None
                            self.source_port = None
                            self.is_frag = None
                            self.is_syn = None
                            self.opcode = None
                            self.flow_type = None
                            self.listener_tag = None
                            self.local_flag = None
                            self.is_fgid = None
                            self.deliver_list_short = None
                            self.deliver_list_long = None
                            self.min_ttl = None
                            self.accepts = None
                            self.drops = None
                            self.stale = None
                            self.pifib_type = None
                            self.pifib_program_time = None
                            self.domain_idx = None
                            self.domain_name = None
                            self._segment_path = lambda: "entry" + "[entry='" + str(self.entry) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(LptsPifib_.Nodes.Node.TypeValues.TypeValue.Entry, ['entry', 'vrf_name', 'vid', 'l3protocol', 'l4protocol', 'intf_name', 'intf_handle', 'destination_addr', 'source_addr', 'destination_type', 'destination_value', 'source_port', 'is_frag', 'is_syn', 'opcode', 'flow_type', 'listener_tag', 'local_flag', 'is_fgid', 'deliver_list_short', 'deliver_list_long', 'min_ttl', 'accepts', 'drops', 'stale', 'pifib_type', 'pifib_program_time', 'domain_idx', 'domain_name'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_pre_ifib_oper as meta
                            return meta._meta_table['LptsPifib_.Nodes.Node.TypeValues.TypeValue.Entry']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_pre_ifib_oper as meta
                        return meta._meta_table['LptsPifib_.Nodes.Node.TypeValues.TypeValue']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_pre_ifib_oper as meta
                    return meta._meta_table['LptsPifib_.Nodes.Node.TypeValues']['meta_info']


            class Domains(_Entity_):
                """
                data for pre\-ifib domains
                
                .. attribute:: config_data
                
                	Domain Config Data
                	**type**\:  :py:class:`ConfigData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib_.Nodes.Node.Domains.ConfigData>`
                
                	**config**\: False
                
                .. attribute:: domains_enabled
                
                	Domains Enabled
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: number_of_supported_domains
                
                	Number of Supported Domains
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                

                """

                _prefix = 'lpts-pre-ifib-oper'
                _revision = '2019-11-06'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(LptsPifib_.Nodes.Node.Domains, self).__init__()

                    self.yang_name = "domains"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("config-data", ("config_data", LptsPifib_.Nodes.Node.Domains.ConfigData))])
                    self._leafs = OrderedDict([
                        ('domains_enabled', (YLeaf(YType.boolean, 'domains-enabled'), ['bool'])),
                        ('number_of_supported_domains', (YLeaf(YType.uint32, 'number-of-supported-domains'), ['int'])),
                    ])
                    self.domains_enabled = None
                    self.number_of_supported_domains = None

                    self.config_data = LptsPifib_.Nodes.Node.Domains.ConfigData()
                    self.config_data.parent = self
                    self._children_name_map["config_data"] = "config-data"
                    self._segment_path = lambda: "domains"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(LptsPifib_.Nodes.Node.Domains, ['domains_enabled', 'number_of_supported_domains'], name, value)


                class ConfigData(_Entity_):
                    """
                    Domain Config Data
                    
                    .. attribute:: number_of_active_domains
                    
                    	Number of Active Domains
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: domains_info
                    
                    	Domains Info
                    	**type**\: list of  		 :py:class:`DomainsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib_.Nodes.Node.Domains.ConfigData.DomainsInfo>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'lpts-pre-ifib-oper'
                    _revision = '2019-11-06'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(LptsPifib_.Nodes.Node.Domains.ConfigData, self).__init__()

                        self.yang_name = "config-data"
                        self.yang_parent_name = "domains"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("domains-info", ("domains_info", LptsPifib_.Nodes.Node.Domains.ConfigData.DomainsInfo))])
                        self._leafs = OrderedDict([
                            ('number_of_active_domains', (YLeaf(YType.uint8, 'number-of-active-domains'), ['int'])),
                        ])
                        self.number_of_active_domains = None

                        self.domains_info = YList(self)
                        self._segment_path = lambda: "config-data"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(LptsPifib_.Nodes.Node.Domains.ConfigData, ['number_of_active_domains'], name, value)


                    class DomainsInfo(_Entity_):
                        """
                        Domains Info
                        
                        .. attribute:: domain_name
                        
                        	Domain Name
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: domain_index
                        
                        	Domain Index
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: number_of_interfaces
                        
                        	Number of Interfaces
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: interface
                        
                        	Interface List
                        	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib_.Nodes.Node.Domains.ConfigData.DomainsInfo.Interface>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'lpts-pre-ifib-oper'
                        _revision = '2019-11-06'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(LptsPifib_.Nodes.Node.Domains.ConfigData.DomainsInfo, self).__init__()

                            self.yang_name = "domains-info"
                            self.yang_parent_name = "config-data"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("interface", ("interface", LptsPifib_.Nodes.Node.Domains.ConfigData.DomainsInfo.Interface))])
                            self._leafs = OrderedDict([
                                ('domain_name', (YLeaf(YType.str, 'domain-name'), ['str'])),
                                ('domain_index', (YLeaf(YType.uint8, 'domain-index'), ['int'])),
                                ('number_of_interfaces', (YLeaf(YType.uint32, 'number-of-interfaces'), ['int'])),
                            ])
                            self.domain_name = None
                            self.domain_index = None
                            self.number_of_interfaces = None

                            self.interface = YList(self)
                            self._segment_path = lambda: "domains-info"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(LptsPifib_.Nodes.Node.Domains.ConfigData.DomainsInfo, ['domain_name', 'domain_index', 'number_of_interfaces'], name, value)


                        class Interface(_Entity_):
                            """
                            Interface List
                            
                            .. attribute:: interface_handle
                            
                            	Interface Handle
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            	**config**\: False
                            
                            .. attribute:: interface_name
                            
                            	Interface Name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: virtual_interface
                            
                            	Interface is Virtual
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'lpts-pre-ifib-oper'
                            _revision = '2019-11-06'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(LptsPifib_.Nodes.Node.Domains.ConfigData.DomainsInfo.Interface, self).__init__()

                                self.yang_name = "interface"
                                self.yang_parent_name = "domains-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('interface_handle', (YLeaf(YType.str, 'interface-handle'), ['str'])),
                                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                    ('virtual_interface', (YLeaf(YType.boolean, 'virtual-interface'), ['bool'])),
                                ])
                                self.interface_handle = None
                                self.interface_name = None
                                self.virtual_interface = None
                                self._segment_path = lambda: "interface"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(LptsPifib_.Nodes.Node.Domains.ConfigData.DomainsInfo.Interface, ['interface_handle', 'interface_name', 'virtual_interface'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_pre_ifib_oper as meta
                                return meta._meta_table['LptsPifib_.Nodes.Node.Domains.ConfigData.DomainsInfo.Interface']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_pre_ifib_oper as meta
                            return meta._meta_table['LptsPifib_.Nodes.Node.Domains.ConfigData.DomainsInfo']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_pre_ifib_oper as meta
                        return meta._meta_table['LptsPifib_.Nodes.Node.Domains.ConfigData']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_pre_ifib_oper as meta
                    return meta._meta_table['LptsPifib_.Nodes.Node.Domains']['meta_info']


            class DynamicFlowsStats(_Entity_):
                """
                Dynamic Flows Statistics
                
                .. attribute:: dynamic_flows_enabled
                
                	Dynamic Flows Enabled
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: platform_supported_max
                
                	Platform Max
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: platform_configured_max
                
                	Platform Config Limit
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: platform_total_configured
                
                	Platform Total Configured
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: total_hw_entries
                
                	Total HW Entries
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: total_sw_entries
                
                	Total SW Entries
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: flow
                
                	Flow Datalist
                	**type**\: list of  		 :py:class:`Flow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib_.Nodes.Node.DynamicFlowsStats.Flow>`
                
                	**config**\: False
                
                

                """

                _prefix = 'lpts-pre-ifib-oper'
                _revision = '2019-11-06'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(LptsPifib_.Nodes.Node.DynamicFlowsStats, self).__init__()

                    self.yang_name = "dynamic-flows-stats"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("flow", ("flow", LptsPifib_.Nodes.Node.DynamicFlowsStats.Flow))])
                    self._leafs = OrderedDict([
                        ('dynamic_flows_enabled', (YLeaf(YType.boolean, 'dynamic-flows-enabled'), ['bool'])),
                        ('platform_supported_max', (YLeaf(YType.uint32, 'platform-supported-max'), ['int'])),
                        ('platform_configured_max', (YLeaf(YType.uint32, 'platform-configured-max'), ['int'])),
                        ('platform_total_configured', (YLeaf(YType.uint32, 'platform-total-configured'), ['int'])),
                        ('total_hw_entries', (YLeaf(YType.uint32, 'total-hw-entries'), ['int'])),
                        ('total_sw_entries', (YLeaf(YType.uint32, 'total-sw-entries'), ['int'])),
                    ])
                    self.dynamic_flows_enabled = None
                    self.platform_supported_max = None
                    self.platform_configured_max = None
                    self.platform_total_configured = None
                    self.total_hw_entries = None
                    self.total_sw_entries = None

                    self.flow = YList(self)
                    self._segment_path = lambda: "dynamic-flows-stats"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(LptsPifib_.Nodes.Node.DynamicFlowsStats, ['dynamic_flows_enabled', 'platform_supported_max', 'platform_configured_max', 'platform_total_configured', 'total_hw_entries', 'total_sw_entries'], name, value)


                class Flow(_Entity_):
                    """
                    Flow Datalist
                    
                    .. attribute:: flow_name
                    
                    	Flow Name
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: configurable
                    
                    	Is Configurable
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: configured
                    
                    	Is Configured
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: default_max
                    
                    	Default Max
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: configured_max
                    
                    	Configured Max
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: active_max
                    
                    	Active Max
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: hardware_count
                    
                    	Hardware Count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: software_count
                    
                    	Software Count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: pending_software_entries
                    
                    	Pending Software Entries
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'lpts-pre-ifib-oper'
                    _revision = '2019-11-06'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(LptsPifib_.Nodes.Node.DynamicFlowsStats.Flow, self).__init__()

                        self.yang_name = "flow"
                        self.yang_parent_name = "dynamic-flows-stats"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('flow_name', (YLeaf(YType.str, 'flow-name'), ['str'])),
                            ('configurable', (YLeaf(YType.boolean, 'configurable'), ['bool'])),
                            ('configured', (YLeaf(YType.boolean, 'configured'), ['bool'])),
                            ('default_max', (YLeaf(YType.uint32, 'default-max'), ['int'])),
                            ('configured_max', (YLeaf(YType.str, 'configured-max'), ['str'])),
                            ('active_max', (YLeaf(YType.uint32, 'active-max'), ['int'])),
                            ('hardware_count', (YLeaf(YType.uint32, 'hardware-count'), ['int'])),
                            ('software_count', (YLeaf(YType.uint32, 'software-count'), ['int'])),
                            ('pending_software_entries', (YLeaf(YType.boolean, 'pending-software-entries'), ['bool'])),
                        ])
                        self.flow_name = None
                        self.configurable = None
                        self.configured = None
                        self.default_max = None
                        self.configured_max = None
                        self.active_max = None
                        self.hardware_count = None
                        self.software_count = None
                        self.pending_software_entries = None
                        self._segment_path = lambda: "flow"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(LptsPifib_.Nodes.Node.DynamicFlowsStats.Flow, ['flow_name', 'configurable', 'configured', 'default_max', 'configured_max', 'active_max', 'hardware_count', 'software_count', 'pending_software_entries'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_pre_ifib_oper as meta
                        return meta._meta_table['LptsPifib_.Nodes.Node.DynamicFlowsStats.Flow']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_pre_ifib_oper as meta
                    return meta._meta_table['LptsPifib_.Nodes.Node.DynamicFlowsStats']['meta_info']


            class PuntPolicerStats(_Entity_):
                """
                Punt Policer Statistics
                
                .. attribute:: config_data
                
                	Punt Policer Config Data
                	**type**\:  :py:class:`ConfigData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib_.Nodes.Node.PuntPolicerStats.ConfigData>`
                
                	**config**\: False
                
                .. attribute:: punt_policer_supported
                
                	Punt Policer Supported
                	**type**\: bool
                
                	**config**\: False
                
                

                """

                _prefix = 'lpts-pre-ifib-oper'
                _revision = '2019-11-06'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(LptsPifib_.Nodes.Node.PuntPolicerStats, self).__init__()

                    self.yang_name = "punt-policer-stats"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("config-data", ("config_data", LptsPifib_.Nodes.Node.PuntPolicerStats.ConfigData))])
                    self._leafs = OrderedDict([
                        ('punt_policer_supported', (YLeaf(YType.boolean, 'punt-policer-supported'), ['bool'])),
                    ])
                    self.punt_policer_supported = None

                    self.config_data = LptsPifib_.Nodes.Node.PuntPolicerStats.ConfigData()
                    self.config_data.parent = self
                    self._children_name_map["config_data"] = "config-data"
                    self._segment_path = lambda: "punt-policer-stats"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(LptsPifib_.Nodes.Node.PuntPolicerStats, ['punt_policer_supported'], name, value)


                class ConfigData(_Entity_):
                    """
                    Punt Policer Config Data
                    
                    .. attribute:: has_config
                    
                    	config presence
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: number_of_interfaces
                    
                    	Number of Interfaces
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: number_of_domains
                    
                    	Number of Domains
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: interface
                    
                    	Interface List
                    	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib_.Nodes.Node.PuntPolicerStats.ConfigData.Interface>`
                    
                    	**config**\: False
                    
                    .. attribute:: domain
                    
                    	Domain List
                    	**type**\: list of  		 :py:class:`Domain <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib_.Nodes.Node.PuntPolicerStats.ConfigData.Domain>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'lpts-pre-ifib-oper'
                    _revision = '2019-11-06'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(LptsPifib_.Nodes.Node.PuntPolicerStats.ConfigData, self).__init__()

                        self.yang_name = "config-data"
                        self.yang_parent_name = "punt-policer-stats"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("interface", ("interface", LptsPifib_.Nodes.Node.PuntPolicerStats.ConfigData.Interface)), ("domain", ("domain", LptsPifib_.Nodes.Node.PuntPolicerStats.ConfigData.Domain))])
                        self._leafs = OrderedDict([
                            ('has_config', (YLeaf(YType.boolean, 'has-config'), ['bool'])),
                            ('number_of_interfaces', (YLeaf(YType.uint32, 'number-of-interfaces'), ['int'])),
                            ('number_of_domains', (YLeaf(YType.uint32, 'number-of-domains'), ['int'])),
                        ])
                        self.has_config = None
                        self.number_of_interfaces = None
                        self.number_of_domains = None

                        self.interface = YList(self)
                        self.domain = YList(self)
                        self._segment_path = lambda: "config-data"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(LptsPifib_.Nodes.Node.PuntPolicerStats.ConfigData, ['has_config', 'number_of_interfaces', 'number_of_domains'], name, value)


                    class Interface(_Entity_):
                        """
                        Interface List
                        
                        .. attribute:: interface_handle
                        
                        	Interface Handle
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        	**config**\: False
                        
                        .. attribute:: interface_name
                        
                        	Interface Name
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: virtual_interface
                        
                        	Interface is Virtual
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: number_of_punt_types
                        
                        	Number of Punt types
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: punt_type
                        
                        	Punt type List
                        	**type**\: list of  		 :py:class:`PuntType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib_.Nodes.Node.PuntPolicerStats.ConfigData.Interface.PuntType>`
                        
                        	**config**\: False
                        
                        .. attribute:: applied_config
                        
                        	Applied Policer Data
                        	**type**\: list of  		 :py:class:`AppliedConfig <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib_.Nodes.Node.PuntPolicerStats.ConfigData.Interface.AppliedConfig>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'lpts-pre-ifib-oper'
                        _revision = '2019-11-06'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(LptsPifib_.Nodes.Node.PuntPolicerStats.ConfigData.Interface, self).__init__()

                            self.yang_name = "interface"
                            self.yang_parent_name = "config-data"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("punt-type", ("punt_type", LptsPifib_.Nodes.Node.PuntPolicerStats.ConfigData.Interface.PuntType)), ("applied-config", ("applied_config", LptsPifib_.Nodes.Node.PuntPolicerStats.ConfigData.Interface.AppliedConfig))])
                            self._leafs = OrderedDict([
                                ('interface_handle', (YLeaf(YType.str, 'interface-handle'), ['str'])),
                                ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                ('virtual_interface', (YLeaf(YType.boolean, 'virtual-interface'), ['bool'])),
                                ('number_of_punt_types', (YLeaf(YType.uint32, 'number-of-punt-types'), ['int'])),
                            ])
                            self.interface_handle = None
                            self.interface_name = None
                            self.virtual_interface = None
                            self.number_of_punt_types = None

                            self.punt_type = YList(self)
                            self.applied_config = YList(self)
                            self._segment_path = lambda: "interface"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(LptsPifib_.Nodes.Node.PuntPolicerStats.ConfigData.Interface, ['interface_handle', 'interface_name', 'virtual_interface', 'number_of_punt_types'], name, value)


                        class PuntType(_Entity_):
                            """
                            Punt type List
                            
                            .. attribute:: punt_name
                            
                            	Punt Name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: configured
                            
                            	Is Configured
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: active_cfg_state
                            
                            	Active Cfg State
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: enabled
                            
                            	Is Enabled
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: pending
                            
                            	Is Pending
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: configured_rate
                            
                            	Configured Policer Rate
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: operational_rate
                            
                            	Operational Policer Rate
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: domain_name
                            
                            	Domain Name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: domain_index
                            
                            	Domain Index
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            .. attribute:: accepted
                            
                            	Packets matched to accept
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: dropped
                            
                            	Packets matched for drop
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'lpts-pre-ifib-oper'
                            _revision = '2019-11-06'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(LptsPifib_.Nodes.Node.PuntPolicerStats.ConfigData.Interface.PuntType, self).__init__()

                                self.yang_name = "punt-type"
                                self.yang_parent_name = "interface"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('punt_name', (YLeaf(YType.str, 'punt-name'), ['str'])),
                                    ('configured', (YLeaf(YType.boolean, 'configured'), ['bool'])),
                                    ('active_cfg_state', (YLeaf(YType.str, 'active-cfg-state'), ['str'])),
                                    ('enabled', (YLeaf(YType.boolean, 'enabled'), ['bool'])),
                                    ('pending', (YLeaf(YType.boolean, 'pending'), ['bool'])),
                                    ('configured_rate', (YLeaf(YType.uint32, 'configured-rate'), ['int'])),
                                    ('operational_rate', (YLeaf(YType.uint32, 'operational-rate'), ['int'])),
                                    ('domain_name', (YLeaf(YType.str, 'domain-name'), ['str'])),
                                    ('domain_index', (YLeaf(YType.uint8, 'domain-index'), ['int'])),
                                    ('accepted', (YLeaf(YType.uint64, 'accepted'), ['int'])),
                                    ('dropped', (YLeaf(YType.uint64, 'dropped'), ['int'])),
                                ])
                                self.punt_name = None
                                self.configured = None
                                self.active_cfg_state = None
                                self.enabled = None
                                self.pending = None
                                self.configured_rate = None
                                self.operational_rate = None
                                self.domain_name = None
                                self.domain_index = None
                                self.accepted = None
                                self.dropped = None
                                self._segment_path = lambda: "punt-type"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(LptsPifib_.Nodes.Node.PuntPolicerStats.ConfigData.Interface.PuntType, ['punt_name', 'configured', 'active_cfg_state', 'enabled', 'pending', 'configured_rate', 'operational_rate', 'domain_name', 'domain_index', 'accepted', 'dropped'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_pre_ifib_oper as meta
                                return meta._meta_table['LptsPifib_.Nodes.Node.PuntPolicerStats.ConfigData.Interface.PuntType']['meta_info']


                        class AppliedConfig(_Entity_):
                            """
                            Applied Policer Data
                            
                            .. attribute:: interface_handle
                            
                            	Interface Handle
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            	**config**\: False
                            
                            .. attribute:: virtual_interface
                            
                            	Interface is Virtual
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: punt_name
                            
                            	Punt Name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: enabled
                            
                            	Is Enabled
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: configured_rate
                            
                            	Configured Policer Rate
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: domain_index
                            
                            	Domain Index
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            .. attribute:: punt_police_program_time
                            
                            	Creation or Update Time
                            	**type**\: str
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'lpts-pre-ifib-oper'
                            _revision = '2019-11-06'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(LptsPifib_.Nodes.Node.PuntPolicerStats.ConfigData.Interface.AppliedConfig, self).__init__()

                                self.yang_name = "applied-config"
                                self.yang_parent_name = "interface"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('interface_handle', (YLeaf(YType.str, 'interface-handle'), ['str'])),
                                    ('virtual_interface', (YLeaf(YType.boolean, 'virtual-interface'), ['bool'])),
                                    ('punt_name', (YLeaf(YType.str, 'punt-name'), ['str'])),
                                    ('enabled', (YLeaf(YType.boolean, 'enabled'), ['bool'])),
                                    ('configured_rate', (YLeaf(YType.uint32, 'configured-rate'), ['int'])),
                                    ('domain_index', (YLeaf(YType.uint8, 'domain-index'), ['int'])),
                                    ('punt_police_program_time', (YLeaf(YType.str, 'punt-police-program-time'), ['str'])),
                                ])
                                self.interface_handle = None
                                self.virtual_interface = None
                                self.punt_name = None
                                self.enabled = None
                                self.configured_rate = None
                                self.domain_index = None
                                self.punt_police_program_time = None
                                self._segment_path = lambda: "applied-config"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(LptsPifib_.Nodes.Node.PuntPolicerStats.ConfigData.Interface.AppliedConfig, ['interface_handle', 'virtual_interface', 'punt_name', 'enabled', 'configured_rate', 'domain_index', 'punt_police_program_time'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_pre_ifib_oper as meta
                                return meta._meta_table['LptsPifib_.Nodes.Node.PuntPolicerStats.ConfigData.Interface.AppliedConfig']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_pre_ifib_oper as meta
                            return meta._meta_table['LptsPifib_.Nodes.Node.PuntPolicerStats.ConfigData.Interface']['meta_info']


                    class Domain(_Entity_):
                        """
                        Domain List
                        
                        .. attribute:: domain_index
                        
                        	Domain Index
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: domain_name
                        
                        	Domain Name
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: valid
                        
                        	Domain is Valid
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: number_of_punt_types
                        
                        	Number of Punt types
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: punt_type
                        
                        	Punt type List
                        	**type**\: list of  		 :py:class:`PuntType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib_.Nodes.Node.PuntPolicerStats.ConfigData.Domain.PuntType>`
                        
                        	**config**\: False
                        
                        .. attribute:: applied_config
                        
                        	Applied Policer Data
                        	**type**\: list of  		 :py:class:`AppliedConfig <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib_.Nodes.Node.PuntPolicerStats.ConfigData.Domain.AppliedConfig>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'lpts-pre-ifib-oper'
                        _revision = '2019-11-06'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(LptsPifib_.Nodes.Node.PuntPolicerStats.ConfigData.Domain, self).__init__()

                            self.yang_name = "domain"
                            self.yang_parent_name = "config-data"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("punt-type", ("punt_type", LptsPifib_.Nodes.Node.PuntPolicerStats.ConfigData.Domain.PuntType)), ("applied-config", ("applied_config", LptsPifib_.Nodes.Node.PuntPolicerStats.ConfigData.Domain.AppliedConfig))])
                            self._leafs = OrderedDict([
                                ('domain_index', (YLeaf(YType.uint8, 'domain-index'), ['int'])),
                                ('domain_name', (YLeaf(YType.str, 'domain-name'), ['str'])),
                                ('valid', (YLeaf(YType.boolean, 'valid'), ['bool'])),
                                ('number_of_punt_types', (YLeaf(YType.uint32, 'number-of-punt-types'), ['int'])),
                            ])
                            self.domain_index = None
                            self.domain_name = None
                            self.valid = None
                            self.number_of_punt_types = None

                            self.punt_type = YList(self)
                            self.applied_config = YList(self)
                            self._segment_path = lambda: "domain"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(LptsPifib_.Nodes.Node.PuntPolicerStats.ConfigData.Domain, ['domain_index', 'domain_name', 'valid', 'number_of_punt_types'], name, value)


                        class PuntType(_Entity_):
                            """
                            Punt type List
                            
                            .. attribute:: punt_name
                            
                            	Punt Name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: configured
                            
                            	Is Configured
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: active_cfg_state
                            
                            	Active Cfg State
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: enabled
                            
                            	Is Enabled
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: pending
                            
                            	Is Pending
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: configured_rate
                            
                            	Configured Policer Rate
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: operational_rate
                            
                            	Operational Policer Rate
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: domain_name
                            
                            	Domain Name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: domain_index
                            
                            	Domain Index
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            .. attribute:: accepted
                            
                            	Packets matched to accept
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: dropped
                            
                            	Packets matched for drop
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'lpts-pre-ifib-oper'
                            _revision = '2019-11-06'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(LptsPifib_.Nodes.Node.PuntPolicerStats.ConfigData.Domain.PuntType, self).__init__()

                                self.yang_name = "punt-type"
                                self.yang_parent_name = "domain"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('punt_name', (YLeaf(YType.str, 'punt-name'), ['str'])),
                                    ('configured', (YLeaf(YType.boolean, 'configured'), ['bool'])),
                                    ('active_cfg_state', (YLeaf(YType.str, 'active-cfg-state'), ['str'])),
                                    ('enabled', (YLeaf(YType.boolean, 'enabled'), ['bool'])),
                                    ('pending', (YLeaf(YType.boolean, 'pending'), ['bool'])),
                                    ('configured_rate', (YLeaf(YType.uint32, 'configured-rate'), ['int'])),
                                    ('operational_rate', (YLeaf(YType.uint32, 'operational-rate'), ['int'])),
                                    ('domain_name', (YLeaf(YType.str, 'domain-name'), ['str'])),
                                    ('domain_index', (YLeaf(YType.uint8, 'domain-index'), ['int'])),
                                    ('accepted', (YLeaf(YType.uint64, 'accepted'), ['int'])),
                                    ('dropped', (YLeaf(YType.uint64, 'dropped'), ['int'])),
                                ])
                                self.punt_name = None
                                self.configured = None
                                self.active_cfg_state = None
                                self.enabled = None
                                self.pending = None
                                self.configured_rate = None
                                self.operational_rate = None
                                self.domain_name = None
                                self.domain_index = None
                                self.accepted = None
                                self.dropped = None
                                self._segment_path = lambda: "punt-type"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(LptsPifib_.Nodes.Node.PuntPolicerStats.ConfigData.Domain.PuntType, ['punt_name', 'configured', 'active_cfg_state', 'enabled', 'pending', 'configured_rate', 'operational_rate', 'domain_name', 'domain_index', 'accepted', 'dropped'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_pre_ifib_oper as meta
                                return meta._meta_table['LptsPifib_.Nodes.Node.PuntPolicerStats.ConfigData.Domain.PuntType']['meta_info']


                        class AppliedConfig(_Entity_):
                            """
                            Applied Policer Data
                            
                            .. attribute:: interface_handle
                            
                            	Interface Handle
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            	**config**\: False
                            
                            .. attribute:: virtual_interface
                            
                            	Interface is Virtual
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: punt_name
                            
                            	Punt Name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: enabled
                            
                            	Is Enabled
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: configured_rate
                            
                            	Configured Policer Rate
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: domain_index
                            
                            	Domain Index
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            .. attribute:: punt_police_program_time
                            
                            	Creation or Update Time
                            	**type**\: str
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'lpts-pre-ifib-oper'
                            _revision = '2019-11-06'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(LptsPifib_.Nodes.Node.PuntPolicerStats.ConfigData.Domain.AppliedConfig, self).__init__()

                                self.yang_name = "applied-config"
                                self.yang_parent_name = "domain"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('interface_handle', (YLeaf(YType.str, 'interface-handle'), ['str'])),
                                    ('virtual_interface', (YLeaf(YType.boolean, 'virtual-interface'), ['bool'])),
                                    ('punt_name', (YLeaf(YType.str, 'punt-name'), ['str'])),
                                    ('enabled', (YLeaf(YType.boolean, 'enabled'), ['bool'])),
                                    ('configured_rate', (YLeaf(YType.uint32, 'configured-rate'), ['int'])),
                                    ('domain_index', (YLeaf(YType.uint8, 'domain-index'), ['int'])),
                                    ('punt_police_program_time', (YLeaf(YType.str, 'punt-police-program-time'), ['str'])),
                                ])
                                self.interface_handle = None
                                self.virtual_interface = None
                                self.punt_name = None
                                self.enabled = None
                                self.configured_rate = None
                                self.domain_index = None
                                self.punt_police_program_time = None
                                self._segment_path = lambda: "applied-config"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(LptsPifib_.Nodes.Node.PuntPolicerStats.ConfigData.Domain.AppliedConfig, ['interface_handle', 'virtual_interface', 'punt_name', 'enabled', 'configured_rate', 'domain_index', 'punt_police_program_time'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_pre_ifib_oper as meta
                                return meta._meta_table['LptsPifib_.Nodes.Node.PuntPolicerStats.ConfigData.Domain.AppliedConfig']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_pre_ifib_oper as meta
                            return meta._meta_table['LptsPifib_.Nodes.Node.PuntPolicerStats.ConfigData.Domain']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_pre_ifib_oper as meta
                        return meta._meta_table['LptsPifib_.Nodes.Node.PuntPolicerStats.ConfigData']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_pre_ifib_oper as meta
                    return meta._meta_table['LptsPifib_.Nodes.Node.PuntPolicerStats']['meta_info']


            class Hardware(_Entity_):
                """
                Hardware specific
                
                .. attribute:: usage_entries
                
                	Usage Table options
                	**type**\:  :py:class:`UsageEntries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib_.Nodes.Node.Hardware.UsageEntries>`
                
                	**config**\: False
                
                .. attribute:: police
                
                	Police details
                	**type**\:  :py:class:`Police <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib_.Nodes.Node.Hardware.Police>`
                
                	**config**\: False
                
                .. attribute:: static_police
                
                	Static Police details
                	**type**\:  :py:class:`StaticPolice <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib_.Nodes.Node.Hardware.StaticPolice>`
                
                	**config**\: False
                
                .. attribute:: bfd
                
                	Bfd details
                	**type**\:  :py:class:`Bfd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib_.Nodes.Node.Hardware.Bfd>`
                
                	**config**\: False
                
                .. attribute:: statistics
                
                	Hardware Entry type
                	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib_.Nodes.Node.Hardware.Statistics>`
                
                	**config**\: False
                
                .. attribute:: index_entries
                
                	Hardware Entry options
                	**type**\:  :py:class:`IndexEntries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib_.Nodes.Node.Hardware.IndexEntries>`
                
                	**config**\: False
                
                

                """

                _prefix = 'platform-pifib-oper'
                _revision = '2016-02-22'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(LptsPifib_.Nodes.Node.Hardware, self).__init__()

                    self.yang_name = "hardware"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("usage-entries", ("usage_entries", LptsPifib_.Nodes.Node.Hardware.UsageEntries)), ("police", ("police", LptsPifib_.Nodes.Node.Hardware.Police)), ("static-police", ("static_police", LptsPifib_.Nodes.Node.Hardware.StaticPolice)), ("bfd", ("bfd", LptsPifib_.Nodes.Node.Hardware.Bfd)), ("statistics", ("statistics", LptsPifib_.Nodes.Node.Hardware.Statistics)), ("index-entries", ("index_entries", LptsPifib_.Nodes.Node.Hardware.IndexEntries))])
                    self._leafs = OrderedDict()

                    self.usage_entries = LptsPifib_.Nodes.Node.Hardware.UsageEntries()
                    self.usage_entries.parent = self
                    self._children_name_map["usage_entries"] = "usage-entries"

                    self.police = LptsPifib_.Nodes.Node.Hardware.Police()
                    self.police.parent = self
                    self._children_name_map["police"] = "police"

                    self.static_police = LptsPifib_.Nodes.Node.Hardware.StaticPolice()
                    self.static_police.parent = self
                    self._children_name_map["static_police"] = "static-police"

                    self.bfd = LptsPifib_.Nodes.Node.Hardware.Bfd()
                    self.bfd.parent = self
                    self._children_name_map["bfd"] = "bfd"

                    self.statistics = LptsPifib_.Nodes.Node.Hardware.Statistics()
                    self.statistics.parent = self
                    self._children_name_map["statistics"] = "statistics"

                    self.index_entries = LptsPifib_.Nodes.Node.Hardware.IndexEntries()
                    self.index_entries.parent = self
                    self._children_name_map["index_entries"] = "index-entries"
                    self._segment_path = lambda: "Cisco-IOS-XR-platform-pifib-oper:hardware"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(LptsPifib_.Nodes.Node.Hardware, [], name, value)


                class UsageEntries(_Entity_):
                    """
                    Usage Table options
                    
                    .. attribute:: usage_entry
                    
                    	Usage details
                    	**type**\: list of  		 :py:class:`UsageEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib_.Nodes.Node.Hardware.UsageEntries.UsageEntry>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'platform-pifib-oper'
                    _revision = '2016-02-22'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(LptsPifib_.Nodes.Node.Hardware.UsageEntries, self).__init__()

                        self.yang_name = "usage-entries"
                        self.yang_parent_name = "hardware"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("usage-entry", ("usage_entry", LptsPifib_.Nodes.Node.Hardware.UsageEntries.UsageEntry))])
                        self._leafs = OrderedDict()

                        self.usage_entry = YList(self)
                        self._segment_path = lambda: "usage-entries"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(LptsPifib_.Nodes.Node.Hardware.UsageEntries, [], name, value)


                    class UsageEntry(_Entity_):
                        """
                        Usage details
                        
                        .. attribute:: region_id  (key)
                        
                        	Region ID
                        	**type**\:  :py:class:`UsageAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_platform_pifib_oper.UsageAddressFamily>`
                        
                        	**config**\: False
                        
                        .. attribute:: usage_info
                        
                        	Per TCAM type usage info
                        	**type**\: list of  		 :py:class:`UsageInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib_.Nodes.Node.Hardware.UsageEntries.UsageEntry.UsageInfo>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'platform-pifib-oper'
                        _revision = '2016-02-22'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(LptsPifib_.Nodes.Node.Hardware.UsageEntries.UsageEntry, self).__init__()

                            self.yang_name = "usage-entry"
                            self.yang_parent_name = "usage-entries"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['region_id']
                            self._child_classes = OrderedDict([("usage-info", ("usage_info", LptsPifib_.Nodes.Node.Hardware.UsageEntries.UsageEntry.UsageInfo))])
                            self._leafs = OrderedDict([
                                ('region_id', (YLeaf(YType.enumeration, 'region-id'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_platform_pifib_oper', 'UsageAddressFamily', '')])),
                            ])
                            self.region_id = None

                            self.usage_info = YList(self)
                            self._segment_path = lambda: "usage-entry" + "[region-id='" + str(self.region_id) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(LptsPifib_.Nodes.Node.Hardware.UsageEntries.UsageEntry, ['region_id'], name, value)


                        class UsageInfo(_Entity_):
                            """
                            Per TCAM type usage info
                            
                            .. attribute:: pipe_id
                            
                            	Pipe ID
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            .. attribute:: region
                            
                            	Region Type
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            .. attribute:: region_id
                            
                            	Region ID
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            .. attribute:: size
                            
                            	Maximum Number of Entries in the Region
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: used
                            
                            	Used Number of Entries in the Region
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'platform-pifib-oper'
                            _revision = '2016-02-22'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(LptsPifib_.Nodes.Node.Hardware.UsageEntries.UsageEntry.UsageInfo, self).__init__()

                                self.yang_name = "usage-info"
                                self.yang_parent_name = "usage-entry"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('pipe_id', (YLeaf(YType.uint8, 'pipe-id'), ['int'])),
                                    ('region', (YLeaf(YType.uint8, 'region'), ['int'])),
                                    ('region_id', (YLeaf(YType.uint8, 'region-id'), ['int'])),
                                    ('size', (YLeaf(YType.uint32, 'size'), ['int'])),
                                    ('used', (YLeaf(YType.uint32, 'used'), ['int'])),
                                ])
                                self.pipe_id = None
                                self.region = None
                                self.region_id = None
                                self.size = None
                                self.used = None
                                self._segment_path = lambda: "usage-info"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(LptsPifib_.Nodes.Node.Hardware.UsageEntries.UsageEntry.UsageInfo, ['pipe_id', 'region', 'region_id', 'size', 'used'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_pre_ifib_oper as meta
                                return meta._meta_table['LptsPifib_.Nodes.Node.Hardware.UsageEntries.UsageEntry.UsageInfo']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_pre_ifib_oper as meta
                            return meta._meta_table['LptsPifib_.Nodes.Node.Hardware.UsageEntries.UsageEntry']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_pre_ifib_oper as meta
                        return meta._meta_table['LptsPifib_.Nodes.Node.Hardware.UsageEntries']['meta_info']


                class Police(_Entity_):
                    """
                    Police details
                    
                    .. attribute:: police_info
                    
                    	Per flow type police info
                    	**type**\: list of  		 :py:class:`PoliceInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib_.Nodes.Node.Hardware.Police.PoliceInfo>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'platform-pifib-oper'
                    _revision = '2016-02-22'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(LptsPifib_.Nodes.Node.Hardware.Police, self).__init__()

                        self.yang_name = "police"
                        self.yang_parent_name = "hardware"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("police-info", ("police_info", LptsPifib_.Nodes.Node.Hardware.Police.PoliceInfo))])
                        self._leafs = OrderedDict()

                        self.police_info = YList(self)
                        self._segment_path = lambda: "police"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(LptsPifib_.Nodes.Node.Hardware.Police, [], name, value)


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
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
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
                        
                        .. attribute:: iptos_value
                        
                        	iptos value
                        	**type**\: int
                        
                        	**range:** 0..255
                        
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
                        
                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'platform-pifib-oper'
                        _revision = '2016-02-22'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(LptsPifib_.Nodes.Node.Hardware.Police.PoliceInfo, self).__init__()

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
                                ('avgrate_type', (YLeaf(YType.uint32, 'avgrate-type'), ['int'])),
                                ('accepted_stats', (YLeaf(YType.uint64, 'accepted-stats'), ['int'])),
                                ('dropped_stats', (YLeaf(YType.uint64, 'dropped-stats'), ['int'])),
                                ('policer', (YLeaf(YType.uint32, 'policer'), ['int'])),
                                ('iptos_value', (YLeaf(YType.uint8, 'iptos-value'), ['int'])),
                                ('change_type', (YLeaf(YType.uint8, 'change-type'), ['int'])),
                                ('acl_config', (YLeaf(YType.uint8, 'acl-config'), ['int'])),
                                ('acl_str', (YLeaf(YType.str, 'acl-str'), ['str'])),
                            ])
                            self.avgrate = None
                            self.burst = None
                            self.static_avgrate = None
                            self.avgrate_type = None
                            self.accepted_stats = None
                            self.dropped_stats = None
                            self.policer = None
                            self.iptos_value = None
                            self.change_type = None
                            self.acl_config = None
                            self.acl_str = None
                            self._segment_path = lambda: "police-info"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(LptsPifib_.Nodes.Node.Hardware.Police.PoliceInfo, ['avgrate', 'burst', 'static_avgrate', 'avgrate_type', 'accepted_stats', 'dropped_stats', 'policer', 'iptos_value', 'change_type', 'acl_config', 'acl_str'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_pre_ifib_oper as meta
                            return meta._meta_table['LptsPifib_.Nodes.Node.Hardware.Police.PoliceInfo']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_pre_ifib_oper as meta
                        return meta._meta_table['LptsPifib_.Nodes.Node.Hardware.Police']['meta_info']


                class StaticPolice(_Entity_):
                    """
                    Static Police details
                    
                    .. attribute:: static_info
                    
                    	Per punt reason info
                    	**type**\: list of  		 :py:class:`StaticInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib_.Nodes.Node.Hardware.StaticPolice.StaticInfo>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'platform-pifib-oper'
                    _revision = '2016-02-22'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(LptsPifib_.Nodes.Node.Hardware.StaticPolice, self).__init__()

                        self.yang_name = "static-police"
                        self.yang_parent_name = "hardware"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("static-info", ("static_info", LptsPifib_.Nodes.Node.Hardware.StaticPolice.StaticInfo))])
                        self._leafs = OrderedDict()

                        self.static_info = YList(self)
                        self._segment_path = lambda: "static-police"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(LptsPifib_.Nodes.Node.Hardware.StaticPolice, [], name, value)


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
                        
                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                        
                        	**config**\: False
                        
                        .. attribute:: change_type
                        
                        	change type
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'platform-pifib-oper'
                        _revision = '2016-02-22'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(LptsPifib_.Nodes.Node.Hardware.StaticPolice.StaticInfo, self).__init__()

                            self.yang_name = "static-info"
                            self.yang_parent_name = "static-police"
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
                            self._perform_setattr(LptsPifib_.Nodes.Node.Hardware.StaticPolice.StaticInfo, ['punt_reason', 'sid', 'flow_rate', 'burst_rate', 'accepted', 'dropped', 'punt_reason_string', 'change_type'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_pre_ifib_oper as meta
                            return meta._meta_table['LptsPifib_.Nodes.Node.Hardware.StaticPolice.StaticInfo']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_pre_ifib_oper as meta
                        return meta._meta_table['LptsPifib_.Nodes.Node.Hardware.StaticPolice']['meta_info']


                class Bfd(_Entity_):
                    """
                    Bfd details
                    
                    .. attribute:: bfd_entry_info
                    
                    	Per bfd disc entry info
                    	**type**\: list of  		 :py:class:`BfdEntryInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib_.Nodes.Node.Hardware.Bfd.BfdEntryInfo>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'platform-pifib-oper'
                    _revision = '2016-02-22'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(LptsPifib_.Nodes.Node.Hardware.Bfd, self).__init__()

                        self.yang_name = "bfd"
                        self.yang_parent_name = "hardware"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("bfd-entry-info", ("bfd_entry_info", LptsPifib_.Nodes.Node.Hardware.Bfd.BfdEntryInfo))])
                        self._leafs = OrderedDict()

                        self.bfd_entry_info = YList(self)
                        self._segment_path = lambda: "bfd"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(LptsPifib_.Nodes.Node.Hardware.Bfd, [], name, value)


                    class BfdEntryInfo(_Entity_):
                        """
                        Per bfd disc entry info
                        
                        .. attribute:: index
                        
                        	index
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: is_mcast
                        
                        	is mcast
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: fgid_or_vqi
                        
                        	fgid or vqi
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: is_valid
                        
                        	is valid
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: policer_id
                        
                        	policer id
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'platform-pifib-oper'
                        _revision = '2016-02-22'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(LptsPifib_.Nodes.Node.Hardware.Bfd.BfdEntryInfo, self).__init__()

                            self.yang_name = "bfd-entry-info"
                            self.yang_parent_name = "bfd"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('index', (YLeaf(YType.uint8, 'index'), ['int'])),
                                ('is_mcast', (YLeaf(YType.uint8, 'is-mcast'), ['int'])),
                                ('fgid_or_vqi', (YLeaf(YType.uint32, 'fgid-or-vqi'), ['int'])),
                                ('is_valid', (YLeaf(YType.uint8, 'is-valid'), ['int'])),
                                ('policer_id', (YLeaf(YType.uint32, 'policer-id'), ['int'])),
                            ])
                            self.index = None
                            self.is_mcast = None
                            self.fgid_or_vqi = None
                            self.is_valid = None
                            self.policer_id = None
                            self._segment_path = lambda: "bfd-entry-info"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(LptsPifib_.Nodes.Node.Hardware.Bfd.BfdEntryInfo, ['index', 'is_mcast', 'fgid_or_vqi', 'is_valid', 'policer_id'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_pre_ifib_oper as meta
                            return meta._meta_table['LptsPifib_.Nodes.Node.Hardware.Bfd.BfdEntryInfo']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_pre_ifib_oper as meta
                        return meta._meta_table['LptsPifib_.Nodes.Node.Hardware.Bfd']['meta_info']


                class Statistics(_Entity_):
                    """
                    Hardware Entry type
                    
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

                    _prefix = 'platform-pifib-oper'
                    _revision = '2016-02-22'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(LptsPifib_.Nodes.Node.Hardware.Statistics, self).__init__()

                        self.yang_name = "statistics"
                        self.yang_parent_name = "hardware"
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
                        self._segment_path = lambda: "statistics"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(LptsPifib_.Nodes.Node.Hardware.Statistics, ['accepted', 'dropped', 'clear_ts', 'no_stats_mem_err'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_pre_ifib_oper as meta
                        return meta._meta_table['LptsPifib_.Nodes.Node.Hardware.Statistics']['meta_info']


                class IndexEntries(_Entity_):
                    """
                    Hardware Entry options
                    
                    .. attribute:: index_entry
                    
                    	Entry options
                    	**type**\: list of  		 :py:class:`IndexEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib_.Nodes.Node.Hardware.IndexEntries.IndexEntry>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'platform-pifib-oper'
                    _revision = '2016-02-22'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(LptsPifib_.Nodes.Node.Hardware.IndexEntries, self).__init__()

                        self.yang_name = "index-entries"
                        self.yang_parent_name = "hardware"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("index-entry", ("index_entry", LptsPifib_.Nodes.Node.Hardware.IndexEntries.IndexEntry))])
                        self._leafs = OrderedDict()

                        self.index_entry = YList(self)
                        self._segment_path = lambda: "index-entries"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(LptsPifib_.Nodes.Node.Hardware.IndexEntries, [], name, value)


                    class IndexEntry(_Entity_):
                        """
                        Entry options
                        
                        .. attribute:: index  (key)
                        
                        	Index
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: l3protocol
                        
                        	Layer 3 Protocol
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: l4protocol
                        
                        	Layer 4 Protocol
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: intf_handle
                        
                        	Interface Handle
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: intf_name
                        
                        	Interface Name
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: uidb_index
                        
                        	Interface uidb index
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: local_addr
                        
                        	Local IP Address
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: local_prefix_len
                        
                        	Local Prefix Length
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: remote_addr
                        
                        	Remote IP Address
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: remote_prefix_len
                        
                        	Remote Prefix Length
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: vrf_id
                        
                        	VRF ID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: u_value
                        
                        	Remote Port/ICMP Type/IGMP Type
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: u_len
                        
                        	Union Key Length
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: local_port
                        
                        	Local port
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: is_frag
                        
                        	Is Fragment
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: is_syn
                        
                        	Is SYN
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: action
                        
                        	Action
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: action_string
                        
                        	Action String
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: listener_tag
                        
                        	Listener Tag
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: is_fgid
                        
                        	Is FGID or not
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: is_vrf
                        
                        	Is VRF or not
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: is_optimized
                        
                        	Is optimized or not
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: is_uidb_opt_bit
                        
                        	Is uidb set for optimized entry or not
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: fgid_or_sfp
                        
                        	fabric group id or swith fabric port
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: remote_rack
                        
                        	Is entry remote or not
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: rack_id
                        
                        	Remote racknum if remote
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: rslot
                        
                        	Remote slotnum if remote
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: cir
                        
                        	Committed Information Rate
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: flow_type
                        
                        	Flow type
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: priority
                        
                        	Flow priority or COS
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: sid
                        
                        	Stream ID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: policer_avgrate
                        
                        	Policer avg. rate limit
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: policer_burst
                        
                        	Policer burst
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: lookup_priority
                        
                        	Lookup priority
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**config**\: False
                        
                        .. attribute:: storage_priority
                        
                        	Storage priority
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**config**\: False
                        
                        .. attribute:: num_tm_entries
                        
                        	Number of TCAM entries used
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**config**\: False
                        
                        .. attribute:: entry_ptr
                        
                        	ptr to ifib\_entry\_st
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: entry_shadow_ptr
                        
                        	ptr to ifib\_entry\_shadow\_st
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: list_node_ptr
                        
                        	ptr to dlqueue list node
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: state
                        
                        	state of pifib entry
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: retry_fail_cause
                        
                        	failure cause
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: num_retries
                        
                        	retries count
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: min_ttl
                        
                        	Minimum TTL
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: u_type
                        
                        	Union Key Type
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: remote_fgid
                        
                        	Remote FGID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: acl_str
                        
                        	Acl name
                        	**type**\: str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                        
                        	**config**\: False
                        
                        .. attribute:: no_stats
                        
                        	Stats not available
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: hw_info
                        
                        	Per pipe type hardware info
                        	**type**\: list of  		 :py:class:`HwInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib_.Nodes.Node.Hardware.IndexEntries.IndexEntry.HwInfo>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'platform-pifib-oper'
                        _revision = '2016-02-22'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(LptsPifib_.Nodes.Node.Hardware.IndexEntries.IndexEntry, self).__init__()

                            self.yang_name = "index-entry"
                            self.yang_parent_name = "index-entries"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['index']
                            self._child_classes = OrderedDict([("hw-info", ("hw_info", LptsPifib_.Nodes.Node.Hardware.IndexEntries.IndexEntry.HwInfo))])
                            self._leafs = OrderedDict([
                                ('index', (YLeaf(YType.uint32, 'index'), ['int'])),
                                ('l3protocol', (YLeaf(YType.uint32, 'l3protocol'), ['int'])),
                                ('l4protocol', (YLeaf(YType.uint32, 'l4protocol'), ['int'])),
                                ('intf_handle', (YLeaf(YType.uint32, 'intf-handle'), ['int'])),
                                ('intf_name', (YLeaf(YType.str, 'intf-name'), ['str'])),
                                ('uidb_index', (YLeaf(YType.uint32, 'uidb-index'), ['int'])),
                                ('local_addr', (YLeaf(YType.str, 'local-addr'), ['str'])),
                                ('local_prefix_len', (YLeaf(YType.uint32, 'local-prefix-len'), ['int'])),
                                ('remote_addr', (YLeaf(YType.str, 'remote-addr'), ['str'])),
                                ('remote_prefix_len', (YLeaf(YType.uint32, 'remote-prefix-len'), ['int'])),
                                ('vrf_id', (YLeaf(YType.uint32, 'vrf-id'), ['int'])),
                                ('u_value', (YLeaf(YType.uint32, 'u-value'), ['int'])),
                                ('u_len', (YLeaf(YType.uint32, 'u-len'), ['int'])),
                                ('local_port', (YLeaf(YType.uint32, 'local-port'), ['int'])),
                                ('is_frag', (YLeaf(YType.uint8, 'is-frag'), ['int'])),
                                ('is_syn', (YLeaf(YType.uint8, 'is-syn'), ['int'])),
                                ('action', (YLeaf(YType.uint8, 'action'), ['int'])),
                                ('action_string', (YLeaf(YType.str, 'action-string'), ['str'])),
                                ('listener_tag', (YLeaf(YType.uint8, 'listener-tag'), ['int'])),
                                ('is_fgid', (YLeaf(YType.uint8, 'is-fgid'), ['int'])),
                                ('is_vrf', (YLeaf(YType.uint8, 'is-vrf'), ['int'])),
                                ('is_optimized', (YLeaf(YType.uint8, 'is-optimized'), ['int'])),
                                ('is_uidb_opt_bit', (YLeaf(YType.uint8, 'is-uidb-opt-bit'), ['int'])),
                                ('fgid_or_sfp', (YLeaf(YType.uint32, 'fgid-or-sfp'), ['int'])),
                                ('remote_rack', (YLeaf(YType.uint8, 'remote-rack'), ['int'])),
                                ('rack_id', (YLeaf(YType.uint32, 'rack-id'), ['int'])),
                                ('rslot', (YLeaf(YType.uint32, 'rslot'), ['int'])),
                                ('cir', (YLeaf(YType.uint64, 'cir'), ['int'])),
                                ('flow_type', (YLeaf(YType.uint32, 'flow-type'), ['int'])),
                                ('priority', (YLeaf(YType.uint32, 'priority'), ['int'])),
                                ('sid', (YLeaf(YType.uint32, 'sid'), ['int'])),
                                ('policer_avgrate', (YLeaf(YType.uint32, 'policer-avgrate'), ['int'])),
                                ('policer_burst', (YLeaf(YType.uint32, 'policer-burst'), ['int'])),
                                ('lookup_priority', (YLeaf(YType.int32, 'lookup-priority'), ['int'])),
                                ('storage_priority', (YLeaf(YType.int32, 'storage-priority'), ['int'])),
                                ('num_tm_entries', (YLeaf(YType.int32, 'num-tm-entries'), ['int'])),
                                ('entry_ptr', (YLeaf(YType.uint32, 'entry-ptr'), ['int'])),
                                ('entry_shadow_ptr', (YLeaf(YType.uint32, 'entry-shadow-ptr'), ['int'])),
                                ('list_node_ptr', (YLeaf(YType.uint32, 'list-node-ptr'), ['int'])),
                                ('state', (YLeaf(YType.uint8, 'state'), ['int'])),
                                ('retry_fail_cause', (YLeaf(YType.uint8, 'retry-fail-cause'), ['int'])),
                                ('num_retries', (YLeaf(YType.uint8, 'num-retries'), ['int'])),
                                ('min_ttl', (YLeaf(YType.uint8, 'min-ttl'), ['int'])),
                                ('u_type', (YLeaf(YType.uint8, 'u-type'), ['int'])),
                                ('remote_fgid', (YLeaf(YType.uint32, 'remote-fgid'), ['int'])),
                                ('acl_str', (YLeaf(YType.str, 'acl-str'), ['str'])),
                                ('no_stats', (YLeaf(YType.uint8, 'no-stats'), ['int'])),
                            ])
                            self.index = None
                            self.l3protocol = None
                            self.l4protocol = None
                            self.intf_handle = None
                            self.intf_name = None
                            self.uidb_index = None
                            self.local_addr = None
                            self.local_prefix_len = None
                            self.remote_addr = None
                            self.remote_prefix_len = None
                            self.vrf_id = None
                            self.u_value = None
                            self.u_len = None
                            self.local_port = None
                            self.is_frag = None
                            self.is_syn = None
                            self.action = None
                            self.action_string = None
                            self.listener_tag = None
                            self.is_fgid = None
                            self.is_vrf = None
                            self.is_optimized = None
                            self.is_uidb_opt_bit = None
                            self.fgid_or_sfp = None
                            self.remote_rack = None
                            self.rack_id = None
                            self.rslot = None
                            self.cir = None
                            self.flow_type = None
                            self.priority = None
                            self.sid = None
                            self.policer_avgrate = None
                            self.policer_burst = None
                            self.lookup_priority = None
                            self.storage_priority = None
                            self.num_tm_entries = None
                            self.entry_ptr = None
                            self.entry_shadow_ptr = None
                            self.list_node_ptr = None
                            self.state = None
                            self.retry_fail_cause = None
                            self.num_retries = None
                            self.min_ttl = None
                            self.u_type = None
                            self.remote_fgid = None
                            self.acl_str = None
                            self.no_stats = None

                            self.hw_info = YList(self)
                            self._segment_path = lambda: "index-entry" + "[index='" + str(self.index) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(LptsPifib_.Nodes.Node.Hardware.IndexEntries.IndexEntry, ['index', 'l3protocol', 'l4protocol', 'intf_handle', 'intf_name', 'uidb_index', 'local_addr', 'local_prefix_len', 'remote_addr', 'remote_prefix_len', 'vrf_id', 'u_value', 'u_len', 'local_port', 'is_frag', 'is_syn', 'action', 'action_string', 'listener_tag', 'is_fgid', 'is_vrf', 'is_optimized', 'is_uidb_opt_bit', 'fgid_or_sfp', 'remote_rack', 'rack_id', 'rslot', 'cir', 'flow_type', 'priority', 'sid', 'policer_avgrate', 'policer_burst', 'lookup_priority', 'storage_priority', 'num_tm_entries', 'entry_ptr', 'entry_shadow_ptr', 'list_node_ptr', 'state', 'retry_fail_cause', 'num_retries', 'min_ttl', 'u_type', 'remote_fgid', 'acl_str', 'no_stats'], name, value)


                        class HwInfo(_Entity_):
                            """
                            Per pipe type hardware info
                            
                            .. attribute:: policer
                            
                            	Policer Pointer
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: stats_ptr
                            
                            	Stats Pointer
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: accepted
                            
                            	Accepted Packets Counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: dropped
                            
                            	Dropped Packets Counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: sort_start_offset
                            
                            	Relative position in sorting order
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: tm_start_offset
                            
                            	Relative position in TCAM
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'platform-pifib-oper'
                            _revision = '2016-02-22'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(LptsPifib_.Nodes.Node.Hardware.IndexEntries.IndexEntry.HwInfo, self).__init__()

                                self.yang_name = "hw-info"
                                self.yang_parent_name = "index-entry"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('policer', (YLeaf(YType.uint32, 'policer'), ['int'])),
                                    ('stats_ptr', (YLeaf(YType.uint32, 'stats-ptr'), ['int'])),
                                    ('accepted', (YLeaf(YType.uint64, 'accepted'), ['int'])),
                                    ('dropped', (YLeaf(YType.uint64, 'dropped'), ['int'])),
                                    ('sort_start_offset', (YLeaf(YType.int32, 'sort-start-offset'), ['int'])),
                                    ('tm_start_offset', (YLeaf(YType.int32, 'tm-start-offset'), ['int'])),
                                ])
                                self.policer = None
                                self.stats_ptr = None
                                self.accepted = None
                                self.dropped = None
                                self.sort_start_offset = None
                                self.tm_start_offset = None
                                self._segment_path = lambda: "hw-info"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(LptsPifib_.Nodes.Node.Hardware.IndexEntries.IndexEntry.HwInfo, ['policer', 'stats_ptr', 'accepted', 'dropped', 'sort_start_offset', 'tm_start_offset'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_pre_ifib_oper as meta
                                return meta._meta_table['LptsPifib_.Nodes.Node.Hardware.IndexEntries.IndexEntry.HwInfo']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_pre_ifib_oper as meta
                            return meta._meta_table['LptsPifib_.Nodes.Node.Hardware.IndexEntries.IndexEntry']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_pre_ifib_oper as meta
                        return meta._meta_table['LptsPifib_.Nodes.Node.Hardware.IndexEntries']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_pre_ifib_oper as meta
                    return meta._meta_table['LptsPifib_.Nodes.Node.Hardware']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_pre_ifib_oper as meta
                return meta._meta_table['LptsPifib_.Nodes.Node']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_pre_ifib_oper as meta
            return meta._meta_table['LptsPifib_.Nodes']['meta_info']

    def clone_ptr(self):
        self._top_entity = LptsPifib_()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_pre_ifib_oper as meta
        return meta._meta_table['LptsPifib_']['meta_info']


