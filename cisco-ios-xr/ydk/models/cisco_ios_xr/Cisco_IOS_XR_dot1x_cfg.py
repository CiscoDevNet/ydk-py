""" Cisco_IOS_XR_dot1x_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR dot1x package configuration.

This module contains definitions
for the following management objects\:
  dot1x\: Global Dot1x Configuration
  eap\: eap

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Dot1X(Entity):
    """
    Global Dot1x Configuration
    
    .. attribute:: dot1x_profile
    
    	Global Dot1x Profile Name
    	**type**\: list of  		 :py:class:`Dot1XProfile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_cfg.Dot1X.Dot1XProfile>`
    
    

    """

    _prefix = 'dot1x-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(Dot1X, self).__init__()
        self._top_entity = None

        self.yang_name = "dot1x"
        self.yang_parent_name = "Cisco-IOS-XR-dot1x-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([("dot1x-profile", ("dot1x_profile", Dot1X.Dot1XProfile))])
        self._leafs = OrderedDict()

        self.dot1x_profile = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-dot1x-cfg:dot1x"

    def __setattr__(self, name, value):
        self._perform_setattr(Dot1X, [], name, value)


    class Dot1XProfile(Entity):
        """
        Global Dot1x Profile Name
        
        .. attribute:: profile_name  (key)
        
        	Name of the Dot1x Profile
        	**type**\: str
        
        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
        
        .. attribute:: supplicant
        
        	Dot1x Supplicant Related Configuration
        	**type**\:  :py:class:`Supplicant <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_cfg.Dot1X.Dot1XProfile.Supplicant>`
        
        .. attribute:: authenticator
        
        	Dot1x Authenticator Related Configuration
        	**type**\:  :py:class:`Authenticator <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_cfg.Dot1X.Dot1XProfile.Authenticator>`
        
        .. attribute:: pae
        
        	Dot1x PAE (Port Access Entity) Role
        	**type**\: str
        
        	**pattern:** (supplicant)\|(authenticator)\|(both)
        
        

        """

        _prefix = 'dot1x-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Dot1X.Dot1XProfile, self).__init__()

            self.yang_name = "dot1x-profile"
            self.yang_parent_name = "dot1x"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['profile_name']
            self._child_container_classes = OrderedDict([("supplicant", ("supplicant", Dot1X.Dot1XProfile.Supplicant)), ("authenticator", ("authenticator", Dot1X.Dot1XProfile.Authenticator))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('profile_name', YLeaf(YType.str, 'profile-name')),
                ('pae', YLeaf(YType.str, 'pae')),
            ])
            self.profile_name = None
            self.pae = None

            self.supplicant = Dot1X.Dot1XProfile.Supplicant()
            self.supplicant.parent = self
            self._children_name_map["supplicant"] = "supplicant"
            self._children_yang_names.add("supplicant")

            self.authenticator = Dot1X.Dot1XProfile.Authenticator()
            self.authenticator.parent = self
            self._children_name_map["authenticator"] = "authenticator"
            self._children_yang_names.add("authenticator")
            self._segment_path = lambda: "dot1x-profile" + "[profile-name='" + str(self.profile_name) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-dot1x-cfg:dot1x/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Dot1X.Dot1XProfile, ['profile_name', 'pae'], name, value)


        class Supplicant(Entity):
            """
            Dot1x Supplicant Related Configuration
            
            .. attribute:: eap_profile
            
            	EAP Profile for Supplicant
            	**type**\: str
            
            

            """

            _prefix = 'dot1x-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Dot1X.Dot1XProfile.Supplicant, self).__init__()

                self.yang_name = "supplicant"
                self.yang_parent_name = "dot1x-profile"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('eap_profile', YLeaf(YType.str, 'eap-profile')),
                ])
                self.eap_profile = None
                self._segment_path = lambda: "supplicant"

            def __setattr__(self, name, value):
                self._perform_setattr(Dot1X.Dot1XProfile.Supplicant, ['eap_profile'], name, value)


        class Authenticator(Entity):
            """
            Dot1x Authenticator Related Configuration
            
            .. attribute:: timers
            
            	Timers for Authenticator
            	**type**\:  :py:class:`Timers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_cfg.Dot1X.Dot1XProfile.Authenticator.Timers>`
            
            

            """

            _prefix = 'dot1x-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Dot1X.Dot1XProfile.Authenticator, self).__init__()

                self.yang_name = "authenticator"
                self.yang_parent_name = "dot1x-profile"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([("timers", ("timers", Dot1X.Dot1XProfile.Authenticator.Timers))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict()

                self.timers = Dot1X.Dot1XProfile.Authenticator.Timers()
                self.timers.parent = self
                self._children_name_map["timers"] = "timers"
                self._children_yang_names.add("timers")
                self._segment_path = lambda: "authenticator"


            class Timers(Entity):
                """
                Timers for Authenticator
                
                .. attribute:: reauth_time
                
                	After this time ReAuthentication will be trigerred
                	**type**\:  :py:class:`ReauthTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_cfg.Dot1X.Dot1XProfile.Authenticator.Timers.ReauthTime>`
                
                

                """

                _prefix = 'dot1x-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Dot1X.Dot1XProfile.Authenticator.Timers, self).__init__()

                    self.yang_name = "timers"
                    self.yang_parent_name = "authenticator"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("reauth-time", ("reauth_time", Dot1X.Dot1XProfile.Authenticator.Timers.ReauthTime))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict()

                    self.reauth_time = Dot1X.Dot1XProfile.Authenticator.Timers.ReauthTime()
                    self.reauth_time.parent = self
                    self._children_name_map["reauth_time"] = "reauth-time"
                    self._children_yang_names.add("reauth-time")
                    self._segment_path = lambda: "timers"


                class ReauthTime(Entity):
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
                        super(Dot1X.Dot1XProfile.Authenticator.Timers.ReauthTime, self).__init__()

                        self.yang_name = "reauth-time"
                        self.yang_parent_name = "timers"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('server', YLeaf(YType.boolean, 'server')),
                            ('local', YLeaf(YType.uint32, 'local')),
                        ])
                        self.server = None
                        self.local = None
                        self._segment_path = lambda: "reauth-time"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dot1X.Dot1XProfile.Authenticator.Timers.ReauthTime, ['server', 'local'], name, value)

    def clone_ptr(self):
        self._top_entity = Dot1X()
        return self._top_entity

class Eap(Entity):
    """
    eap
    
    .. attribute:: eap_profile
    
    	Global EAP Profile Configuration
    	**type**\: list of  		 :py:class:`EapProfile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_cfg.Eap.EapProfile>`
    
    

    """

    _prefix = 'dot1x-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(Eap, self).__init__()
        self._top_entity = None

        self.yang_name = "eap"
        self.yang_parent_name = "Cisco-IOS-XR-dot1x-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([("eap-profile", ("eap_profile", Eap.EapProfile))])
        self._leafs = OrderedDict()

        self.eap_profile = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-dot1x-cfg:eap"

    def __setattr__(self, name, value):
        self._perform_setattr(Eap, [], name, value)


    class EapProfile(Entity):
        """
        Global EAP Profile Configuration
        
        .. attribute:: profile_name  (key)
        
        	Name of the EAP Profile
        	**type**\: str
        
        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
        
        .. attribute:: eaptls
        
        	EAP TLS Configuration
        	**type**\:  :py:class:`Eaptls <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_cfg.Eap.EapProfile.Eaptls>`
        
        .. attribute:: identity
        
        	Configure EAP Identity/UserName
        	**type**\: str
        
        

        """

        _prefix = 'dot1x-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Eap.EapProfile, self).__init__()

            self.yang_name = "eap-profile"
            self.yang_parent_name = "eap"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['profile_name']
            self._child_container_classes = OrderedDict([("eaptls", ("eaptls", Eap.EapProfile.Eaptls))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('profile_name', YLeaf(YType.str, 'profile-name')),
                ('identity', YLeaf(YType.str, 'identity')),
            ])
            self.profile_name = None
            self.identity = None

            self.eaptls = Eap.EapProfile.Eaptls()
            self.eaptls.parent = self
            self._children_name_map["eaptls"] = "eaptls"
            self._children_yang_names.add("eaptls")
            self._segment_path = lambda: "eap-profile" + "[profile-name='" + str(self.profile_name) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-dot1x-cfg:eap/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Eap.EapProfile, ['profile_name', 'identity'], name, value)


        class Eaptls(Entity):
            """
            EAP TLS Configuration
            
            .. attribute:: pki_trustpoint
            
            	Configure PKI Trustpoint
            	**type**\: str
            
            

            """

            _prefix = 'dot1x-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Eap.EapProfile.Eaptls, self).__init__()

                self.yang_name = "eaptls"
                self.yang_parent_name = "eap-profile"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('pki_trustpoint', YLeaf(YType.str, 'pki-trustpoint')),
                ])
                self.pki_trustpoint = None
                self._segment_path = lambda: "eaptls"

            def __setattr__(self, name, value):
                self._perform_setattr(Eap.EapProfile.Eaptls, ['pki_trustpoint'], name, value)

    def clone_ptr(self):
        self._top_entity = Eap()
        return self._top_entity

