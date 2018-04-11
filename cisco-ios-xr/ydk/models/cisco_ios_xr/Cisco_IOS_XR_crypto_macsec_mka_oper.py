""" Cisco_IOS_XR_crypto_macsec_mka_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR crypto\-macsec\-mka package operational data.

This module contains definitions
for the following management objects\:
  macsec\: Macsec operational data

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
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
    
    .. attribute:: mka
    
    	MKA Data
    	**type**\:  :py:class:`Mka <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_oper.Macsec.Mka>`
    
    

    """

    _prefix = 'crypto-macsec-mka-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Macsec, self).__init__()
        self._top_entity = None

        self.yang_name = "macsec"
        self.yang_parent_name = "Cisco-IOS-XR-crypto-macsec-mka-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("mka", ("mka", Macsec.Mka))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.mka = Macsec.Mka()
        self.mka.parent = self
        self._children_name_map["mka"] = "mka"
        self._children_yang_names.add("mka")
        self._segment_path = lambda: "Cisco-IOS-XR-crypto-macsec-mka-oper:macsec"


    class Mka(Entity):
        """
        MKA Data
        
        .. attribute:: interfaces
        
        	MKA Data
        	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_oper.Macsec.Mka.Interfaces>`
        
        

        """

        _prefix = 'crypto-macsec-mka-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Macsec.Mka, self).__init__()

            self.yang_name = "mka"
            self.yang_parent_name = "macsec"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([("interfaces", ("interfaces", Macsec.Mka.Interfaces))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict()

            self.interfaces = Macsec.Mka.Interfaces()
            self.interfaces.parent = self
            self._children_name_map["interfaces"] = "interfaces"
            self._children_yang_names.add("interfaces")
            self._segment_path = lambda: "mka"
            self._absolute_path = lambda: "Cisco-IOS-XR-crypto-macsec-mka-oper:macsec/%s" % self._segment_path()


        class Interfaces(Entity):
            """
            MKA Data
            
            .. attribute:: interface
            
            	MKA Data for the Interface
            	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_oper.Macsec.Mka.Interfaces.Interface>`
            
            

            """

            _prefix = 'crypto-macsec-mka-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Macsec.Mka.Interfaces, self).__init__()

                self.yang_name = "interfaces"
                self.yang_parent_name = "mka"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("interface", ("interface", Macsec.Mka.Interfaces.Interface))])
                self._leafs = OrderedDict()

                self.interface = YList(self)
                self._segment_path = lambda: "interfaces"
                self._absolute_path = lambda: "Cisco-IOS-XR-crypto-macsec-mka-oper:macsec/mka/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Macsec.Mka.Interfaces, [], name, value)


            class Interface(Entity):
                """
                MKA Data for the Interface
                
                .. attribute:: name  (key)
                
                	Interface Name
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9./\-]+
                
                .. attribute:: session
                
                	MKA Session Data
                	**type**\:  :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_oper.Macsec.Mka.Interfaces.Interface.Session>`
                
                

                """

                _prefix = 'crypto-macsec-mka-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Macsec.Mka.Interfaces.Interface, self).__init__()

                    self.yang_name = "interface"
                    self.yang_parent_name = "interfaces"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['name']
                    self._child_container_classes = OrderedDict([("session", ("session", Macsec.Mka.Interfaces.Interface.Session))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('name', YLeaf(YType.str, 'name')),
                    ])
                    self.name = None

                    self.session = Macsec.Mka.Interfaces.Interface.Session()
                    self.session.parent = self
                    self._children_name_map["session"] = "session"
                    self._children_yang_names.add("session")
                    self._segment_path = lambda: "interface" + "[name='" + str(self.name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-crypto-macsec-mka-oper:macsec/mka/interfaces/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Macsec.Mka.Interfaces.Interface, ['name'], name, value)


                class Session(Entity):
                    """
                    MKA Session Data
                    
                    .. attribute:: session_summary
                    
                    	Session summary
                    	**type**\:  :py:class:`SessionSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_oper.Macsec.Mka.Interfaces.Interface.Session.SessionSummary>`
                    
                    .. attribute:: vp
                    
                    	Virtual Pointer Info
                    	**type**\:  :py:class:`Vp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_oper.Macsec.Mka.Interfaces.Interface.Session.Vp>`
                    
                    .. attribute:: ca
                    
                    	CA List for a Session
                    	**type**\: list of  		 :py:class:`Ca <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_oper.Macsec.Mka.Interfaces.Interface.Session.Ca>`
                    
                    

                    """

                    _prefix = 'crypto-macsec-mka-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Macsec.Mka.Interfaces.Interface.Session, self).__init__()

                        self.yang_name = "session"
                        self.yang_parent_name = "interface"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("session-summary", ("session_summary", Macsec.Mka.Interfaces.Interface.Session.SessionSummary)), ("vp", ("vp", Macsec.Mka.Interfaces.Interface.Session.Vp))])
                        self._child_list_classes = OrderedDict([("ca", ("ca", Macsec.Mka.Interfaces.Interface.Session.Ca))])
                        self._leafs = OrderedDict()

                        self.session_summary = Macsec.Mka.Interfaces.Interface.Session.SessionSummary()
                        self.session_summary.parent = self
                        self._children_name_map["session_summary"] = "session-summary"
                        self._children_yang_names.add("session-summary")

                        self.vp = Macsec.Mka.Interfaces.Interface.Session.Vp()
                        self.vp.parent = self
                        self._children_name_map["vp"] = "vp"
                        self._children_yang_names.add("vp")

                        self.ca = YList(self)
                        self._segment_path = lambda: "session"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Macsec.Mka.Interfaces.Interface.Session, [], name, value)


                    class SessionSummary(Entity):
                        """
                        Session summary
                        
                        .. attribute:: outer_tag
                        
                        	VLAN Outer TAG
                        	**type**\:  :py:class:`OuterTag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_oper.Macsec.Mka.Interfaces.Interface.Session.SessionSummary.OuterTag>`
                        
                        .. attribute:: inner_tag
                        
                        	VLAN Inner TAG
                        	**type**\:  :py:class:`InnerTag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_oper.Macsec.Mka.Interfaces.Interface.Session.SessionSummary.InnerTag>`
                        
                        .. attribute:: interface_name
                        
                        	macsec configured interface
                        	**type**\: str
                        
                        .. attribute:: inherited_policy
                        
                        	Is Inherited Policy
                        	**type**\: bool
                        
                        .. attribute:: policy
                        
                        	Policy Name
                        	**type**\: str
                        
                        .. attribute:: priority
                        
                        	Key Server Priority
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: my_mac
                        
                        	My MAC
                        	**type**\: str
                        
                        .. attribute:: delay_protection
                        
                        	Delay Protect
                        	**type**\: bool
                        
                        .. attribute:: replay_protect
                        
                        	Replay Protect
                        	**type**\: bool
                        
                        .. attribute:: window_size
                        
                        	Replay Window Size
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: include_icv_indicator
                        
                        	IncludeICVIndicator
                        	**type**\: bool
                        
                        .. attribute:: confidentiality_offset
                        
                        	Confidentiality Offset
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: algo_agility
                        
                        	Alogorithm Agility
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: capability
                        
                        	MACSec Capability
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: cipher_str
                        
                        	Cipher String
                        	**type**\: str
                        
                        .. attribute:: mac_sec_desired
                        
                        	MACSec Desired
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'crypto-macsec-mka-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Macsec.Mka.Interfaces.Interface.Session.SessionSummary, self).__init__()

                            self.yang_name = "session-summary"
                            self.yang_parent_name = "session"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("outer-tag", ("outer_tag", Macsec.Mka.Interfaces.Interface.Session.SessionSummary.OuterTag)), ("inner-tag", ("inner_tag", Macsec.Mka.Interfaces.Interface.Session.SessionSummary.InnerTag))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('interface_name', YLeaf(YType.str, 'interface-name')),
                                ('inherited_policy', YLeaf(YType.boolean, 'inherited-policy')),
                                ('policy', YLeaf(YType.str, 'policy')),
                                ('priority', YLeaf(YType.uint32, 'priority')),
                                ('my_mac', YLeaf(YType.str, 'my-mac')),
                                ('delay_protection', YLeaf(YType.boolean, 'delay-protection')),
                                ('replay_protect', YLeaf(YType.boolean, 'replay-protect')),
                                ('window_size', YLeaf(YType.uint32, 'window-size')),
                                ('include_icv_indicator', YLeaf(YType.boolean, 'include-icv-indicator')),
                                ('confidentiality_offset', YLeaf(YType.uint32, 'confidentiality-offset')),
                                ('algo_agility', YLeaf(YType.uint32, 'algo-agility')),
                                ('capability', YLeaf(YType.uint32, 'capability')),
                                ('cipher_str', YLeaf(YType.str, 'cipher-str')),
                                ('mac_sec_desired', YLeaf(YType.boolean, 'mac-sec-desired')),
                            ])
                            self.interface_name = None
                            self.inherited_policy = None
                            self.policy = None
                            self.priority = None
                            self.my_mac = None
                            self.delay_protection = None
                            self.replay_protect = None
                            self.window_size = None
                            self.include_icv_indicator = None
                            self.confidentiality_offset = None
                            self.algo_agility = None
                            self.capability = None
                            self.cipher_str = None
                            self.mac_sec_desired = None

                            self.outer_tag = Macsec.Mka.Interfaces.Interface.Session.SessionSummary.OuterTag()
                            self.outer_tag.parent = self
                            self._children_name_map["outer_tag"] = "outer-tag"
                            self._children_yang_names.add("outer-tag")

                            self.inner_tag = Macsec.Mka.Interfaces.Interface.Session.SessionSummary.InnerTag()
                            self.inner_tag.parent = self
                            self._children_name_map["inner_tag"] = "inner-tag"
                            self._children_yang_names.add("inner-tag")
                            self._segment_path = lambda: "session-summary"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Macsec.Mka.Interfaces.Interface.Session.SessionSummary, ['interface_name', 'inherited_policy', 'policy', 'priority', 'my_mac', 'delay_protection', 'replay_protect', 'window_size', 'include_icv_indicator', 'confidentiality_offset', 'algo_agility', 'capability', 'cipher_str', 'mac_sec_desired'], name, value)


                        class OuterTag(Entity):
                            """
                            VLAN Outer TAG
                            
                            .. attribute:: ether_type
                            
                            	EtherType
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: priority
                            
                            	Priority
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: cfi
                            
                            	Cannonical Format Identifier
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: vlan_id
                            
                            	Vlan Id
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'crypto-macsec-mka-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Macsec.Mka.Interfaces.Interface.Session.SessionSummary.OuterTag, self).__init__()

                                self.yang_name = "outer-tag"
                                self.yang_parent_name = "session-summary"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('ether_type', YLeaf(YType.uint16, 'ether-type')),
                                    ('priority', YLeaf(YType.uint8, 'priority')),
                                    ('cfi', YLeaf(YType.uint8, 'cfi')),
                                    ('vlan_id', YLeaf(YType.uint16, 'vlan-id')),
                                ])
                                self.ether_type = None
                                self.priority = None
                                self.cfi = None
                                self.vlan_id = None
                                self._segment_path = lambda: "outer-tag"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Macsec.Mka.Interfaces.Interface.Session.SessionSummary.OuterTag, ['ether_type', 'priority', 'cfi', 'vlan_id'], name, value)


                        class InnerTag(Entity):
                            """
                            VLAN Inner TAG
                            
                            .. attribute:: ether_type
                            
                            	EtherType
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: priority
                            
                            	Priority
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: cfi
                            
                            	Cannonical Format Identifier
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: vlan_id
                            
                            	Vlan Id
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'crypto-macsec-mka-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Macsec.Mka.Interfaces.Interface.Session.SessionSummary.InnerTag, self).__init__()

                                self.yang_name = "inner-tag"
                                self.yang_parent_name = "session-summary"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('ether_type', YLeaf(YType.uint16, 'ether-type')),
                                    ('priority', YLeaf(YType.uint8, 'priority')),
                                    ('cfi', YLeaf(YType.uint8, 'cfi')),
                                    ('vlan_id', YLeaf(YType.uint16, 'vlan-id')),
                                ])
                                self.ether_type = None
                                self.priority = None
                                self.cfi = None
                                self.vlan_id = None
                                self._segment_path = lambda: "inner-tag"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Macsec.Mka.Interfaces.Interface.Session.SessionSummary.InnerTag, ['ether_type', 'priority', 'cfi', 'vlan_id'], name, value)


                    class Vp(Entity):
                        """
                        Virtual Pointer Info
                        
                        .. attribute:: my_sci
                        
                        	Local SCI(MAC)
                        	**type**\: str
                        
                        .. attribute:: virtual_port_id
                        
                        	Virtual Port ID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: latest_rx
                        
                        	Latest Rx status
                        	**type**\: bool
                        
                        .. attribute:: latest_tx
                        
                        	Latest Tx status
                        	**type**\: bool
                        
                        .. attribute:: latest_an
                        
                        	Latest SAK AN
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: latest_ki
                        
                        	Latest SAK KI
                        	**type**\: str
                        
                        .. attribute:: latest_kn
                        
                        	Latest SAK KN
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: old_rx
                        
                        	Old Rx status
                        	**type**\: bool
                        
                        .. attribute:: old_tx
                        
                        	Old Tx status
                        	**type**\: bool
                        
                        .. attribute:: old_an
                        
                        	Old SAK AN
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: old_ki
                        
                        	Old SAK KI
                        	**type**\: str
                        
                        .. attribute:: old_kn
                        
                        	Old SAK KN
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: wait_time
                        
                        	SAK Transmit Wait Time
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: retire_time
                        
                        	SAK Retire time
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: cipher_suite
                        
                        	SAK Cipher Suite
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ssci
                        
                        	SSCI of the Local TxSC
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: time_to_sak_rekey
                        
                        	Next SAK Rekey time in Sec
                        	**type**\: str
                        
                        .. attribute:: fallback_keepalive
                        
                        	Fallback Keepalive
                        	**type**\: list of  		 :py:class:`FallbackKeepalive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_oper.Macsec.Mka.Interfaces.Interface.Session.Vp.FallbackKeepalive>`
                        
                        

                        """

                        _prefix = 'crypto-macsec-mka-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Macsec.Mka.Interfaces.Interface.Session.Vp, self).__init__()

                            self.yang_name = "vp"
                            self.yang_parent_name = "session"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("fallback-keepalive", ("fallback_keepalive", Macsec.Mka.Interfaces.Interface.Session.Vp.FallbackKeepalive))])
                            self._leafs = OrderedDict([
                                ('my_sci', YLeaf(YType.str, 'my-sci')),
                                ('virtual_port_id', YLeaf(YType.uint32, 'virtual-port-id')),
                                ('latest_rx', YLeaf(YType.boolean, 'latest-rx')),
                                ('latest_tx', YLeaf(YType.boolean, 'latest-tx')),
                                ('latest_an', YLeaf(YType.uint32, 'latest-an')),
                                ('latest_ki', YLeaf(YType.str, 'latest-ki')),
                                ('latest_kn', YLeaf(YType.uint32, 'latest-kn')),
                                ('old_rx', YLeaf(YType.boolean, 'old-rx')),
                                ('old_tx', YLeaf(YType.boolean, 'old-tx')),
                                ('old_an', YLeaf(YType.uint32, 'old-an')),
                                ('old_ki', YLeaf(YType.str, 'old-ki')),
                                ('old_kn', YLeaf(YType.uint32, 'old-kn')),
                                ('wait_time', YLeaf(YType.uint32, 'wait-time')),
                                ('retire_time', YLeaf(YType.uint32, 'retire-time')),
                                ('cipher_suite', YLeaf(YType.uint32, 'cipher-suite')),
                                ('ssci', YLeaf(YType.uint32, 'ssci')),
                                ('time_to_sak_rekey', YLeaf(YType.str, 'time-to-sak-rekey')),
                            ])
                            self.my_sci = None
                            self.virtual_port_id = None
                            self.latest_rx = None
                            self.latest_tx = None
                            self.latest_an = None
                            self.latest_ki = None
                            self.latest_kn = None
                            self.old_rx = None
                            self.old_tx = None
                            self.old_an = None
                            self.old_ki = None
                            self.old_kn = None
                            self.wait_time = None
                            self.retire_time = None
                            self.cipher_suite = None
                            self.ssci = None
                            self.time_to_sak_rekey = None

                            self.fallback_keepalive = YList(self)
                            self._segment_path = lambda: "vp"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Macsec.Mka.Interfaces.Interface.Session.Vp, ['my_sci', 'virtual_port_id', 'latest_rx', 'latest_tx', 'latest_an', 'latest_ki', 'latest_kn', 'old_rx', 'old_tx', 'old_an', 'old_ki', 'old_kn', 'wait_time', 'retire_time', 'cipher_suite', 'ssci', 'time_to_sak_rekey'], name, value)


                        class FallbackKeepalive(Entity):
                            """
                            Fallback Keepalive
                            
                            .. attribute:: peers_status
                            
                            	Peers Status
                            	**type**\:  :py:class:`PeersStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_oper.Macsec.Mka.Interfaces.Interface.Session.Vp.FallbackKeepalive.PeersStatus>`
                            
                            .. attribute:: ckn
                            
                            	CKN
                            	**type**\: str
                            
                            	**length:** 0..65
                            
                            .. attribute:: mi
                            
                            	Member Identifier
                            	**type**\: str
                            
                            	**length:** 0..25
                            
                            .. attribute:: mn
                            
                            	Message Number
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'crypto-macsec-mka-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Macsec.Mka.Interfaces.Interface.Session.Vp.FallbackKeepalive, self).__init__()

                                self.yang_name = "fallback-keepalive"
                                self.yang_parent_name = "vp"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("peers-status", ("peers_status", Macsec.Mka.Interfaces.Interface.Session.Vp.FallbackKeepalive.PeersStatus))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('ckn', YLeaf(YType.str, 'ckn')),
                                    ('mi', YLeaf(YType.str, 'mi')),
                                    ('mn', YLeaf(YType.uint32, 'mn')),
                                ])
                                self.ckn = None
                                self.mi = None
                                self.mn = None

                                self.peers_status = Macsec.Mka.Interfaces.Interface.Session.Vp.FallbackKeepalive.PeersStatus()
                                self.peers_status.parent = self
                                self._children_name_map["peers_status"] = "peers-status"
                                self._children_yang_names.add("peers-status")
                                self._segment_path = lambda: "fallback-keepalive"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Macsec.Mka.Interfaces.Interface.Session.Vp.FallbackKeepalive, ['ckn', 'mi', 'mn'], name, value)


                            class PeersStatus(Entity):
                                """
                                Peers Status
                                
                                .. attribute:: tx_mkpdu_timestamp
                                
                                	Tx MKPDU Timestamp
                                	**type**\: str
                                
                                	**length:** 0..128
                                
                                .. attribute:: peer_count
                                
                                	Peer Count
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: peer
                                
                                	Peer List
                                	**type**\: list of  		 :py:class:`Peer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_oper.Macsec.Mka.Interfaces.Interface.Session.Vp.FallbackKeepalive.PeersStatus.Peer>`
                                
                                

                                """

                                _prefix = 'crypto-macsec-mka-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Macsec.Mka.Interfaces.Interface.Session.Vp.FallbackKeepalive.PeersStatus, self).__init__()

                                    self.yang_name = "peers-status"
                                    self.yang_parent_name = "fallback-keepalive"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([("peer", ("peer", Macsec.Mka.Interfaces.Interface.Session.Vp.FallbackKeepalive.PeersStatus.Peer))])
                                    self._leafs = OrderedDict([
                                        ('tx_mkpdu_timestamp', YLeaf(YType.str, 'tx-mkpdu-timestamp')),
                                        ('peer_count', YLeaf(YType.uint32, 'peer-count')),
                                    ])
                                    self.tx_mkpdu_timestamp = None
                                    self.peer_count = None

                                    self.peer = YList(self)
                                    self._segment_path = lambda: "peers-status"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Macsec.Mka.Interfaces.Interface.Session.Vp.FallbackKeepalive.PeersStatus, ['tx_mkpdu_timestamp', 'peer_count'], name, value)


                                class Peer(Entity):
                                    """
                                    Peer List
                                    
                                    .. attribute:: peer_data
                                    
                                    	Peer Status Data
                                    	**type**\:  :py:class:`PeerData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_oper.Macsec.Mka.Interfaces.Interface.Session.Vp.FallbackKeepalive.PeersStatus.Peer.PeerData>`
                                    
                                    .. attribute:: sci
                                    
                                    	Rx SCI
                                    	**type**\: str
                                    
                                    	**length:** 0..17
                                    
                                    

                                    """

                                    _prefix = 'crypto-macsec-mka-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Macsec.Mka.Interfaces.Interface.Session.Vp.FallbackKeepalive.PeersStatus.Peer, self).__init__()

                                        self.yang_name = "peer"
                                        self.yang_parent_name = "peers-status"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([("peer-data", ("peer_data", Macsec.Mka.Interfaces.Interface.Session.Vp.FallbackKeepalive.PeersStatus.Peer.PeerData))])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('sci', YLeaf(YType.str, 'sci')),
                                        ])
                                        self.sci = None

                                        self.peer_data = Macsec.Mka.Interfaces.Interface.Session.Vp.FallbackKeepalive.PeersStatus.Peer.PeerData()
                                        self.peer_data.parent = self
                                        self._children_name_map["peer_data"] = "peer-data"
                                        self._children_yang_names.add("peer-data")
                                        self._segment_path = lambda: "peer"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Macsec.Mka.Interfaces.Interface.Session.Vp.FallbackKeepalive.PeersStatus.Peer, ['sci'], name, value)


                                    class PeerData(Entity):
                                        """
                                        Peer Status Data
                                        
                                        .. attribute:: mi
                                        
                                        	Member ID
                                        	**type**\: str
                                        
                                        	**length:** 0..25
                                        
                                        .. attribute:: icv_status
                                        
                                        	ICV Status
                                        	**type**\: str
                                        
                                        	**length:** 0..10
                                        
                                        .. attribute:: icv_check_timestamp
                                        
                                        	ICV Check Timestamp
                                        	**type**\: str
                                        
                                        	**length:** 0..128
                                        
                                        

                                        """

                                        _prefix = 'crypto-macsec-mka-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Macsec.Mka.Interfaces.Interface.Session.Vp.FallbackKeepalive.PeersStatus.Peer.PeerData, self).__init__()

                                            self.yang_name = "peer-data"
                                            self.yang_parent_name = "peer"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('mi', YLeaf(YType.str, 'mi')),
                                                ('icv_status', YLeaf(YType.str, 'icv-status')),
                                                ('icv_check_timestamp', YLeaf(YType.str, 'icv-check-timestamp')),
                                            ])
                                            self.mi = None
                                            self.icv_status = None
                                            self.icv_check_timestamp = None
                                            self._segment_path = lambda: "peer-data"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Macsec.Mka.Interfaces.Interface.Session.Vp.FallbackKeepalive.PeersStatus.Peer.PeerData, ['mi', 'icv_status', 'icv_check_timestamp'], name, value)


                    class Ca(Entity):
                        """
                        CA List for a Session
                        
                        .. attribute:: peers_status
                        
                        	Peers Status
                        	**type**\:  :py:class:`PeersStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_oper.Macsec.Mka.Interfaces.Interface.Session.Ca.PeersStatus>`
                        
                        .. attribute:: is_key_server
                        
                        	Is Key Server
                        	**type**\: bool
                        
                        .. attribute:: status
                        
                        	Session Status [Secured/Not Secured]
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: num_live_peers
                        
                        	Number of Live Peers
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: first_ca
                        
                        	Is First CA
                        	**type**\: bool
                        
                        .. attribute:: peer_sci
                        
                        	Peer SCI(MAC)
                        	**type**\: str
                        
                        .. attribute:: num_live_peers_responded
                        
                        	Number of Live Peers responded
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ckn
                        
                        	CKN
                        	**type**\: str
                        
                        .. attribute:: my_mi
                        
                        	Member Identifier
                        	**type**\: str
                        
                        .. attribute:: my_mn
                        
                        	Message Number
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: authenticator
                        
                        	authenticator
                        	**type**\: bool
                        
                        .. attribute:: status_description
                        
                        	Status Description
                        	**type**\: str
                        
                        .. attribute:: authentication_mode
                        
                        	CA Authentication Mode \:PRIMARY\-PSK/FALLBACK\-PSK/EAP
                        	**type**\: str
                        
                        .. attribute:: key_chain
                        
                        	Key Chain name
                        	**type**\: str
                        
                        .. attribute:: live_peer
                        
                        	Live Peer List
                        	**type**\: list of  		 :py:class:`LivePeer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_oper.Macsec.Mka.Interfaces.Interface.Session.Ca.LivePeer>`
                        
                        .. attribute:: potential_peer
                        
                        	Potential Peer List
                        	**type**\: list of  		 :py:class:`PotentialPeer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_oper.Macsec.Mka.Interfaces.Interface.Session.Ca.PotentialPeer>`
                        
                        .. attribute:: dormant_peer
                        
                        	Dormant Peer List
                        	**type**\: list of  		 :py:class:`DormantPeer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_oper.Macsec.Mka.Interfaces.Interface.Session.Ca.DormantPeer>`
                        
                        

                        """

                        _prefix = 'crypto-macsec-mka-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Macsec.Mka.Interfaces.Interface.Session.Ca, self).__init__()

                            self.yang_name = "ca"
                            self.yang_parent_name = "session"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("peers-status", ("peers_status", Macsec.Mka.Interfaces.Interface.Session.Ca.PeersStatus))])
                            self._child_list_classes = OrderedDict([("live-peer", ("live_peer", Macsec.Mka.Interfaces.Interface.Session.Ca.LivePeer)), ("potential-peer", ("potential_peer", Macsec.Mka.Interfaces.Interface.Session.Ca.PotentialPeer)), ("dormant-peer", ("dormant_peer", Macsec.Mka.Interfaces.Interface.Session.Ca.DormantPeer))])
                            self._leafs = OrderedDict([
                                ('is_key_server', YLeaf(YType.boolean, 'is-key-server')),
                                ('status', YLeaf(YType.uint32, 'status')),
                                ('num_live_peers', YLeaf(YType.uint32, 'num-live-peers')),
                                ('first_ca', YLeaf(YType.boolean, 'first-ca')),
                                ('peer_sci', YLeaf(YType.str, 'peer-sci')),
                                ('num_live_peers_responded', YLeaf(YType.uint32, 'num-live-peers-responded')),
                                ('ckn', YLeaf(YType.str, 'ckn')),
                                ('my_mi', YLeaf(YType.str, 'my-mi')),
                                ('my_mn', YLeaf(YType.uint32, 'my-mn')),
                                ('authenticator', YLeaf(YType.boolean, 'authenticator')),
                                ('status_description', YLeaf(YType.str, 'status-description')),
                                ('authentication_mode', YLeaf(YType.str, 'authentication-mode')),
                                ('key_chain', YLeaf(YType.str, 'key-chain')),
                            ])
                            self.is_key_server = None
                            self.status = None
                            self.num_live_peers = None
                            self.first_ca = None
                            self.peer_sci = None
                            self.num_live_peers_responded = None
                            self.ckn = None
                            self.my_mi = None
                            self.my_mn = None
                            self.authenticator = None
                            self.status_description = None
                            self.authentication_mode = None
                            self.key_chain = None

                            self.peers_status = Macsec.Mka.Interfaces.Interface.Session.Ca.PeersStatus()
                            self.peers_status.parent = self
                            self._children_name_map["peers_status"] = "peers-status"
                            self._children_yang_names.add("peers-status")

                            self.live_peer = YList(self)
                            self.potential_peer = YList(self)
                            self.dormant_peer = YList(self)
                            self._segment_path = lambda: "ca"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Macsec.Mka.Interfaces.Interface.Session.Ca, ['is_key_server', 'status', 'num_live_peers', 'first_ca', 'peer_sci', 'num_live_peers_responded', 'ckn', 'my_mi', 'my_mn', 'authenticator', 'status_description', 'authentication_mode', 'key_chain'], name, value)


                        class PeersStatus(Entity):
                            """
                            Peers Status
                            
                            .. attribute:: tx_mkpdu_timestamp
                            
                            	Tx MKPDU Timestamp
                            	**type**\: str
                            
                            	**length:** 0..128
                            
                            .. attribute:: peer_count
                            
                            	Peer Count
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: peer
                            
                            	Peer List
                            	**type**\: list of  		 :py:class:`Peer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_oper.Macsec.Mka.Interfaces.Interface.Session.Ca.PeersStatus.Peer>`
                            
                            

                            """

                            _prefix = 'crypto-macsec-mka-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Macsec.Mka.Interfaces.Interface.Session.Ca.PeersStatus, self).__init__()

                                self.yang_name = "peers-status"
                                self.yang_parent_name = "ca"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([("peer", ("peer", Macsec.Mka.Interfaces.Interface.Session.Ca.PeersStatus.Peer))])
                                self._leafs = OrderedDict([
                                    ('tx_mkpdu_timestamp', YLeaf(YType.str, 'tx-mkpdu-timestamp')),
                                    ('peer_count', YLeaf(YType.uint32, 'peer-count')),
                                ])
                                self.tx_mkpdu_timestamp = None
                                self.peer_count = None

                                self.peer = YList(self)
                                self._segment_path = lambda: "peers-status"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Macsec.Mka.Interfaces.Interface.Session.Ca.PeersStatus, ['tx_mkpdu_timestamp', 'peer_count'], name, value)


                            class Peer(Entity):
                                """
                                Peer List
                                
                                .. attribute:: peer_data
                                
                                	Peer Status Data
                                	**type**\:  :py:class:`PeerData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_oper.Macsec.Mka.Interfaces.Interface.Session.Ca.PeersStatus.Peer.PeerData>`
                                
                                .. attribute:: sci
                                
                                	Rx SCI
                                	**type**\: str
                                
                                	**length:** 0..17
                                
                                

                                """

                                _prefix = 'crypto-macsec-mka-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Macsec.Mka.Interfaces.Interface.Session.Ca.PeersStatus.Peer, self).__init__()

                                    self.yang_name = "peer"
                                    self.yang_parent_name = "peers-status"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([("peer-data", ("peer_data", Macsec.Mka.Interfaces.Interface.Session.Ca.PeersStatus.Peer.PeerData))])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('sci', YLeaf(YType.str, 'sci')),
                                    ])
                                    self.sci = None

                                    self.peer_data = Macsec.Mka.Interfaces.Interface.Session.Ca.PeersStatus.Peer.PeerData()
                                    self.peer_data.parent = self
                                    self._children_name_map["peer_data"] = "peer-data"
                                    self._children_yang_names.add("peer-data")
                                    self._segment_path = lambda: "peer"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Macsec.Mka.Interfaces.Interface.Session.Ca.PeersStatus.Peer, ['sci'], name, value)


                                class PeerData(Entity):
                                    """
                                    Peer Status Data
                                    
                                    .. attribute:: mi
                                    
                                    	Member ID
                                    	**type**\: str
                                    
                                    	**length:** 0..25
                                    
                                    .. attribute:: icv_status
                                    
                                    	ICV Status
                                    	**type**\: str
                                    
                                    	**length:** 0..10
                                    
                                    .. attribute:: icv_check_timestamp
                                    
                                    	ICV Check Timestamp
                                    	**type**\: str
                                    
                                    	**length:** 0..128
                                    
                                    

                                    """

                                    _prefix = 'crypto-macsec-mka-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Macsec.Mka.Interfaces.Interface.Session.Ca.PeersStatus.Peer.PeerData, self).__init__()

                                        self.yang_name = "peer-data"
                                        self.yang_parent_name = "peer"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('mi', YLeaf(YType.str, 'mi')),
                                            ('icv_status', YLeaf(YType.str, 'icv-status')),
                                            ('icv_check_timestamp', YLeaf(YType.str, 'icv-check-timestamp')),
                                        ])
                                        self.mi = None
                                        self.icv_status = None
                                        self.icv_check_timestamp = None
                                        self._segment_path = lambda: "peer-data"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Macsec.Mka.Interfaces.Interface.Session.Ca.PeersStatus.Peer.PeerData, ['mi', 'icv_status', 'icv_check_timestamp'], name, value)


                        class LivePeer(Entity):
                            """
                            Live Peer List
                            
                            .. attribute:: mi
                            
                            	Member ID
                            	**type**\: str
                            
                            .. attribute:: sci
                            
                            	Rx SCI
                            	**type**\: str
                            
                            .. attribute:: mn
                            
                            	Message Number
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: priority
                            
                            	KS Priority
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: ssci
                            
                            	Peer SSCI
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'crypto-macsec-mka-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Macsec.Mka.Interfaces.Interface.Session.Ca.LivePeer, self).__init__()

                                self.yang_name = "live-peer"
                                self.yang_parent_name = "ca"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('mi', YLeaf(YType.str, 'mi')),
                                    ('sci', YLeaf(YType.str, 'sci')),
                                    ('mn', YLeaf(YType.uint32, 'mn')),
                                    ('priority', YLeaf(YType.uint32, 'priority')),
                                    ('ssci', YLeaf(YType.uint32, 'ssci')),
                                ])
                                self.mi = None
                                self.sci = None
                                self.mn = None
                                self.priority = None
                                self.ssci = None
                                self._segment_path = lambda: "live-peer"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Macsec.Mka.Interfaces.Interface.Session.Ca.LivePeer, ['mi', 'sci', 'mn', 'priority', 'ssci'], name, value)


                        class PotentialPeer(Entity):
                            """
                            Potential Peer List
                            
                            .. attribute:: mi
                            
                            	Member ID
                            	**type**\: str
                            
                            .. attribute:: sci
                            
                            	Rx SCI
                            	**type**\: str
                            
                            .. attribute:: mn
                            
                            	Message Number
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: priority
                            
                            	KS Priority
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: ssci
                            
                            	Peer SSCI
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'crypto-macsec-mka-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Macsec.Mka.Interfaces.Interface.Session.Ca.PotentialPeer, self).__init__()

                                self.yang_name = "potential-peer"
                                self.yang_parent_name = "ca"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('mi', YLeaf(YType.str, 'mi')),
                                    ('sci', YLeaf(YType.str, 'sci')),
                                    ('mn', YLeaf(YType.uint32, 'mn')),
                                    ('priority', YLeaf(YType.uint32, 'priority')),
                                    ('ssci', YLeaf(YType.uint32, 'ssci')),
                                ])
                                self.mi = None
                                self.sci = None
                                self.mn = None
                                self.priority = None
                                self.ssci = None
                                self._segment_path = lambda: "potential-peer"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Macsec.Mka.Interfaces.Interface.Session.Ca.PotentialPeer, ['mi', 'sci', 'mn', 'priority', 'ssci'], name, value)


                        class DormantPeer(Entity):
                            """
                            Dormant Peer List
                            
                            .. attribute:: mi
                            
                            	Member ID
                            	**type**\: str
                            
                            .. attribute:: sci
                            
                            	Rx SCI
                            	**type**\: str
                            
                            .. attribute:: mn
                            
                            	Message Number
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: priority
                            
                            	KS Priority
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: ssci
                            
                            	Peer SSCI
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'crypto-macsec-mka-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Macsec.Mka.Interfaces.Interface.Session.Ca.DormantPeer, self).__init__()

                                self.yang_name = "dormant-peer"
                                self.yang_parent_name = "ca"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('mi', YLeaf(YType.str, 'mi')),
                                    ('sci', YLeaf(YType.str, 'sci')),
                                    ('mn', YLeaf(YType.uint32, 'mn')),
                                    ('priority', YLeaf(YType.uint32, 'priority')),
                                    ('ssci', YLeaf(YType.uint32, 'ssci')),
                                ])
                                self.mi = None
                                self.sci = None
                                self.mn = None
                                self.priority = None
                                self.ssci = None
                                self._segment_path = lambda: "dormant-peer"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Macsec.Mka.Interfaces.Interface.Session.Ca.DormantPeer, ['mi', 'sci', 'mn', 'priority', 'ssci'], name, value)

    def clone_ptr(self):
        self._top_entity = Macsec()
        return self._top_entity

