""" Cisco_IOS_XR_ncs1k_mxp_headless_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ncs1k\-mxp\-headless package operational data.

This module contains definitions
for the following management objects\:
  headless\-func\-data\: Information related to headless
    functionality

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class MxpOtnPrbsStatus(Enum):
    """
    MxpOtnPrbsStatus (Enum Class)

    Mxp otn prbs status

    .. data:: locked = 0

    	Locked

    .. data:: not_locked = 1

    	Not Locked

    .. data:: not_applicable = 2

    	Not Applicable

    .. data:: locked_with_errors = 3

    	Locked With Errors

    """

    locked = Enum.YLeaf(0, "locked")

    not_locked = Enum.YLeaf(1, "not-locked")

    not_applicable = Enum.YLeaf(2, "not-applicable")

    locked_with_errors = Enum.YLeaf(3, "locked-with-errors")



class HeadlessFuncData(Entity):
    """
    Information related to headless functionality
    
    .. attribute:: otn_port_names
    
    	OTN Statistics collected during last headless operation
    	**type**\:  :py:class:`OtnPortNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_headless_oper.HeadlessFuncData.OtnPortNames>`
    
    .. attribute:: ethernet_port_names
    
    	Ethernet Statistics collected during last headless operation
    	**type**\:  :py:class:`EthernetPortNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_headless_oper.HeadlessFuncData.EthernetPortNames>`
    
    

    """

    _prefix = 'ncs1k-mxp-headless-oper'
    _revision = '2017-03-30'

    def __init__(self):
        super(HeadlessFuncData, self).__init__()
        self._top_entity = None

        self.yang_name = "headless-func-data"
        self.yang_parent_name = "Cisco-IOS-XR-ncs1k-mxp-headless-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("otn-port-names", ("otn_port_names", HeadlessFuncData.OtnPortNames)), ("ethernet-port-names", ("ethernet_port_names", HeadlessFuncData.EthernetPortNames))])
        self._leafs = OrderedDict()

        self.otn_port_names = HeadlessFuncData.OtnPortNames()
        self.otn_port_names.parent = self
        self._children_name_map["otn_port_names"] = "otn-port-names"

        self.ethernet_port_names = HeadlessFuncData.EthernetPortNames()
        self.ethernet_port_names.parent = self
        self._children_name_map["ethernet_port_names"] = "ethernet-port-names"
        self._segment_path = lambda: "Cisco-IOS-XR-ncs1k-mxp-headless-oper:headless-func-data"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(HeadlessFuncData, [], name, value)


    class OtnPortNames(Entity):
        """
        OTN Statistics collected during last headless
        operation
        
        .. attribute:: otn_port_name
        
        	port Name
        	**type**\: list of  		 :py:class:`OtnPortName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_headless_oper.HeadlessFuncData.OtnPortNames.OtnPortName>`
        
        

        """

        _prefix = 'ncs1k-mxp-headless-oper'
        _revision = '2017-03-30'

        def __init__(self):
            super(HeadlessFuncData.OtnPortNames, self).__init__()

            self.yang_name = "otn-port-names"
            self.yang_parent_name = "headless-func-data"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("otn-port-name", ("otn_port_name", HeadlessFuncData.OtnPortNames.OtnPortName))])
            self._leafs = OrderedDict()

            self.otn_port_name = YList(self)
            self._segment_path = lambda: "otn-port-names"
            self._absolute_path = lambda: "Cisco-IOS-XR-ncs1k-mxp-headless-oper:headless-func-data/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(HeadlessFuncData.OtnPortNames, [], name, value)


        class OtnPortName(Entity):
            """
            port Name
            
            .. attribute:: name  (key)
            
            	Port name
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
            
            .. attribute:: otn_statistics
            
            	OTN statistics
            	**type**\:  :py:class:`OtnStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_headless_oper.HeadlessFuncData.OtnPortNames.OtnPortName.OtnStatistics>`
            
            .. attribute:: prbs_statistics
            
            	PRBS Statistics
            	**type**\:  :py:class:`PrbsStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_headless_oper.HeadlessFuncData.OtnPortNames.OtnPortName.PrbsStatistics>`
            
            .. attribute:: started_stateful
            
            	Started Stateful
            	**type**\: bool
            
            .. attribute:: headless_start_time
            
            	Headless Start Time
            	**type**\: str
            
            	**length:** 0..64
            
            .. attribute:: headless_end_time
            
            	Headless End Time
            	**type**\: str
            
            	**length:** 0..64
            
            

            """

            _prefix = 'ncs1k-mxp-headless-oper'
            _revision = '2017-03-30'

            def __init__(self):
                super(HeadlessFuncData.OtnPortNames.OtnPortName, self).__init__()

                self.yang_name = "otn-port-name"
                self.yang_parent_name = "otn-port-names"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['name']
                self._child_classes = OrderedDict([("otn-statistics", ("otn_statistics", HeadlessFuncData.OtnPortNames.OtnPortName.OtnStatistics)), ("prbs-statistics", ("prbs_statistics", HeadlessFuncData.OtnPortNames.OtnPortName.PrbsStatistics))])
                self._leafs = OrderedDict([
                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                    ('started_stateful', (YLeaf(YType.boolean, 'started-stateful'), ['bool'])),
                    ('headless_start_time', (YLeaf(YType.str, 'headless-start-time'), ['str'])),
                    ('headless_end_time', (YLeaf(YType.str, 'headless-end-time'), ['str'])),
                ])
                self.name = None
                self.started_stateful = None
                self.headless_start_time = None
                self.headless_end_time = None

                self.otn_statistics = HeadlessFuncData.OtnPortNames.OtnPortName.OtnStatistics()
                self.otn_statistics.parent = self
                self._children_name_map["otn_statistics"] = "otn-statistics"

                self.prbs_statistics = HeadlessFuncData.OtnPortNames.OtnPortName.PrbsStatistics()
                self.prbs_statistics.parent = self
                self._children_name_map["prbs_statistics"] = "prbs-statistics"
                self._segment_path = lambda: "otn-port-name" + "[name='" + str(self.name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ncs1k-mxp-headless-oper:headless-func-data/otn-port-names/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(HeadlessFuncData.OtnPortNames.OtnPortName, ['name', 'started_stateful', 'headless_start_time', 'headless_end_time'], name, value)


            class OtnStatistics(Entity):
                """
                OTN statistics
                
                .. attribute:: sm_bip
                
                	SmBip
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: sm_bei
                
                	SmBei
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: fec_ec
                
                	FecEc
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: fec_uc
                
                	FecUc
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'ncs1k-mxp-headless-oper'
                _revision = '2017-03-30'

                def __init__(self):
                    super(HeadlessFuncData.OtnPortNames.OtnPortName.OtnStatistics, self).__init__()

                    self.yang_name = "otn-statistics"
                    self.yang_parent_name = "otn-port-name"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('sm_bip', (YLeaf(YType.uint64, 'sm-bip'), ['int'])),
                        ('sm_bei', (YLeaf(YType.uint64, 'sm-bei'), ['int'])),
                        ('fec_ec', (YLeaf(YType.uint64, 'fec-ec'), ['int'])),
                        ('fec_uc', (YLeaf(YType.uint64, 'fec-uc'), ['int'])),
                    ])
                    self.sm_bip = None
                    self.sm_bei = None
                    self.fec_ec = None
                    self.fec_uc = None
                    self._segment_path = lambda: "otn-statistics"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(HeadlessFuncData.OtnPortNames.OtnPortName.OtnStatistics, ['sm_bip', 'sm_bei', 'fec_ec', 'fec_uc'], name, value)


            class PrbsStatistics(Entity):
                """
                PRBS Statistics
                
                .. attribute:: ebc
                
                	EBC
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: sync_status
                
                	SyncStatus
                	**type**\:  :py:class:`MxpOtnPrbsStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_headless_oper.MxpOtnPrbsStatus>`
                
                

                """

                _prefix = 'ncs1k-mxp-headless-oper'
                _revision = '2017-03-30'

                def __init__(self):
                    super(HeadlessFuncData.OtnPortNames.OtnPortName.PrbsStatistics, self).__init__()

                    self.yang_name = "prbs-statistics"
                    self.yang_parent_name = "otn-port-name"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('ebc', (YLeaf(YType.uint64, 'ebc'), ['int'])),
                        ('sync_status', (YLeaf(YType.enumeration, 'sync-status'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_headless_oper', 'MxpOtnPrbsStatus', '')])),
                    ])
                    self.ebc = None
                    self.sync_status = None
                    self._segment_path = lambda: "prbs-statistics"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(HeadlessFuncData.OtnPortNames.OtnPortName.PrbsStatistics, ['ebc', 'sync_status'], name, value)


    class EthernetPortNames(Entity):
        """
        Ethernet Statistics collected during last
        headless operation
        
        .. attribute:: ethernet_port_name
        
        	Port Name
        	**type**\: list of  		 :py:class:`EthernetPortName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_headless_oper.HeadlessFuncData.EthernetPortNames.EthernetPortName>`
        
        

        """

        _prefix = 'ncs1k-mxp-headless-oper'
        _revision = '2017-03-30'

        def __init__(self):
            super(HeadlessFuncData.EthernetPortNames, self).__init__()

            self.yang_name = "ethernet-port-names"
            self.yang_parent_name = "headless-func-data"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ethernet-port-name", ("ethernet_port_name", HeadlessFuncData.EthernetPortNames.EthernetPortName))])
            self._leafs = OrderedDict()

            self.ethernet_port_name = YList(self)
            self._segment_path = lambda: "ethernet-port-names"
            self._absolute_path = lambda: "Cisco-IOS-XR-ncs1k-mxp-headless-oper:headless-func-data/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(HeadlessFuncData.EthernetPortNames, [], name, value)


        class EthernetPortName(Entity):
            """
            Port Name
            
            .. attribute:: name  (key)
            
            	Port name
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
            
            .. attribute:: ether_statistics
            
            	Ether Statistics
            	**type**\:  :py:class:`EtherStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_headless_oper.HeadlessFuncData.EthernetPortNames.EthernetPortName.EtherStatistics>`
            
            .. attribute:: started_stateful
            
            	Started Stateful
            	**type**\: bool
            
            .. attribute:: headless_start_time
            
            	Headless Start Time
            	**type**\: str
            
            	**length:** 0..64
            
            .. attribute:: headless_end_time
            
            	Headless End Time
            	**type**\: str
            
            	**length:** 0..64
            
            

            """

            _prefix = 'ncs1k-mxp-headless-oper'
            _revision = '2017-03-30'

            def __init__(self):
                super(HeadlessFuncData.EthernetPortNames.EthernetPortName, self).__init__()

                self.yang_name = "ethernet-port-name"
                self.yang_parent_name = "ethernet-port-names"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['name']
                self._child_classes = OrderedDict([("ether-statistics", ("ether_statistics", HeadlessFuncData.EthernetPortNames.EthernetPortName.EtherStatistics))])
                self._leafs = OrderedDict([
                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                    ('started_stateful', (YLeaf(YType.boolean, 'started-stateful'), ['bool'])),
                    ('headless_start_time', (YLeaf(YType.str, 'headless-start-time'), ['str'])),
                    ('headless_end_time', (YLeaf(YType.str, 'headless-end-time'), ['str'])),
                ])
                self.name = None
                self.started_stateful = None
                self.headless_start_time = None
                self.headless_end_time = None

                self.ether_statistics = HeadlessFuncData.EthernetPortNames.EthernetPortName.EtherStatistics()
                self.ether_statistics.parent = self
                self._children_name_map["ether_statistics"] = "ether-statistics"
                self._segment_path = lambda: "ethernet-port-name" + "[name='" + str(self.name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ncs1k-mxp-headless-oper:headless-func-data/ethernet-port-names/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(HeadlessFuncData.EthernetPortNames.EthernetPortName, ['name', 'started_stateful', 'headless_start_time', 'headless_end_time'], name, value)


            class EtherStatistics(Entity):
                """
                Ether Statistics
                
                .. attribute:: rx_pkts_over_sized
                
                	RxPktsOverSized
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rx_pkts_bad_fcs
                
                	RxPktsBadFcs
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rx_error_jabbers
                
                	RxErrorJabbers
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rx_pkts_multicast
                
                	RxPktsMulticast
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rx_pkts_broadcast
                
                	RxPktsBroadcast
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rx_pkts_under_sized
                
                	RxPktsUnderSized
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rx_packets
                
                	RxPackets
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rx_total_bytes
                
                	RxTotalBytes
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rx_bytes_good
                
                	RxBytesGood
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rx_pkts_good
                
                	RxPktsGood
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: tx_bytes_good
                
                	TxBytesGood
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: tx_pkts_good
                
                	TxPktsGood
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rx_recv_fragments
                
                	RxRecvFragments
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rx_pkts64_bytes
                
                	RxPkts64Bytes
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rx_pkts65_to127_bytes
                
                	RxPkts65To127Bytes
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rx_pkts128to255_bytes
                
                	RxPkts128to255Bytes
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rx_pkts256_to511_bytes
                
                	RxPkts256To511Bytes
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rx_pkts512_to1023_bytes
                
                	RxPkts512To1023Bytes
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rx_pkts1024_to1518_bytes
                
                	RxPkts1024To1518Bytes
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rx_pkts_unicast
                
                	RxPktsUnicast
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: tx_packets
                
                	TxPackets
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: tx_total_bytes
                
                	TxTotalBytes
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: tx_pkts_under_sized
                
                	TxPktsUnderSized
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: tx_pkts_over_sized
                
                	TxPktsOverSized
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: tx_fragments
                
                	TxFragments
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: tx_jabber
                
                	TxJabber
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: tx_bad_fcs
                
                	TxBadFCS
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rx_pkt_drop
                
                	RxPktDrop
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rx_pause
                
                	RxPause
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: tx_pause
                
                	TxPause
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rx_lldp_pkt
                
                	RxLldpPkt
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rx8021q_pkt
                
                	Rx8021QPkt
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'ncs1k-mxp-headless-oper'
                _revision = '2017-03-30'

                def __init__(self):
                    super(HeadlessFuncData.EthernetPortNames.EthernetPortName.EtherStatistics, self).__init__()

                    self.yang_name = "ether-statistics"
                    self.yang_parent_name = "ethernet-port-name"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('rx_pkts_over_sized', (YLeaf(YType.uint64, 'rx-pkts-over-sized'), ['int'])),
                        ('rx_pkts_bad_fcs', (YLeaf(YType.uint64, 'rx-pkts-bad-fcs'), ['int'])),
                        ('rx_error_jabbers', (YLeaf(YType.uint64, 'rx-error-jabbers'), ['int'])),
                        ('rx_pkts_multicast', (YLeaf(YType.uint64, 'rx-pkts-multicast'), ['int'])),
                        ('rx_pkts_broadcast', (YLeaf(YType.uint64, 'rx-pkts-broadcast'), ['int'])),
                        ('rx_pkts_under_sized', (YLeaf(YType.uint64, 'rx-pkts-under-sized'), ['int'])),
                        ('rx_packets', (YLeaf(YType.uint64, 'rx-packets'), ['int'])),
                        ('rx_total_bytes', (YLeaf(YType.uint64, 'rx-total-bytes'), ['int'])),
                        ('rx_bytes_good', (YLeaf(YType.uint64, 'rx-bytes-good'), ['int'])),
                        ('rx_pkts_good', (YLeaf(YType.uint64, 'rx-pkts-good'), ['int'])),
                        ('tx_bytes_good', (YLeaf(YType.uint64, 'tx-bytes-good'), ['int'])),
                        ('tx_pkts_good', (YLeaf(YType.uint64, 'tx-pkts-good'), ['int'])),
                        ('rx_recv_fragments', (YLeaf(YType.uint64, 'rx-recv-fragments'), ['int'])),
                        ('rx_pkts64_bytes', (YLeaf(YType.uint64, 'rx-pkts64-bytes'), ['int'])),
                        ('rx_pkts65_to127_bytes', (YLeaf(YType.uint64, 'rx-pkts65-to127-bytes'), ['int'])),
                        ('rx_pkts128to255_bytes', (YLeaf(YType.uint64, 'rx-pkts128to255-bytes'), ['int'])),
                        ('rx_pkts256_to511_bytes', (YLeaf(YType.uint64, 'rx-pkts256-to511-bytes'), ['int'])),
                        ('rx_pkts512_to1023_bytes', (YLeaf(YType.uint64, 'rx-pkts512-to1023-bytes'), ['int'])),
                        ('rx_pkts1024_to1518_bytes', (YLeaf(YType.uint64, 'rx-pkts1024-to1518-bytes'), ['int'])),
                        ('rx_pkts_unicast', (YLeaf(YType.uint64, 'rx-pkts-unicast'), ['int'])),
                        ('tx_packets', (YLeaf(YType.uint64, 'tx-packets'), ['int'])),
                        ('tx_total_bytes', (YLeaf(YType.uint64, 'tx-total-bytes'), ['int'])),
                        ('tx_pkts_under_sized', (YLeaf(YType.uint64, 'tx-pkts-under-sized'), ['int'])),
                        ('tx_pkts_over_sized', (YLeaf(YType.uint64, 'tx-pkts-over-sized'), ['int'])),
                        ('tx_fragments', (YLeaf(YType.uint64, 'tx-fragments'), ['int'])),
                        ('tx_jabber', (YLeaf(YType.uint64, 'tx-jabber'), ['int'])),
                        ('tx_bad_fcs', (YLeaf(YType.uint64, 'tx-bad-fcs'), ['int'])),
                        ('rx_pkt_drop', (YLeaf(YType.uint64, 'rx-pkt-drop'), ['int'])),
                        ('rx_pause', (YLeaf(YType.uint64, 'rx-pause'), ['int'])),
                        ('tx_pause', (YLeaf(YType.uint64, 'tx-pause'), ['int'])),
                        ('rx_lldp_pkt', (YLeaf(YType.uint64, 'rx-lldp-pkt'), ['int'])),
                        ('rx8021q_pkt', (YLeaf(YType.uint64, 'rx8021q-pkt'), ['int'])),
                    ])
                    self.rx_pkts_over_sized = None
                    self.rx_pkts_bad_fcs = None
                    self.rx_error_jabbers = None
                    self.rx_pkts_multicast = None
                    self.rx_pkts_broadcast = None
                    self.rx_pkts_under_sized = None
                    self.rx_packets = None
                    self.rx_total_bytes = None
                    self.rx_bytes_good = None
                    self.rx_pkts_good = None
                    self.tx_bytes_good = None
                    self.tx_pkts_good = None
                    self.rx_recv_fragments = None
                    self.rx_pkts64_bytes = None
                    self.rx_pkts65_to127_bytes = None
                    self.rx_pkts128to255_bytes = None
                    self.rx_pkts256_to511_bytes = None
                    self.rx_pkts512_to1023_bytes = None
                    self.rx_pkts1024_to1518_bytes = None
                    self.rx_pkts_unicast = None
                    self.tx_packets = None
                    self.tx_total_bytes = None
                    self.tx_pkts_under_sized = None
                    self.tx_pkts_over_sized = None
                    self.tx_fragments = None
                    self.tx_jabber = None
                    self.tx_bad_fcs = None
                    self.rx_pkt_drop = None
                    self.rx_pause = None
                    self.tx_pause = None
                    self.rx_lldp_pkt = None
                    self.rx8021q_pkt = None
                    self._segment_path = lambda: "ether-statistics"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(HeadlessFuncData.EthernetPortNames.EthernetPortName.EtherStatistics, ['rx_pkts_over_sized', 'rx_pkts_bad_fcs', 'rx_error_jabbers', 'rx_pkts_multicast', 'rx_pkts_broadcast', 'rx_pkts_under_sized', 'rx_packets', 'rx_total_bytes', 'rx_bytes_good', 'rx_pkts_good', 'tx_bytes_good', 'tx_pkts_good', 'rx_recv_fragments', 'rx_pkts64_bytes', 'rx_pkts65_to127_bytes', 'rx_pkts128to255_bytes', 'rx_pkts256_to511_bytes', 'rx_pkts512_to1023_bytes', 'rx_pkts1024_to1518_bytes', 'rx_pkts_unicast', 'tx_packets', 'tx_total_bytes', 'tx_pkts_under_sized', 'tx_pkts_over_sized', 'tx_fragments', 'tx_jabber', 'tx_bad_fcs', 'rx_pkt_drop', 'rx_pause', 'tx_pause', 'rx_lldp_pkt', 'rx8021q_pkt'], name, value)

    def clone_ptr(self):
        self._top_entity = HeadlessFuncData()
        return self._top_entity

