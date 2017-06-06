""" Cisco_IOS_XR_tunnel_l2tun_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR tunnel\-l2tun package operational data.

This module contains definitions
for the following management objects\:
  l2tp\: L2TP operational data
  l2tpv2\: l2tpv2

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class DigestHashEnum(Enum):
    """
    DigestHashEnum

    Digest hash types

    .. data:: md5 = 0

    	MD5

    .. data:: sha1 = 1

    	SHA1

    """

    md5 = 0

    sha1 = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
        return meta._meta_table['DigestHashEnum']



class L2Tp(object):
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
        self.classes = L2Tp.Classes()
        self.classes.parent = self
        self.counter_hist_fail = L2Tp.CounterHistFail()
        self.counter_hist_fail.parent = self
        self.counters = L2Tp.Counters()
        self.counters.parent = self
        self.session = L2Tp.Session()
        self.session.parent = self
        self.sessions = L2Tp.Sessions()
        self.sessions.parent = self
        self.tunnel_configurations = L2Tp.TunnelConfigurations()
        self.tunnel_configurations.parent = self
        self.tunnels = L2Tp.Tunnels()
        self.tunnels.parent = self


    class Counters(object):
        """
        L2TP control messages counters
        
        .. attribute:: control
        
        	L2TP control messages counters
        	**type**\:   :py:class:`Control <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tp.Counters.Control>`
        
        

        """

        _prefix = 'tunnel-l2tun-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.control = L2Tp.Counters.Control()
            self.control.parent = self


        class Control(object):
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
                self.parent = None
                self.tunnel_xr = L2Tp.Counters.Control.TunnelXr()
                self.tunnel_xr.parent = self
                self.tunnels = L2Tp.Counters.Control.Tunnels()
                self.tunnels.parent = self


            class TunnelXr(object):
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
                    self.parent = None
                    self.authentication = L2Tp.Counters.Control.TunnelXr.Authentication()
                    self.authentication.parent = self
                    self.global_ = L2Tp.Counters.Control.TunnelXr.Global_()
                    self.global_.parent = self


                class Authentication(object):
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
                        self.parent = None
                        self.challenge_avp = L2Tp.Counters.Control.TunnelXr.Authentication.ChallengeAvp()
                        self.challenge_avp.parent = self
                        self.challenge_reponse = L2Tp.Counters.Control.TunnelXr.Authentication.ChallengeReponse()
                        self.challenge_reponse.parent = self
                        self.common_digest = L2Tp.Counters.Control.TunnelXr.Authentication.CommonDigest()
                        self.common_digest.parent = self
                        self.integrity_check = L2Tp.Counters.Control.TunnelXr.Authentication.IntegrityCheck()
                        self.integrity_check.parent = self
                        self.local_secret = L2Tp.Counters.Control.TunnelXr.Authentication.LocalSecret()
                        self.local_secret.parent = self
                        self.nonce_avp = L2Tp.Counters.Control.TunnelXr.Authentication.NonceAvp()
                        self.nonce_avp.parent = self
                        self.overall_statistics = L2Tp.Counters.Control.TunnelXr.Authentication.OverallStatistics()
                        self.overall_statistics.parent = self
                        self.primary_digest = L2Tp.Counters.Control.TunnelXr.Authentication.PrimaryDigest()
                        self.primary_digest.parent = self
                        self.secondary_digest = L2Tp.Counters.Control.TunnelXr.Authentication.SecondaryDigest()
                        self.secondary_digest.parent = self


                    class NonceAvp(object):
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
                            self.parent = None
                            self.bad_hash = None
                            self.bad_length = None
                            self.failed = None
                            self.generate_response_failures = None
                            self.ignored = None
                            self.missing = None
                            self.passed = None
                            self.skipped = None
                            self.unexpected = None
                            self.unexpected_zlb = None
                            self.validate = None

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/Cisco-IOS-XR-tunnel-l2tun-oper:counters/Cisco-IOS-XR-tunnel-l2tun-oper:control/Cisco-IOS-XR-tunnel-l2tun-oper:tunnel-xr/Cisco-IOS-XR-tunnel-l2tun-oper:authentication/Cisco-IOS-XR-tunnel-l2tun-oper:nonce-avp'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.bad_hash is not None:
                                return True

                            if self.bad_length is not None:
                                return True

                            if self.failed is not None:
                                return True

                            if self.generate_response_failures is not None:
                                return True

                            if self.ignored is not None:
                                return True

                            if self.missing is not None:
                                return True

                            if self.passed is not None:
                                return True

                            if self.skipped is not None:
                                return True

                            if self.unexpected is not None:
                                return True

                            if self.unexpected_zlb is not None:
                                return True

                            if self.validate is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                            return meta._meta_table['L2Tp.Counters.Control.TunnelXr.Authentication.NonceAvp']['meta_info']


                    class CommonDigest(object):
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
                            self.parent = None
                            self.bad_hash = None
                            self.bad_length = None
                            self.failed = None
                            self.generate_response_failures = None
                            self.ignored = None
                            self.missing = None
                            self.passed = None
                            self.skipped = None
                            self.unexpected = None
                            self.unexpected_zlb = None
                            self.validate = None

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/Cisco-IOS-XR-tunnel-l2tun-oper:counters/Cisco-IOS-XR-tunnel-l2tun-oper:control/Cisco-IOS-XR-tunnel-l2tun-oper:tunnel-xr/Cisco-IOS-XR-tunnel-l2tun-oper:authentication/Cisco-IOS-XR-tunnel-l2tun-oper:common-digest'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.bad_hash is not None:
                                return True

                            if self.bad_length is not None:
                                return True

                            if self.failed is not None:
                                return True

                            if self.generate_response_failures is not None:
                                return True

                            if self.ignored is not None:
                                return True

                            if self.missing is not None:
                                return True

                            if self.passed is not None:
                                return True

                            if self.skipped is not None:
                                return True

                            if self.unexpected is not None:
                                return True

                            if self.unexpected_zlb is not None:
                                return True

                            if self.validate is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                            return meta._meta_table['L2Tp.Counters.Control.TunnelXr.Authentication.CommonDigest']['meta_info']


                    class PrimaryDigest(object):
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
                            self.parent = None
                            self.bad_hash = None
                            self.bad_length = None
                            self.failed = None
                            self.generate_response_failures = None
                            self.ignored = None
                            self.missing = None
                            self.passed = None
                            self.skipped = None
                            self.unexpected = None
                            self.unexpected_zlb = None
                            self.validate = None

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/Cisco-IOS-XR-tunnel-l2tun-oper:counters/Cisco-IOS-XR-tunnel-l2tun-oper:control/Cisco-IOS-XR-tunnel-l2tun-oper:tunnel-xr/Cisco-IOS-XR-tunnel-l2tun-oper:authentication/Cisco-IOS-XR-tunnel-l2tun-oper:primary-digest'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.bad_hash is not None:
                                return True

                            if self.bad_length is not None:
                                return True

                            if self.failed is not None:
                                return True

                            if self.generate_response_failures is not None:
                                return True

                            if self.ignored is not None:
                                return True

                            if self.missing is not None:
                                return True

                            if self.passed is not None:
                                return True

                            if self.skipped is not None:
                                return True

                            if self.unexpected is not None:
                                return True

                            if self.unexpected_zlb is not None:
                                return True

                            if self.validate is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                            return meta._meta_table['L2Tp.Counters.Control.TunnelXr.Authentication.PrimaryDigest']['meta_info']


                    class SecondaryDigest(object):
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
                            self.parent = None
                            self.bad_hash = None
                            self.bad_length = None
                            self.failed = None
                            self.generate_response_failures = None
                            self.ignored = None
                            self.missing = None
                            self.passed = None
                            self.skipped = None
                            self.unexpected = None
                            self.unexpected_zlb = None
                            self.validate = None

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/Cisco-IOS-XR-tunnel-l2tun-oper:counters/Cisco-IOS-XR-tunnel-l2tun-oper:control/Cisco-IOS-XR-tunnel-l2tun-oper:tunnel-xr/Cisco-IOS-XR-tunnel-l2tun-oper:authentication/Cisco-IOS-XR-tunnel-l2tun-oper:secondary-digest'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.bad_hash is not None:
                                return True

                            if self.bad_length is not None:
                                return True

                            if self.failed is not None:
                                return True

                            if self.generate_response_failures is not None:
                                return True

                            if self.ignored is not None:
                                return True

                            if self.missing is not None:
                                return True

                            if self.passed is not None:
                                return True

                            if self.skipped is not None:
                                return True

                            if self.unexpected is not None:
                                return True

                            if self.unexpected_zlb is not None:
                                return True

                            if self.validate is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                            return meta._meta_table['L2Tp.Counters.Control.TunnelXr.Authentication.SecondaryDigest']['meta_info']


                    class IntegrityCheck(object):
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
                            self.parent = None
                            self.bad_hash = None
                            self.bad_length = None
                            self.failed = None
                            self.generate_response_failures = None
                            self.ignored = None
                            self.missing = None
                            self.passed = None
                            self.skipped = None
                            self.unexpected = None
                            self.unexpected_zlb = None
                            self.validate = None

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/Cisco-IOS-XR-tunnel-l2tun-oper:counters/Cisco-IOS-XR-tunnel-l2tun-oper:control/Cisco-IOS-XR-tunnel-l2tun-oper:tunnel-xr/Cisco-IOS-XR-tunnel-l2tun-oper:authentication/Cisco-IOS-XR-tunnel-l2tun-oper:integrity-check'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.bad_hash is not None:
                                return True

                            if self.bad_length is not None:
                                return True

                            if self.failed is not None:
                                return True

                            if self.generate_response_failures is not None:
                                return True

                            if self.ignored is not None:
                                return True

                            if self.missing is not None:
                                return True

                            if self.passed is not None:
                                return True

                            if self.skipped is not None:
                                return True

                            if self.unexpected is not None:
                                return True

                            if self.unexpected_zlb is not None:
                                return True

                            if self.validate is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                            return meta._meta_table['L2Tp.Counters.Control.TunnelXr.Authentication.IntegrityCheck']['meta_info']


                    class LocalSecret(object):
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
                            self.parent = None
                            self.bad_hash = None
                            self.bad_length = None
                            self.failed = None
                            self.generate_response_failures = None
                            self.ignored = None
                            self.missing = None
                            self.passed = None
                            self.skipped = None
                            self.unexpected = None
                            self.unexpected_zlb = None
                            self.validate = None

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/Cisco-IOS-XR-tunnel-l2tun-oper:counters/Cisco-IOS-XR-tunnel-l2tun-oper:control/Cisco-IOS-XR-tunnel-l2tun-oper:tunnel-xr/Cisco-IOS-XR-tunnel-l2tun-oper:authentication/Cisco-IOS-XR-tunnel-l2tun-oper:local-secret'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.bad_hash is not None:
                                return True

                            if self.bad_length is not None:
                                return True

                            if self.failed is not None:
                                return True

                            if self.generate_response_failures is not None:
                                return True

                            if self.ignored is not None:
                                return True

                            if self.missing is not None:
                                return True

                            if self.passed is not None:
                                return True

                            if self.skipped is not None:
                                return True

                            if self.unexpected is not None:
                                return True

                            if self.unexpected_zlb is not None:
                                return True

                            if self.validate is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                            return meta._meta_table['L2Tp.Counters.Control.TunnelXr.Authentication.LocalSecret']['meta_info']


                    class ChallengeAvp(object):
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
                            self.parent = None
                            self.bad_hash = None
                            self.bad_length = None
                            self.failed = None
                            self.generate_response_failures = None
                            self.ignored = None
                            self.missing = None
                            self.passed = None
                            self.skipped = None
                            self.unexpected = None
                            self.unexpected_zlb = None
                            self.validate = None

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/Cisco-IOS-XR-tunnel-l2tun-oper:counters/Cisco-IOS-XR-tunnel-l2tun-oper:control/Cisco-IOS-XR-tunnel-l2tun-oper:tunnel-xr/Cisco-IOS-XR-tunnel-l2tun-oper:authentication/Cisco-IOS-XR-tunnel-l2tun-oper:challenge-avp'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.bad_hash is not None:
                                return True

                            if self.bad_length is not None:
                                return True

                            if self.failed is not None:
                                return True

                            if self.generate_response_failures is not None:
                                return True

                            if self.ignored is not None:
                                return True

                            if self.missing is not None:
                                return True

                            if self.passed is not None:
                                return True

                            if self.skipped is not None:
                                return True

                            if self.unexpected is not None:
                                return True

                            if self.unexpected_zlb is not None:
                                return True

                            if self.validate is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                            return meta._meta_table['L2Tp.Counters.Control.TunnelXr.Authentication.ChallengeAvp']['meta_info']


                    class ChallengeReponse(object):
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
                            self.parent = None
                            self.bad_hash = None
                            self.bad_length = None
                            self.failed = None
                            self.generate_response_failures = None
                            self.ignored = None
                            self.missing = None
                            self.passed = None
                            self.skipped = None
                            self.unexpected = None
                            self.unexpected_zlb = None
                            self.validate = None

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/Cisco-IOS-XR-tunnel-l2tun-oper:counters/Cisco-IOS-XR-tunnel-l2tun-oper:control/Cisco-IOS-XR-tunnel-l2tun-oper:tunnel-xr/Cisco-IOS-XR-tunnel-l2tun-oper:authentication/Cisco-IOS-XR-tunnel-l2tun-oper:challenge-reponse'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.bad_hash is not None:
                                return True

                            if self.bad_length is not None:
                                return True

                            if self.failed is not None:
                                return True

                            if self.generate_response_failures is not None:
                                return True

                            if self.ignored is not None:
                                return True

                            if self.missing is not None:
                                return True

                            if self.passed is not None:
                                return True

                            if self.skipped is not None:
                                return True

                            if self.unexpected is not None:
                                return True

                            if self.unexpected_zlb is not None:
                                return True

                            if self.validate is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                            return meta._meta_table['L2Tp.Counters.Control.TunnelXr.Authentication.ChallengeReponse']['meta_info']


                    class OverallStatistics(object):
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
                            self.parent = None
                            self.bad_hash = None
                            self.bad_length = None
                            self.failed = None
                            self.generate_response_failures = None
                            self.ignored = None
                            self.missing = None
                            self.passed = None
                            self.skipped = None
                            self.unexpected = None
                            self.unexpected_zlb = None
                            self.validate = None

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/Cisco-IOS-XR-tunnel-l2tun-oper:counters/Cisco-IOS-XR-tunnel-l2tun-oper:control/Cisco-IOS-XR-tunnel-l2tun-oper:tunnel-xr/Cisco-IOS-XR-tunnel-l2tun-oper:authentication/Cisco-IOS-XR-tunnel-l2tun-oper:overall-statistics'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.bad_hash is not None:
                                return True

                            if self.bad_length is not None:
                                return True

                            if self.failed is not None:
                                return True

                            if self.generate_response_failures is not None:
                                return True

                            if self.ignored is not None:
                                return True

                            if self.missing is not None:
                                return True

                            if self.passed is not None:
                                return True

                            if self.skipped is not None:
                                return True

                            if self.unexpected is not None:
                                return True

                            if self.unexpected_zlb is not None:
                                return True

                            if self.validate is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                            return meta._meta_table['L2Tp.Counters.Control.TunnelXr.Authentication.OverallStatistics']['meta_info']

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/Cisco-IOS-XR-tunnel-l2tun-oper:counters/Cisco-IOS-XR-tunnel-l2tun-oper:control/Cisco-IOS-XR-tunnel-l2tun-oper:tunnel-xr/Cisco-IOS-XR-tunnel-l2tun-oper:authentication'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.challenge_avp is not None and self.challenge_avp._has_data():
                            return True

                        if self.challenge_reponse is not None and self.challenge_reponse._has_data():
                            return True

                        if self.common_digest is not None and self.common_digest._has_data():
                            return True

                        if self.integrity_check is not None and self.integrity_check._has_data():
                            return True

                        if self.local_secret is not None and self.local_secret._has_data():
                            return True

                        if self.nonce_avp is not None and self.nonce_avp._has_data():
                            return True

                        if self.overall_statistics is not None and self.overall_statistics._has_data():
                            return True

                        if self.primary_digest is not None and self.primary_digest._has_data():
                            return True

                        if self.secondary_digest is not None and self.secondary_digest._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                        return meta._meta_table['L2Tp.Counters.Control.TunnelXr.Authentication']['meta_info']


                class Global_(object):
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
                        self.parent = None
                        self.drop = L2Tp.Counters.Control.TunnelXr.Global_.Drop()
                        self.drop.parent = self
                        self.received = L2Tp.Counters.Control.TunnelXr.Global_.Received()
                        self.received.parent = self
                        self.retransmit = L2Tp.Counters.Control.TunnelXr.Global_.Retransmit()
                        self.retransmit.parent = self
                        self.total_drop = None
                        self.total_received = None
                        self.total_retransmit = None
                        self.total_transmit = None
                        self.transmit = L2Tp.Counters.Control.TunnelXr.Global_.Transmit()
                        self.transmit.parent = self


                    class Transmit(object):
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
                            self.parent = None
                            self.acknowledgement_packets = None
                            self.call_disconnect_notify_packets = None
                            self.hello_packets = None
                            self.incoming_call_connected_packets = None
                            self.incoming_call_replies = None
                            self.incoming_call_requests = None
                            self.outgoing_call_connected_packets = None
                            self.outgoing_call_replies = None
                            self.outgoing_call_requests = None
                            self.service_relay_replies = None
                            self.service_relay_requests = None
                            self.set_link_info_packets = None
                            self.start_control_connection_notifications = None
                            self.start_control_connection_replies = None
                            self.start_control_connection_requests = None
                            self.stop_control_connection_notifications = None
                            self.unknown_packets = None
                            self.wan_error_notify_packets = None
                            self.zero_length_body_packets = None

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/Cisco-IOS-XR-tunnel-l2tun-oper:counters/Cisco-IOS-XR-tunnel-l2tun-oper:control/Cisco-IOS-XR-tunnel-l2tun-oper:tunnel-xr/Cisco-IOS-XR-tunnel-l2tun-oper:global/Cisco-IOS-XR-tunnel-l2tun-oper:transmit'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.acknowledgement_packets is not None:
                                return True

                            if self.call_disconnect_notify_packets is not None:
                                return True

                            if self.hello_packets is not None:
                                return True

                            if self.incoming_call_connected_packets is not None:
                                return True

                            if self.incoming_call_replies is not None:
                                return True

                            if self.incoming_call_requests is not None:
                                return True

                            if self.outgoing_call_connected_packets is not None:
                                return True

                            if self.outgoing_call_replies is not None:
                                return True

                            if self.outgoing_call_requests is not None:
                                return True

                            if self.service_relay_replies is not None:
                                return True

                            if self.service_relay_requests is not None:
                                return True

                            if self.set_link_info_packets is not None:
                                return True

                            if self.start_control_connection_notifications is not None:
                                return True

                            if self.start_control_connection_replies is not None:
                                return True

                            if self.start_control_connection_requests is not None:
                                return True

                            if self.stop_control_connection_notifications is not None:
                                return True

                            if self.unknown_packets is not None:
                                return True

                            if self.wan_error_notify_packets is not None:
                                return True

                            if self.zero_length_body_packets is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                            return meta._meta_table['L2Tp.Counters.Control.TunnelXr.Global_.Transmit']['meta_info']


                    class Retransmit(object):
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
                            self.parent = None
                            self.acknowledgement_packets = None
                            self.call_disconnect_notify_packets = None
                            self.hello_packets = None
                            self.incoming_call_connected_packets = None
                            self.incoming_call_replies = None
                            self.incoming_call_requests = None
                            self.outgoing_call_connected_packets = None
                            self.outgoing_call_replies = None
                            self.outgoing_call_requests = None
                            self.service_relay_replies = None
                            self.service_relay_requests = None
                            self.set_link_info_packets = None
                            self.start_control_connection_notifications = None
                            self.start_control_connection_replies = None
                            self.start_control_connection_requests = None
                            self.stop_control_connection_notifications = None
                            self.unknown_packets = None
                            self.wan_error_notify_packets = None
                            self.zero_length_body_packets = None

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/Cisco-IOS-XR-tunnel-l2tun-oper:counters/Cisco-IOS-XR-tunnel-l2tun-oper:control/Cisco-IOS-XR-tunnel-l2tun-oper:tunnel-xr/Cisco-IOS-XR-tunnel-l2tun-oper:global/Cisco-IOS-XR-tunnel-l2tun-oper:retransmit'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.acknowledgement_packets is not None:
                                return True

                            if self.call_disconnect_notify_packets is not None:
                                return True

                            if self.hello_packets is not None:
                                return True

                            if self.incoming_call_connected_packets is not None:
                                return True

                            if self.incoming_call_replies is not None:
                                return True

                            if self.incoming_call_requests is not None:
                                return True

                            if self.outgoing_call_connected_packets is not None:
                                return True

                            if self.outgoing_call_replies is not None:
                                return True

                            if self.outgoing_call_requests is not None:
                                return True

                            if self.service_relay_replies is not None:
                                return True

                            if self.service_relay_requests is not None:
                                return True

                            if self.set_link_info_packets is not None:
                                return True

                            if self.start_control_connection_notifications is not None:
                                return True

                            if self.start_control_connection_replies is not None:
                                return True

                            if self.start_control_connection_requests is not None:
                                return True

                            if self.stop_control_connection_notifications is not None:
                                return True

                            if self.unknown_packets is not None:
                                return True

                            if self.wan_error_notify_packets is not None:
                                return True

                            if self.zero_length_body_packets is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                            return meta._meta_table['L2Tp.Counters.Control.TunnelXr.Global_.Retransmit']['meta_info']


                    class Received(object):
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
                            self.parent = None
                            self.acknowledgement_packets = None
                            self.call_disconnect_notify_packets = None
                            self.hello_packets = None
                            self.incoming_call_connected_packets = None
                            self.incoming_call_replies = None
                            self.incoming_call_requests = None
                            self.outgoing_call_connected_packets = None
                            self.outgoing_call_replies = None
                            self.outgoing_call_requests = None
                            self.service_relay_replies = None
                            self.service_relay_requests = None
                            self.set_link_info_packets = None
                            self.start_control_connection_notifications = None
                            self.start_control_connection_replies = None
                            self.start_control_connection_requests = None
                            self.stop_control_connection_notifications = None
                            self.unknown_packets = None
                            self.wan_error_notify_packets = None
                            self.zero_length_body_packets = None

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/Cisco-IOS-XR-tunnel-l2tun-oper:counters/Cisco-IOS-XR-tunnel-l2tun-oper:control/Cisco-IOS-XR-tunnel-l2tun-oper:tunnel-xr/Cisco-IOS-XR-tunnel-l2tun-oper:global/Cisco-IOS-XR-tunnel-l2tun-oper:received'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.acknowledgement_packets is not None:
                                return True

                            if self.call_disconnect_notify_packets is not None:
                                return True

                            if self.hello_packets is not None:
                                return True

                            if self.incoming_call_connected_packets is not None:
                                return True

                            if self.incoming_call_replies is not None:
                                return True

                            if self.incoming_call_requests is not None:
                                return True

                            if self.outgoing_call_connected_packets is not None:
                                return True

                            if self.outgoing_call_replies is not None:
                                return True

                            if self.outgoing_call_requests is not None:
                                return True

                            if self.service_relay_replies is not None:
                                return True

                            if self.service_relay_requests is not None:
                                return True

                            if self.set_link_info_packets is not None:
                                return True

                            if self.start_control_connection_notifications is not None:
                                return True

                            if self.start_control_connection_replies is not None:
                                return True

                            if self.start_control_connection_requests is not None:
                                return True

                            if self.stop_control_connection_notifications is not None:
                                return True

                            if self.unknown_packets is not None:
                                return True

                            if self.wan_error_notify_packets is not None:
                                return True

                            if self.zero_length_body_packets is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                            return meta._meta_table['L2Tp.Counters.Control.TunnelXr.Global_.Received']['meta_info']


                    class Drop(object):
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
                            self.parent = None
                            self.acknowledgement_packets = None
                            self.call_disconnect_notify_packets = None
                            self.hello_packets = None
                            self.incoming_call_connected_packets = None
                            self.incoming_call_replies = None
                            self.incoming_call_requests = None
                            self.outgoing_call_connected_packets = None
                            self.outgoing_call_replies = None
                            self.outgoing_call_requests = None
                            self.service_relay_replies = None
                            self.service_relay_requests = None
                            self.set_link_info_packets = None
                            self.start_control_connection_notifications = None
                            self.start_control_connection_replies = None
                            self.start_control_connection_requests = None
                            self.stop_control_connection_notifications = None
                            self.unknown_packets = None
                            self.wan_error_notify_packets = None
                            self.zero_length_body_packets = None

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/Cisco-IOS-XR-tunnel-l2tun-oper:counters/Cisco-IOS-XR-tunnel-l2tun-oper:control/Cisco-IOS-XR-tunnel-l2tun-oper:tunnel-xr/Cisco-IOS-XR-tunnel-l2tun-oper:global/Cisco-IOS-XR-tunnel-l2tun-oper:drop'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.acknowledgement_packets is not None:
                                return True

                            if self.call_disconnect_notify_packets is not None:
                                return True

                            if self.hello_packets is not None:
                                return True

                            if self.incoming_call_connected_packets is not None:
                                return True

                            if self.incoming_call_replies is not None:
                                return True

                            if self.incoming_call_requests is not None:
                                return True

                            if self.outgoing_call_connected_packets is not None:
                                return True

                            if self.outgoing_call_replies is not None:
                                return True

                            if self.outgoing_call_requests is not None:
                                return True

                            if self.service_relay_replies is not None:
                                return True

                            if self.service_relay_requests is not None:
                                return True

                            if self.set_link_info_packets is not None:
                                return True

                            if self.start_control_connection_notifications is not None:
                                return True

                            if self.start_control_connection_replies is not None:
                                return True

                            if self.start_control_connection_requests is not None:
                                return True

                            if self.stop_control_connection_notifications is not None:
                                return True

                            if self.unknown_packets is not None:
                                return True

                            if self.wan_error_notify_packets is not None:
                                return True

                            if self.zero_length_body_packets is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                            return meta._meta_table['L2Tp.Counters.Control.TunnelXr.Global_.Drop']['meta_info']

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/Cisco-IOS-XR-tunnel-l2tun-oper:counters/Cisco-IOS-XR-tunnel-l2tun-oper:control/Cisco-IOS-XR-tunnel-l2tun-oper:tunnel-xr/Cisco-IOS-XR-tunnel-l2tun-oper:global'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.drop is not None and self.drop._has_data():
                            return True

                        if self.received is not None and self.received._has_data():
                            return True

                        if self.retransmit is not None and self.retransmit._has_data():
                            return True

                        if self.total_drop is not None:
                            return True

                        if self.total_received is not None:
                            return True

                        if self.total_retransmit is not None:
                            return True

                        if self.total_transmit is not None:
                            return True

                        if self.transmit is not None and self.transmit._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                        return meta._meta_table['L2Tp.Counters.Control.TunnelXr.Global_']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/Cisco-IOS-XR-tunnel-l2tun-oper:counters/Cisco-IOS-XR-tunnel-l2tun-oper:control/Cisco-IOS-XR-tunnel-l2tun-oper:tunnel-xr'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.authentication is not None and self.authentication._has_data():
                        return True

                    if self.global_ is not None and self.global_._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                    return meta._meta_table['L2Tp.Counters.Control.TunnelXr']['meta_info']


            class Tunnels(object):
                """
                Table of tunnel IDs of control message counters
                
                .. attribute:: tunnel
                
                	L2TP tunnel control message counters
                	**type**\: list of    :py:class:`Tunnel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tp.Counters.Control.Tunnels.Tunnel>`
                
                

                """

                _prefix = 'tunnel-l2tun-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.tunnel = YList()
                    self.tunnel.parent = self
                    self.tunnel.name = 'tunnel'


                class Tunnel(object):
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
                        self.parent = None
                        self.tunnel_id = None
                        self.brief = L2Tp.Counters.Control.Tunnels.Tunnel.Brief()
                        self.brief.parent = self
                        self.global_ = L2Tp.Counters.Control.Tunnels.Tunnel.Global_()
                        self.global_.parent = self


                    class Brief(object):
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
                            self.parent = None
                            self.local_address = None
                            self.remote_address = None
                            self.remote_tunnel_id = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-tunnel-l2tun-oper:brief'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.local_address is not None:
                                return True

                            if self.remote_address is not None:
                                return True

                            if self.remote_tunnel_id is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                            return meta._meta_table['L2Tp.Counters.Control.Tunnels.Tunnel.Brief']['meta_info']


                    class Global_(object):
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
                            self.parent = None
                            self.drop = L2Tp.Counters.Control.Tunnels.Tunnel.Global_.Drop()
                            self.drop.parent = self
                            self.received = L2Tp.Counters.Control.Tunnels.Tunnel.Global_.Received()
                            self.received.parent = self
                            self.retransmit = L2Tp.Counters.Control.Tunnels.Tunnel.Global_.Retransmit()
                            self.retransmit.parent = self
                            self.total_drop = None
                            self.total_received = None
                            self.total_retransmit = None
                            self.total_transmit = None
                            self.transmit = L2Tp.Counters.Control.Tunnels.Tunnel.Global_.Transmit()
                            self.transmit.parent = self


                        class Transmit(object):
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
                                self.parent = None
                                self.acknowledgement_packets = None
                                self.call_disconnect_notify_packets = None
                                self.hello_packets = None
                                self.incoming_call_connected_packets = None
                                self.incoming_call_replies = None
                                self.incoming_call_requests = None
                                self.outgoing_call_connected_packets = None
                                self.outgoing_call_replies = None
                                self.outgoing_call_requests = None
                                self.service_relay_replies = None
                                self.service_relay_requests = None
                                self.set_link_info_packets = None
                                self.start_control_connection_notifications = None
                                self.start_control_connection_replies = None
                                self.start_control_connection_requests = None
                                self.stop_control_connection_notifications = None
                                self.unknown_packets = None
                                self.wan_error_notify_packets = None
                                self.zero_length_body_packets = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-tunnel-l2tun-oper:transmit'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.acknowledgement_packets is not None:
                                    return True

                                if self.call_disconnect_notify_packets is not None:
                                    return True

                                if self.hello_packets is not None:
                                    return True

                                if self.incoming_call_connected_packets is not None:
                                    return True

                                if self.incoming_call_replies is not None:
                                    return True

                                if self.incoming_call_requests is not None:
                                    return True

                                if self.outgoing_call_connected_packets is not None:
                                    return True

                                if self.outgoing_call_replies is not None:
                                    return True

                                if self.outgoing_call_requests is not None:
                                    return True

                                if self.service_relay_replies is not None:
                                    return True

                                if self.service_relay_requests is not None:
                                    return True

                                if self.set_link_info_packets is not None:
                                    return True

                                if self.start_control_connection_notifications is not None:
                                    return True

                                if self.start_control_connection_replies is not None:
                                    return True

                                if self.start_control_connection_requests is not None:
                                    return True

                                if self.stop_control_connection_notifications is not None:
                                    return True

                                if self.unknown_packets is not None:
                                    return True

                                if self.wan_error_notify_packets is not None:
                                    return True

                                if self.zero_length_body_packets is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                                return meta._meta_table['L2Tp.Counters.Control.Tunnels.Tunnel.Global_.Transmit']['meta_info']


                        class Retransmit(object):
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
                                self.parent = None
                                self.acknowledgement_packets = None
                                self.call_disconnect_notify_packets = None
                                self.hello_packets = None
                                self.incoming_call_connected_packets = None
                                self.incoming_call_replies = None
                                self.incoming_call_requests = None
                                self.outgoing_call_connected_packets = None
                                self.outgoing_call_replies = None
                                self.outgoing_call_requests = None
                                self.service_relay_replies = None
                                self.service_relay_requests = None
                                self.set_link_info_packets = None
                                self.start_control_connection_notifications = None
                                self.start_control_connection_replies = None
                                self.start_control_connection_requests = None
                                self.stop_control_connection_notifications = None
                                self.unknown_packets = None
                                self.wan_error_notify_packets = None
                                self.zero_length_body_packets = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-tunnel-l2tun-oper:retransmit'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.acknowledgement_packets is not None:
                                    return True

                                if self.call_disconnect_notify_packets is not None:
                                    return True

                                if self.hello_packets is not None:
                                    return True

                                if self.incoming_call_connected_packets is not None:
                                    return True

                                if self.incoming_call_replies is not None:
                                    return True

                                if self.incoming_call_requests is not None:
                                    return True

                                if self.outgoing_call_connected_packets is not None:
                                    return True

                                if self.outgoing_call_replies is not None:
                                    return True

                                if self.outgoing_call_requests is not None:
                                    return True

                                if self.service_relay_replies is not None:
                                    return True

                                if self.service_relay_requests is not None:
                                    return True

                                if self.set_link_info_packets is not None:
                                    return True

                                if self.start_control_connection_notifications is not None:
                                    return True

                                if self.start_control_connection_replies is not None:
                                    return True

                                if self.start_control_connection_requests is not None:
                                    return True

                                if self.stop_control_connection_notifications is not None:
                                    return True

                                if self.unknown_packets is not None:
                                    return True

                                if self.wan_error_notify_packets is not None:
                                    return True

                                if self.zero_length_body_packets is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                                return meta._meta_table['L2Tp.Counters.Control.Tunnels.Tunnel.Global_.Retransmit']['meta_info']


                        class Received(object):
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
                                self.parent = None
                                self.acknowledgement_packets = None
                                self.call_disconnect_notify_packets = None
                                self.hello_packets = None
                                self.incoming_call_connected_packets = None
                                self.incoming_call_replies = None
                                self.incoming_call_requests = None
                                self.outgoing_call_connected_packets = None
                                self.outgoing_call_replies = None
                                self.outgoing_call_requests = None
                                self.service_relay_replies = None
                                self.service_relay_requests = None
                                self.set_link_info_packets = None
                                self.start_control_connection_notifications = None
                                self.start_control_connection_replies = None
                                self.start_control_connection_requests = None
                                self.stop_control_connection_notifications = None
                                self.unknown_packets = None
                                self.wan_error_notify_packets = None
                                self.zero_length_body_packets = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-tunnel-l2tun-oper:received'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.acknowledgement_packets is not None:
                                    return True

                                if self.call_disconnect_notify_packets is not None:
                                    return True

                                if self.hello_packets is not None:
                                    return True

                                if self.incoming_call_connected_packets is not None:
                                    return True

                                if self.incoming_call_replies is not None:
                                    return True

                                if self.incoming_call_requests is not None:
                                    return True

                                if self.outgoing_call_connected_packets is not None:
                                    return True

                                if self.outgoing_call_replies is not None:
                                    return True

                                if self.outgoing_call_requests is not None:
                                    return True

                                if self.service_relay_replies is not None:
                                    return True

                                if self.service_relay_requests is not None:
                                    return True

                                if self.set_link_info_packets is not None:
                                    return True

                                if self.start_control_connection_notifications is not None:
                                    return True

                                if self.start_control_connection_replies is not None:
                                    return True

                                if self.start_control_connection_requests is not None:
                                    return True

                                if self.stop_control_connection_notifications is not None:
                                    return True

                                if self.unknown_packets is not None:
                                    return True

                                if self.wan_error_notify_packets is not None:
                                    return True

                                if self.zero_length_body_packets is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                                return meta._meta_table['L2Tp.Counters.Control.Tunnels.Tunnel.Global_.Received']['meta_info']


                        class Drop(object):
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
                                self.parent = None
                                self.acknowledgement_packets = None
                                self.call_disconnect_notify_packets = None
                                self.hello_packets = None
                                self.incoming_call_connected_packets = None
                                self.incoming_call_replies = None
                                self.incoming_call_requests = None
                                self.outgoing_call_connected_packets = None
                                self.outgoing_call_replies = None
                                self.outgoing_call_requests = None
                                self.service_relay_replies = None
                                self.service_relay_requests = None
                                self.set_link_info_packets = None
                                self.start_control_connection_notifications = None
                                self.start_control_connection_replies = None
                                self.start_control_connection_requests = None
                                self.stop_control_connection_notifications = None
                                self.unknown_packets = None
                                self.wan_error_notify_packets = None
                                self.zero_length_body_packets = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-tunnel-l2tun-oper:drop'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.acknowledgement_packets is not None:
                                    return True

                                if self.call_disconnect_notify_packets is not None:
                                    return True

                                if self.hello_packets is not None:
                                    return True

                                if self.incoming_call_connected_packets is not None:
                                    return True

                                if self.incoming_call_replies is not None:
                                    return True

                                if self.incoming_call_requests is not None:
                                    return True

                                if self.outgoing_call_connected_packets is not None:
                                    return True

                                if self.outgoing_call_replies is not None:
                                    return True

                                if self.outgoing_call_requests is not None:
                                    return True

                                if self.service_relay_replies is not None:
                                    return True

                                if self.service_relay_requests is not None:
                                    return True

                                if self.set_link_info_packets is not None:
                                    return True

                                if self.start_control_connection_notifications is not None:
                                    return True

                                if self.start_control_connection_replies is not None:
                                    return True

                                if self.start_control_connection_requests is not None:
                                    return True

                                if self.stop_control_connection_notifications is not None:
                                    return True

                                if self.unknown_packets is not None:
                                    return True

                                if self.wan_error_notify_packets is not None:
                                    return True

                                if self.zero_length_body_packets is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                                return meta._meta_table['L2Tp.Counters.Control.Tunnels.Tunnel.Global_.Drop']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-tunnel-l2tun-oper:global'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.drop is not None and self.drop._has_data():
                                return True

                            if self.received is not None and self.received._has_data():
                                return True

                            if self.retransmit is not None and self.retransmit._has_data():
                                return True

                            if self.total_drop is not None:
                                return True

                            if self.total_received is not None:
                                return True

                            if self.total_retransmit is not None:
                                return True

                            if self.total_transmit is not None:
                                return True

                            if self.transmit is not None and self.transmit._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                            return meta._meta_table['L2Tp.Counters.Control.Tunnels.Tunnel.Global_']['meta_info']

                    @property
                    def _common_path(self):
                        if self.tunnel_id is None:
                            raise YPYModelError('Key property tunnel_id is None')

                        return '/Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/Cisco-IOS-XR-tunnel-l2tun-oper:counters/Cisco-IOS-XR-tunnel-l2tun-oper:control/Cisco-IOS-XR-tunnel-l2tun-oper:tunnels/Cisco-IOS-XR-tunnel-l2tun-oper:tunnel[Cisco-IOS-XR-tunnel-l2tun-oper:tunnel-id = ' + str(self.tunnel_id) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.tunnel_id is not None:
                            return True

                        if self.brief is not None and self.brief._has_data():
                            return True

                        if self.global_ is not None and self.global_._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                        return meta._meta_table['L2Tp.Counters.Control.Tunnels.Tunnel']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/Cisco-IOS-XR-tunnel-l2tun-oper:counters/Cisco-IOS-XR-tunnel-l2tun-oper:control/Cisco-IOS-XR-tunnel-l2tun-oper:tunnels'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.tunnel is not None:
                        for child_ref in self.tunnel:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                    return meta._meta_table['L2Tp.Counters.Control.Tunnels']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/Cisco-IOS-XR-tunnel-l2tun-oper:counters/Cisco-IOS-XR-tunnel-l2tun-oper:control'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.tunnel_xr is not None and self.tunnel_xr._has_data():
                    return True

                if self.tunnels is not None and self.tunnels._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                return meta._meta_table['L2Tp.Counters.Control']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/Cisco-IOS-XR-tunnel-l2tun-oper:counters'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.control is not None and self.control._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
            return meta._meta_table['L2Tp.Counters']['meta_info']


    class TunnelConfigurations(object):
        """
        List of tunnel IDs
        
        .. attribute:: tunnel_configuration
        
        	L2TP tunnel information
        	**type**\: list of    :py:class:`TunnelConfiguration <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tp.TunnelConfigurations.TunnelConfiguration>`
        
        

        """

        _prefix = 'tunnel-l2tun-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.tunnel_configuration = YList()
            self.tunnel_configuration.parent = self
            self.tunnel_configuration.name = 'tunnel_configuration'


        class TunnelConfiguration(object):
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
                self.parent = None
                self.local_tunnel_id = None
                self.l2tp_class = L2Tp.TunnelConfigurations.TunnelConfiguration.L2TpClass()
                self.l2tp_class.parent = self
                self.remote_tunnel_id = None


            class L2TpClass(object):
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
                	**type**\:   :py:class:`DigestHashEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.DigestHashEnum>`
                
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
                    self.parent = None
                    self.accounting_method_list = None
                    self.class_name_xr = None
                    self.digest_hash = None
                    self.encoded_password = None
                    self.hello_timeout = None
                    self.host_name = None
                    self.initial_retransmit_maximum_timeout = None
                    self.initial_retransmit_minimum_timeout = None
                    self.initial_retransmit_retries = None
                    self.ip_tos = None
                    self.is_authentication_enabled = None
                    self.is_congestion_control_enabled = None
                    self.is_digest_check_enabled = None
                    self.is_digest_enabled = None
                    self.is_hidden = None
                    self.is_peer_address_checked = None
                    self.password = None
                    self.receive_window_size = None
                    self.retransmit_maximum_timeout = None
                    self.retransmit_minimum_timeout = None
                    self.retransmit_retries = None
                    self.setup_timeout = None
                    self.timeout_no_user = None
                    self.vrf_name = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-tunnel-l2tun-oper:l2tp-class'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.accounting_method_list is not None:
                        return True

                    if self.class_name_xr is not None:
                        return True

                    if self.digest_hash is not None:
                        return True

                    if self.encoded_password is not None:
                        return True

                    if self.hello_timeout is not None:
                        return True

                    if self.host_name is not None:
                        return True

                    if self.initial_retransmit_maximum_timeout is not None:
                        return True

                    if self.initial_retransmit_minimum_timeout is not None:
                        return True

                    if self.initial_retransmit_retries is not None:
                        return True

                    if self.ip_tos is not None:
                        return True

                    if self.is_authentication_enabled is not None:
                        return True

                    if self.is_congestion_control_enabled is not None:
                        return True

                    if self.is_digest_check_enabled is not None:
                        return True

                    if self.is_digest_enabled is not None:
                        return True

                    if self.is_hidden is not None:
                        return True

                    if self.is_peer_address_checked is not None:
                        return True

                    if self.password is not None:
                        return True

                    if self.receive_window_size is not None:
                        return True

                    if self.retransmit_maximum_timeout is not None:
                        return True

                    if self.retransmit_minimum_timeout is not None:
                        return True

                    if self.retransmit_retries is not None:
                        return True

                    if self.setup_timeout is not None:
                        return True

                    if self.timeout_no_user is not None:
                        return True

                    if self.vrf_name is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                    return meta._meta_table['L2Tp.TunnelConfigurations.TunnelConfiguration.L2TpClass']['meta_info']

            @property
            def _common_path(self):
                if self.local_tunnel_id is None:
                    raise YPYModelError('Key property local_tunnel_id is None')

                return '/Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/Cisco-IOS-XR-tunnel-l2tun-oper:tunnel-configurations/Cisco-IOS-XR-tunnel-l2tun-oper:tunnel-configuration[Cisco-IOS-XR-tunnel-l2tun-oper:local-tunnel-id = ' + str(self.local_tunnel_id) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.local_tunnel_id is not None:
                    return True

                if self.l2tp_class is not None and self.l2tp_class._has_data():
                    return True

                if self.remote_tunnel_id is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                return meta._meta_table['L2Tp.TunnelConfigurations.TunnelConfiguration']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/Cisco-IOS-XR-tunnel-l2tun-oper:tunnel-configurations'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.tunnel_configuration is not None:
                for child_ref in self.tunnel_configuration:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
            return meta._meta_table['L2Tp.TunnelConfigurations']['meta_info']


    class CounterHistFail(object):
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
            self.parent = None
            self.pkt_timeout = YLeafList()
            self.pkt_timeout.parent = self
            self.pkt_timeout.name = 'pkt_timeout'
            self.rx_counters = None
            self.sess_down_tmout = None
            self.tx_counters = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/Cisco-IOS-XR-tunnel-l2tun-oper:counter-hist-fail'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.pkt_timeout is not None:
                for child in self.pkt_timeout:
                    if child is not None:
                        return True

            if self.rx_counters is not None:
                return True

            if self.sess_down_tmout is not None:
                return True

            if self.tx_counters is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
            return meta._meta_table['L2Tp.CounterHistFail']['meta_info']


    class Classes(object):
        """
        List of L2TP class names
        
        .. attribute:: class_
        
        	L2TP class name
        	**type**\: list of    :py:class:`Class_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tp.Classes.Class_>`
        
        

        """

        _prefix = 'tunnel-l2tun-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.class_ = YList()
            self.class_.parent = self
            self.class_.name = 'class_'


        class Class_(object):
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
            	**type**\:   :py:class:`DigestHashEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.DigestHashEnum>`
            
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
                self.parent = None
                self.class_name = None
                self.accounting_method_list = None
                self.class_name_xr = None
                self.digest_hash = None
                self.encoded_password = None
                self.hello_timeout = None
                self.host_name = None
                self.initial_retransmit_maximum_timeout = None
                self.initial_retransmit_minimum_timeout = None
                self.initial_retransmit_retries = None
                self.ip_tos = None
                self.is_authentication_enabled = None
                self.is_congestion_control_enabled = None
                self.is_digest_check_enabled = None
                self.is_digest_enabled = None
                self.is_hidden = None
                self.is_peer_address_checked = None
                self.password = None
                self.receive_window_size = None
                self.retransmit_maximum_timeout = None
                self.retransmit_minimum_timeout = None
                self.retransmit_retries = None
                self.setup_timeout = None
                self.timeout_no_user = None
                self.vrf_name = None

            @property
            def _common_path(self):
                if self.class_name is None:
                    raise YPYModelError('Key property class_name is None')

                return '/Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/Cisco-IOS-XR-tunnel-l2tun-oper:classes/Cisco-IOS-XR-tunnel-l2tun-oper:class[Cisco-IOS-XR-tunnel-l2tun-oper:class-name = ' + str(self.class_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.class_name is not None:
                    return True

                if self.accounting_method_list is not None:
                    return True

                if self.class_name_xr is not None:
                    return True

                if self.digest_hash is not None:
                    return True

                if self.encoded_password is not None:
                    return True

                if self.hello_timeout is not None:
                    return True

                if self.host_name is not None:
                    return True

                if self.initial_retransmit_maximum_timeout is not None:
                    return True

                if self.initial_retransmit_minimum_timeout is not None:
                    return True

                if self.initial_retransmit_retries is not None:
                    return True

                if self.ip_tos is not None:
                    return True

                if self.is_authentication_enabled is not None:
                    return True

                if self.is_congestion_control_enabled is not None:
                    return True

                if self.is_digest_check_enabled is not None:
                    return True

                if self.is_digest_enabled is not None:
                    return True

                if self.is_hidden is not None:
                    return True

                if self.is_peer_address_checked is not None:
                    return True

                if self.password is not None:
                    return True

                if self.receive_window_size is not None:
                    return True

                if self.retransmit_maximum_timeout is not None:
                    return True

                if self.retransmit_minimum_timeout is not None:
                    return True

                if self.retransmit_retries is not None:
                    return True

                if self.setup_timeout is not None:
                    return True

                if self.timeout_no_user is not None:
                    return True

                if self.vrf_name is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                return meta._meta_table['L2Tp.Classes.Class_']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/Cisco-IOS-XR-tunnel-l2tun-oper:classes'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.class_ is not None:
                for child_ref in self.class_:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
            return meta._meta_table['L2Tp.Classes']['meta_info']


    class Tunnels(object):
        """
        List of tunnel IDs
        
        .. attribute:: tunnel
        
        	L2TP tunnel  information
        	**type**\: list of    :py:class:`Tunnel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tp.Tunnels.Tunnel>`
        
        

        """

        _prefix = 'tunnel-l2tun-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.tunnel = YList()
            self.tunnel.parent = self
            self.tunnel.name = 'tunnel'


        class Tunnel(object):
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
                self.parent = None
                self.local_tunnel_id = None
                self.active_sessions = None
                self.class_name = None
                self.digest_secrets = None
                self.is_congestion_control_enabled = None
                self.is_pmtu_enabled = None
                self.is_tunnel_up = None
                self.local_address = None
                self.local_port = None
                self.local_tunnel_name = None
                self.local_window_size = None
                self.maximum_retransmission_time = None
                self.order_queue_size = None
                self.packet_queue_check = None
                self.protocol = None
                self.remote_address = None
                self.remote_port = None
                self.remote_tunnel_id = None
                self.remote_tunnel_name = None
                self.remote_window_size = None
                self.resend_maximum_queue_size = None
                self.resend_queue_size = None
                self.resends = None
                self.retransmission_time = None
                self.retransmit_time = YLeafList()
                self.retransmit_time.parent = self
                self.retransmit_time.name = 'retransmit_time'
                self.sequence_nr = None
                self.sequence_ns = None
                self.total_out_of_order_drop_packets = None
                self.total_out_of_order_reorder_packets = None
                self.total_peer_authentication_failures = None
                self.unsent_maximum_queue_size = None
                self.unsent_queue_size = None
                self.zero_length_body_acknowledgement_sent = None

            @property
            def _common_path(self):
                if self.local_tunnel_id is None:
                    raise YPYModelError('Key property local_tunnel_id is None')

                return '/Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/Cisco-IOS-XR-tunnel-l2tun-oper:tunnels/Cisco-IOS-XR-tunnel-l2tun-oper:tunnel[Cisco-IOS-XR-tunnel-l2tun-oper:local-tunnel-id = ' + str(self.local_tunnel_id) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.local_tunnel_id is not None:
                    return True

                if self.active_sessions is not None:
                    return True

                if self.class_name is not None:
                    return True

                if self.digest_secrets is not None:
                    return True

                if self.is_congestion_control_enabled is not None:
                    return True

                if self.is_pmtu_enabled is not None:
                    return True

                if self.is_tunnel_up is not None:
                    return True

                if self.local_address is not None:
                    return True

                if self.local_port is not None:
                    return True

                if self.local_tunnel_name is not None:
                    return True

                if self.local_window_size is not None:
                    return True

                if self.maximum_retransmission_time is not None:
                    return True

                if self.order_queue_size is not None:
                    return True

                if self.packet_queue_check is not None:
                    return True

                if self.protocol is not None:
                    return True

                if self.remote_address is not None:
                    return True

                if self.remote_port is not None:
                    return True

                if self.remote_tunnel_id is not None:
                    return True

                if self.remote_tunnel_name is not None:
                    return True

                if self.remote_window_size is not None:
                    return True

                if self.resend_maximum_queue_size is not None:
                    return True

                if self.resend_queue_size is not None:
                    return True

                if self.resends is not None:
                    return True

                if self.retransmission_time is not None:
                    return True

                if self.retransmit_time is not None:
                    for child in self.retransmit_time:
                        if child is not None:
                            return True

                if self.sequence_nr is not None:
                    return True

                if self.sequence_ns is not None:
                    return True

                if self.total_out_of_order_drop_packets is not None:
                    return True

                if self.total_out_of_order_reorder_packets is not None:
                    return True

                if self.total_peer_authentication_failures is not None:
                    return True

                if self.unsent_maximum_queue_size is not None:
                    return True

                if self.unsent_queue_size is not None:
                    return True

                if self.zero_length_body_acknowledgement_sent is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                return meta._meta_table['L2Tp.Tunnels.Tunnel']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/Cisco-IOS-XR-tunnel-l2tun-oper:tunnels'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.tunnel is not None:
                for child_ref in self.tunnel:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
            return meta._meta_table['L2Tp.Tunnels']['meta_info']


    class Sessions(object):
        """
        List of session IDs
        
        .. attribute:: session
        
        	L2TP information for a particular session
        	**type**\: list of    :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tp.Sessions.Session>`
        
        

        """

        _prefix = 'tunnel-l2tun-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.session = YList()
            self.session.parent = self
            self.session.name = 'session'


        class Session(object):
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
                self.parent = None
                self.local_tunnel_id = None
                self.local_session_id = None
                self.call_serial_number = None
                self.interface_name = None
                self.is_conditional_debug_enabled = None
                self.is_sequencing_on = None
                self.is_session_locally_initiated = None
                self.is_session_manual = None
                self.is_session_state_established = None
                self.is_session_up = None
                self.is_udp_checksum_enabled = None
                self.l2tp_sh_sess_tie_breaker = None
                self.l2tp_sh_sess_tie_breaker_enabled = None
                self.l2tp_sh_sess_udp_lport = None
                self.l2tp_sh_sess_udp_rport = None
                self.local_ip_address = None
                self.local_tunnel_name = None
                self.protocol = None
                self.remote_ip_address = None
                self.remote_session_id = None
                self.remote_tunnel_id = None
                self.remote_tunnel_name = None
                self.session_application_data = L2Tp.Sessions.Session.SessionApplicationData()
                self.session_application_data.parent = self
                self.unique_id = None


            class SessionApplicationData(object):
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
                    self.parent = None
                    self.l2tp_sh_sess_app_type = None
                    self.vpdn = L2Tp.Sessions.Session.SessionApplicationData.Vpdn()
                    self.vpdn.parent = self
                    self.xconnect = L2Tp.Sessions.Session.SessionApplicationData.Xconnect()
                    self.xconnect.parent = self


                class Xconnect(object):
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
                        self.parent = None
                        self.circuit_name = None
                        self.ipv6_protocol_tunneling = None
                        self.is_circuit_state_up = None
                        self.is_local_circuit_state_up = None
                        self.is_remote_circuit_state_up = None
                        self.sessionvc_id = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-tunnel-l2tun-oper:xconnect'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.circuit_name is not None:
                            return True

                        if self.ipv6_protocol_tunneling is not None:
                            return True

                        if self.is_circuit_state_up is not None:
                            return True

                        if self.is_local_circuit_state_up is not None:
                            return True

                        if self.is_remote_circuit_state_up is not None:
                            return True

                        if self.sessionvc_id is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                        return meta._meta_table['L2Tp.Sessions.Session.SessionApplicationData.Xconnect']['meta_info']


                class Vpdn(object):
                    """
                    VPDN data
                    
                    .. attribute:: interface_name
                    
                    	Interface name
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: username
                    
                    	Session username
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'tunnel-l2tun-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.interface_name = None
                        self.username = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-tunnel-l2tun-oper:vpdn'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.interface_name is not None:
                            return True

                        if self.username is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                        return meta._meta_table['L2Tp.Sessions.Session.SessionApplicationData.Vpdn']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-tunnel-l2tun-oper:session-application-data'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.l2tp_sh_sess_app_type is not None:
                        return True

                    if self.vpdn is not None and self.vpdn._has_data():
                        return True

                    if self.xconnect is not None and self.xconnect._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                    return meta._meta_table['L2Tp.Sessions.Session.SessionApplicationData']['meta_info']

            @property
            def _common_path(self):
                if self.local_tunnel_id is None:
                    raise YPYModelError('Key property local_tunnel_id is None')
                if self.local_session_id is None:
                    raise YPYModelError('Key property local_session_id is None')

                return '/Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/Cisco-IOS-XR-tunnel-l2tun-oper:sessions/Cisco-IOS-XR-tunnel-l2tun-oper:session[Cisco-IOS-XR-tunnel-l2tun-oper:local-tunnel-id = ' + str(self.local_tunnel_id) + '][Cisco-IOS-XR-tunnel-l2tun-oper:local-session-id = ' + str(self.local_session_id) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.local_tunnel_id is not None:
                    return True

                if self.local_session_id is not None:
                    return True

                if self.call_serial_number is not None:
                    return True

                if self.interface_name is not None:
                    return True

                if self.is_conditional_debug_enabled is not None:
                    return True

                if self.is_sequencing_on is not None:
                    return True

                if self.is_session_locally_initiated is not None:
                    return True

                if self.is_session_manual is not None:
                    return True

                if self.is_session_state_established is not None:
                    return True

                if self.is_session_up is not None:
                    return True

                if self.is_udp_checksum_enabled is not None:
                    return True

                if self.l2tp_sh_sess_tie_breaker is not None:
                    return True

                if self.l2tp_sh_sess_tie_breaker_enabled is not None:
                    return True

                if self.l2tp_sh_sess_udp_lport is not None:
                    return True

                if self.l2tp_sh_sess_udp_rport is not None:
                    return True

                if self.local_ip_address is not None:
                    return True

                if self.local_tunnel_name is not None:
                    return True

                if self.protocol is not None:
                    return True

                if self.remote_ip_address is not None:
                    return True

                if self.remote_session_id is not None:
                    return True

                if self.remote_tunnel_id is not None:
                    return True

                if self.remote_tunnel_name is not None:
                    return True

                if self.session_application_data is not None and self.session_application_data._has_data():
                    return True

                if self.unique_id is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                return meta._meta_table['L2Tp.Sessions.Session']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/Cisco-IOS-XR-tunnel-l2tun-oper:sessions'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.session is not None:
                for child_ref in self.session:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
            return meta._meta_table['L2Tp.Sessions']['meta_info']


    class Session(object):
        """
        L2TP control messages counters
        
        .. attribute:: unavailable
        
        	L2TP session unavailable  information
        	**type**\:   :py:class:`Unavailable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tp.Session.Unavailable>`
        
        

        """

        _prefix = 'tunnel-l2tun-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.unavailable = L2Tp.Session.Unavailable()
            self.unavailable.parent = self


        class Unavailable(object):
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
                self.parent = None
                self.sessions_on_hold = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/Cisco-IOS-XR-tunnel-l2tun-oper:session/Cisco-IOS-XR-tunnel-l2tun-oper:unavailable'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.sessions_on_hold is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                return meta._meta_table['L2Tp.Session.Unavailable']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-tunnel-l2tun-oper:l2tp/Cisco-IOS-XR-tunnel-l2tun-oper:session'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.unavailable is not None and self.unavailable._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
            return meta._meta_table['L2Tp.Session']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-tunnel-l2tun-oper:l2tp'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.classes is not None and self.classes._has_data():
            return True

        if self.counter_hist_fail is not None and self.counter_hist_fail._has_data():
            return True

        if self.counters is not None and self.counters._has_data():
            return True

        if self.session is not None and self.session._has_data():
            return True

        if self.sessions is not None and self.sessions._has_data():
            return True

        if self.tunnel_configurations is not None and self.tunnel_configurations._has_data():
            return True

        if self.tunnels is not None and self.tunnels._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
        return meta._meta_table['L2Tp']['meta_info']


class L2Tpv2(object):
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
        self.classes = L2Tpv2.Classes()
        self.classes.parent = self
        self.counter_hist_fail = L2Tpv2.CounterHistFail()
        self.counter_hist_fail.parent = self
        self.counters = L2Tpv2.Counters()
        self.counters.parent = self
        self.session = L2Tpv2.Session()
        self.session.parent = self
        self.sessions = L2Tpv2.Sessions()
        self.sessions.parent = self
        self.statistics = L2Tpv2.Statistics()
        self.statistics.parent = self
        self.tunnel = L2Tpv2.Tunnel()
        self.tunnel.parent = self
        self.tunnel_configurations = L2Tpv2.TunnelConfigurations()
        self.tunnel_configurations.parent = self
        self.tunnels = L2Tpv2.Tunnels()
        self.tunnels.parent = self


    class Counters(object):
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
            self.parent = None
            self.control = L2Tpv2.Counters.Control()
            self.control.parent = self
            self.forwarding = L2Tpv2.Counters.Forwarding()
            self.forwarding.parent = self


        class Forwarding(object):
            """
            L2TP forwarding messages counters
            
            .. attribute:: sessions
            
            	List of class and session IDs
            	**type**\:   :py:class:`Sessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tpv2.Counters.Forwarding.Sessions>`
            
            

            """

            _prefix = 'tunnel-l2tun-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.sessions = L2Tpv2.Counters.Forwarding.Sessions()
                self.sessions.parent = self


            class Sessions(object):
                """
                List of class and session IDs
                
                .. attribute:: session
                
                	L2TP information for a particular session
                	**type**\: list of    :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tpv2.Counters.Forwarding.Sessions.Session>`
                
                

                """

                _prefix = 'tunnel-l2tun-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.session = YList()
                    self.session.parent = self
                    self.session.name = 'session'


                class Session(object):
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
                        self.parent = None
                        self.tunnel_id = None
                        self.session_id = None
                        self.in_bytes = None
                        self.in_packets = None
                        self.out_bytes = None
                        self.out_packets = None
                        self.remote_session_id = None

                    @property
                    def _common_path(self):
                        if self.tunnel_id is None:
                            raise YPYModelError('Key property tunnel_id is None')
                        if self.session_id is None:
                            raise YPYModelError('Key property session_id is None')

                        return '/Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/Cisco-IOS-XR-tunnel-l2tun-oper:counters/Cisco-IOS-XR-tunnel-l2tun-oper:forwarding/Cisco-IOS-XR-tunnel-l2tun-oper:sessions/Cisco-IOS-XR-tunnel-l2tun-oper:session[Cisco-IOS-XR-tunnel-l2tun-oper:tunnel-id = ' + str(self.tunnel_id) + '][Cisco-IOS-XR-tunnel-l2tun-oper:session-id = ' + str(self.session_id) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.tunnel_id is not None:
                            return True

                        if self.session_id is not None:
                            return True

                        if self.in_bytes is not None:
                            return True

                        if self.in_packets is not None:
                            return True

                        if self.out_bytes is not None:
                            return True

                        if self.out_packets is not None:
                            return True

                        if self.remote_session_id is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                        return meta._meta_table['L2Tpv2.Counters.Forwarding.Sessions.Session']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/Cisco-IOS-XR-tunnel-l2tun-oper:counters/Cisco-IOS-XR-tunnel-l2tun-oper:forwarding/Cisco-IOS-XR-tunnel-l2tun-oper:sessions'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.session is not None:
                        for child_ref in self.session:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                    return meta._meta_table['L2Tpv2.Counters.Forwarding.Sessions']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/Cisco-IOS-XR-tunnel-l2tun-oper:counters/Cisco-IOS-XR-tunnel-l2tun-oper:forwarding'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.sessions is not None and self.sessions._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                return meta._meta_table['L2Tpv2.Counters.Forwarding']['meta_info']


        class Control(object):
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
                self.parent = None
                self.tunnel_xr = L2Tpv2.Counters.Control.TunnelXr()
                self.tunnel_xr.parent = self
                self.tunnels = L2Tpv2.Counters.Control.Tunnels()
                self.tunnels.parent = self


            class TunnelXr(object):
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
                    self.parent = None
                    self.authentication = L2Tpv2.Counters.Control.TunnelXr.Authentication()
                    self.authentication.parent = self
                    self.global_ = L2Tpv2.Counters.Control.TunnelXr.Global_()
                    self.global_.parent = self


                class Authentication(object):
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
                        self.parent = None
                        self.challenge_avp = L2Tpv2.Counters.Control.TunnelXr.Authentication.ChallengeAvp()
                        self.challenge_avp.parent = self
                        self.challenge_reponse = L2Tpv2.Counters.Control.TunnelXr.Authentication.ChallengeReponse()
                        self.challenge_reponse.parent = self
                        self.common_digest = L2Tpv2.Counters.Control.TunnelXr.Authentication.CommonDigest()
                        self.common_digest.parent = self
                        self.integrity_check = L2Tpv2.Counters.Control.TunnelXr.Authentication.IntegrityCheck()
                        self.integrity_check.parent = self
                        self.local_secret = L2Tpv2.Counters.Control.TunnelXr.Authentication.LocalSecret()
                        self.local_secret.parent = self
                        self.nonce_avp = L2Tpv2.Counters.Control.TunnelXr.Authentication.NonceAvp()
                        self.nonce_avp.parent = self
                        self.overall_statistics = L2Tpv2.Counters.Control.TunnelXr.Authentication.OverallStatistics()
                        self.overall_statistics.parent = self
                        self.primary_digest = L2Tpv2.Counters.Control.TunnelXr.Authentication.PrimaryDigest()
                        self.primary_digest.parent = self
                        self.secondary_digest = L2Tpv2.Counters.Control.TunnelXr.Authentication.SecondaryDigest()
                        self.secondary_digest.parent = self


                    class NonceAvp(object):
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
                            self.parent = None
                            self.bad_hash = None
                            self.bad_length = None
                            self.failed = None
                            self.generate_response_failures = None
                            self.ignored = None
                            self.missing = None
                            self.passed = None
                            self.skipped = None
                            self.unexpected = None
                            self.unexpected_zlb = None
                            self.validate = None

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/Cisco-IOS-XR-tunnel-l2tun-oper:counters/Cisco-IOS-XR-tunnel-l2tun-oper:control/Cisco-IOS-XR-tunnel-l2tun-oper:tunnel-xr/Cisco-IOS-XR-tunnel-l2tun-oper:authentication/Cisco-IOS-XR-tunnel-l2tun-oper:nonce-avp'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.bad_hash is not None:
                                return True

                            if self.bad_length is not None:
                                return True

                            if self.failed is not None:
                                return True

                            if self.generate_response_failures is not None:
                                return True

                            if self.ignored is not None:
                                return True

                            if self.missing is not None:
                                return True

                            if self.passed is not None:
                                return True

                            if self.skipped is not None:
                                return True

                            if self.unexpected is not None:
                                return True

                            if self.unexpected_zlb is not None:
                                return True

                            if self.validate is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                            return meta._meta_table['L2Tpv2.Counters.Control.TunnelXr.Authentication.NonceAvp']['meta_info']


                    class CommonDigest(object):
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
                            self.parent = None
                            self.bad_hash = None
                            self.bad_length = None
                            self.failed = None
                            self.generate_response_failures = None
                            self.ignored = None
                            self.missing = None
                            self.passed = None
                            self.skipped = None
                            self.unexpected = None
                            self.unexpected_zlb = None
                            self.validate = None

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/Cisco-IOS-XR-tunnel-l2tun-oper:counters/Cisco-IOS-XR-tunnel-l2tun-oper:control/Cisco-IOS-XR-tunnel-l2tun-oper:tunnel-xr/Cisco-IOS-XR-tunnel-l2tun-oper:authentication/Cisco-IOS-XR-tunnel-l2tun-oper:common-digest'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.bad_hash is not None:
                                return True

                            if self.bad_length is not None:
                                return True

                            if self.failed is not None:
                                return True

                            if self.generate_response_failures is not None:
                                return True

                            if self.ignored is not None:
                                return True

                            if self.missing is not None:
                                return True

                            if self.passed is not None:
                                return True

                            if self.skipped is not None:
                                return True

                            if self.unexpected is not None:
                                return True

                            if self.unexpected_zlb is not None:
                                return True

                            if self.validate is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                            return meta._meta_table['L2Tpv2.Counters.Control.TunnelXr.Authentication.CommonDigest']['meta_info']


                    class PrimaryDigest(object):
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
                            self.parent = None
                            self.bad_hash = None
                            self.bad_length = None
                            self.failed = None
                            self.generate_response_failures = None
                            self.ignored = None
                            self.missing = None
                            self.passed = None
                            self.skipped = None
                            self.unexpected = None
                            self.unexpected_zlb = None
                            self.validate = None

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/Cisco-IOS-XR-tunnel-l2tun-oper:counters/Cisco-IOS-XR-tunnel-l2tun-oper:control/Cisco-IOS-XR-tunnel-l2tun-oper:tunnel-xr/Cisco-IOS-XR-tunnel-l2tun-oper:authentication/Cisco-IOS-XR-tunnel-l2tun-oper:primary-digest'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.bad_hash is not None:
                                return True

                            if self.bad_length is not None:
                                return True

                            if self.failed is not None:
                                return True

                            if self.generate_response_failures is not None:
                                return True

                            if self.ignored is not None:
                                return True

                            if self.missing is not None:
                                return True

                            if self.passed is not None:
                                return True

                            if self.skipped is not None:
                                return True

                            if self.unexpected is not None:
                                return True

                            if self.unexpected_zlb is not None:
                                return True

                            if self.validate is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                            return meta._meta_table['L2Tpv2.Counters.Control.TunnelXr.Authentication.PrimaryDigest']['meta_info']


                    class SecondaryDigest(object):
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
                            self.parent = None
                            self.bad_hash = None
                            self.bad_length = None
                            self.failed = None
                            self.generate_response_failures = None
                            self.ignored = None
                            self.missing = None
                            self.passed = None
                            self.skipped = None
                            self.unexpected = None
                            self.unexpected_zlb = None
                            self.validate = None

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/Cisco-IOS-XR-tunnel-l2tun-oper:counters/Cisco-IOS-XR-tunnel-l2tun-oper:control/Cisco-IOS-XR-tunnel-l2tun-oper:tunnel-xr/Cisco-IOS-XR-tunnel-l2tun-oper:authentication/Cisco-IOS-XR-tunnel-l2tun-oper:secondary-digest'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.bad_hash is not None:
                                return True

                            if self.bad_length is not None:
                                return True

                            if self.failed is not None:
                                return True

                            if self.generate_response_failures is not None:
                                return True

                            if self.ignored is not None:
                                return True

                            if self.missing is not None:
                                return True

                            if self.passed is not None:
                                return True

                            if self.skipped is not None:
                                return True

                            if self.unexpected is not None:
                                return True

                            if self.unexpected_zlb is not None:
                                return True

                            if self.validate is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                            return meta._meta_table['L2Tpv2.Counters.Control.TunnelXr.Authentication.SecondaryDigest']['meta_info']


                    class IntegrityCheck(object):
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
                            self.parent = None
                            self.bad_hash = None
                            self.bad_length = None
                            self.failed = None
                            self.generate_response_failures = None
                            self.ignored = None
                            self.missing = None
                            self.passed = None
                            self.skipped = None
                            self.unexpected = None
                            self.unexpected_zlb = None
                            self.validate = None

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/Cisco-IOS-XR-tunnel-l2tun-oper:counters/Cisco-IOS-XR-tunnel-l2tun-oper:control/Cisco-IOS-XR-tunnel-l2tun-oper:tunnel-xr/Cisco-IOS-XR-tunnel-l2tun-oper:authentication/Cisco-IOS-XR-tunnel-l2tun-oper:integrity-check'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.bad_hash is not None:
                                return True

                            if self.bad_length is not None:
                                return True

                            if self.failed is not None:
                                return True

                            if self.generate_response_failures is not None:
                                return True

                            if self.ignored is not None:
                                return True

                            if self.missing is not None:
                                return True

                            if self.passed is not None:
                                return True

                            if self.skipped is not None:
                                return True

                            if self.unexpected is not None:
                                return True

                            if self.unexpected_zlb is not None:
                                return True

                            if self.validate is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                            return meta._meta_table['L2Tpv2.Counters.Control.TunnelXr.Authentication.IntegrityCheck']['meta_info']


                    class LocalSecret(object):
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
                            self.parent = None
                            self.bad_hash = None
                            self.bad_length = None
                            self.failed = None
                            self.generate_response_failures = None
                            self.ignored = None
                            self.missing = None
                            self.passed = None
                            self.skipped = None
                            self.unexpected = None
                            self.unexpected_zlb = None
                            self.validate = None

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/Cisco-IOS-XR-tunnel-l2tun-oper:counters/Cisco-IOS-XR-tunnel-l2tun-oper:control/Cisco-IOS-XR-tunnel-l2tun-oper:tunnel-xr/Cisco-IOS-XR-tunnel-l2tun-oper:authentication/Cisco-IOS-XR-tunnel-l2tun-oper:local-secret'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.bad_hash is not None:
                                return True

                            if self.bad_length is not None:
                                return True

                            if self.failed is not None:
                                return True

                            if self.generate_response_failures is not None:
                                return True

                            if self.ignored is not None:
                                return True

                            if self.missing is not None:
                                return True

                            if self.passed is not None:
                                return True

                            if self.skipped is not None:
                                return True

                            if self.unexpected is not None:
                                return True

                            if self.unexpected_zlb is not None:
                                return True

                            if self.validate is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                            return meta._meta_table['L2Tpv2.Counters.Control.TunnelXr.Authentication.LocalSecret']['meta_info']


                    class ChallengeAvp(object):
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
                            self.parent = None
                            self.bad_hash = None
                            self.bad_length = None
                            self.failed = None
                            self.generate_response_failures = None
                            self.ignored = None
                            self.missing = None
                            self.passed = None
                            self.skipped = None
                            self.unexpected = None
                            self.unexpected_zlb = None
                            self.validate = None

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/Cisco-IOS-XR-tunnel-l2tun-oper:counters/Cisco-IOS-XR-tunnel-l2tun-oper:control/Cisco-IOS-XR-tunnel-l2tun-oper:tunnel-xr/Cisco-IOS-XR-tunnel-l2tun-oper:authentication/Cisco-IOS-XR-tunnel-l2tun-oper:challenge-avp'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.bad_hash is not None:
                                return True

                            if self.bad_length is not None:
                                return True

                            if self.failed is not None:
                                return True

                            if self.generate_response_failures is not None:
                                return True

                            if self.ignored is not None:
                                return True

                            if self.missing is not None:
                                return True

                            if self.passed is not None:
                                return True

                            if self.skipped is not None:
                                return True

                            if self.unexpected is not None:
                                return True

                            if self.unexpected_zlb is not None:
                                return True

                            if self.validate is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                            return meta._meta_table['L2Tpv2.Counters.Control.TunnelXr.Authentication.ChallengeAvp']['meta_info']


                    class ChallengeReponse(object):
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
                            self.parent = None
                            self.bad_hash = None
                            self.bad_length = None
                            self.failed = None
                            self.generate_response_failures = None
                            self.ignored = None
                            self.missing = None
                            self.passed = None
                            self.skipped = None
                            self.unexpected = None
                            self.unexpected_zlb = None
                            self.validate = None

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/Cisco-IOS-XR-tunnel-l2tun-oper:counters/Cisco-IOS-XR-tunnel-l2tun-oper:control/Cisco-IOS-XR-tunnel-l2tun-oper:tunnel-xr/Cisco-IOS-XR-tunnel-l2tun-oper:authentication/Cisco-IOS-XR-tunnel-l2tun-oper:challenge-reponse'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.bad_hash is not None:
                                return True

                            if self.bad_length is not None:
                                return True

                            if self.failed is not None:
                                return True

                            if self.generate_response_failures is not None:
                                return True

                            if self.ignored is not None:
                                return True

                            if self.missing is not None:
                                return True

                            if self.passed is not None:
                                return True

                            if self.skipped is not None:
                                return True

                            if self.unexpected is not None:
                                return True

                            if self.unexpected_zlb is not None:
                                return True

                            if self.validate is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                            return meta._meta_table['L2Tpv2.Counters.Control.TunnelXr.Authentication.ChallengeReponse']['meta_info']


                    class OverallStatistics(object):
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
                            self.parent = None
                            self.bad_hash = None
                            self.bad_length = None
                            self.failed = None
                            self.generate_response_failures = None
                            self.ignored = None
                            self.missing = None
                            self.passed = None
                            self.skipped = None
                            self.unexpected = None
                            self.unexpected_zlb = None
                            self.validate = None

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/Cisco-IOS-XR-tunnel-l2tun-oper:counters/Cisco-IOS-XR-tunnel-l2tun-oper:control/Cisco-IOS-XR-tunnel-l2tun-oper:tunnel-xr/Cisco-IOS-XR-tunnel-l2tun-oper:authentication/Cisco-IOS-XR-tunnel-l2tun-oper:overall-statistics'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.bad_hash is not None:
                                return True

                            if self.bad_length is not None:
                                return True

                            if self.failed is not None:
                                return True

                            if self.generate_response_failures is not None:
                                return True

                            if self.ignored is not None:
                                return True

                            if self.missing is not None:
                                return True

                            if self.passed is not None:
                                return True

                            if self.skipped is not None:
                                return True

                            if self.unexpected is not None:
                                return True

                            if self.unexpected_zlb is not None:
                                return True

                            if self.validate is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                            return meta._meta_table['L2Tpv2.Counters.Control.TunnelXr.Authentication.OverallStatistics']['meta_info']

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/Cisco-IOS-XR-tunnel-l2tun-oper:counters/Cisco-IOS-XR-tunnel-l2tun-oper:control/Cisco-IOS-XR-tunnel-l2tun-oper:tunnel-xr/Cisco-IOS-XR-tunnel-l2tun-oper:authentication'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.challenge_avp is not None and self.challenge_avp._has_data():
                            return True

                        if self.challenge_reponse is not None and self.challenge_reponse._has_data():
                            return True

                        if self.common_digest is not None and self.common_digest._has_data():
                            return True

                        if self.integrity_check is not None and self.integrity_check._has_data():
                            return True

                        if self.local_secret is not None and self.local_secret._has_data():
                            return True

                        if self.nonce_avp is not None and self.nonce_avp._has_data():
                            return True

                        if self.overall_statistics is not None and self.overall_statistics._has_data():
                            return True

                        if self.primary_digest is not None and self.primary_digest._has_data():
                            return True

                        if self.secondary_digest is not None and self.secondary_digest._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                        return meta._meta_table['L2Tpv2.Counters.Control.TunnelXr.Authentication']['meta_info']


                class Global_(object):
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
                        self.parent = None
                        self.drop = L2Tpv2.Counters.Control.TunnelXr.Global_.Drop()
                        self.drop.parent = self
                        self.received = L2Tpv2.Counters.Control.TunnelXr.Global_.Received()
                        self.received.parent = self
                        self.retransmit = L2Tpv2.Counters.Control.TunnelXr.Global_.Retransmit()
                        self.retransmit.parent = self
                        self.total_drop = None
                        self.total_received = None
                        self.total_retransmit = None
                        self.total_transmit = None
                        self.transmit = L2Tpv2.Counters.Control.TunnelXr.Global_.Transmit()
                        self.transmit.parent = self


                    class Transmit(object):
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
                            self.parent = None
                            self.acknowledgement_packets = None
                            self.call_disconnect_notify_packets = None
                            self.hello_packets = None
                            self.incoming_call_connected_packets = None
                            self.incoming_call_replies = None
                            self.incoming_call_requests = None
                            self.outgoing_call_connected_packets = None
                            self.outgoing_call_replies = None
                            self.outgoing_call_requests = None
                            self.service_relay_replies = None
                            self.service_relay_requests = None
                            self.set_link_info_packets = None
                            self.start_control_connection_notifications = None
                            self.start_control_connection_replies = None
                            self.start_control_connection_requests = None
                            self.stop_control_connection_notifications = None
                            self.unknown_packets = None
                            self.wan_error_notify_packets = None
                            self.zero_length_body_packets = None

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/Cisco-IOS-XR-tunnel-l2tun-oper:counters/Cisco-IOS-XR-tunnel-l2tun-oper:control/Cisco-IOS-XR-tunnel-l2tun-oper:tunnel-xr/Cisco-IOS-XR-tunnel-l2tun-oper:global/Cisco-IOS-XR-tunnel-l2tun-oper:transmit'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.acknowledgement_packets is not None:
                                return True

                            if self.call_disconnect_notify_packets is not None:
                                return True

                            if self.hello_packets is not None:
                                return True

                            if self.incoming_call_connected_packets is not None:
                                return True

                            if self.incoming_call_replies is not None:
                                return True

                            if self.incoming_call_requests is not None:
                                return True

                            if self.outgoing_call_connected_packets is not None:
                                return True

                            if self.outgoing_call_replies is not None:
                                return True

                            if self.outgoing_call_requests is not None:
                                return True

                            if self.service_relay_replies is not None:
                                return True

                            if self.service_relay_requests is not None:
                                return True

                            if self.set_link_info_packets is not None:
                                return True

                            if self.start_control_connection_notifications is not None:
                                return True

                            if self.start_control_connection_replies is not None:
                                return True

                            if self.start_control_connection_requests is not None:
                                return True

                            if self.stop_control_connection_notifications is not None:
                                return True

                            if self.unknown_packets is not None:
                                return True

                            if self.wan_error_notify_packets is not None:
                                return True

                            if self.zero_length_body_packets is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                            return meta._meta_table['L2Tpv2.Counters.Control.TunnelXr.Global_.Transmit']['meta_info']


                    class Retransmit(object):
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
                            self.parent = None
                            self.acknowledgement_packets = None
                            self.call_disconnect_notify_packets = None
                            self.hello_packets = None
                            self.incoming_call_connected_packets = None
                            self.incoming_call_replies = None
                            self.incoming_call_requests = None
                            self.outgoing_call_connected_packets = None
                            self.outgoing_call_replies = None
                            self.outgoing_call_requests = None
                            self.service_relay_replies = None
                            self.service_relay_requests = None
                            self.set_link_info_packets = None
                            self.start_control_connection_notifications = None
                            self.start_control_connection_replies = None
                            self.start_control_connection_requests = None
                            self.stop_control_connection_notifications = None
                            self.unknown_packets = None
                            self.wan_error_notify_packets = None
                            self.zero_length_body_packets = None

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/Cisco-IOS-XR-tunnel-l2tun-oper:counters/Cisco-IOS-XR-tunnel-l2tun-oper:control/Cisco-IOS-XR-tunnel-l2tun-oper:tunnel-xr/Cisco-IOS-XR-tunnel-l2tun-oper:global/Cisco-IOS-XR-tunnel-l2tun-oper:retransmit'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.acknowledgement_packets is not None:
                                return True

                            if self.call_disconnect_notify_packets is not None:
                                return True

                            if self.hello_packets is not None:
                                return True

                            if self.incoming_call_connected_packets is not None:
                                return True

                            if self.incoming_call_replies is not None:
                                return True

                            if self.incoming_call_requests is not None:
                                return True

                            if self.outgoing_call_connected_packets is not None:
                                return True

                            if self.outgoing_call_replies is not None:
                                return True

                            if self.outgoing_call_requests is not None:
                                return True

                            if self.service_relay_replies is not None:
                                return True

                            if self.service_relay_requests is not None:
                                return True

                            if self.set_link_info_packets is not None:
                                return True

                            if self.start_control_connection_notifications is not None:
                                return True

                            if self.start_control_connection_replies is not None:
                                return True

                            if self.start_control_connection_requests is not None:
                                return True

                            if self.stop_control_connection_notifications is not None:
                                return True

                            if self.unknown_packets is not None:
                                return True

                            if self.wan_error_notify_packets is not None:
                                return True

                            if self.zero_length_body_packets is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                            return meta._meta_table['L2Tpv2.Counters.Control.TunnelXr.Global_.Retransmit']['meta_info']


                    class Received(object):
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
                            self.parent = None
                            self.acknowledgement_packets = None
                            self.call_disconnect_notify_packets = None
                            self.hello_packets = None
                            self.incoming_call_connected_packets = None
                            self.incoming_call_replies = None
                            self.incoming_call_requests = None
                            self.outgoing_call_connected_packets = None
                            self.outgoing_call_replies = None
                            self.outgoing_call_requests = None
                            self.service_relay_replies = None
                            self.service_relay_requests = None
                            self.set_link_info_packets = None
                            self.start_control_connection_notifications = None
                            self.start_control_connection_replies = None
                            self.start_control_connection_requests = None
                            self.stop_control_connection_notifications = None
                            self.unknown_packets = None
                            self.wan_error_notify_packets = None
                            self.zero_length_body_packets = None

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/Cisco-IOS-XR-tunnel-l2tun-oper:counters/Cisco-IOS-XR-tunnel-l2tun-oper:control/Cisco-IOS-XR-tunnel-l2tun-oper:tunnel-xr/Cisco-IOS-XR-tunnel-l2tun-oper:global/Cisco-IOS-XR-tunnel-l2tun-oper:received'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.acknowledgement_packets is not None:
                                return True

                            if self.call_disconnect_notify_packets is not None:
                                return True

                            if self.hello_packets is not None:
                                return True

                            if self.incoming_call_connected_packets is not None:
                                return True

                            if self.incoming_call_replies is not None:
                                return True

                            if self.incoming_call_requests is not None:
                                return True

                            if self.outgoing_call_connected_packets is not None:
                                return True

                            if self.outgoing_call_replies is not None:
                                return True

                            if self.outgoing_call_requests is not None:
                                return True

                            if self.service_relay_replies is not None:
                                return True

                            if self.service_relay_requests is not None:
                                return True

                            if self.set_link_info_packets is not None:
                                return True

                            if self.start_control_connection_notifications is not None:
                                return True

                            if self.start_control_connection_replies is not None:
                                return True

                            if self.start_control_connection_requests is not None:
                                return True

                            if self.stop_control_connection_notifications is not None:
                                return True

                            if self.unknown_packets is not None:
                                return True

                            if self.wan_error_notify_packets is not None:
                                return True

                            if self.zero_length_body_packets is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                            return meta._meta_table['L2Tpv2.Counters.Control.TunnelXr.Global_.Received']['meta_info']


                    class Drop(object):
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
                            self.parent = None
                            self.acknowledgement_packets = None
                            self.call_disconnect_notify_packets = None
                            self.hello_packets = None
                            self.incoming_call_connected_packets = None
                            self.incoming_call_replies = None
                            self.incoming_call_requests = None
                            self.outgoing_call_connected_packets = None
                            self.outgoing_call_replies = None
                            self.outgoing_call_requests = None
                            self.service_relay_replies = None
                            self.service_relay_requests = None
                            self.set_link_info_packets = None
                            self.start_control_connection_notifications = None
                            self.start_control_connection_replies = None
                            self.start_control_connection_requests = None
                            self.stop_control_connection_notifications = None
                            self.unknown_packets = None
                            self.wan_error_notify_packets = None
                            self.zero_length_body_packets = None

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/Cisco-IOS-XR-tunnel-l2tun-oper:counters/Cisco-IOS-XR-tunnel-l2tun-oper:control/Cisco-IOS-XR-tunnel-l2tun-oper:tunnel-xr/Cisco-IOS-XR-tunnel-l2tun-oper:global/Cisco-IOS-XR-tunnel-l2tun-oper:drop'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.acknowledgement_packets is not None:
                                return True

                            if self.call_disconnect_notify_packets is not None:
                                return True

                            if self.hello_packets is not None:
                                return True

                            if self.incoming_call_connected_packets is not None:
                                return True

                            if self.incoming_call_replies is not None:
                                return True

                            if self.incoming_call_requests is not None:
                                return True

                            if self.outgoing_call_connected_packets is not None:
                                return True

                            if self.outgoing_call_replies is not None:
                                return True

                            if self.outgoing_call_requests is not None:
                                return True

                            if self.service_relay_replies is not None:
                                return True

                            if self.service_relay_requests is not None:
                                return True

                            if self.set_link_info_packets is not None:
                                return True

                            if self.start_control_connection_notifications is not None:
                                return True

                            if self.start_control_connection_replies is not None:
                                return True

                            if self.start_control_connection_requests is not None:
                                return True

                            if self.stop_control_connection_notifications is not None:
                                return True

                            if self.unknown_packets is not None:
                                return True

                            if self.wan_error_notify_packets is not None:
                                return True

                            if self.zero_length_body_packets is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                            return meta._meta_table['L2Tpv2.Counters.Control.TunnelXr.Global_.Drop']['meta_info']

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/Cisco-IOS-XR-tunnel-l2tun-oper:counters/Cisco-IOS-XR-tunnel-l2tun-oper:control/Cisco-IOS-XR-tunnel-l2tun-oper:tunnel-xr/Cisco-IOS-XR-tunnel-l2tun-oper:global'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.drop is not None and self.drop._has_data():
                            return True

                        if self.received is not None and self.received._has_data():
                            return True

                        if self.retransmit is not None and self.retransmit._has_data():
                            return True

                        if self.total_drop is not None:
                            return True

                        if self.total_received is not None:
                            return True

                        if self.total_retransmit is not None:
                            return True

                        if self.total_transmit is not None:
                            return True

                        if self.transmit is not None and self.transmit._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                        return meta._meta_table['L2Tpv2.Counters.Control.TunnelXr.Global_']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/Cisco-IOS-XR-tunnel-l2tun-oper:counters/Cisco-IOS-XR-tunnel-l2tun-oper:control/Cisco-IOS-XR-tunnel-l2tun-oper:tunnel-xr'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.authentication is not None and self.authentication._has_data():
                        return True

                    if self.global_ is not None and self.global_._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                    return meta._meta_table['L2Tpv2.Counters.Control.TunnelXr']['meta_info']


            class Tunnels(object):
                """
                Table of tunnel IDs of control message counters
                
                .. attribute:: tunnel
                
                	L2TP tunnel control message counters
                	**type**\: list of    :py:class:`Tunnel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tpv2.Counters.Control.Tunnels.Tunnel>`
                
                

                """

                _prefix = 'tunnel-l2tun-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.tunnel = YList()
                    self.tunnel.parent = self
                    self.tunnel.name = 'tunnel'


                class Tunnel(object):
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
                        self.parent = None
                        self.tunnel_id = None
                        self.brief = L2Tpv2.Counters.Control.Tunnels.Tunnel.Brief()
                        self.brief.parent = self
                        self.global_ = L2Tpv2.Counters.Control.Tunnels.Tunnel.Global_()
                        self.global_.parent = self


                    class Brief(object):
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
                            self.parent = None
                            self.local_address = None
                            self.remote_address = None
                            self.remote_tunnel_id = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-tunnel-l2tun-oper:brief'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.local_address is not None:
                                return True

                            if self.remote_address is not None:
                                return True

                            if self.remote_tunnel_id is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                            return meta._meta_table['L2Tpv2.Counters.Control.Tunnels.Tunnel.Brief']['meta_info']


                    class Global_(object):
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
                            self.parent = None
                            self.drop = L2Tpv2.Counters.Control.Tunnels.Tunnel.Global_.Drop()
                            self.drop.parent = self
                            self.received = L2Tpv2.Counters.Control.Tunnels.Tunnel.Global_.Received()
                            self.received.parent = self
                            self.retransmit = L2Tpv2.Counters.Control.Tunnels.Tunnel.Global_.Retransmit()
                            self.retransmit.parent = self
                            self.total_drop = None
                            self.total_received = None
                            self.total_retransmit = None
                            self.total_transmit = None
                            self.transmit = L2Tpv2.Counters.Control.Tunnels.Tunnel.Global_.Transmit()
                            self.transmit.parent = self


                        class Transmit(object):
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
                                self.parent = None
                                self.acknowledgement_packets = None
                                self.call_disconnect_notify_packets = None
                                self.hello_packets = None
                                self.incoming_call_connected_packets = None
                                self.incoming_call_replies = None
                                self.incoming_call_requests = None
                                self.outgoing_call_connected_packets = None
                                self.outgoing_call_replies = None
                                self.outgoing_call_requests = None
                                self.service_relay_replies = None
                                self.service_relay_requests = None
                                self.set_link_info_packets = None
                                self.start_control_connection_notifications = None
                                self.start_control_connection_replies = None
                                self.start_control_connection_requests = None
                                self.stop_control_connection_notifications = None
                                self.unknown_packets = None
                                self.wan_error_notify_packets = None
                                self.zero_length_body_packets = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-tunnel-l2tun-oper:transmit'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.acknowledgement_packets is not None:
                                    return True

                                if self.call_disconnect_notify_packets is not None:
                                    return True

                                if self.hello_packets is not None:
                                    return True

                                if self.incoming_call_connected_packets is not None:
                                    return True

                                if self.incoming_call_replies is not None:
                                    return True

                                if self.incoming_call_requests is not None:
                                    return True

                                if self.outgoing_call_connected_packets is not None:
                                    return True

                                if self.outgoing_call_replies is not None:
                                    return True

                                if self.outgoing_call_requests is not None:
                                    return True

                                if self.service_relay_replies is not None:
                                    return True

                                if self.service_relay_requests is not None:
                                    return True

                                if self.set_link_info_packets is not None:
                                    return True

                                if self.start_control_connection_notifications is not None:
                                    return True

                                if self.start_control_connection_replies is not None:
                                    return True

                                if self.start_control_connection_requests is not None:
                                    return True

                                if self.stop_control_connection_notifications is not None:
                                    return True

                                if self.unknown_packets is not None:
                                    return True

                                if self.wan_error_notify_packets is not None:
                                    return True

                                if self.zero_length_body_packets is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                                return meta._meta_table['L2Tpv2.Counters.Control.Tunnels.Tunnel.Global_.Transmit']['meta_info']


                        class Retransmit(object):
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
                                self.parent = None
                                self.acknowledgement_packets = None
                                self.call_disconnect_notify_packets = None
                                self.hello_packets = None
                                self.incoming_call_connected_packets = None
                                self.incoming_call_replies = None
                                self.incoming_call_requests = None
                                self.outgoing_call_connected_packets = None
                                self.outgoing_call_replies = None
                                self.outgoing_call_requests = None
                                self.service_relay_replies = None
                                self.service_relay_requests = None
                                self.set_link_info_packets = None
                                self.start_control_connection_notifications = None
                                self.start_control_connection_replies = None
                                self.start_control_connection_requests = None
                                self.stop_control_connection_notifications = None
                                self.unknown_packets = None
                                self.wan_error_notify_packets = None
                                self.zero_length_body_packets = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-tunnel-l2tun-oper:retransmit'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.acknowledgement_packets is not None:
                                    return True

                                if self.call_disconnect_notify_packets is not None:
                                    return True

                                if self.hello_packets is not None:
                                    return True

                                if self.incoming_call_connected_packets is not None:
                                    return True

                                if self.incoming_call_replies is not None:
                                    return True

                                if self.incoming_call_requests is not None:
                                    return True

                                if self.outgoing_call_connected_packets is not None:
                                    return True

                                if self.outgoing_call_replies is not None:
                                    return True

                                if self.outgoing_call_requests is not None:
                                    return True

                                if self.service_relay_replies is not None:
                                    return True

                                if self.service_relay_requests is not None:
                                    return True

                                if self.set_link_info_packets is not None:
                                    return True

                                if self.start_control_connection_notifications is not None:
                                    return True

                                if self.start_control_connection_replies is not None:
                                    return True

                                if self.start_control_connection_requests is not None:
                                    return True

                                if self.stop_control_connection_notifications is not None:
                                    return True

                                if self.unknown_packets is not None:
                                    return True

                                if self.wan_error_notify_packets is not None:
                                    return True

                                if self.zero_length_body_packets is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                                return meta._meta_table['L2Tpv2.Counters.Control.Tunnels.Tunnel.Global_.Retransmit']['meta_info']


                        class Received(object):
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
                                self.parent = None
                                self.acknowledgement_packets = None
                                self.call_disconnect_notify_packets = None
                                self.hello_packets = None
                                self.incoming_call_connected_packets = None
                                self.incoming_call_replies = None
                                self.incoming_call_requests = None
                                self.outgoing_call_connected_packets = None
                                self.outgoing_call_replies = None
                                self.outgoing_call_requests = None
                                self.service_relay_replies = None
                                self.service_relay_requests = None
                                self.set_link_info_packets = None
                                self.start_control_connection_notifications = None
                                self.start_control_connection_replies = None
                                self.start_control_connection_requests = None
                                self.stop_control_connection_notifications = None
                                self.unknown_packets = None
                                self.wan_error_notify_packets = None
                                self.zero_length_body_packets = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-tunnel-l2tun-oper:received'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.acknowledgement_packets is not None:
                                    return True

                                if self.call_disconnect_notify_packets is not None:
                                    return True

                                if self.hello_packets is not None:
                                    return True

                                if self.incoming_call_connected_packets is not None:
                                    return True

                                if self.incoming_call_replies is not None:
                                    return True

                                if self.incoming_call_requests is not None:
                                    return True

                                if self.outgoing_call_connected_packets is not None:
                                    return True

                                if self.outgoing_call_replies is not None:
                                    return True

                                if self.outgoing_call_requests is not None:
                                    return True

                                if self.service_relay_replies is not None:
                                    return True

                                if self.service_relay_requests is not None:
                                    return True

                                if self.set_link_info_packets is not None:
                                    return True

                                if self.start_control_connection_notifications is not None:
                                    return True

                                if self.start_control_connection_replies is not None:
                                    return True

                                if self.start_control_connection_requests is not None:
                                    return True

                                if self.stop_control_connection_notifications is not None:
                                    return True

                                if self.unknown_packets is not None:
                                    return True

                                if self.wan_error_notify_packets is not None:
                                    return True

                                if self.zero_length_body_packets is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                                return meta._meta_table['L2Tpv2.Counters.Control.Tunnels.Tunnel.Global_.Received']['meta_info']


                        class Drop(object):
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
                                self.parent = None
                                self.acknowledgement_packets = None
                                self.call_disconnect_notify_packets = None
                                self.hello_packets = None
                                self.incoming_call_connected_packets = None
                                self.incoming_call_replies = None
                                self.incoming_call_requests = None
                                self.outgoing_call_connected_packets = None
                                self.outgoing_call_replies = None
                                self.outgoing_call_requests = None
                                self.service_relay_replies = None
                                self.service_relay_requests = None
                                self.set_link_info_packets = None
                                self.start_control_connection_notifications = None
                                self.start_control_connection_replies = None
                                self.start_control_connection_requests = None
                                self.stop_control_connection_notifications = None
                                self.unknown_packets = None
                                self.wan_error_notify_packets = None
                                self.zero_length_body_packets = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-tunnel-l2tun-oper:drop'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.acknowledgement_packets is not None:
                                    return True

                                if self.call_disconnect_notify_packets is not None:
                                    return True

                                if self.hello_packets is not None:
                                    return True

                                if self.incoming_call_connected_packets is not None:
                                    return True

                                if self.incoming_call_replies is not None:
                                    return True

                                if self.incoming_call_requests is not None:
                                    return True

                                if self.outgoing_call_connected_packets is not None:
                                    return True

                                if self.outgoing_call_replies is not None:
                                    return True

                                if self.outgoing_call_requests is not None:
                                    return True

                                if self.service_relay_replies is not None:
                                    return True

                                if self.service_relay_requests is not None:
                                    return True

                                if self.set_link_info_packets is not None:
                                    return True

                                if self.start_control_connection_notifications is not None:
                                    return True

                                if self.start_control_connection_replies is not None:
                                    return True

                                if self.start_control_connection_requests is not None:
                                    return True

                                if self.stop_control_connection_notifications is not None:
                                    return True

                                if self.unknown_packets is not None:
                                    return True

                                if self.wan_error_notify_packets is not None:
                                    return True

                                if self.zero_length_body_packets is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                                return meta._meta_table['L2Tpv2.Counters.Control.Tunnels.Tunnel.Global_.Drop']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-tunnel-l2tun-oper:global'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.drop is not None and self.drop._has_data():
                                return True

                            if self.received is not None and self.received._has_data():
                                return True

                            if self.retransmit is not None and self.retransmit._has_data():
                                return True

                            if self.total_drop is not None:
                                return True

                            if self.total_received is not None:
                                return True

                            if self.total_retransmit is not None:
                                return True

                            if self.total_transmit is not None:
                                return True

                            if self.transmit is not None and self.transmit._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                            return meta._meta_table['L2Tpv2.Counters.Control.Tunnels.Tunnel.Global_']['meta_info']

                    @property
                    def _common_path(self):
                        if self.tunnel_id is None:
                            raise YPYModelError('Key property tunnel_id is None')

                        return '/Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/Cisco-IOS-XR-tunnel-l2tun-oper:counters/Cisco-IOS-XR-tunnel-l2tun-oper:control/Cisco-IOS-XR-tunnel-l2tun-oper:tunnels/Cisco-IOS-XR-tunnel-l2tun-oper:tunnel[Cisco-IOS-XR-tunnel-l2tun-oper:tunnel-id = ' + str(self.tunnel_id) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.tunnel_id is not None:
                            return True

                        if self.brief is not None and self.brief._has_data():
                            return True

                        if self.global_ is not None and self.global_._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                        return meta._meta_table['L2Tpv2.Counters.Control.Tunnels.Tunnel']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/Cisco-IOS-XR-tunnel-l2tun-oper:counters/Cisco-IOS-XR-tunnel-l2tun-oper:control/Cisco-IOS-XR-tunnel-l2tun-oper:tunnels'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.tunnel is not None:
                        for child_ref in self.tunnel:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                    return meta._meta_table['L2Tpv2.Counters.Control.Tunnels']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/Cisco-IOS-XR-tunnel-l2tun-oper:counters/Cisco-IOS-XR-tunnel-l2tun-oper:control'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.tunnel_xr is not None and self.tunnel_xr._has_data():
                    return True

                if self.tunnels is not None and self.tunnels._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                return meta._meta_table['L2Tpv2.Counters.Control']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/Cisco-IOS-XR-tunnel-l2tun-oper:counters'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.control is not None and self.control._has_data():
                return True

            if self.forwarding is not None and self.forwarding._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
            return meta._meta_table['L2Tpv2.Counters']['meta_info']


    class Statistics(object):
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
            self.parent = None
            self.average_packet_processing_time = None
            self.buffered_packets = None
            self.incoming_dropped_packets = None
            self.netio_packets = None
            self.received_out_of_order_packets = None
            self.received_packets = None
            self.reorder_deviation_packets = None
            self.reorder_packets = None
            self.sent_packets = None
            self.sessions = None
            self.tunnels = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/Cisco-IOS-XR-tunnel-l2tun-oper:statistics'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.average_packet_processing_time is not None:
                return True

            if self.buffered_packets is not None:
                return True

            if self.incoming_dropped_packets is not None:
                return True

            if self.netio_packets is not None:
                return True

            if self.received_out_of_order_packets is not None:
                return True

            if self.received_packets is not None:
                return True

            if self.reorder_deviation_packets is not None:
                return True

            if self.reorder_packets is not None:
                return True

            if self.sent_packets is not None:
                return True

            if self.sessions is not None:
                return True

            if self.tunnels is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
            return meta._meta_table['L2Tpv2.Statistics']['meta_info']


    class Tunnel(object):
        """
        L2TPv2 tunnel 
        
        .. attribute:: accounting
        
        	Tunnel accounting counters
        	**type**\:   :py:class:`Accounting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tpv2.Tunnel.Accounting>`
        
        

        """

        _prefix = 'tunnel-l2tun-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.accounting = L2Tpv2.Tunnel.Accounting()
            self.accounting.parent = self


        class Accounting(object):
            """
            Tunnel accounting counters
            
            .. attribute:: statistics
            
            	Tunnel accounting statistics
            	**type**\:   :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tpv2.Tunnel.Accounting.Statistics>`
            
            

            """

            _prefix = 'tunnel-l2tun-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.statistics = L2Tpv2.Tunnel.Accounting.Statistics()
                self.statistics.parent = self


            class Statistics(object):
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
                    self.parent = None
                    self.current_size = None
                    self.memory_failures = None
                    self.negative_acknowledgement = None
                    self.positive_acknowledgement = None
                    self.queue_statistics_size = None
                    self.records_checkpointed = None
                    self.records_fail_to_recover = None
                    self.records_failed_to_checkpoint = None
                    self.records_recovered_from_checkpoint = None
                    self.records_sent_from_queue = None
                    self.records_sent_successfully = None
                    self.reject = None
                    self.start = None
                    self.stop = None
                    self.transport_failures = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/Cisco-IOS-XR-tunnel-l2tun-oper:tunnel/Cisco-IOS-XR-tunnel-l2tun-oper:accounting/Cisco-IOS-XR-tunnel-l2tun-oper:statistics'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.current_size is not None:
                        return True

                    if self.memory_failures is not None:
                        return True

                    if self.negative_acknowledgement is not None:
                        return True

                    if self.positive_acknowledgement is not None:
                        return True

                    if self.queue_statistics_size is not None:
                        return True

                    if self.records_checkpointed is not None:
                        return True

                    if self.records_fail_to_recover is not None:
                        return True

                    if self.records_failed_to_checkpoint is not None:
                        return True

                    if self.records_recovered_from_checkpoint is not None:
                        return True

                    if self.records_sent_from_queue is not None:
                        return True

                    if self.records_sent_successfully is not None:
                        return True

                    if self.reject is not None:
                        return True

                    if self.start is not None:
                        return True

                    if self.stop is not None:
                        return True

                    if self.transport_failures is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                    return meta._meta_table['L2Tpv2.Tunnel.Accounting.Statistics']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/Cisco-IOS-XR-tunnel-l2tun-oper:tunnel/Cisco-IOS-XR-tunnel-l2tun-oper:accounting'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.statistics is not None and self.statistics._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                return meta._meta_table['L2Tpv2.Tunnel.Accounting']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/Cisco-IOS-XR-tunnel-l2tun-oper:tunnel'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.accounting is not None and self.accounting._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
            return meta._meta_table['L2Tpv2.Tunnel']['meta_info']


    class TunnelConfigurations(object):
        """
        List of tunnel IDs
        
        .. attribute:: tunnel_configuration
        
        	L2TP tunnel information
        	**type**\: list of    :py:class:`TunnelConfiguration <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tpv2.TunnelConfigurations.TunnelConfiguration>`
        
        

        """

        _prefix = 'tunnel-l2tun-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.tunnel_configuration = YList()
            self.tunnel_configuration.parent = self
            self.tunnel_configuration.name = 'tunnel_configuration'


        class TunnelConfiguration(object):
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
                self.parent = None
                self.local_tunnel_id = None
                self.l2tp_class = L2Tpv2.TunnelConfigurations.TunnelConfiguration.L2TpClass()
                self.l2tp_class.parent = self
                self.remote_tunnel_id = None


            class L2TpClass(object):
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
                	**type**\:   :py:class:`DigestHashEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.DigestHashEnum>`
                
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
                    self.parent = None
                    self.accounting_method_list = None
                    self.class_name_xr = None
                    self.digest_hash = None
                    self.encoded_password = None
                    self.hello_timeout = None
                    self.host_name = None
                    self.initial_retransmit_maximum_timeout = None
                    self.initial_retransmit_minimum_timeout = None
                    self.initial_retransmit_retries = None
                    self.ip_tos = None
                    self.is_authentication_enabled = None
                    self.is_congestion_control_enabled = None
                    self.is_digest_check_enabled = None
                    self.is_digest_enabled = None
                    self.is_hidden = None
                    self.is_peer_address_checked = None
                    self.password = None
                    self.receive_window_size = None
                    self.retransmit_maximum_timeout = None
                    self.retransmit_minimum_timeout = None
                    self.retransmit_retries = None
                    self.setup_timeout = None
                    self.timeout_no_user = None
                    self.vrf_name = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-tunnel-l2tun-oper:l2tp-class'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.accounting_method_list is not None:
                        return True

                    if self.class_name_xr is not None:
                        return True

                    if self.digest_hash is not None:
                        return True

                    if self.encoded_password is not None:
                        return True

                    if self.hello_timeout is not None:
                        return True

                    if self.host_name is not None:
                        return True

                    if self.initial_retransmit_maximum_timeout is not None:
                        return True

                    if self.initial_retransmit_minimum_timeout is not None:
                        return True

                    if self.initial_retransmit_retries is not None:
                        return True

                    if self.ip_tos is not None:
                        return True

                    if self.is_authentication_enabled is not None:
                        return True

                    if self.is_congestion_control_enabled is not None:
                        return True

                    if self.is_digest_check_enabled is not None:
                        return True

                    if self.is_digest_enabled is not None:
                        return True

                    if self.is_hidden is not None:
                        return True

                    if self.is_peer_address_checked is not None:
                        return True

                    if self.password is not None:
                        return True

                    if self.receive_window_size is not None:
                        return True

                    if self.retransmit_maximum_timeout is not None:
                        return True

                    if self.retransmit_minimum_timeout is not None:
                        return True

                    if self.retransmit_retries is not None:
                        return True

                    if self.setup_timeout is not None:
                        return True

                    if self.timeout_no_user is not None:
                        return True

                    if self.vrf_name is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                    return meta._meta_table['L2Tpv2.TunnelConfigurations.TunnelConfiguration.L2TpClass']['meta_info']

            @property
            def _common_path(self):
                if self.local_tunnel_id is None:
                    raise YPYModelError('Key property local_tunnel_id is None')

                return '/Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/Cisco-IOS-XR-tunnel-l2tun-oper:tunnel-configurations/Cisco-IOS-XR-tunnel-l2tun-oper:tunnel-configuration[Cisco-IOS-XR-tunnel-l2tun-oper:local-tunnel-id = ' + str(self.local_tunnel_id) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.local_tunnel_id is not None:
                    return True

                if self.l2tp_class is not None and self.l2tp_class._has_data():
                    return True

                if self.remote_tunnel_id is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                return meta._meta_table['L2Tpv2.TunnelConfigurations.TunnelConfiguration']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/Cisco-IOS-XR-tunnel-l2tun-oper:tunnel-configurations'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.tunnel_configuration is not None:
                for child_ref in self.tunnel_configuration:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
            return meta._meta_table['L2Tpv2.TunnelConfigurations']['meta_info']


    class CounterHistFail(object):
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
            self.parent = None
            self.pkt_timeout = YLeafList()
            self.pkt_timeout.parent = self
            self.pkt_timeout.name = 'pkt_timeout'
            self.rx_counters = None
            self.sess_down_tmout = None
            self.tx_counters = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/Cisco-IOS-XR-tunnel-l2tun-oper:counter-hist-fail'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.pkt_timeout is not None:
                for child in self.pkt_timeout:
                    if child is not None:
                        return True

            if self.rx_counters is not None:
                return True

            if self.sess_down_tmout is not None:
                return True

            if self.tx_counters is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
            return meta._meta_table['L2Tpv2.CounterHistFail']['meta_info']


    class Classes(object):
        """
        List of L2TP class names
        
        .. attribute:: class_
        
        	L2TP class name
        	**type**\: list of    :py:class:`Class_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tpv2.Classes.Class_>`
        
        

        """

        _prefix = 'tunnel-l2tun-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.class_ = YList()
            self.class_.parent = self
            self.class_.name = 'class_'


        class Class_(object):
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
            	**type**\:   :py:class:`DigestHashEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.DigestHashEnum>`
            
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
                self.parent = None
                self.class_name = None
                self.accounting_method_list = None
                self.class_name_xr = None
                self.digest_hash = None
                self.encoded_password = None
                self.hello_timeout = None
                self.host_name = None
                self.initial_retransmit_maximum_timeout = None
                self.initial_retransmit_minimum_timeout = None
                self.initial_retransmit_retries = None
                self.ip_tos = None
                self.is_authentication_enabled = None
                self.is_congestion_control_enabled = None
                self.is_digest_check_enabled = None
                self.is_digest_enabled = None
                self.is_hidden = None
                self.is_peer_address_checked = None
                self.password = None
                self.receive_window_size = None
                self.retransmit_maximum_timeout = None
                self.retransmit_minimum_timeout = None
                self.retransmit_retries = None
                self.setup_timeout = None
                self.timeout_no_user = None
                self.vrf_name = None

            @property
            def _common_path(self):
                if self.class_name is None:
                    raise YPYModelError('Key property class_name is None')

                return '/Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/Cisco-IOS-XR-tunnel-l2tun-oper:classes/Cisco-IOS-XR-tunnel-l2tun-oper:class[Cisco-IOS-XR-tunnel-l2tun-oper:class-name = ' + str(self.class_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.class_name is not None:
                    return True

                if self.accounting_method_list is not None:
                    return True

                if self.class_name_xr is not None:
                    return True

                if self.digest_hash is not None:
                    return True

                if self.encoded_password is not None:
                    return True

                if self.hello_timeout is not None:
                    return True

                if self.host_name is not None:
                    return True

                if self.initial_retransmit_maximum_timeout is not None:
                    return True

                if self.initial_retransmit_minimum_timeout is not None:
                    return True

                if self.initial_retransmit_retries is not None:
                    return True

                if self.ip_tos is not None:
                    return True

                if self.is_authentication_enabled is not None:
                    return True

                if self.is_congestion_control_enabled is not None:
                    return True

                if self.is_digest_check_enabled is not None:
                    return True

                if self.is_digest_enabled is not None:
                    return True

                if self.is_hidden is not None:
                    return True

                if self.is_peer_address_checked is not None:
                    return True

                if self.password is not None:
                    return True

                if self.receive_window_size is not None:
                    return True

                if self.retransmit_maximum_timeout is not None:
                    return True

                if self.retransmit_minimum_timeout is not None:
                    return True

                if self.retransmit_retries is not None:
                    return True

                if self.setup_timeout is not None:
                    return True

                if self.timeout_no_user is not None:
                    return True

                if self.vrf_name is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                return meta._meta_table['L2Tpv2.Classes.Class_']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/Cisco-IOS-XR-tunnel-l2tun-oper:classes'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.class_ is not None:
                for child_ref in self.class_:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
            return meta._meta_table['L2Tpv2.Classes']['meta_info']


    class Tunnels(object):
        """
        List of tunnel IDs
        
        .. attribute:: tunnel
        
        	L2TP tunnel  information
        	**type**\: list of    :py:class:`Tunnel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tpv2.Tunnels.Tunnel>`
        
        

        """

        _prefix = 'tunnel-l2tun-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.tunnel = YList()
            self.tunnel.parent = self
            self.tunnel.name = 'tunnel'


        class Tunnel(object):
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
                self.parent = None
                self.local_tunnel_id = None
                self.active_sessions = None
                self.class_name = None
                self.digest_secrets = None
                self.is_congestion_control_enabled = None
                self.is_pmtu_enabled = None
                self.is_tunnel_up = None
                self.local_address = None
                self.local_port = None
                self.local_tunnel_name = None
                self.local_window_size = None
                self.maximum_retransmission_time = None
                self.order_queue_size = None
                self.packet_queue_check = None
                self.protocol = None
                self.remote_address = None
                self.remote_port = None
                self.remote_tunnel_id = None
                self.remote_tunnel_name = None
                self.remote_window_size = None
                self.resend_maximum_queue_size = None
                self.resend_queue_size = None
                self.resends = None
                self.retransmission_time = None
                self.retransmit_time = YLeafList()
                self.retransmit_time.parent = self
                self.retransmit_time.name = 'retransmit_time'
                self.sequence_nr = None
                self.sequence_ns = None
                self.total_out_of_order_drop_packets = None
                self.total_out_of_order_reorder_packets = None
                self.total_peer_authentication_failures = None
                self.unsent_maximum_queue_size = None
                self.unsent_queue_size = None
                self.zero_length_body_acknowledgement_sent = None

            @property
            def _common_path(self):
                if self.local_tunnel_id is None:
                    raise YPYModelError('Key property local_tunnel_id is None')

                return '/Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/Cisco-IOS-XR-tunnel-l2tun-oper:tunnels/Cisco-IOS-XR-tunnel-l2tun-oper:tunnel[Cisco-IOS-XR-tunnel-l2tun-oper:local-tunnel-id = ' + str(self.local_tunnel_id) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.local_tunnel_id is not None:
                    return True

                if self.active_sessions is not None:
                    return True

                if self.class_name is not None:
                    return True

                if self.digest_secrets is not None:
                    return True

                if self.is_congestion_control_enabled is not None:
                    return True

                if self.is_pmtu_enabled is not None:
                    return True

                if self.is_tunnel_up is not None:
                    return True

                if self.local_address is not None:
                    return True

                if self.local_port is not None:
                    return True

                if self.local_tunnel_name is not None:
                    return True

                if self.local_window_size is not None:
                    return True

                if self.maximum_retransmission_time is not None:
                    return True

                if self.order_queue_size is not None:
                    return True

                if self.packet_queue_check is not None:
                    return True

                if self.protocol is not None:
                    return True

                if self.remote_address is not None:
                    return True

                if self.remote_port is not None:
                    return True

                if self.remote_tunnel_id is not None:
                    return True

                if self.remote_tunnel_name is not None:
                    return True

                if self.remote_window_size is not None:
                    return True

                if self.resend_maximum_queue_size is not None:
                    return True

                if self.resend_queue_size is not None:
                    return True

                if self.resends is not None:
                    return True

                if self.retransmission_time is not None:
                    return True

                if self.retransmit_time is not None:
                    for child in self.retransmit_time:
                        if child is not None:
                            return True

                if self.sequence_nr is not None:
                    return True

                if self.sequence_ns is not None:
                    return True

                if self.total_out_of_order_drop_packets is not None:
                    return True

                if self.total_out_of_order_reorder_packets is not None:
                    return True

                if self.total_peer_authentication_failures is not None:
                    return True

                if self.unsent_maximum_queue_size is not None:
                    return True

                if self.unsent_queue_size is not None:
                    return True

                if self.zero_length_body_acknowledgement_sent is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                return meta._meta_table['L2Tpv2.Tunnels.Tunnel']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/Cisco-IOS-XR-tunnel-l2tun-oper:tunnels'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.tunnel is not None:
                for child_ref in self.tunnel:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
            return meta._meta_table['L2Tpv2.Tunnels']['meta_info']


    class Sessions(object):
        """
        List of session IDs
        
        .. attribute:: session
        
        	L2TP information for a particular session
        	**type**\: list of    :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tpv2.Sessions.Session>`
        
        

        """

        _prefix = 'tunnel-l2tun-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.session = YList()
            self.session.parent = self
            self.session.name = 'session'


        class Session(object):
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
                self.parent = None
                self.local_tunnel_id = None
                self.local_session_id = None
                self.call_serial_number = None
                self.interface_name = None
                self.is_conditional_debug_enabled = None
                self.is_sequencing_on = None
                self.is_session_locally_initiated = None
                self.is_session_manual = None
                self.is_session_state_established = None
                self.is_session_up = None
                self.is_udp_checksum_enabled = None
                self.l2tp_sh_sess_tie_breaker = None
                self.l2tp_sh_sess_tie_breaker_enabled = None
                self.l2tp_sh_sess_udp_lport = None
                self.l2tp_sh_sess_udp_rport = None
                self.local_ip_address = None
                self.local_tunnel_name = None
                self.protocol = None
                self.remote_ip_address = None
                self.remote_session_id = None
                self.remote_tunnel_id = None
                self.remote_tunnel_name = None
                self.session_application_data = L2Tpv2.Sessions.Session.SessionApplicationData()
                self.session_application_data.parent = self
                self.unique_id = None


            class SessionApplicationData(object):
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
                    self.parent = None
                    self.l2tp_sh_sess_app_type = None
                    self.vpdn = L2Tpv2.Sessions.Session.SessionApplicationData.Vpdn()
                    self.vpdn.parent = self
                    self.xconnect = L2Tpv2.Sessions.Session.SessionApplicationData.Xconnect()
                    self.xconnect.parent = self


                class Xconnect(object):
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
                        self.parent = None
                        self.circuit_name = None
                        self.ipv6_protocol_tunneling = None
                        self.is_circuit_state_up = None
                        self.is_local_circuit_state_up = None
                        self.is_remote_circuit_state_up = None
                        self.sessionvc_id = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-tunnel-l2tun-oper:xconnect'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.circuit_name is not None:
                            return True

                        if self.ipv6_protocol_tunneling is not None:
                            return True

                        if self.is_circuit_state_up is not None:
                            return True

                        if self.is_local_circuit_state_up is not None:
                            return True

                        if self.is_remote_circuit_state_up is not None:
                            return True

                        if self.sessionvc_id is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                        return meta._meta_table['L2Tpv2.Sessions.Session.SessionApplicationData.Xconnect']['meta_info']


                class Vpdn(object):
                    """
                    VPDN data
                    
                    .. attribute:: interface_name
                    
                    	Interface name
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: username
                    
                    	Session username
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'tunnel-l2tun-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.interface_name = None
                        self.username = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-tunnel-l2tun-oper:vpdn'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.interface_name is not None:
                            return True

                        if self.username is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                        return meta._meta_table['L2Tpv2.Sessions.Session.SessionApplicationData.Vpdn']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-tunnel-l2tun-oper:session-application-data'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.l2tp_sh_sess_app_type is not None:
                        return True

                    if self.vpdn is not None and self.vpdn._has_data():
                        return True

                    if self.xconnect is not None and self.xconnect._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                    return meta._meta_table['L2Tpv2.Sessions.Session.SessionApplicationData']['meta_info']

            @property
            def _common_path(self):
                if self.local_tunnel_id is None:
                    raise YPYModelError('Key property local_tunnel_id is None')
                if self.local_session_id is None:
                    raise YPYModelError('Key property local_session_id is None')

                return '/Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/Cisco-IOS-XR-tunnel-l2tun-oper:sessions/Cisco-IOS-XR-tunnel-l2tun-oper:session[Cisco-IOS-XR-tunnel-l2tun-oper:local-tunnel-id = ' + str(self.local_tunnel_id) + '][Cisco-IOS-XR-tunnel-l2tun-oper:local-session-id = ' + str(self.local_session_id) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.local_tunnel_id is not None:
                    return True

                if self.local_session_id is not None:
                    return True

                if self.call_serial_number is not None:
                    return True

                if self.interface_name is not None:
                    return True

                if self.is_conditional_debug_enabled is not None:
                    return True

                if self.is_sequencing_on is not None:
                    return True

                if self.is_session_locally_initiated is not None:
                    return True

                if self.is_session_manual is not None:
                    return True

                if self.is_session_state_established is not None:
                    return True

                if self.is_session_up is not None:
                    return True

                if self.is_udp_checksum_enabled is not None:
                    return True

                if self.l2tp_sh_sess_tie_breaker is not None:
                    return True

                if self.l2tp_sh_sess_tie_breaker_enabled is not None:
                    return True

                if self.l2tp_sh_sess_udp_lport is not None:
                    return True

                if self.l2tp_sh_sess_udp_rport is not None:
                    return True

                if self.local_ip_address is not None:
                    return True

                if self.local_tunnel_name is not None:
                    return True

                if self.protocol is not None:
                    return True

                if self.remote_ip_address is not None:
                    return True

                if self.remote_session_id is not None:
                    return True

                if self.remote_tunnel_id is not None:
                    return True

                if self.remote_tunnel_name is not None:
                    return True

                if self.session_application_data is not None and self.session_application_data._has_data():
                    return True

                if self.unique_id is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                return meta._meta_table['L2Tpv2.Sessions.Session']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/Cisco-IOS-XR-tunnel-l2tun-oper:sessions'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.session is not None:
                for child_ref in self.session:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
            return meta._meta_table['L2Tpv2.Sessions']['meta_info']


    class Session(object):
        """
        L2TP control messages counters
        
        .. attribute:: unavailable
        
        	L2TP session unavailable  information
        	**type**\:   :py:class:`Unavailable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_oper.L2Tpv2.Session.Unavailable>`
        
        

        """

        _prefix = 'tunnel-l2tun-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.unavailable = L2Tpv2.Session.Unavailable()
            self.unavailable.parent = self


        class Unavailable(object):
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
                self.parent = None
                self.sessions_on_hold = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/Cisco-IOS-XR-tunnel-l2tun-oper:session/Cisco-IOS-XR-tunnel-l2tun-oper:unavailable'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.sessions_on_hold is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
                return meta._meta_table['L2Tpv2.Session.Unavailable']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2/Cisco-IOS-XR-tunnel-l2tun-oper:session'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.unavailable is not None and self.unavailable._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
            return meta._meta_table['L2Tpv2.Session']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-tunnel-l2tun-oper:l2tpv2'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.classes is not None and self.classes._has_data():
            return True

        if self.counter_hist_fail is not None and self.counter_hist_fail._has_data():
            return True

        if self.counters is not None and self.counters._has_data():
            return True

        if self.session is not None and self.session._has_data():
            return True

        if self.sessions is not None and self.sessions._has_data():
            return True

        if self.statistics is not None and self.statistics._has_data():
            return True

        if self.tunnel is not None and self.tunnel._has_data():
            return True

        if self.tunnel_configurations is not None and self.tunnel_configurations._has_data():
            return True

        if self.tunnels is not None and self.tunnels._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_oper as meta
        return meta._meta_table['L2Tpv2']['meta_info']


