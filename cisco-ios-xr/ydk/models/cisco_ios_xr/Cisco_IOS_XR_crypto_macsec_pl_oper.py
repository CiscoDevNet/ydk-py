""" Cisco_IOS_XR_crypto_macsec_pl_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR crypto\-macsec\-pl package operational data.

This module contains definitions
for the following management objects\:
  macsec\-platform\: MACSec operational data

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class MacsecCard(Enum):
    """
    MacsecCard

    Macsec card

    .. data:: macsec_none = 0

    	macsec none

    .. data:: macsec_msfpga = 1

    	macsec msfpga

    .. data:: macsec_xlmsfpga = 2

    	macsec xlmsfpga

    .. data:: macsec_apm = 3

    	macsec apm

    """

    macsec_none = Enum.YLeaf(0, "macsec-none")

    macsec_msfpga = Enum.YLeaf(1, "macsec-msfpga")

    macsec_xlmsfpga = Enum.YLeaf(2, "macsec-xlmsfpga")

    macsec_apm = Enum.YLeaf(3, "macsec-apm")



class MacsecPlatform(Entity):
    """
    MACSec operational data
    
    .. attribute:: nodes
    
    	NodeTable for all the nodes
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes>`
    
    

    """

    _prefix = 'crypto-macsec-pl-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(MacsecPlatform, self).__init__()
        self._top_entity = None

        self.yang_name = "macsec-platform"
        self.yang_parent_name = "Cisco-IOS-XR-crypto-macsec-pl-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"nodes" : ("nodes", MacsecPlatform.Nodes)}
        self._child_list_classes = {}

        self.nodes = MacsecPlatform.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")
        self._segment_path = lambda: "Cisco-IOS-XR-crypto-macsec-pl-oper:macsec-platform"


    class Nodes(Entity):
        """
        NodeTable for all the nodes
        
        .. attribute:: node
        
        	Node where macsec interfaces exist
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node>`
        
        

        """

        _prefix = 'crypto-macsec-pl-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(MacsecPlatform.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "macsec-platform"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"node" : ("node", MacsecPlatform.Nodes.Node)}

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-crypto-macsec-pl-oper:macsec-platform/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(MacsecPlatform.Nodes, [], name, value)


        class Node(Entity):
            """
            Node where macsec interfaces exist
            
            .. attribute:: node_name  <key>
            
            	Node
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: interfaces
            
            	Table of Interfaces
            	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces>`
            
            

            """

            _prefix = 'crypto-macsec-pl-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(MacsecPlatform.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"interfaces" : ("interfaces", MacsecPlatform.Nodes.Node.Interfaces)}
                self._child_list_classes = {}

                self.node_name = YLeaf(YType.str, "node-name")

                self.interfaces = MacsecPlatform.Nodes.Node.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"
                self._children_yang_names.add("interfaces")
                self._segment_path = lambda: "node" + "[node-name='" + self.node_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-crypto-macsec-pl-oper:macsec-platform/nodes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MacsecPlatform.Nodes.Node, ['node_name'], name, value)


            class Interfaces(Entity):
                """
                Table of Interfaces
                
                .. attribute:: interface
                
                	Interface Where Macsec is configured
                	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface>`
                
                

                """

                _prefix = 'crypto-macsec-pl-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MacsecPlatform.Nodes.Node.Interfaces, self).__init__()

                    self.yang_name = "interfaces"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"interface" : ("interface", MacsecPlatform.Nodes.Node.Interfaces.Interface)}

                    self.interface = YList(self)
                    self._segment_path = lambda: "interfaces"

                def __setattr__(self, name, value):
                    self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces, [], name, value)


                class Interface(Entity):
                    """
                    Interface Where Macsec is configured
                    
                    .. attribute:: name  <key>
                    
                    	Value
                    	**type**\:  str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
                    .. attribute:: hw_flow_s
                    
                    	Table of Hardware Flows
                    	**type**\:   :py:class:`HwFlowS <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS>`
                    
                    .. attribute:: hw_sas
                    
                    	Table of Hardware SAs
                    	**type**\:   :py:class:`HwSas <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas>`
                    
                    .. attribute:: hw_statistics
                    
                    	The Hardware Statistics
                    	**type**\:   :py:class:`HwStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics>`
                    
                    .. attribute:: sw_statistics
                    
                    	The Software Statistics
                    	**type**\:   :py:class:`SwStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics>`
                    
                    

                    """

                    _prefix = 'crypto-macsec-pl-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(MacsecPlatform.Nodes.Node.Interfaces.Interface, self).__init__()

                        self.yang_name = "interface"
                        self.yang_parent_name = "interfaces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"hw-flow-s" : ("hw_flow_s", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS), "hw-sas" : ("hw_sas", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas), "hw-statistics" : ("hw_statistics", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics), "sw-statistics" : ("sw_statistics", MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics)}
                        self._child_list_classes = {}

                        self.name = YLeaf(YType.str, "name")

                        self.hw_flow_s = MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS()
                        self.hw_flow_s.parent = self
                        self._children_name_map["hw_flow_s"] = "hw-flow-s"
                        self._children_yang_names.add("hw-flow-s")

                        self.hw_sas = MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas()
                        self.hw_sas.parent = self
                        self._children_name_map["hw_sas"] = "hw-sas"
                        self._children_yang_names.add("hw-sas")

                        self.hw_statistics = MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics()
                        self.hw_statistics.parent = self
                        self._children_name_map["hw_statistics"] = "hw-statistics"
                        self._children_yang_names.add("hw-statistics")

                        self.sw_statistics = MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics()
                        self.sw_statistics.parent = self
                        self._children_name_map["sw_statistics"] = "sw-statistics"
                        self._children_yang_names.add("sw-statistics")
                        self._segment_path = lambda: "interface" + "[name='" + self.name.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface, ['name'], name, value)


                    class HwFlowS(Entity):
                        """
                        Table of Hardware Flows
                        
                        .. attribute:: hw_flow
                        
                        	Hardware Flow
                        	**type**\: list of    :py:class:`HwFlow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow>`
                        
                        

                        """

                        _prefix = 'crypto-macsec-pl-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS, self).__init__()

                            self.yang_name = "hw-flow-s"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"hw-flow" : ("hw_flow", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow)}

                            self.hw_flow = YList(self)
                            self._segment_path = lambda: "hw-flow-s"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS, [], name, value)


                        class HwFlow(Entity):
                            """
                            Hardware Flow
                            
                            .. attribute:: flow_id  <key>
                            
                            	FLOW ID
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: ext
                            
                            	ext
                            	**type**\:   :py:class:`Ext <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Ext>`
                            
                            

                            """

                            _prefix = 'crypto-macsec-pl-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow, self).__init__()

                                self.yang_name = "hw-flow"
                                self.yang_parent_name = "hw-flow-s"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"ext" : ("ext", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Ext)}
                                self._child_list_classes = {}

                                self.flow_id = YLeaf(YType.int32, "flow-id")

                                self.ext = MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Ext()
                                self.ext.parent = self
                                self._children_name_map["ext"] = "ext"
                                self._children_yang_names.add("ext")
                                self._segment_path = lambda: "hw-flow" + "[flow-id='" + self.flow_id.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow, ['flow_id'], name, value)


                            class Ext(Entity):
                                """
                                ext
                                
                                .. attribute:: es200_flow
                                
                                	ES200 Flow Information
                                	**type**\:   :py:class:`Es200Flow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Ext.Es200Flow>`
                                
                                .. attribute:: msfpga_flow
                                
                                	MSFPGA Flow Information
                                	**type**\:   :py:class:`MsfpgaFlow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Ext.MsfpgaFlow>`
                                
                                .. attribute:: type
                                
                                	type
                                	**type**\:   :py:class:`MacsecCard <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecCard>`
                                
                                

                                """

                                _prefix = 'crypto-macsec-pl-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Ext, self).__init__()

                                    self.yang_name = "ext"
                                    self.yang_parent_name = "hw-flow"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {"es200-flow" : ("es200_flow", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Ext.Es200Flow), "msfpga-flow" : ("msfpga_flow", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Ext.MsfpgaFlow)}
                                    self._child_list_classes = {}

                                    self.type = YLeaf(YType.enumeration, "type")

                                    self.es200_flow = MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Ext.Es200Flow()
                                    self.es200_flow.parent = self
                                    self._children_name_map["es200_flow"] = "es200-flow"
                                    self._children_yang_names.add("es200-flow")

                                    self.msfpga_flow = MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Ext.MsfpgaFlow()
                                    self.msfpga_flow.parent = self
                                    self._children_name_map["msfpga_flow"] = "msfpga-flow"
                                    self._children_yang_names.add("msfpga-flow")
                                    self._segment_path = lambda: "ext"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Ext, ['type'], name, value)


                                class Es200Flow(Entity):
                                    """
                                    ES200 Flow Information
                                    
                                    .. attribute:: rx_flow
                                    
                                    	Rx Flow Details
                                    	**type**\:   :py:class:`RxFlow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Ext.Es200Flow.RxFlow>`
                                    
                                    .. attribute:: tx_flow
                                    
                                    	Tx Flow Details
                                    	**type**\:   :py:class:`TxFlow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Ext.Es200Flow.TxFlow>`
                                    
                                    

                                    """

                                    _prefix = 'crypto-macsec-pl-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Ext.Es200Flow, self).__init__()

                                        self.yang_name = "es200-flow"
                                        self.yang_parent_name = "ext"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {"rx-flow" : ("rx_flow", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Ext.Es200Flow.RxFlow), "tx-flow" : ("tx_flow", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Ext.Es200Flow.TxFlow)}
                                        self._child_list_classes = {}

                                        self.rx_flow = MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Ext.Es200Flow.RxFlow()
                                        self.rx_flow.parent = self
                                        self._children_name_map["rx_flow"] = "rx-flow"
                                        self._children_yang_names.add("rx-flow")

                                        self.tx_flow = MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Ext.Es200Flow.TxFlow()
                                        self.tx_flow.parent = self
                                        self._children_name_map["tx_flow"] = "tx-flow"
                                        self._children_yang_names.add("tx-flow")
                                        self._segment_path = lambda: "es200-flow"


                                    class RxFlow(Entity):
                                        """
                                        Rx Flow Details
                                        
                                        .. attribute:: drop
                                        
                                        	Drop the packet
                                        	**type**\:  bool
                                        
                                        .. attribute:: ethertype
                                        
                                        	Parsed EtherType to match could be 0 if Ethertype should'nt                              be matched can be 0x88E5 for MACSec tag
                                        	**type**\:  int
                                        
                                        	**range:** 0..65535
                                        
                                        .. attribute:: flow_hits
                                        
                                        	Pkts matching the Flow
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: flow_no
                                        
                                        	Flow Number
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: force_ctrl
                                        
                                        	Force the pkt as control pkt irrepective         of the results of control packet detector
                                        	**type**\:  bool
                                        
                                        .. attribute:: inner_vlan_dei
                                        
                                        	Dei to match for innner Vlan tag
                                        	**type**\:  bool
                                        
                                        .. attribute:: inner_vlan_id
                                        
                                        	VLAN ID for inner tag used when two              VLAN Tags should be matched
                                        	**type**\:  int
                                        
                                        	**range:** 0..65535
                                        
                                        .. attribute:: inner_vlan_user_pri
                                        
                                        	 VLAN User priority for inner tag use            when matching two VLAN tags
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: is_flow_enabled
                                        
                                        	Is Flow Enabled
                                        	**type**\:  bool
                                        
                                        .. attribute:: macda
                                        
                                        	MAC DA
                                        	**type**\:  list of int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: mask_da
                                        
                                        	DA mask
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: mask_ethertype
                                        
                                        	Parsed EtherType mask
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: mask_plain_bits
                                        
                                        	Plain Bits mask
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: match_priority
                                        
                                        	priority for match 0\-15(highest) 
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: mpls1_bos
                                        
                                        	 botton of stack 
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: mpls1_exp
                                        
                                        	 exp 
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: mpls1_label
                                        
                                        	 label 
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: mpls2_bos
                                        
                                        	 botton of stack 
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: mpls2_exp
                                        
                                        	 exp 
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: mpls2_label
                                        
                                        	 label 
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: outer_vlan_dei
                                        
                                        	Dei to match for outer Vlan tag
                                        	**type**\:  bool
                                        
                                        .. attribute:: outer_vlan_id
                                        
                                        	 VLAN ID for outer tag use this when             only one tag should be matched
                                        	**type**\:  int
                                        
                                        	**range:** 0..65535
                                        
                                        .. attribute:: outer_vlan_user_pri
                                        
                                        	VLAN User Priority for outer tag  use            this when only one tag should be matched
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: pbb_bvid
                                        
                                        	 Backbone Vlan id 
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: pbb_dei
                                        
                                        	 dei 
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: pbb_pcp
                                        
                                        	 pcp 
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: pbb_sid
                                        
                                        	 Service Instance id 
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: pkt_type
                                        
                                        	Type of packet. See ethMscCfyEPktType\_e
                                        	**type**\:  str
                                        
                                        .. attribute:: plain_bits
                                        
                                        	Plain bits to compare. Max values\:               untagged pkt \- 40 bits after EthType             1 VLAN tag \- 24 bits after parsed EthType        2 VLAN tags\- 8 bits after parsed EthType         1 MPLS tag \- 32 bits after 1st tag               2 MPLS tags\- 8 bits following after 2nd          or atmost 5th MPLS tag                           PBB \- 16 bits after C\-SA                         PBB with VLAN tag \- 16 bits of VLAN tag 
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: bit
                                        
                                        .. attribute:: plain_bits_size
                                        
                                        	No. of bits used in plainBits
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: psci
                                        
                                        	 SCI to be matched value required for            ingress only, pass NULL for egress
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: tag_num
                                        
                                        	No. of MPLS or VLAN tags See ethMscCfyETagNum\_e 
                                        	**type**\:  str
                                        
                                        .. attribute:: tci
                                        
                                        	value of 'e' in TCI to match (1bit )
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: tci_c
                                        
                                        	value of 'c' in TCI to match (1bit) 
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: tci_chk
                                        
                                        	TCI bits will be checked only when this          bit is enabled. All the values of TCI bits       are mandatory when TCI check is used
                                        	**type**\:  bool
                                        
                                        .. attribute:: tci_e_xr
                                        
                                        	value of 'es' in TCI to match (1bit) 
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: tci_sc
                                        
                                        	value of 'sc' in TCI to match (1bit) 
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: tci_scb
                                        
                                        	value of 'scb' in TCI to match (1bit) 
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: tci_v
                                        
                                        	value of 'v' in TCI to match (1bit) 
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'crypto-macsec-pl-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Ext.Es200Flow.RxFlow, self).__init__()

                                            self.yang_name = "rx-flow"
                                            self.yang_parent_name = "es200-flow"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.drop = YLeaf(YType.boolean, "drop")

                                            self.ethertype = YLeaf(YType.uint16, "ethertype")

                                            self.flow_hits = YLeaf(YType.uint64, "flow-hits")

                                            self.flow_no = YLeaf(YType.uint32, "flow-no")

                                            self.force_ctrl = YLeaf(YType.boolean, "force-ctrl")

                                            self.inner_vlan_dei = YLeaf(YType.boolean, "inner-vlan-dei")

                                            self.inner_vlan_id = YLeaf(YType.uint16, "inner-vlan-id")

                                            self.inner_vlan_user_pri = YLeaf(YType.uint8, "inner-vlan-user-pri")

                                            self.is_flow_enabled = YLeaf(YType.boolean, "is-flow-enabled")

                                            self.macda = YLeafList(YType.uint8, "macda")

                                            self.mask_da = YLeaf(YType.uint64, "mask-da")

                                            self.mask_ethertype = YLeaf(YType.uint32, "mask-ethertype")

                                            self.mask_plain_bits = YLeaf(YType.uint64, "mask-plain-bits")

                                            self.match_priority = YLeaf(YType.uint8, "match-priority")

                                            self.mpls1_bos = YLeaf(YType.uint8, "mpls1-bos")

                                            self.mpls1_exp = YLeaf(YType.uint8, "mpls1-exp")

                                            self.mpls1_label = YLeaf(YType.uint32, "mpls1-label")

                                            self.mpls2_bos = YLeaf(YType.uint8, "mpls2-bos")

                                            self.mpls2_exp = YLeaf(YType.uint8, "mpls2-exp")

                                            self.mpls2_label = YLeaf(YType.uint32, "mpls2-label")

                                            self.outer_vlan_dei = YLeaf(YType.boolean, "outer-vlan-dei")

                                            self.outer_vlan_id = YLeaf(YType.uint16, "outer-vlan-id")

                                            self.outer_vlan_user_pri = YLeaf(YType.uint8, "outer-vlan-user-pri")

                                            self.pbb_bvid = YLeaf(YType.uint32, "pbb-bvid")

                                            self.pbb_dei = YLeaf(YType.uint8, "pbb-dei")

                                            self.pbb_pcp = YLeaf(YType.uint8, "pbb-pcp")

                                            self.pbb_sid = YLeaf(YType.uint32, "pbb-sid")

                                            self.pkt_type = YLeaf(YType.str, "pkt-type")

                                            self.plain_bits = YLeaf(YType.uint64, "plain-bits")

                                            self.plain_bits_size = YLeaf(YType.uint8, "plain-bits-size")

                                            self.psci = YLeaf(YType.uint64, "psci")

                                            self.tag_num = YLeaf(YType.str, "tag-num")

                                            self.tci = YLeaf(YType.uint8, "tci")

                                            self.tci_c = YLeaf(YType.uint8, "tci-c")

                                            self.tci_chk = YLeaf(YType.boolean, "tci-chk")

                                            self.tci_e_xr = YLeaf(YType.uint8, "tci-e-xr")

                                            self.tci_sc = YLeaf(YType.uint8, "tci-sc")

                                            self.tci_scb = YLeaf(YType.uint8, "tci-scb")

                                            self.tci_v = YLeaf(YType.uint8, "tci-v")
                                            self._segment_path = lambda: "rx-flow"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Ext.Es200Flow.RxFlow, ['drop', 'ethertype', 'flow_hits', 'flow_no', 'force_ctrl', 'inner_vlan_dei', 'inner_vlan_id', 'inner_vlan_user_pri', 'is_flow_enabled', 'macda', 'mask_da', 'mask_ethertype', 'mask_plain_bits', 'match_priority', 'mpls1_bos', 'mpls1_exp', 'mpls1_label', 'mpls2_bos', 'mpls2_exp', 'mpls2_label', 'outer_vlan_dei', 'outer_vlan_id', 'outer_vlan_user_pri', 'pbb_bvid', 'pbb_dei', 'pbb_pcp', 'pbb_sid', 'pkt_type', 'plain_bits', 'plain_bits_size', 'psci', 'tag_num', 'tci', 'tci_c', 'tci_chk', 'tci_e_xr', 'tci_sc', 'tci_scb', 'tci_v'], name, value)


                                    class TxFlow(Entity):
                                        """
                                        Tx Flow Details
                                        
                                        .. attribute:: drop
                                        
                                        	Drop the packet
                                        	**type**\:  bool
                                        
                                        .. attribute:: ethertype
                                        
                                        	Parsed EtherType to match could be 0 if Ethertype should'nt                              be matched can be 0x88E5 for MACSec tag
                                        	**type**\:  int
                                        
                                        	**range:** 0..65535
                                        
                                        .. attribute:: flow_hits
                                        
                                        	Pkts matching the Flow
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: flow_no
                                        
                                        	Flow Number
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: force_ctrl
                                        
                                        	Force the pkt as control pkt irrepective         of the results of control packet detector
                                        	**type**\:  bool
                                        
                                        .. attribute:: inner_vlan_dei
                                        
                                        	Dei to match for innner Vlan tag
                                        	**type**\:  bool
                                        
                                        .. attribute:: inner_vlan_id
                                        
                                        	VLAN ID for inner tag used when two              VLAN Tags should be matched
                                        	**type**\:  int
                                        
                                        	**range:** 0..65535
                                        
                                        .. attribute:: inner_vlan_user_pri
                                        
                                        	 VLAN User priority for inner tag use            when matching two VLAN tags
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: is_flow_enabled
                                        
                                        	Is Flow Enabled
                                        	**type**\:  bool
                                        
                                        .. attribute:: macda
                                        
                                        	MAC DA
                                        	**type**\:  list of int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: mask_da
                                        
                                        	DA mask
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: mask_ethertype
                                        
                                        	Parsed EtherType mask
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: mask_plain_bits
                                        
                                        	Plain Bits mask
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: match_priority
                                        
                                        	priority for match 0\-15(highest) 
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: mpls1_bos
                                        
                                        	 botton of stack 
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: mpls1_exp
                                        
                                        	 exp 
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: mpls1_label
                                        
                                        	 label 
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: mpls2_bos
                                        
                                        	 botton of stack 
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: mpls2_exp
                                        
                                        	 exp 
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: mpls2_label
                                        
                                        	 label 
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: outer_vlan_dei
                                        
                                        	Dei to match for outer Vlan tag
                                        	**type**\:  bool
                                        
                                        .. attribute:: outer_vlan_id
                                        
                                        	 VLAN ID for outer tag use this when             only one tag should be matched
                                        	**type**\:  int
                                        
                                        	**range:** 0..65535
                                        
                                        .. attribute:: outer_vlan_user_pri
                                        
                                        	VLAN User Priority for outer tag  use            this when only one tag should be matched
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: pbb_bvid
                                        
                                        	 Backbone Vlan id 
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: pbb_dei
                                        
                                        	 dei 
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: pbb_pcp
                                        
                                        	 pcp 
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: pbb_sid
                                        
                                        	 Service Instance id 
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: pkt_type
                                        
                                        	Type of packet. See ethMscCfyEPktType\_e
                                        	**type**\:  str
                                        
                                        .. attribute:: plain_bits
                                        
                                        	Plain bits to compare. Max values\:               untagged pkt \- 40 bits after EthType             1 VLAN tag \- 24 bits after parsed EthType        2 VLAN tags\- 8 bits after parsed EthType         1 MPLS tag \- 32 bits after 1st tag               2 MPLS tags\- 8 bits following after 2nd          or atmost 5th MPLS tag                           PBB \- 16 bits after C\-SA                         PBB with VLAN tag \- 16 bits of VLAN tag 
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: bit
                                        
                                        .. attribute:: plain_bits_size
                                        
                                        	No. of bits used in plainBits
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: psci
                                        
                                        	 SCI to be matched value required for            ingress only, pass NULL for egress
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: tag_num
                                        
                                        	No. of MPLS or VLAN tags See ethMscCfyETagNum\_e 
                                        	**type**\:  str
                                        
                                        .. attribute:: tci
                                        
                                        	value of 'e' in TCI to match (1bit )
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: tci_c
                                        
                                        	value of 'c' in TCI to match (1bit) 
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: tci_chk
                                        
                                        	TCI bits will be checked only when this          bit is enabled. All the values of TCI bits       are mandatory when TCI check is used
                                        	**type**\:  bool
                                        
                                        .. attribute:: tci_e_xr
                                        
                                        	value of 'es' in TCI to match (1bit) 
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: tci_sc
                                        
                                        	value of 'sc' in TCI to match (1bit) 
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: tci_scb
                                        
                                        	value of 'scb' in TCI to match (1bit) 
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: tci_v
                                        
                                        	value of 'v' in TCI to match (1bit) 
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'crypto-macsec-pl-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Ext.Es200Flow.TxFlow, self).__init__()

                                            self.yang_name = "tx-flow"
                                            self.yang_parent_name = "es200-flow"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.drop = YLeaf(YType.boolean, "drop")

                                            self.ethertype = YLeaf(YType.uint16, "ethertype")

                                            self.flow_hits = YLeaf(YType.uint64, "flow-hits")

                                            self.flow_no = YLeaf(YType.uint32, "flow-no")

                                            self.force_ctrl = YLeaf(YType.boolean, "force-ctrl")

                                            self.inner_vlan_dei = YLeaf(YType.boolean, "inner-vlan-dei")

                                            self.inner_vlan_id = YLeaf(YType.uint16, "inner-vlan-id")

                                            self.inner_vlan_user_pri = YLeaf(YType.uint8, "inner-vlan-user-pri")

                                            self.is_flow_enabled = YLeaf(YType.boolean, "is-flow-enabled")

                                            self.macda = YLeafList(YType.uint8, "macda")

                                            self.mask_da = YLeaf(YType.uint64, "mask-da")

                                            self.mask_ethertype = YLeaf(YType.uint32, "mask-ethertype")

                                            self.mask_plain_bits = YLeaf(YType.uint64, "mask-plain-bits")

                                            self.match_priority = YLeaf(YType.uint8, "match-priority")

                                            self.mpls1_bos = YLeaf(YType.uint8, "mpls1-bos")

                                            self.mpls1_exp = YLeaf(YType.uint8, "mpls1-exp")

                                            self.mpls1_label = YLeaf(YType.uint32, "mpls1-label")

                                            self.mpls2_bos = YLeaf(YType.uint8, "mpls2-bos")

                                            self.mpls2_exp = YLeaf(YType.uint8, "mpls2-exp")

                                            self.mpls2_label = YLeaf(YType.uint32, "mpls2-label")

                                            self.outer_vlan_dei = YLeaf(YType.boolean, "outer-vlan-dei")

                                            self.outer_vlan_id = YLeaf(YType.uint16, "outer-vlan-id")

                                            self.outer_vlan_user_pri = YLeaf(YType.uint8, "outer-vlan-user-pri")

                                            self.pbb_bvid = YLeaf(YType.uint32, "pbb-bvid")

                                            self.pbb_dei = YLeaf(YType.uint8, "pbb-dei")

                                            self.pbb_pcp = YLeaf(YType.uint8, "pbb-pcp")

                                            self.pbb_sid = YLeaf(YType.uint32, "pbb-sid")

                                            self.pkt_type = YLeaf(YType.str, "pkt-type")

                                            self.plain_bits = YLeaf(YType.uint64, "plain-bits")

                                            self.plain_bits_size = YLeaf(YType.uint8, "plain-bits-size")

                                            self.psci = YLeaf(YType.uint64, "psci")

                                            self.tag_num = YLeaf(YType.str, "tag-num")

                                            self.tci = YLeaf(YType.uint8, "tci")

                                            self.tci_c = YLeaf(YType.uint8, "tci-c")

                                            self.tci_chk = YLeaf(YType.boolean, "tci-chk")

                                            self.tci_e_xr = YLeaf(YType.uint8, "tci-e-xr")

                                            self.tci_sc = YLeaf(YType.uint8, "tci-sc")

                                            self.tci_scb = YLeaf(YType.uint8, "tci-scb")

                                            self.tci_v = YLeaf(YType.uint8, "tci-v")
                                            self._segment_path = lambda: "tx-flow"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Ext.Es200Flow.TxFlow, ['drop', 'ethertype', 'flow_hits', 'flow_no', 'force_ctrl', 'inner_vlan_dei', 'inner_vlan_id', 'inner_vlan_user_pri', 'is_flow_enabled', 'macda', 'mask_da', 'mask_ethertype', 'mask_plain_bits', 'match_priority', 'mpls1_bos', 'mpls1_exp', 'mpls1_label', 'mpls2_bos', 'mpls2_exp', 'mpls2_label', 'outer_vlan_dei', 'outer_vlan_id', 'outer_vlan_user_pri', 'pbb_bvid', 'pbb_dei', 'pbb_pcp', 'pbb_sid', 'pkt_type', 'plain_bits', 'plain_bits_size', 'psci', 'tag_num', 'tci', 'tci_c', 'tci_chk', 'tci_e_xr', 'tci_sc', 'tci_scb', 'tci_v'], name, value)


                                class MsfpgaFlow(Entity):
                                    """
                                    MSFPGA Flow Information
                                    
                                    .. attribute:: rx_flow
                                    
                                    	Rx Flow Details
                                    	**type**\:   :py:class:`RxFlow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Ext.MsfpgaFlow.RxFlow>`
                                    
                                    .. attribute:: tx_flow
                                    
                                    	Tx Flow Details
                                    	**type**\:   :py:class:`TxFlow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Ext.MsfpgaFlow.TxFlow>`
                                    
                                    

                                    """

                                    _prefix = 'crypto-macsec-pl-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Ext.MsfpgaFlow, self).__init__()

                                        self.yang_name = "msfpga-flow"
                                        self.yang_parent_name = "ext"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {"rx-flow" : ("rx_flow", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Ext.MsfpgaFlow.RxFlow), "tx-flow" : ("tx_flow", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Ext.MsfpgaFlow.TxFlow)}
                                        self._child_list_classes = {}

                                        self.rx_flow = MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Ext.MsfpgaFlow.RxFlow()
                                        self.rx_flow.parent = self
                                        self._children_name_map["rx_flow"] = "rx-flow"
                                        self._children_yang_names.add("rx-flow")

                                        self.tx_flow = MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Ext.MsfpgaFlow.TxFlow()
                                        self.tx_flow.parent = self
                                        self._children_name_map["tx_flow"] = "tx-flow"
                                        self._children_yang_names.add("tx-flow")
                                        self._segment_path = lambda: "msfpga-flow"


                                    class RxFlow(Entity):
                                        """
                                        Rx Flow Details
                                        
                                        .. attribute:: action
                                        
                                        	Action
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: ctrl_check
                                        
                                        	Ctrl Pkt ChkEn
                                        	**type**\:  bool
                                        
                                        .. attribute:: dmac_inuse
                                        
                                        	If MAC DA in Use
                                        	**type**\:  bool
                                        
                                        .. attribute:: ethertype
                                        
                                        	Ether Type
                                        	**type**\:  int
                                        
                                        	**range:** 0..65535
                                        
                                        .. attribute:: flow_id
                                        
                                        	Flow Index
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: in_use
                                        
                                        	In Use
                                        	**type**\:  bool
                                        
                                        .. attribute:: inner_vlan
                                        
                                        	Inner VLAN ID
                                        	**type**\:  int
                                        
                                        	**range:** 0..65535
                                        
                                        .. attribute:: inner_vlan_tpid
                                        
                                        	Inner Vlan TPID
                                        	**type**\:  int
                                        
                                        	**range:** 0..65535
                                        
                                        .. attribute:: inner_vlan_up
                                        
                                        	Inner Vlan UserPri
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: is_ctrl_pkt
                                        
                                        	Is Control Pkt
                                        	**type**\:  bool
                                        
                                        .. attribute:: is_egress
                                        
                                        	rx\_tx direction
                                        	**type**\:  bool
                                        
                                        .. attribute:: macda
                                        
                                        	MAC DA
                                        	**type**\:  list of int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: macsa
                                        
                                        	MAC SA
                                        	**type**\:  list of int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: match_bad_tag
                                        
                                        	Match Bad Tag
                                        	**type**\:  bool
                                        
                                        .. attribute:: match_kay_tag
                                        
                                        	MatchKaYTag
                                        	**type**\:  bool
                                        
                                        .. attribute:: match_pri
                                        
                                        	Match Priority
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: match_tagged
                                        
                                        	MatchTagged
                                        	**type**\:  bool
                                        
                                        .. attribute:: match_untagged
                                        
                                        	MatchUntagged
                                        	**type**\:  bool
                                        
                                        .. attribute:: outer_vlan
                                        
                                        	Outer VLAN ID
                                        	**type**\:  int
                                        
                                        	**range:** 0..65535
                                        
                                        .. attribute:: outer_vlan_tpid
                                        
                                        	Outer Vlan TPID
                                        	**type**\:  int
                                        
                                        	**range:** 0..65535
                                        
                                        .. attribute:: outer_vlan_up
                                        
                                        	Outer Vlan UserPri
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: sai
                                        
                                        	SAI
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: sci
                                        
                                        	SCI
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: sci_inuse
                                        
                                        	If SCI in use
                                        	**type**\:  bool
                                        
                                        .. attribute:: smac_inuse
                                        
                                        	If MAC SA in Use
                                        	**type**\:  bool
                                        
                                        .. attribute:: source_port
                                        
                                        	Source Port
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: source_port_chk
                                        
                                        	Source Port ChkEn
                                        	**type**\:  bool
                                        
                                        .. attribute:: tci
                                        
                                        	TCI E
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: tci_an
                                        
                                        	TCI AN
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: tci_an_chk
                                        
                                        	TciAnChkEn
                                        	**type**\:  bool
                                        
                                        .. attribute:: tci_c
                                        
                                        	TCI C
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: tci_chk
                                        
                                        	TciChkEn
                                        	**type**\:  bool
                                        
                                        .. attribute:: tci_e_xr
                                        
                                        	TCI ES
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: tci_sc
                                        
                                        	TCI SC
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: tci_scb
                                        
                                        	TCI SCB
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: tci_v
                                        
                                        	TCI V
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: valid
                                        
                                        	Flow Validity
                                        	**type**\:  bool
                                        
                                        

                                        """

                                        _prefix = 'crypto-macsec-pl-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Ext.MsfpgaFlow.RxFlow, self).__init__()

                                            self.yang_name = "rx-flow"
                                            self.yang_parent_name = "msfpga-flow"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.action = YLeaf(YType.uint8, "action")

                                            self.ctrl_check = YLeaf(YType.boolean, "ctrl-check")

                                            self.dmac_inuse = YLeaf(YType.boolean, "dmac-inuse")

                                            self.ethertype = YLeaf(YType.uint16, "ethertype")

                                            self.flow_id = YLeaf(YType.uint8, "flow-id")

                                            self.in_use = YLeaf(YType.boolean, "in-use")

                                            self.inner_vlan = YLeaf(YType.uint16, "inner-vlan")

                                            self.inner_vlan_tpid = YLeaf(YType.uint16, "inner-vlan-tpid")

                                            self.inner_vlan_up = YLeaf(YType.uint8, "inner-vlan-up")

                                            self.is_ctrl_pkt = YLeaf(YType.boolean, "is-ctrl-pkt")

                                            self.is_egress = YLeaf(YType.boolean, "is-egress")

                                            self.macda = YLeafList(YType.uint8, "macda")

                                            self.macsa = YLeafList(YType.uint8, "macsa")

                                            self.match_bad_tag = YLeaf(YType.boolean, "match-bad-tag")

                                            self.match_kay_tag = YLeaf(YType.boolean, "match-kay-tag")

                                            self.match_pri = YLeaf(YType.uint8, "match-pri")

                                            self.match_tagged = YLeaf(YType.boolean, "match-tagged")

                                            self.match_untagged = YLeaf(YType.boolean, "match-untagged")

                                            self.outer_vlan = YLeaf(YType.uint16, "outer-vlan")

                                            self.outer_vlan_tpid = YLeaf(YType.uint16, "outer-vlan-tpid")

                                            self.outer_vlan_up = YLeaf(YType.uint8, "outer-vlan-up")

                                            self.sai = YLeaf(YType.uint32, "sai")

                                            self.sci = YLeaf(YType.uint64, "sci")

                                            self.sci_inuse = YLeaf(YType.boolean, "sci-inuse")

                                            self.smac_inuse = YLeaf(YType.boolean, "smac-inuse")

                                            self.source_port = YLeaf(YType.uint32, "source-port")

                                            self.source_port_chk = YLeaf(YType.boolean, "source-port-chk")

                                            self.tci = YLeaf(YType.uint8, "tci")

                                            self.tci_an = YLeaf(YType.uint8, "tci-an")

                                            self.tci_an_chk = YLeaf(YType.boolean, "tci-an-chk")

                                            self.tci_c = YLeaf(YType.uint8, "tci-c")

                                            self.tci_chk = YLeaf(YType.boolean, "tci-chk")

                                            self.tci_e_xr = YLeaf(YType.uint8, "tci-e-xr")

                                            self.tci_sc = YLeaf(YType.uint8, "tci-sc")

                                            self.tci_scb = YLeaf(YType.uint8, "tci-scb")

                                            self.tci_v = YLeaf(YType.uint8, "tci-v")

                                            self.valid = YLeaf(YType.boolean, "valid")
                                            self._segment_path = lambda: "rx-flow"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Ext.MsfpgaFlow.RxFlow, ['action', 'ctrl_check', 'dmac_inuse', 'ethertype', 'flow_id', 'in_use', 'inner_vlan', 'inner_vlan_tpid', 'inner_vlan_up', 'is_ctrl_pkt', 'is_egress', 'macda', 'macsa', 'match_bad_tag', 'match_kay_tag', 'match_pri', 'match_tagged', 'match_untagged', 'outer_vlan', 'outer_vlan_tpid', 'outer_vlan_up', 'sai', 'sci', 'sci_inuse', 'smac_inuse', 'source_port', 'source_port_chk', 'tci', 'tci_an', 'tci_an_chk', 'tci_c', 'tci_chk', 'tci_e_xr', 'tci_sc', 'tci_scb', 'tci_v', 'valid'], name, value)


                                    class TxFlow(Entity):
                                        """
                                        Tx Flow Details
                                        
                                        .. attribute:: action
                                        
                                        	Action
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: ctrl_check
                                        
                                        	Ctrl Pkt ChkEn
                                        	**type**\:  bool
                                        
                                        .. attribute:: dmac_inuse
                                        
                                        	If MAC DA in Use
                                        	**type**\:  bool
                                        
                                        .. attribute:: ethertype
                                        
                                        	Ether Type
                                        	**type**\:  int
                                        
                                        	**range:** 0..65535
                                        
                                        .. attribute:: flow_id
                                        
                                        	Flow Index
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: in_use
                                        
                                        	In Use
                                        	**type**\:  bool
                                        
                                        .. attribute:: inner_vlan
                                        
                                        	Inner VLAN ID
                                        	**type**\:  int
                                        
                                        	**range:** 0..65535
                                        
                                        .. attribute:: inner_vlan_tpid
                                        
                                        	Inner Vlan TPID
                                        	**type**\:  int
                                        
                                        	**range:** 0..65535
                                        
                                        .. attribute:: inner_vlan_up
                                        
                                        	Inner Vlan UserPri
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: is_ctrl_pkt
                                        
                                        	Is Control Pkt
                                        	**type**\:  bool
                                        
                                        .. attribute:: is_egress
                                        
                                        	rx\_tx direction
                                        	**type**\:  bool
                                        
                                        .. attribute:: macda
                                        
                                        	MAC DA
                                        	**type**\:  list of int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: macsa
                                        
                                        	MAC SA
                                        	**type**\:  list of int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: match_bad_tag
                                        
                                        	Match Bad Tag
                                        	**type**\:  bool
                                        
                                        .. attribute:: match_kay_tag
                                        
                                        	MatchKaYTag
                                        	**type**\:  bool
                                        
                                        .. attribute:: match_pri
                                        
                                        	Match Priority
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: match_tagged
                                        
                                        	MatchTagged
                                        	**type**\:  bool
                                        
                                        .. attribute:: match_untagged
                                        
                                        	MatchUntagged
                                        	**type**\:  bool
                                        
                                        .. attribute:: outer_vlan
                                        
                                        	Outer VLAN ID
                                        	**type**\:  int
                                        
                                        	**range:** 0..65535
                                        
                                        .. attribute:: outer_vlan_tpid
                                        
                                        	Outer Vlan TPID
                                        	**type**\:  int
                                        
                                        	**range:** 0..65535
                                        
                                        .. attribute:: outer_vlan_up
                                        
                                        	Outer Vlan UserPri
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: sai
                                        
                                        	SAI
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: sci
                                        
                                        	SCI
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: sci_inuse
                                        
                                        	If SCI in use
                                        	**type**\:  bool
                                        
                                        .. attribute:: smac_inuse
                                        
                                        	If MAC SA in Use
                                        	**type**\:  bool
                                        
                                        .. attribute:: source_port
                                        
                                        	Source Port
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: source_port_chk
                                        
                                        	Source Port ChkEn
                                        	**type**\:  bool
                                        
                                        .. attribute:: tci
                                        
                                        	TCI E
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: tci_an
                                        
                                        	TCI AN
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: tci_an_chk
                                        
                                        	TciAnChkEn
                                        	**type**\:  bool
                                        
                                        .. attribute:: tci_c
                                        
                                        	TCI C
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: tci_chk
                                        
                                        	TciChkEn
                                        	**type**\:  bool
                                        
                                        .. attribute:: tci_e_xr
                                        
                                        	TCI ES
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: tci_sc
                                        
                                        	TCI SC
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: tci_scb
                                        
                                        	TCI SCB
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: tci_v
                                        
                                        	TCI V
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: valid
                                        
                                        	Flow Validity
                                        	**type**\:  bool
                                        
                                        

                                        """

                                        _prefix = 'crypto-macsec-pl-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Ext.MsfpgaFlow.TxFlow, self).__init__()

                                            self.yang_name = "tx-flow"
                                            self.yang_parent_name = "msfpga-flow"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.action = YLeaf(YType.uint8, "action")

                                            self.ctrl_check = YLeaf(YType.boolean, "ctrl-check")

                                            self.dmac_inuse = YLeaf(YType.boolean, "dmac-inuse")

                                            self.ethertype = YLeaf(YType.uint16, "ethertype")

                                            self.flow_id = YLeaf(YType.uint8, "flow-id")

                                            self.in_use = YLeaf(YType.boolean, "in-use")

                                            self.inner_vlan = YLeaf(YType.uint16, "inner-vlan")

                                            self.inner_vlan_tpid = YLeaf(YType.uint16, "inner-vlan-tpid")

                                            self.inner_vlan_up = YLeaf(YType.uint8, "inner-vlan-up")

                                            self.is_ctrl_pkt = YLeaf(YType.boolean, "is-ctrl-pkt")

                                            self.is_egress = YLeaf(YType.boolean, "is-egress")

                                            self.macda = YLeafList(YType.uint8, "macda")

                                            self.macsa = YLeafList(YType.uint8, "macsa")

                                            self.match_bad_tag = YLeaf(YType.boolean, "match-bad-tag")

                                            self.match_kay_tag = YLeaf(YType.boolean, "match-kay-tag")

                                            self.match_pri = YLeaf(YType.uint8, "match-pri")

                                            self.match_tagged = YLeaf(YType.boolean, "match-tagged")

                                            self.match_untagged = YLeaf(YType.boolean, "match-untagged")

                                            self.outer_vlan = YLeaf(YType.uint16, "outer-vlan")

                                            self.outer_vlan_tpid = YLeaf(YType.uint16, "outer-vlan-tpid")

                                            self.outer_vlan_up = YLeaf(YType.uint8, "outer-vlan-up")

                                            self.sai = YLeaf(YType.uint32, "sai")

                                            self.sci = YLeaf(YType.uint64, "sci")

                                            self.sci_inuse = YLeaf(YType.boolean, "sci-inuse")

                                            self.smac_inuse = YLeaf(YType.boolean, "smac-inuse")

                                            self.source_port = YLeaf(YType.uint32, "source-port")

                                            self.source_port_chk = YLeaf(YType.boolean, "source-port-chk")

                                            self.tci = YLeaf(YType.uint8, "tci")

                                            self.tci_an = YLeaf(YType.uint8, "tci-an")

                                            self.tci_an_chk = YLeaf(YType.boolean, "tci-an-chk")

                                            self.tci_c = YLeaf(YType.uint8, "tci-c")

                                            self.tci_chk = YLeaf(YType.boolean, "tci-chk")

                                            self.tci_e_xr = YLeaf(YType.uint8, "tci-e-xr")

                                            self.tci_sc = YLeaf(YType.uint8, "tci-sc")

                                            self.tci_scb = YLeaf(YType.uint8, "tci-scb")

                                            self.tci_v = YLeaf(YType.uint8, "tci-v")

                                            self.valid = YLeaf(YType.boolean, "valid")
                                            self._segment_path = lambda: "tx-flow"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Ext.MsfpgaFlow.TxFlow, ['action', 'ctrl_check', 'dmac_inuse', 'ethertype', 'flow_id', 'in_use', 'inner_vlan', 'inner_vlan_tpid', 'inner_vlan_up', 'is_ctrl_pkt', 'is_egress', 'macda', 'macsa', 'match_bad_tag', 'match_kay_tag', 'match_pri', 'match_tagged', 'match_untagged', 'outer_vlan', 'outer_vlan_tpid', 'outer_vlan_up', 'sai', 'sci', 'sci_inuse', 'smac_inuse', 'source_port', 'source_port_chk', 'tci', 'tci_an', 'tci_an_chk', 'tci_c', 'tci_chk', 'tci_e_xr', 'tci_sc', 'tci_scb', 'tci_v', 'valid'], name, value)


                    class HwSas(Entity):
                        """
                        Table of Hardware SAs
                        
                        .. attribute:: hw_sa
                        
                        	Hardware Security Association
                        	**type**\: list of    :py:class:`HwSa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa>`
                        
                        

                        """

                        _prefix = 'crypto-macsec-pl-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas, self).__init__()

                            self.yang_name = "hw-sas"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"hw-sa" : ("hw_sa", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa)}

                            self.hw_sa = YList(self)
                            self._segment_path = lambda: "hw-sas"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas, [], name, value)


                        class HwSa(Entity):
                            """
                            Hardware Security Association
                            
                            .. attribute:: sa_id  <key>
                            
                            	SA ID
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: ext
                            
                            	ext
                            	**type**\:   :py:class:`Ext <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext>`
                            
                            

                            """

                            _prefix = 'crypto-macsec-pl-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa, self).__init__()

                                self.yang_name = "hw-sa"
                                self.yang_parent_name = "hw-sas"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"ext" : ("ext", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext)}
                                self._child_list_classes = {}

                                self.sa_id = YLeaf(YType.int32, "sa-id")

                                self.ext = MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext()
                                self.ext.parent = self
                                self._children_name_map["ext"] = "ext"
                                self._children_yang_names.add("ext")
                                self._segment_path = lambda: "hw-sa" + "[sa-id='" + self.sa_id.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa, ['sa_id'], name, value)


                            class Ext(Entity):
                                """
                                ext
                                
                                .. attribute:: es200_sa
                                
                                	ES200 SA Information
                                	**type**\:   :py:class:`Es200Sa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.Es200Sa>`
                                
                                .. attribute:: msfpga_sa
                                
                                	MSFPGA SA Information
                                	**type**\:   :py:class:`MsfpgaSa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.MsfpgaSa>`
                                
                                .. attribute:: type
                                
                                	type
                                	**type**\:   :py:class:`MacsecCard <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecCard>`
                                
                                .. attribute:: xlfpga_sa
                                
                                	XLFPGA SA Information
                                	**type**\:   :py:class:`XlfpgaSa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.XlfpgaSa>`
                                
                                

                                """

                                _prefix = 'crypto-macsec-pl-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext, self).__init__()

                                    self.yang_name = "ext"
                                    self.yang_parent_name = "hw-sa"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {"es200-sa" : ("es200_sa", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.Es200Sa), "msfpga-sa" : ("msfpga_sa", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.MsfpgaSa), "xlfpga-sa" : ("xlfpga_sa", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.XlfpgaSa)}
                                    self._child_list_classes = {}

                                    self.type = YLeaf(YType.enumeration, "type")

                                    self.es200_sa = MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.Es200Sa()
                                    self.es200_sa.parent = self
                                    self._children_name_map["es200_sa"] = "es200-sa"
                                    self._children_yang_names.add("es200-sa")

                                    self.msfpga_sa = MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.MsfpgaSa()
                                    self.msfpga_sa.parent = self
                                    self._children_name_map["msfpga_sa"] = "msfpga-sa"
                                    self._children_yang_names.add("msfpga-sa")

                                    self.xlfpga_sa = MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.XlfpgaSa()
                                    self.xlfpga_sa.parent = self
                                    self._children_name_map["xlfpga_sa"] = "xlfpga-sa"
                                    self._children_yang_names.add("xlfpga-sa")
                                    self._segment_path = lambda: "ext"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext, ['type'], name, value)


                                class Es200Sa(Entity):
                                    """
                                    ES200 SA Information
                                    
                                    .. attribute:: rx_sa
                                    
                                    	Rx SA Details
                                    	**type**\: list of    :py:class:`RxSa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.Es200Sa.RxSa>`
                                    
                                    .. attribute:: tx_sa
                                    
                                    	Tx SA Details
                                    	**type**\:   :py:class:`TxSa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.Es200Sa.TxSa>`
                                    
                                    

                                    """

                                    _prefix = 'crypto-macsec-pl-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.Es200Sa, self).__init__()

                                        self.yang_name = "es200-sa"
                                        self.yang_parent_name = "ext"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {"tx-sa" : ("tx_sa", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.Es200Sa.TxSa)}
                                        self._child_list_classes = {"rx-sa" : ("rx_sa", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.Es200Sa.RxSa)}

                                        self.tx_sa = MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.Es200Sa.TxSa()
                                        self.tx_sa.parent = self
                                        self._children_name_map["tx_sa"] = "tx-sa"
                                        self._children_yang_names.add("tx-sa")

                                        self.rx_sa = YList(self)
                                        self._segment_path = lambda: "es200-sa"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.Es200Sa, [], name, value)


                                    class RxSa(Entity):
                                        """
                                        Rx SA Details
                                        
                                        .. attribute:: in_octets_decrypted_validated1
                                        
                                        	octets1 decrypted/validated
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: in_octets_validated
                                        
                                        	octets validated
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: in_pkts_delayed
                                        
                                        	PN of packet outside replay window & validateFrames !strict
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: in_pkts_invalid
                                        
                                        	packet not valid & validateFrames !strict
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: in_pkts_late
                                        
                                        	PN of packet outside replay window & validateFrames strict
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: in_pkts_not_using_sa
                                        
                                        	packet assigned to SA not in use & validateFrames strict
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: in_pkts_not_valid
                                        
                                        	packet not valid & validateFrames strict
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: in_pkts_ok
                                        
                                        	packets with no error
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: in_pkts_unchecked
                                        
                                        	frame not valid & validateFrames disabled
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: in_pkts_unused_sa
                                        
                                        	packet assigned to SA not in use& validateFrames !strict
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: is_valid
                                        
                                        	Is structure valid
                                        	**type**\:  bool
                                        
                                        .. attribute:: sa_id
                                        
                                        	SA Index
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: sc_no
                                        
                                        	SC Number
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: xform_params
                                        
                                        	 Xform Params
                                        	**type**\:   :py:class:`XformParams <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.Es200Sa.RxSa.XformParams>`
                                        
                                        

                                        """

                                        _prefix = 'crypto-macsec-pl-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.Es200Sa.RxSa, self).__init__()

                                            self.yang_name = "rx-sa"
                                            self.yang_parent_name = "es200-sa"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {"xform-params" : ("xform_params", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.Es200Sa.RxSa.XformParams)}
                                            self._child_list_classes = {}

                                            self.in_octets_decrypted_validated1 = YLeaf(YType.uint8, "in-octets-decrypted-validated1")

                                            self.in_octets_validated = YLeaf(YType.uint8, "in-octets-validated")

                                            self.in_pkts_delayed = YLeaf(YType.uint8, "in-pkts-delayed")

                                            self.in_pkts_invalid = YLeaf(YType.uint8, "in-pkts-invalid")

                                            self.in_pkts_late = YLeaf(YType.uint8, "in-pkts-late")

                                            self.in_pkts_not_using_sa = YLeaf(YType.uint8, "in-pkts-not-using-sa")

                                            self.in_pkts_not_valid = YLeaf(YType.uint8, "in-pkts-not-valid")

                                            self.in_pkts_ok = YLeaf(YType.uint8, "in-pkts-ok")

                                            self.in_pkts_unchecked = YLeaf(YType.uint8, "in-pkts-unchecked")

                                            self.in_pkts_unused_sa = YLeaf(YType.uint8, "in-pkts-unused-sa")

                                            self.is_valid = YLeaf(YType.boolean, "is-valid")

                                            self.sa_id = YLeaf(YType.uint8, "sa-id")

                                            self.sc_no = YLeaf(YType.uint32, "sc-no")

                                            self.xform_params = MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.Es200Sa.RxSa.XformParams()
                                            self.xform_params.parent = self
                                            self._children_name_map["xform_params"] = "xform-params"
                                            self._children_yang_names.add("xform-params")
                                            self._segment_path = lambda: "rx-sa"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.Es200Sa.RxSa, ['in_octets_decrypted_validated1', 'in_octets_validated', 'in_pkts_delayed', 'in_pkts_invalid', 'in_pkts_late', 'in_pkts_not_using_sa', 'in_pkts_not_valid', 'in_pkts_ok', 'in_pkts_unchecked', 'in_pkts_unused_sa', 'is_valid', 'sa_id', 'sc_no'], name, value)


                                        class XformParams(Entity):
                                            """
                                             Xform Params
                                            
                                            .. attribute:: aes_key_len
                                            
                                            	AES Key length
                                            	**type**\:  str
                                            
                                            .. attribute:: assoc_num
                                            
                                            	Association Number for egress
                                            	**type**\:  int
                                            
                                            	**range:** 0..255
                                            
                                            .. attribute:: bgen_auth_key
                                            
                                            	TRUE to generate the authKey, so authKey in this struct not used                                  APM\_FALSE to use provided authKey
                                            	**type**\:  bool
                                            
                                            .. attribute:: crypt_algo
                                            
                                            	Cryptographic algo used
                                            	**type**\:  str
                                            
                                            .. attribute:: is_egress_tr
                                            
                                            	APM\_TRUE if this is Egress Transform record, APM\_FALSE otherwise
                                            	**type**\:  bool
                                            
                                            .. attribute:: is_seq_num64_bit
                                            
                                            	TRUE if Seq Num is 64\-bit, FALSE if it is 32\-bit
                                            	**type**\:  bool
                                            
                                            .. attribute:: replay_win_size
                                            
                                            	range of pkt nos considered valid
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            

                                            """

                                            _prefix = 'crypto-macsec-pl-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.Es200Sa.RxSa.XformParams, self).__init__()

                                                self.yang_name = "xform-params"
                                                self.yang_parent_name = "rx-sa"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {}
                                                self._child_list_classes = {}

                                                self.aes_key_len = YLeaf(YType.str, "aes-key-len")

                                                self.assoc_num = YLeaf(YType.uint8, "assoc-num")

                                                self.bgen_auth_key = YLeaf(YType.boolean, "bgen-auth-key")

                                                self.crypt_algo = YLeaf(YType.str, "crypt-algo")

                                                self.is_egress_tr = YLeaf(YType.boolean, "is-egress-tr")

                                                self.is_seq_num64_bit = YLeaf(YType.boolean, "is-seq-num64-bit")

                                                self.replay_win_size = YLeaf(YType.uint32, "replay-win-size")
                                                self._segment_path = lambda: "xform-params"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.Es200Sa.RxSa.XformParams, ['aes_key_len', 'assoc_num', 'bgen_auth_key', 'crypt_algo', 'is_egress_tr', 'is_seq_num64_bit', 'replay_win_size'], name, value)


                                    class TxSa(Entity):
                                        """
                                        Tx SA Details
                                        
                                        .. attribute:: current_pkt_number
                                        
                                        	Current packet Number
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: initial_pkt_number
                                        
                                        	Initial Packet Number
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: is_valid
                                        
                                        	Is structure valid
                                        	**type**\:  bool
                                        
                                        .. attribute:: max_pkt_number
                                        
                                        	Maximum packet Number
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: out_octets_encrypted_protected1
                                        
                                        	octets1 encrypted/protected
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: out_pkts_encrypted_protected
                                        
                                        	packets encrypted/protected
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: out_pkts_too_long
                                        
                                        	packets exceeding egress MTU
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: sa_id
                                        
                                        	SA Index
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: sc_no
                                        
                                        	SC Number
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: xform_params
                                        
                                        	 Xform Params
                                        	**type**\:   :py:class:`XformParams <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.Es200Sa.TxSa.XformParams>`
                                        
                                        

                                        """

                                        _prefix = 'crypto-macsec-pl-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.Es200Sa.TxSa, self).__init__()

                                            self.yang_name = "tx-sa"
                                            self.yang_parent_name = "es200-sa"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {"xform-params" : ("xform_params", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.Es200Sa.TxSa.XformParams)}
                                            self._child_list_classes = {}

                                            self.current_pkt_number = YLeaf(YType.uint64, "current-pkt-number")

                                            self.initial_pkt_number = YLeaf(YType.uint8, "initial-pkt-number")

                                            self.is_valid = YLeaf(YType.boolean, "is-valid")

                                            self.max_pkt_number = YLeaf(YType.uint64, "max-pkt-number")

                                            self.out_octets_encrypted_protected1 = YLeaf(YType.uint8, "out-octets-encrypted-protected1")

                                            self.out_pkts_encrypted_protected = YLeaf(YType.uint8, "out-pkts-encrypted-protected")

                                            self.out_pkts_too_long = YLeaf(YType.uint8, "out-pkts-too-long")

                                            self.sa_id = YLeaf(YType.uint8, "sa-id")

                                            self.sc_no = YLeaf(YType.uint32, "sc-no")

                                            self.xform_params = MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.Es200Sa.TxSa.XformParams()
                                            self.xform_params.parent = self
                                            self._children_name_map["xform_params"] = "xform-params"
                                            self._children_yang_names.add("xform-params")
                                            self._segment_path = lambda: "tx-sa"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.Es200Sa.TxSa, ['current_pkt_number', 'initial_pkt_number', 'is_valid', 'max_pkt_number', 'out_octets_encrypted_protected1', 'out_pkts_encrypted_protected', 'out_pkts_too_long', 'sa_id', 'sc_no'], name, value)


                                        class XformParams(Entity):
                                            """
                                             Xform Params
                                            
                                            .. attribute:: aes_key_len
                                            
                                            	AES Key length
                                            	**type**\:  str
                                            
                                            .. attribute:: assoc_num
                                            
                                            	Association Number for egress
                                            	**type**\:  int
                                            
                                            	**range:** 0..255
                                            
                                            .. attribute:: bgen_auth_key
                                            
                                            	TRUE to generate the authKey, so authKey in this struct not used                                  APM\_FALSE to use provided authKey
                                            	**type**\:  bool
                                            
                                            .. attribute:: crypt_algo
                                            
                                            	Cryptographic algo used
                                            	**type**\:  str
                                            
                                            .. attribute:: is_egress_tr
                                            
                                            	APM\_TRUE if this is Egress Transform record, APM\_FALSE otherwise
                                            	**type**\:  bool
                                            
                                            .. attribute:: is_seq_num64_bit
                                            
                                            	TRUE if Seq Num is 64\-bit, FALSE if it is 32\-bit
                                            	**type**\:  bool
                                            
                                            .. attribute:: replay_win_size
                                            
                                            	range of pkt nos considered valid
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            

                                            """

                                            _prefix = 'crypto-macsec-pl-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.Es200Sa.TxSa.XformParams, self).__init__()

                                                self.yang_name = "xform-params"
                                                self.yang_parent_name = "tx-sa"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {}
                                                self._child_list_classes = {}

                                                self.aes_key_len = YLeaf(YType.str, "aes-key-len")

                                                self.assoc_num = YLeaf(YType.uint8, "assoc-num")

                                                self.bgen_auth_key = YLeaf(YType.boolean, "bgen-auth-key")

                                                self.crypt_algo = YLeaf(YType.str, "crypt-algo")

                                                self.is_egress_tr = YLeaf(YType.boolean, "is-egress-tr")

                                                self.is_seq_num64_bit = YLeaf(YType.boolean, "is-seq-num64-bit")

                                                self.replay_win_size = YLeaf(YType.uint32, "replay-win-size")
                                                self._segment_path = lambda: "xform-params"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.Es200Sa.TxSa.XformParams, ['aes_key_len', 'assoc_num', 'bgen_auth_key', 'crypt_algo', 'is_egress_tr', 'is_seq_num64_bit', 'replay_win_size'], name, value)


                                class MsfpgaSa(Entity):
                                    """
                                    MSFPGA SA Information
                                    
                                    .. attribute:: rx_sa
                                    
                                    	Rx SA Details
                                    	**type**\:   :py:class:`RxSa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.MsfpgaSa.RxSa>`
                                    
                                    .. attribute:: tx_sa
                                    
                                    	Tx SA Details
                                    	**type**\:   :py:class:`TxSa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.MsfpgaSa.TxSa>`
                                    
                                    

                                    """

                                    _prefix = 'crypto-macsec-pl-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.MsfpgaSa, self).__init__()

                                        self.yang_name = "msfpga-sa"
                                        self.yang_parent_name = "ext"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {"rx-sa" : ("rx_sa", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.MsfpgaSa.RxSa), "tx-sa" : ("tx_sa", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.MsfpgaSa.TxSa)}
                                        self._child_list_classes = {}

                                        self.rx_sa = MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.MsfpgaSa.RxSa()
                                        self.rx_sa.parent = self
                                        self._children_name_map["rx_sa"] = "rx-sa"
                                        self._children_yang_names.add("rx-sa")

                                        self.tx_sa = MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.MsfpgaSa.TxSa()
                                        self.tx_sa.parent = self
                                        self._children_name_map["tx_sa"] = "tx-sa"
                                        self._children_yang_names.add("tx-sa")
                                        self._segment_path = lambda: "msfpga-sa"


                                    class RxSa(Entity):
                                        """
                                        Rx SA Details
                                        
                                        .. attribute:: action
                                        
                                        	Action
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: an
                                        
                                        	Association Number
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: c_offset
                                        
                                        	Conf offset
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: crypto_algo
                                        
                                        	Crypto Algorithm
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: in_use
                                        
                                        	In Use
                                        	**type**\:  bool
                                        
                                        .. attribute:: is_egress
                                        
                                        	rx\_tx direction
                                        	**type**\:  bool
                                        
                                        .. attribute:: key_len
                                        
                                        	Key Length
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: next_pn
                                        
                                        	Next Packet Number
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: q_bit
                                        
                                        	Q bit
                                        	**type**\:  bool
                                        
                                        .. attribute:: qq_bit
                                        
                                        	QQ bit
                                        	**type**\:  bool
                                        
                                        .. attribute:: sa_id
                                        
                                        	SA Index
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: sci
                                        
                                        	SCI
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: valid
                                        
                                        	SA Validity
                                        	**type**\:  bool
                                        
                                        .. attribute:: xpn
                                        
                                        	XPN EN
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'crypto-macsec-pl-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.MsfpgaSa.RxSa, self).__init__()

                                            self.yang_name = "rx-sa"
                                            self.yang_parent_name = "msfpga-sa"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.action = YLeaf(YType.uint8, "action")

                                            self.an = YLeaf(YType.uint8, "an")

                                            self.c_offset = YLeaf(YType.uint8, "c-offset")

                                            self.crypto_algo = YLeaf(YType.uint8, "crypto-algo")

                                            self.in_use = YLeaf(YType.boolean, "in-use")

                                            self.is_egress = YLeaf(YType.boolean, "is-egress")

                                            self.key_len = YLeaf(YType.uint8, "key-len")

                                            self.next_pn = YLeaf(YType.uint64, "next-pn")

                                            self.q_bit = YLeaf(YType.boolean, "q-bit")

                                            self.qq_bit = YLeaf(YType.boolean, "qq-bit")

                                            self.sa_id = YLeaf(YType.uint8, "sa-id")

                                            self.sci = YLeaf(YType.uint64, "sci")

                                            self.valid = YLeaf(YType.boolean, "valid")

                                            self.xpn = YLeaf(YType.uint8, "xpn")
                                            self._segment_path = lambda: "rx-sa"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.MsfpgaSa.RxSa, ['action', 'an', 'c_offset', 'crypto_algo', 'in_use', 'is_egress', 'key_len', 'next_pn', 'q_bit', 'qq_bit', 'sa_id', 'sci', 'valid', 'xpn'], name, value)


                                    class TxSa(Entity):
                                        """
                                        Tx SA Details
                                        
                                        .. attribute:: action
                                        
                                        	Action
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: an
                                        
                                        	Association Number
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: c_offset
                                        
                                        	Conf offset
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: crypto_algo
                                        
                                        	Crypto Algorithm
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: in_use
                                        
                                        	In Use
                                        	**type**\:  bool
                                        
                                        .. attribute:: is_egress
                                        
                                        	rx\_tx direction
                                        	**type**\:  bool
                                        
                                        .. attribute:: key_len
                                        
                                        	Key Length
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: next_pn
                                        
                                        	Next Packet Number
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: q_bit
                                        
                                        	Q bit
                                        	**type**\:  bool
                                        
                                        .. attribute:: qq_bit
                                        
                                        	QQ bit
                                        	**type**\:  bool
                                        
                                        .. attribute:: sa_id
                                        
                                        	SA Index
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: sci
                                        
                                        	SCI
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: valid
                                        
                                        	SA Validity
                                        	**type**\:  bool
                                        
                                        .. attribute:: xpn
                                        
                                        	XPN EN
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'crypto-macsec-pl-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.MsfpgaSa.TxSa, self).__init__()

                                            self.yang_name = "tx-sa"
                                            self.yang_parent_name = "msfpga-sa"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.action = YLeaf(YType.uint8, "action")

                                            self.an = YLeaf(YType.uint8, "an")

                                            self.c_offset = YLeaf(YType.uint8, "c-offset")

                                            self.crypto_algo = YLeaf(YType.uint8, "crypto-algo")

                                            self.in_use = YLeaf(YType.boolean, "in-use")

                                            self.is_egress = YLeaf(YType.boolean, "is-egress")

                                            self.key_len = YLeaf(YType.uint8, "key-len")

                                            self.next_pn = YLeaf(YType.uint64, "next-pn")

                                            self.q_bit = YLeaf(YType.boolean, "q-bit")

                                            self.qq_bit = YLeaf(YType.boolean, "qq-bit")

                                            self.sa_id = YLeaf(YType.uint8, "sa-id")

                                            self.sci = YLeaf(YType.uint64, "sci")

                                            self.valid = YLeaf(YType.boolean, "valid")

                                            self.xpn = YLeaf(YType.uint8, "xpn")
                                            self._segment_path = lambda: "tx-sa"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.MsfpgaSa.TxSa, ['action', 'an', 'c_offset', 'crypto_algo', 'in_use', 'is_egress', 'key_len', 'next_pn', 'q_bit', 'qq_bit', 'sa_id', 'sci', 'valid', 'xpn'], name, value)


                                class XlfpgaSa(Entity):
                                    """
                                    XLFPGA SA Information
                                    
                                    .. attribute:: rx_sa
                                    
                                    	Rx SA Details
                                    	**type**\:   :py:class:`RxSa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.XlfpgaSa.RxSa>`
                                    
                                    .. attribute:: tx_sa
                                    
                                    	Tx SA Details
                                    	**type**\:   :py:class:`TxSa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.XlfpgaSa.TxSa>`
                                    
                                    

                                    """

                                    _prefix = 'crypto-macsec-pl-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.XlfpgaSa, self).__init__()

                                        self.yang_name = "xlfpga-sa"
                                        self.yang_parent_name = "ext"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {"rx-sa" : ("rx_sa", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.XlfpgaSa.RxSa), "tx-sa" : ("tx_sa", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.XlfpgaSa.TxSa)}
                                        self._child_list_classes = {}

                                        self.rx_sa = MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.XlfpgaSa.RxSa()
                                        self.rx_sa.parent = self
                                        self._children_name_map["rx_sa"] = "rx-sa"
                                        self._children_yang_names.add("rx-sa")

                                        self.tx_sa = MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.XlfpgaSa.TxSa()
                                        self.tx_sa.parent = self
                                        self._children_name_map["tx_sa"] = "tx-sa"
                                        self._children_yang_names.add("tx-sa")
                                        self._segment_path = lambda: "xlfpga-sa"


                                    class RxSa(Entity):
                                        """
                                        Rx SA Details
                                        
                                        .. attribute:: an
                                        
                                        	Association Number
                                        	**type**\:  str
                                        
                                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                        
                                        .. attribute:: auth_err_cfg
                                        
                                        	Auth  Error Config
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: cipher_suite
                                        
                                        	Cipher Suite Used
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: confidentiality_offset
                                        
                                        	Confidentiality Offset
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: crc_value
                                        
                                        	CRC Value
                                        	**type**\:  list of int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: current_packet_num
                                        
                                        	Current Packet Number
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: fcs_err_cfg
                                        
                                        	FCS Error Config
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: lowest_acceptable_packet_num
                                        
                                        	Lowest Acceptable Packet Number
                                        	**type**\:  list of int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: max_packet_num
                                        
                                        	Max Packet Number
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: next_expected_packet_num
                                        
                                        	Next expected Packet Number
                                        	**type**\:  list of int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: num_an_in_use
                                        
                                        	Num of AN's in Use
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: pkt_tagged_detected
                                        
                                        	Tagged Pkts Detected
                                        	**type**\:  bool
                                        
                                        .. attribute:: pkt_tagged_validated
                                        
                                        	Tagged Pkts Validated
                                        	**type**\:  bool
                                        
                                        .. attribute:: pkt_untagged_detected
                                        
                                        	Untagged Pkts Detected
                                        	**type**\:  bool
                                        
                                        .. attribute:: protection_enable
                                        
                                        	Protection Enabled
                                        	**type**\:  bool
                                        
                                        .. attribute:: recent_an
                                        
                                        	Recent Association Num
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: replay_protect_mode
                                        
                                        	Replay Protect Mode
                                        	**type**\:  bool
                                        
                                        .. attribute:: replay_window
                                        
                                        	Replay Window 
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: secure_channel_id
                                        
                                        	Secure Channel ID
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: secure_mode
                                        
                                        	Secure Mode \- Must/Should
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: ssci
                                        
                                        	Short Secure Channel ID
                                        	**type**\:  list of int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: validation_mode
                                        
                                        	Validation Mode
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'crypto-macsec-pl-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.XlfpgaSa.RxSa, self).__init__()

                                            self.yang_name = "rx-sa"
                                            self.yang_parent_name = "xlfpga-sa"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.an = YLeaf(YType.str, "an")

                                            self.auth_err_cfg = YLeaf(YType.uint32, "auth-err-cfg")

                                            self.cipher_suite = YLeaf(YType.uint32, "cipher-suite")

                                            self.confidentiality_offset = YLeaf(YType.uint8, "confidentiality-offset")

                                            self.crc_value = YLeafList(YType.uint32, "crc-value")

                                            self.current_packet_num = YLeaf(YType.uint64, "current-packet-num")

                                            self.fcs_err_cfg = YLeaf(YType.uint32, "fcs-err-cfg")

                                            self.lowest_acceptable_packet_num = YLeafList(YType.uint64, "lowest-acceptable-packet-num")

                                            self.max_packet_num = YLeaf(YType.uint64, "max-packet-num")

                                            self.next_expected_packet_num = YLeafList(YType.uint64, "next-expected-packet-num")

                                            self.num_an_in_use = YLeaf(YType.uint32, "num-an-in-use")

                                            self.pkt_tagged_detected = YLeaf(YType.boolean, "pkt-tagged-detected")

                                            self.pkt_tagged_validated = YLeaf(YType.boolean, "pkt-tagged-validated")

                                            self.pkt_untagged_detected = YLeaf(YType.boolean, "pkt-untagged-detected")

                                            self.protection_enable = YLeaf(YType.boolean, "protection-enable")

                                            self.recent_an = YLeaf(YType.uint8, "recent-an")

                                            self.replay_protect_mode = YLeaf(YType.boolean, "replay-protect-mode")

                                            self.replay_window = YLeaf(YType.uint32, "replay-window")

                                            self.secure_channel_id = YLeaf(YType.uint64, "secure-channel-id")

                                            self.secure_mode = YLeaf(YType.uint32, "secure-mode")

                                            self.ssci = YLeafList(YType.uint32, "ssci")

                                            self.validation_mode = YLeaf(YType.uint32, "validation-mode")
                                            self._segment_path = lambda: "rx-sa"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.XlfpgaSa.RxSa, ['an', 'auth_err_cfg', 'cipher_suite', 'confidentiality_offset', 'crc_value', 'current_packet_num', 'fcs_err_cfg', 'lowest_acceptable_packet_num', 'max_packet_num', 'next_expected_packet_num', 'num_an_in_use', 'pkt_tagged_detected', 'pkt_tagged_validated', 'pkt_untagged_detected', 'protection_enable', 'recent_an', 'replay_protect_mode', 'replay_window', 'secure_channel_id', 'secure_mode', 'ssci', 'validation_mode'], name, value)


                                    class TxSa(Entity):
                                        """
                                        Tx SA Details
                                        
                                        .. attribute:: an
                                        
                                        	Association Number
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: cipher_suite
                                        
                                        	Cipher Suite Used
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: confidentiality_offset
                                        
                                        	Confidentiality Offset
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: crc_value
                                        
                                        	CRC Value
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: current_packet_num
                                        
                                        	Current Packet Number
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: fcs_err_cfg
                                        
                                        	FCS Error Config
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: initial_packet_number
                                        
                                        	Initial Packet Number
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: max_packet_num
                                        
                                        	Max Packet Number
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: protection_enable
                                        
                                        	Protection Enabled
                                        	**type**\:  bool
                                        
                                        .. attribute:: sectag_length
                                        
                                        	Sec Tag Length(bytes) 
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: secure_channel_id
                                        
                                        	Secure Channel ID
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: secure_mode
                                        
                                        	Secure Mode \- Must/Should
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: ssci
                                        
                                        	Short Secure Channel ID
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'crypto-macsec-pl-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.XlfpgaSa.TxSa, self).__init__()

                                            self.yang_name = "tx-sa"
                                            self.yang_parent_name = "xlfpga-sa"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.an = YLeaf(YType.uint8, "an")

                                            self.cipher_suite = YLeaf(YType.uint32, "cipher-suite")

                                            self.confidentiality_offset = YLeaf(YType.uint8, "confidentiality-offset")

                                            self.crc_value = YLeaf(YType.uint32, "crc-value")

                                            self.current_packet_num = YLeaf(YType.uint64, "current-packet-num")

                                            self.fcs_err_cfg = YLeaf(YType.uint8, "fcs-err-cfg")

                                            self.initial_packet_number = YLeaf(YType.uint64, "initial-packet-number")

                                            self.max_packet_num = YLeaf(YType.uint64, "max-packet-num")

                                            self.protection_enable = YLeaf(YType.boolean, "protection-enable")

                                            self.sectag_length = YLeaf(YType.uint32, "sectag-length")

                                            self.secure_channel_id = YLeaf(YType.uint64, "secure-channel-id")

                                            self.secure_mode = YLeaf(YType.uint8, "secure-mode")

                                            self.ssci = YLeaf(YType.uint32, "ssci")
                                            self._segment_path = lambda: "tx-sa"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.XlfpgaSa.TxSa, ['an', 'cipher_suite', 'confidentiality_offset', 'crc_value', 'current_packet_num', 'fcs_err_cfg', 'initial_packet_number', 'max_packet_num', 'protection_enable', 'sectag_length', 'secure_channel_id', 'secure_mode', 'ssci'], name, value)


                    class HwStatistics(Entity):
                        """
                        The Hardware Statistics
                        
                        .. attribute:: ext
                        
                        	ext
                        	**type**\:   :py:class:`Ext <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext>`
                        
                        

                        """

                        _prefix = 'crypto-macsec-pl-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics, self).__init__()

                            self.yang_name = "hw-statistics"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"ext" : ("ext", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext)}
                            self._child_list_classes = {}

                            self.ext = MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext()
                            self.ext.parent = self
                            self._children_name_map["ext"] = "ext"
                            self._children_yang_names.add("ext")
                            self._segment_path = lambda: "hw-statistics"


                        class Ext(Entity):
                            """
                            ext
                            
                            .. attribute:: es200_stats
                            
                            	ES200 Stats
                            	**type**\:   :py:class:`Es200Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats>`
                            
                            .. attribute:: msfpga_stats
                            
                            	MSFPGA Stats
                            	**type**\:   :py:class:`MsfpgaStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.MsfpgaStats>`
                            
                            .. attribute:: type
                            
                            	type
                            	**type**\:   :py:class:`MacsecCard <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecCard>`
                            
                            .. attribute:: xlfpga_stats
                            
                            	XLFPGA Stats
                            	**type**\:   :py:class:`XlfpgaStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.XlfpgaStats>`
                            
                            

                            """

                            _prefix = 'crypto-macsec-pl-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext, self).__init__()

                                self.yang_name = "ext"
                                self.yang_parent_name = "hw-statistics"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"es200-stats" : ("es200_stats", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats), "msfpga-stats" : ("msfpga_stats", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.MsfpgaStats), "xlfpga-stats" : ("xlfpga_stats", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.XlfpgaStats)}
                                self._child_list_classes = {}

                                self.type = YLeaf(YType.enumeration, "type")

                                self.es200_stats = MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats()
                                self.es200_stats.parent = self
                                self._children_name_map["es200_stats"] = "es200-stats"
                                self._children_yang_names.add("es200-stats")

                                self.msfpga_stats = MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.MsfpgaStats()
                                self.msfpga_stats.parent = self
                                self._children_name_map["msfpga_stats"] = "msfpga-stats"
                                self._children_yang_names.add("msfpga-stats")

                                self.xlfpga_stats = MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.XlfpgaStats()
                                self.xlfpga_stats.parent = self
                                self._children_name_map["xlfpga_stats"] = "xlfpga-stats"
                                self._children_yang_names.add("xlfpga-stats")
                                self._segment_path = lambda: "ext"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext, ['type'], name, value)


                            class Es200Stats(Entity):
                                """
                                ES200 Stats
                                
                                .. attribute:: rx_interface_macsec_stats
                                
                                	Rx interface Macsec Stats
                                	**type**\:   :py:class:`RxInterfaceMacsecStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats.RxInterfaceMacsecStats>`
                                
                                .. attribute:: rx_port_stats
                                
                                	Port level RX Stats
                                	**type**\:   :py:class:`RxPortStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats.RxPortStats>`
                                
                                .. attribute:: rx_sa_stats
                                
                                	Rx SA Stats
                                	**type**\:   :py:class:`RxSaStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats.RxSaStats>`
                                
                                .. attribute:: rx_sc_macsec_stats
                                
                                	Rx SC Macsec Stats
                                	**type**\:   :py:class:`RxScMacsecStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats.RxScMacsecStats>`
                                
                                .. attribute:: tx_interface_macsec_stats
                                
                                	Tx interface Macsec Stats
                                	**type**\:   :py:class:`TxInterfaceMacsecStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats.TxInterfaceMacsecStats>`
                                
                                .. attribute:: tx_port_stats
                                
                                	Port level TX Stats
                                	**type**\:   :py:class:`TxPortStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats.TxPortStats>`
                                
                                .. attribute:: tx_sa_stats
                                
                                	Tx SA Stats
                                	**type**\:   :py:class:`TxSaStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats.TxSaStats>`
                                
                                .. attribute:: tx_sc_macsec_stats
                                
                                	Tx SC Macsec Stats
                                	**type**\:   :py:class:`TxScMacsecStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats.TxScMacsecStats>`
                                
                                

                                """

                                _prefix = 'crypto-macsec-pl-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats, self).__init__()

                                    self.yang_name = "es200-stats"
                                    self.yang_parent_name = "ext"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {"rx-interface-macsec-stats" : ("rx_interface_macsec_stats", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats.RxInterfaceMacsecStats), "rx-port-stats" : ("rx_port_stats", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats.RxPortStats), "rx-sa-stats" : ("rx_sa_stats", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats.RxSaStats), "rx-sc-macsec-stats" : ("rx_sc_macsec_stats", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats.RxScMacsecStats), "tx-interface-macsec-stats" : ("tx_interface_macsec_stats", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats.TxInterfaceMacsecStats), "tx-port-stats" : ("tx_port_stats", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats.TxPortStats), "tx-sa-stats" : ("tx_sa_stats", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats.TxSaStats), "tx-sc-macsec-stats" : ("tx_sc_macsec_stats", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats.TxScMacsecStats)}
                                    self._child_list_classes = {}

                                    self.rx_interface_macsec_stats = MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats.RxInterfaceMacsecStats()
                                    self.rx_interface_macsec_stats.parent = self
                                    self._children_name_map["rx_interface_macsec_stats"] = "rx-interface-macsec-stats"
                                    self._children_yang_names.add("rx-interface-macsec-stats")

                                    self.rx_port_stats = MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats.RxPortStats()
                                    self.rx_port_stats.parent = self
                                    self._children_name_map["rx_port_stats"] = "rx-port-stats"
                                    self._children_yang_names.add("rx-port-stats")

                                    self.rx_sa_stats = MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats.RxSaStats()
                                    self.rx_sa_stats.parent = self
                                    self._children_name_map["rx_sa_stats"] = "rx-sa-stats"
                                    self._children_yang_names.add("rx-sa-stats")

                                    self.rx_sc_macsec_stats = MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats.RxScMacsecStats()
                                    self.rx_sc_macsec_stats.parent = self
                                    self._children_name_map["rx_sc_macsec_stats"] = "rx-sc-macsec-stats"
                                    self._children_yang_names.add("rx-sc-macsec-stats")

                                    self.tx_interface_macsec_stats = MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats.TxInterfaceMacsecStats()
                                    self.tx_interface_macsec_stats.parent = self
                                    self._children_name_map["tx_interface_macsec_stats"] = "tx-interface-macsec-stats"
                                    self._children_yang_names.add("tx-interface-macsec-stats")

                                    self.tx_port_stats = MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats.TxPortStats()
                                    self.tx_port_stats.parent = self
                                    self._children_name_map["tx_port_stats"] = "tx-port-stats"
                                    self._children_yang_names.add("tx-port-stats")

                                    self.tx_sa_stats = MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats.TxSaStats()
                                    self.tx_sa_stats.parent = self
                                    self._children_name_map["tx_sa_stats"] = "tx-sa-stats"
                                    self._children_yang_names.add("tx-sa-stats")

                                    self.tx_sc_macsec_stats = MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats.TxScMacsecStats()
                                    self.tx_sc_macsec_stats.parent = self
                                    self._children_name_map["tx_sc_macsec_stats"] = "tx-sc-macsec-stats"
                                    self._children_yang_names.add("tx-sc-macsec-stats")
                                    self._segment_path = lambda: "es200-stats"


                                class RxInterfaceMacsecStats(Entity):
                                    """
                                    Rx interface Macsec Stats
                                    
                                    .. attribute:: in_bcast_pkts_ctrl
                                    
                                    	Broadcast pkts rx on controlled port
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_bcast_pkts_unctrl
                                    
                                    	Broadcast pkts rx on uncontrolled port
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_drop_pkts_class
                                    
                                    	Packets dropped due to overflow in classification pipeline
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_drop_pkts_data
                                    
                                    	Packets dropped due to overflow in processing pipeline
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_mcast_pkts_ctrl
                                    
                                    	Multicast pkts rx on controlled port
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_mcast_pkts_unctrl
                                    
                                    	Multicast pkts rx on uncontrolled port
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_octets_ctrl
                                    
                                    	Octets rx on controlled port
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_octets_unctrl
                                    
                                    	Octets rx on uncontrolled port
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkt_bad_tag
                                    
                                    	ingress frames received with an invalid MACSec tag or ICV                                       added with next one gives InPktsSCIMiss
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkt_ctrl
                                    
                                    	ingress packet that is classified as control packet
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkt_no_sci
                                    
                                    	correctly tagged ingress frames for which no valid SC found &                                 validateFrames is strict
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkt_no_tag
                                    
                                    	ingress packet untagged & validateFrames is strict
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkts_tagged_ctrl
                                    
                                    	ingress packets that are control or KaY packets
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkts_unknown_sci
                                    
                                    	correctly tagged ingress frames for which no valid SC found &                                 validateFrames is !strict
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkts_untagged
                                    
                                    	ingress packet untagged & validateFrames is  !strict
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_rx_drop_pkts_ctrl
                                    
                                    	Data pkts dropped due to overrun
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_rx_drop_pkts_unctrl
                                    
                                    	Control pkts dropped due to overrun
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_rx_error_pkts_ctrl
                                    
                                    	Data pkts error\-terminated due to overrun
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_rx_error_pkts_unctrl
                                    
                                    	Control pkts error\-terminated due to overrun
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_ucast_pkts_ctrl
                                    
                                    	Unicast pkts rx on controlled port
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_ucast_pkts_unctrl
                                    
                                    	Unicast pkts rx on uncontrolled port
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: transform_error_pkts
                                    
                                    	counter to count internal errors in the MACSec core
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'crypto-macsec-pl-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats.RxInterfaceMacsecStats, self).__init__()

                                        self.yang_name = "rx-interface-macsec-stats"
                                        self.yang_parent_name = "es200-stats"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.in_bcast_pkts_ctrl = YLeaf(YType.uint64, "in-bcast-pkts-ctrl")

                                        self.in_bcast_pkts_unctrl = YLeaf(YType.uint64, "in-bcast-pkts-unctrl")

                                        self.in_drop_pkts_class = YLeaf(YType.uint64, "in-drop-pkts-class")

                                        self.in_drop_pkts_data = YLeaf(YType.uint64, "in-drop-pkts-data")

                                        self.in_mcast_pkts_ctrl = YLeaf(YType.uint64, "in-mcast-pkts-ctrl")

                                        self.in_mcast_pkts_unctrl = YLeaf(YType.uint64, "in-mcast-pkts-unctrl")

                                        self.in_octets_ctrl = YLeaf(YType.uint64, "in-octets-ctrl")

                                        self.in_octets_unctrl = YLeaf(YType.uint64, "in-octets-unctrl")

                                        self.in_pkt_bad_tag = YLeaf(YType.uint64, "in-pkt-bad-tag")

                                        self.in_pkt_ctrl = YLeaf(YType.uint64, "in-pkt-ctrl")

                                        self.in_pkt_no_sci = YLeaf(YType.uint64, "in-pkt-no-sci")

                                        self.in_pkt_no_tag = YLeaf(YType.uint64, "in-pkt-no-tag")

                                        self.in_pkts_tagged_ctrl = YLeaf(YType.uint64, "in-pkts-tagged-ctrl")

                                        self.in_pkts_unknown_sci = YLeaf(YType.uint64, "in-pkts-unknown-sci")

                                        self.in_pkts_untagged = YLeaf(YType.uint64, "in-pkts-untagged")

                                        self.in_rx_drop_pkts_ctrl = YLeaf(YType.uint64, "in-rx-drop-pkts-ctrl")

                                        self.in_rx_drop_pkts_unctrl = YLeaf(YType.uint64, "in-rx-drop-pkts-unctrl")

                                        self.in_rx_error_pkts_ctrl = YLeaf(YType.uint64, "in-rx-error-pkts-ctrl")

                                        self.in_rx_error_pkts_unctrl = YLeaf(YType.uint64, "in-rx-error-pkts-unctrl")

                                        self.in_ucast_pkts_ctrl = YLeaf(YType.uint64, "in-ucast-pkts-ctrl")

                                        self.in_ucast_pkts_unctrl = YLeaf(YType.uint64, "in-ucast-pkts-unctrl")

                                        self.transform_error_pkts = YLeaf(YType.uint64, "transform-error-pkts")
                                        self._segment_path = lambda: "rx-interface-macsec-stats"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats.RxInterfaceMacsecStats, ['in_bcast_pkts_ctrl', 'in_bcast_pkts_unctrl', 'in_drop_pkts_class', 'in_drop_pkts_data', 'in_mcast_pkts_ctrl', 'in_mcast_pkts_unctrl', 'in_octets_ctrl', 'in_octets_unctrl', 'in_pkt_bad_tag', 'in_pkt_ctrl', 'in_pkt_no_sci', 'in_pkt_no_tag', 'in_pkts_tagged_ctrl', 'in_pkts_unknown_sci', 'in_pkts_untagged', 'in_rx_drop_pkts_ctrl', 'in_rx_drop_pkts_unctrl', 'in_rx_error_pkts_ctrl', 'in_rx_error_pkts_unctrl', 'in_ucast_pkts_ctrl', 'in_ucast_pkts_unctrl', 'transform_error_pkts'], name, value)


                                class RxPortStats(Entity):
                                    """
                                    Port level RX Stats
                                    
                                    .. attribute:: flow_miss
                                    
                                    	Pkts matching none of flow entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: multi_flow_match
                                    
                                    	Pkts matching multiple flow entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: parser_dropped
                                    
                                    	Pkts dropped by header parser as invalid
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: pkts_ctrl
                                    
                                    	Control pkts forwarded
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: pkts_data
                                    
                                    	Data pkts forwarded
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: pkts_dropped
                                    
                                    	Pkts dropped by classifier
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: pkts_err_in
                                    
                                    	Pkts received with an error indication
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'crypto-macsec-pl-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats.RxPortStats, self).__init__()

                                        self.yang_name = "rx-port-stats"
                                        self.yang_parent_name = "es200-stats"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.flow_miss = YLeaf(YType.uint64, "flow-miss")

                                        self.multi_flow_match = YLeaf(YType.uint64, "multi-flow-match")

                                        self.parser_dropped = YLeaf(YType.uint64, "parser-dropped")

                                        self.pkts_ctrl = YLeaf(YType.uint64, "pkts-ctrl")

                                        self.pkts_data = YLeaf(YType.uint64, "pkts-data")

                                        self.pkts_dropped = YLeaf(YType.uint64, "pkts-dropped")

                                        self.pkts_err_in = YLeaf(YType.uint64, "pkts-err-in")
                                        self._segment_path = lambda: "rx-port-stats"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats.RxPortStats, ['flow_miss', 'multi_flow_match', 'parser_dropped', 'pkts_ctrl', 'pkts_data', 'pkts_dropped', 'pkts_err_in'], name, value)


                                class RxSaStats(Entity):
                                    """
                                    Rx SA Stats
                                    
                                    .. attribute:: in_octets_decrypted_validated1
                                    
                                    	octets1 decrypted/validated
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_octets_validated
                                    
                                    	octets validated
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkts_delayed
                                    
                                    	PN of packet outside replay window & validateFrames !strict
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkts_invalid
                                    
                                    	packet not valid & validateFrames !strict
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkts_late
                                    
                                    	PN of packet outside replay window & validateFrames strict
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkts_not_using_sa
                                    
                                    	packet assigned to SA not in use & validateFrames strict
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkts_not_valid
                                    
                                    	packet not valid & validateFrames strict
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkts_ok
                                    
                                    	packets with no error
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkts_unchecked
                                    
                                    	frame not valid & validateFrames disabled
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkts_unused_sa
                                    
                                    	packet assigned to SA not in use & validateFrames !strict
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'crypto-macsec-pl-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats.RxSaStats, self).__init__()

                                        self.yang_name = "rx-sa-stats"
                                        self.yang_parent_name = "es200-stats"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.in_octets_decrypted_validated1 = YLeaf(YType.uint64, "in-octets-decrypted-validated1")

                                        self.in_octets_validated = YLeaf(YType.uint64, "in-octets-validated")

                                        self.in_pkts_delayed = YLeaf(YType.uint64, "in-pkts-delayed")

                                        self.in_pkts_invalid = YLeaf(YType.uint64, "in-pkts-invalid")

                                        self.in_pkts_late = YLeaf(YType.uint64, "in-pkts-late")

                                        self.in_pkts_not_using_sa = YLeaf(YType.uint64, "in-pkts-not-using-sa")

                                        self.in_pkts_not_valid = YLeaf(YType.uint64, "in-pkts-not-valid")

                                        self.in_pkts_ok = YLeaf(YType.uint64, "in-pkts-ok")

                                        self.in_pkts_unchecked = YLeaf(YType.uint64, "in-pkts-unchecked")

                                        self.in_pkts_unused_sa = YLeaf(YType.uint64, "in-pkts-unused-sa")
                                        self._segment_path = lambda: "rx-sa-stats"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats.RxSaStats, ['in_octets_decrypted_validated1', 'in_octets_validated', 'in_pkts_delayed', 'in_pkts_invalid', 'in_pkts_late', 'in_pkts_not_using_sa', 'in_pkts_not_valid', 'in_pkts_ok', 'in_pkts_unchecked', 'in_pkts_unused_sa'], name, value)


                                class RxScMacsecStats(Entity):
                                    """
                                    Rx SC Macsec Stats
                                    
                                    .. attribute:: in_pkts_sa_not_in_use
                                    
                                    	Packets received with SA not in use
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'crypto-macsec-pl-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats.RxScMacsecStats, self).__init__()

                                        self.yang_name = "rx-sc-macsec-stats"
                                        self.yang_parent_name = "es200-stats"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.in_pkts_sa_not_in_use = YLeaf(YType.uint64, "in-pkts-sa-not-in-use")
                                        self._segment_path = lambda: "rx-sc-macsec-stats"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats.RxScMacsecStats, ['in_pkts_sa_not_in_use'], name, value)


                                class TxInterfaceMacsecStats(Entity):
                                    """
                                    Tx interface Macsec Stats
                                    
                                    .. attribute:: out_bcast_pkts_ctrl
                                    
                                    	Broadcast pkts tx on controlled port
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_bcast_pkts_unctrl
                                    
                                    	Broadcast pkts tx on uncontrolled port
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_drop_pkts_class
                                    
                                    	Packets dropped due to overflow in classification pipeline
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_drop_pkts_data
                                    
                                    	Packets dropped due to overflow in  processing pipeline
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_mcast_pkts_ctrl
                                    
                                    	Multicast pkts tx on controlled port
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_mcast_pkts_unctrl
                                    
                                    	Multicast pkts tx on uncontrolled port
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_octets_common
                                    
                                    	Octets tx on common port
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_octets_ctrl
                                    
                                    	Octets tx on controlled port
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_octets_unctrl
                                    
                                    	Octets tx on uncontrolled port
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_pkt_ctrl
                                    
                                    	egress packet that is classified as control packet
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_pkts_untagged
                                    
                                    	egress packet to go out untagged when protectFrames not set
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_rx_drop_pkts_ctrl
                                    
                                    	Data pkts dropped due to overrun
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_rx_drop_pkts_unctrl
                                    
                                    	Control pkts dropped due to overrun
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_rx_err_pkts_ctrl
                                    
                                    	Data pkts error\-terminated due to overrun
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_rx_err_pkts_unctrl
                                    
                                    	Control pkts error\-terminated due to overrun
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_ucast_pkts_ctrl
                                    
                                    	Unicast pkts tx on controlled port
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_ucast_pkts_unctrl
                                    
                                    	Unicast pkts tx on uncontrolled port
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: transform_error_pkts
                                    
                                    	counter to count internal errors in the MACSec core
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'crypto-macsec-pl-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats.TxInterfaceMacsecStats, self).__init__()

                                        self.yang_name = "tx-interface-macsec-stats"
                                        self.yang_parent_name = "es200-stats"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.out_bcast_pkts_ctrl = YLeaf(YType.uint64, "out-bcast-pkts-ctrl")

                                        self.out_bcast_pkts_unctrl = YLeaf(YType.uint64, "out-bcast-pkts-unctrl")

                                        self.out_drop_pkts_class = YLeaf(YType.uint64, "out-drop-pkts-class")

                                        self.out_drop_pkts_data = YLeaf(YType.uint64, "out-drop-pkts-data")

                                        self.out_mcast_pkts_ctrl = YLeaf(YType.uint64, "out-mcast-pkts-ctrl")

                                        self.out_mcast_pkts_unctrl = YLeaf(YType.uint64, "out-mcast-pkts-unctrl")

                                        self.out_octets_common = YLeaf(YType.uint64, "out-octets-common")

                                        self.out_octets_ctrl = YLeaf(YType.uint64, "out-octets-ctrl")

                                        self.out_octets_unctrl = YLeaf(YType.uint64, "out-octets-unctrl")

                                        self.out_pkt_ctrl = YLeaf(YType.uint64, "out-pkt-ctrl")

                                        self.out_pkts_untagged = YLeaf(YType.uint64, "out-pkts-untagged")

                                        self.out_rx_drop_pkts_ctrl = YLeaf(YType.uint64, "out-rx-drop-pkts-ctrl")

                                        self.out_rx_drop_pkts_unctrl = YLeaf(YType.uint64, "out-rx-drop-pkts-unctrl")

                                        self.out_rx_err_pkts_ctrl = YLeaf(YType.uint64, "out-rx-err-pkts-ctrl")

                                        self.out_rx_err_pkts_unctrl = YLeaf(YType.uint64, "out-rx-err-pkts-unctrl")

                                        self.out_ucast_pkts_ctrl = YLeaf(YType.uint64, "out-ucast-pkts-ctrl")

                                        self.out_ucast_pkts_unctrl = YLeaf(YType.uint64, "out-ucast-pkts-unctrl")

                                        self.transform_error_pkts = YLeaf(YType.uint64, "transform-error-pkts")
                                        self._segment_path = lambda: "tx-interface-macsec-stats"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats.TxInterfaceMacsecStats, ['out_bcast_pkts_ctrl', 'out_bcast_pkts_unctrl', 'out_drop_pkts_class', 'out_drop_pkts_data', 'out_mcast_pkts_ctrl', 'out_mcast_pkts_unctrl', 'out_octets_common', 'out_octets_ctrl', 'out_octets_unctrl', 'out_pkt_ctrl', 'out_pkts_untagged', 'out_rx_drop_pkts_ctrl', 'out_rx_drop_pkts_unctrl', 'out_rx_err_pkts_ctrl', 'out_rx_err_pkts_unctrl', 'out_ucast_pkts_ctrl', 'out_ucast_pkts_unctrl', 'transform_error_pkts'], name, value)


                                class TxPortStats(Entity):
                                    """
                                    Port level TX Stats
                                    
                                    .. attribute:: flow_miss
                                    
                                    	Pkts matching none of flow entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: multi_flow_match
                                    
                                    	Pkts matching multiple flow entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: parser_dropped
                                    
                                    	Pkts dropped by header parser as invalid
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: pkts_ctrl
                                    
                                    	Control pkts forwarded
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: pkts_data
                                    
                                    	Data pkts forwarded
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: pkts_dropped
                                    
                                    	Pkts dropped by classifier
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: pkts_err_in
                                    
                                    	Pkts received with an error indication
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'crypto-macsec-pl-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats.TxPortStats, self).__init__()

                                        self.yang_name = "tx-port-stats"
                                        self.yang_parent_name = "es200-stats"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.flow_miss = YLeaf(YType.uint64, "flow-miss")

                                        self.multi_flow_match = YLeaf(YType.uint64, "multi-flow-match")

                                        self.parser_dropped = YLeaf(YType.uint64, "parser-dropped")

                                        self.pkts_ctrl = YLeaf(YType.uint64, "pkts-ctrl")

                                        self.pkts_data = YLeaf(YType.uint64, "pkts-data")

                                        self.pkts_dropped = YLeaf(YType.uint64, "pkts-dropped")

                                        self.pkts_err_in = YLeaf(YType.uint64, "pkts-err-in")
                                        self._segment_path = lambda: "tx-port-stats"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats.TxPortStats, ['flow_miss', 'multi_flow_match', 'parser_dropped', 'pkts_ctrl', 'pkts_data', 'pkts_dropped', 'pkts_err_in'], name, value)


                                class TxSaStats(Entity):
                                    """
                                    Tx SA Stats
                                    
                                    .. attribute:: out_octets_encrypted_protected1
                                    
                                    	octets1 encrypted/protected ?
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_pkts_encrypted_protected
                                    
                                    	packets encrypted/protected
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_pkts_too_long
                                    
                                    	packets exceeding egress MTU
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'crypto-macsec-pl-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats.TxSaStats, self).__init__()

                                        self.yang_name = "tx-sa-stats"
                                        self.yang_parent_name = "es200-stats"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.out_octets_encrypted_protected1 = YLeaf(YType.uint64, "out-octets-encrypted-protected1")

                                        self.out_pkts_encrypted_protected = YLeaf(YType.uint64, "out-pkts-encrypted-protected")

                                        self.out_pkts_too_long = YLeaf(YType.uint64, "out-pkts-too-long")
                                        self._segment_path = lambda: "tx-sa-stats"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats.TxSaStats, ['out_octets_encrypted_protected1', 'out_pkts_encrypted_protected', 'out_pkts_too_long'], name, value)


                                class TxScMacsecStats(Entity):
                                    """
                                    Tx SC Macsec Stats
                                    
                                    .. attribute:: out_pkts_sa_not_in_use
                                    
                                    	Packets received with SA not in use
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'crypto-macsec-pl-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats.TxScMacsecStats, self).__init__()

                                        self.yang_name = "tx-sc-macsec-stats"
                                        self.yang_parent_name = "es200-stats"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.out_pkts_sa_not_in_use = YLeaf(YType.uint64, "out-pkts-sa-not-in-use")
                                        self._segment_path = lambda: "tx-sc-macsec-stats"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats.TxScMacsecStats, ['out_pkts_sa_not_in_use'], name, value)


                            class MsfpgaStats(Entity):
                                """
                                MSFPGA Stats
                                
                                .. attribute:: rx_interface_macsec_stats
                                
                                	Rx interface Macsec Stats
                                	**type**\:   :py:class:`RxInterfaceMacsecStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.MsfpgaStats.RxInterfaceMacsecStats>`
                                
                                .. attribute:: rx_sa_stats
                                
                                	Rx SA Stats
                                	**type**\:   :py:class:`RxSaStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.MsfpgaStats.RxSaStats>`
                                
                                .. attribute:: tx_interface_macsec_stats
                                
                                	Tx interface Macsec Stats
                                	**type**\:   :py:class:`TxInterfaceMacsecStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.MsfpgaStats.TxInterfaceMacsecStats>`
                                
                                .. attribute:: tx_sa_stats
                                
                                	Tx SA Stats
                                	**type**\:   :py:class:`TxSaStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.MsfpgaStats.TxSaStats>`
                                
                                

                                """

                                _prefix = 'crypto-macsec-pl-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.MsfpgaStats, self).__init__()

                                    self.yang_name = "msfpga-stats"
                                    self.yang_parent_name = "ext"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {"rx-interface-macsec-stats" : ("rx_interface_macsec_stats", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.MsfpgaStats.RxInterfaceMacsecStats), "rx-sa-stats" : ("rx_sa_stats", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.MsfpgaStats.RxSaStats), "tx-interface-macsec-stats" : ("tx_interface_macsec_stats", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.MsfpgaStats.TxInterfaceMacsecStats), "tx-sa-stats" : ("tx_sa_stats", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.MsfpgaStats.TxSaStats)}
                                    self._child_list_classes = {}

                                    self.rx_interface_macsec_stats = MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.MsfpgaStats.RxInterfaceMacsecStats()
                                    self.rx_interface_macsec_stats.parent = self
                                    self._children_name_map["rx_interface_macsec_stats"] = "rx-interface-macsec-stats"
                                    self._children_yang_names.add("rx-interface-macsec-stats")

                                    self.rx_sa_stats = MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.MsfpgaStats.RxSaStats()
                                    self.rx_sa_stats.parent = self
                                    self._children_name_map["rx_sa_stats"] = "rx-sa-stats"
                                    self._children_yang_names.add("rx-sa-stats")

                                    self.tx_interface_macsec_stats = MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.MsfpgaStats.TxInterfaceMacsecStats()
                                    self.tx_interface_macsec_stats.parent = self
                                    self._children_name_map["tx_interface_macsec_stats"] = "tx-interface-macsec-stats"
                                    self._children_yang_names.add("tx-interface-macsec-stats")

                                    self.tx_sa_stats = MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.MsfpgaStats.TxSaStats()
                                    self.tx_sa_stats.parent = self
                                    self._children_name_map["tx_sa_stats"] = "tx-sa-stats"
                                    self._children_yang_names.add("tx-sa-stats")
                                    self._segment_path = lambda: "msfpga-stats"


                                class RxInterfaceMacsecStats(Entity):
                                    """
                                    Rx interface Macsec Stats
                                    
                                    .. attribute:: in_pkt_bad_tag
                                    
                                    	Rx Pkts Bad tag
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkt_no_sci
                                    
                                    	Rx Pkts No Sci
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkt_notag
                                    
                                    	Rx Pkts Notag
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkt_overrun
                                    
                                    	Rx Pkts Over Run
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkt_tagged
                                    
                                    	Rx Pkts Tagged
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkt_uncontrolled
                                    
                                    	Rx Pkts Uncontrolled
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkt_unknown_sci
                                    
                                    	Rx Pkts Unknown Sci
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkt_untagged
                                    
                                    	Rx Pkts Untagged
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'crypto-macsec-pl-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.MsfpgaStats.RxInterfaceMacsecStats, self).__init__()

                                        self.yang_name = "rx-interface-macsec-stats"
                                        self.yang_parent_name = "msfpga-stats"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.in_pkt_bad_tag = YLeaf(YType.uint64, "in-pkt-bad-tag")

                                        self.in_pkt_no_sci = YLeaf(YType.uint64, "in-pkt-no-sci")

                                        self.in_pkt_notag = YLeaf(YType.uint64, "in-pkt-notag")

                                        self.in_pkt_overrun = YLeaf(YType.uint64, "in-pkt-overrun")

                                        self.in_pkt_tagged = YLeaf(YType.uint64, "in-pkt-tagged")

                                        self.in_pkt_uncontrolled = YLeaf(YType.uint64, "in-pkt-uncontrolled")

                                        self.in_pkt_unknown_sci = YLeaf(YType.uint64, "in-pkt-unknown-sci")

                                        self.in_pkt_untagged = YLeaf(YType.uint64, "in-pkt-untagged")
                                        self._segment_path = lambda: "rx-interface-macsec-stats"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.MsfpgaStats.RxInterfaceMacsecStats, ['in_pkt_bad_tag', 'in_pkt_no_sci', 'in_pkt_notag', 'in_pkt_overrun', 'in_pkt_tagged', 'in_pkt_uncontrolled', 'in_pkt_unknown_sci', 'in_pkt_untagged'], name, value)


                                class RxSaStats(Entity):
                                    """
                                    Rx SA Stats
                                    
                                    .. attribute:: in_octets_decrypted
                                    
                                    	Rx Octets Decrypted
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_octets_validated
                                    
                                    	Rx Octets Validated
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkts_delayed
                                    
                                    	Rx Pkts Delayed
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkts_invalid
                                    
                                    	Rx Pkts Invalid
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkts_late
                                    
                                    	Rx Pkts Late
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkts_not_using_sa
                                    
                                    	Rx Pkts Not Using SA
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkts_not_valid
                                    
                                    	Rx Pkts Not Valid
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkts_ok
                                    
                                    	Rx Pkts OK
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkts_unchecked
                                    
                                    	Rx Pkts Unchecked
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkts_unused_sa
                                    
                                    	Rx Pkts Unused SA
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'crypto-macsec-pl-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.MsfpgaStats.RxSaStats, self).__init__()

                                        self.yang_name = "rx-sa-stats"
                                        self.yang_parent_name = "msfpga-stats"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.in_octets_decrypted = YLeaf(YType.uint64, "in-octets-decrypted")

                                        self.in_octets_validated = YLeaf(YType.uint64, "in-octets-validated")

                                        self.in_pkts_delayed = YLeaf(YType.uint64, "in-pkts-delayed")

                                        self.in_pkts_invalid = YLeaf(YType.uint64, "in-pkts-invalid")

                                        self.in_pkts_late = YLeaf(YType.uint64, "in-pkts-late")

                                        self.in_pkts_not_using_sa = YLeaf(YType.uint64, "in-pkts-not-using-sa")

                                        self.in_pkts_not_valid = YLeaf(YType.uint64, "in-pkts-not-valid")

                                        self.in_pkts_ok = YLeaf(YType.uint64, "in-pkts-ok")

                                        self.in_pkts_unchecked = YLeaf(YType.uint64, "in-pkts-unchecked")

                                        self.in_pkts_unused_sa = YLeaf(YType.uint64, "in-pkts-unused-sa")
                                        self._segment_path = lambda: "rx-sa-stats"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.MsfpgaStats.RxSaStats, ['in_octets_decrypted', 'in_octets_validated', 'in_pkts_delayed', 'in_pkts_invalid', 'in_pkts_late', 'in_pkts_not_using_sa', 'in_pkts_not_valid', 'in_pkts_ok', 'in_pkts_unchecked', 'in_pkts_unused_sa'], name, value)


                                class TxInterfaceMacsecStats(Entity):
                                    """
                                    Tx interface Macsec Stats
                                    
                                    .. attribute:: out_pkt_too_long
                                    
                                    	Tx Pkts Too Long
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_pkt_uncontrolled
                                    
                                    	Tx Pkts Uncontrolled
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_pkt_untagged
                                    
                                    	Tx Pkts Untagged
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'crypto-macsec-pl-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.MsfpgaStats.TxInterfaceMacsecStats, self).__init__()

                                        self.yang_name = "tx-interface-macsec-stats"
                                        self.yang_parent_name = "msfpga-stats"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.out_pkt_too_long = YLeaf(YType.uint64, "out-pkt-too-long")

                                        self.out_pkt_uncontrolled = YLeaf(YType.uint64, "out-pkt-uncontrolled")

                                        self.out_pkt_untagged = YLeaf(YType.uint64, "out-pkt-untagged")
                                        self._segment_path = lambda: "tx-interface-macsec-stats"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.MsfpgaStats.TxInterfaceMacsecStats, ['out_pkt_too_long', 'out_pkt_uncontrolled', 'out_pkt_untagged'], name, value)


                                class TxSaStats(Entity):
                                    """
                                    Tx SA Stats
                                    
                                    .. attribute:: out_octets_encrypted
                                    
                                    	Tx Octets Encrypted
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_octets_protected
                                    
                                    	Tx Octets Protected
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_pkts_encrypted
                                    
                                    	Tx Pkts Encrypted
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_pkts_protected
                                    
                                    	Tx Pkts Protected
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'crypto-macsec-pl-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.MsfpgaStats.TxSaStats, self).__init__()

                                        self.yang_name = "tx-sa-stats"
                                        self.yang_parent_name = "msfpga-stats"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.out_octets_encrypted = YLeaf(YType.uint64, "out-octets-encrypted")

                                        self.out_octets_protected = YLeaf(YType.uint64, "out-octets-protected")

                                        self.out_pkts_encrypted = YLeaf(YType.uint64, "out-pkts-encrypted")

                                        self.out_pkts_protected = YLeaf(YType.uint64, "out-pkts-protected")
                                        self._segment_path = lambda: "tx-sa-stats"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.MsfpgaStats.TxSaStats, ['out_octets_encrypted', 'out_octets_protected', 'out_pkts_encrypted', 'out_pkts_protected'], name, value)


                            class XlfpgaStats(Entity):
                                """
                                XLFPGA Stats
                                
                                .. attribute:: macsec_rx_stats
                                
                                	Rx SC and SA Level Stats
                                	**type**\:   :py:class:`MacsecRxStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.XlfpgaStats.MacsecRxStats>`
                                
                                .. attribute:: macsec_tx_stats
                                
                                	Tx SC and SA Level Stats
                                	**type**\:   :py:class:`MacsecTxStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.XlfpgaStats.MacsecTxStats>`
                                
                                

                                """

                                _prefix = 'crypto-macsec-pl-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.XlfpgaStats, self).__init__()

                                    self.yang_name = "xlfpga-stats"
                                    self.yang_parent_name = "ext"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {"macsec-rx-stats" : ("macsec_rx_stats", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.XlfpgaStats.MacsecRxStats), "macsec-tx-stats" : ("macsec_tx_stats", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.XlfpgaStats.MacsecTxStats)}
                                    self._child_list_classes = {}

                                    self.macsec_rx_stats = MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.XlfpgaStats.MacsecRxStats()
                                    self.macsec_rx_stats.parent = self
                                    self._children_name_map["macsec_rx_stats"] = "macsec-rx-stats"
                                    self._children_yang_names.add("macsec-rx-stats")

                                    self.macsec_tx_stats = MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.XlfpgaStats.MacsecTxStats()
                                    self.macsec_tx_stats.parent = self
                                    self._children_name_map["macsec_tx_stats"] = "macsec-tx-stats"
                                    self._children_yang_names.add("macsec-tx-stats")
                                    self._segment_path = lambda: "xlfpga-stats"


                                class MacsecRxStats(Entity):
                                    """
                                    Rx SC and SA Level Stats
                                    
                                    .. attribute:: rx_sa_stat
                                    
                                    	Rx SA Level Stats
                                    	**type**\: list of    :py:class:`RxSaStat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.XlfpgaStats.MacsecRxStats.RxSaStat>`
                                    
                                    .. attribute:: sc_bad_tag_pkts
                                    
                                    	Rx Bad Tag Packets
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_bypass_pkts
                                    
                                    	Rx Bypass Packets
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_decrypted_octets
                                    
                                    	Rx Octets Decrypted
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_delayed_pkts
                                    
                                    	Rx Delayed Pkts
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_dropped_pkts
                                    
                                    	Rx Dropped Packets
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_eapol_pkts
                                    
                                    	Rx Eapol Packets
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_invalid_pkts
                                    
                                    	Rx Pkts Invalid
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_late_pkts
                                    
                                    	Rx Late Pkts
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_no_sci_pkts
                                    
                                    	Rx No SCI Pkts
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_no_tag_pkts
                                    
                                    	Rx No Tag Packets
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_not_using_pkts
                                    
                                    	Rx Pkts Not Using SA
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_not_valid_pkts
                                    
                                    	Rx Not Valid Pkts
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_ok_pkts
                                    
                                    	Rx Pkts Ok
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_overrun_pkts
                                    
                                    	Rx Overrun Pkts
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_unchecked_pkts
                                    
                                    	Rx Unchecked Pkts
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_unknown_sci_pkts
                                    
                                    	Rx Unknown SCI Pkts
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_untagged_pkts
                                    
                                    	Rx Untagged Packets
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_unused_pkts
                                    
                                    	Rx Pkts Unused SA
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'crypto-macsec-pl-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.XlfpgaStats.MacsecRxStats, self).__init__()

                                        self.yang_name = "macsec-rx-stats"
                                        self.yang_parent_name = "xlfpga-stats"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {"rx-sa-stat" : ("rx_sa_stat", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.XlfpgaStats.MacsecRxStats.RxSaStat)}

                                        self.sc_bad_tag_pkts = YLeaf(YType.uint64, "sc-bad-tag-pkts")

                                        self.sc_bypass_pkts = YLeaf(YType.uint64, "sc-bypass-pkts")

                                        self.sc_decrypted_octets = YLeaf(YType.uint64, "sc-decrypted-octets")

                                        self.sc_delayed_pkts = YLeaf(YType.uint64, "sc-delayed-pkts")

                                        self.sc_dropped_pkts = YLeaf(YType.uint64, "sc-dropped-pkts")

                                        self.sc_eapol_pkts = YLeaf(YType.uint64, "sc-eapol-pkts")

                                        self.sc_invalid_pkts = YLeaf(YType.uint64, "sc-invalid-pkts")

                                        self.sc_late_pkts = YLeaf(YType.uint64, "sc-late-pkts")

                                        self.sc_no_sci_pkts = YLeaf(YType.uint64, "sc-no-sci-pkts")

                                        self.sc_no_tag_pkts = YLeaf(YType.uint64, "sc-no-tag-pkts")

                                        self.sc_not_using_pkts = YLeaf(YType.uint64, "sc-not-using-pkts")

                                        self.sc_not_valid_pkts = YLeaf(YType.uint64, "sc-not-valid-pkts")

                                        self.sc_ok_pkts = YLeaf(YType.uint64, "sc-ok-pkts")

                                        self.sc_overrun_pkts = YLeaf(YType.uint64, "sc-overrun-pkts")

                                        self.sc_unchecked_pkts = YLeaf(YType.uint64, "sc-unchecked-pkts")

                                        self.sc_unknown_sci_pkts = YLeaf(YType.uint64, "sc-unknown-sci-pkts")

                                        self.sc_untagged_pkts = YLeaf(YType.uint64, "sc-untagged-pkts")

                                        self.sc_unused_pkts = YLeaf(YType.uint64, "sc-unused-pkts")

                                        self.rx_sa_stat = YList(self)
                                        self._segment_path = lambda: "macsec-rx-stats"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.XlfpgaStats.MacsecRxStats, ['sc_bad_tag_pkts', 'sc_bypass_pkts', 'sc_decrypted_octets', 'sc_delayed_pkts', 'sc_dropped_pkts', 'sc_eapol_pkts', 'sc_invalid_pkts', 'sc_late_pkts', 'sc_no_sci_pkts', 'sc_no_tag_pkts', 'sc_not_using_pkts', 'sc_not_valid_pkts', 'sc_ok_pkts', 'sc_overrun_pkts', 'sc_unchecked_pkts', 'sc_unknown_sci_pkts', 'sc_untagged_pkts', 'sc_unused_pkts'], name, value)


                                    class RxSaStat(Entity):
                                        """
                                        Rx SA Level Stats
                                        
                                        .. attribute:: an
                                        
                                        	Current Rx AN
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: sa_invalid_pkts
                                        
                                        	Rx Invalid Pkts for current AN
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: sa_not_using_pkts
                                        
                                        	Rx Pkts not using SA for Current AN
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: sa_not_valid_pkts
                                        
                                        	Rx Not Valid Pkts for Current AN
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: sa_ok_pkts
                                        
                                        	Rx Ok Pkts for Current AN
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: sa_unused_pkts
                                        
                                        	Rx Pkts Unused Pkts for Current AN
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        

                                        """

                                        _prefix = 'crypto-macsec-pl-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.XlfpgaStats.MacsecRxStats.RxSaStat, self).__init__()

                                            self.yang_name = "rx-sa-stat"
                                            self.yang_parent_name = "macsec-rx-stats"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.an = YLeaf(YType.uint64, "an")

                                            self.sa_invalid_pkts = YLeaf(YType.uint64, "sa-invalid-pkts")

                                            self.sa_not_using_pkts = YLeaf(YType.uint64, "sa-not-using-pkts")

                                            self.sa_not_valid_pkts = YLeaf(YType.uint64, "sa-not-valid-pkts")

                                            self.sa_ok_pkts = YLeaf(YType.uint64, "sa-ok-pkts")

                                            self.sa_unused_pkts = YLeaf(YType.uint64, "sa-unused-pkts")
                                            self._segment_path = lambda: "rx-sa-stat"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.XlfpgaStats.MacsecRxStats.RxSaStat, ['an', 'sa_invalid_pkts', 'sa_not_using_pkts', 'sa_not_valid_pkts', 'sa_ok_pkts', 'sa_unused_pkts'], name, value)


                                class MacsecTxStats(Entity):
                                    """
                                    Tx SC and SA Level Stats
                                    
                                    .. attribute:: current_an
                                    
                                    	Current Tx AN
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sa_encrypted_pkts
                                    
                                    	Current Tx SA Encrypted Packets
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_bypass_pkts
                                    
                                    	Tx Bypass Packets
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_dropped_pkts
                                    
                                    	Tx Dropped Packets
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_eapol_pkts
                                    
                                    	Tx Eapol Packets
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_encrypted_octets
                                    
                                    	Tx Octets Encrypted
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_encrypted_pkts
                                    
                                    	Tx packets Encrypted
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_overrun_pkts
                                    
                                    	Tx Overrun Packets
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_toolong_pkts
                                    
                                    	Tx Pkts Too Long
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_untagged_pkts
                                    
                                    	Tx Untagged Packets
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'crypto-macsec-pl-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.XlfpgaStats.MacsecTxStats, self).__init__()

                                        self.yang_name = "macsec-tx-stats"
                                        self.yang_parent_name = "xlfpga-stats"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.current_an = YLeaf(YType.uint64, "current-an")

                                        self.sa_encrypted_pkts = YLeaf(YType.uint64, "sa-encrypted-pkts")

                                        self.sc_bypass_pkts = YLeaf(YType.uint64, "sc-bypass-pkts")

                                        self.sc_dropped_pkts = YLeaf(YType.uint64, "sc-dropped-pkts")

                                        self.sc_eapol_pkts = YLeaf(YType.uint64, "sc-eapol-pkts")

                                        self.sc_encrypted_octets = YLeaf(YType.uint64, "sc-encrypted-octets")

                                        self.sc_encrypted_pkts = YLeaf(YType.uint64, "sc-encrypted-pkts")

                                        self.sc_overrun_pkts = YLeaf(YType.uint64, "sc-overrun-pkts")

                                        self.sc_toolong_pkts = YLeaf(YType.uint64, "sc-toolong-pkts")

                                        self.sc_untagged_pkts = YLeaf(YType.uint64, "sc-untagged-pkts")
                                        self._segment_path = lambda: "macsec-tx-stats"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.XlfpgaStats.MacsecTxStats, ['current_an', 'sa_encrypted_pkts', 'sc_bypass_pkts', 'sc_dropped_pkts', 'sc_eapol_pkts', 'sc_encrypted_octets', 'sc_encrypted_pkts', 'sc_overrun_pkts', 'sc_toolong_pkts', 'sc_untagged_pkts'], name, value)


                    class SwStatistics(Entity):
                        """
                        The Software Statistics
                        
                        .. attribute:: ext
                        
                        	ext
                        	**type**\:   :py:class:`Ext <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext>`
                        
                        

                        """

                        _prefix = 'crypto-macsec-pl-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics, self).__init__()

                            self.yang_name = "sw-statistics"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"ext" : ("ext", MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext)}
                            self._child_list_classes = {}

                            self.ext = MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext()
                            self.ext.parent = self
                            self._children_name_map["ext"] = "ext"
                            self._children_yang_names.add("ext")
                            self._segment_path = lambda: "sw-statistics"


                        class Ext(Entity):
                            """
                            ext
                            
                            .. attribute:: es200_stats
                            
                            	ES200 Stats
                            	**type**\:   :py:class:`Es200Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats>`
                            
                            .. attribute:: msfpga_stats
                            
                            	MSFPGA Stats
                            	**type**\:   :py:class:`MsfpgaStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.MsfpgaStats>`
                            
                            .. attribute:: type
                            
                            	type
                            	**type**\:   :py:class:`MacsecCard <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecCard>`
                            
                            .. attribute:: xlfpga_stats
                            
                            	XLFPGA Stats
                            	**type**\:   :py:class:`XlfpgaStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.XlfpgaStats>`
                            
                            

                            """

                            _prefix = 'crypto-macsec-pl-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext, self).__init__()

                                self.yang_name = "ext"
                                self.yang_parent_name = "sw-statistics"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"es200-stats" : ("es200_stats", MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats), "msfpga-stats" : ("msfpga_stats", MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.MsfpgaStats), "xlfpga-stats" : ("xlfpga_stats", MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.XlfpgaStats)}
                                self._child_list_classes = {}

                                self.type = YLeaf(YType.enumeration, "type")

                                self.es200_stats = MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats()
                                self.es200_stats.parent = self
                                self._children_name_map["es200_stats"] = "es200-stats"
                                self._children_yang_names.add("es200-stats")

                                self.msfpga_stats = MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.MsfpgaStats()
                                self.msfpga_stats.parent = self
                                self._children_name_map["msfpga_stats"] = "msfpga-stats"
                                self._children_yang_names.add("msfpga-stats")

                                self.xlfpga_stats = MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.XlfpgaStats()
                                self.xlfpga_stats.parent = self
                                self._children_name_map["xlfpga_stats"] = "xlfpga-stats"
                                self._children_yang_names.add("xlfpga-stats")
                                self._segment_path = lambda: "ext"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext, ['type'], name, value)


                            class Es200Stats(Entity):
                                """
                                ES200 Stats
                                
                                .. attribute:: rx_interface_macsec_stats
                                
                                	Rx interface Macsec Stats
                                	**type**\:   :py:class:`RxInterfaceMacsecStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats.RxInterfaceMacsecStats>`
                                
                                .. attribute:: rx_port_stats
                                
                                	Port level RX Stats
                                	**type**\:   :py:class:`RxPortStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats.RxPortStats>`
                                
                                .. attribute:: rx_sa_stats
                                
                                	Rx SA Stats
                                	**type**\:   :py:class:`RxSaStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats.RxSaStats>`
                                
                                .. attribute:: rx_sc_macsec_stats
                                
                                	Rx SC Macsec Stats
                                	**type**\:   :py:class:`RxScMacsecStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats.RxScMacsecStats>`
                                
                                .. attribute:: tx_interface_macsec_stats
                                
                                	Tx interface Macsec Stats
                                	**type**\:   :py:class:`TxInterfaceMacsecStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats.TxInterfaceMacsecStats>`
                                
                                .. attribute:: tx_port_stats
                                
                                	Port level TX Stats
                                	**type**\:   :py:class:`TxPortStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats.TxPortStats>`
                                
                                .. attribute:: tx_sa_stats
                                
                                	Tx SA Stats
                                	**type**\:   :py:class:`TxSaStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats.TxSaStats>`
                                
                                .. attribute:: tx_sc_macsec_stats
                                
                                	Tx SC Macsec Stats
                                	**type**\:   :py:class:`TxScMacsecStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats.TxScMacsecStats>`
                                
                                

                                """

                                _prefix = 'crypto-macsec-pl-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats, self).__init__()

                                    self.yang_name = "es200-stats"
                                    self.yang_parent_name = "ext"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {"rx-interface-macsec-stats" : ("rx_interface_macsec_stats", MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats.RxInterfaceMacsecStats), "rx-port-stats" : ("rx_port_stats", MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats.RxPortStats), "rx-sa-stats" : ("rx_sa_stats", MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats.RxSaStats), "rx-sc-macsec-stats" : ("rx_sc_macsec_stats", MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats.RxScMacsecStats), "tx-interface-macsec-stats" : ("tx_interface_macsec_stats", MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats.TxInterfaceMacsecStats), "tx-port-stats" : ("tx_port_stats", MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats.TxPortStats), "tx-sa-stats" : ("tx_sa_stats", MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats.TxSaStats), "tx-sc-macsec-stats" : ("tx_sc_macsec_stats", MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats.TxScMacsecStats)}
                                    self._child_list_classes = {}

                                    self.rx_interface_macsec_stats = MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats.RxInterfaceMacsecStats()
                                    self.rx_interface_macsec_stats.parent = self
                                    self._children_name_map["rx_interface_macsec_stats"] = "rx-interface-macsec-stats"
                                    self._children_yang_names.add("rx-interface-macsec-stats")

                                    self.rx_port_stats = MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats.RxPortStats()
                                    self.rx_port_stats.parent = self
                                    self._children_name_map["rx_port_stats"] = "rx-port-stats"
                                    self._children_yang_names.add("rx-port-stats")

                                    self.rx_sa_stats = MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats.RxSaStats()
                                    self.rx_sa_stats.parent = self
                                    self._children_name_map["rx_sa_stats"] = "rx-sa-stats"
                                    self._children_yang_names.add("rx-sa-stats")

                                    self.rx_sc_macsec_stats = MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats.RxScMacsecStats()
                                    self.rx_sc_macsec_stats.parent = self
                                    self._children_name_map["rx_sc_macsec_stats"] = "rx-sc-macsec-stats"
                                    self._children_yang_names.add("rx-sc-macsec-stats")

                                    self.tx_interface_macsec_stats = MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats.TxInterfaceMacsecStats()
                                    self.tx_interface_macsec_stats.parent = self
                                    self._children_name_map["tx_interface_macsec_stats"] = "tx-interface-macsec-stats"
                                    self._children_yang_names.add("tx-interface-macsec-stats")

                                    self.tx_port_stats = MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats.TxPortStats()
                                    self.tx_port_stats.parent = self
                                    self._children_name_map["tx_port_stats"] = "tx-port-stats"
                                    self._children_yang_names.add("tx-port-stats")

                                    self.tx_sa_stats = MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats.TxSaStats()
                                    self.tx_sa_stats.parent = self
                                    self._children_name_map["tx_sa_stats"] = "tx-sa-stats"
                                    self._children_yang_names.add("tx-sa-stats")

                                    self.tx_sc_macsec_stats = MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats.TxScMacsecStats()
                                    self.tx_sc_macsec_stats.parent = self
                                    self._children_name_map["tx_sc_macsec_stats"] = "tx-sc-macsec-stats"
                                    self._children_yang_names.add("tx-sc-macsec-stats")
                                    self._segment_path = lambda: "es200-stats"


                                class RxInterfaceMacsecStats(Entity):
                                    """
                                    Rx interface Macsec Stats
                                    
                                    .. attribute:: in_bcast_pkts_ctrl
                                    
                                    	Broadcast pkts rx on controlled port
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_bcast_pkts_unctrl
                                    
                                    	Broadcast pkts rx on uncontrolled port
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_drop_pkts_class
                                    
                                    	Packets dropped due to overflow in classification pipeline
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_drop_pkts_data
                                    
                                    	Packets dropped due to overflow in processing pipeline
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_mcast_pkts_ctrl
                                    
                                    	Multicast pkts rx on controlled port
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_mcast_pkts_unctrl
                                    
                                    	Multicast pkts rx on uncontrolled port
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_octets_ctrl
                                    
                                    	Octets rx on controlled port
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_octets_unctrl
                                    
                                    	Octets rx on uncontrolled port
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkt_bad_tag
                                    
                                    	ingress frames received with an invalid MACSec tag or ICV                                       added with next one gives InPktsSCIMiss
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkt_ctrl
                                    
                                    	ingress packet that is classified as control packet
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkt_no_sci
                                    
                                    	correctly tagged ingress frames for which no valid SC found &                                 validateFrames is strict
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkt_no_tag
                                    
                                    	ingress packet untagged & validateFrames is strict
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkts_tagged_ctrl
                                    
                                    	ingress packets that are control or KaY packets
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkts_unknown_sci
                                    
                                    	correctly tagged ingress frames for which no valid SC found &                                 validateFrames is !strict
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkts_untagged
                                    
                                    	ingress packet untagged & validateFrames is  !strict
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_rx_drop_pkts_ctrl
                                    
                                    	Data pkts dropped due to overrun
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_rx_drop_pkts_unctrl
                                    
                                    	Control pkts dropped due to overrun
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_rx_error_pkts_ctrl
                                    
                                    	Data pkts error\-terminated due to overrun
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_rx_error_pkts_unctrl
                                    
                                    	Control pkts error\-terminated due to overrun
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_ucast_pkts_ctrl
                                    
                                    	Unicast pkts rx on controlled port
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_ucast_pkts_unctrl
                                    
                                    	Unicast pkts rx on uncontrolled port
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: transform_error_pkts
                                    
                                    	counter to count internal errors in the MACSec core
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'crypto-macsec-pl-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats.RxInterfaceMacsecStats, self).__init__()

                                        self.yang_name = "rx-interface-macsec-stats"
                                        self.yang_parent_name = "es200-stats"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.in_bcast_pkts_ctrl = YLeaf(YType.uint64, "in-bcast-pkts-ctrl")

                                        self.in_bcast_pkts_unctrl = YLeaf(YType.uint64, "in-bcast-pkts-unctrl")

                                        self.in_drop_pkts_class = YLeaf(YType.uint64, "in-drop-pkts-class")

                                        self.in_drop_pkts_data = YLeaf(YType.uint64, "in-drop-pkts-data")

                                        self.in_mcast_pkts_ctrl = YLeaf(YType.uint64, "in-mcast-pkts-ctrl")

                                        self.in_mcast_pkts_unctrl = YLeaf(YType.uint64, "in-mcast-pkts-unctrl")

                                        self.in_octets_ctrl = YLeaf(YType.uint64, "in-octets-ctrl")

                                        self.in_octets_unctrl = YLeaf(YType.uint64, "in-octets-unctrl")

                                        self.in_pkt_bad_tag = YLeaf(YType.uint64, "in-pkt-bad-tag")

                                        self.in_pkt_ctrl = YLeaf(YType.uint64, "in-pkt-ctrl")

                                        self.in_pkt_no_sci = YLeaf(YType.uint64, "in-pkt-no-sci")

                                        self.in_pkt_no_tag = YLeaf(YType.uint64, "in-pkt-no-tag")

                                        self.in_pkts_tagged_ctrl = YLeaf(YType.uint64, "in-pkts-tagged-ctrl")

                                        self.in_pkts_unknown_sci = YLeaf(YType.uint64, "in-pkts-unknown-sci")

                                        self.in_pkts_untagged = YLeaf(YType.uint64, "in-pkts-untagged")

                                        self.in_rx_drop_pkts_ctrl = YLeaf(YType.uint64, "in-rx-drop-pkts-ctrl")

                                        self.in_rx_drop_pkts_unctrl = YLeaf(YType.uint64, "in-rx-drop-pkts-unctrl")

                                        self.in_rx_error_pkts_ctrl = YLeaf(YType.uint64, "in-rx-error-pkts-ctrl")

                                        self.in_rx_error_pkts_unctrl = YLeaf(YType.uint64, "in-rx-error-pkts-unctrl")

                                        self.in_ucast_pkts_ctrl = YLeaf(YType.uint64, "in-ucast-pkts-ctrl")

                                        self.in_ucast_pkts_unctrl = YLeaf(YType.uint64, "in-ucast-pkts-unctrl")

                                        self.transform_error_pkts = YLeaf(YType.uint64, "transform-error-pkts")
                                        self._segment_path = lambda: "rx-interface-macsec-stats"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats.RxInterfaceMacsecStats, ['in_bcast_pkts_ctrl', 'in_bcast_pkts_unctrl', 'in_drop_pkts_class', 'in_drop_pkts_data', 'in_mcast_pkts_ctrl', 'in_mcast_pkts_unctrl', 'in_octets_ctrl', 'in_octets_unctrl', 'in_pkt_bad_tag', 'in_pkt_ctrl', 'in_pkt_no_sci', 'in_pkt_no_tag', 'in_pkts_tagged_ctrl', 'in_pkts_unknown_sci', 'in_pkts_untagged', 'in_rx_drop_pkts_ctrl', 'in_rx_drop_pkts_unctrl', 'in_rx_error_pkts_ctrl', 'in_rx_error_pkts_unctrl', 'in_ucast_pkts_ctrl', 'in_ucast_pkts_unctrl', 'transform_error_pkts'], name, value)


                                class RxPortStats(Entity):
                                    """
                                    Port level RX Stats
                                    
                                    .. attribute:: flow_miss
                                    
                                    	Pkts matching none of flow entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: multi_flow_match
                                    
                                    	Pkts matching multiple flow entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: parser_dropped
                                    
                                    	Pkts dropped by header parser as invalid
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: pkts_ctrl
                                    
                                    	Control pkts forwarded
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: pkts_data
                                    
                                    	Data pkts forwarded
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: pkts_dropped
                                    
                                    	Pkts dropped by classifier
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: pkts_err_in
                                    
                                    	Pkts received with an error indication
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'crypto-macsec-pl-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats.RxPortStats, self).__init__()

                                        self.yang_name = "rx-port-stats"
                                        self.yang_parent_name = "es200-stats"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.flow_miss = YLeaf(YType.uint64, "flow-miss")

                                        self.multi_flow_match = YLeaf(YType.uint64, "multi-flow-match")

                                        self.parser_dropped = YLeaf(YType.uint64, "parser-dropped")

                                        self.pkts_ctrl = YLeaf(YType.uint64, "pkts-ctrl")

                                        self.pkts_data = YLeaf(YType.uint64, "pkts-data")

                                        self.pkts_dropped = YLeaf(YType.uint64, "pkts-dropped")

                                        self.pkts_err_in = YLeaf(YType.uint64, "pkts-err-in")
                                        self._segment_path = lambda: "rx-port-stats"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats.RxPortStats, ['flow_miss', 'multi_flow_match', 'parser_dropped', 'pkts_ctrl', 'pkts_data', 'pkts_dropped', 'pkts_err_in'], name, value)


                                class RxSaStats(Entity):
                                    """
                                    Rx SA Stats
                                    
                                    .. attribute:: in_octets_decrypted_validated1
                                    
                                    	octets1 decrypted/validated
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_octets_validated
                                    
                                    	octets validated
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkts_delayed
                                    
                                    	PN of packet outside replay window & validateFrames !strict
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkts_invalid
                                    
                                    	packet not valid & validateFrames !strict
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkts_late
                                    
                                    	PN of packet outside replay window & validateFrames strict
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkts_not_using_sa
                                    
                                    	packet assigned to SA not in use & validateFrames strict
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkts_not_valid
                                    
                                    	packet not valid & validateFrames strict
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkts_ok
                                    
                                    	packets with no error
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkts_unchecked
                                    
                                    	frame not valid & validateFrames disabled
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkts_unused_sa
                                    
                                    	packet assigned to SA not in use & validateFrames !strict
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'crypto-macsec-pl-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats.RxSaStats, self).__init__()

                                        self.yang_name = "rx-sa-stats"
                                        self.yang_parent_name = "es200-stats"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.in_octets_decrypted_validated1 = YLeaf(YType.uint64, "in-octets-decrypted-validated1")

                                        self.in_octets_validated = YLeaf(YType.uint64, "in-octets-validated")

                                        self.in_pkts_delayed = YLeaf(YType.uint64, "in-pkts-delayed")

                                        self.in_pkts_invalid = YLeaf(YType.uint64, "in-pkts-invalid")

                                        self.in_pkts_late = YLeaf(YType.uint64, "in-pkts-late")

                                        self.in_pkts_not_using_sa = YLeaf(YType.uint64, "in-pkts-not-using-sa")

                                        self.in_pkts_not_valid = YLeaf(YType.uint64, "in-pkts-not-valid")

                                        self.in_pkts_ok = YLeaf(YType.uint64, "in-pkts-ok")

                                        self.in_pkts_unchecked = YLeaf(YType.uint64, "in-pkts-unchecked")

                                        self.in_pkts_unused_sa = YLeaf(YType.uint64, "in-pkts-unused-sa")
                                        self._segment_path = lambda: "rx-sa-stats"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats.RxSaStats, ['in_octets_decrypted_validated1', 'in_octets_validated', 'in_pkts_delayed', 'in_pkts_invalid', 'in_pkts_late', 'in_pkts_not_using_sa', 'in_pkts_not_valid', 'in_pkts_ok', 'in_pkts_unchecked', 'in_pkts_unused_sa'], name, value)


                                class RxScMacsecStats(Entity):
                                    """
                                    Rx SC Macsec Stats
                                    
                                    .. attribute:: in_pkts_sa_not_in_use
                                    
                                    	Packets received with SA not in use
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'crypto-macsec-pl-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats.RxScMacsecStats, self).__init__()

                                        self.yang_name = "rx-sc-macsec-stats"
                                        self.yang_parent_name = "es200-stats"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.in_pkts_sa_not_in_use = YLeaf(YType.uint64, "in-pkts-sa-not-in-use")
                                        self._segment_path = lambda: "rx-sc-macsec-stats"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats.RxScMacsecStats, ['in_pkts_sa_not_in_use'], name, value)


                                class TxInterfaceMacsecStats(Entity):
                                    """
                                    Tx interface Macsec Stats
                                    
                                    .. attribute:: out_bcast_pkts_ctrl
                                    
                                    	Broadcast pkts tx on controlled port
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_bcast_pkts_unctrl
                                    
                                    	Broadcast pkts tx on uncontrolled port
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_drop_pkts_class
                                    
                                    	Packets dropped due to overflow in classification pipeline
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_drop_pkts_data
                                    
                                    	Packets dropped due to overflow in  processing pipeline
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_mcast_pkts_ctrl
                                    
                                    	Multicast pkts tx on controlled port
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_mcast_pkts_unctrl
                                    
                                    	Multicast pkts tx on uncontrolled port
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_octets_common
                                    
                                    	Octets tx on common port
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_octets_ctrl
                                    
                                    	Octets tx on controlled port
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_octets_unctrl
                                    
                                    	Octets tx on uncontrolled port
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_pkt_ctrl
                                    
                                    	egress packet that is classified as control packet
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_pkts_untagged
                                    
                                    	egress packet to go out untagged when protectFrames not set
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_rx_drop_pkts_ctrl
                                    
                                    	Data pkts dropped due to overrun
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_rx_drop_pkts_unctrl
                                    
                                    	Control pkts dropped due to overrun
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_rx_err_pkts_ctrl
                                    
                                    	Data pkts error\-terminated due to overrun
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_rx_err_pkts_unctrl
                                    
                                    	Control pkts error\-terminated due to overrun
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_ucast_pkts_ctrl
                                    
                                    	Unicast pkts tx on controlled port
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_ucast_pkts_unctrl
                                    
                                    	Unicast pkts tx on uncontrolled port
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: transform_error_pkts
                                    
                                    	counter to count internal errors in the MACSec core
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'crypto-macsec-pl-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats.TxInterfaceMacsecStats, self).__init__()

                                        self.yang_name = "tx-interface-macsec-stats"
                                        self.yang_parent_name = "es200-stats"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.out_bcast_pkts_ctrl = YLeaf(YType.uint64, "out-bcast-pkts-ctrl")

                                        self.out_bcast_pkts_unctrl = YLeaf(YType.uint64, "out-bcast-pkts-unctrl")

                                        self.out_drop_pkts_class = YLeaf(YType.uint64, "out-drop-pkts-class")

                                        self.out_drop_pkts_data = YLeaf(YType.uint64, "out-drop-pkts-data")

                                        self.out_mcast_pkts_ctrl = YLeaf(YType.uint64, "out-mcast-pkts-ctrl")

                                        self.out_mcast_pkts_unctrl = YLeaf(YType.uint64, "out-mcast-pkts-unctrl")

                                        self.out_octets_common = YLeaf(YType.uint64, "out-octets-common")

                                        self.out_octets_ctrl = YLeaf(YType.uint64, "out-octets-ctrl")

                                        self.out_octets_unctrl = YLeaf(YType.uint64, "out-octets-unctrl")

                                        self.out_pkt_ctrl = YLeaf(YType.uint64, "out-pkt-ctrl")

                                        self.out_pkts_untagged = YLeaf(YType.uint64, "out-pkts-untagged")

                                        self.out_rx_drop_pkts_ctrl = YLeaf(YType.uint64, "out-rx-drop-pkts-ctrl")

                                        self.out_rx_drop_pkts_unctrl = YLeaf(YType.uint64, "out-rx-drop-pkts-unctrl")

                                        self.out_rx_err_pkts_ctrl = YLeaf(YType.uint64, "out-rx-err-pkts-ctrl")

                                        self.out_rx_err_pkts_unctrl = YLeaf(YType.uint64, "out-rx-err-pkts-unctrl")

                                        self.out_ucast_pkts_ctrl = YLeaf(YType.uint64, "out-ucast-pkts-ctrl")

                                        self.out_ucast_pkts_unctrl = YLeaf(YType.uint64, "out-ucast-pkts-unctrl")

                                        self.transform_error_pkts = YLeaf(YType.uint64, "transform-error-pkts")
                                        self._segment_path = lambda: "tx-interface-macsec-stats"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats.TxInterfaceMacsecStats, ['out_bcast_pkts_ctrl', 'out_bcast_pkts_unctrl', 'out_drop_pkts_class', 'out_drop_pkts_data', 'out_mcast_pkts_ctrl', 'out_mcast_pkts_unctrl', 'out_octets_common', 'out_octets_ctrl', 'out_octets_unctrl', 'out_pkt_ctrl', 'out_pkts_untagged', 'out_rx_drop_pkts_ctrl', 'out_rx_drop_pkts_unctrl', 'out_rx_err_pkts_ctrl', 'out_rx_err_pkts_unctrl', 'out_ucast_pkts_ctrl', 'out_ucast_pkts_unctrl', 'transform_error_pkts'], name, value)


                                class TxPortStats(Entity):
                                    """
                                    Port level TX Stats
                                    
                                    .. attribute:: flow_miss
                                    
                                    	Pkts matching none of flow entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: multi_flow_match
                                    
                                    	Pkts matching multiple flow entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: parser_dropped
                                    
                                    	Pkts dropped by header parser as invalid
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: pkts_ctrl
                                    
                                    	Control pkts forwarded
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: pkts_data
                                    
                                    	Data pkts forwarded
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: pkts_dropped
                                    
                                    	Pkts dropped by classifier
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: pkts_err_in
                                    
                                    	Pkts received with an error indication
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'crypto-macsec-pl-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats.TxPortStats, self).__init__()

                                        self.yang_name = "tx-port-stats"
                                        self.yang_parent_name = "es200-stats"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.flow_miss = YLeaf(YType.uint64, "flow-miss")

                                        self.multi_flow_match = YLeaf(YType.uint64, "multi-flow-match")

                                        self.parser_dropped = YLeaf(YType.uint64, "parser-dropped")

                                        self.pkts_ctrl = YLeaf(YType.uint64, "pkts-ctrl")

                                        self.pkts_data = YLeaf(YType.uint64, "pkts-data")

                                        self.pkts_dropped = YLeaf(YType.uint64, "pkts-dropped")

                                        self.pkts_err_in = YLeaf(YType.uint64, "pkts-err-in")
                                        self._segment_path = lambda: "tx-port-stats"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats.TxPortStats, ['flow_miss', 'multi_flow_match', 'parser_dropped', 'pkts_ctrl', 'pkts_data', 'pkts_dropped', 'pkts_err_in'], name, value)


                                class TxSaStats(Entity):
                                    """
                                    Tx SA Stats
                                    
                                    .. attribute:: out_octets_encrypted_protected1
                                    
                                    	octets1 encrypted/protected ?
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_pkts_encrypted_protected
                                    
                                    	packets encrypted/protected
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_pkts_too_long
                                    
                                    	packets exceeding egress MTU
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'crypto-macsec-pl-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats.TxSaStats, self).__init__()

                                        self.yang_name = "tx-sa-stats"
                                        self.yang_parent_name = "es200-stats"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.out_octets_encrypted_protected1 = YLeaf(YType.uint64, "out-octets-encrypted-protected1")

                                        self.out_pkts_encrypted_protected = YLeaf(YType.uint64, "out-pkts-encrypted-protected")

                                        self.out_pkts_too_long = YLeaf(YType.uint64, "out-pkts-too-long")
                                        self._segment_path = lambda: "tx-sa-stats"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats.TxSaStats, ['out_octets_encrypted_protected1', 'out_pkts_encrypted_protected', 'out_pkts_too_long'], name, value)


                                class TxScMacsecStats(Entity):
                                    """
                                    Tx SC Macsec Stats
                                    
                                    .. attribute:: out_pkts_sa_not_in_use
                                    
                                    	Packets received with SA not in use
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'crypto-macsec-pl-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats.TxScMacsecStats, self).__init__()

                                        self.yang_name = "tx-sc-macsec-stats"
                                        self.yang_parent_name = "es200-stats"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.out_pkts_sa_not_in_use = YLeaf(YType.uint64, "out-pkts-sa-not-in-use")
                                        self._segment_path = lambda: "tx-sc-macsec-stats"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats.TxScMacsecStats, ['out_pkts_sa_not_in_use'], name, value)


                            class MsfpgaStats(Entity):
                                """
                                MSFPGA Stats
                                
                                .. attribute:: rx_interface_macsec_stats
                                
                                	Rx interface Macsec Stats
                                	**type**\:   :py:class:`RxInterfaceMacsecStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.MsfpgaStats.RxInterfaceMacsecStats>`
                                
                                .. attribute:: rx_sa_stats
                                
                                	Rx SA Stats
                                	**type**\:   :py:class:`RxSaStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.MsfpgaStats.RxSaStats>`
                                
                                .. attribute:: tx_interface_macsec_stats
                                
                                	Tx interface Macsec Stats
                                	**type**\:   :py:class:`TxInterfaceMacsecStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.MsfpgaStats.TxInterfaceMacsecStats>`
                                
                                .. attribute:: tx_sa_stats
                                
                                	Tx SA Stats
                                	**type**\:   :py:class:`TxSaStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.MsfpgaStats.TxSaStats>`
                                
                                

                                """

                                _prefix = 'crypto-macsec-pl-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.MsfpgaStats, self).__init__()

                                    self.yang_name = "msfpga-stats"
                                    self.yang_parent_name = "ext"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {"rx-interface-macsec-stats" : ("rx_interface_macsec_stats", MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.MsfpgaStats.RxInterfaceMacsecStats), "rx-sa-stats" : ("rx_sa_stats", MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.MsfpgaStats.RxSaStats), "tx-interface-macsec-stats" : ("tx_interface_macsec_stats", MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.MsfpgaStats.TxInterfaceMacsecStats), "tx-sa-stats" : ("tx_sa_stats", MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.MsfpgaStats.TxSaStats)}
                                    self._child_list_classes = {}

                                    self.rx_interface_macsec_stats = MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.MsfpgaStats.RxInterfaceMacsecStats()
                                    self.rx_interface_macsec_stats.parent = self
                                    self._children_name_map["rx_interface_macsec_stats"] = "rx-interface-macsec-stats"
                                    self._children_yang_names.add("rx-interface-macsec-stats")

                                    self.rx_sa_stats = MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.MsfpgaStats.RxSaStats()
                                    self.rx_sa_stats.parent = self
                                    self._children_name_map["rx_sa_stats"] = "rx-sa-stats"
                                    self._children_yang_names.add("rx-sa-stats")

                                    self.tx_interface_macsec_stats = MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.MsfpgaStats.TxInterfaceMacsecStats()
                                    self.tx_interface_macsec_stats.parent = self
                                    self._children_name_map["tx_interface_macsec_stats"] = "tx-interface-macsec-stats"
                                    self._children_yang_names.add("tx-interface-macsec-stats")

                                    self.tx_sa_stats = MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.MsfpgaStats.TxSaStats()
                                    self.tx_sa_stats.parent = self
                                    self._children_name_map["tx_sa_stats"] = "tx-sa-stats"
                                    self._children_yang_names.add("tx-sa-stats")
                                    self._segment_path = lambda: "msfpga-stats"


                                class RxInterfaceMacsecStats(Entity):
                                    """
                                    Rx interface Macsec Stats
                                    
                                    .. attribute:: in_pkt_bad_tag
                                    
                                    	Rx Pkts Bad tag
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkt_no_sci
                                    
                                    	Rx Pkts No Sci
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkt_notag
                                    
                                    	Rx Pkts Notag
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkt_overrun
                                    
                                    	Rx Pkts Over Run
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkt_tagged
                                    
                                    	Rx Pkts Tagged
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkt_uncontrolled
                                    
                                    	Rx Pkts Uncontrolled
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkt_unknown_sci
                                    
                                    	Rx Pkts Unknown Sci
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkt_untagged
                                    
                                    	Rx Pkts Untagged
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'crypto-macsec-pl-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.MsfpgaStats.RxInterfaceMacsecStats, self).__init__()

                                        self.yang_name = "rx-interface-macsec-stats"
                                        self.yang_parent_name = "msfpga-stats"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.in_pkt_bad_tag = YLeaf(YType.uint64, "in-pkt-bad-tag")

                                        self.in_pkt_no_sci = YLeaf(YType.uint64, "in-pkt-no-sci")

                                        self.in_pkt_notag = YLeaf(YType.uint64, "in-pkt-notag")

                                        self.in_pkt_overrun = YLeaf(YType.uint64, "in-pkt-overrun")

                                        self.in_pkt_tagged = YLeaf(YType.uint64, "in-pkt-tagged")

                                        self.in_pkt_uncontrolled = YLeaf(YType.uint64, "in-pkt-uncontrolled")

                                        self.in_pkt_unknown_sci = YLeaf(YType.uint64, "in-pkt-unknown-sci")

                                        self.in_pkt_untagged = YLeaf(YType.uint64, "in-pkt-untagged")
                                        self._segment_path = lambda: "rx-interface-macsec-stats"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.MsfpgaStats.RxInterfaceMacsecStats, ['in_pkt_bad_tag', 'in_pkt_no_sci', 'in_pkt_notag', 'in_pkt_overrun', 'in_pkt_tagged', 'in_pkt_uncontrolled', 'in_pkt_unknown_sci', 'in_pkt_untagged'], name, value)


                                class RxSaStats(Entity):
                                    """
                                    Rx SA Stats
                                    
                                    .. attribute:: in_octets_decrypted
                                    
                                    	Rx Octets Decrypted
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_octets_validated
                                    
                                    	Rx Octets Validated
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkts_delayed
                                    
                                    	Rx Pkts Delayed
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkts_invalid
                                    
                                    	Rx Pkts Invalid
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkts_late
                                    
                                    	Rx Pkts Late
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkts_not_using_sa
                                    
                                    	Rx Pkts Not Using SA
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkts_not_valid
                                    
                                    	Rx Pkts Not Valid
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkts_ok
                                    
                                    	Rx Pkts OK
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkts_unchecked
                                    
                                    	Rx Pkts Unchecked
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkts_unused_sa
                                    
                                    	Rx Pkts Unused SA
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'crypto-macsec-pl-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.MsfpgaStats.RxSaStats, self).__init__()

                                        self.yang_name = "rx-sa-stats"
                                        self.yang_parent_name = "msfpga-stats"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.in_octets_decrypted = YLeaf(YType.uint64, "in-octets-decrypted")

                                        self.in_octets_validated = YLeaf(YType.uint64, "in-octets-validated")

                                        self.in_pkts_delayed = YLeaf(YType.uint64, "in-pkts-delayed")

                                        self.in_pkts_invalid = YLeaf(YType.uint64, "in-pkts-invalid")

                                        self.in_pkts_late = YLeaf(YType.uint64, "in-pkts-late")

                                        self.in_pkts_not_using_sa = YLeaf(YType.uint64, "in-pkts-not-using-sa")

                                        self.in_pkts_not_valid = YLeaf(YType.uint64, "in-pkts-not-valid")

                                        self.in_pkts_ok = YLeaf(YType.uint64, "in-pkts-ok")

                                        self.in_pkts_unchecked = YLeaf(YType.uint64, "in-pkts-unchecked")

                                        self.in_pkts_unused_sa = YLeaf(YType.uint64, "in-pkts-unused-sa")
                                        self._segment_path = lambda: "rx-sa-stats"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.MsfpgaStats.RxSaStats, ['in_octets_decrypted', 'in_octets_validated', 'in_pkts_delayed', 'in_pkts_invalid', 'in_pkts_late', 'in_pkts_not_using_sa', 'in_pkts_not_valid', 'in_pkts_ok', 'in_pkts_unchecked', 'in_pkts_unused_sa'], name, value)


                                class TxInterfaceMacsecStats(Entity):
                                    """
                                    Tx interface Macsec Stats
                                    
                                    .. attribute:: out_pkt_too_long
                                    
                                    	Tx Pkts Too Long
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_pkt_uncontrolled
                                    
                                    	Tx Pkts Uncontrolled
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_pkt_untagged
                                    
                                    	Tx Pkts Untagged
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'crypto-macsec-pl-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.MsfpgaStats.TxInterfaceMacsecStats, self).__init__()

                                        self.yang_name = "tx-interface-macsec-stats"
                                        self.yang_parent_name = "msfpga-stats"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.out_pkt_too_long = YLeaf(YType.uint64, "out-pkt-too-long")

                                        self.out_pkt_uncontrolled = YLeaf(YType.uint64, "out-pkt-uncontrolled")

                                        self.out_pkt_untagged = YLeaf(YType.uint64, "out-pkt-untagged")
                                        self._segment_path = lambda: "tx-interface-macsec-stats"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.MsfpgaStats.TxInterfaceMacsecStats, ['out_pkt_too_long', 'out_pkt_uncontrolled', 'out_pkt_untagged'], name, value)


                                class TxSaStats(Entity):
                                    """
                                    Tx SA Stats
                                    
                                    .. attribute:: out_octets_encrypted
                                    
                                    	Tx Octets Encrypted
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_octets_protected
                                    
                                    	Tx Octets Protected
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_pkts_encrypted
                                    
                                    	Tx Pkts Encrypted
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_pkts_protected
                                    
                                    	Tx Pkts Protected
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'crypto-macsec-pl-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.MsfpgaStats.TxSaStats, self).__init__()

                                        self.yang_name = "tx-sa-stats"
                                        self.yang_parent_name = "msfpga-stats"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.out_octets_encrypted = YLeaf(YType.uint64, "out-octets-encrypted")

                                        self.out_octets_protected = YLeaf(YType.uint64, "out-octets-protected")

                                        self.out_pkts_encrypted = YLeaf(YType.uint64, "out-pkts-encrypted")

                                        self.out_pkts_protected = YLeaf(YType.uint64, "out-pkts-protected")
                                        self._segment_path = lambda: "tx-sa-stats"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.MsfpgaStats.TxSaStats, ['out_octets_encrypted', 'out_octets_protected', 'out_pkts_encrypted', 'out_pkts_protected'], name, value)


                            class XlfpgaStats(Entity):
                                """
                                XLFPGA Stats
                                
                                .. attribute:: macsec_rx_stats
                                
                                	Rx SC and SA Level Stats
                                	**type**\:   :py:class:`MacsecRxStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.XlfpgaStats.MacsecRxStats>`
                                
                                .. attribute:: macsec_tx_stats
                                
                                	Tx SC and SA Level Stats
                                	**type**\:   :py:class:`MacsecTxStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.XlfpgaStats.MacsecTxStats>`
                                
                                

                                """

                                _prefix = 'crypto-macsec-pl-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.XlfpgaStats, self).__init__()

                                    self.yang_name = "xlfpga-stats"
                                    self.yang_parent_name = "ext"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {"macsec-rx-stats" : ("macsec_rx_stats", MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.XlfpgaStats.MacsecRxStats), "macsec-tx-stats" : ("macsec_tx_stats", MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.XlfpgaStats.MacsecTxStats)}
                                    self._child_list_classes = {}

                                    self.macsec_rx_stats = MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.XlfpgaStats.MacsecRxStats()
                                    self.macsec_rx_stats.parent = self
                                    self._children_name_map["macsec_rx_stats"] = "macsec-rx-stats"
                                    self._children_yang_names.add("macsec-rx-stats")

                                    self.macsec_tx_stats = MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.XlfpgaStats.MacsecTxStats()
                                    self.macsec_tx_stats.parent = self
                                    self._children_name_map["macsec_tx_stats"] = "macsec-tx-stats"
                                    self._children_yang_names.add("macsec-tx-stats")
                                    self._segment_path = lambda: "xlfpga-stats"


                                class MacsecRxStats(Entity):
                                    """
                                    Rx SC and SA Level Stats
                                    
                                    .. attribute:: rx_sa_stat
                                    
                                    	Rx SA Level Stats
                                    	**type**\: list of    :py:class:`RxSaStat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.XlfpgaStats.MacsecRxStats.RxSaStat>`
                                    
                                    .. attribute:: sc_bad_tag_pkts
                                    
                                    	Rx Bad Tag Packets
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_bypass_pkts
                                    
                                    	Rx Bypass Packets
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_decrypted_octets
                                    
                                    	Rx Octets Decrypted
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_delayed_pkts
                                    
                                    	Rx Delayed Pkts
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_dropped_pkts
                                    
                                    	Rx Dropped Packets
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_eapol_pkts
                                    
                                    	Rx Eapol Packets
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_invalid_pkts
                                    
                                    	Rx Pkts Invalid
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_late_pkts
                                    
                                    	Rx Late Pkts
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_no_sci_pkts
                                    
                                    	Rx No SCI Pkts
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_no_tag_pkts
                                    
                                    	Rx No Tag Packets
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_not_using_pkts
                                    
                                    	Rx Pkts Not Using SA
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_not_valid_pkts
                                    
                                    	Rx Not Valid Pkts
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_ok_pkts
                                    
                                    	Rx Pkts Ok
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_overrun_pkts
                                    
                                    	Rx Overrun Pkts
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_unchecked_pkts
                                    
                                    	Rx Unchecked Pkts
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_unknown_sci_pkts
                                    
                                    	Rx Unknown SCI Pkts
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_untagged_pkts
                                    
                                    	Rx Untagged Packets
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_unused_pkts
                                    
                                    	Rx Pkts Unused SA
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'crypto-macsec-pl-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.XlfpgaStats.MacsecRxStats, self).__init__()

                                        self.yang_name = "macsec-rx-stats"
                                        self.yang_parent_name = "xlfpga-stats"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {"rx-sa-stat" : ("rx_sa_stat", MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.XlfpgaStats.MacsecRxStats.RxSaStat)}

                                        self.sc_bad_tag_pkts = YLeaf(YType.uint64, "sc-bad-tag-pkts")

                                        self.sc_bypass_pkts = YLeaf(YType.uint64, "sc-bypass-pkts")

                                        self.sc_decrypted_octets = YLeaf(YType.uint64, "sc-decrypted-octets")

                                        self.sc_delayed_pkts = YLeaf(YType.uint64, "sc-delayed-pkts")

                                        self.sc_dropped_pkts = YLeaf(YType.uint64, "sc-dropped-pkts")

                                        self.sc_eapol_pkts = YLeaf(YType.uint64, "sc-eapol-pkts")

                                        self.sc_invalid_pkts = YLeaf(YType.uint64, "sc-invalid-pkts")

                                        self.sc_late_pkts = YLeaf(YType.uint64, "sc-late-pkts")

                                        self.sc_no_sci_pkts = YLeaf(YType.uint64, "sc-no-sci-pkts")

                                        self.sc_no_tag_pkts = YLeaf(YType.uint64, "sc-no-tag-pkts")

                                        self.sc_not_using_pkts = YLeaf(YType.uint64, "sc-not-using-pkts")

                                        self.sc_not_valid_pkts = YLeaf(YType.uint64, "sc-not-valid-pkts")

                                        self.sc_ok_pkts = YLeaf(YType.uint64, "sc-ok-pkts")

                                        self.sc_overrun_pkts = YLeaf(YType.uint64, "sc-overrun-pkts")

                                        self.sc_unchecked_pkts = YLeaf(YType.uint64, "sc-unchecked-pkts")

                                        self.sc_unknown_sci_pkts = YLeaf(YType.uint64, "sc-unknown-sci-pkts")

                                        self.sc_untagged_pkts = YLeaf(YType.uint64, "sc-untagged-pkts")

                                        self.sc_unused_pkts = YLeaf(YType.uint64, "sc-unused-pkts")

                                        self.rx_sa_stat = YList(self)
                                        self._segment_path = lambda: "macsec-rx-stats"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.XlfpgaStats.MacsecRxStats, ['sc_bad_tag_pkts', 'sc_bypass_pkts', 'sc_decrypted_octets', 'sc_delayed_pkts', 'sc_dropped_pkts', 'sc_eapol_pkts', 'sc_invalid_pkts', 'sc_late_pkts', 'sc_no_sci_pkts', 'sc_no_tag_pkts', 'sc_not_using_pkts', 'sc_not_valid_pkts', 'sc_ok_pkts', 'sc_overrun_pkts', 'sc_unchecked_pkts', 'sc_unknown_sci_pkts', 'sc_untagged_pkts', 'sc_unused_pkts'], name, value)


                                    class RxSaStat(Entity):
                                        """
                                        Rx SA Level Stats
                                        
                                        .. attribute:: an
                                        
                                        	Current Rx AN
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: sa_invalid_pkts
                                        
                                        	Rx Invalid Pkts for current AN
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: sa_not_using_pkts
                                        
                                        	Rx Pkts not using SA for Current AN
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: sa_not_valid_pkts
                                        
                                        	Rx Not Valid Pkts for Current AN
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: sa_ok_pkts
                                        
                                        	Rx Ok Pkts for Current AN
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: sa_unused_pkts
                                        
                                        	Rx Pkts Unused Pkts for Current AN
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        

                                        """

                                        _prefix = 'crypto-macsec-pl-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.XlfpgaStats.MacsecRxStats.RxSaStat, self).__init__()

                                            self.yang_name = "rx-sa-stat"
                                            self.yang_parent_name = "macsec-rx-stats"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.an = YLeaf(YType.uint64, "an")

                                            self.sa_invalid_pkts = YLeaf(YType.uint64, "sa-invalid-pkts")

                                            self.sa_not_using_pkts = YLeaf(YType.uint64, "sa-not-using-pkts")

                                            self.sa_not_valid_pkts = YLeaf(YType.uint64, "sa-not-valid-pkts")

                                            self.sa_ok_pkts = YLeaf(YType.uint64, "sa-ok-pkts")

                                            self.sa_unused_pkts = YLeaf(YType.uint64, "sa-unused-pkts")
                                            self._segment_path = lambda: "rx-sa-stat"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.XlfpgaStats.MacsecRxStats.RxSaStat, ['an', 'sa_invalid_pkts', 'sa_not_using_pkts', 'sa_not_valid_pkts', 'sa_ok_pkts', 'sa_unused_pkts'], name, value)


                                class MacsecTxStats(Entity):
                                    """
                                    Tx SC and SA Level Stats
                                    
                                    .. attribute:: current_an
                                    
                                    	Current Tx AN
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sa_encrypted_pkts
                                    
                                    	Current Tx SA Encrypted Packets
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_bypass_pkts
                                    
                                    	Tx Bypass Packets
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_dropped_pkts
                                    
                                    	Tx Dropped Packets
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_eapol_pkts
                                    
                                    	Tx Eapol Packets
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_encrypted_octets
                                    
                                    	Tx Octets Encrypted
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_encrypted_pkts
                                    
                                    	Tx packets Encrypted
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_overrun_pkts
                                    
                                    	Tx Overrun Packets
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_toolong_pkts
                                    
                                    	Tx Pkts Too Long
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_untagged_pkts
                                    
                                    	Tx Untagged Packets
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'crypto-macsec-pl-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.XlfpgaStats.MacsecTxStats, self).__init__()

                                        self.yang_name = "macsec-tx-stats"
                                        self.yang_parent_name = "xlfpga-stats"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.current_an = YLeaf(YType.uint64, "current-an")

                                        self.sa_encrypted_pkts = YLeaf(YType.uint64, "sa-encrypted-pkts")

                                        self.sc_bypass_pkts = YLeaf(YType.uint64, "sc-bypass-pkts")

                                        self.sc_dropped_pkts = YLeaf(YType.uint64, "sc-dropped-pkts")

                                        self.sc_eapol_pkts = YLeaf(YType.uint64, "sc-eapol-pkts")

                                        self.sc_encrypted_octets = YLeaf(YType.uint64, "sc-encrypted-octets")

                                        self.sc_encrypted_pkts = YLeaf(YType.uint64, "sc-encrypted-pkts")

                                        self.sc_overrun_pkts = YLeaf(YType.uint64, "sc-overrun-pkts")

                                        self.sc_toolong_pkts = YLeaf(YType.uint64, "sc-toolong-pkts")

                                        self.sc_untagged_pkts = YLeaf(YType.uint64, "sc-untagged-pkts")
                                        self._segment_path = lambda: "macsec-tx-stats"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.XlfpgaStats.MacsecTxStats, ['current_an', 'sa_encrypted_pkts', 'sc_bypass_pkts', 'sc_dropped_pkts', 'sc_eapol_pkts', 'sc_encrypted_octets', 'sc_encrypted_pkts', 'sc_overrun_pkts', 'sc_toolong_pkts', 'sc_untagged_pkts'], name, value)

    def clone_ptr(self):
        self._top_entity = MacsecPlatform()
        return self._top_entity

