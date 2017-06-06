""" Cisco_IOS_XR_ncs1k_mxp_headless_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ncs1k\-mxp\-headless package operational data.

This module contains definitions
for the following management objects\:
  headless\-func\-data\: Information related to headless
    functionality

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class HeadlessFuncData(object):
    """
    Information related to headless functionality
    
    .. attribute:: ethernet_port_names
    
    	Ethernet Statistics collected during last headless operation
    	**type**\:   :py:class:`EthernetPortNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_headless_oper.HeadlessFuncData.EthernetPortNames>`
    
    .. attribute:: otn_port_names
    
    	OTN Statistics collected during last headless operation
    	**type**\:   :py:class:`OtnPortNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_headless_oper.HeadlessFuncData.OtnPortNames>`
    
    

    """

    _prefix = 'ncs1k-mxp-headless-oper'
    _revision = '2016-09-13'

    def __init__(self):
        self.ethernet_port_names = HeadlessFuncData.EthernetPortNames()
        self.ethernet_port_names.parent = self
        self.otn_port_names = HeadlessFuncData.OtnPortNames()
        self.otn_port_names.parent = self


    class OtnPortNames(object):
        """
        OTN Statistics collected during last headless
        operation
        
        .. attribute:: otn_port_name
        
        	port Name
        	**type**\: list of    :py:class:`OtnPortName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_headless_oper.HeadlessFuncData.OtnPortNames.OtnPortName>`
        
        

        """

        _prefix = 'ncs1k-mxp-headless-oper'
        _revision = '2016-09-13'

        def __init__(self):
            self.parent = None
            self.otn_port_name = YList()
            self.otn_port_name.parent = self
            self.otn_port_name.name = 'otn_port_name'


        class OtnPortName(object):
            """
            port Name
            
            .. attribute:: name  <key>
            
            	Port name
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: headless_end_time
            
            	Headless End Time
            	**type**\:  str
            
            	**length:** 0..64
            
            .. attribute:: headless_start_time
            
            	Headless Start Time
            	**type**\:  str
            
            	**length:** 0..64
            
            .. attribute:: otn_statistics
            
            	OTN statistics
            	**type**\:   :py:class:`OtnStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_headless_oper.HeadlessFuncData.OtnPortNames.OtnPortName.OtnStatistics>`
            
            .. attribute:: started_stateful
            
            	Started Stateful
            	**type**\:  bool
            
            

            """

            _prefix = 'ncs1k-mxp-headless-oper'
            _revision = '2016-09-13'

            def __init__(self):
                self.parent = None
                self.name = None
                self.headless_end_time = None
                self.headless_start_time = None
                self.otn_statistics = HeadlessFuncData.OtnPortNames.OtnPortName.OtnStatistics()
                self.otn_statistics.parent = self
                self.started_stateful = None


            class OtnStatistics(object):
                """
                OTN statistics
                
                .. attribute:: fec_ec
                
                	FecEc
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: fec_uc
                
                	FecUc
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: sm_bei
                
                	SmBei
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: sm_bip
                
                	SmBip
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'ncs1k-mxp-headless-oper'
                _revision = '2016-09-13'

                def __init__(self):
                    self.parent = None
                    self.fec_ec = None
                    self.fec_uc = None
                    self.sm_bei = None
                    self.sm_bip = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ncs1k-mxp-headless-oper:otn-statistics'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.fec_ec is not None:
                        return True

                    if self.fec_uc is not None:
                        return True

                    if self.sm_bei is not None:
                        return True

                    if self.sm_bip is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs1k_mxp_headless_oper as meta
                    return meta._meta_table['HeadlessFuncData.OtnPortNames.OtnPortName.OtnStatistics']['meta_info']

            @property
            def _common_path(self):
                if self.name is None:
                    raise YPYModelError('Key property name is None')

                return '/Cisco-IOS-XR-ncs1k-mxp-headless-oper:headless-func-data/Cisco-IOS-XR-ncs1k-mxp-headless-oper:otn-port-names/Cisco-IOS-XR-ncs1k-mxp-headless-oper:otn-port-name[Cisco-IOS-XR-ncs1k-mxp-headless-oper:name = ' + str(self.name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.name is not None:
                    return True

                if self.headless_end_time is not None:
                    return True

                if self.headless_start_time is not None:
                    return True

                if self.otn_statistics is not None and self.otn_statistics._has_data():
                    return True

                if self.started_stateful is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs1k_mxp_headless_oper as meta
                return meta._meta_table['HeadlessFuncData.OtnPortNames.OtnPortName']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ncs1k-mxp-headless-oper:headless-func-data/Cisco-IOS-XR-ncs1k-mxp-headless-oper:otn-port-names'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.otn_port_name is not None:
                for child_ref in self.otn_port_name:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs1k_mxp_headless_oper as meta
            return meta._meta_table['HeadlessFuncData.OtnPortNames']['meta_info']


    class EthernetPortNames(object):
        """
        Ethernet Statistics collected during last
        headless operation
        
        .. attribute:: ethernet_port_name
        
        	Port Name
        	**type**\: list of    :py:class:`EthernetPortName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_headless_oper.HeadlessFuncData.EthernetPortNames.EthernetPortName>`
        
        

        """

        _prefix = 'ncs1k-mxp-headless-oper'
        _revision = '2016-09-13'

        def __init__(self):
            self.parent = None
            self.ethernet_port_name = YList()
            self.ethernet_port_name.parent = self
            self.ethernet_port_name.name = 'ethernet_port_name'


        class EthernetPortName(object):
            """
            Port Name
            
            .. attribute:: name  <key>
            
            	Port name
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: ether_statistics
            
            	Ether Statistics
            	**type**\:   :py:class:`EtherStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_headless_oper.HeadlessFuncData.EthernetPortNames.EthernetPortName.EtherStatistics>`
            
            .. attribute:: headless_end_time
            
            	Headless End Time
            	**type**\:  str
            
            	**length:** 0..64
            
            .. attribute:: headless_start_time
            
            	Headless Start Time
            	**type**\:  str
            
            	**length:** 0..64
            
            .. attribute:: started_stateful
            
            	Started Stateful
            	**type**\:  bool
            
            

            """

            _prefix = 'ncs1k-mxp-headless-oper'
            _revision = '2016-09-13'

            def __init__(self):
                self.parent = None
                self.name = None
                self.ether_statistics = HeadlessFuncData.EthernetPortNames.EthernetPortName.EtherStatistics()
                self.ether_statistics.parent = self
                self.headless_end_time = None
                self.headless_start_time = None
                self.started_stateful = None


            class EtherStatistics(object):
                """
                Ether Statistics
                
                .. attribute:: rx8021q_pkt
                
                	Rx8021QPkt
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rx_bytes_good
                
                	RxBytesGood
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rx_error_jabbers
                
                	RxErrorJabbers
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rx_lldp_pkt
                
                	RxLldpPkt
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rx_packets
                
                	RxPackets
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rx_pause
                
                	RxPause
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rx_pkt_drop
                
                	RxPktDrop
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rx_pkts1024_to1518_bytes
                
                	RxPkts1024To1518Bytes
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rx_pkts128to255_bytes
                
                	RxPkts128to255Bytes
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rx_pkts256_to511_bytes
                
                	RxPkts256To511Bytes
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rx_pkts512_to1023_bytes
                
                	RxPkts512To1023Bytes
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rx_pkts64_bytes
                
                	RxPkts64Bytes
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rx_pkts65_to127_bytes
                
                	RxPkts65To127Bytes
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rx_pkts_bad_fcs
                
                	RxPktsBadFcs
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rx_pkts_broadcast
                
                	RxPktsBroadcast
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rx_pkts_good
                
                	RxPktsGood
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rx_pkts_multicast
                
                	RxPktsMulticast
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rx_pkts_over_sized
                
                	RxPktsOverSized
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rx_pkts_under_sized
                
                	RxPktsUnderSized
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rx_pkts_unicast
                
                	RxPktsUnicast
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rx_recv_fragments
                
                	RxRecvFragments
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rx_total_bytes
                
                	RxTotalBytes
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: tx_bad_fcs
                
                	TxBadFCS
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: tx_bytes_good
                
                	TxBytesGood
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: tx_fragments
                
                	TxFragments
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: tx_jabber
                
                	TxJabber
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: tx_packets
                
                	TxPackets
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: tx_pause
                
                	TxPause
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: tx_pkts_good
                
                	TxPktsGood
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: tx_pkts_over_sized
                
                	TxPktsOverSized
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: tx_pkts_under_sized
                
                	TxPktsUnderSized
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: tx_total_bytes
                
                	TxTotalBytes
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'ncs1k-mxp-headless-oper'
                _revision = '2016-09-13'

                def __init__(self):
                    self.parent = None
                    self.rx8021q_pkt = None
                    self.rx_bytes_good = None
                    self.rx_error_jabbers = None
                    self.rx_lldp_pkt = None
                    self.rx_packets = None
                    self.rx_pause = None
                    self.rx_pkt_drop = None
                    self.rx_pkts1024_to1518_bytes = None
                    self.rx_pkts128to255_bytes = None
                    self.rx_pkts256_to511_bytes = None
                    self.rx_pkts512_to1023_bytes = None
                    self.rx_pkts64_bytes = None
                    self.rx_pkts65_to127_bytes = None
                    self.rx_pkts_bad_fcs = None
                    self.rx_pkts_broadcast = None
                    self.rx_pkts_good = None
                    self.rx_pkts_multicast = None
                    self.rx_pkts_over_sized = None
                    self.rx_pkts_under_sized = None
                    self.rx_pkts_unicast = None
                    self.rx_recv_fragments = None
                    self.rx_total_bytes = None
                    self.tx_bad_fcs = None
                    self.tx_bytes_good = None
                    self.tx_fragments = None
                    self.tx_jabber = None
                    self.tx_packets = None
                    self.tx_pause = None
                    self.tx_pkts_good = None
                    self.tx_pkts_over_sized = None
                    self.tx_pkts_under_sized = None
                    self.tx_total_bytes = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ncs1k-mxp-headless-oper:ether-statistics'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.rx8021q_pkt is not None:
                        return True

                    if self.rx_bytes_good is not None:
                        return True

                    if self.rx_error_jabbers is not None:
                        return True

                    if self.rx_lldp_pkt is not None:
                        return True

                    if self.rx_packets is not None:
                        return True

                    if self.rx_pause is not None:
                        return True

                    if self.rx_pkt_drop is not None:
                        return True

                    if self.rx_pkts1024_to1518_bytes is not None:
                        return True

                    if self.rx_pkts128to255_bytes is not None:
                        return True

                    if self.rx_pkts256_to511_bytes is not None:
                        return True

                    if self.rx_pkts512_to1023_bytes is not None:
                        return True

                    if self.rx_pkts64_bytes is not None:
                        return True

                    if self.rx_pkts65_to127_bytes is not None:
                        return True

                    if self.rx_pkts_bad_fcs is not None:
                        return True

                    if self.rx_pkts_broadcast is not None:
                        return True

                    if self.rx_pkts_good is not None:
                        return True

                    if self.rx_pkts_multicast is not None:
                        return True

                    if self.rx_pkts_over_sized is not None:
                        return True

                    if self.rx_pkts_under_sized is not None:
                        return True

                    if self.rx_pkts_unicast is not None:
                        return True

                    if self.rx_recv_fragments is not None:
                        return True

                    if self.rx_total_bytes is not None:
                        return True

                    if self.tx_bad_fcs is not None:
                        return True

                    if self.tx_bytes_good is not None:
                        return True

                    if self.tx_fragments is not None:
                        return True

                    if self.tx_jabber is not None:
                        return True

                    if self.tx_packets is not None:
                        return True

                    if self.tx_pause is not None:
                        return True

                    if self.tx_pkts_good is not None:
                        return True

                    if self.tx_pkts_over_sized is not None:
                        return True

                    if self.tx_pkts_under_sized is not None:
                        return True

                    if self.tx_total_bytes is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs1k_mxp_headless_oper as meta
                    return meta._meta_table['HeadlessFuncData.EthernetPortNames.EthernetPortName.EtherStatistics']['meta_info']

            @property
            def _common_path(self):
                if self.name is None:
                    raise YPYModelError('Key property name is None')

                return '/Cisco-IOS-XR-ncs1k-mxp-headless-oper:headless-func-data/Cisco-IOS-XR-ncs1k-mxp-headless-oper:ethernet-port-names/Cisco-IOS-XR-ncs1k-mxp-headless-oper:ethernet-port-name[Cisco-IOS-XR-ncs1k-mxp-headless-oper:name = ' + str(self.name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.name is not None:
                    return True

                if self.ether_statistics is not None and self.ether_statistics._has_data():
                    return True

                if self.headless_end_time is not None:
                    return True

                if self.headless_start_time is not None:
                    return True

                if self.started_stateful is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs1k_mxp_headless_oper as meta
                return meta._meta_table['HeadlessFuncData.EthernetPortNames.EthernetPortName']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ncs1k-mxp-headless-oper:headless-func-data/Cisco-IOS-XR-ncs1k-mxp-headless-oper:ethernet-port-names'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ethernet_port_name is not None:
                for child_ref in self.ethernet_port_name:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs1k_mxp_headless_oper as meta
            return meta._meta_table['HeadlessFuncData.EthernetPortNames']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ncs1k-mxp-headless-oper:headless-func-data'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.ethernet_port_names is not None and self.ethernet_port_names._has_data():
            return True

        if self.otn_port_names is not None and self.otn_port_names._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs1k_mxp_headless_oper as meta
        return meta._meta_table['HeadlessFuncData']['meta_info']


