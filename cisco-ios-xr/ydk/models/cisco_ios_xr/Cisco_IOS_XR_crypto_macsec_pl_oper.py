""" Cisco_IOS_XR_crypto_macsec_pl_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR crypto\-macsec\-pl package operational data.

This module contains definitions
for the following management objects\:
  macsec\: MACSec operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class Macsec(object):
    """
    MACSec operational data
    
    .. attribute:: nodes
    
    	NodeTable for all the nodes
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes>`
    
    

    """

    _prefix = 'crypto-macsec-pl-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.nodes = Macsec.Nodes()
        self.nodes.parent = self


    class Nodes(object):
        """
        NodeTable for all the nodes
        
        .. attribute:: node
        
        	Node where macsec interfaces exist
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node>`
        
        

        """

        _prefix = 'crypto-macsec-pl-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.node = YList()
            self.node.parent = self
            self.node.name = 'node'


        class Node(object):
            """
            Node where macsec interfaces exist
            
            .. attribute:: node_name  <key>
            
            	Node
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: interfaces
            
            	Table of Interfaces
            	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces>`
            
            

            """

            _prefix = 'crypto-macsec-pl-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.node_name = None
                self.interfaces = Macsec.Nodes.Node.Interfaces()
                self.interfaces.parent = self


            class Interfaces(object):
                """
                Table of Interfaces
                
                .. attribute:: interface
                
                	Interface Where Macsec is configured
                	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface>`
                
                

                """

                _prefix = 'crypto-macsec-pl-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.interface = YList()
                    self.interface.parent = self
                    self.interface.name = 'interface'


                class Interface(object):
                    """
                    Interface Where Macsec is configured
                    
                    .. attribute:: name  <key>
                    
                    	Value
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: hw_flow_s
                    
                    	Table of Hardware Flows
                    	**type**\:   :py:class:`HwFlowS <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.HwFlowS>`
                    
                    .. attribute:: hw_sas
                    
                    	Table of Hardware SAs
                    	**type**\:   :py:class:`HwSas <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.HwSas>`
                    
                    .. attribute:: hw_statistics
                    
                    	The Hardware Statistics
                    	**type**\:   :py:class:`HwStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.HwStatistics>`
                    
                    .. attribute:: sw_flow_s
                    
                    	Table of sofware Flows
                    	**type**\:   :py:class:`SwFlowS <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.SwFlowS>`
                    
                    .. attribute:: sw_sas
                    
                    	Table of Software SAs
                    	**type**\:   :py:class:`SwSas <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.SwSas>`
                    
                    .. attribute:: sw_statistics
                    
                    	The Software Statistics
                    	**type**\:   :py:class:`SwStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.SwStatistics>`
                    
                    

                    """

                    _prefix = 'crypto-macsec-pl-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.name = None
                        self.hw_flow_s = Macsec.Nodes.Node.Interfaces.Interface.HwFlowS()
                        self.hw_flow_s.parent = self
                        self.hw_sas = Macsec.Nodes.Node.Interfaces.Interface.HwSas()
                        self.hw_sas.parent = self
                        self.hw_statistics = Macsec.Nodes.Node.Interfaces.Interface.HwStatistics()
                        self.hw_statistics.parent = self
                        self.sw_flow_s = Macsec.Nodes.Node.Interfaces.Interface.SwFlowS()
                        self.sw_flow_s.parent = self
                        self.sw_sas = Macsec.Nodes.Node.Interfaces.Interface.SwSas()
                        self.sw_sas.parent = self
                        self.sw_statistics = Macsec.Nodes.Node.Interfaces.Interface.SwStatistics()
                        self.sw_statistics.parent = self


                    class HwStatistics(object):
                        """
                        The Hardware Statistics
                        
                        .. attribute:: es200_stats
                        
                        	ES200 Stats
                        	**type**\:   :py:class:`Es200Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.Es200Stats>`
                        
                        .. attribute:: hw_type
                        
                        	Hardware Type
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: msfpga_stats
                        
                        	MSFPGA Stats
                        	**type**\:   :py:class:`MsfpgaStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.MsfpgaStats>`
                        
                        .. attribute:: xlfpga_stats
                        
                        	XLFPGA Stats
                        	**type**\:   :py:class:`XlfpgaStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.XlfpgaStats>`
                        
                        

                        """

                        _prefix = 'crypto-macsec-pl-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.es200_stats = Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.Es200Stats()
                            self.es200_stats.parent = self
                            self.hw_type = None
                            self.msfpga_stats = Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.MsfpgaStats()
                            self.msfpga_stats.parent = self
                            self.xlfpga_stats = Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.XlfpgaStats()
                            self.xlfpga_stats.parent = self


                        class MsfpgaStats(object):
                            """
                            MSFPGA Stats
                            
                            .. attribute:: rx_interface_macsec_stats
                            
                            	Rx interface Macsec Stats
                            	**type**\:   :py:class:`RxInterfaceMacsecStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.MsfpgaStats.RxInterfaceMacsecStats>`
                            
                            .. attribute:: rx_sa_stats
                            
                            	Rx SA Stats
                            	**type**\:   :py:class:`RxSaStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.MsfpgaStats.RxSaStats>`
                            
                            .. attribute:: tx_interface_macsec_stats
                            
                            	Tx interface Macsec Stats
                            	**type**\:   :py:class:`TxInterfaceMacsecStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.MsfpgaStats.TxInterfaceMacsecStats>`
                            
                            .. attribute:: tx_sa_stats
                            
                            	Tx SA Stats
                            	**type**\:   :py:class:`TxSaStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.MsfpgaStats.TxSaStats>`
                            
                            

                            """

                            _prefix = 'crypto-macsec-pl-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.rx_interface_macsec_stats = Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.MsfpgaStats.RxInterfaceMacsecStats()
                                self.rx_interface_macsec_stats.parent = self
                                self.rx_sa_stats = Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.MsfpgaStats.RxSaStats()
                                self.rx_sa_stats.parent = self
                                self.tx_interface_macsec_stats = Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.MsfpgaStats.TxInterfaceMacsecStats()
                                self.tx_interface_macsec_stats.parent = self
                                self.tx_sa_stats = Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.MsfpgaStats.TxSaStats()
                                self.tx_sa_stats.parent = self


                            class TxSaStats(object):
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
                                    self.parent = None
                                    self.out_octets_encrypted = None
                                    self.out_octets_protected = None
                                    self.out_pkts_encrypted = None
                                    self.out_pkts_protected = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-pl-oper:tx-sa-stats'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.out_octets_encrypted is not None:
                                        return True

                                    if self.out_octets_protected is not None:
                                        return True

                                    if self.out_pkts_encrypted is not None:
                                        return True

                                    if self.out_pkts_protected is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_pl_oper as meta
                                    return meta._meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.MsfpgaStats.TxSaStats']['meta_info']


                            class RxSaStats(object):
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
                                    self.parent = None
                                    self.in_octets_decrypted = None
                                    self.in_octets_validated = None
                                    self.in_pkts_delayed = None
                                    self.in_pkts_invalid = None
                                    self.in_pkts_late = None
                                    self.in_pkts_not_using_sa = None
                                    self.in_pkts_not_valid = None
                                    self.in_pkts_ok = None
                                    self.in_pkts_unchecked = None
                                    self.in_pkts_unused_sa = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-pl-oper:rx-sa-stats'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.in_octets_decrypted is not None:
                                        return True

                                    if self.in_octets_validated is not None:
                                        return True

                                    if self.in_pkts_delayed is not None:
                                        return True

                                    if self.in_pkts_invalid is not None:
                                        return True

                                    if self.in_pkts_late is not None:
                                        return True

                                    if self.in_pkts_not_using_sa is not None:
                                        return True

                                    if self.in_pkts_not_valid is not None:
                                        return True

                                    if self.in_pkts_ok is not None:
                                        return True

                                    if self.in_pkts_unchecked is not None:
                                        return True

                                    if self.in_pkts_unused_sa is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_pl_oper as meta
                                    return meta._meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.MsfpgaStats.RxSaStats']['meta_info']


                            class TxInterfaceMacsecStats(object):
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
                                    self.parent = None
                                    self.out_pkt_too_long = None
                                    self.out_pkt_uncontrolled = None
                                    self.out_pkt_untagged = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-pl-oper:tx-interface-macsec-stats'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.out_pkt_too_long is not None:
                                        return True

                                    if self.out_pkt_uncontrolled is not None:
                                        return True

                                    if self.out_pkt_untagged is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_pl_oper as meta
                                    return meta._meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.MsfpgaStats.TxInterfaceMacsecStats']['meta_info']


                            class RxInterfaceMacsecStats(object):
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
                                    self.parent = None
                                    self.in_pkt_bad_tag = None
                                    self.in_pkt_no_sci = None
                                    self.in_pkt_notag = None
                                    self.in_pkt_overrun = None
                                    self.in_pkt_tagged = None
                                    self.in_pkt_uncontrolled = None
                                    self.in_pkt_unknown_sci = None
                                    self.in_pkt_untagged = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-pl-oper:rx-interface-macsec-stats'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.in_pkt_bad_tag is not None:
                                        return True

                                    if self.in_pkt_no_sci is not None:
                                        return True

                                    if self.in_pkt_notag is not None:
                                        return True

                                    if self.in_pkt_overrun is not None:
                                        return True

                                    if self.in_pkt_tagged is not None:
                                        return True

                                    if self.in_pkt_uncontrolled is not None:
                                        return True

                                    if self.in_pkt_unknown_sci is not None:
                                        return True

                                    if self.in_pkt_untagged is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_pl_oper as meta
                                    return meta._meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.MsfpgaStats.RxInterfaceMacsecStats']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-pl-oper:msfpga-stats'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.rx_interface_macsec_stats is not None and self.rx_interface_macsec_stats._has_data():
                                    return True

                                if self.rx_sa_stats is not None and self.rx_sa_stats._has_data():
                                    return True

                                if self.tx_interface_macsec_stats is not None and self.tx_interface_macsec_stats._has_data():
                                    return True

                                if self.tx_sa_stats is not None and self.tx_sa_stats._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_pl_oper as meta
                                return meta._meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.MsfpgaStats']['meta_info']


                        class XlfpgaStats(object):
                            """
                            XLFPGA Stats
                            
                            .. attribute:: macsec_rx_stats
                            
                            	Rx SC and SA Level Stats
                            	**type**\:   :py:class:`MacsecRxStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.XlfpgaStats.MacsecRxStats>`
                            
                            .. attribute:: macsec_tx_stats
                            
                            	Tx SC and SA Level Stats
                            	**type**\:   :py:class:`MacsecTxStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.XlfpgaStats.MacsecTxStats>`
                            
                            

                            """

                            _prefix = 'crypto-macsec-pl-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.macsec_rx_stats = Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.XlfpgaStats.MacsecRxStats()
                                self.macsec_rx_stats.parent = self
                                self.macsec_tx_stats = Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.XlfpgaStats.MacsecTxStats()
                                self.macsec_tx_stats.parent = self


                            class MacsecTxStats(object):
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
                                    self.parent = None
                                    self.current_an = None
                                    self.sa_encrypted_pkts = None
                                    self.sc_encrypted_octets = None
                                    self.sc_encrypted_pkts = None
                                    self.sc_overrun_pkts = None
                                    self.sc_toolong_pkts = None
                                    self.sc_untagged_pkts = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-pl-oper:macsec-tx-stats'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.current_an is not None:
                                        return True

                                    if self.sa_encrypted_pkts is not None:
                                        return True

                                    if self.sc_encrypted_octets is not None:
                                        return True

                                    if self.sc_encrypted_pkts is not None:
                                        return True

                                    if self.sc_overrun_pkts is not None:
                                        return True

                                    if self.sc_toolong_pkts is not None:
                                        return True

                                    if self.sc_untagged_pkts is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_pl_oper as meta
                                    return meta._meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.XlfpgaStats.MacsecTxStats']['meta_info']


                            class MacsecRxStats(object):
                                """
                                Rx SC and SA Level Stats
                                
                                .. attribute:: rx_sa_stat
                                
                                	Rx SA Level Stats
                                	**type**\: list of    :py:class:`RxSaStat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.XlfpgaStats.MacsecRxStats.RxSaStat>`
                                
                                .. attribute:: sc_bad_tag_pkts
                                
                                	Rx Bad Tag Packets
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
                                    self.parent = None
                                    self.rx_sa_stat = YList()
                                    self.rx_sa_stat.parent = self
                                    self.rx_sa_stat.name = 'rx_sa_stat'
                                    self.sc_bad_tag_pkts = None
                                    self.sc_decrypted_octets = None
                                    self.sc_delayed_pkts = None
                                    self.sc_invalid_pkts = None
                                    self.sc_late_pkts = None
                                    self.sc_no_sci_pkts = None
                                    self.sc_no_tag_pkts = None
                                    self.sc_not_using_pkts = None
                                    self.sc_not_valid_pkts = None
                                    self.sc_ok_pkts = None
                                    self.sc_overrun_pkts = None
                                    self.sc_unchecked_pkts = None
                                    self.sc_unknown_sci_pkts = None
                                    self.sc_untagged_pkts = None
                                    self.sc_unused_pkts = None


                                class RxSaStat(object):
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
                                        self.parent = None
                                        self.an = None
                                        self.sa_invalid_pkts = None
                                        self.sa_not_using_pkts = None
                                        self.sa_not_valid_pkts = None
                                        self.sa_ok_pkts = None
                                        self.sa_unused_pkts = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-pl-oper:rx-sa-stat'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.an is not None:
                                            return True

                                        if self.sa_invalid_pkts is not None:
                                            return True

                                        if self.sa_not_using_pkts is not None:
                                            return True

                                        if self.sa_not_valid_pkts is not None:
                                            return True

                                        if self.sa_ok_pkts is not None:
                                            return True

                                        if self.sa_unused_pkts is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_pl_oper as meta
                                        return meta._meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.XlfpgaStats.MacsecRxStats.RxSaStat']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-pl-oper:macsec-rx-stats'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.rx_sa_stat is not None:
                                        for child_ref in self.rx_sa_stat:
                                            if child_ref._has_data():
                                                return True

                                    if self.sc_bad_tag_pkts is not None:
                                        return True

                                    if self.sc_decrypted_octets is not None:
                                        return True

                                    if self.sc_delayed_pkts is not None:
                                        return True

                                    if self.sc_invalid_pkts is not None:
                                        return True

                                    if self.sc_late_pkts is not None:
                                        return True

                                    if self.sc_no_sci_pkts is not None:
                                        return True

                                    if self.sc_no_tag_pkts is not None:
                                        return True

                                    if self.sc_not_using_pkts is not None:
                                        return True

                                    if self.sc_not_valid_pkts is not None:
                                        return True

                                    if self.sc_ok_pkts is not None:
                                        return True

                                    if self.sc_overrun_pkts is not None:
                                        return True

                                    if self.sc_unchecked_pkts is not None:
                                        return True

                                    if self.sc_unknown_sci_pkts is not None:
                                        return True

                                    if self.sc_untagged_pkts is not None:
                                        return True

                                    if self.sc_unused_pkts is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_pl_oper as meta
                                    return meta._meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.XlfpgaStats.MacsecRxStats']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-pl-oper:xlfpga-stats'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.macsec_rx_stats is not None and self.macsec_rx_stats._has_data():
                                    return True

                                if self.macsec_tx_stats is not None and self.macsec_tx_stats._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_pl_oper as meta
                                return meta._meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.XlfpgaStats']['meta_info']


                        class Es200Stats(object):
                            """
                            ES200 Stats
                            
                            .. attribute:: rx_interface_macsec_stats
                            
                            	Rx interface Macsec Stats
                            	**type**\:   :py:class:`RxInterfaceMacsecStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.Es200Stats.RxInterfaceMacsecStats>`
                            
                            .. attribute:: rx_sa_stats
                            
                            	Rx SA Stats
                            	**type**\:   :py:class:`RxSaStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.Es200Stats.RxSaStats>`
                            
                            .. attribute:: tx_interface_macsec_stats
                            
                            	Tx interface Macsec Stats
                            	**type**\:   :py:class:`TxInterfaceMacsecStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.Es200Stats.TxInterfaceMacsecStats>`
                            
                            .. attribute:: tx_sa_stats
                            
                            	Tx SA Stats
                            	**type**\:   :py:class:`TxSaStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.Es200Stats.TxSaStats>`
                            
                            

                            """

                            _prefix = 'crypto-macsec-pl-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.rx_interface_macsec_stats = Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.Es200Stats.RxInterfaceMacsecStats()
                                self.rx_interface_macsec_stats.parent = self
                                self.rx_sa_stats = Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.Es200Stats.RxSaStats()
                                self.rx_sa_stats.parent = self
                                self.tx_interface_macsec_stats = Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.Es200Stats.TxInterfaceMacsecStats()
                                self.tx_interface_macsec_stats.parent = self
                                self.tx_sa_stats = Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.Es200Stats.TxSaStats()
                                self.tx_sa_stats.parent = self


                            class TxSaStats(object):
                                """
                                Tx SA Stats
                                
                                .. attribute:: out_octets_encrypted_protected1
                                
                                	octets1 encrypted/protected ?
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: out_octets_encrypted_protected2
                                
                                	octets2 encrypted/protected ?
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: out_pkts_encrypted_protected
                                
                                	packets encrypted/protected
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: out_pkts_sa_not_in_use
                                
                                	packets coming on SA that is expired or otherwise not\-in\-use
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
                                    self.parent = None
                                    self.out_octets_encrypted_protected1 = None
                                    self.out_octets_encrypted_protected2 = None
                                    self.out_pkts_encrypted_protected = None
                                    self.out_pkts_sa_not_in_use = None
                                    self.out_pkts_too_long = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-pl-oper:tx-sa-stats'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.out_octets_encrypted_protected1 is not None:
                                        return True

                                    if self.out_octets_encrypted_protected2 is not None:
                                        return True

                                    if self.out_pkts_encrypted_protected is not None:
                                        return True

                                    if self.out_pkts_sa_not_in_use is not None:
                                        return True

                                    if self.out_pkts_too_long is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_pl_oper as meta
                                    return meta._meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.Es200Stats.TxSaStats']['meta_info']


                            class RxSaStats(object):
                                """
                                Rx SA Stats
                                
                                .. attribute:: in_octets_decrypted_validated1
                                
                                	octets1 decrypted/validated
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: in_octets_decrypted_validated2
                                
                                	octets2 decrypted/validated
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
                                
                                .. attribute:: in_pkts_sa_not_in_use
                                
                                	packets coming on SA that is
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
                                    self.parent = None
                                    self.in_octets_decrypted_validated1 = None
                                    self.in_octets_decrypted_validated2 = None
                                    self.in_octets_validated = None
                                    self.in_pkts_delayed = None
                                    self.in_pkts_invalid = None
                                    self.in_pkts_late = None
                                    self.in_pkts_not_using_sa = None
                                    self.in_pkts_not_valid = None
                                    self.in_pkts_ok = None
                                    self.in_pkts_sa_not_in_use = None
                                    self.in_pkts_unchecked = None
                                    self.in_pkts_unused_sa = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-pl-oper:rx-sa-stats'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.in_octets_decrypted_validated1 is not None:
                                        return True

                                    if self.in_octets_decrypted_validated2 is not None:
                                        return True

                                    if self.in_octets_validated is not None:
                                        return True

                                    if self.in_pkts_delayed is not None:
                                        return True

                                    if self.in_pkts_invalid is not None:
                                        return True

                                    if self.in_pkts_late is not None:
                                        return True

                                    if self.in_pkts_not_using_sa is not None:
                                        return True

                                    if self.in_pkts_not_valid is not None:
                                        return True

                                    if self.in_pkts_ok is not None:
                                        return True

                                    if self.in_pkts_sa_not_in_use is not None:
                                        return True

                                    if self.in_pkts_unchecked is not None:
                                        return True

                                    if self.in_pkts_unused_sa is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_pl_oper as meta
                                    return meta._meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.Es200Stats.RxSaStats']['meta_info']


                            class TxInterfaceMacsecStats(object):
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
                                    self.parent = None
                                    self.out_bcast_pkts_ctrl = None
                                    self.out_bcast_pkts_unctrl = None
                                    self.out_drop_pkts_class = None
                                    self.out_drop_pkts_data = None
                                    self.out_mcast_pkts_ctrl = None
                                    self.out_mcast_pkts_unctrl = None
                                    self.out_octets_common = None
                                    self.out_octets_ctrl = None
                                    self.out_octets_unctrl = None
                                    self.out_pkt_ctrl = None
                                    self.out_pkts_untagged = None
                                    self.out_rx_drop_pkts_ctrl = None
                                    self.out_rx_drop_pkts_unctrl = None
                                    self.out_rx_err_pkts_ctrl = None
                                    self.out_rx_err_pkts_unctrl = None
                                    self.out_ucast_pkts_ctrl = None
                                    self.out_ucast_pkts_unctrl = None
                                    self.transform_error_pkts = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-pl-oper:tx-interface-macsec-stats'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.out_bcast_pkts_ctrl is not None:
                                        return True

                                    if self.out_bcast_pkts_unctrl is not None:
                                        return True

                                    if self.out_drop_pkts_class is not None:
                                        return True

                                    if self.out_drop_pkts_data is not None:
                                        return True

                                    if self.out_mcast_pkts_ctrl is not None:
                                        return True

                                    if self.out_mcast_pkts_unctrl is not None:
                                        return True

                                    if self.out_octets_common is not None:
                                        return True

                                    if self.out_octets_ctrl is not None:
                                        return True

                                    if self.out_octets_unctrl is not None:
                                        return True

                                    if self.out_pkt_ctrl is not None:
                                        return True

                                    if self.out_pkts_untagged is not None:
                                        return True

                                    if self.out_rx_drop_pkts_ctrl is not None:
                                        return True

                                    if self.out_rx_drop_pkts_unctrl is not None:
                                        return True

                                    if self.out_rx_err_pkts_ctrl is not None:
                                        return True

                                    if self.out_rx_err_pkts_unctrl is not None:
                                        return True

                                    if self.out_ucast_pkts_ctrl is not None:
                                        return True

                                    if self.out_ucast_pkts_unctrl is not None:
                                        return True

                                    if self.transform_error_pkts is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_pl_oper as meta
                                    return meta._meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.Es200Stats.TxInterfaceMacsecStats']['meta_info']


                            class RxInterfaceMacsecStats(object):
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
                                
                                	correctly tagged ingress frames for which no valid SC found & \\;                              validateFrames is strict
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
                                    self.parent = None
                                    self.in_bcast_pkts_ctrl = None
                                    self.in_bcast_pkts_unctrl = None
                                    self.in_drop_pkts_class = None
                                    self.in_drop_pkts_data = None
                                    self.in_mcast_pkts_ctrl = None
                                    self.in_mcast_pkts_unctrl = None
                                    self.in_octets_ctrl = None
                                    self.in_octets_unctrl = None
                                    self.in_pkt_bad_tag = None
                                    self.in_pkt_ctrl = None
                                    self.in_pkt_no_sci = None
                                    self.in_pkt_no_tag = None
                                    self.in_pkts_tagged_ctrl = None
                                    self.in_pkts_unknown_sci = None
                                    self.in_pkts_untagged = None
                                    self.in_rx_drop_pkts_ctrl = None
                                    self.in_rx_drop_pkts_unctrl = None
                                    self.in_rx_error_pkts_ctrl = None
                                    self.in_rx_error_pkts_unctrl = None
                                    self.in_ucast_pkts_ctrl = None
                                    self.in_ucast_pkts_unctrl = None
                                    self.transform_error_pkts = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-pl-oper:rx-interface-macsec-stats'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.in_bcast_pkts_ctrl is not None:
                                        return True

                                    if self.in_bcast_pkts_unctrl is not None:
                                        return True

                                    if self.in_drop_pkts_class is not None:
                                        return True

                                    if self.in_drop_pkts_data is not None:
                                        return True

                                    if self.in_mcast_pkts_ctrl is not None:
                                        return True

                                    if self.in_mcast_pkts_unctrl is not None:
                                        return True

                                    if self.in_octets_ctrl is not None:
                                        return True

                                    if self.in_octets_unctrl is not None:
                                        return True

                                    if self.in_pkt_bad_tag is not None:
                                        return True

                                    if self.in_pkt_ctrl is not None:
                                        return True

                                    if self.in_pkt_no_sci is not None:
                                        return True

                                    if self.in_pkt_no_tag is not None:
                                        return True

                                    if self.in_pkts_tagged_ctrl is not None:
                                        return True

                                    if self.in_pkts_unknown_sci is not None:
                                        return True

                                    if self.in_pkts_untagged is not None:
                                        return True

                                    if self.in_rx_drop_pkts_ctrl is not None:
                                        return True

                                    if self.in_rx_drop_pkts_unctrl is not None:
                                        return True

                                    if self.in_rx_error_pkts_ctrl is not None:
                                        return True

                                    if self.in_rx_error_pkts_unctrl is not None:
                                        return True

                                    if self.in_ucast_pkts_ctrl is not None:
                                        return True

                                    if self.in_ucast_pkts_unctrl is not None:
                                        return True

                                    if self.transform_error_pkts is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_pl_oper as meta
                                    return meta._meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.Es200Stats.RxInterfaceMacsecStats']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-pl-oper:es200-stats'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.rx_interface_macsec_stats is not None and self.rx_interface_macsec_stats._has_data():
                                    return True

                                if self.rx_sa_stats is not None and self.rx_sa_stats._has_data():
                                    return True

                                if self.tx_interface_macsec_stats is not None and self.tx_interface_macsec_stats._has_data():
                                    return True

                                if self.tx_sa_stats is not None and self.tx_sa_stats._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_pl_oper as meta
                                return meta._meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.Es200Stats']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-pl-oper:hw-statistics'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.es200_stats is not None and self.es200_stats._has_data():
                                return True

                            if self.hw_type is not None:
                                return True

                            if self.msfpga_stats is not None and self.msfpga_stats._has_data():
                                return True

                            if self.xlfpga_stats is not None and self.xlfpga_stats._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_pl_oper as meta
                            return meta._meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwStatistics']['meta_info']


                    class SwSas(object):
                        """
                        Table of Software SAs
                        
                        .. attribute:: sw_sa
                        
                        	Software Security Association
                        	**type**\: list of    :py:class:`SwSa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa>`
                        
                        

                        """

                        _prefix = 'crypto-macsec-pl-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.sw_sa = YList()
                            self.sw_sa.parent = self
                            self.sw_sa.name = 'sw_sa'


                        class SwSa(object):
                            """
                            Software Security Association
                            
                            .. attribute:: sa_id  <key>
                            
                            	SA ID
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: es200_sa
                            
                            	ES200 SA Information
                            	**type**\:   :py:class:`Es200Sa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.Es200Sa>`
                            
                            .. attribute:: hw_type
                            
                            	Hardware Type
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: msfpga_sa
                            
                            	MSFPGA SA Information
                            	**type**\:   :py:class:`MsfpgaSa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.MsfpgaSa>`
                            
                            .. attribute:: xlfpga_sa
                            
                            	XLFPGA SA Information
                            	**type**\:   :py:class:`XlfpgaSa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.XlfpgaSa>`
                            
                            

                            """

                            _prefix = 'crypto-macsec-pl-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.sa_id = None
                                self.es200_sa = Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.Es200Sa()
                                self.es200_sa.parent = self
                                self.hw_type = None
                                self.msfpga_sa = Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.MsfpgaSa()
                                self.msfpga_sa.parent = self
                                self.xlfpga_sa = Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.XlfpgaSa()
                                self.xlfpga_sa.parent = self


                            class MsfpgaSa(object):
                                """
                                MSFPGA SA Information
                                
                                .. attribute:: rx_sa
                                
                                	Rx SA Details
                                	**type**\:   :py:class:`RxSa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.MsfpgaSa.RxSa>`
                                
                                .. attribute:: tx_sa
                                
                                	Tx SA Details
                                	**type**\:   :py:class:`TxSa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.MsfpgaSa.TxSa>`
                                
                                

                                """

                                _prefix = 'crypto-macsec-pl-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.rx_sa = Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.MsfpgaSa.RxSa()
                                    self.rx_sa.parent = self
                                    self.tx_sa = Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.MsfpgaSa.TxSa()
                                    self.tx_sa.parent = self


                                class TxSa(object):
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
                                        self.parent = None
                                        self.action = None
                                        self.an = None
                                        self.c_offset = None
                                        self.crypto_algo = None
                                        self.in_use = None
                                        self.is_egress = None
                                        self.key_len = None
                                        self.next_pn = None
                                        self.q_bit = None
                                        self.qq_bit = None
                                        self.sa_id = None
                                        self.sci = None
                                        self.valid = None
                                        self.xpn = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-pl-oper:tx-sa'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.action is not None:
                                            return True

                                        if self.an is not None:
                                            return True

                                        if self.c_offset is not None:
                                            return True

                                        if self.crypto_algo is not None:
                                            return True

                                        if self.in_use is not None:
                                            return True

                                        if self.is_egress is not None:
                                            return True

                                        if self.key_len is not None:
                                            return True

                                        if self.next_pn is not None:
                                            return True

                                        if self.q_bit is not None:
                                            return True

                                        if self.qq_bit is not None:
                                            return True

                                        if self.sa_id is not None:
                                            return True

                                        if self.sci is not None:
                                            return True

                                        if self.valid is not None:
                                            return True

                                        if self.xpn is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_pl_oper as meta
                                        return meta._meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.MsfpgaSa.TxSa']['meta_info']


                                class RxSa(object):
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
                                        self.parent = None
                                        self.action = None
                                        self.an = None
                                        self.c_offset = None
                                        self.crypto_algo = None
                                        self.in_use = None
                                        self.is_egress = None
                                        self.key_len = None
                                        self.next_pn = None
                                        self.q_bit = None
                                        self.qq_bit = None
                                        self.sa_id = None
                                        self.sci = None
                                        self.valid = None
                                        self.xpn = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-pl-oper:rx-sa'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.action is not None:
                                            return True

                                        if self.an is not None:
                                            return True

                                        if self.c_offset is not None:
                                            return True

                                        if self.crypto_algo is not None:
                                            return True

                                        if self.in_use is not None:
                                            return True

                                        if self.is_egress is not None:
                                            return True

                                        if self.key_len is not None:
                                            return True

                                        if self.next_pn is not None:
                                            return True

                                        if self.q_bit is not None:
                                            return True

                                        if self.qq_bit is not None:
                                            return True

                                        if self.sa_id is not None:
                                            return True

                                        if self.sci is not None:
                                            return True

                                        if self.valid is not None:
                                            return True

                                        if self.xpn is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_pl_oper as meta
                                        return meta._meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.MsfpgaSa.RxSa']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-pl-oper:msfpga-sa'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.rx_sa is not None and self.rx_sa._has_data():
                                        return True

                                    if self.tx_sa is not None and self.tx_sa._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_pl_oper as meta
                                    return meta._meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.MsfpgaSa']['meta_info']


                            class XlfpgaSa(object):
                                """
                                XLFPGA SA Information
                                
                                .. attribute:: rx_sa
                                
                                	Rx SA Details
                                	**type**\:   :py:class:`RxSa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.XlfpgaSa.RxSa>`
                                
                                .. attribute:: tx_sa
                                
                                	Tx SA Details
                                	**type**\:   :py:class:`TxSa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.XlfpgaSa.TxSa>`
                                
                                

                                """

                                _prefix = 'crypto-macsec-pl-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.rx_sa = Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.XlfpgaSa.RxSa()
                                    self.rx_sa.parent = self
                                    self.tx_sa = Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.XlfpgaSa.TxSa()
                                    self.tx_sa.parent = self


                                class TxSa(object):
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
                                        self.parent = None
                                        self.an = None
                                        self.cipher_suite = None
                                        self.confidentiality_offset = None
                                        self.crc_value = None
                                        self.current_packet_num = None
                                        self.fcs_err_cfg = None
                                        self.initial_packet_number = None
                                        self.max_packet_num = None
                                        self.protection_enable = None
                                        self.sectag_length = None
                                        self.secure_channel_id = None
                                        self.secure_mode = None
                                        self.ssci = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-pl-oper:tx-sa'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.an is not None:
                                            return True

                                        if self.cipher_suite is not None:
                                            return True

                                        if self.confidentiality_offset is not None:
                                            return True

                                        if self.crc_value is not None:
                                            return True

                                        if self.current_packet_num is not None:
                                            return True

                                        if self.fcs_err_cfg is not None:
                                            return True

                                        if self.initial_packet_number is not None:
                                            return True

                                        if self.max_packet_num is not None:
                                            return True

                                        if self.protection_enable is not None:
                                            return True

                                        if self.sectag_length is not None:
                                            return True

                                        if self.secure_channel_id is not None:
                                            return True

                                        if self.secure_mode is not None:
                                            return True

                                        if self.ssci is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_pl_oper as meta
                                        return meta._meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.XlfpgaSa.TxSa']['meta_info']


                                class RxSa(object):
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
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: max_packet_num
                                    
                                    	Max Packet Number
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: next_expected_packet_num
                                    
                                    	Next expected Packet Number
                                    	**type**\:  int
                                    
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
                                        self.parent = None
                                        self.an = None
                                        self.auth_err_cfg = None
                                        self.cipher_suite = None
                                        self.confidentiality_offset = None
                                        self.crc_value = YLeafList()
                                        self.crc_value.parent = self
                                        self.crc_value.name = 'crc_value'
                                        self.current_packet_num = None
                                        self.fcs_err_cfg = None
                                        self.lowest_acceptable_packet_num = None
                                        self.max_packet_num = None
                                        self.next_expected_packet_num = None
                                        self.num_an_in_use = None
                                        self.pkt_tagged_detected = None
                                        self.pkt_tagged_validated = None
                                        self.pkt_untagged_detected = None
                                        self.protection_enable = None
                                        self.recent_an = None
                                        self.replay_protect_mode = None
                                        self.replay_window = None
                                        self.secure_channel_id = None
                                        self.secure_mode = None
                                        self.ssci = YLeafList()
                                        self.ssci.parent = self
                                        self.ssci.name = 'ssci'
                                        self.validation_mode = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-pl-oper:rx-sa'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.an is not None:
                                            return True

                                        if self.auth_err_cfg is not None:
                                            return True

                                        if self.cipher_suite is not None:
                                            return True

                                        if self.confidentiality_offset is not None:
                                            return True

                                        if self.crc_value is not None:
                                            for child in self.crc_value:
                                                if child is not None:
                                                    return True

                                        if self.current_packet_num is not None:
                                            return True

                                        if self.fcs_err_cfg is not None:
                                            return True

                                        if self.lowest_acceptable_packet_num is not None:
                                            return True

                                        if self.max_packet_num is not None:
                                            return True

                                        if self.next_expected_packet_num is not None:
                                            return True

                                        if self.num_an_in_use is not None:
                                            return True

                                        if self.pkt_tagged_detected is not None:
                                            return True

                                        if self.pkt_tagged_validated is not None:
                                            return True

                                        if self.pkt_untagged_detected is not None:
                                            return True

                                        if self.protection_enable is not None:
                                            return True

                                        if self.recent_an is not None:
                                            return True

                                        if self.replay_protect_mode is not None:
                                            return True

                                        if self.replay_window is not None:
                                            return True

                                        if self.secure_channel_id is not None:
                                            return True

                                        if self.secure_mode is not None:
                                            return True

                                        if self.ssci is not None:
                                            for child in self.ssci:
                                                if child is not None:
                                                    return True

                                        if self.validation_mode is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_pl_oper as meta
                                        return meta._meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.XlfpgaSa.RxSa']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-pl-oper:xlfpga-sa'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.rx_sa is not None and self.rx_sa._has_data():
                                        return True

                                    if self.tx_sa is not None and self.tx_sa._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_pl_oper as meta
                                    return meta._meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.XlfpgaSa']['meta_info']


                            class Es200Sa(object):
                                """
                                ES200 SA Information
                                
                                .. attribute:: rx_sa
                                
                                	Rx SA Details
                                	**type**\:   :py:class:`RxSa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.Es200Sa.RxSa>`
                                
                                .. attribute:: tx_sa
                                
                                	Tx SA Details
                                	**type**\:   :py:class:`TxSa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.Es200Sa.TxSa>`
                                
                                

                                """

                                _prefix = 'crypto-macsec-pl-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.rx_sa = Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.Es200Sa.RxSa()
                                    self.rx_sa.parent = self
                                    self.tx_sa = Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.Es200Sa.TxSa()
                                    self.tx_sa.parent = self


                                class TxSa(object):
                                    """
                                    Tx SA Details
                                    
                                    .. attribute:: is_valid
                                    
                                    	Is structure valid
                                    	**type**\:  bool
                                    
                                    .. attribute:: out_octets_encrypted_protected1
                                    
                                    	octets1 encrypted/protected
                                    	**type**\:  int
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: out_octets_encrypted_protected2
                                    
                                    	octets2 encrypted/protected
                                    	**type**\:  int
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: out_pkts_encrypted_protected
                                    
                                    	packets encrypted/protected
                                    	**type**\:  int
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: out_pkts_sa_not_in_use
                                    
                                    	packets coming on SA that is
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
                                    	**type**\:   :py:class:`XformParams <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.Es200Sa.TxSa.XformParams>`
                                    
                                    

                                    """

                                    _prefix = 'crypto-macsec-pl-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.is_valid = None
                                        self.out_octets_encrypted_protected1 = None
                                        self.out_octets_encrypted_protected2 = None
                                        self.out_pkts_encrypted_protected = None
                                        self.out_pkts_sa_not_in_use = None
                                        self.out_pkts_too_long = None
                                        self.sa_id = None
                                        self.sc_no = None
                                        self.xform_params = Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.Es200Sa.TxSa.XformParams()
                                        self.xform_params.parent = self


                                    class XformParams(object):
                                        """
                                         Xform Params
                                        
                                        .. attribute:: aes_key_len
                                        
                                        	AES Key length
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: assoc_num
                                        
                                        	Association Number for egress
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: bgen_auth_key
                                        
                                        	TRUE to generate the authKey, so authKey in this struct not used                                  APM\_FALSE to use provided authKey
                                        	**type**\:  bool
                                        
                                        .. attribute:: crypt_algo
                                        
                                        	Cryptographic algo used
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
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
                                            self.parent = None
                                            self.aes_key_len = None
                                            self.assoc_num = None
                                            self.bgen_auth_key = None
                                            self.crypt_algo = None
                                            self.is_egress_tr = None
                                            self.is_seq_num64_bit = None
                                            self.replay_win_size = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-pl-oper:xform-params'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.aes_key_len is not None:
                                                return True

                                            if self.assoc_num is not None:
                                                return True

                                            if self.bgen_auth_key is not None:
                                                return True

                                            if self.crypt_algo is not None:
                                                return True

                                            if self.is_egress_tr is not None:
                                                return True

                                            if self.is_seq_num64_bit is not None:
                                                return True

                                            if self.replay_win_size is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_pl_oper as meta
                                            return meta._meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.Es200Sa.TxSa.XformParams']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-pl-oper:tx-sa'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_valid is not None:
                                            return True

                                        if self.out_octets_encrypted_protected1 is not None:
                                            return True

                                        if self.out_octets_encrypted_protected2 is not None:
                                            return True

                                        if self.out_pkts_encrypted_protected is not None:
                                            return True

                                        if self.out_pkts_sa_not_in_use is not None:
                                            return True

                                        if self.out_pkts_too_long is not None:
                                            return True

                                        if self.sa_id is not None:
                                            return True

                                        if self.sc_no is not None:
                                            return True

                                        if self.xform_params is not None and self.xform_params._has_data():
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_pl_oper as meta
                                        return meta._meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.Es200Sa.TxSa']['meta_info']


                                class RxSa(object):
                                    """
                                    Rx SA Details
                                    
                                    .. attribute:: in_octets_decrypted_validated1
                                    
                                    	octets1 decrypted/validated
                                    	**type**\:  int
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: in_octets_decrypted_validated2
                                    
                                    	octets2 decrypted/validated
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
                                    	**type**\:   :py:class:`XformParams <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.Es200Sa.RxSa.XformParams>`
                                    
                                    

                                    """

                                    _prefix = 'crypto-macsec-pl-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.in_octets_decrypted_validated1 = None
                                        self.in_octets_decrypted_validated2 = None
                                        self.in_octets_validated = None
                                        self.in_pkts_delayed = None
                                        self.in_pkts_invalid = None
                                        self.in_pkts_late = None
                                        self.in_pkts_not_using_sa = None
                                        self.in_pkts_not_valid = None
                                        self.in_pkts_ok = None
                                        self.in_pkts_unchecked = None
                                        self.in_pkts_unused_sa = None
                                        self.is_valid = None
                                        self.sa_id = None
                                        self.sc_no = None
                                        self.xform_params = Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.Es200Sa.RxSa.XformParams()
                                        self.xform_params.parent = self


                                    class XformParams(object):
                                        """
                                         Xform Params
                                        
                                        .. attribute:: aes_key_len
                                        
                                        	AES Key length
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: assoc_num
                                        
                                        	Association Number for egress
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: bgen_auth_key
                                        
                                        	TRUE to generate the authKey, so authKey in this struct not used                                  APM\_FALSE to use provided authKey
                                        	**type**\:  bool
                                        
                                        .. attribute:: crypt_algo
                                        
                                        	Cryptographic algo used
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
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
                                            self.parent = None
                                            self.aes_key_len = None
                                            self.assoc_num = None
                                            self.bgen_auth_key = None
                                            self.crypt_algo = None
                                            self.is_egress_tr = None
                                            self.is_seq_num64_bit = None
                                            self.replay_win_size = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-pl-oper:xform-params'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.aes_key_len is not None:
                                                return True

                                            if self.assoc_num is not None:
                                                return True

                                            if self.bgen_auth_key is not None:
                                                return True

                                            if self.crypt_algo is not None:
                                                return True

                                            if self.is_egress_tr is not None:
                                                return True

                                            if self.is_seq_num64_bit is not None:
                                                return True

                                            if self.replay_win_size is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_pl_oper as meta
                                            return meta._meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.Es200Sa.RxSa.XformParams']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-pl-oper:rx-sa'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.in_octets_decrypted_validated1 is not None:
                                            return True

                                        if self.in_octets_decrypted_validated2 is not None:
                                            return True

                                        if self.in_octets_validated is not None:
                                            return True

                                        if self.in_pkts_delayed is not None:
                                            return True

                                        if self.in_pkts_invalid is not None:
                                            return True

                                        if self.in_pkts_late is not None:
                                            return True

                                        if self.in_pkts_not_using_sa is not None:
                                            return True

                                        if self.in_pkts_not_valid is not None:
                                            return True

                                        if self.in_pkts_ok is not None:
                                            return True

                                        if self.in_pkts_unchecked is not None:
                                            return True

                                        if self.in_pkts_unused_sa is not None:
                                            return True

                                        if self.is_valid is not None:
                                            return True

                                        if self.sa_id is not None:
                                            return True

                                        if self.sc_no is not None:
                                            return True

                                        if self.xform_params is not None and self.xform_params._has_data():
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_pl_oper as meta
                                        return meta._meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.Es200Sa.RxSa']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-pl-oper:es200-sa'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.rx_sa is not None and self.rx_sa._has_data():
                                        return True

                                    if self.tx_sa is not None and self.tx_sa._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_pl_oper as meta
                                    return meta._meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.Es200Sa']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.sa_id is None:
                                    raise YPYModelError('Key property sa_id is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-pl-oper:sw-sa[Cisco-IOS-XR-crypto-macsec-pl-oper:sa-id = ' + str(self.sa_id) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.sa_id is not None:
                                    return True

                                if self.es200_sa is not None and self.es200_sa._has_data():
                                    return True

                                if self.hw_type is not None:
                                    return True

                                if self.msfpga_sa is not None and self.msfpga_sa._has_data():
                                    return True

                                if self.xlfpga_sa is not None and self.xlfpga_sa._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_pl_oper as meta
                                return meta._meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-pl-oper:sw-sas'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.sw_sa is not None:
                                for child_ref in self.sw_sa:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_pl_oper as meta
                            return meta._meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwSas']['meta_info']


                    class HwSas(object):
                        """
                        Table of Hardware SAs
                        
                        .. attribute:: hw_sa
                        
                        	Hardware Security Association
                        	**type**\: list of    :py:class:`HwSa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa>`
                        
                        

                        """

                        _prefix = 'crypto-macsec-pl-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.hw_sa = YList()
                            self.hw_sa.parent = self
                            self.hw_sa.name = 'hw_sa'


                        class HwSa(object):
                            """
                            Hardware Security Association
                            
                            .. attribute:: sa_id  <key>
                            
                            	SA ID
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: es200_sa
                            
                            	ES200 SA Information
                            	**type**\:   :py:class:`Es200Sa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Es200Sa>`
                            
                            .. attribute:: hw_type
                            
                            	Hardware Type
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: msfpga_sa
                            
                            	MSFPGA SA Information
                            	**type**\:   :py:class:`MsfpgaSa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.MsfpgaSa>`
                            
                            .. attribute:: xlfpga_sa
                            
                            	XLFPGA SA Information
                            	**type**\:   :py:class:`XlfpgaSa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.XlfpgaSa>`
                            
                            

                            """

                            _prefix = 'crypto-macsec-pl-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.sa_id = None
                                self.es200_sa = Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Es200Sa()
                                self.es200_sa.parent = self
                                self.hw_type = None
                                self.msfpga_sa = Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.MsfpgaSa()
                                self.msfpga_sa.parent = self
                                self.xlfpga_sa = Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.XlfpgaSa()
                                self.xlfpga_sa.parent = self


                            class MsfpgaSa(object):
                                """
                                MSFPGA SA Information
                                
                                .. attribute:: rx_sa
                                
                                	Rx SA Details
                                	**type**\:   :py:class:`RxSa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.MsfpgaSa.RxSa>`
                                
                                .. attribute:: tx_sa
                                
                                	Tx SA Details
                                	**type**\:   :py:class:`TxSa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.MsfpgaSa.TxSa>`
                                
                                

                                """

                                _prefix = 'crypto-macsec-pl-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.rx_sa = Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.MsfpgaSa.RxSa()
                                    self.rx_sa.parent = self
                                    self.tx_sa = Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.MsfpgaSa.TxSa()
                                    self.tx_sa.parent = self


                                class TxSa(object):
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
                                        self.parent = None
                                        self.action = None
                                        self.an = None
                                        self.c_offset = None
                                        self.crypto_algo = None
                                        self.in_use = None
                                        self.is_egress = None
                                        self.key_len = None
                                        self.next_pn = None
                                        self.q_bit = None
                                        self.qq_bit = None
                                        self.sa_id = None
                                        self.sci = None
                                        self.valid = None
                                        self.xpn = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-pl-oper:tx-sa'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.action is not None:
                                            return True

                                        if self.an is not None:
                                            return True

                                        if self.c_offset is not None:
                                            return True

                                        if self.crypto_algo is not None:
                                            return True

                                        if self.in_use is not None:
                                            return True

                                        if self.is_egress is not None:
                                            return True

                                        if self.key_len is not None:
                                            return True

                                        if self.next_pn is not None:
                                            return True

                                        if self.q_bit is not None:
                                            return True

                                        if self.qq_bit is not None:
                                            return True

                                        if self.sa_id is not None:
                                            return True

                                        if self.sci is not None:
                                            return True

                                        if self.valid is not None:
                                            return True

                                        if self.xpn is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_pl_oper as meta
                                        return meta._meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.MsfpgaSa.TxSa']['meta_info']


                                class RxSa(object):
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
                                        self.parent = None
                                        self.action = None
                                        self.an = None
                                        self.c_offset = None
                                        self.crypto_algo = None
                                        self.in_use = None
                                        self.is_egress = None
                                        self.key_len = None
                                        self.next_pn = None
                                        self.q_bit = None
                                        self.qq_bit = None
                                        self.sa_id = None
                                        self.sci = None
                                        self.valid = None
                                        self.xpn = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-pl-oper:rx-sa'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.action is not None:
                                            return True

                                        if self.an is not None:
                                            return True

                                        if self.c_offset is not None:
                                            return True

                                        if self.crypto_algo is not None:
                                            return True

                                        if self.in_use is not None:
                                            return True

                                        if self.is_egress is not None:
                                            return True

                                        if self.key_len is not None:
                                            return True

                                        if self.next_pn is not None:
                                            return True

                                        if self.q_bit is not None:
                                            return True

                                        if self.qq_bit is not None:
                                            return True

                                        if self.sa_id is not None:
                                            return True

                                        if self.sci is not None:
                                            return True

                                        if self.valid is not None:
                                            return True

                                        if self.xpn is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_pl_oper as meta
                                        return meta._meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.MsfpgaSa.RxSa']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-pl-oper:msfpga-sa'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.rx_sa is not None and self.rx_sa._has_data():
                                        return True

                                    if self.tx_sa is not None and self.tx_sa._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_pl_oper as meta
                                    return meta._meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.MsfpgaSa']['meta_info']


                            class XlfpgaSa(object):
                                """
                                XLFPGA SA Information
                                
                                .. attribute:: rx_sa
                                
                                	Rx SA Details
                                	**type**\:   :py:class:`RxSa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.XlfpgaSa.RxSa>`
                                
                                .. attribute:: tx_sa
                                
                                	Tx SA Details
                                	**type**\:   :py:class:`TxSa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.XlfpgaSa.TxSa>`
                                
                                

                                """

                                _prefix = 'crypto-macsec-pl-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.rx_sa = Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.XlfpgaSa.RxSa()
                                    self.rx_sa.parent = self
                                    self.tx_sa = Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.XlfpgaSa.TxSa()
                                    self.tx_sa.parent = self


                                class TxSa(object):
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
                                        self.parent = None
                                        self.an = None
                                        self.cipher_suite = None
                                        self.confidentiality_offset = None
                                        self.crc_value = None
                                        self.current_packet_num = None
                                        self.fcs_err_cfg = None
                                        self.initial_packet_number = None
                                        self.max_packet_num = None
                                        self.protection_enable = None
                                        self.sectag_length = None
                                        self.secure_channel_id = None
                                        self.secure_mode = None
                                        self.ssci = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-pl-oper:tx-sa'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.an is not None:
                                            return True

                                        if self.cipher_suite is not None:
                                            return True

                                        if self.confidentiality_offset is not None:
                                            return True

                                        if self.crc_value is not None:
                                            return True

                                        if self.current_packet_num is not None:
                                            return True

                                        if self.fcs_err_cfg is not None:
                                            return True

                                        if self.initial_packet_number is not None:
                                            return True

                                        if self.max_packet_num is not None:
                                            return True

                                        if self.protection_enable is not None:
                                            return True

                                        if self.sectag_length is not None:
                                            return True

                                        if self.secure_channel_id is not None:
                                            return True

                                        if self.secure_mode is not None:
                                            return True

                                        if self.ssci is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_pl_oper as meta
                                        return meta._meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.XlfpgaSa.TxSa']['meta_info']


                                class RxSa(object):
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
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: max_packet_num
                                    
                                    	Max Packet Number
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: next_expected_packet_num
                                    
                                    	Next expected Packet Number
                                    	**type**\:  int
                                    
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
                                        self.parent = None
                                        self.an = None
                                        self.auth_err_cfg = None
                                        self.cipher_suite = None
                                        self.confidentiality_offset = None
                                        self.crc_value = YLeafList()
                                        self.crc_value.parent = self
                                        self.crc_value.name = 'crc_value'
                                        self.current_packet_num = None
                                        self.fcs_err_cfg = None
                                        self.lowest_acceptable_packet_num = None
                                        self.max_packet_num = None
                                        self.next_expected_packet_num = None
                                        self.num_an_in_use = None
                                        self.pkt_tagged_detected = None
                                        self.pkt_tagged_validated = None
                                        self.pkt_untagged_detected = None
                                        self.protection_enable = None
                                        self.recent_an = None
                                        self.replay_protect_mode = None
                                        self.replay_window = None
                                        self.secure_channel_id = None
                                        self.secure_mode = None
                                        self.ssci = YLeafList()
                                        self.ssci.parent = self
                                        self.ssci.name = 'ssci'
                                        self.validation_mode = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-pl-oper:rx-sa'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.an is not None:
                                            return True

                                        if self.auth_err_cfg is not None:
                                            return True

                                        if self.cipher_suite is not None:
                                            return True

                                        if self.confidentiality_offset is not None:
                                            return True

                                        if self.crc_value is not None:
                                            for child in self.crc_value:
                                                if child is not None:
                                                    return True

                                        if self.current_packet_num is not None:
                                            return True

                                        if self.fcs_err_cfg is not None:
                                            return True

                                        if self.lowest_acceptable_packet_num is not None:
                                            return True

                                        if self.max_packet_num is not None:
                                            return True

                                        if self.next_expected_packet_num is not None:
                                            return True

                                        if self.num_an_in_use is not None:
                                            return True

                                        if self.pkt_tagged_detected is not None:
                                            return True

                                        if self.pkt_tagged_validated is not None:
                                            return True

                                        if self.pkt_untagged_detected is not None:
                                            return True

                                        if self.protection_enable is not None:
                                            return True

                                        if self.recent_an is not None:
                                            return True

                                        if self.replay_protect_mode is not None:
                                            return True

                                        if self.replay_window is not None:
                                            return True

                                        if self.secure_channel_id is not None:
                                            return True

                                        if self.secure_mode is not None:
                                            return True

                                        if self.ssci is not None:
                                            for child in self.ssci:
                                                if child is not None:
                                                    return True

                                        if self.validation_mode is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_pl_oper as meta
                                        return meta._meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.XlfpgaSa.RxSa']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-pl-oper:xlfpga-sa'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.rx_sa is not None and self.rx_sa._has_data():
                                        return True

                                    if self.tx_sa is not None and self.tx_sa._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_pl_oper as meta
                                    return meta._meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.XlfpgaSa']['meta_info']


                            class Es200Sa(object):
                                """
                                ES200 SA Information
                                
                                .. attribute:: rx_sa
                                
                                	Rx SA Details
                                	**type**\:   :py:class:`RxSa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Es200Sa.RxSa>`
                                
                                .. attribute:: tx_sa
                                
                                	Tx SA Details
                                	**type**\:   :py:class:`TxSa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Es200Sa.TxSa>`
                                
                                

                                """

                                _prefix = 'crypto-macsec-pl-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.rx_sa = Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Es200Sa.RxSa()
                                    self.rx_sa.parent = self
                                    self.tx_sa = Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Es200Sa.TxSa()
                                    self.tx_sa.parent = self


                                class TxSa(object):
                                    """
                                    Tx SA Details
                                    
                                    .. attribute:: is_valid
                                    
                                    	Is structure valid
                                    	**type**\:  bool
                                    
                                    .. attribute:: out_octets_encrypted_protected1
                                    
                                    	octets1 encrypted/protected
                                    	**type**\:  int
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: out_octets_encrypted_protected2
                                    
                                    	octets2 encrypted/protected
                                    	**type**\:  int
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: out_pkts_encrypted_protected
                                    
                                    	packets encrypted/protected
                                    	**type**\:  int
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: out_pkts_sa_not_in_use
                                    
                                    	packets coming on SA that is
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
                                    	**type**\:   :py:class:`XformParams <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Es200Sa.TxSa.XformParams>`
                                    
                                    

                                    """

                                    _prefix = 'crypto-macsec-pl-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.is_valid = None
                                        self.out_octets_encrypted_protected1 = None
                                        self.out_octets_encrypted_protected2 = None
                                        self.out_pkts_encrypted_protected = None
                                        self.out_pkts_sa_not_in_use = None
                                        self.out_pkts_too_long = None
                                        self.sa_id = None
                                        self.sc_no = None
                                        self.xform_params = Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Es200Sa.TxSa.XformParams()
                                        self.xform_params.parent = self


                                    class XformParams(object):
                                        """
                                         Xform Params
                                        
                                        .. attribute:: aes_key_len
                                        
                                        	AES Key length
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: assoc_num
                                        
                                        	Association Number for egress
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: bgen_auth_key
                                        
                                        	TRUE to generate the authKey, so authKey in this struct not used                                  APM\_FALSE to use provided authKey
                                        	**type**\:  bool
                                        
                                        .. attribute:: crypt_algo
                                        
                                        	Cryptographic algo used
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
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
                                            self.parent = None
                                            self.aes_key_len = None
                                            self.assoc_num = None
                                            self.bgen_auth_key = None
                                            self.crypt_algo = None
                                            self.is_egress_tr = None
                                            self.is_seq_num64_bit = None
                                            self.replay_win_size = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-pl-oper:xform-params'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.aes_key_len is not None:
                                                return True

                                            if self.assoc_num is not None:
                                                return True

                                            if self.bgen_auth_key is not None:
                                                return True

                                            if self.crypt_algo is not None:
                                                return True

                                            if self.is_egress_tr is not None:
                                                return True

                                            if self.is_seq_num64_bit is not None:
                                                return True

                                            if self.replay_win_size is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_pl_oper as meta
                                            return meta._meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Es200Sa.TxSa.XformParams']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-pl-oper:tx-sa'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_valid is not None:
                                            return True

                                        if self.out_octets_encrypted_protected1 is not None:
                                            return True

                                        if self.out_octets_encrypted_protected2 is not None:
                                            return True

                                        if self.out_pkts_encrypted_protected is not None:
                                            return True

                                        if self.out_pkts_sa_not_in_use is not None:
                                            return True

                                        if self.out_pkts_too_long is not None:
                                            return True

                                        if self.sa_id is not None:
                                            return True

                                        if self.sc_no is not None:
                                            return True

                                        if self.xform_params is not None and self.xform_params._has_data():
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_pl_oper as meta
                                        return meta._meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Es200Sa.TxSa']['meta_info']


                                class RxSa(object):
                                    """
                                    Rx SA Details
                                    
                                    .. attribute:: in_octets_decrypted_validated1
                                    
                                    	octets1 decrypted/validated
                                    	**type**\:  int
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: in_octets_decrypted_validated2
                                    
                                    	octets2 decrypted/validated
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
                                    	**type**\:   :py:class:`XformParams <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Es200Sa.RxSa.XformParams>`
                                    
                                    

                                    """

                                    _prefix = 'crypto-macsec-pl-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.in_octets_decrypted_validated1 = None
                                        self.in_octets_decrypted_validated2 = None
                                        self.in_octets_validated = None
                                        self.in_pkts_delayed = None
                                        self.in_pkts_invalid = None
                                        self.in_pkts_late = None
                                        self.in_pkts_not_using_sa = None
                                        self.in_pkts_not_valid = None
                                        self.in_pkts_ok = None
                                        self.in_pkts_unchecked = None
                                        self.in_pkts_unused_sa = None
                                        self.is_valid = None
                                        self.sa_id = None
                                        self.sc_no = None
                                        self.xform_params = Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Es200Sa.RxSa.XformParams()
                                        self.xform_params.parent = self


                                    class XformParams(object):
                                        """
                                         Xform Params
                                        
                                        .. attribute:: aes_key_len
                                        
                                        	AES Key length
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: assoc_num
                                        
                                        	Association Number for egress
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: bgen_auth_key
                                        
                                        	TRUE to generate the authKey, so authKey in this struct not used                                  APM\_FALSE to use provided authKey
                                        	**type**\:  bool
                                        
                                        .. attribute:: crypt_algo
                                        
                                        	Cryptographic algo used
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
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
                                            self.parent = None
                                            self.aes_key_len = None
                                            self.assoc_num = None
                                            self.bgen_auth_key = None
                                            self.crypt_algo = None
                                            self.is_egress_tr = None
                                            self.is_seq_num64_bit = None
                                            self.replay_win_size = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-pl-oper:xform-params'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.aes_key_len is not None:
                                                return True

                                            if self.assoc_num is not None:
                                                return True

                                            if self.bgen_auth_key is not None:
                                                return True

                                            if self.crypt_algo is not None:
                                                return True

                                            if self.is_egress_tr is not None:
                                                return True

                                            if self.is_seq_num64_bit is not None:
                                                return True

                                            if self.replay_win_size is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_pl_oper as meta
                                            return meta._meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Es200Sa.RxSa.XformParams']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-pl-oper:rx-sa'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.in_octets_decrypted_validated1 is not None:
                                            return True

                                        if self.in_octets_decrypted_validated2 is not None:
                                            return True

                                        if self.in_octets_validated is not None:
                                            return True

                                        if self.in_pkts_delayed is not None:
                                            return True

                                        if self.in_pkts_invalid is not None:
                                            return True

                                        if self.in_pkts_late is not None:
                                            return True

                                        if self.in_pkts_not_using_sa is not None:
                                            return True

                                        if self.in_pkts_not_valid is not None:
                                            return True

                                        if self.in_pkts_ok is not None:
                                            return True

                                        if self.in_pkts_unchecked is not None:
                                            return True

                                        if self.in_pkts_unused_sa is not None:
                                            return True

                                        if self.is_valid is not None:
                                            return True

                                        if self.sa_id is not None:
                                            return True

                                        if self.sc_no is not None:
                                            return True

                                        if self.xform_params is not None and self.xform_params._has_data():
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_pl_oper as meta
                                        return meta._meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Es200Sa.RxSa']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-pl-oper:es200-sa'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.rx_sa is not None and self.rx_sa._has_data():
                                        return True

                                    if self.tx_sa is not None and self.tx_sa._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_pl_oper as meta
                                    return meta._meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Es200Sa']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.sa_id is None:
                                    raise YPYModelError('Key property sa_id is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-pl-oper:hw-sa[Cisco-IOS-XR-crypto-macsec-pl-oper:sa-id = ' + str(self.sa_id) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.sa_id is not None:
                                    return True

                                if self.es200_sa is not None and self.es200_sa._has_data():
                                    return True

                                if self.hw_type is not None:
                                    return True

                                if self.msfpga_sa is not None and self.msfpga_sa._has_data():
                                    return True

                                if self.xlfpga_sa is not None and self.xlfpga_sa._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_pl_oper as meta
                                return meta._meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-pl-oper:hw-sas'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.hw_sa is not None:
                                for child_ref in self.hw_sa:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_pl_oper as meta
                            return meta._meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwSas']['meta_info']


                    class HwFlowS(object):
                        """
                        Table of Hardware Flows
                        
                        .. attribute:: hw_flow
                        
                        	Hardware Flow
                        	**type**\: list of    :py:class:`HwFlow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow>`
                        
                        

                        """

                        _prefix = 'crypto-macsec-pl-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.hw_flow = YList()
                            self.hw_flow.parent = self
                            self.hw_flow.name = 'hw_flow'


                        class HwFlow(object):
                            """
                            Hardware Flow
                            
                            .. attribute:: flow_id  <key>
                            
                            	FLOW ID
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: es200_flow
                            
                            	ES200 Flow Information
                            	**type**\:   :py:class:`Es200Flow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Es200Flow>`
                            
                            .. attribute:: hw_type
                            
                            	Hardware Type
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: msfpga_flow
                            
                            	MSFPGA Flow Information
                            	**type**\:   :py:class:`MsfpgaFlow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.MsfpgaFlow>`
                            
                            

                            """

                            _prefix = 'crypto-macsec-pl-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.flow_id = None
                                self.es200_flow = Macsec.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Es200Flow()
                                self.es200_flow.parent = self
                                self.hw_type = None
                                self.msfpga_flow = Macsec.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.MsfpgaFlow()
                                self.msfpga_flow.parent = self


                            class MsfpgaFlow(object):
                                """
                                MSFPGA Flow Information
                                
                                .. attribute:: rx_flow
                                
                                	Rx Flow Details
                                	**type**\:   :py:class:`RxFlow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.MsfpgaFlow.RxFlow>`
                                
                                .. attribute:: tx_flow
                                
                                	Tx Flow Details
                                	**type**\:   :py:class:`TxFlow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.MsfpgaFlow.TxFlow>`
                                
                                

                                """

                                _prefix = 'crypto-macsec-pl-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.rx_flow = Macsec.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.MsfpgaFlow.RxFlow()
                                    self.rx_flow.parent = self
                                    self.tx_flow = Macsec.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.MsfpgaFlow.TxFlow()
                                    self.tx_flow.parent = self


                                class TxFlow(object):
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
                                        self.parent = None
                                        self.action = None
                                        self.ctrl_check = None
                                        self.dmac_inuse = None
                                        self.ethertype = None
                                        self.flow_id = None
                                        self.in_use = None
                                        self.inner_vlan = None
                                        self.inner_vlan_tpid = None
                                        self.inner_vlan_up = None
                                        self.is_ctrl_pkt = None
                                        self.is_egress = None
                                        self.macda = YLeafList()
                                        self.macda.parent = self
                                        self.macda.name = 'macda'
                                        self.macsa = YLeafList()
                                        self.macsa.parent = self
                                        self.macsa.name = 'macsa'
                                        self.match_bad_tag = None
                                        self.match_kay_tag = None
                                        self.match_pri = None
                                        self.match_tagged = None
                                        self.match_untagged = None
                                        self.outer_vlan = None
                                        self.outer_vlan_tpid = None
                                        self.outer_vlan_up = None
                                        self.sai = None
                                        self.sci = None
                                        self.sci_inuse = None
                                        self.smac_inuse = None
                                        self.source_port = None
                                        self.source_port_chk = None
                                        self.tci = None
                                        self.tci_an = None
                                        self.tci_an_chk = None
                                        self.tci_c = None
                                        self.tci_chk = None
                                        self.tci_e_xr = None
                                        self.tci_sc = None
                                        self.tci_scb = None
                                        self.tci_v = None
                                        self.valid = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-pl-oper:tx-flow'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.action is not None:
                                            return True

                                        if self.ctrl_check is not None:
                                            return True

                                        if self.dmac_inuse is not None:
                                            return True

                                        if self.ethertype is not None:
                                            return True

                                        if self.flow_id is not None:
                                            return True

                                        if self.in_use is not None:
                                            return True

                                        if self.inner_vlan is not None:
                                            return True

                                        if self.inner_vlan_tpid is not None:
                                            return True

                                        if self.inner_vlan_up is not None:
                                            return True

                                        if self.is_ctrl_pkt is not None:
                                            return True

                                        if self.is_egress is not None:
                                            return True

                                        if self.macda is not None:
                                            for child in self.macda:
                                                if child is not None:
                                                    return True

                                        if self.macsa is not None:
                                            for child in self.macsa:
                                                if child is not None:
                                                    return True

                                        if self.match_bad_tag is not None:
                                            return True

                                        if self.match_kay_tag is not None:
                                            return True

                                        if self.match_pri is not None:
                                            return True

                                        if self.match_tagged is not None:
                                            return True

                                        if self.match_untagged is not None:
                                            return True

                                        if self.outer_vlan is not None:
                                            return True

                                        if self.outer_vlan_tpid is not None:
                                            return True

                                        if self.outer_vlan_up is not None:
                                            return True

                                        if self.sai is not None:
                                            return True

                                        if self.sci is not None:
                                            return True

                                        if self.sci_inuse is not None:
                                            return True

                                        if self.smac_inuse is not None:
                                            return True

                                        if self.source_port is not None:
                                            return True

                                        if self.source_port_chk is not None:
                                            return True

                                        if self.tci is not None:
                                            return True

                                        if self.tci_an is not None:
                                            return True

                                        if self.tci_an_chk is not None:
                                            return True

                                        if self.tci_c is not None:
                                            return True

                                        if self.tci_chk is not None:
                                            return True

                                        if self.tci_e_xr is not None:
                                            return True

                                        if self.tci_sc is not None:
                                            return True

                                        if self.tci_scb is not None:
                                            return True

                                        if self.tci_v is not None:
                                            return True

                                        if self.valid is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_pl_oper as meta
                                        return meta._meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.MsfpgaFlow.TxFlow']['meta_info']


                                class RxFlow(object):
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
                                        self.parent = None
                                        self.action = None
                                        self.ctrl_check = None
                                        self.dmac_inuse = None
                                        self.ethertype = None
                                        self.flow_id = None
                                        self.in_use = None
                                        self.inner_vlan = None
                                        self.inner_vlan_tpid = None
                                        self.inner_vlan_up = None
                                        self.is_ctrl_pkt = None
                                        self.is_egress = None
                                        self.macda = YLeafList()
                                        self.macda.parent = self
                                        self.macda.name = 'macda'
                                        self.macsa = YLeafList()
                                        self.macsa.parent = self
                                        self.macsa.name = 'macsa'
                                        self.match_bad_tag = None
                                        self.match_kay_tag = None
                                        self.match_pri = None
                                        self.match_tagged = None
                                        self.match_untagged = None
                                        self.outer_vlan = None
                                        self.outer_vlan_tpid = None
                                        self.outer_vlan_up = None
                                        self.sai = None
                                        self.sci = None
                                        self.sci_inuse = None
                                        self.smac_inuse = None
                                        self.source_port = None
                                        self.source_port_chk = None
                                        self.tci = None
                                        self.tci_an = None
                                        self.tci_an_chk = None
                                        self.tci_c = None
                                        self.tci_chk = None
                                        self.tci_e_xr = None
                                        self.tci_sc = None
                                        self.tci_scb = None
                                        self.tci_v = None
                                        self.valid = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-pl-oper:rx-flow'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.action is not None:
                                            return True

                                        if self.ctrl_check is not None:
                                            return True

                                        if self.dmac_inuse is not None:
                                            return True

                                        if self.ethertype is not None:
                                            return True

                                        if self.flow_id is not None:
                                            return True

                                        if self.in_use is not None:
                                            return True

                                        if self.inner_vlan is not None:
                                            return True

                                        if self.inner_vlan_tpid is not None:
                                            return True

                                        if self.inner_vlan_up is not None:
                                            return True

                                        if self.is_ctrl_pkt is not None:
                                            return True

                                        if self.is_egress is not None:
                                            return True

                                        if self.macda is not None:
                                            for child in self.macda:
                                                if child is not None:
                                                    return True

                                        if self.macsa is not None:
                                            for child in self.macsa:
                                                if child is not None:
                                                    return True

                                        if self.match_bad_tag is not None:
                                            return True

                                        if self.match_kay_tag is not None:
                                            return True

                                        if self.match_pri is not None:
                                            return True

                                        if self.match_tagged is not None:
                                            return True

                                        if self.match_untagged is not None:
                                            return True

                                        if self.outer_vlan is not None:
                                            return True

                                        if self.outer_vlan_tpid is not None:
                                            return True

                                        if self.outer_vlan_up is not None:
                                            return True

                                        if self.sai is not None:
                                            return True

                                        if self.sci is not None:
                                            return True

                                        if self.sci_inuse is not None:
                                            return True

                                        if self.smac_inuse is not None:
                                            return True

                                        if self.source_port is not None:
                                            return True

                                        if self.source_port_chk is not None:
                                            return True

                                        if self.tci is not None:
                                            return True

                                        if self.tci_an is not None:
                                            return True

                                        if self.tci_an_chk is not None:
                                            return True

                                        if self.tci_c is not None:
                                            return True

                                        if self.tci_chk is not None:
                                            return True

                                        if self.tci_e_xr is not None:
                                            return True

                                        if self.tci_sc is not None:
                                            return True

                                        if self.tci_scb is not None:
                                            return True

                                        if self.tci_v is not None:
                                            return True

                                        if self.valid is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_pl_oper as meta
                                        return meta._meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.MsfpgaFlow.RxFlow']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-pl-oper:msfpga-flow'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.rx_flow is not None and self.rx_flow._has_data():
                                        return True

                                    if self.tx_flow is not None and self.tx_flow._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_pl_oper as meta
                                    return meta._meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.MsfpgaFlow']['meta_info']


                            class Es200Flow(object):
                                """
                                ES200 Flow Information
                                
                                .. attribute:: rx_flow
                                
                                	Rx Flow Details
                                	**type**\:   :py:class:`RxFlow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Es200Flow.RxFlow>`
                                
                                .. attribute:: tx_flow
                                
                                	Tx Flow Details
                                	**type**\:   :py:class:`TxFlow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Es200Flow.TxFlow>`
                                
                                

                                """

                                _prefix = 'crypto-macsec-pl-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.rx_flow = Macsec.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Es200Flow.RxFlow()
                                    self.rx_flow.parent = self
                                    self.tx_flow = Macsec.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Es200Flow.TxFlow()
                                    self.tx_flow.parent = self


                                class TxFlow(object):
                                    """
                                    Tx Flow Details
                                    
                                    .. attribute:: drop
                                    
                                    	Drop the packet
                                    	**type**\:  bool
                                    
                                    .. attribute:: ethertype
                                    
                                    	Parsed EtherType to match could be 0 if Ethertype should'nt                              be matched can be 0x88E5 for MACSec tag
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: flow_miss
                                    
                                    	Pkts matching none of flow entries
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
                                    
                                    .. attribute:: multi_flow_match
                                    
                                    	Pkts matching multiple flow entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
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
                                    
                                    .. attribute:: parser_dropped
                                    
                                    	Pkts dropped by header parser as invalid
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
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
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
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
                                    
                                    .. attribute:: plain_bits
                                    
                                    	Plain bits to compare. Max values\:               untagged pkt \- 40 bits after EthType             1 VLAN tag \- 24 bits after parsed EthType        2 VLAN tags\- 8 bits after  parsed EthType        1 MPLS tag \- 32 bits after 1st tag               2 MPLS tags\- 8 bits following after 2nd          or atmost 5th MPLS tag                           PBB \- 16 bits after C\-SA                         PBB with VLAN tag \- 16 bits of VLAN tag 
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
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
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
                                    
                                    .. attribute:: vlan_dei
                                    
                                    	 dei 
                                    	**type**\:  int
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: vlan_id
                                    
                                    	 vlan id 
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: vlan_pcp
                                    
                                    	 pcp 
                                    	**type**\:  int
                                    
                                    	**range:** 0..255
                                    
                                    

                                    """

                                    _prefix = 'crypto-macsec-pl-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.drop = None
                                        self.ethertype = None
                                        self.flow_miss = None
                                        self.flow_no = None
                                        self.force_ctrl = None
                                        self.inner_vlan_dei = None
                                        self.inner_vlan_id = None
                                        self.inner_vlan_user_pri = None
                                        self.is_flow_enabled = None
                                        self.macda = YLeafList()
                                        self.macda.parent = self
                                        self.macda.name = 'macda'
                                        self.mask_da = None
                                        self.mask_ethertype = None
                                        self.mask_plain_bits = None
                                        self.match_priority = None
                                        self.mpls1_bos = None
                                        self.mpls1_exp = None
                                        self.mpls1_label = None
                                        self.mpls2_bos = None
                                        self.mpls2_exp = None
                                        self.mpls2_label = None
                                        self.multi_flow_match = None
                                        self.outer_vlan_dei = None
                                        self.outer_vlan_id = None
                                        self.outer_vlan_user_pri = None
                                        self.parser_dropped = None
                                        self.pbb_bvid = None
                                        self.pbb_dei = None
                                        self.pbb_pcp = None
                                        self.pbb_sid = None
                                        self.pkt_type = None
                                        self.pkts_ctrl = None
                                        self.pkts_data = None
                                        self.pkts_dropped = None
                                        self.pkts_err_in = None
                                        self.plain_bits = None
                                        self.plain_bits_size = None
                                        self.psci = None
                                        self.tag_num = None
                                        self.tci = None
                                        self.tci_c = None
                                        self.tci_chk = None
                                        self.tci_e_xr = None
                                        self.tci_sc = None
                                        self.tci_scb = None
                                        self.tci_v = None
                                        self.vlan_dei = None
                                        self.vlan_id = None
                                        self.vlan_pcp = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-pl-oper:tx-flow'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.drop is not None:
                                            return True

                                        if self.ethertype is not None:
                                            return True

                                        if self.flow_miss is not None:
                                            return True

                                        if self.flow_no is not None:
                                            return True

                                        if self.force_ctrl is not None:
                                            return True

                                        if self.inner_vlan_dei is not None:
                                            return True

                                        if self.inner_vlan_id is not None:
                                            return True

                                        if self.inner_vlan_user_pri is not None:
                                            return True

                                        if self.is_flow_enabled is not None:
                                            return True

                                        if self.macda is not None:
                                            for child in self.macda:
                                                if child is not None:
                                                    return True

                                        if self.mask_da is not None:
                                            return True

                                        if self.mask_ethertype is not None:
                                            return True

                                        if self.mask_plain_bits is not None:
                                            return True

                                        if self.match_priority is not None:
                                            return True

                                        if self.mpls1_bos is not None:
                                            return True

                                        if self.mpls1_exp is not None:
                                            return True

                                        if self.mpls1_label is not None:
                                            return True

                                        if self.mpls2_bos is not None:
                                            return True

                                        if self.mpls2_exp is not None:
                                            return True

                                        if self.mpls2_label is not None:
                                            return True

                                        if self.multi_flow_match is not None:
                                            return True

                                        if self.outer_vlan_dei is not None:
                                            return True

                                        if self.outer_vlan_id is not None:
                                            return True

                                        if self.outer_vlan_user_pri is not None:
                                            return True

                                        if self.parser_dropped is not None:
                                            return True

                                        if self.pbb_bvid is not None:
                                            return True

                                        if self.pbb_dei is not None:
                                            return True

                                        if self.pbb_pcp is not None:
                                            return True

                                        if self.pbb_sid is not None:
                                            return True

                                        if self.pkt_type is not None:
                                            return True

                                        if self.pkts_ctrl is not None:
                                            return True

                                        if self.pkts_data is not None:
                                            return True

                                        if self.pkts_dropped is not None:
                                            return True

                                        if self.pkts_err_in is not None:
                                            return True

                                        if self.plain_bits is not None:
                                            return True

                                        if self.plain_bits_size is not None:
                                            return True

                                        if self.psci is not None:
                                            return True

                                        if self.tag_num is not None:
                                            return True

                                        if self.tci is not None:
                                            return True

                                        if self.tci_c is not None:
                                            return True

                                        if self.tci_chk is not None:
                                            return True

                                        if self.tci_e_xr is not None:
                                            return True

                                        if self.tci_sc is not None:
                                            return True

                                        if self.tci_scb is not None:
                                            return True

                                        if self.tci_v is not None:
                                            return True

                                        if self.vlan_dei is not None:
                                            return True

                                        if self.vlan_id is not None:
                                            return True

                                        if self.vlan_pcp is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_pl_oper as meta
                                        return meta._meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Es200Flow.TxFlow']['meta_info']


                                class RxFlow(object):
                                    """
                                    Rx Flow Details
                                    
                                    .. attribute:: drop
                                    
                                    	Drop the packet
                                    	**type**\:  bool
                                    
                                    .. attribute:: ethertype
                                    
                                    	Parsed EtherType to match could be 0 if Ethertype should'nt                              be matched can be 0x88E5 for MACSec tag
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: flow_miss
                                    
                                    	Pkts matching none of flow entries
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
                                    
                                    .. attribute:: multi_flow_match
                                    
                                    	Pkts matching multiple flow entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
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
                                    
                                    .. attribute:: parser_dropped
                                    
                                    	Pkts dropped by header parser as invalid
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
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
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
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
                                    
                                    .. attribute:: plain_bits
                                    
                                    	Plain bits to compare. Max values\:               untagged pkt \- 40 bits after EthType             1 VLAN tag \- 24 bits after parsed EthType        2 VLAN tags\- 8 bits after  parsed EthType        1 MPLS tag \- 32 bits after 1st tag               2 MPLS tags\- 8 bits following after 2nd          or atmost 5th MPLS tag                           PBB \- 16 bits after C\-SA                         PBB with VLAN tag \- 16 bits of VLAN tag 
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
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
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
                                    
                                    .. attribute:: vlan_dei
                                    
                                    	 dei 
                                    	**type**\:  int
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: vlan_id
                                    
                                    	 vlan id 
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: vlan_pcp
                                    
                                    	 pcp 
                                    	**type**\:  int
                                    
                                    	**range:** 0..255
                                    
                                    

                                    """

                                    _prefix = 'crypto-macsec-pl-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.drop = None
                                        self.ethertype = None
                                        self.flow_miss = None
                                        self.flow_no = None
                                        self.force_ctrl = None
                                        self.inner_vlan_dei = None
                                        self.inner_vlan_id = None
                                        self.inner_vlan_user_pri = None
                                        self.is_flow_enabled = None
                                        self.macda = YLeafList()
                                        self.macda.parent = self
                                        self.macda.name = 'macda'
                                        self.mask_da = None
                                        self.mask_ethertype = None
                                        self.mask_plain_bits = None
                                        self.match_priority = None
                                        self.mpls1_bos = None
                                        self.mpls1_exp = None
                                        self.mpls1_label = None
                                        self.mpls2_bos = None
                                        self.mpls2_exp = None
                                        self.mpls2_label = None
                                        self.multi_flow_match = None
                                        self.outer_vlan_dei = None
                                        self.outer_vlan_id = None
                                        self.outer_vlan_user_pri = None
                                        self.parser_dropped = None
                                        self.pbb_bvid = None
                                        self.pbb_dei = None
                                        self.pbb_pcp = None
                                        self.pbb_sid = None
                                        self.pkt_type = None
                                        self.pkts_ctrl = None
                                        self.pkts_data = None
                                        self.pkts_dropped = None
                                        self.pkts_err_in = None
                                        self.plain_bits = None
                                        self.plain_bits_size = None
                                        self.psci = None
                                        self.tag_num = None
                                        self.tci = None
                                        self.tci_c = None
                                        self.tci_chk = None
                                        self.tci_e_xr = None
                                        self.tci_sc = None
                                        self.tci_scb = None
                                        self.tci_v = None
                                        self.vlan_dei = None
                                        self.vlan_id = None
                                        self.vlan_pcp = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-pl-oper:rx-flow'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.drop is not None:
                                            return True

                                        if self.ethertype is not None:
                                            return True

                                        if self.flow_miss is not None:
                                            return True

                                        if self.flow_no is not None:
                                            return True

                                        if self.force_ctrl is not None:
                                            return True

                                        if self.inner_vlan_dei is not None:
                                            return True

                                        if self.inner_vlan_id is not None:
                                            return True

                                        if self.inner_vlan_user_pri is not None:
                                            return True

                                        if self.is_flow_enabled is not None:
                                            return True

                                        if self.macda is not None:
                                            for child in self.macda:
                                                if child is not None:
                                                    return True

                                        if self.mask_da is not None:
                                            return True

                                        if self.mask_ethertype is not None:
                                            return True

                                        if self.mask_plain_bits is not None:
                                            return True

                                        if self.match_priority is not None:
                                            return True

                                        if self.mpls1_bos is not None:
                                            return True

                                        if self.mpls1_exp is not None:
                                            return True

                                        if self.mpls1_label is not None:
                                            return True

                                        if self.mpls2_bos is not None:
                                            return True

                                        if self.mpls2_exp is not None:
                                            return True

                                        if self.mpls2_label is not None:
                                            return True

                                        if self.multi_flow_match is not None:
                                            return True

                                        if self.outer_vlan_dei is not None:
                                            return True

                                        if self.outer_vlan_id is not None:
                                            return True

                                        if self.outer_vlan_user_pri is not None:
                                            return True

                                        if self.parser_dropped is not None:
                                            return True

                                        if self.pbb_bvid is not None:
                                            return True

                                        if self.pbb_dei is not None:
                                            return True

                                        if self.pbb_pcp is not None:
                                            return True

                                        if self.pbb_sid is not None:
                                            return True

                                        if self.pkt_type is not None:
                                            return True

                                        if self.pkts_ctrl is not None:
                                            return True

                                        if self.pkts_data is not None:
                                            return True

                                        if self.pkts_dropped is not None:
                                            return True

                                        if self.pkts_err_in is not None:
                                            return True

                                        if self.plain_bits is not None:
                                            return True

                                        if self.plain_bits_size is not None:
                                            return True

                                        if self.psci is not None:
                                            return True

                                        if self.tag_num is not None:
                                            return True

                                        if self.tci is not None:
                                            return True

                                        if self.tci_c is not None:
                                            return True

                                        if self.tci_chk is not None:
                                            return True

                                        if self.tci_e_xr is not None:
                                            return True

                                        if self.tci_sc is not None:
                                            return True

                                        if self.tci_scb is not None:
                                            return True

                                        if self.tci_v is not None:
                                            return True

                                        if self.vlan_dei is not None:
                                            return True

                                        if self.vlan_id is not None:
                                            return True

                                        if self.vlan_pcp is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_pl_oper as meta
                                        return meta._meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Es200Flow.RxFlow']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-pl-oper:es200-flow'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.rx_flow is not None and self.rx_flow._has_data():
                                        return True

                                    if self.tx_flow is not None and self.tx_flow._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_pl_oper as meta
                                    return meta._meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Es200Flow']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.flow_id is None:
                                    raise YPYModelError('Key property flow_id is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-pl-oper:hw-flow[Cisco-IOS-XR-crypto-macsec-pl-oper:flow-id = ' + str(self.flow_id) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.flow_id is not None:
                                    return True

                                if self.es200_flow is not None and self.es200_flow._has_data():
                                    return True

                                if self.hw_type is not None:
                                    return True

                                if self.msfpga_flow is not None and self.msfpga_flow._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_pl_oper as meta
                                return meta._meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-pl-oper:hw-flow-s'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.hw_flow is not None:
                                for child_ref in self.hw_flow:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_pl_oper as meta
                            return meta._meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwFlowS']['meta_info']


                    class SwFlowS(object):
                        """
                        Table of sofware Flows
                        
                        .. attribute:: sw_flow
                        
                        	Software Flow
                        	**type**\: list of    :py:class:`SwFlow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.SwFlowS.SwFlow>`
                        
                        

                        """

                        _prefix = 'crypto-macsec-pl-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.sw_flow = YList()
                            self.sw_flow.parent = self
                            self.sw_flow.name = 'sw_flow'


                        class SwFlow(object):
                            """
                            Software Flow
                            
                            .. attribute:: flow_id  <key>
                            
                            	FLOW ID
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: es200_flow
                            
                            	ES200 Flow Information
                            	**type**\:   :py:class:`Es200Flow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.SwFlowS.SwFlow.Es200Flow>`
                            
                            .. attribute:: hw_type
                            
                            	Hardware Type
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: msfpga_flow
                            
                            	MSFPGA Flow Information
                            	**type**\:   :py:class:`MsfpgaFlow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.SwFlowS.SwFlow.MsfpgaFlow>`
                            
                            

                            """

                            _prefix = 'crypto-macsec-pl-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.flow_id = None
                                self.es200_flow = Macsec.Nodes.Node.Interfaces.Interface.SwFlowS.SwFlow.Es200Flow()
                                self.es200_flow.parent = self
                                self.hw_type = None
                                self.msfpga_flow = Macsec.Nodes.Node.Interfaces.Interface.SwFlowS.SwFlow.MsfpgaFlow()
                                self.msfpga_flow.parent = self


                            class MsfpgaFlow(object):
                                """
                                MSFPGA Flow Information
                                
                                .. attribute:: rx_flow
                                
                                	Rx Flow Details
                                	**type**\:   :py:class:`RxFlow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.SwFlowS.SwFlow.MsfpgaFlow.RxFlow>`
                                
                                .. attribute:: tx_flow
                                
                                	Tx Flow Details
                                	**type**\:   :py:class:`TxFlow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.SwFlowS.SwFlow.MsfpgaFlow.TxFlow>`
                                
                                

                                """

                                _prefix = 'crypto-macsec-pl-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.rx_flow = Macsec.Nodes.Node.Interfaces.Interface.SwFlowS.SwFlow.MsfpgaFlow.RxFlow()
                                    self.rx_flow.parent = self
                                    self.tx_flow = Macsec.Nodes.Node.Interfaces.Interface.SwFlowS.SwFlow.MsfpgaFlow.TxFlow()
                                    self.tx_flow.parent = self


                                class TxFlow(object):
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
                                        self.parent = None
                                        self.action = None
                                        self.ctrl_check = None
                                        self.dmac_inuse = None
                                        self.ethertype = None
                                        self.flow_id = None
                                        self.in_use = None
                                        self.inner_vlan = None
                                        self.inner_vlan_tpid = None
                                        self.inner_vlan_up = None
                                        self.is_ctrl_pkt = None
                                        self.is_egress = None
                                        self.macda = YLeafList()
                                        self.macda.parent = self
                                        self.macda.name = 'macda'
                                        self.macsa = YLeafList()
                                        self.macsa.parent = self
                                        self.macsa.name = 'macsa'
                                        self.match_bad_tag = None
                                        self.match_kay_tag = None
                                        self.match_pri = None
                                        self.match_tagged = None
                                        self.match_untagged = None
                                        self.outer_vlan = None
                                        self.outer_vlan_tpid = None
                                        self.outer_vlan_up = None
                                        self.sai = None
                                        self.sci = None
                                        self.sci_inuse = None
                                        self.smac_inuse = None
                                        self.source_port = None
                                        self.source_port_chk = None
                                        self.tci = None
                                        self.tci_an = None
                                        self.tci_an_chk = None
                                        self.tci_c = None
                                        self.tci_chk = None
                                        self.tci_e_xr = None
                                        self.tci_sc = None
                                        self.tci_scb = None
                                        self.tci_v = None
                                        self.valid = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-pl-oper:tx-flow'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.action is not None:
                                            return True

                                        if self.ctrl_check is not None:
                                            return True

                                        if self.dmac_inuse is not None:
                                            return True

                                        if self.ethertype is not None:
                                            return True

                                        if self.flow_id is not None:
                                            return True

                                        if self.in_use is not None:
                                            return True

                                        if self.inner_vlan is not None:
                                            return True

                                        if self.inner_vlan_tpid is not None:
                                            return True

                                        if self.inner_vlan_up is not None:
                                            return True

                                        if self.is_ctrl_pkt is not None:
                                            return True

                                        if self.is_egress is not None:
                                            return True

                                        if self.macda is not None:
                                            for child in self.macda:
                                                if child is not None:
                                                    return True

                                        if self.macsa is not None:
                                            for child in self.macsa:
                                                if child is not None:
                                                    return True

                                        if self.match_bad_tag is not None:
                                            return True

                                        if self.match_kay_tag is not None:
                                            return True

                                        if self.match_pri is not None:
                                            return True

                                        if self.match_tagged is not None:
                                            return True

                                        if self.match_untagged is not None:
                                            return True

                                        if self.outer_vlan is not None:
                                            return True

                                        if self.outer_vlan_tpid is not None:
                                            return True

                                        if self.outer_vlan_up is not None:
                                            return True

                                        if self.sai is not None:
                                            return True

                                        if self.sci is not None:
                                            return True

                                        if self.sci_inuse is not None:
                                            return True

                                        if self.smac_inuse is not None:
                                            return True

                                        if self.source_port is not None:
                                            return True

                                        if self.source_port_chk is not None:
                                            return True

                                        if self.tci is not None:
                                            return True

                                        if self.tci_an is not None:
                                            return True

                                        if self.tci_an_chk is not None:
                                            return True

                                        if self.tci_c is not None:
                                            return True

                                        if self.tci_chk is not None:
                                            return True

                                        if self.tci_e_xr is not None:
                                            return True

                                        if self.tci_sc is not None:
                                            return True

                                        if self.tci_scb is not None:
                                            return True

                                        if self.tci_v is not None:
                                            return True

                                        if self.valid is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_pl_oper as meta
                                        return meta._meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwFlowS.SwFlow.MsfpgaFlow.TxFlow']['meta_info']


                                class RxFlow(object):
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
                                        self.parent = None
                                        self.action = None
                                        self.ctrl_check = None
                                        self.dmac_inuse = None
                                        self.ethertype = None
                                        self.flow_id = None
                                        self.in_use = None
                                        self.inner_vlan = None
                                        self.inner_vlan_tpid = None
                                        self.inner_vlan_up = None
                                        self.is_ctrl_pkt = None
                                        self.is_egress = None
                                        self.macda = YLeafList()
                                        self.macda.parent = self
                                        self.macda.name = 'macda'
                                        self.macsa = YLeafList()
                                        self.macsa.parent = self
                                        self.macsa.name = 'macsa'
                                        self.match_bad_tag = None
                                        self.match_kay_tag = None
                                        self.match_pri = None
                                        self.match_tagged = None
                                        self.match_untagged = None
                                        self.outer_vlan = None
                                        self.outer_vlan_tpid = None
                                        self.outer_vlan_up = None
                                        self.sai = None
                                        self.sci = None
                                        self.sci_inuse = None
                                        self.smac_inuse = None
                                        self.source_port = None
                                        self.source_port_chk = None
                                        self.tci = None
                                        self.tci_an = None
                                        self.tci_an_chk = None
                                        self.tci_c = None
                                        self.tci_chk = None
                                        self.tci_e_xr = None
                                        self.tci_sc = None
                                        self.tci_scb = None
                                        self.tci_v = None
                                        self.valid = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-pl-oper:rx-flow'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.action is not None:
                                            return True

                                        if self.ctrl_check is not None:
                                            return True

                                        if self.dmac_inuse is not None:
                                            return True

                                        if self.ethertype is not None:
                                            return True

                                        if self.flow_id is not None:
                                            return True

                                        if self.in_use is not None:
                                            return True

                                        if self.inner_vlan is not None:
                                            return True

                                        if self.inner_vlan_tpid is not None:
                                            return True

                                        if self.inner_vlan_up is not None:
                                            return True

                                        if self.is_ctrl_pkt is not None:
                                            return True

                                        if self.is_egress is not None:
                                            return True

                                        if self.macda is not None:
                                            for child in self.macda:
                                                if child is not None:
                                                    return True

                                        if self.macsa is not None:
                                            for child in self.macsa:
                                                if child is not None:
                                                    return True

                                        if self.match_bad_tag is not None:
                                            return True

                                        if self.match_kay_tag is not None:
                                            return True

                                        if self.match_pri is not None:
                                            return True

                                        if self.match_tagged is not None:
                                            return True

                                        if self.match_untagged is not None:
                                            return True

                                        if self.outer_vlan is not None:
                                            return True

                                        if self.outer_vlan_tpid is not None:
                                            return True

                                        if self.outer_vlan_up is not None:
                                            return True

                                        if self.sai is not None:
                                            return True

                                        if self.sci is not None:
                                            return True

                                        if self.sci_inuse is not None:
                                            return True

                                        if self.smac_inuse is not None:
                                            return True

                                        if self.source_port is not None:
                                            return True

                                        if self.source_port_chk is not None:
                                            return True

                                        if self.tci is not None:
                                            return True

                                        if self.tci_an is not None:
                                            return True

                                        if self.tci_an_chk is not None:
                                            return True

                                        if self.tci_c is not None:
                                            return True

                                        if self.tci_chk is not None:
                                            return True

                                        if self.tci_e_xr is not None:
                                            return True

                                        if self.tci_sc is not None:
                                            return True

                                        if self.tci_scb is not None:
                                            return True

                                        if self.tci_v is not None:
                                            return True

                                        if self.valid is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_pl_oper as meta
                                        return meta._meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwFlowS.SwFlow.MsfpgaFlow.RxFlow']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-pl-oper:msfpga-flow'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.rx_flow is not None and self.rx_flow._has_data():
                                        return True

                                    if self.tx_flow is not None and self.tx_flow._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_pl_oper as meta
                                    return meta._meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwFlowS.SwFlow.MsfpgaFlow']['meta_info']


                            class Es200Flow(object):
                                """
                                ES200 Flow Information
                                
                                .. attribute:: rx_flow
                                
                                	Rx Flow Details
                                	**type**\:   :py:class:`RxFlow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.SwFlowS.SwFlow.Es200Flow.RxFlow>`
                                
                                .. attribute:: tx_flow
                                
                                	Tx Flow Details
                                	**type**\:   :py:class:`TxFlow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.SwFlowS.SwFlow.Es200Flow.TxFlow>`
                                
                                

                                """

                                _prefix = 'crypto-macsec-pl-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.rx_flow = Macsec.Nodes.Node.Interfaces.Interface.SwFlowS.SwFlow.Es200Flow.RxFlow()
                                    self.rx_flow.parent = self
                                    self.tx_flow = Macsec.Nodes.Node.Interfaces.Interface.SwFlowS.SwFlow.Es200Flow.TxFlow()
                                    self.tx_flow.parent = self


                                class TxFlow(object):
                                    """
                                    Tx Flow Details
                                    
                                    .. attribute:: drop
                                    
                                    	Drop the packet
                                    	**type**\:  bool
                                    
                                    .. attribute:: ethertype
                                    
                                    	Parsed EtherType to match could be 0 if Ethertype should'nt                              be matched can be 0x88E5 for MACSec tag
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: flow_miss
                                    
                                    	Pkts matching none of flow entries
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
                                    
                                    .. attribute:: multi_flow_match
                                    
                                    	Pkts matching multiple flow entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
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
                                    
                                    .. attribute:: parser_dropped
                                    
                                    	Pkts dropped by header parser as invalid
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
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
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
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
                                    
                                    .. attribute:: plain_bits
                                    
                                    	Plain bits to compare. Max values\:               untagged pkt \- 40 bits after EthType             1 VLAN tag \- 24 bits after parsed EthType        2 VLAN tags\- 8 bits after  parsed EthType        1 MPLS tag \- 32 bits after 1st tag               2 MPLS tags\- 8 bits following after 2nd          or atmost 5th MPLS tag                           PBB \- 16 bits after C\-SA                         PBB with VLAN tag \- 16 bits of VLAN tag 
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
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
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
                                    
                                    .. attribute:: vlan_dei
                                    
                                    	 dei 
                                    	**type**\:  int
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: vlan_id
                                    
                                    	 vlan id 
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: vlan_pcp
                                    
                                    	 pcp 
                                    	**type**\:  int
                                    
                                    	**range:** 0..255
                                    
                                    

                                    """

                                    _prefix = 'crypto-macsec-pl-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.drop = None
                                        self.ethertype = None
                                        self.flow_miss = None
                                        self.flow_no = None
                                        self.force_ctrl = None
                                        self.inner_vlan_dei = None
                                        self.inner_vlan_id = None
                                        self.inner_vlan_user_pri = None
                                        self.is_flow_enabled = None
                                        self.macda = YLeafList()
                                        self.macda.parent = self
                                        self.macda.name = 'macda'
                                        self.mask_da = None
                                        self.mask_ethertype = None
                                        self.mask_plain_bits = None
                                        self.match_priority = None
                                        self.mpls1_bos = None
                                        self.mpls1_exp = None
                                        self.mpls1_label = None
                                        self.mpls2_bos = None
                                        self.mpls2_exp = None
                                        self.mpls2_label = None
                                        self.multi_flow_match = None
                                        self.outer_vlan_dei = None
                                        self.outer_vlan_id = None
                                        self.outer_vlan_user_pri = None
                                        self.parser_dropped = None
                                        self.pbb_bvid = None
                                        self.pbb_dei = None
                                        self.pbb_pcp = None
                                        self.pbb_sid = None
                                        self.pkt_type = None
                                        self.pkts_ctrl = None
                                        self.pkts_data = None
                                        self.pkts_dropped = None
                                        self.pkts_err_in = None
                                        self.plain_bits = None
                                        self.plain_bits_size = None
                                        self.psci = None
                                        self.tag_num = None
                                        self.tci = None
                                        self.tci_c = None
                                        self.tci_chk = None
                                        self.tci_e_xr = None
                                        self.tci_sc = None
                                        self.tci_scb = None
                                        self.tci_v = None
                                        self.vlan_dei = None
                                        self.vlan_id = None
                                        self.vlan_pcp = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-pl-oper:tx-flow'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.drop is not None:
                                            return True

                                        if self.ethertype is not None:
                                            return True

                                        if self.flow_miss is not None:
                                            return True

                                        if self.flow_no is not None:
                                            return True

                                        if self.force_ctrl is not None:
                                            return True

                                        if self.inner_vlan_dei is not None:
                                            return True

                                        if self.inner_vlan_id is not None:
                                            return True

                                        if self.inner_vlan_user_pri is not None:
                                            return True

                                        if self.is_flow_enabled is not None:
                                            return True

                                        if self.macda is not None:
                                            for child in self.macda:
                                                if child is not None:
                                                    return True

                                        if self.mask_da is not None:
                                            return True

                                        if self.mask_ethertype is not None:
                                            return True

                                        if self.mask_plain_bits is not None:
                                            return True

                                        if self.match_priority is not None:
                                            return True

                                        if self.mpls1_bos is not None:
                                            return True

                                        if self.mpls1_exp is not None:
                                            return True

                                        if self.mpls1_label is not None:
                                            return True

                                        if self.mpls2_bos is not None:
                                            return True

                                        if self.mpls2_exp is not None:
                                            return True

                                        if self.mpls2_label is not None:
                                            return True

                                        if self.multi_flow_match is not None:
                                            return True

                                        if self.outer_vlan_dei is not None:
                                            return True

                                        if self.outer_vlan_id is not None:
                                            return True

                                        if self.outer_vlan_user_pri is not None:
                                            return True

                                        if self.parser_dropped is not None:
                                            return True

                                        if self.pbb_bvid is not None:
                                            return True

                                        if self.pbb_dei is not None:
                                            return True

                                        if self.pbb_pcp is not None:
                                            return True

                                        if self.pbb_sid is not None:
                                            return True

                                        if self.pkt_type is not None:
                                            return True

                                        if self.pkts_ctrl is not None:
                                            return True

                                        if self.pkts_data is not None:
                                            return True

                                        if self.pkts_dropped is not None:
                                            return True

                                        if self.pkts_err_in is not None:
                                            return True

                                        if self.plain_bits is not None:
                                            return True

                                        if self.plain_bits_size is not None:
                                            return True

                                        if self.psci is not None:
                                            return True

                                        if self.tag_num is not None:
                                            return True

                                        if self.tci is not None:
                                            return True

                                        if self.tci_c is not None:
                                            return True

                                        if self.tci_chk is not None:
                                            return True

                                        if self.tci_e_xr is not None:
                                            return True

                                        if self.tci_sc is not None:
                                            return True

                                        if self.tci_scb is not None:
                                            return True

                                        if self.tci_v is not None:
                                            return True

                                        if self.vlan_dei is not None:
                                            return True

                                        if self.vlan_id is not None:
                                            return True

                                        if self.vlan_pcp is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_pl_oper as meta
                                        return meta._meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwFlowS.SwFlow.Es200Flow.TxFlow']['meta_info']


                                class RxFlow(object):
                                    """
                                    Rx Flow Details
                                    
                                    .. attribute:: drop
                                    
                                    	Drop the packet
                                    	**type**\:  bool
                                    
                                    .. attribute:: ethertype
                                    
                                    	Parsed EtherType to match could be 0 if Ethertype should'nt                              be matched can be 0x88E5 for MACSec tag
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: flow_miss
                                    
                                    	Pkts matching none of flow entries
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
                                    
                                    .. attribute:: multi_flow_match
                                    
                                    	Pkts matching multiple flow entries
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
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
                                    
                                    .. attribute:: parser_dropped
                                    
                                    	Pkts dropped by header parser as invalid
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
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
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
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
                                    
                                    .. attribute:: plain_bits
                                    
                                    	Plain bits to compare. Max values\:               untagged pkt \- 40 bits after EthType             1 VLAN tag \- 24 bits after parsed EthType        2 VLAN tags\- 8 bits after  parsed EthType        1 MPLS tag \- 32 bits after 1st tag               2 MPLS tags\- 8 bits following after 2nd          or atmost 5th MPLS tag                           PBB \- 16 bits after C\-SA                         PBB with VLAN tag \- 16 bits of VLAN tag 
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
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
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
                                    
                                    .. attribute:: vlan_dei
                                    
                                    	 dei 
                                    	**type**\:  int
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: vlan_id
                                    
                                    	 vlan id 
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: vlan_pcp
                                    
                                    	 pcp 
                                    	**type**\:  int
                                    
                                    	**range:** 0..255
                                    
                                    

                                    """

                                    _prefix = 'crypto-macsec-pl-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.drop = None
                                        self.ethertype = None
                                        self.flow_miss = None
                                        self.flow_no = None
                                        self.force_ctrl = None
                                        self.inner_vlan_dei = None
                                        self.inner_vlan_id = None
                                        self.inner_vlan_user_pri = None
                                        self.is_flow_enabled = None
                                        self.macda = YLeafList()
                                        self.macda.parent = self
                                        self.macda.name = 'macda'
                                        self.mask_da = None
                                        self.mask_ethertype = None
                                        self.mask_plain_bits = None
                                        self.match_priority = None
                                        self.mpls1_bos = None
                                        self.mpls1_exp = None
                                        self.mpls1_label = None
                                        self.mpls2_bos = None
                                        self.mpls2_exp = None
                                        self.mpls2_label = None
                                        self.multi_flow_match = None
                                        self.outer_vlan_dei = None
                                        self.outer_vlan_id = None
                                        self.outer_vlan_user_pri = None
                                        self.parser_dropped = None
                                        self.pbb_bvid = None
                                        self.pbb_dei = None
                                        self.pbb_pcp = None
                                        self.pbb_sid = None
                                        self.pkt_type = None
                                        self.pkts_ctrl = None
                                        self.pkts_data = None
                                        self.pkts_dropped = None
                                        self.pkts_err_in = None
                                        self.plain_bits = None
                                        self.plain_bits_size = None
                                        self.psci = None
                                        self.tag_num = None
                                        self.tci = None
                                        self.tci_c = None
                                        self.tci_chk = None
                                        self.tci_e_xr = None
                                        self.tci_sc = None
                                        self.tci_scb = None
                                        self.tci_v = None
                                        self.vlan_dei = None
                                        self.vlan_id = None
                                        self.vlan_pcp = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-pl-oper:rx-flow'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.drop is not None:
                                            return True

                                        if self.ethertype is not None:
                                            return True

                                        if self.flow_miss is not None:
                                            return True

                                        if self.flow_no is not None:
                                            return True

                                        if self.force_ctrl is not None:
                                            return True

                                        if self.inner_vlan_dei is not None:
                                            return True

                                        if self.inner_vlan_id is not None:
                                            return True

                                        if self.inner_vlan_user_pri is not None:
                                            return True

                                        if self.is_flow_enabled is not None:
                                            return True

                                        if self.macda is not None:
                                            for child in self.macda:
                                                if child is not None:
                                                    return True

                                        if self.mask_da is not None:
                                            return True

                                        if self.mask_ethertype is not None:
                                            return True

                                        if self.mask_plain_bits is not None:
                                            return True

                                        if self.match_priority is not None:
                                            return True

                                        if self.mpls1_bos is not None:
                                            return True

                                        if self.mpls1_exp is not None:
                                            return True

                                        if self.mpls1_label is not None:
                                            return True

                                        if self.mpls2_bos is not None:
                                            return True

                                        if self.mpls2_exp is not None:
                                            return True

                                        if self.mpls2_label is not None:
                                            return True

                                        if self.multi_flow_match is not None:
                                            return True

                                        if self.outer_vlan_dei is not None:
                                            return True

                                        if self.outer_vlan_id is not None:
                                            return True

                                        if self.outer_vlan_user_pri is not None:
                                            return True

                                        if self.parser_dropped is not None:
                                            return True

                                        if self.pbb_bvid is not None:
                                            return True

                                        if self.pbb_dei is not None:
                                            return True

                                        if self.pbb_pcp is not None:
                                            return True

                                        if self.pbb_sid is not None:
                                            return True

                                        if self.pkt_type is not None:
                                            return True

                                        if self.pkts_ctrl is not None:
                                            return True

                                        if self.pkts_data is not None:
                                            return True

                                        if self.pkts_dropped is not None:
                                            return True

                                        if self.pkts_err_in is not None:
                                            return True

                                        if self.plain_bits is not None:
                                            return True

                                        if self.plain_bits_size is not None:
                                            return True

                                        if self.psci is not None:
                                            return True

                                        if self.tag_num is not None:
                                            return True

                                        if self.tci is not None:
                                            return True

                                        if self.tci_c is not None:
                                            return True

                                        if self.tci_chk is not None:
                                            return True

                                        if self.tci_e_xr is not None:
                                            return True

                                        if self.tci_sc is not None:
                                            return True

                                        if self.tci_scb is not None:
                                            return True

                                        if self.tci_v is not None:
                                            return True

                                        if self.vlan_dei is not None:
                                            return True

                                        if self.vlan_id is not None:
                                            return True

                                        if self.vlan_pcp is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_pl_oper as meta
                                        return meta._meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwFlowS.SwFlow.Es200Flow.RxFlow']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-pl-oper:es200-flow'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.rx_flow is not None and self.rx_flow._has_data():
                                        return True

                                    if self.tx_flow is not None and self.tx_flow._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_pl_oper as meta
                                    return meta._meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwFlowS.SwFlow.Es200Flow']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.flow_id is None:
                                    raise YPYModelError('Key property flow_id is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-pl-oper:sw-flow[Cisco-IOS-XR-crypto-macsec-pl-oper:flow-id = ' + str(self.flow_id) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.flow_id is not None:
                                    return True

                                if self.es200_flow is not None and self.es200_flow._has_data():
                                    return True

                                if self.hw_type is not None:
                                    return True

                                if self.msfpga_flow is not None and self.msfpga_flow._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_pl_oper as meta
                                return meta._meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwFlowS.SwFlow']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-pl-oper:sw-flow-s'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.sw_flow is not None:
                                for child_ref in self.sw_flow:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_pl_oper as meta
                            return meta._meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwFlowS']['meta_info']


                    class SwStatistics(object):
                        """
                        The Software Statistics
                        
                        .. attribute:: es200_stats
                        
                        	ES200 Stats
                        	**type**\:   :py:class:`Es200Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.Es200Stats>`
                        
                        .. attribute:: hw_type
                        
                        	Hardware Type
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: msfpga_stats
                        
                        	MSFPGA Stats
                        	**type**\:   :py:class:`MsfpgaStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.MsfpgaStats>`
                        
                        .. attribute:: xlfpga_stats
                        
                        	XLFPGA Stats
                        	**type**\:   :py:class:`XlfpgaStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.XlfpgaStats>`
                        
                        

                        """

                        _prefix = 'crypto-macsec-pl-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.es200_stats = Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.Es200Stats()
                            self.es200_stats.parent = self
                            self.hw_type = None
                            self.msfpga_stats = Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.MsfpgaStats()
                            self.msfpga_stats.parent = self
                            self.xlfpga_stats = Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.XlfpgaStats()
                            self.xlfpga_stats.parent = self


                        class MsfpgaStats(object):
                            """
                            MSFPGA Stats
                            
                            .. attribute:: rx_interface_macsec_stats
                            
                            	Rx interface Macsec Stats
                            	**type**\:   :py:class:`RxInterfaceMacsecStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.MsfpgaStats.RxInterfaceMacsecStats>`
                            
                            .. attribute:: rx_sa_stats
                            
                            	Rx SA Stats
                            	**type**\:   :py:class:`RxSaStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.MsfpgaStats.RxSaStats>`
                            
                            .. attribute:: tx_interface_macsec_stats
                            
                            	Tx interface Macsec Stats
                            	**type**\:   :py:class:`TxInterfaceMacsecStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.MsfpgaStats.TxInterfaceMacsecStats>`
                            
                            .. attribute:: tx_sa_stats
                            
                            	Tx SA Stats
                            	**type**\:   :py:class:`TxSaStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.MsfpgaStats.TxSaStats>`
                            
                            

                            """

                            _prefix = 'crypto-macsec-pl-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.rx_interface_macsec_stats = Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.MsfpgaStats.RxInterfaceMacsecStats()
                                self.rx_interface_macsec_stats.parent = self
                                self.rx_sa_stats = Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.MsfpgaStats.RxSaStats()
                                self.rx_sa_stats.parent = self
                                self.tx_interface_macsec_stats = Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.MsfpgaStats.TxInterfaceMacsecStats()
                                self.tx_interface_macsec_stats.parent = self
                                self.tx_sa_stats = Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.MsfpgaStats.TxSaStats()
                                self.tx_sa_stats.parent = self


                            class TxSaStats(object):
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
                                    self.parent = None
                                    self.out_octets_encrypted = None
                                    self.out_octets_protected = None
                                    self.out_pkts_encrypted = None
                                    self.out_pkts_protected = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-pl-oper:tx-sa-stats'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.out_octets_encrypted is not None:
                                        return True

                                    if self.out_octets_protected is not None:
                                        return True

                                    if self.out_pkts_encrypted is not None:
                                        return True

                                    if self.out_pkts_protected is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_pl_oper as meta
                                    return meta._meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.MsfpgaStats.TxSaStats']['meta_info']


                            class RxSaStats(object):
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
                                    self.parent = None
                                    self.in_octets_decrypted = None
                                    self.in_octets_validated = None
                                    self.in_pkts_delayed = None
                                    self.in_pkts_invalid = None
                                    self.in_pkts_late = None
                                    self.in_pkts_not_using_sa = None
                                    self.in_pkts_not_valid = None
                                    self.in_pkts_ok = None
                                    self.in_pkts_unchecked = None
                                    self.in_pkts_unused_sa = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-pl-oper:rx-sa-stats'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.in_octets_decrypted is not None:
                                        return True

                                    if self.in_octets_validated is not None:
                                        return True

                                    if self.in_pkts_delayed is not None:
                                        return True

                                    if self.in_pkts_invalid is not None:
                                        return True

                                    if self.in_pkts_late is not None:
                                        return True

                                    if self.in_pkts_not_using_sa is not None:
                                        return True

                                    if self.in_pkts_not_valid is not None:
                                        return True

                                    if self.in_pkts_ok is not None:
                                        return True

                                    if self.in_pkts_unchecked is not None:
                                        return True

                                    if self.in_pkts_unused_sa is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_pl_oper as meta
                                    return meta._meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.MsfpgaStats.RxSaStats']['meta_info']


                            class TxInterfaceMacsecStats(object):
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
                                    self.parent = None
                                    self.out_pkt_too_long = None
                                    self.out_pkt_uncontrolled = None
                                    self.out_pkt_untagged = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-pl-oper:tx-interface-macsec-stats'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.out_pkt_too_long is not None:
                                        return True

                                    if self.out_pkt_uncontrolled is not None:
                                        return True

                                    if self.out_pkt_untagged is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_pl_oper as meta
                                    return meta._meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.MsfpgaStats.TxInterfaceMacsecStats']['meta_info']


                            class RxInterfaceMacsecStats(object):
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
                                    self.parent = None
                                    self.in_pkt_bad_tag = None
                                    self.in_pkt_no_sci = None
                                    self.in_pkt_notag = None
                                    self.in_pkt_overrun = None
                                    self.in_pkt_tagged = None
                                    self.in_pkt_uncontrolled = None
                                    self.in_pkt_unknown_sci = None
                                    self.in_pkt_untagged = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-pl-oper:rx-interface-macsec-stats'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.in_pkt_bad_tag is not None:
                                        return True

                                    if self.in_pkt_no_sci is not None:
                                        return True

                                    if self.in_pkt_notag is not None:
                                        return True

                                    if self.in_pkt_overrun is not None:
                                        return True

                                    if self.in_pkt_tagged is not None:
                                        return True

                                    if self.in_pkt_uncontrolled is not None:
                                        return True

                                    if self.in_pkt_unknown_sci is not None:
                                        return True

                                    if self.in_pkt_untagged is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_pl_oper as meta
                                    return meta._meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.MsfpgaStats.RxInterfaceMacsecStats']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-pl-oper:msfpga-stats'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.rx_interface_macsec_stats is not None and self.rx_interface_macsec_stats._has_data():
                                    return True

                                if self.rx_sa_stats is not None and self.rx_sa_stats._has_data():
                                    return True

                                if self.tx_interface_macsec_stats is not None and self.tx_interface_macsec_stats._has_data():
                                    return True

                                if self.tx_sa_stats is not None and self.tx_sa_stats._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_pl_oper as meta
                                return meta._meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.MsfpgaStats']['meta_info']


                        class XlfpgaStats(object):
                            """
                            XLFPGA Stats
                            
                            .. attribute:: macsec_rx_stats
                            
                            	Rx SC and SA Level Stats
                            	**type**\:   :py:class:`MacsecRxStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.XlfpgaStats.MacsecRxStats>`
                            
                            .. attribute:: macsec_tx_stats
                            
                            	Tx SC and SA Level Stats
                            	**type**\:   :py:class:`MacsecTxStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.XlfpgaStats.MacsecTxStats>`
                            
                            

                            """

                            _prefix = 'crypto-macsec-pl-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.macsec_rx_stats = Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.XlfpgaStats.MacsecRxStats()
                                self.macsec_rx_stats.parent = self
                                self.macsec_tx_stats = Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.XlfpgaStats.MacsecTxStats()
                                self.macsec_tx_stats.parent = self


                            class MacsecTxStats(object):
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
                                    self.parent = None
                                    self.current_an = None
                                    self.sa_encrypted_pkts = None
                                    self.sc_encrypted_octets = None
                                    self.sc_encrypted_pkts = None
                                    self.sc_overrun_pkts = None
                                    self.sc_toolong_pkts = None
                                    self.sc_untagged_pkts = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-pl-oper:macsec-tx-stats'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.current_an is not None:
                                        return True

                                    if self.sa_encrypted_pkts is not None:
                                        return True

                                    if self.sc_encrypted_octets is not None:
                                        return True

                                    if self.sc_encrypted_pkts is not None:
                                        return True

                                    if self.sc_overrun_pkts is not None:
                                        return True

                                    if self.sc_toolong_pkts is not None:
                                        return True

                                    if self.sc_untagged_pkts is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_pl_oper as meta
                                    return meta._meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.XlfpgaStats.MacsecTxStats']['meta_info']


                            class MacsecRxStats(object):
                                """
                                Rx SC and SA Level Stats
                                
                                .. attribute:: rx_sa_stat
                                
                                	Rx SA Level Stats
                                	**type**\: list of    :py:class:`RxSaStat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.XlfpgaStats.MacsecRxStats.RxSaStat>`
                                
                                .. attribute:: sc_bad_tag_pkts
                                
                                	Rx Bad Tag Packets
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
                                    self.parent = None
                                    self.rx_sa_stat = YList()
                                    self.rx_sa_stat.parent = self
                                    self.rx_sa_stat.name = 'rx_sa_stat'
                                    self.sc_bad_tag_pkts = None
                                    self.sc_decrypted_octets = None
                                    self.sc_delayed_pkts = None
                                    self.sc_invalid_pkts = None
                                    self.sc_late_pkts = None
                                    self.sc_no_sci_pkts = None
                                    self.sc_no_tag_pkts = None
                                    self.sc_not_using_pkts = None
                                    self.sc_not_valid_pkts = None
                                    self.sc_ok_pkts = None
                                    self.sc_overrun_pkts = None
                                    self.sc_unchecked_pkts = None
                                    self.sc_unknown_sci_pkts = None
                                    self.sc_untagged_pkts = None
                                    self.sc_unused_pkts = None


                                class RxSaStat(object):
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
                                        self.parent = None
                                        self.an = None
                                        self.sa_invalid_pkts = None
                                        self.sa_not_using_pkts = None
                                        self.sa_not_valid_pkts = None
                                        self.sa_ok_pkts = None
                                        self.sa_unused_pkts = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-pl-oper:rx-sa-stat'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.an is not None:
                                            return True

                                        if self.sa_invalid_pkts is not None:
                                            return True

                                        if self.sa_not_using_pkts is not None:
                                            return True

                                        if self.sa_not_valid_pkts is not None:
                                            return True

                                        if self.sa_ok_pkts is not None:
                                            return True

                                        if self.sa_unused_pkts is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_pl_oper as meta
                                        return meta._meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.XlfpgaStats.MacsecRxStats.RxSaStat']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-pl-oper:macsec-rx-stats'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.rx_sa_stat is not None:
                                        for child_ref in self.rx_sa_stat:
                                            if child_ref._has_data():
                                                return True

                                    if self.sc_bad_tag_pkts is not None:
                                        return True

                                    if self.sc_decrypted_octets is not None:
                                        return True

                                    if self.sc_delayed_pkts is not None:
                                        return True

                                    if self.sc_invalid_pkts is not None:
                                        return True

                                    if self.sc_late_pkts is not None:
                                        return True

                                    if self.sc_no_sci_pkts is not None:
                                        return True

                                    if self.sc_no_tag_pkts is not None:
                                        return True

                                    if self.sc_not_using_pkts is not None:
                                        return True

                                    if self.sc_not_valid_pkts is not None:
                                        return True

                                    if self.sc_ok_pkts is not None:
                                        return True

                                    if self.sc_overrun_pkts is not None:
                                        return True

                                    if self.sc_unchecked_pkts is not None:
                                        return True

                                    if self.sc_unknown_sci_pkts is not None:
                                        return True

                                    if self.sc_untagged_pkts is not None:
                                        return True

                                    if self.sc_unused_pkts is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_pl_oper as meta
                                    return meta._meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.XlfpgaStats.MacsecRxStats']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-pl-oper:xlfpga-stats'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.macsec_rx_stats is not None and self.macsec_rx_stats._has_data():
                                    return True

                                if self.macsec_tx_stats is not None and self.macsec_tx_stats._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_pl_oper as meta
                                return meta._meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.XlfpgaStats']['meta_info']


                        class Es200Stats(object):
                            """
                            ES200 Stats
                            
                            .. attribute:: rx_interface_macsec_stats
                            
                            	Rx interface Macsec Stats
                            	**type**\:   :py:class:`RxInterfaceMacsecStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.Es200Stats.RxInterfaceMacsecStats>`
                            
                            .. attribute:: rx_sa_stats
                            
                            	Rx SA Stats
                            	**type**\:   :py:class:`RxSaStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.Es200Stats.RxSaStats>`
                            
                            .. attribute:: tx_interface_macsec_stats
                            
                            	Tx interface Macsec Stats
                            	**type**\:   :py:class:`TxInterfaceMacsecStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.Es200Stats.TxInterfaceMacsecStats>`
                            
                            .. attribute:: tx_sa_stats
                            
                            	Tx SA Stats
                            	**type**\:   :py:class:`TxSaStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.Es200Stats.TxSaStats>`
                            
                            

                            """

                            _prefix = 'crypto-macsec-pl-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.rx_interface_macsec_stats = Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.Es200Stats.RxInterfaceMacsecStats()
                                self.rx_interface_macsec_stats.parent = self
                                self.rx_sa_stats = Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.Es200Stats.RxSaStats()
                                self.rx_sa_stats.parent = self
                                self.tx_interface_macsec_stats = Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.Es200Stats.TxInterfaceMacsecStats()
                                self.tx_interface_macsec_stats.parent = self
                                self.tx_sa_stats = Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.Es200Stats.TxSaStats()
                                self.tx_sa_stats.parent = self


                            class TxSaStats(object):
                                """
                                Tx SA Stats
                                
                                .. attribute:: out_octets_encrypted_protected1
                                
                                	octets1 encrypted/protected ?
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: out_octets_encrypted_protected2
                                
                                	octets2 encrypted/protected ?
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: out_pkts_encrypted_protected
                                
                                	packets encrypted/protected
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: out_pkts_sa_not_in_use
                                
                                	packets coming on SA that is expired or otherwise not\-in\-use
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
                                    self.parent = None
                                    self.out_octets_encrypted_protected1 = None
                                    self.out_octets_encrypted_protected2 = None
                                    self.out_pkts_encrypted_protected = None
                                    self.out_pkts_sa_not_in_use = None
                                    self.out_pkts_too_long = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-pl-oper:tx-sa-stats'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.out_octets_encrypted_protected1 is not None:
                                        return True

                                    if self.out_octets_encrypted_protected2 is not None:
                                        return True

                                    if self.out_pkts_encrypted_protected is not None:
                                        return True

                                    if self.out_pkts_sa_not_in_use is not None:
                                        return True

                                    if self.out_pkts_too_long is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_pl_oper as meta
                                    return meta._meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.Es200Stats.TxSaStats']['meta_info']


                            class RxSaStats(object):
                                """
                                Rx SA Stats
                                
                                .. attribute:: in_octets_decrypted_validated1
                                
                                	octets1 decrypted/validated
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: in_octets_decrypted_validated2
                                
                                	octets2 decrypted/validated
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
                                
                                .. attribute:: in_pkts_sa_not_in_use
                                
                                	packets coming on SA that is
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
                                    self.parent = None
                                    self.in_octets_decrypted_validated1 = None
                                    self.in_octets_decrypted_validated2 = None
                                    self.in_octets_validated = None
                                    self.in_pkts_delayed = None
                                    self.in_pkts_invalid = None
                                    self.in_pkts_late = None
                                    self.in_pkts_not_using_sa = None
                                    self.in_pkts_not_valid = None
                                    self.in_pkts_ok = None
                                    self.in_pkts_sa_not_in_use = None
                                    self.in_pkts_unchecked = None
                                    self.in_pkts_unused_sa = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-pl-oper:rx-sa-stats'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.in_octets_decrypted_validated1 is not None:
                                        return True

                                    if self.in_octets_decrypted_validated2 is not None:
                                        return True

                                    if self.in_octets_validated is not None:
                                        return True

                                    if self.in_pkts_delayed is not None:
                                        return True

                                    if self.in_pkts_invalid is not None:
                                        return True

                                    if self.in_pkts_late is not None:
                                        return True

                                    if self.in_pkts_not_using_sa is not None:
                                        return True

                                    if self.in_pkts_not_valid is not None:
                                        return True

                                    if self.in_pkts_ok is not None:
                                        return True

                                    if self.in_pkts_sa_not_in_use is not None:
                                        return True

                                    if self.in_pkts_unchecked is not None:
                                        return True

                                    if self.in_pkts_unused_sa is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_pl_oper as meta
                                    return meta._meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.Es200Stats.RxSaStats']['meta_info']


                            class TxInterfaceMacsecStats(object):
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
                                    self.parent = None
                                    self.out_bcast_pkts_ctrl = None
                                    self.out_bcast_pkts_unctrl = None
                                    self.out_drop_pkts_class = None
                                    self.out_drop_pkts_data = None
                                    self.out_mcast_pkts_ctrl = None
                                    self.out_mcast_pkts_unctrl = None
                                    self.out_octets_common = None
                                    self.out_octets_ctrl = None
                                    self.out_octets_unctrl = None
                                    self.out_pkt_ctrl = None
                                    self.out_pkts_untagged = None
                                    self.out_rx_drop_pkts_ctrl = None
                                    self.out_rx_drop_pkts_unctrl = None
                                    self.out_rx_err_pkts_ctrl = None
                                    self.out_rx_err_pkts_unctrl = None
                                    self.out_ucast_pkts_ctrl = None
                                    self.out_ucast_pkts_unctrl = None
                                    self.transform_error_pkts = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-pl-oper:tx-interface-macsec-stats'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.out_bcast_pkts_ctrl is not None:
                                        return True

                                    if self.out_bcast_pkts_unctrl is not None:
                                        return True

                                    if self.out_drop_pkts_class is not None:
                                        return True

                                    if self.out_drop_pkts_data is not None:
                                        return True

                                    if self.out_mcast_pkts_ctrl is not None:
                                        return True

                                    if self.out_mcast_pkts_unctrl is not None:
                                        return True

                                    if self.out_octets_common is not None:
                                        return True

                                    if self.out_octets_ctrl is not None:
                                        return True

                                    if self.out_octets_unctrl is not None:
                                        return True

                                    if self.out_pkt_ctrl is not None:
                                        return True

                                    if self.out_pkts_untagged is not None:
                                        return True

                                    if self.out_rx_drop_pkts_ctrl is not None:
                                        return True

                                    if self.out_rx_drop_pkts_unctrl is not None:
                                        return True

                                    if self.out_rx_err_pkts_ctrl is not None:
                                        return True

                                    if self.out_rx_err_pkts_unctrl is not None:
                                        return True

                                    if self.out_ucast_pkts_ctrl is not None:
                                        return True

                                    if self.out_ucast_pkts_unctrl is not None:
                                        return True

                                    if self.transform_error_pkts is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_pl_oper as meta
                                    return meta._meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.Es200Stats.TxInterfaceMacsecStats']['meta_info']


                            class RxInterfaceMacsecStats(object):
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
                                
                                	correctly tagged ingress frames for which no valid SC found & \\;                              validateFrames is strict
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
                                    self.parent = None
                                    self.in_bcast_pkts_ctrl = None
                                    self.in_bcast_pkts_unctrl = None
                                    self.in_drop_pkts_class = None
                                    self.in_drop_pkts_data = None
                                    self.in_mcast_pkts_ctrl = None
                                    self.in_mcast_pkts_unctrl = None
                                    self.in_octets_ctrl = None
                                    self.in_octets_unctrl = None
                                    self.in_pkt_bad_tag = None
                                    self.in_pkt_ctrl = None
                                    self.in_pkt_no_sci = None
                                    self.in_pkt_no_tag = None
                                    self.in_pkts_tagged_ctrl = None
                                    self.in_pkts_unknown_sci = None
                                    self.in_pkts_untagged = None
                                    self.in_rx_drop_pkts_ctrl = None
                                    self.in_rx_drop_pkts_unctrl = None
                                    self.in_rx_error_pkts_ctrl = None
                                    self.in_rx_error_pkts_unctrl = None
                                    self.in_ucast_pkts_ctrl = None
                                    self.in_ucast_pkts_unctrl = None
                                    self.transform_error_pkts = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-pl-oper:rx-interface-macsec-stats'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.in_bcast_pkts_ctrl is not None:
                                        return True

                                    if self.in_bcast_pkts_unctrl is not None:
                                        return True

                                    if self.in_drop_pkts_class is not None:
                                        return True

                                    if self.in_drop_pkts_data is not None:
                                        return True

                                    if self.in_mcast_pkts_ctrl is not None:
                                        return True

                                    if self.in_mcast_pkts_unctrl is not None:
                                        return True

                                    if self.in_octets_ctrl is not None:
                                        return True

                                    if self.in_octets_unctrl is not None:
                                        return True

                                    if self.in_pkt_bad_tag is not None:
                                        return True

                                    if self.in_pkt_ctrl is not None:
                                        return True

                                    if self.in_pkt_no_sci is not None:
                                        return True

                                    if self.in_pkt_no_tag is not None:
                                        return True

                                    if self.in_pkts_tagged_ctrl is not None:
                                        return True

                                    if self.in_pkts_unknown_sci is not None:
                                        return True

                                    if self.in_pkts_untagged is not None:
                                        return True

                                    if self.in_rx_drop_pkts_ctrl is not None:
                                        return True

                                    if self.in_rx_drop_pkts_unctrl is not None:
                                        return True

                                    if self.in_rx_error_pkts_ctrl is not None:
                                        return True

                                    if self.in_rx_error_pkts_unctrl is not None:
                                        return True

                                    if self.in_ucast_pkts_ctrl is not None:
                                        return True

                                    if self.in_ucast_pkts_unctrl is not None:
                                        return True

                                    if self.transform_error_pkts is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_pl_oper as meta
                                    return meta._meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.Es200Stats.RxInterfaceMacsecStats']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-pl-oper:es200-stats'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.rx_interface_macsec_stats is not None and self.rx_interface_macsec_stats._has_data():
                                    return True

                                if self.rx_sa_stats is not None and self.rx_sa_stats._has_data():
                                    return True

                                if self.tx_interface_macsec_stats is not None and self.tx_interface_macsec_stats._has_data():
                                    return True

                                if self.tx_sa_stats is not None and self.tx_sa_stats._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_pl_oper as meta
                                return meta._meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.Es200Stats']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-pl-oper:sw-statistics'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.es200_stats is not None and self.es200_stats._has_data():
                                return True

                            if self.hw_type is not None:
                                return True

                            if self.msfpga_stats is not None and self.msfpga_stats._has_data():
                                return True

                            if self.xlfpga_stats is not None and self.xlfpga_stats._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_pl_oper as meta
                            return meta._meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwStatistics']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.name is None:
                            raise YPYModelError('Key property name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-pl-oper:interface[Cisco-IOS-XR-crypto-macsec-pl-oper:name = ' + str(self.name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.name is not None:
                            return True

                        if self.hw_flow_s is not None and self.hw_flow_s._has_data():
                            return True

                        if self.hw_sas is not None and self.hw_sas._has_data():
                            return True

                        if self.hw_statistics is not None and self.hw_statistics._has_data():
                            return True

                        if self.sw_flow_s is not None and self.sw_flow_s._has_data():
                            return True

                        if self.sw_sas is not None and self.sw_sas._has_data():
                            return True

                        if self.sw_statistics is not None and self.sw_statistics._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_pl_oper as meta
                        return meta._meta_table['Macsec.Nodes.Node.Interfaces.Interface']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-pl-oper:interfaces'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.interface is not None:
                        for child_ref in self.interface:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_pl_oper as meta
                    return meta._meta_table['Macsec.Nodes.Node.Interfaces']['meta_info']

            @property
            def _common_path(self):
                if self.node_name is None:
                    raise YPYModelError('Key property node_name is None')

                return '/Cisco-IOS-XR-crypto-macsec-pl-oper:macsec/Cisco-IOS-XR-crypto-macsec-pl-oper:nodes/Cisco-IOS-XR-crypto-macsec-pl-oper:node[Cisco-IOS-XR-crypto-macsec-pl-oper:node-name = ' + str(self.node_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.node_name is not None:
                    return True

                if self.interfaces is not None and self.interfaces._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_pl_oper as meta
                return meta._meta_table['Macsec.Nodes.Node']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-crypto-macsec-pl-oper:macsec/Cisco-IOS-XR-crypto-macsec-pl-oper:nodes'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.node is not None:
                for child_ref in self.node:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_pl_oper as meta
            return meta._meta_table['Macsec.Nodes']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-crypto-macsec-pl-oper:macsec'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.nodes is not None and self.nodes._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_pl_oper as meta
        return meta._meta_table['Macsec']['meta_info']


