""" Cisco_IOS_XR_tunnel_l2tun_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR tunnel\-l2tun package operational data.

This module contains definitions
for the following management objects\:
  l2tp\: L2TP operational data
  l2tpv2\: l2tpv2

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class DigestHash(Enum):
    """
    DigestHash (Enum Class)

    Digest hash types

    .. data:: md5 = 0

    	MD5

    .. data:: sha1 = 1

    	SHA1

    """

    md5 = Enum.YLeaf(0, "md5")

    sha1 = Enum.YLeaf(1, "sha1")



class L2tp(Entity):
    """
    L2TP operational data
    
    .. attribute:: counters
    
    	L2TP control messages counters
    	**type**\:  :py:class:`Counters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Counters>`
    
    .. attribute:: tunnel_configurations
    
    	List of tunnel IDs
    	**type**\:  :py:class:`TunnelConfigurations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.TunnelConfigurations>`
    
    .. attribute:: counter_hist_fail
    
    	Failure events leading to disconnection
    	**type**\:  :py:class:`CounterHistFail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.CounterHistFail>`
    
    .. attribute:: classes
    
    	List of L2TP class names
    	**type**\:  :py:class:`Classes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Classes>`
    
    .. attribute:: tunnels
    
    	List of tunnel IDs
    	**type**\:  :py:class:`Tunnels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Tunnels>`
    
    .. attribute:: sessions
    
    	List of session IDs
    	**type**\:  :py:class:`Sessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Sessions>`
    
    .. attribute:: session
    
    	L2TP control messages counters
    	**type**\:  :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Session>`
    
    

    """

    _prefix = 'tunnel-l2tun-oper'
    _revision = '2017-09-07'

    def __init__(self):
        super(L2tp, self).__init__()
        self._top_entity = None

        self.yang_name = "l2tp"
        self.yang_parent_name = "Cisco-IOS-XR-tunnel-l2tun-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("counters", ("counters", L2tp.Counters)), ("tunnel-configurations", ("tunnel_configurations", L2tp.TunnelConfigurations)), ("counter-hist-fail", ("counter_hist_fail", L2tp.CounterHistFail)), ("classes", ("classes", L2tp.Classes)), ("tunnels", ("tunnels", L2tp.Tunnels)), ("sessions", ("sessions", L2tp.Sessions)), ("session", ("session", L2tp.Session))])
        self._leafs = OrderedDict()

        self.counters = L2tp.Counters()
        self.counters.parent = self
        self._children_name_map["counters"] = "counters"

        self.tunnel_configurations = L2tp.TunnelConfigurations()
        self.tunnel_configurations.parent = self
        self._children_name_map["tunnel_configurations"] = "tunnel-configurations"

        self.counter_hist_fail = L2tp.CounterHistFail()
        self.counter_hist_fail.parent = self
        self._children_name_map["counter_hist_fail"] = "counter-hist-fail"

        self.classes = L2tp.Classes()
        self.classes.parent = self
        self._children_name_map["classes"] = "classes"

        self.tunnels = L2tp.Tunnels()
        self.tunnels.parent = self
        self._children_name_map["tunnels"] = "tunnels"

        self.sessions = L2tp.Sessions()
        self.sessions.parent = self
        self._children_name_map["sessions"] = "sessions"

        self.session = L2tp.Session()
        self.session.parent = self
        self._children_name_map["session"] = "session"
        self._segment_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tp"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(L2tp, [], name, value)


    class Counters(Entity):
        """
        L2TP control messages counters
        
        .. attribute:: control
        
        	L2TP control messages counters
        	**type**\:  :py:class:`Control <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Counters.Control>`
        
        

        """

        _prefix = 'tunnel-l2tun-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(L2tp.Counters, self).__init__()

            self.yang_name = "counters"
            self.yang_parent_name = "l2tp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("control", ("control", L2tp.Counters.Control))])
            self._leafs = OrderedDict()

            self.control = L2tp.Counters.Control()
            self.control.parent = self
            self._children_name_map["control"] = "control"
            self._segment_path = lambda: "counters"
            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(L2tp.Counters, [], name, value)


        class Control(Entity):
            """
            L2TP control messages counters
            
            .. attribute:: tunnel_xr
            
            	L2TP control tunnel messages counters
            	**type**\:  :py:class:`TunnelXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Counters.Control.TunnelXr>`
            
            .. attribute:: tunnels
            
            	Table of tunnel IDs of control message counters
            	**type**\:  :py:class:`Tunnels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Counters.Control.Tunnels>`
            
            

            """

            _prefix = 'tunnel-l2tun-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(L2tp.Counters.Control, self).__init__()

                self.yang_name = "control"
                self.yang_parent_name = "counters"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("tunnel-xr", ("tunnel_xr", L2tp.Counters.Control.TunnelXr)), ("tunnels", ("tunnels", L2tp.Counters.Control.Tunnels))])
                self._leafs = OrderedDict()

                self.tunnel_xr = L2tp.Counters.Control.TunnelXr()
                self.tunnel_xr.parent = self
                self._children_name_map["tunnel_xr"] = "tunnel-xr"

                self.tunnels = L2tp.Counters.Control.Tunnels()
                self.tunnels.parent = self
                self._children_name_map["tunnels"] = "tunnels"
                self._segment_path = lambda: "control"
                self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/counters/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(L2tp.Counters.Control, [], name, value)


            class TunnelXr(Entity):
                """
                L2TP control tunnel messages counters
                
                .. attribute:: authentication
                
                	Tunnel authentication counters
                	**type**\:  :py:class:`Authentication <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Counters.Control.TunnelXr.Authentication>`
                
                .. attribute:: global_
                
                	Tunnel counters
                	**type**\:  :py:class:`Global <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Counters.Control.TunnelXr.Global>`
                
                

                """

                _prefix = 'tunnel-l2tun-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(L2tp.Counters.Control.TunnelXr, self).__init__()

                    self.yang_name = "tunnel-xr"
                    self.yang_parent_name = "control"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("authentication", ("authentication", L2tp.Counters.Control.TunnelXr.Authentication)), ("global", ("global_", L2tp.Counters.Control.TunnelXr.Global))])
                    self._leafs = OrderedDict()

                    self.authentication = L2tp.Counters.Control.TunnelXr.Authentication()
                    self.authentication.parent = self
                    self._children_name_map["authentication"] = "authentication"

                    self.global_ = L2tp.Counters.Control.TunnelXr.Global()
                    self.global_.parent = self
                    self._children_name_map["global_"] = "global"
                    self._segment_path = lambda: "tunnel-xr"
                    self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/counters/control/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(L2tp.Counters.Control.TunnelXr, [], name, value)


                class Authentication(Entity):
                    """
                    Tunnel authentication counters
                    
                    .. attribute:: nonce_avp
                    
                    	Nonce AVP statistics
                    	**type**\:  :py:class:`NonceAvp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Counters.Control.TunnelXr.Authentication.NonceAvp>`
                    
                    .. attribute:: common_digest
                    
                    	Common digest statistics
                    	**type**\:  :py:class:`CommonDigest <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Counters.Control.TunnelXr.Authentication.CommonDigest>`
                    
                    .. attribute:: primary_digest
                    
                    	Primary digest statistics
                    	**type**\:  :py:class:`PrimaryDigest <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Counters.Control.TunnelXr.Authentication.PrimaryDigest>`
                    
                    .. attribute:: secondary_digest
                    
                    	Secondary digest statistics
                    	**type**\:  :py:class:`SecondaryDigest <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Counters.Control.TunnelXr.Authentication.SecondaryDigest>`
                    
                    .. attribute:: integrity_check
                    
                    	Integrity check statistics
                    	**type**\:  :py:class:`IntegrityCheck <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Counters.Control.TunnelXr.Authentication.IntegrityCheck>`
                    
                    .. attribute:: local_secret
                    
                    	Local secret statistics
                    	**type**\:  :py:class:`LocalSecret <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Counters.Control.TunnelXr.Authentication.LocalSecret>`
                    
                    .. attribute:: challenge_avp
                    
                    	Challenge AVP statistics
                    	**type**\:  :py:class:`ChallengeAvp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Counters.Control.TunnelXr.Authentication.ChallengeAvp>`
                    
                    .. attribute:: challenge_reponse
                    
                    	Challenge response statistics
                    	**type**\:  :py:class:`ChallengeReponse <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Counters.Control.TunnelXr.Authentication.ChallengeReponse>`
                    
                    .. attribute:: overall_statistics
                    
                    	Overall statistics
                    	**type**\:  :py:class:`OverallStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Counters.Control.TunnelXr.Authentication.OverallStatistics>`
                    
                    

                    """

                    _prefix = 'tunnel-l2tun-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(L2tp.Counters.Control.TunnelXr.Authentication, self).__init__()

                        self.yang_name = "authentication"
                        self.yang_parent_name = "tunnel-xr"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("nonce-avp", ("nonce_avp", L2tp.Counters.Control.TunnelXr.Authentication.NonceAvp)), ("common-digest", ("common_digest", L2tp.Counters.Control.TunnelXr.Authentication.CommonDigest)), ("primary-digest", ("primary_digest", L2tp.Counters.Control.TunnelXr.Authentication.PrimaryDigest)), ("secondary-digest", ("secondary_digest", L2tp.Counters.Control.TunnelXr.Authentication.SecondaryDigest)), ("integrity-check", ("integrity_check", L2tp.Counters.Control.TunnelXr.Authentication.IntegrityCheck)), ("local-secret", ("local_secret", L2tp.Counters.Control.TunnelXr.Authentication.LocalSecret)), ("challenge-avp", ("challenge_avp", L2tp.Counters.Control.TunnelXr.Authentication.ChallengeAvp)), ("challenge-reponse", ("challenge_reponse", L2tp.Counters.Control.TunnelXr.Authentication.ChallengeReponse)), ("overall-statistics", ("overall_statistics", L2tp.Counters.Control.TunnelXr.Authentication.OverallStatistics))])
                        self._leafs = OrderedDict()

                        self.nonce_avp = L2tp.Counters.Control.TunnelXr.Authentication.NonceAvp()
                        self.nonce_avp.parent = self
                        self._children_name_map["nonce_avp"] = "nonce-avp"

                        self.common_digest = L2tp.Counters.Control.TunnelXr.Authentication.CommonDigest()
                        self.common_digest.parent = self
                        self._children_name_map["common_digest"] = "common-digest"

                        self.primary_digest = L2tp.Counters.Control.TunnelXr.Authentication.PrimaryDigest()
                        self.primary_digest.parent = self
                        self._children_name_map["primary_digest"] = "primary-digest"

                        self.secondary_digest = L2tp.Counters.Control.TunnelXr.Authentication.SecondaryDigest()
                        self.secondary_digest.parent = self
                        self._children_name_map["secondary_digest"] = "secondary-digest"

                        self.integrity_check = L2tp.Counters.Control.TunnelXr.Authentication.IntegrityCheck()
                        self.integrity_check.parent = self
                        self._children_name_map["integrity_check"] = "integrity-check"

                        self.local_secret = L2tp.Counters.Control.TunnelXr.Authentication.LocalSecret()
                        self.local_secret.parent = self
                        self._children_name_map["local_secret"] = "local-secret"

                        self.challenge_avp = L2tp.Counters.Control.TunnelXr.Authentication.ChallengeAvp()
                        self.challenge_avp.parent = self
                        self._children_name_map["challenge_avp"] = "challenge-avp"

                        self.challenge_reponse = L2tp.Counters.Control.TunnelXr.Authentication.ChallengeReponse()
                        self.challenge_reponse.parent = self
                        self._children_name_map["challenge_reponse"] = "challenge-reponse"

                        self.overall_statistics = L2tp.Counters.Control.TunnelXr.Authentication.OverallStatistics()
                        self.overall_statistics.parent = self
                        self._children_name_map["overall_statistics"] = "overall-statistics"
                        self._segment_path = lambda: "authentication"
                        self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/counters/control/tunnel-xr/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2tp.Counters.Control.TunnelXr.Authentication, [], name, value)


                    class NonceAvp(Entity):
                        """
                        Nonce AVP statistics
                        
                        .. attribute:: validate
                        
                        	Validate
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_hash
                        
                        	Bad hash
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_length
                        
                        	Bad length
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ignored
                        
                        	Ignored
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: missing
                        
                        	Missing
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: passed
                        
                        	Passed
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: failed
                        
                        	Failed
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: skipped
                        
                        	Skipped
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: generate_response_failures
                        
                        	Generate response fail
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unexpected
                        
                        	Unexpected
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unexpected_zlb
                        
                        	Unexpected ZLB
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'tunnel-l2tun-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(L2tp.Counters.Control.TunnelXr.Authentication.NonceAvp, self).__init__()

                            self.yang_name = "nonce-avp"
                            self.yang_parent_name = "authentication"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('validate', (YLeaf(YType.uint32, 'validate'), ['int'])),
                                ('bad_hash', (YLeaf(YType.uint32, 'bad-hash'), ['int'])),
                                ('bad_length', (YLeaf(YType.uint32, 'bad-length'), ['int'])),
                                ('ignored', (YLeaf(YType.uint32, 'ignored'), ['int'])),
                                ('missing', (YLeaf(YType.uint32, 'missing'), ['int'])),
                                ('passed', (YLeaf(YType.uint32, 'passed'), ['int'])),
                                ('failed', (YLeaf(YType.uint32, 'failed'), ['int'])),
                                ('skipped', (YLeaf(YType.uint32, 'skipped'), ['int'])),
                                ('generate_response_failures', (YLeaf(YType.uint32, 'generate-response-failures'), ['int'])),
                                ('unexpected', (YLeaf(YType.uint32, 'unexpected'), ['int'])),
                                ('unexpected_zlb', (YLeaf(YType.uint32, 'unexpected-zlb'), ['int'])),
                            ])
                            self.validate = None
                            self.bad_hash = None
                            self.bad_length = None
                            self.ignored = None
                            self.missing = None
                            self.passed = None
                            self.failed = None
                            self.skipped = None
                            self.generate_response_failures = None
                            self.unexpected = None
                            self.unexpected_zlb = None
                            self._segment_path = lambda: "nonce-avp"
                            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/counters/control/tunnel-xr/authentication/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2tp.Counters.Control.TunnelXr.Authentication.NonceAvp, [u'validate', u'bad_hash', u'bad_length', u'ignored', u'missing', u'passed', u'failed', u'skipped', u'generate_response_failures', u'unexpected', u'unexpected_zlb'], name, value)


                    class CommonDigest(Entity):
                        """
                        Common digest statistics
                        
                        .. attribute:: validate
                        
                        	Validate
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_hash
                        
                        	Bad hash
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_length
                        
                        	Bad length
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ignored
                        
                        	Ignored
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: missing
                        
                        	Missing
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: passed
                        
                        	Passed
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: failed
                        
                        	Failed
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: skipped
                        
                        	Skipped
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: generate_response_failures
                        
                        	Generate response fail
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unexpected
                        
                        	Unexpected
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unexpected_zlb
                        
                        	Unexpected ZLB
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'tunnel-l2tun-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(L2tp.Counters.Control.TunnelXr.Authentication.CommonDigest, self).__init__()

                            self.yang_name = "common-digest"
                            self.yang_parent_name = "authentication"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('validate', (YLeaf(YType.uint32, 'validate'), ['int'])),
                                ('bad_hash', (YLeaf(YType.uint32, 'bad-hash'), ['int'])),
                                ('bad_length', (YLeaf(YType.uint32, 'bad-length'), ['int'])),
                                ('ignored', (YLeaf(YType.uint32, 'ignored'), ['int'])),
                                ('missing', (YLeaf(YType.uint32, 'missing'), ['int'])),
                                ('passed', (YLeaf(YType.uint32, 'passed'), ['int'])),
                                ('failed', (YLeaf(YType.uint32, 'failed'), ['int'])),
                                ('skipped', (YLeaf(YType.uint32, 'skipped'), ['int'])),
                                ('generate_response_failures', (YLeaf(YType.uint32, 'generate-response-failures'), ['int'])),
                                ('unexpected', (YLeaf(YType.uint32, 'unexpected'), ['int'])),
                                ('unexpected_zlb', (YLeaf(YType.uint32, 'unexpected-zlb'), ['int'])),
                            ])
                            self.validate = None
                            self.bad_hash = None
                            self.bad_length = None
                            self.ignored = None
                            self.missing = None
                            self.passed = None
                            self.failed = None
                            self.skipped = None
                            self.generate_response_failures = None
                            self.unexpected = None
                            self.unexpected_zlb = None
                            self._segment_path = lambda: "common-digest"
                            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/counters/control/tunnel-xr/authentication/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2tp.Counters.Control.TunnelXr.Authentication.CommonDigest, [u'validate', u'bad_hash', u'bad_length', u'ignored', u'missing', u'passed', u'failed', u'skipped', u'generate_response_failures', u'unexpected', u'unexpected_zlb'], name, value)


                    class PrimaryDigest(Entity):
                        """
                        Primary digest statistics
                        
                        .. attribute:: validate
                        
                        	Validate
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_hash
                        
                        	Bad hash
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_length
                        
                        	Bad length
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ignored
                        
                        	Ignored
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: missing
                        
                        	Missing
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: passed
                        
                        	Passed
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: failed
                        
                        	Failed
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: skipped
                        
                        	Skipped
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: generate_response_failures
                        
                        	Generate response fail
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unexpected
                        
                        	Unexpected
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unexpected_zlb
                        
                        	Unexpected ZLB
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'tunnel-l2tun-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(L2tp.Counters.Control.TunnelXr.Authentication.PrimaryDigest, self).__init__()

                            self.yang_name = "primary-digest"
                            self.yang_parent_name = "authentication"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('validate', (YLeaf(YType.uint32, 'validate'), ['int'])),
                                ('bad_hash', (YLeaf(YType.uint32, 'bad-hash'), ['int'])),
                                ('bad_length', (YLeaf(YType.uint32, 'bad-length'), ['int'])),
                                ('ignored', (YLeaf(YType.uint32, 'ignored'), ['int'])),
                                ('missing', (YLeaf(YType.uint32, 'missing'), ['int'])),
                                ('passed', (YLeaf(YType.uint32, 'passed'), ['int'])),
                                ('failed', (YLeaf(YType.uint32, 'failed'), ['int'])),
                                ('skipped', (YLeaf(YType.uint32, 'skipped'), ['int'])),
                                ('generate_response_failures', (YLeaf(YType.uint32, 'generate-response-failures'), ['int'])),
                                ('unexpected', (YLeaf(YType.uint32, 'unexpected'), ['int'])),
                                ('unexpected_zlb', (YLeaf(YType.uint32, 'unexpected-zlb'), ['int'])),
                            ])
                            self.validate = None
                            self.bad_hash = None
                            self.bad_length = None
                            self.ignored = None
                            self.missing = None
                            self.passed = None
                            self.failed = None
                            self.skipped = None
                            self.generate_response_failures = None
                            self.unexpected = None
                            self.unexpected_zlb = None
                            self._segment_path = lambda: "primary-digest"
                            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/counters/control/tunnel-xr/authentication/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2tp.Counters.Control.TunnelXr.Authentication.PrimaryDigest, [u'validate', u'bad_hash', u'bad_length', u'ignored', u'missing', u'passed', u'failed', u'skipped', u'generate_response_failures', u'unexpected', u'unexpected_zlb'], name, value)


                    class SecondaryDigest(Entity):
                        """
                        Secondary digest statistics
                        
                        .. attribute:: validate
                        
                        	Validate
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_hash
                        
                        	Bad hash
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_length
                        
                        	Bad length
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ignored
                        
                        	Ignored
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: missing
                        
                        	Missing
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: passed
                        
                        	Passed
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: failed
                        
                        	Failed
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: skipped
                        
                        	Skipped
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: generate_response_failures
                        
                        	Generate response fail
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unexpected
                        
                        	Unexpected
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unexpected_zlb
                        
                        	Unexpected ZLB
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'tunnel-l2tun-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(L2tp.Counters.Control.TunnelXr.Authentication.SecondaryDigest, self).__init__()

                            self.yang_name = "secondary-digest"
                            self.yang_parent_name = "authentication"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('validate', (YLeaf(YType.uint32, 'validate'), ['int'])),
                                ('bad_hash', (YLeaf(YType.uint32, 'bad-hash'), ['int'])),
                                ('bad_length', (YLeaf(YType.uint32, 'bad-length'), ['int'])),
                                ('ignored', (YLeaf(YType.uint32, 'ignored'), ['int'])),
                                ('missing', (YLeaf(YType.uint32, 'missing'), ['int'])),
                                ('passed', (YLeaf(YType.uint32, 'passed'), ['int'])),
                                ('failed', (YLeaf(YType.uint32, 'failed'), ['int'])),
                                ('skipped', (YLeaf(YType.uint32, 'skipped'), ['int'])),
                                ('generate_response_failures', (YLeaf(YType.uint32, 'generate-response-failures'), ['int'])),
                                ('unexpected', (YLeaf(YType.uint32, 'unexpected'), ['int'])),
                                ('unexpected_zlb', (YLeaf(YType.uint32, 'unexpected-zlb'), ['int'])),
                            ])
                            self.validate = None
                            self.bad_hash = None
                            self.bad_length = None
                            self.ignored = None
                            self.missing = None
                            self.passed = None
                            self.failed = None
                            self.skipped = None
                            self.generate_response_failures = None
                            self.unexpected = None
                            self.unexpected_zlb = None
                            self._segment_path = lambda: "secondary-digest"
                            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/counters/control/tunnel-xr/authentication/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2tp.Counters.Control.TunnelXr.Authentication.SecondaryDigest, [u'validate', u'bad_hash', u'bad_length', u'ignored', u'missing', u'passed', u'failed', u'skipped', u'generate_response_failures', u'unexpected', u'unexpected_zlb'], name, value)


                    class IntegrityCheck(Entity):
                        """
                        Integrity check statistics
                        
                        .. attribute:: validate
                        
                        	Validate
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_hash
                        
                        	Bad hash
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_length
                        
                        	Bad length
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ignored
                        
                        	Ignored
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: missing
                        
                        	Missing
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: passed
                        
                        	Passed
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: failed
                        
                        	Failed
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: skipped
                        
                        	Skipped
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: generate_response_failures
                        
                        	Generate response fail
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unexpected
                        
                        	Unexpected
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unexpected_zlb
                        
                        	Unexpected ZLB
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'tunnel-l2tun-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(L2tp.Counters.Control.TunnelXr.Authentication.IntegrityCheck, self).__init__()

                            self.yang_name = "integrity-check"
                            self.yang_parent_name = "authentication"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('validate', (YLeaf(YType.uint32, 'validate'), ['int'])),
                                ('bad_hash', (YLeaf(YType.uint32, 'bad-hash'), ['int'])),
                                ('bad_length', (YLeaf(YType.uint32, 'bad-length'), ['int'])),
                                ('ignored', (YLeaf(YType.uint32, 'ignored'), ['int'])),
                                ('missing', (YLeaf(YType.uint32, 'missing'), ['int'])),
                                ('passed', (YLeaf(YType.uint32, 'passed'), ['int'])),
                                ('failed', (YLeaf(YType.uint32, 'failed'), ['int'])),
                                ('skipped', (YLeaf(YType.uint32, 'skipped'), ['int'])),
                                ('generate_response_failures', (YLeaf(YType.uint32, 'generate-response-failures'), ['int'])),
                                ('unexpected', (YLeaf(YType.uint32, 'unexpected'), ['int'])),
                                ('unexpected_zlb', (YLeaf(YType.uint32, 'unexpected-zlb'), ['int'])),
                            ])
                            self.validate = None
                            self.bad_hash = None
                            self.bad_length = None
                            self.ignored = None
                            self.missing = None
                            self.passed = None
                            self.failed = None
                            self.skipped = None
                            self.generate_response_failures = None
                            self.unexpected = None
                            self.unexpected_zlb = None
                            self._segment_path = lambda: "integrity-check"
                            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/counters/control/tunnel-xr/authentication/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2tp.Counters.Control.TunnelXr.Authentication.IntegrityCheck, [u'validate', u'bad_hash', u'bad_length', u'ignored', u'missing', u'passed', u'failed', u'skipped', u'generate_response_failures', u'unexpected', u'unexpected_zlb'], name, value)


                    class LocalSecret(Entity):
                        """
                        Local secret statistics
                        
                        .. attribute:: validate
                        
                        	Validate
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_hash
                        
                        	Bad hash
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_length
                        
                        	Bad length
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ignored
                        
                        	Ignored
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: missing
                        
                        	Missing
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: passed
                        
                        	Passed
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: failed
                        
                        	Failed
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: skipped
                        
                        	Skipped
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: generate_response_failures
                        
                        	Generate response fail
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unexpected
                        
                        	Unexpected
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unexpected_zlb
                        
                        	Unexpected ZLB
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'tunnel-l2tun-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(L2tp.Counters.Control.TunnelXr.Authentication.LocalSecret, self).__init__()

                            self.yang_name = "local-secret"
                            self.yang_parent_name = "authentication"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('validate', (YLeaf(YType.uint32, 'validate'), ['int'])),
                                ('bad_hash', (YLeaf(YType.uint32, 'bad-hash'), ['int'])),
                                ('bad_length', (YLeaf(YType.uint32, 'bad-length'), ['int'])),
                                ('ignored', (YLeaf(YType.uint32, 'ignored'), ['int'])),
                                ('missing', (YLeaf(YType.uint32, 'missing'), ['int'])),
                                ('passed', (YLeaf(YType.uint32, 'passed'), ['int'])),
                                ('failed', (YLeaf(YType.uint32, 'failed'), ['int'])),
                                ('skipped', (YLeaf(YType.uint32, 'skipped'), ['int'])),
                                ('generate_response_failures', (YLeaf(YType.uint32, 'generate-response-failures'), ['int'])),
                                ('unexpected', (YLeaf(YType.uint32, 'unexpected'), ['int'])),
                                ('unexpected_zlb', (YLeaf(YType.uint32, 'unexpected-zlb'), ['int'])),
                            ])
                            self.validate = None
                            self.bad_hash = None
                            self.bad_length = None
                            self.ignored = None
                            self.missing = None
                            self.passed = None
                            self.failed = None
                            self.skipped = None
                            self.generate_response_failures = None
                            self.unexpected = None
                            self.unexpected_zlb = None
                            self._segment_path = lambda: "local-secret"
                            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/counters/control/tunnel-xr/authentication/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2tp.Counters.Control.TunnelXr.Authentication.LocalSecret, [u'validate', u'bad_hash', u'bad_length', u'ignored', u'missing', u'passed', u'failed', u'skipped', u'generate_response_failures', u'unexpected', u'unexpected_zlb'], name, value)


                    class ChallengeAvp(Entity):
                        """
                        Challenge AVP statistics
                        
                        .. attribute:: validate
                        
                        	Validate
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_hash
                        
                        	Bad hash
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_length
                        
                        	Bad length
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ignored
                        
                        	Ignored
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: missing
                        
                        	Missing
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: passed
                        
                        	Passed
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: failed
                        
                        	Failed
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: skipped
                        
                        	Skipped
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: generate_response_failures
                        
                        	Generate response fail
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unexpected
                        
                        	Unexpected
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unexpected_zlb
                        
                        	Unexpected ZLB
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'tunnel-l2tun-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(L2tp.Counters.Control.TunnelXr.Authentication.ChallengeAvp, self).__init__()

                            self.yang_name = "challenge-avp"
                            self.yang_parent_name = "authentication"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('validate', (YLeaf(YType.uint32, 'validate'), ['int'])),
                                ('bad_hash', (YLeaf(YType.uint32, 'bad-hash'), ['int'])),
                                ('bad_length', (YLeaf(YType.uint32, 'bad-length'), ['int'])),
                                ('ignored', (YLeaf(YType.uint32, 'ignored'), ['int'])),
                                ('missing', (YLeaf(YType.uint32, 'missing'), ['int'])),
                                ('passed', (YLeaf(YType.uint32, 'passed'), ['int'])),
                                ('failed', (YLeaf(YType.uint32, 'failed'), ['int'])),
                                ('skipped', (YLeaf(YType.uint32, 'skipped'), ['int'])),
                                ('generate_response_failures', (YLeaf(YType.uint32, 'generate-response-failures'), ['int'])),
                                ('unexpected', (YLeaf(YType.uint32, 'unexpected'), ['int'])),
                                ('unexpected_zlb', (YLeaf(YType.uint32, 'unexpected-zlb'), ['int'])),
                            ])
                            self.validate = None
                            self.bad_hash = None
                            self.bad_length = None
                            self.ignored = None
                            self.missing = None
                            self.passed = None
                            self.failed = None
                            self.skipped = None
                            self.generate_response_failures = None
                            self.unexpected = None
                            self.unexpected_zlb = None
                            self._segment_path = lambda: "challenge-avp"
                            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/counters/control/tunnel-xr/authentication/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2tp.Counters.Control.TunnelXr.Authentication.ChallengeAvp, [u'validate', u'bad_hash', u'bad_length', u'ignored', u'missing', u'passed', u'failed', u'skipped', u'generate_response_failures', u'unexpected', u'unexpected_zlb'], name, value)


                    class ChallengeReponse(Entity):
                        """
                        Challenge response statistics
                        
                        .. attribute:: validate
                        
                        	Validate
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_hash
                        
                        	Bad hash
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_length
                        
                        	Bad length
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ignored
                        
                        	Ignored
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: missing
                        
                        	Missing
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: passed
                        
                        	Passed
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: failed
                        
                        	Failed
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: skipped
                        
                        	Skipped
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: generate_response_failures
                        
                        	Generate response fail
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unexpected
                        
                        	Unexpected
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unexpected_zlb
                        
                        	Unexpected ZLB
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'tunnel-l2tun-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(L2tp.Counters.Control.TunnelXr.Authentication.ChallengeReponse, self).__init__()

                            self.yang_name = "challenge-reponse"
                            self.yang_parent_name = "authentication"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('validate', (YLeaf(YType.uint32, 'validate'), ['int'])),
                                ('bad_hash', (YLeaf(YType.uint32, 'bad-hash'), ['int'])),
                                ('bad_length', (YLeaf(YType.uint32, 'bad-length'), ['int'])),
                                ('ignored', (YLeaf(YType.uint32, 'ignored'), ['int'])),
                                ('missing', (YLeaf(YType.uint32, 'missing'), ['int'])),
                                ('passed', (YLeaf(YType.uint32, 'passed'), ['int'])),
                                ('failed', (YLeaf(YType.uint32, 'failed'), ['int'])),
                                ('skipped', (YLeaf(YType.uint32, 'skipped'), ['int'])),
                                ('generate_response_failures', (YLeaf(YType.uint32, 'generate-response-failures'), ['int'])),
                                ('unexpected', (YLeaf(YType.uint32, 'unexpected'), ['int'])),
                                ('unexpected_zlb', (YLeaf(YType.uint32, 'unexpected-zlb'), ['int'])),
                            ])
                            self.validate = None
                            self.bad_hash = None
                            self.bad_length = None
                            self.ignored = None
                            self.missing = None
                            self.passed = None
                            self.failed = None
                            self.skipped = None
                            self.generate_response_failures = None
                            self.unexpected = None
                            self.unexpected_zlb = None
                            self._segment_path = lambda: "challenge-reponse"
                            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/counters/control/tunnel-xr/authentication/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2tp.Counters.Control.TunnelXr.Authentication.ChallengeReponse, [u'validate', u'bad_hash', u'bad_length', u'ignored', u'missing', u'passed', u'failed', u'skipped', u'generate_response_failures', u'unexpected', u'unexpected_zlb'], name, value)


                    class OverallStatistics(Entity):
                        """
                        Overall statistics
                        
                        .. attribute:: validate
                        
                        	Validate
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_hash
                        
                        	Bad hash
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_length
                        
                        	Bad length
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ignored
                        
                        	Ignored
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: missing
                        
                        	Missing
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: passed
                        
                        	Passed
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: failed
                        
                        	Failed
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: skipped
                        
                        	Skipped
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: generate_response_failures
                        
                        	Generate response fail
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unexpected
                        
                        	Unexpected
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unexpected_zlb
                        
                        	Unexpected ZLB
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'tunnel-l2tun-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(L2tp.Counters.Control.TunnelXr.Authentication.OverallStatistics, self).__init__()

                            self.yang_name = "overall-statistics"
                            self.yang_parent_name = "authentication"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('validate', (YLeaf(YType.uint32, 'validate'), ['int'])),
                                ('bad_hash', (YLeaf(YType.uint32, 'bad-hash'), ['int'])),
                                ('bad_length', (YLeaf(YType.uint32, 'bad-length'), ['int'])),
                                ('ignored', (YLeaf(YType.uint32, 'ignored'), ['int'])),
                                ('missing', (YLeaf(YType.uint32, 'missing'), ['int'])),
                                ('passed', (YLeaf(YType.uint32, 'passed'), ['int'])),
                                ('failed', (YLeaf(YType.uint32, 'failed'), ['int'])),
                                ('skipped', (YLeaf(YType.uint32, 'skipped'), ['int'])),
                                ('generate_response_failures', (YLeaf(YType.uint32, 'generate-response-failures'), ['int'])),
                                ('unexpected', (YLeaf(YType.uint32, 'unexpected'), ['int'])),
                                ('unexpected_zlb', (YLeaf(YType.uint32, 'unexpected-zlb'), ['int'])),
                            ])
                            self.validate = None
                            self.bad_hash = None
                            self.bad_length = None
                            self.ignored = None
                            self.missing = None
                            self.passed = None
                            self.failed = None
                            self.skipped = None
                            self.generate_response_failures = None
                            self.unexpected = None
                            self.unexpected_zlb = None
                            self._segment_path = lambda: "overall-statistics"
                            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/counters/control/tunnel-xr/authentication/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2tp.Counters.Control.TunnelXr.Authentication.OverallStatistics, [u'validate', u'bad_hash', u'bad_length', u'ignored', u'missing', u'passed', u'failed', u'skipped', u'generate_response_failures', u'unexpected', u'unexpected_zlb'], name, value)


                class Global(Entity):
                    """
                    Tunnel counters
                    
                    .. attribute:: transmit
                    
                    	Transmit data
                    	**type**\:  :py:class:`Transmit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Counters.Control.TunnelXr.Global.Transmit>`
                    
                    .. attribute:: retransmit
                    
                    	Re transmit data
                    	**type**\:  :py:class:`Retransmit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Counters.Control.TunnelXr.Global.Retransmit>`
                    
                    .. attribute:: received
                    
                    	Received data
                    	**type**\:  :py:class:`Received <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Counters.Control.TunnelXr.Global.Received>`
                    
                    .. attribute:: drop
                    
                    	Drop data
                    	**type**\:  :py:class:`Drop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Counters.Control.TunnelXr.Global.Drop>`
                    
                    .. attribute:: total_transmit
                    
                    	Total transmit
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: total_retransmit
                    
                    	Total retransmit
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: total_received
                    
                    	Total received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: total_drop
                    
                    	Total drop
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'tunnel-l2tun-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(L2tp.Counters.Control.TunnelXr.Global, self).__init__()

                        self.yang_name = "global"
                        self.yang_parent_name = "tunnel-xr"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("transmit", ("transmit", L2tp.Counters.Control.TunnelXr.Global.Transmit)), ("retransmit", ("retransmit", L2tp.Counters.Control.TunnelXr.Global.Retransmit)), ("received", ("received", L2tp.Counters.Control.TunnelXr.Global.Received)), ("drop", ("drop", L2tp.Counters.Control.TunnelXr.Global.Drop))])
                        self._leafs = OrderedDict([
                            ('total_transmit', (YLeaf(YType.uint32, 'total-transmit'), ['int'])),
                            ('total_retransmit', (YLeaf(YType.uint32, 'total-retransmit'), ['int'])),
                            ('total_received', (YLeaf(YType.uint32, 'total-received'), ['int'])),
                            ('total_drop', (YLeaf(YType.uint32, 'total-drop'), ['int'])),
                        ])
                        self.total_transmit = None
                        self.total_retransmit = None
                        self.total_received = None
                        self.total_drop = None

                        self.transmit = L2tp.Counters.Control.TunnelXr.Global.Transmit()
                        self.transmit.parent = self
                        self._children_name_map["transmit"] = "transmit"

                        self.retransmit = L2tp.Counters.Control.TunnelXr.Global.Retransmit()
                        self.retransmit.parent = self
                        self._children_name_map["retransmit"] = "retransmit"

                        self.received = L2tp.Counters.Control.TunnelXr.Global.Received()
                        self.received.parent = self
                        self._children_name_map["received"] = "received"

                        self.drop = L2tp.Counters.Control.TunnelXr.Global.Drop()
                        self.drop.parent = self
                        self._children_name_map["drop"] = "drop"
                        self._segment_path = lambda: "global"
                        self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/counters/control/tunnel-xr/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2tp.Counters.Control.TunnelXr.Global, [u'total_transmit', u'total_retransmit', u'total_received', u'total_drop'], name, value)


                    class Transmit(Entity):
                        """
                        Transmit data
                        
                        .. attribute:: unknown_packets
                        
                        	Unknown packets
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: zero_length_body_packets
                        
                        	Zero length body packets
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: start_control_connection_requests
                        
                        	Start control connection requests
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: start_control_connection_replies
                        
                        	Start control connection replies
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: start_control_connection_notifications
                        
                        	Start control connection notifications
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: stop_control_connection_notifications
                        
                        	Stop control connection notifications
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: hello_packets
                        
                        	Keep alive messages
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: outgoing_call_requests
                        
                        	Outgoing call requests
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: outgoing_call_replies
                        
                        	Outgoing call replies
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: outgoing_call_connected_packets
                        
                        	Outgoing call connected packets
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: incoming_call_requests
                        
                        	Incoming call requests
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: incoming_call_replies
                        
                        	Incoming call replies
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: incoming_call_connected_packets
                        
                        	Incoming call connected packets
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: call_disconnect_notify_packets
                        
                        	Call disconnect notify packets
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: wan_error_notify_packets
                        
                        	WAN error notify packets
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: set_link_info_packets
                        
                        	Set link info packets
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: service_relay_requests
                        
                        	Service relay request counts
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: service_relay_replies
                        
                        	Service relay reply counts
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: acknowledgement_packets
                        
                        	Packets acknowledgement
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'tunnel-l2tun-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(L2tp.Counters.Control.TunnelXr.Global.Transmit, self).__init__()

                            self.yang_name = "transmit"
                            self.yang_parent_name = "global"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('unknown_packets', (YLeaf(YType.uint32, 'unknown-packets'), ['int'])),
                                ('zero_length_body_packets', (YLeaf(YType.uint32, 'zero-length-body-packets'), ['int'])),
                                ('start_control_connection_requests', (YLeaf(YType.uint32, 'start-control-connection-requests'), ['int'])),
                                ('start_control_connection_replies', (YLeaf(YType.uint32, 'start-control-connection-replies'), ['int'])),
                                ('start_control_connection_notifications', (YLeaf(YType.uint32, 'start-control-connection-notifications'), ['int'])),
                                ('stop_control_connection_notifications', (YLeaf(YType.uint32, 'stop-control-connection-notifications'), ['int'])),
                                ('hello_packets', (YLeaf(YType.uint32, 'hello-packets'), ['int'])),
                                ('outgoing_call_requests', (YLeaf(YType.uint32, 'outgoing-call-requests'), ['int'])),
                                ('outgoing_call_replies', (YLeaf(YType.uint32, 'outgoing-call-replies'), ['int'])),
                                ('outgoing_call_connected_packets', (YLeaf(YType.uint32, 'outgoing-call-connected-packets'), ['int'])),
                                ('incoming_call_requests', (YLeaf(YType.uint32, 'incoming-call-requests'), ['int'])),
                                ('incoming_call_replies', (YLeaf(YType.uint32, 'incoming-call-replies'), ['int'])),
                                ('incoming_call_connected_packets', (YLeaf(YType.uint32, 'incoming-call-connected-packets'), ['int'])),
                                ('call_disconnect_notify_packets', (YLeaf(YType.uint32, 'call-disconnect-notify-packets'), ['int'])),
                                ('wan_error_notify_packets', (YLeaf(YType.uint32, 'wan-error-notify-packets'), ['int'])),
                                ('set_link_info_packets', (YLeaf(YType.uint32, 'set-link-info-packets'), ['int'])),
                                ('service_relay_requests', (YLeaf(YType.uint32, 'service-relay-requests'), ['int'])),
                                ('service_relay_replies', (YLeaf(YType.uint32, 'service-relay-replies'), ['int'])),
                                ('acknowledgement_packets', (YLeaf(YType.uint32, 'acknowledgement-packets'), ['int'])),
                            ])
                            self.unknown_packets = None
                            self.zero_length_body_packets = None
                            self.start_control_connection_requests = None
                            self.start_control_connection_replies = None
                            self.start_control_connection_notifications = None
                            self.stop_control_connection_notifications = None
                            self.hello_packets = None
                            self.outgoing_call_requests = None
                            self.outgoing_call_replies = None
                            self.outgoing_call_connected_packets = None
                            self.incoming_call_requests = None
                            self.incoming_call_replies = None
                            self.incoming_call_connected_packets = None
                            self.call_disconnect_notify_packets = None
                            self.wan_error_notify_packets = None
                            self.set_link_info_packets = None
                            self.service_relay_requests = None
                            self.service_relay_replies = None
                            self.acknowledgement_packets = None
                            self._segment_path = lambda: "transmit"
                            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/counters/control/tunnel-xr/global/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2tp.Counters.Control.TunnelXr.Global.Transmit, [u'unknown_packets', u'zero_length_body_packets', u'start_control_connection_requests', u'start_control_connection_replies', u'start_control_connection_notifications', u'stop_control_connection_notifications', u'hello_packets', u'outgoing_call_requests', u'outgoing_call_replies', u'outgoing_call_connected_packets', u'incoming_call_requests', u'incoming_call_replies', u'incoming_call_connected_packets', u'call_disconnect_notify_packets', u'wan_error_notify_packets', u'set_link_info_packets', u'service_relay_requests', u'service_relay_replies', u'acknowledgement_packets'], name, value)


                    class Retransmit(Entity):
                        """
                        Re transmit data
                        
                        .. attribute:: unknown_packets
                        
                        	Unknown packets
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: zero_length_body_packets
                        
                        	Zero length body packets
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: start_control_connection_requests
                        
                        	Start control connection requests
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: start_control_connection_replies
                        
                        	Start control connection replies
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: start_control_connection_notifications
                        
                        	Start control connection notifications
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: stop_control_connection_notifications
                        
                        	Stop control connection notifications
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: hello_packets
                        
                        	Keep alive messages
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: outgoing_call_requests
                        
                        	Outgoing call requests
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: outgoing_call_replies
                        
                        	Outgoing call replies
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: outgoing_call_connected_packets
                        
                        	Outgoing call connected packets
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: incoming_call_requests
                        
                        	Incoming call requests
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: incoming_call_replies
                        
                        	Incoming call replies
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: incoming_call_connected_packets
                        
                        	Incoming call connected packets
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: call_disconnect_notify_packets
                        
                        	Call disconnect notify packets
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: wan_error_notify_packets
                        
                        	WAN error notify packets
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: set_link_info_packets
                        
                        	Set link info packets
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: service_relay_requests
                        
                        	Service relay request counts
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: service_relay_replies
                        
                        	Service relay reply counts
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: acknowledgement_packets
                        
                        	Packets acknowledgement
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'tunnel-l2tun-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(L2tp.Counters.Control.TunnelXr.Global.Retransmit, self).__init__()

                            self.yang_name = "retransmit"
                            self.yang_parent_name = "global"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('unknown_packets', (YLeaf(YType.uint32, 'unknown-packets'), ['int'])),
                                ('zero_length_body_packets', (YLeaf(YType.uint32, 'zero-length-body-packets'), ['int'])),
                                ('start_control_connection_requests', (YLeaf(YType.uint32, 'start-control-connection-requests'), ['int'])),
                                ('start_control_connection_replies', (YLeaf(YType.uint32, 'start-control-connection-replies'), ['int'])),
                                ('start_control_connection_notifications', (YLeaf(YType.uint32, 'start-control-connection-notifications'), ['int'])),
                                ('stop_control_connection_notifications', (YLeaf(YType.uint32, 'stop-control-connection-notifications'), ['int'])),
                                ('hello_packets', (YLeaf(YType.uint32, 'hello-packets'), ['int'])),
                                ('outgoing_call_requests', (YLeaf(YType.uint32, 'outgoing-call-requests'), ['int'])),
                                ('outgoing_call_replies', (YLeaf(YType.uint32, 'outgoing-call-replies'), ['int'])),
                                ('outgoing_call_connected_packets', (YLeaf(YType.uint32, 'outgoing-call-connected-packets'), ['int'])),
                                ('incoming_call_requests', (YLeaf(YType.uint32, 'incoming-call-requests'), ['int'])),
                                ('incoming_call_replies', (YLeaf(YType.uint32, 'incoming-call-replies'), ['int'])),
                                ('incoming_call_connected_packets', (YLeaf(YType.uint32, 'incoming-call-connected-packets'), ['int'])),
                                ('call_disconnect_notify_packets', (YLeaf(YType.uint32, 'call-disconnect-notify-packets'), ['int'])),
                                ('wan_error_notify_packets', (YLeaf(YType.uint32, 'wan-error-notify-packets'), ['int'])),
                                ('set_link_info_packets', (YLeaf(YType.uint32, 'set-link-info-packets'), ['int'])),
                                ('service_relay_requests', (YLeaf(YType.uint32, 'service-relay-requests'), ['int'])),
                                ('service_relay_replies', (YLeaf(YType.uint32, 'service-relay-replies'), ['int'])),
                                ('acknowledgement_packets', (YLeaf(YType.uint32, 'acknowledgement-packets'), ['int'])),
                            ])
                            self.unknown_packets = None
                            self.zero_length_body_packets = None
                            self.start_control_connection_requests = None
                            self.start_control_connection_replies = None
                            self.start_control_connection_notifications = None
                            self.stop_control_connection_notifications = None
                            self.hello_packets = None
                            self.outgoing_call_requests = None
                            self.outgoing_call_replies = None
                            self.outgoing_call_connected_packets = None
                            self.incoming_call_requests = None
                            self.incoming_call_replies = None
                            self.incoming_call_connected_packets = None
                            self.call_disconnect_notify_packets = None
                            self.wan_error_notify_packets = None
                            self.set_link_info_packets = None
                            self.service_relay_requests = None
                            self.service_relay_replies = None
                            self.acknowledgement_packets = None
                            self._segment_path = lambda: "retransmit"
                            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/counters/control/tunnel-xr/global/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2tp.Counters.Control.TunnelXr.Global.Retransmit, [u'unknown_packets', u'zero_length_body_packets', u'start_control_connection_requests', u'start_control_connection_replies', u'start_control_connection_notifications', u'stop_control_connection_notifications', u'hello_packets', u'outgoing_call_requests', u'outgoing_call_replies', u'outgoing_call_connected_packets', u'incoming_call_requests', u'incoming_call_replies', u'incoming_call_connected_packets', u'call_disconnect_notify_packets', u'wan_error_notify_packets', u'set_link_info_packets', u'service_relay_requests', u'service_relay_replies', u'acknowledgement_packets'], name, value)


                    class Received(Entity):
                        """
                        Received data
                        
                        .. attribute:: unknown_packets
                        
                        	Unknown packets
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: zero_length_body_packets
                        
                        	Zero length body packets
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: start_control_connection_requests
                        
                        	Start control connection requests
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: start_control_connection_replies
                        
                        	Start control connection replies
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: start_control_connection_notifications
                        
                        	Start control connection notifications
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: stop_control_connection_notifications
                        
                        	Stop control connection notifications
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: hello_packets
                        
                        	Keep alive messages
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: outgoing_call_requests
                        
                        	Outgoing call requests
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: outgoing_call_replies
                        
                        	Outgoing call replies
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: outgoing_call_connected_packets
                        
                        	Outgoing call connected packets
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: incoming_call_requests
                        
                        	Incoming call requests
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: incoming_call_replies
                        
                        	Incoming call replies
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: incoming_call_connected_packets
                        
                        	Incoming call connected packets
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: call_disconnect_notify_packets
                        
                        	Call disconnect notify packets
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: wan_error_notify_packets
                        
                        	WAN error notify packets
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: set_link_info_packets
                        
                        	Set link info packets
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: service_relay_requests
                        
                        	Service relay request counts
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: service_relay_replies
                        
                        	Service relay reply counts
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: acknowledgement_packets
                        
                        	Packets acknowledgement
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'tunnel-l2tun-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(L2tp.Counters.Control.TunnelXr.Global.Received, self).__init__()

                            self.yang_name = "received"
                            self.yang_parent_name = "global"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('unknown_packets', (YLeaf(YType.uint32, 'unknown-packets'), ['int'])),
                                ('zero_length_body_packets', (YLeaf(YType.uint32, 'zero-length-body-packets'), ['int'])),
                                ('start_control_connection_requests', (YLeaf(YType.uint32, 'start-control-connection-requests'), ['int'])),
                                ('start_control_connection_replies', (YLeaf(YType.uint32, 'start-control-connection-replies'), ['int'])),
                                ('start_control_connection_notifications', (YLeaf(YType.uint32, 'start-control-connection-notifications'), ['int'])),
                                ('stop_control_connection_notifications', (YLeaf(YType.uint32, 'stop-control-connection-notifications'), ['int'])),
                                ('hello_packets', (YLeaf(YType.uint32, 'hello-packets'), ['int'])),
                                ('outgoing_call_requests', (YLeaf(YType.uint32, 'outgoing-call-requests'), ['int'])),
                                ('outgoing_call_replies', (YLeaf(YType.uint32, 'outgoing-call-replies'), ['int'])),
                                ('outgoing_call_connected_packets', (YLeaf(YType.uint32, 'outgoing-call-connected-packets'), ['int'])),
                                ('incoming_call_requests', (YLeaf(YType.uint32, 'incoming-call-requests'), ['int'])),
                                ('incoming_call_replies', (YLeaf(YType.uint32, 'incoming-call-replies'), ['int'])),
                                ('incoming_call_connected_packets', (YLeaf(YType.uint32, 'incoming-call-connected-packets'), ['int'])),
                                ('call_disconnect_notify_packets', (YLeaf(YType.uint32, 'call-disconnect-notify-packets'), ['int'])),
                                ('wan_error_notify_packets', (YLeaf(YType.uint32, 'wan-error-notify-packets'), ['int'])),
                                ('set_link_info_packets', (YLeaf(YType.uint32, 'set-link-info-packets'), ['int'])),
                                ('service_relay_requests', (YLeaf(YType.uint32, 'service-relay-requests'), ['int'])),
                                ('service_relay_replies', (YLeaf(YType.uint32, 'service-relay-replies'), ['int'])),
                                ('acknowledgement_packets', (YLeaf(YType.uint32, 'acknowledgement-packets'), ['int'])),
                            ])
                            self.unknown_packets = None
                            self.zero_length_body_packets = None
                            self.start_control_connection_requests = None
                            self.start_control_connection_replies = None
                            self.start_control_connection_notifications = None
                            self.stop_control_connection_notifications = None
                            self.hello_packets = None
                            self.outgoing_call_requests = None
                            self.outgoing_call_replies = None
                            self.outgoing_call_connected_packets = None
                            self.incoming_call_requests = None
                            self.incoming_call_replies = None
                            self.incoming_call_connected_packets = None
                            self.call_disconnect_notify_packets = None
                            self.wan_error_notify_packets = None
                            self.set_link_info_packets = None
                            self.service_relay_requests = None
                            self.service_relay_replies = None
                            self.acknowledgement_packets = None
                            self._segment_path = lambda: "received"
                            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/counters/control/tunnel-xr/global/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2tp.Counters.Control.TunnelXr.Global.Received, [u'unknown_packets', u'zero_length_body_packets', u'start_control_connection_requests', u'start_control_connection_replies', u'start_control_connection_notifications', u'stop_control_connection_notifications', u'hello_packets', u'outgoing_call_requests', u'outgoing_call_replies', u'outgoing_call_connected_packets', u'incoming_call_requests', u'incoming_call_replies', u'incoming_call_connected_packets', u'call_disconnect_notify_packets', u'wan_error_notify_packets', u'set_link_info_packets', u'service_relay_requests', u'service_relay_replies', u'acknowledgement_packets'], name, value)


                    class Drop(Entity):
                        """
                        Drop data
                        
                        .. attribute:: unknown_packets
                        
                        	Unknown packets
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: zero_length_body_packets
                        
                        	Zero length body packets
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: start_control_connection_requests
                        
                        	Start control connection requests
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: start_control_connection_replies
                        
                        	Start control connection replies
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: start_control_connection_notifications
                        
                        	Start control connection notifications
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: stop_control_connection_notifications
                        
                        	Stop control connection notifications
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: hello_packets
                        
                        	Keep alive messages
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: outgoing_call_requests
                        
                        	Outgoing call requests
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: outgoing_call_replies
                        
                        	Outgoing call replies
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: outgoing_call_connected_packets
                        
                        	Outgoing call connected packets
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: incoming_call_requests
                        
                        	Incoming call requests
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: incoming_call_replies
                        
                        	Incoming call replies
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: incoming_call_connected_packets
                        
                        	Incoming call connected packets
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: call_disconnect_notify_packets
                        
                        	Call disconnect notify packets
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: wan_error_notify_packets
                        
                        	WAN error notify packets
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: set_link_info_packets
                        
                        	Set link info packets
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: service_relay_requests
                        
                        	Service relay request counts
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: service_relay_replies
                        
                        	Service relay reply counts
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: acknowledgement_packets
                        
                        	Packets acknowledgement
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'tunnel-l2tun-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(L2tp.Counters.Control.TunnelXr.Global.Drop, self).__init__()

                            self.yang_name = "drop"
                            self.yang_parent_name = "global"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('unknown_packets', (YLeaf(YType.uint32, 'unknown-packets'), ['int'])),
                                ('zero_length_body_packets', (YLeaf(YType.uint32, 'zero-length-body-packets'), ['int'])),
                                ('start_control_connection_requests', (YLeaf(YType.uint32, 'start-control-connection-requests'), ['int'])),
                                ('start_control_connection_replies', (YLeaf(YType.uint32, 'start-control-connection-replies'), ['int'])),
                                ('start_control_connection_notifications', (YLeaf(YType.uint32, 'start-control-connection-notifications'), ['int'])),
                                ('stop_control_connection_notifications', (YLeaf(YType.uint32, 'stop-control-connection-notifications'), ['int'])),
                                ('hello_packets', (YLeaf(YType.uint32, 'hello-packets'), ['int'])),
                                ('outgoing_call_requests', (YLeaf(YType.uint32, 'outgoing-call-requests'), ['int'])),
                                ('outgoing_call_replies', (YLeaf(YType.uint32, 'outgoing-call-replies'), ['int'])),
                                ('outgoing_call_connected_packets', (YLeaf(YType.uint32, 'outgoing-call-connected-packets'), ['int'])),
                                ('incoming_call_requests', (YLeaf(YType.uint32, 'incoming-call-requests'), ['int'])),
                                ('incoming_call_replies', (YLeaf(YType.uint32, 'incoming-call-replies'), ['int'])),
                                ('incoming_call_connected_packets', (YLeaf(YType.uint32, 'incoming-call-connected-packets'), ['int'])),
                                ('call_disconnect_notify_packets', (YLeaf(YType.uint32, 'call-disconnect-notify-packets'), ['int'])),
                                ('wan_error_notify_packets', (YLeaf(YType.uint32, 'wan-error-notify-packets'), ['int'])),
                                ('set_link_info_packets', (YLeaf(YType.uint32, 'set-link-info-packets'), ['int'])),
                                ('service_relay_requests', (YLeaf(YType.uint32, 'service-relay-requests'), ['int'])),
                                ('service_relay_replies', (YLeaf(YType.uint32, 'service-relay-replies'), ['int'])),
                                ('acknowledgement_packets', (YLeaf(YType.uint32, 'acknowledgement-packets'), ['int'])),
                            ])
                            self.unknown_packets = None
                            self.zero_length_body_packets = None
                            self.start_control_connection_requests = None
                            self.start_control_connection_replies = None
                            self.start_control_connection_notifications = None
                            self.stop_control_connection_notifications = None
                            self.hello_packets = None
                            self.outgoing_call_requests = None
                            self.outgoing_call_replies = None
                            self.outgoing_call_connected_packets = None
                            self.incoming_call_requests = None
                            self.incoming_call_replies = None
                            self.incoming_call_connected_packets = None
                            self.call_disconnect_notify_packets = None
                            self.wan_error_notify_packets = None
                            self.set_link_info_packets = None
                            self.service_relay_requests = None
                            self.service_relay_replies = None
                            self.acknowledgement_packets = None
                            self._segment_path = lambda: "drop"
                            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/counters/control/tunnel-xr/global/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2tp.Counters.Control.TunnelXr.Global.Drop, [u'unknown_packets', u'zero_length_body_packets', u'start_control_connection_requests', u'start_control_connection_replies', u'start_control_connection_notifications', u'stop_control_connection_notifications', u'hello_packets', u'outgoing_call_requests', u'outgoing_call_replies', u'outgoing_call_connected_packets', u'incoming_call_requests', u'incoming_call_replies', u'incoming_call_connected_packets', u'call_disconnect_notify_packets', u'wan_error_notify_packets', u'set_link_info_packets', u'service_relay_requests', u'service_relay_replies', u'acknowledgement_packets'], name, value)


            class Tunnels(Entity):
                """
                Table of tunnel IDs of control message counters
                
                .. attribute:: tunnel
                
                	L2TP tunnel control message counters
                	**type**\: list of  		 :py:class:`Tunnel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Counters.Control.Tunnels.Tunnel>`
                
                

                """

                _prefix = 'tunnel-l2tun-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(L2tp.Counters.Control.Tunnels, self).__init__()

                    self.yang_name = "tunnels"
                    self.yang_parent_name = "control"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("tunnel", ("tunnel", L2tp.Counters.Control.Tunnels.Tunnel))])
                    self._leafs = OrderedDict()

                    self.tunnel = YList(self)
                    self._segment_path = lambda: "tunnels"
                    self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/counters/control/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(L2tp.Counters.Control.Tunnels, [], name, value)


                class Tunnel(Entity):
                    """
                    L2TP tunnel control message counters
                    
                    .. attribute:: tunnel_id  (key)
                    
                    	L2TP tunnel ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: brief
                    
                    	L2TP control message local and remote addresses
                    	**type**\:  :py:class:`Brief <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Counters.Control.Tunnels.Tunnel.Brief>`
                    
                    .. attribute:: global_
                    
                    	Global data
                    	**type**\:  :py:class:`Global <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Counters.Control.Tunnels.Tunnel.Global>`
                    
                    

                    """

                    _prefix = 'tunnel-l2tun-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(L2tp.Counters.Control.Tunnels.Tunnel, self).__init__()

                        self.yang_name = "tunnel"
                        self.yang_parent_name = "tunnels"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['tunnel_id']
                        self._child_classes = OrderedDict([("brief", ("brief", L2tp.Counters.Control.Tunnels.Tunnel.Brief)), ("global", ("global_", L2tp.Counters.Control.Tunnels.Tunnel.Global))])
                        self._leafs = OrderedDict([
                            ('tunnel_id', (YLeaf(YType.uint32, 'tunnel-id'), ['int'])),
                        ])
                        self.tunnel_id = None

                        self.brief = L2tp.Counters.Control.Tunnels.Tunnel.Brief()
                        self.brief.parent = self
                        self._children_name_map["brief"] = "brief"

                        self.global_ = L2tp.Counters.Control.Tunnels.Tunnel.Global()
                        self.global_.parent = self
                        self._children_name_map["global_"] = "global"
                        self._segment_path = lambda: "tunnel" + "[tunnel-id='" + str(self.tunnel_id) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/counters/control/tunnels/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2tp.Counters.Control.Tunnels.Tunnel, ['tunnel_id'], name, value)


                    class Brief(Entity):
                        """
                        L2TP control message local and remote addresses
                        
                        .. attribute:: remote_tunnel_id
                        
                        	Remote tunnel ID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: local_address
                        
                        	Local IP address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: remote_address
                        
                        	Remote IP address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'tunnel-l2tun-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(L2tp.Counters.Control.Tunnels.Tunnel.Brief, self).__init__()

                            self.yang_name = "brief"
                            self.yang_parent_name = "tunnel"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('remote_tunnel_id', (YLeaf(YType.uint32, 'remote-tunnel-id'), ['int'])),
                                ('local_address', (YLeaf(YType.str, 'local-address'), ['str'])),
                                ('remote_address', (YLeaf(YType.str, 'remote-address'), ['str'])),
                            ])
                            self.remote_tunnel_id = None
                            self.local_address = None
                            self.remote_address = None
                            self._segment_path = lambda: "brief"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2tp.Counters.Control.Tunnels.Tunnel.Brief, [u'remote_tunnel_id', u'local_address', u'remote_address'], name, value)


                    class Global(Entity):
                        """
                        Global data
                        
                        .. attribute:: transmit
                        
                        	Transmit data
                        	**type**\:  :py:class:`Transmit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Counters.Control.Tunnels.Tunnel.Global.Transmit>`
                        
                        .. attribute:: retransmit
                        
                        	Re transmit data
                        	**type**\:  :py:class:`Retransmit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Counters.Control.Tunnels.Tunnel.Global.Retransmit>`
                        
                        .. attribute:: received
                        
                        	Received data
                        	**type**\:  :py:class:`Received <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Counters.Control.Tunnels.Tunnel.Global.Received>`
                        
                        .. attribute:: drop
                        
                        	Drop data
                        	**type**\:  :py:class:`Drop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Counters.Control.Tunnels.Tunnel.Global.Drop>`
                        
                        .. attribute:: total_transmit
                        
                        	Total transmit
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: total_retransmit
                        
                        	Total retransmit
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: total_received
                        
                        	Total received
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: total_drop
                        
                        	Total drop
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'tunnel-l2tun-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(L2tp.Counters.Control.Tunnels.Tunnel.Global, self).__init__()

                            self.yang_name = "global"
                            self.yang_parent_name = "tunnel"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("transmit", ("transmit", L2tp.Counters.Control.Tunnels.Tunnel.Global.Transmit)), ("retransmit", ("retransmit", L2tp.Counters.Control.Tunnels.Tunnel.Global.Retransmit)), ("received", ("received", L2tp.Counters.Control.Tunnels.Tunnel.Global.Received)), ("drop", ("drop", L2tp.Counters.Control.Tunnels.Tunnel.Global.Drop))])
                            self._leafs = OrderedDict([
                                ('total_transmit', (YLeaf(YType.uint32, 'total-transmit'), ['int'])),
                                ('total_retransmit', (YLeaf(YType.uint32, 'total-retransmit'), ['int'])),
                                ('total_received', (YLeaf(YType.uint32, 'total-received'), ['int'])),
                                ('total_drop', (YLeaf(YType.uint32, 'total-drop'), ['int'])),
                            ])
                            self.total_transmit = None
                            self.total_retransmit = None
                            self.total_received = None
                            self.total_drop = None

                            self.transmit = L2tp.Counters.Control.Tunnels.Tunnel.Global.Transmit()
                            self.transmit.parent = self
                            self._children_name_map["transmit"] = "transmit"

                            self.retransmit = L2tp.Counters.Control.Tunnels.Tunnel.Global.Retransmit()
                            self.retransmit.parent = self
                            self._children_name_map["retransmit"] = "retransmit"

                            self.received = L2tp.Counters.Control.Tunnels.Tunnel.Global.Received()
                            self.received.parent = self
                            self._children_name_map["received"] = "received"

                            self.drop = L2tp.Counters.Control.Tunnels.Tunnel.Global.Drop()
                            self.drop.parent = self
                            self._children_name_map["drop"] = "drop"
                            self._segment_path = lambda: "global"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2tp.Counters.Control.Tunnels.Tunnel.Global, [u'total_transmit', u'total_retransmit', u'total_received', u'total_drop'], name, value)


                        class Transmit(Entity):
                            """
                            Transmit data
                            
                            .. attribute:: unknown_packets
                            
                            	Unknown packets
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: zero_length_body_packets
                            
                            	Zero length body packets
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: start_control_connection_requests
                            
                            	Start control connection requests
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: start_control_connection_replies
                            
                            	Start control connection replies
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: start_control_connection_notifications
                            
                            	Start control connection notifications
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: stop_control_connection_notifications
                            
                            	Stop control connection notifications
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: hello_packets
                            
                            	Keep alive messages
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: outgoing_call_requests
                            
                            	Outgoing call requests
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: outgoing_call_replies
                            
                            	Outgoing call replies
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: outgoing_call_connected_packets
                            
                            	Outgoing call connected packets
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: incoming_call_requests
                            
                            	Incoming call requests
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: incoming_call_replies
                            
                            	Incoming call replies
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: incoming_call_connected_packets
                            
                            	Incoming call connected packets
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: call_disconnect_notify_packets
                            
                            	Call disconnect notify packets
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: wan_error_notify_packets
                            
                            	WAN error notify packets
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: set_link_info_packets
                            
                            	Set link info packets
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: service_relay_requests
                            
                            	Service relay request counts
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: service_relay_replies
                            
                            	Service relay reply counts
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: acknowledgement_packets
                            
                            	Packets acknowledgement
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'tunnel-l2tun-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(L2tp.Counters.Control.Tunnels.Tunnel.Global.Transmit, self).__init__()

                                self.yang_name = "transmit"
                                self.yang_parent_name = "global"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('unknown_packets', (YLeaf(YType.uint32, 'unknown-packets'), ['int'])),
                                    ('zero_length_body_packets', (YLeaf(YType.uint32, 'zero-length-body-packets'), ['int'])),
                                    ('start_control_connection_requests', (YLeaf(YType.uint32, 'start-control-connection-requests'), ['int'])),
                                    ('start_control_connection_replies', (YLeaf(YType.uint32, 'start-control-connection-replies'), ['int'])),
                                    ('start_control_connection_notifications', (YLeaf(YType.uint32, 'start-control-connection-notifications'), ['int'])),
                                    ('stop_control_connection_notifications', (YLeaf(YType.uint32, 'stop-control-connection-notifications'), ['int'])),
                                    ('hello_packets', (YLeaf(YType.uint32, 'hello-packets'), ['int'])),
                                    ('outgoing_call_requests', (YLeaf(YType.uint32, 'outgoing-call-requests'), ['int'])),
                                    ('outgoing_call_replies', (YLeaf(YType.uint32, 'outgoing-call-replies'), ['int'])),
                                    ('outgoing_call_connected_packets', (YLeaf(YType.uint32, 'outgoing-call-connected-packets'), ['int'])),
                                    ('incoming_call_requests', (YLeaf(YType.uint32, 'incoming-call-requests'), ['int'])),
                                    ('incoming_call_replies', (YLeaf(YType.uint32, 'incoming-call-replies'), ['int'])),
                                    ('incoming_call_connected_packets', (YLeaf(YType.uint32, 'incoming-call-connected-packets'), ['int'])),
                                    ('call_disconnect_notify_packets', (YLeaf(YType.uint32, 'call-disconnect-notify-packets'), ['int'])),
                                    ('wan_error_notify_packets', (YLeaf(YType.uint32, 'wan-error-notify-packets'), ['int'])),
                                    ('set_link_info_packets', (YLeaf(YType.uint32, 'set-link-info-packets'), ['int'])),
                                    ('service_relay_requests', (YLeaf(YType.uint32, 'service-relay-requests'), ['int'])),
                                    ('service_relay_replies', (YLeaf(YType.uint32, 'service-relay-replies'), ['int'])),
                                    ('acknowledgement_packets', (YLeaf(YType.uint32, 'acknowledgement-packets'), ['int'])),
                                ])
                                self.unknown_packets = None
                                self.zero_length_body_packets = None
                                self.start_control_connection_requests = None
                                self.start_control_connection_replies = None
                                self.start_control_connection_notifications = None
                                self.stop_control_connection_notifications = None
                                self.hello_packets = None
                                self.outgoing_call_requests = None
                                self.outgoing_call_replies = None
                                self.outgoing_call_connected_packets = None
                                self.incoming_call_requests = None
                                self.incoming_call_replies = None
                                self.incoming_call_connected_packets = None
                                self.call_disconnect_notify_packets = None
                                self.wan_error_notify_packets = None
                                self.set_link_info_packets = None
                                self.service_relay_requests = None
                                self.service_relay_replies = None
                                self.acknowledgement_packets = None
                                self._segment_path = lambda: "transmit"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2tp.Counters.Control.Tunnels.Tunnel.Global.Transmit, [u'unknown_packets', u'zero_length_body_packets', u'start_control_connection_requests', u'start_control_connection_replies', u'start_control_connection_notifications', u'stop_control_connection_notifications', u'hello_packets', u'outgoing_call_requests', u'outgoing_call_replies', u'outgoing_call_connected_packets', u'incoming_call_requests', u'incoming_call_replies', u'incoming_call_connected_packets', u'call_disconnect_notify_packets', u'wan_error_notify_packets', u'set_link_info_packets', u'service_relay_requests', u'service_relay_replies', u'acknowledgement_packets'], name, value)


                        class Retransmit(Entity):
                            """
                            Re transmit data
                            
                            .. attribute:: unknown_packets
                            
                            	Unknown packets
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: zero_length_body_packets
                            
                            	Zero length body packets
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: start_control_connection_requests
                            
                            	Start control connection requests
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: start_control_connection_replies
                            
                            	Start control connection replies
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: start_control_connection_notifications
                            
                            	Start control connection notifications
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: stop_control_connection_notifications
                            
                            	Stop control connection notifications
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: hello_packets
                            
                            	Keep alive messages
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: outgoing_call_requests
                            
                            	Outgoing call requests
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: outgoing_call_replies
                            
                            	Outgoing call replies
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: outgoing_call_connected_packets
                            
                            	Outgoing call connected packets
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: incoming_call_requests
                            
                            	Incoming call requests
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: incoming_call_replies
                            
                            	Incoming call replies
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: incoming_call_connected_packets
                            
                            	Incoming call connected packets
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: call_disconnect_notify_packets
                            
                            	Call disconnect notify packets
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: wan_error_notify_packets
                            
                            	WAN error notify packets
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: set_link_info_packets
                            
                            	Set link info packets
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: service_relay_requests
                            
                            	Service relay request counts
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: service_relay_replies
                            
                            	Service relay reply counts
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: acknowledgement_packets
                            
                            	Packets acknowledgement
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'tunnel-l2tun-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(L2tp.Counters.Control.Tunnels.Tunnel.Global.Retransmit, self).__init__()

                                self.yang_name = "retransmit"
                                self.yang_parent_name = "global"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('unknown_packets', (YLeaf(YType.uint32, 'unknown-packets'), ['int'])),
                                    ('zero_length_body_packets', (YLeaf(YType.uint32, 'zero-length-body-packets'), ['int'])),
                                    ('start_control_connection_requests', (YLeaf(YType.uint32, 'start-control-connection-requests'), ['int'])),
                                    ('start_control_connection_replies', (YLeaf(YType.uint32, 'start-control-connection-replies'), ['int'])),
                                    ('start_control_connection_notifications', (YLeaf(YType.uint32, 'start-control-connection-notifications'), ['int'])),
                                    ('stop_control_connection_notifications', (YLeaf(YType.uint32, 'stop-control-connection-notifications'), ['int'])),
                                    ('hello_packets', (YLeaf(YType.uint32, 'hello-packets'), ['int'])),
                                    ('outgoing_call_requests', (YLeaf(YType.uint32, 'outgoing-call-requests'), ['int'])),
                                    ('outgoing_call_replies', (YLeaf(YType.uint32, 'outgoing-call-replies'), ['int'])),
                                    ('outgoing_call_connected_packets', (YLeaf(YType.uint32, 'outgoing-call-connected-packets'), ['int'])),
                                    ('incoming_call_requests', (YLeaf(YType.uint32, 'incoming-call-requests'), ['int'])),
                                    ('incoming_call_replies', (YLeaf(YType.uint32, 'incoming-call-replies'), ['int'])),
                                    ('incoming_call_connected_packets', (YLeaf(YType.uint32, 'incoming-call-connected-packets'), ['int'])),
                                    ('call_disconnect_notify_packets', (YLeaf(YType.uint32, 'call-disconnect-notify-packets'), ['int'])),
                                    ('wan_error_notify_packets', (YLeaf(YType.uint32, 'wan-error-notify-packets'), ['int'])),
                                    ('set_link_info_packets', (YLeaf(YType.uint32, 'set-link-info-packets'), ['int'])),
                                    ('service_relay_requests', (YLeaf(YType.uint32, 'service-relay-requests'), ['int'])),
                                    ('service_relay_replies', (YLeaf(YType.uint32, 'service-relay-replies'), ['int'])),
                                    ('acknowledgement_packets', (YLeaf(YType.uint32, 'acknowledgement-packets'), ['int'])),
                                ])
                                self.unknown_packets = None
                                self.zero_length_body_packets = None
                                self.start_control_connection_requests = None
                                self.start_control_connection_replies = None
                                self.start_control_connection_notifications = None
                                self.stop_control_connection_notifications = None
                                self.hello_packets = None
                                self.outgoing_call_requests = None
                                self.outgoing_call_replies = None
                                self.outgoing_call_connected_packets = None
                                self.incoming_call_requests = None
                                self.incoming_call_replies = None
                                self.incoming_call_connected_packets = None
                                self.call_disconnect_notify_packets = None
                                self.wan_error_notify_packets = None
                                self.set_link_info_packets = None
                                self.service_relay_requests = None
                                self.service_relay_replies = None
                                self.acknowledgement_packets = None
                                self._segment_path = lambda: "retransmit"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2tp.Counters.Control.Tunnels.Tunnel.Global.Retransmit, [u'unknown_packets', u'zero_length_body_packets', u'start_control_connection_requests', u'start_control_connection_replies', u'start_control_connection_notifications', u'stop_control_connection_notifications', u'hello_packets', u'outgoing_call_requests', u'outgoing_call_replies', u'outgoing_call_connected_packets', u'incoming_call_requests', u'incoming_call_replies', u'incoming_call_connected_packets', u'call_disconnect_notify_packets', u'wan_error_notify_packets', u'set_link_info_packets', u'service_relay_requests', u'service_relay_replies', u'acknowledgement_packets'], name, value)


                        class Received(Entity):
                            """
                            Received data
                            
                            .. attribute:: unknown_packets
                            
                            	Unknown packets
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: zero_length_body_packets
                            
                            	Zero length body packets
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: start_control_connection_requests
                            
                            	Start control connection requests
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: start_control_connection_replies
                            
                            	Start control connection replies
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: start_control_connection_notifications
                            
                            	Start control connection notifications
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: stop_control_connection_notifications
                            
                            	Stop control connection notifications
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: hello_packets
                            
                            	Keep alive messages
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: outgoing_call_requests
                            
                            	Outgoing call requests
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: outgoing_call_replies
                            
                            	Outgoing call replies
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: outgoing_call_connected_packets
                            
                            	Outgoing call connected packets
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: incoming_call_requests
                            
                            	Incoming call requests
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: incoming_call_replies
                            
                            	Incoming call replies
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: incoming_call_connected_packets
                            
                            	Incoming call connected packets
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: call_disconnect_notify_packets
                            
                            	Call disconnect notify packets
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: wan_error_notify_packets
                            
                            	WAN error notify packets
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: set_link_info_packets
                            
                            	Set link info packets
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: service_relay_requests
                            
                            	Service relay request counts
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: service_relay_replies
                            
                            	Service relay reply counts
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: acknowledgement_packets
                            
                            	Packets acknowledgement
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'tunnel-l2tun-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(L2tp.Counters.Control.Tunnels.Tunnel.Global.Received, self).__init__()

                                self.yang_name = "received"
                                self.yang_parent_name = "global"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('unknown_packets', (YLeaf(YType.uint32, 'unknown-packets'), ['int'])),
                                    ('zero_length_body_packets', (YLeaf(YType.uint32, 'zero-length-body-packets'), ['int'])),
                                    ('start_control_connection_requests', (YLeaf(YType.uint32, 'start-control-connection-requests'), ['int'])),
                                    ('start_control_connection_replies', (YLeaf(YType.uint32, 'start-control-connection-replies'), ['int'])),
                                    ('start_control_connection_notifications', (YLeaf(YType.uint32, 'start-control-connection-notifications'), ['int'])),
                                    ('stop_control_connection_notifications', (YLeaf(YType.uint32, 'stop-control-connection-notifications'), ['int'])),
                                    ('hello_packets', (YLeaf(YType.uint32, 'hello-packets'), ['int'])),
                                    ('outgoing_call_requests', (YLeaf(YType.uint32, 'outgoing-call-requests'), ['int'])),
                                    ('outgoing_call_replies', (YLeaf(YType.uint32, 'outgoing-call-replies'), ['int'])),
                                    ('outgoing_call_connected_packets', (YLeaf(YType.uint32, 'outgoing-call-connected-packets'), ['int'])),
                                    ('incoming_call_requests', (YLeaf(YType.uint32, 'incoming-call-requests'), ['int'])),
                                    ('incoming_call_replies', (YLeaf(YType.uint32, 'incoming-call-replies'), ['int'])),
                                    ('incoming_call_connected_packets', (YLeaf(YType.uint32, 'incoming-call-connected-packets'), ['int'])),
                                    ('call_disconnect_notify_packets', (YLeaf(YType.uint32, 'call-disconnect-notify-packets'), ['int'])),
                                    ('wan_error_notify_packets', (YLeaf(YType.uint32, 'wan-error-notify-packets'), ['int'])),
                                    ('set_link_info_packets', (YLeaf(YType.uint32, 'set-link-info-packets'), ['int'])),
                                    ('service_relay_requests', (YLeaf(YType.uint32, 'service-relay-requests'), ['int'])),
                                    ('service_relay_replies', (YLeaf(YType.uint32, 'service-relay-replies'), ['int'])),
                                    ('acknowledgement_packets', (YLeaf(YType.uint32, 'acknowledgement-packets'), ['int'])),
                                ])
                                self.unknown_packets = None
                                self.zero_length_body_packets = None
                                self.start_control_connection_requests = None
                                self.start_control_connection_replies = None
                                self.start_control_connection_notifications = None
                                self.stop_control_connection_notifications = None
                                self.hello_packets = None
                                self.outgoing_call_requests = None
                                self.outgoing_call_replies = None
                                self.outgoing_call_connected_packets = None
                                self.incoming_call_requests = None
                                self.incoming_call_replies = None
                                self.incoming_call_connected_packets = None
                                self.call_disconnect_notify_packets = None
                                self.wan_error_notify_packets = None
                                self.set_link_info_packets = None
                                self.service_relay_requests = None
                                self.service_relay_replies = None
                                self.acknowledgement_packets = None
                                self._segment_path = lambda: "received"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2tp.Counters.Control.Tunnels.Tunnel.Global.Received, [u'unknown_packets', u'zero_length_body_packets', u'start_control_connection_requests', u'start_control_connection_replies', u'start_control_connection_notifications', u'stop_control_connection_notifications', u'hello_packets', u'outgoing_call_requests', u'outgoing_call_replies', u'outgoing_call_connected_packets', u'incoming_call_requests', u'incoming_call_replies', u'incoming_call_connected_packets', u'call_disconnect_notify_packets', u'wan_error_notify_packets', u'set_link_info_packets', u'service_relay_requests', u'service_relay_replies', u'acknowledgement_packets'], name, value)


                        class Drop(Entity):
                            """
                            Drop data
                            
                            .. attribute:: unknown_packets
                            
                            	Unknown packets
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: zero_length_body_packets
                            
                            	Zero length body packets
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: start_control_connection_requests
                            
                            	Start control connection requests
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: start_control_connection_replies
                            
                            	Start control connection replies
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: start_control_connection_notifications
                            
                            	Start control connection notifications
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: stop_control_connection_notifications
                            
                            	Stop control connection notifications
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: hello_packets
                            
                            	Keep alive messages
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: outgoing_call_requests
                            
                            	Outgoing call requests
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: outgoing_call_replies
                            
                            	Outgoing call replies
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: outgoing_call_connected_packets
                            
                            	Outgoing call connected packets
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: incoming_call_requests
                            
                            	Incoming call requests
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: incoming_call_replies
                            
                            	Incoming call replies
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: incoming_call_connected_packets
                            
                            	Incoming call connected packets
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: call_disconnect_notify_packets
                            
                            	Call disconnect notify packets
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: wan_error_notify_packets
                            
                            	WAN error notify packets
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: set_link_info_packets
                            
                            	Set link info packets
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: service_relay_requests
                            
                            	Service relay request counts
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: service_relay_replies
                            
                            	Service relay reply counts
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: acknowledgement_packets
                            
                            	Packets acknowledgement
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'tunnel-l2tun-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(L2tp.Counters.Control.Tunnels.Tunnel.Global.Drop, self).__init__()

                                self.yang_name = "drop"
                                self.yang_parent_name = "global"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('unknown_packets', (YLeaf(YType.uint32, 'unknown-packets'), ['int'])),
                                    ('zero_length_body_packets', (YLeaf(YType.uint32, 'zero-length-body-packets'), ['int'])),
                                    ('start_control_connection_requests', (YLeaf(YType.uint32, 'start-control-connection-requests'), ['int'])),
                                    ('start_control_connection_replies', (YLeaf(YType.uint32, 'start-control-connection-replies'), ['int'])),
                                    ('start_control_connection_notifications', (YLeaf(YType.uint32, 'start-control-connection-notifications'), ['int'])),
                                    ('stop_control_connection_notifications', (YLeaf(YType.uint32, 'stop-control-connection-notifications'), ['int'])),
                                    ('hello_packets', (YLeaf(YType.uint32, 'hello-packets'), ['int'])),
                                    ('outgoing_call_requests', (YLeaf(YType.uint32, 'outgoing-call-requests'), ['int'])),
                                    ('outgoing_call_replies', (YLeaf(YType.uint32, 'outgoing-call-replies'), ['int'])),
                                    ('outgoing_call_connected_packets', (YLeaf(YType.uint32, 'outgoing-call-connected-packets'), ['int'])),
                                    ('incoming_call_requests', (YLeaf(YType.uint32, 'incoming-call-requests'), ['int'])),
                                    ('incoming_call_replies', (YLeaf(YType.uint32, 'incoming-call-replies'), ['int'])),
                                    ('incoming_call_connected_packets', (YLeaf(YType.uint32, 'incoming-call-connected-packets'), ['int'])),
                                    ('call_disconnect_notify_packets', (YLeaf(YType.uint32, 'call-disconnect-notify-packets'), ['int'])),
                                    ('wan_error_notify_packets', (YLeaf(YType.uint32, 'wan-error-notify-packets'), ['int'])),
                                    ('set_link_info_packets', (YLeaf(YType.uint32, 'set-link-info-packets'), ['int'])),
                                    ('service_relay_requests', (YLeaf(YType.uint32, 'service-relay-requests'), ['int'])),
                                    ('service_relay_replies', (YLeaf(YType.uint32, 'service-relay-replies'), ['int'])),
                                    ('acknowledgement_packets', (YLeaf(YType.uint32, 'acknowledgement-packets'), ['int'])),
                                ])
                                self.unknown_packets = None
                                self.zero_length_body_packets = None
                                self.start_control_connection_requests = None
                                self.start_control_connection_replies = None
                                self.start_control_connection_notifications = None
                                self.stop_control_connection_notifications = None
                                self.hello_packets = None
                                self.outgoing_call_requests = None
                                self.outgoing_call_replies = None
                                self.outgoing_call_connected_packets = None
                                self.incoming_call_requests = None
                                self.incoming_call_replies = None
                                self.incoming_call_connected_packets = None
                                self.call_disconnect_notify_packets = None
                                self.wan_error_notify_packets = None
                                self.set_link_info_packets = None
                                self.service_relay_requests = None
                                self.service_relay_replies = None
                                self.acknowledgement_packets = None
                                self._segment_path = lambda: "drop"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2tp.Counters.Control.Tunnels.Tunnel.Global.Drop, [u'unknown_packets', u'zero_length_body_packets', u'start_control_connection_requests', u'start_control_connection_replies', u'start_control_connection_notifications', u'stop_control_connection_notifications', u'hello_packets', u'outgoing_call_requests', u'outgoing_call_replies', u'outgoing_call_connected_packets', u'incoming_call_requests', u'incoming_call_replies', u'incoming_call_connected_packets', u'call_disconnect_notify_packets', u'wan_error_notify_packets', u'set_link_info_packets', u'service_relay_requests', u'service_relay_replies', u'acknowledgement_packets'], name, value)


    class TunnelConfigurations(Entity):
        """
        List of tunnel IDs
        
        .. attribute:: tunnel_configuration
        
        	L2TP tunnel information
        	**type**\: list of  		 :py:class:`TunnelConfiguration <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.TunnelConfigurations.TunnelConfiguration>`
        
        

        """

        _prefix = 'tunnel-l2tun-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(L2tp.TunnelConfigurations, self).__init__()

            self.yang_name = "tunnel-configurations"
            self.yang_parent_name = "l2tp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("tunnel-configuration", ("tunnel_configuration", L2tp.TunnelConfigurations.TunnelConfiguration))])
            self._leafs = OrderedDict()

            self.tunnel_configuration = YList(self)
            self._segment_path = lambda: "tunnel-configurations"
            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(L2tp.TunnelConfigurations, [], name, value)


        class TunnelConfiguration(Entity):
            """
            L2TP tunnel information
            
            .. attribute:: local_tunnel_id  (key)
            
            	Local tunnel ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: l2tp_class
            
            	L2Tp class data
            	**type**\:  :py:class:`L2tpClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.TunnelConfigurations.TunnelConfiguration.L2tpClass>`
            
            .. attribute:: remote_tunnel_id
            
            	Remote tunnel ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'tunnel-l2tun-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(L2tp.TunnelConfigurations.TunnelConfiguration, self).__init__()

                self.yang_name = "tunnel-configuration"
                self.yang_parent_name = "tunnel-configurations"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['local_tunnel_id']
                self._child_classes = OrderedDict([("l2tp-class", ("l2tp_class", L2tp.TunnelConfigurations.TunnelConfiguration.L2tpClass))])
                self._leafs = OrderedDict([
                    ('local_tunnel_id', (YLeaf(YType.uint32, 'local-tunnel-id'), ['int'])),
                    ('remote_tunnel_id', (YLeaf(YType.uint32, 'remote-tunnel-id'), ['int'])),
                ])
                self.local_tunnel_id = None
                self.remote_tunnel_id = None

                self.l2tp_class = L2tp.TunnelConfigurations.TunnelConfiguration.L2tpClass()
                self.l2tp_class.parent = self
                self._children_name_map["l2tp_class"] = "l2tp-class"
                self._segment_path = lambda: "tunnel-configuration" + "[local-tunnel-id='" + str(self.local_tunnel_id) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/tunnel-configurations/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(L2tp.TunnelConfigurations.TunnelConfiguration, ['local_tunnel_id', u'remote_tunnel_id'], name, value)


            class L2tpClass(Entity):
                """
                L2Tp class data
                
                .. attribute:: ip_tos
                
                	IP TOS
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: vrf_name
                
                	VRF name
                	**type**\: str
                
                	**length:** 0..256
                
                .. attribute:: receive_window_size
                
                	Receive window size
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: class_name_xr
                
                	Class name
                	**type**\: str
                
                	**length:** 0..256
                
                .. attribute:: digest_hash
                
                	Hash configured as MD5 or SHA1
                	**type**\:  :py:class:`DigestHash <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.DigestHash>`
                
                .. attribute:: password
                
                	Password
                	**type**\: str
                
                	**length:** 0..25
                
                .. attribute:: encoded_password
                
                	Encoded password
                	**type**\: str
                
                	**length:** 0..256
                
                .. attribute:: host_name
                
                	Host name
                	**type**\: str
                
                	**length:** 0..256
                
                .. attribute:: accounting_method_list
                
                	Accounting List
                	**type**\: str
                
                	**length:** 0..256
                
                .. attribute:: hello_timeout
                
                	Hello timeout value in seconds
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: setup_timeout
                
                	Timeout setup value in seconds
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: retransmit_minimum_timeout
                
                	Retransmit minimum timeout in seconds
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: retransmit_maximum_timeout
                
                	Retransmit maximum timeout in seconds
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: initial_retransmit_minimum_timeout
                
                	Initial timeout minimum in seconds
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: initial_retransmit_maximum_timeout
                
                	Initial timeout maximum in seconds
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: timeout_no_user
                
                	Timeout no user
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: retransmit_retries
                
                	Retransmit retries
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: initial_retransmit_retries
                
                	Initial retransmit retries
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: is_authentication_enabled
                
                	True if authentication is enabled
                	**type**\: bool
                
                .. attribute:: is_hidden
                
                	True if class is hidden
                	**type**\: bool
                
                .. attribute:: is_digest_enabled
                
                	True if digest authentication is enabled
                	**type**\: bool
                
                .. attribute:: is_digest_check_enabled
                
                	True if digest check is enabled
                	**type**\: bool
                
                .. attribute:: is_congestion_control_enabled
                
                	True if congestion control is enabled
                	**type**\: bool
                
                .. attribute:: is_peer_address_checked
                
                	True if peer address is checked
                	**type**\: bool
                
                

                """

                _prefix = 'tunnel-l2tun-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(L2tp.TunnelConfigurations.TunnelConfiguration.L2tpClass, self).__init__()

                    self.yang_name = "l2tp-class"
                    self.yang_parent_name = "tunnel-configuration"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('ip_tos', (YLeaf(YType.uint8, 'ip-tos'), ['int'])),
                        ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                        ('receive_window_size', (YLeaf(YType.uint16, 'receive-window-size'), ['int'])),
                        ('class_name_xr', (YLeaf(YType.str, 'class-name-xr'), ['str'])),
                        ('digest_hash', (YLeaf(YType.enumeration, 'digest-hash'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper', 'DigestHash', '')])),
                        ('password', (YLeaf(YType.str, 'password'), ['str'])),
                        ('encoded_password', (YLeaf(YType.str, 'encoded-password'), ['str'])),
                        ('host_name', (YLeaf(YType.str, 'host-name'), ['str'])),
                        ('accounting_method_list', (YLeaf(YType.str, 'accounting-method-list'), ['str'])),
                        ('hello_timeout', (YLeaf(YType.uint32, 'hello-timeout'), ['int'])),
                        ('setup_timeout', (YLeaf(YType.uint32, 'setup-timeout'), ['int'])),
                        ('retransmit_minimum_timeout', (YLeaf(YType.uint32, 'retransmit-minimum-timeout'), ['int'])),
                        ('retransmit_maximum_timeout', (YLeaf(YType.uint32, 'retransmit-maximum-timeout'), ['int'])),
                        ('initial_retransmit_minimum_timeout', (YLeaf(YType.uint32, 'initial-retransmit-minimum-timeout'), ['int'])),
                        ('initial_retransmit_maximum_timeout', (YLeaf(YType.uint32, 'initial-retransmit-maximum-timeout'), ['int'])),
                        ('timeout_no_user', (YLeaf(YType.uint32, 'timeout-no-user'), ['int'])),
                        ('retransmit_retries', (YLeaf(YType.uint32, 'retransmit-retries'), ['int'])),
                        ('initial_retransmit_retries', (YLeaf(YType.uint32, 'initial-retransmit-retries'), ['int'])),
                        ('is_authentication_enabled', (YLeaf(YType.boolean, 'is-authentication-enabled'), ['bool'])),
                        ('is_hidden', (YLeaf(YType.boolean, 'is-hidden'), ['bool'])),
                        ('is_digest_enabled', (YLeaf(YType.boolean, 'is-digest-enabled'), ['bool'])),
                        ('is_digest_check_enabled', (YLeaf(YType.boolean, 'is-digest-check-enabled'), ['bool'])),
                        ('is_congestion_control_enabled', (YLeaf(YType.boolean, 'is-congestion-control-enabled'), ['bool'])),
                        ('is_peer_address_checked', (YLeaf(YType.boolean, 'is-peer-address-checked'), ['bool'])),
                    ])
                    self.ip_tos = None
                    self.vrf_name = None
                    self.receive_window_size = None
                    self.class_name_xr = None
                    self.digest_hash = None
                    self.password = None
                    self.encoded_password = None
                    self.host_name = None
                    self.accounting_method_list = None
                    self.hello_timeout = None
                    self.setup_timeout = None
                    self.retransmit_minimum_timeout = None
                    self.retransmit_maximum_timeout = None
                    self.initial_retransmit_minimum_timeout = None
                    self.initial_retransmit_maximum_timeout = None
                    self.timeout_no_user = None
                    self.retransmit_retries = None
                    self.initial_retransmit_retries = None
                    self.is_authentication_enabled = None
                    self.is_hidden = None
                    self.is_digest_enabled = None
                    self.is_digest_check_enabled = None
                    self.is_congestion_control_enabled = None
                    self.is_peer_address_checked = None
                    self._segment_path = lambda: "l2tp-class"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(L2tp.TunnelConfigurations.TunnelConfiguration.L2tpClass, [u'ip_tos', u'vrf_name', u'receive_window_size', u'class_name_xr', u'digest_hash', u'password', u'encoded_password', u'host_name', u'accounting_method_list', u'hello_timeout', u'setup_timeout', u'retransmit_minimum_timeout', u'retransmit_maximum_timeout', u'initial_retransmit_minimum_timeout', u'initial_retransmit_maximum_timeout', u'timeout_no_user', u'retransmit_retries', u'initial_retransmit_retries', u'is_authentication_enabled', u'is_hidden', u'is_digest_enabled', u'is_digest_check_enabled', u'is_congestion_control_enabled', u'is_peer_address_checked'], name, value)


    class CounterHistFail(Entity):
        """
        Failure events leading to disconnection
        
        .. attribute:: sess_down_tmout
        
        	sesions affected due to timeout
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: tx_counters
        
        	Send side counters
        	**type**\: str
        
        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
        
        .. attribute:: rx_counters
        
        	Receive side counters
        	**type**\: str
        
        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
        
        .. attribute:: pkt_timeout
        
        	timeout events by packet
        	**type**\: list of  		 :py:class:`PktTimeout <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.CounterHistFail.PktTimeout>`
        
        

        """

        _prefix = 'tunnel-l2tun-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(L2tp.CounterHistFail, self).__init__()

            self.yang_name = "counter-hist-fail"
            self.yang_parent_name = "l2tp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("pkt-timeout", ("pkt_timeout", L2tp.CounterHistFail.PktTimeout))])
            self._leafs = OrderedDict([
                ('sess_down_tmout', (YLeaf(YType.uint32, 'sess-down-tmout'), ['int'])),
                ('tx_counters', (YLeaf(YType.str, 'tx-counters'), ['str'])),
                ('rx_counters', (YLeaf(YType.str, 'rx-counters'), ['str'])),
            ])
            self.sess_down_tmout = None
            self.tx_counters = None
            self.rx_counters = None

            self.pkt_timeout = YList(self)
            self._segment_path = lambda: "counter-hist-fail"
            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(L2tp.CounterHistFail, [u'sess_down_tmout', u'tx_counters', u'rx_counters'], name, value)


        class PktTimeout(Entity):
            """
            timeout events by packet
            
            .. attribute:: entry
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'tunnel-l2tun-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(L2tp.CounterHistFail.PktTimeout, self).__init__()

                self.yang_name = "pkt-timeout"
                self.yang_parent_name = "counter-hist-fail"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entry', (YLeaf(YType.uint32, 'entry'), ['int'])),
                ])
                self.entry = None
                self._segment_path = lambda: "pkt-timeout"
                self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/counter-hist-fail/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(L2tp.CounterHistFail.PktTimeout, [u'entry'], name, value)


    class Classes(Entity):
        """
        List of L2TP class names
        
        .. attribute:: class_
        
        	L2TP class name
        	**type**\: list of  		 :py:class:`Class <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Classes.Class>`
        
        

        """

        _prefix = 'tunnel-l2tun-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(L2tp.Classes, self).__init__()

            self.yang_name = "classes"
            self.yang_parent_name = "l2tp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("class", ("class_", L2tp.Classes.Class))])
            self._leafs = OrderedDict()

            self.class_ = YList(self)
            self._segment_path = lambda: "classes"
            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(L2tp.Classes, [], name, value)


        class Class(Entity):
            """
            L2TP class name
            
            .. attribute:: class_name  (key)
            
            	L2TP class name
            	**type**\: str
            
            	**length:** 1..31
            
            .. attribute:: ip_tos
            
            	IP TOS
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: vrf_name
            
            	VRF name
            	**type**\: str
            
            	**length:** 0..256
            
            .. attribute:: receive_window_size
            
            	Receive window size
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: class_name_xr
            
            	Class name
            	**type**\: str
            
            	**length:** 0..256
            
            .. attribute:: digest_hash
            
            	Hash configured as MD5 or SHA1
            	**type**\:  :py:class:`DigestHash <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.DigestHash>`
            
            .. attribute:: password
            
            	Password
            	**type**\: str
            
            	**length:** 0..25
            
            .. attribute:: encoded_password
            
            	Encoded password
            	**type**\: str
            
            	**length:** 0..256
            
            .. attribute:: host_name
            
            	Host name
            	**type**\: str
            
            	**length:** 0..256
            
            .. attribute:: accounting_method_list
            
            	Accounting List
            	**type**\: str
            
            	**length:** 0..256
            
            .. attribute:: hello_timeout
            
            	Hello timeout value in seconds
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: second
            
            .. attribute:: setup_timeout
            
            	Timeout setup value in seconds
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: second
            
            .. attribute:: retransmit_minimum_timeout
            
            	Retransmit minimum timeout in seconds
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: second
            
            .. attribute:: retransmit_maximum_timeout
            
            	Retransmit maximum timeout in seconds
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: second
            
            .. attribute:: initial_retransmit_minimum_timeout
            
            	Initial timeout minimum in seconds
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: second
            
            .. attribute:: initial_retransmit_maximum_timeout
            
            	Initial timeout maximum in seconds
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: second
            
            .. attribute:: timeout_no_user
            
            	Timeout no user
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: retransmit_retries
            
            	Retransmit retries
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: initial_retransmit_retries
            
            	Initial retransmit retries
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: is_authentication_enabled
            
            	True if authentication is enabled
            	**type**\: bool
            
            .. attribute:: is_hidden
            
            	True if class is hidden
            	**type**\: bool
            
            .. attribute:: is_digest_enabled
            
            	True if digest authentication is enabled
            	**type**\: bool
            
            .. attribute:: is_digest_check_enabled
            
            	True if digest check is enabled
            	**type**\: bool
            
            .. attribute:: is_congestion_control_enabled
            
            	True if congestion control is enabled
            	**type**\: bool
            
            .. attribute:: is_peer_address_checked
            
            	True if peer address is checked
            	**type**\: bool
            
            

            """

            _prefix = 'tunnel-l2tun-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(L2tp.Classes.Class, self).__init__()

                self.yang_name = "class"
                self.yang_parent_name = "classes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['class_name']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('class_name', (YLeaf(YType.str, 'class-name'), ['str'])),
                    ('ip_tos', (YLeaf(YType.uint8, 'ip-tos'), ['int'])),
                    ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                    ('receive_window_size', (YLeaf(YType.uint16, 'receive-window-size'), ['int'])),
                    ('class_name_xr', (YLeaf(YType.str, 'class-name-xr'), ['str'])),
                    ('digest_hash', (YLeaf(YType.enumeration, 'digest-hash'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper', 'DigestHash', '')])),
                    ('password', (YLeaf(YType.str, 'password'), ['str'])),
                    ('encoded_password', (YLeaf(YType.str, 'encoded-password'), ['str'])),
                    ('host_name', (YLeaf(YType.str, 'host-name'), ['str'])),
                    ('accounting_method_list', (YLeaf(YType.str, 'accounting-method-list'), ['str'])),
                    ('hello_timeout', (YLeaf(YType.uint32, 'hello-timeout'), ['int'])),
                    ('setup_timeout', (YLeaf(YType.uint32, 'setup-timeout'), ['int'])),
                    ('retransmit_minimum_timeout', (YLeaf(YType.uint32, 'retransmit-minimum-timeout'), ['int'])),
                    ('retransmit_maximum_timeout', (YLeaf(YType.uint32, 'retransmit-maximum-timeout'), ['int'])),
                    ('initial_retransmit_minimum_timeout', (YLeaf(YType.uint32, 'initial-retransmit-minimum-timeout'), ['int'])),
                    ('initial_retransmit_maximum_timeout', (YLeaf(YType.uint32, 'initial-retransmit-maximum-timeout'), ['int'])),
                    ('timeout_no_user', (YLeaf(YType.uint32, 'timeout-no-user'), ['int'])),
                    ('retransmit_retries', (YLeaf(YType.uint32, 'retransmit-retries'), ['int'])),
                    ('initial_retransmit_retries', (YLeaf(YType.uint32, 'initial-retransmit-retries'), ['int'])),
                    ('is_authentication_enabled', (YLeaf(YType.boolean, 'is-authentication-enabled'), ['bool'])),
                    ('is_hidden', (YLeaf(YType.boolean, 'is-hidden'), ['bool'])),
                    ('is_digest_enabled', (YLeaf(YType.boolean, 'is-digest-enabled'), ['bool'])),
                    ('is_digest_check_enabled', (YLeaf(YType.boolean, 'is-digest-check-enabled'), ['bool'])),
                    ('is_congestion_control_enabled', (YLeaf(YType.boolean, 'is-congestion-control-enabled'), ['bool'])),
                    ('is_peer_address_checked', (YLeaf(YType.boolean, 'is-peer-address-checked'), ['bool'])),
                ])
                self.class_name = None
                self.ip_tos = None
                self.vrf_name = None
                self.receive_window_size = None
                self.class_name_xr = None
                self.digest_hash = None
                self.password = None
                self.encoded_password = None
                self.host_name = None
                self.accounting_method_list = None
                self.hello_timeout = None
                self.setup_timeout = None
                self.retransmit_minimum_timeout = None
                self.retransmit_maximum_timeout = None
                self.initial_retransmit_minimum_timeout = None
                self.initial_retransmit_maximum_timeout = None
                self.timeout_no_user = None
                self.retransmit_retries = None
                self.initial_retransmit_retries = None
                self.is_authentication_enabled = None
                self.is_hidden = None
                self.is_digest_enabled = None
                self.is_digest_check_enabled = None
                self.is_congestion_control_enabled = None
                self.is_peer_address_checked = None
                self._segment_path = lambda: "class" + "[class-name='" + str(self.class_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/classes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(L2tp.Classes.Class, ['class_name', u'ip_tos', u'vrf_name', u'receive_window_size', u'class_name_xr', u'digest_hash', u'password', u'encoded_password', u'host_name', u'accounting_method_list', u'hello_timeout', u'setup_timeout', u'retransmit_minimum_timeout', u'retransmit_maximum_timeout', u'initial_retransmit_minimum_timeout', u'initial_retransmit_maximum_timeout', u'timeout_no_user', u'retransmit_retries', u'initial_retransmit_retries', u'is_authentication_enabled', u'is_hidden', u'is_digest_enabled', u'is_digest_check_enabled', u'is_congestion_control_enabled', u'is_peer_address_checked'], name, value)


    class Tunnels(Entity):
        """
        List of tunnel IDs
        
        .. attribute:: tunnel
        
        	L2TP tunnel  information
        	**type**\: list of  		 :py:class:`Tunnel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Tunnels.Tunnel>`
        
        

        """

        _prefix = 'tunnel-l2tun-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(L2tp.Tunnels, self).__init__()

            self.yang_name = "tunnels"
            self.yang_parent_name = "l2tp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("tunnel", ("tunnel", L2tp.Tunnels.Tunnel))])
            self._leafs = OrderedDict()

            self.tunnel = YList(self)
            self._segment_path = lambda: "tunnels"
            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(L2tp.Tunnels, [], name, value)


        class Tunnel(Entity):
            """
            L2TP tunnel  information
            
            .. attribute:: local_tunnel_id  (key)
            
            	Local tunnel ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: local_address
            
            	Local tunnel address
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: remote_address
            
            	Remote tunnel address
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: local_port
            
            	Local port
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: remote_port
            
            	Remote port
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: protocol
            
            	Protocol
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: is_pmtu_enabled
            
            	True if tunnel PMTU checking is enabled
            	**type**\: bool
            
            .. attribute:: remote_tunnel_id
            
            	Remote tunnel ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: local_tunnel_name
            
            	Local tunnel name
            	**type**\: str
            
            	**length:** 0..256
            
            .. attribute:: remote_tunnel_name
            
            	Remote tunnel name
            	**type**\: str
            
            	**length:** 0..256
            
            .. attribute:: class_name
            
            	L2TP class name
            	**type**\: str
            
            	**length:** 0..256
            
            .. attribute:: active_sessions
            
            	Number of active sessions
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sequence_ns
            
            	Sequence NS
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: sequence_nr
            
            	Sequence NR
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: local_window_size
            
            	Local window size
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: remote_window_size
            
            	Remote window size
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: retransmission_time
            
            	Retransmission time in seconds
            	**type**\: int
            
            	**range:** 0..65535
            
            	**units**\: second
            
            .. attribute:: maximum_retransmission_time
            
            	Maximum retransmission time in seconds
            	**type**\: int
            
            	**range:** 0..65535
            
            	**units**\: second
            
            .. attribute:: unsent_queue_size
            
            	Unsent queue size
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: unsent_maximum_queue_size
            
            	Unsent maximum queue size
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: resend_queue_size
            
            	Resend queue size
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: resend_maximum_queue_size
            
            	Resend maximum queue size
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: order_queue_size
            
            	Order queue size
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: packet_queue_check
            
            	Current number session packet queue check
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: digest_secrets
            
            	Control message authentication with digest secrets
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: resends
            
            	Total resends
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: zero_length_body_acknowledgement_sent
            
            	Total zero length body acknowledgement
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: total_out_of_order_drop_packets
            
            	Total out of order dropped packets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: total_out_of_order_reorder_packets
            
            	Total out of order reorder packets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: total_peer_authentication_failures
            
            	Number of peer authentication failures
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: is_tunnel_up
            
            	True if tunnel is up
            	**type**\: bool
            
            .. attribute:: is_congestion_control_enabled
            
            	True if congestion control is enabled else false
            	**type**\: bool
            
            .. attribute:: retransmit_time
            
            	Retransmit time distribution in seconds
            	**type**\: list of  		 :py:class:`RetransmitTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Tunnels.Tunnel.RetransmitTime>`
            
            

            """

            _prefix = 'tunnel-l2tun-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(L2tp.Tunnels.Tunnel, self).__init__()

                self.yang_name = "tunnel"
                self.yang_parent_name = "tunnels"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['local_tunnel_id']
                self._child_classes = OrderedDict([("retransmit-time", ("retransmit_time", L2tp.Tunnels.Tunnel.RetransmitTime))])
                self._leafs = OrderedDict([
                    ('local_tunnel_id', (YLeaf(YType.uint32, 'local-tunnel-id'), ['int'])),
                    ('local_address', (YLeaf(YType.str, 'local-address'), ['str'])),
                    ('remote_address', (YLeaf(YType.str, 'remote-address'), ['str'])),
                    ('local_port', (YLeaf(YType.uint16, 'local-port'), ['int'])),
                    ('remote_port', (YLeaf(YType.uint16, 'remote-port'), ['int'])),
                    ('protocol', (YLeaf(YType.uint8, 'protocol'), ['int'])),
                    ('is_pmtu_enabled', (YLeaf(YType.boolean, 'is-pmtu-enabled'), ['bool'])),
                    ('remote_tunnel_id', (YLeaf(YType.uint32, 'remote-tunnel-id'), ['int'])),
                    ('local_tunnel_name', (YLeaf(YType.str, 'local-tunnel-name'), ['str'])),
                    ('remote_tunnel_name', (YLeaf(YType.str, 'remote-tunnel-name'), ['str'])),
                    ('class_name', (YLeaf(YType.str, 'class-name'), ['str'])),
                    ('active_sessions', (YLeaf(YType.uint32, 'active-sessions'), ['int'])),
                    ('sequence_ns', (YLeaf(YType.uint16, 'sequence-ns'), ['int'])),
                    ('sequence_nr', (YLeaf(YType.uint16, 'sequence-nr'), ['int'])),
                    ('local_window_size', (YLeaf(YType.uint16, 'local-window-size'), ['int'])),
                    ('remote_window_size', (YLeaf(YType.uint16, 'remote-window-size'), ['int'])),
                    ('retransmission_time', (YLeaf(YType.uint16, 'retransmission-time'), ['int'])),
                    ('maximum_retransmission_time', (YLeaf(YType.uint16, 'maximum-retransmission-time'), ['int'])),
                    ('unsent_queue_size', (YLeaf(YType.uint16, 'unsent-queue-size'), ['int'])),
                    ('unsent_maximum_queue_size', (YLeaf(YType.uint16, 'unsent-maximum-queue-size'), ['int'])),
                    ('resend_queue_size', (YLeaf(YType.uint16, 'resend-queue-size'), ['int'])),
                    ('resend_maximum_queue_size', (YLeaf(YType.uint16, 'resend-maximum-queue-size'), ['int'])),
                    ('order_queue_size', (YLeaf(YType.uint16, 'order-queue-size'), ['int'])),
                    ('packet_queue_check', (YLeaf(YType.uint16, 'packet-queue-check'), ['int'])),
                    ('digest_secrets', (YLeaf(YType.uint16, 'digest-secrets'), ['int'])),
                    ('resends', (YLeaf(YType.uint32, 'resends'), ['int'])),
                    ('zero_length_body_acknowledgement_sent', (YLeaf(YType.uint32, 'zero-length-body-acknowledgement-sent'), ['int'])),
                    ('total_out_of_order_drop_packets', (YLeaf(YType.uint32, 'total-out-of-order-drop-packets'), ['int'])),
                    ('total_out_of_order_reorder_packets', (YLeaf(YType.uint32, 'total-out-of-order-reorder-packets'), ['int'])),
                    ('total_peer_authentication_failures', (YLeaf(YType.uint32, 'total-peer-authentication-failures'), ['int'])),
                    ('is_tunnel_up', (YLeaf(YType.boolean, 'is-tunnel-up'), ['bool'])),
                    ('is_congestion_control_enabled', (YLeaf(YType.boolean, 'is-congestion-control-enabled'), ['bool'])),
                ])
                self.local_tunnel_id = None
                self.local_address = None
                self.remote_address = None
                self.local_port = None
                self.remote_port = None
                self.protocol = None
                self.is_pmtu_enabled = None
                self.remote_tunnel_id = None
                self.local_tunnel_name = None
                self.remote_tunnel_name = None
                self.class_name = None
                self.active_sessions = None
                self.sequence_ns = None
                self.sequence_nr = None
                self.local_window_size = None
                self.remote_window_size = None
                self.retransmission_time = None
                self.maximum_retransmission_time = None
                self.unsent_queue_size = None
                self.unsent_maximum_queue_size = None
                self.resend_queue_size = None
                self.resend_maximum_queue_size = None
                self.order_queue_size = None
                self.packet_queue_check = None
                self.digest_secrets = None
                self.resends = None
                self.zero_length_body_acknowledgement_sent = None
                self.total_out_of_order_drop_packets = None
                self.total_out_of_order_reorder_packets = None
                self.total_peer_authentication_failures = None
                self.is_tunnel_up = None
                self.is_congestion_control_enabled = None

                self.retransmit_time = YList(self)
                self._segment_path = lambda: "tunnel" + "[local-tunnel-id='" + str(self.local_tunnel_id) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/tunnels/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(L2tp.Tunnels.Tunnel, ['local_tunnel_id', u'local_address', u'remote_address', u'local_port', u'remote_port', u'protocol', u'is_pmtu_enabled', u'remote_tunnel_id', u'local_tunnel_name', u'remote_tunnel_name', u'class_name', u'active_sessions', u'sequence_ns', u'sequence_nr', u'local_window_size', u'remote_window_size', u'retransmission_time', u'maximum_retransmission_time', u'unsent_queue_size', u'unsent_maximum_queue_size', u'resend_queue_size', u'resend_maximum_queue_size', u'order_queue_size', u'packet_queue_check', u'digest_secrets', u'resends', u'zero_length_body_acknowledgement_sent', u'total_out_of_order_drop_packets', u'total_out_of_order_reorder_packets', u'total_peer_authentication_failures', u'is_tunnel_up', u'is_congestion_control_enabled'], name, value)


            class RetransmitTime(Entity):
                """
                Retransmit time distribution in seconds
                
                .. attribute:: entry
                
                	
                	**type**\: int
                
                	**range:** 0..65535
                
                	**units**\: second
                
                

                """

                _prefix = 'tunnel-l2tun-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(L2tp.Tunnels.Tunnel.RetransmitTime, self).__init__()

                    self.yang_name = "retransmit-time"
                    self.yang_parent_name = "tunnel"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('entry', (YLeaf(YType.uint16, 'entry'), ['int'])),
                    ])
                    self.entry = None
                    self._segment_path = lambda: "retransmit-time"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(L2tp.Tunnels.Tunnel.RetransmitTime, [u'entry'], name, value)


    class Sessions(Entity):
        """
        List of session IDs
        
        .. attribute:: session
        
        	L2TP information for a particular session
        	**type**\: list of  		 :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Sessions.Session>`
        
        

        """

        _prefix = 'tunnel-l2tun-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(L2tp.Sessions, self).__init__()

            self.yang_name = "sessions"
            self.yang_parent_name = "l2tp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("session", ("session", L2tp.Sessions.Session))])
            self._leafs = OrderedDict()

            self.session = YList(self)
            self._segment_path = lambda: "sessions"
            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(L2tp.Sessions, [], name, value)


        class Session(Entity):
            """
            L2TP information for a particular session
            
            .. attribute:: local_tunnel_id  (key)
            
            	Local tunnel ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: local_session_id  (key)
            
            	Local session ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: session_application_data
            
            	Session application data
            	**type**\:  :py:class:`SessionApplicationData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Sessions.Session.SessionApplicationData>`
            
            .. attribute:: local_ip_address
            
            	Local session IP address
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: remote_ip_address
            
            	Remote session IP address
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: l2tp_sh_sess_udp_lport
            
            	l2tp sh sess udp lport
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: l2tp_sh_sess_udp_rport
            
            	l2tp sh sess udp rport
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: protocol
            
            	Protocol
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: remote_tunnel_id
            
            	Remote tunnel ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: call_serial_number
            
            	Call serial number
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: local_tunnel_name
            
            	Local tunnel name
            	**type**\: str
            
            	**length:** 0..256
            
            .. attribute:: remote_tunnel_name
            
            	Remote tunnel name
            	**type**\: str
            
            	**length:** 0..256
            
            .. attribute:: remote_session_id
            
            	Remote session ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: l2tp_sh_sess_tie_breaker_enabled
            
            	l2tp sh sess tie breaker enabled
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: l2tp_sh_sess_tie_breaker
            
            	l2tp sh sess tie breaker
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: is_session_manual
            
            	True if session is manual
            	**type**\: bool
            
            .. attribute:: is_session_up
            
            	True if session is up
            	**type**\: bool
            
            .. attribute:: is_udp_checksum_enabled
            
            	True if UDP checksum enabled
            	**type**\: bool
            
            .. attribute:: is_sequencing_on
            
            	True if session sequence is on
            	**type**\: bool
            
            .. attribute:: is_session_state_established
            
            	True if session state is established
            	**type**\: bool
            
            .. attribute:: is_session_locally_initiated
            
            	True if session initiated locally
            	**type**\: bool
            
            .. attribute:: is_conditional_debug_enabled
            
            	True if conditional debugging is enabled
            	**type**\: bool
            
            .. attribute:: unique_id
            
            	Unique ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: interface_name
            
            	Interface name
            	**type**\: str
            
            	**length:** 0..256
            
            

            """

            _prefix = 'tunnel-l2tun-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(L2tp.Sessions.Session, self).__init__()

                self.yang_name = "session"
                self.yang_parent_name = "sessions"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['local_tunnel_id','local_session_id']
                self._child_classes = OrderedDict([("session-application-data", ("session_application_data", L2tp.Sessions.Session.SessionApplicationData))])
                self._leafs = OrderedDict([
                    ('local_tunnel_id', (YLeaf(YType.uint32, 'local-tunnel-id'), ['int'])),
                    ('local_session_id', (YLeaf(YType.uint32, 'local-session-id'), ['int'])),
                    ('local_ip_address', (YLeaf(YType.str, 'local-ip-address'), ['str'])),
                    ('remote_ip_address', (YLeaf(YType.str, 'remote-ip-address'), ['str'])),
                    ('l2tp_sh_sess_udp_lport', (YLeaf(YType.uint16, 'l2tp-sh-sess-udp-lport'), ['int'])),
                    ('l2tp_sh_sess_udp_rport', (YLeaf(YType.uint16, 'l2tp-sh-sess-udp-rport'), ['int'])),
                    ('protocol', (YLeaf(YType.uint8, 'protocol'), ['int'])),
                    ('remote_tunnel_id', (YLeaf(YType.uint32, 'remote-tunnel-id'), ['int'])),
                    ('call_serial_number', (YLeaf(YType.uint32, 'call-serial-number'), ['int'])),
                    ('local_tunnel_name', (YLeaf(YType.str, 'local-tunnel-name'), ['str'])),
                    ('remote_tunnel_name', (YLeaf(YType.str, 'remote-tunnel-name'), ['str'])),
                    ('remote_session_id', (YLeaf(YType.uint32, 'remote-session-id'), ['int'])),
                    ('l2tp_sh_sess_tie_breaker_enabled', (YLeaf(YType.uint8, 'l2tp-sh-sess-tie-breaker-enabled'), ['int'])),
                    ('l2tp_sh_sess_tie_breaker', (YLeaf(YType.uint64, 'l2tp-sh-sess-tie-breaker'), ['int'])),
                    ('is_session_manual', (YLeaf(YType.boolean, 'is-session-manual'), ['bool'])),
                    ('is_session_up', (YLeaf(YType.boolean, 'is-session-up'), ['bool'])),
                    ('is_udp_checksum_enabled', (YLeaf(YType.boolean, 'is-udp-checksum-enabled'), ['bool'])),
                    ('is_sequencing_on', (YLeaf(YType.boolean, 'is-sequencing-on'), ['bool'])),
                    ('is_session_state_established', (YLeaf(YType.boolean, 'is-session-state-established'), ['bool'])),
                    ('is_session_locally_initiated', (YLeaf(YType.boolean, 'is-session-locally-initiated'), ['bool'])),
                    ('is_conditional_debug_enabled', (YLeaf(YType.boolean, 'is-conditional-debug-enabled'), ['bool'])),
                    ('unique_id', (YLeaf(YType.uint32, 'unique-id'), ['int'])),
                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                ])
                self.local_tunnel_id = None
                self.local_session_id = None
                self.local_ip_address = None
                self.remote_ip_address = None
                self.l2tp_sh_sess_udp_lport = None
                self.l2tp_sh_sess_udp_rport = None
                self.protocol = None
                self.remote_tunnel_id = None
                self.call_serial_number = None
                self.local_tunnel_name = None
                self.remote_tunnel_name = None
                self.remote_session_id = None
                self.l2tp_sh_sess_tie_breaker_enabled = None
                self.l2tp_sh_sess_tie_breaker = None
                self.is_session_manual = None
                self.is_session_up = None
                self.is_udp_checksum_enabled = None
                self.is_sequencing_on = None
                self.is_session_state_established = None
                self.is_session_locally_initiated = None
                self.is_conditional_debug_enabled = None
                self.unique_id = None
                self.interface_name = None

                self.session_application_data = L2tp.Sessions.Session.SessionApplicationData()
                self.session_application_data.parent = self
                self._children_name_map["session_application_data"] = "session-application-data"
                self._segment_path = lambda: "session" + "[local-tunnel-id='" + str(self.local_tunnel_id) + "']" + "[local-session-id='" + str(self.local_session_id) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/sessions/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(L2tp.Sessions.Session, ['local_tunnel_id', 'local_session_id', u'local_ip_address', u'remote_ip_address', u'l2tp_sh_sess_udp_lport', u'l2tp_sh_sess_udp_rport', u'protocol', u'remote_tunnel_id', u'call_serial_number', u'local_tunnel_name', u'remote_tunnel_name', u'remote_session_id', u'l2tp_sh_sess_tie_breaker_enabled', u'l2tp_sh_sess_tie_breaker', u'is_session_manual', u'is_session_up', u'is_udp_checksum_enabled', u'is_sequencing_on', u'is_session_state_established', u'is_session_locally_initiated', u'is_conditional_debug_enabled', u'unique_id', u'interface_name'], name, value)


            class SessionApplicationData(Entity):
                """
                Session application data
                
                .. attribute:: xconnect
                
                	Xconnect data
                	**type**\:  :py:class:`Xconnect <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Sessions.Session.SessionApplicationData.Xconnect>`
                
                .. attribute:: vpdn
                
                	VPDN data
                	**type**\:  :py:class:`Vpdn <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Sessions.Session.SessionApplicationData.Vpdn>`
                
                .. attribute:: l2tp_sh_sess_app_type
                
                	l2tp sh sess app type
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'tunnel-l2tun-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(L2tp.Sessions.Session.SessionApplicationData, self).__init__()

                    self.yang_name = "session-application-data"
                    self.yang_parent_name = "session"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("xconnect", ("xconnect", L2tp.Sessions.Session.SessionApplicationData.Xconnect)), ("vpdn", ("vpdn", L2tp.Sessions.Session.SessionApplicationData.Vpdn))])
                    self._leafs = OrderedDict([
                        ('l2tp_sh_sess_app_type', (YLeaf(YType.uint32, 'l2tp-sh-sess-app-type'), ['int'])),
                    ])
                    self.l2tp_sh_sess_app_type = None

                    self.xconnect = L2tp.Sessions.Session.SessionApplicationData.Xconnect()
                    self.xconnect.parent = self
                    self._children_name_map["xconnect"] = "xconnect"

                    self.vpdn = L2tp.Sessions.Session.SessionApplicationData.Vpdn()
                    self.vpdn.parent = self
                    self._children_name_map["vpdn"] = "vpdn"
                    self._segment_path = lambda: "session-application-data"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(L2tp.Sessions.Session.SessionApplicationData, [u'l2tp_sh_sess_app_type'], name, value)


                class Xconnect(Entity):
                    """
                    Xconnect data
                    
                    .. attribute:: circuit_name
                    
                    	Circuit name
                    	**type**\: str
                    
                    .. attribute:: sessionvc_id
                    
                    	Session VC ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: is_circuit_state_up
                    
                    	True if circuit state is up
                    	**type**\: bool
                    
                    .. attribute:: is_local_circuit_state_up
                    
                    	True if local circuit state is up
                    	**type**\: bool
                    
                    .. attribute:: is_remote_circuit_state_up
                    
                    	True if remote circuit state is up
                    	**type**\: bool
                    
                    .. attribute:: ipv6_protocol_tunneling
                    
                    	IPv6ProtocolTunneling
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'tunnel-l2tun-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(L2tp.Sessions.Session.SessionApplicationData.Xconnect, self).__init__()

                        self.yang_name = "xconnect"
                        self.yang_parent_name = "session-application-data"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('circuit_name', (YLeaf(YType.str, 'circuit-name'), ['str'])),
                            ('sessionvc_id', (YLeaf(YType.uint32, 'sessionvc-id'), ['int'])),
                            ('is_circuit_state_up', (YLeaf(YType.boolean, 'is-circuit-state-up'), ['bool'])),
                            ('is_local_circuit_state_up', (YLeaf(YType.boolean, 'is-local-circuit-state-up'), ['bool'])),
                            ('is_remote_circuit_state_up', (YLeaf(YType.boolean, 'is-remote-circuit-state-up'), ['bool'])),
                            ('ipv6_protocol_tunneling', (YLeaf(YType.boolean, 'ipv6-protocol-tunneling'), ['bool'])),
                        ])
                        self.circuit_name = None
                        self.sessionvc_id = None
                        self.is_circuit_state_up = None
                        self.is_local_circuit_state_up = None
                        self.is_remote_circuit_state_up = None
                        self.ipv6_protocol_tunneling = None
                        self._segment_path = lambda: "xconnect"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2tp.Sessions.Session.SessionApplicationData.Xconnect, [u'circuit_name', u'sessionvc_id', u'is_circuit_state_up', u'is_local_circuit_state_up', u'is_remote_circuit_state_up', u'ipv6_protocol_tunneling'], name, value)


                class Vpdn(Entity):
                    """
                    VPDN data
                    
                    .. attribute:: username
                    
                    	Session username
                    	**type**\: str
                    
                    .. attribute:: interface_name
                    
                    	Interface name
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    

                    """

                    _prefix = 'tunnel-l2tun-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(L2tp.Sessions.Session.SessionApplicationData.Vpdn, self).__init__()

                        self.yang_name = "vpdn"
                        self.yang_parent_name = "session-application-data"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('username', (YLeaf(YType.str, 'username'), ['str'])),
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                        ])
                        self.username = None
                        self.interface_name = None
                        self._segment_path = lambda: "vpdn"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2tp.Sessions.Session.SessionApplicationData.Vpdn, [u'username', u'interface_name'], name, value)


    class Session(Entity):
        """
        L2TP control messages counters
        
        .. attribute:: unavailable
        
        	L2TP session unavailable  information
        	**type**\:  :py:class:`Unavailable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Session.Unavailable>`
        
        

        """

        _prefix = 'tunnel-l2tun-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(L2tp.Session, self).__init__()

            self.yang_name = "session"
            self.yang_parent_name = "l2tp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("unavailable", ("unavailable", L2tp.Session.Unavailable))])
            self._leafs = OrderedDict()

            self.unavailable = L2tp.Session.Unavailable()
            self.unavailable.parent = self
            self._children_name_map["unavailable"] = "unavailable"
            self._segment_path = lambda: "session"
            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(L2tp.Session, [], name, value)


        class Unavailable(Entity):
            """
            L2TP session unavailable  information
            
            .. attribute:: sessions_on_hold
            
            	Number of session ID in hold database
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'tunnel-l2tun-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(L2tp.Session.Unavailable, self).__init__()

                self.yang_name = "unavailable"
                self.yang_parent_name = "session"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('sessions_on_hold', (YLeaf(YType.uint32, 'sessions-on-hold'), ['int'])),
                ])
                self.sessions_on_hold = None
                self._segment_path = lambda: "unavailable"
                self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/session/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(L2tp.Session.Unavailable, [u'sessions_on_hold'], name, value)

    def clone_ptr(self):
        self._top_entity = L2tp()
        return self._top_entity

class L2tpv2(Entity):
    """
    l2tpv2
    
    .. attribute:: counters
    
    	L2TP control messages counters
    	**type**\:  :py:class:`Counters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Counters>`
    
    .. attribute:: statistics
    
    	L2TP v2 statistics information
    	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Statistics>`
    
    .. attribute:: tunnel
    
    	L2TPv2 tunnel 
    	**type**\:  :py:class:`Tunnel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Tunnel>`
    
    .. attribute:: tunnel_configurations
    
    	List of tunnel IDs
    	**type**\:  :py:class:`TunnelConfigurations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.TunnelConfigurations>`
    
    .. attribute:: counter_hist_fail
    
    	Failure events leading to disconnection
    	**type**\:  :py:class:`CounterHistFail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.CounterHistFail>`
    
    .. attribute:: classes
    
    	List of L2TP class names
    	**type**\:  :py:class:`Classes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Classes>`
    
    .. attribute:: tunnels
    
    	List of tunnel IDs
    	**type**\:  :py:class:`Tunnels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Tunnels>`
    
    .. attribute:: sessions
    
    	List of session IDs
    	**type**\:  :py:class:`Sessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Sessions>`
    
    .. attribute:: session
    
    	L2TP control messages counters
    	**type**\:  :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Session>`
    
    

    """

    _prefix = 'tunnel-l2tun-oper'
    _revision = '2017-09-07'

    def __init__(self):
        super(L2tpv2, self).__init__()
        self._top_entity = None

        self.yang_name = "l2tpv2"
        self.yang_parent_name = "Cisco-IOS-XR-tunnel-l2tun-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("counters", ("counters", L2tpv2.Counters)), ("statistics", ("statistics", L2tpv2.Statistics)), ("tunnel", ("tunnel", L2tpv2.Tunnel)), ("tunnel-configurations", ("tunnel_configurations", L2tpv2.TunnelConfigurations)), ("counter-hist-fail", ("counter_hist_fail", L2tpv2.CounterHistFail)), ("classes", ("classes", L2tpv2.Classes)), ("tunnels", ("tunnels", L2tpv2.Tunnels)), ("sessions", ("sessions", L2tpv2.Sessions)), ("session", ("session", L2tpv2.Session))])
        self._leafs = OrderedDict()

        self.counters = L2tpv2.Counters()
        self.counters.parent = self
        self._children_name_map["counters"] = "counters"

        self.statistics = L2tpv2.Statistics()
        self.statistics.parent = self
        self._children_name_map["statistics"] = "statistics"

        self.tunnel = L2tpv2.Tunnel()
        self.tunnel.parent = self
        self._children_name_map["tunnel"] = "tunnel"

        self.tunnel_configurations = L2tpv2.TunnelConfigurations()
        self.tunnel_configurations.parent = self
        self._children_name_map["tunnel_configurations"] = "tunnel-configurations"

        self.counter_hist_fail = L2tpv2.CounterHistFail()
        self.counter_hist_fail.parent = self
        self._children_name_map["counter_hist_fail"] = "counter-hist-fail"

        self.classes = L2tpv2.Classes()
        self.classes.parent = self
        self._children_name_map["classes"] = "classes"

        self.tunnels = L2tpv2.Tunnels()
        self.tunnels.parent = self
        self._children_name_map["tunnels"] = "tunnels"

        self.sessions = L2tpv2.Sessions()
        self.sessions.parent = self
        self._children_name_map["sessions"] = "sessions"

        self.session = L2tpv2.Session()
        self.session.parent = self
        self._children_name_map["session"] = "session"
        self._segment_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(L2tpv2, [], name, value)


    class Counters(Entity):
        """
        L2TP control messages counters
        
        .. attribute:: forwarding
        
        	L2TP forwarding messages counters
        	**type**\:  :py:class:`Forwarding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Counters.Forwarding>`
        
        .. attribute:: control
        
        	L2TP control messages counters
        	**type**\:  :py:class:`Control <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Counters.Control>`
        
        

        """

        _prefix = 'tunnel-l2tun-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(L2tpv2.Counters, self).__init__()

            self.yang_name = "counters"
            self.yang_parent_name = "l2tpv2"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("forwarding", ("forwarding", L2tpv2.Counters.Forwarding)), ("control", ("control", L2tpv2.Counters.Control))])
            self._leafs = OrderedDict()

            self.forwarding = L2tpv2.Counters.Forwarding()
            self.forwarding.parent = self
            self._children_name_map["forwarding"] = "forwarding"

            self.control = L2tpv2.Counters.Control()
            self.control.parent = self
            self._children_name_map["control"] = "control"
            self._segment_path = lambda: "counters"
            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(L2tpv2.Counters, [], name, value)


        class Forwarding(Entity):
            """
            L2TP forwarding messages counters
            
            .. attribute:: sessions
            
            	List of class and session IDs
            	**type**\:  :py:class:`Sessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Counters.Forwarding.Sessions>`
            
            

            """

            _prefix = 'tunnel-l2tun-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(L2tpv2.Counters.Forwarding, self).__init__()

                self.yang_name = "forwarding"
                self.yang_parent_name = "counters"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("sessions", ("sessions", L2tpv2.Counters.Forwarding.Sessions))])
                self._leafs = OrderedDict()

                self.sessions = L2tpv2.Counters.Forwarding.Sessions()
                self.sessions.parent = self
                self._children_name_map["sessions"] = "sessions"
                self._segment_path = lambda: "forwarding"
                self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/counters/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(L2tpv2.Counters.Forwarding, [], name, value)


            class Sessions(Entity):
                """
                List of class and session IDs
                
                .. attribute:: session
                
                	L2TP information for a particular session
                	**type**\: list of  		 :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Counters.Forwarding.Sessions.Session>`
                
                

                """

                _prefix = 'tunnel-l2tun-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(L2tpv2.Counters.Forwarding.Sessions, self).__init__()

                    self.yang_name = "sessions"
                    self.yang_parent_name = "forwarding"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("session", ("session", L2tpv2.Counters.Forwarding.Sessions.Session))])
                    self._leafs = OrderedDict()

                    self.session = YList(self)
                    self._segment_path = lambda: "sessions"
                    self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/counters/forwarding/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(L2tpv2.Counters.Forwarding.Sessions, [], name, value)


                class Session(Entity):
                    """
                    L2TP information for a particular session
                    
                    .. attribute:: tunnel_id  (key)
                    
                    	Local tunnel ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: session_id  (key)
                    
                    	Local session ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: remote_session_id
                    
                    	Remote session ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: in_packets
                    
                    	Number of packets sent in
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: out_packets
                    
                    	Number of packets sent out
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: in_bytes
                    
                    	Number of bytes sent in
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: byte
                    
                    .. attribute:: out_bytes
                    
                    	Number of bytes sent out
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: byte
                    
                    

                    """

                    _prefix = 'tunnel-l2tun-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(L2tpv2.Counters.Forwarding.Sessions.Session, self).__init__()

                        self.yang_name = "session"
                        self.yang_parent_name = "sessions"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['tunnel_id','session_id']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('tunnel_id', (YLeaf(YType.uint32, 'tunnel-id'), ['int'])),
                            ('session_id', (YLeaf(YType.uint32, 'session-id'), ['int'])),
                            ('remote_session_id', (YLeaf(YType.uint32, 'remote-session-id'), ['int'])),
                            ('in_packets', (YLeaf(YType.uint64, 'in-packets'), ['int'])),
                            ('out_packets', (YLeaf(YType.uint64, 'out-packets'), ['int'])),
                            ('in_bytes', (YLeaf(YType.uint64, 'in-bytes'), ['int'])),
                            ('out_bytes', (YLeaf(YType.uint64, 'out-bytes'), ['int'])),
                        ])
                        self.tunnel_id = None
                        self.session_id = None
                        self.remote_session_id = None
                        self.in_packets = None
                        self.out_packets = None
                        self.in_bytes = None
                        self.out_bytes = None
                        self._segment_path = lambda: "session" + "[tunnel-id='" + str(self.tunnel_id) + "']" + "[session-id='" + str(self.session_id) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/counters/forwarding/sessions/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2tpv2.Counters.Forwarding.Sessions.Session, ['tunnel_id', 'session_id', u'remote_session_id', u'in_packets', u'out_packets', u'in_bytes', u'out_bytes'], name, value)


        class Control(Entity):
            """
            L2TP control messages counters
            
            .. attribute:: tunnel_xr
            
            	L2TP control tunnel messages counters
            	**type**\:  :py:class:`TunnelXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Counters.Control.TunnelXr>`
            
            .. attribute:: tunnels
            
            	Table of tunnel IDs of control message counters
            	**type**\:  :py:class:`Tunnels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Counters.Control.Tunnels>`
            
            

            """

            _prefix = 'tunnel-l2tun-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(L2tpv2.Counters.Control, self).__init__()

                self.yang_name = "control"
                self.yang_parent_name = "counters"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("tunnel-xr", ("tunnel_xr", L2tpv2.Counters.Control.TunnelXr)), ("tunnels", ("tunnels", L2tpv2.Counters.Control.Tunnels))])
                self._leafs = OrderedDict()

                self.tunnel_xr = L2tpv2.Counters.Control.TunnelXr()
                self.tunnel_xr.parent = self
                self._children_name_map["tunnel_xr"] = "tunnel-xr"

                self.tunnels = L2tpv2.Counters.Control.Tunnels()
                self.tunnels.parent = self
                self._children_name_map["tunnels"] = "tunnels"
                self._segment_path = lambda: "control"
                self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/counters/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(L2tpv2.Counters.Control, [], name, value)


            class TunnelXr(Entity):
                """
                L2TP control tunnel messages counters
                
                .. attribute:: authentication
                
                	Tunnel authentication counters
                	**type**\:  :py:class:`Authentication <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Counters.Control.TunnelXr.Authentication>`
                
                .. attribute:: global_
                
                	Tunnel counters
                	**type**\:  :py:class:`Global <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Counters.Control.TunnelXr.Global>`
                
                

                """

                _prefix = 'tunnel-l2tun-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(L2tpv2.Counters.Control.TunnelXr, self).__init__()

                    self.yang_name = "tunnel-xr"
                    self.yang_parent_name = "control"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("authentication", ("authentication", L2tpv2.Counters.Control.TunnelXr.Authentication)), ("global", ("global_", L2tpv2.Counters.Control.TunnelXr.Global))])
                    self._leafs = OrderedDict()

                    self.authentication = L2tpv2.Counters.Control.TunnelXr.Authentication()
                    self.authentication.parent = self
                    self._children_name_map["authentication"] = "authentication"

                    self.global_ = L2tpv2.Counters.Control.TunnelXr.Global()
                    self.global_.parent = self
                    self._children_name_map["global_"] = "global"
                    self._segment_path = lambda: "tunnel-xr"
                    self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/counters/control/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(L2tpv2.Counters.Control.TunnelXr, [], name, value)


                class Authentication(Entity):
                    """
                    Tunnel authentication counters
                    
                    .. attribute:: nonce_avp
                    
                    	Nonce AVP statistics
                    	**type**\:  :py:class:`NonceAvp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Counters.Control.TunnelXr.Authentication.NonceAvp>`
                    
                    .. attribute:: common_digest
                    
                    	Common digest statistics
                    	**type**\:  :py:class:`CommonDigest <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Counters.Control.TunnelXr.Authentication.CommonDigest>`
                    
                    .. attribute:: primary_digest
                    
                    	Primary digest statistics
                    	**type**\:  :py:class:`PrimaryDigest <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Counters.Control.TunnelXr.Authentication.PrimaryDigest>`
                    
                    .. attribute:: secondary_digest
                    
                    	Secondary digest statistics
                    	**type**\:  :py:class:`SecondaryDigest <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Counters.Control.TunnelXr.Authentication.SecondaryDigest>`
                    
                    .. attribute:: integrity_check
                    
                    	Integrity check statistics
                    	**type**\:  :py:class:`IntegrityCheck <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Counters.Control.TunnelXr.Authentication.IntegrityCheck>`
                    
                    .. attribute:: local_secret
                    
                    	Local secret statistics
                    	**type**\:  :py:class:`LocalSecret <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Counters.Control.TunnelXr.Authentication.LocalSecret>`
                    
                    .. attribute:: challenge_avp
                    
                    	Challenge AVP statistics
                    	**type**\:  :py:class:`ChallengeAvp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Counters.Control.TunnelXr.Authentication.ChallengeAvp>`
                    
                    .. attribute:: challenge_reponse
                    
                    	Challenge response statistics
                    	**type**\:  :py:class:`ChallengeReponse <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Counters.Control.TunnelXr.Authentication.ChallengeReponse>`
                    
                    .. attribute:: overall_statistics
                    
                    	Overall statistics
                    	**type**\:  :py:class:`OverallStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Counters.Control.TunnelXr.Authentication.OverallStatistics>`
                    
                    

                    """

                    _prefix = 'tunnel-l2tun-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(L2tpv2.Counters.Control.TunnelXr.Authentication, self).__init__()

                        self.yang_name = "authentication"
                        self.yang_parent_name = "tunnel-xr"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("nonce-avp", ("nonce_avp", L2tpv2.Counters.Control.TunnelXr.Authentication.NonceAvp)), ("common-digest", ("common_digest", L2tpv2.Counters.Control.TunnelXr.Authentication.CommonDigest)), ("primary-digest", ("primary_digest", L2tpv2.Counters.Control.TunnelXr.Authentication.PrimaryDigest)), ("secondary-digest", ("secondary_digest", L2tpv2.Counters.Control.TunnelXr.Authentication.SecondaryDigest)), ("integrity-check", ("integrity_check", L2tpv2.Counters.Control.TunnelXr.Authentication.IntegrityCheck)), ("local-secret", ("local_secret", L2tpv2.Counters.Control.TunnelXr.Authentication.LocalSecret)), ("challenge-avp", ("challenge_avp", L2tpv2.Counters.Control.TunnelXr.Authentication.ChallengeAvp)), ("challenge-reponse", ("challenge_reponse", L2tpv2.Counters.Control.TunnelXr.Authentication.ChallengeReponse)), ("overall-statistics", ("overall_statistics", L2tpv2.Counters.Control.TunnelXr.Authentication.OverallStatistics))])
                        self._leafs = OrderedDict()

                        self.nonce_avp = L2tpv2.Counters.Control.TunnelXr.Authentication.NonceAvp()
                        self.nonce_avp.parent = self
                        self._children_name_map["nonce_avp"] = "nonce-avp"

                        self.common_digest = L2tpv2.Counters.Control.TunnelXr.Authentication.CommonDigest()
                        self.common_digest.parent = self
                        self._children_name_map["common_digest"] = "common-digest"

                        self.primary_digest = L2tpv2.Counters.Control.TunnelXr.Authentication.PrimaryDigest()
                        self.primary_digest.parent = self
                        self._children_name_map["primary_digest"] = "primary-digest"

                        self.secondary_digest = L2tpv2.Counters.Control.TunnelXr.Authentication.SecondaryDigest()
                        self.secondary_digest.parent = self
                        self._children_name_map["secondary_digest"] = "secondary-digest"

                        self.integrity_check = L2tpv2.Counters.Control.TunnelXr.Authentication.IntegrityCheck()
                        self.integrity_check.parent = self
                        self._children_name_map["integrity_check"] = "integrity-check"

                        self.local_secret = L2tpv2.Counters.Control.TunnelXr.Authentication.LocalSecret()
                        self.local_secret.parent = self
                        self._children_name_map["local_secret"] = "local-secret"

                        self.challenge_avp = L2tpv2.Counters.Control.TunnelXr.Authentication.ChallengeAvp()
                        self.challenge_avp.parent = self
                        self._children_name_map["challenge_avp"] = "challenge-avp"

                        self.challenge_reponse = L2tpv2.Counters.Control.TunnelXr.Authentication.ChallengeReponse()
                        self.challenge_reponse.parent = self
                        self._children_name_map["challenge_reponse"] = "challenge-reponse"

                        self.overall_statistics = L2tpv2.Counters.Control.TunnelXr.Authentication.OverallStatistics()
                        self.overall_statistics.parent = self
                        self._children_name_map["overall_statistics"] = "overall-statistics"
                        self._segment_path = lambda: "authentication"
                        self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/counters/control/tunnel-xr/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2tpv2.Counters.Control.TunnelXr.Authentication, [], name, value)


                    class NonceAvp(Entity):
                        """
                        Nonce AVP statistics
                        
                        .. attribute:: validate
                        
                        	Validate
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_hash
                        
                        	Bad hash
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_length
                        
                        	Bad length
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ignored
                        
                        	Ignored
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: missing
                        
                        	Missing
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: passed
                        
                        	Passed
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: failed
                        
                        	Failed
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: skipped
                        
                        	Skipped
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: generate_response_failures
                        
                        	Generate response fail
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unexpected
                        
                        	Unexpected
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unexpected_zlb
                        
                        	Unexpected ZLB
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'tunnel-l2tun-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(L2tpv2.Counters.Control.TunnelXr.Authentication.NonceAvp, self).__init__()

                            self.yang_name = "nonce-avp"
                            self.yang_parent_name = "authentication"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('validate', (YLeaf(YType.uint32, 'validate'), ['int'])),
                                ('bad_hash', (YLeaf(YType.uint32, 'bad-hash'), ['int'])),
                                ('bad_length', (YLeaf(YType.uint32, 'bad-length'), ['int'])),
                                ('ignored', (YLeaf(YType.uint32, 'ignored'), ['int'])),
                                ('missing', (YLeaf(YType.uint32, 'missing'), ['int'])),
                                ('passed', (YLeaf(YType.uint32, 'passed'), ['int'])),
                                ('failed', (YLeaf(YType.uint32, 'failed'), ['int'])),
                                ('skipped', (YLeaf(YType.uint32, 'skipped'), ['int'])),
                                ('generate_response_failures', (YLeaf(YType.uint32, 'generate-response-failures'), ['int'])),
                                ('unexpected', (YLeaf(YType.uint32, 'unexpected'), ['int'])),
                                ('unexpected_zlb', (YLeaf(YType.uint32, 'unexpected-zlb'), ['int'])),
                            ])
                            self.validate = None
                            self.bad_hash = None
                            self.bad_length = None
                            self.ignored = None
                            self.missing = None
                            self.passed = None
                            self.failed = None
                            self.skipped = None
                            self.generate_response_failures = None
                            self.unexpected = None
                            self.unexpected_zlb = None
                            self._segment_path = lambda: "nonce-avp"
                            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/counters/control/tunnel-xr/authentication/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2tpv2.Counters.Control.TunnelXr.Authentication.NonceAvp, [u'validate', u'bad_hash', u'bad_length', u'ignored', u'missing', u'passed', u'failed', u'skipped', u'generate_response_failures', u'unexpected', u'unexpected_zlb'], name, value)


                    class CommonDigest(Entity):
                        """
                        Common digest statistics
                        
                        .. attribute:: validate
                        
                        	Validate
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_hash
                        
                        	Bad hash
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_length
                        
                        	Bad length
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ignored
                        
                        	Ignored
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: missing
                        
                        	Missing
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: passed
                        
                        	Passed
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: failed
                        
                        	Failed
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: skipped
                        
                        	Skipped
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: generate_response_failures
                        
                        	Generate response fail
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unexpected
                        
                        	Unexpected
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unexpected_zlb
                        
                        	Unexpected ZLB
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'tunnel-l2tun-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(L2tpv2.Counters.Control.TunnelXr.Authentication.CommonDigest, self).__init__()

                            self.yang_name = "common-digest"
                            self.yang_parent_name = "authentication"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('validate', (YLeaf(YType.uint32, 'validate'), ['int'])),
                                ('bad_hash', (YLeaf(YType.uint32, 'bad-hash'), ['int'])),
                                ('bad_length', (YLeaf(YType.uint32, 'bad-length'), ['int'])),
                                ('ignored', (YLeaf(YType.uint32, 'ignored'), ['int'])),
                                ('missing', (YLeaf(YType.uint32, 'missing'), ['int'])),
                                ('passed', (YLeaf(YType.uint32, 'passed'), ['int'])),
                                ('failed', (YLeaf(YType.uint32, 'failed'), ['int'])),
                                ('skipped', (YLeaf(YType.uint32, 'skipped'), ['int'])),
                                ('generate_response_failures', (YLeaf(YType.uint32, 'generate-response-failures'), ['int'])),
                                ('unexpected', (YLeaf(YType.uint32, 'unexpected'), ['int'])),
                                ('unexpected_zlb', (YLeaf(YType.uint32, 'unexpected-zlb'), ['int'])),
                            ])
                            self.validate = None
                            self.bad_hash = None
                            self.bad_length = None
                            self.ignored = None
                            self.missing = None
                            self.passed = None
                            self.failed = None
                            self.skipped = None
                            self.generate_response_failures = None
                            self.unexpected = None
                            self.unexpected_zlb = None
                            self._segment_path = lambda: "common-digest"
                            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/counters/control/tunnel-xr/authentication/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2tpv2.Counters.Control.TunnelXr.Authentication.CommonDigest, [u'validate', u'bad_hash', u'bad_length', u'ignored', u'missing', u'passed', u'failed', u'skipped', u'generate_response_failures', u'unexpected', u'unexpected_zlb'], name, value)


                    class PrimaryDigest(Entity):
                        """
                        Primary digest statistics
                        
                        .. attribute:: validate
                        
                        	Validate
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_hash
                        
                        	Bad hash
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_length
                        
                        	Bad length
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ignored
                        
                        	Ignored
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: missing
                        
                        	Missing
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: passed
                        
                        	Passed
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: failed
                        
                        	Failed
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: skipped
                        
                        	Skipped
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: generate_response_failures
                        
                        	Generate response fail
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unexpected
                        
                        	Unexpected
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unexpected_zlb
                        
                        	Unexpected ZLB
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'tunnel-l2tun-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(L2tpv2.Counters.Control.TunnelXr.Authentication.PrimaryDigest, self).__init__()

                            self.yang_name = "primary-digest"
                            self.yang_parent_name = "authentication"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('validate', (YLeaf(YType.uint32, 'validate'), ['int'])),
                                ('bad_hash', (YLeaf(YType.uint32, 'bad-hash'), ['int'])),
                                ('bad_length', (YLeaf(YType.uint32, 'bad-length'), ['int'])),
                                ('ignored', (YLeaf(YType.uint32, 'ignored'), ['int'])),
                                ('missing', (YLeaf(YType.uint32, 'missing'), ['int'])),
                                ('passed', (YLeaf(YType.uint32, 'passed'), ['int'])),
                                ('failed', (YLeaf(YType.uint32, 'failed'), ['int'])),
                                ('skipped', (YLeaf(YType.uint32, 'skipped'), ['int'])),
                                ('generate_response_failures', (YLeaf(YType.uint32, 'generate-response-failures'), ['int'])),
                                ('unexpected', (YLeaf(YType.uint32, 'unexpected'), ['int'])),
                                ('unexpected_zlb', (YLeaf(YType.uint32, 'unexpected-zlb'), ['int'])),
                            ])
                            self.validate = None
                            self.bad_hash = None
                            self.bad_length = None
                            self.ignored = None
                            self.missing = None
                            self.passed = None
                            self.failed = None
                            self.skipped = None
                            self.generate_response_failures = None
                            self.unexpected = None
                            self.unexpected_zlb = None
                            self._segment_path = lambda: "primary-digest"
                            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/counters/control/tunnel-xr/authentication/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2tpv2.Counters.Control.TunnelXr.Authentication.PrimaryDigest, [u'validate', u'bad_hash', u'bad_length', u'ignored', u'missing', u'passed', u'failed', u'skipped', u'generate_response_failures', u'unexpected', u'unexpected_zlb'], name, value)


                    class SecondaryDigest(Entity):
                        """
                        Secondary digest statistics
                        
                        .. attribute:: validate
                        
                        	Validate
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_hash
                        
                        	Bad hash
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_length
                        
                        	Bad length
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ignored
                        
                        	Ignored
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: missing
                        
                        	Missing
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: passed
                        
                        	Passed
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: failed
                        
                        	Failed
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: skipped
                        
                        	Skipped
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: generate_response_failures
                        
                        	Generate response fail
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unexpected
                        
                        	Unexpected
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unexpected_zlb
                        
                        	Unexpected ZLB
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'tunnel-l2tun-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(L2tpv2.Counters.Control.TunnelXr.Authentication.SecondaryDigest, self).__init__()

                            self.yang_name = "secondary-digest"
                            self.yang_parent_name = "authentication"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('validate', (YLeaf(YType.uint32, 'validate'), ['int'])),
                                ('bad_hash', (YLeaf(YType.uint32, 'bad-hash'), ['int'])),
                                ('bad_length', (YLeaf(YType.uint32, 'bad-length'), ['int'])),
                                ('ignored', (YLeaf(YType.uint32, 'ignored'), ['int'])),
                                ('missing', (YLeaf(YType.uint32, 'missing'), ['int'])),
                                ('passed', (YLeaf(YType.uint32, 'passed'), ['int'])),
                                ('failed', (YLeaf(YType.uint32, 'failed'), ['int'])),
                                ('skipped', (YLeaf(YType.uint32, 'skipped'), ['int'])),
                                ('generate_response_failures', (YLeaf(YType.uint32, 'generate-response-failures'), ['int'])),
                                ('unexpected', (YLeaf(YType.uint32, 'unexpected'), ['int'])),
                                ('unexpected_zlb', (YLeaf(YType.uint32, 'unexpected-zlb'), ['int'])),
                            ])
                            self.validate = None
                            self.bad_hash = None
                            self.bad_length = None
                            self.ignored = None
                            self.missing = None
                            self.passed = None
                            self.failed = None
                            self.skipped = None
                            self.generate_response_failures = None
                            self.unexpected = None
                            self.unexpected_zlb = None
                            self._segment_path = lambda: "secondary-digest"
                            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/counters/control/tunnel-xr/authentication/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2tpv2.Counters.Control.TunnelXr.Authentication.SecondaryDigest, [u'validate', u'bad_hash', u'bad_length', u'ignored', u'missing', u'passed', u'failed', u'skipped', u'generate_response_failures', u'unexpected', u'unexpected_zlb'], name, value)


                    class IntegrityCheck(Entity):
                        """
                        Integrity check statistics
                        
                        .. attribute:: validate
                        
                        	Validate
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_hash
                        
                        	Bad hash
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_length
                        
                        	Bad length
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ignored
                        
                        	Ignored
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: missing
                        
                        	Missing
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: passed
                        
                        	Passed
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: failed
                        
                        	Failed
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: skipped
                        
                        	Skipped
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: generate_response_failures
                        
                        	Generate response fail
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unexpected
                        
                        	Unexpected
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unexpected_zlb
                        
                        	Unexpected ZLB
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'tunnel-l2tun-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(L2tpv2.Counters.Control.TunnelXr.Authentication.IntegrityCheck, self).__init__()

                            self.yang_name = "integrity-check"
                            self.yang_parent_name = "authentication"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('validate', (YLeaf(YType.uint32, 'validate'), ['int'])),
                                ('bad_hash', (YLeaf(YType.uint32, 'bad-hash'), ['int'])),
                                ('bad_length', (YLeaf(YType.uint32, 'bad-length'), ['int'])),
                                ('ignored', (YLeaf(YType.uint32, 'ignored'), ['int'])),
                                ('missing', (YLeaf(YType.uint32, 'missing'), ['int'])),
                                ('passed', (YLeaf(YType.uint32, 'passed'), ['int'])),
                                ('failed', (YLeaf(YType.uint32, 'failed'), ['int'])),
                                ('skipped', (YLeaf(YType.uint32, 'skipped'), ['int'])),
                                ('generate_response_failures', (YLeaf(YType.uint32, 'generate-response-failures'), ['int'])),
                                ('unexpected', (YLeaf(YType.uint32, 'unexpected'), ['int'])),
                                ('unexpected_zlb', (YLeaf(YType.uint32, 'unexpected-zlb'), ['int'])),
                            ])
                            self.validate = None
                            self.bad_hash = None
                            self.bad_length = None
                            self.ignored = None
                            self.missing = None
                            self.passed = None
                            self.failed = None
                            self.skipped = None
                            self.generate_response_failures = None
                            self.unexpected = None
                            self.unexpected_zlb = None
                            self._segment_path = lambda: "integrity-check"
                            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/counters/control/tunnel-xr/authentication/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2tpv2.Counters.Control.TunnelXr.Authentication.IntegrityCheck, [u'validate', u'bad_hash', u'bad_length', u'ignored', u'missing', u'passed', u'failed', u'skipped', u'generate_response_failures', u'unexpected', u'unexpected_zlb'], name, value)


                    class LocalSecret(Entity):
                        """
                        Local secret statistics
                        
                        .. attribute:: validate
                        
                        	Validate
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_hash
                        
                        	Bad hash
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_length
                        
                        	Bad length
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ignored
                        
                        	Ignored
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: missing
                        
                        	Missing
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: passed
                        
                        	Passed
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: failed
                        
                        	Failed
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: skipped
                        
                        	Skipped
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: generate_response_failures
                        
                        	Generate response fail
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unexpected
                        
                        	Unexpected
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unexpected_zlb
                        
                        	Unexpected ZLB
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'tunnel-l2tun-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(L2tpv2.Counters.Control.TunnelXr.Authentication.LocalSecret, self).__init__()

                            self.yang_name = "local-secret"
                            self.yang_parent_name = "authentication"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('validate', (YLeaf(YType.uint32, 'validate'), ['int'])),
                                ('bad_hash', (YLeaf(YType.uint32, 'bad-hash'), ['int'])),
                                ('bad_length', (YLeaf(YType.uint32, 'bad-length'), ['int'])),
                                ('ignored', (YLeaf(YType.uint32, 'ignored'), ['int'])),
                                ('missing', (YLeaf(YType.uint32, 'missing'), ['int'])),
                                ('passed', (YLeaf(YType.uint32, 'passed'), ['int'])),
                                ('failed', (YLeaf(YType.uint32, 'failed'), ['int'])),
                                ('skipped', (YLeaf(YType.uint32, 'skipped'), ['int'])),
                                ('generate_response_failures', (YLeaf(YType.uint32, 'generate-response-failures'), ['int'])),
                                ('unexpected', (YLeaf(YType.uint32, 'unexpected'), ['int'])),
                                ('unexpected_zlb', (YLeaf(YType.uint32, 'unexpected-zlb'), ['int'])),
                            ])
                            self.validate = None
                            self.bad_hash = None
                            self.bad_length = None
                            self.ignored = None
                            self.missing = None
                            self.passed = None
                            self.failed = None
                            self.skipped = None
                            self.generate_response_failures = None
                            self.unexpected = None
                            self.unexpected_zlb = None
                            self._segment_path = lambda: "local-secret"
                            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/counters/control/tunnel-xr/authentication/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2tpv2.Counters.Control.TunnelXr.Authentication.LocalSecret, [u'validate', u'bad_hash', u'bad_length', u'ignored', u'missing', u'passed', u'failed', u'skipped', u'generate_response_failures', u'unexpected', u'unexpected_zlb'], name, value)


                    class ChallengeAvp(Entity):
                        """
                        Challenge AVP statistics
                        
                        .. attribute:: validate
                        
                        	Validate
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_hash
                        
                        	Bad hash
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_length
                        
                        	Bad length
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ignored
                        
                        	Ignored
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: missing
                        
                        	Missing
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: passed
                        
                        	Passed
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: failed
                        
                        	Failed
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: skipped
                        
                        	Skipped
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: generate_response_failures
                        
                        	Generate response fail
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unexpected
                        
                        	Unexpected
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unexpected_zlb
                        
                        	Unexpected ZLB
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'tunnel-l2tun-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(L2tpv2.Counters.Control.TunnelXr.Authentication.ChallengeAvp, self).__init__()

                            self.yang_name = "challenge-avp"
                            self.yang_parent_name = "authentication"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('validate', (YLeaf(YType.uint32, 'validate'), ['int'])),
                                ('bad_hash', (YLeaf(YType.uint32, 'bad-hash'), ['int'])),
                                ('bad_length', (YLeaf(YType.uint32, 'bad-length'), ['int'])),
                                ('ignored', (YLeaf(YType.uint32, 'ignored'), ['int'])),
                                ('missing', (YLeaf(YType.uint32, 'missing'), ['int'])),
                                ('passed', (YLeaf(YType.uint32, 'passed'), ['int'])),
                                ('failed', (YLeaf(YType.uint32, 'failed'), ['int'])),
                                ('skipped', (YLeaf(YType.uint32, 'skipped'), ['int'])),
                                ('generate_response_failures', (YLeaf(YType.uint32, 'generate-response-failures'), ['int'])),
                                ('unexpected', (YLeaf(YType.uint32, 'unexpected'), ['int'])),
                                ('unexpected_zlb', (YLeaf(YType.uint32, 'unexpected-zlb'), ['int'])),
                            ])
                            self.validate = None
                            self.bad_hash = None
                            self.bad_length = None
                            self.ignored = None
                            self.missing = None
                            self.passed = None
                            self.failed = None
                            self.skipped = None
                            self.generate_response_failures = None
                            self.unexpected = None
                            self.unexpected_zlb = None
                            self._segment_path = lambda: "challenge-avp"
                            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/counters/control/tunnel-xr/authentication/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2tpv2.Counters.Control.TunnelXr.Authentication.ChallengeAvp, [u'validate', u'bad_hash', u'bad_length', u'ignored', u'missing', u'passed', u'failed', u'skipped', u'generate_response_failures', u'unexpected', u'unexpected_zlb'], name, value)


                    class ChallengeReponse(Entity):
                        """
                        Challenge response statistics
                        
                        .. attribute:: validate
                        
                        	Validate
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_hash
                        
                        	Bad hash
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_length
                        
                        	Bad length
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ignored
                        
                        	Ignored
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: missing
                        
                        	Missing
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: passed
                        
                        	Passed
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: failed
                        
                        	Failed
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: skipped
                        
                        	Skipped
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: generate_response_failures
                        
                        	Generate response fail
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unexpected
                        
                        	Unexpected
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unexpected_zlb
                        
                        	Unexpected ZLB
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'tunnel-l2tun-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(L2tpv2.Counters.Control.TunnelXr.Authentication.ChallengeReponse, self).__init__()

                            self.yang_name = "challenge-reponse"
                            self.yang_parent_name = "authentication"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('validate', (YLeaf(YType.uint32, 'validate'), ['int'])),
                                ('bad_hash', (YLeaf(YType.uint32, 'bad-hash'), ['int'])),
                                ('bad_length', (YLeaf(YType.uint32, 'bad-length'), ['int'])),
                                ('ignored', (YLeaf(YType.uint32, 'ignored'), ['int'])),
                                ('missing', (YLeaf(YType.uint32, 'missing'), ['int'])),
                                ('passed', (YLeaf(YType.uint32, 'passed'), ['int'])),
                                ('failed', (YLeaf(YType.uint32, 'failed'), ['int'])),
                                ('skipped', (YLeaf(YType.uint32, 'skipped'), ['int'])),
                                ('generate_response_failures', (YLeaf(YType.uint32, 'generate-response-failures'), ['int'])),
                                ('unexpected', (YLeaf(YType.uint32, 'unexpected'), ['int'])),
                                ('unexpected_zlb', (YLeaf(YType.uint32, 'unexpected-zlb'), ['int'])),
                            ])
                            self.validate = None
                            self.bad_hash = None
                            self.bad_length = None
                            self.ignored = None
                            self.missing = None
                            self.passed = None
                            self.failed = None
                            self.skipped = None
                            self.generate_response_failures = None
                            self.unexpected = None
                            self.unexpected_zlb = None
                            self._segment_path = lambda: "challenge-reponse"
                            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/counters/control/tunnel-xr/authentication/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2tpv2.Counters.Control.TunnelXr.Authentication.ChallengeReponse, [u'validate', u'bad_hash', u'bad_length', u'ignored', u'missing', u'passed', u'failed', u'skipped', u'generate_response_failures', u'unexpected', u'unexpected_zlb'], name, value)


                    class OverallStatistics(Entity):
                        """
                        Overall statistics
                        
                        .. attribute:: validate
                        
                        	Validate
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_hash
                        
                        	Bad hash
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_length
                        
                        	Bad length
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ignored
                        
                        	Ignored
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: missing
                        
                        	Missing
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: passed
                        
                        	Passed
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: failed
                        
                        	Failed
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: skipped
                        
                        	Skipped
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: generate_response_failures
                        
                        	Generate response fail
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unexpected
                        
                        	Unexpected
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unexpected_zlb
                        
                        	Unexpected ZLB
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'tunnel-l2tun-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(L2tpv2.Counters.Control.TunnelXr.Authentication.OverallStatistics, self).__init__()

                            self.yang_name = "overall-statistics"
                            self.yang_parent_name = "authentication"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('validate', (YLeaf(YType.uint32, 'validate'), ['int'])),
                                ('bad_hash', (YLeaf(YType.uint32, 'bad-hash'), ['int'])),
                                ('bad_length', (YLeaf(YType.uint32, 'bad-length'), ['int'])),
                                ('ignored', (YLeaf(YType.uint32, 'ignored'), ['int'])),
                                ('missing', (YLeaf(YType.uint32, 'missing'), ['int'])),
                                ('passed', (YLeaf(YType.uint32, 'passed'), ['int'])),
                                ('failed', (YLeaf(YType.uint32, 'failed'), ['int'])),
                                ('skipped', (YLeaf(YType.uint32, 'skipped'), ['int'])),
                                ('generate_response_failures', (YLeaf(YType.uint32, 'generate-response-failures'), ['int'])),
                                ('unexpected', (YLeaf(YType.uint32, 'unexpected'), ['int'])),
                                ('unexpected_zlb', (YLeaf(YType.uint32, 'unexpected-zlb'), ['int'])),
                            ])
                            self.validate = None
                            self.bad_hash = None
                            self.bad_length = None
                            self.ignored = None
                            self.missing = None
                            self.passed = None
                            self.failed = None
                            self.skipped = None
                            self.generate_response_failures = None
                            self.unexpected = None
                            self.unexpected_zlb = None
                            self._segment_path = lambda: "overall-statistics"
                            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/counters/control/tunnel-xr/authentication/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2tpv2.Counters.Control.TunnelXr.Authentication.OverallStatistics, [u'validate', u'bad_hash', u'bad_length', u'ignored', u'missing', u'passed', u'failed', u'skipped', u'generate_response_failures', u'unexpected', u'unexpected_zlb'], name, value)


                class Global(Entity):
                    """
                    Tunnel counters
                    
                    .. attribute:: transmit
                    
                    	Transmit data
                    	**type**\:  :py:class:`Transmit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Counters.Control.TunnelXr.Global.Transmit>`
                    
                    .. attribute:: retransmit
                    
                    	Re transmit data
                    	**type**\:  :py:class:`Retransmit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Counters.Control.TunnelXr.Global.Retransmit>`
                    
                    .. attribute:: received
                    
                    	Received data
                    	**type**\:  :py:class:`Received <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Counters.Control.TunnelXr.Global.Received>`
                    
                    .. attribute:: drop
                    
                    	Drop data
                    	**type**\:  :py:class:`Drop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Counters.Control.TunnelXr.Global.Drop>`
                    
                    .. attribute:: total_transmit
                    
                    	Total transmit
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: total_retransmit
                    
                    	Total retransmit
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: total_received
                    
                    	Total received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: total_drop
                    
                    	Total drop
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'tunnel-l2tun-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(L2tpv2.Counters.Control.TunnelXr.Global, self).__init__()

                        self.yang_name = "global"
                        self.yang_parent_name = "tunnel-xr"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("transmit", ("transmit", L2tpv2.Counters.Control.TunnelXr.Global.Transmit)), ("retransmit", ("retransmit", L2tpv2.Counters.Control.TunnelXr.Global.Retransmit)), ("received", ("received", L2tpv2.Counters.Control.TunnelXr.Global.Received)), ("drop", ("drop", L2tpv2.Counters.Control.TunnelXr.Global.Drop))])
                        self._leafs = OrderedDict([
                            ('total_transmit', (YLeaf(YType.uint32, 'total-transmit'), ['int'])),
                            ('total_retransmit', (YLeaf(YType.uint32, 'total-retransmit'), ['int'])),
                            ('total_received', (YLeaf(YType.uint32, 'total-received'), ['int'])),
                            ('total_drop', (YLeaf(YType.uint32, 'total-drop'), ['int'])),
                        ])
                        self.total_transmit = None
                        self.total_retransmit = None
                        self.total_received = None
                        self.total_drop = None

                        self.transmit = L2tpv2.Counters.Control.TunnelXr.Global.Transmit()
                        self.transmit.parent = self
                        self._children_name_map["transmit"] = "transmit"

                        self.retransmit = L2tpv2.Counters.Control.TunnelXr.Global.Retransmit()
                        self.retransmit.parent = self
                        self._children_name_map["retransmit"] = "retransmit"

                        self.received = L2tpv2.Counters.Control.TunnelXr.Global.Received()
                        self.received.parent = self
                        self._children_name_map["received"] = "received"

                        self.drop = L2tpv2.Counters.Control.TunnelXr.Global.Drop()
                        self.drop.parent = self
                        self._children_name_map["drop"] = "drop"
                        self._segment_path = lambda: "global"
                        self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/counters/control/tunnel-xr/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2tpv2.Counters.Control.TunnelXr.Global, [u'total_transmit', u'total_retransmit', u'total_received', u'total_drop'], name, value)


                    class Transmit(Entity):
                        """
                        Transmit data
                        
                        .. attribute:: unknown_packets
                        
                        	Unknown packets
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: zero_length_body_packets
                        
                        	Zero length body packets
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: start_control_connection_requests
                        
                        	Start control connection requests
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: start_control_connection_replies
                        
                        	Start control connection replies
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: start_control_connection_notifications
                        
                        	Start control connection notifications
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: stop_control_connection_notifications
                        
                        	Stop control connection notifications
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: hello_packets
                        
                        	Keep alive messages
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: outgoing_call_requests
                        
                        	Outgoing call requests
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: outgoing_call_replies
                        
                        	Outgoing call replies
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: outgoing_call_connected_packets
                        
                        	Outgoing call connected packets
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: incoming_call_requests
                        
                        	Incoming call requests
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: incoming_call_replies
                        
                        	Incoming call replies
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: incoming_call_connected_packets
                        
                        	Incoming call connected packets
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: call_disconnect_notify_packets
                        
                        	Call disconnect notify packets
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: wan_error_notify_packets
                        
                        	WAN error notify packets
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: set_link_info_packets
                        
                        	Set link info packets
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: service_relay_requests
                        
                        	Service relay request counts
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: service_relay_replies
                        
                        	Service relay reply counts
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: acknowledgement_packets
                        
                        	Packets acknowledgement
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'tunnel-l2tun-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(L2tpv2.Counters.Control.TunnelXr.Global.Transmit, self).__init__()

                            self.yang_name = "transmit"
                            self.yang_parent_name = "global"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('unknown_packets', (YLeaf(YType.uint32, 'unknown-packets'), ['int'])),
                                ('zero_length_body_packets', (YLeaf(YType.uint32, 'zero-length-body-packets'), ['int'])),
                                ('start_control_connection_requests', (YLeaf(YType.uint32, 'start-control-connection-requests'), ['int'])),
                                ('start_control_connection_replies', (YLeaf(YType.uint32, 'start-control-connection-replies'), ['int'])),
                                ('start_control_connection_notifications', (YLeaf(YType.uint32, 'start-control-connection-notifications'), ['int'])),
                                ('stop_control_connection_notifications', (YLeaf(YType.uint32, 'stop-control-connection-notifications'), ['int'])),
                                ('hello_packets', (YLeaf(YType.uint32, 'hello-packets'), ['int'])),
                                ('outgoing_call_requests', (YLeaf(YType.uint32, 'outgoing-call-requests'), ['int'])),
                                ('outgoing_call_replies', (YLeaf(YType.uint32, 'outgoing-call-replies'), ['int'])),
                                ('outgoing_call_connected_packets', (YLeaf(YType.uint32, 'outgoing-call-connected-packets'), ['int'])),
                                ('incoming_call_requests', (YLeaf(YType.uint32, 'incoming-call-requests'), ['int'])),
                                ('incoming_call_replies', (YLeaf(YType.uint32, 'incoming-call-replies'), ['int'])),
                                ('incoming_call_connected_packets', (YLeaf(YType.uint32, 'incoming-call-connected-packets'), ['int'])),
                                ('call_disconnect_notify_packets', (YLeaf(YType.uint32, 'call-disconnect-notify-packets'), ['int'])),
                                ('wan_error_notify_packets', (YLeaf(YType.uint32, 'wan-error-notify-packets'), ['int'])),
                                ('set_link_info_packets', (YLeaf(YType.uint32, 'set-link-info-packets'), ['int'])),
                                ('service_relay_requests', (YLeaf(YType.uint32, 'service-relay-requests'), ['int'])),
                                ('service_relay_replies', (YLeaf(YType.uint32, 'service-relay-replies'), ['int'])),
                                ('acknowledgement_packets', (YLeaf(YType.uint32, 'acknowledgement-packets'), ['int'])),
                            ])
                            self.unknown_packets = None
                            self.zero_length_body_packets = None
                            self.start_control_connection_requests = None
                            self.start_control_connection_replies = None
                            self.start_control_connection_notifications = None
                            self.stop_control_connection_notifications = None
                            self.hello_packets = None
                            self.outgoing_call_requests = None
                            self.outgoing_call_replies = None
                            self.outgoing_call_connected_packets = None
                            self.incoming_call_requests = None
                            self.incoming_call_replies = None
                            self.incoming_call_connected_packets = None
                            self.call_disconnect_notify_packets = None
                            self.wan_error_notify_packets = None
                            self.set_link_info_packets = None
                            self.service_relay_requests = None
                            self.service_relay_replies = None
                            self.acknowledgement_packets = None
                            self._segment_path = lambda: "transmit"
                            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/counters/control/tunnel-xr/global/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2tpv2.Counters.Control.TunnelXr.Global.Transmit, [u'unknown_packets', u'zero_length_body_packets', u'start_control_connection_requests', u'start_control_connection_replies', u'start_control_connection_notifications', u'stop_control_connection_notifications', u'hello_packets', u'outgoing_call_requests', u'outgoing_call_replies', u'outgoing_call_connected_packets', u'incoming_call_requests', u'incoming_call_replies', u'incoming_call_connected_packets', u'call_disconnect_notify_packets', u'wan_error_notify_packets', u'set_link_info_packets', u'service_relay_requests', u'service_relay_replies', u'acknowledgement_packets'], name, value)


                    class Retransmit(Entity):
                        """
                        Re transmit data
                        
                        .. attribute:: unknown_packets
                        
                        	Unknown packets
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: zero_length_body_packets
                        
                        	Zero length body packets
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: start_control_connection_requests
                        
                        	Start control connection requests
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: start_control_connection_replies
                        
                        	Start control connection replies
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: start_control_connection_notifications
                        
                        	Start control connection notifications
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: stop_control_connection_notifications
                        
                        	Stop control connection notifications
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: hello_packets
                        
                        	Keep alive messages
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: outgoing_call_requests
                        
                        	Outgoing call requests
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: outgoing_call_replies
                        
                        	Outgoing call replies
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: outgoing_call_connected_packets
                        
                        	Outgoing call connected packets
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: incoming_call_requests
                        
                        	Incoming call requests
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: incoming_call_replies
                        
                        	Incoming call replies
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: incoming_call_connected_packets
                        
                        	Incoming call connected packets
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: call_disconnect_notify_packets
                        
                        	Call disconnect notify packets
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: wan_error_notify_packets
                        
                        	WAN error notify packets
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: set_link_info_packets
                        
                        	Set link info packets
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: service_relay_requests
                        
                        	Service relay request counts
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: service_relay_replies
                        
                        	Service relay reply counts
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: acknowledgement_packets
                        
                        	Packets acknowledgement
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'tunnel-l2tun-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(L2tpv2.Counters.Control.TunnelXr.Global.Retransmit, self).__init__()

                            self.yang_name = "retransmit"
                            self.yang_parent_name = "global"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('unknown_packets', (YLeaf(YType.uint32, 'unknown-packets'), ['int'])),
                                ('zero_length_body_packets', (YLeaf(YType.uint32, 'zero-length-body-packets'), ['int'])),
                                ('start_control_connection_requests', (YLeaf(YType.uint32, 'start-control-connection-requests'), ['int'])),
                                ('start_control_connection_replies', (YLeaf(YType.uint32, 'start-control-connection-replies'), ['int'])),
                                ('start_control_connection_notifications', (YLeaf(YType.uint32, 'start-control-connection-notifications'), ['int'])),
                                ('stop_control_connection_notifications', (YLeaf(YType.uint32, 'stop-control-connection-notifications'), ['int'])),
                                ('hello_packets', (YLeaf(YType.uint32, 'hello-packets'), ['int'])),
                                ('outgoing_call_requests', (YLeaf(YType.uint32, 'outgoing-call-requests'), ['int'])),
                                ('outgoing_call_replies', (YLeaf(YType.uint32, 'outgoing-call-replies'), ['int'])),
                                ('outgoing_call_connected_packets', (YLeaf(YType.uint32, 'outgoing-call-connected-packets'), ['int'])),
                                ('incoming_call_requests', (YLeaf(YType.uint32, 'incoming-call-requests'), ['int'])),
                                ('incoming_call_replies', (YLeaf(YType.uint32, 'incoming-call-replies'), ['int'])),
                                ('incoming_call_connected_packets', (YLeaf(YType.uint32, 'incoming-call-connected-packets'), ['int'])),
                                ('call_disconnect_notify_packets', (YLeaf(YType.uint32, 'call-disconnect-notify-packets'), ['int'])),
                                ('wan_error_notify_packets', (YLeaf(YType.uint32, 'wan-error-notify-packets'), ['int'])),
                                ('set_link_info_packets', (YLeaf(YType.uint32, 'set-link-info-packets'), ['int'])),
                                ('service_relay_requests', (YLeaf(YType.uint32, 'service-relay-requests'), ['int'])),
                                ('service_relay_replies', (YLeaf(YType.uint32, 'service-relay-replies'), ['int'])),
                                ('acknowledgement_packets', (YLeaf(YType.uint32, 'acknowledgement-packets'), ['int'])),
                            ])
                            self.unknown_packets = None
                            self.zero_length_body_packets = None
                            self.start_control_connection_requests = None
                            self.start_control_connection_replies = None
                            self.start_control_connection_notifications = None
                            self.stop_control_connection_notifications = None
                            self.hello_packets = None
                            self.outgoing_call_requests = None
                            self.outgoing_call_replies = None
                            self.outgoing_call_connected_packets = None
                            self.incoming_call_requests = None
                            self.incoming_call_replies = None
                            self.incoming_call_connected_packets = None
                            self.call_disconnect_notify_packets = None
                            self.wan_error_notify_packets = None
                            self.set_link_info_packets = None
                            self.service_relay_requests = None
                            self.service_relay_replies = None
                            self.acknowledgement_packets = None
                            self._segment_path = lambda: "retransmit"
                            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/counters/control/tunnel-xr/global/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2tpv2.Counters.Control.TunnelXr.Global.Retransmit, [u'unknown_packets', u'zero_length_body_packets', u'start_control_connection_requests', u'start_control_connection_replies', u'start_control_connection_notifications', u'stop_control_connection_notifications', u'hello_packets', u'outgoing_call_requests', u'outgoing_call_replies', u'outgoing_call_connected_packets', u'incoming_call_requests', u'incoming_call_replies', u'incoming_call_connected_packets', u'call_disconnect_notify_packets', u'wan_error_notify_packets', u'set_link_info_packets', u'service_relay_requests', u'service_relay_replies', u'acknowledgement_packets'], name, value)


                    class Received(Entity):
                        """
                        Received data
                        
                        .. attribute:: unknown_packets
                        
                        	Unknown packets
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: zero_length_body_packets
                        
                        	Zero length body packets
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: start_control_connection_requests
                        
                        	Start control connection requests
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: start_control_connection_replies
                        
                        	Start control connection replies
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: start_control_connection_notifications
                        
                        	Start control connection notifications
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: stop_control_connection_notifications
                        
                        	Stop control connection notifications
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: hello_packets
                        
                        	Keep alive messages
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: outgoing_call_requests
                        
                        	Outgoing call requests
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: outgoing_call_replies
                        
                        	Outgoing call replies
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: outgoing_call_connected_packets
                        
                        	Outgoing call connected packets
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: incoming_call_requests
                        
                        	Incoming call requests
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: incoming_call_replies
                        
                        	Incoming call replies
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: incoming_call_connected_packets
                        
                        	Incoming call connected packets
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: call_disconnect_notify_packets
                        
                        	Call disconnect notify packets
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: wan_error_notify_packets
                        
                        	WAN error notify packets
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: set_link_info_packets
                        
                        	Set link info packets
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: service_relay_requests
                        
                        	Service relay request counts
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: service_relay_replies
                        
                        	Service relay reply counts
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: acknowledgement_packets
                        
                        	Packets acknowledgement
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'tunnel-l2tun-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(L2tpv2.Counters.Control.TunnelXr.Global.Received, self).__init__()

                            self.yang_name = "received"
                            self.yang_parent_name = "global"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('unknown_packets', (YLeaf(YType.uint32, 'unknown-packets'), ['int'])),
                                ('zero_length_body_packets', (YLeaf(YType.uint32, 'zero-length-body-packets'), ['int'])),
                                ('start_control_connection_requests', (YLeaf(YType.uint32, 'start-control-connection-requests'), ['int'])),
                                ('start_control_connection_replies', (YLeaf(YType.uint32, 'start-control-connection-replies'), ['int'])),
                                ('start_control_connection_notifications', (YLeaf(YType.uint32, 'start-control-connection-notifications'), ['int'])),
                                ('stop_control_connection_notifications', (YLeaf(YType.uint32, 'stop-control-connection-notifications'), ['int'])),
                                ('hello_packets', (YLeaf(YType.uint32, 'hello-packets'), ['int'])),
                                ('outgoing_call_requests', (YLeaf(YType.uint32, 'outgoing-call-requests'), ['int'])),
                                ('outgoing_call_replies', (YLeaf(YType.uint32, 'outgoing-call-replies'), ['int'])),
                                ('outgoing_call_connected_packets', (YLeaf(YType.uint32, 'outgoing-call-connected-packets'), ['int'])),
                                ('incoming_call_requests', (YLeaf(YType.uint32, 'incoming-call-requests'), ['int'])),
                                ('incoming_call_replies', (YLeaf(YType.uint32, 'incoming-call-replies'), ['int'])),
                                ('incoming_call_connected_packets', (YLeaf(YType.uint32, 'incoming-call-connected-packets'), ['int'])),
                                ('call_disconnect_notify_packets', (YLeaf(YType.uint32, 'call-disconnect-notify-packets'), ['int'])),
                                ('wan_error_notify_packets', (YLeaf(YType.uint32, 'wan-error-notify-packets'), ['int'])),
                                ('set_link_info_packets', (YLeaf(YType.uint32, 'set-link-info-packets'), ['int'])),
                                ('service_relay_requests', (YLeaf(YType.uint32, 'service-relay-requests'), ['int'])),
                                ('service_relay_replies', (YLeaf(YType.uint32, 'service-relay-replies'), ['int'])),
                                ('acknowledgement_packets', (YLeaf(YType.uint32, 'acknowledgement-packets'), ['int'])),
                            ])
                            self.unknown_packets = None
                            self.zero_length_body_packets = None
                            self.start_control_connection_requests = None
                            self.start_control_connection_replies = None
                            self.start_control_connection_notifications = None
                            self.stop_control_connection_notifications = None
                            self.hello_packets = None
                            self.outgoing_call_requests = None
                            self.outgoing_call_replies = None
                            self.outgoing_call_connected_packets = None
                            self.incoming_call_requests = None
                            self.incoming_call_replies = None
                            self.incoming_call_connected_packets = None
                            self.call_disconnect_notify_packets = None
                            self.wan_error_notify_packets = None
                            self.set_link_info_packets = None
                            self.service_relay_requests = None
                            self.service_relay_replies = None
                            self.acknowledgement_packets = None
                            self._segment_path = lambda: "received"
                            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/counters/control/tunnel-xr/global/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2tpv2.Counters.Control.TunnelXr.Global.Received, [u'unknown_packets', u'zero_length_body_packets', u'start_control_connection_requests', u'start_control_connection_replies', u'start_control_connection_notifications', u'stop_control_connection_notifications', u'hello_packets', u'outgoing_call_requests', u'outgoing_call_replies', u'outgoing_call_connected_packets', u'incoming_call_requests', u'incoming_call_replies', u'incoming_call_connected_packets', u'call_disconnect_notify_packets', u'wan_error_notify_packets', u'set_link_info_packets', u'service_relay_requests', u'service_relay_replies', u'acknowledgement_packets'], name, value)


                    class Drop(Entity):
                        """
                        Drop data
                        
                        .. attribute:: unknown_packets
                        
                        	Unknown packets
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: zero_length_body_packets
                        
                        	Zero length body packets
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: start_control_connection_requests
                        
                        	Start control connection requests
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: start_control_connection_replies
                        
                        	Start control connection replies
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: start_control_connection_notifications
                        
                        	Start control connection notifications
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: stop_control_connection_notifications
                        
                        	Stop control connection notifications
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: hello_packets
                        
                        	Keep alive messages
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: outgoing_call_requests
                        
                        	Outgoing call requests
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: outgoing_call_replies
                        
                        	Outgoing call replies
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: outgoing_call_connected_packets
                        
                        	Outgoing call connected packets
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: incoming_call_requests
                        
                        	Incoming call requests
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: incoming_call_replies
                        
                        	Incoming call replies
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: incoming_call_connected_packets
                        
                        	Incoming call connected packets
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: call_disconnect_notify_packets
                        
                        	Call disconnect notify packets
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: wan_error_notify_packets
                        
                        	WAN error notify packets
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: set_link_info_packets
                        
                        	Set link info packets
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: service_relay_requests
                        
                        	Service relay request counts
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: service_relay_replies
                        
                        	Service relay reply counts
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: acknowledgement_packets
                        
                        	Packets acknowledgement
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'tunnel-l2tun-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(L2tpv2.Counters.Control.TunnelXr.Global.Drop, self).__init__()

                            self.yang_name = "drop"
                            self.yang_parent_name = "global"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('unknown_packets', (YLeaf(YType.uint32, 'unknown-packets'), ['int'])),
                                ('zero_length_body_packets', (YLeaf(YType.uint32, 'zero-length-body-packets'), ['int'])),
                                ('start_control_connection_requests', (YLeaf(YType.uint32, 'start-control-connection-requests'), ['int'])),
                                ('start_control_connection_replies', (YLeaf(YType.uint32, 'start-control-connection-replies'), ['int'])),
                                ('start_control_connection_notifications', (YLeaf(YType.uint32, 'start-control-connection-notifications'), ['int'])),
                                ('stop_control_connection_notifications', (YLeaf(YType.uint32, 'stop-control-connection-notifications'), ['int'])),
                                ('hello_packets', (YLeaf(YType.uint32, 'hello-packets'), ['int'])),
                                ('outgoing_call_requests', (YLeaf(YType.uint32, 'outgoing-call-requests'), ['int'])),
                                ('outgoing_call_replies', (YLeaf(YType.uint32, 'outgoing-call-replies'), ['int'])),
                                ('outgoing_call_connected_packets', (YLeaf(YType.uint32, 'outgoing-call-connected-packets'), ['int'])),
                                ('incoming_call_requests', (YLeaf(YType.uint32, 'incoming-call-requests'), ['int'])),
                                ('incoming_call_replies', (YLeaf(YType.uint32, 'incoming-call-replies'), ['int'])),
                                ('incoming_call_connected_packets', (YLeaf(YType.uint32, 'incoming-call-connected-packets'), ['int'])),
                                ('call_disconnect_notify_packets', (YLeaf(YType.uint32, 'call-disconnect-notify-packets'), ['int'])),
                                ('wan_error_notify_packets', (YLeaf(YType.uint32, 'wan-error-notify-packets'), ['int'])),
                                ('set_link_info_packets', (YLeaf(YType.uint32, 'set-link-info-packets'), ['int'])),
                                ('service_relay_requests', (YLeaf(YType.uint32, 'service-relay-requests'), ['int'])),
                                ('service_relay_replies', (YLeaf(YType.uint32, 'service-relay-replies'), ['int'])),
                                ('acknowledgement_packets', (YLeaf(YType.uint32, 'acknowledgement-packets'), ['int'])),
                            ])
                            self.unknown_packets = None
                            self.zero_length_body_packets = None
                            self.start_control_connection_requests = None
                            self.start_control_connection_replies = None
                            self.start_control_connection_notifications = None
                            self.stop_control_connection_notifications = None
                            self.hello_packets = None
                            self.outgoing_call_requests = None
                            self.outgoing_call_replies = None
                            self.outgoing_call_connected_packets = None
                            self.incoming_call_requests = None
                            self.incoming_call_replies = None
                            self.incoming_call_connected_packets = None
                            self.call_disconnect_notify_packets = None
                            self.wan_error_notify_packets = None
                            self.set_link_info_packets = None
                            self.service_relay_requests = None
                            self.service_relay_replies = None
                            self.acknowledgement_packets = None
                            self._segment_path = lambda: "drop"
                            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/counters/control/tunnel-xr/global/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2tpv2.Counters.Control.TunnelXr.Global.Drop, [u'unknown_packets', u'zero_length_body_packets', u'start_control_connection_requests', u'start_control_connection_replies', u'start_control_connection_notifications', u'stop_control_connection_notifications', u'hello_packets', u'outgoing_call_requests', u'outgoing_call_replies', u'outgoing_call_connected_packets', u'incoming_call_requests', u'incoming_call_replies', u'incoming_call_connected_packets', u'call_disconnect_notify_packets', u'wan_error_notify_packets', u'set_link_info_packets', u'service_relay_requests', u'service_relay_replies', u'acknowledgement_packets'], name, value)


            class Tunnels(Entity):
                """
                Table of tunnel IDs of control message counters
                
                .. attribute:: tunnel
                
                	L2TP tunnel control message counters
                	**type**\: list of  		 :py:class:`Tunnel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Counters.Control.Tunnels.Tunnel>`
                
                

                """

                _prefix = 'tunnel-l2tun-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(L2tpv2.Counters.Control.Tunnels, self).__init__()

                    self.yang_name = "tunnels"
                    self.yang_parent_name = "control"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("tunnel", ("tunnel", L2tpv2.Counters.Control.Tunnels.Tunnel))])
                    self._leafs = OrderedDict()

                    self.tunnel = YList(self)
                    self._segment_path = lambda: "tunnels"
                    self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/counters/control/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(L2tpv2.Counters.Control.Tunnels, [], name, value)


                class Tunnel(Entity):
                    """
                    L2TP tunnel control message counters
                    
                    .. attribute:: tunnel_id  (key)
                    
                    	L2TP tunnel ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: brief
                    
                    	L2TP control message local and remote addresses
                    	**type**\:  :py:class:`Brief <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Counters.Control.Tunnels.Tunnel.Brief>`
                    
                    .. attribute:: global_
                    
                    	Global data
                    	**type**\:  :py:class:`Global <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Counters.Control.Tunnels.Tunnel.Global>`
                    
                    

                    """

                    _prefix = 'tunnel-l2tun-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(L2tpv2.Counters.Control.Tunnels.Tunnel, self).__init__()

                        self.yang_name = "tunnel"
                        self.yang_parent_name = "tunnels"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['tunnel_id']
                        self._child_classes = OrderedDict([("brief", ("brief", L2tpv2.Counters.Control.Tunnels.Tunnel.Brief)), ("global", ("global_", L2tpv2.Counters.Control.Tunnels.Tunnel.Global))])
                        self._leafs = OrderedDict([
                            ('tunnel_id', (YLeaf(YType.uint32, 'tunnel-id'), ['int'])),
                        ])
                        self.tunnel_id = None

                        self.brief = L2tpv2.Counters.Control.Tunnels.Tunnel.Brief()
                        self.brief.parent = self
                        self._children_name_map["brief"] = "brief"

                        self.global_ = L2tpv2.Counters.Control.Tunnels.Tunnel.Global()
                        self.global_.parent = self
                        self._children_name_map["global_"] = "global"
                        self._segment_path = lambda: "tunnel" + "[tunnel-id='" + str(self.tunnel_id) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/counters/control/tunnels/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2tpv2.Counters.Control.Tunnels.Tunnel, ['tunnel_id'], name, value)


                    class Brief(Entity):
                        """
                        L2TP control message local and remote addresses
                        
                        .. attribute:: remote_tunnel_id
                        
                        	Remote tunnel ID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: local_address
                        
                        	Local IP address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: remote_address
                        
                        	Remote IP address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'tunnel-l2tun-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(L2tpv2.Counters.Control.Tunnels.Tunnel.Brief, self).__init__()

                            self.yang_name = "brief"
                            self.yang_parent_name = "tunnel"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('remote_tunnel_id', (YLeaf(YType.uint32, 'remote-tunnel-id'), ['int'])),
                                ('local_address', (YLeaf(YType.str, 'local-address'), ['str'])),
                                ('remote_address', (YLeaf(YType.str, 'remote-address'), ['str'])),
                            ])
                            self.remote_tunnel_id = None
                            self.local_address = None
                            self.remote_address = None
                            self._segment_path = lambda: "brief"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2tpv2.Counters.Control.Tunnels.Tunnel.Brief, [u'remote_tunnel_id', u'local_address', u'remote_address'], name, value)


                    class Global(Entity):
                        """
                        Global data
                        
                        .. attribute:: transmit
                        
                        	Transmit data
                        	**type**\:  :py:class:`Transmit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Counters.Control.Tunnels.Tunnel.Global.Transmit>`
                        
                        .. attribute:: retransmit
                        
                        	Re transmit data
                        	**type**\:  :py:class:`Retransmit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Counters.Control.Tunnels.Tunnel.Global.Retransmit>`
                        
                        .. attribute:: received
                        
                        	Received data
                        	**type**\:  :py:class:`Received <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Counters.Control.Tunnels.Tunnel.Global.Received>`
                        
                        .. attribute:: drop
                        
                        	Drop data
                        	**type**\:  :py:class:`Drop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Counters.Control.Tunnels.Tunnel.Global.Drop>`
                        
                        .. attribute:: total_transmit
                        
                        	Total transmit
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: total_retransmit
                        
                        	Total retransmit
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: total_received
                        
                        	Total received
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: total_drop
                        
                        	Total drop
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'tunnel-l2tun-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(L2tpv2.Counters.Control.Tunnels.Tunnel.Global, self).__init__()

                            self.yang_name = "global"
                            self.yang_parent_name = "tunnel"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("transmit", ("transmit", L2tpv2.Counters.Control.Tunnels.Tunnel.Global.Transmit)), ("retransmit", ("retransmit", L2tpv2.Counters.Control.Tunnels.Tunnel.Global.Retransmit)), ("received", ("received", L2tpv2.Counters.Control.Tunnels.Tunnel.Global.Received)), ("drop", ("drop", L2tpv2.Counters.Control.Tunnels.Tunnel.Global.Drop))])
                            self._leafs = OrderedDict([
                                ('total_transmit', (YLeaf(YType.uint32, 'total-transmit'), ['int'])),
                                ('total_retransmit', (YLeaf(YType.uint32, 'total-retransmit'), ['int'])),
                                ('total_received', (YLeaf(YType.uint32, 'total-received'), ['int'])),
                                ('total_drop', (YLeaf(YType.uint32, 'total-drop'), ['int'])),
                            ])
                            self.total_transmit = None
                            self.total_retransmit = None
                            self.total_received = None
                            self.total_drop = None

                            self.transmit = L2tpv2.Counters.Control.Tunnels.Tunnel.Global.Transmit()
                            self.transmit.parent = self
                            self._children_name_map["transmit"] = "transmit"

                            self.retransmit = L2tpv2.Counters.Control.Tunnels.Tunnel.Global.Retransmit()
                            self.retransmit.parent = self
                            self._children_name_map["retransmit"] = "retransmit"

                            self.received = L2tpv2.Counters.Control.Tunnels.Tunnel.Global.Received()
                            self.received.parent = self
                            self._children_name_map["received"] = "received"

                            self.drop = L2tpv2.Counters.Control.Tunnels.Tunnel.Global.Drop()
                            self.drop.parent = self
                            self._children_name_map["drop"] = "drop"
                            self._segment_path = lambda: "global"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2tpv2.Counters.Control.Tunnels.Tunnel.Global, [u'total_transmit', u'total_retransmit', u'total_received', u'total_drop'], name, value)


                        class Transmit(Entity):
                            """
                            Transmit data
                            
                            .. attribute:: unknown_packets
                            
                            	Unknown packets
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: zero_length_body_packets
                            
                            	Zero length body packets
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: start_control_connection_requests
                            
                            	Start control connection requests
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: start_control_connection_replies
                            
                            	Start control connection replies
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: start_control_connection_notifications
                            
                            	Start control connection notifications
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: stop_control_connection_notifications
                            
                            	Stop control connection notifications
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: hello_packets
                            
                            	Keep alive messages
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: outgoing_call_requests
                            
                            	Outgoing call requests
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: outgoing_call_replies
                            
                            	Outgoing call replies
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: outgoing_call_connected_packets
                            
                            	Outgoing call connected packets
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: incoming_call_requests
                            
                            	Incoming call requests
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: incoming_call_replies
                            
                            	Incoming call replies
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: incoming_call_connected_packets
                            
                            	Incoming call connected packets
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: call_disconnect_notify_packets
                            
                            	Call disconnect notify packets
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: wan_error_notify_packets
                            
                            	WAN error notify packets
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: set_link_info_packets
                            
                            	Set link info packets
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: service_relay_requests
                            
                            	Service relay request counts
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: service_relay_replies
                            
                            	Service relay reply counts
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: acknowledgement_packets
                            
                            	Packets acknowledgement
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'tunnel-l2tun-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(L2tpv2.Counters.Control.Tunnels.Tunnel.Global.Transmit, self).__init__()

                                self.yang_name = "transmit"
                                self.yang_parent_name = "global"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('unknown_packets', (YLeaf(YType.uint32, 'unknown-packets'), ['int'])),
                                    ('zero_length_body_packets', (YLeaf(YType.uint32, 'zero-length-body-packets'), ['int'])),
                                    ('start_control_connection_requests', (YLeaf(YType.uint32, 'start-control-connection-requests'), ['int'])),
                                    ('start_control_connection_replies', (YLeaf(YType.uint32, 'start-control-connection-replies'), ['int'])),
                                    ('start_control_connection_notifications', (YLeaf(YType.uint32, 'start-control-connection-notifications'), ['int'])),
                                    ('stop_control_connection_notifications', (YLeaf(YType.uint32, 'stop-control-connection-notifications'), ['int'])),
                                    ('hello_packets', (YLeaf(YType.uint32, 'hello-packets'), ['int'])),
                                    ('outgoing_call_requests', (YLeaf(YType.uint32, 'outgoing-call-requests'), ['int'])),
                                    ('outgoing_call_replies', (YLeaf(YType.uint32, 'outgoing-call-replies'), ['int'])),
                                    ('outgoing_call_connected_packets', (YLeaf(YType.uint32, 'outgoing-call-connected-packets'), ['int'])),
                                    ('incoming_call_requests', (YLeaf(YType.uint32, 'incoming-call-requests'), ['int'])),
                                    ('incoming_call_replies', (YLeaf(YType.uint32, 'incoming-call-replies'), ['int'])),
                                    ('incoming_call_connected_packets', (YLeaf(YType.uint32, 'incoming-call-connected-packets'), ['int'])),
                                    ('call_disconnect_notify_packets', (YLeaf(YType.uint32, 'call-disconnect-notify-packets'), ['int'])),
                                    ('wan_error_notify_packets', (YLeaf(YType.uint32, 'wan-error-notify-packets'), ['int'])),
                                    ('set_link_info_packets', (YLeaf(YType.uint32, 'set-link-info-packets'), ['int'])),
                                    ('service_relay_requests', (YLeaf(YType.uint32, 'service-relay-requests'), ['int'])),
                                    ('service_relay_replies', (YLeaf(YType.uint32, 'service-relay-replies'), ['int'])),
                                    ('acknowledgement_packets', (YLeaf(YType.uint32, 'acknowledgement-packets'), ['int'])),
                                ])
                                self.unknown_packets = None
                                self.zero_length_body_packets = None
                                self.start_control_connection_requests = None
                                self.start_control_connection_replies = None
                                self.start_control_connection_notifications = None
                                self.stop_control_connection_notifications = None
                                self.hello_packets = None
                                self.outgoing_call_requests = None
                                self.outgoing_call_replies = None
                                self.outgoing_call_connected_packets = None
                                self.incoming_call_requests = None
                                self.incoming_call_replies = None
                                self.incoming_call_connected_packets = None
                                self.call_disconnect_notify_packets = None
                                self.wan_error_notify_packets = None
                                self.set_link_info_packets = None
                                self.service_relay_requests = None
                                self.service_relay_replies = None
                                self.acknowledgement_packets = None
                                self._segment_path = lambda: "transmit"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2tpv2.Counters.Control.Tunnels.Tunnel.Global.Transmit, [u'unknown_packets', u'zero_length_body_packets', u'start_control_connection_requests', u'start_control_connection_replies', u'start_control_connection_notifications', u'stop_control_connection_notifications', u'hello_packets', u'outgoing_call_requests', u'outgoing_call_replies', u'outgoing_call_connected_packets', u'incoming_call_requests', u'incoming_call_replies', u'incoming_call_connected_packets', u'call_disconnect_notify_packets', u'wan_error_notify_packets', u'set_link_info_packets', u'service_relay_requests', u'service_relay_replies', u'acknowledgement_packets'], name, value)


                        class Retransmit(Entity):
                            """
                            Re transmit data
                            
                            .. attribute:: unknown_packets
                            
                            	Unknown packets
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: zero_length_body_packets
                            
                            	Zero length body packets
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: start_control_connection_requests
                            
                            	Start control connection requests
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: start_control_connection_replies
                            
                            	Start control connection replies
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: start_control_connection_notifications
                            
                            	Start control connection notifications
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: stop_control_connection_notifications
                            
                            	Stop control connection notifications
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: hello_packets
                            
                            	Keep alive messages
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: outgoing_call_requests
                            
                            	Outgoing call requests
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: outgoing_call_replies
                            
                            	Outgoing call replies
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: outgoing_call_connected_packets
                            
                            	Outgoing call connected packets
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: incoming_call_requests
                            
                            	Incoming call requests
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: incoming_call_replies
                            
                            	Incoming call replies
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: incoming_call_connected_packets
                            
                            	Incoming call connected packets
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: call_disconnect_notify_packets
                            
                            	Call disconnect notify packets
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: wan_error_notify_packets
                            
                            	WAN error notify packets
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: set_link_info_packets
                            
                            	Set link info packets
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: service_relay_requests
                            
                            	Service relay request counts
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: service_relay_replies
                            
                            	Service relay reply counts
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: acknowledgement_packets
                            
                            	Packets acknowledgement
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'tunnel-l2tun-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(L2tpv2.Counters.Control.Tunnels.Tunnel.Global.Retransmit, self).__init__()

                                self.yang_name = "retransmit"
                                self.yang_parent_name = "global"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('unknown_packets', (YLeaf(YType.uint32, 'unknown-packets'), ['int'])),
                                    ('zero_length_body_packets', (YLeaf(YType.uint32, 'zero-length-body-packets'), ['int'])),
                                    ('start_control_connection_requests', (YLeaf(YType.uint32, 'start-control-connection-requests'), ['int'])),
                                    ('start_control_connection_replies', (YLeaf(YType.uint32, 'start-control-connection-replies'), ['int'])),
                                    ('start_control_connection_notifications', (YLeaf(YType.uint32, 'start-control-connection-notifications'), ['int'])),
                                    ('stop_control_connection_notifications', (YLeaf(YType.uint32, 'stop-control-connection-notifications'), ['int'])),
                                    ('hello_packets', (YLeaf(YType.uint32, 'hello-packets'), ['int'])),
                                    ('outgoing_call_requests', (YLeaf(YType.uint32, 'outgoing-call-requests'), ['int'])),
                                    ('outgoing_call_replies', (YLeaf(YType.uint32, 'outgoing-call-replies'), ['int'])),
                                    ('outgoing_call_connected_packets', (YLeaf(YType.uint32, 'outgoing-call-connected-packets'), ['int'])),
                                    ('incoming_call_requests', (YLeaf(YType.uint32, 'incoming-call-requests'), ['int'])),
                                    ('incoming_call_replies', (YLeaf(YType.uint32, 'incoming-call-replies'), ['int'])),
                                    ('incoming_call_connected_packets', (YLeaf(YType.uint32, 'incoming-call-connected-packets'), ['int'])),
                                    ('call_disconnect_notify_packets', (YLeaf(YType.uint32, 'call-disconnect-notify-packets'), ['int'])),
                                    ('wan_error_notify_packets', (YLeaf(YType.uint32, 'wan-error-notify-packets'), ['int'])),
                                    ('set_link_info_packets', (YLeaf(YType.uint32, 'set-link-info-packets'), ['int'])),
                                    ('service_relay_requests', (YLeaf(YType.uint32, 'service-relay-requests'), ['int'])),
                                    ('service_relay_replies', (YLeaf(YType.uint32, 'service-relay-replies'), ['int'])),
                                    ('acknowledgement_packets', (YLeaf(YType.uint32, 'acknowledgement-packets'), ['int'])),
                                ])
                                self.unknown_packets = None
                                self.zero_length_body_packets = None
                                self.start_control_connection_requests = None
                                self.start_control_connection_replies = None
                                self.start_control_connection_notifications = None
                                self.stop_control_connection_notifications = None
                                self.hello_packets = None
                                self.outgoing_call_requests = None
                                self.outgoing_call_replies = None
                                self.outgoing_call_connected_packets = None
                                self.incoming_call_requests = None
                                self.incoming_call_replies = None
                                self.incoming_call_connected_packets = None
                                self.call_disconnect_notify_packets = None
                                self.wan_error_notify_packets = None
                                self.set_link_info_packets = None
                                self.service_relay_requests = None
                                self.service_relay_replies = None
                                self.acknowledgement_packets = None
                                self._segment_path = lambda: "retransmit"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2tpv2.Counters.Control.Tunnels.Tunnel.Global.Retransmit, [u'unknown_packets', u'zero_length_body_packets', u'start_control_connection_requests', u'start_control_connection_replies', u'start_control_connection_notifications', u'stop_control_connection_notifications', u'hello_packets', u'outgoing_call_requests', u'outgoing_call_replies', u'outgoing_call_connected_packets', u'incoming_call_requests', u'incoming_call_replies', u'incoming_call_connected_packets', u'call_disconnect_notify_packets', u'wan_error_notify_packets', u'set_link_info_packets', u'service_relay_requests', u'service_relay_replies', u'acknowledgement_packets'], name, value)


                        class Received(Entity):
                            """
                            Received data
                            
                            .. attribute:: unknown_packets
                            
                            	Unknown packets
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: zero_length_body_packets
                            
                            	Zero length body packets
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: start_control_connection_requests
                            
                            	Start control connection requests
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: start_control_connection_replies
                            
                            	Start control connection replies
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: start_control_connection_notifications
                            
                            	Start control connection notifications
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: stop_control_connection_notifications
                            
                            	Stop control connection notifications
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: hello_packets
                            
                            	Keep alive messages
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: outgoing_call_requests
                            
                            	Outgoing call requests
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: outgoing_call_replies
                            
                            	Outgoing call replies
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: outgoing_call_connected_packets
                            
                            	Outgoing call connected packets
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: incoming_call_requests
                            
                            	Incoming call requests
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: incoming_call_replies
                            
                            	Incoming call replies
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: incoming_call_connected_packets
                            
                            	Incoming call connected packets
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: call_disconnect_notify_packets
                            
                            	Call disconnect notify packets
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: wan_error_notify_packets
                            
                            	WAN error notify packets
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: set_link_info_packets
                            
                            	Set link info packets
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: service_relay_requests
                            
                            	Service relay request counts
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: service_relay_replies
                            
                            	Service relay reply counts
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: acknowledgement_packets
                            
                            	Packets acknowledgement
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'tunnel-l2tun-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(L2tpv2.Counters.Control.Tunnels.Tunnel.Global.Received, self).__init__()

                                self.yang_name = "received"
                                self.yang_parent_name = "global"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('unknown_packets', (YLeaf(YType.uint32, 'unknown-packets'), ['int'])),
                                    ('zero_length_body_packets', (YLeaf(YType.uint32, 'zero-length-body-packets'), ['int'])),
                                    ('start_control_connection_requests', (YLeaf(YType.uint32, 'start-control-connection-requests'), ['int'])),
                                    ('start_control_connection_replies', (YLeaf(YType.uint32, 'start-control-connection-replies'), ['int'])),
                                    ('start_control_connection_notifications', (YLeaf(YType.uint32, 'start-control-connection-notifications'), ['int'])),
                                    ('stop_control_connection_notifications', (YLeaf(YType.uint32, 'stop-control-connection-notifications'), ['int'])),
                                    ('hello_packets', (YLeaf(YType.uint32, 'hello-packets'), ['int'])),
                                    ('outgoing_call_requests', (YLeaf(YType.uint32, 'outgoing-call-requests'), ['int'])),
                                    ('outgoing_call_replies', (YLeaf(YType.uint32, 'outgoing-call-replies'), ['int'])),
                                    ('outgoing_call_connected_packets', (YLeaf(YType.uint32, 'outgoing-call-connected-packets'), ['int'])),
                                    ('incoming_call_requests', (YLeaf(YType.uint32, 'incoming-call-requests'), ['int'])),
                                    ('incoming_call_replies', (YLeaf(YType.uint32, 'incoming-call-replies'), ['int'])),
                                    ('incoming_call_connected_packets', (YLeaf(YType.uint32, 'incoming-call-connected-packets'), ['int'])),
                                    ('call_disconnect_notify_packets', (YLeaf(YType.uint32, 'call-disconnect-notify-packets'), ['int'])),
                                    ('wan_error_notify_packets', (YLeaf(YType.uint32, 'wan-error-notify-packets'), ['int'])),
                                    ('set_link_info_packets', (YLeaf(YType.uint32, 'set-link-info-packets'), ['int'])),
                                    ('service_relay_requests', (YLeaf(YType.uint32, 'service-relay-requests'), ['int'])),
                                    ('service_relay_replies', (YLeaf(YType.uint32, 'service-relay-replies'), ['int'])),
                                    ('acknowledgement_packets', (YLeaf(YType.uint32, 'acknowledgement-packets'), ['int'])),
                                ])
                                self.unknown_packets = None
                                self.zero_length_body_packets = None
                                self.start_control_connection_requests = None
                                self.start_control_connection_replies = None
                                self.start_control_connection_notifications = None
                                self.stop_control_connection_notifications = None
                                self.hello_packets = None
                                self.outgoing_call_requests = None
                                self.outgoing_call_replies = None
                                self.outgoing_call_connected_packets = None
                                self.incoming_call_requests = None
                                self.incoming_call_replies = None
                                self.incoming_call_connected_packets = None
                                self.call_disconnect_notify_packets = None
                                self.wan_error_notify_packets = None
                                self.set_link_info_packets = None
                                self.service_relay_requests = None
                                self.service_relay_replies = None
                                self.acknowledgement_packets = None
                                self._segment_path = lambda: "received"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2tpv2.Counters.Control.Tunnels.Tunnel.Global.Received, [u'unknown_packets', u'zero_length_body_packets', u'start_control_connection_requests', u'start_control_connection_replies', u'start_control_connection_notifications', u'stop_control_connection_notifications', u'hello_packets', u'outgoing_call_requests', u'outgoing_call_replies', u'outgoing_call_connected_packets', u'incoming_call_requests', u'incoming_call_replies', u'incoming_call_connected_packets', u'call_disconnect_notify_packets', u'wan_error_notify_packets', u'set_link_info_packets', u'service_relay_requests', u'service_relay_replies', u'acknowledgement_packets'], name, value)


                        class Drop(Entity):
                            """
                            Drop data
                            
                            .. attribute:: unknown_packets
                            
                            	Unknown packets
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: zero_length_body_packets
                            
                            	Zero length body packets
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: start_control_connection_requests
                            
                            	Start control connection requests
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: start_control_connection_replies
                            
                            	Start control connection replies
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: start_control_connection_notifications
                            
                            	Start control connection notifications
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: stop_control_connection_notifications
                            
                            	Stop control connection notifications
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: hello_packets
                            
                            	Keep alive messages
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: outgoing_call_requests
                            
                            	Outgoing call requests
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: outgoing_call_replies
                            
                            	Outgoing call replies
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: outgoing_call_connected_packets
                            
                            	Outgoing call connected packets
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: incoming_call_requests
                            
                            	Incoming call requests
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: incoming_call_replies
                            
                            	Incoming call replies
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: incoming_call_connected_packets
                            
                            	Incoming call connected packets
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: call_disconnect_notify_packets
                            
                            	Call disconnect notify packets
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: wan_error_notify_packets
                            
                            	WAN error notify packets
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: set_link_info_packets
                            
                            	Set link info packets
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: service_relay_requests
                            
                            	Service relay request counts
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: service_relay_replies
                            
                            	Service relay reply counts
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: acknowledgement_packets
                            
                            	Packets acknowledgement
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'tunnel-l2tun-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(L2tpv2.Counters.Control.Tunnels.Tunnel.Global.Drop, self).__init__()

                                self.yang_name = "drop"
                                self.yang_parent_name = "global"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('unknown_packets', (YLeaf(YType.uint32, 'unknown-packets'), ['int'])),
                                    ('zero_length_body_packets', (YLeaf(YType.uint32, 'zero-length-body-packets'), ['int'])),
                                    ('start_control_connection_requests', (YLeaf(YType.uint32, 'start-control-connection-requests'), ['int'])),
                                    ('start_control_connection_replies', (YLeaf(YType.uint32, 'start-control-connection-replies'), ['int'])),
                                    ('start_control_connection_notifications', (YLeaf(YType.uint32, 'start-control-connection-notifications'), ['int'])),
                                    ('stop_control_connection_notifications', (YLeaf(YType.uint32, 'stop-control-connection-notifications'), ['int'])),
                                    ('hello_packets', (YLeaf(YType.uint32, 'hello-packets'), ['int'])),
                                    ('outgoing_call_requests', (YLeaf(YType.uint32, 'outgoing-call-requests'), ['int'])),
                                    ('outgoing_call_replies', (YLeaf(YType.uint32, 'outgoing-call-replies'), ['int'])),
                                    ('outgoing_call_connected_packets', (YLeaf(YType.uint32, 'outgoing-call-connected-packets'), ['int'])),
                                    ('incoming_call_requests', (YLeaf(YType.uint32, 'incoming-call-requests'), ['int'])),
                                    ('incoming_call_replies', (YLeaf(YType.uint32, 'incoming-call-replies'), ['int'])),
                                    ('incoming_call_connected_packets', (YLeaf(YType.uint32, 'incoming-call-connected-packets'), ['int'])),
                                    ('call_disconnect_notify_packets', (YLeaf(YType.uint32, 'call-disconnect-notify-packets'), ['int'])),
                                    ('wan_error_notify_packets', (YLeaf(YType.uint32, 'wan-error-notify-packets'), ['int'])),
                                    ('set_link_info_packets', (YLeaf(YType.uint32, 'set-link-info-packets'), ['int'])),
                                    ('service_relay_requests', (YLeaf(YType.uint32, 'service-relay-requests'), ['int'])),
                                    ('service_relay_replies', (YLeaf(YType.uint32, 'service-relay-replies'), ['int'])),
                                    ('acknowledgement_packets', (YLeaf(YType.uint32, 'acknowledgement-packets'), ['int'])),
                                ])
                                self.unknown_packets = None
                                self.zero_length_body_packets = None
                                self.start_control_connection_requests = None
                                self.start_control_connection_replies = None
                                self.start_control_connection_notifications = None
                                self.stop_control_connection_notifications = None
                                self.hello_packets = None
                                self.outgoing_call_requests = None
                                self.outgoing_call_replies = None
                                self.outgoing_call_connected_packets = None
                                self.incoming_call_requests = None
                                self.incoming_call_replies = None
                                self.incoming_call_connected_packets = None
                                self.call_disconnect_notify_packets = None
                                self.wan_error_notify_packets = None
                                self.set_link_info_packets = None
                                self.service_relay_requests = None
                                self.service_relay_replies = None
                                self.acknowledgement_packets = None
                                self._segment_path = lambda: "drop"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2tpv2.Counters.Control.Tunnels.Tunnel.Global.Drop, [u'unknown_packets', u'zero_length_body_packets', u'start_control_connection_requests', u'start_control_connection_replies', u'start_control_connection_notifications', u'stop_control_connection_notifications', u'hello_packets', u'outgoing_call_requests', u'outgoing_call_replies', u'outgoing_call_connected_packets', u'incoming_call_requests', u'incoming_call_replies', u'incoming_call_connected_packets', u'call_disconnect_notify_packets', u'wan_error_notify_packets', u'set_link_info_packets', u'service_relay_requests', u'service_relay_replies', u'acknowledgement_packets'], name, value)


    class Statistics(Entity):
        """
        L2TP v2 statistics information
        
        .. attribute:: tunnels
        
        	Number of tunnels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: sessions
        
        	Number of sessions
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: sent_packets
        
        	Number of packets sent
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: received_packets
        
        	Number of packets received
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: average_packet_processing_time
        
        	Average processing time for received packets  (in micro seconds)
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: microsecond
        
        .. attribute:: received_out_of_order_packets
        
        	Out of order packets received
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: reorder_packets
        
        	Re order packets
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: reorder_deviation_packets
        
        	Re order deviation
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: incoming_dropped_packets
        
        	In coming packets dropped
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: buffered_packets
        
        	Bufferred packets
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: netio_packets
        
        	Packets RX in netio
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'tunnel-l2tun-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(L2tpv2.Statistics, self).__init__()

            self.yang_name = "statistics"
            self.yang_parent_name = "l2tpv2"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('tunnels', (YLeaf(YType.uint32, 'tunnels'), ['int'])),
                ('sessions', (YLeaf(YType.uint32, 'sessions'), ['int'])),
                ('sent_packets', (YLeaf(YType.uint32, 'sent-packets'), ['int'])),
                ('received_packets', (YLeaf(YType.uint32, 'received-packets'), ['int'])),
                ('average_packet_processing_time', (YLeaf(YType.uint32, 'average-packet-processing-time'), ['int'])),
                ('received_out_of_order_packets', (YLeaf(YType.uint32, 'received-out-of-order-packets'), ['int'])),
                ('reorder_packets', (YLeaf(YType.uint32, 'reorder-packets'), ['int'])),
                ('reorder_deviation_packets', (YLeaf(YType.uint32, 'reorder-deviation-packets'), ['int'])),
                ('incoming_dropped_packets', (YLeaf(YType.uint32, 'incoming-dropped-packets'), ['int'])),
                ('buffered_packets', (YLeaf(YType.uint32, 'buffered-packets'), ['int'])),
                ('netio_packets', (YLeaf(YType.uint32, 'netio-packets'), ['int'])),
            ])
            self.tunnels = None
            self.sessions = None
            self.sent_packets = None
            self.received_packets = None
            self.average_packet_processing_time = None
            self.received_out_of_order_packets = None
            self.reorder_packets = None
            self.reorder_deviation_packets = None
            self.incoming_dropped_packets = None
            self.buffered_packets = None
            self.netio_packets = None
            self._segment_path = lambda: "statistics"
            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(L2tpv2.Statistics, [u'tunnels', u'sessions', u'sent_packets', u'received_packets', u'average_packet_processing_time', u'received_out_of_order_packets', u'reorder_packets', u'reorder_deviation_packets', u'incoming_dropped_packets', u'buffered_packets', u'netio_packets'], name, value)


    class Tunnel(Entity):
        """
        L2TPv2 tunnel 
        
        .. attribute:: accounting
        
        	Tunnel accounting counters
        	**type**\:  :py:class:`Accounting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Tunnel.Accounting>`
        
        

        """

        _prefix = 'tunnel-l2tun-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(L2tpv2.Tunnel, self).__init__()

            self.yang_name = "tunnel"
            self.yang_parent_name = "l2tpv2"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("accounting", ("accounting", L2tpv2.Tunnel.Accounting))])
            self._leafs = OrderedDict()

            self.accounting = L2tpv2.Tunnel.Accounting()
            self.accounting.parent = self
            self._children_name_map["accounting"] = "accounting"
            self._segment_path = lambda: "tunnel"
            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(L2tpv2.Tunnel, [], name, value)


        class Accounting(Entity):
            """
            Tunnel accounting counters
            
            .. attribute:: statistics
            
            	Tunnel accounting statistics
            	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Tunnel.Accounting.Statistics>`
            
            

            """

            _prefix = 'tunnel-l2tun-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(L2tpv2.Tunnel.Accounting, self).__init__()

                self.yang_name = "accounting"
                self.yang_parent_name = "tunnel"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("statistics", ("statistics", L2tpv2.Tunnel.Accounting.Statistics))])
                self._leafs = OrderedDict()

                self.statistics = L2tpv2.Tunnel.Accounting.Statistics()
                self.statistics.parent = self
                self._children_name_map["statistics"] = "statistics"
                self._segment_path = lambda: "accounting"
                self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/tunnel/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(L2tpv2.Tunnel.Accounting, [], name, value)


            class Statistics(Entity):
                """
                Tunnel accounting statistics
                
                .. attribute:: records_sent_successfully
                
                	Accounting records sent successfully
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: start
                
                	Accounting start
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: stop
                
                	Accounting stop
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: reject
                
                	Accounting reject
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: transport_failures
                
                	Transport failures
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: positive_acknowledgement
                
                	Positive acknowledgement
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: negative_acknowledgement
                
                	Negative acknowledgement
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: records_checkpointed
                
                	Total records checkpointed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: records_failed_to_checkpoint
                
                	Records fail to checkpoint
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: records_sent_from_queue
                
                	Records sent from queue
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: memory_failures
                
                	Memory failures
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: current_size
                
                	Current checkpoint size
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: records_recovered_from_checkpoint
                
                	Records recovered from checkpoint
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: records_fail_to_recover
                
                	Records fail to recover
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: queue_statistics_size
                
                	Queue statistics size
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                

                """

                _prefix = 'tunnel-l2tun-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(L2tpv2.Tunnel.Accounting.Statistics, self).__init__()

                    self.yang_name = "statistics"
                    self.yang_parent_name = "accounting"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('records_sent_successfully', (YLeaf(YType.uint64, 'records-sent-successfully'), ['int'])),
                        ('start', (YLeaf(YType.uint64, 'start'), ['int'])),
                        ('stop', (YLeaf(YType.uint64, 'stop'), ['int'])),
                        ('reject', (YLeaf(YType.uint64, 'reject'), ['int'])),
                        ('transport_failures', (YLeaf(YType.uint64, 'transport-failures'), ['int'])),
                        ('positive_acknowledgement', (YLeaf(YType.uint64, 'positive-acknowledgement'), ['int'])),
                        ('negative_acknowledgement', (YLeaf(YType.uint64, 'negative-acknowledgement'), ['int'])),
                        ('records_checkpointed', (YLeaf(YType.uint64, 'records-checkpointed'), ['int'])),
                        ('records_failed_to_checkpoint', (YLeaf(YType.uint64, 'records-failed-to-checkpoint'), ['int'])),
                        ('records_sent_from_queue', (YLeaf(YType.uint64, 'records-sent-from-queue'), ['int'])),
                        ('memory_failures', (YLeaf(YType.uint32, 'memory-failures'), ['int'])),
                        ('current_size', (YLeaf(YType.uint32, 'current-size'), ['int'])),
                        ('records_recovered_from_checkpoint', (YLeaf(YType.uint32, 'records-recovered-from-checkpoint'), ['int'])),
                        ('records_fail_to_recover', (YLeaf(YType.uint32, 'records-fail-to-recover'), ['int'])),
                        ('queue_statistics_size', (YLeaf(YType.int32, 'queue-statistics-size'), ['int'])),
                    ])
                    self.records_sent_successfully = None
                    self.start = None
                    self.stop = None
                    self.reject = None
                    self.transport_failures = None
                    self.positive_acknowledgement = None
                    self.negative_acknowledgement = None
                    self.records_checkpointed = None
                    self.records_failed_to_checkpoint = None
                    self.records_sent_from_queue = None
                    self.memory_failures = None
                    self.current_size = None
                    self.records_recovered_from_checkpoint = None
                    self.records_fail_to_recover = None
                    self.queue_statistics_size = None
                    self._segment_path = lambda: "statistics"
                    self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/tunnel/accounting/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(L2tpv2.Tunnel.Accounting.Statistics, [u'records_sent_successfully', u'start', u'stop', u'reject', u'transport_failures', u'positive_acknowledgement', u'negative_acknowledgement', u'records_checkpointed', u'records_failed_to_checkpoint', u'records_sent_from_queue', u'memory_failures', u'current_size', u'records_recovered_from_checkpoint', u'records_fail_to_recover', u'queue_statistics_size'], name, value)


    class TunnelConfigurations(Entity):
        """
        List of tunnel IDs
        
        .. attribute:: tunnel_configuration
        
        	L2TP tunnel information
        	**type**\: list of  		 :py:class:`TunnelConfiguration <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.TunnelConfigurations.TunnelConfiguration>`
        
        

        """

        _prefix = 'tunnel-l2tun-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(L2tpv2.TunnelConfigurations, self).__init__()

            self.yang_name = "tunnel-configurations"
            self.yang_parent_name = "l2tpv2"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("tunnel-configuration", ("tunnel_configuration", L2tpv2.TunnelConfigurations.TunnelConfiguration))])
            self._leafs = OrderedDict()

            self.tunnel_configuration = YList(self)
            self._segment_path = lambda: "tunnel-configurations"
            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(L2tpv2.TunnelConfigurations, [], name, value)


        class TunnelConfiguration(Entity):
            """
            L2TP tunnel information
            
            .. attribute:: local_tunnel_id  (key)
            
            	Local tunnel ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: l2tp_class
            
            	L2Tp class data
            	**type**\:  :py:class:`L2tpClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.TunnelConfigurations.TunnelConfiguration.L2tpClass>`
            
            .. attribute:: remote_tunnel_id
            
            	Remote tunnel ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'tunnel-l2tun-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(L2tpv2.TunnelConfigurations.TunnelConfiguration, self).__init__()

                self.yang_name = "tunnel-configuration"
                self.yang_parent_name = "tunnel-configurations"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['local_tunnel_id']
                self._child_classes = OrderedDict([("l2tp-class", ("l2tp_class", L2tpv2.TunnelConfigurations.TunnelConfiguration.L2tpClass))])
                self._leafs = OrderedDict([
                    ('local_tunnel_id', (YLeaf(YType.uint32, 'local-tunnel-id'), ['int'])),
                    ('remote_tunnel_id', (YLeaf(YType.uint32, 'remote-tunnel-id'), ['int'])),
                ])
                self.local_tunnel_id = None
                self.remote_tunnel_id = None

                self.l2tp_class = L2tpv2.TunnelConfigurations.TunnelConfiguration.L2tpClass()
                self.l2tp_class.parent = self
                self._children_name_map["l2tp_class"] = "l2tp-class"
                self._segment_path = lambda: "tunnel-configuration" + "[local-tunnel-id='" + str(self.local_tunnel_id) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/tunnel-configurations/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(L2tpv2.TunnelConfigurations.TunnelConfiguration, ['local_tunnel_id', u'remote_tunnel_id'], name, value)


            class L2tpClass(Entity):
                """
                L2Tp class data
                
                .. attribute:: ip_tos
                
                	IP TOS
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: vrf_name
                
                	VRF name
                	**type**\: str
                
                	**length:** 0..256
                
                .. attribute:: receive_window_size
                
                	Receive window size
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: class_name_xr
                
                	Class name
                	**type**\: str
                
                	**length:** 0..256
                
                .. attribute:: digest_hash
                
                	Hash configured as MD5 or SHA1
                	**type**\:  :py:class:`DigestHash <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.DigestHash>`
                
                .. attribute:: password
                
                	Password
                	**type**\: str
                
                	**length:** 0..25
                
                .. attribute:: encoded_password
                
                	Encoded password
                	**type**\: str
                
                	**length:** 0..256
                
                .. attribute:: host_name
                
                	Host name
                	**type**\: str
                
                	**length:** 0..256
                
                .. attribute:: accounting_method_list
                
                	Accounting List
                	**type**\: str
                
                	**length:** 0..256
                
                .. attribute:: hello_timeout
                
                	Hello timeout value in seconds
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: setup_timeout
                
                	Timeout setup value in seconds
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: retransmit_minimum_timeout
                
                	Retransmit minimum timeout in seconds
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: retransmit_maximum_timeout
                
                	Retransmit maximum timeout in seconds
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: initial_retransmit_minimum_timeout
                
                	Initial timeout minimum in seconds
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: initial_retransmit_maximum_timeout
                
                	Initial timeout maximum in seconds
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: timeout_no_user
                
                	Timeout no user
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: retransmit_retries
                
                	Retransmit retries
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: initial_retransmit_retries
                
                	Initial retransmit retries
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: is_authentication_enabled
                
                	True if authentication is enabled
                	**type**\: bool
                
                .. attribute:: is_hidden
                
                	True if class is hidden
                	**type**\: bool
                
                .. attribute:: is_digest_enabled
                
                	True if digest authentication is enabled
                	**type**\: bool
                
                .. attribute:: is_digest_check_enabled
                
                	True if digest check is enabled
                	**type**\: bool
                
                .. attribute:: is_congestion_control_enabled
                
                	True if congestion control is enabled
                	**type**\: bool
                
                .. attribute:: is_peer_address_checked
                
                	True if peer address is checked
                	**type**\: bool
                
                

                """

                _prefix = 'tunnel-l2tun-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(L2tpv2.TunnelConfigurations.TunnelConfiguration.L2tpClass, self).__init__()

                    self.yang_name = "l2tp-class"
                    self.yang_parent_name = "tunnel-configuration"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('ip_tos', (YLeaf(YType.uint8, 'ip-tos'), ['int'])),
                        ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                        ('receive_window_size', (YLeaf(YType.uint16, 'receive-window-size'), ['int'])),
                        ('class_name_xr', (YLeaf(YType.str, 'class-name-xr'), ['str'])),
                        ('digest_hash', (YLeaf(YType.enumeration, 'digest-hash'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper', 'DigestHash', '')])),
                        ('password', (YLeaf(YType.str, 'password'), ['str'])),
                        ('encoded_password', (YLeaf(YType.str, 'encoded-password'), ['str'])),
                        ('host_name', (YLeaf(YType.str, 'host-name'), ['str'])),
                        ('accounting_method_list', (YLeaf(YType.str, 'accounting-method-list'), ['str'])),
                        ('hello_timeout', (YLeaf(YType.uint32, 'hello-timeout'), ['int'])),
                        ('setup_timeout', (YLeaf(YType.uint32, 'setup-timeout'), ['int'])),
                        ('retransmit_minimum_timeout', (YLeaf(YType.uint32, 'retransmit-minimum-timeout'), ['int'])),
                        ('retransmit_maximum_timeout', (YLeaf(YType.uint32, 'retransmit-maximum-timeout'), ['int'])),
                        ('initial_retransmit_minimum_timeout', (YLeaf(YType.uint32, 'initial-retransmit-minimum-timeout'), ['int'])),
                        ('initial_retransmit_maximum_timeout', (YLeaf(YType.uint32, 'initial-retransmit-maximum-timeout'), ['int'])),
                        ('timeout_no_user', (YLeaf(YType.uint32, 'timeout-no-user'), ['int'])),
                        ('retransmit_retries', (YLeaf(YType.uint32, 'retransmit-retries'), ['int'])),
                        ('initial_retransmit_retries', (YLeaf(YType.uint32, 'initial-retransmit-retries'), ['int'])),
                        ('is_authentication_enabled', (YLeaf(YType.boolean, 'is-authentication-enabled'), ['bool'])),
                        ('is_hidden', (YLeaf(YType.boolean, 'is-hidden'), ['bool'])),
                        ('is_digest_enabled', (YLeaf(YType.boolean, 'is-digest-enabled'), ['bool'])),
                        ('is_digest_check_enabled', (YLeaf(YType.boolean, 'is-digest-check-enabled'), ['bool'])),
                        ('is_congestion_control_enabled', (YLeaf(YType.boolean, 'is-congestion-control-enabled'), ['bool'])),
                        ('is_peer_address_checked', (YLeaf(YType.boolean, 'is-peer-address-checked'), ['bool'])),
                    ])
                    self.ip_tos = None
                    self.vrf_name = None
                    self.receive_window_size = None
                    self.class_name_xr = None
                    self.digest_hash = None
                    self.password = None
                    self.encoded_password = None
                    self.host_name = None
                    self.accounting_method_list = None
                    self.hello_timeout = None
                    self.setup_timeout = None
                    self.retransmit_minimum_timeout = None
                    self.retransmit_maximum_timeout = None
                    self.initial_retransmit_minimum_timeout = None
                    self.initial_retransmit_maximum_timeout = None
                    self.timeout_no_user = None
                    self.retransmit_retries = None
                    self.initial_retransmit_retries = None
                    self.is_authentication_enabled = None
                    self.is_hidden = None
                    self.is_digest_enabled = None
                    self.is_digest_check_enabled = None
                    self.is_congestion_control_enabled = None
                    self.is_peer_address_checked = None
                    self._segment_path = lambda: "l2tp-class"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(L2tpv2.TunnelConfigurations.TunnelConfiguration.L2tpClass, [u'ip_tos', u'vrf_name', u'receive_window_size', u'class_name_xr', u'digest_hash', u'password', u'encoded_password', u'host_name', u'accounting_method_list', u'hello_timeout', u'setup_timeout', u'retransmit_minimum_timeout', u'retransmit_maximum_timeout', u'initial_retransmit_minimum_timeout', u'initial_retransmit_maximum_timeout', u'timeout_no_user', u'retransmit_retries', u'initial_retransmit_retries', u'is_authentication_enabled', u'is_hidden', u'is_digest_enabled', u'is_digest_check_enabled', u'is_congestion_control_enabled', u'is_peer_address_checked'], name, value)


    class CounterHistFail(Entity):
        """
        Failure events leading to disconnection
        
        .. attribute:: sess_down_tmout
        
        	sesions affected due to timeout
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: tx_counters
        
        	Send side counters
        	**type**\: str
        
        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
        
        .. attribute:: rx_counters
        
        	Receive side counters
        	**type**\: str
        
        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
        
        .. attribute:: pkt_timeout
        
        	timeout events by packet
        	**type**\: list of  		 :py:class:`PktTimeout <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.CounterHistFail.PktTimeout>`
        
        

        """

        _prefix = 'tunnel-l2tun-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(L2tpv2.CounterHistFail, self).__init__()

            self.yang_name = "counter-hist-fail"
            self.yang_parent_name = "l2tpv2"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("pkt-timeout", ("pkt_timeout", L2tpv2.CounterHistFail.PktTimeout))])
            self._leafs = OrderedDict([
                ('sess_down_tmout', (YLeaf(YType.uint32, 'sess-down-tmout'), ['int'])),
                ('tx_counters', (YLeaf(YType.str, 'tx-counters'), ['str'])),
                ('rx_counters', (YLeaf(YType.str, 'rx-counters'), ['str'])),
            ])
            self.sess_down_tmout = None
            self.tx_counters = None
            self.rx_counters = None

            self.pkt_timeout = YList(self)
            self._segment_path = lambda: "counter-hist-fail"
            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(L2tpv2.CounterHistFail, [u'sess_down_tmout', u'tx_counters', u'rx_counters'], name, value)


        class PktTimeout(Entity):
            """
            timeout events by packet
            
            .. attribute:: entry
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'tunnel-l2tun-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(L2tpv2.CounterHistFail.PktTimeout, self).__init__()

                self.yang_name = "pkt-timeout"
                self.yang_parent_name = "counter-hist-fail"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entry', (YLeaf(YType.uint32, 'entry'), ['int'])),
                ])
                self.entry = None
                self._segment_path = lambda: "pkt-timeout"
                self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/counter-hist-fail/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(L2tpv2.CounterHistFail.PktTimeout, [u'entry'], name, value)


    class Classes(Entity):
        """
        List of L2TP class names
        
        .. attribute:: class_
        
        	L2TP class name
        	**type**\: list of  		 :py:class:`Class <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Classes.Class>`
        
        

        """

        _prefix = 'tunnel-l2tun-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(L2tpv2.Classes, self).__init__()

            self.yang_name = "classes"
            self.yang_parent_name = "l2tpv2"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("class", ("class_", L2tpv2.Classes.Class))])
            self._leafs = OrderedDict()

            self.class_ = YList(self)
            self._segment_path = lambda: "classes"
            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(L2tpv2.Classes, [], name, value)


        class Class(Entity):
            """
            L2TP class name
            
            .. attribute:: class_name  (key)
            
            	L2TP class name
            	**type**\: str
            
            	**length:** 1..31
            
            .. attribute:: ip_tos
            
            	IP TOS
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: vrf_name
            
            	VRF name
            	**type**\: str
            
            	**length:** 0..256
            
            .. attribute:: receive_window_size
            
            	Receive window size
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: class_name_xr
            
            	Class name
            	**type**\: str
            
            	**length:** 0..256
            
            .. attribute:: digest_hash
            
            	Hash configured as MD5 or SHA1
            	**type**\:  :py:class:`DigestHash <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.DigestHash>`
            
            .. attribute:: password
            
            	Password
            	**type**\: str
            
            	**length:** 0..25
            
            .. attribute:: encoded_password
            
            	Encoded password
            	**type**\: str
            
            	**length:** 0..256
            
            .. attribute:: host_name
            
            	Host name
            	**type**\: str
            
            	**length:** 0..256
            
            .. attribute:: accounting_method_list
            
            	Accounting List
            	**type**\: str
            
            	**length:** 0..256
            
            .. attribute:: hello_timeout
            
            	Hello timeout value in seconds
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: second
            
            .. attribute:: setup_timeout
            
            	Timeout setup value in seconds
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: second
            
            .. attribute:: retransmit_minimum_timeout
            
            	Retransmit minimum timeout in seconds
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: second
            
            .. attribute:: retransmit_maximum_timeout
            
            	Retransmit maximum timeout in seconds
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: second
            
            .. attribute:: initial_retransmit_minimum_timeout
            
            	Initial timeout minimum in seconds
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: second
            
            .. attribute:: initial_retransmit_maximum_timeout
            
            	Initial timeout maximum in seconds
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: second
            
            .. attribute:: timeout_no_user
            
            	Timeout no user
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: retransmit_retries
            
            	Retransmit retries
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: initial_retransmit_retries
            
            	Initial retransmit retries
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: is_authentication_enabled
            
            	True if authentication is enabled
            	**type**\: bool
            
            .. attribute:: is_hidden
            
            	True if class is hidden
            	**type**\: bool
            
            .. attribute:: is_digest_enabled
            
            	True if digest authentication is enabled
            	**type**\: bool
            
            .. attribute:: is_digest_check_enabled
            
            	True if digest check is enabled
            	**type**\: bool
            
            .. attribute:: is_congestion_control_enabled
            
            	True if congestion control is enabled
            	**type**\: bool
            
            .. attribute:: is_peer_address_checked
            
            	True if peer address is checked
            	**type**\: bool
            
            

            """

            _prefix = 'tunnel-l2tun-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(L2tpv2.Classes.Class, self).__init__()

                self.yang_name = "class"
                self.yang_parent_name = "classes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['class_name']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('class_name', (YLeaf(YType.str, 'class-name'), ['str'])),
                    ('ip_tos', (YLeaf(YType.uint8, 'ip-tos'), ['int'])),
                    ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                    ('receive_window_size', (YLeaf(YType.uint16, 'receive-window-size'), ['int'])),
                    ('class_name_xr', (YLeaf(YType.str, 'class-name-xr'), ['str'])),
                    ('digest_hash', (YLeaf(YType.enumeration, 'digest-hash'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper', 'DigestHash', '')])),
                    ('password', (YLeaf(YType.str, 'password'), ['str'])),
                    ('encoded_password', (YLeaf(YType.str, 'encoded-password'), ['str'])),
                    ('host_name', (YLeaf(YType.str, 'host-name'), ['str'])),
                    ('accounting_method_list', (YLeaf(YType.str, 'accounting-method-list'), ['str'])),
                    ('hello_timeout', (YLeaf(YType.uint32, 'hello-timeout'), ['int'])),
                    ('setup_timeout', (YLeaf(YType.uint32, 'setup-timeout'), ['int'])),
                    ('retransmit_minimum_timeout', (YLeaf(YType.uint32, 'retransmit-minimum-timeout'), ['int'])),
                    ('retransmit_maximum_timeout', (YLeaf(YType.uint32, 'retransmit-maximum-timeout'), ['int'])),
                    ('initial_retransmit_minimum_timeout', (YLeaf(YType.uint32, 'initial-retransmit-minimum-timeout'), ['int'])),
                    ('initial_retransmit_maximum_timeout', (YLeaf(YType.uint32, 'initial-retransmit-maximum-timeout'), ['int'])),
                    ('timeout_no_user', (YLeaf(YType.uint32, 'timeout-no-user'), ['int'])),
                    ('retransmit_retries', (YLeaf(YType.uint32, 'retransmit-retries'), ['int'])),
                    ('initial_retransmit_retries', (YLeaf(YType.uint32, 'initial-retransmit-retries'), ['int'])),
                    ('is_authentication_enabled', (YLeaf(YType.boolean, 'is-authentication-enabled'), ['bool'])),
                    ('is_hidden', (YLeaf(YType.boolean, 'is-hidden'), ['bool'])),
                    ('is_digest_enabled', (YLeaf(YType.boolean, 'is-digest-enabled'), ['bool'])),
                    ('is_digest_check_enabled', (YLeaf(YType.boolean, 'is-digest-check-enabled'), ['bool'])),
                    ('is_congestion_control_enabled', (YLeaf(YType.boolean, 'is-congestion-control-enabled'), ['bool'])),
                    ('is_peer_address_checked', (YLeaf(YType.boolean, 'is-peer-address-checked'), ['bool'])),
                ])
                self.class_name = None
                self.ip_tos = None
                self.vrf_name = None
                self.receive_window_size = None
                self.class_name_xr = None
                self.digest_hash = None
                self.password = None
                self.encoded_password = None
                self.host_name = None
                self.accounting_method_list = None
                self.hello_timeout = None
                self.setup_timeout = None
                self.retransmit_minimum_timeout = None
                self.retransmit_maximum_timeout = None
                self.initial_retransmit_minimum_timeout = None
                self.initial_retransmit_maximum_timeout = None
                self.timeout_no_user = None
                self.retransmit_retries = None
                self.initial_retransmit_retries = None
                self.is_authentication_enabled = None
                self.is_hidden = None
                self.is_digest_enabled = None
                self.is_digest_check_enabled = None
                self.is_congestion_control_enabled = None
                self.is_peer_address_checked = None
                self._segment_path = lambda: "class" + "[class-name='" + str(self.class_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/classes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(L2tpv2.Classes.Class, ['class_name', u'ip_tos', u'vrf_name', u'receive_window_size', u'class_name_xr', u'digest_hash', u'password', u'encoded_password', u'host_name', u'accounting_method_list', u'hello_timeout', u'setup_timeout', u'retransmit_minimum_timeout', u'retransmit_maximum_timeout', u'initial_retransmit_minimum_timeout', u'initial_retransmit_maximum_timeout', u'timeout_no_user', u'retransmit_retries', u'initial_retransmit_retries', u'is_authentication_enabled', u'is_hidden', u'is_digest_enabled', u'is_digest_check_enabled', u'is_congestion_control_enabled', u'is_peer_address_checked'], name, value)


    class Tunnels(Entity):
        """
        List of tunnel IDs
        
        .. attribute:: tunnel
        
        	L2TP tunnel  information
        	**type**\: list of  		 :py:class:`Tunnel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Tunnels.Tunnel>`
        
        

        """

        _prefix = 'tunnel-l2tun-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(L2tpv2.Tunnels, self).__init__()

            self.yang_name = "tunnels"
            self.yang_parent_name = "l2tpv2"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("tunnel", ("tunnel", L2tpv2.Tunnels.Tunnel))])
            self._leafs = OrderedDict()

            self.tunnel = YList(self)
            self._segment_path = lambda: "tunnels"
            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(L2tpv2.Tunnels, [], name, value)


        class Tunnel(Entity):
            """
            L2TP tunnel  information
            
            .. attribute:: local_tunnel_id  (key)
            
            	Local tunnel ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: local_address
            
            	Local tunnel address
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: remote_address
            
            	Remote tunnel address
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: local_port
            
            	Local port
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: remote_port
            
            	Remote port
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: protocol
            
            	Protocol
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: is_pmtu_enabled
            
            	True if tunnel PMTU checking is enabled
            	**type**\: bool
            
            .. attribute:: remote_tunnel_id
            
            	Remote tunnel ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: local_tunnel_name
            
            	Local tunnel name
            	**type**\: str
            
            	**length:** 0..256
            
            .. attribute:: remote_tunnel_name
            
            	Remote tunnel name
            	**type**\: str
            
            	**length:** 0..256
            
            .. attribute:: class_name
            
            	L2TP class name
            	**type**\: str
            
            	**length:** 0..256
            
            .. attribute:: active_sessions
            
            	Number of active sessions
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sequence_ns
            
            	Sequence NS
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: sequence_nr
            
            	Sequence NR
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: local_window_size
            
            	Local window size
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: remote_window_size
            
            	Remote window size
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: retransmission_time
            
            	Retransmission time in seconds
            	**type**\: int
            
            	**range:** 0..65535
            
            	**units**\: second
            
            .. attribute:: maximum_retransmission_time
            
            	Maximum retransmission time in seconds
            	**type**\: int
            
            	**range:** 0..65535
            
            	**units**\: second
            
            .. attribute:: unsent_queue_size
            
            	Unsent queue size
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: unsent_maximum_queue_size
            
            	Unsent maximum queue size
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: resend_queue_size
            
            	Resend queue size
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: resend_maximum_queue_size
            
            	Resend maximum queue size
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: order_queue_size
            
            	Order queue size
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: packet_queue_check
            
            	Current number session packet queue check
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: digest_secrets
            
            	Control message authentication with digest secrets
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: resends
            
            	Total resends
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: zero_length_body_acknowledgement_sent
            
            	Total zero length body acknowledgement
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: total_out_of_order_drop_packets
            
            	Total out of order dropped packets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: total_out_of_order_reorder_packets
            
            	Total out of order reorder packets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: total_peer_authentication_failures
            
            	Number of peer authentication failures
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: is_tunnel_up
            
            	True if tunnel is up
            	**type**\: bool
            
            .. attribute:: is_congestion_control_enabled
            
            	True if congestion control is enabled else false
            	**type**\: bool
            
            .. attribute:: retransmit_time
            
            	Retransmit time distribution in seconds
            	**type**\: list of  		 :py:class:`RetransmitTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Tunnels.Tunnel.RetransmitTime>`
            
            

            """

            _prefix = 'tunnel-l2tun-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(L2tpv2.Tunnels.Tunnel, self).__init__()

                self.yang_name = "tunnel"
                self.yang_parent_name = "tunnels"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['local_tunnel_id']
                self._child_classes = OrderedDict([("retransmit-time", ("retransmit_time", L2tpv2.Tunnels.Tunnel.RetransmitTime))])
                self._leafs = OrderedDict([
                    ('local_tunnel_id', (YLeaf(YType.uint32, 'local-tunnel-id'), ['int'])),
                    ('local_address', (YLeaf(YType.str, 'local-address'), ['str'])),
                    ('remote_address', (YLeaf(YType.str, 'remote-address'), ['str'])),
                    ('local_port', (YLeaf(YType.uint16, 'local-port'), ['int'])),
                    ('remote_port', (YLeaf(YType.uint16, 'remote-port'), ['int'])),
                    ('protocol', (YLeaf(YType.uint8, 'protocol'), ['int'])),
                    ('is_pmtu_enabled', (YLeaf(YType.boolean, 'is-pmtu-enabled'), ['bool'])),
                    ('remote_tunnel_id', (YLeaf(YType.uint32, 'remote-tunnel-id'), ['int'])),
                    ('local_tunnel_name', (YLeaf(YType.str, 'local-tunnel-name'), ['str'])),
                    ('remote_tunnel_name', (YLeaf(YType.str, 'remote-tunnel-name'), ['str'])),
                    ('class_name', (YLeaf(YType.str, 'class-name'), ['str'])),
                    ('active_sessions', (YLeaf(YType.uint32, 'active-sessions'), ['int'])),
                    ('sequence_ns', (YLeaf(YType.uint16, 'sequence-ns'), ['int'])),
                    ('sequence_nr', (YLeaf(YType.uint16, 'sequence-nr'), ['int'])),
                    ('local_window_size', (YLeaf(YType.uint16, 'local-window-size'), ['int'])),
                    ('remote_window_size', (YLeaf(YType.uint16, 'remote-window-size'), ['int'])),
                    ('retransmission_time', (YLeaf(YType.uint16, 'retransmission-time'), ['int'])),
                    ('maximum_retransmission_time', (YLeaf(YType.uint16, 'maximum-retransmission-time'), ['int'])),
                    ('unsent_queue_size', (YLeaf(YType.uint16, 'unsent-queue-size'), ['int'])),
                    ('unsent_maximum_queue_size', (YLeaf(YType.uint16, 'unsent-maximum-queue-size'), ['int'])),
                    ('resend_queue_size', (YLeaf(YType.uint16, 'resend-queue-size'), ['int'])),
                    ('resend_maximum_queue_size', (YLeaf(YType.uint16, 'resend-maximum-queue-size'), ['int'])),
                    ('order_queue_size', (YLeaf(YType.uint16, 'order-queue-size'), ['int'])),
                    ('packet_queue_check', (YLeaf(YType.uint16, 'packet-queue-check'), ['int'])),
                    ('digest_secrets', (YLeaf(YType.uint16, 'digest-secrets'), ['int'])),
                    ('resends', (YLeaf(YType.uint32, 'resends'), ['int'])),
                    ('zero_length_body_acknowledgement_sent', (YLeaf(YType.uint32, 'zero-length-body-acknowledgement-sent'), ['int'])),
                    ('total_out_of_order_drop_packets', (YLeaf(YType.uint32, 'total-out-of-order-drop-packets'), ['int'])),
                    ('total_out_of_order_reorder_packets', (YLeaf(YType.uint32, 'total-out-of-order-reorder-packets'), ['int'])),
                    ('total_peer_authentication_failures', (YLeaf(YType.uint32, 'total-peer-authentication-failures'), ['int'])),
                    ('is_tunnel_up', (YLeaf(YType.boolean, 'is-tunnel-up'), ['bool'])),
                    ('is_congestion_control_enabled', (YLeaf(YType.boolean, 'is-congestion-control-enabled'), ['bool'])),
                ])
                self.local_tunnel_id = None
                self.local_address = None
                self.remote_address = None
                self.local_port = None
                self.remote_port = None
                self.protocol = None
                self.is_pmtu_enabled = None
                self.remote_tunnel_id = None
                self.local_tunnel_name = None
                self.remote_tunnel_name = None
                self.class_name = None
                self.active_sessions = None
                self.sequence_ns = None
                self.sequence_nr = None
                self.local_window_size = None
                self.remote_window_size = None
                self.retransmission_time = None
                self.maximum_retransmission_time = None
                self.unsent_queue_size = None
                self.unsent_maximum_queue_size = None
                self.resend_queue_size = None
                self.resend_maximum_queue_size = None
                self.order_queue_size = None
                self.packet_queue_check = None
                self.digest_secrets = None
                self.resends = None
                self.zero_length_body_acknowledgement_sent = None
                self.total_out_of_order_drop_packets = None
                self.total_out_of_order_reorder_packets = None
                self.total_peer_authentication_failures = None
                self.is_tunnel_up = None
                self.is_congestion_control_enabled = None

                self.retransmit_time = YList(self)
                self._segment_path = lambda: "tunnel" + "[local-tunnel-id='" + str(self.local_tunnel_id) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/tunnels/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(L2tpv2.Tunnels.Tunnel, ['local_tunnel_id', u'local_address', u'remote_address', u'local_port', u'remote_port', u'protocol', u'is_pmtu_enabled', u'remote_tunnel_id', u'local_tunnel_name', u'remote_tunnel_name', u'class_name', u'active_sessions', u'sequence_ns', u'sequence_nr', u'local_window_size', u'remote_window_size', u'retransmission_time', u'maximum_retransmission_time', u'unsent_queue_size', u'unsent_maximum_queue_size', u'resend_queue_size', u'resend_maximum_queue_size', u'order_queue_size', u'packet_queue_check', u'digest_secrets', u'resends', u'zero_length_body_acknowledgement_sent', u'total_out_of_order_drop_packets', u'total_out_of_order_reorder_packets', u'total_peer_authentication_failures', u'is_tunnel_up', u'is_congestion_control_enabled'], name, value)


            class RetransmitTime(Entity):
                """
                Retransmit time distribution in seconds
                
                .. attribute:: entry
                
                	
                	**type**\: int
                
                	**range:** 0..65535
                
                	**units**\: second
                
                

                """

                _prefix = 'tunnel-l2tun-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(L2tpv2.Tunnels.Tunnel.RetransmitTime, self).__init__()

                    self.yang_name = "retransmit-time"
                    self.yang_parent_name = "tunnel"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('entry', (YLeaf(YType.uint16, 'entry'), ['int'])),
                    ])
                    self.entry = None
                    self._segment_path = lambda: "retransmit-time"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(L2tpv2.Tunnels.Tunnel.RetransmitTime, [u'entry'], name, value)


    class Sessions(Entity):
        """
        List of session IDs
        
        .. attribute:: session
        
        	L2TP information for a particular session
        	**type**\: list of  		 :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Sessions.Session>`
        
        

        """

        _prefix = 'tunnel-l2tun-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(L2tpv2.Sessions, self).__init__()

            self.yang_name = "sessions"
            self.yang_parent_name = "l2tpv2"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("session", ("session", L2tpv2.Sessions.Session))])
            self._leafs = OrderedDict()

            self.session = YList(self)
            self._segment_path = lambda: "sessions"
            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(L2tpv2.Sessions, [], name, value)


        class Session(Entity):
            """
            L2TP information for a particular session
            
            .. attribute:: local_tunnel_id  (key)
            
            	Local tunnel ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: local_session_id  (key)
            
            	Local session ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: session_application_data
            
            	Session application data
            	**type**\:  :py:class:`SessionApplicationData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Sessions.Session.SessionApplicationData>`
            
            .. attribute:: local_ip_address
            
            	Local session IP address
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: remote_ip_address
            
            	Remote session IP address
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: l2tp_sh_sess_udp_lport
            
            	l2tp sh sess udp lport
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: l2tp_sh_sess_udp_rport
            
            	l2tp sh sess udp rport
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: protocol
            
            	Protocol
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: remote_tunnel_id
            
            	Remote tunnel ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: call_serial_number
            
            	Call serial number
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: local_tunnel_name
            
            	Local tunnel name
            	**type**\: str
            
            	**length:** 0..256
            
            .. attribute:: remote_tunnel_name
            
            	Remote tunnel name
            	**type**\: str
            
            	**length:** 0..256
            
            .. attribute:: remote_session_id
            
            	Remote session ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: l2tp_sh_sess_tie_breaker_enabled
            
            	l2tp sh sess tie breaker enabled
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: l2tp_sh_sess_tie_breaker
            
            	l2tp sh sess tie breaker
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: is_session_manual
            
            	True if session is manual
            	**type**\: bool
            
            .. attribute:: is_session_up
            
            	True if session is up
            	**type**\: bool
            
            .. attribute:: is_udp_checksum_enabled
            
            	True if UDP checksum enabled
            	**type**\: bool
            
            .. attribute:: is_sequencing_on
            
            	True if session sequence is on
            	**type**\: bool
            
            .. attribute:: is_session_state_established
            
            	True if session state is established
            	**type**\: bool
            
            .. attribute:: is_session_locally_initiated
            
            	True if session initiated locally
            	**type**\: bool
            
            .. attribute:: is_conditional_debug_enabled
            
            	True if conditional debugging is enabled
            	**type**\: bool
            
            .. attribute:: unique_id
            
            	Unique ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: interface_name
            
            	Interface name
            	**type**\: str
            
            	**length:** 0..256
            
            

            """

            _prefix = 'tunnel-l2tun-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(L2tpv2.Sessions.Session, self).__init__()

                self.yang_name = "session"
                self.yang_parent_name = "sessions"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['local_tunnel_id','local_session_id']
                self._child_classes = OrderedDict([("session-application-data", ("session_application_data", L2tpv2.Sessions.Session.SessionApplicationData))])
                self._leafs = OrderedDict([
                    ('local_tunnel_id', (YLeaf(YType.uint32, 'local-tunnel-id'), ['int'])),
                    ('local_session_id', (YLeaf(YType.uint32, 'local-session-id'), ['int'])),
                    ('local_ip_address', (YLeaf(YType.str, 'local-ip-address'), ['str'])),
                    ('remote_ip_address', (YLeaf(YType.str, 'remote-ip-address'), ['str'])),
                    ('l2tp_sh_sess_udp_lport', (YLeaf(YType.uint16, 'l2tp-sh-sess-udp-lport'), ['int'])),
                    ('l2tp_sh_sess_udp_rport', (YLeaf(YType.uint16, 'l2tp-sh-sess-udp-rport'), ['int'])),
                    ('protocol', (YLeaf(YType.uint8, 'protocol'), ['int'])),
                    ('remote_tunnel_id', (YLeaf(YType.uint32, 'remote-tunnel-id'), ['int'])),
                    ('call_serial_number', (YLeaf(YType.uint32, 'call-serial-number'), ['int'])),
                    ('local_tunnel_name', (YLeaf(YType.str, 'local-tunnel-name'), ['str'])),
                    ('remote_tunnel_name', (YLeaf(YType.str, 'remote-tunnel-name'), ['str'])),
                    ('remote_session_id', (YLeaf(YType.uint32, 'remote-session-id'), ['int'])),
                    ('l2tp_sh_sess_tie_breaker_enabled', (YLeaf(YType.uint8, 'l2tp-sh-sess-tie-breaker-enabled'), ['int'])),
                    ('l2tp_sh_sess_tie_breaker', (YLeaf(YType.uint64, 'l2tp-sh-sess-tie-breaker'), ['int'])),
                    ('is_session_manual', (YLeaf(YType.boolean, 'is-session-manual'), ['bool'])),
                    ('is_session_up', (YLeaf(YType.boolean, 'is-session-up'), ['bool'])),
                    ('is_udp_checksum_enabled', (YLeaf(YType.boolean, 'is-udp-checksum-enabled'), ['bool'])),
                    ('is_sequencing_on', (YLeaf(YType.boolean, 'is-sequencing-on'), ['bool'])),
                    ('is_session_state_established', (YLeaf(YType.boolean, 'is-session-state-established'), ['bool'])),
                    ('is_session_locally_initiated', (YLeaf(YType.boolean, 'is-session-locally-initiated'), ['bool'])),
                    ('is_conditional_debug_enabled', (YLeaf(YType.boolean, 'is-conditional-debug-enabled'), ['bool'])),
                    ('unique_id', (YLeaf(YType.uint32, 'unique-id'), ['int'])),
                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                ])
                self.local_tunnel_id = None
                self.local_session_id = None
                self.local_ip_address = None
                self.remote_ip_address = None
                self.l2tp_sh_sess_udp_lport = None
                self.l2tp_sh_sess_udp_rport = None
                self.protocol = None
                self.remote_tunnel_id = None
                self.call_serial_number = None
                self.local_tunnel_name = None
                self.remote_tunnel_name = None
                self.remote_session_id = None
                self.l2tp_sh_sess_tie_breaker_enabled = None
                self.l2tp_sh_sess_tie_breaker = None
                self.is_session_manual = None
                self.is_session_up = None
                self.is_udp_checksum_enabled = None
                self.is_sequencing_on = None
                self.is_session_state_established = None
                self.is_session_locally_initiated = None
                self.is_conditional_debug_enabled = None
                self.unique_id = None
                self.interface_name = None

                self.session_application_data = L2tpv2.Sessions.Session.SessionApplicationData()
                self.session_application_data.parent = self
                self._children_name_map["session_application_data"] = "session-application-data"
                self._segment_path = lambda: "session" + "[local-tunnel-id='" + str(self.local_tunnel_id) + "']" + "[local-session-id='" + str(self.local_session_id) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/sessions/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(L2tpv2.Sessions.Session, ['local_tunnel_id', 'local_session_id', u'local_ip_address', u'remote_ip_address', u'l2tp_sh_sess_udp_lport', u'l2tp_sh_sess_udp_rport', u'protocol', u'remote_tunnel_id', u'call_serial_number', u'local_tunnel_name', u'remote_tunnel_name', u'remote_session_id', u'l2tp_sh_sess_tie_breaker_enabled', u'l2tp_sh_sess_tie_breaker', u'is_session_manual', u'is_session_up', u'is_udp_checksum_enabled', u'is_sequencing_on', u'is_session_state_established', u'is_session_locally_initiated', u'is_conditional_debug_enabled', u'unique_id', u'interface_name'], name, value)


            class SessionApplicationData(Entity):
                """
                Session application data
                
                .. attribute:: xconnect
                
                	Xconnect data
                	**type**\:  :py:class:`Xconnect <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Sessions.Session.SessionApplicationData.Xconnect>`
                
                .. attribute:: vpdn
                
                	VPDN data
                	**type**\:  :py:class:`Vpdn <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Sessions.Session.SessionApplicationData.Vpdn>`
                
                .. attribute:: l2tp_sh_sess_app_type
                
                	l2tp sh sess app type
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'tunnel-l2tun-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(L2tpv2.Sessions.Session.SessionApplicationData, self).__init__()

                    self.yang_name = "session-application-data"
                    self.yang_parent_name = "session"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("xconnect", ("xconnect", L2tpv2.Sessions.Session.SessionApplicationData.Xconnect)), ("vpdn", ("vpdn", L2tpv2.Sessions.Session.SessionApplicationData.Vpdn))])
                    self._leafs = OrderedDict([
                        ('l2tp_sh_sess_app_type', (YLeaf(YType.uint32, 'l2tp-sh-sess-app-type'), ['int'])),
                    ])
                    self.l2tp_sh_sess_app_type = None

                    self.xconnect = L2tpv2.Sessions.Session.SessionApplicationData.Xconnect()
                    self.xconnect.parent = self
                    self._children_name_map["xconnect"] = "xconnect"

                    self.vpdn = L2tpv2.Sessions.Session.SessionApplicationData.Vpdn()
                    self.vpdn.parent = self
                    self._children_name_map["vpdn"] = "vpdn"
                    self._segment_path = lambda: "session-application-data"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(L2tpv2.Sessions.Session.SessionApplicationData, [u'l2tp_sh_sess_app_type'], name, value)


                class Xconnect(Entity):
                    """
                    Xconnect data
                    
                    .. attribute:: circuit_name
                    
                    	Circuit name
                    	**type**\: str
                    
                    .. attribute:: sessionvc_id
                    
                    	Session VC ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: is_circuit_state_up
                    
                    	True if circuit state is up
                    	**type**\: bool
                    
                    .. attribute:: is_local_circuit_state_up
                    
                    	True if local circuit state is up
                    	**type**\: bool
                    
                    .. attribute:: is_remote_circuit_state_up
                    
                    	True if remote circuit state is up
                    	**type**\: bool
                    
                    .. attribute:: ipv6_protocol_tunneling
                    
                    	IPv6ProtocolTunneling
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'tunnel-l2tun-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(L2tpv2.Sessions.Session.SessionApplicationData.Xconnect, self).__init__()

                        self.yang_name = "xconnect"
                        self.yang_parent_name = "session-application-data"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('circuit_name', (YLeaf(YType.str, 'circuit-name'), ['str'])),
                            ('sessionvc_id', (YLeaf(YType.uint32, 'sessionvc-id'), ['int'])),
                            ('is_circuit_state_up', (YLeaf(YType.boolean, 'is-circuit-state-up'), ['bool'])),
                            ('is_local_circuit_state_up', (YLeaf(YType.boolean, 'is-local-circuit-state-up'), ['bool'])),
                            ('is_remote_circuit_state_up', (YLeaf(YType.boolean, 'is-remote-circuit-state-up'), ['bool'])),
                            ('ipv6_protocol_tunneling', (YLeaf(YType.boolean, 'ipv6-protocol-tunneling'), ['bool'])),
                        ])
                        self.circuit_name = None
                        self.sessionvc_id = None
                        self.is_circuit_state_up = None
                        self.is_local_circuit_state_up = None
                        self.is_remote_circuit_state_up = None
                        self.ipv6_protocol_tunneling = None
                        self._segment_path = lambda: "xconnect"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2tpv2.Sessions.Session.SessionApplicationData.Xconnect, [u'circuit_name', u'sessionvc_id', u'is_circuit_state_up', u'is_local_circuit_state_up', u'is_remote_circuit_state_up', u'ipv6_protocol_tunneling'], name, value)


                class Vpdn(Entity):
                    """
                    VPDN data
                    
                    .. attribute:: username
                    
                    	Session username
                    	**type**\: str
                    
                    .. attribute:: interface_name
                    
                    	Interface name
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    

                    """

                    _prefix = 'tunnel-l2tun-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(L2tpv2.Sessions.Session.SessionApplicationData.Vpdn, self).__init__()

                        self.yang_name = "vpdn"
                        self.yang_parent_name = "session-application-data"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('username', (YLeaf(YType.str, 'username'), ['str'])),
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                        ])
                        self.username = None
                        self.interface_name = None
                        self._segment_path = lambda: "vpdn"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2tpv2.Sessions.Session.SessionApplicationData.Vpdn, [u'username', u'interface_name'], name, value)


    class Session(Entity):
        """
        L2TP control messages counters
        
        .. attribute:: unavailable
        
        	L2TP session unavailable  information
        	**type**\:  :py:class:`Unavailable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Session.Unavailable>`
        
        

        """

        _prefix = 'tunnel-l2tun-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(L2tpv2.Session, self).__init__()

            self.yang_name = "session"
            self.yang_parent_name = "l2tpv2"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("unavailable", ("unavailable", L2tpv2.Session.Unavailable))])
            self._leafs = OrderedDict()

            self.unavailable = L2tpv2.Session.Unavailable()
            self.unavailable.parent = self
            self._children_name_map["unavailable"] = "unavailable"
            self._segment_path = lambda: "session"
            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(L2tpv2.Session, [], name, value)


        class Unavailable(Entity):
            """
            L2TP session unavailable  information
            
            .. attribute:: sessions_on_hold
            
            	Number of session ID in hold database
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'tunnel-l2tun-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(L2tpv2.Session.Unavailable, self).__init__()

                self.yang_name = "unavailable"
                self.yang_parent_name = "session"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('sessions_on_hold', (YLeaf(YType.uint32, 'sessions-on-hold'), ['int'])),
                ])
                self.sessions_on_hold = None
                self._segment_path = lambda: "unavailable"
                self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/session/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(L2tpv2.Session.Unavailable, [u'sessions_on_hold'], name, value)

    def clone_ptr(self):
        self._top_entity = L2tpv2()
        return self._top_entity

