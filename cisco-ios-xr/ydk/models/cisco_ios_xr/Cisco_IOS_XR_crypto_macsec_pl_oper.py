""" Cisco_IOS_XR_crypto_macsec_pl_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR crypto\-macsec\-pl package operational data.

This module contains definitions
for the following management objects\:
  macsec\-platform\: MACSec operational data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class MacsecPhyVendor(Enum):
    """
    MacsecPhyVendor (Enum Class)

    Macsec phy vendor

    .. data:: msfpga = 0

    	msfpga

    .. data:: xlmsfpga = 1

    	xlmsfpga

    .. data:: apm_es200 = 2

    	apm es200

    .. data:: apm_x120 = 3

    	apm x120

    .. data:: mv88ec808 = 4

    	mv88ec808

    .. data:: max_card_type = 5

    	max card type

    .. data:: unknown = 6

    	unknown

    .. data:: invalid = 7

    	invalid

    """

    msfpga = Enum.YLeaf(0, "msfpga")

    xlmsfpga = Enum.YLeaf(1, "xlmsfpga")

    apm_es200 = Enum.YLeaf(2, "apm-es200")

    apm_x120 = Enum.YLeaf(3, "apm-x120")

    mv88ec808 = Enum.YLeaf(4, "mv88ec808")

    max_card_type = Enum.YLeaf(5, "max-card-type")

    unknown = Enum.YLeaf(6, "unknown")

    invalid = Enum.YLeaf(7, "invalid")



class MacsecPlatform(Entity):
    """
    MACSec operational data
    
    .. attribute:: nodes
    
    	NodeTable for all the nodes
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes>`
    
    

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
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("nodes", ("nodes", MacsecPlatform.Nodes))])
        self._leafs = OrderedDict()

        self.nodes = MacsecPlatform.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._segment_path = lambda: "Cisco-IOS-XR-crypto-macsec-pl-oper:macsec-platform"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(MacsecPlatform, [], name, value)


    class Nodes(Entity):
        """
        NodeTable for all the nodes
        
        .. attribute:: node
        
        	Node where macsec interfaces exist
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node>`
        
        

        """

        _prefix = 'crypto-macsec-pl-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(MacsecPlatform.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "macsec-platform"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("node", ("node", MacsecPlatform.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-crypto-macsec-pl-oper:macsec-platform/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(MacsecPlatform.Nodes, [], name, value)


        class Node(Entity):
            """
            Node where macsec interfaces exist
            
            .. attribute:: node_name  (key)
            
            	Node
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: interfaces
            
            	Table of Interfaces
            	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces>`
            
            

            """

            _prefix = 'crypto-macsec-pl-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(MacsecPlatform.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_classes = OrderedDict([("interfaces", ("interfaces", MacsecPlatform.Nodes.Node.Interfaces))])
                self._leafs = OrderedDict([
                    ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                ])
                self.node_name = None

                self.interfaces = MacsecPlatform.Nodes.Node.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"
                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-crypto-macsec-pl-oper:macsec-platform/nodes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(MacsecPlatform.Nodes.Node, ['node_name'], name, value)


            class Interfaces(Entity):
                """
                Table of Interfaces
                
                .. attribute:: interface
                
                	Interface Where Macsec is configured
                	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface>`
                
                

                """

                _prefix = 'crypto-macsec-pl-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MacsecPlatform.Nodes.Node.Interfaces, self).__init__()

                    self.yang_name = "interfaces"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("interface", ("interface", MacsecPlatform.Nodes.Node.Interfaces.Interface))])
                    self._leafs = OrderedDict()

                    self.interface = YList(self)
                    self._segment_path = lambda: "interfaces"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces, [], name, value)


                class Interface(Entity):
                    """
                    Interface Where Macsec is configured
                    
                    .. attribute:: name  (key)
                    
                    	Value
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: hw_statistics
                    
                    	The Hardware Statistics
                    	**type**\:  :py:class:`HwStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics>`
                    
                    .. attribute:: hw_sas
                    
                    	Table of Hardware SAs
                    	**type**\:  :py:class:`HwSas <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas>`
                    
                    .. attribute:: hw_flow_s
                    
                    	Table of Hardware Flows
                    	**type**\:  :py:class:`HwFlowS <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS>`
                    
                    .. attribute:: sw_statistics
                    
                    	The Software Statistics
                    	**type**\:  :py:class:`SwStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics>`
                    
                    

                    """

                    _prefix = 'crypto-macsec-pl-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(MacsecPlatform.Nodes.Node.Interfaces.Interface, self).__init__()

                        self.yang_name = "interface"
                        self.yang_parent_name = "interfaces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['name']
                        self._child_classes = OrderedDict([("hw-statistics", ("hw_statistics", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics)), ("hw-sas", ("hw_sas", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas)), ("hw-flow-s", ("hw_flow_s", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS)), ("sw-statistics", ("sw_statistics", MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics))])
                        self._leafs = OrderedDict([
                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                        ])
                        self.name = None

                        self.hw_statistics = MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics()
                        self.hw_statistics.parent = self
                        self._children_name_map["hw_statistics"] = "hw-statistics"

                        self.hw_sas = MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas()
                        self.hw_sas.parent = self
                        self._children_name_map["hw_sas"] = "hw-sas"

                        self.hw_flow_s = MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS()
                        self.hw_flow_s.parent = self
                        self._children_name_map["hw_flow_s"] = "hw-flow-s"

                        self.sw_statistics = MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics()
                        self.sw_statistics.parent = self
                        self._children_name_map["sw_statistics"] = "sw-statistics"
                        self._segment_path = lambda: "interface" + "[name='" + str(self.name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface, ['name'], name, value)


                    class HwStatistics(Entity):
                        """
                        The Hardware Statistics
                        
                        .. attribute:: ext
                        
                        	ext
                        	**type**\:  :py:class:`Ext <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext>`
                        
                        

                        """

                        _prefix = 'crypto-macsec-pl-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics, self).__init__()

                            self.yang_name = "hw-statistics"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("ext", ("ext", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext))])
                            self._leafs = OrderedDict()

                            self.ext = MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext()
                            self.ext.parent = self
                            self._children_name_map["ext"] = "ext"
                            self._segment_path = lambda: "hw-statistics"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics, [], name, value)


                        class Ext(Entity):
                            """
                            ext
                            
                            .. attribute:: msfpga_stats
                            
                            	MSFPGA Stats
                            	**type**\:  :py:class:`MsfpgaStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.MsfpgaStats>`
                            
                            .. attribute:: xlfpga_stats
                            
                            	XLFPGA Stats
                            	**type**\:  :py:class:`XlfpgaStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.XlfpgaStats>`
                            
                            .. attribute:: es200_stats
                            
                            	ES200 Stats
                            	**type**\:  :py:class:`Es200Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats>`
                            
                            .. attribute:: type
                            
                            	type
                            	**type**\:  :py:class:`MacsecPhyVendor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPhyVendor>`
                            
                            

                            """

                            _prefix = 'crypto-macsec-pl-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext, self).__init__()

                                self.yang_name = "ext"
                                self.yang_parent_name = "hw-statistics"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("msfpga-stats", ("msfpga_stats", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.MsfpgaStats)), ("xlfpga-stats", ("xlfpga_stats", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.XlfpgaStats)), ("es200-stats", ("es200_stats", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats))])
                                self._leafs = OrderedDict([
                                    ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'MacsecPhyVendor', '')])),
                                ])
                                self.type = None

                                self.msfpga_stats = MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.MsfpgaStats()
                                self.msfpga_stats.parent = self
                                self._children_name_map["msfpga_stats"] = "msfpga-stats"

                                self.xlfpga_stats = MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.XlfpgaStats()
                                self.xlfpga_stats.parent = self
                                self._children_name_map["xlfpga_stats"] = "xlfpga-stats"

                                self.es200_stats = MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats()
                                self.es200_stats.parent = self
                                self._children_name_map["es200_stats"] = "es200-stats"
                                self._segment_path = lambda: "ext"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext, ['type'], name, value)


                            class MsfpgaStats(Entity):
                                """
                                MSFPGA Stats
                                
                                .. attribute:: tx_sa_stats
                                
                                	Tx SA Stats
                                	**type**\:  :py:class:`TxSaStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.MsfpgaStats.TxSaStats>`
                                
                                .. attribute:: rx_sa_stats
                                
                                	Rx SA Stats
                                	**type**\:  :py:class:`RxSaStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.MsfpgaStats.RxSaStats>`
                                
                                .. attribute:: tx_interface_macsec_stats
                                
                                	Tx interface Macsec Stats
                                	**type**\:  :py:class:`TxInterfaceMacsecStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.MsfpgaStats.TxInterfaceMacsecStats>`
                                
                                .. attribute:: rx_interface_macsec_stats
                                
                                	Rx interface Macsec Stats
                                	**type**\:  :py:class:`RxInterfaceMacsecStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.MsfpgaStats.RxInterfaceMacsecStats>`
                                
                                

                                """

                                _prefix = 'crypto-macsec-pl-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.MsfpgaStats, self).__init__()

                                    self.yang_name = "msfpga-stats"
                                    self.yang_parent_name = "ext"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("tx-sa-stats", ("tx_sa_stats", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.MsfpgaStats.TxSaStats)), ("rx-sa-stats", ("rx_sa_stats", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.MsfpgaStats.RxSaStats)), ("tx-interface-macsec-stats", ("tx_interface_macsec_stats", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.MsfpgaStats.TxInterfaceMacsecStats)), ("rx-interface-macsec-stats", ("rx_interface_macsec_stats", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.MsfpgaStats.RxInterfaceMacsecStats))])
                                    self._leafs = OrderedDict()

                                    self.tx_sa_stats = MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.MsfpgaStats.TxSaStats()
                                    self.tx_sa_stats.parent = self
                                    self._children_name_map["tx_sa_stats"] = "tx-sa-stats"

                                    self.rx_sa_stats = MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.MsfpgaStats.RxSaStats()
                                    self.rx_sa_stats.parent = self
                                    self._children_name_map["rx_sa_stats"] = "rx-sa-stats"

                                    self.tx_interface_macsec_stats = MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.MsfpgaStats.TxInterfaceMacsecStats()
                                    self.tx_interface_macsec_stats.parent = self
                                    self._children_name_map["tx_interface_macsec_stats"] = "tx-interface-macsec-stats"

                                    self.rx_interface_macsec_stats = MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.MsfpgaStats.RxInterfaceMacsecStats()
                                    self.rx_interface_macsec_stats.parent = self
                                    self._children_name_map["rx_interface_macsec_stats"] = "rx-interface-macsec-stats"
                                    self._segment_path = lambda: "msfpga-stats"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.MsfpgaStats, [], name, value)


                                class TxSaStats(Entity):
                                    """
                                    Tx SA Stats
                                    
                                    .. attribute:: out_pkts_protected
                                    
                                    	Tx Pkts Protected
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_pkts_encrypted
                                    
                                    	Tx Pkts Encrypted
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_octets_protected
                                    
                                    	Tx Octets Protected
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_octets_encrypted
                                    
                                    	Tx Octets Encrypted
                                    	**type**\: int
                                    
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
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('out_pkts_protected', (YLeaf(YType.uint64, 'out-pkts-protected'), ['int'])),
                                            ('out_pkts_encrypted', (YLeaf(YType.uint64, 'out-pkts-encrypted'), ['int'])),
                                            ('out_octets_protected', (YLeaf(YType.uint64, 'out-octets-protected'), ['int'])),
                                            ('out_octets_encrypted', (YLeaf(YType.uint64, 'out-octets-encrypted'), ['int'])),
                                        ])
                                        self.out_pkts_protected = None
                                        self.out_pkts_encrypted = None
                                        self.out_octets_protected = None
                                        self.out_octets_encrypted = None
                                        self._segment_path = lambda: "tx-sa-stats"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.MsfpgaStats.TxSaStats, ['out_pkts_protected', 'out_pkts_encrypted', 'out_octets_protected', 'out_octets_encrypted'], name, value)


                                class RxSaStats(Entity):
                                    """
                                    Rx SA Stats
                                    
                                    .. attribute:: in_pkts_unused_sa
                                    
                                    	Rx Pkts Unused SA
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkts_not_using_sa
                                    
                                    	Rx Pkts Not Using SA
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkts_not_valid
                                    
                                    	Rx Pkts Not Valid
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkts_invalid
                                    
                                    	Rx Pkts Invalid
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkts_ok
                                    
                                    	Rx Pkts OK
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkts_delayed
                                    
                                    	Rx Pkts Delayed
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkts_late
                                    
                                    	Rx Pkts Late
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkts_unchecked
                                    
                                    	Rx Pkts Unchecked
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_octets_validated
                                    
                                    	Rx Octets Validated
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_octets_decrypted
                                    
                                    	Rx Octets Decrypted
                                    	**type**\: int
                                    
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
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('in_pkts_unused_sa', (YLeaf(YType.uint64, 'in-pkts-unused-sa'), ['int'])),
                                            ('in_pkts_not_using_sa', (YLeaf(YType.uint64, 'in-pkts-not-using-sa'), ['int'])),
                                            ('in_pkts_not_valid', (YLeaf(YType.uint64, 'in-pkts-not-valid'), ['int'])),
                                            ('in_pkts_invalid', (YLeaf(YType.uint64, 'in-pkts-invalid'), ['int'])),
                                            ('in_pkts_ok', (YLeaf(YType.uint64, 'in-pkts-ok'), ['int'])),
                                            ('in_pkts_delayed', (YLeaf(YType.uint64, 'in-pkts-delayed'), ['int'])),
                                            ('in_pkts_late', (YLeaf(YType.uint64, 'in-pkts-late'), ['int'])),
                                            ('in_pkts_unchecked', (YLeaf(YType.uint64, 'in-pkts-unchecked'), ['int'])),
                                            ('in_octets_validated', (YLeaf(YType.uint64, 'in-octets-validated'), ['int'])),
                                            ('in_octets_decrypted', (YLeaf(YType.uint64, 'in-octets-decrypted'), ['int'])),
                                        ])
                                        self.in_pkts_unused_sa = None
                                        self.in_pkts_not_using_sa = None
                                        self.in_pkts_not_valid = None
                                        self.in_pkts_invalid = None
                                        self.in_pkts_ok = None
                                        self.in_pkts_delayed = None
                                        self.in_pkts_late = None
                                        self.in_pkts_unchecked = None
                                        self.in_octets_validated = None
                                        self.in_octets_decrypted = None
                                        self._segment_path = lambda: "rx-sa-stats"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.MsfpgaStats.RxSaStats, ['in_pkts_unused_sa', 'in_pkts_not_using_sa', 'in_pkts_not_valid', 'in_pkts_invalid', 'in_pkts_ok', 'in_pkts_delayed', 'in_pkts_late', 'in_pkts_unchecked', 'in_octets_validated', 'in_octets_decrypted'], name, value)


                                class TxInterfaceMacsecStats(Entity):
                                    """
                                    Tx interface Macsec Stats
                                    
                                    .. attribute:: out_pkt_uncontrolled
                                    
                                    	Tx Pkts Uncontrolled
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_pkt_untagged
                                    
                                    	Tx Pkts Untagged
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_pkt_too_long
                                    
                                    	Tx Pkts Too Long
                                    	**type**\: int
                                    
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
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('out_pkt_uncontrolled', (YLeaf(YType.uint64, 'out-pkt-uncontrolled'), ['int'])),
                                            ('out_pkt_untagged', (YLeaf(YType.uint64, 'out-pkt-untagged'), ['int'])),
                                            ('out_pkt_too_long', (YLeaf(YType.uint64, 'out-pkt-too-long'), ['int'])),
                                        ])
                                        self.out_pkt_uncontrolled = None
                                        self.out_pkt_untagged = None
                                        self.out_pkt_too_long = None
                                        self._segment_path = lambda: "tx-interface-macsec-stats"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.MsfpgaStats.TxInterfaceMacsecStats, ['out_pkt_uncontrolled', 'out_pkt_untagged', 'out_pkt_too_long'], name, value)


                                class RxInterfaceMacsecStats(Entity):
                                    """
                                    Rx interface Macsec Stats
                                    
                                    .. attribute:: in_pkt_untagged
                                    
                                    	Rx Pkts Untagged
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkt_notag
                                    
                                    	Rx Pkts Notag
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkt_bad_tag
                                    
                                    	Rx Pkts Bad tag
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkt_no_sci
                                    
                                    	Rx Pkts No Sci
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkt_unknown_sci
                                    
                                    	Rx Pkts Unknown Sci
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkt_tagged
                                    
                                    	Rx Pkts Tagged
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkt_overrun
                                    
                                    	Rx Pkts Over Run
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkt_uncontrolled
                                    
                                    	Rx Pkts Uncontrolled
                                    	**type**\: int
                                    
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
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('in_pkt_untagged', (YLeaf(YType.uint64, 'in-pkt-untagged'), ['int'])),
                                            ('in_pkt_notag', (YLeaf(YType.uint64, 'in-pkt-notag'), ['int'])),
                                            ('in_pkt_bad_tag', (YLeaf(YType.uint64, 'in-pkt-bad-tag'), ['int'])),
                                            ('in_pkt_no_sci', (YLeaf(YType.uint64, 'in-pkt-no-sci'), ['int'])),
                                            ('in_pkt_unknown_sci', (YLeaf(YType.uint64, 'in-pkt-unknown-sci'), ['int'])),
                                            ('in_pkt_tagged', (YLeaf(YType.uint64, 'in-pkt-tagged'), ['int'])),
                                            ('in_pkt_overrun', (YLeaf(YType.uint64, 'in-pkt-overrun'), ['int'])),
                                            ('in_pkt_uncontrolled', (YLeaf(YType.uint64, 'in-pkt-uncontrolled'), ['int'])),
                                        ])
                                        self.in_pkt_untagged = None
                                        self.in_pkt_notag = None
                                        self.in_pkt_bad_tag = None
                                        self.in_pkt_no_sci = None
                                        self.in_pkt_unknown_sci = None
                                        self.in_pkt_tagged = None
                                        self.in_pkt_overrun = None
                                        self.in_pkt_uncontrolled = None
                                        self._segment_path = lambda: "rx-interface-macsec-stats"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.MsfpgaStats.RxInterfaceMacsecStats, ['in_pkt_untagged', 'in_pkt_notag', 'in_pkt_bad_tag', 'in_pkt_no_sci', 'in_pkt_unknown_sci', 'in_pkt_tagged', 'in_pkt_overrun', 'in_pkt_uncontrolled'], name, value)


                            class XlfpgaStats(Entity):
                                """
                                XLFPGA Stats
                                
                                .. attribute:: macsec_tx_stats
                                
                                	Tx SC and SA Level Stats
                                	**type**\:  :py:class:`MacsecTxStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.XlfpgaStats.MacsecTxStats>`
                                
                                .. attribute:: macsec_rx_stats
                                
                                	Rx SC and SA Level Stats
                                	**type**\:  :py:class:`MacsecRxStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.XlfpgaStats.MacsecRxStats>`
                                
                                

                                """

                                _prefix = 'crypto-macsec-pl-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.XlfpgaStats, self).__init__()

                                    self.yang_name = "xlfpga-stats"
                                    self.yang_parent_name = "ext"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("macsec-tx-stats", ("macsec_tx_stats", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.XlfpgaStats.MacsecTxStats)), ("macsec-rx-stats", ("macsec_rx_stats", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.XlfpgaStats.MacsecRxStats))])
                                    self._leafs = OrderedDict()

                                    self.macsec_tx_stats = MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.XlfpgaStats.MacsecTxStats()
                                    self.macsec_tx_stats.parent = self
                                    self._children_name_map["macsec_tx_stats"] = "macsec-tx-stats"

                                    self.macsec_rx_stats = MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.XlfpgaStats.MacsecRxStats()
                                    self.macsec_rx_stats.parent = self
                                    self._children_name_map["macsec_rx_stats"] = "macsec-rx-stats"
                                    self._segment_path = lambda: "xlfpga-stats"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.XlfpgaStats, [], name, value)


                                class MacsecTxStats(Entity):
                                    """
                                    Tx SC and SA Level Stats
                                    
                                    .. attribute:: sc_encrypted_octets
                                    
                                    	Tx Octets Encrypted
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_toolong_pkts
                                    
                                    	Tx Pkts Too Long
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_encrypted_pkts
                                    
                                    	Tx packets Encrypted
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_untagged_pkts
                                    
                                    	Tx Untagged Packets
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_overrun_pkts
                                    
                                    	Tx Overrun Packets
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_bypass_pkts
                                    
                                    	Tx Bypass Packets
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_eapol_pkts
                                    
                                    	Tx Eapol Packets
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_dropped_pkts
                                    
                                    	Tx Dropped Packets
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: current_an
                                    
                                    	Current Tx AN
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sa_encrypted_pkts
                                    
                                    	Current Tx SA Encrypted Packets
                                    	**type**\: int
                                    
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
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('sc_encrypted_octets', (YLeaf(YType.uint64, 'sc-encrypted-octets'), ['int'])),
                                            ('sc_toolong_pkts', (YLeaf(YType.uint64, 'sc-toolong-pkts'), ['int'])),
                                            ('sc_encrypted_pkts', (YLeaf(YType.uint64, 'sc-encrypted-pkts'), ['int'])),
                                            ('sc_untagged_pkts', (YLeaf(YType.uint64, 'sc-untagged-pkts'), ['int'])),
                                            ('sc_overrun_pkts', (YLeaf(YType.uint64, 'sc-overrun-pkts'), ['int'])),
                                            ('sc_bypass_pkts', (YLeaf(YType.uint64, 'sc-bypass-pkts'), ['int'])),
                                            ('sc_eapol_pkts', (YLeaf(YType.uint64, 'sc-eapol-pkts'), ['int'])),
                                            ('sc_dropped_pkts', (YLeaf(YType.uint64, 'sc-dropped-pkts'), ['int'])),
                                            ('current_an', (YLeaf(YType.uint64, 'current-an'), ['int'])),
                                            ('sa_encrypted_pkts', (YLeaf(YType.uint64, 'sa-encrypted-pkts'), ['int'])),
                                        ])
                                        self.sc_encrypted_octets = None
                                        self.sc_toolong_pkts = None
                                        self.sc_encrypted_pkts = None
                                        self.sc_untagged_pkts = None
                                        self.sc_overrun_pkts = None
                                        self.sc_bypass_pkts = None
                                        self.sc_eapol_pkts = None
                                        self.sc_dropped_pkts = None
                                        self.current_an = None
                                        self.sa_encrypted_pkts = None
                                        self._segment_path = lambda: "macsec-tx-stats"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.XlfpgaStats.MacsecTxStats, ['sc_encrypted_octets', 'sc_toolong_pkts', 'sc_encrypted_pkts', 'sc_untagged_pkts', 'sc_overrun_pkts', 'sc_bypass_pkts', 'sc_eapol_pkts', 'sc_dropped_pkts', 'current_an', 'sa_encrypted_pkts'], name, value)


                                class MacsecRxStats(Entity):
                                    """
                                    Rx SC and SA Level Stats
                                    
                                    .. attribute:: sc_decrypted_octets
                                    
                                    	Rx Octets Decrypted
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_no_tag_pkts
                                    
                                    	Rx No Tag Packets
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_untagged_pkts
                                    
                                    	Rx Untagged Packets
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_bad_tag_pkts
                                    
                                    	Rx Bad Tag Packets
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_late_pkts
                                    
                                    	Rx Late Pkts
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_delayed_pkts
                                    
                                    	Rx Delayed Pkts
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_unchecked_pkts
                                    
                                    	Rx Unchecked Pkts
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_no_sci_pkts
                                    
                                    	Rx No SCI Pkts
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_unknown_sci_pkts
                                    
                                    	Rx Unknown SCI Pkts
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_ok_pkts
                                    
                                    	Rx Pkts Ok
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_not_using_pkts
                                    
                                    	Rx Pkts Not Using SA
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_unused_pkts
                                    
                                    	Rx Pkts Unused SA
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_not_valid_pkts
                                    
                                    	Rx Not Valid Pkts
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_invalid_pkts
                                    
                                    	Rx Pkts Invalid
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_overrun_pkts
                                    
                                    	Rx Overrun Pkts
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_bypass_pkts
                                    
                                    	Rx Bypass Packets
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_eapol_pkts
                                    
                                    	Rx Eapol Packets
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_dropped_pkts
                                    
                                    	Rx Dropped Packets
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: rx_sa_stat
                                    
                                    	Rx SA Level Stats
                                    	**type**\: list of  		 :py:class:`RxSaStat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.XlfpgaStats.MacsecRxStats.RxSaStat>`
                                    
                                    

                                    """

                                    _prefix = 'crypto-macsec-pl-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.XlfpgaStats.MacsecRxStats, self).__init__()

                                        self.yang_name = "macsec-rx-stats"
                                        self.yang_parent_name = "xlfpga-stats"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("rx-sa-stat", ("rx_sa_stat", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.XlfpgaStats.MacsecRxStats.RxSaStat))])
                                        self._leafs = OrderedDict([
                                            ('sc_decrypted_octets', (YLeaf(YType.uint64, 'sc-decrypted-octets'), ['int'])),
                                            ('sc_no_tag_pkts', (YLeaf(YType.uint64, 'sc-no-tag-pkts'), ['int'])),
                                            ('sc_untagged_pkts', (YLeaf(YType.uint64, 'sc-untagged-pkts'), ['int'])),
                                            ('sc_bad_tag_pkts', (YLeaf(YType.uint64, 'sc-bad-tag-pkts'), ['int'])),
                                            ('sc_late_pkts', (YLeaf(YType.uint64, 'sc-late-pkts'), ['int'])),
                                            ('sc_delayed_pkts', (YLeaf(YType.uint64, 'sc-delayed-pkts'), ['int'])),
                                            ('sc_unchecked_pkts', (YLeaf(YType.uint64, 'sc-unchecked-pkts'), ['int'])),
                                            ('sc_no_sci_pkts', (YLeaf(YType.uint64, 'sc-no-sci-pkts'), ['int'])),
                                            ('sc_unknown_sci_pkts', (YLeaf(YType.uint64, 'sc-unknown-sci-pkts'), ['int'])),
                                            ('sc_ok_pkts', (YLeaf(YType.uint64, 'sc-ok-pkts'), ['int'])),
                                            ('sc_not_using_pkts', (YLeaf(YType.uint64, 'sc-not-using-pkts'), ['int'])),
                                            ('sc_unused_pkts', (YLeaf(YType.uint64, 'sc-unused-pkts'), ['int'])),
                                            ('sc_not_valid_pkts', (YLeaf(YType.uint64, 'sc-not-valid-pkts'), ['int'])),
                                            ('sc_invalid_pkts', (YLeaf(YType.uint64, 'sc-invalid-pkts'), ['int'])),
                                            ('sc_overrun_pkts', (YLeaf(YType.uint64, 'sc-overrun-pkts'), ['int'])),
                                            ('sc_bypass_pkts', (YLeaf(YType.uint64, 'sc-bypass-pkts'), ['int'])),
                                            ('sc_eapol_pkts', (YLeaf(YType.uint64, 'sc-eapol-pkts'), ['int'])),
                                            ('sc_dropped_pkts', (YLeaf(YType.uint64, 'sc-dropped-pkts'), ['int'])),
                                        ])
                                        self.sc_decrypted_octets = None
                                        self.sc_no_tag_pkts = None
                                        self.sc_untagged_pkts = None
                                        self.sc_bad_tag_pkts = None
                                        self.sc_late_pkts = None
                                        self.sc_delayed_pkts = None
                                        self.sc_unchecked_pkts = None
                                        self.sc_no_sci_pkts = None
                                        self.sc_unknown_sci_pkts = None
                                        self.sc_ok_pkts = None
                                        self.sc_not_using_pkts = None
                                        self.sc_unused_pkts = None
                                        self.sc_not_valid_pkts = None
                                        self.sc_invalid_pkts = None
                                        self.sc_overrun_pkts = None
                                        self.sc_bypass_pkts = None
                                        self.sc_eapol_pkts = None
                                        self.sc_dropped_pkts = None

                                        self.rx_sa_stat = YList(self)
                                        self._segment_path = lambda: "macsec-rx-stats"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.XlfpgaStats.MacsecRxStats, ['sc_decrypted_octets', 'sc_no_tag_pkts', 'sc_untagged_pkts', 'sc_bad_tag_pkts', 'sc_late_pkts', 'sc_delayed_pkts', 'sc_unchecked_pkts', 'sc_no_sci_pkts', 'sc_unknown_sci_pkts', 'sc_ok_pkts', 'sc_not_using_pkts', 'sc_unused_pkts', 'sc_not_valid_pkts', 'sc_invalid_pkts', 'sc_overrun_pkts', 'sc_bypass_pkts', 'sc_eapol_pkts', 'sc_dropped_pkts'], name, value)


                                    class RxSaStat(Entity):
                                        """
                                        Rx SA Level Stats
                                        
                                        .. attribute:: an
                                        
                                        	Current Rx AN
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: sa_ok_pkts
                                        
                                        	Rx Ok Pkts for Current AN
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: sa_not_using_pkts
                                        
                                        	Rx Pkts not using SA for Current AN
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: sa_unused_pkts
                                        
                                        	Rx Pkts Unused Pkts for Current AN
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: sa_not_valid_pkts
                                        
                                        	Rx Not Valid Pkts for Current AN
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: sa_invalid_pkts
                                        
                                        	Rx Invalid Pkts for current AN
                                        	**type**\: int
                                        
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
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('an', (YLeaf(YType.uint64, 'an'), ['int'])),
                                                ('sa_ok_pkts', (YLeaf(YType.uint64, 'sa-ok-pkts'), ['int'])),
                                                ('sa_not_using_pkts', (YLeaf(YType.uint64, 'sa-not-using-pkts'), ['int'])),
                                                ('sa_unused_pkts', (YLeaf(YType.uint64, 'sa-unused-pkts'), ['int'])),
                                                ('sa_not_valid_pkts', (YLeaf(YType.uint64, 'sa-not-valid-pkts'), ['int'])),
                                                ('sa_invalid_pkts', (YLeaf(YType.uint64, 'sa-invalid-pkts'), ['int'])),
                                            ])
                                            self.an = None
                                            self.sa_ok_pkts = None
                                            self.sa_not_using_pkts = None
                                            self.sa_unused_pkts = None
                                            self.sa_not_valid_pkts = None
                                            self.sa_invalid_pkts = None
                                            self._segment_path = lambda: "rx-sa-stat"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.XlfpgaStats.MacsecRxStats.RxSaStat, ['an', 'sa_ok_pkts', 'sa_not_using_pkts', 'sa_unused_pkts', 'sa_not_valid_pkts', 'sa_invalid_pkts'], name, value)


                            class Es200Stats(Entity):
                                """
                                ES200 Stats
                                
                                .. attribute:: tx_sa_stats
                                
                                	Tx SA Stats
                                	**type**\:  :py:class:`TxSaStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats.TxSaStats>`
                                
                                .. attribute:: rx_sa_stats
                                
                                	Rx SA Stats
                                	**type**\:  :py:class:`RxSaStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats.RxSaStats>`
                                
                                .. attribute:: tx_sc_macsec_stats
                                
                                	Tx SC Macsec Stats
                                	**type**\:  :py:class:`TxScMacsecStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats.TxScMacsecStats>`
                                
                                .. attribute:: rx_sc_macsec_stats
                                
                                	Rx SC Macsec Stats
                                	**type**\:  :py:class:`RxScMacsecStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats.RxScMacsecStats>`
                                
                                .. attribute:: tx_interface_macsec_stats
                                
                                	Tx interface Macsec Stats
                                	**type**\:  :py:class:`TxInterfaceMacsecStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats.TxInterfaceMacsecStats>`
                                
                                .. attribute:: rx_interface_macsec_stats
                                
                                	Rx interface Macsec Stats
                                	**type**\:  :py:class:`RxInterfaceMacsecStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats.RxInterfaceMacsecStats>`
                                
                                .. attribute:: tx_port_stats
                                
                                	Port level TX Stats
                                	**type**\:  :py:class:`TxPortStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats.TxPortStats>`
                                
                                .. attribute:: rx_port_stats
                                
                                	Port level RX Stats
                                	**type**\:  :py:class:`RxPortStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats.RxPortStats>`
                                
                                

                                """

                                _prefix = 'crypto-macsec-pl-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats, self).__init__()

                                    self.yang_name = "es200-stats"
                                    self.yang_parent_name = "ext"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("tx-sa-stats", ("tx_sa_stats", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats.TxSaStats)), ("rx-sa-stats", ("rx_sa_stats", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats.RxSaStats)), ("tx-sc-macsec-stats", ("tx_sc_macsec_stats", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats.TxScMacsecStats)), ("rx-sc-macsec-stats", ("rx_sc_macsec_stats", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats.RxScMacsecStats)), ("tx-interface-macsec-stats", ("tx_interface_macsec_stats", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats.TxInterfaceMacsecStats)), ("rx-interface-macsec-stats", ("rx_interface_macsec_stats", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats.RxInterfaceMacsecStats)), ("tx-port-stats", ("tx_port_stats", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats.TxPortStats)), ("rx-port-stats", ("rx_port_stats", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats.RxPortStats))])
                                    self._leafs = OrderedDict()

                                    self.tx_sa_stats = MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats.TxSaStats()
                                    self.tx_sa_stats.parent = self
                                    self._children_name_map["tx_sa_stats"] = "tx-sa-stats"

                                    self.rx_sa_stats = MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats.RxSaStats()
                                    self.rx_sa_stats.parent = self
                                    self._children_name_map["rx_sa_stats"] = "rx-sa-stats"

                                    self.tx_sc_macsec_stats = MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats.TxScMacsecStats()
                                    self.tx_sc_macsec_stats.parent = self
                                    self._children_name_map["tx_sc_macsec_stats"] = "tx-sc-macsec-stats"

                                    self.rx_sc_macsec_stats = MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats.RxScMacsecStats()
                                    self.rx_sc_macsec_stats.parent = self
                                    self._children_name_map["rx_sc_macsec_stats"] = "rx-sc-macsec-stats"

                                    self.tx_interface_macsec_stats = MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats.TxInterfaceMacsecStats()
                                    self.tx_interface_macsec_stats.parent = self
                                    self._children_name_map["tx_interface_macsec_stats"] = "tx-interface-macsec-stats"

                                    self.rx_interface_macsec_stats = MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats.RxInterfaceMacsecStats()
                                    self.rx_interface_macsec_stats.parent = self
                                    self._children_name_map["rx_interface_macsec_stats"] = "rx-interface-macsec-stats"

                                    self.tx_port_stats = MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats.TxPortStats()
                                    self.tx_port_stats.parent = self
                                    self._children_name_map["tx_port_stats"] = "tx-port-stats"

                                    self.rx_port_stats = MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats.RxPortStats()
                                    self.rx_port_stats.parent = self
                                    self._children_name_map["rx_port_stats"] = "rx-port-stats"
                                    self._segment_path = lambda: "es200-stats"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats, [], name, value)


                                class TxSaStats(Entity):
                                    """
                                    Tx SA Stats
                                    
                                    .. attribute:: out_pkts_too_long
                                    
                                    	packets exceeding egress MTU
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_pkts_encrypted_protected
                                    
                                    	packets encrypted/protected
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_octets_encrypted_protected1
                                    
                                    	octets1 encrypted/protected ?
                                    	**type**\: int
                                    
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
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('out_pkts_too_long', (YLeaf(YType.uint64, 'out-pkts-too-long'), ['int'])),
                                            ('out_pkts_encrypted_protected', (YLeaf(YType.uint64, 'out-pkts-encrypted-protected'), ['int'])),
                                            ('out_octets_encrypted_protected1', (YLeaf(YType.uint64, 'out-octets-encrypted-protected1'), ['int'])),
                                        ])
                                        self.out_pkts_too_long = None
                                        self.out_pkts_encrypted_protected = None
                                        self.out_octets_encrypted_protected1 = None
                                        self._segment_path = lambda: "tx-sa-stats"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats.TxSaStats, ['out_pkts_too_long', 'out_pkts_encrypted_protected', 'out_octets_encrypted_protected1'], name, value)


                                class RxSaStats(Entity):
                                    """
                                    Rx SA Stats
                                    
                                    .. attribute:: in_pkts_unchecked
                                    
                                    	frame not valid & validateFrames disabled
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkts_delayed
                                    
                                    	PN of packet outside replay window & validateFrames !strict
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkts_late
                                    
                                    	PN of packet outside replay window & validateFrames strict
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkts_ok
                                    
                                    	packets with no error
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkts_invalid
                                    
                                    	packet not valid & validateFrames !strict
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkts_not_valid
                                    
                                    	packet not valid & validateFrames strict
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkts_not_using_sa
                                    
                                    	packet assigned to SA not in use & validateFrames strict
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkts_unused_sa
                                    
                                    	packet assigned to SA not in use & validateFrames !strict
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_octets_decrypted_validated1
                                    
                                    	octets1 decrypted/validated
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_octets_validated
                                    
                                    	octets validated
                                    	**type**\: int
                                    
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
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('in_pkts_unchecked', (YLeaf(YType.uint64, 'in-pkts-unchecked'), ['int'])),
                                            ('in_pkts_delayed', (YLeaf(YType.uint64, 'in-pkts-delayed'), ['int'])),
                                            ('in_pkts_late', (YLeaf(YType.uint64, 'in-pkts-late'), ['int'])),
                                            ('in_pkts_ok', (YLeaf(YType.uint64, 'in-pkts-ok'), ['int'])),
                                            ('in_pkts_invalid', (YLeaf(YType.uint64, 'in-pkts-invalid'), ['int'])),
                                            ('in_pkts_not_valid', (YLeaf(YType.uint64, 'in-pkts-not-valid'), ['int'])),
                                            ('in_pkts_not_using_sa', (YLeaf(YType.uint64, 'in-pkts-not-using-sa'), ['int'])),
                                            ('in_pkts_unused_sa', (YLeaf(YType.uint64, 'in-pkts-unused-sa'), ['int'])),
                                            ('in_octets_decrypted_validated1', (YLeaf(YType.uint64, 'in-octets-decrypted-validated1'), ['int'])),
                                            ('in_octets_validated', (YLeaf(YType.uint64, 'in-octets-validated'), ['int'])),
                                        ])
                                        self.in_pkts_unchecked = None
                                        self.in_pkts_delayed = None
                                        self.in_pkts_late = None
                                        self.in_pkts_ok = None
                                        self.in_pkts_invalid = None
                                        self.in_pkts_not_valid = None
                                        self.in_pkts_not_using_sa = None
                                        self.in_pkts_unused_sa = None
                                        self.in_octets_decrypted_validated1 = None
                                        self.in_octets_validated = None
                                        self._segment_path = lambda: "rx-sa-stats"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats.RxSaStats, ['in_pkts_unchecked', 'in_pkts_delayed', 'in_pkts_late', 'in_pkts_ok', 'in_pkts_invalid', 'in_pkts_not_valid', 'in_pkts_not_using_sa', 'in_pkts_unused_sa', 'in_octets_decrypted_validated1', 'in_octets_validated'], name, value)


                                class TxScMacsecStats(Entity):
                                    """
                                    Tx SC Macsec Stats
                                    
                                    .. attribute:: out_pkts_sa_not_in_use
                                    
                                    	Packets received with SA not in use
                                    	**type**\: int
                                    
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
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('out_pkts_sa_not_in_use', (YLeaf(YType.uint64, 'out-pkts-sa-not-in-use'), ['int'])),
                                        ])
                                        self.out_pkts_sa_not_in_use = None
                                        self._segment_path = lambda: "tx-sc-macsec-stats"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats.TxScMacsecStats, ['out_pkts_sa_not_in_use'], name, value)


                                class RxScMacsecStats(Entity):
                                    """
                                    Rx SC Macsec Stats
                                    
                                    .. attribute:: in_pkts_sa_not_in_use
                                    
                                    	Packets received with SA not in use
                                    	**type**\: int
                                    
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
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('in_pkts_sa_not_in_use', (YLeaf(YType.uint64, 'in-pkts-sa-not-in-use'), ['int'])),
                                        ])
                                        self.in_pkts_sa_not_in_use = None
                                        self._segment_path = lambda: "rx-sc-macsec-stats"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats.RxScMacsecStats, ['in_pkts_sa_not_in_use'], name, value)


                                class TxInterfaceMacsecStats(Entity):
                                    """
                                    Tx interface Macsec Stats
                                    
                                    .. attribute:: transform_error_pkts
                                    
                                    	counter to count internal errors in the MACSec core
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_pkt_ctrl
                                    
                                    	egress packet that is classified as control packet
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_pkts_untagged
                                    
                                    	egress packet to go out untagged when protectFrames not set
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_octets_unctrl
                                    
                                    	Octets tx on uncontrolled port
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_octets_ctrl
                                    
                                    	Octets tx on controlled port
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_octets_common
                                    
                                    	Octets tx on common port
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_ucast_pkts_unctrl
                                    
                                    	Unicast pkts tx on uncontrolled port
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_ucast_pkts_ctrl
                                    
                                    	Unicast pkts tx on controlled port
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_mcast_pkts_unctrl
                                    
                                    	Multicast pkts tx on uncontrolled port
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_mcast_pkts_ctrl
                                    
                                    	Multicast pkts tx on controlled port
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_bcast_pkts_unctrl
                                    
                                    	Broadcast pkts tx on uncontrolled port
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_bcast_pkts_ctrl
                                    
                                    	Broadcast pkts tx on controlled port
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_rx_drop_pkts_unctrl
                                    
                                    	Control pkts dropped due to overrun
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_rx_drop_pkts_ctrl
                                    
                                    	Data pkts dropped due to overrun
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_rx_err_pkts_unctrl
                                    
                                    	Control pkts error\-terminated due to overrun
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_rx_err_pkts_ctrl
                                    
                                    	Data pkts error\-terminated due to overrun
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_drop_pkts_class
                                    
                                    	Packets dropped due to overflow in classification pipeline
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_drop_pkts_data
                                    
                                    	Packets dropped due to overflow in  processing pipeline
                                    	**type**\: int
                                    
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
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('transform_error_pkts', (YLeaf(YType.uint64, 'transform-error-pkts'), ['int'])),
                                            ('out_pkt_ctrl', (YLeaf(YType.uint64, 'out-pkt-ctrl'), ['int'])),
                                            ('out_pkts_untagged', (YLeaf(YType.uint64, 'out-pkts-untagged'), ['int'])),
                                            ('out_octets_unctrl', (YLeaf(YType.uint64, 'out-octets-unctrl'), ['int'])),
                                            ('out_octets_ctrl', (YLeaf(YType.uint64, 'out-octets-ctrl'), ['int'])),
                                            ('out_octets_common', (YLeaf(YType.uint64, 'out-octets-common'), ['int'])),
                                            ('out_ucast_pkts_unctrl', (YLeaf(YType.uint64, 'out-ucast-pkts-unctrl'), ['int'])),
                                            ('out_ucast_pkts_ctrl', (YLeaf(YType.uint64, 'out-ucast-pkts-ctrl'), ['int'])),
                                            ('out_mcast_pkts_unctrl', (YLeaf(YType.uint64, 'out-mcast-pkts-unctrl'), ['int'])),
                                            ('out_mcast_pkts_ctrl', (YLeaf(YType.uint64, 'out-mcast-pkts-ctrl'), ['int'])),
                                            ('out_bcast_pkts_unctrl', (YLeaf(YType.uint64, 'out-bcast-pkts-unctrl'), ['int'])),
                                            ('out_bcast_pkts_ctrl', (YLeaf(YType.uint64, 'out-bcast-pkts-ctrl'), ['int'])),
                                            ('out_rx_drop_pkts_unctrl', (YLeaf(YType.uint64, 'out-rx-drop-pkts-unctrl'), ['int'])),
                                            ('out_rx_drop_pkts_ctrl', (YLeaf(YType.uint64, 'out-rx-drop-pkts-ctrl'), ['int'])),
                                            ('out_rx_err_pkts_unctrl', (YLeaf(YType.uint64, 'out-rx-err-pkts-unctrl'), ['int'])),
                                            ('out_rx_err_pkts_ctrl', (YLeaf(YType.uint64, 'out-rx-err-pkts-ctrl'), ['int'])),
                                            ('out_drop_pkts_class', (YLeaf(YType.uint64, 'out-drop-pkts-class'), ['int'])),
                                            ('out_drop_pkts_data', (YLeaf(YType.uint64, 'out-drop-pkts-data'), ['int'])),
                                        ])
                                        self.transform_error_pkts = None
                                        self.out_pkt_ctrl = None
                                        self.out_pkts_untagged = None
                                        self.out_octets_unctrl = None
                                        self.out_octets_ctrl = None
                                        self.out_octets_common = None
                                        self.out_ucast_pkts_unctrl = None
                                        self.out_ucast_pkts_ctrl = None
                                        self.out_mcast_pkts_unctrl = None
                                        self.out_mcast_pkts_ctrl = None
                                        self.out_bcast_pkts_unctrl = None
                                        self.out_bcast_pkts_ctrl = None
                                        self.out_rx_drop_pkts_unctrl = None
                                        self.out_rx_drop_pkts_ctrl = None
                                        self.out_rx_err_pkts_unctrl = None
                                        self.out_rx_err_pkts_ctrl = None
                                        self.out_drop_pkts_class = None
                                        self.out_drop_pkts_data = None
                                        self._segment_path = lambda: "tx-interface-macsec-stats"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats.TxInterfaceMacsecStats, ['transform_error_pkts', 'out_pkt_ctrl', 'out_pkts_untagged', 'out_octets_unctrl', 'out_octets_ctrl', 'out_octets_common', 'out_ucast_pkts_unctrl', 'out_ucast_pkts_ctrl', 'out_mcast_pkts_unctrl', 'out_mcast_pkts_ctrl', 'out_bcast_pkts_unctrl', 'out_bcast_pkts_ctrl', 'out_rx_drop_pkts_unctrl', 'out_rx_drop_pkts_ctrl', 'out_rx_err_pkts_unctrl', 'out_rx_err_pkts_ctrl', 'out_drop_pkts_class', 'out_drop_pkts_data'], name, value)


                                class RxInterfaceMacsecStats(Entity):
                                    """
                                    Rx interface Macsec Stats
                                    
                                    .. attribute:: transform_error_pkts
                                    
                                    	counter to count internal errors in the MACSec core
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkt_ctrl
                                    
                                    	ingress packet that is classified as control packet
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkt_no_tag
                                    
                                    	ingress packet untagged & validateFrames is strict
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkts_untagged
                                    
                                    	ingress packet untagged & validateFrames is  !strict
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkt_bad_tag
                                    
                                    	ingress frames received with an invalid MACSec tag or ICV                                       added with next one gives InPktsSCIMiss
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkt_no_sci
                                    
                                    	correctly tagged ingress frames for which no valid SC found &                                 validateFrames is strict
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkts_unknown_sci
                                    
                                    	correctly tagged ingress frames for which no valid SC found &                                 validateFrames is !strict
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkts_tagged_ctrl
                                    
                                    	ingress packets that are control or KaY packets
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_octets_unctrl
                                    
                                    	Octets rx on uncontrolled port
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_octets_ctrl
                                    
                                    	Octets rx on controlled port
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_ucast_pkts_unctrl
                                    
                                    	Unicast pkts rx on uncontrolled port
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_ucast_pkts_ctrl
                                    
                                    	Unicast pkts rx on controlled port
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_mcast_pkts_unctrl
                                    
                                    	Multicast pkts rx on uncontrolled port
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_mcast_pkts_ctrl
                                    
                                    	Multicast pkts rx on controlled port
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_bcast_pkts_unctrl
                                    
                                    	Broadcast pkts rx on uncontrolled port
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_bcast_pkts_ctrl
                                    
                                    	Broadcast pkts rx on controlled port
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_rx_drop_pkts_unctrl
                                    
                                    	Control pkts dropped due to overrun
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_rx_drop_pkts_ctrl
                                    
                                    	Data pkts dropped due to overrun
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_rx_error_pkts_unctrl
                                    
                                    	Control pkts error\-terminated due to overrun
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_rx_error_pkts_ctrl
                                    
                                    	Data pkts error\-terminated due to overrun
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_drop_pkts_class
                                    
                                    	Packets dropped due to overflow in classification pipeline
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_drop_pkts_data
                                    
                                    	Packets dropped due to overflow in processing pipeline
                                    	**type**\: int
                                    
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
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('transform_error_pkts', (YLeaf(YType.uint64, 'transform-error-pkts'), ['int'])),
                                            ('in_pkt_ctrl', (YLeaf(YType.uint64, 'in-pkt-ctrl'), ['int'])),
                                            ('in_pkt_no_tag', (YLeaf(YType.uint64, 'in-pkt-no-tag'), ['int'])),
                                            ('in_pkts_untagged', (YLeaf(YType.uint64, 'in-pkts-untagged'), ['int'])),
                                            ('in_pkt_bad_tag', (YLeaf(YType.uint64, 'in-pkt-bad-tag'), ['int'])),
                                            ('in_pkt_no_sci', (YLeaf(YType.uint64, 'in-pkt-no-sci'), ['int'])),
                                            ('in_pkts_unknown_sci', (YLeaf(YType.uint64, 'in-pkts-unknown-sci'), ['int'])),
                                            ('in_pkts_tagged_ctrl', (YLeaf(YType.uint64, 'in-pkts-tagged-ctrl'), ['int'])),
                                            ('in_octets_unctrl', (YLeaf(YType.uint64, 'in-octets-unctrl'), ['int'])),
                                            ('in_octets_ctrl', (YLeaf(YType.uint64, 'in-octets-ctrl'), ['int'])),
                                            ('in_ucast_pkts_unctrl', (YLeaf(YType.uint64, 'in-ucast-pkts-unctrl'), ['int'])),
                                            ('in_ucast_pkts_ctrl', (YLeaf(YType.uint64, 'in-ucast-pkts-ctrl'), ['int'])),
                                            ('in_mcast_pkts_unctrl', (YLeaf(YType.uint64, 'in-mcast-pkts-unctrl'), ['int'])),
                                            ('in_mcast_pkts_ctrl', (YLeaf(YType.uint64, 'in-mcast-pkts-ctrl'), ['int'])),
                                            ('in_bcast_pkts_unctrl', (YLeaf(YType.uint64, 'in-bcast-pkts-unctrl'), ['int'])),
                                            ('in_bcast_pkts_ctrl', (YLeaf(YType.uint64, 'in-bcast-pkts-ctrl'), ['int'])),
                                            ('in_rx_drop_pkts_unctrl', (YLeaf(YType.uint64, 'in-rx-drop-pkts-unctrl'), ['int'])),
                                            ('in_rx_drop_pkts_ctrl', (YLeaf(YType.uint64, 'in-rx-drop-pkts-ctrl'), ['int'])),
                                            ('in_rx_error_pkts_unctrl', (YLeaf(YType.uint64, 'in-rx-error-pkts-unctrl'), ['int'])),
                                            ('in_rx_error_pkts_ctrl', (YLeaf(YType.uint64, 'in-rx-error-pkts-ctrl'), ['int'])),
                                            ('in_drop_pkts_class', (YLeaf(YType.uint64, 'in-drop-pkts-class'), ['int'])),
                                            ('in_drop_pkts_data', (YLeaf(YType.uint64, 'in-drop-pkts-data'), ['int'])),
                                        ])
                                        self.transform_error_pkts = None
                                        self.in_pkt_ctrl = None
                                        self.in_pkt_no_tag = None
                                        self.in_pkts_untagged = None
                                        self.in_pkt_bad_tag = None
                                        self.in_pkt_no_sci = None
                                        self.in_pkts_unknown_sci = None
                                        self.in_pkts_tagged_ctrl = None
                                        self.in_octets_unctrl = None
                                        self.in_octets_ctrl = None
                                        self.in_ucast_pkts_unctrl = None
                                        self.in_ucast_pkts_ctrl = None
                                        self.in_mcast_pkts_unctrl = None
                                        self.in_mcast_pkts_ctrl = None
                                        self.in_bcast_pkts_unctrl = None
                                        self.in_bcast_pkts_ctrl = None
                                        self.in_rx_drop_pkts_unctrl = None
                                        self.in_rx_drop_pkts_ctrl = None
                                        self.in_rx_error_pkts_unctrl = None
                                        self.in_rx_error_pkts_ctrl = None
                                        self.in_drop_pkts_class = None
                                        self.in_drop_pkts_data = None
                                        self._segment_path = lambda: "rx-interface-macsec-stats"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats.RxInterfaceMacsecStats, ['transform_error_pkts', 'in_pkt_ctrl', 'in_pkt_no_tag', 'in_pkts_untagged', 'in_pkt_bad_tag', 'in_pkt_no_sci', 'in_pkts_unknown_sci', 'in_pkts_tagged_ctrl', 'in_octets_unctrl', 'in_octets_ctrl', 'in_ucast_pkts_unctrl', 'in_ucast_pkts_ctrl', 'in_mcast_pkts_unctrl', 'in_mcast_pkts_ctrl', 'in_bcast_pkts_unctrl', 'in_bcast_pkts_ctrl', 'in_rx_drop_pkts_unctrl', 'in_rx_drop_pkts_ctrl', 'in_rx_error_pkts_unctrl', 'in_rx_error_pkts_ctrl', 'in_drop_pkts_class', 'in_drop_pkts_data'], name, value)


                                class TxPortStats(Entity):
                                    """
                                    Port level TX Stats
                                    
                                    .. attribute:: multi_flow_match
                                    
                                    	Pkts matching multiple flow entries
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: parser_dropped
                                    
                                    	Pkts dropped by header parser as invalid
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: flow_miss
                                    
                                    	Pkts matching none of flow entries
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: pkts_ctrl
                                    
                                    	Control pkts forwarded
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: pkts_data
                                    
                                    	Data pkts forwarded
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: pkts_dropped
                                    
                                    	Pkts dropped by classifier
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: pkts_err_in
                                    
                                    	Pkts received with an error indication
                                    	**type**\: int
                                    
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
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('multi_flow_match', (YLeaf(YType.uint64, 'multi-flow-match'), ['int'])),
                                            ('parser_dropped', (YLeaf(YType.uint64, 'parser-dropped'), ['int'])),
                                            ('flow_miss', (YLeaf(YType.uint64, 'flow-miss'), ['int'])),
                                            ('pkts_ctrl', (YLeaf(YType.uint64, 'pkts-ctrl'), ['int'])),
                                            ('pkts_data', (YLeaf(YType.uint64, 'pkts-data'), ['int'])),
                                            ('pkts_dropped', (YLeaf(YType.uint64, 'pkts-dropped'), ['int'])),
                                            ('pkts_err_in', (YLeaf(YType.uint64, 'pkts-err-in'), ['int'])),
                                        ])
                                        self.multi_flow_match = None
                                        self.parser_dropped = None
                                        self.flow_miss = None
                                        self.pkts_ctrl = None
                                        self.pkts_data = None
                                        self.pkts_dropped = None
                                        self.pkts_err_in = None
                                        self._segment_path = lambda: "tx-port-stats"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats.TxPortStats, ['multi_flow_match', 'parser_dropped', 'flow_miss', 'pkts_ctrl', 'pkts_data', 'pkts_dropped', 'pkts_err_in'], name, value)


                                class RxPortStats(Entity):
                                    """
                                    Port level RX Stats
                                    
                                    .. attribute:: multi_flow_match
                                    
                                    	Pkts matching multiple flow entries
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: parser_dropped
                                    
                                    	Pkts dropped by header parser as invalid
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: flow_miss
                                    
                                    	Pkts matching none of flow entries
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: pkts_ctrl
                                    
                                    	Control pkts forwarded
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: pkts_data
                                    
                                    	Data pkts forwarded
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: pkts_dropped
                                    
                                    	Pkts dropped by classifier
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: pkts_err_in
                                    
                                    	Pkts received with an error indication
                                    	**type**\: int
                                    
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
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('multi_flow_match', (YLeaf(YType.uint64, 'multi-flow-match'), ['int'])),
                                            ('parser_dropped', (YLeaf(YType.uint64, 'parser-dropped'), ['int'])),
                                            ('flow_miss', (YLeaf(YType.uint64, 'flow-miss'), ['int'])),
                                            ('pkts_ctrl', (YLeaf(YType.uint64, 'pkts-ctrl'), ['int'])),
                                            ('pkts_data', (YLeaf(YType.uint64, 'pkts-data'), ['int'])),
                                            ('pkts_dropped', (YLeaf(YType.uint64, 'pkts-dropped'), ['int'])),
                                            ('pkts_err_in', (YLeaf(YType.uint64, 'pkts-err-in'), ['int'])),
                                        ])
                                        self.multi_flow_match = None
                                        self.parser_dropped = None
                                        self.flow_miss = None
                                        self.pkts_ctrl = None
                                        self.pkts_data = None
                                        self.pkts_dropped = None
                                        self.pkts_err_in = None
                                        self._segment_path = lambda: "rx-port-stats"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwStatistics.Ext.Es200Stats.RxPortStats, ['multi_flow_match', 'parser_dropped', 'flow_miss', 'pkts_ctrl', 'pkts_data', 'pkts_dropped', 'pkts_err_in'], name, value)


                    class HwSas(Entity):
                        """
                        Table of Hardware SAs
                        
                        .. attribute:: hw_sa
                        
                        	Hardware Security Association
                        	**type**\: list of  		 :py:class:`HwSa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa>`
                        
                        

                        """

                        _prefix = 'crypto-macsec-pl-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas, self).__init__()

                            self.yang_name = "hw-sas"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("hw-sa", ("hw_sa", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa))])
                            self._leafs = OrderedDict()

                            self.hw_sa = YList(self)
                            self._segment_path = lambda: "hw-sas"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas, [], name, value)


                        class HwSa(Entity):
                            """
                            Hardware Security Association
                            
                            .. attribute:: sa_id  (key)
                            
                            	SA ID
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: ext
                            
                            	ext
                            	**type**\:  :py:class:`Ext <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext>`
                            
                            

                            """

                            _prefix = 'crypto-macsec-pl-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa, self).__init__()

                                self.yang_name = "hw-sa"
                                self.yang_parent_name = "hw-sas"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['sa_id']
                                self._child_classes = OrderedDict([("ext", ("ext", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext))])
                                self._leafs = OrderedDict([
                                    ('sa_id', (YLeaf(YType.uint32, 'sa-id'), ['int'])),
                                ])
                                self.sa_id = None

                                self.ext = MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext()
                                self.ext.parent = self
                                self._children_name_map["ext"] = "ext"
                                self._segment_path = lambda: "hw-sa" + "[sa-id='" + str(self.sa_id) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa, ['sa_id'], name, value)


                            class Ext(Entity):
                                """
                                ext
                                
                                .. attribute:: msfpga_sa
                                
                                	MSFPGA SA Information
                                	**type**\:  :py:class:`MsfpgaSa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.MsfpgaSa>`
                                
                                .. attribute:: xlfpga_sa
                                
                                	XLFPGA SA Information
                                	**type**\:  :py:class:`XlfpgaSa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.XlfpgaSa>`
                                
                                .. attribute:: es200_sa
                                
                                	ES200 SA Information
                                	**type**\:  :py:class:`Es200Sa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.Es200Sa>`
                                
                                .. attribute:: type
                                
                                	type
                                	**type**\:  :py:class:`MacsecPhyVendor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPhyVendor>`
                                
                                

                                """

                                _prefix = 'crypto-macsec-pl-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext, self).__init__()

                                    self.yang_name = "ext"
                                    self.yang_parent_name = "hw-sa"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("msfpga-sa", ("msfpga_sa", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.MsfpgaSa)), ("xlfpga-sa", ("xlfpga_sa", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.XlfpgaSa)), ("es200-sa", ("es200_sa", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.Es200Sa))])
                                    self._leafs = OrderedDict([
                                        ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'MacsecPhyVendor', '')])),
                                    ])
                                    self.type = None

                                    self.msfpga_sa = MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.MsfpgaSa()
                                    self.msfpga_sa.parent = self
                                    self._children_name_map["msfpga_sa"] = "msfpga-sa"

                                    self.xlfpga_sa = MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.XlfpgaSa()
                                    self.xlfpga_sa.parent = self
                                    self._children_name_map["xlfpga_sa"] = "xlfpga-sa"

                                    self.es200_sa = MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.Es200Sa()
                                    self.es200_sa.parent = self
                                    self._children_name_map["es200_sa"] = "es200-sa"
                                    self._segment_path = lambda: "ext"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext, ['type'], name, value)


                                class MsfpgaSa(Entity):
                                    """
                                    MSFPGA SA Information
                                    
                                    .. attribute:: tx_sa
                                    
                                    	Tx SA Details
                                    	**type**\:  :py:class:`TxSa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.MsfpgaSa.TxSa>`
                                    
                                    .. attribute:: rx_sa
                                    
                                    	Rx SA Details
                                    	**type**\:  :py:class:`RxSa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.MsfpgaSa.RxSa>`
                                    
                                    

                                    """

                                    _prefix = 'crypto-macsec-pl-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.MsfpgaSa, self).__init__()

                                        self.yang_name = "msfpga-sa"
                                        self.yang_parent_name = "ext"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("tx-sa", ("tx_sa", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.MsfpgaSa.TxSa)), ("rx-sa", ("rx_sa", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.MsfpgaSa.RxSa))])
                                        self._leafs = OrderedDict()

                                        self.tx_sa = MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.MsfpgaSa.TxSa()
                                        self.tx_sa.parent = self
                                        self._children_name_map["tx_sa"] = "tx-sa"

                                        self.rx_sa = MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.MsfpgaSa.RxSa()
                                        self.rx_sa.parent = self
                                        self._children_name_map["rx_sa"] = "rx-sa"
                                        self._segment_path = lambda: "msfpga-sa"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.MsfpgaSa, [], name, value)


                                    class TxSa(Entity):
                                        """
                                        Tx SA Details
                                        
                                        .. attribute:: sa_id
                                        
                                        	SA Index
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: valid
                                        
                                        	SA Validity
                                        	**type**\: bool
                                        
                                        .. attribute:: is_egress
                                        
                                        	rx\_tx direction
                                        	**type**\: bool
                                        
                                        .. attribute:: crypto_algo
                                        
                                        	Crypto Algorithm
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: key_len
                                        
                                        	Key Length
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: an
                                        
                                        	Association Number
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: xpn
                                        
                                        	XPN EN
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: sci
                                        
                                        	SCI
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: in_use
                                        
                                        	In Use
                                        	**type**\: bool
                                        
                                        .. attribute:: next_pn
                                        
                                        	Next Packet Number
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: c_offset
                                        
                                        	Conf offset
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: action
                                        
                                        	Action
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: q_bit
                                        
                                        	Q bit
                                        	**type**\: bool
                                        
                                        .. attribute:: qq_bit
                                        
                                        	QQ bit
                                        	**type**\: bool
                                        
                                        

                                        """

                                        _prefix = 'crypto-macsec-pl-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.MsfpgaSa.TxSa, self).__init__()

                                            self.yang_name = "tx-sa"
                                            self.yang_parent_name = "msfpga-sa"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('sa_id', (YLeaf(YType.uint8, 'sa-id'), ['int'])),
                                                ('valid', (YLeaf(YType.boolean, 'valid'), ['bool'])),
                                                ('is_egress', (YLeaf(YType.boolean, 'is-egress'), ['bool'])),
                                                ('crypto_algo', (YLeaf(YType.uint8, 'crypto-algo'), ['int'])),
                                                ('key_len', (YLeaf(YType.uint8, 'key-len'), ['int'])),
                                                ('an', (YLeaf(YType.uint8, 'an'), ['int'])),
                                                ('xpn', (YLeaf(YType.uint8, 'xpn'), ['int'])),
                                                ('sci', (YLeaf(YType.uint64, 'sci'), ['int'])),
                                                ('in_use', (YLeaf(YType.boolean, 'in-use'), ['bool'])),
                                                ('next_pn', (YLeaf(YType.uint64, 'next-pn'), ['int'])),
                                                ('c_offset', (YLeaf(YType.uint8, 'c-offset'), ['int'])),
                                                ('action', (YLeaf(YType.uint8, 'action'), ['int'])),
                                                ('q_bit', (YLeaf(YType.boolean, 'q-bit'), ['bool'])),
                                                ('qq_bit', (YLeaf(YType.boolean, 'qq-bit'), ['bool'])),
                                            ])
                                            self.sa_id = None
                                            self.valid = None
                                            self.is_egress = None
                                            self.crypto_algo = None
                                            self.key_len = None
                                            self.an = None
                                            self.xpn = None
                                            self.sci = None
                                            self.in_use = None
                                            self.next_pn = None
                                            self.c_offset = None
                                            self.action = None
                                            self.q_bit = None
                                            self.qq_bit = None
                                            self._segment_path = lambda: "tx-sa"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.MsfpgaSa.TxSa, ['sa_id', 'valid', 'is_egress', 'crypto_algo', 'key_len', 'an', 'xpn', 'sci', 'in_use', 'next_pn', 'c_offset', 'action', 'q_bit', 'qq_bit'], name, value)


                                    class RxSa(Entity):
                                        """
                                        Rx SA Details
                                        
                                        .. attribute:: sa_id
                                        
                                        	SA Index
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: valid
                                        
                                        	SA Validity
                                        	**type**\: bool
                                        
                                        .. attribute:: is_egress
                                        
                                        	rx\_tx direction
                                        	**type**\: bool
                                        
                                        .. attribute:: crypto_algo
                                        
                                        	Crypto Algorithm
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: key_len
                                        
                                        	Key Length
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: an
                                        
                                        	Association Number
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: xpn
                                        
                                        	XPN EN
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: sci
                                        
                                        	SCI
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: in_use
                                        
                                        	In Use
                                        	**type**\: bool
                                        
                                        .. attribute:: next_pn
                                        
                                        	Next Packet Number
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: c_offset
                                        
                                        	Conf offset
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: action
                                        
                                        	Action
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: q_bit
                                        
                                        	Q bit
                                        	**type**\: bool
                                        
                                        .. attribute:: qq_bit
                                        
                                        	QQ bit
                                        	**type**\: bool
                                        
                                        

                                        """

                                        _prefix = 'crypto-macsec-pl-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.MsfpgaSa.RxSa, self).__init__()

                                            self.yang_name = "rx-sa"
                                            self.yang_parent_name = "msfpga-sa"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('sa_id', (YLeaf(YType.uint8, 'sa-id'), ['int'])),
                                                ('valid', (YLeaf(YType.boolean, 'valid'), ['bool'])),
                                                ('is_egress', (YLeaf(YType.boolean, 'is-egress'), ['bool'])),
                                                ('crypto_algo', (YLeaf(YType.uint8, 'crypto-algo'), ['int'])),
                                                ('key_len', (YLeaf(YType.uint8, 'key-len'), ['int'])),
                                                ('an', (YLeaf(YType.uint8, 'an'), ['int'])),
                                                ('xpn', (YLeaf(YType.uint8, 'xpn'), ['int'])),
                                                ('sci', (YLeaf(YType.uint64, 'sci'), ['int'])),
                                                ('in_use', (YLeaf(YType.boolean, 'in-use'), ['bool'])),
                                                ('next_pn', (YLeaf(YType.uint64, 'next-pn'), ['int'])),
                                                ('c_offset', (YLeaf(YType.uint8, 'c-offset'), ['int'])),
                                                ('action', (YLeaf(YType.uint8, 'action'), ['int'])),
                                                ('q_bit', (YLeaf(YType.boolean, 'q-bit'), ['bool'])),
                                                ('qq_bit', (YLeaf(YType.boolean, 'qq-bit'), ['bool'])),
                                            ])
                                            self.sa_id = None
                                            self.valid = None
                                            self.is_egress = None
                                            self.crypto_algo = None
                                            self.key_len = None
                                            self.an = None
                                            self.xpn = None
                                            self.sci = None
                                            self.in_use = None
                                            self.next_pn = None
                                            self.c_offset = None
                                            self.action = None
                                            self.q_bit = None
                                            self.qq_bit = None
                                            self._segment_path = lambda: "rx-sa"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.MsfpgaSa.RxSa, ['sa_id', 'valid', 'is_egress', 'crypto_algo', 'key_len', 'an', 'xpn', 'sci', 'in_use', 'next_pn', 'c_offset', 'action', 'q_bit', 'qq_bit'], name, value)


                                class XlfpgaSa(Entity):
                                    """
                                    XLFPGA SA Information
                                    
                                    .. attribute:: tx_sa
                                    
                                    	Tx SA Details
                                    	**type**\:  :py:class:`TxSa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.XlfpgaSa.TxSa>`
                                    
                                    .. attribute:: rx_sa
                                    
                                    	Rx SA Details
                                    	**type**\:  :py:class:`RxSa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.XlfpgaSa.RxSa>`
                                    
                                    

                                    """

                                    _prefix = 'crypto-macsec-pl-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.XlfpgaSa, self).__init__()

                                        self.yang_name = "xlfpga-sa"
                                        self.yang_parent_name = "ext"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("tx-sa", ("tx_sa", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.XlfpgaSa.TxSa)), ("rx-sa", ("rx_sa", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.XlfpgaSa.RxSa))])
                                        self._leafs = OrderedDict()

                                        self.tx_sa = MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.XlfpgaSa.TxSa()
                                        self.tx_sa.parent = self
                                        self._children_name_map["tx_sa"] = "tx-sa"

                                        self.rx_sa = MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.XlfpgaSa.RxSa()
                                        self.rx_sa.parent = self
                                        self._children_name_map["rx_sa"] = "rx-sa"
                                        self._segment_path = lambda: "xlfpga-sa"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.XlfpgaSa, [], name, value)


                                    class TxSa(Entity):
                                        """
                                        Tx SA Details
                                        
                                        .. attribute:: protection_enable
                                        
                                        	Protection Enabled
                                        	**type**\: bool
                                        
                                        .. attribute:: secure_mode
                                        
                                        	Secure Mode \- Must/Should
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: secure_channel_id
                                        
                                        	Secure Channel ID
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: sectag_length
                                        
                                        	Sec Tag Length(bytes) 
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: cipher_suite
                                        
                                        	Cipher Suite Used
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: confidentiality_offset
                                        
                                        	Confidentiality Offset
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: fcs_err_cfg
                                        
                                        	FCS Error Config
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: max_packet_num
                                        
                                        	Max Packet Number
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: an
                                        
                                        	Association Number
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: initial_packet_number
                                        
                                        	Initial Packet Number
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: ssci
                                        
                                        	Short Secure Channel ID
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: current_packet_num
                                        
                                        	Current Packet Number
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: crc_value
                                        
                                        	CRC Value
                                        	**type**\: int
                                        
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
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('protection_enable', (YLeaf(YType.boolean, 'protection-enable'), ['bool'])),
                                                ('secure_mode', (YLeaf(YType.uint8, 'secure-mode'), ['int'])),
                                                ('secure_channel_id', (YLeaf(YType.uint64, 'secure-channel-id'), ['int'])),
                                                ('sectag_length', (YLeaf(YType.uint32, 'sectag-length'), ['int'])),
                                                ('cipher_suite', (YLeaf(YType.uint32, 'cipher-suite'), ['int'])),
                                                ('confidentiality_offset', (YLeaf(YType.uint8, 'confidentiality-offset'), ['int'])),
                                                ('fcs_err_cfg', (YLeaf(YType.uint8, 'fcs-err-cfg'), ['int'])),
                                                ('max_packet_num', (YLeaf(YType.uint64, 'max-packet-num'), ['int'])),
                                                ('an', (YLeaf(YType.uint8, 'an'), ['int'])),
                                                ('initial_packet_number', (YLeaf(YType.uint64, 'initial-packet-number'), ['int'])),
                                                ('ssci', (YLeaf(YType.uint32, 'ssci'), ['int'])),
                                                ('current_packet_num', (YLeaf(YType.uint64, 'current-packet-num'), ['int'])),
                                                ('crc_value', (YLeaf(YType.uint32, 'crc-value'), ['int'])),
                                            ])
                                            self.protection_enable = None
                                            self.secure_mode = None
                                            self.secure_channel_id = None
                                            self.sectag_length = None
                                            self.cipher_suite = None
                                            self.confidentiality_offset = None
                                            self.fcs_err_cfg = None
                                            self.max_packet_num = None
                                            self.an = None
                                            self.initial_packet_number = None
                                            self.ssci = None
                                            self.current_packet_num = None
                                            self.crc_value = None
                                            self._segment_path = lambda: "tx-sa"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.XlfpgaSa.TxSa, ['protection_enable', 'secure_mode', 'secure_channel_id', 'sectag_length', 'cipher_suite', 'confidentiality_offset', 'fcs_err_cfg', 'max_packet_num', 'an', 'initial_packet_number', 'ssci', 'current_packet_num', 'crc_value'], name, value)


                                    class RxSa(Entity):
                                        """
                                        Rx SA Details
                                        
                                        .. attribute:: protection_enable
                                        
                                        	Protection Enabled
                                        	**type**\: bool
                                        
                                        .. attribute:: secure_mode
                                        
                                        	Secure Mode \- Must/Should
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: replay_protect_mode
                                        
                                        	Replay Protect Mode
                                        	**type**\: bool
                                        
                                        .. attribute:: validation_mode
                                        
                                        	Validation Mode
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: replay_window
                                        
                                        	Replay Window 
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: secure_channel_id
                                        
                                        	Secure Channel ID
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: cipher_suite
                                        
                                        	Cipher Suite Used
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: confidentiality_offset
                                        
                                        	Confidentiality Offset
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: fcs_err_cfg
                                        
                                        	FCS Error Config
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: auth_err_cfg
                                        
                                        	Auth  Error Config
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: max_packet_num
                                        
                                        	Max Packet Number
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: num_an_in_use
                                        
                                        	Num of AN's in Use
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: an
                                        
                                        	Association Number
                                        	**type**\: str
                                        
                                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                        
                                        .. attribute:: recent_an
                                        
                                        	Recent Association Num
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: pkt_untagged_detected
                                        
                                        	Untagged Pkts Detected
                                        	**type**\: bool
                                        
                                        .. attribute:: pkt_tagged_detected
                                        
                                        	Tagged Pkts Detected
                                        	**type**\: bool
                                        
                                        .. attribute:: pkt_tagged_validated
                                        
                                        	Tagged Pkts Validated
                                        	**type**\: bool
                                        
                                        .. attribute:: current_packet_num
                                        
                                        	Current Packet Number
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: ssci
                                        
                                        	Short Secure Channel ID
                                        	**type**\: list of int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: lowest_acceptable_packet_num
                                        
                                        	Lowest Acceptable Packet Number
                                        	**type**\: list of int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: next_expected_packet_num
                                        
                                        	Next expected Packet Number
                                        	**type**\: list of int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: crc_value
                                        
                                        	CRC Value
                                        	**type**\: list of int
                                        
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
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('protection_enable', (YLeaf(YType.boolean, 'protection-enable'), ['bool'])),
                                                ('secure_mode', (YLeaf(YType.uint32, 'secure-mode'), ['int'])),
                                                ('replay_protect_mode', (YLeaf(YType.boolean, 'replay-protect-mode'), ['bool'])),
                                                ('validation_mode', (YLeaf(YType.uint32, 'validation-mode'), ['int'])),
                                                ('replay_window', (YLeaf(YType.uint32, 'replay-window'), ['int'])),
                                                ('secure_channel_id', (YLeaf(YType.uint64, 'secure-channel-id'), ['int'])),
                                                ('cipher_suite', (YLeaf(YType.uint32, 'cipher-suite'), ['int'])),
                                                ('confidentiality_offset', (YLeaf(YType.uint8, 'confidentiality-offset'), ['int'])),
                                                ('fcs_err_cfg', (YLeaf(YType.uint32, 'fcs-err-cfg'), ['int'])),
                                                ('auth_err_cfg', (YLeaf(YType.uint32, 'auth-err-cfg'), ['int'])),
                                                ('max_packet_num', (YLeaf(YType.uint64, 'max-packet-num'), ['int'])),
                                                ('num_an_in_use', (YLeaf(YType.uint32, 'num-an-in-use'), ['int'])),
                                                ('an', (YLeaf(YType.str, 'an'), ['str'])),
                                                ('recent_an', (YLeaf(YType.uint8, 'recent-an'), ['int'])),
                                                ('pkt_untagged_detected', (YLeaf(YType.boolean, 'pkt-untagged-detected'), ['bool'])),
                                                ('pkt_tagged_detected', (YLeaf(YType.boolean, 'pkt-tagged-detected'), ['bool'])),
                                                ('pkt_tagged_validated', (YLeaf(YType.boolean, 'pkt-tagged-validated'), ['bool'])),
                                                ('current_packet_num', (YLeaf(YType.uint64, 'current-packet-num'), ['int'])),
                                                ('ssci', (YLeafList(YType.uint32, 'ssci'), ['int'])),
                                                ('lowest_acceptable_packet_num', (YLeafList(YType.uint64, 'lowest-acceptable-packet-num'), ['int'])),
                                                ('next_expected_packet_num', (YLeafList(YType.uint64, 'next-expected-packet-num'), ['int'])),
                                                ('crc_value', (YLeafList(YType.uint32, 'crc-value'), ['int'])),
                                            ])
                                            self.protection_enable = None
                                            self.secure_mode = None
                                            self.replay_protect_mode = None
                                            self.validation_mode = None
                                            self.replay_window = None
                                            self.secure_channel_id = None
                                            self.cipher_suite = None
                                            self.confidentiality_offset = None
                                            self.fcs_err_cfg = None
                                            self.auth_err_cfg = None
                                            self.max_packet_num = None
                                            self.num_an_in_use = None
                                            self.an = None
                                            self.recent_an = None
                                            self.pkt_untagged_detected = None
                                            self.pkt_tagged_detected = None
                                            self.pkt_tagged_validated = None
                                            self.current_packet_num = None
                                            self.ssci = []
                                            self.lowest_acceptable_packet_num = []
                                            self.next_expected_packet_num = []
                                            self.crc_value = []
                                            self._segment_path = lambda: "rx-sa"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.XlfpgaSa.RxSa, ['protection_enable', 'secure_mode', 'replay_protect_mode', 'validation_mode', 'replay_window', 'secure_channel_id', 'cipher_suite', 'confidentiality_offset', 'fcs_err_cfg', 'auth_err_cfg', 'max_packet_num', 'num_an_in_use', 'an', 'recent_an', 'pkt_untagged_detected', 'pkt_tagged_detected', 'pkt_tagged_validated', 'current_packet_num', 'ssci', 'lowest_acceptable_packet_num', 'next_expected_packet_num', 'crc_value'], name, value)


                                class Es200Sa(Entity):
                                    """
                                    ES200 SA Information
                                    
                                    .. attribute:: tx_sa
                                    
                                    	Tx SA Details
                                    	**type**\:  :py:class:`TxSa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.Es200Sa.TxSa>`
                                    
                                    .. attribute:: rx_sa
                                    
                                    	Rx SA Details
                                    	**type**\: list of  		 :py:class:`RxSa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.Es200Sa.RxSa>`
                                    
                                    

                                    """

                                    _prefix = 'crypto-macsec-pl-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.Es200Sa, self).__init__()

                                        self.yang_name = "es200-sa"
                                        self.yang_parent_name = "ext"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("tx-sa", ("tx_sa", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.Es200Sa.TxSa)), ("rx-sa", ("rx_sa", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.Es200Sa.RxSa))])
                                        self._leafs = OrderedDict()

                                        self.tx_sa = MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.Es200Sa.TxSa()
                                        self.tx_sa.parent = self
                                        self._children_name_map["tx_sa"] = "tx-sa"

                                        self.rx_sa = YList(self)
                                        self._segment_path = lambda: "es200-sa"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.Es200Sa, [], name, value)


                                    class TxSa(Entity):
                                        """
                                        Tx SA Details
                                        
                                        .. attribute:: xform_params
                                        
                                        	 Xform Params
                                        	**type**\:  :py:class:`XformParams <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.Es200Sa.TxSa.XformParams>`
                                        
                                        .. attribute:: is_valid
                                        
                                        	Is structure valid
                                        	**type**\: bool
                                        
                                        .. attribute:: sa_id
                                        
                                        	SA Index
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: sc_no
                                        
                                        	SC Number
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: out_pkts_too_long
                                        
                                        	packets exceeding egress MTU
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: out_pkts_encrypted_protected
                                        
                                        	packets encrypted/protected
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: out_octets_encrypted_protected1
                                        
                                        	octets1 encrypted/protected
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: initial_pkt_number
                                        
                                        	Initial Packet Number
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: current_pkt_number
                                        
                                        	Current packet Number
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: max_pkt_number
                                        
                                        	Maximum packet Number
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        

                                        """

                                        _prefix = 'crypto-macsec-pl-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.Es200Sa.TxSa, self).__init__()

                                            self.yang_name = "tx-sa"
                                            self.yang_parent_name = "es200-sa"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("xform-params", ("xform_params", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.Es200Sa.TxSa.XformParams))])
                                            self._leafs = OrderedDict([
                                                ('is_valid', (YLeaf(YType.boolean, 'is-valid'), ['bool'])),
                                                ('sa_id', (YLeaf(YType.uint8, 'sa-id'), ['int'])),
                                                ('sc_no', (YLeaf(YType.uint32, 'sc-no'), ['int'])),
                                                ('out_pkts_too_long', (YLeaf(YType.uint8, 'out-pkts-too-long'), ['int'])),
                                                ('out_pkts_encrypted_protected', (YLeaf(YType.uint8, 'out-pkts-encrypted-protected'), ['int'])),
                                                ('out_octets_encrypted_protected1', (YLeaf(YType.uint8, 'out-octets-encrypted-protected1'), ['int'])),
                                                ('initial_pkt_number', (YLeaf(YType.uint8, 'initial-pkt-number'), ['int'])),
                                                ('current_pkt_number', (YLeaf(YType.uint64, 'current-pkt-number'), ['int'])),
                                                ('max_pkt_number', (YLeaf(YType.uint64, 'max-pkt-number'), ['int'])),
                                            ])
                                            self.is_valid = None
                                            self.sa_id = None
                                            self.sc_no = None
                                            self.out_pkts_too_long = None
                                            self.out_pkts_encrypted_protected = None
                                            self.out_octets_encrypted_protected1 = None
                                            self.initial_pkt_number = None
                                            self.current_pkt_number = None
                                            self.max_pkt_number = None

                                            self.xform_params = MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.Es200Sa.TxSa.XformParams()
                                            self.xform_params.parent = self
                                            self._children_name_map["xform_params"] = "xform-params"
                                            self._segment_path = lambda: "tx-sa"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.Es200Sa.TxSa, ['is_valid', 'sa_id', 'sc_no', 'out_pkts_too_long', 'out_pkts_encrypted_protected', 'out_octets_encrypted_protected1', 'initial_pkt_number', 'current_pkt_number', 'max_pkt_number'], name, value)


                                        class XformParams(Entity):
                                            """
                                             Xform Params
                                            
                                            .. attribute:: replay_win_size
                                            
                                            	range of pkt nos considered valid
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: crypt_algo
                                            
                                            	Cryptographic algo used
                                            	**type**\: str
                                            
                                            .. attribute:: is_egress_tr
                                            
                                            	APM\_TRUE if this is Egress Transform record, APM\_FALSE otherwise
                                            	**type**\: bool
                                            
                                            .. attribute:: aes_key_len
                                            
                                            	AES Key length
                                            	**type**\: str
                                            
                                            .. attribute:: assoc_num
                                            
                                            	Association Number for egress
                                            	**type**\: int
                                            
                                            	**range:** 0..255
                                            
                                            .. attribute:: is_seq_num64_bit
                                            
                                            	TRUE if Seq Num is 64\-bit, FALSE if it is 32\-bit
                                            	**type**\: bool
                                            
                                            .. attribute:: bgen_auth_key
                                            
                                            	TRUE to generate the authKey, so authKey in this struct not used                                  APM\_FALSE to use provided authKey
                                            	**type**\: bool
                                            
                                            

                                            """

                                            _prefix = 'crypto-macsec-pl-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.Es200Sa.TxSa.XformParams, self).__init__()

                                                self.yang_name = "xform-params"
                                                self.yang_parent_name = "tx-sa"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('replay_win_size', (YLeaf(YType.uint32, 'replay-win-size'), ['int'])),
                                                    ('crypt_algo', (YLeaf(YType.str, 'crypt-algo'), ['str'])),
                                                    ('is_egress_tr', (YLeaf(YType.boolean, 'is-egress-tr'), ['bool'])),
                                                    ('aes_key_len', (YLeaf(YType.str, 'aes-key-len'), ['str'])),
                                                    ('assoc_num', (YLeaf(YType.uint8, 'assoc-num'), ['int'])),
                                                    ('is_seq_num64_bit', (YLeaf(YType.boolean, 'is-seq-num64-bit'), ['bool'])),
                                                    ('bgen_auth_key', (YLeaf(YType.boolean, 'bgen-auth-key'), ['bool'])),
                                                ])
                                                self.replay_win_size = None
                                                self.crypt_algo = None
                                                self.is_egress_tr = None
                                                self.aes_key_len = None
                                                self.assoc_num = None
                                                self.is_seq_num64_bit = None
                                                self.bgen_auth_key = None
                                                self._segment_path = lambda: "xform-params"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.Es200Sa.TxSa.XformParams, ['replay_win_size', 'crypt_algo', 'is_egress_tr', 'aes_key_len', 'assoc_num', 'is_seq_num64_bit', 'bgen_auth_key'], name, value)


                                    class RxSa(Entity):
                                        """
                                        Rx SA Details
                                        
                                        .. attribute:: xform_params
                                        
                                        	 Xform Params
                                        	**type**\:  :py:class:`XformParams <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.Es200Sa.RxSa.XformParams>`
                                        
                                        .. attribute:: is_valid
                                        
                                        	Is structure valid
                                        	**type**\: bool
                                        
                                        .. attribute:: sa_id
                                        
                                        	SA Index
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: sc_no
                                        
                                        	SC Number
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: in_pkts_unchecked
                                        
                                        	frame not valid & validateFrames disabled
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: in_pkts_delayed
                                        
                                        	PN of packet outside replay window & validateFrames !strict
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: in_pkts_late
                                        
                                        	PN of packet outside replay window & validateFrames strict
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: in_pkts_ok
                                        
                                        	packets with no error
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: in_pkts_invalid
                                        
                                        	packet not valid & validateFrames !strict
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: in_pkts_not_valid
                                        
                                        	packet not valid & validateFrames strict
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: in_pkts_not_using_sa
                                        
                                        	packet assigned to SA not in use & validateFrames strict
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: in_pkts_unused_sa
                                        
                                        	packet assigned to SA not in use& validateFrames !strict
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: in_octets_decrypted_validated1
                                        
                                        	octets1 decrypted/validated
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: in_octets_validated
                                        
                                        	octets validated
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'crypto-macsec-pl-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.Es200Sa.RxSa, self).__init__()

                                            self.yang_name = "rx-sa"
                                            self.yang_parent_name = "es200-sa"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("xform-params", ("xform_params", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.Es200Sa.RxSa.XformParams))])
                                            self._leafs = OrderedDict([
                                                ('is_valid', (YLeaf(YType.boolean, 'is-valid'), ['bool'])),
                                                ('sa_id', (YLeaf(YType.uint8, 'sa-id'), ['int'])),
                                                ('sc_no', (YLeaf(YType.uint32, 'sc-no'), ['int'])),
                                                ('in_pkts_unchecked', (YLeaf(YType.uint8, 'in-pkts-unchecked'), ['int'])),
                                                ('in_pkts_delayed', (YLeaf(YType.uint8, 'in-pkts-delayed'), ['int'])),
                                                ('in_pkts_late', (YLeaf(YType.uint8, 'in-pkts-late'), ['int'])),
                                                ('in_pkts_ok', (YLeaf(YType.uint8, 'in-pkts-ok'), ['int'])),
                                                ('in_pkts_invalid', (YLeaf(YType.uint8, 'in-pkts-invalid'), ['int'])),
                                                ('in_pkts_not_valid', (YLeaf(YType.uint8, 'in-pkts-not-valid'), ['int'])),
                                                ('in_pkts_not_using_sa', (YLeaf(YType.uint8, 'in-pkts-not-using-sa'), ['int'])),
                                                ('in_pkts_unused_sa', (YLeaf(YType.uint8, 'in-pkts-unused-sa'), ['int'])),
                                                ('in_octets_decrypted_validated1', (YLeaf(YType.uint8, 'in-octets-decrypted-validated1'), ['int'])),
                                                ('in_octets_validated', (YLeaf(YType.uint8, 'in-octets-validated'), ['int'])),
                                            ])
                                            self.is_valid = None
                                            self.sa_id = None
                                            self.sc_no = None
                                            self.in_pkts_unchecked = None
                                            self.in_pkts_delayed = None
                                            self.in_pkts_late = None
                                            self.in_pkts_ok = None
                                            self.in_pkts_invalid = None
                                            self.in_pkts_not_valid = None
                                            self.in_pkts_not_using_sa = None
                                            self.in_pkts_unused_sa = None
                                            self.in_octets_decrypted_validated1 = None
                                            self.in_octets_validated = None

                                            self.xform_params = MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.Es200Sa.RxSa.XformParams()
                                            self.xform_params.parent = self
                                            self._children_name_map["xform_params"] = "xform-params"
                                            self._segment_path = lambda: "rx-sa"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.Es200Sa.RxSa, ['is_valid', 'sa_id', 'sc_no', 'in_pkts_unchecked', 'in_pkts_delayed', 'in_pkts_late', 'in_pkts_ok', 'in_pkts_invalid', 'in_pkts_not_valid', 'in_pkts_not_using_sa', 'in_pkts_unused_sa', 'in_octets_decrypted_validated1', 'in_octets_validated'], name, value)


                                        class XformParams(Entity):
                                            """
                                             Xform Params
                                            
                                            .. attribute:: replay_win_size
                                            
                                            	range of pkt nos considered valid
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: crypt_algo
                                            
                                            	Cryptographic algo used
                                            	**type**\: str
                                            
                                            .. attribute:: is_egress_tr
                                            
                                            	APM\_TRUE if this is Egress Transform record, APM\_FALSE otherwise
                                            	**type**\: bool
                                            
                                            .. attribute:: aes_key_len
                                            
                                            	AES Key length
                                            	**type**\: str
                                            
                                            .. attribute:: assoc_num
                                            
                                            	Association Number for egress
                                            	**type**\: int
                                            
                                            	**range:** 0..255
                                            
                                            .. attribute:: is_seq_num64_bit
                                            
                                            	TRUE if Seq Num is 64\-bit, FALSE if it is 32\-bit
                                            	**type**\: bool
                                            
                                            .. attribute:: bgen_auth_key
                                            
                                            	TRUE to generate the authKey, so authKey in this struct not used                                  APM\_FALSE to use provided authKey
                                            	**type**\: bool
                                            
                                            

                                            """

                                            _prefix = 'crypto-macsec-pl-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.Es200Sa.RxSa.XformParams, self).__init__()

                                                self.yang_name = "xform-params"
                                                self.yang_parent_name = "rx-sa"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('replay_win_size', (YLeaf(YType.uint32, 'replay-win-size'), ['int'])),
                                                    ('crypt_algo', (YLeaf(YType.str, 'crypt-algo'), ['str'])),
                                                    ('is_egress_tr', (YLeaf(YType.boolean, 'is-egress-tr'), ['bool'])),
                                                    ('aes_key_len', (YLeaf(YType.str, 'aes-key-len'), ['str'])),
                                                    ('assoc_num', (YLeaf(YType.uint8, 'assoc-num'), ['int'])),
                                                    ('is_seq_num64_bit', (YLeaf(YType.boolean, 'is-seq-num64-bit'), ['bool'])),
                                                    ('bgen_auth_key', (YLeaf(YType.boolean, 'bgen-auth-key'), ['bool'])),
                                                ])
                                                self.replay_win_size = None
                                                self.crypt_algo = None
                                                self.is_egress_tr = None
                                                self.aes_key_len = None
                                                self.assoc_num = None
                                                self.is_seq_num64_bit = None
                                                self.bgen_auth_key = None
                                                self._segment_path = lambda: "xform-params"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Ext.Es200Sa.RxSa.XformParams, ['replay_win_size', 'crypt_algo', 'is_egress_tr', 'aes_key_len', 'assoc_num', 'is_seq_num64_bit', 'bgen_auth_key'], name, value)


                    class HwFlowS(Entity):
                        """
                        Table of Hardware Flows
                        
                        .. attribute:: hw_flow
                        
                        	Hardware Flow
                        	**type**\: list of  		 :py:class:`HwFlow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow>`
                        
                        

                        """

                        _prefix = 'crypto-macsec-pl-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS, self).__init__()

                            self.yang_name = "hw-flow-s"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("hw-flow", ("hw_flow", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow))])
                            self._leafs = OrderedDict()

                            self.hw_flow = YList(self)
                            self._segment_path = lambda: "hw-flow-s"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS, [], name, value)


                        class HwFlow(Entity):
                            """
                            Hardware Flow
                            
                            .. attribute:: flow_id  (key)
                            
                            	FLOW ID
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: ext
                            
                            	ext
                            	**type**\:  :py:class:`Ext <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Ext>`
                            
                            

                            """

                            _prefix = 'crypto-macsec-pl-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow, self).__init__()

                                self.yang_name = "hw-flow"
                                self.yang_parent_name = "hw-flow-s"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['flow_id']
                                self._child_classes = OrderedDict([("ext", ("ext", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Ext))])
                                self._leafs = OrderedDict([
                                    ('flow_id', (YLeaf(YType.uint32, 'flow-id'), ['int'])),
                                ])
                                self.flow_id = None

                                self.ext = MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Ext()
                                self.ext.parent = self
                                self._children_name_map["ext"] = "ext"
                                self._segment_path = lambda: "hw-flow" + "[flow-id='" + str(self.flow_id) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow, ['flow_id'], name, value)


                            class Ext(Entity):
                                """
                                ext
                                
                                .. attribute:: msfpga_flow
                                
                                	MSFPGA Flow Information
                                	**type**\:  :py:class:`MsfpgaFlow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Ext.MsfpgaFlow>`
                                
                                .. attribute:: es200_flow
                                
                                	ES200 Flow Information
                                	**type**\:  :py:class:`Es200Flow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Ext.Es200Flow>`
                                
                                .. attribute:: type
                                
                                	type
                                	**type**\:  :py:class:`MacsecPhyVendor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPhyVendor>`
                                
                                

                                """

                                _prefix = 'crypto-macsec-pl-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Ext, self).__init__()

                                    self.yang_name = "ext"
                                    self.yang_parent_name = "hw-flow"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("msfpga-flow", ("msfpga_flow", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Ext.MsfpgaFlow)), ("es200-flow", ("es200_flow", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Ext.Es200Flow))])
                                    self._leafs = OrderedDict([
                                        ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'MacsecPhyVendor', '')])),
                                    ])
                                    self.type = None

                                    self.msfpga_flow = MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Ext.MsfpgaFlow()
                                    self.msfpga_flow.parent = self
                                    self._children_name_map["msfpga_flow"] = "msfpga-flow"

                                    self.es200_flow = MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Ext.Es200Flow()
                                    self.es200_flow.parent = self
                                    self._children_name_map["es200_flow"] = "es200-flow"
                                    self._segment_path = lambda: "ext"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Ext, ['type'], name, value)


                                class MsfpgaFlow(Entity):
                                    """
                                    MSFPGA Flow Information
                                    
                                    .. attribute:: tx_flow
                                    
                                    	Tx Flow Details
                                    	**type**\:  :py:class:`TxFlow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Ext.MsfpgaFlow.TxFlow>`
                                    
                                    .. attribute:: rx_flow
                                    
                                    	Rx Flow Details
                                    	**type**\:  :py:class:`RxFlow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Ext.MsfpgaFlow.RxFlow>`
                                    
                                    

                                    """

                                    _prefix = 'crypto-macsec-pl-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Ext.MsfpgaFlow, self).__init__()

                                        self.yang_name = "msfpga-flow"
                                        self.yang_parent_name = "ext"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("tx-flow", ("tx_flow", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Ext.MsfpgaFlow.TxFlow)), ("rx-flow", ("rx_flow", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Ext.MsfpgaFlow.RxFlow))])
                                        self._leafs = OrderedDict()

                                        self.tx_flow = MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Ext.MsfpgaFlow.TxFlow()
                                        self.tx_flow.parent = self
                                        self._children_name_map["tx_flow"] = "tx-flow"

                                        self.rx_flow = MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Ext.MsfpgaFlow.RxFlow()
                                        self.rx_flow.parent = self
                                        self._children_name_map["rx_flow"] = "rx-flow"
                                        self._segment_path = lambda: "msfpga-flow"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Ext.MsfpgaFlow, [], name, value)


                                    class TxFlow(Entity):
                                        """
                                        Tx Flow Details
                                        
                                        .. attribute:: flow_id
                                        
                                        	Flow Index
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: valid
                                        
                                        	Flow Validity
                                        	**type**\: bool
                                        
                                        .. attribute:: is_egress
                                        
                                        	rx\_tx direction
                                        	**type**\: bool
                                        
                                        .. attribute:: in_use
                                        
                                        	In Use
                                        	**type**\: bool
                                        
                                        .. attribute:: action
                                        
                                        	Action
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: smac_inuse
                                        
                                        	If MAC SA in Use
                                        	**type**\: bool
                                        
                                        .. attribute:: dmac_inuse
                                        
                                        	If MAC DA in Use
                                        	**type**\: bool
                                        
                                        .. attribute:: ethertype
                                        
                                        	Ether Type
                                        	**type**\: int
                                        
                                        	**range:** 0..65535
                                        
                                        .. attribute:: outer_vlan
                                        
                                        	Outer VLAN ID
                                        	**type**\: int
                                        
                                        	**range:** 0..65535
                                        
                                        .. attribute:: outer_vlan_up
                                        
                                        	Outer Vlan UserPri
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: outer_vlan_tpid
                                        
                                        	Outer Vlan TPID
                                        	**type**\: int
                                        
                                        	**range:** 0..65535
                                        
                                        .. attribute:: inner_vlan
                                        
                                        	Inner VLAN ID
                                        	**type**\: int
                                        
                                        	**range:** 0..65535
                                        
                                        .. attribute:: inner_vlan_up
                                        
                                        	Inner Vlan UserPri
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: inner_vlan_tpid
                                        
                                        	Inner Vlan TPID
                                        	**type**\: int
                                        
                                        	**range:** 0..65535
                                        
                                        .. attribute:: source_port
                                        
                                        	Source Port
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: source_port_chk
                                        
                                        	Source Port ChkEn
                                        	**type**\: bool
                                        
                                        .. attribute:: sci_inuse
                                        
                                        	If SCI in use
                                        	**type**\: bool
                                        
                                        .. attribute:: sci
                                        
                                        	SCI
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: match_pri
                                        
                                        	Match Priority
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: is_ctrl_pkt
                                        
                                        	Is Control Pkt
                                        	**type**\: bool
                                        
                                        .. attribute:: ctrl_check
                                        
                                        	Ctrl Pkt ChkEn
                                        	**type**\: bool
                                        
                                        .. attribute:: match_untagged
                                        
                                        	MatchUntagged
                                        	**type**\: bool
                                        
                                        .. attribute:: match_tagged
                                        
                                        	MatchTagged
                                        	**type**\: bool
                                        
                                        .. attribute:: match_bad_tag
                                        
                                        	Match Bad Tag
                                        	**type**\: bool
                                        
                                        .. attribute:: match_kay_tag
                                        
                                        	MatchKaYTag
                                        	**type**\: bool
                                        
                                        .. attribute:: tci_v
                                        
                                        	TCI V
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: tci_e_xr
                                        
                                        	TCI ES
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: tci_sc
                                        
                                        	TCI SC
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: tci_scb
                                        
                                        	TCI SCB
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: tci
                                        
                                        	TCI E
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: tci_c
                                        
                                        	TCI C
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: tci_an
                                        
                                        	TCI AN
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: tci_an_chk
                                        
                                        	TciAnChkEn
                                        	**type**\: bool
                                        
                                        .. attribute:: tci_chk
                                        
                                        	TciChkEn
                                        	**type**\: bool
                                        
                                        .. attribute:: sai
                                        
                                        	SAI
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: macsa
                                        
                                        	MAC SA
                                        	**type**\: list of int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: macda
                                        
                                        	MAC DA
                                        	**type**\: list of int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'crypto-macsec-pl-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Ext.MsfpgaFlow.TxFlow, self).__init__()

                                            self.yang_name = "tx-flow"
                                            self.yang_parent_name = "msfpga-flow"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('flow_id', (YLeaf(YType.uint8, 'flow-id'), ['int'])),
                                                ('valid', (YLeaf(YType.boolean, 'valid'), ['bool'])),
                                                ('is_egress', (YLeaf(YType.boolean, 'is-egress'), ['bool'])),
                                                ('in_use', (YLeaf(YType.boolean, 'in-use'), ['bool'])),
                                                ('action', (YLeaf(YType.uint8, 'action'), ['int'])),
                                                ('smac_inuse', (YLeaf(YType.boolean, 'smac-inuse'), ['bool'])),
                                                ('dmac_inuse', (YLeaf(YType.boolean, 'dmac-inuse'), ['bool'])),
                                                ('ethertype', (YLeaf(YType.uint16, 'ethertype'), ['int'])),
                                                ('outer_vlan', (YLeaf(YType.uint16, 'outer-vlan'), ['int'])),
                                                ('outer_vlan_up', (YLeaf(YType.uint8, 'outer-vlan-up'), ['int'])),
                                                ('outer_vlan_tpid', (YLeaf(YType.uint16, 'outer-vlan-tpid'), ['int'])),
                                                ('inner_vlan', (YLeaf(YType.uint16, 'inner-vlan'), ['int'])),
                                                ('inner_vlan_up', (YLeaf(YType.uint8, 'inner-vlan-up'), ['int'])),
                                                ('inner_vlan_tpid', (YLeaf(YType.uint16, 'inner-vlan-tpid'), ['int'])),
                                                ('source_port', (YLeaf(YType.uint32, 'source-port'), ['int'])),
                                                ('source_port_chk', (YLeaf(YType.boolean, 'source-port-chk'), ['bool'])),
                                                ('sci_inuse', (YLeaf(YType.boolean, 'sci-inuse'), ['bool'])),
                                                ('sci', (YLeaf(YType.uint64, 'sci'), ['int'])),
                                                ('match_pri', (YLeaf(YType.uint8, 'match-pri'), ['int'])),
                                                ('is_ctrl_pkt', (YLeaf(YType.boolean, 'is-ctrl-pkt'), ['bool'])),
                                                ('ctrl_check', (YLeaf(YType.boolean, 'ctrl-check'), ['bool'])),
                                                ('match_untagged', (YLeaf(YType.boolean, 'match-untagged'), ['bool'])),
                                                ('match_tagged', (YLeaf(YType.boolean, 'match-tagged'), ['bool'])),
                                                ('match_bad_tag', (YLeaf(YType.boolean, 'match-bad-tag'), ['bool'])),
                                                ('match_kay_tag', (YLeaf(YType.boolean, 'match-kay-tag'), ['bool'])),
                                                ('tci_v', (YLeaf(YType.uint8, 'tci-v'), ['int'])),
                                                ('tci_e_xr', (YLeaf(YType.uint8, 'tci-e-xr'), ['int'])),
                                                ('tci_sc', (YLeaf(YType.uint8, 'tci-sc'), ['int'])),
                                                ('tci_scb', (YLeaf(YType.uint8, 'tci-scb'), ['int'])),
                                                ('tci', (YLeaf(YType.uint8, 'tci'), ['int'])),
                                                ('tci_c', (YLeaf(YType.uint8, 'tci-c'), ['int'])),
                                                ('tci_an', (YLeaf(YType.uint8, 'tci-an'), ['int'])),
                                                ('tci_an_chk', (YLeaf(YType.boolean, 'tci-an-chk'), ['bool'])),
                                                ('tci_chk', (YLeaf(YType.boolean, 'tci-chk'), ['bool'])),
                                                ('sai', (YLeaf(YType.uint32, 'sai'), ['int'])),
                                                ('macsa', (YLeafList(YType.uint8, 'macsa'), ['int'])),
                                                ('macda', (YLeafList(YType.uint8, 'macda'), ['int'])),
                                            ])
                                            self.flow_id = None
                                            self.valid = None
                                            self.is_egress = None
                                            self.in_use = None
                                            self.action = None
                                            self.smac_inuse = None
                                            self.dmac_inuse = None
                                            self.ethertype = None
                                            self.outer_vlan = None
                                            self.outer_vlan_up = None
                                            self.outer_vlan_tpid = None
                                            self.inner_vlan = None
                                            self.inner_vlan_up = None
                                            self.inner_vlan_tpid = None
                                            self.source_port = None
                                            self.source_port_chk = None
                                            self.sci_inuse = None
                                            self.sci = None
                                            self.match_pri = None
                                            self.is_ctrl_pkt = None
                                            self.ctrl_check = None
                                            self.match_untagged = None
                                            self.match_tagged = None
                                            self.match_bad_tag = None
                                            self.match_kay_tag = None
                                            self.tci_v = None
                                            self.tci_e_xr = None
                                            self.tci_sc = None
                                            self.tci_scb = None
                                            self.tci = None
                                            self.tci_c = None
                                            self.tci_an = None
                                            self.tci_an_chk = None
                                            self.tci_chk = None
                                            self.sai = None
                                            self.macsa = []
                                            self.macda = []
                                            self._segment_path = lambda: "tx-flow"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Ext.MsfpgaFlow.TxFlow, ['flow_id', 'valid', 'is_egress', 'in_use', 'action', 'smac_inuse', 'dmac_inuse', 'ethertype', 'outer_vlan', 'outer_vlan_up', 'outer_vlan_tpid', 'inner_vlan', 'inner_vlan_up', 'inner_vlan_tpid', 'source_port', 'source_port_chk', 'sci_inuse', 'sci', 'match_pri', 'is_ctrl_pkt', 'ctrl_check', 'match_untagged', 'match_tagged', 'match_bad_tag', 'match_kay_tag', 'tci_v', 'tci_e_xr', 'tci_sc', 'tci_scb', 'tci', 'tci_c', 'tci_an', 'tci_an_chk', 'tci_chk', 'sai', 'macsa', 'macda'], name, value)


                                    class RxFlow(Entity):
                                        """
                                        Rx Flow Details
                                        
                                        .. attribute:: flow_id
                                        
                                        	Flow Index
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: valid
                                        
                                        	Flow Validity
                                        	**type**\: bool
                                        
                                        .. attribute:: is_egress
                                        
                                        	rx\_tx direction
                                        	**type**\: bool
                                        
                                        .. attribute:: in_use
                                        
                                        	In Use
                                        	**type**\: bool
                                        
                                        .. attribute:: action
                                        
                                        	Action
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: smac_inuse
                                        
                                        	If MAC SA in Use
                                        	**type**\: bool
                                        
                                        .. attribute:: dmac_inuse
                                        
                                        	If MAC DA in Use
                                        	**type**\: bool
                                        
                                        .. attribute:: ethertype
                                        
                                        	Ether Type
                                        	**type**\: int
                                        
                                        	**range:** 0..65535
                                        
                                        .. attribute:: outer_vlan
                                        
                                        	Outer VLAN ID
                                        	**type**\: int
                                        
                                        	**range:** 0..65535
                                        
                                        .. attribute:: outer_vlan_up
                                        
                                        	Outer Vlan UserPri
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: outer_vlan_tpid
                                        
                                        	Outer Vlan TPID
                                        	**type**\: int
                                        
                                        	**range:** 0..65535
                                        
                                        .. attribute:: inner_vlan
                                        
                                        	Inner VLAN ID
                                        	**type**\: int
                                        
                                        	**range:** 0..65535
                                        
                                        .. attribute:: inner_vlan_up
                                        
                                        	Inner Vlan UserPri
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: inner_vlan_tpid
                                        
                                        	Inner Vlan TPID
                                        	**type**\: int
                                        
                                        	**range:** 0..65535
                                        
                                        .. attribute:: source_port
                                        
                                        	Source Port
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: source_port_chk
                                        
                                        	Source Port ChkEn
                                        	**type**\: bool
                                        
                                        .. attribute:: sci_inuse
                                        
                                        	If SCI in use
                                        	**type**\: bool
                                        
                                        .. attribute:: sci
                                        
                                        	SCI
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: match_pri
                                        
                                        	Match Priority
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: is_ctrl_pkt
                                        
                                        	Is Control Pkt
                                        	**type**\: bool
                                        
                                        .. attribute:: ctrl_check
                                        
                                        	Ctrl Pkt ChkEn
                                        	**type**\: bool
                                        
                                        .. attribute:: match_untagged
                                        
                                        	MatchUntagged
                                        	**type**\: bool
                                        
                                        .. attribute:: match_tagged
                                        
                                        	MatchTagged
                                        	**type**\: bool
                                        
                                        .. attribute:: match_bad_tag
                                        
                                        	Match Bad Tag
                                        	**type**\: bool
                                        
                                        .. attribute:: match_kay_tag
                                        
                                        	MatchKaYTag
                                        	**type**\: bool
                                        
                                        .. attribute:: tci_v
                                        
                                        	TCI V
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: tci_e_xr
                                        
                                        	TCI ES
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: tci_sc
                                        
                                        	TCI SC
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: tci_scb
                                        
                                        	TCI SCB
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: tci
                                        
                                        	TCI E
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: tci_c
                                        
                                        	TCI C
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: tci_an
                                        
                                        	TCI AN
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: tci_an_chk
                                        
                                        	TciAnChkEn
                                        	**type**\: bool
                                        
                                        .. attribute:: tci_chk
                                        
                                        	TciChkEn
                                        	**type**\: bool
                                        
                                        .. attribute:: sai
                                        
                                        	SAI
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: macsa
                                        
                                        	MAC SA
                                        	**type**\: list of int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: macda
                                        
                                        	MAC DA
                                        	**type**\: list of int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'crypto-macsec-pl-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Ext.MsfpgaFlow.RxFlow, self).__init__()

                                            self.yang_name = "rx-flow"
                                            self.yang_parent_name = "msfpga-flow"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('flow_id', (YLeaf(YType.uint8, 'flow-id'), ['int'])),
                                                ('valid', (YLeaf(YType.boolean, 'valid'), ['bool'])),
                                                ('is_egress', (YLeaf(YType.boolean, 'is-egress'), ['bool'])),
                                                ('in_use', (YLeaf(YType.boolean, 'in-use'), ['bool'])),
                                                ('action', (YLeaf(YType.uint8, 'action'), ['int'])),
                                                ('smac_inuse', (YLeaf(YType.boolean, 'smac-inuse'), ['bool'])),
                                                ('dmac_inuse', (YLeaf(YType.boolean, 'dmac-inuse'), ['bool'])),
                                                ('ethertype', (YLeaf(YType.uint16, 'ethertype'), ['int'])),
                                                ('outer_vlan', (YLeaf(YType.uint16, 'outer-vlan'), ['int'])),
                                                ('outer_vlan_up', (YLeaf(YType.uint8, 'outer-vlan-up'), ['int'])),
                                                ('outer_vlan_tpid', (YLeaf(YType.uint16, 'outer-vlan-tpid'), ['int'])),
                                                ('inner_vlan', (YLeaf(YType.uint16, 'inner-vlan'), ['int'])),
                                                ('inner_vlan_up', (YLeaf(YType.uint8, 'inner-vlan-up'), ['int'])),
                                                ('inner_vlan_tpid', (YLeaf(YType.uint16, 'inner-vlan-tpid'), ['int'])),
                                                ('source_port', (YLeaf(YType.uint32, 'source-port'), ['int'])),
                                                ('source_port_chk', (YLeaf(YType.boolean, 'source-port-chk'), ['bool'])),
                                                ('sci_inuse', (YLeaf(YType.boolean, 'sci-inuse'), ['bool'])),
                                                ('sci', (YLeaf(YType.uint64, 'sci'), ['int'])),
                                                ('match_pri', (YLeaf(YType.uint8, 'match-pri'), ['int'])),
                                                ('is_ctrl_pkt', (YLeaf(YType.boolean, 'is-ctrl-pkt'), ['bool'])),
                                                ('ctrl_check', (YLeaf(YType.boolean, 'ctrl-check'), ['bool'])),
                                                ('match_untagged', (YLeaf(YType.boolean, 'match-untagged'), ['bool'])),
                                                ('match_tagged', (YLeaf(YType.boolean, 'match-tagged'), ['bool'])),
                                                ('match_bad_tag', (YLeaf(YType.boolean, 'match-bad-tag'), ['bool'])),
                                                ('match_kay_tag', (YLeaf(YType.boolean, 'match-kay-tag'), ['bool'])),
                                                ('tci_v', (YLeaf(YType.uint8, 'tci-v'), ['int'])),
                                                ('tci_e_xr', (YLeaf(YType.uint8, 'tci-e-xr'), ['int'])),
                                                ('tci_sc', (YLeaf(YType.uint8, 'tci-sc'), ['int'])),
                                                ('tci_scb', (YLeaf(YType.uint8, 'tci-scb'), ['int'])),
                                                ('tci', (YLeaf(YType.uint8, 'tci'), ['int'])),
                                                ('tci_c', (YLeaf(YType.uint8, 'tci-c'), ['int'])),
                                                ('tci_an', (YLeaf(YType.uint8, 'tci-an'), ['int'])),
                                                ('tci_an_chk', (YLeaf(YType.boolean, 'tci-an-chk'), ['bool'])),
                                                ('tci_chk', (YLeaf(YType.boolean, 'tci-chk'), ['bool'])),
                                                ('sai', (YLeaf(YType.uint32, 'sai'), ['int'])),
                                                ('macsa', (YLeafList(YType.uint8, 'macsa'), ['int'])),
                                                ('macda', (YLeafList(YType.uint8, 'macda'), ['int'])),
                                            ])
                                            self.flow_id = None
                                            self.valid = None
                                            self.is_egress = None
                                            self.in_use = None
                                            self.action = None
                                            self.smac_inuse = None
                                            self.dmac_inuse = None
                                            self.ethertype = None
                                            self.outer_vlan = None
                                            self.outer_vlan_up = None
                                            self.outer_vlan_tpid = None
                                            self.inner_vlan = None
                                            self.inner_vlan_up = None
                                            self.inner_vlan_tpid = None
                                            self.source_port = None
                                            self.source_port_chk = None
                                            self.sci_inuse = None
                                            self.sci = None
                                            self.match_pri = None
                                            self.is_ctrl_pkt = None
                                            self.ctrl_check = None
                                            self.match_untagged = None
                                            self.match_tagged = None
                                            self.match_bad_tag = None
                                            self.match_kay_tag = None
                                            self.tci_v = None
                                            self.tci_e_xr = None
                                            self.tci_sc = None
                                            self.tci_scb = None
                                            self.tci = None
                                            self.tci_c = None
                                            self.tci_an = None
                                            self.tci_an_chk = None
                                            self.tci_chk = None
                                            self.sai = None
                                            self.macsa = []
                                            self.macda = []
                                            self._segment_path = lambda: "rx-flow"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Ext.MsfpgaFlow.RxFlow, ['flow_id', 'valid', 'is_egress', 'in_use', 'action', 'smac_inuse', 'dmac_inuse', 'ethertype', 'outer_vlan', 'outer_vlan_up', 'outer_vlan_tpid', 'inner_vlan', 'inner_vlan_up', 'inner_vlan_tpid', 'source_port', 'source_port_chk', 'sci_inuse', 'sci', 'match_pri', 'is_ctrl_pkt', 'ctrl_check', 'match_untagged', 'match_tagged', 'match_bad_tag', 'match_kay_tag', 'tci_v', 'tci_e_xr', 'tci_sc', 'tci_scb', 'tci', 'tci_c', 'tci_an', 'tci_an_chk', 'tci_chk', 'sai', 'macsa', 'macda'], name, value)


                                class Es200Flow(Entity):
                                    """
                                    ES200 Flow Information
                                    
                                    .. attribute:: tx_flow
                                    
                                    	Tx Flow Details
                                    	**type**\:  :py:class:`TxFlow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Ext.Es200Flow.TxFlow>`
                                    
                                    .. attribute:: rx_flow
                                    
                                    	Rx Flow Details
                                    	**type**\:  :py:class:`RxFlow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Ext.Es200Flow.RxFlow>`
                                    
                                    

                                    """

                                    _prefix = 'crypto-macsec-pl-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Ext.Es200Flow, self).__init__()

                                        self.yang_name = "es200-flow"
                                        self.yang_parent_name = "ext"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("tx-flow", ("tx_flow", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Ext.Es200Flow.TxFlow)), ("rx-flow", ("rx_flow", MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Ext.Es200Flow.RxFlow))])
                                        self._leafs = OrderedDict()

                                        self.tx_flow = MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Ext.Es200Flow.TxFlow()
                                        self.tx_flow.parent = self
                                        self._children_name_map["tx_flow"] = "tx-flow"

                                        self.rx_flow = MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Ext.Es200Flow.RxFlow()
                                        self.rx_flow.parent = self
                                        self._children_name_map["rx_flow"] = "rx-flow"
                                        self._segment_path = lambda: "es200-flow"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Ext.Es200Flow, [], name, value)


                                    class TxFlow(Entity):
                                        """
                                        Tx Flow Details
                                        
                                        .. attribute:: flow_no
                                        
                                        	Flow Number
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: is_flow_enabled
                                        
                                        	Is Flow Enabled
                                        	**type**\: bool
                                        
                                        .. attribute:: ethertype
                                        
                                        	Parsed EtherType to match could be 0 if Ethertype should'nt                              be matched can be 0x88E5 for MACSec tag
                                        	**type**\: int
                                        
                                        	**range:** 0..65535
                                        
                                        .. attribute:: outer_vlan_id
                                        
                                        	 VLAN ID for outer tag use this when             only one tag should be matched
                                        	**type**\: int
                                        
                                        	**range:** 0..65535
                                        
                                        .. attribute:: outer_vlan_user_pri
                                        
                                        	VLAN User Priority for outer tag  use            this when only one tag should be matched
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: inner_vlan_id
                                        
                                        	VLAN ID for inner tag used when two              VLAN Tags should be matched
                                        	**type**\: int
                                        
                                        	**range:** 0..65535
                                        
                                        .. attribute:: inner_vlan_user_pri
                                        
                                        	 VLAN User priority for inner tag use            when matching two VLAN tags
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: psci
                                        
                                        	 SCI to be matched value required for            ingress only, pass NULL for egress
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: match_priority
                                        
                                        	priority for match 0\-15(highest) 
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: tci_v
                                        
                                        	value of 'v' in TCI to match (1bit) 
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: tci_e_xr
                                        
                                        	value of 'es' in TCI to match (1bit) 
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: tci_sc
                                        
                                        	value of 'sc' in TCI to match (1bit) 
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: tci_scb
                                        
                                        	value of 'scb' in TCI to match (1bit) 
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: tci
                                        
                                        	value of 'e' in TCI to match (1bit )
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: tci_c
                                        
                                        	value of 'c' in TCI to match (1bit) 
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: tci_chk
                                        
                                        	TCI bits will be checked only when this          bit is enabled. All the values of TCI bits       are mandatory when TCI check is used
                                        	**type**\: bool
                                        
                                        .. attribute:: pkt_type
                                        
                                        	Type of packet. See ethMscCfyEPktType\_e
                                        	**type**\: str
                                        
                                        .. attribute:: tag_num
                                        
                                        	No. of MPLS or VLAN tags See ethMscCfyETagNum\_e 
                                        	**type**\: str
                                        
                                        .. attribute:: inner_vlan_dei
                                        
                                        	Dei to match for innner Vlan tag
                                        	**type**\: bool
                                        
                                        .. attribute:: outer_vlan_dei
                                        
                                        	Dei to match for outer Vlan tag
                                        	**type**\: bool
                                        
                                        .. attribute:: pbb_sid
                                        
                                        	 Service Instance id 
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: pbb_bvid
                                        
                                        	 Backbone Vlan id 
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: pbb_pcp
                                        
                                        	 pcp 
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: pbb_dei
                                        
                                        	 dei 
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: mpls1_label
                                        
                                        	 label 
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: mpls1_exp
                                        
                                        	 exp 
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: mpls1_bos
                                        
                                        	 botton of stack 
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: mpls2_label
                                        
                                        	 label 
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: mpls2_exp
                                        
                                        	 exp 
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: mpls2_bos
                                        
                                        	 botton of stack 
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: plain_bits
                                        
                                        	Plain bits to compare. Max values\:               untagged pkt \- 40 bits after EthType             1 VLAN tag \- 24 bits after parsed EthType        2 VLAN tags\- 8 bits after parsed EthType         1 MPLS tag \- 32 bits after 1st tag               2 MPLS tags\- 8 bits following after 2nd          or atmost 5th MPLS tag                           PBB \- 16 bits after C\-SA                         PBB with VLAN tag \- 16 bits of VLAN tag 
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: bit
                                        
                                        .. attribute:: plain_bits_size
                                        
                                        	No. of bits used in plainBits
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: force_ctrl
                                        
                                        	Force the pkt as control pkt irrepective         of the results of control packet detector
                                        	**type**\: bool
                                        
                                        .. attribute:: drop
                                        
                                        	Drop the packet
                                        	**type**\: bool
                                        
                                        .. attribute:: mask_da
                                        
                                        	DA mask
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: mask_ethertype
                                        
                                        	Parsed EtherType mask
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: mask_plain_bits
                                        
                                        	Plain Bits mask
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: flow_hits
                                        
                                        	Pkts matching the Flow
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: macda
                                        
                                        	MAC DA
                                        	**type**\: list of int
                                        
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
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('flow_no', (YLeaf(YType.uint32, 'flow-no'), ['int'])),
                                                ('is_flow_enabled', (YLeaf(YType.boolean, 'is-flow-enabled'), ['bool'])),
                                                ('ethertype', (YLeaf(YType.uint16, 'ethertype'), ['int'])),
                                                ('outer_vlan_id', (YLeaf(YType.uint16, 'outer-vlan-id'), ['int'])),
                                                ('outer_vlan_user_pri', (YLeaf(YType.uint8, 'outer-vlan-user-pri'), ['int'])),
                                                ('inner_vlan_id', (YLeaf(YType.uint16, 'inner-vlan-id'), ['int'])),
                                                ('inner_vlan_user_pri', (YLeaf(YType.uint8, 'inner-vlan-user-pri'), ['int'])),
                                                ('psci', (YLeaf(YType.uint64, 'psci'), ['int'])),
                                                ('match_priority', (YLeaf(YType.uint8, 'match-priority'), ['int'])),
                                                ('tci_v', (YLeaf(YType.uint8, 'tci-v'), ['int'])),
                                                ('tci_e_xr', (YLeaf(YType.uint8, 'tci-e-xr'), ['int'])),
                                                ('tci_sc', (YLeaf(YType.uint8, 'tci-sc'), ['int'])),
                                                ('tci_scb', (YLeaf(YType.uint8, 'tci-scb'), ['int'])),
                                                ('tci', (YLeaf(YType.uint8, 'tci'), ['int'])),
                                                ('tci_c', (YLeaf(YType.uint8, 'tci-c'), ['int'])),
                                                ('tci_chk', (YLeaf(YType.boolean, 'tci-chk'), ['bool'])),
                                                ('pkt_type', (YLeaf(YType.str, 'pkt-type'), ['str'])),
                                                ('tag_num', (YLeaf(YType.str, 'tag-num'), ['str'])),
                                                ('inner_vlan_dei', (YLeaf(YType.boolean, 'inner-vlan-dei'), ['bool'])),
                                                ('outer_vlan_dei', (YLeaf(YType.boolean, 'outer-vlan-dei'), ['bool'])),
                                                ('pbb_sid', (YLeaf(YType.uint32, 'pbb-sid'), ['int'])),
                                                ('pbb_bvid', (YLeaf(YType.uint32, 'pbb-bvid'), ['int'])),
                                                ('pbb_pcp', (YLeaf(YType.uint8, 'pbb-pcp'), ['int'])),
                                                ('pbb_dei', (YLeaf(YType.uint8, 'pbb-dei'), ['int'])),
                                                ('mpls1_label', (YLeaf(YType.uint32, 'mpls1-label'), ['int'])),
                                                ('mpls1_exp', (YLeaf(YType.uint8, 'mpls1-exp'), ['int'])),
                                                ('mpls1_bos', (YLeaf(YType.uint8, 'mpls1-bos'), ['int'])),
                                                ('mpls2_label', (YLeaf(YType.uint32, 'mpls2-label'), ['int'])),
                                                ('mpls2_exp', (YLeaf(YType.uint8, 'mpls2-exp'), ['int'])),
                                                ('mpls2_bos', (YLeaf(YType.uint8, 'mpls2-bos'), ['int'])),
                                                ('plain_bits', (YLeaf(YType.uint64, 'plain-bits'), ['int'])),
                                                ('plain_bits_size', (YLeaf(YType.uint8, 'plain-bits-size'), ['int'])),
                                                ('force_ctrl', (YLeaf(YType.boolean, 'force-ctrl'), ['bool'])),
                                                ('drop', (YLeaf(YType.boolean, 'drop'), ['bool'])),
                                                ('mask_da', (YLeaf(YType.uint64, 'mask-da'), ['int'])),
                                                ('mask_ethertype', (YLeaf(YType.uint32, 'mask-ethertype'), ['int'])),
                                                ('mask_plain_bits', (YLeaf(YType.uint64, 'mask-plain-bits'), ['int'])),
                                                ('flow_hits', (YLeaf(YType.uint64, 'flow-hits'), ['int'])),
                                                ('macda', (YLeafList(YType.uint8, 'macda'), ['int'])),
                                            ])
                                            self.flow_no = None
                                            self.is_flow_enabled = None
                                            self.ethertype = None
                                            self.outer_vlan_id = None
                                            self.outer_vlan_user_pri = None
                                            self.inner_vlan_id = None
                                            self.inner_vlan_user_pri = None
                                            self.psci = None
                                            self.match_priority = None
                                            self.tci_v = None
                                            self.tci_e_xr = None
                                            self.tci_sc = None
                                            self.tci_scb = None
                                            self.tci = None
                                            self.tci_c = None
                                            self.tci_chk = None
                                            self.pkt_type = None
                                            self.tag_num = None
                                            self.inner_vlan_dei = None
                                            self.outer_vlan_dei = None
                                            self.pbb_sid = None
                                            self.pbb_bvid = None
                                            self.pbb_pcp = None
                                            self.pbb_dei = None
                                            self.mpls1_label = None
                                            self.mpls1_exp = None
                                            self.mpls1_bos = None
                                            self.mpls2_label = None
                                            self.mpls2_exp = None
                                            self.mpls2_bos = None
                                            self.plain_bits = None
                                            self.plain_bits_size = None
                                            self.force_ctrl = None
                                            self.drop = None
                                            self.mask_da = None
                                            self.mask_ethertype = None
                                            self.mask_plain_bits = None
                                            self.flow_hits = None
                                            self.macda = []
                                            self._segment_path = lambda: "tx-flow"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Ext.Es200Flow.TxFlow, ['flow_no', 'is_flow_enabled', 'ethertype', 'outer_vlan_id', 'outer_vlan_user_pri', 'inner_vlan_id', 'inner_vlan_user_pri', 'psci', 'match_priority', 'tci_v', 'tci_e_xr', 'tci_sc', 'tci_scb', 'tci', 'tci_c', 'tci_chk', 'pkt_type', 'tag_num', 'inner_vlan_dei', 'outer_vlan_dei', 'pbb_sid', 'pbb_bvid', 'pbb_pcp', 'pbb_dei', 'mpls1_label', 'mpls1_exp', 'mpls1_bos', 'mpls2_label', 'mpls2_exp', 'mpls2_bos', 'plain_bits', 'plain_bits_size', 'force_ctrl', 'drop', 'mask_da', 'mask_ethertype', 'mask_plain_bits', 'flow_hits', 'macda'], name, value)


                                    class RxFlow(Entity):
                                        """
                                        Rx Flow Details
                                        
                                        .. attribute:: flow_no
                                        
                                        	Flow Number
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: is_flow_enabled
                                        
                                        	Is Flow Enabled
                                        	**type**\: bool
                                        
                                        .. attribute:: ethertype
                                        
                                        	Parsed EtherType to match could be 0 if Ethertype should'nt                              be matched can be 0x88E5 for MACSec tag
                                        	**type**\: int
                                        
                                        	**range:** 0..65535
                                        
                                        .. attribute:: outer_vlan_id
                                        
                                        	 VLAN ID for outer tag use this when             only one tag should be matched
                                        	**type**\: int
                                        
                                        	**range:** 0..65535
                                        
                                        .. attribute:: outer_vlan_user_pri
                                        
                                        	VLAN User Priority for outer tag  use            this when only one tag should be matched
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: inner_vlan_id
                                        
                                        	VLAN ID for inner tag used when two              VLAN Tags should be matched
                                        	**type**\: int
                                        
                                        	**range:** 0..65535
                                        
                                        .. attribute:: inner_vlan_user_pri
                                        
                                        	 VLAN User priority for inner tag use            when matching two VLAN tags
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: psci
                                        
                                        	 SCI to be matched value required for            ingress only, pass NULL for egress
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: match_priority
                                        
                                        	priority for match 0\-15(highest) 
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: tci_v
                                        
                                        	value of 'v' in TCI to match (1bit) 
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: tci_e_xr
                                        
                                        	value of 'es' in TCI to match (1bit) 
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: tci_sc
                                        
                                        	value of 'sc' in TCI to match (1bit) 
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: tci_scb
                                        
                                        	value of 'scb' in TCI to match (1bit) 
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: tci
                                        
                                        	value of 'e' in TCI to match (1bit )
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: tci_c
                                        
                                        	value of 'c' in TCI to match (1bit) 
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: tci_chk
                                        
                                        	TCI bits will be checked only when this          bit is enabled. All the values of TCI bits       are mandatory when TCI check is used
                                        	**type**\: bool
                                        
                                        .. attribute:: pkt_type
                                        
                                        	Type of packet. See ethMscCfyEPktType\_e
                                        	**type**\: str
                                        
                                        .. attribute:: tag_num
                                        
                                        	No. of MPLS or VLAN tags See ethMscCfyETagNum\_e 
                                        	**type**\: str
                                        
                                        .. attribute:: inner_vlan_dei
                                        
                                        	Dei to match for innner Vlan tag
                                        	**type**\: bool
                                        
                                        .. attribute:: outer_vlan_dei
                                        
                                        	Dei to match for outer Vlan tag
                                        	**type**\: bool
                                        
                                        .. attribute:: pbb_sid
                                        
                                        	 Service Instance id 
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: pbb_bvid
                                        
                                        	 Backbone Vlan id 
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: pbb_pcp
                                        
                                        	 pcp 
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: pbb_dei
                                        
                                        	 dei 
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: mpls1_label
                                        
                                        	 label 
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: mpls1_exp
                                        
                                        	 exp 
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: mpls1_bos
                                        
                                        	 botton of stack 
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: mpls2_label
                                        
                                        	 label 
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: mpls2_exp
                                        
                                        	 exp 
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: mpls2_bos
                                        
                                        	 botton of stack 
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: plain_bits
                                        
                                        	Plain bits to compare. Max values\:               untagged pkt \- 40 bits after EthType             1 VLAN tag \- 24 bits after parsed EthType        2 VLAN tags\- 8 bits after parsed EthType         1 MPLS tag \- 32 bits after 1st tag               2 MPLS tags\- 8 bits following after 2nd          or atmost 5th MPLS tag                           PBB \- 16 bits after C\-SA                         PBB with VLAN tag \- 16 bits of VLAN tag 
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: bit
                                        
                                        .. attribute:: plain_bits_size
                                        
                                        	No. of bits used in plainBits
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: force_ctrl
                                        
                                        	Force the pkt as control pkt irrepective         of the results of control packet detector
                                        	**type**\: bool
                                        
                                        .. attribute:: drop
                                        
                                        	Drop the packet
                                        	**type**\: bool
                                        
                                        .. attribute:: mask_da
                                        
                                        	DA mask
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: mask_ethertype
                                        
                                        	Parsed EtherType mask
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: mask_plain_bits
                                        
                                        	Plain Bits mask
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: flow_hits
                                        
                                        	Pkts matching the Flow
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: macda
                                        
                                        	MAC DA
                                        	**type**\: list of int
                                        
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
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('flow_no', (YLeaf(YType.uint32, 'flow-no'), ['int'])),
                                                ('is_flow_enabled', (YLeaf(YType.boolean, 'is-flow-enabled'), ['bool'])),
                                                ('ethertype', (YLeaf(YType.uint16, 'ethertype'), ['int'])),
                                                ('outer_vlan_id', (YLeaf(YType.uint16, 'outer-vlan-id'), ['int'])),
                                                ('outer_vlan_user_pri', (YLeaf(YType.uint8, 'outer-vlan-user-pri'), ['int'])),
                                                ('inner_vlan_id', (YLeaf(YType.uint16, 'inner-vlan-id'), ['int'])),
                                                ('inner_vlan_user_pri', (YLeaf(YType.uint8, 'inner-vlan-user-pri'), ['int'])),
                                                ('psci', (YLeaf(YType.uint64, 'psci'), ['int'])),
                                                ('match_priority', (YLeaf(YType.uint8, 'match-priority'), ['int'])),
                                                ('tci_v', (YLeaf(YType.uint8, 'tci-v'), ['int'])),
                                                ('tci_e_xr', (YLeaf(YType.uint8, 'tci-e-xr'), ['int'])),
                                                ('tci_sc', (YLeaf(YType.uint8, 'tci-sc'), ['int'])),
                                                ('tci_scb', (YLeaf(YType.uint8, 'tci-scb'), ['int'])),
                                                ('tci', (YLeaf(YType.uint8, 'tci'), ['int'])),
                                                ('tci_c', (YLeaf(YType.uint8, 'tci-c'), ['int'])),
                                                ('tci_chk', (YLeaf(YType.boolean, 'tci-chk'), ['bool'])),
                                                ('pkt_type', (YLeaf(YType.str, 'pkt-type'), ['str'])),
                                                ('tag_num', (YLeaf(YType.str, 'tag-num'), ['str'])),
                                                ('inner_vlan_dei', (YLeaf(YType.boolean, 'inner-vlan-dei'), ['bool'])),
                                                ('outer_vlan_dei', (YLeaf(YType.boolean, 'outer-vlan-dei'), ['bool'])),
                                                ('pbb_sid', (YLeaf(YType.uint32, 'pbb-sid'), ['int'])),
                                                ('pbb_bvid', (YLeaf(YType.uint32, 'pbb-bvid'), ['int'])),
                                                ('pbb_pcp', (YLeaf(YType.uint8, 'pbb-pcp'), ['int'])),
                                                ('pbb_dei', (YLeaf(YType.uint8, 'pbb-dei'), ['int'])),
                                                ('mpls1_label', (YLeaf(YType.uint32, 'mpls1-label'), ['int'])),
                                                ('mpls1_exp', (YLeaf(YType.uint8, 'mpls1-exp'), ['int'])),
                                                ('mpls1_bos', (YLeaf(YType.uint8, 'mpls1-bos'), ['int'])),
                                                ('mpls2_label', (YLeaf(YType.uint32, 'mpls2-label'), ['int'])),
                                                ('mpls2_exp', (YLeaf(YType.uint8, 'mpls2-exp'), ['int'])),
                                                ('mpls2_bos', (YLeaf(YType.uint8, 'mpls2-bos'), ['int'])),
                                                ('plain_bits', (YLeaf(YType.uint64, 'plain-bits'), ['int'])),
                                                ('plain_bits_size', (YLeaf(YType.uint8, 'plain-bits-size'), ['int'])),
                                                ('force_ctrl', (YLeaf(YType.boolean, 'force-ctrl'), ['bool'])),
                                                ('drop', (YLeaf(YType.boolean, 'drop'), ['bool'])),
                                                ('mask_da', (YLeaf(YType.uint64, 'mask-da'), ['int'])),
                                                ('mask_ethertype', (YLeaf(YType.uint32, 'mask-ethertype'), ['int'])),
                                                ('mask_plain_bits', (YLeaf(YType.uint64, 'mask-plain-bits'), ['int'])),
                                                ('flow_hits', (YLeaf(YType.uint64, 'flow-hits'), ['int'])),
                                                ('macda', (YLeafList(YType.uint8, 'macda'), ['int'])),
                                            ])
                                            self.flow_no = None
                                            self.is_flow_enabled = None
                                            self.ethertype = None
                                            self.outer_vlan_id = None
                                            self.outer_vlan_user_pri = None
                                            self.inner_vlan_id = None
                                            self.inner_vlan_user_pri = None
                                            self.psci = None
                                            self.match_priority = None
                                            self.tci_v = None
                                            self.tci_e_xr = None
                                            self.tci_sc = None
                                            self.tci_scb = None
                                            self.tci = None
                                            self.tci_c = None
                                            self.tci_chk = None
                                            self.pkt_type = None
                                            self.tag_num = None
                                            self.inner_vlan_dei = None
                                            self.outer_vlan_dei = None
                                            self.pbb_sid = None
                                            self.pbb_bvid = None
                                            self.pbb_pcp = None
                                            self.pbb_dei = None
                                            self.mpls1_label = None
                                            self.mpls1_exp = None
                                            self.mpls1_bos = None
                                            self.mpls2_label = None
                                            self.mpls2_exp = None
                                            self.mpls2_bos = None
                                            self.plain_bits = None
                                            self.plain_bits_size = None
                                            self.force_ctrl = None
                                            self.drop = None
                                            self.mask_da = None
                                            self.mask_ethertype = None
                                            self.mask_plain_bits = None
                                            self.flow_hits = None
                                            self.macda = []
                                            self._segment_path = lambda: "rx-flow"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Ext.Es200Flow.RxFlow, ['flow_no', 'is_flow_enabled', 'ethertype', 'outer_vlan_id', 'outer_vlan_user_pri', 'inner_vlan_id', 'inner_vlan_user_pri', 'psci', 'match_priority', 'tci_v', 'tci_e_xr', 'tci_sc', 'tci_scb', 'tci', 'tci_c', 'tci_chk', 'pkt_type', 'tag_num', 'inner_vlan_dei', 'outer_vlan_dei', 'pbb_sid', 'pbb_bvid', 'pbb_pcp', 'pbb_dei', 'mpls1_label', 'mpls1_exp', 'mpls1_bos', 'mpls2_label', 'mpls2_exp', 'mpls2_bos', 'plain_bits', 'plain_bits_size', 'force_ctrl', 'drop', 'mask_da', 'mask_ethertype', 'mask_plain_bits', 'flow_hits', 'macda'], name, value)


                    class SwStatistics(Entity):
                        """
                        The Software Statistics
                        
                        .. attribute:: ext
                        
                        	ext
                        	**type**\:  :py:class:`Ext <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext>`
                        
                        

                        """

                        _prefix = 'crypto-macsec-pl-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics, self).__init__()

                            self.yang_name = "sw-statistics"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("ext", ("ext", MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext))])
                            self._leafs = OrderedDict()

                            self.ext = MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext()
                            self.ext.parent = self
                            self._children_name_map["ext"] = "ext"
                            self._segment_path = lambda: "sw-statistics"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics, [], name, value)


                        class Ext(Entity):
                            """
                            ext
                            
                            .. attribute:: msfpga_stats
                            
                            	MSFPGA Stats
                            	**type**\:  :py:class:`MsfpgaStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.MsfpgaStats>`
                            
                            .. attribute:: xlfpga_stats
                            
                            	XLFPGA Stats
                            	**type**\:  :py:class:`XlfpgaStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.XlfpgaStats>`
                            
                            .. attribute:: es200_stats
                            
                            	ES200 Stats
                            	**type**\:  :py:class:`Es200Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats>`
                            
                            .. attribute:: type
                            
                            	type
                            	**type**\:  :py:class:`MacsecPhyVendor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPhyVendor>`
                            
                            

                            """

                            _prefix = 'crypto-macsec-pl-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext, self).__init__()

                                self.yang_name = "ext"
                                self.yang_parent_name = "sw-statistics"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("msfpga-stats", ("msfpga_stats", MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.MsfpgaStats)), ("xlfpga-stats", ("xlfpga_stats", MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.XlfpgaStats)), ("es200-stats", ("es200_stats", MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats))])
                                self._leafs = OrderedDict([
                                    ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'MacsecPhyVendor', '')])),
                                ])
                                self.type = None

                                self.msfpga_stats = MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.MsfpgaStats()
                                self.msfpga_stats.parent = self
                                self._children_name_map["msfpga_stats"] = "msfpga-stats"

                                self.xlfpga_stats = MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.XlfpgaStats()
                                self.xlfpga_stats.parent = self
                                self._children_name_map["xlfpga_stats"] = "xlfpga-stats"

                                self.es200_stats = MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats()
                                self.es200_stats.parent = self
                                self._children_name_map["es200_stats"] = "es200-stats"
                                self._segment_path = lambda: "ext"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext, ['type'], name, value)


                            class MsfpgaStats(Entity):
                                """
                                MSFPGA Stats
                                
                                .. attribute:: tx_sa_stats
                                
                                	Tx SA Stats
                                	**type**\:  :py:class:`TxSaStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.MsfpgaStats.TxSaStats>`
                                
                                .. attribute:: rx_sa_stats
                                
                                	Rx SA Stats
                                	**type**\:  :py:class:`RxSaStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.MsfpgaStats.RxSaStats>`
                                
                                .. attribute:: tx_interface_macsec_stats
                                
                                	Tx interface Macsec Stats
                                	**type**\:  :py:class:`TxInterfaceMacsecStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.MsfpgaStats.TxInterfaceMacsecStats>`
                                
                                .. attribute:: rx_interface_macsec_stats
                                
                                	Rx interface Macsec Stats
                                	**type**\:  :py:class:`RxInterfaceMacsecStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.MsfpgaStats.RxInterfaceMacsecStats>`
                                
                                

                                """

                                _prefix = 'crypto-macsec-pl-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.MsfpgaStats, self).__init__()

                                    self.yang_name = "msfpga-stats"
                                    self.yang_parent_name = "ext"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("tx-sa-stats", ("tx_sa_stats", MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.MsfpgaStats.TxSaStats)), ("rx-sa-stats", ("rx_sa_stats", MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.MsfpgaStats.RxSaStats)), ("tx-interface-macsec-stats", ("tx_interface_macsec_stats", MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.MsfpgaStats.TxInterfaceMacsecStats)), ("rx-interface-macsec-stats", ("rx_interface_macsec_stats", MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.MsfpgaStats.RxInterfaceMacsecStats))])
                                    self._leafs = OrderedDict()

                                    self.tx_sa_stats = MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.MsfpgaStats.TxSaStats()
                                    self.tx_sa_stats.parent = self
                                    self._children_name_map["tx_sa_stats"] = "tx-sa-stats"

                                    self.rx_sa_stats = MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.MsfpgaStats.RxSaStats()
                                    self.rx_sa_stats.parent = self
                                    self._children_name_map["rx_sa_stats"] = "rx-sa-stats"

                                    self.tx_interface_macsec_stats = MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.MsfpgaStats.TxInterfaceMacsecStats()
                                    self.tx_interface_macsec_stats.parent = self
                                    self._children_name_map["tx_interface_macsec_stats"] = "tx-interface-macsec-stats"

                                    self.rx_interface_macsec_stats = MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.MsfpgaStats.RxInterfaceMacsecStats()
                                    self.rx_interface_macsec_stats.parent = self
                                    self._children_name_map["rx_interface_macsec_stats"] = "rx-interface-macsec-stats"
                                    self._segment_path = lambda: "msfpga-stats"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.MsfpgaStats, [], name, value)


                                class TxSaStats(Entity):
                                    """
                                    Tx SA Stats
                                    
                                    .. attribute:: out_pkts_protected
                                    
                                    	Tx Pkts Protected
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_pkts_encrypted
                                    
                                    	Tx Pkts Encrypted
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_octets_protected
                                    
                                    	Tx Octets Protected
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_octets_encrypted
                                    
                                    	Tx Octets Encrypted
                                    	**type**\: int
                                    
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
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('out_pkts_protected', (YLeaf(YType.uint64, 'out-pkts-protected'), ['int'])),
                                            ('out_pkts_encrypted', (YLeaf(YType.uint64, 'out-pkts-encrypted'), ['int'])),
                                            ('out_octets_protected', (YLeaf(YType.uint64, 'out-octets-protected'), ['int'])),
                                            ('out_octets_encrypted', (YLeaf(YType.uint64, 'out-octets-encrypted'), ['int'])),
                                        ])
                                        self.out_pkts_protected = None
                                        self.out_pkts_encrypted = None
                                        self.out_octets_protected = None
                                        self.out_octets_encrypted = None
                                        self._segment_path = lambda: "tx-sa-stats"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.MsfpgaStats.TxSaStats, ['out_pkts_protected', 'out_pkts_encrypted', 'out_octets_protected', 'out_octets_encrypted'], name, value)


                                class RxSaStats(Entity):
                                    """
                                    Rx SA Stats
                                    
                                    .. attribute:: in_pkts_unused_sa
                                    
                                    	Rx Pkts Unused SA
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkts_not_using_sa
                                    
                                    	Rx Pkts Not Using SA
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkts_not_valid
                                    
                                    	Rx Pkts Not Valid
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkts_invalid
                                    
                                    	Rx Pkts Invalid
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkts_ok
                                    
                                    	Rx Pkts OK
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkts_delayed
                                    
                                    	Rx Pkts Delayed
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkts_late
                                    
                                    	Rx Pkts Late
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkts_unchecked
                                    
                                    	Rx Pkts Unchecked
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_octets_validated
                                    
                                    	Rx Octets Validated
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_octets_decrypted
                                    
                                    	Rx Octets Decrypted
                                    	**type**\: int
                                    
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
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('in_pkts_unused_sa', (YLeaf(YType.uint64, 'in-pkts-unused-sa'), ['int'])),
                                            ('in_pkts_not_using_sa', (YLeaf(YType.uint64, 'in-pkts-not-using-sa'), ['int'])),
                                            ('in_pkts_not_valid', (YLeaf(YType.uint64, 'in-pkts-not-valid'), ['int'])),
                                            ('in_pkts_invalid', (YLeaf(YType.uint64, 'in-pkts-invalid'), ['int'])),
                                            ('in_pkts_ok', (YLeaf(YType.uint64, 'in-pkts-ok'), ['int'])),
                                            ('in_pkts_delayed', (YLeaf(YType.uint64, 'in-pkts-delayed'), ['int'])),
                                            ('in_pkts_late', (YLeaf(YType.uint64, 'in-pkts-late'), ['int'])),
                                            ('in_pkts_unchecked', (YLeaf(YType.uint64, 'in-pkts-unchecked'), ['int'])),
                                            ('in_octets_validated', (YLeaf(YType.uint64, 'in-octets-validated'), ['int'])),
                                            ('in_octets_decrypted', (YLeaf(YType.uint64, 'in-octets-decrypted'), ['int'])),
                                        ])
                                        self.in_pkts_unused_sa = None
                                        self.in_pkts_not_using_sa = None
                                        self.in_pkts_not_valid = None
                                        self.in_pkts_invalid = None
                                        self.in_pkts_ok = None
                                        self.in_pkts_delayed = None
                                        self.in_pkts_late = None
                                        self.in_pkts_unchecked = None
                                        self.in_octets_validated = None
                                        self.in_octets_decrypted = None
                                        self._segment_path = lambda: "rx-sa-stats"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.MsfpgaStats.RxSaStats, ['in_pkts_unused_sa', 'in_pkts_not_using_sa', 'in_pkts_not_valid', 'in_pkts_invalid', 'in_pkts_ok', 'in_pkts_delayed', 'in_pkts_late', 'in_pkts_unchecked', 'in_octets_validated', 'in_octets_decrypted'], name, value)


                                class TxInterfaceMacsecStats(Entity):
                                    """
                                    Tx interface Macsec Stats
                                    
                                    .. attribute:: out_pkt_uncontrolled
                                    
                                    	Tx Pkts Uncontrolled
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_pkt_untagged
                                    
                                    	Tx Pkts Untagged
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_pkt_too_long
                                    
                                    	Tx Pkts Too Long
                                    	**type**\: int
                                    
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
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('out_pkt_uncontrolled', (YLeaf(YType.uint64, 'out-pkt-uncontrolled'), ['int'])),
                                            ('out_pkt_untagged', (YLeaf(YType.uint64, 'out-pkt-untagged'), ['int'])),
                                            ('out_pkt_too_long', (YLeaf(YType.uint64, 'out-pkt-too-long'), ['int'])),
                                        ])
                                        self.out_pkt_uncontrolled = None
                                        self.out_pkt_untagged = None
                                        self.out_pkt_too_long = None
                                        self._segment_path = lambda: "tx-interface-macsec-stats"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.MsfpgaStats.TxInterfaceMacsecStats, ['out_pkt_uncontrolled', 'out_pkt_untagged', 'out_pkt_too_long'], name, value)


                                class RxInterfaceMacsecStats(Entity):
                                    """
                                    Rx interface Macsec Stats
                                    
                                    .. attribute:: in_pkt_untagged
                                    
                                    	Rx Pkts Untagged
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkt_notag
                                    
                                    	Rx Pkts Notag
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkt_bad_tag
                                    
                                    	Rx Pkts Bad tag
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkt_no_sci
                                    
                                    	Rx Pkts No Sci
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkt_unknown_sci
                                    
                                    	Rx Pkts Unknown Sci
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkt_tagged
                                    
                                    	Rx Pkts Tagged
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkt_overrun
                                    
                                    	Rx Pkts Over Run
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkt_uncontrolled
                                    
                                    	Rx Pkts Uncontrolled
                                    	**type**\: int
                                    
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
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('in_pkt_untagged', (YLeaf(YType.uint64, 'in-pkt-untagged'), ['int'])),
                                            ('in_pkt_notag', (YLeaf(YType.uint64, 'in-pkt-notag'), ['int'])),
                                            ('in_pkt_bad_tag', (YLeaf(YType.uint64, 'in-pkt-bad-tag'), ['int'])),
                                            ('in_pkt_no_sci', (YLeaf(YType.uint64, 'in-pkt-no-sci'), ['int'])),
                                            ('in_pkt_unknown_sci', (YLeaf(YType.uint64, 'in-pkt-unknown-sci'), ['int'])),
                                            ('in_pkt_tagged', (YLeaf(YType.uint64, 'in-pkt-tagged'), ['int'])),
                                            ('in_pkt_overrun', (YLeaf(YType.uint64, 'in-pkt-overrun'), ['int'])),
                                            ('in_pkt_uncontrolled', (YLeaf(YType.uint64, 'in-pkt-uncontrolled'), ['int'])),
                                        ])
                                        self.in_pkt_untagged = None
                                        self.in_pkt_notag = None
                                        self.in_pkt_bad_tag = None
                                        self.in_pkt_no_sci = None
                                        self.in_pkt_unknown_sci = None
                                        self.in_pkt_tagged = None
                                        self.in_pkt_overrun = None
                                        self.in_pkt_uncontrolled = None
                                        self._segment_path = lambda: "rx-interface-macsec-stats"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.MsfpgaStats.RxInterfaceMacsecStats, ['in_pkt_untagged', 'in_pkt_notag', 'in_pkt_bad_tag', 'in_pkt_no_sci', 'in_pkt_unknown_sci', 'in_pkt_tagged', 'in_pkt_overrun', 'in_pkt_uncontrolled'], name, value)


                            class XlfpgaStats(Entity):
                                """
                                XLFPGA Stats
                                
                                .. attribute:: macsec_tx_stats
                                
                                	Tx SC and SA Level Stats
                                	**type**\:  :py:class:`MacsecTxStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.XlfpgaStats.MacsecTxStats>`
                                
                                .. attribute:: macsec_rx_stats
                                
                                	Rx SC and SA Level Stats
                                	**type**\:  :py:class:`MacsecRxStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.XlfpgaStats.MacsecRxStats>`
                                
                                

                                """

                                _prefix = 'crypto-macsec-pl-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.XlfpgaStats, self).__init__()

                                    self.yang_name = "xlfpga-stats"
                                    self.yang_parent_name = "ext"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("macsec-tx-stats", ("macsec_tx_stats", MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.XlfpgaStats.MacsecTxStats)), ("macsec-rx-stats", ("macsec_rx_stats", MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.XlfpgaStats.MacsecRxStats))])
                                    self._leafs = OrderedDict()

                                    self.macsec_tx_stats = MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.XlfpgaStats.MacsecTxStats()
                                    self.macsec_tx_stats.parent = self
                                    self._children_name_map["macsec_tx_stats"] = "macsec-tx-stats"

                                    self.macsec_rx_stats = MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.XlfpgaStats.MacsecRxStats()
                                    self.macsec_rx_stats.parent = self
                                    self._children_name_map["macsec_rx_stats"] = "macsec-rx-stats"
                                    self._segment_path = lambda: "xlfpga-stats"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.XlfpgaStats, [], name, value)


                                class MacsecTxStats(Entity):
                                    """
                                    Tx SC and SA Level Stats
                                    
                                    .. attribute:: sc_encrypted_octets
                                    
                                    	Tx Octets Encrypted
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_toolong_pkts
                                    
                                    	Tx Pkts Too Long
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_encrypted_pkts
                                    
                                    	Tx packets Encrypted
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_untagged_pkts
                                    
                                    	Tx Untagged Packets
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_overrun_pkts
                                    
                                    	Tx Overrun Packets
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_bypass_pkts
                                    
                                    	Tx Bypass Packets
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_eapol_pkts
                                    
                                    	Tx Eapol Packets
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_dropped_pkts
                                    
                                    	Tx Dropped Packets
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: current_an
                                    
                                    	Current Tx AN
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sa_encrypted_pkts
                                    
                                    	Current Tx SA Encrypted Packets
                                    	**type**\: int
                                    
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
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('sc_encrypted_octets', (YLeaf(YType.uint64, 'sc-encrypted-octets'), ['int'])),
                                            ('sc_toolong_pkts', (YLeaf(YType.uint64, 'sc-toolong-pkts'), ['int'])),
                                            ('sc_encrypted_pkts', (YLeaf(YType.uint64, 'sc-encrypted-pkts'), ['int'])),
                                            ('sc_untagged_pkts', (YLeaf(YType.uint64, 'sc-untagged-pkts'), ['int'])),
                                            ('sc_overrun_pkts', (YLeaf(YType.uint64, 'sc-overrun-pkts'), ['int'])),
                                            ('sc_bypass_pkts', (YLeaf(YType.uint64, 'sc-bypass-pkts'), ['int'])),
                                            ('sc_eapol_pkts', (YLeaf(YType.uint64, 'sc-eapol-pkts'), ['int'])),
                                            ('sc_dropped_pkts', (YLeaf(YType.uint64, 'sc-dropped-pkts'), ['int'])),
                                            ('current_an', (YLeaf(YType.uint64, 'current-an'), ['int'])),
                                            ('sa_encrypted_pkts', (YLeaf(YType.uint64, 'sa-encrypted-pkts'), ['int'])),
                                        ])
                                        self.sc_encrypted_octets = None
                                        self.sc_toolong_pkts = None
                                        self.sc_encrypted_pkts = None
                                        self.sc_untagged_pkts = None
                                        self.sc_overrun_pkts = None
                                        self.sc_bypass_pkts = None
                                        self.sc_eapol_pkts = None
                                        self.sc_dropped_pkts = None
                                        self.current_an = None
                                        self.sa_encrypted_pkts = None
                                        self._segment_path = lambda: "macsec-tx-stats"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.XlfpgaStats.MacsecTxStats, ['sc_encrypted_octets', 'sc_toolong_pkts', 'sc_encrypted_pkts', 'sc_untagged_pkts', 'sc_overrun_pkts', 'sc_bypass_pkts', 'sc_eapol_pkts', 'sc_dropped_pkts', 'current_an', 'sa_encrypted_pkts'], name, value)


                                class MacsecRxStats(Entity):
                                    """
                                    Rx SC and SA Level Stats
                                    
                                    .. attribute:: sc_decrypted_octets
                                    
                                    	Rx Octets Decrypted
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_no_tag_pkts
                                    
                                    	Rx No Tag Packets
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_untagged_pkts
                                    
                                    	Rx Untagged Packets
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_bad_tag_pkts
                                    
                                    	Rx Bad Tag Packets
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_late_pkts
                                    
                                    	Rx Late Pkts
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_delayed_pkts
                                    
                                    	Rx Delayed Pkts
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_unchecked_pkts
                                    
                                    	Rx Unchecked Pkts
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_no_sci_pkts
                                    
                                    	Rx No SCI Pkts
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_unknown_sci_pkts
                                    
                                    	Rx Unknown SCI Pkts
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_ok_pkts
                                    
                                    	Rx Pkts Ok
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_not_using_pkts
                                    
                                    	Rx Pkts Not Using SA
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_unused_pkts
                                    
                                    	Rx Pkts Unused SA
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_not_valid_pkts
                                    
                                    	Rx Not Valid Pkts
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_invalid_pkts
                                    
                                    	Rx Pkts Invalid
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_overrun_pkts
                                    
                                    	Rx Overrun Pkts
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_bypass_pkts
                                    
                                    	Rx Bypass Packets
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_eapol_pkts
                                    
                                    	Rx Eapol Packets
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: sc_dropped_pkts
                                    
                                    	Rx Dropped Packets
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: rx_sa_stat
                                    
                                    	Rx SA Level Stats
                                    	**type**\: list of  		 :py:class:`RxSaStat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.XlfpgaStats.MacsecRxStats.RxSaStat>`
                                    
                                    

                                    """

                                    _prefix = 'crypto-macsec-pl-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.XlfpgaStats.MacsecRxStats, self).__init__()

                                        self.yang_name = "macsec-rx-stats"
                                        self.yang_parent_name = "xlfpga-stats"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("rx-sa-stat", ("rx_sa_stat", MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.XlfpgaStats.MacsecRxStats.RxSaStat))])
                                        self._leafs = OrderedDict([
                                            ('sc_decrypted_octets', (YLeaf(YType.uint64, 'sc-decrypted-octets'), ['int'])),
                                            ('sc_no_tag_pkts', (YLeaf(YType.uint64, 'sc-no-tag-pkts'), ['int'])),
                                            ('sc_untagged_pkts', (YLeaf(YType.uint64, 'sc-untagged-pkts'), ['int'])),
                                            ('sc_bad_tag_pkts', (YLeaf(YType.uint64, 'sc-bad-tag-pkts'), ['int'])),
                                            ('sc_late_pkts', (YLeaf(YType.uint64, 'sc-late-pkts'), ['int'])),
                                            ('sc_delayed_pkts', (YLeaf(YType.uint64, 'sc-delayed-pkts'), ['int'])),
                                            ('sc_unchecked_pkts', (YLeaf(YType.uint64, 'sc-unchecked-pkts'), ['int'])),
                                            ('sc_no_sci_pkts', (YLeaf(YType.uint64, 'sc-no-sci-pkts'), ['int'])),
                                            ('sc_unknown_sci_pkts', (YLeaf(YType.uint64, 'sc-unknown-sci-pkts'), ['int'])),
                                            ('sc_ok_pkts', (YLeaf(YType.uint64, 'sc-ok-pkts'), ['int'])),
                                            ('sc_not_using_pkts', (YLeaf(YType.uint64, 'sc-not-using-pkts'), ['int'])),
                                            ('sc_unused_pkts', (YLeaf(YType.uint64, 'sc-unused-pkts'), ['int'])),
                                            ('sc_not_valid_pkts', (YLeaf(YType.uint64, 'sc-not-valid-pkts'), ['int'])),
                                            ('sc_invalid_pkts', (YLeaf(YType.uint64, 'sc-invalid-pkts'), ['int'])),
                                            ('sc_overrun_pkts', (YLeaf(YType.uint64, 'sc-overrun-pkts'), ['int'])),
                                            ('sc_bypass_pkts', (YLeaf(YType.uint64, 'sc-bypass-pkts'), ['int'])),
                                            ('sc_eapol_pkts', (YLeaf(YType.uint64, 'sc-eapol-pkts'), ['int'])),
                                            ('sc_dropped_pkts', (YLeaf(YType.uint64, 'sc-dropped-pkts'), ['int'])),
                                        ])
                                        self.sc_decrypted_octets = None
                                        self.sc_no_tag_pkts = None
                                        self.sc_untagged_pkts = None
                                        self.sc_bad_tag_pkts = None
                                        self.sc_late_pkts = None
                                        self.sc_delayed_pkts = None
                                        self.sc_unchecked_pkts = None
                                        self.sc_no_sci_pkts = None
                                        self.sc_unknown_sci_pkts = None
                                        self.sc_ok_pkts = None
                                        self.sc_not_using_pkts = None
                                        self.sc_unused_pkts = None
                                        self.sc_not_valid_pkts = None
                                        self.sc_invalid_pkts = None
                                        self.sc_overrun_pkts = None
                                        self.sc_bypass_pkts = None
                                        self.sc_eapol_pkts = None
                                        self.sc_dropped_pkts = None

                                        self.rx_sa_stat = YList(self)
                                        self._segment_path = lambda: "macsec-rx-stats"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.XlfpgaStats.MacsecRxStats, ['sc_decrypted_octets', 'sc_no_tag_pkts', 'sc_untagged_pkts', 'sc_bad_tag_pkts', 'sc_late_pkts', 'sc_delayed_pkts', 'sc_unchecked_pkts', 'sc_no_sci_pkts', 'sc_unknown_sci_pkts', 'sc_ok_pkts', 'sc_not_using_pkts', 'sc_unused_pkts', 'sc_not_valid_pkts', 'sc_invalid_pkts', 'sc_overrun_pkts', 'sc_bypass_pkts', 'sc_eapol_pkts', 'sc_dropped_pkts'], name, value)


                                    class RxSaStat(Entity):
                                        """
                                        Rx SA Level Stats
                                        
                                        .. attribute:: an
                                        
                                        	Current Rx AN
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: sa_ok_pkts
                                        
                                        	Rx Ok Pkts for Current AN
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: sa_not_using_pkts
                                        
                                        	Rx Pkts not using SA for Current AN
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: sa_unused_pkts
                                        
                                        	Rx Pkts Unused Pkts for Current AN
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: sa_not_valid_pkts
                                        
                                        	Rx Not Valid Pkts for Current AN
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: sa_invalid_pkts
                                        
                                        	Rx Invalid Pkts for current AN
                                        	**type**\: int
                                        
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
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('an', (YLeaf(YType.uint64, 'an'), ['int'])),
                                                ('sa_ok_pkts', (YLeaf(YType.uint64, 'sa-ok-pkts'), ['int'])),
                                                ('sa_not_using_pkts', (YLeaf(YType.uint64, 'sa-not-using-pkts'), ['int'])),
                                                ('sa_unused_pkts', (YLeaf(YType.uint64, 'sa-unused-pkts'), ['int'])),
                                                ('sa_not_valid_pkts', (YLeaf(YType.uint64, 'sa-not-valid-pkts'), ['int'])),
                                                ('sa_invalid_pkts', (YLeaf(YType.uint64, 'sa-invalid-pkts'), ['int'])),
                                            ])
                                            self.an = None
                                            self.sa_ok_pkts = None
                                            self.sa_not_using_pkts = None
                                            self.sa_unused_pkts = None
                                            self.sa_not_valid_pkts = None
                                            self.sa_invalid_pkts = None
                                            self._segment_path = lambda: "rx-sa-stat"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.XlfpgaStats.MacsecRxStats.RxSaStat, ['an', 'sa_ok_pkts', 'sa_not_using_pkts', 'sa_unused_pkts', 'sa_not_valid_pkts', 'sa_invalid_pkts'], name, value)


                            class Es200Stats(Entity):
                                """
                                ES200 Stats
                                
                                .. attribute:: tx_sa_stats
                                
                                	Tx SA Stats
                                	**type**\:  :py:class:`TxSaStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats.TxSaStats>`
                                
                                .. attribute:: rx_sa_stats
                                
                                	Rx SA Stats
                                	**type**\:  :py:class:`RxSaStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats.RxSaStats>`
                                
                                .. attribute:: tx_sc_macsec_stats
                                
                                	Tx SC Macsec Stats
                                	**type**\:  :py:class:`TxScMacsecStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats.TxScMacsecStats>`
                                
                                .. attribute:: rx_sc_macsec_stats
                                
                                	Rx SC Macsec Stats
                                	**type**\:  :py:class:`RxScMacsecStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats.RxScMacsecStats>`
                                
                                .. attribute:: tx_interface_macsec_stats
                                
                                	Tx interface Macsec Stats
                                	**type**\:  :py:class:`TxInterfaceMacsecStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats.TxInterfaceMacsecStats>`
                                
                                .. attribute:: rx_interface_macsec_stats
                                
                                	Rx interface Macsec Stats
                                	**type**\:  :py:class:`RxInterfaceMacsecStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats.RxInterfaceMacsecStats>`
                                
                                .. attribute:: tx_port_stats
                                
                                	Port level TX Stats
                                	**type**\:  :py:class:`TxPortStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats.TxPortStats>`
                                
                                .. attribute:: rx_port_stats
                                
                                	Port level RX Stats
                                	**type**\:  :py:class:`RxPortStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats.RxPortStats>`
                                
                                

                                """

                                _prefix = 'crypto-macsec-pl-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats, self).__init__()

                                    self.yang_name = "es200-stats"
                                    self.yang_parent_name = "ext"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("tx-sa-stats", ("tx_sa_stats", MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats.TxSaStats)), ("rx-sa-stats", ("rx_sa_stats", MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats.RxSaStats)), ("tx-sc-macsec-stats", ("tx_sc_macsec_stats", MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats.TxScMacsecStats)), ("rx-sc-macsec-stats", ("rx_sc_macsec_stats", MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats.RxScMacsecStats)), ("tx-interface-macsec-stats", ("tx_interface_macsec_stats", MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats.TxInterfaceMacsecStats)), ("rx-interface-macsec-stats", ("rx_interface_macsec_stats", MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats.RxInterfaceMacsecStats)), ("tx-port-stats", ("tx_port_stats", MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats.TxPortStats)), ("rx-port-stats", ("rx_port_stats", MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats.RxPortStats))])
                                    self._leafs = OrderedDict()

                                    self.tx_sa_stats = MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats.TxSaStats()
                                    self.tx_sa_stats.parent = self
                                    self._children_name_map["tx_sa_stats"] = "tx-sa-stats"

                                    self.rx_sa_stats = MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats.RxSaStats()
                                    self.rx_sa_stats.parent = self
                                    self._children_name_map["rx_sa_stats"] = "rx-sa-stats"

                                    self.tx_sc_macsec_stats = MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats.TxScMacsecStats()
                                    self.tx_sc_macsec_stats.parent = self
                                    self._children_name_map["tx_sc_macsec_stats"] = "tx-sc-macsec-stats"

                                    self.rx_sc_macsec_stats = MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats.RxScMacsecStats()
                                    self.rx_sc_macsec_stats.parent = self
                                    self._children_name_map["rx_sc_macsec_stats"] = "rx-sc-macsec-stats"

                                    self.tx_interface_macsec_stats = MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats.TxInterfaceMacsecStats()
                                    self.tx_interface_macsec_stats.parent = self
                                    self._children_name_map["tx_interface_macsec_stats"] = "tx-interface-macsec-stats"

                                    self.rx_interface_macsec_stats = MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats.RxInterfaceMacsecStats()
                                    self.rx_interface_macsec_stats.parent = self
                                    self._children_name_map["rx_interface_macsec_stats"] = "rx-interface-macsec-stats"

                                    self.tx_port_stats = MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats.TxPortStats()
                                    self.tx_port_stats.parent = self
                                    self._children_name_map["tx_port_stats"] = "tx-port-stats"

                                    self.rx_port_stats = MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats.RxPortStats()
                                    self.rx_port_stats.parent = self
                                    self._children_name_map["rx_port_stats"] = "rx-port-stats"
                                    self._segment_path = lambda: "es200-stats"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats, [], name, value)


                                class TxSaStats(Entity):
                                    """
                                    Tx SA Stats
                                    
                                    .. attribute:: out_pkts_too_long
                                    
                                    	packets exceeding egress MTU
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_pkts_encrypted_protected
                                    
                                    	packets encrypted/protected
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_octets_encrypted_protected1
                                    
                                    	octets1 encrypted/protected ?
                                    	**type**\: int
                                    
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
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('out_pkts_too_long', (YLeaf(YType.uint64, 'out-pkts-too-long'), ['int'])),
                                            ('out_pkts_encrypted_protected', (YLeaf(YType.uint64, 'out-pkts-encrypted-protected'), ['int'])),
                                            ('out_octets_encrypted_protected1', (YLeaf(YType.uint64, 'out-octets-encrypted-protected1'), ['int'])),
                                        ])
                                        self.out_pkts_too_long = None
                                        self.out_pkts_encrypted_protected = None
                                        self.out_octets_encrypted_protected1 = None
                                        self._segment_path = lambda: "tx-sa-stats"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats.TxSaStats, ['out_pkts_too_long', 'out_pkts_encrypted_protected', 'out_octets_encrypted_protected1'], name, value)


                                class RxSaStats(Entity):
                                    """
                                    Rx SA Stats
                                    
                                    .. attribute:: in_pkts_unchecked
                                    
                                    	frame not valid & validateFrames disabled
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkts_delayed
                                    
                                    	PN of packet outside replay window & validateFrames !strict
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkts_late
                                    
                                    	PN of packet outside replay window & validateFrames strict
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkts_ok
                                    
                                    	packets with no error
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkts_invalid
                                    
                                    	packet not valid & validateFrames !strict
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkts_not_valid
                                    
                                    	packet not valid & validateFrames strict
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkts_not_using_sa
                                    
                                    	packet assigned to SA not in use & validateFrames strict
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkts_unused_sa
                                    
                                    	packet assigned to SA not in use & validateFrames !strict
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_octets_decrypted_validated1
                                    
                                    	octets1 decrypted/validated
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_octets_validated
                                    
                                    	octets validated
                                    	**type**\: int
                                    
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
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('in_pkts_unchecked', (YLeaf(YType.uint64, 'in-pkts-unchecked'), ['int'])),
                                            ('in_pkts_delayed', (YLeaf(YType.uint64, 'in-pkts-delayed'), ['int'])),
                                            ('in_pkts_late', (YLeaf(YType.uint64, 'in-pkts-late'), ['int'])),
                                            ('in_pkts_ok', (YLeaf(YType.uint64, 'in-pkts-ok'), ['int'])),
                                            ('in_pkts_invalid', (YLeaf(YType.uint64, 'in-pkts-invalid'), ['int'])),
                                            ('in_pkts_not_valid', (YLeaf(YType.uint64, 'in-pkts-not-valid'), ['int'])),
                                            ('in_pkts_not_using_sa', (YLeaf(YType.uint64, 'in-pkts-not-using-sa'), ['int'])),
                                            ('in_pkts_unused_sa', (YLeaf(YType.uint64, 'in-pkts-unused-sa'), ['int'])),
                                            ('in_octets_decrypted_validated1', (YLeaf(YType.uint64, 'in-octets-decrypted-validated1'), ['int'])),
                                            ('in_octets_validated', (YLeaf(YType.uint64, 'in-octets-validated'), ['int'])),
                                        ])
                                        self.in_pkts_unchecked = None
                                        self.in_pkts_delayed = None
                                        self.in_pkts_late = None
                                        self.in_pkts_ok = None
                                        self.in_pkts_invalid = None
                                        self.in_pkts_not_valid = None
                                        self.in_pkts_not_using_sa = None
                                        self.in_pkts_unused_sa = None
                                        self.in_octets_decrypted_validated1 = None
                                        self.in_octets_validated = None
                                        self._segment_path = lambda: "rx-sa-stats"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats.RxSaStats, ['in_pkts_unchecked', 'in_pkts_delayed', 'in_pkts_late', 'in_pkts_ok', 'in_pkts_invalid', 'in_pkts_not_valid', 'in_pkts_not_using_sa', 'in_pkts_unused_sa', 'in_octets_decrypted_validated1', 'in_octets_validated'], name, value)


                                class TxScMacsecStats(Entity):
                                    """
                                    Tx SC Macsec Stats
                                    
                                    .. attribute:: out_pkts_sa_not_in_use
                                    
                                    	Packets received with SA not in use
                                    	**type**\: int
                                    
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
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('out_pkts_sa_not_in_use', (YLeaf(YType.uint64, 'out-pkts-sa-not-in-use'), ['int'])),
                                        ])
                                        self.out_pkts_sa_not_in_use = None
                                        self._segment_path = lambda: "tx-sc-macsec-stats"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats.TxScMacsecStats, ['out_pkts_sa_not_in_use'], name, value)


                                class RxScMacsecStats(Entity):
                                    """
                                    Rx SC Macsec Stats
                                    
                                    .. attribute:: in_pkts_sa_not_in_use
                                    
                                    	Packets received with SA not in use
                                    	**type**\: int
                                    
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
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('in_pkts_sa_not_in_use', (YLeaf(YType.uint64, 'in-pkts-sa-not-in-use'), ['int'])),
                                        ])
                                        self.in_pkts_sa_not_in_use = None
                                        self._segment_path = lambda: "rx-sc-macsec-stats"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats.RxScMacsecStats, ['in_pkts_sa_not_in_use'], name, value)


                                class TxInterfaceMacsecStats(Entity):
                                    """
                                    Tx interface Macsec Stats
                                    
                                    .. attribute:: transform_error_pkts
                                    
                                    	counter to count internal errors in the MACSec core
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_pkt_ctrl
                                    
                                    	egress packet that is classified as control packet
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_pkts_untagged
                                    
                                    	egress packet to go out untagged when protectFrames not set
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_octets_unctrl
                                    
                                    	Octets tx on uncontrolled port
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_octets_ctrl
                                    
                                    	Octets tx on controlled port
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_octets_common
                                    
                                    	Octets tx on common port
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_ucast_pkts_unctrl
                                    
                                    	Unicast pkts tx on uncontrolled port
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_ucast_pkts_ctrl
                                    
                                    	Unicast pkts tx on controlled port
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_mcast_pkts_unctrl
                                    
                                    	Multicast pkts tx on uncontrolled port
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_mcast_pkts_ctrl
                                    
                                    	Multicast pkts tx on controlled port
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_bcast_pkts_unctrl
                                    
                                    	Broadcast pkts tx on uncontrolled port
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_bcast_pkts_ctrl
                                    
                                    	Broadcast pkts tx on controlled port
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_rx_drop_pkts_unctrl
                                    
                                    	Control pkts dropped due to overrun
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_rx_drop_pkts_ctrl
                                    
                                    	Data pkts dropped due to overrun
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_rx_err_pkts_unctrl
                                    
                                    	Control pkts error\-terminated due to overrun
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_rx_err_pkts_ctrl
                                    
                                    	Data pkts error\-terminated due to overrun
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_drop_pkts_class
                                    
                                    	Packets dropped due to overflow in classification pipeline
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: out_drop_pkts_data
                                    
                                    	Packets dropped due to overflow in  processing pipeline
                                    	**type**\: int
                                    
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
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('transform_error_pkts', (YLeaf(YType.uint64, 'transform-error-pkts'), ['int'])),
                                            ('out_pkt_ctrl', (YLeaf(YType.uint64, 'out-pkt-ctrl'), ['int'])),
                                            ('out_pkts_untagged', (YLeaf(YType.uint64, 'out-pkts-untagged'), ['int'])),
                                            ('out_octets_unctrl', (YLeaf(YType.uint64, 'out-octets-unctrl'), ['int'])),
                                            ('out_octets_ctrl', (YLeaf(YType.uint64, 'out-octets-ctrl'), ['int'])),
                                            ('out_octets_common', (YLeaf(YType.uint64, 'out-octets-common'), ['int'])),
                                            ('out_ucast_pkts_unctrl', (YLeaf(YType.uint64, 'out-ucast-pkts-unctrl'), ['int'])),
                                            ('out_ucast_pkts_ctrl', (YLeaf(YType.uint64, 'out-ucast-pkts-ctrl'), ['int'])),
                                            ('out_mcast_pkts_unctrl', (YLeaf(YType.uint64, 'out-mcast-pkts-unctrl'), ['int'])),
                                            ('out_mcast_pkts_ctrl', (YLeaf(YType.uint64, 'out-mcast-pkts-ctrl'), ['int'])),
                                            ('out_bcast_pkts_unctrl', (YLeaf(YType.uint64, 'out-bcast-pkts-unctrl'), ['int'])),
                                            ('out_bcast_pkts_ctrl', (YLeaf(YType.uint64, 'out-bcast-pkts-ctrl'), ['int'])),
                                            ('out_rx_drop_pkts_unctrl', (YLeaf(YType.uint64, 'out-rx-drop-pkts-unctrl'), ['int'])),
                                            ('out_rx_drop_pkts_ctrl', (YLeaf(YType.uint64, 'out-rx-drop-pkts-ctrl'), ['int'])),
                                            ('out_rx_err_pkts_unctrl', (YLeaf(YType.uint64, 'out-rx-err-pkts-unctrl'), ['int'])),
                                            ('out_rx_err_pkts_ctrl', (YLeaf(YType.uint64, 'out-rx-err-pkts-ctrl'), ['int'])),
                                            ('out_drop_pkts_class', (YLeaf(YType.uint64, 'out-drop-pkts-class'), ['int'])),
                                            ('out_drop_pkts_data', (YLeaf(YType.uint64, 'out-drop-pkts-data'), ['int'])),
                                        ])
                                        self.transform_error_pkts = None
                                        self.out_pkt_ctrl = None
                                        self.out_pkts_untagged = None
                                        self.out_octets_unctrl = None
                                        self.out_octets_ctrl = None
                                        self.out_octets_common = None
                                        self.out_ucast_pkts_unctrl = None
                                        self.out_ucast_pkts_ctrl = None
                                        self.out_mcast_pkts_unctrl = None
                                        self.out_mcast_pkts_ctrl = None
                                        self.out_bcast_pkts_unctrl = None
                                        self.out_bcast_pkts_ctrl = None
                                        self.out_rx_drop_pkts_unctrl = None
                                        self.out_rx_drop_pkts_ctrl = None
                                        self.out_rx_err_pkts_unctrl = None
                                        self.out_rx_err_pkts_ctrl = None
                                        self.out_drop_pkts_class = None
                                        self.out_drop_pkts_data = None
                                        self._segment_path = lambda: "tx-interface-macsec-stats"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats.TxInterfaceMacsecStats, ['transform_error_pkts', 'out_pkt_ctrl', 'out_pkts_untagged', 'out_octets_unctrl', 'out_octets_ctrl', 'out_octets_common', 'out_ucast_pkts_unctrl', 'out_ucast_pkts_ctrl', 'out_mcast_pkts_unctrl', 'out_mcast_pkts_ctrl', 'out_bcast_pkts_unctrl', 'out_bcast_pkts_ctrl', 'out_rx_drop_pkts_unctrl', 'out_rx_drop_pkts_ctrl', 'out_rx_err_pkts_unctrl', 'out_rx_err_pkts_ctrl', 'out_drop_pkts_class', 'out_drop_pkts_data'], name, value)


                                class RxInterfaceMacsecStats(Entity):
                                    """
                                    Rx interface Macsec Stats
                                    
                                    .. attribute:: transform_error_pkts
                                    
                                    	counter to count internal errors in the MACSec core
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkt_ctrl
                                    
                                    	ingress packet that is classified as control packet
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkt_no_tag
                                    
                                    	ingress packet untagged & validateFrames is strict
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkts_untagged
                                    
                                    	ingress packet untagged & validateFrames is  !strict
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkt_bad_tag
                                    
                                    	ingress frames received with an invalid MACSec tag or ICV                                       added with next one gives InPktsSCIMiss
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkt_no_sci
                                    
                                    	correctly tagged ingress frames for which no valid SC found &                                 validateFrames is strict
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkts_unknown_sci
                                    
                                    	correctly tagged ingress frames for which no valid SC found &                                 validateFrames is !strict
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_pkts_tagged_ctrl
                                    
                                    	ingress packets that are control or KaY packets
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_octets_unctrl
                                    
                                    	Octets rx on uncontrolled port
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_octets_ctrl
                                    
                                    	Octets rx on controlled port
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_ucast_pkts_unctrl
                                    
                                    	Unicast pkts rx on uncontrolled port
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_ucast_pkts_ctrl
                                    
                                    	Unicast pkts rx on controlled port
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_mcast_pkts_unctrl
                                    
                                    	Multicast pkts rx on uncontrolled port
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_mcast_pkts_ctrl
                                    
                                    	Multicast pkts rx on controlled port
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_bcast_pkts_unctrl
                                    
                                    	Broadcast pkts rx on uncontrolled port
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_bcast_pkts_ctrl
                                    
                                    	Broadcast pkts rx on controlled port
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_rx_drop_pkts_unctrl
                                    
                                    	Control pkts dropped due to overrun
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_rx_drop_pkts_ctrl
                                    
                                    	Data pkts dropped due to overrun
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_rx_error_pkts_unctrl
                                    
                                    	Control pkts error\-terminated due to overrun
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_rx_error_pkts_ctrl
                                    
                                    	Data pkts error\-terminated due to overrun
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_drop_pkts_class
                                    
                                    	Packets dropped due to overflow in classification pipeline
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: in_drop_pkts_data
                                    
                                    	Packets dropped due to overflow in processing pipeline
                                    	**type**\: int
                                    
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
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('transform_error_pkts', (YLeaf(YType.uint64, 'transform-error-pkts'), ['int'])),
                                            ('in_pkt_ctrl', (YLeaf(YType.uint64, 'in-pkt-ctrl'), ['int'])),
                                            ('in_pkt_no_tag', (YLeaf(YType.uint64, 'in-pkt-no-tag'), ['int'])),
                                            ('in_pkts_untagged', (YLeaf(YType.uint64, 'in-pkts-untagged'), ['int'])),
                                            ('in_pkt_bad_tag', (YLeaf(YType.uint64, 'in-pkt-bad-tag'), ['int'])),
                                            ('in_pkt_no_sci', (YLeaf(YType.uint64, 'in-pkt-no-sci'), ['int'])),
                                            ('in_pkts_unknown_sci', (YLeaf(YType.uint64, 'in-pkts-unknown-sci'), ['int'])),
                                            ('in_pkts_tagged_ctrl', (YLeaf(YType.uint64, 'in-pkts-tagged-ctrl'), ['int'])),
                                            ('in_octets_unctrl', (YLeaf(YType.uint64, 'in-octets-unctrl'), ['int'])),
                                            ('in_octets_ctrl', (YLeaf(YType.uint64, 'in-octets-ctrl'), ['int'])),
                                            ('in_ucast_pkts_unctrl', (YLeaf(YType.uint64, 'in-ucast-pkts-unctrl'), ['int'])),
                                            ('in_ucast_pkts_ctrl', (YLeaf(YType.uint64, 'in-ucast-pkts-ctrl'), ['int'])),
                                            ('in_mcast_pkts_unctrl', (YLeaf(YType.uint64, 'in-mcast-pkts-unctrl'), ['int'])),
                                            ('in_mcast_pkts_ctrl', (YLeaf(YType.uint64, 'in-mcast-pkts-ctrl'), ['int'])),
                                            ('in_bcast_pkts_unctrl', (YLeaf(YType.uint64, 'in-bcast-pkts-unctrl'), ['int'])),
                                            ('in_bcast_pkts_ctrl', (YLeaf(YType.uint64, 'in-bcast-pkts-ctrl'), ['int'])),
                                            ('in_rx_drop_pkts_unctrl', (YLeaf(YType.uint64, 'in-rx-drop-pkts-unctrl'), ['int'])),
                                            ('in_rx_drop_pkts_ctrl', (YLeaf(YType.uint64, 'in-rx-drop-pkts-ctrl'), ['int'])),
                                            ('in_rx_error_pkts_unctrl', (YLeaf(YType.uint64, 'in-rx-error-pkts-unctrl'), ['int'])),
                                            ('in_rx_error_pkts_ctrl', (YLeaf(YType.uint64, 'in-rx-error-pkts-ctrl'), ['int'])),
                                            ('in_drop_pkts_class', (YLeaf(YType.uint64, 'in-drop-pkts-class'), ['int'])),
                                            ('in_drop_pkts_data', (YLeaf(YType.uint64, 'in-drop-pkts-data'), ['int'])),
                                        ])
                                        self.transform_error_pkts = None
                                        self.in_pkt_ctrl = None
                                        self.in_pkt_no_tag = None
                                        self.in_pkts_untagged = None
                                        self.in_pkt_bad_tag = None
                                        self.in_pkt_no_sci = None
                                        self.in_pkts_unknown_sci = None
                                        self.in_pkts_tagged_ctrl = None
                                        self.in_octets_unctrl = None
                                        self.in_octets_ctrl = None
                                        self.in_ucast_pkts_unctrl = None
                                        self.in_ucast_pkts_ctrl = None
                                        self.in_mcast_pkts_unctrl = None
                                        self.in_mcast_pkts_ctrl = None
                                        self.in_bcast_pkts_unctrl = None
                                        self.in_bcast_pkts_ctrl = None
                                        self.in_rx_drop_pkts_unctrl = None
                                        self.in_rx_drop_pkts_ctrl = None
                                        self.in_rx_error_pkts_unctrl = None
                                        self.in_rx_error_pkts_ctrl = None
                                        self.in_drop_pkts_class = None
                                        self.in_drop_pkts_data = None
                                        self._segment_path = lambda: "rx-interface-macsec-stats"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats.RxInterfaceMacsecStats, ['transform_error_pkts', 'in_pkt_ctrl', 'in_pkt_no_tag', 'in_pkts_untagged', 'in_pkt_bad_tag', 'in_pkt_no_sci', 'in_pkts_unknown_sci', 'in_pkts_tagged_ctrl', 'in_octets_unctrl', 'in_octets_ctrl', 'in_ucast_pkts_unctrl', 'in_ucast_pkts_ctrl', 'in_mcast_pkts_unctrl', 'in_mcast_pkts_ctrl', 'in_bcast_pkts_unctrl', 'in_bcast_pkts_ctrl', 'in_rx_drop_pkts_unctrl', 'in_rx_drop_pkts_ctrl', 'in_rx_error_pkts_unctrl', 'in_rx_error_pkts_ctrl', 'in_drop_pkts_class', 'in_drop_pkts_data'], name, value)


                                class TxPortStats(Entity):
                                    """
                                    Port level TX Stats
                                    
                                    .. attribute:: multi_flow_match
                                    
                                    	Pkts matching multiple flow entries
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: parser_dropped
                                    
                                    	Pkts dropped by header parser as invalid
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: flow_miss
                                    
                                    	Pkts matching none of flow entries
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: pkts_ctrl
                                    
                                    	Control pkts forwarded
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: pkts_data
                                    
                                    	Data pkts forwarded
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: pkts_dropped
                                    
                                    	Pkts dropped by classifier
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: pkts_err_in
                                    
                                    	Pkts received with an error indication
                                    	**type**\: int
                                    
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
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('multi_flow_match', (YLeaf(YType.uint64, 'multi-flow-match'), ['int'])),
                                            ('parser_dropped', (YLeaf(YType.uint64, 'parser-dropped'), ['int'])),
                                            ('flow_miss', (YLeaf(YType.uint64, 'flow-miss'), ['int'])),
                                            ('pkts_ctrl', (YLeaf(YType.uint64, 'pkts-ctrl'), ['int'])),
                                            ('pkts_data', (YLeaf(YType.uint64, 'pkts-data'), ['int'])),
                                            ('pkts_dropped', (YLeaf(YType.uint64, 'pkts-dropped'), ['int'])),
                                            ('pkts_err_in', (YLeaf(YType.uint64, 'pkts-err-in'), ['int'])),
                                        ])
                                        self.multi_flow_match = None
                                        self.parser_dropped = None
                                        self.flow_miss = None
                                        self.pkts_ctrl = None
                                        self.pkts_data = None
                                        self.pkts_dropped = None
                                        self.pkts_err_in = None
                                        self._segment_path = lambda: "tx-port-stats"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats.TxPortStats, ['multi_flow_match', 'parser_dropped', 'flow_miss', 'pkts_ctrl', 'pkts_data', 'pkts_dropped', 'pkts_err_in'], name, value)


                                class RxPortStats(Entity):
                                    """
                                    Port level RX Stats
                                    
                                    .. attribute:: multi_flow_match
                                    
                                    	Pkts matching multiple flow entries
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: parser_dropped
                                    
                                    	Pkts dropped by header parser as invalid
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: flow_miss
                                    
                                    	Pkts matching none of flow entries
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: pkts_ctrl
                                    
                                    	Control pkts forwarded
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: pkts_data
                                    
                                    	Data pkts forwarded
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: pkts_dropped
                                    
                                    	Pkts dropped by classifier
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: pkts_err_in
                                    
                                    	Pkts received with an error indication
                                    	**type**\: int
                                    
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
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('multi_flow_match', (YLeaf(YType.uint64, 'multi-flow-match'), ['int'])),
                                            ('parser_dropped', (YLeaf(YType.uint64, 'parser-dropped'), ['int'])),
                                            ('flow_miss', (YLeaf(YType.uint64, 'flow-miss'), ['int'])),
                                            ('pkts_ctrl', (YLeaf(YType.uint64, 'pkts-ctrl'), ['int'])),
                                            ('pkts_data', (YLeaf(YType.uint64, 'pkts-data'), ['int'])),
                                            ('pkts_dropped', (YLeaf(YType.uint64, 'pkts-dropped'), ['int'])),
                                            ('pkts_err_in', (YLeaf(YType.uint64, 'pkts-err-in'), ['int'])),
                                        ])
                                        self.multi_flow_match = None
                                        self.parser_dropped = None
                                        self.flow_miss = None
                                        self.pkts_ctrl = None
                                        self.pkts_data = None
                                        self.pkts_dropped = None
                                        self.pkts_err_in = None
                                        self._segment_path = lambda: "rx-port-stats"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MacsecPlatform.Nodes.Node.Interfaces.Interface.SwStatistics.Ext.Es200Stats.RxPortStats, ['multi_flow_match', 'parser_dropped', 'flow_miss', 'pkts_ctrl', 'pkts_data', 'pkts_dropped', 'pkts_err_in'], name, value)

    def clone_ptr(self):
        self._top_entity = MacsecPlatform()
        return self._top_entity

