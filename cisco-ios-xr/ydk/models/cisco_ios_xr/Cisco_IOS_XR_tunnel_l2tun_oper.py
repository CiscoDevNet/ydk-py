""" Cisco_IOS_XR_tunnel_l2tun_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR tunnel\-l2tun package operational data.

This module contains definitions
for the following management objects\:
  l2tp\: L2TP operational data
  l2tpv2\: l2tpv2

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class DigestHash(Enum):
    """
    DigestHash

    Digest hash types

    .. data:: md5 = 0

    	MD5

    .. data:: sha1 = 1

    	SHA1

    """

    md5 = Enum.YLeaf(0, "md5")

    sha1 = Enum.YLeaf(1, "sha1")



class L2Tp(Entity):
    """
    L2TP operational data
    
    .. attribute:: classes
    
    	List of L2TP class names
    	**type**\:   :py:class:`Classes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tp.Classes>`
    
    .. attribute:: counter_hist_fail
    
    	Failure events leading to disconnection
    	**type**\:   :py:class:`CounterHistFail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tp.CounterHistFail>`
    
    .. attribute:: counters
    
    	L2TP control messages counters
    	**type**\:   :py:class:`Counters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tp.Counters>`
    
    .. attribute:: session
    
    	L2TP control messages counters
    	**type**\:   :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tp.Session>`
    
    .. attribute:: sessions
    
    	List of session IDs
    	**type**\:   :py:class:`Sessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tp.Sessions>`
    
    .. attribute:: tunnel_configurations
    
    	List of tunnel IDs
    	**type**\:   :py:class:`TunnelConfigurations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tp.TunnelConfigurations>`
    
    .. attribute:: tunnels
    
    	List of tunnel IDs
    	**type**\:   :py:class:`Tunnels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tp.Tunnels>`
    
    

    """

    _prefix = 'tunnel-l2tun-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(L2Tp, self).__init__()
        self._top_entity = None

        self.yang_name = "l2tp"
        self.yang_parent_name = "Cisco-IOS-XR-tunnel-l2tun-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"classes" : ("classes", L2Tp.Classes), "counter-hist-fail" : ("counter_hist_fail", L2Tp.CounterHistFail), "counters" : ("counters", L2Tp.Counters), "session" : ("session", L2Tp.Session), "sessions" : ("sessions", L2Tp.Sessions), "tunnel-configurations" : ("tunnel_configurations", L2Tp.TunnelConfigurations), "tunnels" : ("tunnels", L2Tp.Tunnels)}
        self._child_list_classes = {}

        self.classes = L2Tp.Classes()
        self.classes.parent = self
        self._children_name_map["classes"] = "classes"
        self._children_yang_names.add("classes")

        self.counter_hist_fail = L2Tp.CounterHistFail()
        self.counter_hist_fail.parent = self
        self._children_name_map["counter_hist_fail"] = "counter-hist-fail"
        self._children_yang_names.add("counter-hist-fail")

        self.counters = L2Tp.Counters()
        self.counters.parent = self
        self._children_name_map["counters"] = "counters"
        self._children_yang_names.add("counters")

        self.session = L2Tp.Session()
        self.session.parent = self
        self._children_name_map["session"] = "session"
        self._children_yang_names.add("session")

        self.sessions = L2Tp.Sessions()
        self.sessions.parent = self
        self._children_name_map["sessions"] = "sessions"
        self._children_yang_names.add("sessions")

        self.tunnel_configurations = L2Tp.TunnelConfigurations()
        self.tunnel_configurations.parent = self
        self._children_name_map["tunnel_configurations"] = "tunnel-configurations"
        self._children_yang_names.add("tunnel-configurations")

        self.tunnels = L2Tp.Tunnels()
        self.tunnels.parent = self
        self._children_name_map["tunnels"] = "tunnels"
        self._children_yang_names.add("tunnels")
        self._segment_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tp"


    class Classes(Entity):
        """
        List of L2TP class names
        
        .. attribute:: class_
        
        	L2TP class name
        	**type**\: list of    :py:class:`Class_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tp.Classes.Class_>`
        
        

        """

        _prefix = 'tunnel-l2tun-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(L2Tp.Classes, self).__init__()

            self.yang_name = "classes"
            self.yang_parent_name = "l2tp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"class" : ("class_", L2Tp.Classes.Class_)}

            self.class_ = YList(self)
            self._segment_path = lambda: "classes"
            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(L2Tp.Classes, [], name, value)


        class Class_(Entity):
            """
            L2TP class name
            
            .. attribute:: class_name  <key>
            
            	L2TP class name
            	**type**\:  str
            
            	**length:** 1..31
            
            .. attribute:: accounting_method_list
            
            	Accounting List
            	**type**\:  str
            
            	**length:** 0..256
            
            .. attribute:: class_name_xr
            
            	Class name
            	**type**\:  str
            
            	**length:** 0..256
            
            .. attribute:: digest_hash
            
            	Hash configured as MD5 or SHA1
            	**type**\:   :py:class:`DigestHash <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.DigestHash>`
            
            .. attribute:: encoded_password
            
            	Encoded password
            	**type**\:  str
            
            	**length:** 0..256
            
            .. attribute:: hello_timeout
            
            	Hello timeout value in seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: second
            
            .. attribute:: host_name
            
            	Host name
            	**type**\:  str
            
            	**length:** 0..256
            
            .. attribute:: initial_retransmit_maximum_timeout
            
            	Initial timeout maximum in seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: second
            
            .. attribute:: initial_retransmit_minimum_timeout
            
            	Initial timeout minimum in seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: second
            
            .. attribute:: initial_retransmit_retries
            
            	Initial retransmit retries
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ip_tos
            
            	IP TOS
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: is_authentication_enabled
            
            	True if authentication is enabled
            	**type**\:  bool
            
            .. attribute:: is_congestion_control_enabled
            
            	True if congestion control is enabled
            	**type**\:  bool
            
            .. attribute:: is_digest_check_enabled
            
            	True if digest check is enabled
            	**type**\:  bool
            
            .. attribute:: is_digest_enabled
            
            	True if digest authentication is enabled
            	**type**\:  bool
            
            .. attribute:: is_hidden
            
            	True if class is hidden
            	**type**\:  bool
            
            .. attribute:: is_peer_address_checked
            
            	True if peer address is checked
            	**type**\:  bool
            
            .. attribute:: password
            
            	Password
            	**type**\:  str
            
            	**length:** 0..25
            
            .. attribute:: receive_window_size
            
            	Receive window size
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: retransmit_maximum_timeout
            
            	Retransmit maximum timeout in seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: second
            
            .. attribute:: retransmit_minimum_timeout
            
            	Retransmit minimum timeout in seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: second
            
            .. attribute:: retransmit_retries
            
            	Retransmit retries
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: setup_timeout
            
            	Timeout setup value in seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: second
            
            .. attribute:: timeout_no_user
            
            	Timeout no user
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: vrf_name
            
            	VRF name
            	**type**\:  str
            
            	**length:** 0..256
            
            

            """

            _prefix = 'tunnel-l2tun-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(L2Tp.Classes.Class_, self).__init__()

                self.yang_name = "class"
                self.yang_parent_name = "classes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.class_name = YLeaf(YType.str, "class-name")

                self.accounting_method_list = YLeaf(YType.str, "accounting-method-list")

                self.class_name_xr = YLeaf(YType.str, "class-name-xr")

                self.digest_hash = YLeaf(YType.enumeration, "digest-hash")

                self.encoded_password = YLeaf(YType.str, "encoded-password")

                self.hello_timeout = YLeaf(YType.uint32, "hello-timeout")

                self.host_name = YLeaf(YType.str, "host-name")

                self.initial_retransmit_maximum_timeout = YLeaf(YType.uint32, "initial-retransmit-maximum-timeout")

                self.initial_retransmit_minimum_timeout = YLeaf(YType.uint32, "initial-retransmit-minimum-timeout")

                self.initial_retransmit_retries = YLeaf(YType.uint32, "initial-retransmit-retries")

                self.ip_tos = YLeaf(YType.uint8, "ip-tos")

                self.is_authentication_enabled = YLeaf(YType.boolean, "is-authentication-enabled")

                self.is_congestion_control_enabled = YLeaf(YType.boolean, "is-congestion-control-enabled")

                self.is_digest_check_enabled = YLeaf(YType.boolean, "is-digest-check-enabled")

                self.is_digest_enabled = YLeaf(YType.boolean, "is-digest-enabled")

                self.is_hidden = YLeaf(YType.boolean, "is-hidden")

                self.is_peer_address_checked = YLeaf(YType.boolean, "is-peer-address-checked")

                self.password = YLeaf(YType.str, "password")

                self.receive_window_size = YLeaf(YType.uint16, "receive-window-size")

                self.retransmit_maximum_timeout = YLeaf(YType.uint32, "retransmit-maximum-timeout")

                self.retransmit_minimum_timeout = YLeaf(YType.uint32, "retransmit-minimum-timeout")

                self.retransmit_retries = YLeaf(YType.uint32, "retransmit-retries")

                self.setup_timeout = YLeaf(YType.uint32, "setup-timeout")

                self.timeout_no_user = YLeaf(YType.uint32, "timeout-no-user")

                self.vrf_name = YLeaf(YType.str, "vrf-name")
                self._segment_path = lambda: "class" + "[class-name='" + self.class_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/classes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(L2Tp.Classes.Class_, ['class_name', 'accounting_method_list', 'class_name_xr', 'digest_hash', 'encoded_password', 'hello_timeout', 'host_name', 'initial_retransmit_maximum_timeout', 'initial_retransmit_minimum_timeout', 'initial_retransmit_retries', 'ip_tos', 'is_authentication_enabled', 'is_congestion_control_enabled', 'is_digest_check_enabled', 'is_digest_enabled', 'is_hidden', 'is_peer_address_checked', 'password', 'receive_window_size', 'retransmit_maximum_timeout', 'retransmit_minimum_timeout', 'retransmit_retries', 'setup_timeout', 'timeout_no_user', 'vrf_name'], name, value)


    class CounterHistFail(Entity):
        """
        Failure events leading to disconnection
        
        .. attribute:: pkt_timeout
        
        	timeout events by packet
        	**type**\:  list of int
        
        	**range:** 0..4294967295
        
        .. attribute:: rx_counters
        
        	Receive side counters
        	**type**\:  str
        
        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
        
        .. attribute:: sess_down_tmout
        
        	sesions affected due to timeout
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: tx_counters
        
        	Send side counters
        	**type**\:  str
        
        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
        
        

        """

        _prefix = 'tunnel-l2tun-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(L2Tp.CounterHistFail, self).__init__()

            self.yang_name = "counter-hist-fail"
            self.yang_parent_name = "l2tp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.pkt_timeout = YLeafList(YType.uint32, "pkt-timeout")

            self.rx_counters = YLeaf(YType.str, "rx-counters")

            self.sess_down_tmout = YLeaf(YType.uint32, "sess-down-tmout")

            self.tx_counters = YLeaf(YType.str, "tx-counters")
            self._segment_path = lambda: "counter-hist-fail"
            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(L2Tp.CounterHistFail, ['pkt_timeout', 'rx_counters', 'sess_down_tmout', 'tx_counters'], name, value)


    class Counters(Entity):
        """
        L2TP control messages counters
        
        .. attribute:: control
        
        	L2TP control messages counters
        	**type**\:   :py:class:`Control <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tp.Counters.Control>`
        
        

        """

        _prefix = 'tunnel-l2tun-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(L2Tp.Counters, self).__init__()

            self.yang_name = "counters"
            self.yang_parent_name = "l2tp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"control" : ("control", L2Tp.Counters.Control)}
            self._child_list_classes = {}

            self.control = L2Tp.Counters.Control()
            self.control.parent = self
            self._children_name_map["control"] = "control"
            self._children_yang_names.add("control")
            self._segment_path = lambda: "counters"
            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/%s" % self._segment_path()


        class Control(Entity):
            """
            L2TP control messages counters
            
            .. attribute:: tunnel_xr
            
            	L2TP control tunnel messages counters
            	**type**\:   :py:class:`TunnelXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tp.Counters.Control.TunnelXr>`
            
            .. attribute:: tunnels
            
            	Table of tunnel IDs of control message counters
            	**type**\:   :py:class:`Tunnels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tp.Counters.Control.Tunnels>`
            
            

            """

            _prefix = 'tunnel-l2tun-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(L2Tp.Counters.Control, self).__init__()

                self.yang_name = "control"
                self.yang_parent_name = "counters"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"tunnel-xr" : ("tunnel_xr", L2Tp.Counters.Control.TunnelXr), "tunnels" : ("tunnels", L2Tp.Counters.Control.Tunnels)}
                self._child_list_classes = {}

                self.tunnel_xr = L2Tp.Counters.Control.TunnelXr()
                self.tunnel_xr.parent = self
                self._children_name_map["tunnel_xr"] = "tunnel-xr"
                self._children_yang_names.add("tunnel-xr")

                self.tunnels = L2Tp.Counters.Control.Tunnels()
                self.tunnels.parent = self
                self._children_name_map["tunnels"] = "tunnels"
                self._children_yang_names.add("tunnels")
                self._segment_path = lambda: "control"
                self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/counters/%s" % self._segment_path()


            class TunnelXr(Entity):
                """
                L2TP control tunnel messages counters
                
                .. attribute:: authentication
                
                	Tunnel authentication counters
                	**type**\:   :py:class:`Authentication <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tp.Counters.Control.TunnelXr.Authentication>`
                
                .. attribute:: global_
                
                	Tunnel counters
                	**type**\:   :py:class:`Global_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tp.Counters.Control.TunnelXr.Global_>`
                
                

                """

                _prefix = 'tunnel-l2tun-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(L2Tp.Counters.Control.TunnelXr, self).__init__()

                    self.yang_name = "tunnel-xr"
                    self.yang_parent_name = "control"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"authentication" : ("authentication", L2Tp.Counters.Control.TunnelXr.Authentication), "global" : ("global_", L2Tp.Counters.Control.TunnelXr.Global_)}
                    self._child_list_classes = {}

                    self.authentication = L2Tp.Counters.Control.TunnelXr.Authentication()
                    self.authentication.parent = self
                    self._children_name_map["authentication"] = "authentication"
                    self._children_yang_names.add("authentication")

                    self.global_ = L2Tp.Counters.Control.TunnelXr.Global_()
                    self.global_.parent = self
                    self._children_name_map["global_"] = "global"
                    self._children_yang_names.add("global")
                    self._segment_path = lambda: "tunnel-xr"
                    self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/counters/control/%s" % self._segment_path()


                class Authentication(Entity):
                    """
                    Tunnel authentication counters
                    
                    .. attribute:: challenge_avp
                    
                    	Challenge AVP statistics
                    	**type**\:   :py:class:`ChallengeAvp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tp.Counters.Control.TunnelXr.Authentication.ChallengeAvp>`
                    
                    .. attribute:: challenge_reponse
                    
                    	Challenge response statistics
                    	**type**\:   :py:class:`ChallengeReponse <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tp.Counters.Control.TunnelXr.Authentication.ChallengeReponse>`
                    
                    .. attribute:: common_digest
                    
                    	Common digest statistics
                    	**type**\:   :py:class:`CommonDigest <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tp.Counters.Control.TunnelXr.Authentication.CommonDigest>`
                    
                    .. attribute:: integrity_check
                    
                    	Integrity check statistics
                    	**type**\:   :py:class:`IntegrityCheck <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tp.Counters.Control.TunnelXr.Authentication.IntegrityCheck>`
                    
                    .. attribute:: local_secret
                    
                    	Local secret statistics
                    	**type**\:   :py:class:`LocalSecret <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tp.Counters.Control.TunnelXr.Authentication.LocalSecret>`
                    
                    .. attribute:: nonce_avp
                    
                    	Nonce AVP statistics
                    	**type**\:   :py:class:`NonceAvp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tp.Counters.Control.TunnelXr.Authentication.NonceAvp>`
                    
                    .. attribute:: overall_statistics
                    
                    	Overall statistics
                    	**type**\:   :py:class:`OverallStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tp.Counters.Control.TunnelXr.Authentication.OverallStatistics>`
                    
                    .. attribute:: primary_digest
                    
                    	Primary digest statistics
                    	**type**\:   :py:class:`PrimaryDigest <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tp.Counters.Control.TunnelXr.Authentication.PrimaryDigest>`
                    
                    .. attribute:: secondary_digest
                    
                    	Secondary digest statistics
                    	**type**\:   :py:class:`SecondaryDigest <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tp.Counters.Control.TunnelXr.Authentication.SecondaryDigest>`
                    
                    

                    """

                    _prefix = 'tunnel-l2tun-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(L2Tp.Counters.Control.TunnelXr.Authentication, self).__init__()

                        self.yang_name = "authentication"
                        self.yang_parent_name = "tunnel-xr"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"challenge-avp" : ("challenge_avp", L2Tp.Counters.Control.TunnelXr.Authentication.ChallengeAvp), "challenge-reponse" : ("challenge_reponse", L2Tp.Counters.Control.TunnelXr.Authentication.ChallengeReponse), "common-digest" : ("common_digest", L2Tp.Counters.Control.TunnelXr.Authentication.CommonDigest), "integrity-check" : ("integrity_check", L2Tp.Counters.Control.TunnelXr.Authentication.IntegrityCheck), "local-secret" : ("local_secret", L2Tp.Counters.Control.TunnelXr.Authentication.LocalSecret), "nonce-avp" : ("nonce_avp", L2Tp.Counters.Control.TunnelXr.Authentication.NonceAvp), "overall-statistics" : ("overall_statistics", L2Tp.Counters.Control.TunnelXr.Authentication.OverallStatistics), "primary-digest" : ("primary_digest", L2Tp.Counters.Control.TunnelXr.Authentication.PrimaryDigest), "secondary-digest" : ("secondary_digest", L2Tp.Counters.Control.TunnelXr.Authentication.SecondaryDigest)}
                        self._child_list_classes = {}

                        self.challenge_avp = L2Tp.Counters.Control.TunnelXr.Authentication.ChallengeAvp()
                        self.challenge_avp.parent = self
                        self._children_name_map["challenge_avp"] = "challenge-avp"
                        self._children_yang_names.add("challenge-avp")

                        self.challenge_reponse = L2Tp.Counters.Control.TunnelXr.Authentication.ChallengeReponse()
                        self.challenge_reponse.parent = self
                        self._children_name_map["challenge_reponse"] = "challenge-reponse"
                        self._children_yang_names.add("challenge-reponse")

                        self.common_digest = L2Tp.Counters.Control.TunnelXr.Authentication.CommonDigest()
                        self.common_digest.parent = self
                        self._children_name_map["common_digest"] = "common-digest"
                        self._children_yang_names.add("common-digest")

                        self.integrity_check = L2Tp.Counters.Control.TunnelXr.Authentication.IntegrityCheck()
                        self.integrity_check.parent = self
                        self._children_name_map["integrity_check"] = "integrity-check"
                        self._children_yang_names.add("integrity-check")

                        self.local_secret = L2Tp.Counters.Control.TunnelXr.Authentication.LocalSecret()
                        self.local_secret.parent = self
                        self._children_name_map["local_secret"] = "local-secret"
                        self._children_yang_names.add("local-secret")

                        self.nonce_avp = L2Tp.Counters.Control.TunnelXr.Authentication.NonceAvp()
                        self.nonce_avp.parent = self
                        self._children_name_map["nonce_avp"] = "nonce-avp"
                        self._children_yang_names.add("nonce-avp")

                        self.overall_statistics = L2Tp.Counters.Control.TunnelXr.Authentication.OverallStatistics()
                        self.overall_statistics.parent = self
                        self._children_name_map["overall_statistics"] = "overall-statistics"
                        self._children_yang_names.add("overall-statistics")

                        self.primary_digest = L2Tp.Counters.Control.TunnelXr.Authentication.PrimaryDigest()
                        self.primary_digest.parent = self
                        self._children_name_map["primary_digest"] = "primary-digest"
                        self._children_yang_names.add("primary-digest")

                        self.secondary_digest = L2Tp.Counters.Control.TunnelXr.Authentication.SecondaryDigest()
                        self.secondary_digest.parent = self
                        self._children_name_map["secondary_digest"] = "secondary-digest"
                        self._children_yang_names.add("secondary-digest")
                        self._segment_path = lambda: "authentication"
                        self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/counters/control/tunnel-xr/%s" % self._segment_path()


                    class ChallengeAvp(Entity):
                        """
                        Challenge AVP statistics
                        
                        .. attribute:: bad_hash
                        
                        	Bad hash
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_length
                        
                        	Bad length
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: failed
                        
                        	Failed
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: generate_response_failures
                        
                        	Generate response fail
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ignored
                        
                        	Ignored
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: missing
                        
                        	Missing
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: passed
                        
                        	Passed
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: skipped
                        
                        	Skipped
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unexpected
                        
                        	Unexpected
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unexpected_zlb
                        
                        	Unexpected ZLB
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: validate
                        
                        	Validate
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'tunnel-l2tun-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(L2Tp.Counters.Control.TunnelXr.Authentication.ChallengeAvp, self).__init__()

                            self.yang_name = "challenge-avp"
                            self.yang_parent_name = "authentication"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.bad_hash = YLeaf(YType.uint32, "bad-hash")

                            self.bad_length = YLeaf(YType.uint32, "bad-length")

                            self.failed = YLeaf(YType.uint32, "failed")

                            self.generate_response_failures = YLeaf(YType.uint32, "generate-response-failures")

                            self.ignored = YLeaf(YType.uint32, "ignored")

                            self.missing = YLeaf(YType.uint32, "missing")

                            self.passed = YLeaf(YType.uint32, "passed")

                            self.skipped = YLeaf(YType.uint32, "skipped")

                            self.unexpected = YLeaf(YType.uint32, "unexpected")

                            self.unexpected_zlb = YLeaf(YType.uint32, "unexpected-zlb")

                            self.validate = YLeaf(YType.uint32, "validate")
                            self._segment_path = lambda: "challenge-avp"
                            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/counters/control/tunnel-xr/authentication/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2Tp.Counters.Control.TunnelXr.Authentication.ChallengeAvp, ['bad_hash', 'bad_length', 'failed', 'generate_response_failures', 'ignored', 'missing', 'passed', 'skipped', 'unexpected', 'unexpected_zlb', 'validate'], name, value)


                    class ChallengeReponse(Entity):
                        """
                        Challenge response statistics
                        
                        .. attribute:: bad_hash
                        
                        	Bad hash
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_length
                        
                        	Bad length
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: failed
                        
                        	Failed
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: generate_response_failures
                        
                        	Generate response fail
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ignored
                        
                        	Ignored
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: missing
                        
                        	Missing
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: passed
                        
                        	Passed
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: skipped
                        
                        	Skipped
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unexpected
                        
                        	Unexpected
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unexpected_zlb
                        
                        	Unexpected ZLB
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: validate
                        
                        	Validate
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'tunnel-l2tun-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(L2Tp.Counters.Control.TunnelXr.Authentication.ChallengeReponse, self).__init__()

                            self.yang_name = "challenge-reponse"
                            self.yang_parent_name = "authentication"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.bad_hash = YLeaf(YType.uint32, "bad-hash")

                            self.bad_length = YLeaf(YType.uint32, "bad-length")

                            self.failed = YLeaf(YType.uint32, "failed")

                            self.generate_response_failures = YLeaf(YType.uint32, "generate-response-failures")

                            self.ignored = YLeaf(YType.uint32, "ignored")

                            self.missing = YLeaf(YType.uint32, "missing")

                            self.passed = YLeaf(YType.uint32, "passed")

                            self.skipped = YLeaf(YType.uint32, "skipped")

                            self.unexpected = YLeaf(YType.uint32, "unexpected")

                            self.unexpected_zlb = YLeaf(YType.uint32, "unexpected-zlb")

                            self.validate = YLeaf(YType.uint32, "validate")
                            self._segment_path = lambda: "challenge-reponse"
                            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/counters/control/tunnel-xr/authentication/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2Tp.Counters.Control.TunnelXr.Authentication.ChallengeReponse, ['bad_hash', 'bad_length', 'failed', 'generate_response_failures', 'ignored', 'missing', 'passed', 'skipped', 'unexpected', 'unexpected_zlb', 'validate'], name, value)


                    class CommonDigest(Entity):
                        """
                        Common digest statistics
                        
                        .. attribute:: bad_hash
                        
                        	Bad hash
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_length
                        
                        	Bad length
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: failed
                        
                        	Failed
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: generate_response_failures
                        
                        	Generate response fail
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ignored
                        
                        	Ignored
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: missing
                        
                        	Missing
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: passed
                        
                        	Passed
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: skipped
                        
                        	Skipped
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unexpected
                        
                        	Unexpected
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unexpected_zlb
                        
                        	Unexpected ZLB
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: validate
                        
                        	Validate
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'tunnel-l2tun-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(L2Tp.Counters.Control.TunnelXr.Authentication.CommonDigest, self).__init__()

                            self.yang_name = "common-digest"
                            self.yang_parent_name = "authentication"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.bad_hash = YLeaf(YType.uint32, "bad-hash")

                            self.bad_length = YLeaf(YType.uint32, "bad-length")

                            self.failed = YLeaf(YType.uint32, "failed")

                            self.generate_response_failures = YLeaf(YType.uint32, "generate-response-failures")

                            self.ignored = YLeaf(YType.uint32, "ignored")

                            self.missing = YLeaf(YType.uint32, "missing")

                            self.passed = YLeaf(YType.uint32, "passed")

                            self.skipped = YLeaf(YType.uint32, "skipped")

                            self.unexpected = YLeaf(YType.uint32, "unexpected")

                            self.unexpected_zlb = YLeaf(YType.uint32, "unexpected-zlb")

                            self.validate = YLeaf(YType.uint32, "validate")
                            self._segment_path = lambda: "common-digest"
                            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/counters/control/tunnel-xr/authentication/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2Tp.Counters.Control.TunnelXr.Authentication.CommonDigest, ['bad_hash', 'bad_length', 'failed', 'generate_response_failures', 'ignored', 'missing', 'passed', 'skipped', 'unexpected', 'unexpected_zlb', 'validate'], name, value)


                    class IntegrityCheck(Entity):
                        """
                        Integrity check statistics
                        
                        .. attribute:: bad_hash
                        
                        	Bad hash
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_length
                        
                        	Bad length
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: failed
                        
                        	Failed
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: generate_response_failures
                        
                        	Generate response fail
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ignored
                        
                        	Ignored
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: missing
                        
                        	Missing
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: passed
                        
                        	Passed
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: skipped
                        
                        	Skipped
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unexpected
                        
                        	Unexpected
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unexpected_zlb
                        
                        	Unexpected ZLB
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: validate
                        
                        	Validate
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'tunnel-l2tun-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(L2Tp.Counters.Control.TunnelXr.Authentication.IntegrityCheck, self).__init__()

                            self.yang_name = "integrity-check"
                            self.yang_parent_name = "authentication"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.bad_hash = YLeaf(YType.uint32, "bad-hash")

                            self.bad_length = YLeaf(YType.uint32, "bad-length")

                            self.failed = YLeaf(YType.uint32, "failed")

                            self.generate_response_failures = YLeaf(YType.uint32, "generate-response-failures")

                            self.ignored = YLeaf(YType.uint32, "ignored")

                            self.missing = YLeaf(YType.uint32, "missing")

                            self.passed = YLeaf(YType.uint32, "passed")

                            self.skipped = YLeaf(YType.uint32, "skipped")

                            self.unexpected = YLeaf(YType.uint32, "unexpected")

                            self.unexpected_zlb = YLeaf(YType.uint32, "unexpected-zlb")

                            self.validate = YLeaf(YType.uint32, "validate")
                            self._segment_path = lambda: "integrity-check"
                            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/counters/control/tunnel-xr/authentication/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2Tp.Counters.Control.TunnelXr.Authentication.IntegrityCheck, ['bad_hash', 'bad_length', 'failed', 'generate_response_failures', 'ignored', 'missing', 'passed', 'skipped', 'unexpected', 'unexpected_zlb', 'validate'], name, value)


                    class LocalSecret(Entity):
                        """
                        Local secret statistics
                        
                        .. attribute:: bad_hash
                        
                        	Bad hash
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_length
                        
                        	Bad length
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: failed
                        
                        	Failed
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: generate_response_failures
                        
                        	Generate response fail
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ignored
                        
                        	Ignored
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: missing
                        
                        	Missing
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: passed
                        
                        	Passed
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: skipped
                        
                        	Skipped
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unexpected
                        
                        	Unexpected
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unexpected_zlb
                        
                        	Unexpected ZLB
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: validate
                        
                        	Validate
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'tunnel-l2tun-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(L2Tp.Counters.Control.TunnelXr.Authentication.LocalSecret, self).__init__()

                            self.yang_name = "local-secret"
                            self.yang_parent_name = "authentication"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.bad_hash = YLeaf(YType.uint32, "bad-hash")

                            self.bad_length = YLeaf(YType.uint32, "bad-length")

                            self.failed = YLeaf(YType.uint32, "failed")

                            self.generate_response_failures = YLeaf(YType.uint32, "generate-response-failures")

                            self.ignored = YLeaf(YType.uint32, "ignored")

                            self.missing = YLeaf(YType.uint32, "missing")

                            self.passed = YLeaf(YType.uint32, "passed")

                            self.skipped = YLeaf(YType.uint32, "skipped")

                            self.unexpected = YLeaf(YType.uint32, "unexpected")

                            self.unexpected_zlb = YLeaf(YType.uint32, "unexpected-zlb")

                            self.validate = YLeaf(YType.uint32, "validate")
                            self._segment_path = lambda: "local-secret"
                            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/counters/control/tunnel-xr/authentication/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2Tp.Counters.Control.TunnelXr.Authentication.LocalSecret, ['bad_hash', 'bad_length', 'failed', 'generate_response_failures', 'ignored', 'missing', 'passed', 'skipped', 'unexpected', 'unexpected_zlb', 'validate'], name, value)


                    class NonceAvp(Entity):
                        """
                        Nonce AVP statistics
                        
                        .. attribute:: bad_hash
                        
                        	Bad hash
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_length
                        
                        	Bad length
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: failed
                        
                        	Failed
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: generate_response_failures
                        
                        	Generate response fail
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ignored
                        
                        	Ignored
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: missing
                        
                        	Missing
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: passed
                        
                        	Passed
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: skipped
                        
                        	Skipped
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unexpected
                        
                        	Unexpected
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unexpected_zlb
                        
                        	Unexpected ZLB
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: validate
                        
                        	Validate
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'tunnel-l2tun-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(L2Tp.Counters.Control.TunnelXr.Authentication.NonceAvp, self).__init__()

                            self.yang_name = "nonce-avp"
                            self.yang_parent_name = "authentication"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.bad_hash = YLeaf(YType.uint32, "bad-hash")

                            self.bad_length = YLeaf(YType.uint32, "bad-length")

                            self.failed = YLeaf(YType.uint32, "failed")

                            self.generate_response_failures = YLeaf(YType.uint32, "generate-response-failures")

                            self.ignored = YLeaf(YType.uint32, "ignored")

                            self.missing = YLeaf(YType.uint32, "missing")

                            self.passed = YLeaf(YType.uint32, "passed")

                            self.skipped = YLeaf(YType.uint32, "skipped")

                            self.unexpected = YLeaf(YType.uint32, "unexpected")

                            self.unexpected_zlb = YLeaf(YType.uint32, "unexpected-zlb")

                            self.validate = YLeaf(YType.uint32, "validate")
                            self._segment_path = lambda: "nonce-avp"
                            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/counters/control/tunnel-xr/authentication/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2Tp.Counters.Control.TunnelXr.Authentication.NonceAvp, ['bad_hash', 'bad_length', 'failed', 'generate_response_failures', 'ignored', 'missing', 'passed', 'skipped', 'unexpected', 'unexpected_zlb', 'validate'], name, value)


                    class OverallStatistics(Entity):
                        """
                        Overall statistics
                        
                        .. attribute:: bad_hash
                        
                        	Bad hash
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_length
                        
                        	Bad length
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: failed
                        
                        	Failed
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: generate_response_failures
                        
                        	Generate response fail
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ignored
                        
                        	Ignored
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: missing
                        
                        	Missing
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: passed
                        
                        	Passed
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: skipped
                        
                        	Skipped
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unexpected
                        
                        	Unexpected
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unexpected_zlb
                        
                        	Unexpected ZLB
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: validate
                        
                        	Validate
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'tunnel-l2tun-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(L2Tp.Counters.Control.TunnelXr.Authentication.OverallStatistics, self).__init__()

                            self.yang_name = "overall-statistics"
                            self.yang_parent_name = "authentication"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.bad_hash = YLeaf(YType.uint32, "bad-hash")

                            self.bad_length = YLeaf(YType.uint32, "bad-length")

                            self.failed = YLeaf(YType.uint32, "failed")

                            self.generate_response_failures = YLeaf(YType.uint32, "generate-response-failures")

                            self.ignored = YLeaf(YType.uint32, "ignored")

                            self.missing = YLeaf(YType.uint32, "missing")

                            self.passed = YLeaf(YType.uint32, "passed")

                            self.skipped = YLeaf(YType.uint32, "skipped")

                            self.unexpected = YLeaf(YType.uint32, "unexpected")

                            self.unexpected_zlb = YLeaf(YType.uint32, "unexpected-zlb")

                            self.validate = YLeaf(YType.uint32, "validate")
                            self._segment_path = lambda: "overall-statistics"
                            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/counters/control/tunnel-xr/authentication/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2Tp.Counters.Control.TunnelXr.Authentication.OverallStatistics, ['bad_hash', 'bad_length', 'failed', 'generate_response_failures', 'ignored', 'missing', 'passed', 'skipped', 'unexpected', 'unexpected_zlb', 'validate'], name, value)


                    class PrimaryDigest(Entity):
                        """
                        Primary digest statistics
                        
                        .. attribute:: bad_hash
                        
                        	Bad hash
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_length
                        
                        	Bad length
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: failed
                        
                        	Failed
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: generate_response_failures
                        
                        	Generate response fail
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ignored
                        
                        	Ignored
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: missing
                        
                        	Missing
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: passed
                        
                        	Passed
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: skipped
                        
                        	Skipped
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unexpected
                        
                        	Unexpected
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unexpected_zlb
                        
                        	Unexpected ZLB
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: validate
                        
                        	Validate
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'tunnel-l2tun-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(L2Tp.Counters.Control.TunnelXr.Authentication.PrimaryDigest, self).__init__()

                            self.yang_name = "primary-digest"
                            self.yang_parent_name = "authentication"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.bad_hash = YLeaf(YType.uint32, "bad-hash")

                            self.bad_length = YLeaf(YType.uint32, "bad-length")

                            self.failed = YLeaf(YType.uint32, "failed")

                            self.generate_response_failures = YLeaf(YType.uint32, "generate-response-failures")

                            self.ignored = YLeaf(YType.uint32, "ignored")

                            self.missing = YLeaf(YType.uint32, "missing")

                            self.passed = YLeaf(YType.uint32, "passed")

                            self.skipped = YLeaf(YType.uint32, "skipped")

                            self.unexpected = YLeaf(YType.uint32, "unexpected")

                            self.unexpected_zlb = YLeaf(YType.uint32, "unexpected-zlb")

                            self.validate = YLeaf(YType.uint32, "validate")
                            self._segment_path = lambda: "primary-digest"
                            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/counters/control/tunnel-xr/authentication/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2Tp.Counters.Control.TunnelXr.Authentication.PrimaryDigest, ['bad_hash', 'bad_length', 'failed', 'generate_response_failures', 'ignored', 'missing', 'passed', 'skipped', 'unexpected', 'unexpected_zlb', 'validate'], name, value)


                    class SecondaryDigest(Entity):
                        """
                        Secondary digest statistics
                        
                        .. attribute:: bad_hash
                        
                        	Bad hash
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_length
                        
                        	Bad length
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: failed
                        
                        	Failed
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: generate_response_failures
                        
                        	Generate response fail
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ignored
                        
                        	Ignored
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: missing
                        
                        	Missing
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: passed
                        
                        	Passed
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: skipped
                        
                        	Skipped
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unexpected
                        
                        	Unexpected
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unexpected_zlb
                        
                        	Unexpected ZLB
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: validate
                        
                        	Validate
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'tunnel-l2tun-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(L2Tp.Counters.Control.TunnelXr.Authentication.SecondaryDigest, self).__init__()

                            self.yang_name = "secondary-digest"
                            self.yang_parent_name = "authentication"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.bad_hash = YLeaf(YType.uint32, "bad-hash")

                            self.bad_length = YLeaf(YType.uint32, "bad-length")

                            self.failed = YLeaf(YType.uint32, "failed")

                            self.generate_response_failures = YLeaf(YType.uint32, "generate-response-failures")

                            self.ignored = YLeaf(YType.uint32, "ignored")

                            self.missing = YLeaf(YType.uint32, "missing")

                            self.passed = YLeaf(YType.uint32, "passed")

                            self.skipped = YLeaf(YType.uint32, "skipped")

                            self.unexpected = YLeaf(YType.uint32, "unexpected")

                            self.unexpected_zlb = YLeaf(YType.uint32, "unexpected-zlb")

                            self.validate = YLeaf(YType.uint32, "validate")
                            self._segment_path = lambda: "secondary-digest"
                            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/counters/control/tunnel-xr/authentication/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2Tp.Counters.Control.TunnelXr.Authentication.SecondaryDigest, ['bad_hash', 'bad_length', 'failed', 'generate_response_failures', 'ignored', 'missing', 'passed', 'skipped', 'unexpected', 'unexpected_zlb', 'validate'], name, value)


                class Global_(Entity):
                    """
                    Tunnel counters
                    
                    .. attribute:: drop
                    
                    	Drop data
                    	**type**\:   :py:class:`Drop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tp.Counters.Control.TunnelXr.Global_.Drop>`
                    
                    .. attribute:: received
                    
                    	Received data
                    	**type**\:   :py:class:`Received <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tp.Counters.Control.TunnelXr.Global_.Received>`
                    
                    .. attribute:: retransmit
                    
                    	Re transmit data
                    	**type**\:   :py:class:`Retransmit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tp.Counters.Control.TunnelXr.Global_.Retransmit>`
                    
                    .. attribute:: total_drop
                    
                    	Total drop
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: total_received
                    
                    	Total received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: total_retransmit
                    
                    	Total retransmit
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: total_transmit
                    
                    	Total transmit
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: transmit
                    
                    	Transmit data
                    	**type**\:   :py:class:`Transmit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tp.Counters.Control.TunnelXr.Global_.Transmit>`
                    
                    

                    """

                    _prefix = 'tunnel-l2tun-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(L2Tp.Counters.Control.TunnelXr.Global_, self).__init__()

                        self.yang_name = "global"
                        self.yang_parent_name = "tunnel-xr"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"drop" : ("drop", L2Tp.Counters.Control.TunnelXr.Global_.Drop), "received" : ("received", L2Tp.Counters.Control.TunnelXr.Global_.Received), "retransmit" : ("retransmit", L2Tp.Counters.Control.TunnelXr.Global_.Retransmit), "transmit" : ("transmit", L2Tp.Counters.Control.TunnelXr.Global_.Transmit)}
                        self._child_list_classes = {}

                        self.total_drop = YLeaf(YType.uint32, "total-drop")

                        self.total_received = YLeaf(YType.uint32, "total-received")

                        self.total_retransmit = YLeaf(YType.uint32, "total-retransmit")

                        self.total_transmit = YLeaf(YType.uint32, "total-transmit")

                        self.drop = L2Tp.Counters.Control.TunnelXr.Global_.Drop()
                        self.drop.parent = self
                        self._children_name_map["drop"] = "drop"
                        self._children_yang_names.add("drop")

                        self.received = L2Tp.Counters.Control.TunnelXr.Global_.Received()
                        self.received.parent = self
                        self._children_name_map["received"] = "received"
                        self._children_yang_names.add("received")

                        self.retransmit = L2Tp.Counters.Control.TunnelXr.Global_.Retransmit()
                        self.retransmit.parent = self
                        self._children_name_map["retransmit"] = "retransmit"
                        self._children_yang_names.add("retransmit")

                        self.transmit = L2Tp.Counters.Control.TunnelXr.Global_.Transmit()
                        self.transmit.parent = self
                        self._children_name_map["transmit"] = "transmit"
                        self._children_yang_names.add("transmit")
                        self._segment_path = lambda: "global"
                        self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/counters/control/tunnel-xr/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2Tp.Counters.Control.TunnelXr.Global_, ['total_drop', 'total_received', 'total_retransmit', 'total_transmit'], name, value)


                    class Drop(Entity):
                        """
                        Drop data
                        
                        .. attribute:: acknowledgement_packets
                        
                        	Packets acknowledgement
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: call_disconnect_notify_packets
                        
                        	Call disconnect notify packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: hello_packets
                        
                        	Keep alive messages
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: incoming_call_connected_packets
                        
                        	Incoming call connected packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: incoming_call_replies
                        
                        	Incoming call replies
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: incoming_call_requests
                        
                        	Incoming call requests
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: outgoing_call_connected_packets
                        
                        	Outgoing call connected packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: outgoing_call_replies
                        
                        	Outgoing call replies
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: outgoing_call_requests
                        
                        	Outgoing call requests
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: service_relay_replies
                        
                        	Service relay reply counts
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: service_relay_requests
                        
                        	Service relay request counts
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: set_link_info_packets
                        
                        	Set link info packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: start_control_connection_notifications
                        
                        	Start control connection notifications
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: start_control_connection_replies
                        
                        	Start control connection replies
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: start_control_connection_requests
                        
                        	Start control connection requests
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: stop_control_connection_notifications
                        
                        	Stop control connection notifications
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unknown_packets
                        
                        	Unknown packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: wan_error_notify_packets
                        
                        	WAN error notify packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: zero_length_body_packets
                        
                        	Zero length body packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'tunnel-l2tun-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(L2Tp.Counters.Control.TunnelXr.Global_.Drop, self).__init__()

                            self.yang_name = "drop"
                            self.yang_parent_name = "global"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.acknowledgement_packets = YLeaf(YType.uint32, "acknowledgement-packets")

                            self.call_disconnect_notify_packets = YLeaf(YType.uint32, "call-disconnect-notify-packets")

                            self.hello_packets = YLeaf(YType.uint32, "hello-packets")

                            self.incoming_call_connected_packets = YLeaf(YType.uint32, "incoming-call-connected-packets")

                            self.incoming_call_replies = YLeaf(YType.uint32, "incoming-call-replies")

                            self.incoming_call_requests = YLeaf(YType.uint32, "incoming-call-requests")

                            self.outgoing_call_connected_packets = YLeaf(YType.uint32, "outgoing-call-connected-packets")

                            self.outgoing_call_replies = YLeaf(YType.uint32, "outgoing-call-replies")

                            self.outgoing_call_requests = YLeaf(YType.uint32, "outgoing-call-requests")

                            self.service_relay_replies = YLeaf(YType.uint32, "service-relay-replies")

                            self.service_relay_requests = YLeaf(YType.uint32, "service-relay-requests")

                            self.set_link_info_packets = YLeaf(YType.uint32, "set-link-info-packets")

                            self.start_control_connection_notifications = YLeaf(YType.uint32, "start-control-connection-notifications")

                            self.start_control_connection_replies = YLeaf(YType.uint32, "start-control-connection-replies")

                            self.start_control_connection_requests = YLeaf(YType.uint32, "start-control-connection-requests")

                            self.stop_control_connection_notifications = YLeaf(YType.uint32, "stop-control-connection-notifications")

                            self.unknown_packets = YLeaf(YType.uint32, "unknown-packets")

                            self.wan_error_notify_packets = YLeaf(YType.uint32, "wan-error-notify-packets")

                            self.zero_length_body_packets = YLeaf(YType.uint32, "zero-length-body-packets")
                            self._segment_path = lambda: "drop"
                            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/counters/control/tunnel-xr/global/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2Tp.Counters.Control.TunnelXr.Global_.Drop, ['acknowledgement_packets', 'call_disconnect_notify_packets', 'hello_packets', 'incoming_call_connected_packets', 'incoming_call_replies', 'incoming_call_requests', 'outgoing_call_connected_packets', 'outgoing_call_replies', 'outgoing_call_requests', 'service_relay_replies', 'service_relay_requests', 'set_link_info_packets', 'start_control_connection_notifications', 'start_control_connection_replies', 'start_control_connection_requests', 'stop_control_connection_notifications', 'unknown_packets', 'wan_error_notify_packets', 'zero_length_body_packets'], name, value)


                    class Received(Entity):
                        """
                        Received data
                        
                        .. attribute:: acknowledgement_packets
                        
                        	Packets acknowledgement
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: call_disconnect_notify_packets
                        
                        	Call disconnect notify packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: hello_packets
                        
                        	Keep alive messages
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: incoming_call_connected_packets
                        
                        	Incoming call connected packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: incoming_call_replies
                        
                        	Incoming call replies
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: incoming_call_requests
                        
                        	Incoming call requests
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: outgoing_call_connected_packets
                        
                        	Outgoing call connected packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: outgoing_call_replies
                        
                        	Outgoing call replies
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: outgoing_call_requests
                        
                        	Outgoing call requests
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: service_relay_replies
                        
                        	Service relay reply counts
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: service_relay_requests
                        
                        	Service relay request counts
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: set_link_info_packets
                        
                        	Set link info packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: start_control_connection_notifications
                        
                        	Start control connection notifications
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: start_control_connection_replies
                        
                        	Start control connection replies
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: start_control_connection_requests
                        
                        	Start control connection requests
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: stop_control_connection_notifications
                        
                        	Stop control connection notifications
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unknown_packets
                        
                        	Unknown packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: wan_error_notify_packets
                        
                        	WAN error notify packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: zero_length_body_packets
                        
                        	Zero length body packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'tunnel-l2tun-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(L2Tp.Counters.Control.TunnelXr.Global_.Received, self).__init__()

                            self.yang_name = "received"
                            self.yang_parent_name = "global"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.acknowledgement_packets = YLeaf(YType.uint32, "acknowledgement-packets")

                            self.call_disconnect_notify_packets = YLeaf(YType.uint32, "call-disconnect-notify-packets")

                            self.hello_packets = YLeaf(YType.uint32, "hello-packets")

                            self.incoming_call_connected_packets = YLeaf(YType.uint32, "incoming-call-connected-packets")

                            self.incoming_call_replies = YLeaf(YType.uint32, "incoming-call-replies")

                            self.incoming_call_requests = YLeaf(YType.uint32, "incoming-call-requests")

                            self.outgoing_call_connected_packets = YLeaf(YType.uint32, "outgoing-call-connected-packets")

                            self.outgoing_call_replies = YLeaf(YType.uint32, "outgoing-call-replies")

                            self.outgoing_call_requests = YLeaf(YType.uint32, "outgoing-call-requests")

                            self.service_relay_replies = YLeaf(YType.uint32, "service-relay-replies")

                            self.service_relay_requests = YLeaf(YType.uint32, "service-relay-requests")

                            self.set_link_info_packets = YLeaf(YType.uint32, "set-link-info-packets")

                            self.start_control_connection_notifications = YLeaf(YType.uint32, "start-control-connection-notifications")

                            self.start_control_connection_replies = YLeaf(YType.uint32, "start-control-connection-replies")

                            self.start_control_connection_requests = YLeaf(YType.uint32, "start-control-connection-requests")

                            self.stop_control_connection_notifications = YLeaf(YType.uint32, "stop-control-connection-notifications")

                            self.unknown_packets = YLeaf(YType.uint32, "unknown-packets")

                            self.wan_error_notify_packets = YLeaf(YType.uint32, "wan-error-notify-packets")

                            self.zero_length_body_packets = YLeaf(YType.uint32, "zero-length-body-packets")
                            self._segment_path = lambda: "received"
                            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/counters/control/tunnel-xr/global/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2Tp.Counters.Control.TunnelXr.Global_.Received, ['acknowledgement_packets', 'call_disconnect_notify_packets', 'hello_packets', 'incoming_call_connected_packets', 'incoming_call_replies', 'incoming_call_requests', 'outgoing_call_connected_packets', 'outgoing_call_replies', 'outgoing_call_requests', 'service_relay_replies', 'service_relay_requests', 'set_link_info_packets', 'start_control_connection_notifications', 'start_control_connection_replies', 'start_control_connection_requests', 'stop_control_connection_notifications', 'unknown_packets', 'wan_error_notify_packets', 'zero_length_body_packets'], name, value)


                    class Retransmit(Entity):
                        """
                        Re transmit data
                        
                        .. attribute:: acknowledgement_packets
                        
                        	Packets acknowledgement
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: call_disconnect_notify_packets
                        
                        	Call disconnect notify packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: hello_packets
                        
                        	Keep alive messages
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: incoming_call_connected_packets
                        
                        	Incoming call connected packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: incoming_call_replies
                        
                        	Incoming call replies
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: incoming_call_requests
                        
                        	Incoming call requests
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: outgoing_call_connected_packets
                        
                        	Outgoing call connected packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: outgoing_call_replies
                        
                        	Outgoing call replies
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: outgoing_call_requests
                        
                        	Outgoing call requests
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: service_relay_replies
                        
                        	Service relay reply counts
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: service_relay_requests
                        
                        	Service relay request counts
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: set_link_info_packets
                        
                        	Set link info packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: start_control_connection_notifications
                        
                        	Start control connection notifications
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: start_control_connection_replies
                        
                        	Start control connection replies
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: start_control_connection_requests
                        
                        	Start control connection requests
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: stop_control_connection_notifications
                        
                        	Stop control connection notifications
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unknown_packets
                        
                        	Unknown packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: wan_error_notify_packets
                        
                        	WAN error notify packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: zero_length_body_packets
                        
                        	Zero length body packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'tunnel-l2tun-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(L2Tp.Counters.Control.TunnelXr.Global_.Retransmit, self).__init__()

                            self.yang_name = "retransmit"
                            self.yang_parent_name = "global"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.acknowledgement_packets = YLeaf(YType.uint32, "acknowledgement-packets")

                            self.call_disconnect_notify_packets = YLeaf(YType.uint32, "call-disconnect-notify-packets")

                            self.hello_packets = YLeaf(YType.uint32, "hello-packets")

                            self.incoming_call_connected_packets = YLeaf(YType.uint32, "incoming-call-connected-packets")

                            self.incoming_call_replies = YLeaf(YType.uint32, "incoming-call-replies")

                            self.incoming_call_requests = YLeaf(YType.uint32, "incoming-call-requests")

                            self.outgoing_call_connected_packets = YLeaf(YType.uint32, "outgoing-call-connected-packets")

                            self.outgoing_call_replies = YLeaf(YType.uint32, "outgoing-call-replies")

                            self.outgoing_call_requests = YLeaf(YType.uint32, "outgoing-call-requests")

                            self.service_relay_replies = YLeaf(YType.uint32, "service-relay-replies")

                            self.service_relay_requests = YLeaf(YType.uint32, "service-relay-requests")

                            self.set_link_info_packets = YLeaf(YType.uint32, "set-link-info-packets")

                            self.start_control_connection_notifications = YLeaf(YType.uint32, "start-control-connection-notifications")

                            self.start_control_connection_replies = YLeaf(YType.uint32, "start-control-connection-replies")

                            self.start_control_connection_requests = YLeaf(YType.uint32, "start-control-connection-requests")

                            self.stop_control_connection_notifications = YLeaf(YType.uint32, "stop-control-connection-notifications")

                            self.unknown_packets = YLeaf(YType.uint32, "unknown-packets")

                            self.wan_error_notify_packets = YLeaf(YType.uint32, "wan-error-notify-packets")

                            self.zero_length_body_packets = YLeaf(YType.uint32, "zero-length-body-packets")
                            self._segment_path = lambda: "retransmit"
                            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/counters/control/tunnel-xr/global/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2Tp.Counters.Control.TunnelXr.Global_.Retransmit, ['acknowledgement_packets', 'call_disconnect_notify_packets', 'hello_packets', 'incoming_call_connected_packets', 'incoming_call_replies', 'incoming_call_requests', 'outgoing_call_connected_packets', 'outgoing_call_replies', 'outgoing_call_requests', 'service_relay_replies', 'service_relay_requests', 'set_link_info_packets', 'start_control_connection_notifications', 'start_control_connection_replies', 'start_control_connection_requests', 'stop_control_connection_notifications', 'unknown_packets', 'wan_error_notify_packets', 'zero_length_body_packets'], name, value)


                    class Transmit(Entity):
                        """
                        Transmit data
                        
                        .. attribute:: acknowledgement_packets
                        
                        	Packets acknowledgement
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: call_disconnect_notify_packets
                        
                        	Call disconnect notify packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: hello_packets
                        
                        	Keep alive messages
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: incoming_call_connected_packets
                        
                        	Incoming call connected packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: incoming_call_replies
                        
                        	Incoming call replies
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: incoming_call_requests
                        
                        	Incoming call requests
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: outgoing_call_connected_packets
                        
                        	Outgoing call connected packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: outgoing_call_replies
                        
                        	Outgoing call replies
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: outgoing_call_requests
                        
                        	Outgoing call requests
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: service_relay_replies
                        
                        	Service relay reply counts
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: service_relay_requests
                        
                        	Service relay request counts
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: set_link_info_packets
                        
                        	Set link info packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: start_control_connection_notifications
                        
                        	Start control connection notifications
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: start_control_connection_replies
                        
                        	Start control connection replies
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: start_control_connection_requests
                        
                        	Start control connection requests
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: stop_control_connection_notifications
                        
                        	Stop control connection notifications
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unknown_packets
                        
                        	Unknown packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: wan_error_notify_packets
                        
                        	WAN error notify packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: zero_length_body_packets
                        
                        	Zero length body packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'tunnel-l2tun-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(L2Tp.Counters.Control.TunnelXr.Global_.Transmit, self).__init__()

                            self.yang_name = "transmit"
                            self.yang_parent_name = "global"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.acknowledgement_packets = YLeaf(YType.uint32, "acknowledgement-packets")

                            self.call_disconnect_notify_packets = YLeaf(YType.uint32, "call-disconnect-notify-packets")

                            self.hello_packets = YLeaf(YType.uint32, "hello-packets")

                            self.incoming_call_connected_packets = YLeaf(YType.uint32, "incoming-call-connected-packets")

                            self.incoming_call_replies = YLeaf(YType.uint32, "incoming-call-replies")

                            self.incoming_call_requests = YLeaf(YType.uint32, "incoming-call-requests")

                            self.outgoing_call_connected_packets = YLeaf(YType.uint32, "outgoing-call-connected-packets")

                            self.outgoing_call_replies = YLeaf(YType.uint32, "outgoing-call-replies")

                            self.outgoing_call_requests = YLeaf(YType.uint32, "outgoing-call-requests")

                            self.service_relay_replies = YLeaf(YType.uint32, "service-relay-replies")

                            self.service_relay_requests = YLeaf(YType.uint32, "service-relay-requests")

                            self.set_link_info_packets = YLeaf(YType.uint32, "set-link-info-packets")

                            self.start_control_connection_notifications = YLeaf(YType.uint32, "start-control-connection-notifications")

                            self.start_control_connection_replies = YLeaf(YType.uint32, "start-control-connection-replies")

                            self.start_control_connection_requests = YLeaf(YType.uint32, "start-control-connection-requests")

                            self.stop_control_connection_notifications = YLeaf(YType.uint32, "stop-control-connection-notifications")

                            self.unknown_packets = YLeaf(YType.uint32, "unknown-packets")

                            self.wan_error_notify_packets = YLeaf(YType.uint32, "wan-error-notify-packets")

                            self.zero_length_body_packets = YLeaf(YType.uint32, "zero-length-body-packets")
                            self._segment_path = lambda: "transmit"
                            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/counters/control/tunnel-xr/global/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2Tp.Counters.Control.TunnelXr.Global_.Transmit, ['acknowledgement_packets', 'call_disconnect_notify_packets', 'hello_packets', 'incoming_call_connected_packets', 'incoming_call_replies', 'incoming_call_requests', 'outgoing_call_connected_packets', 'outgoing_call_replies', 'outgoing_call_requests', 'service_relay_replies', 'service_relay_requests', 'set_link_info_packets', 'start_control_connection_notifications', 'start_control_connection_replies', 'start_control_connection_requests', 'stop_control_connection_notifications', 'unknown_packets', 'wan_error_notify_packets', 'zero_length_body_packets'], name, value)


            class Tunnels(Entity):
                """
                Table of tunnel IDs of control message counters
                
                .. attribute:: tunnel
                
                	L2TP tunnel control message counters
                	**type**\: list of    :py:class:`Tunnel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tp.Counters.Control.Tunnels.Tunnel>`
                
                

                """

                _prefix = 'tunnel-l2tun-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(L2Tp.Counters.Control.Tunnels, self).__init__()

                    self.yang_name = "tunnels"
                    self.yang_parent_name = "control"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"tunnel" : ("tunnel", L2Tp.Counters.Control.Tunnels.Tunnel)}

                    self.tunnel = YList(self)
                    self._segment_path = lambda: "tunnels"
                    self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/counters/control/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(L2Tp.Counters.Control.Tunnels, [], name, value)


                class Tunnel(Entity):
                    """
                    L2TP tunnel control message counters
                    
                    .. attribute:: tunnel_id  <key>
                    
                    	L2TP tunnel ID
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: brief
                    
                    	L2TP control message local and remote addresses
                    	**type**\:   :py:class:`Brief <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tp.Counters.Control.Tunnels.Tunnel.Brief>`
                    
                    .. attribute:: global_
                    
                    	Global data
                    	**type**\:   :py:class:`Global_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tp.Counters.Control.Tunnels.Tunnel.Global_>`
                    
                    

                    """

                    _prefix = 'tunnel-l2tun-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(L2Tp.Counters.Control.Tunnels.Tunnel, self).__init__()

                        self.yang_name = "tunnel"
                        self.yang_parent_name = "tunnels"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"brief" : ("brief", L2Tp.Counters.Control.Tunnels.Tunnel.Brief), "global" : ("global_", L2Tp.Counters.Control.Tunnels.Tunnel.Global_)}
                        self._child_list_classes = {}

                        self.tunnel_id = YLeaf(YType.int32, "tunnel-id")

                        self.brief = L2Tp.Counters.Control.Tunnels.Tunnel.Brief()
                        self.brief.parent = self
                        self._children_name_map["brief"] = "brief"
                        self._children_yang_names.add("brief")

                        self.global_ = L2Tp.Counters.Control.Tunnels.Tunnel.Global_()
                        self.global_.parent = self
                        self._children_name_map["global_"] = "global"
                        self._children_yang_names.add("global")
                        self._segment_path = lambda: "tunnel" + "[tunnel-id='" + self.tunnel_id.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/counters/control/tunnels/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2Tp.Counters.Control.Tunnels.Tunnel, ['tunnel_id'], name, value)


                    class Brief(Entity):
                        """
                        L2TP control message local and remote addresses
                        
                        .. attribute:: local_address
                        
                        	Local IP address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: remote_address
                        
                        	Remote IP address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: remote_tunnel_id
                        
                        	Remote tunnel ID
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'tunnel-l2tun-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(L2Tp.Counters.Control.Tunnels.Tunnel.Brief, self).__init__()

                            self.yang_name = "brief"
                            self.yang_parent_name = "tunnel"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.local_address = YLeaf(YType.str, "local-address")

                            self.remote_address = YLeaf(YType.str, "remote-address")

                            self.remote_tunnel_id = YLeaf(YType.uint32, "remote-tunnel-id")
                            self._segment_path = lambda: "brief"

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2Tp.Counters.Control.Tunnels.Tunnel.Brief, ['local_address', 'remote_address', 'remote_tunnel_id'], name, value)


                    class Global_(Entity):
                        """
                        Global data
                        
                        .. attribute:: drop
                        
                        	Drop data
                        	**type**\:   :py:class:`Drop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tp.Counters.Control.Tunnels.Tunnel.Global_.Drop>`
                        
                        .. attribute:: received
                        
                        	Received data
                        	**type**\:   :py:class:`Received <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tp.Counters.Control.Tunnels.Tunnel.Global_.Received>`
                        
                        .. attribute:: retransmit
                        
                        	Re transmit data
                        	**type**\:   :py:class:`Retransmit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tp.Counters.Control.Tunnels.Tunnel.Global_.Retransmit>`
                        
                        .. attribute:: total_drop
                        
                        	Total drop
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: total_received
                        
                        	Total received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: total_retransmit
                        
                        	Total retransmit
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: total_transmit
                        
                        	Total transmit
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: transmit
                        
                        	Transmit data
                        	**type**\:   :py:class:`Transmit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tp.Counters.Control.Tunnels.Tunnel.Global_.Transmit>`
                        
                        

                        """

                        _prefix = 'tunnel-l2tun-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(L2Tp.Counters.Control.Tunnels.Tunnel.Global_, self).__init__()

                            self.yang_name = "global"
                            self.yang_parent_name = "tunnel"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"drop" : ("drop", L2Tp.Counters.Control.Tunnels.Tunnel.Global_.Drop), "received" : ("received", L2Tp.Counters.Control.Tunnels.Tunnel.Global_.Received), "retransmit" : ("retransmit", L2Tp.Counters.Control.Tunnels.Tunnel.Global_.Retransmit), "transmit" : ("transmit", L2Tp.Counters.Control.Tunnels.Tunnel.Global_.Transmit)}
                            self._child_list_classes = {}

                            self.total_drop = YLeaf(YType.uint32, "total-drop")

                            self.total_received = YLeaf(YType.uint32, "total-received")

                            self.total_retransmit = YLeaf(YType.uint32, "total-retransmit")

                            self.total_transmit = YLeaf(YType.uint32, "total-transmit")

                            self.drop = L2Tp.Counters.Control.Tunnels.Tunnel.Global_.Drop()
                            self.drop.parent = self
                            self._children_name_map["drop"] = "drop"
                            self._children_yang_names.add("drop")

                            self.received = L2Tp.Counters.Control.Tunnels.Tunnel.Global_.Received()
                            self.received.parent = self
                            self._children_name_map["received"] = "received"
                            self._children_yang_names.add("received")

                            self.retransmit = L2Tp.Counters.Control.Tunnels.Tunnel.Global_.Retransmit()
                            self.retransmit.parent = self
                            self._children_name_map["retransmit"] = "retransmit"
                            self._children_yang_names.add("retransmit")

                            self.transmit = L2Tp.Counters.Control.Tunnels.Tunnel.Global_.Transmit()
                            self.transmit.parent = self
                            self._children_name_map["transmit"] = "transmit"
                            self._children_yang_names.add("transmit")
                            self._segment_path = lambda: "global"

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2Tp.Counters.Control.Tunnels.Tunnel.Global_, ['total_drop', 'total_received', 'total_retransmit', 'total_transmit'], name, value)


                        class Drop(Entity):
                            """
                            Drop data
                            
                            .. attribute:: acknowledgement_packets
                            
                            	Packets acknowledgement
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: call_disconnect_notify_packets
                            
                            	Call disconnect notify packets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: hello_packets
                            
                            	Keep alive messages
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: incoming_call_connected_packets
                            
                            	Incoming call connected packets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: incoming_call_replies
                            
                            	Incoming call replies
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: incoming_call_requests
                            
                            	Incoming call requests
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: outgoing_call_connected_packets
                            
                            	Outgoing call connected packets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: outgoing_call_replies
                            
                            	Outgoing call replies
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: outgoing_call_requests
                            
                            	Outgoing call requests
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: service_relay_replies
                            
                            	Service relay reply counts
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: service_relay_requests
                            
                            	Service relay request counts
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: set_link_info_packets
                            
                            	Set link info packets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: start_control_connection_notifications
                            
                            	Start control connection notifications
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: start_control_connection_replies
                            
                            	Start control connection replies
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: start_control_connection_requests
                            
                            	Start control connection requests
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: stop_control_connection_notifications
                            
                            	Stop control connection notifications
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: unknown_packets
                            
                            	Unknown packets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: wan_error_notify_packets
                            
                            	WAN error notify packets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: zero_length_body_packets
                            
                            	Zero length body packets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'tunnel-l2tun-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(L2Tp.Counters.Control.Tunnels.Tunnel.Global_.Drop, self).__init__()

                                self.yang_name = "drop"
                                self.yang_parent_name = "global"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.acknowledgement_packets = YLeaf(YType.uint32, "acknowledgement-packets")

                                self.call_disconnect_notify_packets = YLeaf(YType.uint32, "call-disconnect-notify-packets")

                                self.hello_packets = YLeaf(YType.uint32, "hello-packets")

                                self.incoming_call_connected_packets = YLeaf(YType.uint32, "incoming-call-connected-packets")

                                self.incoming_call_replies = YLeaf(YType.uint32, "incoming-call-replies")

                                self.incoming_call_requests = YLeaf(YType.uint32, "incoming-call-requests")

                                self.outgoing_call_connected_packets = YLeaf(YType.uint32, "outgoing-call-connected-packets")

                                self.outgoing_call_replies = YLeaf(YType.uint32, "outgoing-call-replies")

                                self.outgoing_call_requests = YLeaf(YType.uint32, "outgoing-call-requests")

                                self.service_relay_replies = YLeaf(YType.uint32, "service-relay-replies")

                                self.service_relay_requests = YLeaf(YType.uint32, "service-relay-requests")

                                self.set_link_info_packets = YLeaf(YType.uint32, "set-link-info-packets")

                                self.start_control_connection_notifications = YLeaf(YType.uint32, "start-control-connection-notifications")

                                self.start_control_connection_replies = YLeaf(YType.uint32, "start-control-connection-replies")

                                self.start_control_connection_requests = YLeaf(YType.uint32, "start-control-connection-requests")

                                self.stop_control_connection_notifications = YLeaf(YType.uint32, "stop-control-connection-notifications")

                                self.unknown_packets = YLeaf(YType.uint32, "unknown-packets")

                                self.wan_error_notify_packets = YLeaf(YType.uint32, "wan-error-notify-packets")

                                self.zero_length_body_packets = YLeaf(YType.uint32, "zero-length-body-packets")
                                self._segment_path = lambda: "drop"

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2Tp.Counters.Control.Tunnels.Tunnel.Global_.Drop, ['acknowledgement_packets', 'call_disconnect_notify_packets', 'hello_packets', 'incoming_call_connected_packets', 'incoming_call_replies', 'incoming_call_requests', 'outgoing_call_connected_packets', 'outgoing_call_replies', 'outgoing_call_requests', 'service_relay_replies', 'service_relay_requests', 'set_link_info_packets', 'start_control_connection_notifications', 'start_control_connection_replies', 'start_control_connection_requests', 'stop_control_connection_notifications', 'unknown_packets', 'wan_error_notify_packets', 'zero_length_body_packets'], name, value)


                        class Received(Entity):
                            """
                            Received data
                            
                            .. attribute:: acknowledgement_packets
                            
                            	Packets acknowledgement
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: call_disconnect_notify_packets
                            
                            	Call disconnect notify packets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: hello_packets
                            
                            	Keep alive messages
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: incoming_call_connected_packets
                            
                            	Incoming call connected packets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: incoming_call_replies
                            
                            	Incoming call replies
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: incoming_call_requests
                            
                            	Incoming call requests
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: outgoing_call_connected_packets
                            
                            	Outgoing call connected packets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: outgoing_call_replies
                            
                            	Outgoing call replies
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: outgoing_call_requests
                            
                            	Outgoing call requests
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: service_relay_replies
                            
                            	Service relay reply counts
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: service_relay_requests
                            
                            	Service relay request counts
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: set_link_info_packets
                            
                            	Set link info packets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: start_control_connection_notifications
                            
                            	Start control connection notifications
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: start_control_connection_replies
                            
                            	Start control connection replies
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: start_control_connection_requests
                            
                            	Start control connection requests
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: stop_control_connection_notifications
                            
                            	Stop control connection notifications
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: unknown_packets
                            
                            	Unknown packets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: wan_error_notify_packets
                            
                            	WAN error notify packets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: zero_length_body_packets
                            
                            	Zero length body packets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'tunnel-l2tun-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(L2Tp.Counters.Control.Tunnels.Tunnel.Global_.Received, self).__init__()

                                self.yang_name = "received"
                                self.yang_parent_name = "global"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.acknowledgement_packets = YLeaf(YType.uint32, "acknowledgement-packets")

                                self.call_disconnect_notify_packets = YLeaf(YType.uint32, "call-disconnect-notify-packets")

                                self.hello_packets = YLeaf(YType.uint32, "hello-packets")

                                self.incoming_call_connected_packets = YLeaf(YType.uint32, "incoming-call-connected-packets")

                                self.incoming_call_replies = YLeaf(YType.uint32, "incoming-call-replies")

                                self.incoming_call_requests = YLeaf(YType.uint32, "incoming-call-requests")

                                self.outgoing_call_connected_packets = YLeaf(YType.uint32, "outgoing-call-connected-packets")

                                self.outgoing_call_replies = YLeaf(YType.uint32, "outgoing-call-replies")

                                self.outgoing_call_requests = YLeaf(YType.uint32, "outgoing-call-requests")

                                self.service_relay_replies = YLeaf(YType.uint32, "service-relay-replies")

                                self.service_relay_requests = YLeaf(YType.uint32, "service-relay-requests")

                                self.set_link_info_packets = YLeaf(YType.uint32, "set-link-info-packets")

                                self.start_control_connection_notifications = YLeaf(YType.uint32, "start-control-connection-notifications")

                                self.start_control_connection_replies = YLeaf(YType.uint32, "start-control-connection-replies")

                                self.start_control_connection_requests = YLeaf(YType.uint32, "start-control-connection-requests")

                                self.stop_control_connection_notifications = YLeaf(YType.uint32, "stop-control-connection-notifications")

                                self.unknown_packets = YLeaf(YType.uint32, "unknown-packets")

                                self.wan_error_notify_packets = YLeaf(YType.uint32, "wan-error-notify-packets")

                                self.zero_length_body_packets = YLeaf(YType.uint32, "zero-length-body-packets")
                                self._segment_path = lambda: "received"

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2Tp.Counters.Control.Tunnels.Tunnel.Global_.Received, ['acknowledgement_packets', 'call_disconnect_notify_packets', 'hello_packets', 'incoming_call_connected_packets', 'incoming_call_replies', 'incoming_call_requests', 'outgoing_call_connected_packets', 'outgoing_call_replies', 'outgoing_call_requests', 'service_relay_replies', 'service_relay_requests', 'set_link_info_packets', 'start_control_connection_notifications', 'start_control_connection_replies', 'start_control_connection_requests', 'stop_control_connection_notifications', 'unknown_packets', 'wan_error_notify_packets', 'zero_length_body_packets'], name, value)


                        class Retransmit(Entity):
                            """
                            Re transmit data
                            
                            .. attribute:: acknowledgement_packets
                            
                            	Packets acknowledgement
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: call_disconnect_notify_packets
                            
                            	Call disconnect notify packets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: hello_packets
                            
                            	Keep alive messages
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: incoming_call_connected_packets
                            
                            	Incoming call connected packets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: incoming_call_replies
                            
                            	Incoming call replies
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: incoming_call_requests
                            
                            	Incoming call requests
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: outgoing_call_connected_packets
                            
                            	Outgoing call connected packets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: outgoing_call_replies
                            
                            	Outgoing call replies
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: outgoing_call_requests
                            
                            	Outgoing call requests
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: service_relay_replies
                            
                            	Service relay reply counts
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: service_relay_requests
                            
                            	Service relay request counts
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: set_link_info_packets
                            
                            	Set link info packets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: start_control_connection_notifications
                            
                            	Start control connection notifications
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: start_control_connection_replies
                            
                            	Start control connection replies
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: start_control_connection_requests
                            
                            	Start control connection requests
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: stop_control_connection_notifications
                            
                            	Stop control connection notifications
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: unknown_packets
                            
                            	Unknown packets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: wan_error_notify_packets
                            
                            	WAN error notify packets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: zero_length_body_packets
                            
                            	Zero length body packets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'tunnel-l2tun-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(L2Tp.Counters.Control.Tunnels.Tunnel.Global_.Retransmit, self).__init__()

                                self.yang_name = "retransmit"
                                self.yang_parent_name = "global"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.acknowledgement_packets = YLeaf(YType.uint32, "acknowledgement-packets")

                                self.call_disconnect_notify_packets = YLeaf(YType.uint32, "call-disconnect-notify-packets")

                                self.hello_packets = YLeaf(YType.uint32, "hello-packets")

                                self.incoming_call_connected_packets = YLeaf(YType.uint32, "incoming-call-connected-packets")

                                self.incoming_call_replies = YLeaf(YType.uint32, "incoming-call-replies")

                                self.incoming_call_requests = YLeaf(YType.uint32, "incoming-call-requests")

                                self.outgoing_call_connected_packets = YLeaf(YType.uint32, "outgoing-call-connected-packets")

                                self.outgoing_call_replies = YLeaf(YType.uint32, "outgoing-call-replies")

                                self.outgoing_call_requests = YLeaf(YType.uint32, "outgoing-call-requests")

                                self.service_relay_replies = YLeaf(YType.uint32, "service-relay-replies")

                                self.service_relay_requests = YLeaf(YType.uint32, "service-relay-requests")

                                self.set_link_info_packets = YLeaf(YType.uint32, "set-link-info-packets")

                                self.start_control_connection_notifications = YLeaf(YType.uint32, "start-control-connection-notifications")

                                self.start_control_connection_replies = YLeaf(YType.uint32, "start-control-connection-replies")

                                self.start_control_connection_requests = YLeaf(YType.uint32, "start-control-connection-requests")

                                self.stop_control_connection_notifications = YLeaf(YType.uint32, "stop-control-connection-notifications")

                                self.unknown_packets = YLeaf(YType.uint32, "unknown-packets")

                                self.wan_error_notify_packets = YLeaf(YType.uint32, "wan-error-notify-packets")

                                self.zero_length_body_packets = YLeaf(YType.uint32, "zero-length-body-packets")
                                self._segment_path = lambda: "retransmit"

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2Tp.Counters.Control.Tunnels.Tunnel.Global_.Retransmit, ['acknowledgement_packets', 'call_disconnect_notify_packets', 'hello_packets', 'incoming_call_connected_packets', 'incoming_call_replies', 'incoming_call_requests', 'outgoing_call_connected_packets', 'outgoing_call_replies', 'outgoing_call_requests', 'service_relay_replies', 'service_relay_requests', 'set_link_info_packets', 'start_control_connection_notifications', 'start_control_connection_replies', 'start_control_connection_requests', 'stop_control_connection_notifications', 'unknown_packets', 'wan_error_notify_packets', 'zero_length_body_packets'], name, value)


                        class Transmit(Entity):
                            """
                            Transmit data
                            
                            .. attribute:: acknowledgement_packets
                            
                            	Packets acknowledgement
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: call_disconnect_notify_packets
                            
                            	Call disconnect notify packets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: hello_packets
                            
                            	Keep alive messages
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: incoming_call_connected_packets
                            
                            	Incoming call connected packets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: incoming_call_replies
                            
                            	Incoming call replies
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: incoming_call_requests
                            
                            	Incoming call requests
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: outgoing_call_connected_packets
                            
                            	Outgoing call connected packets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: outgoing_call_replies
                            
                            	Outgoing call replies
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: outgoing_call_requests
                            
                            	Outgoing call requests
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: service_relay_replies
                            
                            	Service relay reply counts
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: service_relay_requests
                            
                            	Service relay request counts
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: set_link_info_packets
                            
                            	Set link info packets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: start_control_connection_notifications
                            
                            	Start control connection notifications
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: start_control_connection_replies
                            
                            	Start control connection replies
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: start_control_connection_requests
                            
                            	Start control connection requests
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: stop_control_connection_notifications
                            
                            	Stop control connection notifications
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: unknown_packets
                            
                            	Unknown packets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: wan_error_notify_packets
                            
                            	WAN error notify packets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: zero_length_body_packets
                            
                            	Zero length body packets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'tunnel-l2tun-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(L2Tp.Counters.Control.Tunnels.Tunnel.Global_.Transmit, self).__init__()

                                self.yang_name = "transmit"
                                self.yang_parent_name = "global"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.acknowledgement_packets = YLeaf(YType.uint32, "acknowledgement-packets")

                                self.call_disconnect_notify_packets = YLeaf(YType.uint32, "call-disconnect-notify-packets")

                                self.hello_packets = YLeaf(YType.uint32, "hello-packets")

                                self.incoming_call_connected_packets = YLeaf(YType.uint32, "incoming-call-connected-packets")

                                self.incoming_call_replies = YLeaf(YType.uint32, "incoming-call-replies")

                                self.incoming_call_requests = YLeaf(YType.uint32, "incoming-call-requests")

                                self.outgoing_call_connected_packets = YLeaf(YType.uint32, "outgoing-call-connected-packets")

                                self.outgoing_call_replies = YLeaf(YType.uint32, "outgoing-call-replies")

                                self.outgoing_call_requests = YLeaf(YType.uint32, "outgoing-call-requests")

                                self.service_relay_replies = YLeaf(YType.uint32, "service-relay-replies")

                                self.service_relay_requests = YLeaf(YType.uint32, "service-relay-requests")

                                self.set_link_info_packets = YLeaf(YType.uint32, "set-link-info-packets")

                                self.start_control_connection_notifications = YLeaf(YType.uint32, "start-control-connection-notifications")

                                self.start_control_connection_replies = YLeaf(YType.uint32, "start-control-connection-replies")

                                self.start_control_connection_requests = YLeaf(YType.uint32, "start-control-connection-requests")

                                self.stop_control_connection_notifications = YLeaf(YType.uint32, "stop-control-connection-notifications")

                                self.unknown_packets = YLeaf(YType.uint32, "unknown-packets")

                                self.wan_error_notify_packets = YLeaf(YType.uint32, "wan-error-notify-packets")

                                self.zero_length_body_packets = YLeaf(YType.uint32, "zero-length-body-packets")
                                self._segment_path = lambda: "transmit"

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2Tp.Counters.Control.Tunnels.Tunnel.Global_.Transmit, ['acknowledgement_packets', 'call_disconnect_notify_packets', 'hello_packets', 'incoming_call_connected_packets', 'incoming_call_replies', 'incoming_call_requests', 'outgoing_call_connected_packets', 'outgoing_call_replies', 'outgoing_call_requests', 'service_relay_replies', 'service_relay_requests', 'set_link_info_packets', 'start_control_connection_notifications', 'start_control_connection_replies', 'start_control_connection_requests', 'stop_control_connection_notifications', 'unknown_packets', 'wan_error_notify_packets', 'zero_length_body_packets'], name, value)


    class Session(Entity):
        """
        L2TP control messages counters
        
        .. attribute:: unavailable
        
        	L2TP session unavailable  information
        	**type**\:   :py:class:`Unavailable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tp.Session.Unavailable>`
        
        

        """

        _prefix = 'tunnel-l2tun-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(L2Tp.Session, self).__init__()

            self.yang_name = "session"
            self.yang_parent_name = "l2tp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"unavailable" : ("unavailable", L2Tp.Session.Unavailable)}
            self._child_list_classes = {}

            self.unavailable = L2Tp.Session.Unavailable()
            self.unavailable.parent = self
            self._children_name_map["unavailable"] = "unavailable"
            self._children_yang_names.add("unavailable")
            self._segment_path = lambda: "session"
            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/%s" % self._segment_path()


        class Unavailable(Entity):
            """
            L2TP session unavailable  information
            
            .. attribute:: sessions_on_hold
            
            	Number of session ID in hold database
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'tunnel-l2tun-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(L2Tp.Session.Unavailable, self).__init__()

                self.yang_name = "unavailable"
                self.yang_parent_name = "session"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.sessions_on_hold = YLeaf(YType.uint32, "sessions-on-hold")
                self._segment_path = lambda: "unavailable"
                self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/session/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(L2Tp.Session.Unavailable, ['sessions_on_hold'], name, value)


    class Sessions(Entity):
        """
        List of session IDs
        
        .. attribute:: session
        
        	L2TP information for a particular session
        	**type**\: list of    :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tp.Sessions.Session>`
        
        

        """

        _prefix = 'tunnel-l2tun-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(L2Tp.Sessions, self).__init__()

            self.yang_name = "sessions"
            self.yang_parent_name = "l2tp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"session" : ("session", L2Tp.Sessions.Session)}

            self.session = YList(self)
            self._segment_path = lambda: "sessions"
            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(L2Tp.Sessions, [], name, value)


        class Session(Entity):
            """
            L2TP information for a particular session
            
            .. attribute:: local_tunnel_id  <key>
            
            	Local tunnel ID
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: local_session_id  <key>
            
            	Local session ID
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: call_serial_number
            
            	Call serial number
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: interface_name
            
            	Interface name
            	**type**\:  str
            
            	**length:** 0..256
            
            .. attribute:: is_conditional_debug_enabled
            
            	True if conditional debugging is enabled
            	**type**\:  bool
            
            .. attribute:: is_sequencing_on
            
            	True if session sequence is on
            	**type**\:  bool
            
            .. attribute:: is_session_locally_initiated
            
            	True if session initiated locally
            	**type**\:  bool
            
            .. attribute:: is_session_manual
            
            	True if session is manual
            	**type**\:  bool
            
            .. attribute:: is_session_state_established
            
            	True if session state is established
            	**type**\:  bool
            
            .. attribute:: is_session_up
            
            	True if session is up
            	**type**\:  bool
            
            .. attribute:: is_udp_checksum_enabled
            
            	True if UDP checksum enabled
            	**type**\:  bool
            
            .. attribute:: l2tp_sh_sess_tie_breaker
            
            	l2tp sh sess tie breaker
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: l2tp_sh_sess_tie_breaker_enabled
            
            	l2tp sh sess tie breaker enabled
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: l2tp_sh_sess_udp_lport
            
            	l2tp sh sess udp lport
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: l2tp_sh_sess_udp_rport
            
            	l2tp sh sess udp rport
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: local_ip_address
            
            	Local session IP address
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: local_tunnel_name
            
            	Local tunnel name
            	**type**\:  str
            
            	**length:** 0..256
            
            .. attribute:: protocol
            
            	Protocol
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: remote_ip_address
            
            	Remote session IP address
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: remote_session_id
            
            	Remote session ID
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: remote_tunnel_id
            
            	Remote tunnel ID
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: remote_tunnel_name
            
            	Remote tunnel name
            	**type**\:  str
            
            	**length:** 0..256
            
            .. attribute:: session_application_data
            
            	Session application data
            	**type**\:   :py:class:`SessionApplicationData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tp.Sessions.Session.SessionApplicationData>`
            
            .. attribute:: unique_id
            
            	Unique ID
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'tunnel-l2tun-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(L2Tp.Sessions.Session, self).__init__()

                self.yang_name = "session"
                self.yang_parent_name = "sessions"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"session-application-data" : ("session_application_data", L2Tp.Sessions.Session.SessionApplicationData)}
                self._child_list_classes = {}

                self.local_tunnel_id = YLeaf(YType.int32, "local-tunnel-id")

                self.local_session_id = YLeaf(YType.int32, "local-session-id")

                self.call_serial_number = YLeaf(YType.uint32, "call-serial-number")

                self.interface_name = YLeaf(YType.str, "interface-name")

                self.is_conditional_debug_enabled = YLeaf(YType.boolean, "is-conditional-debug-enabled")

                self.is_sequencing_on = YLeaf(YType.boolean, "is-sequencing-on")

                self.is_session_locally_initiated = YLeaf(YType.boolean, "is-session-locally-initiated")

                self.is_session_manual = YLeaf(YType.boolean, "is-session-manual")

                self.is_session_state_established = YLeaf(YType.boolean, "is-session-state-established")

                self.is_session_up = YLeaf(YType.boolean, "is-session-up")

                self.is_udp_checksum_enabled = YLeaf(YType.boolean, "is-udp-checksum-enabled")

                self.l2tp_sh_sess_tie_breaker = YLeaf(YType.uint64, "l2tp-sh-sess-tie-breaker")

                self.l2tp_sh_sess_tie_breaker_enabled = YLeaf(YType.uint8, "l2tp-sh-sess-tie-breaker-enabled")

                self.l2tp_sh_sess_udp_lport = YLeaf(YType.uint16, "l2tp-sh-sess-udp-lport")

                self.l2tp_sh_sess_udp_rport = YLeaf(YType.uint16, "l2tp-sh-sess-udp-rport")

                self.local_ip_address = YLeaf(YType.str, "local-ip-address")

                self.local_tunnel_name = YLeaf(YType.str, "local-tunnel-name")

                self.protocol = YLeaf(YType.uint8, "protocol")

                self.remote_ip_address = YLeaf(YType.str, "remote-ip-address")

                self.remote_session_id = YLeaf(YType.uint32, "remote-session-id")

                self.remote_tunnel_id = YLeaf(YType.uint32, "remote-tunnel-id")

                self.remote_tunnel_name = YLeaf(YType.str, "remote-tunnel-name")

                self.unique_id = YLeaf(YType.uint32, "unique-id")

                self.session_application_data = L2Tp.Sessions.Session.SessionApplicationData()
                self.session_application_data.parent = self
                self._children_name_map["session_application_data"] = "session-application-data"
                self._children_yang_names.add("session-application-data")
                self._segment_path = lambda: "session" + "[local-tunnel-id='" + self.local_tunnel_id.get() + "']" + "[local-session-id='" + self.local_session_id.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/sessions/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(L2Tp.Sessions.Session, ['local_tunnel_id', 'local_session_id', 'call_serial_number', 'interface_name', 'is_conditional_debug_enabled', 'is_sequencing_on', 'is_session_locally_initiated', 'is_session_manual', 'is_session_state_established', 'is_session_up', 'is_udp_checksum_enabled', 'l2tp_sh_sess_tie_breaker', 'l2tp_sh_sess_tie_breaker_enabled', 'l2tp_sh_sess_udp_lport', 'l2tp_sh_sess_udp_rport', 'local_ip_address', 'local_tunnel_name', 'protocol', 'remote_ip_address', 'remote_session_id', 'remote_tunnel_id', 'remote_tunnel_name', 'unique_id'], name, value)


            class SessionApplicationData(Entity):
                """
                Session application data
                
                .. attribute:: l2tp_sh_sess_app_type
                
                	l2tp sh sess app type
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: vpdn
                
                	VPDN data
                	**type**\:   :py:class:`Vpdn <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tp.Sessions.Session.SessionApplicationData.Vpdn>`
                
                .. attribute:: xconnect
                
                	Xconnect data
                	**type**\:   :py:class:`Xconnect <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tp.Sessions.Session.SessionApplicationData.Xconnect>`
                
                

                """

                _prefix = 'tunnel-l2tun-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(L2Tp.Sessions.Session.SessionApplicationData, self).__init__()

                    self.yang_name = "session-application-data"
                    self.yang_parent_name = "session"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"vpdn" : ("vpdn", L2Tp.Sessions.Session.SessionApplicationData.Vpdn), "xconnect" : ("xconnect", L2Tp.Sessions.Session.SessionApplicationData.Xconnect)}
                    self._child_list_classes = {}

                    self.l2tp_sh_sess_app_type = YLeaf(YType.uint32, "l2tp-sh-sess-app-type")

                    self.vpdn = L2Tp.Sessions.Session.SessionApplicationData.Vpdn()
                    self.vpdn.parent = self
                    self._children_name_map["vpdn"] = "vpdn"
                    self._children_yang_names.add("vpdn")

                    self.xconnect = L2Tp.Sessions.Session.SessionApplicationData.Xconnect()
                    self.xconnect.parent = self
                    self._children_name_map["xconnect"] = "xconnect"
                    self._children_yang_names.add("xconnect")
                    self._segment_path = lambda: "session-application-data"

                def __setattr__(self, name, value):
                    self._perform_setattr(L2Tp.Sessions.Session.SessionApplicationData, ['l2tp_sh_sess_app_type'], name, value)


                class Vpdn(Entity):
                    """
                    VPDN data
                    
                    .. attribute:: interface_name
                    
                    	Interface name
                    	**type**\:  str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
                    .. attribute:: username
                    
                    	Session username
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'tunnel-l2tun-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(L2Tp.Sessions.Session.SessionApplicationData.Vpdn, self).__init__()

                        self.yang_name = "vpdn"
                        self.yang_parent_name = "session-application-data"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.username = YLeaf(YType.str, "username")
                        self._segment_path = lambda: "vpdn"

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2Tp.Sessions.Session.SessionApplicationData.Vpdn, ['interface_name', 'username'], name, value)


                class Xconnect(Entity):
                    """
                    Xconnect data
                    
                    .. attribute:: circuit_name
                    
                    	Circuit name
                    	**type**\:  str
                    
                    .. attribute:: ipv6_protocol_tunneling
                    
                    	IPv6ProtocolTunneling
                    	**type**\:  bool
                    
                    .. attribute:: is_circuit_state_up
                    
                    	True if circuit state is up
                    	**type**\:  bool
                    
                    .. attribute:: is_local_circuit_state_up
                    
                    	True if local circuit state is up
                    	**type**\:  bool
                    
                    .. attribute:: is_remote_circuit_state_up
                    
                    	True if remote circuit state is up
                    	**type**\:  bool
                    
                    .. attribute:: sessionvc_id
                    
                    	Session VC ID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'tunnel-l2tun-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(L2Tp.Sessions.Session.SessionApplicationData.Xconnect, self).__init__()

                        self.yang_name = "xconnect"
                        self.yang_parent_name = "session-application-data"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.circuit_name = YLeaf(YType.str, "circuit-name")

                        self.ipv6_protocol_tunneling = YLeaf(YType.boolean, "ipv6-protocol-tunneling")

                        self.is_circuit_state_up = YLeaf(YType.boolean, "is-circuit-state-up")

                        self.is_local_circuit_state_up = YLeaf(YType.boolean, "is-local-circuit-state-up")

                        self.is_remote_circuit_state_up = YLeaf(YType.boolean, "is-remote-circuit-state-up")

                        self.sessionvc_id = YLeaf(YType.uint32, "sessionvc-id")
                        self._segment_path = lambda: "xconnect"

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2Tp.Sessions.Session.SessionApplicationData.Xconnect, ['circuit_name', 'ipv6_protocol_tunneling', 'is_circuit_state_up', 'is_local_circuit_state_up', 'is_remote_circuit_state_up', 'sessionvc_id'], name, value)


    class TunnelConfigurations(Entity):
        """
        List of tunnel IDs
        
        .. attribute:: tunnel_configuration
        
        	L2TP tunnel information
        	**type**\: list of    :py:class:`TunnelConfiguration <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tp.TunnelConfigurations.TunnelConfiguration>`
        
        

        """

        _prefix = 'tunnel-l2tun-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(L2Tp.TunnelConfigurations, self).__init__()

            self.yang_name = "tunnel-configurations"
            self.yang_parent_name = "l2tp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"tunnel-configuration" : ("tunnel_configuration", L2Tp.TunnelConfigurations.TunnelConfiguration)}

            self.tunnel_configuration = YList(self)
            self._segment_path = lambda: "tunnel-configurations"
            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(L2Tp.TunnelConfigurations, [], name, value)


        class TunnelConfiguration(Entity):
            """
            L2TP tunnel information
            
            .. attribute:: local_tunnel_id  <key>
            
            	Local tunnel ID
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: l2tp_class
            
            	L2Tp class data
            	**type**\:   :py:class:`L2TpClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tp.TunnelConfigurations.TunnelConfiguration.L2TpClass>`
            
            .. attribute:: remote_tunnel_id
            
            	Remote tunnel ID
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'tunnel-l2tun-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(L2Tp.TunnelConfigurations.TunnelConfiguration, self).__init__()

                self.yang_name = "tunnel-configuration"
                self.yang_parent_name = "tunnel-configurations"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"l2tp-class" : ("l2tp_class", L2Tp.TunnelConfigurations.TunnelConfiguration.L2TpClass)}
                self._child_list_classes = {}

                self.local_tunnel_id = YLeaf(YType.int32, "local-tunnel-id")

                self.remote_tunnel_id = YLeaf(YType.uint32, "remote-tunnel-id")

                self.l2tp_class = L2Tp.TunnelConfigurations.TunnelConfiguration.L2TpClass()
                self.l2tp_class.parent = self
                self._children_name_map["l2tp_class"] = "l2tp-class"
                self._children_yang_names.add("l2tp-class")
                self._segment_path = lambda: "tunnel-configuration" + "[local-tunnel-id='" + self.local_tunnel_id.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/tunnel-configurations/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(L2Tp.TunnelConfigurations.TunnelConfiguration, ['local_tunnel_id', 'remote_tunnel_id'], name, value)


            class L2TpClass(Entity):
                """
                L2Tp class data
                
                .. attribute:: accounting_method_list
                
                	Accounting List
                	**type**\:  str
                
                	**length:** 0..256
                
                .. attribute:: class_name_xr
                
                	Class name
                	**type**\:  str
                
                	**length:** 0..256
                
                .. attribute:: digest_hash
                
                	Hash configured as MD5 or SHA1
                	**type**\:   :py:class:`DigestHash <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.DigestHash>`
                
                .. attribute:: encoded_password
                
                	Encoded password
                	**type**\:  str
                
                	**length:** 0..256
                
                .. attribute:: hello_timeout
                
                	Hello timeout value in seconds
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: host_name
                
                	Host name
                	**type**\:  str
                
                	**length:** 0..256
                
                .. attribute:: initial_retransmit_maximum_timeout
                
                	Initial timeout maximum in seconds
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: initial_retransmit_minimum_timeout
                
                	Initial timeout minimum in seconds
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: initial_retransmit_retries
                
                	Initial retransmit retries
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: ip_tos
                
                	IP TOS
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: is_authentication_enabled
                
                	True if authentication is enabled
                	**type**\:  bool
                
                .. attribute:: is_congestion_control_enabled
                
                	True if congestion control is enabled
                	**type**\:  bool
                
                .. attribute:: is_digest_check_enabled
                
                	True if digest check is enabled
                	**type**\:  bool
                
                .. attribute:: is_digest_enabled
                
                	True if digest authentication is enabled
                	**type**\:  bool
                
                .. attribute:: is_hidden
                
                	True if class is hidden
                	**type**\:  bool
                
                .. attribute:: is_peer_address_checked
                
                	True if peer address is checked
                	**type**\:  bool
                
                .. attribute:: password
                
                	Password
                	**type**\:  str
                
                	**length:** 0..25
                
                .. attribute:: receive_window_size
                
                	Receive window size
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: retransmit_maximum_timeout
                
                	Retransmit maximum timeout in seconds
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: retransmit_minimum_timeout
                
                	Retransmit minimum timeout in seconds
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: retransmit_retries
                
                	Retransmit retries
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: setup_timeout
                
                	Timeout setup value in seconds
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: timeout_no_user
                
                	Timeout no user
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: vrf_name
                
                	VRF name
                	**type**\:  str
                
                	**length:** 0..256
                
                

                """

                _prefix = 'tunnel-l2tun-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(L2Tp.TunnelConfigurations.TunnelConfiguration.L2TpClass, self).__init__()

                    self.yang_name = "l2tp-class"
                    self.yang_parent_name = "tunnel-configuration"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.accounting_method_list = YLeaf(YType.str, "accounting-method-list")

                    self.class_name_xr = YLeaf(YType.str, "class-name-xr")

                    self.digest_hash = YLeaf(YType.enumeration, "digest-hash")

                    self.encoded_password = YLeaf(YType.str, "encoded-password")

                    self.hello_timeout = YLeaf(YType.uint32, "hello-timeout")

                    self.host_name = YLeaf(YType.str, "host-name")

                    self.initial_retransmit_maximum_timeout = YLeaf(YType.uint32, "initial-retransmit-maximum-timeout")

                    self.initial_retransmit_minimum_timeout = YLeaf(YType.uint32, "initial-retransmit-minimum-timeout")

                    self.initial_retransmit_retries = YLeaf(YType.uint32, "initial-retransmit-retries")

                    self.ip_tos = YLeaf(YType.uint8, "ip-tos")

                    self.is_authentication_enabled = YLeaf(YType.boolean, "is-authentication-enabled")

                    self.is_congestion_control_enabled = YLeaf(YType.boolean, "is-congestion-control-enabled")

                    self.is_digest_check_enabled = YLeaf(YType.boolean, "is-digest-check-enabled")

                    self.is_digest_enabled = YLeaf(YType.boolean, "is-digest-enabled")

                    self.is_hidden = YLeaf(YType.boolean, "is-hidden")

                    self.is_peer_address_checked = YLeaf(YType.boolean, "is-peer-address-checked")

                    self.password = YLeaf(YType.str, "password")

                    self.receive_window_size = YLeaf(YType.uint16, "receive-window-size")

                    self.retransmit_maximum_timeout = YLeaf(YType.uint32, "retransmit-maximum-timeout")

                    self.retransmit_minimum_timeout = YLeaf(YType.uint32, "retransmit-minimum-timeout")

                    self.retransmit_retries = YLeaf(YType.uint32, "retransmit-retries")

                    self.setup_timeout = YLeaf(YType.uint32, "setup-timeout")

                    self.timeout_no_user = YLeaf(YType.uint32, "timeout-no-user")

                    self.vrf_name = YLeaf(YType.str, "vrf-name")
                    self._segment_path = lambda: "l2tp-class"

                def __setattr__(self, name, value):
                    self._perform_setattr(L2Tp.TunnelConfigurations.TunnelConfiguration.L2TpClass, ['accounting_method_list', 'class_name_xr', 'digest_hash', 'encoded_password', 'hello_timeout', 'host_name', 'initial_retransmit_maximum_timeout', 'initial_retransmit_minimum_timeout', 'initial_retransmit_retries', 'ip_tos', 'is_authentication_enabled', 'is_congestion_control_enabled', 'is_digest_check_enabled', 'is_digest_enabled', 'is_hidden', 'is_peer_address_checked', 'password', 'receive_window_size', 'retransmit_maximum_timeout', 'retransmit_minimum_timeout', 'retransmit_retries', 'setup_timeout', 'timeout_no_user', 'vrf_name'], name, value)


    class Tunnels(Entity):
        """
        List of tunnel IDs
        
        .. attribute:: tunnel
        
        	L2TP tunnel  information
        	**type**\: list of    :py:class:`Tunnel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tp.Tunnels.Tunnel>`
        
        

        """

        _prefix = 'tunnel-l2tun-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(L2Tp.Tunnels, self).__init__()

            self.yang_name = "tunnels"
            self.yang_parent_name = "l2tp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"tunnel" : ("tunnel", L2Tp.Tunnels.Tunnel)}

            self.tunnel = YList(self)
            self._segment_path = lambda: "tunnels"
            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(L2Tp.Tunnels, [], name, value)


        class Tunnel(Entity):
            """
            L2TP tunnel  information
            
            .. attribute:: local_tunnel_id  <key>
            
            	Local tunnel ID
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: active_sessions
            
            	Number of active sessions
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: class_name
            
            	L2TP class name
            	**type**\:  str
            
            	**length:** 0..256
            
            .. attribute:: digest_secrets
            
            	Control message authentication with digest secrets
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: is_congestion_control_enabled
            
            	True if congestion control is enabled else false
            	**type**\:  bool
            
            .. attribute:: is_pmtu_enabled
            
            	True if tunnel PMTU checking is enabled
            	**type**\:  bool
            
            .. attribute:: is_tunnel_up
            
            	True if tunnel is up
            	**type**\:  bool
            
            .. attribute:: local_address
            
            	Local tunnel address
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: local_port
            
            	Local port
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: local_tunnel_name
            
            	Local tunnel name
            	**type**\:  str
            
            	**length:** 0..256
            
            .. attribute:: local_window_size
            
            	Local window size
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: maximum_retransmission_time
            
            	Maximum retransmission time in seconds
            	**type**\:  int
            
            	**range:** 0..65535
            
            	**units**\: second
            
            .. attribute:: order_queue_size
            
            	Order queue size
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: packet_queue_check
            
            	Current number session packet queue check
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: protocol
            
            	Protocol
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: remote_address
            
            	Remote tunnel address
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: remote_port
            
            	Remote port
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: remote_tunnel_id
            
            	Remote tunnel ID
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: remote_tunnel_name
            
            	Remote tunnel name
            	**type**\:  str
            
            	**length:** 0..256
            
            .. attribute:: remote_window_size
            
            	Remote window size
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: resend_maximum_queue_size
            
            	Resend maximum queue size
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: resend_queue_size
            
            	Resend queue size
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: resends
            
            	Total resends
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: retransmission_time
            
            	Retransmission time in seconds
            	**type**\:  int
            
            	**range:** 0..65535
            
            	**units**\: second
            
            .. attribute:: retransmit_time
            
            	Retransmit time distribution in seconds
            	**type**\:  list of int
            
            	**range:** 0..65535
            
            	**units**\: second
            
            .. attribute:: sequence_nr
            
            	Sequence NR
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: sequence_ns
            
            	Sequence NS
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: total_out_of_order_drop_packets
            
            	Total out of order dropped packets
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: total_out_of_order_reorder_packets
            
            	Total out of order reorder packets
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: total_peer_authentication_failures
            
            	Number of peer authentication failures
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: unsent_maximum_queue_size
            
            	Unsent maximum queue size
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: unsent_queue_size
            
            	Unsent queue size
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: zero_length_body_acknowledgement_sent
            
            	Total zero length body acknowledgement
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'tunnel-l2tun-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(L2Tp.Tunnels.Tunnel, self).__init__()

                self.yang_name = "tunnel"
                self.yang_parent_name = "tunnels"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.local_tunnel_id = YLeaf(YType.int32, "local-tunnel-id")

                self.active_sessions = YLeaf(YType.uint32, "active-sessions")

                self.class_name = YLeaf(YType.str, "class-name")

                self.digest_secrets = YLeaf(YType.uint16, "digest-secrets")

                self.is_congestion_control_enabled = YLeaf(YType.boolean, "is-congestion-control-enabled")

                self.is_pmtu_enabled = YLeaf(YType.boolean, "is-pmtu-enabled")

                self.is_tunnel_up = YLeaf(YType.boolean, "is-tunnel-up")

                self.local_address = YLeaf(YType.str, "local-address")

                self.local_port = YLeaf(YType.uint16, "local-port")

                self.local_tunnel_name = YLeaf(YType.str, "local-tunnel-name")

                self.local_window_size = YLeaf(YType.uint16, "local-window-size")

                self.maximum_retransmission_time = YLeaf(YType.uint16, "maximum-retransmission-time")

                self.order_queue_size = YLeaf(YType.uint16, "order-queue-size")

                self.packet_queue_check = YLeaf(YType.uint16, "packet-queue-check")

                self.protocol = YLeaf(YType.uint8, "protocol")

                self.remote_address = YLeaf(YType.str, "remote-address")

                self.remote_port = YLeaf(YType.uint16, "remote-port")

                self.remote_tunnel_id = YLeaf(YType.uint32, "remote-tunnel-id")

                self.remote_tunnel_name = YLeaf(YType.str, "remote-tunnel-name")

                self.remote_window_size = YLeaf(YType.uint16, "remote-window-size")

                self.resend_maximum_queue_size = YLeaf(YType.uint16, "resend-maximum-queue-size")

                self.resend_queue_size = YLeaf(YType.uint16, "resend-queue-size")

                self.resends = YLeaf(YType.uint32, "resends")

                self.retransmission_time = YLeaf(YType.uint16, "retransmission-time")

                self.retransmit_time = YLeafList(YType.uint16, "retransmit-time")

                self.sequence_nr = YLeaf(YType.uint16, "sequence-nr")

                self.sequence_ns = YLeaf(YType.uint16, "sequence-ns")

                self.total_out_of_order_drop_packets = YLeaf(YType.uint32, "total-out-of-order-drop-packets")

                self.total_out_of_order_reorder_packets = YLeaf(YType.uint32, "total-out-of-order-reorder-packets")

                self.total_peer_authentication_failures = YLeaf(YType.uint32, "total-peer-authentication-failures")

                self.unsent_maximum_queue_size = YLeaf(YType.uint16, "unsent-maximum-queue-size")

                self.unsent_queue_size = YLeaf(YType.uint16, "unsent-queue-size")

                self.zero_length_body_acknowledgement_sent = YLeaf(YType.uint32, "zero-length-body-acknowledgement-sent")
                self._segment_path = lambda: "tunnel" + "[local-tunnel-id='" + self.local_tunnel_id.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/tunnels/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(L2Tp.Tunnels.Tunnel, ['local_tunnel_id', 'active_sessions', 'class_name', 'digest_secrets', 'is_congestion_control_enabled', 'is_pmtu_enabled', 'is_tunnel_up', 'local_address', 'local_port', 'local_tunnel_name', 'local_window_size', 'maximum_retransmission_time', 'order_queue_size', 'packet_queue_check', 'protocol', 'remote_address', 'remote_port', 'remote_tunnel_id', 'remote_tunnel_name', 'remote_window_size', 'resend_maximum_queue_size', 'resend_queue_size', 'resends', 'retransmission_time', 'retransmit_time', 'sequence_nr', 'sequence_ns', 'total_out_of_order_drop_packets', 'total_out_of_order_reorder_packets', 'total_peer_authentication_failures', 'unsent_maximum_queue_size', 'unsent_queue_size', 'zero_length_body_acknowledgement_sent'], name, value)

    def clone_ptr(self):
        self._top_entity = L2Tp()
        return self._top_entity

class L2Tpv2(Entity):
    """
    l2tpv2
    
    .. attribute:: classes
    
    	List of L2TP class names
    	**type**\:   :py:class:`Classes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tpv2.Classes>`
    
    .. attribute:: counter_hist_fail
    
    	Failure events leading to disconnection
    	**type**\:   :py:class:`CounterHistFail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tpv2.CounterHistFail>`
    
    .. attribute:: counters
    
    	L2TP control messages counters
    	**type**\:   :py:class:`Counters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tpv2.Counters>`
    
    .. attribute:: session
    
    	L2TP control messages counters
    	**type**\:   :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tpv2.Session>`
    
    .. attribute:: sessions
    
    	List of session IDs
    	**type**\:   :py:class:`Sessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tpv2.Sessions>`
    
    .. attribute:: statistics
    
    	L2TP v2 statistics information
    	**type**\:   :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tpv2.Statistics>`
    
    .. attribute:: tunnel
    
    	L2TPv2 tunnel 
    	**type**\:   :py:class:`Tunnel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tpv2.Tunnel>`
    
    .. attribute:: tunnel_configurations
    
    	List of tunnel IDs
    	**type**\:   :py:class:`TunnelConfigurations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tpv2.TunnelConfigurations>`
    
    .. attribute:: tunnels
    
    	List of tunnel IDs
    	**type**\:   :py:class:`Tunnels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tpv2.Tunnels>`
    
    

    """

    _prefix = 'tunnel-l2tun-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(L2Tpv2, self).__init__()
        self._top_entity = None

        self.yang_name = "l2tpv2"
        self.yang_parent_name = "Cisco-IOS-XR-tunnel-l2tun-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"classes" : ("classes", L2Tpv2.Classes), "counter-hist-fail" : ("counter_hist_fail", L2Tpv2.CounterHistFail), "counters" : ("counters", L2Tpv2.Counters), "session" : ("session", L2Tpv2.Session), "sessions" : ("sessions", L2Tpv2.Sessions), "statistics" : ("statistics", L2Tpv2.Statistics), "tunnel" : ("tunnel", L2Tpv2.Tunnel), "tunnel-configurations" : ("tunnel_configurations", L2Tpv2.TunnelConfigurations), "tunnels" : ("tunnels", L2Tpv2.Tunnels)}
        self._child_list_classes = {}

        self.classes = L2Tpv2.Classes()
        self.classes.parent = self
        self._children_name_map["classes"] = "classes"
        self._children_yang_names.add("classes")

        self.counter_hist_fail = L2Tpv2.CounterHistFail()
        self.counter_hist_fail.parent = self
        self._children_name_map["counter_hist_fail"] = "counter-hist-fail"
        self._children_yang_names.add("counter-hist-fail")

        self.counters = L2Tpv2.Counters()
        self.counters.parent = self
        self._children_name_map["counters"] = "counters"
        self._children_yang_names.add("counters")

        self.session = L2Tpv2.Session()
        self.session.parent = self
        self._children_name_map["session"] = "session"
        self._children_yang_names.add("session")

        self.sessions = L2Tpv2.Sessions()
        self.sessions.parent = self
        self._children_name_map["sessions"] = "sessions"
        self._children_yang_names.add("sessions")

        self.statistics = L2Tpv2.Statistics()
        self.statistics.parent = self
        self._children_name_map["statistics"] = "statistics"
        self._children_yang_names.add("statistics")

        self.tunnel = L2Tpv2.Tunnel()
        self.tunnel.parent = self
        self._children_name_map["tunnel"] = "tunnel"
        self._children_yang_names.add("tunnel")

        self.tunnel_configurations = L2Tpv2.TunnelConfigurations()
        self.tunnel_configurations.parent = self
        self._children_name_map["tunnel_configurations"] = "tunnel-configurations"
        self._children_yang_names.add("tunnel-configurations")

        self.tunnels = L2Tpv2.Tunnels()
        self.tunnels.parent = self
        self._children_name_map["tunnels"] = "tunnels"
        self._children_yang_names.add("tunnels")
        self._segment_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2"


    class Classes(Entity):
        """
        List of L2TP class names
        
        .. attribute:: class_
        
        	L2TP class name
        	**type**\: list of    :py:class:`Class_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tpv2.Classes.Class_>`
        
        

        """

        _prefix = 'tunnel-l2tun-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(L2Tpv2.Classes, self).__init__()

            self.yang_name = "classes"
            self.yang_parent_name = "l2tpv2"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"class" : ("class_", L2Tpv2.Classes.Class_)}

            self.class_ = YList(self)
            self._segment_path = lambda: "classes"
            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(L2Tpv2.Classes, [], name, value)


        class Class_(Entity):
            """
            L2TP class name
            
            .. attribute:: class_name  <key>
            
            	L2TP class name
            	**type**\:  str
            
            	**length:** 1..31
            
            .. attribute:: accounting_method_list
            
            	Accounting List
            	**type**\:  str
            
            	**length:** 0..256
            
            .. attribute:: class_name_xr
            
            	Class name
            	**type**\:  str
            
            	**length:** 0..256
            
            .. attribute:: digest_hash
            
            	Hash configured as MD5 or SHA1
            	**type**\:   :py:class:`DigestHash <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.DigestHash>`
            
            .. attribute:: encoded_password
            
            	Encoded password
            	**type**\:  str
            
            	**length:** 0..256
            
            .. attribute:: hello_timeout
            
            	Hello timeout value in seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: second
            
            .. attribute:: host_name
            
            	Host name
            	**type**\:  str
            
            	**length:** 0..256
            
            .. attribute:: initial_retransmit_maximum_timeout
            
            	Initial timeout maximum in seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: second
            
            .. attribute:: initial_retransmit_minimum_timeout
            
            	Initial timeout minimum in seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: second
            
            .. attribute:: initial_retransmit_retries
            
            	Initial retransmit retries
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ip_tos
            
            	IP TOS
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: is_authentication_enabled
            
            	True if authentication is enabled
            	**type**\:  bool
            
            .. attribute:: is_congestion_control_enabled
            
            	True if congestion control is enabled
            	**type**\:  bool
            
            .. attribute:: is_digest_check_enabled
            
            	True if digest check is enabled
            	**type**\:  bool
            
            .. attribute:: is_digest_enabled
            
            	True if digest authentication is enabled
            	**type**\:  bool
            
            .. attribute:: is_hidden
            
            	True if class is hidden
            	**type**\:  bool
            
            .. attribute:: is_peer_address_checked
            
            	True if peer address is checked
            	**type**\:  bool
            
            .. attribute:: password
            
            	Password
            	**type**\:  str
            
            	**length:** 0..25
            
            .. attribute:: receive_window_size
            
            	Receive window size
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: retransmit_maximum_timeout
            
            	Retransmit maximum timeout in seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: second
            
            .. attribute:: retransmit_minimum_timeout
            
            	Retransmit minimum timeout in seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: second
            
            .. attribute:: retransmit_retries
            
            	Retransmit retries
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: setup_timeout
            
            	Timeout setup value in seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: second
            
            .. attribute:: timeout_no_user
            
            	Timeout no user
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: vrf_name
            
            	VRF name
            	**type**\:  str
            
            	**length:** 0..256
            
            

            """

            _prefix = 'tunnel-l2tun-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(L2Tpv2.Classes.Class_, self).__init__()

                self.yang_name = "class"
                self.yang_parent_name = "classes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.class_name = YLeaf(YType.str, "class-name")

                self.accounting_method_list = YLeaf(YType.str, "accounting-method-list")

                self.class_name_xr = YLeaf(YType.str, "class-name-xr")

                self.digest_hash = YLeaf(YType.enumeration, "digest-hash")

                self.encoded_password = YLeaf(YType.str, "encoded-password")

                self.hello_timeout = YLeaf(YType.uint32, "hello-timeout")

                self.host_name = YLeaf(YType.str, "host-name")

                self.initial_retransmit_maximum_timeout = YLeaf(YType.uint32, "initial-retransmit-maximum-timeout")

                self.initial_retransmit_minimum_timeout = YLeaf(YType.uint32, "initial-retransmit-minimum-timeout")

                self.initial_retransmit_retries = YLeaf(YType.uint32, "initial-retransmit-retries")

                self.ip_tos = YLeaf(YType.uint8, "ip-tos")

                self.is_authentication_enabled = YLeaf(YType.boolean, "is-authentication-enabled")

                self.is_congestion_control_enabled = YLeaf(YType.boolean, "is-congestion-control-enabled")

                self.is_digest_check_enabled = YLeaf(YType.boolean, "is-digest-check-enabled")

                self.is_digest_enabled = YLeaf(YType.boolean, "is-digest-enabled")

                self.is_hidden = YLeaf(YType.boolean, "is-hidden")

                self.is_peer_address_checked = YLeaf(YType.boolean, "is-peer-address-checked")

                self.password = YLeaf(YType.str, "password")

                self.receive_window_size = YLeaf(YType.uint16, "receive-window-size")

                self.retransmit_maximum_timeout = YLeaf(YType.uint32, "retransmit-maximum-timeout")

                self.retransmit_minimum_timeout = YLeaf(YType.uint32, "retransmit-minimum-timeout")

                self.retransmit_retries = YLeaf(YType.uint32, "retransmit-retries")

                self.setup_timeout = YLeaf(YType.uint32, "setup-timeout")

                self.timeout_no_user = YLeaf(YType.uint32, "timeout-no-user")

                self.vrf_name = YLeaf(YType.str, "vrf-name")
                self._segment_path = lambda: "class" + "[class-name='" + self.class_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/classes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(L2Tpv2.Classes.Class_, ['class_name', 'accounting_method_list', 'class_name_xr', 'digest_hash', 'encoded_password', 'hello_timeout', 'host_name', 'initial_retransmit_maximum_timeout', 'initial_retransmit_minimum_timeout', 'initial_retransmit_retries', 'ip_tos', 'is_authentication_enabled', 'is_congestion_control_enabled', 'is_digest_check_enabled', 'is_digest_enabled', 'is_hidden', 'is_peer_address_checked', 'password', 'receive_window_size', 'retransmit_maximum_timeout', 'retransmit_minimum_timeout', 'retransmit_retries', 'setup_timeout', 'timeout_no_user', 'vrf_name'], name, value)


    class CounterHistFail(Entity):
        """
        Failure events leading to disconnection
        
        .. attribute:: pkt_timeout
        
        	timeout events by packet
        	**type**\:  list of int
        
        	**range:** 0..4294967295
        
        .. attribute:: rx_counters
        
        	Receive side counters
        	**type**\:  str
        
        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
        
        .. attribute:: sess_down_tmout
        
        	sesions affected due to timeout
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: tx_counters
        
        	Send side counters
        	**type**\:  str
        
        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
        
        

        """

        _prefix = 'tunnel-l2tun-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(L2Tpv2.CounterHistFail, self).__init__()

            self.yang_name = "counter-hist-fail"
            self.yang_parent_name = "l2tpv2"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.pkt_timeout = YLeafList(YType.uint32, "pkt-timeout")

            self.rx_counters = YLeaf(YType.str, "rx-counters")

            self.sess_down_tmout = YLeaf(YType.uint32, "sess-down-tmout")

            self.tx_counters = YLeaf(YType.str, "tx-counters")
            self._segment_path = lambda: "counter-hist-fail"
            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(L2Tpv2.CounterHistFail, ['pkt_timeout', 'rx_counters', 'sess_down_tmout', 'tx_counters'], name, value)


    class Counters(Entity):
        """
        L2TP control messages counters
        
        .. attribute:: control
        
        	L2TP control messages counters
        	**type**\:   :py:class:`Control <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tpv2.Counters.Control>`
        
        .. attribute:: forwarding
        
        	L2TP forwarding messages counters
        	**type**\:   :py:class:`Forwarding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tpv2.Counters.Forwarding>`
        
        

        """

        _prefix = 'tunnel-l2tun-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(L2Tpv2.Counters, self).__init__()

            self.yang_name = "counters"
            self.yang_parent_name = "l2tpv2"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"control" : ("control", L2Tpv2.Counters.Control), "forwarding" : ("forwarding", L2Tpv2.Counters.Forwarding)}
            self._child_list_classes = {}

            self.control = L2Tpv2.Counters.Control()
            self.control.parent = self
            self._children_name_map["control"] = "control"
            self._children_yang_names.add("control")

            self.forwarding = L2Tpv2.Counters.Forwarding()
            self.forwarding.parent = self
            self._children_name_map["forwarding"] = "forwarding"
            self._children_yang_names.add("forwarding")
            self._segment_path = lambda: "counters"
            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/%s" % self._segment_path()


        class Control(Entity):
            """
            L2TP control messages counters
            
            .. attribute:: tunnel_xr
            
            	L2TP control tunnel messages counters
            	**type**\:   :py:class:`TunnelXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tpv2.Counters.Control.TunnelXr>`
            
            .. attribute:: tunnels
            
            	Table of tunnel IDs of control message counters
            	**type**\:   :py:class:`Tunnels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tpv2.Counters.Control.Tunnels>`
            
            

            """

            _prefix = 'tunnel-l2tun-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(L2Tpv2.Counters.Control, self).__init__()

                self.yang_name = "control"
                self.yang_parent_name = "counters"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"tunnel-xr" : ("tunnel_xr", L2Tpv2.Counters.Control.TunnelXr), "tunnels" : ("tunnels", L2Tpv2.Counters.Control.Tunnels)}
                self._child_list_classes = {}

                self.tunnel_xr = L2Tpv2.Counters.Control.TunnelXr()
                self.tunnel_xr.parent = self
                self._children_name_map["tunnel_xr"] = "tunnel-xr"
                self._children_yang_names.add("tunnel-xr")

                self.tunnels = L2Tpv2.Counters.Control.Tunnels()
                self.tunnels.parent = self
                self._children_name_map["tunnels"] = "tunnels"
                self._children_yang_names.add("tunnels")
                self._segment_path = lambda: "control"
                self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/counters/%s" % self._segment_path()


            class TunnelXr(Entity):
                """
                L2TP control tunnel messages counters
                
                .. attribute:: authentication
                
                	Tunnel authentication counters
                	**type**\:   :py:class:`Authentication <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tpv2.Counters.Control.TunnelXr.Authentication>`
                
                .. attribute:: global_
                
                	Tunnel counters
                	**type**\:   :py:class:`Global_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tpv2.Counters.Control.TunnelXr.Global_>`
                
                

                """

                _prefix = 'tunnel-l2tun-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(L2Tpv2.Counters.Control.TunnelXr, self).__init__()

                    self.yang_name = "tunnel-xr"
                    self.yang_parent_name = "control"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"authentication" : ("authentication", L2Tpv2.Counters.Control.TunnelXr.Authentication), "global" : ("global_", L2Tpv2.Counters.Control.TunnelXr.Global_)}
                    self._child_list_classes = {}

                    self.authentication = L2Tpv2.Counters.Control.TunnelXr.Authentication()
                    self.authentication.parent = self
                    self._children_name_map["authentication"] = "authentication"
                    self._children_yang_names.add("authentication")

                    self.global_ = L2Tpv2.Counters.Control.TunnelXr.Global_()
                    self.global_.parent = self
                    self._children_name_map["global_"] = "global"
                    self._children_yang_names.add("global")
                    self._segment_path = lambda: "tunnel-xr"
                    self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/counters/control/%s" % self._segment_path()


                class Authentication(Entity):
                    """
                    Tunnel authentication counters
                    
                    .. attribute:: challenge_avp
                    
                    	Challenge AVP statistics
                    	**type**\:   :py:class:`ChallengeAvp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tpv2.Counters.Control.TunnelXr.Authentication.ChallengeAvp>`
                    
                    .. attribute:: challenge_reponse
                    
                    	Challenge response statistics
                    	**type**\:   :py:class:`ChallengeReponse <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tpv2.Counters.Control.TunnelXr.Authentication.ChallengeReponse>`
                    
                    .. attribute:: common_digest
                    
                    	Common digest statistics
                    	**type**\:   :py:class:`CommonDigest <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tpv2.Counters.Control.TunnelXr.Authentication.CommonDigest>`
                    
                    .. attribute:: integrity_check
                    
                    	Integrity check statistics
                    	**type**\:   :py:class:`IntegrityCheck <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tpv2.Counters.Control.TunnelXr.Authentication.IntegrityCheck>`
                    
                    .. attribute:: local_secret
                    
                    	Local secret statistics
                    	**type**\:   :py:class:`LocalSecret <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tpv2.Counters.Control.TunnelXr.Authentication.LocalSecret>`
                    
                    .. attribute:: nonce_avp
                    
                    	Nonce AVP statistics
                    	**type**\:   :py:class:`NonceAvp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tpv2.Counters.Control.TunnelXr.Authentication.NonceAvp>`
                    
                    .. attribute:: overall_statistics
                    
                    	Overall statistics
                    	**type**\:   :py:class:`OverallStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tpv2.Counters.Control.TunnelXr.Authentication.OverallStatistics>`
                    
                    .. attribute:: primary_digest
                    
                    	Primary digest statistics
                    	**type**\:   :py:class:`PrimaryDigest <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tpv2.Counters.Control.TunnelXr.Authentication.PrimaryDigest>`
                    
                    .. attribute:: secondary_digest
                    
                    	Secondary digest statistics
                    	**type**\:   :py:class:`SecondaryDigest <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tpv2.Counters.Control.TunnelXr.Authentication.SecondaryDigest>`
                    
                    

                    """

                    _prefix = 'tunnel-l2tun-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(L2Tpv2.Counters.Control.TunnelXr.Authentication, self).__init__()

                        self.yang_name = "authentication"
                        self.yang_parent_name = "tunnel-xr"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"challenge-avp" : ("challenge_avp", L2Tpv2.Counters.Control.TunnelXr.Authentication.ChallengeAvp), "challenge-reponse" : ("challenge_reponse", L2Tpv2.Counters.Control.TunnelXr.Authentication.ChallengeReponse), "common-digest" : ("common_digest", L2Tpv2.Counters.Control.TunnelXr.Authentication.CommonDigest), "integrity-check" : ("integrity_check", L2Tpv2.Counters.Control.TunnelXr.Authentication.IntegrityCheck), "local-secret" : ("local_secret", L2Tpv2.Counters.Control.TunnelXr.Authentication.LocalSecret), "nonce-avp" : ("nonce_avp", L2Tpv2.Counters.Control.TunnelXr.Authentication.NonceAvp), "overall-statistics" : ("overall_statistics", L2Tpv2.Counters.Control.TunnelXr.Authentication.OverallStatistics), "primary-digest" : ("primary_digest", L2Tpv2.Counters.Control.TunnelXr.Authentication.PrimaryDigest), "secondary-digest" : ("secondary_digest", L2Tpv2.Counters.Control.TunnelXr.Authentication.SecondaryDigest)}
                        self._child_list_classes = {}

                        self.challenge_avp = L2Tpv2.Counters.Control.TunnelXr.Authentication.ChallengeAvp()
                        self.challenge_avp.parent = self
                        self._children_name_map["challenge_avp"] = "challenge-avp"
                        self._children_yang_names.add("challenge-avp")

                        self.challenge_reponse = L2Tpv2.Counters.Control.TunnelXr.Authentication.ChallengeReponse()
                        self.challenge_reponse.parent = self
                        self._children_name_map["challenge_reponse"] = "challenge-reponse"
                        self._children_yang_names.add("challenge-reponse")

                        self.common_digest = L2Tpv2.Counters.Control.TunnelXr.Authentication.CommonDigest()
                        self.common_digest.parent = self
                        self._children_name_map["common_digest"] = "common-digest"
                        self._children_yang_names.add("common-digest")

                        self.integrity_check = L2Tpv2.Counters.Control.TunnelXr.Authentication.IntegrityCheck()
                        self.integrity_check.parent = self
                        self._children_name_map["integrity_check"] = "integrity-check"
                        self._children_yang_names.add("integrity-check")

                        self.local_secret = L2Tpv2.Counters.Control.TunnelXr.Authentication.LocalSecret()
                        self.local_secret.parent = self
                        self._children_name_map["local_secret"] = "local-secret"
                        self._children_yang_names.add("local-secret")

                        self.nonce_avp = L2Tpv2.Counters.Control.TunnelXr.Authentication.NonceAvp()
                        self.nonce_avp.parent = self
                        self._children_name_map["nonce_avp"] = "nonce-avp"
                        self._children_yang_names.add("nonce-avp")

                        self.overall_statistics = L2Tpv2.Counters.Control.TunnelXr.Authentication.OverallStatistics()
                        self.overall_statistics.parent = self
                        self._children_name_map["overall_statistics"] = "overall-statistics"
                        self._children_yang_names.add("overall-statistics")

                        self.primary_digest = L2Tpv2.Counters.Control.TunnelXr.Authentication.PrimaryDigest()
                        self.primary_digest.parent = self
                        self._children_name_map["primary_digest"] = "primary-digest"
                        self._children_yang_names.add("primary-digest")

                        self.secondary_digest = L2Tpv2.Counters.Control.TunnelXr.Authentication.SecondaryDigest()
                        self.secondary_digest.parent = self
                        self._children_name_map["secondary_digest"] = "secondary-digest"
                        self._children_yang_names.add("secondary-digest")
                        self._segment_path = lambda: "authentication"
                        self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/counters/control/tunnel-xr/%s" % self._segment_path()


                    class ChallengeAvp(Entity):
                        """
                        Challenge AVP statistics
                        
                        .. attribute:: bad_hash
                        
                        	Bad hash
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_length
                        
                        	Bad length
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: failed
                        
                        	Failed
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: generate_response_failures
                        
                        	Generate response fail
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ignored
                        
                        	Ignored
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: missing
                        
                        	Missing
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: passed
                        
                        	Passed
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: skipped
                        
                        	Skipped
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unexpected
                        
                        	Unexpected
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unexpected_zlb
                        
                        	Unexpected ZLB
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: validate
                        
                        	Validate
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'tunnel-l2tun-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(L2Tpv2.Counters.Control.TunnelXr.Authentication.ChallengeAvp, self).__init__()

                            self.yang_name = "challenge-avp"
                            self.yang_parent_name = "authentication"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.bad_hash = YLeaf(YType.uint32, "bad-hash")

                            self.bad_length = YLeaf(YType.uint32, "bad-length")

                            self.failed = YLeaf(YType.uint32, "failed")

                            self.generate_response_failures = YLeaf(YType.uint32, "generate-response-failures")

                            self.ignored = YLeaf(YType.uint32, "ignored")

                            self.missing = YLeaf(YType.uint32, "missing")

                            self.passed = YLeaf(YType.uint32, "passed")

                            self.skipped = YLeaf(YType.uint32, "skipped")

                            self.unexpected = YLeaf(YType.uint32, "unexpected")

                            self.unexpected_zlb = YLeaf(YType.uint32, "unexpected-zlb")

                            self.validate = YLeaf(YType.uint32, "validate")
                            self._segment_path = lambda: "challenge-avp"
                            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/counters/control/tunnel-xr/authentication/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2Tpv2.Counters.Control.TunnelXr.Authentication.ChallengeAvp, ['bad_hash', 'bad_length', 'failed', 'generate_response_failures', 'ignored', 'missing', 'passed', 'skipped', 'unexpected', 'unexpected_zlb', 'validate'], name, value)


                    class ChallengeReponse(Entity):
                        """
                        Challenge response statistics
                        
                        .. attribute:: bad_hash
                        
                        	Bad hash
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_length
                        
                        	Bad length
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: failed
                        
                        	Failed
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: generate_response_failures
                        
                        	Generate response fail
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ignored
                        
                        	Ignored
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: missing
                        
                        	Missing
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: passed
                        
                        	Passed
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: skipped
                        
                        	Skipped
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unexpected
                        
                        	Unexpected
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unexpected_zlb
                        
                        	Unexpected ZLB
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: validate
                        
                        	Validate
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'tunnel-l2tun-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(L2Tpv2.Counters.Control.TunnelXr.Authentication.ChallengeReponse, self).__init__()

                            self.yang_name = "challenge-reponse"
                            self.yang_parent_name = "authentication"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.bad_hash = YLeaf(YType.uint32, "bad-hash")

                            self.bad_length = YLeaf(YType.uint32, "bad-length")

                            self.failed = YLeaf(YType.uint32, "failed")

                            self.generate_response_failures = YLeaf(YType.uint32, "generate-response-failures")

                            self.ignored = YLeaf(YType.uint32, "ignored")

                            self.missing = YLeaf(YType.uint32, "missing")

                            self.passed = YLeaf(YType.uint32, "passed")

                            self.skipped = YLeaf(YType.uint32, "skipped")

                            self.unexpected = YLeaf(YType.uint32, "unexpected")

                            self.unexpected_zlb = YLeaf(YType.uint32, "unexpected-zlb")

                            self.validate = YLeaf(YType.uint32, "validate")
                            self._segment_path = lambda: "challenge-reponse"
                            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/counters/control/tunnel-xr/authentication/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2Tpv2.Counters.Control.TunnelXr.Authentication.ChallengeReponse, ['bad_hash', 'bad_length', 'failed', 'generate_response_failures', 'ignored', 'missing', 'passed', 'skipped', 'unexpected', 'unexpected_zlb', 'validate'], name, value)


                    class CommonDigest(Entity):
                        """
                        Common digest statistics
                        
                        .. attribute:: bad_hash
                        
                        	Bad hash
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_length
                        
                        	Bad length
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: failed
                        
                        	Failed
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: generate_response_failures
                        
                        	Generate response fail
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ignored
                        
                        	Ignored
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: missing
                        
                        	Missing
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: passed
                        
                        	Passed
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: skipped
                        
                        	Skipped
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unexpected
                        
                        	Unexpected
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unexpected_zlb
                        
                        	Unexpected ZLB
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: validate
                        
                        	Validate
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'tunnel-l2tun-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(L2Tpv2.Counters.Control.TunnelXr.Authentication.CommonDigest, self).__init__()

                            self.yang_name = "common-digest"
                            self.yang_parent_name = "authentication"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.bad_hash = YLeaf(YType.uint32, "bad-hash")

                            self.bad_length = YLeaf(YType.uint32, "bad-length")

                            self.failed = YLeaf(YType.uint32, "failed")

                            self.generate_response_failures = YLeaf(YType.uint32, "generate-response-failures")

                            self.ignored = YLeaf(YType.uint32, "ignored")

                            self.missing = YLeaf(YType.uint32, "missing")

                            self.passed = YLeaf(YType.uint32, "passed")

                            self.skipped = YLeaf(YType.uint32, "skipped")

                            self.unexpected = YLeaf(YType.uint32, "unexpected")

                            self.unexpected_zlb = YLeaf(YType.uint32, "unexpected-zlb")

                            self.validate = YLeaf(YType.uint32, "validate")
                            self._segment_path = lambda: "common-digest"
                            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/counters/control/tunnel-xr/authentication/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2Tpv2.Counters.Control.TunnelXr.Authentication.CommonDigest, ['bad_hash', 'bad_length', 'failed', 'generate_response_failures', 'ignored', 'missing', 'passed', 'skipped', 'unexpected', 'unexpected_zlb', 'validate'], name, value)


                    class IntegrityCheck(Entity):
                        """
                        Integrity check statistics
                        
                        .. attribute:: bad_hash
                        
                        	Bad hash
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_length
                        
                        	Bad length
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: failed
                        
                        	Failed
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: generate_response_failures
                        
                        	Generate response fail
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ignored
                        
                        	Ignored
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: missing
                        
                        	Missing
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: passed
                        
                        	Passed
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: skipped
                        
                        	Skipped
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unexpected
                        
                        	Unexpected
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unexpected_zlb
                        
                        	Unexpected ZLB
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: validate
                        
                        	Validate
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'tunnel-l2tun-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(L2Tpv2.Counters.Control.TunnelXr.Authentication.IntegrityCheck, self).__init__()

                            self.yang_name = "integrity-check"
                            self.yang_parent_name = "authentication"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.bad_hash = YLeaf(YType.uint32, "bad-hash")

                            self.bad_length = YLeaf(YType.uint32, "bad-length")

                            self.failed = YLeaf(YType.uint32, "failed")

                            self.generate_response_failures = YLeaf(YType.uint32, "generate-response-failures")

                            self.ignored = YLeaf(YType.uint32, "ignored")

                            self.missing = YLeaf(YType.uint32, "missing")

                            self.passed = YLeaf(YType.uint32, "passed")

                            self.skipped = YLeaf(YType.uint32, "skipped")

                            self.unexpected = YLeaf(YType.uint32, "unexpected")

                            self.unexpected_zlb = YLeaf(YType.uint32, "unexpected-zlb")

                            self.validate = YLeaf(YType.uint32, "validate")
                            self._segment_path = lambda: "integrity-check"
                            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/counters/control/tunnel-xr/authentication/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2Tpv2.Counters.Control.TunnelXr.Authentication.IntegrityCheck, ['bad_hash', 'bad_length', 'failed', 'generate_response_failures', 'ignored', 'missing', 'passed', 'skipped', 'unexpected', 'unexpected_zlb', 'validate'], name, value)


                    class LocalSecret(Entity):
                        """
                        Local secret statistics
                        
                        .. attribute:: bad_hash
                        
                        	Bad hash
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_length
                        
                        	Bad length
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: failed
                        
                        	Failed
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: generate_response_failures
                        
                        	Generate response fail
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ignored
                        
                        	Ignored
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: missing
                        
                        	Missing
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: passed
                        
                        	Passed
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: skipped
                        
                        	Skipped
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unexpected
                        
                        	Unexpected
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unexpected_zlb
                        
                        	Unexpected ZLB
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: validate
                        
                        	Validate
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'tunnel-l2tun-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(L2Tpv2.Counters.Control.TunnelXr.Authentication.LocalSecret, self).__init__()

                            self.yang_name = "local-secret"
                            self.yang_parent_name = "authentication"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.bad_hash = YLeaf(YType.uint32, "bad-hash")

                            self.bad_length = YLeaf(YType.uint32, "bad-length")

                            self.failed = YLeaf(YType.uint32, "failed")

                            self.generate_response_failures = YLeaf(YType.uint32, "generate-response-failures")

                            self.ignored = YLeaf(YType.uint32, "ignored")

                            self.missing = YLeaf(YType.uint32, "missing")

                            self.passed = YLeaf(YType.uint32, "passed")

                            self.skipped = YLeaf(YType.uint32, "skipped")

                            self.unexpected = YLeaf(YType.uint32, "unexpected")

                            self.unexpected_zlb = YLeaf(YType.uint32, "unexpected-zlb")

                            self.validate = YLeaf(YType.uint32, "validate")
                            self._segment_path = lambda: "local-secret"
                            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/counters/control/tunnel-xr/authentication/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2Tpv2.Counters.Control.TunnelXr.Authentication.LocalSecret, ['bad_hash', 'bad_length', 'failed', 'generate_response_failures', 'ignored', 'missing', 'passed', 'skipped', 'unexpected', 'unexpected_zlb', 'validate'], name, value)


                    class NonceAvp(Entity):
                        """
                        Nonce AVP statistics
                        
                        .. attribute:: bad_hash
                        
                        	Bad hash
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_length
                        
                        	Bad length
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: failed
                        
                        	Failed
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: generate_response_failures
                        
                        	Generate response fail
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ignored
                        
                        	Ignored
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: missing
                        
                        	Missing
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: passed
                        
                        	Passed
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: skipped
                        
                        	Skipped
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unexpected
                        
                        	Unexpected
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unexpected_zlb
                        
                        	Unexpected ZLB
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: validate
                        
                        	Validate
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'tunnel-l2tun-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(L2Tpv2.Counters.Control.TunnelXr.Authentication.NonceAvp, self).__init__()

                            self.yang_name = "nonce-avp"
                            self.yang_parent_name = "authentication"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.bad_hash = YLeaf(YType.uint32, "bad-hash")

                            self.bad_length = YLeaf(YType.uint32, "bad-length")

                            self.failed = YLeaf(YType.uint32, "failed")

                            self.generate_response_failures = YLeaf(YType.uint32, "generate-response-failures")

                            self.ignored = YLeaf(YType.uint32, "ignored")

                            self.missing = YLeaf(YType.uint32, "missing")

                            self.passed = YLeaf(YType.uint32, "passed")

                            self.skipped = YLeaf(YType.uint32, "skipped")

                            self.unexpected = YLeaf(YType.uint32, "unexpected")

                            self.unexpected_zlb = YLeaf(YType.uint32, "unexpected-zlb")

                            self.validate = YLeaf(YType.uint32, "validate")
                            self._segment_path = lambda: "nonce-avp"
                            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/counters/control/tunnel-xr/authentication/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2Tpv2.Counters.Control.TunnelXr.Authentication.NonceAvp, ['bad_hash', 'bad_length', 'failed', 'generate_response_failures', 'ignored', 'missing', 'passed', 'skipped', 'unexpected', 'unexpected_zlb', 'validate'], name, value)


                    class OverallStatistics(Entity):
                        """
                        Overall statistics
                        
                        .. attribute:: bad_hash
                        
                        	Bad hash
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_length
                        
                        	Bad length
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: failed
                        
                        	Failed
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: generate_response_failures
                        
                        	Generate response fail
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ignored
                        
                        	Ignored
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: missing
                        
                        	Missing
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: passed
                        
                        	Passed
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: skipped
                        
                        	Skipped
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unexpected
                        
                        	Unexpected
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unexpected_zlb
                        
                        	Unexpected ZLB
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: validate
                        
                        	Validate
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'tunnel-l2tun-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(L2Tpv2.Counters.Control.TunnelXr.Authentication.OverallStatistics, self).__init__()

                            self.yang_name = "overall-statistics"
                            self.yang_parent_name = "authentication"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.bad_hash = YLeaf(YType.uint32, "bad-hash")

                            self.bad_length = YLeaf(YType.uint32, "bad-length")

                            self.failed = YLeaf(YType.uint32, "failed")

                            self.generate_response_failures = YLeaf(YType.uint32, "generate-response-failures")

                            self.ignored = YLeaf(YType.uint32, "ignored")

                            self.missing = YLeaf(YType.uint32, "missing")

                            self.passed = YLeaf(YType.uint32, "passed")

                            self.skipped = YLeaf(YType.uint32, "skipped")

                            self.unexpected = YLeaf(YType.uint32, "unexpected")

                            self.unexpected_zlb = YLeaf(YType.uint32, "unexpected-zlb")

                            self.validate = YLeaf(YType.uint32, "validate")
                            self._segment_path = lambda: "overall-statistics"
                            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/counters/control/tunnel-xr/authentication/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2Tpv2.Counters.Control.TunnelXr.Authentication.OverallStatistics, ['bad_hash', 'bad_length', 'failed', 'generate_response_failures', 'ignored', 'missing', 'passed', 'skipped', 'unexpected', 'unexpected_zlb', 'validate'], name, value)


                    class PrimaryDigest(Entity):
                        """
                        Primary digest statistics
                        
                        .. attribute:: bad_hash
                        
                        	Bad hash
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_length
                        
                        	Bad length
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: failed
                        
                        	Failed
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: generate_response_failures
                        
                        	Generate response fail
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ignored
                        
                        	Ignored
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: missing
                        
                        	Missing
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: passed
                        
                        	Passed
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: skipped
                        
                        	Skipped
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unexpected
                        
                        	Unexpected
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unexpected_zlb
                        
                        	Unexpected ZLB
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: validate
                        
                        	Validate
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'tunnel-l2tun-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(L2Tpv2.Counters.Control.TunnelXr.Authentication.PrimaryDigest, self).__init__()

                            self.yang_name = "primary-digest"
                            self.yang_parent_name = "authentication"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.bad_hash = YLeaf(YType.uint32, "bad-hash")

                            self.bad_length = YLeaf(YType.uint32, "bad-length")

                            self.failed = YLeaf(YType.uint32, "failed")

                            self.generate_response_failures = YLeaf(YType.uint32, "generate-response-failures")

                            self.ignored = YLeaf(YType.uint32, "ignored")

                            self.missing = YLeaf(YType.uint32, "missing")

                            self.passed = YLeaf(YType.uint32, "passed")

                            self.skipped = YLeaf(YType.uint32, "skipped")

                            self.unexpected = YLeaf(YType.uint32, "unexpected")

                            self.unexpected_zlb = YLeaf(YType.uint32, "unexpected-zlb")

                            self.validate = YLeaf(YType.uint32, "validate")
                            self._segment_path = lambda: "primary-digest"
                            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/counters/control/tunnel-xr/authentication/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2Tpv2.Counters.Control.TunnelXr.Authentication.PrimaryDigest, ['bad_hash', 'bad_length', 'failed', 'generate_response_failures', 'ignored', 'missing', 'passed', 'skipped', 'unexpected', 'unexpected_zlb', 'validate'], name, value)


                    class SecondaryDigest(Entity):
                        """
                        Secondary digest statistics
                        
                        .. attribute:: bad_hash
                        
                        	Bad hash
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_length
                        
                        	Bad length
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: failed
                        
                        	Failed
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: generate_response_failures
                        
                        	Generate response fail
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ignored
                        
                        	Ignored
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: missing
                        
                        	Missing
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: passed
                        
                        	Passed
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: skipped
                        
                        	Skipped
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unexpected
                        
                        	Unexpected
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unexpected_zlb
                        
                        	Unexpected ZLB
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: validate
                        
                        	Validate
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'tunnel-l2tun-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(L2Tpv2.Counters.Control.TunnelXr.Authentication.SecondaryDigest, self).__init__()

                            self.yang_name = "secondary-digest"
                            self.yang_parent_name = "authentication"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.bad_hash = YLeaf(YType.uint32, "bad-hash")

                            self.bad_length = YLeaf(YType.uint32, "bad-length")

                            self.failed = YLeaf(YType.uint32, "failed")

                            self.generate_response_failures = YLeaf(YType.uint32, "generate-response-failures")

                            self.ignored = YLeaf(YType.uint32, "ignored")

                            self.missing = YLeaf(YType.uint32, "missing")

                            self.passed = YLeaf(YType.uint32, "passed")

                            self.skipped = YLeaf(YType.uint32, "skipped")

                            self.unexpected = YLeaf(YType.uint32, "unexpected")

                            self.unexpected_zlb = YLeaf(YType.uint32, "unexpected-zlb")

                            self.validate = YLeaf(YType.uint32, "validate")
                            self._segment_path = lambda: "secondary-digest"
                            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/counters/control/tunnel-xr/authentication/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2Tpv2.Counters.Control.TunnelXr.Authentication.SecondaryDigest, ['bad_hash', 'bad_length', 'failed', 'generate_response_failures', 'ignored', 'missing', 'passed', 'skipped', 'unexpected', 'unexpected_zlb', 'validate'], name, value)


                class Global_(Entity):
                    """
                    Tunnel counters
                    
                    .. attribute:: drop
                    
                    	Drop data
                    	**type**\:   :py:class:`Drop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tpv2.Counters.Control.TunnelXr.Global_.Drop>`
                    
                    .. attribute:: received
                    
                    	Received data
                    	**type**\:   :py:class:`Received <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tpv2.Counters.Control.TunnelXr.Global_.Received>`
                    
                    .. attribute:: retransmit
                    
                    	Re transmit data
                    	**type**\:   :py:class:`Retransmit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tpv2.Counters.Control.TunnelXr.Global_.Retransmit>`
                    
                    .. attribute:: total_drop
                    
                    	Total drop
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: total_received
                    
                    	Total received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: total_retransmit
                    
                    	Total retransmit
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: total_transmit
                    
                    	Total transmit
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: transmit
                    
                    	Transmit data
                    	**type**\:   :py:class:`Transmit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tpv2.Counters.Control.TunnelXr.Global_.Transmit>`
                    
                    

                    """

                    _prefix = 'tunnel-l2tun-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(L2Tpv2.Counters.Control.TunnelXr.Global_, self).__init__()

                        self.yang_name = "global"
                        self.yang_parent_name = "tunnel-xr"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"drop" : ("drop", L2Tpv2.Counters.Control.TunnelXr.Global_.Drop), "received" : ("received", L2Tpv2.Counters.Control.TunnelXr.Global_.Received), "retransmit" : ("retransmit", L2Tpv2.Counters.Control.TunnelXr.Global_.Retransmit), "transmit" : ("transmit", L2Tpv2.Counters.Control.TunnelXr.Global_.Transmit)}
                        self._child_list_classes = {}

                        self.total_drop = YLeaf(YType.uint32, "total-drop")

                        self.total_received = YLeaf(YType.uint32, "total-received")

                        self.total_retransmit = YLeaf(YType.uint32, "total-retransmit")

                        self.total_transmit = YLeaf(YType.uint32, "total-transmit")

                        self.drop = L2Tpv2.Counters.Control.TunnelXr.Global_.Drop()
                        self.drop.parent = self
                        self._children_name_map["drop"] = "drop"
                        self._children_yang_names.add("drop")

                        self.received = L2Tpv2.Counters.Control.TunnelXr.Global_.Received()
                        self.received.parent = self
                        self._children_name_map["received"] = "received"
                        self._children_yang_names.add("received")

                        self.retransmit = L2Tpv2.Counters.Control.TunnelXr.Global_.Retransmit()
                        self.retransmit.parent = self
                        self._children_name_map["retransmit"] = "retransmit"
                        self._children_yang_names.add("retransmit")

                        self.transmit = L2Tpv2.Counters.Control.TunnelXr.Global_.Transmit()
                        self.transmit.parent = self
                        self._children_name_map["transmit"] = "transmit"
                        self._children_yang_names.add("transmit")
                        self._segment_path = lambda: "global"
                        self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/counters/control/tunnel-xr/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2Tpv2.Counters.Control.TunnelXr.Global_, ['total_drop', 'total_received', 'total_retransmit', 'total_transmit'], name, value)


                    class Drop(Entity):
                        """
                        Drop data
                        
                        .. attribute:: acknowledgement_packets
                        
                        	Packets acknowledgement
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: call_disconnect_notify_packets
                        
                        	Call disconnect notify packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: hello_packets
                        
                        	Keep alive messages
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: incoming_call_connected_packets
                        
                        	Incoming call connected packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: incoming_call_replies
                        
                        	Incoming call replies
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: incoming_call_requests
                        
                        	Incoming call requests
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: outgoing_call_connected_packets
                        
                        	Outgoing call connected packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: outgoing_call_replies
                        
                        	Outgoing call replies
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: outgoing_call_requests
                        
                        	Outgoing call requests
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: service_relay_replies
                        
                        	Service relay reply counts
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: service_relay_requests
                        
                        	Service relay request counts
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: set_link_info_packets
                        
                        	Set link info packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: start_control_connection_notifications
                        
                        	Start control connection notifications
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: start_control_connection_replies
                        
                        	Start control connection replies
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: start_control_connection_requests
                        
                        	Start control connection requests
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: stop_control_connection_notifications
                        
                        	Stop control connection notifications
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unknown_packets
                        
                        	Unknown packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: wan_error_notify_packets
                        
                        	WAN error notify packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: zero_length_body_packets
                        
                        	Zero length body packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'tunnel-l2tun-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(L2Tpv2.Counters.Control.TunnelXr.Global_.Drop, self).__init__()

                            self.yang_name = "drop"
                            self.yang_parent_name = "global"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.acknowledgement_packets = YLeaf(YType.uint32, "acknowledgement-packets")

                            self.call_disconnect_notify_packets = YLeaf(YType.uint32, "call-disconnect-notify-packets")

                            self.hello_packets = YLeaf(YType.uint32, "hello-packets")

                            self.incoming_call_connected_packets = YLeaf(YType.uint32, "incoming-call-connected-packets")

                            self.incoming_call_replies = YLeaf(YType.uint32, "incoming-call-replies")

                            self.incoming_call_requests = YLeaf(YType.uint32, "incoming-call-requests")

                            self.outgoing_call_connected_packets = YLeaf(YType.uint32, "outgoing-call-connected-packets")

                            self.outgoing_call_replies = YLeaf(YType.uint32, "outgoing-call-replies")

                            self.outgoing_call_requests = YLeaf(YType.uint32, "outgoing-call-requests")

                            self.service_relay_replies = YLeaf(YType.uint32, "service-relay-replies")

                            self.service_relay_requests = YLeaf(YType.uint32, "service-relay-requests")

                            self.set_link_info_packets = YLeaf(YType.uint32, "set-link-info-packets")

                            self.start_control_connection_notifications = YLeaf(YType.uint32, "start-control-connection-notifications")

                            self.start_control_connection_replies = YLeaf(YType.uint32, "start-control-connection-replies")

                            self.start_control_connection_requests = YLeaf(YType.uint32, "start-control-connection-requests")

                            self.stop_control_connection_notifications = YLeaf(YType.uint32, "stop-control-connection-notifications")

                            self.unknown_packets = YLeaf(YType.uint32, "unknown-packets")

                            self.wan_error_notify_packets = YLeaf(YType.uint32, "wan-error-notify-packets")

                            self.zero_length_body_packets = YLeaf(YType.uint32, "zero-length-body-packets")
                            self._segment_path = lambda: "drop"
                            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/counters/control/tunnel-xr/global/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2Tpv2.Counters.Control.TunnelXr.Global_.Drop, ['acknowledgement_packets', 'call_disconnect_notify_packets', 'hello_packets', 'incoming_call_connected_packets', 'incoming_call_replies', 'incoming_call_requests', 'outgoing_call_connected_packets', 'outgoing_call_replies', 'outgoing_call_requests', 'service_relay_replies', 'service_relay_requests', 'set_link_info_packets', 'start_control_connection_notifications', 'start_control_connection_replies', 'start_control_connection_requests', 'stop_control_connection_notifications', 'unknown_packets', 'wan_error_notify_packets', 'zero_length_body_packets'], name, value)


                    class Received(Entity):
                        """
                        Received data
                        
                        .. attribute:: acknowledgement_packets
                        
                        	Packets acknowledgement
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: call_disconnect_notify_packets
                        
                        	Call disconnect notify packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: hello_packets
                        
                        	Keep alive messages
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: incoming_call_connected_packets
                        
                        	Incoming call connected packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: incoming_call_replies
                        
                        	Incoming call replies
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: incoming_call_requests
                        
                        	Incoming call requests
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: outgoing_call_connected_packets
                        
                        	Outgoing call connected packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: outgoing_call_replies
                        
                        	Outgoing call replies
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: outgoing_call_requests
                        
                        	Outgoing call requests
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: service_relay_replies
                        
                        	Service relay reply counts
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: service_relay_requests
                        
                        	Service relay request counts
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: set_link_info_packets
                        
                        	Set link info packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: start_control_connection_notifications
                        
                        	Start control connection notifications
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: start_control_connection_replies
                        
                        	Start control connection replies
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: start_control_connection_requests
                        
                        	Start control connection requests
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: stop_control_connection_notifications
                        
                        	Stop control connection notifications
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unknown_packets
                        
                        	Unknown packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: wan_error_notify_packets
                        
                        	WAN error notify packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: zero_length_body_packets
                        
                        	Zero length body packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'tunnel-l2tun-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(L2Tpv2.Counters.Control.TunnelXr.Global_.Received, self).__init__()

                            self.yang_name = "received"
                            self.yang_parent_name = "global"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.acknowledgement_packets = YLeaf(YType.uint32, "acknowledgement-packets")

                            self.call_disconnect_notify_packets = YLeaf(YType.uint32, "call-disconnect-notify-packets")

                            self.hello_packets = YLeaf(YType.uint32, "hello-packets")

                            self.incoming_call_connected_packets = YLeaf(YType.uint32, "incoming-call-connected-packets")

                            self.incoming_call_replies = YLeaf(YType.uint32, "incoming-call-replies")

                            self.incoming_call_requests = YLeaf(YType.uint32, "incoming-call-requests")

                            self.outgoing_call_connected_packets = YLeaf(YType.uint32, "outgoing-call-connected-packets")

                            self.outgoing_call_replies = YLeaf(YType.uint32, "outgoing-call-replies")

                            self.outgoing_call_requests = YLeaf(YType.uint32, "outgoing-call-requests")

                            self.service_relay_replies = YLeaf(YType.uint32, "service-relay-replies")

                            self.service_relay_requests = YLeaf(YType.uint32, "service-relay-requests")

                            self.set_link_info_packets = YLeaf(YType.uint32, "set-link-info-packets")

                            self.start_control_connection_notifications = YLeaf(YType.uint32, "start-control-connection-notifications")

                            self.start_control_connection_replies = YLeaf(YType.uint32, "start-control-connection-replies")

                            self.start_control_connection_requests = YLeaf(YType.uint32, "start-control-connection-requests")

                            self.stop_control_connection_notifications = YLeaf(YType.uint32, "stop-control-connection-notifications")

                            self.unknown_packets = YLeaf(YType.uint32, "unknown-packets")

                            self.wan_error_notify_packets = YLeaf(YType.uint32, "wan-error-notify-packets")

                            self.zero_length_body_packets = YLeaf(YType.uint32, "zero-length-body-packets")
                            self._segment_path = lambda: "received"
                            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/counters/control/tunnel-xr/global/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2Tpv2.Counters.Control.TunnelXr.Global_.Received, ['acknowledgement_packets', 'call_disconnect_notify_packets', 'hello_packets', 'incoming_call_connected_packets', 'incoming_call_replies', 'incoming_call_requests', 'outgoing_call_connected_packets', 'outgoing_call_replies', 'outgoing_call_requests', 'service_relay_replies', 'service_relay_requests', 'set_link_info_packets', 'start_control_connection_notifications', 'start_control_connection_replies', 'start_control_connection_requests', 'stop_control_connection_notifications', 'unknown_packets', 'wan_error_notify_packets', 'zero_length_body_packets'], name, value)


                    class Retransmit(Entity):
                        """
                        Re transmit data
                        
                        .. attribute:: acknowledgement_packets
                        
                        	Packets acknowledgement
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: call_disconnect_notify_packets
                        
                        	Call disconnect notify packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: hello_packets
                        
                        	Keep alive messages
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: incoming_call_connected_packets
                        
                        	Incoming call connected packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: incoming_call_replies
                        
                        	Incoming call replies
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: incoming_call_requests
                        
                        	Incoming call requests
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: outgoing_call_connected_packets
                        
                        	Outgoing call connected packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: outgoing_call_replies
                        
                        	Outgoing call replies
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: outgoing_call_requests
                        
                        	Outgoing call requests
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: service_relay_replies
                        
                        	Service relay reply counts
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: service_relay_requests
                        
                        	Service relay request counts
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: set_link_info_packets
                        
                        	Set link info packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: start_control_connection_notifications
                        
                        	Start control connection notifications
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: start_control_connection_replies
                        
                        	Start control connection replies
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: start_control_connection_requests
                        
                        	Start control connection requests
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: stop_control_connection_notifications
                        
                        	Stop control connection notifications
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unknown_packets
                        
                        	Unknown packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: wan_error_notify_packets
                        
                        	WAN error notify packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: zero_length_body_packets
                        
                        	Zero length body packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'tunnel-l2tun-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(L2Tpv2.Counters.Control.TunnelXr.Global_.Retransmit, self).__init__()

                            self.yang_name = "retransmit"
                            self.yang_parent_name = "global"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.acknowledgement_packets = YLeaf(YType.uint32, "acknowledgement-packets")

                            self.call_disconnect_notify_packets = YLeaf(YType.uint32, "call-disconnect-notify-packets")

                            self.hello_packets = YLeaf(YType.uint32, "hello-packets")

                            self.incoming_call_connected_packets = YLeaf(YType.uint32, "incoming-call-connected-packets")

                            self.incoming_call_replies = YLeaf(YType.uint32, "incoming-call-replies")

                            self.incoming_call_requests = YLeaf(YType.uint32, "incoming-call-requests")

                            self.outgoing_call_connected_packets = YLeaf(YType.uint32, "outgoing-call-connected-packets")

                            self.outgoing_call_replies = YLeaf(YType.uint32, "outgoing-call-replies")

                            self.outgoing_call_requests = YLeaf(YType.uint32, "outgoing-call-requests")

                            self.service_relay_replies = YLeaf(YType.uint32, "service-relay-replies")

                            self.service_relay_requests = YLeaf(YType.uint32, "service-relay-requests")

                            self.set_link_info_packets = YLeaf(YType.uint32, "set-link-info-packets")

                            self.start_control_connection_notifications = YLeaf(YType.uint32, "start-control-connection-notifications")

                            self.start_control_connection_replies = YLeaf(YType.uint32, "start-control-connection-replies")

                            self.start_control_connection_requests = YLeaf(YType.uint32, "start-control-connection-requests")

                            self.stop_control_connection_notifications = YLeaf(YType.uint32, "stop-control-connection-notifications")

                            self.unknown_packets = YLeaf(YType.uint32, "unknown-packets")

                            self.wan_error_notify_packets = YLeaf(YType.uint32, "wan-error-notify-packets")

                            self.zero_length_body_packets = YLeaf(YType.uint32, "zero-length-body-packets")
                            self._segment_path = lambda: "retransmit"
                            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/counters/control/tunnel-xr/global/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2Tpv2.Counters.Control.TunnelXr.Global_.Retransmit, ['acknowledgement_packets', 'call_disconnect_notify_packets', 'hello_packets', 'incoming_call_connected_packets', 'incoming_call_replies', 'incoming_call_requests', 'outgoing_call_connected_packets', 'outgoing_call_replies', 'outgoing_call_requests', 'service_relay_replies', 'service_relay_requests', 'set_link_info_packets', 'start_control_connection_notifications', 'start_control_connection_replies', 'start_control_connection_requests', 'stop_control_connection_notifications', 'unknown_packets', 'wan_error_notify_packets', 'zero_length_body_packets'], name, value)


                    class Transmit(Entity):
                        """
                        Transmit data
                        
                        .. attribute:: acknowledgement_packets
                        
                        	Packets acknowledgement
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: call_disconnect_notify_packets
                        
                        	Call disconnect notify packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: hello_packets
                        
                        	Keep alive messages
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: incoming_call_connected_packets
                        
                        	Incoming call connected packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: incoming_call_replies
                        
                        	Incoming call replies
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: incoming_call_requests
                        
                        	Incoming call requests
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: outgoing_call_connected_packets
                        
                        	Outgoing call connected packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: outgoing_call_replies
                        
                        	Outgoing call replies
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: outgoing_call_requests
                        
                        	Outgoing call requests
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: service_relay_replies
                        
                        	Service relay reply counts
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: service_relay_requests
                        
                        	Service relay request counts
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: set_link_info_packets
                        
                        	Set link info packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: start_control_connection_notifications
                        
                        	Start control connection notifications
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: start_control_connection_replies
                        
                        	Start control connection replies
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: start_control_connection_requests
                        
                        	Start control connection requests
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: stop_control_connection_notifications
                        
                        	Stop control connection notifications
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unknown_packets
                        
                        	Unknown packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: wan_error_notify_packets
                        
                        	WAN error notify packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: zero_length_body_packets
                        
                        	Zero length body packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'tunnel-l2tun-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(L2Tpv2.Counters.Control.TunnelXr.Global_.Transmit, self).__init__()

                            self.yang_name = "transmit"
                            self.yang_parent_name = "global"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.acknowledgement_packets = YLeaf(YType.uint32, "acknowledgement-packets")

                            self.call_disconnect_notify_packets = YLeaf(YType.uint32, "call-disconnect-notify-packets")

                            self.hello_packets = YLeaf(YType.uint32, "hello-packets")

                            self.incoming_call_connected_packets = YLeaf(YType.uint32, "incoming-call-connected-packets")

                            self.incoming_call_replies = YLeaf(YType.uint32, "incoming-call-replies")

                            self.incoming_call_requests = YLeaf(YType.uint32, "incoming-call-requests")

                            self.outgoing_call_connected_packets = YLeaf(YType.uint32, "outgoing-call-connected-packets")

                            self.outgoing_call_replies = YLeaf(YType.uint32, "outgoing-call-replies")

                            self.outgoing_call_requests = YLeaf(YType.uint32, "outgoing-call-requests")

                            self.service_relay_replies = YLeaf(YType.uint32, "service-relay-replies")

                            self.service_relay_requests = YLeaf(YType.uint32, "service-relay-requests")

                            self.set_link_info_packets = YLeaf(YType.uint32, "set-link-info-packets")

                            self.start_control_connection_notifications = YLeaf(YType.uint32, "start-control-connection-notifications")

                            self.start_control_connection_replies = YLeaf(YType.uint32, "start-control-connection-replies")

                            self.start_control_connection_requests = YLeaf(YType.uint32, "start-control-connection-requests")

                            self.stop_control_connection_notifications = YLeaf(YType.uint32, "stop-control-connection-notifications")

                            self.unknown_packets = YLeaf(YType.uint32, "unknown-packets")

                            self.wan_error_notify_packets = YLeaf(YType.uint32, "wan-error-notify-packets")

                            self.zero_length_body_packets = YLeaf(YType.uint32, "zero-length-body-packets")
                            self._segment_path = lambda: "transmit"
                            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/counters/control/tunnel-xr/global/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2Tpv2.Counters.Control.TunnelXr.Global_.Transmit, ['acknowledgement_packets', 'call_disconnect_notify_packets', 'hello_packets', 'incoming_call_connected_packets', 'incoming_call_replies', 'incoming_call_requests', 'outgoing_call_connected_packets', 'outgoing_call_replies', 'outgoing_call_requests', 'service_relay_replies', 'service_relay_requests', 'set_link_info_packets', 'start_control_connection_notifications', 'start_control_connection_replies', 'start_control_connection_requests', 'stop_control_connection_notifications', 'unknown_packets', 'wan_error_notify_packets', 'zero_length_body_packets'], name, value)


            class Tunnels(Entity):
                """
                Table of tunnel IDs of control message counters
                
                .. attribute:: tunnel
                
                	L2TP tunnel control message counters
                	**type**\: list of    :py:class:`Tunnel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tpv2.Counters.Control.Tunnels.Tunnel>`
                
                

                """

                _prefix = 'tunnel-l2tun-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(L2Tpv2.Counters.Control.Tunnels, self).__init__()

                    self.yang_name = "tunnels"
                    self.yang_parent_name = "control"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"tunnel" : ("tunnel", L2Tpv2.Counters.Control.Tunnels.Tunnel)}

                    self.tunnel = YList(self)
                    self._segment_path = lambda: "tunnels"
                    self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/counters/control/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(L2Tpv2.Counters.Control.Tunnels, [], name, value)


                class Tunnel(Entity):
                    """
                    L2TP tunnel control message counters
                    
                    .. attribute:: tunnel_id  <key>
                    
                    	L2TP tunnel ID
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: brief
                    
                    	L2TP control message local and remote addresses
                    	**type**\:   :py:class:`Brief <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tpv2.Counters.Control.Tunnels.Tunnel.Brief>`
                    
                    .. attribute:: global_
                    
                    	Global data
                    	**type**\:   :py:class:`Global_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tpv2.Counters.Control.Tunnels.Tunnel.Global_>`
                    
                    

                    """

                    _prefix = 'tunnel-l2tun-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(L2Tpv2.Counters.Control.Tunnels.Tunnel, self).__init__()

                        self.yang_name = "tunnel"
                        self.yang_parent_name = "tunnels"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"brief" : ("brief", L2Tpv2.Counters.Control.Tunnels.Tunnel.Brief), "global" : ("global_", L2Tpv2.Counters.Control.Tunnels.Tunnel.Global_)}
                        self._child_list_classes = {}

                        self.tunnel_id = YLeaf(YType.int32, "tunnel-id")

                        self.brief = L2Tpv2.Counters.Control.Tunnels.Tunnel.Brief()
                        self.brief.parent = self
                        self._children_name_map["brief"] = "brief"
                        self._children_yang_names.add("brief")

                        self.global_ = L2Tpv2.Counters.Control.Tunnels.Tunnel.Global_()
                        self.global_.parent = self
                        self._children_name_map["global_"] = "global"
                        self._children_yang_names.add("global")
                        self._segment_path = lambda: "tunnel" + "[tunnel-id='" + self.tunnel_id.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/counters/control/tunnels/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2Tpv2.Counters.Control.Tunnels.Tunnel, ['tunnel_id'], name, value)


                    class Brief(Entity):
                        """
                        L2TP control message local and remote addresses
                        
                        .. attribute:: local_address
                        
                        	Local IP address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: remote_address
                        
                        	Remote IP address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: remote_tunnel_id
                        
                        	Remote tunnel ID
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'tunnel-l2tun-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(L2Tpv2.Counters.Control.Tunnels.Tunnel.Brief, self).__init__()

                            self.yang_name = "brief"
                            self.yang_parent_name = "tunnel"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.local_address = YLeaf(YType.str, "local-address")

                            self.remote_address = YLeaf(YType.str, "remote-address")

                            self.remote_tunnel_id = YLeaf(YType.uint32, "remote-tunnel-id")
                            self._segment_path = lambda: "brief"

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2Tpv2.Counters.Control.Tunnels.Tunnel.Brief, ['local_address', 'remote_address', 'remote_tunnel_id'], name, value)


                    class Global_(Entity):
                        """
                        Global data
                        
                        .. attribute:: drop
                        
                        	Drop data
                        	**type**\:   :py:class:`Drop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tpv2.Counters.Control.Tunnels.Tunnel.Global_.Drop>`
                        
                        .. attribute:: received
                        
                        	Received data
                        	**type**\:   :py:class:`Received <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tpv2.Counters.Control.Tunnels.Tunnel.Global_.Received>`
                        
                        .. attribute:: retransmit
                        
                        	Re transmit data
                        	**type**\:   :py:class:`Retransmit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tpv2.Counters.Control.Tunnels.Tunnel.Global_.Retransmit>`
                        
                        .. attribute:: total_drop
                        
                        	Total drop
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: total_received
                        
                        	Total received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: total_retransmit
                        
                        	Total retransmit
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: total_transmit
                        
                        	Total transmit
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: transmit
                        
                        	Transmit data
                        	**type**\:   :py:class:`Transmit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tpv2.Counters.Control.Tunnels.Tunnel.Global_.Transmit>`
                        
                        

                        """

                        _prefix = 'tunnel-l2tun-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(L2Tpv2.Counters.Control.Tunnels.Tunnel.Global_, self).__init__()

                            self.yang_name = "global"
                            self.yang_parent_name = "tunnel"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"drop" : ("drop", L2Tpv2.Counters.Control.Tunnels.Tunnel.Global_.Drop), "received" : ("received", L2Tpv2.Counters.Control.Tunnels.Tunnel.Global_.Received), "retransmit" : ("retransmit", L2Tpv2.Counters.Control.Tunnels.Tunnel.Global_.Retransmit), "transmit" : ("transmit", L2Tpv2.Counters.Control.Tunnels.Tunnel.Global_.Transmit)}
                            self._child_list_classes = {}

                            self.total_drop = YLeaf(YType.uint32, "total-drop")

                            self.total_received = YLeaf(YType.uint32, "total-received")

                            self.total_retransmit = YLeaf(YType.uint32, "total-retransmit")

                            self.total_transmit = YLeaf(YType.uint32, "total-transmit")

                            self.drop = L2Tpv2.Counters.Control.Tunnels.Tunnel.Global_.Drop()
                            self.drop.parent = self
                            self._children_name_map["drop"] = "drop"
                            self._children_yang_names.add("drop")

                            self.received = L2Tpv2.Counters.Control.Tunnels.Tunnel.Global_.Received()
                            self.received.parent = self
                            self._children_name_map["received"] = "received"
                            self._children_yang_names.add("received")

                            self.retransmit = L2Tpv2.Counters.Control.Tunnels.Tunnel.Global_.Retransmit()
                            self.retransmit.parent = self
                            self._children_name_map["retransmit"] = "retransmit"
                            self._children_yang_names.add("retransmit")

                            self.transmit = L2Tpv2.Counters.Control.Tunnels.Tunnel.Global_.Transmit()
                            self.transmit.parent = self
                            self._children_name_map["transmit"] = "transmit"
                            self._children_yang_names.add("transmit")
                            self._segment_path = lambda: "global"

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2Tpv2.Counters.Control.Tunnels.Tunnel.Global_, ['total_drop', 'total_received', 'total_retransmit', 'total_transmit'], name, value)


                        class Drop(Entity):
                            """
                            Drop data
                            
                            .. attribute:: acknowledgement_packets
                            
                            	Packets acknowledgement
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: call_disconnect_notify_packets
                            
                            	Call disconnect notify packets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: hello_packets
                            
                            	Keep alive messages
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: incoming_call_connected_packets
                            
                            	Incoming call connected packets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: incoming_call_replies
                            
                            	Incoming call replies
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: incoming_call_requests
                            
                            	Incoming call requests
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: outgoing_call_connected_packets
                            
                            	Outgoing call connected packets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: outgoing_call_replies
                            
                            	Outgoing call replies
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: outgoing_call_requests
                            
                            	Outgoing call requests
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: service_relay_replies
                            
                            	Service relay reply counts
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: service_relay_requests
                            
                            	Service relay request counts
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: set_link_info_packets
                            
                            	Set link info packets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: start_control_connection_notifications
                            
                            	Start control connection notifications
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: start_control_connection_replies
                            
                            	Start control connection replies
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: start_control_connection_requests
                            
                            	Start control connection requests
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: stop_control_connection_notifications
                            
                            	Stop control connection notifications
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: unknown_packets
                            
                            	Unknown packets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: wan_error_notify_packets
                            
                            	WAN error notify packets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: zero_length_body_packets
                            
                            	Zero length body packets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'tunnel-l2tun-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(L2Tpv2.Counters.Control.Tunnels.Tunnel.Global_.Drop, self).__init__()

                                self.yang_name = "drop"
                                self.yang_parent_name = "global"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.acknowledgement_packets = YLeaf(YType.uint32, "acknowledgement-packets")

                                self.call_disconnect_notify_packets = YLeaf(YType.uint32, "call-disconnect-notify-packets")

                                self.hello_packets = YLeaf(YType.uint32, "hello-packets")

                                self.incoming_call_connected_packets = YLeaf(YType.uint32, "incoming-call-connected-packets")

                                self.incoming_call_replies = YLeaf(YType.uint32, "incoming-call-replies")

                                self.incoming_call_requests = YLeaf(YType.uint32, "incoming-call-requests")

                                self.outgoing_call_connected_packets = YLeaf(YType.uint32, "outgoing-call-connected-packets")

                                self.outgoing_call_replies = YLeaf(YType.uint32, "outgoing-call-replies")

                                self.outgoing_call_requests = YLeaf(YType.uint32, "outgoing-call-requests")

                                self.service_relay_replies = YLeaf(YType.uint32, "service-relay-replies")

                                self.service_relay_requests = YLeaf(YType.uint32, "service-relay-requests")

                                self.set_link_info_packets = YLeaf(YType.uint32, "set-link-info-packets")

                                self.start_control_connection_notifications = YLeaf(YType.uint32, "start-control-connection-notifications")

                                self.start_control_connection_replies = YLeaf(YType.uint32, "start-control-connection-replies")

                                self.start_control_connection_requests = YLeaf(YType.uint32, "start-control-connection-requests")

                                self.stop_control_connection_notifications = YLeaf(YType.uint32, "stop-control-connection-notifications")

                                self.unknown_packets = YLeaf(YType.uint32, "unknown-packets")

                                self.wan_error_notify_packets = YLeaf(YType.uint32, "wan-error-notify-packets")

                                self.zero_length_body_packets = YLeaf(YType.uint32, "zero-length-body-packets")
                                self._segment_path = lambda: "drop"

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2Tpv2.Counters.Control.Tunnels.Tunnel.Global_.Drop, ['acknowledgement_packets', 'call_disconnect_notify_packets', 'hello_packets', 'incoming_call_connected_packets', 'incoming_call_replies', 'incoming_call_requests', 'outgoing_call_connected_packets', 'outgoing_call_replies', 'outgoing_call_requests', 'service_relay_replies', 'service_relay_requests', 'set_link_info_packets', 'start_control_connection_notifications', 'start_control_connection_replies', 'start_control_connection_requests', 'stop_control_connection_notifications', 'unknown_packets', 'wan_error_notify_packets', 'zero_length_body_packets'], name, value)


                        class Received(Entity):
                            """
                            Received data
                            
                            .. attribute:: acknowledgement_packets
                            
                            	Packets acknowledgement
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: call_disconnect_notify_packets
                            
                            	Call disconnect notify packets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: hello_packets
                            
                            	Keep alive messages
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: incoming_call_connected_packets
                            
                            	Incoming call connected packets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: incoming_call_replies
                            
                            	Incoming call replies
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: incoming_call_requests
                            
                            	Incoming call requests
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: outgoing_call_connected_packets
                            
                            	Outgoing call connected packets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: outgoing_call_replies
                            
                            	Outgoing call replies
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: outgoing_call_requests
                            
                            	Outgoing call requests
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: service_relay_replies
                            
                            	Service relay reply counts
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: service_relay_requests
                            
                            	Service relay request counts
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: set_link_info_packets
                            
                            	Set link info packets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: start_control_connection_notifications
                            
                            	Start control connection notifications
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: start_control_connection_replies
                            
                            	Start control connection replies
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: start_control_connection_requests
                            
                            	Start control connection requests
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: stop_control_connection_notifications
                            
                            	Stop control connection notifications
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: unknown_packets
                            
                            	Unknown packets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: wan_error_notify_packets
                            
                            	WAN error notify packets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: zero_length_body_packets
                            
                            	Zero length body packets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'tunnel-l2tun-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(L2Tpv2.Counters.Control.Tunnels.Tunnel.Global_.Received, self).__init__()

                                self.yang_name = "received"
                                self.yang_parent_name = "global"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.acknowledgement_packets = YLeaf(YType.uint32, "acknowledgement-packets")

                                self.call_disconnect_notify_packets = YLeaf(YType.uint32, "call-disconnect-notify-packets")

                                self.hello_packets = YLeaf(YType.uint32, "hello-packets")

                                self.incoming_call_connected_packets = YLeaf(YType.uint32, "incoming-call-connected-packets")

                                self.incoming_call_replies = YLeaf(YType.uint32, "incoming-call-replies")

                                self.incoming_call_requests = YLeaf(YType.uint32, "incoming-call-requests")

                                self.outgoing_call_connected_packets = YLeaf(YType.uint32, "outgoing-call-connected-packets")

                                self.outgoing_call_replies = YLeaf(YType.uint32, "outgoing-call-replies")

                                self.outgoing_call_requests = YLeaf(YType.uint32, "outgoing-call-requests")

                                self.service_relay_replies = YLeaf(YType.uint32, "service-relay-replies")

                                self.service_relay_requests = YLeaf(YType.uint32, "service-relay-requests")

                                self.set_link_info_packets = YLeaf(YType.uint32, "set-link-info-packets")

                                self.start_control_connection_notifications = YLeaf(YType.uint32, "start-control-connection-notifications")

                                self.start_control_connection_replies = YLeaf(YType.uint32, "start-control-connection-replies")

                                self.start_control_connection_requests = YLeaf(YType.uint32, "start-control-connection-requests")

                                self.stop_control_connection_notifications = YLeaf(YType.uint32, "stop-control-connection-notifications")

                                self.unknown_packets = YLeaf(YType.uint32, "unknown-packets")

                                self.wan_error_notify_packets = YLeaf(YType.uint32, "wan-error-notify-packets")

                                self.zero_length_body_packets = YLeaf(YType.uint32, "zero-length-body-packets")
                                self._segment_path = lambda: "received"

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2Tpv2.Counters.Control.Tunnels.Tunnel.Global_.Received, ['acknowledgement_packets', 'call_disconnect_notify_packets', 'hello_packets', 'incoming_call_connected_packets', 'incoming_call_replies', 'incoming_call_requests', 'outgoing_call_connected_packets', 'outgoing_call_replies', 'outgoing_call_requests', 'service_relay_replies', 'service_relay_requests', 'set_link_info_packets', 'start_control_connection_notifications', 'start_control_connection_replies', 'start_control_connection_requests', 'stop_control_connection_notifications', 'unknown_packets', 'wan_error_notify_packets', 'zero_length_body_packets'], name, value)


                        class Retransmit(Entity):
                            """
                            Re transmit data
                            
                            .. attribute:: acknowledgement_packets
                            
                            	Packets acknowledgement
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: call_disconnect_notify_packets
                            
                            	Call disconnect notify packets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: hello_packets
                            
                            	Keep alive messages
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: incoming_call_connected_packets
                            
                            	Incoming call connected packets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: incoming_call_replies
                            
                            	Incoming call replies
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: incoming_call_requests
                            
                            	Incoming call requests
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: outgoing_call_connected_packets
                            
                            	Outgoing call connected packets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: outgoing_call_replies
                            
                            	Outgoing call replies
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: outgoing_call_requests
                            
                            	Outgoing call requests
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: service_relay_replies
                            
                            	Service relay reply counts
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: service_relay_requests
                            
                            	Service relay request counts
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: set_link_info_packets
                            
                            	Set link info packets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: start_control_connection_notifications
                            
                            	Start control connection notifications
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: start_control_connection_replies
                            
                            	Start control connection replies
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: start_control_connection_requests
                            
                            	Start control connection requests
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: stop_control_connection_notifications
                            
                            	Stop control connection notifications
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: unknown_packets
                            
                            	Unknown packets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: wan_error_notify_packets
                            
                            	WAN error notify packets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: zero_length_body_packets
                            
                            	Zero length body packets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'tunnel-l2tun-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(L2Tpv2.Counters.Control.Tunnels.Tunnel.Global_.Retransmit, self).__init__()

                                self.yang_name = "retransmit"
                                self.yang_parent_name = "global"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.acknowledgement_packets = YLeaf(YType.uint32, "acknowledgement-packets")

                                self.call_disconnect_notify_packets = YLeaf(YType.uint32, "call-disconnect-notify-packets")

                                self.hello_packets = YLeaf(YType.uint32, "hello-packets")

                                self.incoming_call_connected_packets = YLeaf(YType.uint32, "incoming-call-connected-packets")

                                self.incoming_call_replies = YLeaf(YType.uint32, "incoming-call-replies")

                                self.incoming_call_requests = YLeaf(YType.uint32, "incoming-call-requests")

                                self.outgoing_call_connected_packets = YLeaf(YType.uint32, "outgoing-call-connected-packets")

                                self.outgoing_call_replies = YLeaf(YType.uint32, "outgoing-call-replies")

                                self.outgoing_call_requests = YLeaf(YType.uint32, "outgoing-call-requests")

                                self.service_relay_replies = YLeaf(YType.uint32, "service-relay-replies")

                                self.service_relay_requests = YLeaf(YType.uint32, "service-relay-requests")

                                self.set_link_info_packets = YLeaf(YType.uint32, "set-link-info-packets")

                                self.start_control_connection_notifications = YLeaf(YType.uint32, "start-control-connection-notifications")

                                self.start_control_connection_replies = YLeaf(YType.uint32, "start-control-connection-replies")

                                self.start_control_connection_requests = YLeaf(YType.uint32, "start-control-connection-requests")

                                self.stop_control_connection_notifications = YLeaf(YType.uint32, "stop-control-connection-notifications")

                                self.unknown_packets = YLeaf(YType.uint32, "unknown-packets")

                                self.wan_error_notify_packets = YLeaf(YType.uint32, "wan-error-notify-packets")

                                self.zero_length_body_packets = YLeaf(YType.uint32, "zero-length-body-packets")
                                self._segment_path = lambda: "retransmit"

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2Tpv2.Counters.Control.Tunnels.Tunnel.Global_.Retransmit, ['acknowledgement_packets', 'call_disconnect_notify_packets', 'hello_packets', 'incoming_call_connected_packets', 'incoming_call_replies', 'incoming_call_requests', 'outgoing_call_connected_packets', 'outgoing_call_replies', 'outgoing_call_requests', 'service_relay_replies', 'service_relay_requests', 'set_link_info_packets', 'start_control_connection_notifications', 'start_control_connection_replies', 'start_control_connection_requests', 'stop_control_connection_notifications', 'unknown_packets', 'wan_error_notify_packets', 'zero_length_body_packets'], name, value)


                        class Transmit(Entity):
                            """
                            Transmit data
                            
                            .. attribute:: acknowledgement_packets
                            
                            	Packets acknowledgement
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: call_disconnect_notify_packets
                            
                            	Call disconnect notify packets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: hello_packets
                            
                            	Keep alive messages
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: incoming_call_connected_packets
                            
                            	Incoming call connected packets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: incoming_call_replies
                            
                            	Incoming call replies
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: incoming_call_requests
                            
                            	Incoming call requests
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: outgoing_call_connected_packets
                            
                            	Outgoing call connected packets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: outgoing_call_replies
                            
                            	Outgoing call replies
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: outgoing_call_requests
                            
                            	Outgoing call requests
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: service_relay_replies
                            
                            	Service relay reply counts
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: service_relay_requests
                            
                            	Service relay request counts
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: set_link_info_packets
                            
                            	Set link info packets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: start_control_connection_notifications
                            
                            	Start control connection notifications
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: start_control_connection_replies
                            
                            	Start control connection replies
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: start_control_connection_requests
                            
                            	Start control connection requests
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: stop_control_connection_notifications
                            
                            	Stop control connection notifications
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: unknown_packets
                            
                            	Unknown packets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: wan_error_notify_packets
                            
                            	WAN error notify packets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: zero_length_body_packets
                            
                            	Zero length body packets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'tunnel-l2tun-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(L2Tpv2.Counters.Control.Tunnels.Tunnel.Global_.Transmit, self).__init__()

                                self.yang_name = "transmit"
                                self.yang_parent_name = "global"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.acknowledgement_packets = YLeaf(YType.uint32, "acknowledgement-packets")

                                self.call_disconnect_notify_packets = YLeaf(YType.uint32, "call-disconnect-notify-packets")

                                self.hello_packets = YLeaf(YType.uint32, "hello-packets")

                                self.incoming_call_connected_packets = YLeaf(YType.uint32, "incoming-call-connected-packets")

                                self.incoming_call_replies = YLeaf(YType.uint32, "incoming-call-replies")

                                self.incoming_call_requests = YLeaf(YType.uint32, "incoming-call-requests")

                                self.outgoing_call_connected_packets = YLeaf(YType.uint32, "outgoing-call-connected-packets")

                                self.outgoing_call_replies = YLeaf(YType.uint32, "outgoing-call-replies")

                                self.outgoing_call_requests = YLeaf(YType.uint32, "outgoing-call-requests")

                                self.service_relay_replies = YLeaf(YType.uint32, "service-relay-replies")

                                self.service_relay_requests = YLeaf(YType.uint32, "service-relay-requests")

                                self.set_link_info_packets = YLeaf(YType.uint32, "set-link-info-packets")

                                self.start_control_connection_notifications = YLeaf(YType.uint32, "start-control-connection-notifications")

                                self.start_control_connection_replies = YLeaf(YType.uint32, "start-control-connection-replies")

                                self.start_control_connection_requests = YLeaf(YType.uint32, "start-control-connection-requests")

                                self.stop_control_connection_notifications = YLeaf(YType.uint32, "stop-control-connection-notifications")

                                self.unknown_packets = YLeaf(YType.uint32, "unknown-packets")

                                self.wan_error_notify_packets = YLeaf(YType.uint32, "wan-error-notify-packets")

                                self.zero_length_body_packets = YLeaf(YType.uint32, "zero-length-body-packets")
                                self._segment_path = lambda: "transmit"

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2Tpv2.Counters.Control.Tunnels.Tunnel.Global_.Transmit, ['acknowledgement_packets', 'call_disconnect_notify_packets', 'hello_packets', 'incoming_call_connected_packets', 'incoming_call_replies', 'incoming_call_requests', 'outgoing_call_connected_packets', 'outgoing_call_replies', 'outgoing_call_requests', 'service_relay_replies', 'service_relay_requests', 'set_link_info_packets', 'start_control_connection_notifications', 'start_control_connection_replies', 'start_control_connection_requests', 'stop_control_connection_notifications', 'unknown_packets', 'wan_error_notify_packets', 'zero_length_body_packets'], name, value)


        class Forwarding(Entity):
            """
            L2TP forwarding messages counters
            
            .. attribute:: sessions
            
            	List of class and session IDs
            	**type**\:   :py:class:`Sessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tpv2.Counters.Forwarding.Sessions>`
            
            

            """

            _prefix = 'tunnel-l2tun-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(L2Tpv2.Counters.Forwarding, self).__init__()

                self.yang_name = "forwarding"
                self.yang_parent_name = "counters"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"sessions" : ("sessions", L2Tpv2.Counters.Forwarding.Sessions)}
                self._child_list_classes = {}

                self.sessions = L2Tpv2.Counters.Forwarding.Sessions()
                self.sessions.parent = self
                self._children_name_map["sessions"] = "sessions"
                self._children_yang_names.add("sessions")
                self._segment_path = lambda: "forwarding"
                self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/counters/%s" % self._segment_path()


            class Sessions(Entity):
                """
                List of class and session IDs
                
                .. attribute:: session
                
                	L2TP information for a particular session
                	**type**\: list of    :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tpv2.Counters.Forwarding.Sessions.Session>`
                
                

                """

                _prefix = 'tunnel-l2tun-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(L2Tpv2.Counters.Forwarding.Sessions, self).__init__()

                    self.yang_name = "sessions"
                    self.yang_parent_name = "forwarding"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"session" : ("session", L2Tpv2.Counters.Forwarding.Sessions.Session)}

                    self.session = YList(self)
                    self._segment_path = lambda: "sessions"
                    self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/counters/forwarding/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(L2Tpv2.Counters.Forwarding.Sessions, [], name, value)


                class Session(Entity):
                    """
                    L2TP information for a particular session
                    
                    .. attribute:: tunnel_id  <key>
                    
                    	Local tunnel ID
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: session_id  <key>
                    
                    	Local session ID
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: in_bytes
                    
                    	Number of bytes sent in
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: byte
                    
                    .. attribute:: in_packets
                    
                    	Number of packets sent in
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: out_bytes
                    
                    	Number of bytes sent out
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: byte
                    
                    .. attribute:: out_packets
                    
                    	Number of packets sent out
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: remote_session_id
                    
                    	Remote session ID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'tunnel-l2tun-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(L2Tpv2.Counters.Forwarding.Sessions.Session, self).__init__()

                        self.yang_name = "session"
                        self.yang_parent_name = "sessions"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.tunnel_id = YLeaf(YType.int32, "tunnel-id")

                        self.session_id = YLeaf(YType.int32, "session-id")

                        self.in_bytes = YLeaf(YType.uint64, "in-bytes")

                        self.in_packets = YLeaf(YType.uint64, "in-packets")

                        self.out_bytes = YLeaf(YType.uint64, "out-bytes")

                        self.out_packets = YLeaf(YType.uint64, "out-packets")

                        self.remote_session_id = YLeaf(YType.uint32, "remote-session-id")
                        self._segment_path = lambda: "session" + "[tunnel-id='" + self.tunnel_id.get() + "']" + "[session-id='" + self.session_id.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/counters/forwarding/sessions/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2Tpv2.Counters.Forwarding.Sessions.Session, ['tunnel_id', 'session_id', 'in_bytes', 'in_packets', 'out_bytes', 'out_packets', 'remote_session_id'], name, value)


    class Session(Entity):
        """
        L2TP control messages counters
        
        .. attribute:: unavailable
        
        	L2TP session unavailable  information
        	**type**\:   :py:class:`Unavailable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tpv2.Session.Unavailable>`
        
        

        """

        _prefix = 'tunnel-l2tun-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(L2Tpv2.Session, self).__init__()

            self.yang_name = "session"
            self.yang_parent_name = "l2tpv2"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"unavailable" : ("unavailable", L2Tpv2.Session.Unavailable)}
            self._child_list_classes = {}

            self.unavailable = L2Tpv2.Session.Unavailable()
            self.unavailable.parent = self
            self._children_name_map["unavailable"] = "unavailable"
            self._children_yang_names.add("unavailable")
            self._segment_path = lambda: "session"
            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/%s" % self._segment_path()


        class Unavailable(Entity):
            """
            L2TP session unavailable  information
            
            .. attribute:: sessions_on_hold
            
            	Number of session ID in hold database
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'tunnel-l2tun-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(L2Tpv2.Session.Unavailable, self).__init__()

                self.yang_name = "unavailable"
                self.yang_parent_name = "session"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.sessions_on_hold = YLeaf(YType.uint32, "sessions-on-hold")
                self._segment_path = lambda: "unavailable"
                self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/session/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(L2Tpv2.Session.Unavailable, ['sessions_on_hold'], name, value)


    class Sessions(Entity):
        """
        List of session IDs
        
        .. attribute:: session
        
        	L2TP information for a particular session
        	**type**\: list of    :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tpv2.Sessions.Session>`
        
        

        """

        _prefix = 'tunnel-l2tun-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(L2Tpv2.Sessions, self).__init__()

            self.yang_name = "sessions"
            self.yang_parent_name = "l2tpv2"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"session" : ("session", L2Tpv2.Sessions.Session)}

            self.session = YList(self)
            self._segment_path = lambda: "sessions"
            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(L2Tpv2.Sessions, [], name, value)


        class Session(Entity):
            """
            L2TP information for a particular session
            
            .. attribute:: local_tunnel_id  <key>
            
            	Local tunnel ID
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: local_session_id  <key>
            
            	Local session ID
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: call_serial_number
            
            	Call serial number
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: interface_name
            
            	Interface name
            	**type**\:  str
            
            	**length:** 0..256
            
            .. attribute:: is_conditional_debug_enabled
            
            	True if conditional debugging is enabled
            	**type**\:  bool
            
            .. attribute:: is_sequencing_on
            
            	True if session sequence is on
            	**type**\:  bool
            
            .. attribute:: is_session_locally_initiated
            
            	True if session initiated locally
            	**type**\:  bool
            
            .. attribute:: is_session_manual
            
            	True if session is manual
            	**type**\:  bool
            
            .. attribute:: is_session_state_established
            
            	True if session state is established
            	**type**\:  bool
            
            .. attribute:: is_session_up
            
            	True if session is up
            	**type**\:  bool
            
            .. attribute:: is_udp_checksum_enabled
            
            	True if UDP checksum enabled
            	**type**\:  bool
            
            .. attribute:: l2tp_sh_sess_tie_breaker
            
            	l2tp sh sess tie breaker
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: l2tp_sh_sess_tie_breaker_enabled
            
            	l2tp sh sess tie breaker enabled
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: l2tp_sh_sess_udp_lport
            
            	l2tp sh sess udp lport
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: l2tp_sh_sess_udp_rport
            
            	l2tp sh sess udp rport
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: local_ip_address
            
            	Local session IP address
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: local_tunnel_name
            
            	Local tunnel name
            	**type**\:  str
            
            	**length:** 0..256
            
            .. attribute:: protocol
            
            	Protocol
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: remote_ip_address
            
            	Remote session IP address
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: remote_session_id
            
            	Remote session ID
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: remote_tunnel_id
            
            	Remote tunnel ID
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: remote_tunnel_name
            
            	Remote tunnel name
            	**type**\:  str
            
            	**length:** 0..256
            
            .. attribute:: session_application_data
            
            	Session application data
            	**type**\:   :py:class:`SessionApplicationData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tpv2.Sessions.Session.SessionApplicationData>`
            
            .. attribute:: unique_id
            
            	Unique ID
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'tunnel-l2tun-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(L2Tpv2.Sessions.Session, self).__init__()

                self.yang_name = "session"
                self.yang_parent_name = "sessions"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"session-application-data" : ("session_application_data", L2Tpv2.Sessions.Session.SessionApplicationData)}
                self._child_list_classes = {}

                self.local_tunnel_id = YLeaf(YType.int32, "local-tunnel-id")

                self.local_session_id = YLeaf(YType.int32, "local-session-id")

                self.call_serial_number = YLeaf(YType.uint32, "call-serial-number")

                self.interface_name = YLeaf(YType.str, "interface-name")

                self.is_conditional_debug_enabled = YLeaf(YType.boolean, "is-conditional-debug-enabled")

                self.is_sequencing_on = YLeaf(YType.boolean, "is-sequencing-on")

                self.is_session_locally_initiated = YLeaf(YType.boolean, "is-session-locally-initiated")

                self.is_session_manual = YLeaf(YType.boolean, "is-session-manual")

                self.is_session_state_established = YLeaf(YType.boolean, "is-session-state-established")

                self.is_session_up = YLeaf(YType.boolean, "is-session-up")

                self.is_udp_checksum_enabled = YLeaf(YType.boolean, "is-udp-checksum-enabled")

                self.l2tp_sh_sess_tie_breaker = YLeaf(YType.uint64, "l2tp-sh-sess-tie-breaker")

                self.l2tp_sh_sess_tie_breaker_enabled = YLeaf(YType.uint8, "l2tp-sh-sess-tie-breaker-enabled")

                self.l2tp_sh_sess_udp_lport = YLeaf(YType.uint16, "l2tp-sh-sess-udp-lport")

                self.l2tp_sh_sess_udp_rport = YLeaf(YType.uint16, "l2tp-sh-sess-udp-rport")

                self.local_ip_address = YLeaf(YType.str, "local-ip-address")

                self.local_tunnel_name = YLeaf(YType.str, "local-tunnel-name")

                self.protocol = YLeaf(YType.uint8, "protocol")

                self.remote_ip_address = YLeaf(YType.str, "remote-ip-address")

                self.remote_session_id = YLeaf(YType.uint32, "remote-session-id")

                self.remote_tunnel_id = YLeaf(YType.uint32, "remote-tunnel-id")

                self.remote_tunnel_name = YLeaf(YType.str, "remote-tunnel-name")

                self.unique_id = YLeaf(YType.uint32, "unique-id")

                self.session_application_data = L2Tpv2.Sessions.Session.SessionApplicationData()
                self.session_application_data.parent = self
                self._children_name_map["session_application_data"] = "session-application-data"
                self._children_yang_names.add("session-application-data")
                self._segment_path = lambda: "session" + "[local-tunnel-id='" + self.local_tunnel_id.get() + "']" + "[local-session-id='" + self.local_session_id.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/sessions/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(L2Tpv2.Sessions.Session, ['local_tunnel_id', 'local_session_id', 'call_serial_number', 'interface_name', 'is_conditional_debug_enabled', 'is_sequencing_on', 'is_session_locally_initiated', 'is_session_manual', 'is_session_state_established', 'is_session_up', 'is_udp_checksum_enabled', 'l2tp_sh_sess_tie_breaker', 'l2tp_sh_sess_tie_breaker_enabled', 'l2tp_sh_sess_udp_lport', 'l2tp_sh_sess_udp_rport', 'local_ip_address', 'local_tunnel_name', 'protocol', 'remote_ip_address', 'remote_session_id', 'remote_tunnel_id', 'remote_tunnel_name', 'unique_id'], name, value)


            class SessionApplicationData(Entity):
                """
                Session application data
                
                .. attribute:: l2tp_sh_sess_app_type
                
                	l2tp sh sess app type
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: vpdn
                
                	VPDN data
                	**type**\:   :py:class:`Vpdn <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tpv2.Sessions.Session.SessionApplicationData.Vpdn>`
                
                .. attribute:: xconnect
                
                	Xconnect data
                	**type**\:   :py:class:`Xconnect <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tpv2.Sessions.Session.SessionApplicationData.Xconnect>`
                
                

                """

                _prefix = 'tunnel-l2tun-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(L2Tpv2.Sessions.Session.SessionApplicationData, self).__init__()

                    self.yang_name = "session-application-data"
                    self.yang_parent_name = "session"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"vpdn" : ("vpdn", L2Tpv2.Sessions.Session.SessionApplicationData.Vpdn), "xconnect" : ("xconnect", L2Tpv2.Sessions.Session.SessionApplicationData.Xconnect)}
                    self._child_list_classes = {}

                    self.l2tp_sh_sess_app_type = YLeaf(YType.uint32, "l2tp-sh-sess-app-type")

                    self.vpdn = L2Tpv2.Sessions.Session.SessionApplicationData.Vpdn()
                    self.vpdn.parent = self
                    self._children_name_map["vpdn"] = "vpdn"
                    self._children_yang_names.add("vpdn")

                    self.xconnect = L2Tpv2.Sessions.Session.SessionApplicationData.Xconnect()
                    self.xconnect.parent = self
                    self._children_name_map["xconnect"] = "xconnect"
                    self._children_yang_names.add("xconnect")
                    self._segment_path = lambda: "session-application-data"

                def __setattr__(self, name, value):
                    self._perform_setattr(L2Tpv2.Sessions.Session.SessionApplicationData, ['l2tp_sh_sess_app_type'], name, value)


                class Vpdn(Entity):
                    """
                    VPDN data
                    
                    .. attribute:: interface_name
                    
                    	Interface name
                    	**type**\:  str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
                    .. attribute:: username
                    
                    	Session username
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'tunnel-l2tun-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(L2Tpv2.Sessions.Session.SessionApplicationData.Vpdn, self).__init__()

                        self.yang_name = "vpdn"
                        self.yang_parent_name = "session-application-data"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.username = YLeaf(YType.str, "username")
                        self._segment_path = lambda: "vpdn"

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2Tpv2.Sessions.Session.SessionApplicationData.Vpdn, ['interface_name', 'username'], name, value)


                class Xconnect(Entity):
                    """
                    Xconnect data
                    
                    .. attribute:: circuit_name
                    
                    	Circuit name
                    	**type**\:  str
                    
                    .. attribute:: ipv6_protocol_tunneling
                    
                    	IPv6ProtocolTunneling
                    	**type**\:  bool
                    
                    .. attribute:: is_circuit_state_up
                    
                    	True if circuit state is up
                    	**type**\:  bool
                    
                    .. attribute:: is_local_circuit_state_up
                    
                    	True if local circuit state is up
                    	**type**\:  bool
                    
                    .. attribute:: is_remote_circuit_state_up
                    
                    	True if remote circuit state is up
                    	**type**\:  bool
                    
                    .. attribute:: sessionvc_id
                    
                    	Session VC ID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'tunnel-l2tun-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(L2Tpv2.Sessions.Session.SessionApplicationData.Xconnect, self).__init__()

                        self.yang_name = "xconnect"
                        self.yang_parent_name = "session-application-data"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.circuit_name = YLeaf(YType.str, "circuit-name")

                        self.ipv6_protocol_tunneling = YLeaf(YType.boolean, "ipv6-protocol-tunneling")

                        self.is_circuit_state_up = YLeaf(YType.boolean, "is-circuit-state-up")

                        self.is_local_circuit_state_up = YLeaf(YType.boolean, "is-local-circuit-state-up")

                        self.is_remote_circuit_state_up = YLeaf(YType.boolean, "is-remote-circuit-state-up")

                        self.sessionvc_id = YLeaf(YType.uint32, "sessionvc-id")
                        self._segment_path = lambda: "xconnect"

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2Tpv2.Sessions.Session.SessionApplicationData.Xconnect, ['circuit_name', 'ipv6_protocol_tunneling', 'is_circuit_state_up', 'is_local_circuit_state_up', 'is_remote_circuit_state_up', 'sessionvc_id'], name, value)


    class Statistics(Entity):
        """
        L2TP v2 statistics information
        
        .. attribute:: average_packet_processing_time
        
        	Average processing time for received packets  (in micro seconds)
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: microsecond
        
        .. attribute:: buffered_packets
        
        	Bufferred packets
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: incoming_dropped_packets
        
        	In coming packets dropped
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: netio_packets
        
        	Packets RX in netio
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: received_out_of_order_packets
        
        	Out of order packets received
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: received_packets
        
        	Number of packets received
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: reorder_deviation_packets
        
        	Re order deviation
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: reorder_packets
        
        	Re order packets
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: sent_packets
        
        	Number of packets sent
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: sessions
        
        	Number of sessions
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: tunnels
        
        	Number of tunnels
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'tunnel-l2tun-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(L2Tpv2.Statistics, self).__init__()

            self.yang_name = "statistics"
            self.yang_parent_name = "l2tpv2"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.average_packet_processing_time = YLeaf(YType.uint32, "average-packet-processing-time")

            self.buffered_packets = YLeaf(YType.uint32, "buffered-packets")

            self.incoming_dropped_packets = YLeaf(YType.uint32, "incoming-dropped-packets")

            self.netio_packets = YLeaf(YType.uint32, "netio-packets")

            self.received_out_of_order_packets = YLeaf(YType.uint32, "received-out-of-order-packets")

            self.received_packets = YLeaf(YType.uint32, "received-packets")

            self.reorder_deviation_packets = YLeaf(YType.uint32, "reorder-deviation-packets")

            self.reorder_packets = YLeaf(YType.uint32, "reorder-packets")

            self.sent_packets = YLeaf(YType.uint32, "sent-packets")

            self.sessions = YLeaf(YType.uint32, "sessions")

            self.tunnels = YLeaf(YType.uint32, "tunnels")
            self._segment_path = lambda: "statistics"
            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(L2Tpv2.Statistics, ['average_packet_processing_time', 'buffered_packets', 'incoming_dropped_packets', 'netio_packets', 'received_out_of_order_packets', 'received_packets', 'reorder_deviation_packets', 'reorder_packets', 'sent_packets', 'sessions', 'tunnels'], name, value)


    class Tunnel(Entity):
        """
        L2TPv2 tunnel 
        
        .. attribute:: accounting
        
        	Tunnel accounting counters
        	**type**\:   :py:class:`Accounting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tpv2.Tunnel.Accounting>`
        
        

        """

        _prefix = 'tunnel-l2tun-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(L2Tpv2.Tunnel, self).__init__()

            self.yang_name = "tunnel"
            self.yang_parent_name = "l2tpv2"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"accounting" : ("accounting", L2Tpv2.Tunnel.Accounting)}
            self._child_list_classes = {}

            self.accounting = L2Tpv2.Tunnel.Accounting()
            self.accounting.parent = self
            self._children_name_map["accounting"] = "accounting"
            self._children_yang_names.add("accounting")
            self._segment_path = lambda: "tunnel"
            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/%s" % self._segment_path()


        class Accounting(Entity):
            """
            Tunnel accounting counters
            
            .. attribute:: statistics
            
            	Tunnel accounting statistics
            	**type**\:   :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tpv2.Tunnel.Accounting.Statistics>`
            
            

            """

            _prefix = 'tunnel-l2tun-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(L2Tpv2.Tunnel.Accounting, self).__init__()

                self.yang_name = "accounting"
                self.yang_parent_name = "tunnel"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"statistics" : ("statistics", L2Tpv2.Tunnel.Accounting.Statistics)}
                self._child_list_classes = {}

                self.statistics = L2Tpv2.Tunnel.Accounting.Statistics()
                self.statistics.parent = self
                self._children_name_map["statistics"] = "statistics"
                self._children_yang_names.add("statistics")
                self._segment_path = lambda: "accounting"
                self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/tunnel/%s" % self._segment_path()


            class Statistics(Entity):
                """
                Tunnel accounting statistics
                
                .. attribute:: current_size
                
                	Current checkpoint size
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: memory_failures
                
                	Memory failures
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: negative_acknowledgement
                
                	Negative acknowledgement
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: positive_acknowledgement
                
                	Positive acknowledgement
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: queue_statistics_size
                
                	Queue statistics size
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: records_checkpointed
                
                	Total records checkpointed
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: records_fail_to_recover
                
                	Records fail to recover
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: records_failed_to_checkpoint
                
                	Records fail to checkpoint
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: records_recovered_from_checkpoint
                
                	Records recovered from checkpoint
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: records_sent_from_queue
                
                	Records sent from queue
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: records_sent_successfully
                
                	Accounting records sent successfully
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: reject
                
                	Accounting reject
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: start
                
                	Accounting start
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: stop
                
                	Accounting stop
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: transport_failures
                
                	Transport failures
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'tunnel-l2tun-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(L2Tpv2.Tunnel.Accounting.Statistics, self).__init__()

                    self.yang_name = "statistics"
                    self.yang_parent_name = "accounting"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.current_size = YLeaf(YType.uint32, "current-size")

                    self.memory_failures = YLeaf(YType.uint32, "memory-failures")

                    self.negative_acknowledgement = YLeaf(YType.uint64, "negative-acknowledgement")

                    self.positive_acknowledgement = YLeaf(YType.uint64, "positive-acknowledgement")

                    self.queue_statistics_size = YLeaf(YType.int32, "queue-statistics-size")

                    self.records_checkpointed = YLeaf(YType.uint64, "records-checkpointed")

                    self.records_fail_to_recover = YLeaf(YType.uint32, "records-fail-to-recover")

                    self.records_failed_to_checkpoint = YLeaf(YType.uint64, "records-failed-to-checkpoint")

                    self.records_recovered_from_checkpoint = YLeaf(YType.uint32, "records-recovered-from-checkpoint")

                    self.records_sent_from_queue = YLeaf(YType.uint64, "records-sent-from-queue")

                    self.records_sent_successfully = YLeaf(YType.uint64, "records-sent-successfully")

                    self.reject = YLeaf(YType.uint64, "reject")

                    self.start = YLeaf(YType.uint64, "start")

                    self.stop = YLeaf(YType.uint64, "stop")

                    self.transport_failures = YLeaf(YType.uint64, "transport-failures")
                    self._segment_path = lambda: "statistics"
                    self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/tunnel/accounting/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(L2Tpv2.Tunnel.Accounting.Statistics, ['current_size', 'memory_failures', 'negative_acknowledgement', 'positive_acknowledgement', 'queue_statistics_size', 'records_checkpointed', 'records_fail_to_recover', 'records_failed_to_checkpoint', 'records_recovered_from_checkpoint', 'records_sent_from_queue', 'records_sent_successfully', 'reject', 'start', 'stop', 'transport_failures'], name, value)


    class TunnelConfigurations(Entity):
        """
        List of tunnel IDs
        
        .. attribute:: tunnel_configuration
        
        	L2TP tunnel information
        	**type**\: list of    :py:class:`TunnelConfiguration <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tpv2.TunnelConfigurations.TunnelConfiguration>`
        
        

        """

        _prefix = 'tunnel-l2tun-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(L2Tpv2.TunnelConfigurations, self).__init__()

            self.yang_name = "tunnel-configurations"
            self.yang_parent_name = "l2tpv2"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"tunnel-configuration" : ("tunnel_configuration", L2Tpv2.TunnelConfigurations.TunnelConfiguration)}

            self.tunnel_configuration = YList(self)
            self._segment_path = lambda: "tunnel-configurations"
            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(L2Tpv2.TunnelConfigurations, [], name, value)


        class TunnelConfiguration(Entity):
            """
            L2TP tunnel information
            
            .. attribute:: local_tunnel_id  <key>
            
            	Local tunnel ID
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: l2tp_class
            
            	L2Tp class data
            	**type**\:   :py:class:`L2TpClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tpv2.TunnelConfigurations.TunnelConfiguration.L2TpClass>`
            
            .. attribute:: remote_tunnel_id
            
            	Remote tunnel ID
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'tunnel-l2tun-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(L2Tpv2.TunnelConfigurations.TunnelConfiguration, self).__init__()

                self.yang_name = "tunnel-configuration"
                self.yang_parent_name = "tunnel-configurations"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"l2tp-class" : ("l2tp_class", L2Tpv2.TunnelConfigurations.TunnelConfiguration.L2TpClass)}
                self._child_list_classes = {}

                self.local_tunnel_id = YLeaf(YType.int32, "local-tunnel-id")

                self.remote_tunnel_id = YLeaf(YType.uint32, "remote-tunnel-id")

                self.l2tp_class = L2Tpv2.TunnelConfigurations.TunnelConfiguration.L2TpClass()
                self.l2tp_class.parent = self
                self._children_name_map["l2tp_class"] = "l2tp-class"
                self._children_yang_names.add("l2tp-class")
                self._segment_path = lambda: "tunnel-configuration" + "[local-tunnel-id='" + self.local_tunnel_id.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/tunnel-configurations/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(L2Tpv2.TunnelConfigurations.TunnelConfiguration, ['local_tunnel_id', 'remote_tunnel_id'], name, value)


            class L2TpClass(Entity):
                """
                L2Tp class data
                
                .. attribute:: accounting_method_list
                
                	Accounting List
                	**type**\:  str
                
                	**length:** 0..256
                
                .. attribute:: class_name_xr
                
                	Class name
                	**type**\:  str
                
                	**length:** 0..256
                
                .. attribute:: digest_hash
                
                	Hash configured as MD5 or SHA1
                	**type**\:   :py:class:`DigestHash <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.DigestHash>`
                
                .. attribute:: encoded_password
                
                	Encoded password
                	**type**\:  str
                
                	**length:** 0..256
                
                .. attribute:: hello_timeout
                
                	Hello timeout value in seconds
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: host_name
                
                	Host name
                	**type**\:  str
                
                	**length:** 0..256
                
                .. attribute:: initial_retransmit_maximum_timeout
                
                	Initial timeout maximum in seconds
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: initial_retransmit_minimum_timeout
                
                	Initial timeout minimum in seconds
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: initial_retransmit_retries
                
                	Initial retransmit retries
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: ip_tos
                
                	IP TOS
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: is_authentication_enabled
                
                	True if authentication is enabled
                	**type**\:  bool
                
                .. attribute:: is_congestion_control_enabled
                
                	True if congestion control is enabled
                	**type**\:  bool
                
                .. attribute:: is_digest_check_enabled
                
                	True if digest check is enabled
                	**type**\:  bool
                
                .. attribute:: is_digest_enabled
                
                	True if digest authentication is enabled
                	**type**\:  bool
                
                .. attribute:: is_hidden
                
                	True if class is hidden
                	**type**\:  bool
                
                .. attribute:: is_peer_address_checked
                
                	True if peer address is checked
                	**type**\:  bool
                
                .. attribute:: password
                
                	Password
                	**type**\:  str
                
                	**length:** 0..25
                
                .. attribute:: receive_window_size
                
                	Receive window size
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: retransmit_maximum_timeout
                
                	Retransmit maximum timeout in seconds
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: retransmit_minimum_timeout
                
                	Retransmit minimum timeout in seconds
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: retransmit_retries
                
                	Retransmit retries
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: setup_timeout
                
                	Timeout setup value in seconds
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: timeout_no_user
                
                	Timeout no user
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: vrf_name
                
                	VRF name
                	**type**\:  str
                
                	**length:** 0..256
                
                

                """

                _prefix = 'tunnel-l2tun-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(L2Tpv2.TunnelConfigurations.TunnelConfiguration.L2TpClass, self).__init__()

                    self.yang_name = "l2tp-class"
                    self.yang_parent_name = "tunnel-configuration"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.accounting_method_list = YLeaf(YType.str, "accounting-method-list")

                    self.class_name_xr = YLeaf(YType.str, "class-name-xr")

                    self.digest_hash = YLeaf(YType.enumeration, "digest-hash")

                    self.encoded_password = YLeaf(YType.str, "encoded-password")

                    self.hello_timeout = YLeaf(YType.uint32, "hello-timeout")

                    self.host_name = YLeaf(YType.str, "host-name")

                    self.initial_retransmit_maximum_timeout = YLeaf(YType.uint32, "initial-retransmit-maximum-timeout")

                    self.initial_retransmit_minimum_timeout = YLeaf(YType.uint32, "initial-retransmit-minimum-timeout")

                    self.initial_retransmit_retries = YLeaf(YType.uint32, "initial-retransmit-retries")

                    self.ip_tos = YLeaf(YType.uint8, "ip-tos")

                    self.is_authentication_enabled = YLeaf(YType.boolean, "is-authentication-enabled")

                    self.is_congestion_control_enabled = YLeaf(YType.boolean, "is-congestion-control-enabled")

                    self.is_digest_check_enabled = YLeaf(YType.boolean, "is-digest-check-enabled")

                    self.is_digest_enabled = YLeaf(YType.boolean, "is-digest-enabled")

                    self.is_hidden = YLeaf(YType.boolean, "is-hidden")

                    self.is_peer_address_checked = YLeaf(YType.boolean, "is-peer-address-checked")

                    self.password = YLeaf(YType.str, "password")

                    self.receive_window_size = YLeaf(YType.uint16, "receive-window-size")

                    self.retransmit_maximum_timeout = YLeaf(YType.uint32, "retransmit-maximum-timeout")

                    self.retransmit_minimum_timeout = YLeaf(YType.uint32, "retransmit-minimum-timeout")

                    self.retransmit_retries = YLeaf(YType.uint32, "retransmit-retries")

                    self.setup_timeout = YLeaf(YType.uint32, "setup-timeout")

                    self.timeout_no_user = YLeaf(YType.uint32, "timeout-no-user")

                    self.vrf_name = YLeaf(YType.str, "vrf-name")
                    self._segment_path = lambda: "l2tp-class"

                def __setattr__(self, name, value):
                    self._perform_setattr(L2Tpv2.TunnelConfigurations.TunnelConfiguration.L2TpClass, ['accounting_method_list', 'class_name_xr', 'digest_hash', 'encoded_password', 'hello_timeout', 'host_name', 'initial_retransmit_maximum_timeout', 'initial_retransmit_minimum_timeout', 'initial_retransmit_retries', 'ip_tos', 'is_authentication_enabled', 'is_congestion_control_enabled', 'is_digest_check_enabled', 'is_digest_enabled', 'is_hidden', 'is_peer_address_checked', 'password', 'receive_window_size', 'retransmit_maximum_timeout', 'retransmit_minimum_timeout', 'retransmit_retries', 'setup_timeout', 'timeout_no_user', 'vrf_name'], name, value)


    class Tunnels(Entity):
        """
        List of tunnel IDs
        
        .. attribute:: tunnel
        
        	L2TP tunnel  information
        	**type**\: list of    :py:class:`Tunnel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tpv2.Tunnels.Tunnel>`
        
        

        """

        _prefix = 'tunnel-l2tun-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(L2Tpv2.Tunnels, self).__init__()

            self.yang_name = "tunnels"
            self.yang_parent_name = "l2tpv2"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"tunnel" : ("tunnel", L2Tpv2.Tunnels.Tunnel)}

            self.tunnel = YList(self)
            self._segment_path = lambda: "tunnels"
            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(L2Tpv2.Tunnels, [], name, value)


        class Tunnel(Entity):
            """
            L2TP tunnel  information
            
            .. attribute:: local_tunnel_id  <key>
            
            	Local tunnel ID
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: active_sessions
            
            	Number of active sessions
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: class_name
            
            	L2TP class name
            	**type**\:  str
            
            	**length:** 0..256
            
            .. attribute:: digest_secrets
            
            	Control message authentication with digest secrets
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: is_congestion_control_enabled
            
            	True if congestion control is enabled else false
            	**type**\:  bool
            
            .. attribute:: is_pmtu_enabled
            
            	True if tunnel PMTU checking is enabled
            	**type**\:  bool
            
            .. attribute:: is_tunnel_up
            
            	True if tunnel is up
            	**type**\:  bool
            
            .. attribute:: local_address
            
            	Local tunnel address
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: local_port
            
            	Local port
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: local_tunnel_name
            
            	Local tunnel name
            	**type**\:  str
            
            	**length:** 0..256
            
            .. attribute:: local_window_size
            
            	Local window size
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: maximum_retransmission_time
            
            	Maximum retransmission time in seconds
            	**type**\:  int
            
            	**range:** 0..65535
            
            	**units**\: second
            
            .. attribute:: order_queue_size
            
            	Order queue size
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: packet_queue_check
            
            	Current number session packet queue check
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: protocol
            
            	Protocol
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: remote_address
            
            	Remote tunnel address
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: remote_port
            
            	Remote port
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: remote_tunnel_id
            
            	Remote tunnel ID
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: remote_tunnel_name
            
            	Remote tunnel name
            	**type**\:  str
            
            	**length:** 0..256
            
            .. attribute:: remote_window_size
            
            	Remote window size
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: resend_maximum_queue_size
            
            	Resend maximum queue size
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: resend_queue_size
            
            	Resend queue size
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: resends
            
            	Total resends
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: retransmission_time
            
            	Retransmission time in seconds
            	**type**\:  int
            
            	**range:** 0..65535
            
            	**units**\: second
            
            .. attribute:: retransmit_time
            
            	Retransmit time distribution in seconds
            	**type**\:  list of int
            
            	**range:** 0..65535
            
            	**units**\: second
            
            .. attribute:: sequence_nr
            
            	Sequence NR
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: sequence_ns
            
            	Sequence NS
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: total_out_of_order_drop_packets
            
            	Total out of order dropped packets
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: total_out_of_order_reorder_packets
            
            	Total out of order reorder packets
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: total_peer_authentication_failures
            
            	Number of peer authentication failures
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: unsent_maximum_queue_size
            
            	Unsent maximum queue size
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: unsent_queue_size
            
            	Unsent queue size
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: zero_length_body_acknowledgement_sent
            
            	Total zero length body acknowledgement
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'tunnel-l2tun-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(L2Tpv2.Tunnels.Tunnel, self).__init__()

                self.yang_name = "tunnel"
                self.yang_parent_name = "tunnels"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.local_tunnel_id = YLeaf(YType.int32, "local-tunnel-id")

                self.active_sessions = YLeaf(YType.uint32, "active-sessions")

                self.class_name = YLeaf(YType.str, "class-name")

                self.digest_secrets = YLeaf(YType.uint16, "digest-secrets")

                self.is_congestion_control_enabled = YLeaf(YType.boolean, "is-congestion-control-enabled")

                self.is_pmtu_enabled = YLeaf(YType.boolean, "is-pmtu-enabled")

                self.is_tunnel_up = YLeaf(YType.boolean, "is-tunnel-up")

                self.local_address = YLeaf(YType.str, "local-address")

                self.local_port = YLeaf(YType.uint16, "local-port")

                self.local_tunnel_name = YLeaf(YType.str, "local-tunnel-name")

                self.local_window_size = YLeaf(YType.uint16, "local-window-size")

                self.maximum_retransmission_time = YLeaf(YType.uint16, "maximum-retransmission-time")

                self.order_queue_size = YLeaf(YType.uint16, "order-queue-size")

                self.packet_queue_check = YLeaf(YType.uint16, "packet-queue-check")

                self.protocol = YLeaf(YType.uint8, "protocol")

                self.remote_address = YLeaf(YType.str, "remote-address")

                self.remote_port = YLeaf(YType.uint16, "remote-port")

                self.remote_tunnel_id = YLeaf(YType.uint32, "remote-tunnel-id")

                self.remote_tunnel_name = YLeaf(YType.str, "remote-tunnel-name")

                self.remote_window_size = YLeaf(YType.uint16, "remote-window-size")

                self.resend_maximum_queue_size = YLeaf(YType.uint16, "resend-maximum-queue-size")

                self.resend_queue_size = YLeaf(YType.uint16, "resend-queue-size")

                self.resends = YLeaf(YType.uint32, "resends")

                self.retransmission_time = YLeaf(YType.uint16, "retransmission-time")

                self.retransmit_time = YLeafList(YType.uint16, "retransmit-time")

                self.sequence_nr = YLeaf(YType.uint16, "sequence-nr")

                self.sequence_ns = YLeaf(YType.uint16, "sequence-ns")

                self.total_out_of_order_drop_packets = YLeaf(YType.uint32, "total-out-of-order-drop-packets")

                self.total_out_of_order_reorder_packets = YLeaf(YType.uint32, "total-out-of-order-reorder-packets")

                self.total_peer_authentication_failures = YLeaf(YType.uint32, "total-peer-authentication-failures")

                self.unsent_maximum_queue_size = YLeaf(YType.uint16, "unsent-maximum-queue-size")

                self.unsent_queue_size = YLeaf(YType.uint16, "unsent-queue-size")

                self.zero_length_body_acknowledgement_sent = YLeaf(YType.uint32, "zero-length-body-acknowledgement-sent")
                self._segment_path = lambda: "tunnel" + "[local-tunnel-id='" + self.local_tunnel_id.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/tunnels/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(L2Tpv2.Tunnels.Tunnel, ['local_tunnel_id', 'active_sessions', 'class_name', 'digest_secrets', 'is_congestion_control_enabled', 'is_pmtu_enabled', 'is_tunnel_up', 'local_address', 'local_port', 'local_tunnel_name', 'local_window_size', 'maximum_retransmission_time', 'order_queue_size', 'packet_queue_check', 'protocol', 'remote_address', 'remote_port', 'remote_tunnel_id', 'remote_tunnel_name', 'remote_window_size', 'resend_maximum_queue_size', 'resend_queue_size', 'resends', 'retransmission_time', 'retransmit_time', 'sequence_nr', 'sequence_ns', 'total_out_of_order_drop_packets', 'total_out_of_order_reorder_packets', 'total_peer_authentication_failures', 'unsent_maximum_queue_size', 'unsent_queue_size', 'zero_length_body_acknowledgement_sent'], name, value)

    def clone_ptr(self):
        self._top_entity = L2Tpv2()
        return self._top_entity

