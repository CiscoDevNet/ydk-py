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
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
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


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
        return meta._meta_table['DigestHash']



class L2tp(_Entity_):
    """
    L2TP operational data
    
    .. attribute:: nodes
    
    	List of nodes for which subscriber data is collected
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Nodes>`
    
    	**config**\: False
    
    

    """

    _prefix = 'tunnel-l2tun-oper'
    _revision = '2018-11-01'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(L2tp, self).__init__()
        self._top_entity = None

        self.yang_name = "l2tp"
        self.yang_parent_name = "Cisco-IOS-XR-tunnel-l2tun-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("nodes", ("nodes", L2tp.Nodes))])
        self._leafs = OrderedDict()

        self.nodes = L2tp.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._segment_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tp"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(L2tp, [], name, value)


    class Nodes(_Entity_):
        """
        List of nodes for which subscriber data is
        collected
        
        .. attribute:: node
        
        	Subscriber data for a particular node
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Nodes.Node>`
        
        	**config**\: False
        
        

        """

        _prefix = 'tunnel-l2tun-oper'
        _revision = '2018-11-01'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(L2tp.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "l2tp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("node", ("node", L2tp.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(L2tp.Nodes, [], name, value)


        class Node(_Entity_):
            """
            Subscriber data for a particular node
            
            .. attribute:: node_name  (key)
            
            	Node name
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            	**config**\: False
            
            .. attribute:: counters
            
            	L2TP control messages counters
            	**type**\:  :py:class:`Counters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Nodes.Node.Counters>`
            
            	**config**\: False
            
            .. attribute:: tunnel_configurations
            
            	List of tunnel IDs
            	**type**\:  :py:class:`TunnelConfigurations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Nodes.Node.TunnelConfigurations>`
            
            	**config**\: False
            
            .. attribute:: counter_hist_fail
            
            	Failure events leading to disconnection
            	**type**\:  :py:class:`CounterHistFail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Nodes.Node.CounterHistFail>`
            
            	**config**\: False
            
            .. attribute:: classes
            
            	List of L2TP class names
            	**type**\:  :py:class:`Classes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Nodes.Node.Classes>`
            
            	**config**\: False
            
            .. attribute:: tunnels
            
            	List of tunnel IDs
            	**type**\:  :py:class:`Tunnels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Nodes.Node.Tunnels>`
            
            	**config**\: False
            
            .. attribute:: sessions
            
            	List of session IDs
            	**type**\:  :py:class:`Sessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Nodes.Node.Sessions>`
            
            	**config**\: False
            
            .. attribute:: session
            
            	L2TP control messages counters
            	**type**\:  :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Nodes.Node.Session>`
            
            	**config**\: False
            
            .. attribute:: internal
            
            	L2TP v2/v3 internal information
            	**type**\:  :py:class:`Internal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Nodes.Node.Internal>`
            
            	**config**\: False
            
            

            """

            _prefix = 'tunnel-l2tun-oper'
            _revision = '2018-11-01'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(L2tp.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_classes = OrderedDict([("counters", ("counters", L2tp.Nodes.Node.Counters)), ("tunnel-configurations", ("tunnel_configurations", L2tp.Nodes.Node.TunnelConfigurations)), ("counter-hist-fail", ("counter_hist_fail", L2tp.Nodes.Node.CounterHistFail)), ("classes", ("classes", L2tp.Nodes.Node.Classes)), ("tunnels", ("tunnels", L2tp.Nodes.Node.Tunnels)), ("sessions", ("sessions", L2tp.Nodes.Node.Sessions)), ("session", ("session", L2tp.Nodes.Node.Session)), ("internal", ("internal", L2tp.Nodes.Node.Internal))])
                self._leafs = OrderedDict([
                    ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                ])
                self.node_name = None

                self.counters = L2tp.Nodes.Node.Counters()
                self.counters.parent = self
                self._children_name_map["counters"] = "counters"

                self.tunnel_configurations = L2tp.Nodes.Node.TunnelConfigurations()
                self.tunnel_configurations.parent = self
                self._children_name_map["tunnel_configurations"] = "tunnel-configurations"

                self.counter_hist_fail = L2tp.Nodes.Node.CounterHistFail()
                self.counter_hist_fail.parent = self
                self._children_name_map["counter_hist_fail"] = "counter-hist-fail"

                self.classes = L2tp.Nodes.Node.Classes()
                self.classes.parent = self
                self._children_name_map["classes"] = "classes"

                self.tunnels = L2tp.Nodes.Node.Tunnels()
                self.tunnels.parent = self
                self._children_name_map["tunnels"] = "tunnels"

                self.sessions = L2tp.Nodes.Node.Sessions()
                self.sessions.parent = self
                self._children_name_map["sessions"] = "sessions"

                self.session = L2tp.Nodes.Node.Session()
                self.session.parent = self
                self._children_name_map["session"] = "session"

                self.internal = L2tp.Nodes.Node.Internal()
                self.internal.parent = self
                self._children_name_map["internal"] = "internal"
                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/nodes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(L2tp.Nodes.Node, ['node_name'], name, value)


            class Counters(_Entity_):
                """
                L2TP control messages counters
                
                .. attribute:: control
                
                	L2TP control messages counters
                	**type**\:  :py:class:`Control <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Nodes.Node.Counters.Control>`
                
                	**config**\: False
                
                

                """

                _prefix = 'tunnel-l2tun-oper'
                _revision = '2018-11-01'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(L2tp.Nodes.Node.Counters, self).__init__()

                    self.yang_name = "counters"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("control", ("control", L2tp.Nodes.Node.Counters.Control))])
                    self._leafs = OrderedDict()

                    self.control = L2tp.Nodes.Node.Counters.Control()
                    self.control.parent = self
                    self._children_name_map["control"] = "control"
                    self._segment_path = lambda: "counters"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(L2tp.Nodes.Node.Counters, [], name, value)


                class Control(_Entity_):
                    """
                    L2TP control messages counters
                    
                    .. attribute:: tunnel_xr
                    
                    	L2TP control tunnel messages counters
                    	**type**\:  :py:class:`TunnelXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Nodes.Node.Counters.Control.TunnelXr>`
                    
                    	**config**\: False
                    
                    .. attribute:: tunnels
                    
                    	Table of tunnel IDs of control message counters
                    	**type**\:  :py:class:`Tunnels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Nodes.Node.Counters.Control.Tunnels>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'tunnel-l2tun-oper'
                    _revision = '2018-11-01'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(L2tp.Nodes.Node.Counters.Control, self).__init__()

                        self.yang_name = "control"
                        self.yang_parent_name = "counters"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("tunnel-xr", ("tunnel_xr", L2tp.Nodes.Node.Counters.Control.TunnelXr)), ("tunnels", ("tunnels", L2tp.Nodes.Node.Counters.Control.Tunnels))])
                        self._leafs = OrderedDict()

                        self.tunnel_xr = L2tp.Nodes.Node.Counters.Control.TunnelXr()
                        self.tunnel_xr.parent = self
                        self._children_name_map["tunnel_xr"] = "tunnel-xr"

                        self.tunnels = L2tp.Nodes.Node.Counters.Control.Tunnels()
                        self.tunnels.parent = self
                        self._children_name_map["tunnels"] = "tunnels"
                        self._segment_path = lambda: "control"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2tp.Nodes.Node.Counters.Control, [], name, value)


                    class TunnelXr(_Entity_):
                        """
                        L2TP control tunnel messages counters
                        
                        .. attribute:: authentication
                        
                        	Tunnel authentication counters
                        	**type**\:  :py:class:`Authentication <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Nodes.Node.Counters.Control.TunnelXr.Authentication>`
                        
                        	**config**\: False
                        
                        .. attribute:: global_
                        
                        	Tunnel counters
                        	**type**\:  :py:class:`Global <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Nodes.Node.Counters.Control.TunnelXr.Global>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'tunnel-l2tun-oper'
                        _revision = '2018-11-01'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(L2tp.Nodes.Node.Counters.Control.TunnelXr, self).__init__()

                            self.yang_name = "tunnel-xr"
                            self.yang_parent_name = "control"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("authentication", ("authentication", L2tp.Nodes.Node.Counters.Control.TunnelXr.Authentication)), ("global", ("global_", L2tp.Nodes.Node.Counters.Control.TunnelXr.Global))])
                            self._leafs = OrderedDict()

                            self.authentication = L2tp.Nodes.Node.Counters.Control.TunnelXr.Authentication()
                            self.authentication.parent = self
                            self._children_name_map["authentication"] = "authentication"

                            self.global_ = L2tp.Nodes.Node.Counters.Control.TunnelXr.Global()
                            self.global_.parent = self
                            self._children_name_map["global_"] = "global"
                            self._segment_path = lambda: "tunnel-xr"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2tp.Nodes.Node.Counters.Control.TunnelXr, [], name, value)


                        class Authentication(_Entity_):
                            """
                            Tunnel authentication counters
                            
                            .. attribute:: nonce_avp
                            
                            	Nonce AVP statistics
                            	**type**\:  :py:class:`NonceAvp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Nodes.Node.Counters.Control.TunnelXr.Authentication.NonceAvp>`
                            
                            	**config**\: False
                            
                            .. attribute:: common_digest
                            
                            	Common digest statistics
                            	**type**\:  :py:class:`CommonDigest <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Nodes.Node.Counters.Control.TunnelXr.Authentication.CommonDigest>`
                            
                            	**config**\: False
                            
                            .. attribute:: primary_digest
                            
                            	Primary digest statistics
                            	**type**\:  :py:class:`PrimaryDigest <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Nodes.Node.Counters.Control.TunnelXr.Authentication.PrimaryDigest>`
                            
                            	**config**\: False
                            
                            .. attribute:: secondary_digest
                            
                            	Secondary digest statistics
                            	**type**\:  :py:class:`SecondaryDigest <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Nodes.Node.Counters.Control.TunnelXr.Authentication.SecondaryDigest>`
                            
                            	**config**\: False
                            
                            .. attribute:: integrity_check
                            
                            	Integrity check statistics
                            	**type**\:  :py:class:`IntegrityCheck <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Nodes.Node.Counters.Control.TunnelXr.Authentication.IntegrityCheck>`
                            
                            	**config**\: False
                            
                            .. attribute:: local_secret
                            
                            	Local secret statistics
                            	**type**\:  :py:class:`LocalSecret <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Nodes.Node.Counters.Control.TunnelXr.Authentication.LocalSecret>`
                            
                            	**config**\: False
                            
                            .. attribute:: challenge_avp
                            
                            	Challenge AVP statistics
                            	**type**\:  :py:class:`ChallengeAvp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Nodes.Node.Counters.Control.TunnelXr.Authentication.ChallengeAvp>`
                            
                            	**config**\: False
                            
                            .. attribute:: challenge_reponse
                            
                            	Challenge response statistics
                            	**type**\:  :py:class:`ChallengeReponse <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Nodes.Node.Counters.Control.TunnelXr.Authentication.ChallengeReponse>`
                            
                            	**config**\: False
                            
                            .. attribute:: overall_statistics
                            
                            	Overall statistics
                            	**type**\:  :py:class:`OverallStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Nodes.Node.Counters.Control.TunnelXr.Authentication.OverallStatistics>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'tunnel-l2tun-oper'
                            _revision = '2018-11-01'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(L2tp.Nodes.Node.Counters.Control.TunnelXr.Authentication, self).__init__()

                                self.yang_name = "authentication"
                                self.yang_parent_name = "tunnel-xr"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("nonce-avp", ("nonce_avp", L2tp.Nodes.Node.Counters.Control.TunnelXr.Authentication.NonceAvp)), ("common-digest", ("common_digest", L2tp.Nodes.Node.Counters.Control.TunnelXr.Authentication.CommonDigest)), ("primary-digest", ("primary_digest", L2tp.Nodes.Node.Counters.Control.TunnelXr.Authentication.PrimaryDigest)), ("secondary-digest", ("secondary_digest", L2tp.Nodes.Node.Counters.Control.TunnelXr.Authentication.SecondaryDigest)), ("integrity-check", ("integrity_check", L2tp.Nodes.Node.Counters.Control.TunnelXr.Authentication.IntegrityCheck)), ("local-secret", ("local_secret", L2tp.Nodes.Node.Counters.Control.TunnelXr.Authentication.LocalSecret)), ("challenge-avp", ("challenge_avp", L2tp.Nodes.Node.Counters.Control.TunnelXr.Authentication.ChallengeAvp)), ("challenge-reponse", ("challenge_reponse", L2tp.Nodes.Node.Counters.Control.TunnelXr.Authentication.ChallengeReponse)), ("overall-statistics", ("overall_statistics", L2tp.Nodes.Node.Counters.Control.TunnelXr.Authentication.OverallStatistics))])
                                self._leafs = OrderedDict()

                                self.nonce_avp = L2tp.Nodes.Node.Counters.Control.TunnelXr.Authentication.NonceAvp()
                                self.nonce_avp.parent = self
                                self._children_name_map["nonce_avp"] = "nonce-avp"

                                self.common_digest = L2tp.Nodes.Node.Counters.Control.TunnelXr.Authentication.CommonDigest()
                                self.common_digest.parent = self
                                self._children_name_map["common_digest"] = "common-digest"

                                self.primary_digest = L2tp.Nodes.Node.Counters.Control.TunnelXr.Authentication.PrimaryDigest()
                                self.primary_digest.parent = self
                                self._children_name_map["primary_digest"] = "primary-digest"

                                self.secondary_digest = L2tp.Nodes.Node.Counters.Control.TunnelXr.Authentication.SecondaryDigest()
                                self.secondary_digest.parent = self
                                self._children_name_map["secondary_digest"] = "secondary-digest"

                                self.integrity_check = L2tp.Nodes.Node.Counters.Control.TunnelXr.Authentication.IntegrityCheck()
                                self.integrity_check.parent = self
                                self._children_name_map["integrity_check"] = "integrity-check"

                                self.local_secret = L2tp.Nodes.Node.Counters.Control.TunnelXr.Authentication.LocalSecret()
                                self.local_secret.parent = self
                                self._children_name_map["local_secret"] = "local-secret"

                                self.challenge_avp = L2tp.Nodes.Node.Counters.Control.TunnelXr.Authentication.ChallengeAvp()
                                self.challenge_avp.parent = self
                                self._children_name_map["challenge_avp"] = "challenge-avp"

                                self.challenge_reponse = L2tp.Nodes.Node.Counters.Control.TunnelXr.Authentication.ChallengeReponse()
                                self.challenge_reponse.parent = self
                                self._children_name_map["challenge_reponse"] = "challenge-reponse"

                                self.overall_statistics = L2tp.Nodes.Node.Counters.Control.TunnelXr.Authentication.OverallStatistics()
                                self.overall_statistics.parent = self
                                self._children_name_map["overall_statistics"] = "overall-statistics"
                                self._segment_path = lambda: "authentication"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2tp.Nodes.Node.Counters.Control.TunnelXr.Authentication, [], name, value)


                            class NonceAvp(_Entity_):
                                """
                                Nonce AVP statistics
                                
                                .. attribute:: validate
                                
                                	Validate
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: bad_hash
                                
                                	Bad hash
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: bad_length
                                
                                	Bad length
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: ignored
                                
                                	Ignored
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: missing
                                
                                	Missing
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: passed
                                
                                	Passed
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: failed
                                
                                	Failed
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: skipped
                                
                                	Skipped
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: generate_response_failures
                                
                                	Generate response fail
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: unexpected
                                
                                	Unexpected
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: unexpected_zlb
                                
                                	Unexpected ZLB
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'tunnel-l2tun-oper'
                                _revision = '2018-11-01'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(L2tp.Nodes.Node.Counters.Control.TunnelXr.Authentication.NonceAvp, self).__init__()

                                    self.yang_name = "nonce-avp"
                                    self.yang_parent_name = "authentication"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
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
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2tp.Nodes.Node.Counters.Control.TunnelXr.Authentication.NonceAvp, ['validate', 'bad_hash', 'bad_length', 'ignored', 'missing', 'passed', 'failed', 'skipped', 'generate_response_failures', 'unexpected', 'unexpected_zlb'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                                    return meta._meta_table['L2tp.Nodes.Node.Counters.Control.TunnelXr.Authentication.NonceAvp']['meta_info']


                            class CommonDigest(_Entity_):
                                """
                                Common digest statistics
                                
                                .. attribute:: validate
                                
                                	Validate
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: bad_hash
                                
                                	Bad hash
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: bad_length
                                
                                	Bad length
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: ignored
                                
                                	Ignored
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: missing
                                
                                	Missing
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: passed
                                
                                	Passed
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: failed
                                
                                	Failed
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: skipped
                                
                                	Skipped
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: generate_response_failures
                                
                                	Generate response fail
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: unexpected
                                
                                	Unexpected
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: unexpected_zlb
                                
                                	Unexpected ZLB
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'tunnel-l2tun-oper'
                                _revision = '2018-11-01'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(L2tp.Nodes.Node.Counters.Control.TunnelXr.Authentication.CommonDigest, self).__init__()

                                    self.yang_name = "common-digest"
                                    self.yang_parent_name = "authentication"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
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
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2tp.Nodes.Node.Counters.Control.TunnelXr.Authentication.CommonDigest, ['validate', 'bad_hash', 'bad_length', 'ignored', 'missing', 'passed', 'failed', 'skipped', 'generate_response_failures', 'unexpected', 'unexpected_zlb'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                                    return meta._meta_table['L2tp.Nodes.Node.Counters.Control.TunnelXr.Authentication.CommonDigest']['meta_info']


                            class PrimaryDigest(_Entity_):
                                """
                                Primary digest statistics
                                
                                .. attribute:: validate
                                
                                	Validate
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: bad_hash
                                
                                	Bad hash
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: bad_length
                                
                                	Bad length
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: ignored
                                
                                	Ignored
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: missing
                                
                                	Missing
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: passed
                                
                                	Passed
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: failed
                                
                                	Failed
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: skipped
                                
                                	Skipped
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: generate_response_failures
                                
                                	Generate response fail
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: unexpected
                                
                                	Unexpected
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: unexpected_zlb
                                
                                	Unexpected ZLB
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'tunnel-l2tun-oper'
                                _revision = '2018-11-01'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(L2tp.Nodes.Node.Counters.Control.TunnelXr.Authentication.PrimaryDigest, self).__init__()

                                    self.yang_name = "primary-digest"
                                    self.yang_parent_name = "authentication"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
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
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2tp.Nodes.Node.Counters.Control.TunnelXr.Authentication.PrimaryDigest, ['validate', 'bad_hash', 'bad_length', 'ignored', 'missing', 'passed', 'failed', 'skipped', 'generate_response_failures', 'unexpected', 'unexpected_zlb'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                                    return meta._meta_table['L2tp.Nodes.Node.Counters.Control.TunnelXr.Authentication.PrimaryDigest']['meta_info']


                            class SecondaryDigest(_Entity_):
                                """
                                Secondary digest statistics
                                
                                .. attribute:: validate
                                
                                	Validate
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: bad_hash
                                
                                	Bad hash
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: bad_length
                                
                                	Bad length
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: ignored
                                
                                	Ignored
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: missing
                                
                                	Missing
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: passed
                                
                                	Passed
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: failed
                                
                                	Failed
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: skipped
                                
                                	Skipped
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: generate_response_failures
                                
                                	Generate response fail
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: unexpected
                                
                                	Unexpected
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: unexpected_zlb
                                
                                	Unexpected ZLB
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'tunnel-l2tun-oper'
                                _revision = '2018-11-01'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(L2tp.Nodes.Node.Counters.Control.TunnelXr.Authentication.SecondaryDigest, self).__init__()

                                    self.yang_name = "secondary-digest"
                                    self.yang_parent_name = "authentication"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
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
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2tp.Nodes.Node.Counters.Control.TunnelXr.Authentication.SecondaryDigest, ['validate', 'bad_hash', 'bad_length', 'ignored', 'missing', 'passed', 'failed', 'skipped', 'generate_response_failures', 'unexpected', 'unexpected_zlb'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                                    return meta._meta_table['L2tp.Nodes.Node.Counters.Control.TunnelXr.Authentication.SecondaryDigest']['meta_info']


                            class IntegrityCheck(_Entity_):
                                """
                                Integrity check statistics
                                
                                .. attribute:: validate
                                
                                	Validate
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: bad_hash
                                
                                	Bad hash
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: bad_length
                                
                                	Bad length
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: ignored
                                
                                	Ignored
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: missing
                                
                                	Missing
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: passed
                                
                                	Passed
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: failed
                                
                                	Failed
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: skipped
                                
                                	Skipped
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: generate_response_failures
                                
                                	Generate response fail
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: unexpected
                                
                                	Unexpected
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: unexpected_zlb
                                
                                	Unexpected ZLB
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'tunnel-l2tun-oper'
                                _revision = '2018-11-01'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(L2tp.Nodes.Node.Counters.Control.TunnelXr.Authentication.IntegrityCheck, self).__init__()

                                    self.yang_name = "integrity-check"
                                    self.yang_parent_name = "authentication"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
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
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2tp.Nodes.Node.Counters.Control.TunnelXr.Authentication.IntegrityCheck, ['validate', 'bad_hash', 'bad_length', 'ignored', 'missing', 'passed', 'failed', 'skipped', 'generate_response_failures', 'unexpected', 'unexpected_zlb'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                                    return meta._meta_table['L2tp.Nodes.Node.Counters.Control.TunnelXr.Authentication.IntegrityCheck']['meta_info']


                            class LocalSecret(_Entity_):
                                """
                                Local secret statistics
                                
                                .. attribute:: validate
                                
                                	Validate
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: bad_hash
                                
                                	Bad hash
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: bad_length
                                
                                	Bad length
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: ignored
                                
                                	Ignored
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: missing
                                
                                	Missing
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: passed
                                
                                	Passed
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: failed
                                
                                	Failed
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: skipped
                                
                                	Skipped
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: generate_response_failures
                                
                                	Generate response fail
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: unexpected
                                
                                	Unexpected
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: unexpected_zlb
                                
                                	Unexpected ZLB
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'tunnel-l2tun-oper'
                                _revision = '2018-11-01'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(L2tp.Nodes.Node.Counters.Control.TunnelXr.Authentication.LocalSecret, self).__init__()

                                    self.yang_name = "local-secret"
                                    self.yang_parent_name = "authentication"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
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
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2tp.Nodes.Node.Counters.Control.TunnelXr.Authentication.LocalSecret, ['validate', 'bad_hash', 'bad_length', 'ignored', 'missing', 'passed', 'failed', 'skipped', 'generate_response_failures', 'unexpected', 'unexpected_zlb'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                                    return meta._meta_table['L2tp.Nodes.Node.Counters.Control.TunnelXr.Authentication.LocalSecret']['meta_info']


                            class ChallengeAvp(_Entity_):
                                """
                                Challenge AVP statistics
                                
                                .. attribute:: validate
                                
                                	Validate
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: bad_hash
                                
                                	Bad hash
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: bad_length
                                
                                	Bad length
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: ignored
                                
                                	Ignored
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: missing
                                
                                	Missing
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: passed
                                
                                	Passed
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: failed
                                
                                	Failed
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: skipped
                                
                                	Skipped
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: generate_response_failures
                                
                                	Generate response fail
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: unexpected
                                
                                	Unexpected
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: unexpected_zlb
                                
                                	Unexpected ZLB
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'tunnel-l2tun-oper'
                                _revision = '2018-11-01'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(L2tp.Nodes.Node.Counters.Control.TunnelXr.Authentication.ChallengeAvp, self).__init__()

                                    self.yang_name = "challenge-avp"
                                    self.yang_parent_name = "authentication"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
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
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2tp.Nodes.Node.Counters.Control.TunnelXr.Authentication.ChallengeAvp, ['validate', 'bad_hash', 'bad_length', 'ignored', 'missing', 'passed', 'failed', 'skipped', 'generate_response_failures', 'unexpected', 'unexpected_zlb'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                                    return meta._meta_table['L2tp.Nodes.Node.Counters.Control.TunnelXr.Authentication.ChallengeAvp']['meta_info']


                            class ChallengeReponse(_Entity_):
                                """
                                Challenge response statistics
                                
                                .. attribute:: validate
                                
                                	Validate
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: bad_hash
                                
                                	Bad hash
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: bad_length
                                
                                	Bad length
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: ignored
                                
                                	Ignored
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: missing
                                
                                	Missing
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: passed
                                
                                	Passed
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: failed
                                
                                	Failed
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: skipped
                                
                                	Skipped
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: generate_response_failures
                                
                                	Generate response fail
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: unexpected
                                
                                	Unexpected
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: unexpected_zlb
                                
                                	Unexpected ZLB
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'tunnel-l2tun-oper'
                                _revision = '2018-11-01'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(L2tp.Nodes.Node.Counters.Control.TunnelXr.Authentication.ChallengeReponse, self).__init__()

                                    self.yang_name = "challenge-reponse"
                                    self.yang_parent_name = "authentication"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
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
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2tp.Nodes.Node.Counters.Control.TunnelXr.Authentication.ChallengeReponse, ['validate', 'bad_hash', 'bad_length', 'ignored', 'missing', 'passed', 'failed', 'skipped', 'generate_response_failures', 'unexpected', 'unexpected_zlb'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                                    return meta._meta_table['L2tp.Nodes.Node.Counters.Control.TunnelXr.Authentication.ChallengeReponse']['meta_info']


                            class OverallStatistics(_Entity_):
                                """
                                Overall statistics
                                
                                .. attribute:: validate
                                
                                	Validate
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: bad_hash
                                
                                	Bad hash
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: bad_length
                                
                                	Bad length
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: ignored
                                
                                	Ignored
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: missing
                                
                                	Missing
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: passed
                                
                                	Passed
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: failed
                                
                                	Failed
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: skipped
                                
                                	Skipped
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: generate_response_failures
                                
                                	Generate response fail
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: unexpected
                                
                                	Unexpected
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: unexpected_zlb
                                
                                	Unexpected ZLB
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'tunnel-l2tun-oper'
                                _revision = '2018-11-01'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(L2tp.Nodes.Node.Counters.Control.TunnelXr.Authentication.OverallStatistics, self).__init__()

                                    self.yang_name = "overall-statistics"
                                    self.yang_parent_name = "authentication"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
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
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2tp.Nodes.Node.Counters.Control.TunnelXr.Authentication.OverallStatistics, ['validate', 'bad_hash', 'bad_length', 'ignored', 'missing', 'passed', 'failed', 'skipped', 'generate_response_failures', 'unexpected', 'unexpected_zlb'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                                    return meta._meta_table['L2tp.Nodes.Node.Counters.Control.TunnelXr.Authentication.OverallStatistics']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                                return meta._meta_table['L2tp.Nodes.Node.Counters.Control.TunnelXr.Authentication']['meta_info']


                        class Global(_Entity_):
                            """
                            Tunnel counters
                            
                            .. attribute:: transmit
                            
                            	Transmit data
                            	**type**\:  :py:class:`Transmit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Nodes.Node.Counters.Control.TunnelXr.Global.Transmit>`
                            
                            	**config**\: False
                            
                            .. attribute:: retransmit
                            
                            	Re transmit data
                            	**type**\:  :py:class:`Retransmit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Nodes.Node.Counters.Control.TunnelXr.Global.Retransmit>`
                            
                            	**config**\: False
                            
                            .. attribute:: received
                            
                            	Received data
                            	**type**\:  :py:class:`Received <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Nodes.Node.Counters.Control.TunnelXr.Global.Received>`
                            
                            	**config**\: False
                            
                            .. attribute:: drop
                            
                            	Drop data
                            	**type**\:  :py:class:`Drop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Nodes.Node.Counters.Control.TunnelXr.Global.Drop>`
                            
                            	**config**\: False
                            
                            .. attribute:: total_transmit
                            
                            	Total transmit
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: total_retransmit
                            
                            	Total retransmit
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: total_received
                            
                            	Total received
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: total_drop
                            
                            	Total drop
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'tunnel-l2tun-oper'
                            _revision = '2018-11-01'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(L2tp.Nodes.Node.Counters.Control.TunnelXr.Global, self).__init__()

                                self.yang_name = "global"
                                self.yang_parent_name = "tunnel-xr"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("transmit", ("transmit", L2tp.Nodes.Node.Counters.Control.TunnelXr.Global.Transmit)), ("retransmit", ("retransmit", L2tp.Nodes.Node.Counters.Control.TunnelXr.Global.Retransmit)), ("received", ("received", L2tp.Nodes.Node.Counters.Control.TunnelXr.Global.Received)), ("drop", ("drop", L2tp.Nodes.Node.Counters.Control.TunnelXr.Global.Drop))])
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

                                self.transmit = L2tp.Nodes.Node.Counters.Control.TunnelXr.Global.Transmit()
                                self.transmit.parent = self
                                self._children_name_map["transmit"] = "transmit"

                                self.retransmit = L2tp.Nodes.Node.Counters.Control.TunnelXr.Global.Retransmit()
                                self.retransmit.parent = self
                                self._children_name_map["retransmit"] = "retransmit"

                                self.received = L2tp.Nodes.Node.Counters.Control.TunnelXr.Global.Received()
                                self.received.parent = self
                                self._children_name_map["received"] = "received"

                                self.drop = L2tp.Nodes.Node.Counters.Control.TunnelXr.Global.Drop()
                                self.drop.parent = self
                                self._children_name_map["drop"] = "drop"
                                self._segment_path = lambda: "global"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2tp.Nodes.Node.Counters.Control.TunnelXr.Global, ['total_transmit', 'total_retransmit', 'total_received', 'total_drop'], name, value)


                            class Transmit(_Entity_):
                                """
                                Transmit data
                                
                                .. attribute:: unknown_packets
                                
                                	Unknown packets
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: zero_length_body_packets
                                
                                	Zero length body packets
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: start_control_connection_requests
                                
                                	Start control connection requests
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: start_control_connection_replies
                                
                                	Start control connection replies
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: start_control_connection_notifications
                                
                                	Start control connection notifications
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: stop_control_connection_notifications
                                
                                	Stop control connection notifications
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: hello_packets
                                
                                	Keep alive messages
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: outgoing_call_requests
                                
                                	Outgoing call requests
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: outgoing_call_replies
                                
                                	Outgoing call replies
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: outgoing_call_connected_packets
                                
                                	Outgoing call connected packets
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: incoming_call_requests
                                
                                	Incoming call requests
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: incoming_call_replies
                                
                                	Incoming call replies
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: incoming_call_connected_packets
                                
                                	Incoming call connected packets
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: call_disconnect_notify_packets
                                
                                	Call disconnect notify packets
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: wan_error_notify_packets
                                
                                	WAN error notify packets
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: set_link_info_packets
                                
                                	Set link info packets
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: service_relay_requests
                                
                                	Service relay request counts
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: service_relay_replies
                                
                                	Service relay reply counts
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: acknowledgement_packets
                                
                                	Packets acknowledgement
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'tunnel-l2tun-oper'
                                _revision = '2018-11-01'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(L2tp.Nodes.Node.Counters.Control.TunnelXr.Global.Transmit, self).__init__()

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
                                    self._perform_setattr(L2tp.Nodes.Node.Counters.Control.TunnelXr.Global.Transmit, ['unknown_packets', 'zero_length_body_packets', 'start_control_connection_requests', 'start_control_connection_replies', 'start_control_connection_notifications', 'stop_control_connection_notifications', 'hello_packets', 'outgoing_call_requests', 'outgoing_call_replies', 'outgoing_call_connected_packets', 'incoming_call_requests', 'incoming_call_replies', 'incoming_call_connected_packets', 'call_disconnect_notify_packets', 'wan_error_notify_packets', 'set_link_info_packets', 'service_relay_requests', 'service_relay_replies', 'acknowledgement_packets'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                                    return meta._meta_table['L2tp.Nodes.Node.Counters.Control.TunnelXr.Global.Transmit']['meta_info']


                            class Retransmit(_Entity_):
                                """
                                Re transmit data
                                
                                .. attribute:: unknown_packets
                                
                                	Unknown packets
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: zero_length_body_packets
                                
                                	Zero length body packets
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: start_control_connection_requests
                                
                                	Start control connection requests
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: start_control_connection_replies
                                
                                	Start control connection replies
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: start_control_connection_notifications
                                
                                	Start control connection notifications
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: stop_control_connection_notifications
                                
                                	Stop control connection notifications
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: hello_packets
                                
                                	Keep alive messages
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: outgoing_call_requests
                                
                                	Outgoing call requests
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: outgoing_call_replies
                                
                                	Outgoing call replies
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: outgoing_call_connected_packets
                                
                                	Outgoing call connected packets
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: incoming_call_requests
                                
                                	Incoming call requests
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: incoming_call_replies
                                
                                	Incoming call replies
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: incoming_call_connected_packets
                                
                                	Incoming call connected packets
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: call_disconnect_notify_packets
                                
                                	Call disconnect notify packets
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: wan_error_notify_packets
                                
                                	WAN error notify packets
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: set_link_info_packets
                                
                                	Set link info packets
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: service_relay_requests
                                
                                	Service relay request counts
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: service_relay_replies
                                
                                	Service relay reply counts
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: acknowledgement_packets
                                
                                	Packets acknowledgement
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'tunnel-l2tun-oper'
                                _revision = '2018-11-01'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(L2tp.Nodes.Node.Counters.Control.TunnelXr.Global.Retransmit, self).__init__()

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
                                    self._perform_setattr(L2tp.Nodes.Node.Counters.Control.TunnelXr.Global.Retransmit, ['unknown_packets', 'zero_length_body_packets', 'start_control_connection_requests', 'start_control_connection_replies', 'start_control_connection_notifications', 'stop_control_connection_notifications', 'hello_packets', 'outgoing_call_requests', 'outgoing_call_replies', 'outgoing_call_connected_packets', 'incoming_call_requests', 'incoming_call_replies', 'incoming_call_connected_packets', 'call_disconnect_notify_packets', 'wan_error_notify_packets', 'set_link_info_packets', 'service_relay_requests', 'service_relay_replies', 'acknowledgement_packets'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                                    return meta._meta_table['L2tp.Nodes.Node.Counters.Control.TunnelXr.Global.Retransmit']['meta_info']


                            class Received(_Entity_):
                                """
                                Received data
                                
                                .. attribute:: unknown_packets
                                
                                	Unknown packets
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: zero_length_body_packets
                                
                                	Zero length body packets
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: start_control_connection_requests
                                
                                	Start control connection requests
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: start_control_connection_replies
                                
                                	Start control connection replies
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: start_control_connection_notifications
                                
                                	Start control connection notifications
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: stop_control_connection_notifications
                                
                                	Stop control connection notifications
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: hello_packets
                                
                                	Keep alive messages
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: outgoing_call_requests
                                
                                	Outgoing call requests
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: outgoing_call_replies
                                
                                	Outgoing call replies
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: outgoing_call_connected_packets
                                
                                	Outgoing call connected packets
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: incoming_call_requests
                                
                                	Incoming call requests
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: incoming_call_replies
                                
                                	Incoming call replies
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: incoming_call_connected_packets
                                
                                	Incoming call connected packets
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: call_disconnect_notify_packets
                                
                                	Call disconnect notify packets
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: wan_error_notify_packets
                                
                                	WAN error notify packets
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: set_link_info_packets
                                
                                	Set link info packets
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: service_relay_requests
                                
                                	Service relay request counts
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: service_relay_replies
                                
                                	Service relay reply counts
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: acknowledgement_packets
                                
                                	Packets acknowledgement
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'tunnel-l2tun-oper'
                                _revision = '2018-11-01'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(L2tp.Nodes.Node.Counters.Control.TunnelXr.Global.Received, self).__init__()

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
                                    self._perform_setattr(L2tp.Nodes.Node.Counters.Control.TunnelXr.Global.Received, ['unknown_packets', 'zero_length_body_packets', 'start_control_connection_requests', 'start_control_connection_replies', 'start_control_connection_notifications', 'stop_control_connection_notifications', 'hello_packets', 'outgoing_call_requests', 'outgoing_call_replies', 'outgoing_call_connected_packets', 'incoming_call_requests', 'incoming_call_replies', 'incoming_call_connected_packets', 'call_disconnect_notify_packets', 'wan_error_notify_packets', 'set_link_info_packets', 'service_relay_requests', 'service_relay_replies', 'acknowledgement_packets'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                                    return meta._meta_table['L2tp.Nodes.Node.Counters.Control.TunnelXr.Global.Received']['meta_info']


                            class Drop(_Entity_):
                                """
                                Drop data
                                
                                .. attribute:: unknown_packets
                                
                                	Unknown packets
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: zero_length_body_packets
                                
                                	Zero length body packets
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: start_control_connection_requests
                                
                                	Start control connection requests
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: start_control_connection_replies
                                
                                	Start control connection replies
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: start_control_connection_notifications
                                
                                	Start control connection notifications
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: stop_control_connection_notifications
                                
                                	Stop control connection notifications
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: hello_packets
                                
                                	Keep alive messages
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: outgoing_call_requests
                                
                                	Outgoing call requests
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: outgoing_call_replies
                                
                                	Outgoing call replies
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: outgoing_call_connected_packets
                                
                                	Outgoing call connected packets
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: incoming_call_requests
                                
                                	Incoming call requests
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: incoming_call_replies
                                
                                	Incoming call replies
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: incoming_call_connected_packets
                                
                                	Incoming call connected packets
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: call_disconnect_notify_packets
                                
                                	Call disconnect notify packets
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: wan_error_notify_packets
                                
                                	WAN error notify packets
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: set_link_info_packets
                                
                                	Set link info packets
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: service_relay_requests
                                
                                	Service relay request counts
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: service_relay_replies
                                
                                	Service relay reply counts
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: acknowledgement_packets
                                
                                	Packets acknowledgement
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'tunnel-l2tun-oper'
                                _revision = '2018-11-01'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(L2tp.Nodes.Node.Counters.Control.TunnelXr.Global.Drop, self).__init__()

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
                                    self._perform_setattr(L2tp.Nodes.Node.Counters.Control.TunnelXr.Global.Drop, ['unknown_packets', 'zero_length_body_packets', 'start_control_connection_requests', 'start_control_connection_replies', 'start_control_connection_notifications', 'stop_control_connection_notifications', 'hello_packets', 'outgoing_call_requests', 'outgoing_call_replies', 'outgoing_call_connected_packets', 'incoming_call_requests', 'incoming_call_replies', 'incoming_call_connected_packets', 'call_disconnect_notify_packets', 'wan_error_notify_packets', 'set_link_info_packets', 'service_relay_requests', 'service_relay_replies', 'acknowledgement_packets'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                                    return meta._meta_table['L2tp.Nodes.Node.Counters.Control.TunnelXr.Global.Drop']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                                return meta._meta_table['L2tp.Nodes.Node.Counters.Control.TunnelXr.Global']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                            return meta._meta_table['L2tp.Nodes.Node.Counters.Control.TunnelXr']['meta_info']


                    class Tunnels(_Entity_):
                        """
                        Table of tunnel IDs of control message counters
                        
                        .. attribute:: tunnel
                        
                        	L2TP tunnel control message counters
                        	**type**\: list of  		 :py:class:`Tunnel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Nodes.Node.Counters.Control.Tunnels.Tunnel>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'tunnel-l2tun-oper'
                        _revision = '2018-11-01'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(L2tp.Nodes.Node.Counters.Control.Tunnels, self).__init__()

                            self.yang_name = "tunnels"
                            self.yang_parent_name = "control"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("tunnel", ("tunnel", L2tp.Nodes.Node.Counters.Control.Tunnels.Tunnel))])
                            self._leafs = OrderedDict()

                            self.tunnel = YList(self)
                            self._segment_path = lambda: "tunnels"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2tp.Nodes.Node.Counters.Control.Tunnels, [], name, value)


                        class Tunnel(_Entity_):
                            """
                            L2TP tunnel control message counters
                            
                            .. attribute:: tunnel_id  (key)
                            
                            	L2TP tunnel ID
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: brief
                            
                            	L2TP control message local and remote addresses
                            	**type**\:  :py:class:`Brief <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Nodes.Node.Counters.Control.Tunnels.Tunnel.Brief>`
                            
                            	**config**\: False
                            
                            .. attribute:: global_
                            
                            	Global data
                            	**type**\:  :py:class:`Global <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Nodes.Node.Counters.Control.Tunnels.Tunnel.Global>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'tunnel-l2tun-oper'
                            _revision = '2018-11-01'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(L2tp.Nodes.Node.Counters.Control.Tunnels.Tunnel, self).__init__()

                                self.yang_name = "tunnel"
                                self.yang_parent_name = "tunnels"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['tunnel_id']
                                self._child_classes = OrderedDict([("brief", ("brief", L2tp.Nodes.Node.Counters.Control.Tunnels.Tunnel.Brief)), ("global", ("global_", L2tp.Nodes.Node.Counters.Control.Tunnels.Tunnel.Global))])
                                self._leafs = OrderedDict([
                                    ('tunnel_id', (YLeaf(YType.uint32, 'tunnel-id'), ['int'])),
                                ])
                                self.tunnel_id = None

                                self.brief = L2tp.Nodes.Node.Counters.Control.Tunnels.Tunnel.Brief()
                                self.brief.parent = self
                                self._children_name_map["brief"] = "brief"

                                self.global_ = L2tp.Nodes.Node.Counters.Control.Tunnels.Tunnel.Global()
                                self.global_.parent = self
                                self._children_name_map["global_"] = "global"
                                self._segment_path = lambda: "tunnel" + "[tunnel-id='" + str(self.tunnel_id) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2tp.Nodes.Node.Counters.Control.Tunnels.Tunnel, ['tunnel_id'], name, value)


                            class Brief(_Entity_):
                                """
                                L2TP control message local and remote addresses
                                
                                .. attribute:: remote_tunnel_id
                                
                                	Remote tunnel ID
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: local_address
                                
                                	Local IP address
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                	**config**\: False
                                
                                .. attribute:: remote_address
                                
                                	Remote IP address
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'tunnel-l2tun-oper'
                                _revision = '2018-11-01'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(L2tp.Nodes.Node.Counters.Control.Tunnels.Tunnel.Brief, self).__init__()

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
                                    self._perform_setattr(L2tp.Nodes.Node.Counters.Control.Tunnels.Tunnel.Brief, ['remote_tunnel_id', 'local_address', 'remote_address'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                                    return meta._meta_table['L2tp.Nodes.Node.Counters.Control.Tunnels.Tunnel.Brief']['meta_info']


                            class Global(_Entity_):
                                """
                                Global data
                                
                                .. attribute:: transmit
                                
                                	Transmit data
                                	**type**\:  :py:class:`Transmit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Nodes.Node.Counters.Control.Tunnels.Tunnel.Global.Transmit>`
                                
                                	**config**\: False
                                
                                .. attribute:: retransmit
                                
                                	Re transmit data
                                	**type**\:  :py:class:`Retransmit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Nodes.Node.Counters.Control.Tunnels.Tunnel.Global.Retransmit>`
                                
                                	**config**\: False
                                
                                .. attribute:: received
                                
                                	Received data
                                	**type**\:  :py:class:`Received <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Nodes.Node.Counters.Control.Tunnels.Tunnel.Global.Received>`
                                
                                	**config**\: False
                                
                                .. attribute:: drop
                                
                                	Drop data
                                	**type**\:  :py:class:`Drop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Nodes.Node.Counters.Control.Tunnels.Tunnel.Global.Drop>`
                                
                                	**config**\: False
                                
                                .. attribute:: total_transmit
                                
                                	Total transmit
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: total_retransmit
                                
                                	Total retransmit
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: total_received
                                
                                	Total received
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: total_drop
                                
                                	Total drop
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'tunnel-l2tun-oper'
                                _revision = '2018-11-01'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(L2tp.Nodes.Node.Counters.Control.Tunnels.Tunnel.Global, self).__init__()

                                    self.yang_name = "global"
                                    self.yang_parent_name = "tunnel"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("transmit", ("transmit", L2tp.Nodes.Node.Counters.Control.Tunnels.Tunnel.Global.Transmit)), ("retransmit", ("retransmit", L2tp.Nodes.Node.Counters.Control.Tunnels.Tunnel.Global.Retransmit)), ("received", ("received", L2tp.Nodes.Node.Counters.Control.Tunnels.Tunnel.Global.Received)), ("drop", ("drop", L2tp.Nodes.Node.Counters.Control.Tunnels.Tunnel.Global.Drop))])
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

                                    self.transmit = L2tp.Nodes.Node.Counters.Control.Tunnels.Tunnel.Global.Transmit()
                                    self.transmit.parent = self
                                    self._children_name_map["transmit"] = "transmit"

                                    self.retransmit = L2tp.Nodes.Node.Counters.Control.Tunnels.Tunnel.Global.Retransmit()
                                    self.retransmit.parent = self
                                    self._children_name_map["retransmit"] = "retransmit"

                                    self.received = L2tp.Nodes.Node.Counters.Control.Tunnels.Tunnel.Global.Received()
                                    self.received.parent = self
                                    self._children_name_map["received"] = "received"

                                    self.drop = L2tp.Nodes.Node.Counters.Control.Tunnels.Tunnel.Global.Drop()
                                    self.drop.parent = self
                                    self._children_name_map["drop"] = "drop"
                                    self._segment_path = lambda: "global"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2tp.Nodes.Node.Counters.Control.Tunnels.Tunnel.Global, ['total_transmit', 'total_retransmit', 'total_received', 'total_drop'], name, value)


                                class Transmit(_Entity_):
                                    """
                                    Transmit data
                                    
                                    .. attribute:: unknown_packets
                                    
                                    	Unknown packets
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: zero_length_body_packets
                                    
                                    	Zero length body packets
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: start_control_connection_requests
                                    
                                    	Start control connection requests
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: start_control_connection_replies
                                    
                                    	Start control connection replies
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: start_control_connection_notifications
                                    
                                    	Start control connection notifications
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: stop_control_connection_notifications
                                    
                                    	Stop control connection notifications
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: hello_packets
                                    
                                    	Keep alive messages
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: outgoing_call_requests
                                    
                                    	Outgoing call requests
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: outgoing_call_replies
                                    
                                    	Outgoing call replies
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: outgoing_call_connected_packets
                                    
                                    	Outgoing call connected packets
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: incoming_call_requests
                                    
                                    	Incoming call requests
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: incoming_call_replies
                                    
                                    	Incoming call replies
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: incoming_call_connected_packets
                                    
                                    	Incoming call connected packets
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: call_disconnect_notify_packets
                                    
                                    	Call disconnect notify packets
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: wan_error_notify_packets
                                    
                                    	WAN error notify packets
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: set_link_info_packets
                                    
                                    	Set link info packets
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: service_relay_requests
                                    
                                    	Service relay request counts
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: service_relay_replies
                                    
                                    	Service relay reply counts
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: acknowledgement_packets
                                    
                                    	Packets acknowledgement
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'tunnel-l2tun-oper'
                                    _revision = '2018-11-01'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(L2tp.Nodes.Node.Counters.Control.Tunnels.Tunnel.Global.Transmit, self).__init__()

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
                                        self._perform_setattr(L2tp.Nodes.Node.Counters.Control.Tunnels.Tunnel.Global.Transmit, ['unknown_packets', 'zero_length_body_packets', 'start_control_connection_requests', 'start_control_connection_replies', 'start_control_connection_notifications', 'stop_control_connection_notifications', 'hello_packets', 'outgoing_call_requests', 'outgoing_call_replies', 'outgoing_call_connected_packets', 'incoming_call_requests', 'incoming_call_replies', 'incoming_call_connected_packets', 'call_disconnect_notify_packets', 'wan_error_notify_packets', 'set_link_info_packets', 'service_relay_requests', 'service_relay_replies', 'acknowledgement_packets'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                                        return meta._meta_table['L2tp.Nodes.Node.Counters.Control.Tunnels.Tunnel.Global.Transmit']['meta_info']


                                class Retransmit(_Entity_):
                                    """
                                    Re transmit data
                                    
                                    .. attribute:: unknown_packets
                                    
                                    	Unknown packets
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: zero_length_body_packets
                                    
                                    	Zero length body packets
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: start_control_connection_requests
                                    
                                    	Start control connection requests
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: start_control_connection_replies
                                    
                                    	Start control connection replies
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: start_control_connection_notifications
                                    
                                    	Start control connection notifications
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: stop_control_connection_notifications
                                    
                                    	Stop control connection notifications
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: hello_packets
                                    
                                    	Keep alive messages
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: outgoing_call_requests
                                    
                                    	Outgoing call requests
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: outgoing_call_replies
                                    
                                    	Outgoing call replies
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: outgoing_call_connected_packets
                                    
                                    	Outgoing call connected packets
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: incoming_call_requests
                                    
                                    	Incoming call requests
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: incoming_call_replies
                                    
                                    	Incoming call replies
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: incoming_call_connected_packets
                                    
                                    	Incoming call connected packets
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: call_disconnect_notify_packets
                                    
                                    	Call disconnect notify packets
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: wan_error_notify_packets
                                    
                                    	WAN error notify packets
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: set_link_info_packets
                                    
                                    	Set link info packets
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: service_relay_requests
                                    
                                    	Service relay request counts
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: service_relay_replies
                                    
                                    	Service relay reply counts
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: acknowledgement_packets
                                    
                                    	Packets acknowledgement
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'tunnel-l2tun-oper'
                                    _revision = '2018-11-01'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(L2tp.Nodes.Node.Counters.Control.Tunnels.Tunnel.Global.Retransmit, self).__init__()

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
                                        self._perform_setattr(L2tp.Nodes.Node.Counters.Control.Tunnels.Tunnel.Global.Retransmit, ['unknown_packets', 'zero_length_body_packets', 'start_control_connection_requests', 'start_control_connection_replies', 'start_control_connection_notifications', 'stop_control_connection_notifications', 'hello_packets', 'outgoing_call_requests', 'outgoing_call_replies', 'outgoing_call_connected_packets', 'incoming_call_requests', 'incoming_call_replies', 'incoming_call_connected_packets', 'call_disconnect_notify_packets', 'wan_error_notify_packets', 'set_link_info_packets', 'service_relay_requests', 'service_relay_replies', 'acknowledgement_packets'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                                        return meta._meta_table['L2tp.Nodes.Node.Counters.Control.Tunnels.Tunnel.Global.Retransmit']['meta_info']


                                class Received(_Entity_):
                                    """
                                    Received data
                                    
                                    .. attribute:: unknown_packets
                                    
                                    	Unknown packets
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: zero_length_body_packets
                                    
                                    	Zero length body packets
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: start_control_connection_requests
                                    
                                    	Start control connection requests
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: start_control_connection_replies
                                    
                                    	Start control connection replies
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: start_control_connection_notifications
                                    
                                    	Start control connection notifications
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: stop_control_connection_notifications
                                    
                                    	Stop control connection notifications
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: hello_packets
                                    
                                    	Keep alive messages
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: outgoing_call_requests
                                    
                                    	Outgoing call requests
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: outgoing_call_replies
                                    
                                    	Outgoing call replies
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: outgoing_call_connected_packets
                                    
                                    	Outgoing call connected packets
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: incoming_call_requests
                                    
                                    	Incoming call requests
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: incoming_call_replies
                                    
                                    	Incoming call replies
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: incoming_call_connected_packets
                                    
                                    	Incoming call connected packets
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: call_disconnect_notify_packets
                                    
                                    	Call disconnect notify packets
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: wan_error_notify_packets
                                    
                                    	WAN error notify packets
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: set_link_info_packets
                                    
                                    	Set link info packets
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: service_relay_requests
                                    
                                    	Service relay request counts
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: service_relay_replies
                                    
                                    	Service relay reply counts
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: acknowledgement_packets
                                    
                                    	Packets acknowledgement
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'tunnel-l2tun-oper'
                                    _revision = '2018-11-01'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(L2tp.Nodes.Node.Counters.Control.Tunnels.Tunnel.Global.Received, self).__init__()

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
                                        self._perform_setattr(L2tp.Nodes.Node.Counters.Control.Tunnels.Tunnel.Global.Received, ['unknown_packets', 'zero_length_body_packets', 'start_control_connection_requests', 'start_control_connection_replies', 'start_control_connection_notifications', 'stop_control_connection_notifications', 'hello_packets', 'outgoing_call_requests', 'outgoing_call_replies', 'outgoing_call_connected_packets', 'incoming_call_requests', 'incoming_call_replies', 'incoming_call_connected_packets', 'call_disconnect_notify_packets', 'wan_error_notify_packets', 'set_link_info_packets', 'service_relay_requests', 'service_relay_replies', 'acknowledgement_packets'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                                        return meta._meta_table['L2tp.Nodes.Node.Counters.Control.Tunnels.Tunnel.Global.Received']['meta_info']


                                class Drop(_Entity_):
                                    """
                                    Drop data
                                    
                                    .. attribute:: unknown_packets
                                    
                                    	Unknown packets
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: zero_length_body_packets
                                    
                                    	Zero length body packets
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: start_control_connection_requests
                                    
                                    	Start control connection requests
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: start_control_connection_replies
                                    
                                    	Start control connection replies
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: start_control_connection_notifications
                                    
                                    	Start control connection notifications
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: stop_control_connection_notifications
                                    
                                    	Stop control connection notifications
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: hello_packets
                                    
                                    	Keep alive messages
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: outgoing_call_requests
                                    
                                    	Outgoing call requests
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: outgoing_call_replies
                                    
                                    	Outgoing call replies
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: outgoing_call_connected_packets
                                    
                                    	Outgoing call connected packets
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: incoming_call_requests
                                    
                                    	Incoming call requests
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: incoming_call_replies
                                    
                                    	Incoming call replies
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: incoming_call_connected_packets
                                    
                                    	Incoming call connected packets
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: call_disconnect_notify_packets
                                    
                                    	Call disconnect notify packets
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: wan_error_notify_packets
                                    
                                    	WAN error notify packets
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: set_link_info_packets
                                    
                                    	Set link info packets
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: service_relay_requests
                                    
                                    	Service relay request counts
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: service_relay_replies
                                    
                                    	Service relay reply counts
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: acknowledgement_packets
                                    
                                    	Packets acknowledgement
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'tunnel-l2tun-oper'
                                    _revision = '2018-11-01'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(L2tp.Nodes.Node.Counters.Control.Tunnels.Tunnel.Global.Drop, self).__init__()

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
                                        self._perform_setattr(L2tp.Nodes.Node.Counters.Control.Tunnels.Tunnel.Global.Drop, ['unknown_packets', 'zero_length_body_packets', 'start_control_connection_requests', 'start_control_connection_replies', 'start_control_connection_notifications', 'stop_control_connection_notifications', 'hello_packets', 'outgoing_call_requests', 'outgoing_call_replies', 'outgoing_call_connected_packets', 'incoming_call_requests', 'incoming_call_replies', 'incoming_call_connected_packets', 'call_disconnect_notify_packets', 'wan_error_notify_packets', 'set_link_info_packets', 'service_relay_requests', 'service_relay_replies', 'acknowledgement_packets'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                                        return meta._meta_table['L2tp.Nodes.Node.Counters.Control.Tunnels.Tunnel.Global.Drop']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                                    return meta._meta_table['L2tp.Nodes.Node.Counters.Control.Tunnels.Tunnel.Global']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                                return meta._meta_table['L2tp.Nodes.Node.Counters.Control.Tunnels.Tunnel']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                            return meta._meta_table['L2tp.Nodes.Node.Counters.Control.Tunnels']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                        return meta._meta_table['L2tp.Nodes.Node.Counters.Control']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                    return meta._meta_table['L2tp.Nodes.Node.Counters']['meta_info']


            class TunnelConfigurations(_Entity_):
                """
                List of tunnel IDs
                
                .. attribute:: tunnel_configuration
                
                	L2TP tunnel information
                	**type**\: list of  		 :py:class:`TunnelConfiguration <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Nodes.Node.TunnelConfigurations.TunnelConfiguration>`
                
                	**config**\: False
                
                

                """

                _prefix = 'tunnel-l2tun-oper'
                _revision = '2018-11-01'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(L2tp.Nodes.Node.TunnelConfigurations, self).__init__()

                    self.yang_name = "tunnel-configurations"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("tunnel-configuration", ("tunnel_configuration", L2tp.Nodes.Node.TunnelConfigurations.TunnelConfiguration))])
                    self._leafs = OrderedDict()

                    self.tunnel_configuration = YList(self)
                    self._segment_path = lambda: "tunnel-configurations"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(L2tp.Nodes.Node.TunnelConfigurations, [], name, value)


                class TunnelConfiguration(_Entity_):
                    """
                    L2TP tunnel information
                    
                    .. attribute:: local_tunnel_id  (key)
                    
                    	Local tunnel ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_class
                    
                    	L2Tp class data
                    	**type**\:  :py:class:`L2tpClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Nodes.Node.TunnelConfigurations.TunnelConfiguration.L2tpClass>`
                    
                    	**config**\: False
                    
                    .. attribute:: remote_tunnel_id
                    
                    	Remote tunnel ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'tunnel-l2tun-oper'
                    _revision = '2018-11-01'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(L2tp.Nodes.Node.TunnelConfigurations.TunnelConfiguration, self).__init__()

                        self.yang_name = "tunnel-configuration"
                        self.yang_parent_name = "tunnel-configurations"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['local_tunnel_id']
                        self._child_classes = OrderedDict([("l2tp-class", ("l2tp_class", L2tp.Nodes.Node.TunnelConfigurations.TunnelConfiguration.L2tpClass))])
                        self._leafs = OrderedDict([
                            ('local_tunnel_id', (YLeaf(YType.uint32, 'local-tunnel-id'), ['int'])),
                            ('remote_tunnel_id', (YLeaf(YType.uint32, 'remote-tunnel-id'), ['int'])),
                        ])
                        self.local_tunnel_id = None
                        self.remote_tunnel_id = None

                        self.l2tp_class = L2tp.Nodes.Node.TunnelConfigurations.TunnelConfiguration.L2tpClass()
                        self.l2tp_class.parent = self
                        self._children_name_map["l2tp_class"] = "l2tp-class"
                        self._segment_path = lambda: "tunnel-configuration" + "[local-tunnel-id='" + str(self.local_tunnel_id) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2tp.Nodes.Node.TunnelConfigurations.TunnelConfiguration, ['local_tunnel_id', 'remote_tunnel_id'], name, value)


                    class L2tpClass(_Entity_):
                        """
                        L2Tp class data
                        
                        .. attribute:: ip_tos
                        
                        	IP TOS
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: vrf_name
                        
                        	VRF name
                        	**type**\: str
                        
                        	**length:** 0..256
                        
                        	**config**\: False
                        
                        .. attribute:: receive_window_size
                        
                        	Receive window size
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        	**config**\: False
                        
                        .. attribute:: class_name_xr
                        
                        	Class name
                        	**type**\: str
                        
                        	**length:** 0..256
                        
                        	**config**\: False
                        
                        .. attribute:: digest_hash
                        
                        	Hash configured as MD5 or SHA1
                        	**type**\:  :py:class:`DigestHash <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.DigestHash>`
                        
                        	**config**\: False
                        
                        .. attribute:: password
                        
                        	Password
                        	**type**\: str
                        
                        	**length:** 0..25
                        
                        	**config**\: False
                        
                        .. attribute:: encoded_password
                        
                        	Encoded password
                        	**type**\: str
                        
                        	**length:** 0..256
                        
                        	**config**\: False
                        
                        .. attribute:: host_name
                        
                        	Host name
                        	**type**\: str
                        
                        	**length:** 0..256
                        
                        	**config**\: False
                        
                        .. attribute:: accounting_method_list
                        
                        	Accounting List
                        	**type**\: str
                        
                        	**length:** 0..256
                        
                        	**config**\: False
                        
                        .. attribute:: hello_timeout
                        
                        	Hello timeout value in seconds
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        	**units**\: second
                        
                        .. attribute:: setup_timeout
                        
                        	Timeout setup value in seconds
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        	**units**\: second
                        
                        .. attribute:: retransmit_minimum_timeout
                        
                        	Retransmit minimum timeout in seconds
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        	**units**\: second
                        
                        .. attribute:: retransmit_maximum_timeout
                        
                        	Retransmit maximum timeout in seconds
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        	**units**\: second
                        
                        .. attribute:: initial_retransmit_minimum_timeout
                        
                        	Initial timeout minimum in seconds
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        	**units**\: second
                        
                        .. attribute:: initial_retransmit_maximum_timeout
                        
                        	Initial timeout maximum in seconds
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        	**units**\: second
                        
                        .. attribute:: timeout_no_user
                        
                        	Timeout no user
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: retransmit_retries
                        
                        	Retransmit retries
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: initial_retransmit_retries
                        
                        	Initial retransmit retries
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: is_authentication_enabled
                        
                        	True if authentication is enabled
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_hidden
                        
                        	True if class is hidden
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_digest_enabled
                        
                        	True if digest authentication is enabled
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_digest_check_enabled
                        
                        	True if digest check is enabled
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_congestion_control_enabled
                        
                        	True if congestion control is enabled
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_peer_address_checked
                        
                        	True if peer address is checked
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'tunnel-l2tun-oper'
                        _revision = '2018-11-01'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(L2tp.Nodes.Node.TunnelConfigurations.TunnelConfiguration.L2tpClass, self).__init__()

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
                            self._perform_setattr(L2tp.Nodes.Node.TunnelConfigurations.TunnelConfiguration.L2tpClass, ['ip_tos', 'vrf_name', 'receive_window_size', 'class_name_xr', 'digest_hash', 'password', 'encoded_password', 'host_name', 'accounting_method_list', 'hello_timeout', 'setup_timeout', 'retransmit_minimum_timeout', 'retransmit_maximum_timeout', 'initial_retransmit_minimum_timeout', 'initial_retransmit_maximum_timeout', 'timeout_no_user', 'retransmit_retries', 'initial_retransmit_retries', 'is_authentication_enabled', 'is_hidden', 'is_digest_enabled', 'is_digest_check_enabled', 'is_congestion_control_enabled', 'is_peer_address_checked'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                            return meta._meta_table['L2tp.Nodes.Node.TunnelConfigurations.TunnelConfiguration.L2tpClass']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                        return meta._meta_table['L2tp.Nodes.Node.TunnelConfigurations.TunnelConfiguration']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                    return meta._meta_table['L2tp.Nodes.Node.TunnelConfigurations']['meta_info']


            class CounterHistFail(_Entity_):
                """
                Failure events leading to disconnection
                
                .. attribute:: sess_down_tmout
                
                	sesions affected due to timeout
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: tx_counters
                
                	Send side counters
                	**type**\: str
                
                	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                
                	**config**\: False
                
                .. attribute:: rx_counters
                
                	Receive side counters
                	**type**\: str
                
                	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                
                	**config**\: False
                
                .. attribute:: pkt_timeout
                
                	timeout events by packet
                	**type**\: list of  		 :py:class:`PktTimeout <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Nodes.Node.CounterHistFail.PktTimeout>`
                
                	**config**\: False
                
                

                """

                _prefix = 'tunnel-l2tun-oper'
                _revision = '2018-11-01'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(L2tp.Nodes.Node.CounterHistFail, self).__init__()

                    self.yang_name = "counter-hist-fail"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("pkt-timeout", ("pkt_timeout", L2tp.Nodes.Node.CounterHistFail.PktTimeout))])
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
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(L2tp.Nodes.Node.CounterHistFail, ['sess_down_tmout', 'tx_counters', 'rx_counters'], name, value)


                class PktTimeout(_Entity_):
                    """
                    timeout events by packet
                    
                    .. attribute:: entry
                    
                    	timeout events by packet
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'tunnel-l2tun-oper'
                    _revision = '2018-11-01'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(L2tp.Nodes.Node.CounterHistFail.PktTimeout, self).__init__()

                        self.yang_name = "pkt-timeout"
                        self.yang_parent_name = "counter-hist-fail"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('entry', (YLeaf(YType.uint32, 'entry'), ['int'])),
                        ])
                        self.entry = None
                        self._segment_path = lambda: "pkt-timeout"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2tp.Nodes.Node.CounterHistFail.PktTimeout, ['entry'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                        return meta._meta_table['L2tp.Nodes.Node.CounterHistFail.PktTimeout']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                    return meta._meta_table['L2tp.Nodes.Node.CounterHistFail']['meta_info']


            class Classes(_Entity_):
                """
                List of L2TP class names
                
                .. attribute:: class_
                
                	L2TP class name
                	**type**\: list of  		 :py:class:`Class <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Nodes.Node.Classes.Class>`
                
                	**config**\: False
                
                

                """

                _prefix = 'tunnel-l2tun-oper'
                _revision = '2018-11-01'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(L2tp.Nodes.Node.Classes, self).__init__()

                    self.yang_name = "classes"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("class", ("class_", L2tp.Nodes.Node.Classes.Class))])
                    self._leafs = OrderedDict()

                    self.class_ = YList(self)
                    self._segment_path = lambda: "classes"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(L2tp.Nodes.Node.Classes, [], name, value)


                class Class(_Entity_):
                    """
                    L2TP class name
                    
                    .. attribute:: class_name  (key)
                    
                    	L2TP class name
                    	**type**\: str
                    
                    	**length:** 1..31
                    
                    	**config**\: False
                    
                    .. attribute:: ip_tos
                    
                    	IP TOS
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: vrf_name
                    
                    	VRF name
                    	**type**\: str
                    
                    	**length:** 0..256
                    
                    	**config**\: False
                    
                    .. attribute:: receive_window_size
                    
                    	Receive window size
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**config**\: False
                    
                    .. attribute:: class_name_xr
                    
                    	Class name
                    	**type**\: str
                    
                    	**length:** 0..256
                    
                    	**config**\: False
                    
                    .. attribute:: digest_hash
                    
                    	Hash configured as MD5 or SHA1
                    	**type**\:  :py:class:`DigestHash <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.DigestHash>`
                    
                    	**config**\: False
                    
                    .. attribute:: password
                    
                    	Password
                    	**type**\: str
                    
                    	**length:** 0..25
                    
                    	**config**\: False
                    
                    .. attribute:: encoded_password
                    
                    	Encoded password
                    	**type**\: str
                    
                    	**length:** 0..256
                    
                    	**config**\: False
                    
                    .. attribute:: host_name
                    
                    	Host name
                    	**type**\: str
                    
                    	**length:** 0..256
                    
                    	**config**\: False
                    
                    .. attribute:: accounting_method_list
                    
                    	Accounting List
                    	**type**\: str
                    
                    	**length:** 0..256
                    
                    	**config**\: False
                    
                    .. attribute:: hello_timeout
                    
                    	Hello timeout value in seconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    	**units**\: second
                    
                    .. attribute:: setup_timeout
                    
                    	Timeout setup value in seconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    	**units**\: second
                    
                    .. attribute:: retransmit_minimum_timeout
                    
                    	Retransmit minimum timeout in seconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    	**units**\: second
                    
                    .. attribute:: retransmit_maximum_timeout
                    
                    	Retransmit maximum timeout in seconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    	**units**\: second
                    
                    .. attribute:: initial_retransmit_minimum_timeout
                    
                    	Initial timeout minimum in seconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    	**units**\: second
                    
                    .. attribute:: initial_retransmit_maximum_timeout
                    
                    	Initial timeout maximum in seconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    	**units**\: second
                    
                    .. attribute:: timeout_no_user
                    
                    	Timeout no user
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: retransmit_retries
                    
                    	Retransmit retries
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: initial_retransmit_retries
                    
                    	Initial retransmit retries
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: is_authentication_enabled
                    
                    	True if authentication is enabled
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: is_hidden
                    
                    	True if class is hidden
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: is_digest_enabled
                    
                    	True if digest authentication is enabled
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: is_digest_check_enabled
                    
                    	True if digest check is enabled
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: is_congestion_control_enabled
                    
                    	True if congestion control is enabled
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: is_peer_address_checked
                    
                    	True if peer address is checked
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'tunnel-l2tun-oper'
                    _revision = '2018-11-01'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(L2tp.Nodes.Node.Classes.Class, self).__init__()

                        self.yang_name = "class"
                        self.yang_parent_name = "classes"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
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
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2tp.Nodes.Node.Classes.Class, ['class_name', 'ip_tos', 'vrf_name', 'receive_window_size', 'class_name_xr', 'digest_hash', 'password', 'encoded_password', 'host_name', 'accounting_method_list', 'hello_timeout', 'setup_timeout', 'retransmit_minimum_timeout', 'retransmit_maximum_timeout', 'initial_retransmit_minimum_timeout', 'initial_retransmit_maximum_timeout', 'timeout_no_user', 'retransmit_retries', 'initial_retransmit_retries', 'is_authentication_enabled', 'is_hidden', 'is_digest_enabled', 'is_digest_check_enabled', 'is_congestion_control_enabled', 'is_peer_address_checked'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                        return meta._meta_table['L2tp.Nodes.Node.Classes.Class']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                    return meta._meta_table['L2tp.Nodes.Node.Classes']['meta_info']


            class Tunnels(_Entity_):
                """
                List of tunnel IDs
                
                .. attribute:: tunnel
                
                	L2TP tunnel  information
                	**type**\: list of  		 :py:class:`Tunnel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Nodes.Node.Tunnels.Tunnel>`
                
                	**config**\: False
                
                

                """

                _prefix = 'tunnel-l2tun-oper'
                _revision = '2018-11-01'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(L2tp.Nodes.Node.Tunnels, self).__init__()

                    self.yang_name = "tunnels"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("tunnel", ("tunnel", L2tp.Nodes.Node.Tunnels.Tunnel))])
                    self._leafs = OrderedDict()

                    self.tunnel = YList(self)
                    self._segment_path = lambda: "tunnels"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(L2tp.Nodes.Node.Tunnels, [], name, value)


                class Tunnel(_Entity_):
                    """
                    L2TP tunnel  information
                    
                    .. attribute:: local_tunnel_id  (key)
                    
                    	Local tunnel ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: local_address
                    
                    	Local tunnel address
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    	**config**\: False
                    
                    .. attribute:: remote_address
                    
                    	Remote tunnel address
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    	**config**\: False
                    
                    .. attribute:: local_port
                    
                    	Local port
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**config**\: False
                    
                    .. attribute:: remote_port
                    
                    	Remote port
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**config**\: False
                    
                    .. attribute:: protocol
                    
                    	Protocol
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: is_pmtu_enabled
                    
                    	True if tunnel PMTU checking is enabled
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: remote_tunnel_id
                    
                    	Remote tunnel ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: local_tunnel_name
                    
                    	Local tunnel name
                    	**type**\: str
                    
                    	**length:** 0..256
                    
                    	**config**\: False
                    
                    .. attribute:: remote_tunnel_name
                    
                    	Remote tunnel name
                    	**type**\: str
                    
                    	**length:** 0..256
                    
                    	**config**\: False
                    
                    .. attribute:: class_name
                    
                    	L2TP class name
                    	**type**\: str
                    
                    	**length:** 0..256
                    
                    	**config**\: False
                    
                    .. attribute:: active_sessions
                    
                    	Number of active sessions
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: sequence_ns
                    
                    	Sequence NS
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**config**\: False
                    
                    .. attribute:: sequence_nr
                    
                    	Sequence NR
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**config**\: False
                    
                    .. attribute:: local_window_size
                    
                    	Local window size
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**config**\: False
                    
                    .. attribute:: remote_window_size
                    
                    	Remote window size
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**config**\: False
                    
                    .. attribute:: retransmission_time
                    
                    	Retransmission time in seconds
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**config**\: False
                    
                    	**units**\: second
                    
                    .. attribute:: maximum_retransmission_time
                    
                    	Maximum retransmission time in seconds
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**config**\: False
                    
                    	**units**\: second
                    
                    .. attribute:: unsent_queue_size
                    
                    	Unsent queue size
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**config**\: False
                    
                    .. attribute:: unsent_maximum_queue_size
                    
                    	Unsent maximum queue size
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**config**\: False
                    
                    .. attribute:: resend_queue_size
                    
                    	Resend queue size
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**config**\: False
                    
                    .. attribute:: resend_maximum_queue_size
                    
                    	Resend maximum queue size
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**config**\: False
                    
                    .. attribute:: order_queue_size
                    
                    	Order queue size
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**config**\: False
                    
                    .. attribute:: packet_queue_check
                    
                    	Current number session packet queue check
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**config**\: False
                    
                    .. attribute:: digest_secrets
                    
                    	Control message authentication with digest secrets
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**config**\: False
                    
                    .. attribute:: resends
                    
                    	Total resends
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: zero_length_body_acknowledgement_sent
                    
                    	Total zero length body acknowledgement
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: total_out_of_order_drop_packets
                    
                    	Total out of order dropped packets
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: total_out_of_order_reorder_packets
                    
                    	Total out of order reorder packets
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: total_peer_authentication_failures
                    
                    	Number of peer authentication failures
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: is_tunnel_up
                    
                    	True if tunnel is up
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: is_congestion_control_enabled
                    
                    	True if congestion control is enabled else false
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: retransmit_time
                    
                    	Retransmit time distribution in seconds
                    	**type**\: list of  		 :py:class:`RetransmitTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Nodes.Node.Tunnels.Tunnel.RetransmitTime>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'tunnel-l2tun-oper'
                    _revision = '2018-11-01'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(L2tp.Nodes.Node.Tunnels.Tunnel, self).__init__()

                        self.yang_name = "tunnel"
                        self.yang_parent_name = "tunnels"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['local_tunnel_id']
                        self._child_classes = OrderedDict([("retransmit-time", ("retransmit_time", L2tp.Nodes.Node.Tunnels.Tunnel.RetransmitTime))])
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
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2tp.Nodes.Node.Tunnels.Tunnel, ['local_tunnel_id', 'local_address', 'remote_address', 'local_port', 'remote_port', 'protocol', 'is_pmtu_enabled', 'remote_tunnel_id', 'local_tunnel_name', 'remote_tunnel_name', 'class_name', 'active_sessions', 'sequence_ns', 'sequence_nr', 'local_window_size', 'remote_window_size', 'retransmission_time', 'maximum_retransmission_time', 'unsent_queue_size', 'unsent_maximum_queue_size', 'resend_queue_size', 'resend_maximum_queue_size', 'order_queue_size', 'packet_queue_check', 'digest_secrets', 'resends', 'zero_length_body_acknowledgement_sent', 'total_out_of_order_drop_packets', 'total_out_of_order_reorder_packets', 'total_peer_authentication_failures', 'is_tunnel_up', 'is_congestion_control_enabled'], name, value)


                    class RetransmitTime(_Entity_):
                        """
                        Retransmit time distribution in seconds
                        
                        .. attribute:: entry
                        
                        	Retransmit time distribution in seconds
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        	**config**\: False
                        
                        	**units**\: second
                        
                        

                        """

                        _prefix = 'tunnel-l2tun-oper'
                        _revision = '2018-11-01'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(L2tp.Nodes.Node.Tunnels.Tunnel.RetransmitTime, self).__init__()

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
                            self._perform_setattr(L2tp.Nodes.Node.Tunnels.Tunnel.RetransmitTime, ['entry'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                            return meta._meta_table['L2tp.Nodes.Node.Tunnels.Tunnel.RetransmitTime']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                        return meta._meta_table['L2tp.Nodes.Node.Tunnels.Tunnel']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                    return meta._meta_table['L2tp.Nodes.Node.Tunnels']['meta_info']


            class Sessions(_Entity_):
                """
                List of session IDs
                
                .. attribute:: session
                
                	L2TP information for a particular session
                	**type**\: list of  		 :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Nodes.Node.Sessions.Session>`
                
                	**config**\: False
                
                

                """

                _prefix = 'tunnel-l2tun-oper'
                _revision = '2018-11-01'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(L2tp.Nodes.Node.Sessions, self).__init__()

                    self.yang_name = "sessions"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("session", ("session", L2tp.Nodes.Node.Sessions.Session))])
                    self._leafs = OrderedDict()

                    self.session = YList(self)
                    self._segment_path = lambda: "sessions"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(L2tp.Nodes.Node.Sessions, [], name, value)


                class Session(_Entity_):
                    """
                    L2TP information for a particular session
                    
                    .. attribute:: local_tunnel_id  (key)
                    
                    	Local tunnel ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: local_session_id  (key)
                    
                    	Local session ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: session_application_data
                    
                    	Session application data
                    	**type**\:  :py:class:`SessionApplicationData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Nodes.Node.Sessions.Session.SessionApplicationData>`
                    
                    	**config**\: False
                    
                    .. attribute:: local_ip_address
                    
                    	Local session IP address
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    	**config**\: False
                    
                    .. attribute:: remote_ip_address
                    
                    	Remote session IP address
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_sess_udp_lport
                    
                    	l2tp sh sess udp lport
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_sess_udp_rport
                    
                    	l2tp sh sess udp rport
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**config**\: False
                    
                    .. attribute:: protocol
                    
                    	Protocol
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: remote_tunnel_id
                    
                    	Remote tunnel ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: call_serial_number
                    
                    	Call serial number
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: local_tunnel_name
                    
                    	Local tunnel name
                    	**type**\: str
                    
                    	**length:** 0..256
                    
                    	**config**\: False
                    
                    .. attribute:: remote_tunnel_name
                    
                    	Remote tunnel name
                    	**type**\: str
                    
                    	**length:** 0..256
                    
                    	**config**\: False
                    
                    .. attribute:: remote_session_id
                    
                    	Remote session ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_sess_tie_breaker_enabled
                    
                    	l2tp sh sess tie breaker enabled
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_sess_tie_breaker
                    
                    	l2tp sh sess tie breaker
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: is_session_manual
                    
                    	True if session is manual
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: is_session_up
                    
                    	True if session is up
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: is_udp_checksum_enabled
                    
                    	True if UDP checksum enabled
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: is_sequencing_on
                    
                    	True if session sequence is on
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: is_session_state_established
                    
                    	True if session state is established
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: is_session_locally_initiated
                    
                    	True if session initiated locally
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: is_conditional_debug_enabled
                    
                    	True if conditional debugging is enabled
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: unique_id
                    
                    	Unique ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: interface_name
                    
                    	Interface name
                    	**type**\: str
                    
                    	**length:** 0..256
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'tunnel-l2tun-oper'
                    _revision = '2018-11-01'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(L2tp.Nodes.Node.Sessions.Session, self).__init__()

                        self.yang_name = "session"
                        self.yang_parent_name = "sessions"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['local_tunnel_id','local_session_id']
                        self._child_classes = OrderedDict([("session-application-data", ("session_application_data", L2tp.Nodes.Node.Sessions.Session.SessionApplicationData))])
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

                        self.session_application_data = L2tp.Nodes.Node.Sessions.Session.SessionApplicationData()
                        self.session_application_data.parent = self
                        self._children_name_map["session_application_data"] = "session-application-data"
                        self._segment_path = lambda: "session" + "[local-tunnel-id='" + str(self.local_tunnel_id) + "']" + "[local-session-id='" + str(self.local_session_id) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2tp.Nodes.Node.Sessions.Session, ['local_tunnel_id', 'local_session_id', 'local_ip_address', 'remote_ip_address', 'l2tp_sh_sess_udp_lport', 'l2tp_sh_sess_udp_rport', 'protocol', 'remote_tunnel_id', 'call_serial_number', 'local_tunnel_name', 'remote_tunnel_name', 'remote_session_id', 'l2tp_sh_sess_tie_breaker_enabled', 'l2tp_sh_sess_tie_breaker', 'is_session_manual', 'is_session_up', 'is_udp_checksum_enabled', 'is_sequencing_on', 'is_session_state_established', 'is_session_locally_initiated', 'is_conditional_debug_enabled', 'unique_id', 'interface_name'], name, value)


                    class SessionApplicationData(_Entity_):
                        """
                        Session application data
                        
                        .. attribute:: xconnect
                        
                        	Xconnect data
                        	**type**\:  :py:class:`Xconnect <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Nodes.Node.Sessions.Session.SessionApplicationData.Xconnect>`
                        
                        	**config**\: False
                        
                        .. attribute:: vpdn
                        
                        	VPDN data
                        	**type**\:  :py:class:`Vpdn <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Nodes.Node.Sessions.Session.SessionApplicationData.Vpdn>`
                        
                        	**config**\: False
                        
                        .. attribute:: l2tp_sh_sess_app_type
                        
                        	l2tp sh sess app type
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'tunnel-l2tun-oper'
                        _revision = '2018-11-01'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(L2tp.Nodes.Node.Sessions.Session.SessionApplicationData, self).__init__()

                            self.yang_name = "session-application-data"
                            self.yang_parent_name = "session"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("xconnect", ("xconnect", L2tp.Nodes.Node.Sessions.Session.SessionApplicationData.Xconnect)), ("vpdn", ("vpdn", L2tp.Nodes.Node.Sessions.Session.SessionApplicationData.Vpdn))])
                            self._leafs = OrderedDict([
                                ('l2tp_sh_sess_app_type', (YLeaf(YType.uint32, 'l2tp-sh-sess-app-type'), ['int'])),
                            ])
                            self.l2tp_sh_sess_app_type = None

                            self.xconnect = L2tp.Nodes.Node.Sessions.Session.SessionApplicationData.Xconnect()
                            self.xconnect.parent = self
                            self._children_name_map["xconnect"] = "xconnect"

                            self.vpdn = L2tp.Nodes.Node.Sessions.Session.SessionApplicationData.Vpdn()
                            self.vpdn.parent = self
                            self._children_name_map["vpdn"] = "vpdn"
                            self._segment_path = lambda: "session-application-data"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2tp.Nodes.Node.Sessions.Session.SessionApplicationData, ['l2tp_sh_sess_app_type'], name, value)


                        class Xconnect(_Entity_):
                            """
                            Xconnect data
                            
                            .. attribute:: circuit_name
                            
                            	Circuit name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: sessionvc_id
                            
                            	Session VC ID
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: is_circuit_state_up
                            
                            	True if circuit state is up
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: is_local_circuit_state_up
                            
                            	True if local circuit state is up
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: is_remote_circuit_state_up
                            
                            	True if remote circuit state is up
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: ipv6_protocol_tunneling
                            
                            	IPv6ProtocolTunneling
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'tunnel-l2tun-oper'
                            _revision = '2018-11-01'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(L2tp.Nodes.Node.Sessions.Session.SessionApplicationData.Xconnect, self).__init__()

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
                                self._perform_setattr(L2tp.Nodes.Node.Sessions.Session.SessionApplicationData.Xconnect, ['circuit_name', 'sessionvc_id', 'is_circuit_state_up', 'is_local_circuit_state_up', 'is_remote_circuit_state_up', 'ipv6_protocol_tunneling'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                                return meta._meta_table['L2tp.Nodes.Node.Sessions.Session.SessionApplicationData.Xconnect']['meta_info']


                        class Vpdn(_Entity_):
                            """
                            VPDN data
                            
                            .. attribute:: username
                            
                            	Session username
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: interface_name
                            
                            	Interface name
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'tunnel-l2tun-oper'
                            _revision = '2018-11-01'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(L2tp.Nodes.Node.Sessions.Session.SessionApplicationData.Vpdn, self).__init__()

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
                                self._perform_setattr(L2tp.Nodes.Node.Sessions.Session.SessionApplicationData.Vpdn, ['username', 'interface_name'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                                return meta._meta_table['L2tp.Nodes.Node.Sessions.Session.SessionApplicationData.Vpdn']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                            return meta._meta_table['L2tp.Nodes.Node.Sessions.Session.SessionApplicationData']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                        return meta._meta_table['L2tp.Nodes.Node.Sessions.Session']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                    return meta._meta_table['L2tp.Nodes.Node.Sessions']['meta_info']


            class Session(_Entity_):
                """
                L2TP control messages counters
                
                .. attribute:: unavailable
                
                	L2TP session unavailable  information
                	**type**\:  :py:class:`Unavailable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Nodes.Node.Session.Unavailable>`
                
                	**config**\: False
                
                

                """

                _prefix = 'tunnel-l2tun-oper'
                _revision = '2018-11-01'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(L2tp.Nodes.Node.Session, self).__init__()

                    self.yang_name = "session"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("unavailable", ("unavailable", L2tp.Nodes.Node.Session.Unavailable))])
                    self._leafs = OrderedDict()

                    self.unavailable = L2tp.Nodes.Node.Session.Unavailable()
                    self.unavailable.parent = self
                    self._children_name_map["unavailable"] = "unavailable"
                    self._segment_path = lambda: "session"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(L2tp.Nodes.Node.Session, [], name, value)


                class Unavailable(_Entity_):
                    """
                    L2TP session unavailable  information
                    
                    .. attribute:: sessions_on_hold
                    
                    	Number of session ID in hold database
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'tunnel-l2tun-oper'
                    _revision = '2018-11-01'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(L2tp.Nodes.Node.Session.Unavailable, self).__init__()

                        self.yang_name = "unavailable"
                        self.yang_parent_name = "session"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('sessions_on_hold', (YLeaf(YType.uint32, 'sessions-on-hold'), ['int'])),
                        ])
                        self.sessions_on_hold = None
                        self._segment_path = lambda: "unavailable"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2tp.Nodes.Node.Session.Unavailable, ['sessions_on_hold'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                        return meta._meta_table['L2tp.Nodes.Node.Session.Unavailable']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                    return meta._meta_table['L2tp.Nodes.Node.Session']['meta_info']


            class Internal(_Entity_):
                """
                L2TP v2/v3 internal information
                
                .. attribute:: internal_stats
                
                	internal stats
                	**type**\:  :py:class:`InternalStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Nodes.Node.Internal.InternalStats>`
                
                	**config**\: False
                
                .. attribute:: internal_stats_last_clear
                
                	internal stats last clear
                	**type**\:  :py:class:`InternalStatsLastClear <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tp.Nodes.Node.Internal.InternalStatsLastClear>`
                
                	**config**\: False
                
                .. attribute:: time_last_clear
                
                	time last clear
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                

                """

                _prefix = 'tunnel-l2tun-oper'
                _revision = '2018-11-01'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(L2tp.Nodes.Node.Internal, self).__init__()

                    self.yang_name = "internal"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("internal-stats", ("internal_stats", L2tp.Nodes.Node.Internal.InternalStats)), ("internal-stats-last-clear", ("internal_stats_last_clear", L2tp.Nodes.Node.Internal.InternalStatsLastClear))])
                    self._leafs = OrderedDict([
                        ('time_last_clear', (YLeaf(YType.uint32, 'time-last-clear'), ['int'])),
                    ])
                    self.time_last_clear = None

                    self.internal_stats = L2tp.Nodes.Node.Internal.InternalStats()
                    self.internal_stats.parent = self
                    self._children_name_map["internal_stats"] = "internal-stats"

                    self.internal_stats_last_clear = L2tp.Nodes.Node.Internal.InternalStatsLastClear()
                    self.internal_stats_last_clear.parent = self
                    self._children_name_map["internal_stats_last_clear"] = "internal-stats-last-clear"
                    self._segment_path = lambda: "internal"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(L2tp.Nodes.Node.Internal, ['time_last_clear'], name, value)


                class InternalStats(_Entity_):
                    """
                    internal stats
                    
                    .. attribute:: l2tp_sh_l2x_num_tunnels
                    
                    	l2tp sh l2x num tunnels
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_sessions
                    
                    	l2tp sh l2x num sessions
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_rx_high_water_mark
                    
                    	l2tp sh l2x rx high water mark
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_ave_msg_process_usecs
                    
                    	l2tp sh l2x ave msg process usecs
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_rx_msgs
                    
                    	l2tp sh l2x num rx msgs
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_tx_msgs
                    
                    	l2tp sh l2x num tx msgs
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_tx_err_drops
                    
                    	l2tp sh l2x num tx err drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_tx_conn_drops
                    
                    	l2tp sh l2x num tx conn drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_reordered_msgs
                    
                    	l2tp sh l2x num reordered msgs
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_max_reorder_deviation
                    
                    	l2tp sh l2x max reorder deviation
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_ooo_msgs
                    
                    	l2tp sh l2x num ooo msgs
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_rx_path_drops
                    
                    	l2tp sh l2x num rx path drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_rx_path_data_pkt_drops
                    
                    	l2tp sh l2x num rx path data pkt drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_rx_queue_drops
                    
                    	l2tp sh l2x num rx queue drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_rx_ooo_drops
                    
                    	l2tp sh l2x num rx ooo drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_buffered_msgs
                    
                    	l2tp sh l2x num buffered msgs
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_mutex_block
                    
                    	l2tp sh l2x num mutex block
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_bad_len_drops
                    
                    	l2tp sh l2x num bad len drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_bad_avp_drops
                    
                    	l2tp sh l2x num bad avp drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_missing_cc_id_drops
                    
                    	l2tp sh l2x num missing cc id drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_missing_sess_id_drops
                    
                    	l2tp sh l2x num missing sess id drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_mismatch_cc_id_drops
                    
                    	l2tp sh l2x num mismatch cc id drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_unknown_cc_drops
                    
                    	l2tp sh l2x num unknown cc drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_unknown_sess_drops
                    
                    	l2tp sh l2x num unknown sess drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_linear_id_search
                    
                    	l2tp sh l2x num linear id search
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_linear_id_search_fail
                    
                    	l2tp sh l2x num linear id search fail
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_netio_pkt_rx
                    
                    	l2tp sh l2x num netio pkt rx
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2tun_ave_msg_process_usecs
                    
                    	l2tp sh l2tun ave msg process usecs
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2tun_num_rx_msgs
                    
                    	l2tp sh l2tun num rx msgs
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2tun_num_tx_msgs
                    
                    	l2tp sh l2tun num tx msgs
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_l2tun_socket_ens_send_error_cnt
                    
                    	l2tp l2tun socket ens send error cnt
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_l2tun_socket_session_accept
                    
                    	l2tp l2tun socket session accept
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_l2tun_socket_session_destroy
                    
                    	l2tp l2tun socket session destroy
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_l2tun_socket_session_connect
                    
                    	l2tp l2tun socket session connect
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_l2tun_socket_session_connect_continue
                    
                    	l2tp l2tun socket session connect continue
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_l2tun_session_connecting
                    
                    	l2tp l2tun session connecting
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_l2tun_session_connected
                    
                    	l2tp l2tun session connected
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_l2tun_session_disconnected
                    
                    	l2tp l2tun session disconnected
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_l2tun_session_incoming
                    
                    	l2tp l2tun session incoming
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_l2tun_session_updated
                    
                    	l2tp l2tun session updated
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_l2tun_session_circuit_status
                    
                    	l2tp l2tun session circuit status
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: l2x_lpts_pa_stats_setup_cnt
                    
                    	l2x lpts pa stats setup cnt
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2x_lpts_pa_stats_destroy_cnt
                    
                    	l2x lpts pa stats destroy cnt
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2x_lpts_pa_stats_alloc_cnt
                    
                    	l2x lpts pa stats alloc cnt
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2x_lpts_pa_stats_alloc_fail_cnt
                    
                    	l2x lpts pa stats alloc fail cnt
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2x_lpts_pa_stats_init_cnt
                    
                    	l2x lpts pa stats init cnt
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2x_lpts_pa_stats_init_fail_cnt
                    
                    	l2x lpts pa stats init fail cnt
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2x_lpts_pa_stats_free_cnt
                    
                    	l2x lpts pa stats free cnt
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2x_lpts_pa_stats_pulse_cnt
                    
                    	l2x lpts pa stats pulse cnt
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2x_lpts_pa_stats_pulse_fail_cnt
                    
                    	l2x lpts pa stats pulse fail cnt
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2x_lpts_pa_stats_bind_cnt
                    
                    	l2x lpts pa stats bind cnt
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2x_lpts_pa_stats_bind_fail_cnt
                    
                    	l2x lpts pa stats bind fail cnt
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2x_lpts_pa_stats_bind_batch_cnt
                    
                    	l2x lpts pa stats bind batch cnt
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2x_lpts_pa_stats_bind_batch_fail_cnt
                    
                    	l2x lpts pa stats bind batch fail cnt
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2x_lpts_pa_stats_bind_time
                    
                    	l2x lpts pa stats bind time
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2x_lpts_pa_stats_expire_cnt
                    
                    	l2x lpts pa stats expire cnt
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2x_lpts_pa_stats_replay_cnt
                    
                    	l2x lpts pa stats replay cnt
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2x_lpts_pa_stats_replay_batch_cnt
                    
                    	l2x lpts pa stats replay batch cnt
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2x_lpts_pa_stats_replay_time
                    
                    	l2x lpts pa stats replay time
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'tunnel-l2tun-oper'
                    _revision = '2018-11-01'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(L2tp.Nodes.Node.Internal.InternalStats, self).__init__()

                        self.yang_name = "internal-stats"
                        self.yang_parent_name = "internal"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('l2tp_sh_l2x_num_tunnels', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-tunnels'), ['int'])),
                            ('l2tp_sh_l2x_num_sessions', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-sessions'), ['int'])),
                            ('l2tp_sh_l2x_rx_high_water_mark', (YLeaf(YType.uint32, 'l2tp-sh-l2x-rx-high-water-mark'), ['int'])),
                            ('l2tp_sh_l2x_ave_msg_process_usecs', (YLeaf(YType.uint64, 'l2tp-sh-l2x-ave-msg-process-usecs'), ['int'])),
                            ('l2tp_sh_l2x_num_rx_msgs', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-rx-msgs'), ['int'])),
                            ('l2tp_sh_l2x_num_tx_msgs', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-tx-msgs'), ['int'])),
                            ('l2tp_sh_l2x_num_tx_err_drops', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-tx-err-drops'), ['int'])),
                            ('l2tp_sh_l2x_num_tx_conn_drops', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-tx-conn-drops'), ['int'])),
                            ('l2tp_sh_l2x_num_reordered_msgs', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-reordered-msgs'), ['int'])),
                            ('l2tp_sh_l2x_max_reorder_deviation', (YLeaf(YType.uint32, 'l2tp-sh-l2x-max-reorder-deviation'), ['int'])),
                            ('l2tp_sh_l2x_num_ooo_msgs', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-ooo-msgs'), ['int'])),
                            ('l2tp_sh_l2x_num_rx_path_drops', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-rx-path-drops'), ['int'])),
                            ('l2tp_sh_l2x_num_rx_path_data_pkt_drops', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-rx-path-data-pkt-drops'), ['int'])),
                            ('l2tp_sh_l2x_num_rx_queue_drops', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-rx-queue-drops'), ['int'])),
                            ('l2tp_sh_l2x_num_rx_ooo_drops', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-rx-ooo-drops'), ['int'])),
                            ('l2tp_sh_l2x_num_buffered_msgs', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-buffered-msgs'), ['int'])),
                            ('l2tp_sh_l2x_num_mutex_block', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-mutex-block'), ['int'])),
                            ('l2tp_sh_l2x_num_bad_len_drops', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-bad-len-drops'), ['int'])),
                            ('l2tp_sh_l2x_num_bad_avp_drops', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-bad-avp-drops'), ['int'])),
                            ('l2tp_sh_l2x_num_missing_cc_id_drops', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-missing-cc-id-drops'), ['int'])),
                            ('l2tp_sh_l2x_num_missing_sess_id_drops', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-missing-sess-id-drops'), ['int'])),
                            ('l2tp_sh_l2x_num_mismatch_cc_id_drops', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-mismatch-cc-id-drops'), ['int'])),
                            ('l2tp_sh_l2x_num_unknown_cc_drops', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-unknown-cc-drops'), ['int'])),
                            ('l2tp_sh_l2x_num_unknown_sess_drops', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-unknown-sess-drops'), ['int'])),
                            ('l2tp_sh_l2x_num_linear_id_search', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-linear-id-search'), ['int'])),
                            ('l2tp_sh_l2x_num_linear_id_search_fail', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-linear-id-search-fail'), ['int'])),
                            ('l2tp_sh_l2x_num_netio_pkt_rx', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-netio-pkt-rx'), ['int'])),
                            ('l2tp_sh_l2tun_ave_msg_process_usecs', (YLeaf(YType.uint64, 'l2tp-sh-l2tun-ave-msg-process-usecs'), ['int'])),
                            ('l2tp_sh_l2tun_num_rx_msgs', (YLeaf(YType.uint32, 'l2tp-sh-l2tun-num-rx-msgs'), ['int'])),
                            ('l2tp_sh_l2tun_num_tx_msgs', (YLeaf(YType.uint32, 'l2tp-sh-l2tun-num-tx-msgs'), ['int'])),
                            ('l2tp_l2tun_socket_ens_send_error_cnt', (YLeaf(YType.uint32, 'l2tp-l2tun-socket-ens-send-error-cnt'), ['int'])),
                            ('l2tp_l2tun_socket_session_accept', (YLeaf(YType.uint64, 'l2tp-l2tun-socket-session-accept'), ['int'])),
                            ('l2tp_l2tun_socket_session_destroy', (YLeaf(YType.uint64, 'l2tp-l2tun-socket-session-destroy'), ['int'])),
                            ('l2tp_l2tun_socket_session_connect', (YLeaf(YType.uint64, 'l2tp-l2tun-socket-session-connect'), ['int'])),
                            ('l2tp_l2tun_socket_session_connect_continue', (YLeaf(YType.uint64, 'l2tp-l2tun-socket-session-connect-continue'), ['int'])),
                            ('l2tp_l2tun_session_connecting', (YLeaf(YType.uint64, 'l2tp-l2tun-session-connecting'), ['int'])),
                            ('l2tp_l2tun_session_connected', (YLeaf(YType.uint64, 'l2tp-l2tun-session-connected'), ['int'])),
                            ('l2tp_l2tun_session_disconnected', (YLeaf(YType.uint64, 'l2tp-l2tun-session-disconnected'), ['int'])),
                            ('l2tp_l2tun_session_incoming', (YLeaf(YType.uint64, 'l2tp-l2tun-session-incoming'), ['int'])),
                            ('l2tp_l2tun_session_updated', (YLeaf(YType.uint64, 'l2tp-l2tun-session-updated'), ['int'])),
                            ('l2tp_l2tun_session_circuit_status', (YLeaf(YType.uint64, 'l2tp-l2tun-session-circuit-status'), ['int'])),
                            ('l2x_lpts_pa_stats_setup_cnt', (YLeaf(YType.uint32, 'l2x-lpts-pa-stats-setup-cnt'), ['int'])),
                            ('l2x_lpts_pa_stats_destroy_cnt', (YLeaf(YType.uint32, 'l2x-lpts-pa-stats-destroy-cnt'), ['int'])),
                            ('l2x_lpts_pa_stats_alloc_cnt', (YLeaf(YType.uint32, 'l2x-lpts-pa-stats-alloc-cnt'), ['int'])),
                            ('l2x_lpts_pa_stats_alloc_fail_cnt', (YLeaf(YType.uint32, 'l2x-lpts-pa-stats-alloc-fail-cnt'), ['int'])),
                            ('l2x_lpts_pa_stats_init_cnt', (YLeaf(YType.uint32, 'l2x-lpts-pa-stats-init-cnt'), ['int'])),
                            ('l2x_lpts_pa_stats_init_fail_cnt', (YLeaf(YType.uint32, 'l2x-lpts-pa-stats-init-fail-cnt'), ['int'])),
                            ('l2x_lpts_pa_stats_free_cnt', (YLeaf(YType.uint32, 'l2x-lpts-pa-stats-free-cnt'), ['int'])),
                            ('l2x_lpts_pa_stats_pulse_cnt', (YLeaf(YType.uint32, 'l2x-lpts-pa-stats-pulse-cnt'), ['int'])),
                            ('l2x_lpts_pa_stats_pulse_fail_cnt', (YLeaf(YType.uint32, 'l2x-lpts-pa-stats-pulse-fail-cnt'), ['int'])),
                            ('l2x_lpts_pa_stats_bind_cnt', (YLeaf(YType.uint32, 'l2x-lpts-pa-stats-bind-cnt'), ['int'])),
                            ('l2x_lpts_pa_stats_bind_fail_cnt', (YLeaf(YType.uint32, 'l2x-lpts-pa-stats-bind-fail-cnt'), ['int'])),
                            ('l2x_lpts_pa_stats_bind_batch_cnt', (YLeaf(YType.uint32, 'l2x-lpts-pa-stats-bind-batch-cnt'), ['int'])),
                            ('l2x_lpts_pa_stats_bind_batch_fail_cnt', (YLeaf(YType.uint32, 'l2x-lpts-pa-stats-bind-batch-fail-cnt'), ['int'])),
                            ('l2x_lpts_pa_stats_bind_time', (YLeaf(YType.uint32, 'l2x-lpts-pa-stats-bind-time'), ['int'])),
                            ('l2x_lpts_pa_stats_expire_cnt', (YLeaf(YType.uint32, 'l2x-lpts-pa-stats-expire-cnt'), ['int'])),
                            ('l2x_lpts_pa_stats_replay_cnt', (YLeaf(YType.uint32, 'l2x-lpts-pa-stats-replay-cnt'), ['int'])),
                            ('l2x_lpts_pa_stats_replay_batch_cnt', (YLeaf(YType.uint32, 'l2x-lpts-pa-stats-replay-batch-cnt'), ['int'])),
                            ('l2x_lpts_pa_stats_replay_time', (YLeaf(YType.uint32, 'l2x-lpts-pa-stats-replay-time'), ['int'])),
                        ])
                        self.l2tp_sh_l2x_num_tunnels = None
                        self.l2tp_sh_l2x_num_sessions = None
                        self.l2tp_sh_l2x_rx_high_water_mark = None
                        self.l2tp_sh_l2x_ave_msg_process_usecs = None
                        self.l2tp_sh_l2x_num_rx_msgs = None
                        self.l2tp_sh_l2x_num_tx_msgs = None
                        self.l2tp_sh_l2x_num_tx_err_drops = None
                        self.l2tp_sh_l2x_num_tx_conn_drops = None
                        self.l2tp_sh_l2x_num_reordered_msgs = None
                        self.l2tp_sh_l2x_max_reorder_deviation = None
                        self.l2tp_sh_l2x_num_ooo_msgs = None
                        self.l2tp_sh_l2x_num_rx_path_drops = None
                        self.l2tp_sh_l2x_num_rx_path_data_pkt_drops = None
                        self.l2tp_sh_l2x_num_rx_queue_drops = None
                        self.l2tp_sh_l2x_num_rx_ooo_drops = None
                        self.l2tp_sh_l2x_num_buffered_msgs = None
                        self.l2tp_sh_l2x_num_mutex_block = None
                        self.l2tp_sh_l2x_num_bad_len_drops = None
                        self.l2tp_sh_l2x_num_bad_avp_drops = None
                        self.l2tp_sh_l2x_num_missing_cc_id_drops = None
                        self.l2tp_sh_l2x_num_missing_sess_id_drops = None
                        self.l2tp_sh_l2x_num_mismatch_cc_id_drops = None
                        self.l2tp_sh_l2x_num_unknown_cc_drops = None
                        self.l2tp_sh_l2x_num_unknown_sess_drops = None
                        self.l2tp_sh_l2x_num_linear_id_search = None
                        self.l2tp_sh_l2x_num_linear_id_search_fail = None
                        self.l2tp_sh_l2x_num_netio_pkt_rx = None
                        self.l2tp_sh_l2tun_ave_msg_process_usecs = None
                        self.l2tp_sh_l2tun_num_rx_msgs = None
                        self.l2tp_sh_l2tun_num_tx_msgs = None
                        self.l2tp_l2tun_socket_ens_send_error_cnt = None
                        self.l2tp_l2tun_socket_session_accept = None
                        self.l2tp_l2tun_socket_session_destroy = None
                        self.l2tp_l2tun_socket_session_connect = None
                        self.l2tp_l2tun_socket_session_connect_continue = None
                        self.l2tp_l2tun_session_connecting = None
                        self.l2tp_l2tun_session_connected = None
                        self.l2tp_l2tun_session_disconnected = None
                        self.l2tp_l2tun_session_incoming = None
                        self.l2tp_l2tun_session_updated = None
                        self.l2tp_l2tun_session_circuit_status = None
                        self.l2x_lpts_pa_stats_setup_cnt = None
                        self.l2x_lpts_pa_stats_destroy_cnt = None
                        self.l2x_lpts_pa_stats_alloc_cnt = None
                        self.l2x_lpts_pa_stats_alloc_fail_cnt = None
                        self.l2x_lpts_pa_stats_init_cnt = None
                        self.l2x_lpts_pa_stats_init_fail_cnt = None
                        self.l2x_lpts_pa_stats_free_cnt = None
                        self.l2x_lpts_pa_stats_pulse_cnt = None
                        self.l2x_lpts_pa_stats_pulse_fail_cnt = None
                        self.l2x_lpts_pa_stats_bind_cnt = None
                        self.l2x_lpts_pa_stats_bind_fail_cnt = None
                        self.l2x_lpts_pa_stats_bind_batch_cnt = None
                        self.l2x_lpts_pa_stats_bind_batch_fail_cnt = None
                        self.l2x_lpts_pa_stats_bind_time = None
                        self.l2x_lpts_pa_stats_expire_cnt = None
                        self.l2x_lpts_pa_stats_replay_cnt = None
                        self.l2x_lpts_pa_stats_replay_batch_cnt = None
                        self.l2x_lpts_pa_stats_replay_time = None
                        self._segment_path = lambda: "internal-stats"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2tp.Nodes.Node.Internal.InternalStats, ['l2tp_sh_l2x_num_tunnels', 'l2tp_sh_l2x_num_sessions', 'l2tp_sh_l2x_rx_high_water_mark', 'l2tp_sh_l2x_ave_msg_process_usecs', 'l2tp_sh_l2x_num_rx_msgs', 'l2tp_sh_l2x_num_tx_msgs', 'l2tp_sh_l2x_num_tx_err_drops', 'l2tp_sh_l2x_num_tx_conn_drops', 'l2tp_sh_l2x_num_reordered_msgs', 'l2tp_sh_l2x_max_reorder_deviation', 'l2tp_sh_l2x_num_ooo_msgs', 'l2tp_sh_l2x_num_rx_path_drops', 'l2tp_sh_l2x_num_rx_path_data_pkt_drops', 'l2tp_sh_l2x_num_rx_queue_drops', 'l2tp_sh_l2x_num_rx_ooo_drops', 'l2tp_sh_l2x_num_buffered_msgs', 'l2tp_sh_l2x_num_mutex_block', 'l2tp_sh_l2x_num_bad_len_drops', 'l2tp_sh_l2x_num_bad_avp_drops', 'l2tp_sh_l2x_num_missing_cc_id_drops', 'l2tp_sh_l2x_num_missing_sess_id_drops', 'l2tp_sh_l2x_num_mismatch_cc_id_drops', 'l2tp_sh_l2x_num_unknown_cc_drops', 'l2tp_sh_l2x_num_unknown_sess_drops', 'l2tp_sh_l2x_num_linear_id_search', 'l2tp_sh_l2x_num_linear_id_search_fail', 'l2tp_sh_l2x_num_netio_pkt_rx', 'l2tp_sh_l2tun_ave_msg_process_usecs', 'l2tp_sh_l2tun_num_rx_msgs', 'l2tp_sh_l2tun_num_tx_msgs', 'l2tp_l2tun_socket_ens_send_error_cnt', 'l2tp_l2tun_socket_session_accept', 'l2tp_l2tun_socket_session_destroy', 'l2tp_l2tun_socket_session_connect', 'l2tp_l2tun_socket_session_connect_continue', 'l2tp_l2tun_session_connecting', 'l2tp_l2tun_session_connected', 'l2tp_l2tun_session_disconnected', 'l2tp_l2tun_session_incoming', 'l2tp_l2tun_session_updated', 'l2tp_l2tun_session_circuit_status', 'l2x_lpts_pa_stats_setup_cnt', 'l2x_lpts_pa_stats_destroy_cnt', 'l2x_lpts_pa_stats_alloc_cnt', 'l2x_lpts_pa_stats_alloc_fail_cnt', 'l2x_lpts_pa_stats_init_cnt', 'l2x_lpts_pa_stats_init_fail_cnt', 'l2x_lpts_pa_stats_free_cnt', 'l2x_lpts_pa_stats_pulse_cnt', 'l2x_lpts_pa_stats_pulse_fail_cnt', 'l2x_lpts_pa_stats_bind_cnt', 'l2x_lpts_pa_stats_bind_fail_cnt', 'l2x_lpts_pa_stats_bind_batch_cnt', 'l2x_lpts_pa_stats_bind_batch_fail_cnt', 'l2x_lpts_pa_stats_bind_time', 'l2x_lpts_pa_stats_expire_cnt', 'l2x_lpts_pa_stats_replay_cnt', 'l2x_lpts_pa_stats_replay_batch_cnt', 'l2x_lpts_pa_stats_replay_time'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                        return meta._meta_table['L2tp.Nodes.Node.Internal.InternalStats']['meta_info']


                class InternalStatsLastClear(_Entity_):
                    """
                    internal stats last clear
                    
                    .. attribute:: l2tp_sh_l2x_num_tunnels
                    
                    	l2tp sh l2x num tunnels
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_sessions
                    
                    	l2tp sh l2x num sessions
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_rx_high_water_mark
                    
                    	l2tp sh l2x rx high water mark
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_ave_msg_process_usecs
                    
                    	l2tp sh l2x ave msg process usecs
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_rx_msgs
                    
                    	l2tp sh l2x num rx msgs
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_tx_msgs
                    
                    	l2tp sh l2x num tx msgs
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_tx_err_drops
                    
                    	l2tp sh l2x num tx err drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_tx_conn_drops
                    
                    	l2tp sh l2x num tx conn drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_reordered_msgs
                    
                    	l2tp sh l2x num reordered msgs
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_max_reorder_deviation
                    
                    	l2tp sh l2x max reorder deviation
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_ooo_msgs
                    
                    	l2tp sh l2x num ooo msgs
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_rx_path_drops
                    
                    	l2tp sh l2x num rx path drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_rx_path_data_pkt_drops
                    
                    	l2tp sh l2x num rx path data pkt drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_rx_queue_drops
                    
                    	l2tp sh l2x num rx queue drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_rx_ooo_drops
                    
                    	l2tp sh l2x num rx ooo drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_buffered_msgs
                    
                    	l2tp sh l2x num buffered msgs
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_mutex_block
                    
                    	l2tp sh l2x num mutex block
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_bad_len_drops
                    
                    	l2tp sh l2x num bad len drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_bad_avp_drops
                    
                    	l2tp sh l2x num bad avp drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_missing_cc_id_drops
                    
                    	l2tp sh l2x num missing cc id drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_missing_sess_id_drops
                    
                    	l2tp sh l2x num missing sess id drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_mismatch_cc_id_drops
                    
                    	l2tp sh l2x num mismatch cc id drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_unknown_cc_drops
                    
                    	l2tp sh l2x num unknown cc drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_unknown_sess_drops
                    
                    	l2tp sh l2x num unknown sess drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_linear_id_search
                    
                    	l2tp sh l2x num linear id search
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_linear_id_search_fail
                    
                    	l2tp sh l2x num linear id search fail
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_netio_pkt_rx
                    
                    	l2tp sh l2x num netio pkt rx
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2tun_ave_msg_process_usecs
                    
                    	l2tp sh l2tun ave msg process usecs
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2tun_num_rx_msgs
                    
                    	l2tp sh l2tun num rx msgs
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2tun_num_tx_msgs
                    
                    	l2tp sh l2tun num tx msgs
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_l2tun_socket_ens_send_error_cnt
                    
                    	l2tp l2tun socket ens send error cnt
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_l2tun_socket_session_accept
                    
                    	l2tp l2tun socket session accept
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_l2tun_socket_session_destroy
                    
                    	l2tp l2tun socket session destroy
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_l2tun_socket_session_connect
                    
                    	l2tp l2tun socket session connect
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_l2tun_socket_session_connect_continue
                    
                    	l2tp l2tun socket session connect continue
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_l2tun_session_connecting
                    
                    	l2tp l2tun session connecting
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_l2tun_session_connected
                    
                    	l2tp l2tun session connected
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_l2tun_session_disconnected
                    
                    	l2tp l2tun session disconnected
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_l2tun_session_incoming
                    
                    	l2tp l2tun session incoming
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_l2tun_session_updated
                    
                    	l2tp l2tun session updated
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_l2tun_session_circuit_status
                    
                    	l2tp l2tun session circuit status
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: l2x_lpts_pa_stats_setup_cnt
                    
                    	l2x lpts pa stats setup cnt
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2x_lpts_pa_stats_destroy_cnt
                    
                    	l2x lpts pa stats destroy cnt
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2x_lpts_pa_stats_alloc_cnt
                    
                    	l2x lpts pa stats alloc cnt
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2x_lpts_pa_stats_alloc_fail_cnt
                    
                    	l2x lpts pa stats alloc fail cnt
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2x_lpts_pa_stats_init_cnt
                    
                    	l2x lpts pa stats init cnt
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2x_lpts_pa_stats_init_fail_cnt
                    
                    	l2x lpts pa stats init fail cnt
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2x_lpts_pa_stats_free_cnt
                    
                    	l2x lpts pa stats free cnt
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2x_lpts_pa_stats_pulse_cnt
                    
                    	l2x lpts pa stats pulse cnt
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2x_lpts_pa_stats_pulse_fail_cnt
                    
                    	l2x lpts pa stats pulse fail cnt
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2x_lpts_pa_stats_bind_cnt
                    
                    	l2x lpts pa stats bind cnt
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2x_lpts_pa_stats_bind_fail_cnt
                    
                    	l2x lpts pa stats bind fail cnt
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2x_lpts_pa_stats_bind_batch_cnt
                    
                    	l2x lpts pa stats bind batch cnt
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2x_lpts_pa_stats_bind_batch_fail_cnt
                    
                    	l2x lpts pa stats bind batch fail cnt
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2x_lpts_pa_stats_bind_time
                    
                    	l2x lpts pa stats bind time
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2x_lpts_pa_stats_expire_cnt
                    
                    	l2x lpts pa stats expire cnt
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2x_lpts_pa_stats_replay_cnt
                    
                    	l2x lpts pa stats replay cnt
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2x_lpts_pa_stats_replay_batch_cnt
                    
                    	l2x lpts pa stats replay batch cnt
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2x_lpts_pa_stats_replay_time
                    
                    	l2x lpts pa stats replay time
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'tunnel-l2tun-oper'
                    _revision = '2018-11-01'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(L2tp.Nodes.Node.Internal.InternalStatsLastClear, self).__init__()

                        self.yang_name = "internal-stats-last-clear"
                        self.yang_parent_name = "internal"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('l2tp_sh_l2x_num_tunnels', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-tunnels'), ['int'])),
                            ('l2tp_sh_l2x_num_sessions', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-sessions'), ['int'])),
                            ('l2tp_sh_l2x_rx_high_water_mark', (YLeaf(YType.uint32, 'l2tp-sh-l2x-rx-high-water-mark'), ['int'])),
                            ('l2tp_sh_l2x_ave_msg_process_usecs', (YLeaf(YType.uint64, 'l2tp-sh-l2x-ave-msg-process-usecs'), ['int'])),
                            ('l2tp_sh_l2x_num_rx_msgs', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-rx-msgs'), ['int'])),
                            ('l2tp_sh_l2x_num_tx_msgs', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-tx-msgs'), ['int'])),
                            ('l2tp_sh_l2x_num_tx_err_drops', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-tx-err-drops'), ['int'])),
                            ('l2tp_sh_l2x_num_tx_conn_drops', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-tx-conn-drops'), ['int'])),
                            ('l2tp_sh_l2x_num_reordered_msgs', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-reordered-msgs'), ['int'])),
                            ('l2tp_sh_l2x_max_reorder_deviation', (YLeaf(YType.uint32, 'l2tp-sh-l2x-max-reorder-deviation'), ['int'])),
                            ('l2tp_sh_l2x_num_ooo_msgs', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-ooo-msgs'), ['int'])),
                            ('l2tp_sh_l2x_num_rx_path_drops', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-rx-path-drops'), ['int'])),
                            ('l2tp_sh_l2x_num_rx_path_data_pkt_drops', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-rx-path-data-pkt-drops'), ['int'])),
                            ('l2tp_sh_l2x_num_rx_queue_drops', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-rx-queue-drops'), ['int'])),
                            ('l2tp_sh_l2x_num_rx_ooo_drops', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-rx-ooo-drops'), ['int'])),
                            ('l2tp_sh_l2x_num_buffered_msgs', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-buffered-msgs'), ['int'])),
                            ('l2tp_sh_l2x_num_mutex_block', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-mutex-block'), ['int'])),
                            ('l2tp_sh_l2x_num_bad_len_drops', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-bad-len-drops'), ['int'])),
                            ('l2tp_sh_l2x_num_bad_avp_drops', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-bad-avp-drops'), ['int'])),
                            ('l2tp_sh_l2x_num_missing_cc_id_drops', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-missing-cc-id-drops'), ['int'])),
                            ('l2tp_sh_l2x_num_missing_sess_id_drops', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-missing-sess-id-drops'), ['int'])),
                            ('l2tp_sh_l2x_num_mismatch_cc_id_drops', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-mismatch-cc-id-drops'), ['int'])),
                            ('l2tp_sh_l2x_num_unknown_cc_drops', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-unknown-cc-drops'), ['int'])),
                            ('l2tp_sh_l2x_num_unknown_sess_drops', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-unknown-sess-drops'), ['int'])),
                            ('l2tp_sh_l2x_num_linear_id_search', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-linear-id-search'), ['int'])),
                            ('l2tp_sh_l2x_num_linear_id_search_fail', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-linear-id-search-fail'), ['int'])),
                            ('l2tp_sh_l2x_num_netio_pkt_rx', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-netio-pkt-rx'), ['int'])),
                            ('l2tp_sh_l2tun_ave_msg_process_usecs', (YLeaf(YType.uint64, 'l2tp-sh-l2tun-ave-msg-process-usecs'), ['int'])),
                            ('l2tp_sh_l2tun_num_rx_msgs', (YLeaf(YType.uint32, 'l2tp-sh-l2tun-num-rx-msgs'), ['int'])),
                            ('l2tp_sh_l2tun_num_tx_msgs', (YLeaf(YType.uint32, 'l2tp-sh-l2tun-num-tx-msgs'), ['int'])),
                            ('l2tp_l2tun_socket_ens_send_error_cnt', (YLeaf(YType.uint32, 'l2tp-l2tun-socket-ens-send-error-cnt'), ['int'])),
                            ('l2tp_l2tun_socket_session_accept', (YLeaf(YType.uint64, 'l2tp-l2tun-socket-session-accept'), ['int'])),
                            ('l2tp_l2tun_socket_session_destroy', (YLeaf(YType.uint64, 'l2tp-l2tun-socket-session-destroy'), ['int'])),
                            ('l2tp_l2tun_socket_session_connect', (YLeaf(YType.uint64, 'l2tp-l2tun-socket-session-connect'), ['int'])),
                            ('l2tp_l2tun_socket_session_connect_continue', (YLeaf(YType.uint64, 'l2tp-l2tun-socket-session-connect-continue'), ['int'])),
                            ('l2tp_l2tun_session_connecting', (YLeaf(YType.uint64, 'l2tp-l2tun-session-connecting'), ['int'])),
                            ('l2tp_l2tun_session_connected', (YLeaf(YType.uint64, 'l2tp-l2tun-session-connected'), ['int'])),
                            ('l2tp_l2tun_session_disconnected', (YLeaf(YType.uint64, 'l2tp-l2tun-session-disconnected'), ['int'])),
                            ('l2tp_l2tun_session_incoming', (YLeaf(YType.uint64, 'l2tp-l2tun-session-incoming'), ['int'])),
                            ('l2tp_l2tun_session_updated', (YLeaf(YType.uint64, 'l2tp-l2tun-session-updated'), ['int'])),
                            ('l2tp_l2tun_session_circuit_status', (YLeaf(YType.uint64, 'l2tp-l2tun-session-circuit-status'), ['int'])),
                            ('l2x_lpts_pa_stats_setup_cnt', (YLeaf(YType.uint32, 'l2x-lpts-pa-stats-setup-cnt'), ['int'])),
                            ('l2x_lpts_pa_stats_destroy_cnt', (YLeaf(YType.uint32, 'l2x-lpts-pa-stats-destroy-cnt'), ['int'])),
                            ('l2x_lpts_pa_stats_alloc_cnt', (YLeaf(YType.uint32, 'l2x-lpts-pa-stats-alloc-cnt'), ['int'])),
                            ('l2x_lpts_pa_stats_alloc_fail_cnt', (YLeaf(YType.uint32, 'l2x-lpts-pa-stats-alloc-fail-cnt'), ['int'])),
                            ('l2x_lpts_pa_stats_init_cnt', (YLeaf(YType.uint32, 'l2x-lpts-pa-stats-init-cnt'), ['int'])),
                            ('l2x_lpts_pa_stats_init_fail_cnt', (YLeaf(YType.uint32, 'l2x-lpts-pa-stats-init-fail-cnt'), ['int'])),
                            ('l2x_lpts_pa_stats_free_cnt', (YLeaf(YType.uint32, 'l2x-lpts-pa-stats-free-cnt'), ['int'])),
                            ('l2x_lpts_pa_stats_pulse_cnt', (YLeaf(YType.uint32, 'l2x-lpts-pa-stats-pulse-cnt'), ['int'])),
                            ('l2x_lpts_pa_stats_pulse_fail_cnt', (YLeaf(YType.uint32, 'l2x-lpts-pa-stats-pulse-fail-cnt'), ['int'])),
                            ('l2x_lpts_pa_stats_bind_cnt', (YLeaf(YType.uint32, 'l2x-lpts-pa-stats-bind-cnt'), ['int'])),
                            ('l2x_lpts_pa_stats_bind_fail_cnt', (YLeaf(YType.uint32, 'l2x-lpts-pa-stats-bind-fail-cnt'), ['int'])),
                            ('l2x_lpts_pa_stats_bind_batch_cnt', (YLeaf(YType.uint32, 'l2x-lpts-pa-stats-bind-batch-cnt'), ['int'])),
                            ('l2x_lpts_pa_stats_bind_batch_fail_cnt', (YLeaf(YType.uint32, 'l2x-lpts-pa-stats-bind-batch-fail-cnt'), ['int'])),
                            ('l2x_lpts_pa_stats_bind_time', (YLeaf(YType.uint32, 'l2x-lpts-pa-stats-bind-time'), ['int'])),
                            ('l2x_lpts_pa_stats_expire_cnt', (YLeaf(YType.uint32, 'l2x-lpts-pa-stats-expire-cnt'), ['int'])),
                            ('l2x_lpts_pa_stats_replay_cnt', (YLeaf(YType.uint32, 'l2x-lpts-pa-stats-replay-cnt'), ['int'])),
                            ('l2x_lpts_pa_stats_replay_batch_cnt', (YLeaf(YType.uint32, 'l2x-lpts-pa-stats-replay-batch-cnt'), ['int'])),
                            ('l2x_lpts_pa_stats_replay_time', (YLeaf(YType.uint32, 'l2x-lpts-pa-stats-replay-time'), ['int'])),
                        ])
                        self.l2tp_sh_l2x_num_tunnels = None
                        self.l2tp_sh_l2x_num_sessions = None
                        self.l2tp_sh_l2x_rx_high_water_mark = None
                        self.l2tp_sh_l2x_ave_msg_process_usecs = None
                        self.l2tp_sh_l2x_num_rx_msgs = None
                        self.l2tp_sh_l2x_num_tx_msgs = None
                        self.l2tp_sh_l2x_num_tx_err_drops = None
                        self.l2tp_sh_l2x_num_tx_conn_drops = None
                        self.l2tp_sh_l2x_num_reordered_msgs = None
                        self.l2tp_sh_l2x_max_reorder_deviation = None
                        self.l2tp_sh_l2x_num_ooo_msgs = None
                        self.l2tp_sh_l2x_num_rx_path_drops = None
                        self.l2tp_sh_l2x_num_rx_path_data_pkt_drops = None
                        self.l2tp_sh_l2x_num_rx_queue_drops = None
                        self.l2tp_sh_l2x_num_rx_ooo_drops = None
                        self.l2tp_sh_l2x_num_buffered_msgs = None
                        self.l2tp_sh_l2x_num_mutex_block = None
                        self.l2tp_sh_l2x_num_bad_len_drops = None
                        self.l2tp_sh_l2x_num_bad_avp_drops = None
                        self.l2tp_sh_l2x_num_missing_cc_id_drops = None
                        self.l2tp_sh_l2x_num_missing_sess_id_drops = None
                        self.l2tp_sh_l2x_num_mismatch_cc_id_drops = None
                        self.l2tp_sh_l2x_num_unknown_cc_drops = None
                        self.l2tp_sh_l2x_num_unknown_sess_drops = None
                        self.l2tp_sh_l2x_num_linear_id_search = None
                        self.l2tp_sh_l2x_num_linear_id_search_fail = None
                        self.l2tp_sh_l2x_num_netio_pkt_rx = None
                        self.l2tp_sh_l2tun_ave_msg_process_usecs = None
                        self.l2tp_sh_l2tun_num_rx_msgs = None
                        self.l2tp_sh_l2tun_num_tx_msgs = None
                        self.l2tp_l2tun_socket_ens_send_error_cnt = None
                        self.l2tp_l2tun_socket_session_accept = None
                        self.l2tp_l2tun_socket_session_destroy = None
                        self.l2tp_l2tun_socket_session_connect = None
                        self.l2tp_l2tun_socket_session_connect_continue = None
                        self.l2tp_l2tun_session_connecting = None
                        self.l2tp_l2tun_session_connected = None
                        self.l2tp_l2tun_session_disconnected = None
                        self.l2tp_l2tun_session_incoming = None
                        self.l2tp_l2tun_session_updated = None
                        self.l2tp_l2tun_session_circuit_status = None
                        self.l2x_lpts_pa_stats_setup_cnt = None
                        self.l2x_lpts_pa_stats_destroy_cnt = None
                        self.l2x_lpts_pa_stats_alloc_cnt = None
                        self.l2x_lpts_pa_stats_alloc_fail_cnt = None
                        self.l2x_lpts_pa_stats_init_cnt = None
                        self.l2x_lpts_pa_stats_init_fail_cnt = None
                        self.l2x_lpts_pa_stats_free_cnt = None
                        self.l2x_lpts_pa_stats_pulse_cnt = None
                        self.l2x_lpts_pa_stats_pulse_fail_cnt = None
                        self.l2x_lpts_pa_stats_bind_cnt = None
                        self.l2x_lpts_pa_stats_bind_fail_cnt = None
                        self.l2x_lpts_pa_stats_bind_batch_cnt = None
                        self.l2x_lpts_pa_stats_bind_batch_fail_cnt = None
                        self.l2x_lpts_pa_stats_bind_time = None
                        self.l2x_lpts_pa_stats_expire_cnt = None
                        self.l2x_lpts_pa_stats_replay_cnt = None
                        self.l2x_lpts_pa_stats_replay_batch_cnt = None
                        self.l2x_lpts_pa_stats_replay_time = None
                        self._segment_path = lambda: "internal-stats-last-clear"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2tp.Nodes.Node.Internal.InternalStatsLastClear, ['l2tp_sh_l2x_num_tunnels', 'l2tp_sh_l2x_num_sessions', 'l2tp_sh_l2x_rx_high_water_mark', 'l2tp_sh_l2x_ave_msg_process_usecs', 'l2tp_sh_l2x_num_rx_msgs', 'l2tp_sh_l2x_num_tx_msgs', 'l2tp_sh_l2x_num_tx_err_drops', 'l2tp_sh_l2x_num_tx_conn_drops', 'l2tp_sh_l2x_num_reordered_msgs', 'l2tp_sh_l2x_max_reorder_deviation', 'l2tp_sh_l2x_num_ooo_msgs', 'l2tp_sh_l2x_num_rx_path_drops', 'l2tp_sh_l2x_num_rx_path_data_pkt_drops', 'l2tp_sh_l2x_num_rx_queue_drops', 'l2tp_sh_l2x_num_rx_ooo_drops', 'l2tp_sh_l2x_num_buffered_msgs', 'l2tp_sh_l2x_num_mutex_block', 'l2tp_sh_l2x_num_bad_len_drops', 'l2tp_sh_l2x_num_bad_avp_drops', 'l2tp_sh_l2x_num_missing_cc_id_drops', 'l2tp_sh_l2x_num_missing_sess_id_drops', 'l2tp_sh_l2x_num_mismatch_cc_id_drops', 'l2tp_sh_l2x_num_unknown_cc_drops', 'l2tp_sh_l2x_num_unknown_sess_drops', 'l2tp_sh_l2x_num_linear_id_search', 'l2tp_sh_l2x_num_linear_id_search_fail', 'l2tp_sh_l2x_num_netio_pkt_rx', 'l2tp_sh_l2tun_ave_msg_process_usecs', 'l2tp_sh_l2tun_num_rx_msgs', 'l2tp_sh_l2tun_num_tx_msgs', 'l2tp_l2tun_socket_ens_send_error_cnt', 'l2tp_l2tun_socket_session_accept', 'l2tp_l2tun_socket_session_destroy', 'l2tp_l2tun_socket_session_connect', 'l2tp_l2tun_socket_session_connect_continue', 'l2tp_l2tun_session_connecting', 'l2tp_l2tun_session_connected', 'l2tp_l2tun_session_disconnected', 'l2tp_l2tun_session_incoming', 'l2tp_l2tun_session_updated', 'l2tp_l2tun_session_circuit_status', 'l2x_lpts_pa_stats_setup_cnt', 'l2x_lpts_pa_stats_destroy_cnt', 'l2x_lpts_pa_stats_alloc_cnt', 'l2x_lpts_pa_stats_alloc_fail_cnt', 'l2x_lpts_pa_stats_init_cnt', 'l2x_lpts_pa_stats_init_fail_cnt', 'l2x_lpts_pa_stats_free_cnt', 'l2x_lpts_pa_stats_pulse_cnt', 'l2x_lpts_pa_stats_pulse_fail_cnt', 'l2x_lpts_pa_stats_bind_cnt', 'l2x_lpts_pa_stats_bind_fail_cnt', 'l2x_lpts_pa_stats_bind_batch_cnt', 'l2x_lpts_pa_stats_bind_batch_fail_cnt', 'l2x_lpts_pa_stats_bind_time', 'l2x_lpts_pa_stats_expire_cnt', 'l2x_lpts_pa_stats_replay_cnt', 'l2x_lpts_pa_stats_replay_batch_cnt', 'l2x_lpts_pa_stats_replay_time'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                        return meta._meta_table['L2tp.Nodes.Node.Internal.InternalStatsLastClear']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                    return meta._meta_table['L2tp.Nodes.Node.Internal']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                return meta._meta_table['L2tp.Nodes.Node']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
            return meta._meta_table['L2tp.Nodes']['meta_info']

    def clone_ptr(self):
        self._top_entity = L2tp()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
        return meta._meta_table['L2tp']['meta_info']


class L2tpv2(_Entity_):
    """
    l2tpv2
    
    .. attribute:: nodes
    
    	List of nodes for which subscriber data is collected
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Nodes>`
    
    	**config**\: False
    
    

    """

    _prefix = 'tunnel-l2tun-oper'
    _revision = '2018-11-01'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(L2tpv2, self).__init__()
        self._top_entity = None

        self.yang_name = "l2tpv2"
        self.yang_parent_name = "Cisco-IOS-XR-tunnel-l2tun-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("nodes", ("nodes", L2tpv2.Nodes))])
        self._leafs = OrderedDict()

        self.nodes = L2tpv2.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._segment_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(L2tpv2, [], name, value)


    class Nodes(_Entity_):
        """
        List of nodes for which subscriber data is
        collected
        
        .. attribute:: node
        
        	Subscriber data for a particular node
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Nodes.Node>`
        
        	**config**\: False
        
        

        """

        _prefix = 'tunnel-l2tun-oper'
        _revision = '2018-11-01'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(L2tpv2.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "l2tpv2"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("node", ("node", L2tpv2.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(L2tpv2.Nodes, [], name, value)


        class Node(_Entity_):
            """
            Subscriber data for a particular node
            
            .. attribute:: node_name  (key)
            
            	Node name
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            	**config**\: False
            
            .. attribute:: counters
            
            	L2TP control messages counters
            	**type**\:  :py:class:`Counters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Nodes.Node.Counters>`
            
            	**config**\: False
            
            .. attribute:: statistics
            
            	L2TP v2 statistics information
            	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Nodes.Node.Statistics>`
            
            	**config**\: False
            
            .. attribute:: tunnel
            
            	L2TPv2 tunnel 
            	**type**\:  :py:class:`Tunnel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Nodes.Node.Tunnel>`
            
            	**config**\: False
            
            .. attribute:: tunnel_configurations
            
            	List of tunnel IDs
            	**type**\:  :py:class:`TunnelConfigurations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Nodes.Node.TunnelConfigurations>`
            
            	**config**\: False
            
            .. attribute:: counter_hist_fail
            
            	Failure events leading to disconnection
            	**type**\:  :py:class:`CounterHistFail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Nodes.Node.CounterHistFail>`
            
            	**config**\: False
            
            .. attribute:: classes
            
            	List of L2TP class names
            	**type**\:  :py:class:`Classes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Nodes.Node.Classes>`
            
            	**config**\: False
            
            .. attribute:: tunnels
            
            	List of tunnel IDs
            	**type**\:  :py:class:`Tunnels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Nodes.Node.Tunnels>`
            
            	**config**\: False
            
            .. attribute:: sessions
            
            	List of session IDs
            	**type**\:  :py:class:`Sessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Nodes.Node.Sessions>`
            
            	**config**\: False
            
            .. attribute:: session
            
            	L2TP control messages counters
            	**type**\:  :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Nodes.Node.Session>`
            
            	**config**\: False
            
            .. attribute:: internal
            
            	L2TP v2/v3 internal information
            	**type**\:  :py:class:`Internal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Nodes.Node.Internal>`
            
            	**config**\: False
            
            

            """

            _prefix = 'tunnel-l2tun-oper'
            _revision = '2018-11-01'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(L2tpv2.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_classes = OrderedDict([("counters", ("counters", L2tpv2.Nodes.Node.Counters)), ("statistics", ("statistics", L2tpv2.Nodes.Node.Statistics)), ("tunnel", ("tunnel", L2tpv2.Nodes.Node.Tunnel)), ("tunnel-configurations", ("tunnel_configurations", L2tpv2.Nodes.Node.TunnelConfigurations)), ("counter-hist-fail", ("counter_hist_fail", L2tpv2.Nodes.Node.CounterHistFail)), ("classes", ("classes", L2tpv2.Nodes.Node.Classes)), ("tunnels", ("tunnels", L2tpv2.Nodes.Node.Tunnels)), ("sessions", ("sessions", L2tpv2.Nodes.Node.Sessions)), ("session", ("session", L2tpv2.Nodes.Node.Session)), ("internal", ("internal", L2tpv2.Nodes.Node.Internal))])
                self._leafs = OrderedDict([
                    ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                ])
                self.node_name = None

                self.counters = L2tpv2.Nodes.Node.Counters()
                self.counters.parent = self
                self._children_name_map["counters"] = "counters"

                self.statistics = L2tpv2.Nodes.Node.Statistics()
                self.statistics.parent = self
                self._children_name_map["statistics"] = "statistics"

                self.tunnel = L2tpv2.Nodes.Node.Tunnel()
                self.tunnel.parent = self
                self._children_name_map["tunnel"] = "tunnel"

                self.tunnel_configurations = L2tpv2.Nodes.Node.TunnelConfigurations()
                self.tunnel_configurations.parent = self
                self._children_name_map["tunnel_configurations"] = "tunnel-configurations"

                self.counter_hist_fail = L2tpv2.Nodes.Node.CounterHistFail()
                self.counter_hist_fail.parent = self
                self._children_name_map["counter_hist_fail"] = "counter-hist-fail"

                self.classes = L2tpv2.Nodes.Node.Classes()
                self.classes.parent = self
                self._children_name_map["classes"] = "classes"

                self.tunnels = L2tpv2.Nodes.Node.Tunnels()
                self.tunnels.parent = self
                self._children_name_map["tunnels"] = "tunnels"

                self.sessions = L2tpv2.Nodes.Node.Sessions()
                self.sessions.parent = self
                self._children_name_map["sessions"] = "sessions"

                self.session = L2tpv2.Nodes.Node.Session()
                self.session.parent = self
                self._children_name_map["session"] = "session"

                self.internal = L2tpv2.Nodes.Node.Internal()
                self.internal.parent = self
                self._children_name_map["internal"] = "internal"
                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/nodes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(L2tpv2.Nodes.Node, ['node_name'], name, value)


            class Counters(_Entity_):
                """
                L2TP control messages counters
                
                .. attribute:: forwarding
                
                	L2TP forwarding messages counters
                	**type**\:  :py:class:`Forwarding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Nodes.Node.Counters.Forwarding>`
                
                	**config**\: False
                
                .. attribute:: control
                
                	L2TP control messages counters
                	**type**\:  :py:class:`Control <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Nodes.Node.Counters.Control>`
                
                	**config**\: False
                
                

                """

                _prefix = 'tunnel-l2tun-oper'
                _revision = '2018-11-01'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(L2tpv2.Nodes.Node.Counters, self).__init__()

                    self.yang_name = "counters"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("forwarding", ("forwarding", L2tpv2.Nodes.Node.Counters.Forwarding)), ("control", ("control", L2tpv2.Nodes.Node.Counters.Control))])
                    self._leafs = OrderedDict()

                    self.forwarding = L2tpv2.Nodes.Node.Counters.Forwarding()
                    self.forwarding.parent = self
                    self._children_name_map["forwarding"] = "forwarding"

                    self.control = L2tpv2.Nodes.Node.Counters.Control()
                    self.control.parent = self
                    self._children_name_map["control"] = "control"
                    self._segment_path = lambda: "counters"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(L2tpv2.Nodes.Node.Counters, [], name, value)


                class Forwarding(_Entity_):
                    """
                    L2TP forwarding messages counters
                    
                    .. attribute:: sessions
                    
                    	List of class and session IDs
                    	**type**\:  :py:class:`Sessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Nodes.Node.Counters.Forwarding.Sessions>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'tunnel-l2tun-oper'
                    _revision = '2018-11-01'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(L2tpv2.Nodes.Node.Counters.Forwarding, self).__init__()

                        self.yang_name = "forwarding"
                        self.yang_parent_name = "counters"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("sessions", ("sessions", L2tpv2.Nodes.Node.Counters.Forwarding.Sessions))])
                        self._leafs = OrderedDict()

                        self.sessions = L2tpv2.Nodes.Node.Counters.Forwarding.Sessions()
                        self.sessions.parent = self
                        self._children_name_map["sessions"] = "sessions"
                        self._segment_path = lambda: "forwarding"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2tpv2.Nodes.Node.Counters.Forwarding, [], name, value)


                    class Sessions(_Entity_):
                        """
                        List of class and session IDs
                        
                        .. attribute:: session
                        
                        	L2TP information for a particular session
                        	**type**\: list of  		 :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Nodes.Node.Counters.Forwarding.Sessions.Session>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'tunnel-l2tun-oper'
                        _revision = '2018-11-01'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(L2tpv2.Nodes.Node.Counters.Forwarding.Sessions, self).__init__()

                            self.yang_name = "sessions"
                            self.yang_parent_name = "forwarding"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("session", ("session", L2tpv2.Nodes.Node.Counters.Forwarding.Sessions.Session))])
                            self._leafs = OrderedDict()

                            self.session = YList(self)
                            self._segment_path = lambda: "sessions"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2tpv2.Nodes.Node.Counters.Forwarding.Sessions, [], name, value)


                        class Session(_Entity_):
                            """
                            L2TP information for a particular session
                            
                            .. attribute:: tunnel_id  (key)
                            
                            	Local tunnel ID
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: session_id  (key)
                            
                            	Local session ID
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: remote_session_id
                            
                            	Remote session ID
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: in_packets
                            
                            	Number of packets sent in
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: out_packets
                            
                            	Number of packets sent out
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: in_bytes
                            
                            	Number of bytes sent in
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            	**units**\: byte
                            
                            .. attribute:: out_bytes
                            
                            	Number of bytes sent out
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'tunnel-l2tun-oper'
                            _revision = '2018-11-01'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(L2tpv2.Nodes.Node.Counters.Forwarding.Sessions.Session, self).__init__()

                                self.yang_name = "session"
                                self.yang_parent_name = "sessions"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
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
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2tpv2.Nodes.Node.Counters.Forwarding.Sessions.Session, ['tunnel_id', 'session_id', 'remote_session_id', 'in_packets', 'out_packets', 'in_bytes', 'out_bytes'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                                return meta._meta_table['L2tpv2.Nodes.Node.Counters.Forwarding.Sessions.Session']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                            return meta._meta_table['L2tpv2.Nodes.Node.Counters.Forwarding.Sessions']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                        return meta._meta_table['L2tpv2.Nodes.Node.Counters.Forwarding']['meta_info']


                class Control(_Entity_):
                    """
                    L2TP control messages counters
                    
                    .. attribute:: tunnel_xr
                    
                    	L2TP control tunnel messages counters
                    	**type**\:  :py:class:`TunnelXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Nodes.Node.Counters.Control.TunnelXr>`
                    
                    	**config**\: False
                    
                    .. attribute:: tunnels
                    
                    	Table of tunnel IDs of control message counters
                    	**type**\:  :py:class:`Tunnels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Nodes.Node.Counters.Control.Tunnels>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'tunnel-l2tun-oper'
                    _revision = '2018-11-01'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(L2tpv2.Nodes.Node.Counters.Control, self).__init__()

                        self.yang_name = "control"
                        self.yang_parent_name = "counters"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("tunnel-xr", ("tunnel_xr", L2tpv2.Nodes.Node.Counters.Control.TunnelXr)), ("tunnels", ("tunnels", L2tpv2.Nodes.Node.Counters.Control.Tunnels))])
                        self._leafs = OrderedDict()

                        self.tunnel_xr = L2tpv2.Nodes.Node.Counters.Control.TunnelXr()
                        self.tunnel_xr.parent = self
                        self._children_name_map["tunnel_xr"] = "tunnel-xr"

                        self.tunnels = L2tpv2.Nodes.Node.Counters.Control.Tunnels()
                        self.tunnels.parent = self
                        self._children_name_map["tunnels"] = "tunnels"
                        self._segment_path = lambda: "control"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2tpv2.Nodes.Node.Counters.Control, [], name, value)


                    class TunnelXr(_Entity_):
                        """
                        L2TP control tunnel messages counters
                        
                        .. attribute:: authentication
                        
                        	Tunnel authentication counters
                        	**type**\:  :py:class:`Authentication <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Authentication>`
                        
                        	**config**\: False
                        
                        .. attribute:: global_
                        
                        	Tunnel counters
                        	**type**\:  :py:class:`Global <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Global>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'tunnel-l2tun-oper'
                        _revision = '2018-11-01'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(L2tpv2.Nodes.Node.Counters.Control.TunnelXr, self).__init__()

                            self.yang_name = "tunnel-xr"
                            self.yang_parent_name = "control"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("authentication", ("authentication", L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Authentication)), ("global", ("global_", L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Global))])
                            self._leafs = OrderedDict()

                            self.authentication = L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Authentication()
                            self.authentication.parent = self
                            self._children_name_map["authentication"] = "authentication"

                            self.global_ = L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Global()
                            self.global_.parent = self
                            self._children_name_map["global_"] = "global"
                            self._segment_path = lambda: "tunnel-xr"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2tpv2.Nodes.Node.Counters.Control.TunnelXr, [], name, value)


                        class Authentication(_Entity_):
                            """
                            Tunnel authentication counters
                            
                            .. attribute:: nonce_avp
                            
                            	Nonce AVP statistics
                            	**type**\:  :py:class:`NonceAvp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Authentication.NonceAvp>`
                            
                            	**config**\: False
                            
                            .. attribute:: common_digest
                            
                            	Common digest statistics
                            	**type**\:  :py:class:`CommonDigest <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Authentication.CommonDigest>`
                            
                            	**config**\: False
                            
                            .. attribute:: primary_digest
                            
                            	Primary digest statistics
                            	**type**\:  :py:class:`PrimaryDigest <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Authentication.PrimaryDigest>`
                            
                            	**config**\: False
                            
                            .. attribute:: secondary_digest
                            
                            	Secondary digest statistics
                            	**type**\:  :py:class:`SecondaryDigest <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Authentication.SecondaryDigest>`
                            
                            	**config**\: False
                            
                            .. attribute:: integrity_check
                            
                            	Integrity check statistics
                            	**type**\:  :py:class:`IntegrityCheck <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Authentication.IntegrityCheck>`
                            
                            	**config**\: False
                            
                            .. attribute:: local_secret
                            
                            	Local secret statistics
                            	**type**\:  :py:class:`LocalSecret <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Authentication.LocalSecret>`
                            
                            	**config**\: False
                            
                            .. attribute:: challenge_avp
                            
                            	Challenge AVP statistics
                            	**type**\:  :py:class:`ChallengeAvp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Authentication.ChallengeAvp>`
                            
                            	**config**\: False
                            
                            .. attribute:: challenge_reponse
                            
                            	Challenge response statistics
                            	**type**\:  :py:class:`ChallengeReponse <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Authentication.ChallengeReponse>`
                            
                            	**config**\: False
                            
                            .. attribute:: overall_statistics
                            
                            	Overall statistics
                            	**type**\:  :py:class:`OverallStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Authentication.OverallStatistics>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'tunnel-l2tun-oper'
                            _revision = '2018-11-01'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Authentication, self).__init__()

                                self.yang_name = "authentication"
                                self.yang_parent_name = "tunnel-xr"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("nonce-avp", ("nonce_avp", L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Authentication.NonceAvp)), ("common-digest", ("common_digest", L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Authentication.CommonDigest)), ("primary-digest", ("primary_digest", L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Authentication.PrimaryDigest)), ("secondary-digest", ("secondary_digest", L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Authentication.SecondaryDigest)), ("integrity-check", ("integrity_check", L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Authentication.IntegrityCheck)), ("local-secret", ("local_secret", L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Authentication.LocalSecret)), ("challenge-avp", ("challenge_avp", L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Authentication.ChallengeAvp)), ("challenge-reponse", ("challenge_reponse", L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Authentication.ChallengeReponse)), ("overall-statistics", ("overall_statistics", L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Authentication.OverallStatistics))])
                                self._leafs = OrderedDict()

                                self.nonce_avp = L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Authentication.NonceAvp()
                                self.nonce_avp.parent = self
                                self._children_name_map["nonce_avp"] = "nonce-avp"

                                self.common_digest = L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Authentication.CommonDigest()
                                self.common_digest.parent = self
                                self._children_name_map["common_digest"] = "common-digest"

                                self.primary_digest = L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Authentication.PrimaryDigest()
                                self.primary_digest.parent = self
                                self._children_name_map["primary_digest"] = "primary-digest"

                                self.secondary_digest = L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Authentication.SecondaryDigest()
                                self.secondary_digest.parent = self
                                self._children_name_map["secondary_digest"] = "secondary-digest"

                                self.integrity_check = L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Authentication.IntegrityCheck()
                                self.integrity_check.parent = self
                                self._children_name_map["integrity_check"] = "integrity-check"

                                self.local_secret = L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Authentication.LocalSecret()
                                self.local_secret.parent = self
                                self._children_name_map["local_secret"] = "local-secret"

                                self.challenge_avp = L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Authentication.ChallengeAvp()
                                self.challenge_avp.parent = self
                                self._children_name_map["challenge_avp"] = "challenge-avp"

                                self.challenge_reponse = L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Authentication.ChallengeReponse()
                                self.challenge_reponse.parent = self
                                self._children_name_map["challenge_reponse"] = "challenge-reponse"

                                self.overall_statistics = L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Authentication.OverallStatistics()
                                self.overall_statistics.parent = self
                                self._children_name_map["overall_statistics"] = "overall-statistics"
                                self._segment_path = lambda: "authentication"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Authentication, [], name, value)


                            class NonceAvp(_Entity_):
                                """
                                Nonce AVP statistics
                                
                                .. attribute:: validate
                                
                                	Validate
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: bad_hash
                                
                                	Bad hash
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: bad_length
                                
                                	Bad length
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: ignored
                                
                                	Ignored
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: missing
                                
                                	Missing
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: passed
                                
                                	Passed
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: failed
                                
                                	Failed
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: skipped
                                
                                	Skipped
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: generate_response_failures
                                
                                	Generate response fail
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: unexpected
                                
                                	Unexpected
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: unexpected_zlb
                                
                                	Unexpected ZLB
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'tunnel-l2tun-oper'
                                _revision = '2018-11-01'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Authentication.NonceAvp, self).__init__()

                                    self.yang_name = "nonce-avp"
                                    self.yang_parent_name = "authentication"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
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
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Authentication.NonceAvp, ['validate', 'bad_hash', 'bad_length', 'ignored', 'missing', 'passed', 'failed', 'skipped', 'generate_response_failures', 'unexpected', 'unexpected_zlb'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                                    return meta._meta_table['L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Authentication.NonceAvp']['meta_info']


                            class CommonDigest(_Entity_):
                                """
                                Common digest statistics
                                
                                .. attribute:: validate
                                
                                	Validate
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: bad_hash
                                
                                	Bad hash
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: bad_length
                                
                                	Bad length
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: ignored
                                
                                	Ignored
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: missing
                                
                                	Missing
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: passed
                                
                                	Passed
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: failed
                                
                                	Failed
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: skipped
                                
                                	Skipped
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: generate_response_failures
                                
                                	Generate response fail
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: unexpected
                                
                                	Unexpected
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: unexpected_zlb
                                
                                	Unexpected ZLB
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'tunnel-l2tun-oper'
                                _revision = '2018-11-01'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Authentication.CommonDigest, self).__init__()

                                    self.yang_name = "common-digest"
                                    self.yang_parent_name = "authentication"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
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
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Authentication.CommonDigest, ['validate', 'bad_hash', 'bad_length', 'ignored', 'missing', 'passed', 'failed', 'skipped', 'generate_response_failures', 'unexpected', 'unexpected_zlb'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                                    return meta._meta_table['L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Authentication.CommonDigest']['meta_info']


                            class PrimaryDigest(_Entity_):
                                """
                                Primary digest statistics
                                
                                .. attribute:: validate
                                
                                	Validate
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: bad_hash
                                
                                	Bad hash
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: bad_length
                                
                                	Bad length
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: ignored
                                
                                	Ignored
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: missing
                                
                                	Missing
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: passed
                                
                                	Passed
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: failed
                                
                                	Failed
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: skipped
                                
                                	Skipped
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: generate_response_failures
                                
                                	Generate response fail
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: unexpected
                                
                                	Unexpected
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: unexpected_zlb
                                
                                	Unexpected ZLB
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'tunnel-l2tun-oper'
                                _revision = '2018-11-01'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Authentication.PrimaryDigest, self).__init__()

                                    self.yang_name = "primary-digest"
                                    self.yang_parent_name = "authentication"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
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
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Authentication.PrimaryDigest, ['validate', 'bad_hash', 'bad_length', 'ignored', 'missing', 'passed', 'failed', 'skipped', 'generate_response_failures', 'unexpected', 'unexpected_zlb'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                                    return meta._meta_table['L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Authentication.PrimaryDigest']['meta_info']


                            class SecondaryDigest(_Entity_):
                                """
                                Secondary digest statistics
                                
                                .. attribute:: validate
                                
                                	Validate
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: bad_hash
                                
                                	Bad hash
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: bad_length
                                
                                	Bad length
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: ignored
                                
                                	Ignored
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: missing
                                
                                	Missing
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: passed
                                
                                	Passed
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: failed
                                
                                	Failed
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: skipped
                                
                                	Skipped
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: generate_response_failures
                                
                                	Generate response fail
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: unexpected
                                
                                	Unexpected
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: unexpected_zlb
                                
                                	Unexpected ZLB
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'tunnel-l2tun-oper'
                                _revision = '2018-11-01'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Authentication.SecondaryDigest, self).__init__()

                                    self.yang_name = "secondary-digest"
                                    self.yang_parent_name = "authentication"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
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
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Authentication.SecondaryDigest, ['validate', 'bad_hash', 'bad_length', 'ignored', 'missing', 'passed', 'failed', 'skipped', 'generate_response_failures', 'unexpected', 'unexpected_zlb'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                                    return meta._meta_table['L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Authentication.SecondaryDigest']['meta_info']


                            class IntegrityCheck(_Entity_):
                                """
                                Integrity check statistics
                                
                                .. attribute:: validate
                                
                                	Validate
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: bad_hash
                                
                                	Bad hash
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: bad_length
                                
                                	Bad length
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: ignored
                                
                                	Ignored
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: missing
                                
                                	Missing
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: passed
                                
                                	Passed
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: failed
                                
                                	Failed
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: skipped
                                
                                	Skipped
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: generate_response_failures
                                
                                	Generate response fail
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: unexpected
                                
                                	Unexpected
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: unexpected_zlb
                                
                                	Unexpected ZLB
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'tunnel-l2tun-oper'
                                _revision = '2018-11-01'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Authentication.IntegrityCheck, self).__init__()

                                    self.yang_name = "integrity-check"
                                    self.yang_parent_name = "authentication"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
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
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Authentication.IntegrityCheck, ['validate', 'bad_hash', 'bad_length', 'ignored', 'missing', 'passed', 'failed', 'skipped', 'generate_response_failures', 'unexpected', 'unexpected_zlb'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                                    return meta._meta_table['L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Authentication.IntegrityCheck']['meta_info']


                            class LocalSecret(_Entity_):
                                """
                                Local secret statistics
                                
                                .. attribute:: validate
                                
                                	Validate
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: bad_hash
                                
                                	Bad hash
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: bad_length
                                
                                	Bad length
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: ignored
                                
                                	Ignored
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: missing
                                
                                	Missing
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: passed
                                
                                	Passed
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: failed
                                
                                	Failed
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: skipped
                                
                                	Skipped
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: generate_response_failures
                                
                                	Generate response fail
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: unexpected
                                
                                	Unexpected
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: unexpected_zlb
                                
                                	Unexpected ZLB
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'tunnel-l2tun-oper'
                                _revision = '2018-11-01'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Authentication.LocalSecret, self).__init__()

                                    self.yang_name = "local-secret"
                                    self.yang_parent_name = "authentication"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
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
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Authentication.LocalSecret, ['validate', 'bad_hash', 'bad_length', 'ignored', 'missing', 'passed', 'failed', 'skipped', 'generate_response_failures', 'unexpected', 'unexpected_zlb'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                                    return meta._meta_table['L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Authentication.LocalSecret']['meta_info']


                            class ChallengeAvp(_Entity_):
                                """
                                Challenge AVP statistics
                                
                                .. attribute:: validate
                                
                                	Validate
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: bad_hash
                                
                                	Bad hash
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: bad_length
                                
                                	Bad length
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: ignored
                                
                                	Ignored
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: missing
                                
                                	Missing
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: passed
                                
                                	Passed
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: failed
                                
                                	Failed
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: skipped
                                
                                	Skipped
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: generate_response_failures
                                
                                	Generate response fail
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: unexpected
                                
                                	Unexpected
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: unexpected_zlb
                                
                                	Unexpected ZLB
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'tunnel-l2tun-oper'
                                _revision = '2018-11-01'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Authentication.ChallengeAvp, self).__init__()

                                    self.yang_name = "challenge-avp"
                                    self.yang_parent_name = "authentication"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
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
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Authentication.ChallengeAvp, ['validate', 'bad_hash', 'bad_length', 'ignored', 'missing', 'passed', 'failed', 'skipped', 'generate_response_failures', 'unexpected', 'unexpected_zlb'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                                    return meta._meta_table['L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Authentication.ChallengeAvp']['meta_info']


                            class ChallengeReponse(_Entity_):
                                """
                                Challenge response statistics
                                
                                .. attribute:: validate
                                
                                	Validate
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: bad_hash
                                
                                	Bad hash
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: bad_length
                                
                                	Bad length
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: ignored
                                
                                	Ignored
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: missing
                                
                                	Missing
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: passed
                                
                                	Passed
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: failed
                                
                                	Failed
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: skipped
                                
                                	Skipped
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: generate_response_failures
                                
                                	Generate response fail
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: unexpected
                                
                                	Unexpected
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: unexpected_zlb
                                
                                	Unexpected ZLB
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'tunnel-l2tun-oper'
                                _revision = '2018-11-01'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Authentication.ChallengeReponse, self).__init__()

                                    self.yang_name = "challenge-reponse"
                                    self.yang_parent_name = "authentication"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
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
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Authentication.ChallengeReponse, ['validate', 'bad_hash', 'bad_length', 'ignored', 'missing', 'passed', 'failed', 'skipped', 'generate_response_failures', 'unexpected', 'unexpected_zlb'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                                    return meta._meta_table['L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Authentication.ChallengeReponse']['meta_info']


                            class OverallStatistics(_Entity_):
                                """
                                Overall statistics
                                
                                .. attribute:: validate
                                
                                	Validate
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: bad_hash
                                
                                	Bad hash
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: bad_length
                                
                                	Bad length
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: ignored
                                
                                	Ignored
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: missing
                                
                                	Missing
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: passed
                                
                                	Passed
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: failed
                                
                                	Failed
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: skipped
                                
                                	Skipped
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: generate_response_failures
                                
                                	Generate response fail
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: unexpected
                                
                                	Unexpected
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: unexpected_zlb
                                
                                	Unexpected ZLB
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'tunnel-l2tun-oper'
                                _revision = '2018-11-01'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Authentication.OverallStatistics, self).__init__()

                                    self.yang_name = "overall-statistics"
                                    self.yang_parent_name = "authentication"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
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
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Authentication.OverallStatistics, ['validate', 'bad_hash', 'bad_length', 'ignored', 'missing', 'passed', 'failed', 'skipped', 'generate_response_failures', 'unexpected', 'unexpected_zlb'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                                    return meta._meta_table['L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Authentication.OverallStatistics']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                                return meta._meta_table['L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Authentication']['meta_info']


                        class Global(_Entity_):
                            """
                            Tunnel counters
                            
                            .. attribute:: transmit
                            
                            	Transmit data
                            	**type**\:  :py:class:`Transmit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Global.Transmit>`
                            
                            	**config**\: False
                            
                            .. attribute:: retransmit
                            
                            	Re transmit data
                            	**type**\:  :py:class:`Retransmit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Global.Retransmit>`
                            
                            	**config**\: False
                            
                            .. attribute:: received
                            
                            	Received data
                            	**type**\:  :py:class:`Received <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Global.Received>`
                            
                            	**config**\: False
                            
                            .. attribute:: drop
                            
                            	Drop data
                            	**type**\:  :py:class:`Drop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Global.Drop>`
                            
                            	**config**\: False
                            
                            .. attribute:: total_transmit
                            
                            	Total transmit
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: total_retransmit
                            
                            	Total retransmit
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: total_received
                            
                            	Total received
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: total_drop
                            
                            	Total drop
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'tunnel-l2tun-oper'
                            _revision = '2018-11-01'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Global, self).__init__()

                                self.yang_name = "global"
                                self.yang_parent_name = "tunnel-xr"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("transmit", ("transmit", L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Global.Transmit)), ("retransmit", ("retransmit", L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Global.Retransmit)), ("received", ("received", L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Global.Received)), ("drop", ("drop", L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Global.Drop))])
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

                                self.transmit = L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Global.Transmit()
                                self.transmit.parent = self
                                self._children_name_map["transmit"] = "transmit"

                                self.retransmit = L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Global.Retransmit()
                                self.retransmit.parent = self
                                self._children_name_map["retransmit"] = "retransmit"

                                self.received = L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Global.Received()
                                self.received.parent = self
                                self._children_name_map["received"] = "received"

                                self.drop = L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Global.Drop()
                                self.drop.parent = self
                                self._children_name_map["drop"] = "drop"
                                self._segment_path = lambda: "global"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Global, ['total_transmit', 'total_retransmit', 'total_received', 'total_drop'], name, value)


                            class Transmit(_Entity_):
                                """
                                Transmit data
                                
                                .. attribute:: unknown_packets
                                
                                	Unknown packets
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: zero_length_body_packets
                                
                                	Zero length body packets
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: start_control_connection_requests
                                
                                	Start control connection requests
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: start_control_connection_replies
                                
                                	Start control connection replies
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: start_control_connection_notifications
                                
                                	Start control connection notifications
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: stop_control_connection_notifications
                                
                                	Stop control connection notifications
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: hello_packets
                                
                                	Keep alive messages
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: outgoing_call_requests
                                
                                	Outgoing call requests
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: outgoing_call_replies
                                
                                	Outgoing call replies
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: outgoing_call_connected_packets
                                
                                	Outgoing call connected packets
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: incoming_call_requests
                                
                                	Incoming call requests
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: incoming_call_replies
                                
                                	Incoming call replies
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: incoming_call_connected_packets
                                
                                	Incoming call connected packets
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: call_disconnect_notify_packets
                                
                                	Call disconnect notify packets
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: wan_error_notify_packets
                                
                                	WAN error notify packets
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: set_link_info_packets
                                
                                	Set link info packets
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: service_relay_requests
                                
                                	Service relay request counts
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: service_relay_replies
                                
                                	Service relay reply counts
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: acknowledgement_packets
                                
                                	Packets acknowledgement
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'tunnel-l2tun-oper'
                                _revision = '2018-11-01'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Global.Transmit, self).__init__()

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
                                    self._perform_setattr(L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Global.Transmit, ['unknown_packets', 'zero_length_body_packets', 'start_control_connection_requests', 'start_control_connection_replies', 'start_control_connection_notifications', 'stop_control_connection_notifications', 'hello_packets', 'outgoing_call_requests', 'outgoing_call_replies', 'outgoing_call_connected_packets', 'incoming_call_requests', 'incoming_call_replies', 'incoming_call_connected_packets', 'call_disconnect_notify_packets', 'wan_error_notify_packets', 'set_link_info_packets', 'service_relay_requests', 'service_relay_replies', 'acknowledgement_packets'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                                    return meta._meta_table['L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Global.Transmit']['meta_info']


                            class Retransmit(_Entity_):
                                """
                                Re transmit data
                                
                                .. attribute:: unknown_packets
                                
                                	Unknown packets
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: zero_length_body_packets
                                
                                	Zero length body packets
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: start_control_connection_requests
                                
                                	Start control connection requests
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: start_control_connection_replies
                                
                                	Start control connection replies
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: start_control_connection_notifications
                                
                                	Start control connection notifications
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: stop_control_connection_notifications
                                
                                	Stop control connection notifications
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: hello_packets
                                
                                	Keep alive messages
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: outgoing_call_requests
                                
                                	Outgoing call requests
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: outgoing_call_replies
                                
                                	Outgoing call replies
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: outgoing_call_connected_packets
                                
                                	Outgoing call connected packets
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: incoming_call_requests
                                
                                	Incoming call requests
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: incoming_call_replies
                                
                                	Incoming call replies
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: incoming_call_connected_packets
                                
                                	Incoming call connected packets
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: call_disconnect_notify_packets
                                
                                	Call disconnect notify packets
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: wan_error_notify_packets
                                
                                	WAN error notify packets
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: set_link_info_packets
                                
                                	Set link info packets
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: service_relay_requests
                                
                                	Service relay request counts
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: service_relay_replies
                                
                                	Service relay reply counts
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: acknowledgement_packets
                                
                                	Packets acknowledgement
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'tunnel-l2tun-oper'
                                _revision = '2018-11-01'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Global.Retransmit, self).__init__()

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
                                    self._perform_setattr(L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Global.Retransmit, ['unknown_packets', 'zero_length_body_packets', 'start_control_connection_requests', 'start_control_connection_replies', 'start_control_connection_notifications', 'stop_control_connection_notifications', 'hello_packets', 'outgoing_call_requests', 'outgoing_call_replies', 'outgoing_call_connected_packets', 'incoming_call_requests', 'incoming_call_replies', 'incoming_call_connected_packets', 'call_disconnect_notify_packets', 'wan_error_notify_packets', 'set_link_info_packets', 'service_relay_requests', 'service_relay_replies', 'acknowledgement_packets'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                                    return meta._meta_table['L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Global.Retransmit']['meta_info']


                            class Received(_Entity_):
                                """
                                Received data
                                
                                .. attribute:: unknown_packets
                                
                                	Unknown packets
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: zero_length_body_packets
                                
                                	Zero length body packets
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: start_control_connection_requests
                                
                                	Start control connection requests
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: start_control_connection_replies
                                
                                	Start control connection replies
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: start_control_connection_notifications
                                
                                	Start control connection notifications
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: stop_control_connection_notifications
                                
                                	Stop control connection notifications
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: hello_packets
                                
                                	Keep alive messages
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: outgoing_call_requests
                                
                                	Outgoing call requests
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: outgoing_call_replies
                                
                                	Outgoing call replies
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: outgoing_call_connected_packets
                                
                                	Outgoing call connected packets
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: incoming_call_requests
                                
                                	Incoming call requests
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: incoming_call_replies
                                
                                	Incoming call replies
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: incoming_call_connected_packets
                                
                                	Incoming call connected packets
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: call_disconnect_notify_packets
                                
                                	Call disconnect notify packets
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: wan_error_notify_packets
                                
                                	WAN error notify packets
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: set_link_info_packets
                                
                                	Set link info packets
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: service_relay_requests
                                
                                	Service relay request counts
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: service_relay_replies
                                
                                	Service relay reply counts
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: acknowledgement_packets
                                
                                	Packets acknowledgement
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'tunnel-l2tun-oper'
                                _revision = '2018-11-01'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Global.Received, self).__init__()

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
                                    self._perform_setattr(L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Global.Received, ['unknown_packets', 'zero_length_body_packets', 'start_control_connection_requests', 'start_control_connection_replies', 'start_control_connection_notifications', 'stop_control_connection_notifications', 'hello_packets', 'outgoing_call_requests', 'outgoing_call_replies', 'outgoing_call_connected_packets', 'incoming_call_requests', 'incoming_call_replies', 'incoming_call_connected_packets', 'call_disconnect_notify_packets', 'wan_error_notify_packets', 'set_link_info_packets', 'service_relay_requests', 'service_relay_replies', 'acknowledgement_packets'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                                    return meta._meta_table['L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Global.Received']['meta_info']


                            class Drop(_Entity_):
                                """
                                Drop data
                                
                                .. attribute:: unknown_packets
                                
                                	Unknown packets
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: zero_length_body_packets
                                
                                	Zero length body packets
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: start_control_connection_requests
                                
                                	Start control connection requests
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: start_control_connection_replies
                                
                                	Start control connection replies
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: start_control_connection_notifications
                                
                                	Start control connection notifications
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: stop_control_connection_notifications
                                
                                	Stop control connection notifications
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: hello_packets
                                
                                	Keep alive messages
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: outgoing_call_requests
                                
                                	Outgoing call requests
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: outgoing_call_replies
                                
                                	Outgoing call replies
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: outgoing_call_connected_packets
                                
                                	Outgoing call connected packets
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: incoming_call_requests
                                
                                	Incoming call requests
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: incoming_call_replies
                                
                                	Incoming call replies
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: incoming_call_connected_packets
                                
                                	Incoming call connected packets
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: call_disconnect_notify_packets
                                
                                	Call disconnect notify packets
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: wan_error_notify_packets
                                
                                	WAN error notify packets
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: set_link_info_packets
                                
                                	Set link info packets
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: service_relay_requests
                                
                                	Service relay request counts
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: service_relay_replies
                                
                                	Service relay reply counts
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: acknowledgement_packets
                                
                                	Packets acknowledgement
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'tunnel-l2tun-oper'
                                _revision = '2018-11-01'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Global.Drop, self).__init__()

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
                                    self._perform_setattr(L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Global.Drop, ['unknown_packets', 'zero_length_body_packets', 'start_control_connection_requests', 'start_control_connection_replies', 'start_control_connection_notifications', 'stop_control_connection_notifications', 'hello_packets', 'outgoing_call_requests', 'outgoing_call_replies', 'outgoing_call_connected_packets', 'incoming_call_requests', 'incoming_call_replies', 'incoming_call_connected_packets', 'call_disconnect_notify_packets', 'wan_error_notify_packets', 'set_link_info_packets', 'service_relay_requests', 'service_relay_replies', 'acknowledgement_packets'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                                    return meta._meta_table['L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Global.Drop']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                                return meta._meta_table['L2tpv2.Nodes.Node.Counters.Control.TunnelXr.Global']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                            return meta._meta_table['L2tpv2.Nodes.Node.Counters.Control.TunnelXr']['meta_info']


                    class Tunnels(_Entity_):
                        """
                        Table of tunnel IDs of control message counters
                        
                        .. attribute:: tunnel
                        
                        	L2TP tunnel control message counters
                        	**type**\: list of  		 :py:class:`Tunnel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Nodes.Node.Counters.Control.Tunnels.Tunnel>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'tunnel-l2tun-oper'
                        _revision = '2018-11-01'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(L2tpv2.Nodes.Node.Counters.Control.Tunnels, self).__init__()

                            self.yang_name = "tunnels"
                            self.yang_parent_name = "control"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("tunnel", ("tunnel", L2tpv2.Nodes.Node.Counters.Control.Tunnels.Tunnel))])
                            self._leafs = OrderedDict()

                            self.tunnel = YList(self)
                            self._segment_path = lambda: "tunnels"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2tpv2.Nodes.Node.Counters.Control.Tunnels, [], name, value)


                        class Tunnel(_Entity_):
                            """
                            L2TP tunnel control message counters
                            
                            .. attribute:: tunnel_id  (key)
                            
                            	L2TP tunnel ID
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: brief
                            
                            	L2TP control message local and remote addresses
                            	**type**\:  :py:class:`Brief <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Nodes.Node.Counters.Control.Tunnels.Tunnel.Brief>`
                            
                            	**config**\: False
                            
                            .. attribute:: global_
                            
                            	Global data
                            	**type**\:  :py:class:`Global <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Nodes.Node.Counters.Control.Tunnels.Tunnel.Global>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'tunnel-l2tun-oper'
                            _revision = '2018-11-01'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(L2tpv2.Nodes.Node.Counters.Control.Tunnels.Tunnel, self).__init__()

                                self.yang_name = "tunnel"
                                self.yang_parent_name = "tunnels"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['tunnel_id']
                                self._child_classes = OrderedDict([("brief", ("brief", L2tpv2.Nodes.Node.Counters.Control.Tunnels.Tunnel.Brief)), ("global", ("global_", L2tpv2.Nodes.Node.Counters.Control.Tunnels.Tunnel.Global))])
                                self._leafs = OrderedDict([
                                    ('tunnel_id', (YLeaf(YType.uint32, 'tunnel-id'), ['int'])),
                                ])
                                self.tunnel_id = None

                                self.brief = L2tpv2.Nodes.Node.Counters.Control.Tunnels.Tunnel.Brief()
                                self.brief.parent = self
                                self._children_name_map["brief"] = "brief"

                                self.global_ = L2tpv2.Nodes.Node.Counters.Control.Tunnels.Tunnel.Global()
                                self.global_.parent = self
                                self._children_name_map["global_"] = "global"
                                self._segment_path = lambda: "tunnel" + "[tunnel-id='" + str(self.tunnel_id) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(L2tpv2.Nodes.Node.Counters.Control.Tunnels.Tunnel, ['tunnel_id'], name, value)


                            class Brief(_Entity_):
                                """
                                L2TP control message local and remote addresses
                                
                                .. attribute:: remote_tunnel_id
                                
                                	Remote tunnel ID
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: local_address
                                
                                	Local IP address
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                	**config**\: False
                                
                                .. attribute:: remote_address
                                
                                	Remote IP address
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'tunnel-l2tun-oper'
                                _revision = '2018-11-01'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(L2tpv2.Nodes.Node.Counters.Control.Tunnels.Tunnel.Brief, self).__init__()

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
                                    self._perform_setattr(L2tpv2.Nodes.Node.Counters.Control.Tunnels.Tunnel.Brief, ['remote_tunnel_id', 'local_address', 'remote_address'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                                    return meta._meta_table['L2tpv2.Nodes.Node.Counters.Control.Tunnels.Tunnel.Brief']['meta_info']


                            class Global(_Entity_):
                                """
                                Global data
                                
                                .. attribute:: transmit
                                
                                	Transmit data
                                	**type**\:  :py:class:`Transmit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Nodes.Node.Counters.Control.Tunnels.Tunnel.Global.Transmit>`
                                
                                	**config**\: False
                                
                                .. attribute:: retransmit
                                
                                	Re transmit data
                                	**type**\:  :py:class:`Retransmit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Nodes.Node.Counters.Control.Tunnels.Tunnel.Global.Retransmit>`
                                
                                	**config**\: False
                                
                                .. attribute:: received
                                
                                	Received data
                                	**type**\:  :py:class:`Received <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Nodes.Node.Counters.Control.Tunnels.Tunnel.Global.Received>`
                                
                                	**config**\: False
                                
                                .. attribute:: drop
                                
                                	Drop data
                                	**type**\:  :py:class:`Drop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Nodes.Node.Counters.Control.Tunnels.Tunnel.Global.Drop>`
                                
                                	**config**\: False
                                
                                .. attribute:: total_transmit
                                
                                	Total transmit
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: total_retransmit
                                
                                	Total retransmit
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: total_received
                                
                                	Total received
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: total_drop
                                
                                	Total drop
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'tunnel-l2tun-oper'
                                _revision = '2018-11-01'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(L2tpv2.Nodes.Node.Counters.Control.Tunnels.Tunnel.Global, self).__init__()

                                    self.yang_name = "global"
                                    self.yang_parent_name = "tunnel"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("transmit", ("transmit", L2tpv2.Nodes.Node.Counters.Control.Tunnels.Tunnel.Global.Transmit)), ("retransmit", ("retransmit", L2tpv2.Nodes.Node.Counters.Control.Tunnels.Tunnel.Global.Retransmit)), ("received", ("received", L2tpv2.Nodes.Node.Counters.Control.Tunnels.Tunnel.Global.Received)), ("drop", ("drop", L2tpv2.Nodes.Node.Counters.Control.Tunnels.Tunnel.Global.Drop))])
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

                                    self.transmit = L2tpv2.Nodes.Node.Counters.Control.Tunnels.Tunnel.Global.Transmit()
                                    self.transmit.parent = self
                                    self._children_name_map["transmit"] = "transmit"

                                    self.retransmit = L2tpv2.Nodes.Node.Counters.Control.Tunnels.Tunnel.Global.Retransmit()
                                    self.retransmit.parent = self
                                    self._children_name_map["retransmit"] = "retransmit"

                                    self.received = L2tpv2.Nodes.Node.Counters.Control.Tunnels.Tunnel.Global.Received()
                                    self.received.parent = self
                                    self._children_name_map["received"] = "received"

                                    self.drop = L2tpv2.Nodes.Node.Counters.Control.Tunnels.Tunnel.Global.Drop()
                                    self.drop.parent = self
                                    self._children_name_map["drop"] = "drop"
                                    self._segment_path = lambda: "global"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(L2tpv2.Nodes.Node.Counters.Control.Tunnels.Tunnel.Global, ['total_transmit', 'total_retransmit', 'total_received', 'total_drop'], name, value)


                                class Transmit(_Entity_):
                                    """
                                    Transmit data
                                    
                                    .. attribute:: unknown_packets
                                    
                                    	Unknown packets
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: zero_length_body_packets
                                    
                                    	Zero length body packets
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: start_control_connection_requests
                                    
                                    	Start control connection requests
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: start_control_connection_replies
                                    
                                    	Start control connection replies
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: start_control_connection_notifications
                                    
                                    	Start control connection notifications
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: stop_control_connection_notifications
                                    
                                    	Stop control connection notifications
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: hello_packets
                                    
                                    	Keep alive messages
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: outgoing_call_requests
                                    
                                    	Outgoing call requests
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: outgoing_call_replies
                                    
                                    	Outgoing call replies
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: outgoing_call_connected_packets
                                    
                                    	Outgoing call connected packets
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: incoming_call_requests
                                    
                                    	Incoming call requests
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: incoming_call_replies
                                    
                                    	Incoming call replies
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: incoming_call_connected_packets
                                    
                                    	Incoming call connected packets
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: call_disconnect_notify_packets
                                    
                                    	Call disconnect notify packets
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: wan_error_notify_packets
                                    
                                    	WAN error notify packets
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: set_link_info_packets
                                    
                                    	Set link info packets
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: service_relay_requests
                                    
                                    	Service relay request counts
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: service_relay_replies
                                    
                                    	Service relay reply counts
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: acknowledgement_packets
                                    
                                    	Packets acknowledgement
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'tunnel-l2tun-oper'
                                    _revision = '2018-11-01'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(L2tpv2.Nodes.Node.Counters.Control.Tunnels.Tunnel.Global.Transmit, self).__init__()

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
                                        self._perform_setattr(L2tpv2.Nodes.Node.Counters.Control.Tunnels.Tunnel.Global.Transmit, ['unknown_packets', 'zero_length_body_packets', 'start_control_connection_requests', 'start_control_connection_replies', 'start_control_connection_notifications', 'stop_control_connection_notifications', 'hello_packets', 'outgoing_call_requests', 'outgoing_call_replies', 'outgoing_call_connected_packets', 'incoming_call_requests', 'incoming_call_replies', 'incoming_call_connected_packets', 'call_disconnect_notify_packets', 'wan_error_notify_packets', 'set_link_info_packets', 'service_relay_requests', 'service_relay_replies', 'acknowledgement_packets'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                                        return meta._meta_table['L2tpv2.Nodes.Node.Counters.Control.Tunnels.Tunnel.Global.Transmit']['meta_info']


                                class Retransmit(_Entity_):
                                    """
                                    Re transmit data
                                    
                                    .. attribute:: unknown_packets
                                    
                                    	Unknown packets
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: zero_length_body_packets
                                    
                                    	Zero length body packets
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: start_control_connection_requests
                                    
                                    	Start control connection requests
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: start_control_connection_replies
                                    
                                    	Start control connection replies
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: start_control_connection_notifications
                                    
                                    	Start control connection notifications
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: stop_control_connection_notifications
                                    
                                    	Stop control connection notifications
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: hello_packets
                                    
                                    	Keep alive messages
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: outgoing_call_requests
                                    
                                    	Outgoing call requests
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: outgoing_call_replies
                                    
                                    	Outgoing call replies
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: outgoing_call_connected_packets
                                    
                                    	Outgoing call connected packets
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: incoming_call_requests
                                    
                                    	Incoming call requests
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: incoming_call_replies
                                    
                                    	Incoming call replies
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: incoming_call_connected_packets
                                    
                                    	Incoming call connected packets
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: call_disconnect_notify_packets
                                    
                                    	Call disconnect notify packets
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: wan_error_notify_packets
                                    
                                    	WAN error notify packets
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: set_link_info_packets
                                    
                                    	Set link info packets
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: service_relay_requests
                                    
                                    	Service relay request counts
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: service_relay_replies
                                    
                                    	Service relay reply counts
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: acknowledgement_packets
                                    
                                    	Packets acknowledgement
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'tunnel-l2tun-oper'
                                    _revision = '2018-11-01'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(L2tpv2.Nodes.Node.Counters.Control.Tunnels.Tunnel.Global.Retransmit, self).__init__()

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
                                        self._perform_setattr(L2tpv2.Nodes.Node.Counters.Control.Tunnels.Tunnel.Global.Retransmit, ['unknown_packets', 'zero_length_body_packets', 'start_control_connection_requests', 'start_control_connection_replies', 'start_control_connection_notifications', 'stop_control_connection_notifications', 'hello_packets', 'outgoing_call_requests', 'outgoing_call_replies', 'outgoing_call_connected_packets', 'incoming_call_requests', 'incoming_call_replies', 'incoming_call_connected_packets', 'call_disconnect_notify_packets', 'wan_error_notify_packets', 'set_link_info_packets', 'service_relay_requests', 'service_relay_replies', 'acknowledgement_packets'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                                        return meta._meta_table['L2tpv2.Nodes.Node.Counters.Control.Tunnels.Tunnel.Global.Retransmit']['meta_info']


                                class Received(_Entity_):
                                    """
                                    Received data
                                    
                                    .. attribute:: unknown_packets
                                    
                                    	Unknown packets
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: zero_length_body_packets
                                    
                                    	Zero length body packets
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: start_control_connection_requests
                                    
                                    	Start control connection requests
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: start_control_connection_replies
                                    
                                    	Start control connection replies
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: start_control_connection_notifications
                                    
                                    	Start control connection notifications
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: stop_control_connection_notifications
                                    
                                    	Stop control connection notifications
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: hello_packets
                                    
                                    	Keep alive messages
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: outgoing_call_requests
                                    
                                    	Outgoing call requests
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: outgoing_call_replies
                                    
                                    	Outgoing call replies
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: outgoing_call_connected_packets
                                    
                                    	Outgoing call connected packets
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: incoming_call_requests
                                    
                                    	Incoming call requests
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: incoming_call_replies
                                    
                                    	Incoming call replies
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: incoming_call_connected_packets
                                    
                                    	Incoming call connected packets
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: call_disconnect_notify_packets
                                    
                                    	Call disconnect notify packets
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: wan_error_notify_packets
                                    
                                    	WAN error notify packets
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: set_link_info_packets
                                    
                                    	Set link info packets
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: service_relay_requests
                                    
                                    	Service relay request counts
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: service_relay_replies
                                    
                                    	Service relay reply counts
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: acknowledgement_packets
                                    
                                    	Packets acknowledgement
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'tunnel-l2tun-oper'
                                    _revision = '2018-11-01'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(L2tpv2.Nodes.Node.Counters.Control.Tunnels.Tunnel.Global.Received, self).__init__()

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
                                        self._perform_setattr(L2tpv2.Nodes.Node.Counters.Control.Tunnels.Tunnel.Global.Received, ['unknown_packets', 'zero_length_body_packets', 'start_control_connection_requests', 'start_control_connection_replies', 'start_control_connection_notifications', 'stop_control_connection_notifications', 'hello_packets', 'outgoing_call_requests', 'outgoing_call_replies', 'outgoing_call_connected_packets', 'incoming_call_requests', 'incoming_call_replies', 'incoming_call_connected_packets', 'call_disconnect_notify_packets', 'wan_error_notify_packets', 'set_link_info_packets', 'service_relay_requests', 'service_relay_replies', 'acknowledgement_packets'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                                        return meta._meta_table['L2tpv2.Nodes.Node.Counters.Control.Tunnels.Tunnel.Global.Received']['meta_info']


                                class Drop(_Entity_):
                                    """
                                    Drop data
                                    
                                    .. attribute:: unknown_packets
                                    
                                    	Unknown packets
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: zero_length_body_packets
                                    
                                    	Zero length body packets
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: start_control_connection_requests
                                    
                                    	Start control connection requests
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: start_control_connection_replies
                                    
                                    	Start control connection replies
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: start_control_connection_notifications
                                    
                                    	Start control connection notifications
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: stop_control_connection_notifications
                                    
                                    	Stop control connection notifications
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: hello_packets
                                    
                                    	Keep alive messages
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: outgoing_call_requests
                                    
                                    	Outgoing call requests
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: outgoing_call_replies
                                    
                                    	Outgoing call replies
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: outgoing_call_connected_packets
                                    
                                    	Outgoing call connected packets
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: incoming_call_requests
                                    
                                    	Incoming call requests
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: incoming_call_replies
                                    
                                    	Incoming call replies
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: incoming_call_connected_packets
                                    
                                    	Incoming call connected packets
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: call_disconnect_notify_packets
                                    
                                    	Call disconnect notify packets
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: wan_error_notify_packets
                                    
                                    	WAN error notify packets
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: set_link_info_packets
                                    
                                    	Set link info packets
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: service_relay_requests
                                    
                                    	Service relay request counts
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: service_relay_replies
                                    
                                    	Service relay reply counts
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: acknowledgement_packets
                                    
                                    	Packets acknowledgement
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'tunnel-l2tun-oper'
                                    _revision = '2018-11-01'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(L2tpv2.Nodes.Node.Counters.Control.Tunnels.Tunnel.Global.Drop, self).__init__()

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
                                        self._perform_setattr(L2tpv2.Nodes.Node.Counters.Control.Tunnels.Tunnel.Global.Drop, ['unknown_packets', 'zero_length_body_packets', 'start_control_connection_requests', 'start_control_connection_replies', 'start_control_connection_notifications', 'stop_control_connection_notifications', 'hello_packets', 'outgoing_call_requests', 'outgoing_call_replies', 'outgoing_call_connected_packets', 'incoming_call_requests', 'incoming_call_replies', 'incoming_call_connected_packets', 'call_disconnect_notify_packets', 'wan_error_notify_packets', 'set_link_info_packets', 'service_relay_requests', 'service_relay_replies', 'acknowledgement_packets'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                                        return meta._meta_table['L2tpv2.Nodes.Node.Counters.Control.Tunnels.Tunnel.Global.Drop']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                                    return meta._meta_table['L2tpv2.Nodes.Node.Counters.Control.Tunnels.Tunnel.Global']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                                return meta._meta_table['L2tpv2.Nodes.Node.Counters.Control.Tunnels.Tunnel']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                            return meta._meta_table['L2tpv2.Nodes.Node.Counters.Control.Tunnels']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                        return meta._meta_table['L2tpv2.Nodes.Node.Counters.Control']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                    return meta._meta_table['L2tpv2.Nodes.Node.Counters']['meta_info']


            class Statistics(_Entity_):
                """
                L2TP v2 statistics information
                
                .. attribute:: tunnels
                
                	Number of tunnels
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: sessions
                
                	Number of sessions
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: sent_packets
                
                	Number of packets sent
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: received_packets
                
                	Number of packets received
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: average_packet_processing_time
                
                	Average processing time for received packets (in micro seconds)
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                	**units**\: microsecond
                
                .. attribute:: received_out_of_order_packets
                
                	Out of order packets received
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: reorder_packets
                
                	Re order packets
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: reorder_deviation_packets
                
                	Re order deviation
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: incoming_dropped_packets
                
                	In coming packets dropped
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: buffered_packets
                
                	Bufferred packets
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: netio_packets
                
                	Packets RX in netio
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                

                """

                _prefix = 'tunnel-l2tun-oper'
                _revision = '2018-11-01'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(L2tpv2.Nodes.Node.Statistics, self).__init__()

                    self.yang_name = "statistics"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
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
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(L2tpv2.Nodes.Node.Statistics, ['tunnels', 'sessions', 'sent_packets', 'received_packets', 'average_packet_processing_time', 'received_out_of_order_packets', 'reorder_packets', 'reorder_deviation_packets', 'incoming_dropped_packets', 'buffered_packets', 'netio_packets'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                    return meta._meta_table['L2tpv2.Nodes.Node.Statistics']['meta_info']


            class Tunnel(_Entity_):
                """
                L2TPv2 tunnel 
                
                .. attribute:: accounting
                
                	Tunnel accounting counters
                	**type**\:  :py:class:`Accounting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Nodes.Node.Tunnel.Accounting>`
                
                	**config**\: False
                
                

                """

                _prefix = 'tunnel-l2tun-oper'
                _revision = '2018-11-01'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(L2tpv2.Nodes.Node.Tunnel, self).__init__()

                    self.yang_name = "tunnel"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("accounting", ("accounting", L2tpv2.Nodes.Node.Tunnel.Accounting))])
                    self._leafs = OrderedDict()

                    self.accounting = L2tpv2.Nodes.Node.Tunnel.Accounting()
                    self.accounting.parent = self
                    self._children_name_map["accounting"] = "accounting"
                    self._segment_path = lambda: "tunnel"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(L2tpv2.Nodes.Node.Tunnel, [], name, value)


                class Accounting(_Entity_):
                    """
                    Tunnel accounting counters
                    
                    .. attribute:: statistics
                    
                    	Tunnel accounting statistics
                    	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Nodes.Node.Tunnel.Accounting.Statistics>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'tunnel-l2tun-oper'
                    _revision = '2018-11-01'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(L2tpv2.Nodes.Node.Tunnel.Accounting, self).__init__()

                        self.yang_name = "accounting"
                        self.yang_parent_name = "tunnel"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("statistics", ("statistics", L2tpv2.Nodes.Node.Tunnel.Accounting.Statistics))])
                        self._leafs = OrderedDict()

                        self.statistics = L2tpv2.Nodes.Node.Tunnel.Accounting.Statistics()
                        self.statistics.parent = self
                        self._children_name_map["statistics"] = "statistics"
                        self._segment_path = lambda: "accounting"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2tpv2.Nodes.Node.Tunnel.Accounting, [], name, value)


                    class Statistics(_Entity_):
                        """
                        Tunnel accounting statistics
                        
                        .. attribute:: records_sent_successfully
                        
                        	Accounting records sent successfully
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: start
                        
                        	Accounting start
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: stop
                        
                        	Accounting stop
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: reject
                        
                        	Accounting reject
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: transport_failures
                        
                        	Transport failures
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: positive_acknowledgement
                        
                        	Positive acknowledgement
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: negative_acknowledgement
                        
                        	Negative acknowledgement
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: records_checkpointed
                        
                        	Total records checkpointed
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: records_failed_to_checkpoint
                        
                        	Records fail to checkpoint
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: records_sent_from_queue
                        
                        	Records sent from queue
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: memory_failures
                        
                        	Memory failures
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: current_size
                        
                        	Current checkpoint size
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: records_recovered_from_checkpoint
                        
                        	Records recovered from checkpoint
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: records_fail_to_recover
                        
                        	Records fail to recover
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: queue_statistics_size
                        
                        	Queue statistics size
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'tunnel-l2tun-oper'
                        _revision = '2018-11-01'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(L2tpv2.Nodes.Node.Tunnel.Accounting.Statistics, self).__init__()

                            self.yang_name = "statistics"
                            self.yang_parent_name = "accounting"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
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
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2tpv2.Nodes.Node.Tunnel.Accounting.Statistics, ['records_sent_successfully', 'start', 'stop', 'reject', 'transport_failures', 'positive_acknowledgement', 'negative_acknowledgement', 'records_checkpointed', 'records_failed_to_checkpoint', 'records_sent_from_queue', 'memory_failures', 'current_size', 'records_recovered_from_checkpoint', 'records_fail_to_recover', 'queue_statistics_size'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                            return meta._meta_table['L2tpv2.Nodes.Node.Tunnel.Accounting.Statistics']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                        return meta._meta_table['L2tpv2.Nodes.Node.Tunnel.Accounting']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                    return meta._meta_table['L2tpv2.Nodes.Node.Tunnel']['meta_info']


            class TunnelConfigurations(_Entity_):
                """
                List of tunnel IDs
                
                .. attribute:: tunnel_configuration
                
                	L2TP tunnel information
                	**type**\: list of  		 :py:class:`TunnelConfiguration <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Nodes.Node.TunnelConfigurations.TunnelConfiguration>`
                
                	**config**\: False
                
                

                """

                _prefix = 'tunnel-l2tun-oper'
                _revision = '2018-11-01'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(L2tpv2.Nodes.Node.TunnelConfigurations, self).__init__()

                    self.yang_name = "tunnel-configurations"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("tunnel-configuration", ("tunnel_configuration", L2tpv2.Nodes.Node.TunnelConfigurations.TunnelConfiguration))])
                    self._leafs = OrderedDict()

                    self.tunnel_configuration = YList(self)
                    self._segment_path = lambda: "tunnel-configurations"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(L2tpv2.Nodes.Node.TunnelConfigurations, [], name, value)


                class TunnelConfiguration(_Entity_):
                    """
                    L2TP tunnel information
                    
                    .. attribute:: local_tunnel_id  (key)
                    
                    	Local tunnel ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_class
                    
                    	L2Tp class data
                    	**type**\:  :py:class:`L2tpClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Nodes.Node.TunnelConfigurations.TunnelConfiguration.L2tpClass>`
                    
                    	**config**\: False
                    
                    .. attribute:: remote_tunnel_id
                    
                    	Remote tunnel ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'tunnel-l2tun-oper'
                    _revision = '2018-11-01'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(L2tpv2.Nodes.Node.TunnelConfigurations.TunnelConfiguration, self).__init__()

                        self.yang_name = "tunnel-configuration"
                        self.yang_parent_name = "tunnel-configurations"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['local_tunnel_id']
                        self._child_classes = OrderedDict([("l2tp-class", ("l2tp_class", L2tpv2.Nodes.Node.TunnelConfigurations.TunnelConfiguration.L2tpClass))])
                        self._leafs = OrderedDict([
                            ('local_tunnel_id', (YLeaf(YType.uint32, 'local-tunnel-id'), ['int'])),
                            ('remote_tunnel_id', (YLeaf(YType.uint32, 'remote-tunnel-id'), ['int'])),
                        ])
                        self.local_tunnel_id = None
                        self.remote_tunnel_id = None

                        self.l2tp_class = L2tpv2.Nodes.Node.TunnelConfigurations.TunnelConfiguration.L2tpClass()
                        self.l2tp_class.parent = self
                        self._children_name_map["l2tp_class"] = "l2tp-class"
                        self._segment_path = lambda: "tunnel-configuration" + "[local-tunnel-id='" + str(self.local_tunnel_id) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2tpv2.Nodes.Node.TunnelConfigurations.TunnelConfiguration, ['local_tunnel_id', 'remote_tunnel_id'], name, value)


                    class L2tpClass(_Entity_):
                        """
                        L2Tp class data
                        
                        .. attribute:: ip_tos
                        
                        	IP TOS
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: vrf_name
                        
                        	VRF name
                        	**type**\: str
                        
                        	**length:** 0..256
                        
                        	**config**\: False
                        
                        .. attribute:: receive_window_size
                        
                        	Receive window size
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        	**config**\: False
                        
                        .. attribute:: class_name_xr
                        
                        	Class name
                        	**type**\: str
                        
                        	**length:** 0..256
                        
                        	**config**\: False
                        
                        .. attribute:: digest_hash
                        
                        	Hash configured as MD5 or SHA1
                        	**type**\:  :py:class:`DigestHash <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.DigestHash>`
                        
                        	**config**\: False
                        
                        .. attribute:: password
                        
                        	Password
                        	**type**\: str
                        
                        	**length:** 0..25
                        
                        	**config**\: False
                        
                        .. attribute:: encoded_password
                        
                        	Encoded password
                        	**type**\: str
                        
                        	**length:** 0..256
                        
                        	**config**\: False
                        
                        .. attribute:: host_name
                        
                        	Host name
                        	**type**\: str
                        
                        	**length:** 0..256
                        
                        	**config**\: False
                        
                        .. attribute:: accounting_method_list
                        
                        	Accounting List
                        	**type**\: str
                        
                        	**length:** 0..256
                        
                        	**config**\: False
                        
                        .. attribute:: hello_timeout
                        
                        	Hello timeout value in seconds
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        	**units**\: second
                        
                        .. attribute:: setup_timeout
                        
                        	Timeout setup value in seconds
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        	**units**\: second
                        
                        .. attribute:: retransmit_minimum_timeout
                        
                        	Retransmit minimum timeout in seconds
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        	**units**\: second
                        
                        .. attribute:: retransmit_maximum_timeout
                        
                        	Retransmit maximum timeout in seconds
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        	**units**\: second
                        
                        .. attribute:: initial_retransmit_minimum_timeout
                        
                        	Initial timeout minimum in seconds
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        	**units**\: second
                        
                        .. attribute:: initial_retransmit_maximum_timeout
                        
                        	Initial timeout maximum in seconds
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        	**units**\: second
                        
                        .. attribute:: timeout_no_user
                        
                        	Timeout no user
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: retransmit_retries
                        
                        	Retransmit retries
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: initial_retransmit_retries
                        
                        	Initial retransmit retries
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: is_authentication_enabled
                        
                        	True if authentication is enabled
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_hidden
                        
                        	True if class is hidden
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_digest_enabled
                        
                        	True if digest authentication is enabled
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_digest_check_enabled
                        
                        	True if digest check is enabled
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_congestion_control_enabled
                        
                        	True if congestion control is enabled
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_peer_address_checked
                        
                        	True if peer address is checked
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'tunnel-l2tun-oper'
                        _revision = '2018-11-01'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(L2tpv2.Nodes.Node.TunnelConfigurations.TunnelConfiguration.L2tpClass, self).__init__()

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
                            self._perform_setattr(L2tpv2.Nodes.Node.TunnelConfigurations.TunnelConfiguration.L2tpClass, ['ip_tos', 'vrf_name', 'receive_window_size', 'class_name_xr', 'digest_hash', 'password', 'encoded_password', 'host_name', 'accounting_method_list', 'hello_timeout', 'setup_timeout', 'retransmit_minimum_timeout', 'retransmit_maximum_timeout', 'initial_retransmit_minimum_timeout', 'initial_retransmit_maximum_timeout', 'timeout_no_user', 'retransmit_retries', 'initial_retransmit_retries', 'is_authentication_enabled', 'is_hidden', 'is_digest_enabled', 'is_digest_check_enabled', 'is_congestion_control_enabled', 'is_peer_address_checked'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                            return meta._meta_table['L2tpv2.Nodes.Node.TunnelConfigurations.TunnelConfiguration.L2tpClass']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                        return meta._meta_table['L2tpv2.Nodes.Node.TunnelConfigurations.TunnelConfiguration']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                    return meta._meta_table['L2tpv2.Nodes.Node.TunnelConfigurations']['meta_info']


            class CounterHistFail(_Entity_):
                """
                Failure events leading to disconnection
                
                .. attribute:: sess_down_tmout
                
                	sesions affected due to timeout
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: tx_counters
                
                	Send side counters
                	**type**\: str
                
                	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                
                	**config**\: False
                
                .. attribute:: rx_counters
                
                	Receive side counters
                	**type**\: str
                
                	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                
                	**config**\: False
                
                .. attribute:: pkt_timeout
                
                	timeout events by packet
                	**type**\: list of  		 :py:class:`PktTimeout <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Nodes.Node.CounterHistFail.PktTimeout>`
                
                	**config**\: False
                
                

                """

                _prefix = 'tunnel-l2tun-oper'
                _revision = '2018-11-01'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(L2tpv2.Nodes.Node.CounterHistFail, self).__init__()

                    self.yang_name = "counter-hist-fail"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("pkt-timeout", ("pkt_timeout", L2tpv2.Nodes.Node.CounterHistFail.PktTimeout))])
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
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(L2tpv2.Nodes.Node.CounterHistFail, ['sess_down_tmout', 'tx_counters', 'rx_counters'], name, value)


                class PktTimeout(_Entity_):
                    """
                    timeout events by packet
                    
                    .. attribute:: entry
                    
                    	timeout events by packet
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'tunnel-l2tun-oper'
                    _revision = '2018-11-01'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(L2tpv2.Nodes.Node.CounterHistFail.PktTimeout, self).__init__()

                        self.yang_name = "pkt-timeout"
                        self.yang_parent_name = "counter-hist-fail"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('entry', (YLeaf(YType.uint32, 'entry'), ['int'])),
                        ])
                        self.entry = None
                        self._segment_path = lambda: "pkt-timeout"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2tpv2.Nodes.Node.CounterHistFail.PktTimeout, ['entry'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                        return meta._meta_table['L2tpv2.Nodes.Node.CounterHistFail.PktTimeout']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                    return meta._meta_table['L2tpv2.Nodes.Node.CounterHistFail']['meta_info']


            class Classes(_Entity_):
                """
                List of L2TP class names
                
                .. attribute:: class_
                
                	L2TP class name
                	**type**\: list of  		 :py:class:`Class <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Nodes.Node.Classes.Class>`
                
                	**config**\: False
                
                

                """

                _prefix = 'tunnel-l2tun-oper'
                _revision = '2018-11-01'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(L2tpv2.Nodes.Node.Classes, self).__init__()

                    self.yang_name = "classes"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("class", ("class_", L2tpv2.Nodes.Node.Classes.Class))])
                    self._leafs = OrderedDict()

                    self.class_ = YList(self)
                    self._segment_path = lambda: "classes"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(L2tpv2.Nodes.Node.Classes, [], name, value)


                class Class(_Entity_):
                    """
                    L2TP class name
                    
                    .. attribute:: class_name  (key)
                    
                    	L2TP class name
                    	**type**\: str
                    
                    	**length:** 1..31
                    
                    	**config**\: False
                    
                    .. attribute:: ip_tos
                    
                    	IP TOS
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: vrf_name
                    
                    	VRF name
                    	**type**\: str
                    
                    	**length:** 0..256
                    
                    	**config**\: False
                    
                    .. attribute:: receive_window_size
                    
                    	Receive window size
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**config**\: False
                    
                    .. attribute:: class_name_xr
                    
                    	Class name
                    	**type**\: str
                    
                    	**length:** 0..256
                    
                    	**config**\: False
                    
                    .. attribute:: digest_hash
                    
                    	Hash configured as MD5 or SHA1
                    	**type**\:  :py:class:`DigestHash <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.DigestHash>`
                    
                    	**config**\: False
                    
                    .. attribute:: password
                    
                    	Password
                    	**type**\: str
                    
                    	**length:** 0..25
                    
                    	**config**\: False
                    
                    .. attribute:: encoded_password
                    
                    	Encoded password
                    	**type**\: str
                    
                    	**length:** 0..256
                    
                    	**config**\: False
                    
                    .. attribute:: host_name
                    
                    	Host name
                    	**type**\: str
                    
                    	**length:** 0..256
                    
                    	**config**\: False
                    
                    .. attribute:: accounting_method_list
                    
                    	Accounting List
                    	**type**\: str
                    
                    	**length:** 0..256
                    
                    	**config**\: False
                    
                    .. attribute:: hello_timeout
                    
                    	Hello timeout value in seconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    	**units**\: second
                    
                    .. attribute:: setup_timeout
                    
                    	Timeout setup value in seconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    	**units**\: second
                    
                    .. attribute:: retransmit_minimum_timeout
                    
                    	Retransmit minimum timeout in seconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    	**units**\: second
                    
                    .. attribute:: retransmit_maximum_timeout
                    
                    	Retransmit maximum timeout in seconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    	**units**\: second
                    
                    .. attribute:: initial_retransmit_minimum_timeout
                    
                    	Initial timeout minimum in seconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    	**units**\: second
                    
                    .. attribute:: initial_retransmit_maximum_timeout
                    
                    	Initial timeout maximum in seconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    	**units**\: second
                    
                    .. attribute:: timeout_no_user
                    
                    	Timeout no user
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: retransmit_retries
                    
                    	Retransmit retries
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: initial_retransmit_retries
                    
                    	Initial retransmit retries
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: is_authentication_enabled
                    
                    	True if authentication is enabled
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: is_hidden
                    
                    	True if class is hidden
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: is_digest_enabled
                    
                    	True if digest authentication is enabled
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: is_digest_check_enabled
                    
                    	True if digest check is enabled
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: is_congestion_control_enabled
                    
                    	True if congestion control is enabled
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: is_peer_address_checked
                    
                    	True if peer address is checked
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'tunnel-l2tun-oper'
                    _revision = '2018-11-01'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(L2tpv2.Nodes.Node.Classes.Class, self).__init__()

                        self.yang_name = "class"
                        self.yang_parent_name = "classes"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
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
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2tpv2.Nodes.Node.Classes.Class, ['class_name', 'ip_tos', 'vrf_name', 'receive_window_size', 'class_name_xr', 'digest_hash', 'password', 'encoded_password', 'host_name', 'accounting_method_list', 'hello_timeout', 'setup_timeout', 'retransmit_minimum_timeout', 'retransmit_maximum_timeout', 'initial_retransmit_minimum_timeout', 'initial_retransmit_maximum_timeout', 'timeout_no_user', 'retransmit_retries', 'initial_retransmit_retries', 'is_authentication_enabled', 'is_hidden', 'is_digest_enabled', 'is_digest_check_enabled', 'is_congestion_control_enabled', 'is_peer_address_checked'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                        return meta._meta_table['L2tpv2.Nodes.Node.Classes.Class']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                    return meta._meta_table['L2tpv2.Nodes.Node.Classes']['meta_info']


            class Tunnels(_Entity_):
                """
                List of tunnel IDs
                
                .. attribute:: tunnel
                
                	L2TP tunnel  information
                	**type**\: list of  		 :py:class:`Tunnel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Nodes.Node.Tunnels.Tunnel>`
                
                	**config**\: False
                
                

                """

                _prefix = 'tunnel-l2tun-oper'
                _revision = '2018-11-01'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(L2tpv2.Nodes.Node.Tunnels, self).__init__()

                    self.yang_name = "tunnels"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("tunnel", ("tunnel", L2tpv2.Nodes.Node.Tunnels.Tunnel))])
                    self._leafs = OrderedDict()

                    self.tunnel = YList(self)
                    self._segment_path = lambda: "tunnels"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(L2tpv2.Nodes.Node.Tunnels, [], name, value)


                class Tunnel(_Entity_):
                    """
                    L2TP tunnel  information
                    
                    .. attribute:: local_tunnel_id  (key)
                    
                    	Local tunnel ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: local_address
                    
                    	Local tunnel address
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    	**config**\: False
                    
                    .. attribute:: remote_address
                    
                    	Remote tunnel address
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    	**config**\: False
                    
                    .. attribute:: local_port
                    
                    	Local port
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**config**\: False
                    
                    .. attribute:: remote_port
                    
                    	Remote port
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**config**\: False
                    
                    .. attribute:: protocol
                    
                    	Protocol
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: is_pmtu_enabled
                    
                    	True if tunnel PMTU checking is enabled
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: remote_tunnel_id
                    
                    	Remote tunnel ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: local_tunnel_name
                    
                    	Local tunnel name
                    	**type**\: str
                    
                    	**length:** 0..256
                    
                    	**config**\: False
                    
                    .. attribute:: remote_tunnel_name
                    
                    	Remote tunnel name
                    	**type**\: str
                    
                    	**length:** 0..256
                    
                    	**config**\: False
                    
                    .. attribute:: class_name
                    
                    	L2TP class name
                    	**type**\: str
                    
                    	**length:** 0..256
                    
                    	**config**\: False
                    
                    .. attribute:: active_sessions
                    
                    	Number of active sessions
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: sequence_ns
                    
                    	Sequence NS
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**config**\: False
                    
                    .. attribute:: sequence_nr
                    
                    	Sequence NR
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**config**\: False
                    
                    .. attribute:: local_window_size
                    
                    	Local window size
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**config**\: False
                    
                    .. attribute:: remote_window_size
                    
                    	Remote window size
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**config**\: False
                    
                    .. attribute:: retransmission_time
                    
                    	Retransmission time in seconds
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**config**\: False
                    
                    	**units**\: second
                    
                    .. attribute:: maximum_retransmission_time
                    
                    	Maximum retransmission time in seconds
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**config**\: False
                    
                    	**units**\: second
                    
                    .. attribute:: unsent_queue_size
                    
                    	Unsent queue size
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**config**\: False
                    
                    .. attribute:: unsent_maximum_queue_size
                    
                    	Unsent maximum queue size
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**config**\: False
                    
                    .. attribute:: resend_queue_size
                    
                    	Resend queue size
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**config**\: False
                    
                    .. attribute:: resend_maximum_queue_size
                    
                    	Resend maximum queue size
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**config**\: False
                    
                    .. attribute:: order_queue_size
                    
                    	Order queue size
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**config**\: False
                    
                    .. attribute:: packet_queue_check
                    
                    	Current number session packet queue check
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**config**\: False
                    
                    .. attribute:: digest_secrets
                    
                    	Control message authentication with digest secrets
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**config**\: False
                    
                    .. attribute:: resends
                    
                    	Total resends
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: zero_length_body_acknowledgement_sent
                    
                    	Total zero length body acknowledgement
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: total_out_of_order_drop_packets
                    
                    	Total out of order dropped packets
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: total_out_of_order_reorder_packets
                    
                    	Total out of order reorder packets
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: total_peer_authentication_failures
                    
                    	Number of peer authentication failures
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: is_tunnel_up
                    
                    	True if tunnel is up
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: is_congestion_control_enabled
                    
                    	True if congestion control is enabled else false
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: retransmit_time
                    
                    	Retransmit time distribution in seconds
                    	**type**\: list of  		 :py:class:`RetransmitTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Nodes.Node.Tunnels.Tunnel.RetransmitTime>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'tunnel-l2tun-oper'
                    _revision = '2018-11-01'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(L2tpv2.Nodes.Node.Tunnels.Tunnel, self).__init__()

                        self.yang_name = "tunnel"
                        self.yang_parent_name = "tunnels"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['local_tunnel_id']
                        self._child_classes = OrderedDict([("retransmit-time", ("retransmit_time", L2tpv2.Nodes.Node.Tunnels.Tunnel.RetransmitTime))])
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
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2tpv2.Nodes.Node.Tunnels.Tunnel, ['local_tunnel_id', 'local_address', 'remote_address', 'local_port', 'remote_port', 'protocol', 'is_pmtu_enabled', 'remote_tunnel_id', 'local_tunnel_name', 'remote_tunnel_name', 'class_name', 'active_sessions', 'sequence_ns', 'sequence_nr', 'local_window_size', 'remote_window_size', 'retransmission_time', 'maximum_retransmission_time', 'unsent_queue_size', 'unsent_maximum_queue_size', 'resend_queue_size', 'resend_maximum_queue_size', 'order_queue_size', 'packet_queue_check', 'digest_secrets', 'resends', 'zero_length_body_acknowledgement_sent', 'total_out_of_order_drop_packets', 'total_out_of_order_reorder_packets', 'total_peer_authentication_failures', 'is_tunnel_up', 'is_congestion_control_enabled'], name, value)


                    class RetransmitTime(_Entity_):
                        """
                        Retransmit time distribution in seconds
                        
                        .. attribute:: entry
                        
                        	Retransmit time distribution in seconds
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        	**config**\: False
                        
                        	**units**\: second
                        
                        

                        """

                        _prefix = 'tunnel-l2tun-oper'
                        _revision = '2018-11-01'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(L2tpv2.Nodes.Node.Tunnels.Tunnel.RetransmitTime, self).__init__()

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
                            self._perform_setattr(L2tpv2.Nodes.Node.Tunnels.Tunnel.RetransmitTime, ['entry'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                            return meta._meta_table['L2tpv2.Nodes.Node.Tunnels.Tunnel.RetransmitTime']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                        return meta._meta_table['L2tpv2.Nodes.Node.Tunnels.Tunnel']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                    return meta._meta_table['L2tpv2.Nodes.Node.Tunnels']['meta_info']


            class Sessions(_Entity_):
                """
                List of session IDs
                
                .. attribute:: session
                
                	L2TP information for a particular session
                	**type**\: list of  		 :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Nodes.Node.Sessions.Session>`
                
                	**config**\: False
                
                

                """

                _prefix = 'tunnel-l2tun-oper'
                _revision = '2018-11-01'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(L2tpv2.Nodes.Node.Sessions, self).__init__()

                    self.yang_name = "sessions"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("session", ("session", L2tpv2.Nodes.Node.Sessions.Session))])
                    self._leafs = OrderedDict()

                    self.session = YList(self)
                    self._segment_path = lambda: "sessions"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(L2tpv2.Nodes.Node.Sessions, [], name, value)


                class Session(_Entity_):
                    """
                    L2TP information for a particular session
                    
                    .. attribute:: local_tunnel_id  (key)
                    
                    	Local tunnel ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: local_session_id  (key)
                    
                    	Local session ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: session_application_data
                    
                    	Session application data
                    	**type**\:  :py:class:`SessionApplicationData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Nodes.Node.Sessions.Session.SessionApplicationData>`
                    
                    	**config**\: False
                    
                    .. attribute:: local_ip_address
                    
                    	Local session IP address
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    	**config**\: False
                    
                    .. attribute:: remote_ip_address
                    
                    	Remote session IP address
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_sess_udp_lport
                    
                    	l2tp sh sess udp lport
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_sess_udp_rport
                    
                    	l2tp sh sess udp rport
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**config**\: False
                    
                    .. attribute:: protocol
                    
                    	Protocol
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: remote_tunnel_id
                    
                    	Remote tunnel ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: call_serial_number
                    
                    	Call serial number
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: local_tunnel_name
                    
                    	Local tunnel name
                    	**type**\: str
                    
                    	**length:** 0..256
                    
                    	**config**\: False
                    
                    .. attribute:: remote_tunnel_name
                    
                    	Remote tunnel name
                    	**type**\: str
                    
                    	**length:** 0..256
                    
                    	**config**\: False
                    
                    .. attribute:: remote_session_id
                    
                    	Remote session ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_sess_tie_breaker_enabled
                    
                    	l2tp sh sess tie breaker enabled
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_sess_tie_breaker
                    
                    	l2tp sh sess tie breaker
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: is_session_manual
                    
                    	True if session is manual
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: is_session_up
                    
                    	True if session is up
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: is_udp_checksum_enabled
                    
                    	True if UDP checksum enabled
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: is_sequencing_on
                    
                    	True if session sequence is on
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: is_session_state_established
                    
                    	True if session state is established
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: is_session_locally_initiated
                    
                    	True if session initiated locally
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: is_conditional_debug_enabled
                    
                    	True if conditional debugging is enabled
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: unique_id
                    
                    	Unique ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: interface_name
                    
                    	Interface name
                    	**type**\: str
                    
                    	**length:** 0..256
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'tunnel-l2tun-oper'
                    _revision = '2018-11-01'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(L2tpv2.Nodes.Node.Sessions.Session, self).__init__()

                        self.yang_name = "session"
                        self.yang_parent_name = "sessions"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['local_tunnel_id','local_session_id']
                        self._child_classes = OrderedDict([("session-application-data", ("session_application_data", L2tpv2.Nodes.Node.Sessions.Session.SessionApplicationData))])
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

                        self.session_application_data = L2tpv2.Nodes.Node.Sessions.Session.SessionApplicationData()
                        self.session_application_data.parent = self
                        self._children_name_map["session_application_data"] = "session-application-data"
                        self._segment_path = lambda: "session" + "[local-tunnel-id='" + str(self.local_tunnel_id) + "']" + "[local-session-id='" + str(self.local_session_id) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2tpv2.Nodes.Node.Sessions.Session, ['local_tunnel_id', 'local_session_id', 'local_ip_address', 'remote_ip_address', 'l2tp_sh_sess_udp_lport', 'l2tp_sh_sess_udp_rport', 'protocol', 'remote_tunnel_id', 'call_serial_number', 'local_tunnel_name', 'remote_tunnel_name', 'remote_session_id', 'l2tp_sh_sess_tie_breaker_enabled', 'l2tp_sh_sess_tie_breaker', 'is_session_manual', 'is_session_up', 'is_udp_checksum_enabled', 'is_sequencing_on', 'is_session_state_established', 'is_session_locally_initiated', 'is_conditional_debug_enabled', 'unique_id', 'interface_name'], name, value)


                    class SessionApplicationData(_Entity_):
                        """
                        Session application data
                        
                        .. attribute:: xconnect
                        
                        	Xconnect data
                        	**type**\:  :py:class:`Xconnect <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Nodes.Node.Sessions.Session.SessionApplicationData.Xconnect>`
                        
                        	**config**\: False
                        
                        .. attribute:: vpdn
                        
                        	VPDN data
                        	**type**\:  :py:class:`Vpdn <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Nodes.Node.Sessions.Session.SessionApplicationData.Vpdn>`
                        
                        	**config**\: False
                        
                        .. attribute:: l2tp_sh_sess_app_type
                        
                        	l2tp sh sess app type
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'tunnel-l2tun-oper'
                        _revision = '2018-11-01'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(L2tpv2.Nodes.Node.Sessions.Session.SessionApplicationData, self).__init__()

                            self.yang_name = "session-application-data"
                            self.yang_parent_name = "session"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("xconnect", ("xconnect", L2tpv2.Nodes.Node.Sessions.Session.SessionApplicationData.Xconnect)), ("vpdn", ("vpdn", L2tpv2.Nodes.Node.Sessions.Session.SessionApplicationData.Vpdn))])
                            self._leafs = OrderedDict([
                                ('l2tp_sh_sess_app_type', (YLeaf(YType.uint32, 'l2tp-sh-sess-app-type'), ['int'])),
                            ])
                            self.l2tp_sh_sess_app_type = None

                            self.xconnect = L2tpv2.Nodes.Node.Sessions.Session.SessionApplicationData.Xconnect()
                            self.xconnect.parent = self
                            self._children_name_map["xconnect"] = "xconnect"

                            self.vpdn = L2tpv2.Nodes.Node.Sessions.Session.SessionApplicationData.Vpdn()
                            self.vpdn.parent = self
                            self._children_name_map["vpdn"] = "vpdn"
                            self._segment_path = lambda: "session-application-data"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2tpv2.Nodes.Node.Sessions.Session.SessionApplicationData, ['l2tp_sh_sess_app_type'], name, value)


                        class Xconnect(_Entity_):
                            """
                            Xconnect data
                            
                            .. attribute:: circuit_name
                            
                            	Circuit name
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: sessionvc_id
                            
                            	Session VC ID
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: is_circuit_state_up
                            
                            	True if circuit state is up
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: is_local_circuit_state_up
                            
                            	True if local circuit state is up
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: is_remote_circuit_state_up
                            
                            	True if remote circuit state is up
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: ipv6_protocol_tunneling
                            
                            	IPv6ProtocolTunneling
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'tunnel-l2tun-oper'
                            _revision = '2018-11-01'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(L2tpv2.Nodes.Node.Sessions.Session.SessionApplicationData.Xconnect, self).__init__()

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
                                self._perform_setattr(L2tpv2.Nodes.Node.Sessions.Session.SessionApplicationData.Xconnect, ['circuit_name', 'sessionvc_id', 'is_circuit_state_up', 'is_local_circuit_state_up', 'is_remote_circuit_state_up', 'ipv6_protocol_tunneling'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                                return meta._meta_table['L2tpv2.Nodes.Node.Sessions.Session.SessionApplicationData.Xconnect']['meta_info']


                        class Vpdn(_Entity_):
                            """
                            VPDN data
                            
                            .. attribute:: username
                            
                            	Session username
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: interface_name
                            
                            	Interface name
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'tunnel-l2tun-oper'
                            _revision = '2018-11-01'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(L2tpv2.Nodes.Node.Sessions.Session.SessionApplicationData.Vpdn, self).__init__()

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
                                self._perform_setattr(L2tpv2.Nodes.Node.Sessions.Session.SessionApplicationData.Vpdn, ['username', 'interface_name'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                                return meta._meta_table['L2tpv2.Nodes.Node.Sessions.Session.SessionApplicationData.Vpdn']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                            return meta._meta_table['L2tpv2.Nodes.Node.Sessions.Session.SessionApplicationData']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                        return meta._meta_table['L2tpv2.Nodes.Node.Sessions.Session']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                    return meta._meta_table['L2tpv2.Nodes.Node.Sessions']['meta_info']


            class Session(_Entity_):
                """
                L2TP control messages counters
                
                .. attribute:: unavailable
                
                	L2TP session unavailable  information
                	**type**\:  :py:class:`Unavailable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Nodes.Node.Session.Unavailable>`
                
                	**config**\: False
                
                

                """

                _prefix = 'tunnel-l2tun-oper'
                _revision = '2018-11-01'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(L2tpv2.Nodes.Node.Session, self).__init__()

                    self.yang_name = "session"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("unavailable", ("unavailable", L2tpv2.Nodes.Node.Session.Unavailable))])
                    self._leafs = OrderedDict()

                    self.unavailable = L2tpv2.Nodes.Node.Session.Unavailable()
                    self.unavailable.parent = self
                    self._children_name_map["unavailable"] = "unavailable"
                    self._segment_path = lambda: "session"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(L2tpv2.Nodes.Node.Session, [], name, value)


                class Unavailable(_Entity_):
                    """
                    L2TP session unavailable  information
                    
                    .. attribute:: sessions_on_hold
                    
                    	Number of session ID in hold database
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'tunnel-l2tun-oper'
                    _revision = '2018-11-01'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(L2tpv2.Nodes.Node.Session.Unavailable, self).__init__()

                        self.yang_name = "unavailable"
                        self.yang_parent_name = "session"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('sessions_on_hold', (YLeaf(YType.uint32, 'sessions-on-hold'), ['int'])),
                        ])
                        self.sessions_on_hold = None
                        self._segment_path = lambda: "unavailable"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2tpv2.Nodes.Node.Session.Unavailable, ['sessions_on_hold'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                        return meta._meta_table['L2tpv2.Nodes.Node.Session.Unavailable']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                    return meta._meta_table['L2tpv2.Nodes.Node.Session']['meta_info']


            class Internal(_Entity_):
                """
                L2TP v2/v3 internal information
                
                .. attribute:: internal_stats
                
                	internal stats
                	**type**\:  :py:class:`InternalStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Nodes.Node.Internal.InternalStats>`
                
                	**config**\: False
                
                .. attribute:: internal_stats_last_clear
                
                	internal stats last clear
                	**type**\:  :py:class:`InternalStatsLastClear <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2tpv2.Nodes.Node.Internal.InternalStatsLastClear>`
                
                	**config**\: False
                
                .. attribute:: time_last_clear
                
                	time last clear
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                

                """

                _prefix = 'tunnel-l2tun-oper'
                _revision = '2018-11-01'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(L2tpv2.Nodes.Node.Internal, self).__init__()

                    self.yang_name = "internal"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("internal-stats", ("internal_stats", L2tpv2.Nodes.Node.Internal.InternalStats)), ("internal-stats-last-clear", ("internal_stats_last_clear", L2tpv2.Nodes.Node.Internal.InternalStatsLastClear))])
                    self._leafs = OrderedDict([
                        ('time_last_clear', (YLeaf(YType.uint32, 'time-last-clear'), ['int'])),
                    ])
                    self.time_last_clear = None

                    self.internal_stats = L2tpv2.Nodes.Node.Internal.InternalStats()
                    self.internal_stats.parent = self
                    self._children_name_map["internal_stats"] = "internal-stats"

                    self.internal_stats_last_clear = L2tpv2.Nodes.Node.Internal.InternalStatsLastClear()
                    self.internal_stats_last_clear.parent = self
                    self._children_name_map["internal_stats_last_clear"] = "internal-stats-last-clear"
                    self._segment_path = lambda: "internal"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(L2tpv2.Nodes.Node.Internal, ['time_last_clear'], name, value)


                class InternalStats(_Entity_):
                    """
                    internal stats
                    
                    .. attribute:: l2tp_sh_l2x_num_tunnels
                    
                    	l2tp sh l2x num tunnels
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_sessions
                    
                    	l2tp sh l2x num sessions
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_rx_high_water_mark
                    
                    	l2tp sh l2x rx high water mark
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_ave_msg_process_usecs
                    
                    	l2tp sh l2x ave msg process usecs
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_rx_msgs
                    
                    	l2tp sh l2x num rx msgs
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_tx_msgs
                    
                    	l2tp sh l2x num tx msgs
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_tx_err_drops
                    
                    	l2tp sh l2x num tx err drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_tx_conn_drops
                    
                    	l2tp sh l2x num tx conn drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_reordered_msgs
                    
                    	l2tp sh l2x num reordered msgs
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_max_reorder_deviation
                    
                    	l2tp sh l2x max reorder deviation
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_ooo_msgs
                    
                    	l2tp sh l2x num ooo msgs
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_rx_path_drops
                    
                    	l2tp sh l2x num rx path drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_rx_path_data_pkt_drops
                    
                    	l2tp sh l2x num rx path data pkt drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_rx_queue_drops
                    
                    	l2tp sh l2x num rx queue drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_rx_ooo_drops
                    
                    	l2tp sh l2x num rx ooo drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_buffered_msgs
                    
                    	l2tp sh l2x num buffered msgs
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_mutex_block
                    
                    	l2tp sh l2x num mutex block
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_bad_len_drops
                    
                    	l2tp sh l2x num bad len drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_bad_avp_drops
                    
                    	l2tp sh l2x num bad avp drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_missing_cc_id_drops
                    
                    	l2tp sh l2x num missing cc id drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_missing_sess_id_drops
                    
                    	l2tp sh l2x num missing sess id drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_mismatch_cc_id_drops
                    
                    	l2tp sh l2x num mismatch cc id drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_unknown_cc_drops
                    
                    	l2tp sh l2x num unknown cc drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_unknown_sess_drops
                    
                    	l2tp sh l2x num unknown sess drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_linear_id_search
                    
                    	l2tp sh l2x num linear id search
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_linear_id_search_fail
                    
                    	l2tp sh l2x num linear id search fail
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_netio_pkt_rx
                    
                    	l2tp sh l2x num netio pkt rx
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2tun_ave_msg_process_usecs
                    
                    	l2tp sh l2tun ave msg process usecs
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2tun_num_rx_msgs
                    
                    	l2tp sh l2tun num rx msgs
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2tun_num_tx_msgs
                    
                    	l2tp sh l2tun num tx msgs
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_l2tun_socket_ens_send_error_cnt
                    
                    	l2tp l2tun socket ens send error cnt
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_l2tun_socket_session_accept
                    
                    	l2tp l2tun socket session accept
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_l2tun_socket_session_destroy
                    
                    	l2tp l2tun socket session destroy
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_l2tun_socket_session_connect
                    
                    	l2tp l2tun socket session connect
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_l2tun_socket_session_connect_continue
                    
                    	l2tp l2tun socket session connect continue
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_l2tun_session_connecting
                    
                    	l2tp l2tun session connecting
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_l2tun_session_connected
                    
                    	l2tp l2tun session connected
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_l2tun_session_disconnected
                    
                    	l2tp l2tun session disconnected
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_l2tun_session_incoming
                    
                    	l2tp l2tun session incoming
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_l2tun_session_updated
                    
                    	l2tp l2tun session updated
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_l2tun_session_circuit_status
                    
                    	l2tp l2tun session circuit status
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: l2x_lpts_pa_stats_setup_cnt
                    
                    	l2x lpts pa stats setup cnt
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2x_lpts_pa_stats_destroy_cnt
                    
                    	l2x lpts pa stats destroy cnt
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2x_lpts_pa_stats_alloc_cnt
                    
                    	l2x lpts pa stats alloc cnt
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2x_lpts_pa_stats_alloc_fail_cnt
                    
                    	l2x lpts pa stats alloc fail cnt
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2x_lpts_pa_stats_init_cnt
                    
                    	l2x lpts pa stats init cnt
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2x_lpts_pa_stats_init_fail_cnt
                    
                    	l2x lpts pa stats init fail cnt
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2x_lpts_pa_stats_free_cnt
                    
                    	l2x lpts pa stats free cnt
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2x_lpts_pa_stats_pulse_cnt
                    
                    	l2x lpts pa stats pulse cnt
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2x_lpts_pa_stats_pulse_fail_cnt
                    
                    	l2x lpts pa stats pulse fail cnt
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2x_lpts_pa_stats_bind_cnt
                    
                    	l2x lpts pa stats bind cnt
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2x_lpts_pa_stats_bind_fail_cnt
                    
                    	l2x lpts pa stats bind fail cnt
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2x_lpts_pa_stats_bind_batch_cnt
                    
                    	l2x lpts pa stats bind batch cnt
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2x_lpts_pa_stats_bind_batch_fail_cnt
                    
                    	l2x lpts pa stats bind batch fail cnt
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2x_lpts_pa_stats_bind_time
                    
                    	l2x lpts pa stats bind time
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2x_lpts_pa_stats_expire_cnt
                    
                    	l2x lpts pa stats expire cnt
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2x_lpts_pa_stats_replay_cnt
                    
                    	l2x lpts pa stats replay cnt
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2x_lpts_pa_stats_replay_batch_cnt
                    
                    	l2x lpts pa stats replay batch cnt
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2x_lpts_pa_stats_replay_time
                    
                    	l2x lpts pa stats replay time
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'tunnel-l2tun-oper'
                    _revision = '2018-11-01'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(L2tpv2.Nodes.Node.Internal.InternalStats, self).__init__()

                        self.yang_name = "internal-stats"
                        self.yang_parent_name = "internal"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('l2tp_sh_l2x_num_tunnels', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-tunnels'), ['int'])),
                            ('l2tp_sh_l2x_num_sessions', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-sessions'), ['int'])),
                            ('l2tp_sh_l2x_rx_high_water_mark', (YLeaf(YType.uint32, 'l2tp-sh-l2x-rx-high-water-mark'), ['int'])),
                            ('l2tp_sh_l2x_ave_msg_process_usecs', (YLeaf(YType.uint64, 'l2tp-sh-l2x-ave-msg-process-usecs'), ['int'])),
                            ('l2tp_sh_l2x_num_rx_msgs', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-rx-msgs'), ['int'])),
                            ('l2tp_sh_l2x_num_tx_msgs', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-tx-msgs'), ['int'])),
                            ('l2tp_sh_l2x_num_tx_err_drops', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-tx-err-drops'), ['int'])),
                            ('l2tp_sh_l2x_num_tx_conn_drops', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-tx-conn-drops'), ['int'])),
                            ('l2tp_sh_l2x_num_reordered_msgs', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-reordered-msgs'), ['int'])),
                            ('l2tp_sh_l2x_max_reorder_deviation', (YLeaf(YType.uint32, 'l2tp-sh-l2x-max-reorder-deviation'), ['int'])),
                            ('l2tp_sh_l2x_num_ooo_msgs', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-ooo-msgs'), ['int'])),
                            ('l2tp_sh_l2x_num_rx_path_drops', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-rx-path-drops'), ['int'])),
                            ('l2tp_sh_l2x_num_rx_path_data_pkt_drops', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-rx-path-data-pkt-drops'), ['int'])),
                            ('l2tp_sh_l2x_num_rx_queue_drops', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-rx-queue-drops'), ['int'])),
                            ('l2tp_sh_l2x_num_rx_ooo_drops', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-rx-ooo-drops'), ['int'])),
                            ('l2tp_sh_l2x_num_buffered_msgs', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-buffered-msgs'), ['int'])),
                            ('l2tp_sh_l2x_num_mutex_block', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-mutex-block'), ['int'])),
                            ('l2tp_sh_l2x_num_bad_len_drops', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-bad-len-drops'), ['int'])),
                            ('l2tp_sh_l2x_num_bad_avp_drops', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-bad-avp-drops'), ['int'])),
                            ('l2tp_sh_l2x_num_missing_cc_id_drops', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-missing-cc-id-drops'), ['int'])),
                            ('l2tp_sh_l2x_num_missing_sess_id_drops', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-missing-sess-id-drops'), ['int'])),
                            ('l2tp_sh_l2x_num_mismatch_cc_id_drops', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-mismatch-cc-id-drops'), ['int'])),
                            ('l2tp_sh_l2x_num_unknown_cc_drops', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-unknown-cc-drops'), ['int'])),
                            ('l2tp_sh_l2x_num_unknown_sess_drops', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-unknown-sess-drops'), ['int'])),
                            ('l2tp_sh_l2x_num_linear_id_search', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-linear-id-search'), ['int'])),
                            ('l2tp_sh_l2x_num_linear_id_search_fail', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-linear-id-search-fail'), ['int'])),
                            ('l2tp_sh_l2x_num_netio_pkt_rx', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-netio-pkt-rx'), ['int'])),
                            ('l2tp_sh_l2tun_ave_msg_process_usecs', (YLeaf(YType.uint64, 'l2tp-sh-l2tun-ave-msg-process-usecs'), ['int'])),
                            ('l2tp_sh_l2tun_num_rx_msgs', (YLeaf(YType.uint32, 'l2tp-sh-l2tun-num-rx-msgs'), ['int'])),
                            ('l2tp_sh_l2tun_num_tx_msgs', (YLeaf(YType.uint32, 'l2tp-sh-l2tun-num-tx-msgs'), ['int'])),
                            ('l2tp_l2tun_socket_ens_send_error_cnt', (YLeaf(YType.uint32, 'l2tp-l2tun-socket-ens-send-error-cnt'), ['int'])),
                            ('l2tp_l2tun_socket_session_accept', (YLeaf(YType.uint64, 'l2tp-l2tun-socket-session-accept'), ['int'])),
                            ('l2tp_l2tun_socket_session_destroy', (YLeaf(YType.uint64, 'l2tp-l2tun-socket-session-destroy'), ['int'])),
                            ('l2tp_l2tun_socket_session_connect', (YLeaf(YType.uint64, 'l2tp-l2tun-socket-session-connect'), ['int'])),
                            ('l2tp_l2tun_socket_session_connect_continue', (YLeaf(YType.uint64, 'l2tp-l2tun-socket-session-connect-continue'), ['int'])),
                            ('l2tp_l2tun_session_connecting', (YLeaf(YType.uint64, 'l2tp-l2tun-session-connecting'), ['int'])),
                            ('l2tp_l2tun_session_connected', (YLeaf(YType.uint64, 'l2tp-l2tun-session-connected'), ['int'])),
                            ('l2tp_l2tun_session_disconnected', (YLeaf(YType.uint64, 'l2tp-l2tun-session-disconnected'), ['int'])),
                            ('l2tp_l2tun_session_incoming', (YLeaf(YType.uint64, 'l2tp-l2tun-session-incoming'), ['int'])),
                            ('l2tp_l2tun_session_updated', (YLeaf(YType.uint64, 'l2tp-l2tun-session-updated'), ['int'])),
                            ('l2tp_l2tun_session_circuit_status', (YLeaf(YType.uint64, 'l2tp-l2tun-session-circuit-status'), ['int'])),
                            ('l2x_lpts_pa_stats_setup_cnt', (YLeaf(YType.uint32, 'l2x-lpts-pa-stats-setup-cnt'), ['int'])),
                            ('l2x_lpts_pa_stats_destroy_cnt', (YLeaf(YType.uint32, 'l2x-lpts-pa-stats-destroy-cnt'), ['int'])),
                            ('l2x_lpts_pa_stats_alloc_cnt', (YLeaf(YType.uint32, 'l2x-lpts-pa-stats-alloc-cnt'), ['int'])),
                            ('l2x_lpts_pa_stats_alloc_fail_cnt', (YLeaf(YType.uint32, 'l2x-lpts-pa-stats-alloc-fail-cnt'), ['int'])),
                            ('l2x_lpts_pa_stats_init_cnt', (YLeaf(YType.uint32, 'l2x-lpts-pa-stats-init-cnt'), ['int'])),
                            ('l2x_lpts_pa_stats_init_fail_cnt', (YLeaf(YType.uint32, 'l2x-lpts-pa-stats-init-fail-cnt'), ['int'])),
                            ('l2x_lpts_pa_stats_free_cnt', (YLeaf(YType.uint32, 'l2x-lpts-pa-stats-free-cnt'), ['int'])),
                            ('l2x_lpts_pa_stats_pulse_cnt', (YLeaf(YType.uint32, 'l2x-lpts-pa-stats-pulse-cnt'), ['int'])),
                            ('l2x_lpts_pa_stats_pulse_fail_cnt', (YLeaf(YType.uint32, 'l2x-lpts-pa-stats-pulse-fail-cnt'), ['int'])),
                            ('l2x_lpts_pa_stats_bind_cnt', (YLeaf(YType.uint32, 'l2x-lpts-pa-stats-bind-cnt'), ['int'])),
                            ('l2x_lpts_pa_stats_bind_fail_cnt', (YLeaf(YType.uint32, 'l2x-lpts-pa-stats-bind-fail-cnt'), ['int'])),
                            ('l2x_lpts_pa_stats_bind_batch_cnt', (YLeaf(YType.uint32, 'l2x-lpts-pa-stats-bind-batch-cnt'), ['int'])),
                            ('l2x_lpts_pa_stats_bind_batch_fail_cnt', (YLeaf(YType.uint32, 'l2x-lpts-pa-stats-bind-batch-fail-cnt'), ['int'])),
                            ('l2x_lpts_pa_stats_bind_time', (YLeaf(YType.uint32, 'l2x-lpts-pa-stats-bind-time'), ['int'])),
                            ('l2x_lpts_pa_stats_expire_cnt', (YLeaf(YType.uint32, 'l2x-lpts-pa-stats-expire-cnt'), ['int'])),
                            ('l2x_lpts_pa_stats_replay_cnt', (YLeaf(YType.uint32, 'l2x-lpts-pa-stats-replay-cnt'), ['int'])),
                            ('l2x_lpts_pa_stats_replay_batch_cnt', (YLeaf(YType.uint32, 'l2x-lpts-pa-stats-replay-batch-cnt'), ['int'])),
                            ('l2x_lpts_pa_stats_replay_time', (YLeaf(YType.uint32, 'l2x-lpts-pa-stats-replay-time'), ['int'])),
                        ])
                        self.l2tp_sh_l2x_num_tunnels = None
                        self.l2tp_sh_l2x_num_sessions = None
                        self.l2tp_sh_l2x_rx_high_water_mark = None
                        self.l2tp_sh_l2x_ave_msg_process_usecs = None
                        self.l2tp_sh_l2x_num_rx_msgs = None
                        self.l2tp_sh_l2x_num_tx_msgs = None
                        self.l2tp_sh_l2x_num_tx_err_drops = None
                        self.l2tp_sh_l2x_num_tx_conn_drops = None
                        self.l2tp_sh_l2x_num_reordered_msgs = None
                        self.l2tp_sh_l2x_max_reorder_deviation = None
                        self.l2tp_sh_l2x_num_ooo_msgs = None
                        self.l2tp_sh_l2x_num_rx_path_drops = None
                        self.l2tp_sh_l2x_num_rx_path_data_pkt_drops = None
                        self.l2tp_sh_l2x_num_rx_queue_drops = None
                        self.l2tp_sh_l2x_num_rx_ooo_drops = None
                        self.l2tp_sh_l2x_num_buffered_msgs = None
                        self.l2tp_sh_l2x_num_mutex_block = None
                        self.l2tp_sh_l2x_num_bad_len_drops = None
                        self.l2tp_sh_l2x_num_bad_avp_drops = None
                        self.l2tp_sh_l2x_num_missing_cc_id_drops = None
                        self.l2tp_sh_l2x_num_missing_sess_id_drops = None
                        self.l2tp_sh_l2x_num_mismatch_cc_id_drops = None
                        self.l2tp_sh_l2x_num_unknown_cc_drops = None
                        self.l2tp_sh_l2x_num_unknown_sess_drops = None
                        self.l2tp_sh_l2x_num_linear_id_search = None
                        self.l2tp_sh_l2x_num_linear_id_search_fail = None
                        self.l2tp_sh_l2x_num_netio_pkt_rx = None
                        self.l2tp_sh_l2tun_ave_msg_process_usecs = None
                        self.l2tp_sh_l2tun_num_rx_msgs = None
                        self.l2tp_sh_l2tun_num_tx_msgs = None
                        self.l2tp_l2tun_socket_ens_send_error_cnt = None
                        self.l2tp_l2tun_socket_session_accept = None
                        self.l2tp_l2tun_socket_session_destroy = None
                        self.l2tp_l2tun_socket_session_connect = None
                        self.l2tp_l2tun_socket_session_connect_continue = None
                        self.l2tp_l2tun_session_connecting = None
                        self.l2tp_l2tun_session_connected = None
                        self.l2tp_l2tun_session_disconnected = None
                        self.l2tp_l2tun_session_incoming = None
                        self.l2tp_l2tun_session_updated = None
                        self.l2tp_l2tun_session_circuit_status = None
                        self.l2x_lpts_pa_stats_setup_cnt = None
                        self.l2x_lpts_pa_stats_destroy_cnt = None
                        self.l2x_lpts_pa_stats_alloc_cnt = None
                        self.l2x_lpts_pa_stats_alloc_fail_cnt = None
                        self.l2x_lpts_pa_stats_init_cnt = None
                        self.l2x_lpts_pa_stats_init_fail_cnt = None
                        self.l2x_lpts_pa_stats_free_cnt = None
                        self.l2x_lpts_pa_stats_pulse_cnt = None
                        self.l2x_lpts_pa_stats_pulse_fail_cnt = None
                        self.l2x_lpts_pa_stats_bind_cnt = None
                        self.l2x_lpts_pa_stats_bind_fail_cnt = None
                        self.l2x_lpts_pa_stats_bind_batch_cnt = None
                        self.l2x_lpts_pa_stats_bind_batch_fail_cnt = None
                        self.l2x_lpts_pa_stats_bind_time = None
                        self.l2x_lpts_pa_stats_expire_cnt = None
                        self.l2x_lpts_pa_stats_replay_cnt = None
                        self.l2x_lpts_pa_stats_replay_batch_cnt = None
                        self.l2x_lpts_pa_stats_replay_time = None
                        self._segment_path = lambda: "internal-stats"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2tpv2.Nodes.Node.Internal.InternalStats, ['l2tp_sh_l2x_num_tunnels', 'l2tp_sh_l2x_num_sessions', 'l2tp_sh_l2x_rx_high_water_mark', 'l2tp_sh_l2x_ave_msg_process_usecs', 'l2tp_sh_l2x_num_rx_msgs', 'l2tp_sh_l2x_num_tx_msgs', 'l2tp_sh_l2x_num_tx_err_drops', 'l2tp_sh_l2x_num_tx_conn_drops', 'l2tp_sh_l2x_num_reordered_msgs', 'l2tp_sh_l2x_max_reorder_deviation', 'l2tp_sh_l2x_num_ooo_msgs', 'l2tp_sh_l2x_num_rx_path_drops', 'l2tp_sh_l2x_num_rx_path_data_pkt_drops', 'l2tp_sh_l2x_num_rx_queue_drops', 'l2tp_sh_l2x_num_rx_ooo_drops', 'l2tp_sh_l2x_num_buffered_msgs', 'l2tp_sh_l2x_num_mutex_block', 'l2tp_sh_l2x_num_bad_len_drops', 'l2tp_sh_l2x_num_bad_avp_drops', 'l2tp_sh_l2x_num_missing_cc_id_drops', 'l2tp_sh_l2x_num_missing_sess_id_drops', 'l2tp_sh_l2x_num_mismatch_cc_id_drops', 'l2tp_sh_l2x_num_unknown_cc_drops', 'l2tp_sh_l2x_num_unknown_sess_drops', 'l2tp_sh_l2x_num_linear_id_search', 'l2tp_sh_l2x_num_linear_id_search_fail', 'l2tp_sh_l2x_num_netio_pkt_rx', 'l2tp_sh_l2tun_ave_msg_process_usecs', 'l2tp_sh_l2tun_num_rx_msgs', 'l2tp_sh_l2tun_num_tx_msgs', 'l2tp_l2tun_socket_ens_send_error_cnt', 'l2tp_l2tun_socket_session_accept', 'l2tp_l2tun_socket_session_destroy', 'l2tp_l2tun_socket_session_connect', 'l2tp_l2tun_socket_session_connect_continue', 'l2tp_l2tun_session_connecting', 'l2tp_l2tun_session_connected', 'l2tp_l2tun_session_disconnected', 'l2tp_l2tun_session_incoming', 'l2tp_l2tun_session_updated', 'l2tp_l2tun_session_circuit_status', 'l2x_lpts_pa_stats_setup_cnt', 'l2x_lpts_pa_stats_destroy_cnt', 'l2x_lpts_pa_stats_alloc_cnt', 'l2x_lpts_pa_stats_alloc_fail_cnt', 'l2x_lpts_pa_stats_init_cnt', 'l2x_lpts_pa_stats_init_fail_cnt', 'l2x_lpts_pa_stats_free_cnt', 'l2x_lpts_pa_stats_pulse_cnt', 'l2x_lpts_pa_stats_pulse_fail_cnt', 'l2x_lpts_pa_stats_bind_cnt', 'l2x_lpts_pa_stats_bind_fail_cnt', 'l2x_lpts_pa_stats_bind_batch_cnt', 'l2x_lpts_pa_stats_bind_batch_fail_cnt', 'l2x_lpts_pa_stats_bind_time', 'l2x_lpts_pa_stats_expire_cnt', 'l2x_lpts_pa_stats_replay_cnt', 'l2x_lpts_pa_stats_replay_batch_cnt', 'l2x_lpts_pa_stats_replay_time'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                        return meta._meta_table['L2tpv2.Nodes.Node.Internal.InternalStats']['meta_info']


                class InternalStatsLastClear(_Entity_):
                    """
                    internal stats last clear
                    
                    .. attribute:: l2tp_sh_l2x_num_tunnels
                    
                    	l2tp sh l2x num tunnels
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_sessions
                    
                    	l2tp sh l2x num sessions
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_rx_high_water_mark
                    
                    	l2tp sh l2x rx high water mark
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_ave_msg_process_usecs
                    
                    	l2tp sh l2x ave msg process usecs
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_rx_msgs
                    
                    	l2tp sh l2x num rx msgs
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_tx_msgs
                    
                    	l2tp sh l2x num tx msgs
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_tx_err_drops
                    
                    	l2tp sh l2x num tx err drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_tx_conn_drops
                    
                    	l2tp sh l2x num tx conn drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_reordered_msgs
                    
                    	l2tp sh l2x num reordered msgs
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_max_reorder_deviation
                    
                    	l2tp sh l2x max reorder deviation
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_ooo_msgs
                    
                    	l2tp sh l2x num ooo msgs
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_rx_path_drops
                    
                    	l2tp sh l2x num rx path drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_rx_path_data_pkt_drops
                    
                    	l2tp sh l2x num rx path data pkt drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_rx_queue_drops
                    
                    	l2tp sh l2x num rx queue drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_rx_ooo_drops
                    
                    	l2tp sh l2x num rx ooo drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_buffered_msgs
                    
                    	l2tp sh l2x num buffered msgs
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_mutex_block
                    
                    	l2tp sh l2x num mutex block
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_bad_len_drops
                    
                    	l2tp sh l2x num bad len drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_bad_avp_drops
                    
                    	l2tp sh l2x num bad avp drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_missing_cc_id_drops
                    
                    	l2tp sh l2x num missing cc id drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_missing_sess_id_drops
                    
                    	l2tp sh l2x num missing sess id drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_mismatch_cc_id_drops
                    
                    	l2tp sh l2x num mismatch cc id drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_unknown_cc_drops
                    
                    	l2tp sh l2x num unknown cc drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_unknown_sess_drops
                    
                    	l2tp sh l2x num unknown sess drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_linear_id_search
                    
                    	l2tp sh l2x num linear id search
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_linear_id_search_fail
                    
                    	l2tp sh l2x num linear id search fail
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2x_num_netio_pkt_rx
                    
                    	l2tp sh l2x num netio pkt rx
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2tun_ave_msg_process_usecs
                    
                    	l2tp sh l2tun ave msg process usecs
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2tun_num_rx_msgs
                    
                    	l2tp sh l2tun num rx msgs
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_sh_l2tun_num_tx_msgs
                    
                    	l2tp sh l2tun num tx msgs
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_l2tun_socket_ens_send_error_cnt
                    
                    	l2tp l2tun socket ens send error cnt
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_l2tun_socket_session_accept
                    
                    	l2tp l2tun socket session accept
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_l2tun_socket_session_destroy
                    
                    	l2tp l2tun socket session destroy
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_l2tun_socket_session_connect
                    
                    	l2tp l2tun socket session connect
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_l2tun_socket_session_connect_continue
                    
                    	l2tp l2tun socket session connect continue
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_l2tun_session_connecting
                    
                    	l2tp l2tun session connecting
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_l2tun_session_connected
                    
                    	l2tp l2tun session connected
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_l2tun_session_disconnected
                    
                    	l2tp l2tun session disconnected
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_l2tun_session_incoming
                    
                    	l2tp l2tun session incoming
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_l2tun_session_updated
                    
                    	l2tp l2tun session updated
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp_l2tun_session_circuit_status
                    
                    	l2tp l2tun session circuit status
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: l2x_lpts_pa_stats_setup_cnt
                    
                    	l2x lpts pa stats setup cnt
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2x_lpts_pa_stats_destroy_cnt
                    
                    	l2x lpts pa stats destroy cnt
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2x_lpts_pa_stats_alloc_cnt
                    
                    	l2x lpts pa stats alloc cnt
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2x_lpts_pa_stats_alloc_fail_cnt
                    
                    	l2x lpts pa stats alloc fail cnt
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2x_lpts_pa_stats_init_cnt
                    
                    	l2x lpts pa stats init cnt
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2x_lpts_pa_stats_init_fail_cnt
                    
                    	l2x lpts pa stats init fail cnt
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2x_lpts_pa_stats_free_cnt
                    
                    	l2x lpts pa stats free cnt
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2x_lpts_pa_stats_pulse_cnt
                    
                    	l2x lpts pa stats pulse cnt
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2x_lpts_pa_stats_pulse_fail_cnt
                    
                    	l2x lpts pa stats pulse fail cnt
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2x_lpts_pa_stats_bind_cnt
                    
                    	l2x lpts pa stats bind cnt
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2x_lpts_pa_stats_bind_fail_cnt
                    
                    	l2x lpts pa stats bind fail cnt
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2x_lpts_pa_stats_bind_batch_cnt
                    
                    	l2x lpts pa stats bind batch cnt
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2x_lpts_pa_stats_bind_batch_fail_cnt
                    
                    	l2x lpts pa stats bind batch fail cnt
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2x_lpts_pa_stats_bind_time
                    
                    	l2x lpts pa stats bind time
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2x_lpts_pa_stats_expire_cnt
                    
                    	l2x lpts pa stats expire cnt
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2x_lpts_pa_stats_replay_cnt
                    
                    	l2x lpts pa stats replay cnt
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2x_lpts_pa_stats_replay_batch_cnt
                    
                    	l2x lpts pa stats replay batch cnt
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: l2x_lpts_pa_stats_replay_time
                    
                    	l2x lpts pa stats replay time
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'tunnel-l2tun-oper'
                    _revision = '2018-11-01'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(L2tpv2.Nodes.Node.Internal.InternalStatsLastClear, self).__init__()

                        self.yang_name = "internal-stats-last-clear"
                        self.yang_parent_name = "internal"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('l2tp_sh_l2x_num_tunnels', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-tunnels'), ['int'])),
                            ('l2tp_sh_l2x_num_sessions', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-sessions'), ['int'])),
                            ('l2tp_sh_l2x_rx_high_water_mark', (YLeaf(YType.uint32, 'l2tp-sh-l2x-rx-high-water-mark'), ['int'])),
                            ('l2tp_sh_l2x_ave_msg_process_usecs', (YLeaf(YType.uint64, 'l2tp-sh-l2x-ave-msg-process-usecs'), ['int'])),
                            ('l2tp_sh_l2x_num_rx_msgs', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-rx-msgs'), ['int'])),
                            ('l2tp_sh_l2x_num_tx_msgs', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-tx-msgs'), ['int'])),
                            ('l2tp_sh_l2x_num_tx_err_drops', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-tx-err-drops'), ['int'])),
                            ('l2tp_sh_l2x_num_tx_conn_drops', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-tx-conn-drops'), ['int'])),
                            ('l2tp_sh_l2x_num_reordered_msgs', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-reordered-msgs'), ['int'])),
                            ('l2tp_sh_l2x_max_reorder_deviation', (YLeaf(YType.uint32, 'l2tp-sh-l2x-max-reorder-deviation'), ['int'])),
                            ('l2tp_sh_l2x_num_ooo_msgs', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-ooo-msgs'), ['int'])),
                            ('l2tp_sh_l2x_num_rx_path_drops', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-rx-path-drops'), ['int'])),
                            ('l2tp_sh_l2x_num_rx_path_data_pkt_drops', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-rx-path-data-pkt-drops'), ['int'])),
                            ('l2tp_sh_l2x_num_rx_queue_drops', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-rx-queue-drops'), ['int'])),
                            ('l2tp_sh_l2x_num_rx_ooo_drops', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-rx-ooo-drops'), ['int'])),
                            ('l2tp_sh_l2x_num_buffered_msgs', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-buffered-msgs'), ['int'])),
                            ('l2tp_sh_l2x_num_mutex_block', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-mutex-block'), ['int'])),
                            ('l2tp_sh_l2x_num_bad_len_drops', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-bad-len-drops'), ['int'])),
                            ('l2tp_sh_l2x_num_bad_avp_drops', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-bad-avp-drops'), ['int'])),
                            ('l2tp_sh_l2x_num_missing_cc_id_drops', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-missing-cc-id-drops'), ['int'])),
                            ('l2tp_sh_l2x_num_missing_sess_id_drops', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-missing-sess-id-drops'), ['int'])),
                            ('l2tp_sh_l2x_num_mismatch_cc_id_drops', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-mismatch-cc-id-drops'), ['int'])),
                            ('l2tp_sh_l2x_num_unknown_cc_drops', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-unknown-cc-drops'), ['int'])),
                            ('l2tp_sh_l2x_num_unknown_sess_drops', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-unknown-sess-drops'), ['int'])),
                            ('l2tp_sh_l2x_num_linear_id_search', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-linear-id-search'), ['int'])),
                            ('l2tp_sh_l2x_num_linear_id_search_fail', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-linear-id-search-fail'), ['int'])),
                            ('l2tp_sh_l2x_num_netio_pkt_rx', (YLeaf(YType.uint32, 'l2tp-sh-l2x-num-netio-pkt-rx'), ['int'])),
                            ('l2tp_sh_l2tun_ave_msg_process_usecs', (YLeaf(YType.uint64, 'l2tp-sh-l2tun-ave-msg-process-usecs'), ['int'])),
                            ('l2tp_sh_l2tun_num_rx_msgs', (YLeaf(YType.uint32, 'l2tp-sh-l2tun-num-rx-msgs'), ['int'])),
                            ('l2tp_sh_l2tun_num_tx_msgs', (YLeaf(YType.uint32, 'l2tp-sh-l2tun-num-tx-msgs'), ['int'])),
                            ('l2tp_l2tun_socket_ens_send_error_cnt', (YLeaf(YType.uint32, 'l2tp-l2tun-socket-ens-send-error-cnt'), ['int'])),
                            ('l2tp_l2tun_socket_session_accept', (YLeaf(YType.uint64, 'l2tp-l2tun-socket-session-accept'), ['int'])),
                            ('l2tp_l2tun_socket_session_destroy', (YLeaf(YType.uint64, 'l2tp-l2tun-socket-session-destroy'), ['int'])),
                            ('l2tp_l2tun_socket_session_connect', (YLeaf(YType.uint64, 'l2tp-l2tun-socket-session-connect'), ['int'])),
                            ('l2tp_l2tun_socket_session_connect_continue', (YLeaf(YType.uint64, 'l2tp-l2tun-socket-session-connect-continue'), ['int'])),
                            ('l2tp_l2tun_session_connecting', (YLeaf(YType.uint64, 'l2tp-l2tun-session-connecting'), ['int'])),
                            ('l2tp_l2tun_session_connected', (YLeaf(YType.uint64, 'l2tp-l2tun-session-connected'), ['int'])),
                            ('l2tp_l2tun_session_disconnected', (YLeaf(YType.uint64, 'l2tp-l2tun-session-disconnected'), ['int'])),
                            ('l2tp_l2tun_session_incoming', (YLeaf(YType.uint64, 'l2tp-l2tun-session-incoming'), ['int'])),
                            ('l2tp_l2tun_session_updated', (YLeaf(YType.uint64, 'l2tp-l2tun-session-updated'), ['int'])),
                            ('l2tp_l2tun_session_circuit_status', (YLeaf(YType.uint64, 'l2tp-l2tun-session-circuit-status'), ['int'])),
                            ('l2x_lpts_pa_stats_setup_cnt', (YLeaf(YType.uint32, 'l2x-lpts-pa-stats-setup-cnt'), ['int'])),
                            ('l2x_lpts_pa_stats_destroy_cnt', (YLeaf(YType.uint32, 'l2x-lpts-pa-stats-destroy-cnt'), ['int'])),
                            ('l2x_lpts_pa_stats_alloc_cnt', (YLeaf(YType.uint32, 'l2x-lpts-pa-stats-alloc-cnt'), ['int'])),
                            ('l2x_lpts_pa_stats_alloc_fail_cnt', (YLeaf(YType.uint32, 'l2x-lpts-pa-stats-alloc-fail-cnt'), ['int'])),
                            ('l2x_lpts_pa_stats_init_cnt', (YLeaf(YType.uint32, 'l2x-lpts-pa-stats-init-cnt'), ['int'])),
                            ('l2x_lpts_pa_stats_init_fail_cnt', (YLeaf(YType.uint32, 'l2x-lpts-pa-stats-init-fail-cnt'), ['int'])),
                            ('l2x_lpts_pa_stats_free_cnt', (YLeaf(YType.uint32, 'l2x-lpts-pa-stats-free-cnt'), ['int'])),
                            ('l2x_lpts_pa_stats_pulse_cnt', (YLeaf(YType.uint32, 'l2x-lpts-pa-stats-pulse-cnt'), ['int'])),
                            ('l2x_lpts_pa_stats_pulse_fail_cnt', (YLeaf(YType.uint32, 'l2x-lpts-pa-stats-pulse-fail-cnt'), ['int'])),
                            ('l2x_lpts_pa_stats_bind_cnt', (YLeaf(YType.uint32, 'l2x-lpts-pa-stats-bind-cnt'), ['int'])),
                            ('l2x_lpts_pa_stats_bind_fail_cnt', (YLeaf(YType.uint32, 'l2x-lpts-pa-stats-bind-fail-cnt'), ['int'])),
                            ('l2x_lpts_pa_stats_bind_batch_cnt', (YLeaf(YType.uint32, 'l2x-lpts-pa-stats-bind-batch-cnt'), ['int'])),
                            ('l2x_lpts_pa_stats_bind_batch_fail_cnt', (YLeaf(YType.uint32, 'l2x-lpts-pa-stats-bind-batch-fail-cnt'), ['int'])),
                            ('l2x_lpts_pa_stats_bind_time', (YLeaf(YType.uint32, 'l2x-lpts-pa-stats-bind-time'), ['int'])),
                            ('l2x_lpts_pa_stats_expire_cnt', (YLeaf(YType.uint32, 'l2x-lpts-pa-stats-expire-cnt'), ['int'])),
                            ('l2x_lpts_pa_stats_replay_cnt', (YLeaf(YType.uint32, 'l2x-lpts-pa-stats-replay-cnt'), ['int'])),
                            ('l2x_lpts_pa_stats_replay_batch_cnt', (YLeaf(YType.uint32, 'l2x-lpts-pa-stats-replay-batch-cnt'), ['int'])),
                            ('l2x_lpts_pa_stats_replay_time', (YLeaf(YType.uint32, 'l2x-lpts-pa-stats-replay-time'), ['int'])),
                        ])
                        self.l2tp_sh_l2x_num_tunnels = None
                        self.l2tp_sh_l2x_num_sessions = None
                        self.l2tp_sh_l2x_rx_high_water_mark = None
                        self.l2tp_sh_l2x_ave_msg_process_usecs = None
                        self.l2tp_sh_l2x_num_rx_msgs = None
                        self.l2tp_sh_l2x_num_tx_msgs = None
                        self.l2tp_sh_l2x_num_tx_err_drops = None
                        self.l2tp_sh_l2x_num_tx_conn_drops = None
                        self.l2tp_sh_l2x_num_reordered_msgs = None
                        self.l2tp_sh_l2x_max_reorder_deviation = None
                        self.l2tp_sh_l2x_num_ooo_msgs = None
                        self.l2tp_sh_l2x_num_rx_path_drops = None
                        self.l2tp_sh_l2x_num_rx_path_data_pkt_drops = None
                        self.l2tp_sh_l2x_num_rx_queue_drops = None
                        self.l2tp_sh_l2x_num_rx_ooo_drops = None
                        self.l2tp_sh_l2x_num_buffered_msgs = None
                        self.l2tp_sh_l2x_num_mutex_block = None
                        self.l2tp_sh_l2x_num_bad_len_drops = None
                        self.l2tp_sh_l2x_num_bad_avp_drops = None
                        self.l2tp_sh_l2x_num_missing_cc_id_drops = None
                        self.l2tp_sh_l2x_num_missing_sess_id_drops = None
                        self.l2tp_sh_l2x_num_mismatch_cc_id_drops = None
                        self.l2tp_sh_l2x_num_unknown_cc_drops = None
                        self.l2tp_sh_l2x_num_unknown_sess_drops = None
                        self.l2tp_sh_l2x_num_linear_id_search = None
                        self.l2tp_sh_l2x_num_linear_id_search_fail = None
                        self.l2tp_sh_l2x_num_netio_pkt_rx = None
                        self.l2tp_sh_l2tun_ave_msg_process_usecs = None
                        self.l2tp_sh_l2tun_num_rx_msgs = None
                        self.l2tp_sh_l2tun_num_tx_msgs = None
                        self.l2tp_l2tun_socket_ens_send_error_cnt = None
                        self.l2tp_l2tun_socket_session_accept = None
                        self.l2tp_l2tun_socket_session_destroy = None
                        self.l2tp_l2tun_socket_session_connect = None
                        self.l2tp_l2tun_socket_session_connect_continue = None
                        self.l2tp_l2tun_session_connecting = None
                        self.l2tp_l2tun_session_connected = None
                        self.l2tp_l2tun_session_disconnected = None
                        self.l2tp_l2tun_session_incoming = None
                        self.l2tp_l2tun_session_updated = None
                        self.l2tp_l2tun_session_circuit_status = None
                        self.l2x_lpts_pa_stats_setup_cnt = None
                        self.l2x_lpts_pa_stats_destroy_cnt = None
                        self.l2x_lpts_pa_stats_alloc_cnt = None
                        self.l2x_lpts_pa_stats_alloc_fail_cnt = None
                        self.l2x_lpts_pa_stats_init_cnt = None
                        self.l2x_lpts_pa_stats_init_fail_cnt = None
                        self.l2x_lpts_pa_stats_free_cnt = None
                        self.l2x_lpts_pa_stats_pulse_cnt = None
                        self.l2x_lpts_pa_stats_pulse_fail_cnt = None
                        self.l2x_lpts_pa_stats_bind_cnt = None
                        self.l2x_lpts_pa_stats_bind_fail_cnt = None
                        self.l2x_lpts_pa_stats_bind_batch_cnt = None
                        self.l2x_lpts_pa_stats_bind_batch_fail_cnt = None
                        self.l2x_lpts_pa_stats_bind_time = None
                        self.l2x_lpts_pa_stats_expire_cnt = None
                        self.l2x_lpts_pa_stats_replay_cnt = None
                        self.l2x_lpts_pa_stats_replay_batch_cnt = None
                        self.l2x_lpts_pa_stats_replay_time = None
                        self._segment_path = lambda: "internal-stats-last-clear"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2tpv2.Nodes.Node.Internal.InternalStatsLastClear, ['l2tp_sh_l2x_num_tunnels', 'l2tp_sh_l2x_num_sessions', 'l2tp_sh_l2x_rx_high_water_mark', 'l2tp_sh_l2x_ave_msg_process_usecs', 'l2tp_sh_l2x_num_rx_msgs', 'l2tp_sh_l2x_num_tx_msgs', 'l2tp_sh_l2x_num_tx_err_drops', 'l2tp_sh_l2x_num_tx_conn_drops', 'l2tp_sh_l2x_num_reordered_msgs', 'l2tp_sh_l2x_max_reorder_deviation', 'l2tp_sh_l2x_num_ooo_msgs', 'l2tp_sh_l2x_num_rx_path_drops', 'l2tp_sh_l2x_num_rx_path_data_pkt_drops', 'l2tp_sh_l2x_num_rx_queue_drops', 'l2tp_sh_l2x_num_rx_ooo_drops', 'l2tp_sh_l2x_num_buffered_msgs', 'l2tp_sh_l2x_num_mutex_block', 'l2tp_sh_l2x_num_bad_len_drops', 'l2tp_sh_l2x_num_bad_avp_drops', 'l2tp_sh_l2x_num_missing_cc_id_drops', 'l2tp_sh_l2x_num_missing_sess_id_drops', 'l2tp_sh_l2x_num_mismatch_cc_id_drops', 'l2tp_sh_l2x_num_unknown_cc_drops', 'l2tp_sh_l2x_num_unknown_sess_drops', 'l2tp_sh_l2x_num_linear_id_search', 'l2tp_sh_l2x_num_linear_id_search_fail', 'l2tp_sh_l2x_num_netio_pkt_rx', 'l2tp_sh_l2tun_ave_msg_process_usecs', 'l2tp_sh_l2tun_num_rx_msgs', 'l2tp_sh_l2tun_num_tx_msgs', 'l2tp_l2tun_socket_ens_send_error_cnt', 'l2tp_l2tun_socket_session_accept', 'l2tp_l2tun_socket_session_destroy', 'l2tp_l2tun_socket_session_connect', 'l2tp_l2tun_socket_session_connect_continue', 'l2tp_l2tun_session_connecting', 'l2tp_l2tun_session_connected', 'l2tp_l2tun_session_disconnected', 'l2tp_l2tun_session_incoming', 'l2tp_l2tun_session_updated', 'l2tp_l2tun_session_circuit_status', 'l2x_lpts_pa_stats_setup_cnt', 'l2x_lpts_pa_stats_destroy_cnt', 'l2x_lpts_pa_stats_alloc_cnt', 'l2x_lpts_pa_stats_alloc_fail_cnt', 'l2x_lpts_pa_stats_init_cnt', 'l2x_lpts_pa_stats_init_fail_cnt', 'l2x_lpts_pa_stats_free_cnt', 'l2x_lpts_pa_stats_pulse_cnt', 'l2x_lpts_pa_stats_pulse_fail_cnt', 'l2x_lpts_pa_stats_bind_cnt', 'l2x_lpts_pa_stats_bind_fail_cnt', 'l2x_lpts_pa_stats_bind_batch_cnt', 'l2x_lpts_pa_stats_bind_batch_fail_cnt', 'l2x_lpts_pa_stats_bind_time', 'l2x_lpts_pa_stats_expire_cnt', 'l2x_lpts_pa_stats_replay_cnt', 'l2x_lpts_pa_stats_replay_batch_cnt', 'l2x_lpts_pa_stats_replay_time'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                        return meta._meta_table['L2tpv2.Nodes.Node.Internal.InternalStatsLastClear']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                    return meta._meta_table['L2tpv2.Nodes.Node.Internal']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                return meta._meta_table['L2tpv2.Nodes.Node']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
            return meta._meta_table['L2tpv2.Nodes']['meta_info']

    def clone_ptr(self):
        self._top_entity = L2tpv2()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
        return meta._meta_table['L2tpv2']['meta_info']


