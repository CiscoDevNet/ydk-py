""" Cisco_IOS_XR_crypto_macsec_secy_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR crypto\-macsec\-secy package operational data.

This module contains definitions
for the following management objects\:
  macsec\: Macsec operational data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class Macsec(Entity):
    """
    Macsec operational data
    
    .. attribute:: secy
    
    	MAC Security Entity
    	**type**\:  :py:class:`Secy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_secy_oper.Macsec.Secy>`
    
    

    """

    _prefix = 'crypto-macsec-secy-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Macsec, self).__init__()
        self._top_entity = None

        self.yang_name = "macsec"
        self.yang_parent_name = "Cisco-IOS-XR-crypto-macsec-secy-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("secy", ("secy", Macsec.Secy))])
        self._leafs = OrderedDict()

        self.secy = Macsec.Secy()
        self.secy.parent = self
        self._children_name_map["secy"] = "secy"
        self._segment_path = lambda: "Cisco-IOS-XR-crypto-macsec-secy-oper:macsec"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Macsec, [], name, value)


    class Secy(Entity):
        """
        MAC Security Entity
        
        .. attribute:: interfaces
        
        	MAC Security Data
        	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_secy_oper.Macsec.Secy.Interfaces>`
        
        

        """

        _prefix = 'crypto-macsec-secy-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Macsec.Secy, self).__init__()

            self.yang_name = "secy"
            self.yang_parent_name = "macsec"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("interfaces", ("interfaces", Macsec.Secy.Interfaces))])
            self._leafs = OrderedDict()

            self.interfaces = Macsec.Secy.Interfaces()
            self.interfaces.parent = self
            self._children_name_map["interfaces"] = "interfaces"
            self._segment_path = lambda: "secy"
            self._absolute_path = lambda: "Cisco-IOS-XR-crypto-macsec-secy-oper:macsec/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Macsec.Secy, [], name, value)


        class Interfaces(Entity):
            """
            MAC Security Data
            
            .. attribute:: interface
            
            	MAC Security Data for the Interface
            	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_secy_oper.Macsec.Secy.Interfaces.Interface>`
            
            

            """

            _prefix = 'crypto-macsec-secy-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Macsec.Secy.Interfaces, self).__init__()

                self.yang_name = "interfaces"
                self.yang_parent_name = "secy"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("interface", ("interface", Macsec.Secy.Interfaces.Interface))])
                self._leafs = OrderedDict()

                self.interface = YList(self)
                self._segment_path = lambda: "interfaces"
                self._absolute_path = lambda: "Cisco-IOS-XR-crypto-macsec-secy-oper:macsec/secy/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Macsec.Secy.Interfaces, [], name, value)


            class Interface(Entity):
                """
                MAC Security Data for the Interface
                
                .. attribute:: name  (key)
                
                	Interface Name
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                .. attribute:: stats
                
                	MACsec Stats
                	**type**\:  :py:class:`Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_secy_oper.Macsec.Secy.Interfaces.Interface.Stats>`
                
                

                """

                _prefix = 'crypto-macsec-secy-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Macsec.Secy.Interfaces.Interface, self).__init__()

                    self.yang_name = "interface"
                    self.yang_parent_name = "interfaces"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['name']
                    self._child_classes = OrderedDict([("stats", ("stats", Macsec.Secy.Interfaces.Interface.Stats))])
                    self._leafs = OrderedDict([
                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                    ])
                    self.name = None

                    self.stats = Macsec.Secy.Interfaces.Interface.Stats()
                    self.stats.parent = self
                    self._children_name_map["stats"] = "stats"
                    self._segment_path = lambda: "interface" + "[name='" + str(self.name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-crypto-macsec-secy-oper:macsec/secy/interfaces/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Macsec.Secy.Interfaces.Interface, ['name'], name, value)


                class Stats(Entity):
                    """
                    MACsec Stats
                    
                    .. attribute:: intf_stats
                    
                    	Interface stats
                    	**type**\:  :py:class:`IntfStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_secy_oper.Macsec.Secy.Interfaces.Interface.Stats.IntfStats>`
                    
                    .. attribute:: tx_sc_stats
                    
                    	Tx SC Stats
                    	**type**\:  :py:class:`TxScStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_secy_oper.Macsec.Secy.Interfaces.Interface.Stats.TxScStats>`
                    
                    .. attribute:: rx_sc_stats
                    
                    	RX SC Stats List
                    	**type**\: list of  		 :py:class:`RxScStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_secy_oper.Macsec.Secy.Interfaces.Interface.Stats.RxScStats>`
                    
                    

                    """

                    _prefix = 'crypto-macsec-secy-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Macsec.Secy.Interfaces.Interface.Stats, self).__init__()

                        self.yang_name = "stats"
                        self.yang_parent_name = "interface"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("intf-stats", ("intf_stats", Macsec.Secy.Interfaces.Interface.Stats.IntfStats)), ("tx-sc-stats", ("tx_sc_stats", Macsec.Secy.Interfaces.Interface.Stats.TxScStats)), ("rx-sc-stats", ("rx_sc_stats", Macsec.Secy.Interfaces.Interface.Stats.RxScStats))])
                        self._leafs = OrderedDict()

                        self.intf_stats = Macsec.Secy.Interfaces.Interface.Stats.IntfStats()
                        self.intf_stats.parent = self
                        self._children_name_map["intf_stats"] = "intf-stats"

                        self.tx_sc_stats = Macsec.Secy.Interfaces.Interface.Stats.TxScStats()
                        self.tx_sc_stats.parent = self
                        self._children_name_map["tx_sc_stats"] = "tx-sc-stats"

                        self.rx_sc_stats = YList(self)
                        self._segment_path = lambda: "stats"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Macsec.Secy.Interfaces.Interface.Stats, [], name, value)


                    class IntfStats(Entity):
                        """
                        Interface stats
                        
                        .. attribute:: in_pkts_untagged
                        
                        	InPktsUntagged
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_pkts_no_tag
                        
                        	InPktsNoTag
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_pkts_bad_tag
                        
                        	InPktsBadTag
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_pkts_unknown_sci
                        
                        	InPktsUnknownSCI
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_pkts_no_sci
                        
                        	InPktsNoSCI
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_pkts_overrun
                        
                        	InPktsOverrun
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_octets_validated
                        
                        	InOctetsValidated
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_octets_decrypted
                        
                        	InOctetsDecrypted
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: out_pkts_untagged
                        
                        	OutPktsUntagged
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: out_pkts_too_long
                        
                        	OutPktsTooLong
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: out_octets_protected
                        
                        	OutOctetsProtected
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: out_octets_encrypted
                        
                        	OutOctetsEncrypted
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'crypto-macsec-secy-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Macsec.Secy.Interfaces.Interface.Stats.IntfStats, self).__init__()

                            self.yang_name = "intf-stats"
                            self.yang_parent_name = "stats"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('in_pkts_untagged', (YLeaf(YType.uint64, 'in-pkts-untagged'), ['int'])),
                                ('in_pkts_no_tag', (YLeaf(YType.uint64, 'in-pkts-no-tag'), ['int'])),
                                ('in_pkts_bad_tag', (YLeaf(YType.uint64, 'in-pkts-bad-tag'), ['int'])),
                                ('in_pkts_unknown_sci', (YLeaf(YType.uint64, 'in-pkts-unknown-sci'), ['int'])),
                                ('in_pkts_no_sci', (YLeaf(YType.uint64, 'in-pkts-no-sci'), ['int'])),
                                ('in_pkts_overrun', (YLeaf(YType.uint64, 'in-pkts-overrun'), ['int'])),
                                ('in_octets_validated', (YLeaf(YType.uint64, 'in-octets-validated'), ['int'])),
                                ('in_octets_decrypted', (YLeaf(YType.uint64, 'in-octets-decrypted'), ['int'])),
                                ('out_pkts_untagged', (YLeaf(YType.uint64, 'out-pkts-untagged'), ['int'])),
                                ('out_pkts_too_long', (YLeaf(YType.uint64, 'out-pkts-too-long'), ['int'])),
                                ('out_octets_protected', (YLeaf(YType.uint64, 'out-octets-protected'), ['int'])),
                                ('out_octets_encrypted', (YLeaf(YType.uint64, 'out-octets-encrypted'), ['int'])),
                            ])
                            self.in_pkts_untagged = None
                            self.in_pkts_no_tag = None
                            self.in_pkts_bad_tag = None
                            self.in_pkts_unknown_sci = None
                            self.in_pkts_no_sci = None
                            self.in_pkts_overrun = None
                            self.in_octets_validated = None
                            self.in_octets_decrypted = None
                            self.out_pkts_untagged = None
                            self.out_pkts_too_long = None
                            self.out_octets_protected = None
                            self.out_octets_encrypted = None
                            self._segment_path = lambda: "intf-stats"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Macsec.Secy.Interfaces.Interface.Stats.IntfStats, ['in_pkts_untagged', 'in_pkts_no_tag', 'in_pkts_bad_tag', 'in_pkts_unknown_sci', 'in_pkts_no_sci', 'in_pkts_overrun', 'in_octets_validated', 'in_octets_decrypted', 'out_pkts_untagged', 'out_pkts_too_long', 'out_octets_protected', 'out_octets_encrypted'], name, value)


                    class TxScStats(Entity):
                        """
                        Tx SC Stats
                        
                        .. attribute:: tx_sci
                        
                        	Tx SCI
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: out_pkts_protected
                        
                        	OutPktsProtected
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: out_pkts_encrypted
                        
                        	OutPktsEncrypted
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: out_octets_protected
                        
                        	OutOctetsProtected
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: out_octets_encrypted
                        
                        	OutOctetsEncrypted
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: out_pkts_too_long
                        
                        	OutPktsTooLong
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: txsa_stat
                        
                        	tx sa stats
                        	**type**\: list of  		 :py:class:`TxsaStat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_secy_oper.Macsec.Secy.Interfaces.Interface.Stats.TxScStats.TxsaStat>`
                        
                        

                        """

                        _prefix = 'crypto-macsec-secy-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Macsec.Secy.Interfaces.Interface.Stats.TxScStats, self).__init__()

                            self.yang_name = "tx-sc-stats"
                            self.yang_parent_name = "stats"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("txsa-stat", ("txsa_stat", Macsec.Secy.Interfaces.Interface.Stats.TxScStats.TxsaStat))])
                            self._leafs = OrderedDict([
                                ('tx_sci', (YLeaf(YType.uint64, 'tx-sci'), ['int'])),
                                ('out_pkts_protected', (YLeaf(YType.uint64, 'out-pkts-protected'), ['int'])),
                                ('out_pkts_encrypted', (YLeaf(YType.uint64, 'out-pkts-encrypted'), ['int'])),
                                ('out_octets_protected', (YLeaf(YType.uint64, 'out-octets-protected'), ['int'])),
                                ('out_octets_encrypted', (YLeaf(YType.uint64, 'out-octets-encrypted'), ['int'])),
                                ('out_pkts_too_long', (YLeaf(YType.uint64, 'out-pkts-too-long'), ['int'])),
                            ])
                            self.tx_sci = None
                            self.out_pkts_protected = None
                            self.out_pkts_encrypted = None
                            self.out_octets_protected = None
                            self.out_octets_encrypted = None
                            self.out_pkts_too_long = None

                            self.txsa_stat = YList(self)
                            self._segment_path = lambda: "tx-sc-stats"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Macsec.Secy.Interfaces.Interface.Stats.TxScStats, ['tx_sci', 'out_pkts_protected', 'out_pkts_encrypted', 'out_octets_protected', 'out_octets_encrypted', 'out_pkts_too_long'], name, value)


                        class TxsaStat(Entity):
                            """
                            tx sa stats
                            
                            .. attribute:: out_pkts_protected
                            
                            	OutPktsProtected
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: out_pkts_encrypted
                            
                            	OutPktsEncrypted
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: next_pn
                            
                            	NextPN
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'crypto-macsec-secy-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Macsec.Secy.Interfaces.Interface.Stats.TxScStats.TxsaStat, self).__init__()

                                self.yang_name = "txsa-stat"
                                self.yang_parent_name = "tx-sc-stats"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('out_pkts_protected', (YLeaf(YType.uint64, 'out-pkts-protected'), ['int'])),
                                    ('out_pkts_encrypted', (YLeaf(YType.uint64, 'out-pkts-encrypted'), ['int'])),
                                    ('next_pn', (YLeaf(YType.uint64, 'next-pn'), ['int'])),
                                ])
                                self.out_pkts_protected = None
                                self.out_pkts_encrypted = None
                                self.next_pn = None
                                self._segment_path = lambda: "txsa-stat"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Macsec.Secy.Interfaces.Interface.Stats.TxScStats.TxsaStat, ['out_pkts_protected', 'out_pkts_encrypted', 'next_pn'], name, value)


                    class RxScStats(Entity):
                        """
                        RX SC Stats List
                        
                        .. attribute:: rx_sci
                        
                        	Rx SCI
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_pkts_unchecked
                        
                        	InPktsUnchecked
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_pkts_delayed
                        
                        	InPktsDelayed
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_pkts_late
                        
                        	InPktsLate
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_pkts_ok
                        
                        	InPktsOK
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_pkts_invalid
                        
                        	InPktsInvalid
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_pkts_not_valid
                        
                        	InPktsNotValid
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_pkts_not_using_sa
                        
                        	InPktsNotUsingSA
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_pkts_unused_sa
                        
                        	InPktsUnusedSA
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_pkts_untagged_hit
                        
                        	InPktsUntaggedHit
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_octets_validated
                        
                        	InOctetsValidated
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_octets_decrypted
                        
                        	InOctetsDecrypted
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: rxsa_stat
                        
                        	rxsa stats
                        	**type**\: list of  		 :py:class:`RxsaStat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_secy_oper.Macsec.Secy.Interfaces.Interface.Stats.RxScStats.RxsaStat>`
                        
                        

                        """

                        _prefix = 'crypto-macsec-secy-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Macsec.Secy.Interfaces.Interface.Stats.RxScStats, self).__init__()

                            self.yang_name = "rx-sc-stats"
                            self.yang_parent_name = "stats"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("rxsa-stat", ("rxsa_stat", Macsec.Secy.Interfaces.Interface.Stats.RxScStats.RxsaStat))])
                            self._leafs = OrderedDict([
                                ('rx_sci', (YLeaf(YType.uint64, 'rx-sci'), ['int'])),
                                ('in_pkts_unchecked', (YLeaf(YType.uint64, 'in-pkts-unchecked'), ['int'])),
                                ('in_pkts_delayed', (YLeaf(YType.uint64, 'in-pkts-delayed'), ['int'])),
                                ('in_pkts_late', (YLeaf(YType.uint64, 'in-pkts-late'), ['int'])),
                                ('in_pkts_ok', (YLeaf(YType.uint64, 'in-pkts-ok'), ['int'])),
                                ('in_pkts_invalid', (YLeaf(YType.uint64, 'in-pkts-invalid'), ['int'])),
                                ('in_pkts_not_valid', (YLeaf(YType.uint64, 'in-pkts-not-valid'), ['int'])),
                                ('in_pkts_not_using_sa', (YLeaf(YType.uint64, 'in-pkts-not-using-sa'), ['int'])),
                                ('in_pkts_unused_sa', (YLeaf(YType.uint64, 'in-pkts-unused-sa'), ['int'])),
                                ('in_pkts_untagged_hit', (YLeaf(YType.uint64, 'in-pkts-untagged-hit'), ['int'])),
                                ('in_octets_validated', (YLeaf(YType.uint64, 'in-octets-validated'), ['int'])),
                                ('in_octets_decrypted', (YLeaf(YType.uint64, 'in-octets-decrypted'), ['int'])),
                            ])
                            self.rx_sci = None
                            self.in_pkts_unchecked = None
                            self.in_pkts_delayed = None
                            self.in_pkts_late = None
                            self.in_pkts_ok = None
                            self.in_pkts_invalid = None
                            self.in_pkts_not_valid = None
                            self.in_pkts_not_using_sa = None
                            self.in_pkts_unused_sa = None
                            self.in_pkts_untagged_hit = None
                            self.in_octets_validated = None
                            self.in_octets_decrypted = None

                            self.rxsa_stat = YList(self)
                            self._segment_path = lambda: "rx-sc-stats"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Macsec.Secy.Interfaces.Interface.Stats.RxScStats, ['rx_sci', 'in_pkts_unchecked', 'in_pkts_delayed', 'in_pkts_late', 'in_pkts_ok', 'in_pkts_invalid', 'in_pkts_not_valid', 'in_pkts_not_using_sa', 'in_pkts_unused_sa', 'in_pkts_untagged_hit', 'in_octets_validated', 'in_octets_decrypted'], name, value)


                        class RxsaStat(Entity):
                            """
                            rxsa stats
                            
                            .. attribute:: in_pkts_ok
                            
                            	InPktsOK
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in_pkts_invalid
                            
                            	InPktsInvalid
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in_pkts_not_valid
                            
                            	InPktsNotValid
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in_pkts_not_using_sa
                            
                            	InPktsNotUsingSA
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in_pkts_unused_sa
                            
                            	InPktsUnusedSA
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: next_pn
                            
                            	NextPN
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'crypto-macsec-secy-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Macsec.Secy.Interfaces.Interface.Stats.RxScStats.RxsaStat, self).__init__()

                                self.yang_name = "rxsa-stat"
                                self.yang_parent_name = "rx-sc-stats"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('in_pkts_ok', (YLeaf(YType.uint64, 'in-pkts-ok'), ['int'])),
                                    ('in_pkts_invalid', (YLeaf(YType.uint64, 'in-pkts-invalid'), ['int'])),
                                    ('in_pkts_not_valid', (YLeaf(YType.uint64, 'in-pkts-not-valid'), ['int'])),
                                    ('in_pkts_not_using_sa', (YLeaf(YType.uint64, 'in-pkts-not-using-sa'), ['int'])),
                                    ('in_pkts_unused_sa', (YLeaf(YType.uint64, 'in-pkts-unused-sa'), ['int'])),
                                    ('next_pn', (YLeaf(YType.uint64, 'next-pn'), ['int'])),
                                ])
                                self.in_pkts_ok = None
                                self.in_pkts_invalid = None
                                self.in_pkts_not_valid = None
                                self.in_pkts_not_using_sa = None
                                self.in_pkts_unused_sa = None
                                self.next_pn = None
                                self._segment_path = lambda: "rxsa-stat"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Macsec.Secy.Interfaces.Interface.Stats.RxScStats.RxsaStat, ['in_pkts_ok', 'in_pkts_invalid', 'in_pkts_not_valid', 'in_pkts_not_using_sa', 'in_pkts_unused_sa', 'next_pn'], name, value)

    def clone_ptr(self):
        self._top_entity = Macsec()
        return self._top_entity

