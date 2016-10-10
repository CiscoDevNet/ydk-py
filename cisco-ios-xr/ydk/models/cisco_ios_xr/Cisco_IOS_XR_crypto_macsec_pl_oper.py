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
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes>`
    
    

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
        	**type**\: list of  :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node>`
        
        

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
            	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces>`
            
            

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
                	**type**\: list of  :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface>`
                
                

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
                    	**type**\:  :py:class:`HwFlowS <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.HwFlowS>`
                    
                    .. attribute:: hw_sas
                    
                    	Table of Hardware SAs
                    	**type**\:  :py:class:`HwSas <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.HwSas>`
                    
                    .. attribute:: hw_statistics
                    
                    	The Hardware Statistics
                    	**type**\:  :py:class:`HwStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.HwStatistics>`
                    
                    .. attribute:: sw_flow_s
                    
                    	Table of sofware Flows
                    	**type**\:  :py:class:`SwFlowS <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.SwFlowS>`
                    
                    .. attribute:: sw_sas
                    
                    	Table of Software SAs
                    	**type**\:  :py:class:`SwSas <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.SwSas>`
                    
                    .. attribute:: sw_statistics
                    
                    	The Software Statistics
                    	**type**\:  :py:class:`SwStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.SwStatistics>`
                    
                    

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
                        
                        .. attribute:: hw_type
                        
                        	Hardware Type
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: msfpga_stats
                        
                        	MSFPGA Stats
                        	**type**\:  :py:class:`MsfpgaStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.MsfpgaStats>`
                        
                        

                        """

                        _prefix = 'crypto-macsec-pl-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.hw_type = None
                            self.msfpga_stats = Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.MsfpgaStats()
                            self.msfpga_stats.parent = self


                        class MsfpgaStats(object):
                            """
                            MSFPGA Stats
                            
                            .. attribute:: rx_interface_macsec_stats
                            
                            	Rx interface Macsec Stats
                            	**type**\:  :py:class:`RxInterfaceMacsecStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.MsfpgaStats.RxInterfaceMacsecStats>`
                            
                            .. attribute:: rx_sa_stats
                            
                            	Rx SA Stats
                            	**type**\:  :py:class:`RxSaStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.MsfpgaStats.RxSaStats>`
                            
                            .. attribute:: tx_interface_macsec_stats
                            
                            	Tx interface Macsec Stats
                            	**type**\:  :py:class:`TxInterfaceMacsecStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.MsfpgaStats.TxInterfaceMacsecStats>`
                            
                            .. attribute:: tx_sa_stats
                            
                            	Tx SA Stats
                            	**type**\:  :py:class:`TxSaStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.MsfpgaStats.TxSaStats>`
                            
                            

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
                            if self.hw_type is not None:
                                return True

                            if self.msfpga_stats is not None and self.msfpga_stats._has_data():
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
                        	**type**\: list of  :py:class:`SwSa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa>`
                        
                        

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
                            
                            .. attribute:: hw_type
                            
                            	Hardware Type
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: msfpga_sa
                            
                            	MSFPGA SA Information
                            	**type**\:  :py:class:`MsfpgaSa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.MsfpgaSa>`
                            
                            

                            """

                            _prefix = 'crypto-macsec-pl-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.sa_id = None
                                self.hw_type = None
                                self.msfpga_sa = Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.MsfpgaSa()
                                self.msfpga_sa.parent = self


                            class MsfpgaSa(object):
                                """
                                MSFPGA SA Information
                                
                                .. attribute:: rx_sa
                                
                                	Rx SA Details
                                	**type**\:  :py:class:`RxSa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.MsfpgaSa.RxSa>`
                                
                                .. attribute:: tx_sa
                                
                                	Tx SA Details
                                	**type**\:  :py:class:`TxSa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.MsfpgaSa.TxSa>`
                                
                                

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

                                if self.hw_type is not None:
                                    return True

                                if self.msfpga_sa is not None and self.msfpga_sa._has_data():
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
                        	**type**\: list of  :py:class:`HwSa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa>`
                        
                        

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
                            
                            .. attribute:: hw_type
                            
                            	Hardware Type
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: msfpga_sa
                            
                            	MSFPGA SA Information
                            	**type**\:  :py:class:`MsfpgaSa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.MsfpgaSa>`
                            
                            

                            """

                            _prefix = 'crypto-macsec-pl-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.sa_id = None
                                self.hw_type = None
                                self.msfpga_sa = Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.MsfpgaSa()
                                self.msfpga_sa.parent = self


                            class MsfpgaSa(object):
                                """
                                MSFPGA SA Information
                                
                                .. attribute:: rx_sa
                                
                                	Rx SA Details
                                	**type**\:  :py:class:`RxSa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.MsfpgaSa.RxSa>`
                                
                                .. attribute:: tx_sa
                                
                                	Tx SA Details
                                	**type**\:  :py:class:`TxSa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.MsfpgaSa.TxSa>`
                                
                                

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

                                if self.hw_type is not None:
                                    return True

                                if self.msfpga_sa is not None and self.msfpga_sa._has_data():
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
                        	**type**\: list of  :py:class:`HwFlow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow>`
                        
                        

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
                            
                            .. attribute:: hw_type
                            
                            	Hardware Type
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: msfpga_flow
                            
                            	MSFPGA Flow Information
                            	**type**\:  :py:class:`MsfpgaFlow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.MsfpgaFlow>`
                            
                            

                            """

                            _prefix = 'crypto-macsec-pl-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.flow_id = None
                                self.hw_type = None
                                self.msfpga_flow = Macsec.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.MsfpgaFlow()
                                self.msfpga_flow.parent = self


                            class MsfpgaFlow(object):
                                """
                                MSFPGA Flow Information
                                
                                .. attribute:: rx_flow
                                
                                	Rx Flow Details
                                	**type**\:  :py:class:`RxFlow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.MsfpgaFlow.RxFlow>`
                                
                                .. attribute:: tx_flow
                                
                                	Tx Flow Details
                                	**type**\:  :py:class:`TxFlow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.MsfpgaFlow.TxFlow>`
                                
                                

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
                        	**type**\: list of  :py:class:`SwFlow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.SwFlowS.SwFlow>`
                        
                        

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
                            
                            .. attribute:: hw_type
                            
                            	Hardware Type
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: msfpga_flow
                            
                            	MSFPGA Flow Information
                            	**type**\:  :py:class:`MsfpgaFlow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.SwFlowS.SwFlow.MsfpgaFlow>`
                            
                            

                            """

                            _prefix = 'crypto-macsec-pl-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.flow_id = None
                                self.hw_type = None
                                self.msfpga_flow = Macsec.Nodes.Node.Interfaces.Interface.SwFlowS.SwFlow.MsfpgaFlow()
                                self.msfpga_flow.parent = self


                            class MsfpgaFlow(object):
                                """
                                MSFPGA Flow Information
                                
                                .. attribute:: rx_flow
                                
                                	Rx Flow Details
                                	**type**\:  :py:class:`RxFlow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.SwFlowS.SwFlow.MsfpgaFlow.RxFlow>`
                                
                                .. attribute:: tx_flow
                                
                                	Tx Flow Details
                                	**type**\:  :py:class:`TxFlow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.SwFlowS.SwFlow.MsfpgaFlow.TxFlow>`
                                
                                

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
                        
                        .. attribute:: hw_type
                        
                        	Hardware Type
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: msfpga_stats
                        
                        	MSFPGA Stats
                        	**type**\:  :py:class:`MsfpgaStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.MsfpgaStats>`
                        
                        

                        """

                        _prefix = 'crypto-macsec-pl-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.hw_type = None
                            self.msfpga_stats = Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.MsfpgaStats()
                            self.msfpga_stats.parent = self


                        class MsfpgaStats(object):
                            """
                            MSFPGA Stats
                            
                            .. attribute:: rx_interface_macsec_stats
                            
                            	Rx interface Macsec Stats
                            	**type**\:  :py:class:`RxInterfaceMacsecStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.MsfpgaStats.RxInterfaceMacsecStats>`
                            
                            .. attribute:: rx_sa_stats
                            
                            	Rx SA Stats
                            	**type**\:  :py:class:`RxSaStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.MsfpgaStats.RxSaStats>`
                            
                            .. attribute:: tx_interface_macsec_stats
                            
                            	Tx interface Macsec Stats
                            	**type**\:  :py:class:`TxInterfaceMacsecStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.MsfpgaStats.TxInterfaceMacsecStats>`
                            
                            .. attribute:: tx_sa_stats
                            
                            	Tx SA Stats
                            	**type**\:  :py:class:`TxSaStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper.Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.MsfpgaStats.TxSaStats>`
                            
                            

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
                            if self.hw_type is not None:
                                return True

                            if self.msfpga_stats is not None and self.msfpga_stats._has_data():
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


