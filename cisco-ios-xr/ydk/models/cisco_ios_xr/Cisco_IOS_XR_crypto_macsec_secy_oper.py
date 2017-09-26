""" Cisco_IOS_XR_crypto_macsec_secy_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR crypto\-macsec\-secy package operational data.

This module contains definitions
for the following management objects\:
  macsec\: Macsec operational data

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Macsec(Entity):
    """
    Macsec operational data
    
    .. attribute:: secy
    
    	MAC Security Entity
    	**type**\:   :py:class:`Secy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_secy_oper.Macsec.Secy>`
    
    

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
        self._child_container_classes = {"secy" : ("secy", Macsec.Secy)}
        self._child_list_classes = {}

        self.secy = Macsec.Secy()
        self.secy.parent = self
        self._children_name_map["secy"] = "secy"
        self._children_yang_names.add("secy")
        self._segment_path = lambda: "Cisco-IOS-XR-crypto-macsec-secy-oper:macsec"


    class Secy(Entity):
        """
        MAC Security Entity
        
        .. attribute:: interfaces
        
        	MAC Security Data
        	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_secy_oper.Macsec.Secy.Interfaces>`
        
        

        """

        _prefix = 'crypto-macsec-secy-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Macsec.Secy, self).__init__()

            self.yang_name = "secy"
            self.yang_parent_name = "macsec"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"interfaces" : ("interfaces", Macsec.Secy.Interfaces)}
            self._child_list_classes = {}

            self.interfaces = Macsec.Secy.Interfaces()
            self.interfaces.parent = self
            self._children_name_map["interfaces"] = "interfaces"
            self._children_yang_names.add("interfaces")
            self._segment_path = lambda: "secy"
            self._absolute_path = lambda: "Cisco-IOS-XR-crypto-macsec-secy-oper:macsec/%s" % self._segment_path()


        class Interfaces(Entity):
            """
            MAC Security Data
            
            .. attribute:: interface
            
            	MAC Security Data for the Interface
            	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_secy_oper.Macsec.Secy.Interfaces.Interface>`
            
            

            """

            _prefix = 'crypto-macsec-secy-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Macsec.Secy.Interfaces, self).__init__()

                self.yang_name = "interfaces"
                self.yang_parent_name = "secy"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"interface" : ("interface", Macsec.Secy.Interfaces.Interface)}

                self.interface = YList(self)
                self._segment_path = lambda: "interfaces"
                self._absolute_path = lambda: "Cisco-IOS-XR-crypto-macsec-secy-oper:macsec/secy/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Macsec.Secy.Interfaces, [], name, value)


            class Interface(Entity):
                """
                MAC Security Data for the Interface
                
                .. attribute:: name  <key>
                
                	Interface Name
                	**type**\:  str
                
                	**pattern:** [a\-zA\-Z0\-9./\-]+
                
                .. attribute:: stats
                
                	MACsec Stats
                	**type**\:   :py:class:`Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_secy_oper.Macsec.Secy.Interfaces.Interface.Stats>`
                
                

                """

                _prefix = 'crypto-macsec-secy-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Macsec.Secy.Interfaces.Interface, self).__init__()

                    self.yang_name = "interface"
                    self.yang_parent_name = "interfaces"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"stats" : ("stats", Macsec.Secy.Interfaces.Interface.Stats)}
                    self._child_list_classes = {}

                    self.name = YLeaf(YType.str, "name")

                    self.stats = Macsec.Secy.Interfaces.Interface.Stats()
                    self.stats.parent = self
                    self._children_name_map["stats"] = "stats"
                    self._children_yang_names.add("stats")
                    self._segment_path = lambda: "interface" + "[name='" + self.name.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-crypto-macsec-secy-oper:macsec/secy/interfaces/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Macsec.Secy.Interfaces.Interface, ['name'], name, value)


                class Stats(Entity):
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
                        super(Macsec.Secy.Interfaces.Interface.Stats, self).__init__()

                        self.yang_name = "stats"
                        self.yang_parent_name = "interface"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"intf-stats" : ("intf_stats", Macsec.Secy.Interfaces.Interface.Stats.IntfStats), "tx-sc-stats" : ("tx_sc_stats", Macsec.Secy.Interfaces.Interface.Stats.TxScStats)}
                        self._child_list_classes = {"rx-sc-stats" : ("rx_sc_stats", Macsec.Secy.Interfaces.Interface.Stats.RxScStats)}

                        self.intf_stats = Macsec.Secy.Interfaces.Interface.Stats.IntfStats()
                        self.intf_stats.parent = self
                        self._children_name_map["intf_stats"] = "intf-stats"
                        self._children_yang_names.add("intf-stats")

                        self.tx_sc_stats = Macsec.Secy.Interfaces.Interface.Stats.TxScStats()
                        self.tx_sc_stats.parent = self
                        self._children_name_map["tx_sc_stats"] = "tx-sc-stats"
                        self._children_yang_names.add("tx-sc-stats")

                        self.rx_sc_stats = YList(self)
                        self._segment_path = lambda: "stats"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Macsec.Secy.Interfaces.Interface.Stats, [], name, value)


                    class IntfStats(Entity):
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
                            super(Macsec.Secy.Interfaces.Interface.Stats.IntfStats, self).__init__()

                            self.yang_name = "intf-stats"
                            self.yang_parent_name = "stats"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.in_octets_decrypted = YLeaf(YType.uint64, "in-octets-decrypted")

                            self.in_octets_validated = YLeaf(YType.uint64, "in-octets-validated")

                            self.in_pkts_bad_tag = YLeaf(YType.uint64, "in-pkts-bad-tag")

                            self.in_pkts_no_sci = YLeaf(YType.uint64, "in-pkts-no-sci")

                            self.in_pkts_no_tag = YLeaf(YType.uint64, "in-pkts-no-tag")

                            self.in_pkts_overrun = YLeaf(YType.uint64, "in-pkts-overrun")

                            self.in_pkts_unknown_sci = YLeaf(YType.uint64, "in-pkts-unknown-sci")

                            self.in_pkts_untagged = YLeaf(YType.uint64, "in-pkts-untagged")

                            self.out_octets_encrypted = YLeaf(YType.uint64, "out-octets-encrypted")

                            self.out_octets_protected = YLeaf(YType.uint64, "out-octets-protected")

                            self.out_pkts_too_long = YLeaf(YType.uint64, "out-pkts-too-long")

                            self.out_pkts_untagged = YLeaf(YType.uint64, "out-pkts-untagged")
                            self._segment_path = lambda: "intf-stats"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Macsec.Secy.Interfaces.Interface.Stats.IntfStats, ['in_octets_decrypted', 'in_octets_validated', 'in_pkts_bad_tag', 'in_pkts_no_sci', 'in_pkts_no_tag', 'in_pkts_overrun', 'in_pkts_unknown_sci', 'in_pkts_untagged', 'out_octets_encrypted', 'out_octets_protected', 'out_pkts_too_long', 'out_pkts_untagged'], name, value)


                    class RxScStats(Entity):
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
                        
                        .. attribute:: rxsa_stat
                        
                        	rxsa stats
                        	**type**\: list of    :py:class:`RxsaStat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_secy_oper.Macsec.Secy.Interfaces.Interface.Stats.RxScStats.RxsaStat>`
                        
                        

                        """

                        _prefix = 'crypto-macsec-secy-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Macsec.Secy.Interfaces.Interface.Stats.RxScStats, self).__init__()

                            self.yang_name = "rx-sc-stats"
                            self.yang_parent_name = "stats"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"rxsa-stat" : ("rxsa_stat", Macsec.Secy.Interfaces.Interface.Stats.RxScStats.RxsaStat)}

                            self.in_octets_decrypted = YLeaf(YType.uint64, "in-octets-decrypted")

                            self.in_octets_validated = YLeaf(YType.uint64, "in-octets-validated")

                            self.in_pkts_delayed = YLeaf(YType.uint64, "in-pkts-delayed")

                            self.in_pkts_invalid = YLeaf(YType.uint64, "in-pkts-invalid")

                            self.in_pkts_late = YLeaf(YType.uint64, "in-pkts-late")

                            self.in_pkts_not_using_sa = YLeaf(YType.uint64, "in-pkts-not-using-sa")

                            self.in_pkts_not_valid = YLeaf(YType.uint64, "in-pkts-not-valid")

                            self.in_pkts_ok = YLeaf(YType.uint64, "in-pkts-ok")

                            self.in_pkts_unchecked = YLeaf(YType.uint64, "in-pkts-unchecked")

                            self.in_pkts_untagged_hit = YLeaf(YType.uint64, "in-pkts-untagged-hit")

                            self.in_pkts_unused_sa = YLeaf(YType.uint64, "in-pkts-unused-sa")

                            self.rx_sci = YLeaf(YType.uint64, "rx-sci")

                            self.rxsa_stat = YList(self)
                            self._segment_path = lambda: "rx-sc-stats"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Macsec.Secy.Interfaces.Interface.Stats.RxScStats, ['in_octets_decrypted', 'in_octets_validated', 'in_pkts_delayed', 'in_pkts_invalid', 'in_pkts_late', 'in_pkts_not_using_sa', 'in_pkts_not_valid', 'in_pkts_ok', 'in_pkts_unchecked', 'in_pkts_untagged_hit', 'in_pkts_unused_sa', 'rx_sci'], name, value)


                        class RxsaStat(Entity):
                            """
                            rxsa stats
                            
                            .. attribute:: in_pkts_invalid
                            
                            	InPktsInvalid
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
                            
                            .. attribute:: in_pkts_unused_sa
                            
                            	InPktsUnusedSA
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: next_pn
                            
                            	NextPN
                            	**type**\:  int
                            
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
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.in_pkts_invalid = YLeaf(YType.uint64, "in-pkts-invalid")

                                self.in_pkts_not_using_sa = YLeaf(YType.uint64, "in-pkts-not-using-sa")

                                self.in_pkts_not_valid = YLeaf(YType.uint64, "in-pkts-not-valid")

                                self.in_pkts_ok = YLeaf(YType.uint64, "in-pkts-ok")

                                self.in_pkts_unused_sa = YLeaf(YType.uint64, "in-pkts-unused-sa")

                                self.next_pn = YLeaf(YType.uint64, "next-pn")
                                self._segment_path = lambda: "rxsa-stat"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Macsec.Secy.Interfaces.Interface.Stats.RxScStats.RxsaStat, ['in_pkts_invalid', 'in_pkts_not_using_sa', 'in_pkts_not_valid', 'in_pkts_ok', 'in_pkts_unused_sa', 'next_pn'], name, value)


                    class TxScStats(Entity):
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
                        
                        .. attribute:: txsa_stat
                        
                        	tx sa stats
                        	**type**\: list of    :py:class:`TxsaStat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_secy_oper.Macsec.Secy.Interfaces.Interface.Stats.TxScStats.TxsaStat>`
                        
                        

                        """

                        _prefix = 'crypto-macsec-secy-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Macsec.Secy.Interfaces.Interface.Stats.TxScStats, self).__init__()

                            self.yang_name = "tx-sc-stats"
                            self.yang_parent_name = "stats"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"txsa-stat" : ("txsa_stat", Macsec.Secy.Interfaces.Interface.Stats.TxScStats.TxsaStat)}

                            self.out_octets_encrypted = YLeaf(YType.uint64, "out-octets-encrypted")

                            self.out_octets_protected = YLeaf(YType.uint64, "out-octets-protected")

                            self.out_pkts_encrypted = YLeaf(YType.uint64, "out-pkts-encrypted")

                            self.out_pkts_protected = YLeaf(YType.uint64, "out-pkts-protected")

                            self.out_pkts_too_long = YLeaf(YType.uint64, "out-pkts-too-long")

                            self.tx_sci = YLeaf(YType.uint64, "tx-sci")

                            self.txsa_stat = YList(self)
                            self._segment_path = lambda: "tx-sc-stats"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Macsec.Secy.Interfaces.Interface.Stats.TxScStats, ['out_octets_encrypted', 'out_octets_protected', 'out_pkts_encrypted', 'out_pkts_protected', 'out_pkts_too_long', 'tx_sci'], name, value)


                        class TxsaStat(Entity):
                            """
                            tx sa stats
                            
                            .. attribute:: next_pn
                            
                            	NextPN
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
                            
                            

                            """

                            _prefix = 'crypto-macsec-secy-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Macsec.Secy.Interfaces.Interface.Stats.TxScStats.TxsaStat, self).__init__()

                                self.yang_name = "txsa-stat"
                                self.yang_parent_name = "tx-sc-stats"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.next_pn = YLeaf(YType.uint64, "next-pn")

                                self.out_pkts_encrypted = YLeaf(YType.uint64, "out-pkts-encrypted")

                                self.out_pkts_protected = YLeaf(YType.uint64, "out-pkts-protected")
                                self._segment_path = lambda: "txsa-stat"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Macsec.Secy.Interfaces.Interface.Stats.TxScStats.TxsaStat, ['next_pn', 'out_pkts_encrypted', 'out_pkts_protected'], name, value)

    def clone_ptr(self):
        self._top_entity = Macsec()
        return self._top_entity

