""" Cisco_IOS_XR_dot1x_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR dot1x package configuration.

This module contains definitions
for the following management objects\:
  dot1x\: Global Dot1x Configuration
  eap\: eap

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



class Dot1xServerDeadAction(Enum):
    """
    Dot1xServerDeadAction (Enum Class)

    Dot1x server dead action

    .. data:: auth_fail = 0

    	server dead action auth-fail

    .. data:: auth_retry = 1

    	server dead action auth-retry

    """

    auth_fail = Enum.YLeaf(0, "auth-fail")

    auth_retry = Enum.YLeaf(1, "auth-retry")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dot1x_cfg as meta
        return meta._meta_table['Dot1xServerDeadAction']



class Dot1x(_Entity_):
    """
    Global Dot1x Configuration
    
    .. attribute:: dot1x_profile
    
    	Global Dot1x Profile Name
    	**type**\: list of  		 :py:class:`Dot1xProfile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_cfg.Dot1x.Dot1xProfile>`
    
    

    """

    _prefix = 'dot1x-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(Dot1x, self).__init__()
        self._top_entity = None

        self.yang_name = "dot1x"
        self.yang_parent_name = "Cisco-IOS-XR-dot1x-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("dot1x-profile", ("dot1x_profile", Dot1x.Dot1xProfile))])
        self._leafs = OrderedDict()

        self.dot1x_profile = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-dot1x-cfg:dot1x"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Dot1x, [], name, value)


    class Dot1xProfile(_Entity_):
        """
        Global Dot1x Profile Name
        
        .. attribute:: profile_name  (key)
        
        	Name of the Dot1x Profile
        	**type**\: str
        
        	**length:** 1..63
        
        .. attribute:: supplicant
        
        	Dot1x Supplicant Related Configuration
        	**type**\:  :py:class:`Supplicant <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_cfg.Dot1x.Dot1xProfile.Supplicant>`
        
        .. attribute:: authenticator
        
        	Dot1x Authenticator Related Configuration
        	**type**\:  :py:class:`Authenticator <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_cfg.Dot1x.Dot1xProfile.Authenticator>`
        
        .. attribute:: pae
        
        	Dot1x PAE (Port Access Entity) Role
        	**type**\: str
        
        	**pattern:** (supplicant)\|(authenticator)\|(both)
        
        

        """

        _prefix = 'dot1x-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Dot1x.Dot1xProfile, self).__init__()

            self.yang_name = "dot1x-profile"
            self.yang_parent_name = "dot1x"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['profile_name']
            self._child_classes = OrderedDict([("supplicant", ("supplicant", Dot1x.Dot1xProfile.Supplicant)), ("authenticator", ("authenticator", Dot1x.Dot1xProfile.Authenticator))])
            self._leafs = OrderedDict([
                ('profile_name', (YLeaf(YType.str, 'profile-name'), ['str'])),
                ('pae', (YLeaf(YType.str, 'pae'), ['str'])),
            ])
            self.profile_name = None
            self.pae = None

            self.supplicant = Dot1x.Dot1xProfile.Supplicant()
            self.supplicant.parent = self
            self._children_name_map["supplicant"] = "supplicant"

            self.authenticator = Dot1x.Dot1xProfile.Authenticator()
            self.authenticator.parent = self
            self._children_name_map["authenticator"] = "authenticator"
            self._segment_path = lambda: "dot1x-profile" + "[profile-name='" + str(self.profile_name) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-dot1x-cfg:dot1x/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Dot1x.Dot1xProfile, ['profile_name', 'pae'], name, value)


        class Supplicant(_Entity_):
            """
            Dot1x Supplicant Related Configuration
            
            .. attribute:: eap_profile
            
            	EAP Profile for Supplicant
            	**type**\: str
            
            	**length:** 1..63
            
            

            """

            _prefix = 'dot1x-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Dot1x.Dot1xProfile.Supplicant, self).__init__()

                self.yang_name = "supplicant"
                self.yang_parent_name = "dot1x-profile"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('eap_profile', (YLeaf(YType.str, 'eap-profile'), ['str'])),
                ])
                self.eap_profile = None
                self._segment_path = lambda: "supplicant"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Dot1x.Dot1xProfile.Supplicant, ['eap_profile'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dot1x_cfg as meta
                return meta._meta_table['Dot1x.Dot1xProfile.Supplicant']['meta_info']


        class Authenticator(_Entity_):
            """
            Dot1x Authenticator Related Configuration
            
            .. attribute:: timers
            
            	Timers for Authenticator
            	**type**\:  :py:class:`Timers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_cfg.Dot1x.Dot1xProfile.Authenticator.Timers>`
            
            .. attribute:: eap_profile
            
            	EAP Profile for Local EAP Server
            	**type**\: str
            
            	**length:** 1..63
            
            .. attribute:: server_dead
            
            	dot1x authenticator action on AAA server unreachability
            	**type**\:  :py:class:`Dot1xServerDeadAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_cfg.Dot1xServerDeadAction>`
            
            

            """

            _prefix = 'dot1x-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Dot1x.Dot1xProfile.Authenticator, self).__init__()

                self.yang_name = "authenticator"
                self.yang_parent_name = "dot1x-profile"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("timers", ("timers", Dot1x.Dot1xProfile.Authenticator.Timers))])
                self._leafs = OrderedDict([
                    ('eap_profile', (YLeaf(YType.str, 'eap-profile'), ['str'])),
                    ('server_dead', (YLeaf(YType.enumeration, 'server-dead'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_cfg', 'Dot1xServerDeadAction', '')])),
                ])
                self.eap_profile = None
                self.server_dead = None

                self.timers = Dot1x.Dot1xProfile.Authenticator.Timers()
                self.timers.parent = self
                self._children_name_map["timers"] = "timers"
                self._segment_path = lambda: "authenticator"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Dot1x.Dot1xProfile.Authenticator, ['eap_profile', 'server_dead'], name, value)


            class Timers(_Entity_):
                """
                Timers for Authenticator
                
                .. attribute:: reauth_time
                
                	After this time ReAuthentication will be trigerred
                	**type**\:  :py:class:`ReauthTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_cfg.Dot1x.Dot1xProfile.Authenticator.Timers.ReauthTime>`
                
                

                """

                _prefix = 'dot1x-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Dot1x.Dot1xProfile.Authenticator.Timers, self).__init__()

                    self.yang_name = "timers"
                    self.yang_parent_name = "authenticator"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("reauth-time", ("reauth_time", Dot1x.Dot1xProfile.Authenticator.Timers.ReauthTime))])
                    self._leafs = OrderedDict()

                    self.reauth_time = Dot1x.Dot1xProfile.Authenticator.Timers.ReauthTime()
                    self.reauth_time.parent = self
                    self._children_name_map["reauth_time"] = "reauth-time"
                    self._segment_path = lambda: "timers"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Dot1x.Dot1xProfile.Authenticator.Timers, [], name, value)


                class ReauthTime(_Entity_):
                    """
                    After this time ReAuthentication will be
                    trigerred
                    
                    .. attribute:: server
                    
                    	Reauth will be triggerred based on the EAP server configuration
                    	**type**\: bool
                    
                    .. attribute:: local
                    
                    	Reauth will be triggerred based on the configuration in box
                    	**type**\: int
                    
                    	**range:** 60..5184000
                    
                    	**units**\: second
                    
                    

                    """

                    _prefix = 'dot1x-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Dot1x.Dot1xProfile.Authenticator.Timers.ReauthTime, self).__init__()

                        self.yang_name = "reauth-time"
                        self.yang_parent_name = "timers"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('server', (YLeaf(YType.boolean, 'server'), ['bool'])),
                            ('local', (YLeaf(YType.uint32, 'local'), ['int'])),
                        ])
                        self.server = None
                        self.local = None
                        self._segment_path = lambda: "reauth-time"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dot1x.Dot1xProfile.Authenticator.Timers.ReauthTime, ['server', 'local'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dot1x_cfg as meta
                        return meta._meta_table['Dot1x.Dot1xProfile.Authenticator.Timers.ReauthTime']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dot1x_cfg as meta
                    return meta._meta_table['Dot1x.Dot1xProfile.Authenticator.Timers']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dot1x_cfg as meta
                return meta._meta_table['Dot1x.Dot1xProfile.Authenticator']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dot1x_cfg as meta
            return meta._meta_table['Dot1x.Dot1xProfile']['meta_info']

    def clone_ptr(self):
        self._top_entity = Dot1x()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dot1x_cfg as meta
        return meta._meta_table['Dot1x']['meta_info']


class Eap(_Entity_):
    """
    eap
    
    .. attribute:: eap_profile
    
    	Global EAP Profile Configuration
    	**type**\: list of  		 :py:class:`EapProfile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_cfg.Eap.EapProfile>`
    
    

    """

    _prefix = 'dot1x-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(Eap, self).__init__()
        self._top_entity = None

        self.yang_name = "eap"
        self.yang_parent_name = "Cisco-IOS-XR-dot1x-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("eap-profile", ("eap_profile", Eap.EapProfile))])
        self._leafs = OrderedDict()

        self.eap_profile = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-dot1x-cfg:eap"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Eap, [], name, value)


    class EapProfile(_Entity_):
        """
        Global EAP Profile Configuration
        
        .. attribute:: profile_name  (key)
        
        	Name of the EAP Profile
        	**type**\: str
        
        	**length:** 1..63
        
        .. attribute:: eaptls
        
        	EAP TLS Configuration
        	**type**\:  :py:class:`Eaptls <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_cfg.Eap.EapProfile.Eaptls>`
        
        .. attribute:: allow_eap_tls1_0
        
        	Configure backward compatibility for TLS 1.0
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: identity
        
        	Configure EAP Identity/UserName
        	**type**\: str
        
        	**length:** 1..63
        
        

        """

        _prefix = 'dot1x-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Eap.EapProfile, self).__init__()

            self.yang_name = "eap-profile"
            self.yang_parent_name = "eap"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['profile_name']
            self._child_classes = OrderedDict([("eaptls", ("eaptls", Eap.EapProfile.Eaptls))])
            self._leafs = OrderedDict([
                ('profile_name', (YLeaf(YType.str, 'profile-name'), ['str'])),
                ('allow_eap_tls1_0', (YLeaf(YType.empty, 'allow-eap-tls1-0'), ['Empty'])),
                ('identity', (YLeaf(YType.str, 'identity'), ['str'])),
            ])
            self.profile_name = None
            self.allow_eap_tls1_0 = None
            self.identity = None

            self.eaptls = Eap.EapProfile.Eaptls()
            self.eaptls.parent = self
            self._children_name_map["eaptls"] = "eaptls"
            self._segment_path = lambda: "eap-profile" + "[profile-name='" + str(self.profile_name) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-dot1x-cfg:eap/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Eap.EapProfile, ['profile_name', 'allow_eap_tls1_0', 'identity'], name, value)


        class Eaptls(_Entity_):
            """
            EAP TLS Configuration
            
            .. attribute:: pki_trustpoint
            
            	Configure PKI Trustpoint
            	**type**\: str
            
            	**length:** 1..63
            
            

            """

            _prefix = 'dot1x-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Eap.EapProfile.Eaptls, self).__init__()

                self.yang_name = "eaptls"
                self.yang_parent_name = "eap-profile"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('pki_trustpoint', (YLeaf(YType.str, 'pki-trustpoint'), ['str'])),
                ])
                self.pki_trustpoint = None
                self._segment_path = lambda: "eaptls"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Eap.EapProfile.Eaptls, ['pki_trustpoint'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dot1x_cfg as meta
                return meta._meta_table['Eap.EapProfile.Eaptls']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dot1x_cfg as meta
            return meta._meta_table['Eap.EapProfile']['meta_info']

    def clone_ptr(self):
        self._top_entity = Eap()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_dot1x_cfg as meta
        return meta._meta_table['Eap']['meta_info']


