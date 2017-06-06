""" Cisco_IOS_XR_crypto_macsec_secy_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR crypto\-macsec\-secy package operational data.

This module contains definitions
for the following management objects\:
  macsec\: Macsec operational data

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
    Macsec operational data
    
    .. attribute:: secy
    
    	MAC Security Entity
    	**type**\:   :py:class:`Secy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_secy_oper.Macsec.Secy>`
    
    

    """

    _prefix = 'crypto-macsec-secy-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.secy = Macsec.Secy()
        self.secy.parent = self


    class Secy(object):
        """
        MAC Security Entity
        
        .. attribute:: interfaces
        
        	MAC Security Data
        	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_secy_oper.Macsec.Secy.Interfaces>`
        
        

        """

        _prefix = 'crypto-macsec-secy-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.interfaces = Macsec.Secy.Interfaces()
            self.interfaces.parent = self


        class Interfaces(object):
            """
            MAC Security Data
            
            .. attribute:: interface
            
            	MAC Security Data for the Interface
            	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_secy_oper.Macsec.Secy.Interfaces.Interface>`
            
            

            """

            _prefix = 'crypto-macsec-secy-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.interface = YList()
                self.interface.parent = self
                self.interface.name = 'interface'


            class Interface(object):
                """
                MAC Security Data for the Interface
                
                .. attribute:: name  <key>
                
                	Interface Name
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: stats
                
                	MACsec Stats
                	**type**\:   :py:class:`Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_secy_oper.Macsec.Secy.Interfaces.Interface.Stats>`
                
                

                """

                _prefix = 'crypto-macsec-secy-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.name = None
                    self.stats = Macsec.Secy.Interfaces.Interface.Stats()
                    self.stats.parent = self


                class Stats(object):
                    """
                    MACsec Stats
                    
                    .. attribute:: intf_stats
                    
                    	Interface stats
                    	**type**\:   :py:class:`IntfStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_secy_oper.Macsec.Secy.Interfaces.Interface.Stats.IntfStats>`
                    
                    .. attribute:: rx_sc_stats
                    
                    	RX SC Stats List
                    	**type**\: list of    :py:class:`RxScStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_secy_oper.Macsec.Secy.Interfaces.Interface.Stats.RxScStats>`
                    
                    .. attribute:: tx_sc_stats
                    
                    	Tx SC Stats
                    	**type**\:   :py:class:`TxScStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_secy_oper.Macsec.Secy.Interfaces.Interface.Stats.TxScStats>`
                    
                    

                    """

                    _prefix = 'crypto-macsec-secy-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.intf_stats = Macsec.Secy.Interfaces.Interface.Stats.IntfStats()
                        self.intf_stats.parent = self
                        self.rx_sc_stats = YList()
                        self.rx_sc_stats.parent = self
                        self.rx_sc_stats.name = 'rx_sc_stats'
                        self.tx_sc_stats = Macsec.Secy.Interfaces.Interface.Stats.TxScStats()
                        self.tx_sc_stats.parent = self


                    class IntfStats(object):
                        """
                        Interface stats
                        
                        .. attribute:: in_octets_decrypted
                        
                        	InOctetsDecrypted
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_octets_validated
                        
                        	InOctetsValidated
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_pkts_bad_tag
                        
                        	InPktsBadTag
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_pkts_no_sci
                        
                        	InPktsNoSCI
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_pkts_no_tag
                        
                        	InPktsNoTag
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_pkts_overrun
                        
                        	InPktsOverrun
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_pkts_unknown_sci
                        
                        	InPktsUnknownSCI
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_pkts_untagged
                        
                        	InPktsUntagged
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: out_octets_encrypted
                        
                        	OutOctetsEncrypted
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: out_octets_protected
                        
                        	OutOctetsProtected
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: out_pkts_too_long
                        
                        	OutPktsTooLong
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: out_pkts_untagged
                        
                        	OutPktsUntagged
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'crypto-macsec-secy-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.in_octets_decrypted = None
                            self.in_octets_validated = None
                            self.in_pkts_bad_tag = None
                            self.in_pkts_no_sci = None
                            self.in_pkts_no_tag = None
                            self.in_pkts_overrun = None
                            self.in_pkts_unknown_sci = None
                            self.in_pkts_untagged = None
                            self.out_octets_encrypted = None
                            self.out_octets_protected = None
                            self.out_pkts_too_long = None
                            self.out_pkts_untagged = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-secy-oper:intf-stats'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.in_octets_decrypted is not None:
                                return True

                            if self.in_octets_validated is not None:
                                return True

                            if self.in_pkts_bad_tag is not None:
                                return True

                            if self.in_pkts_no_sci is not None:
                                return True

                            if self.in_pkts_no_tag is not None:
                                return True

                            if self.in_pkts_overrun is not None:
                                return True

                            if self.in_pkts_unknown_sci is not None:
                                return True

                            if self.in_pkts_untagged is not None:
                                return True

                            if self.out_octets_encrypted is not None:
                                return True

                            if self.out_octets_protected is not None:
                                return True

                            if self.out_pkts_too_long is not None:
                                return True

                            if self.out_pkts_untagged is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_secy_oper as meta
                            return meta._meta_table['Macsec.Secy.Interfaces.Interface.Stats.IntfStats']['meta_info']


                    class TxScStats(object):
                        """
                        Tx SC Stats
                        
                        .. attribute:: out_octets_encrypted
                        
                        	OutOctetsEncrypted
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: out_octets_protected
                        
                        	OutOctetsProtected
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: out_pkts_encrypted
                        
                        	OutPktsEncrypted
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: out_pkts_protected
                        
                        	OutPktsProtected
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: out_pkts_too_long
                        
                        	OutPktsTooLong
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: tx_sci
                        
                        	Tx SCI
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'crypto-macsec-secy-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.out_octets_encrypted = None
                            self.out_octets_protected = None
                            self.out_pkts_encrypted = None
                            self.out_pkts_protected = None
                            self.out_pkts_too_long = None
                            self.tx_sci = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-secy-oper:tx-sc-stats'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.out_octets_encrypted is not None:
                                return True

                            if self.out_octets_protected is not None:
                                return True

                            if self.out_pkts_encrypted is not None:
                                return True

                            if self.out_pkts_protected is not None:
                                return True

                            if self.out_pkts_too_long is not None:
                                return True

                            if self.tx_sci is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_secy_oper as meta
                            return meta._meta_table['Macsec.Secy.Interfaces.Interface.Stats.TxScStats']['meta_info']


                    class RxScStats(object):
                        """
                        RX SC Stats List
                        
                        .. attribute:: in_octets_decrypted
                        
                        	InOctetsDecrypted
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_octets_validated
                        
                        	InOctetsValidated
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_pkts_delayed
                        
                        	InPktsDelayed
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_pkts_invalid
                        
                        	InPktsInvalid
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_pkts_late
                        
                        	InPktsLate
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_pkts_not_using_sa
                        
                        	InPktsNotUsingSA
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_pkts_not_valid
                        
                        	InPktsNotValid
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_pkts_ok
                        
                        	InPktsOK
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_pkts_unchecked
                        
                        	InPktsUnchecked
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_pkts_untagged_hit
                        
                        	InPktsUntaggedHit
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_pkts_unused_sa
                        
                        	InPktsUnusedSA
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: rx_sci
                        
                        	Rx SCI
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'crypto-macsec-secy-oper'
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
                            self.in_pkts_untagged_hit = None
                            self.in_pkts_unused_sa = None
                            self.rx_sci = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-secy-oper:rx-sc-stats'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
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

                            if self.in_pkts_untagged_hit is not None:
                                return True

                            if self.in_pkts_unused_sa is not None:
                                return True

                            if self.rx_sci is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_secy_oper as meta
                            return meta._meta_table['Macsec.Secy.Interfaces.Interface.Stats.RxScStats']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-secy-oper:stats'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.intf_stats is not None and self.intf_stats._has_data():
                            return True

                        if self.rx_sc_stats is not None:
                            for child_ref in self.rx_sc_stats:
                                if child_ref._has_data():
                                    return True

                        if self.tx_sc_stats is not None and self.tx_sc_stats._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_secy_oper as meta
                        return meta._meta_table['Macsec.Secy.Interfaces.Interface.Stats']['meta_info']

                @property
                def _common_path(self):
                    if self.name is None:
                        raise YPYModelError('Key property name is None')

                    return '/Cisco-IOS-XR-crypto-macsec-secy-oper:macsec/Cisco-IOS-XR-crypto-macsec-secy-oper:secy/Cisco-IOS-XR-crypto-macsec-secy-oper:interfaces/Cisco-IOS-XR-crypto-macsec-secy-oper:interface[Cisco-IOS-XR-crypto-macsec-secy-oper:name = ' + str(self.name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.name is not None:
                        return True

                    if self.stats is not None and self.stats._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_secy_oper as meta
                    return meta._meta_table['Macsec.Secy.Interfaces.Interface']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-crypto-macsec-secy-oper:macsec/Cisco-IOS-XR-crypto-macsec-secy-oper:secy/Cisco-IOS-XR-crypto-macsec-secy-oper:interfaces'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.interface is not None:
                    for child_ref in self.interface:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_secy_oper as meta
                return meta._meta_table['Macsec.Secy.Interfaces']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-crypto-macsec-secy-oper:macsec/Cisco-IOS-XR-crypto-macsec-secy-oper:secy'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.interfaces is not None and self.interfaces._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_secy_oper as meta
            return meta._meta_table['Macsec.Secy']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-crypto-macsec-secy-oper:macsec'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.secy is not None and self.secy._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_secy_oper as meta
        return meta._meta_table['Macsec']['meta_info']


