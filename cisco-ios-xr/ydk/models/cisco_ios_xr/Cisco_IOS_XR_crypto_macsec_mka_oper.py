""" Cisco_IOS_XR_crypto_macsec_mka_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR crypto\-macsec\-mka package operational data.

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
    
    .. attribute:: mka
    
    	MKA Data
    	**type**\:   :py:class:`Mka <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_oper.Macsec.Mka>`
    
    

    """

    _prefix = 'crypto-macsec-mka-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.mka = Macsec.Mka()
        self.mka.parent = self


    class Mka(object):
        """
        MKA Data
        
        .. attribute:: interfaces
        
        	MKA Data
        	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_oper.Macsec.Mka.Interfaces>`
        
        

        """

        _prefix = 'crypto-macsec-mka-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.interfaces = Macsec.Mka.Interfaces()
            self.interfaces.parent = self


        class Interfaces(object):
            """
            MKA Data
            
            .. attribute:: interface
            
            	MKA Data for the Interface
            	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_oper.Macsec.Mka.Interfaces.Interface>`
            
            

            """

            _prefix = 'crypto-macsec-mka-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.interface = YList()
                self.interface.parent = self
                self.interface.name = 'interface'


            class Interface(object):
                """
                MKA Data for the Interface
                
                .. attribute:: name  <key>
                
                	Interface Name
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: session
                
                	MKA Session Data
                	**type**\:   :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_oper.Macsec.Mka.Interfaces.Interface.Session>`
                
                

                """

                _prefix = 'crypto-macsec-mka-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.name = None
                    self.session = Macsec.Mka.Interfaces.Interface.Session()
                    self.session.parent = self


                class Session(object):
                    """
                    MKA Session Data
                    
                    .. attribute:: ca
                    
                    	CA List for a Session
                    	**type**\: list of    :py:class:`Ca <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_oper.Macsec.Mka.Interfaces.Interface.Session.Ca>`
                    
                    .. attribute:: session_summary
                    
                    	Session summary
                    	**type**\:   :py:class:`SessionSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_oper.Macsec.Mka.Interfaces.Interface.Session.SessionSummary>`
                    
                    .. attribute:: vp
                    
                    	Virtual Pointer Info
                    	**type**\:   :py:class:`Vp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_oper.Macsec.Mka.Interfaces.Interface.Session.Vp>`
                    
                    

                    """

                    _prefix = 'crypto-macsec-mka-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.ca = YList()
                        self.ca.parent = self
                        self.ca.name = 'ca'
                        self.session_summary = Macsec.Mka.Interfaces.Interface.Session.SessionSummary()
                        self.session_summary.parent = self
                        self.vp = Macsec.Mka.Interfaces.Interface.Session.Vp()
                        self.vp.parent = self


                    class SessionSummary(object):
                        """
                        Session summary
                        
                        .. attribute:: algo_agility
                        
                        	Alogorithm Agility
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: capability
                        
                        	MACSec Capability
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: cipher_str
                        
                        	Cipher String
                        	**type**\:  str
                        
                        .. attribute:: confidentiality_offset
                        
                        	Confidentiality Offset
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: delay_protection
                        
                        	Delay Protect
                        	**type**\:  bool
                        
                        .. attribute:: include_icv_indicator
                        
                        	IncludeICVIndicator
                        	**type**\:  bool
                        
                        .. attribute:: inherited_policy
                        
                        	Is Inherited Policy
                        	**type**\:  bool
                        
                        .. attribute:: inner_tag
                        
                        	VLAN Inner TAG
                        	**type**\:   :py:class:`InnerTag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_oper.Macsec.Mka.Interfaces.Interface.Session.SessionSummary.InnerTag>`
                        
                        .. attribute:: interface_name
                        
                        	macsec configured interface
                        	**type**\:  str
                        
                        .. attribute:: mac_sec_desired
                        
                        	MACSec Desired
                        	**type**\:  bool
                        
                        .. attribute:: my_mac
                        
                        	My MAC
                        	**type**\:  str
                        
                        .. attribute:: outer_tag
                        
                        	VLAN Outer TAG
                        	**type**\:   :py:class:`OuterTag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_oper.Macsec.Mka.Interfaces.Interface.Session.SessionSummary.OuterTag>`
                        
                        .. attribute:: policy
                        
                        	Policy Name
                        	**type**\:  str
                        
                        .. attribute:: priority
                        
                        	Key Server Priority
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: replay_protect
                        
                        	Replay Protect
                        	**type**\:  bool
                        
                        .. attribute:: window_size
                        
                        	Replay Window Size
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'crypto-macsec-mka-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.algo_agility = None
                            self.capability = None
                            self.cipher_str = None
                            self.confidentiality_offset = None
                            self.delay_protection = None
                            self.include_icv_indicator = None
                            self.inherited_policy = None
                            self.inner_tag = Macsec.Mka.Interfaces.Interface.Session.SessionSummary.InnerTag()
                            self.inner_tag.parent = self
                            self.interface_name = None
                            self.mac_sec_desired = None
                            self.my_mac = None
                            self.outer_tag = Macsec.Mka.Interfaces.Interface.Session.SessionSummary.OuterTag()
                            self.outer_tag.parent = self
                            self.policy = None
                            self.priority = None
                            self.replay_protect = None
                            self.window_size = None


                        class OuterTag(object):
                            """
                            VLAN Outer TAG
                            
                            .. attribute:: cfi
                            
                            	cfi
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: etype
                            
                            	etype
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: priority
                            
                            	priority
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: vlan_id
                            
                            	vlan id
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'crypto-macsec-mka-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.cfi = None
                                self.etype = None
                                self.priority = None
                                self.vlan_id = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-mka-oper:outer-tag'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.cfi is not None:
                                    return True

                                if self.etype is not None:
                                    return True

                                if self.priority is not None:
                                    return True

                                if self.vlan_id is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_mka_oper as meta
                                return meta._meta_table['Macsec.Mka.Interfaces.Interface.Session.SessionSummary.OuterTag']['meta_info']


                        class InnerTag(object):
                            """
                            VLAN Inner TAG
                            
                            .. attribute:: cfi
                            
                            	cfi
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: etype
                            
                            	etype
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: priority
                            
                            	priority
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: vlan_id
                            
                            	vlan id
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'crypto-macsec-mka-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.cfi = None
                                self.etype = None
                                self.priority = None
                                self.vlan_id = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-mka-oper:inner-tag'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.cfi is not None:
                                    return True

                                if self.etype is not None:
                                    return True

                                if self.priority is not None:
                                    return True

                                if self.vlan_id is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_mka_oper as meta
                                return meta._meta_table['Macsec.Mka.Interfaces.Interface.Session.SessionSummary.InnerTag']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-mka-oper:session-summary'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.algo_agility is not None:
                                return True

                            if self.capability is not None:
                                return True

                            if self.cipher_str is not None:
                                return True

                            if self.confidentiality_offset is not None:
                                return True

                            if self.delay_protection is not None:
                                return True

                            if self.include_icv_indicator is not None:
                                return True

                            if self.inherited_policy is not None:
                                return True

                            if self.inner_tag is not None and self.inner_tag._has_data():
                                return True

                            if self.interface_name is not None:
                                return True

                            if self.mac_sec_desired is not None:
                                return True

                            if self.my_mac is not None:
                                return True

                            if self.outer_tag is not None and self.outer_tag._has_data():
                                return True

                            if self.policy is not None:
                                return True

                            if self.priority is not None:
                                return True

                            if self.replay_protect is not None:
                                return True

                            if self.window_size is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_mka_oper as meta
                            return meta._meta_table['Macsec.Mka.Interfaces.Interface.Session.SessionSummary']['meta_info']


                    class Vp(object):
                        """
                        Virtual Pointer Info
                        
                        .. attribute:: cipher_suite
                        
                        	SAK Cipher Suite
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: latest_an
                        
                        	Latest SAK AN
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: latest_ki
                        
                        	Latest SAK KI
                        	**type**\:  str
                        
                        .. attribute:: latest_kn
                        
                        	Latest SAK KN
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: latest_rx
                        
                        	Latest Rx status
                        	**type**\:  bool
                        
                        .. attribute:: latest_tx
                        
                        	Latest Tx status
                        	**type**\:  bool
                        
                        .. attribute:: my_sci
                        
                        	Local SCI(MAC)
                        	**type**\:  str
                        
                        .. attribute:: old_an
                        
                        	Old SAK AN
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: old_ki
                        
                        	Old SAK KI
                        	**type**\:  str
                        
                        .. attribute:: old_kn
                        
                        	Old SAK KN
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: old_rx
                        
                        	Old Rx status
                        	**type**\:  bool
                        
                        .. attribute:: old_tx
                        
                        	Old Tx status
                        	**type**\:  bool
                        
                        .. attribute:: retire_time
                        
                        	SAK Retire time
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ssci
                        
                        	SSCI of the Local TxSC
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: time_to_sak_rekey
                        
                        	Next SAK Rekey time in Sec
                        	**type**\:  str
                        
                        .. attribute:: virtual_port_id
                        
                        	Virtual Port ID
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: wait_time
                        
                        	SAK Transmit Wait Time
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'crypto-macsec-mka-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.cipher_suite = None
                            self.latest_an = None
                            self.latest_ki = None
                            self.latest_kn = None
                            self.latest_rx = None
                            self.latest_tx = None
                            self.my_sci = None
                            self.old_an = None
                            self.old_ki = None
                            self.old_kn = None
                            self.old_rx = None
                            self.old_tx = None
                            self.retire_time = None
                            self.ssci = None
                            self.time_to_sak_rekey = None
                            self.virtual_port_id = None
                            self.wait_time = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-mka-oper:vp'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.cipher_suite is not None:
                                return True

                            if self.latest_an is not None:
                                return True

                            if self.latest_ki is not None:
                                return True

                            if self.latest_kn is not None:
                                return True

                            if self.latest_rx is not None:
                                return True

                            if self.latest_tx is not None:
                                return True

                            if self.my_sci is not None:
                                return True

                            if self.old_an is not None:
                                return True

                            if self.old_ki is not None:
                                return True

                            if self.old_kn is not None:
                                return True

                            if self.old_rx is not None:
                                return True

                            if self.old_tx is not None:
                                return True

                            if self.retire_time is not None:
                                return True

                            if self.ssci is not None:
                                return True

                            if self.time_to_sak_rekey is not None:
                                return True

                            if self.virtual_port_id is not None:
                                return True

                            if self.wait_time is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_mka_oper as meta
                            return meta._meta_table['Macsec.Mka.Interfaces.Interface.Session.Vp']['meta_info']


                    class Ca(object):
                        """
                        CA List for a Session
                        
                        .. attribute:: authentication_mode
                        
                        	CA Authentication Mode \:PRIMARY\-PSK/FALLBACK\-PSK/EAP
                        	**type**\:  str
                        
                        .. attribute:: authenticator
                        
                        	authenticator
                        	**type**\:  bool
                        
                        .. attribute:: ckn
                        
                        	CKN
                        	**type**\:  str
                        
                        .. attribute:: dormant_peer
                        
                        	Dormant Peer List
                        	**type**\: list of    :py:class:`DormantPeer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_oper.Macsec.Mka.Interfaces.Interface.Session.Ca.DormantPeer>`
                        
                        .. attribute:: first_ca
                        
                        	Is First CA
                        	**type**\:  bool
                        
                        .. attribute:: is_key_server
                        
                        	Is Key Server
                        	**type**\:  bool
                        
                        .. attribute:: key_chain
                        
                        	Key Chain name
                        	**type**\:  str
                        
                        .. attribute:: live_peer
                        
                        	Live Peer List
                        	**type**\: list of    :py:class:`LivePeer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_oper.Macsec.Mka.Interfaces.Interface.Session.Ca.LivePeer>`
                        
                        .. attribute:: my_mi
                        
                        	Member Identifier
                        	**type**\:  str
                        
                        .. attribute:: my_mn
                        
                        	Message Number
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: num_live_peers
                        
                        	Number of Live Peers
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: num_live_peers_responded
                        
                        	Number of Live Peers responded
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: peer_sci
                        
                        	Peer SCI(MAC)
                        	**type**\:  str
                        
                        .. attribute:: potential_peer
                        
                        	Potential Peer List
                        	**type**\: list of    :py:class:`PotentialPeer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_oper.Macsec.Mka.Interfaces.Interface.Session.Ca.PotentialPeer>`
                        
                        .. attribute:: status
                        
                        	Session Status [Secured/Not Secured]
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: status_description
                        
                        	Status Description
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'crypto-macsec-mka-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.authentication_mode = None
                            self.authenticator = None
                            self.ckn = None
                            self.dormant_peer = YList()
                            self.dormant_peer.parent = self
                            self.dormant_peer.name = 'dormant_peer'
                            self.first_ca = None
                            self.is_key_server = None
                            self.key_chain = None
                            self.live_peer = YList()
                            self.live_peer.parent = self
                            self.live_peer.name = 'live_peer'
                            self.my_mi = None
                            self.my_mn = None
                            self.num_live_peers = None
                            self.num_live_peers_responded = None
                            self.peer_sci = None
                            self.potential_peer = YList()
                            self.potential_peer.parent = self
                            self.potential_peer.name = 'potential_peer'
                            self.status = None
                            self.status_description = None


                        class LivePeer(object):
                            """
                            Live Peer List
                            
                            .. attribute:: mi
                            
                            	Member ID
                            	**type**\:  str
                            
                            .. attribute:: mn
                            
                            	Message Number
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: priority
                            
                            	KS Priority
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: sci
                            
                            	Rx SCI
                            	**type**\:  str
                            
                            .. attribute:: ssci
                            
                            	Peer SSCI
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'crypto-macsec-mka-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.mi = None
                                self.mn = None
                                self.priority = None
                                self.sci = None
                                self.ssci = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-mka-oper:live-peer'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.mi is not None:
                                    return True

                                if self.mn is not None:
                                    return True

                                if self.priority is not None:
                                    return True

                                if self.sci is not None:
                                    return True

                                if self.ssci is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_mka_oper as meta
                                return meta._meta_table['Macsec.Mka.Interfaces.Interface.Session.Ca.LivePeer']['meta_info']


                        class PotentialPeer(object):
                            """
                            Potential Peer List
                            
                            .. attribute:: mi
                            
                            	Member ID
                            	**type**\:  str
                            
                            .. attribute:: mn
                            
                            	Message Number
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: priority
                            
                            	KS Priority
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: sci
                            
                            	Rx SCI
                            	**type**\:  str
                            
                            .. attribute:: ssci
                            
                            	Peer SSCI
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'crypto-macsec-mka-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.mi = None
                                self.mn = None
                                self.priority = None
                                self.sci = None
                                self.ssci = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-mka-oper:potential-peer'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.mi is not None:
                                    return True

                                if self.mn is not None:
                                    return True

                                if self.priority is not None:
                                    return True

                                if self.sci is not None:
                                    return True

                                if self.ssci is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_mka_oper as meta
                                return meta._meta_table['Macsec.Mka.Interfaces.Interface.Session.Ca.PotentialPeer']['meta_info']


                        class DormantPeer(object):
                            """
                            Dormant Peer List
                            
                            .. attribute:: mi
                            
                            	Member ID
                            	**type**\:  str
                            
                            .. attribute:: mn
                            
                            	Message Number
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: priority
                            
                            	KS Priority
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: sci
                            
                            	Rx SCI
                            	**type**\:  str
                            
                            .. attribute:: ssci
                            
                            	Peer SSCI
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'crypto-macsec-mka-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.mi = None
                                self.mn = None
                                self.priority = None
                                self.sci = None
                                self.ssci = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-mka-oper:dormant-peer'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.mi is not None:
                                    return True

                                if self.mn is not None:
                                    return True

                                if self.priority is not None:
                                    return True

                                if self.sci is not None:
                                    return True

                                if self.ssci is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_mka_oper as meta
                                return meta._meta_table['Macsec.Mka.Interfaces.Interface.Session.Ca.DormantPeer']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-mka-oper:ca'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.authentication_mode is not None:
                                return True

                            if self.authenticator is not None:
                                return True

                            if self.ckn is not None:
                                return True

                            if self.dormant_peer is not None:
                                for child_ref in self.dormant_peer:
                                    if child_ref._has_data():
                                        return True

                            if self.first_ca is not None:
                                return True

                            if self.is_key_server is not None:
                                return True

                            if self.key_chain is not None:
                                return True

                            if self.live_peer is not None:
                                for child_ref in self.live_peer:
                                    if child_ref._has_data():
                                        return True

                            if self.my_mi is not None:
                                return True

                            if self.my_mn is not None:
                                return True

                            if self.num_live_peers is not None:
                                return True

                            if self.num_live_peers_responded is not None:
                                return True

                            if self.peer_sci is not None:
                                return True

                            if self.potential_peer is not None:
                                for child_ref in self.potential_peer:
                                    if child_ref._has_data():
                                        return True

                            if self.status is not None:
                                return True

                            if self.status_description is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_mka_oper as meta
                            return meta._meta_table['Macsec.Mka.Interfaces.Interface.Session.Ca']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-crypto-macsec-mka-oper:session'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.ca is not None:
                            for child_ref in self.ca:
                                if child_ref._has_data():
                                    return True

                        if self.session_summary is not None and self.session_summary._has_data():
                            return True

                        if self.vp is not None and self.vp._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_mka_oper as meta
                        return meta._meta_table['Macsec.Mka.Interfaces.Interface.Session']['meta_info']

                @property
                def _common_path(self):
                    if self.name is None:
                        raise YPYModelError('Key property name is None')

                    return '/Cisco-IOS-XR-crypto-macsec-mka-oper:macsec/Cisco-IOS-XR-crypto-macsec-mka-oper:mka/Cisco-IOS-XR-crypto-macsec-mka-oper:interfaces/Cisco-IOS-XR-crypto-macsec-mka-oper:interface[Cisco-IOS-XR-crypto-macsec-mka-oper:name = ' + str(self.name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.name is not None:
                        return True

                    if self.session is not None and self.session._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_mka_oper as meta
                    return meta._meta_table['Macsec.Mka.Interfaces.Interface']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-crypto-macsec-mka-oper:macsec/Cisco-IOS-XR-crypto-macsec-mka-oper:mka/Cisco-IOS-XR-crypto-macsec-mka-oper:interfaces'

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
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_mka_oper as meta
                return meta._meta_table['Macsec.Mka.Interfaces']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-crypto-macsec-mka-oper:macsec/Cisco-IOS-XR-crypto-macsec-mka-oper:mka'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.interfaces is not None and self.interfaces._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_mka_oper as meta
            return meta._meta_table['Macsec.Mka']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-crypto-macsec-mka-oper:macsec'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.mka is not None and self.mka._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_macsec_mka_oper as meta
        return meta._meta_table['Macsec']['meta_info']


