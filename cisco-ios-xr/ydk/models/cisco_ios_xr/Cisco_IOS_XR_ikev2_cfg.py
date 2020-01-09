""" Cisco_IOS_XR_ikev2_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ikev2 package configuration.

This module contains definitions
for the following management objects\:
  ikev2\: Internet key exchange(IKEv2) config commands

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




class Ikev2(_Entity_):
    """
    Internet key exchange(IKEv2) config commands
    
    .. attribute:: keyring_names
    
    	IKEv2 keyring config commands
    	**type**\:  :py:class:`KeyringNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_cfg.Ikev2.KeyringNames>`
    
    .. attribute:: profile_names
    
    	IKEv2 profile config commands
    	**type**\:  :py:class:`ProfileNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_cfg.Ikev2.ProfileNames>`
    
    .. attribute:: policy_names
    
    	Configure IKEv2 policies
    	**type**\:  :py:class:`PolicyNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_cfg.Ikev2.PolicyNames>`
    
    .. attribute:: proposal_names
    
    	Configure IKEv2 proposals
    	**type**\:  :py:class:`ProposalNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_cfg.Ikev2.ProposalNames>`
    
    

    """

    _prefix = 'ikev2-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(Ikev2, self).__init__()
        self._top_entity = None

        self.yang_name = "ikev2"
        self.yang_parent_name = "Cisco-IOS-XR-ikev2-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("keyring-names", ("keyring_names", Ikev2.KeyringNames)), ("profile-names", ("profile_names", Ikev2.ProfileNames)), ("policy-names", ("policy_names", Ikev2.PolicyNames)), ("proposal-names", ("proposal_names", Ikev2.ProposalNames))])
        self._leafs = OrderedDict()

        self.keyring_names = Ikev2.KeyringNames()
        self.keyring_names.parent = self
        self._children_name_map["keyring_names"] = "keyring-names"

        self.profile_names = Ikev2.ProfileNames()
        self.profile_names.parent = self
        self._children_name_map["profile_names"] = "profile-names"

        self.policy_names = Ikev2.PolicyNames()
        self.policy_names.parent = self
        self._children_name_map["policy_names"] = "policy-names"

        self.proposal_names = Ikev2.ProposalNames()
        self.proposal_names.parent = self
        self._children_name_map["proposal_names"] = "proposal-names"
        self._segment_path = lambda: "Cisco-IOS-XR-ikev2-cfg:ikev2"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Ikev2, [], name, value)


    class KeyringNames(_Entity_):
        """
        IKEv2 keyring config commands
        
        .. attribute:: keyring_name
        
        	IKEv2 keyring name
        	**type**\: list of  		 :py:class:`KeyringName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_cfg.Ikev2.KeyringNames.KeyringName>`
        
        

        """

        _prefix = 'ikev2-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Ikev2.KeyringNames, self).__init__()

            self.yang_name = "keyring-names"
            self.yang_parent_name = "ikev2"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("keyring-name", ("keyring_name", Ikev2.KeyringNames.KeyringName))])
            self._leafs = OrderedDict()

            self.keyring_name = YList(self)
            self._segment_path = lambda: "keyring-names"
            self._absolute_path = lambda: "Cisco-IOS-XR-ikev2-cfg:ikev2/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ikev2.KeyringNames, [], name, value)


        class KeyringName(_Entity_):
            """
            IKEv2 keyring name
            
            .. attribute:: name  (key)
            
            	Name of the keyring
            	**type**\: str
            
            	**length:** 1..32
            
            .. attribute:: peer_names
            
            	IKEv2 keyring peer config commands
            	**type**\:  :py:class:`PeerNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_cfg.Ikev2.KeyringNames.KeyringName.PeerNames>`
            
            .. attribute:: keyring_sub
            
            	This indicated existence of keyring
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'ikev2-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Ikev2.KeyringNames.KeyringName, self).__init__()

                self.yang_name = "keyring-name"
                self.yang_parent_name = "keyring-names"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['name']
                self._child_classes = OrderedDict([("peer-names", ("peer_names", Ikev2.KeyringNames.KeyringName.PeerNames))])
                self._leafs = OrderedDict([
                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                    ('keyring_sub', (YLeaf(YType.empty, 'keyring-sub'), ['Empty'])),
                ])
                self.name = None
                self.keyring_sub = None

                self.peer_names = Ikev2.KeyringNames.KeyringName.PeerNames()
                self.peer_names.parent = self
                self._children_name_map["peer_names"] = "peer-names"
                self._segment_path = lambda: "keyring-name" + "[name='" + str(self.name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ikev2-cfg:ikev2/keyring-names/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ikev2.KeyringNames.KeyringName, ['name', 'keyring_sub'], name, value)


            class PeerNames(_Entity_):
                """
                IKEv2 keyring peer config commands
                
                .. attribute:: peer_name
                
                	IKEv2 keyring peer name
                	**type**\: list of  		 :py:class:`PeerName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_cfg.Ikev2.KeyringNames.KeyringName.PeerNames.PeerName>`
                
                

                """

                _prefix = 'ikev2-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Ikev2.KeyringNames.KeyringName.PeerNames, self).__init__()

                    self.yang_name = "peer-names"
                    self.yang_parent_name = "keyring-name"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("peer-name", ("peer_name", Ikev2.KeyringNames.KeyringName.PeerNames.PeerName))])
                    self._leafs = OrderedDict()

                    self.peer_name = YList(self)
                    self._segment_path = lambda: "peer-names"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ikev2.KeyringNames.KeyringName.PeerNames, [], name, value)


                class PeerName(_Entity_):
                    """
                    IKEv2 keyring peer name
                    
                    .. attribute:: name  (key)
                    
                    	Name of the keyring\-peer
                    	**type**\: str
                    
                    	**length:** 1..32
                    
                    .. attribute:: address
                    
                    	IP Address to identify the peer
                    	**type**\:  :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_cfg.Ikev2.KeyringNames.KeyringName.PeerNames.PeerName.Address>`
                    
                    .. attribute:: psk
                    
                    	Pre\-shared key for peer
                    	**type**\:  :py:class:`Psk <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_cfg.Ikev2.KeyringNames.KeyringName.PeerNames.PeerName.Psk>`
                    
                    .. attribute:: peer_sub
                    
                    	This indicates existence of keyring\-peer
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'ikev2-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Ikev2.KeyringNames.KeyringName.PeerNames.PeerName, self).__init__()

                        self.yang_name = "peer-name"
                        self.yang_parent_name = "peer-names"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['name']
                        self._child_classes = OrderedDict([("address", ("address", Ikev2.KeyringNames.KeyringName.PeerNames.PeerName.Address)), ("psk", ("psk", Ikev2.KeyringNames.KeyringName.PeerNames.PeerName.Psk))])
                        self._leafs = OrderedDict([
                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                            ('peer_sub', (YLeaf(YType.empty, 'peer-sub'), ['Empty'])),
                        ])
                        self.name = None
                        self.peer_sub = None

                        self.address = Ikev2.KeyringNames.KeyringName.PeerNames.PeerName.Address()
                        self.address.parent = self
                        self._children_name_map["address"] = "address"

                        self.psk = Ikev2.KeyringNames.KeyringName.PeerNames.PeerName.Psk()
                        self.psk.parent = self
                        self._children_name_map["psk"] = "psk"
                        self._segment_path = lambda: "peer-name" + "[name='" + str(self.name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ikev2.KeyringNames.KeyringName.PeerNames.PeerName, ['name', 'peer_sub'], name, value)


                    class Address(_Entity_):
                        """
                        IP Address to identify the peer
                        
                        .. attribute:: ip
                        
                        	IP Address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: subnet
                        
                        	Subnet
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ikev2-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Ikev2.KeyringNames.KeyringName.PeerNames.PeerName.Address, self).__init__()

                            self.yang_name = "address"
                            self.yang_parent_name = "peer-name"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('ip', (YLeaf(YType.str, 'ip'), ['str'])),
                                ('subnet', (YLeaf(YType.str, 'subnet'), ['str'])),
                            ])
                            self.ip = None
                            self.subnet = None
                            self._segment_path = lambda: "address"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ikev2.KeyringNames.KeyringName.PeerNames.PeerName.Address, ['ip', 'subnet'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ikev2_cfg as meta
                            return meta._meta_table['Ikev2.KeyringNames.KeyringName.PeerNames.PeerName.Address']['meta_info']


                    class Psk(_Entity_):
                        """
                        Pre\-shared key for peer
                        
                        .. attribute:: local_remote_key
                        
                        	Local/Remote pre\-shared key for the peer
                        	**type**\:  :py:class:`LocalRemoteKey <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_cfg.Ikev2.KeyringNames.KeyringName.PeerNames.PeerName.Psk.LocalRemoteKey>`
                        
                        .. attribute:: both_key
                        
                        	Both pre\-shared key for the peer
                        	**type**\: str
                        
                        	**pattern:** (!.+)\|([^!].+)
                        
                        

                        """

                        _prefix = 'ikev2-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Ikev2.KeyringNames.KeyringName.PeerNames.PeerName.Psk, self).__init__()

                            self.yang_name = "psk"
                            self.yang_parent_name = "peer-name"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("local-remote-key", ("local_remote_key", Ikev2.KeyringNames.KeyringName.PeerNames.PeerName.Psk.LocalRemoteKey))])
                            self._leafs = OrderedDict([
                                ('both_key', (YLeaf(YType.str, 'both-key'), ['str'])),
                            ])
                            self.both_key = None

                            self.local_remote_key = Ikev2.KeyringNames.KeyringName.PeerNames.PeerName.Psk.LocalRemoteKey()
                            self.local_remote_key.parent = self
                            self._children_name_map["local_remote_key"] = "local-remote-key"
                            self._segment_path = lambda: "psk"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ikev2.KeyringNames.KeyringName.PeerNames.PeerName.Psk, ['both_key'], name, value)


                        class LocalRemoteKey(_Entity_):
                            """
                            Local/Remote pre\-shared key for the peer
                            
                            .. attribute:: string_xr
                            
                            	Local pre\-shared key
                            	**type**\: str
                            
                            	**pattern:** (!.+)\|([^!].+)
                            
                            .. attribute:: string
                            
                            	Remote pre\-shared key
                            	**type**\: str
                            
                            	**pattern:** (!.+)\|([^!].+)
                            
                            

                            """

                            _prefix = 'ikev2-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Ikev2.KeyringNames.KeyringName.PeerNames.PeerName.Psk.LocalRemoteKey, self).__init__()

                                self.yang_name = "local-remote-key"
                                self.yang_parent_name = "psk"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('string_xr', (YLeaf(YType.str, 'string-xr'), ['str'])),
                                    ('string', (YLeaf(YType.str, 'string'), ['str'])),
                                ])
                                self.string_xr = None
                                self.string = None
                                self._segment_path = lambda: "local-remote-key"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ikev2.KeyringNames.KeyringName.PeerNames.PeerName.Psk.LocalRemoteKey, ['string_xr', 'string'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ikev2_cfg as meta
                                return meta._meta_table['Ikev2.KeyringNames.KeyringName.PeerNames.PeerName.Psk.LocalRemoteKey']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ikev2_cfg as meta
                            return meta._meta_table['Ikev2.KeyringNames.KeyringName.PeerNames.PeerName.Psk']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ikev2_cfg as meta
                        return meta._meta_table['Ikev2.KeyringNames.KeyringName.PeerNames.PeerName']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ikev2_cfg as meta
                    return meta._meta_table['Ikev2.KeyringNames.KeyringName.PeerNames']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ikev2_cfg as meta
                return meta._meta_table['Ikev2.KeyringNames.KeyringName']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ikev2_cfg as meta
            return meta._meta_table['Ikev2.KeyringNames']['meta_info']


    class ProfileNames(_Entity_):
        """
        IKEv2 profile config commands
        
        .. attribute:: profile_name
        
        	IKEv2 profile name
        	**type**\: list of  		 :py:class:`ProfileName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_cfg.Ikev2.ProfileNames.ProfileName>`
        
        

        """

        _prefix = 'ikev2-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Ikev2.ProfileNames, self).__init__()

            self.yang_name = "profile-names"
            self.yang_parent_name = "ikev2"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("profile-name", ("profile_name", Ikev2.ProfileNames.ProfileName))])
            self._leafs = OrderedDict()

            self.profile_name = YList(self)
            self._segment_path = lambda: "profile-names"
            self._absolute_path = lambda: "Cisco-IOS-XR-ikev2-cfg:ikev2/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ikev2.ProfileNames, [], name, value)


        class ProfileName(_Entity_):
            """
            IKEv2 profile name
            
            .. attribute:: name  (key)
            
            	Name of the profile
            	**type**\: str
            
            	**length:** 1..32
            
            .. attribute:: match_identity
            
            	Match a profile based on remote identity
            	**type**\:  :py:class:`MatchIdentity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_cfg.Ikev2.ProfileNames.ProfileName.MatchIdentity>`
            
            .. attribute:: dpd
            
            	Enable IKEv2 liveliness for peers
            	**type**\:  :py:class:`Dpd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_cfg.Ikev2.ProfileNames.ProfileName.Dpd>`
            
            .. attribute:: profile_sub
            
            	This indicates existence of profile
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: lifetime
            
            	Lifetime(in sec) for IKEv2 SA
            	**type**\: int
            
            	**range:** 120..86400
            
            .. attribute:: keyring_in_profile
            
            	Keyring to use with local/remote authentication method
            	**type**\: str
            
            	**length:** 1..32
            
            

            """

            _prefix = 'ikev2-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Ikev2.ProfileNames.ProfileName, self).__init__()

                self.yang_name = "profile-name"
                self.yang_parent_name = "profile-names"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['name']
                self._child_classes = OrderedDict([("match-identity", ("match_identity", Ikev2.ProfileNames.ProfileName.MatchIdentity)), ("dpd", ("dpd", Ikev2.ProfileNames.ProfileName.Dpd))])
                self._leafs = OrderedDict([
                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                    ('profile_sub', (YLeaf(YType.empty, 'profile-sub'), ['Empty'])),
                    ('lifetime', (YLeaf(YType.uint32, 'lifetime'), ['int'])),
                    ('keyring_in_profile', (YLeaf(YType.str, 'keyring-in-profile'), ['str'])),
                ])
                self.name = None
                self.profile_sub = None
                self.lifetime = None
                self.keyring_in_profile = None

                self.match_identity = Ikev2.ProfileNames.ProfileName.MatchIdentity()
                self.match_identity.parent = self
                self._children_name_map["match_identity"] = "match-identity"

                self.dpd = Ikev2.ProfileNames.ProfileName.Dpd()
                self.dpd.parent = self
                self._children_name_map["dpd"] = "dpd"
                self._segment_path = lambda: "profile-name" + "[name='" + str(self.name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ikev2-cfg:ikev2/profile-names/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ikev2.ProfileNames.ProfileName, ['name', 'profile_sub', 'lifetime', 'keyring_in_profile'], name, value)


            class MatchIdentity(_Entity_):
                """
                Match a profile based on remote identity
                
                .. attribute:: address_subs
                
                	Match a profile based on remote identity address
                	**type**\:  :py:class:`AddressSubs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_cfg.Ikev2.ProfileNames.ProfileName.MatchIdentity.AddressSubs>`
                
                .. attribute:: any
                
                	Match any peer identity
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'ikev2-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Ikev2.ProfileNames.ProfileName.MatchIdentity, self).__init__()

                    self.yang_name = "match-identity"
                    self.yang_parent_name = "profile-name"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("address-subs", ("address_subs", Ikev2.ProfileNames.ProfileName.MatchIdentity.AddressSubs))])
                    self._leafs = OrderedDict([
                        ('any', (YLeaf(YType.empty, 'any'), ['Empty'])),
                    ])
                    self.any = None

                    self.address_subs = Ikev2.ProfileNames.ProfileName.MatchIdentity.AddressSubs()
                    self.address_subs.parent = self
                    self._children_name_map["address_subs"] = "address-subs"
                    self._segment_path = lambda: "match-identity"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ikev2.ProfileNames.ProfileName.MatchIdentity, ['any'], name, value)


                class AddressSubs(_Entity_):
                    """
                    Match a profile based on remote identity
                    address
                    
                    .. attribute:: address_sub
                    
                    	Remote ip address for matching identity
                    	**type**\: list of  		 :py:class:`AddressSub <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_cfg.Ikev2.ProfileNames.ProfileName.MatchIdentity.AddressSubs.AddressSub>`
                    
                    

                    """

                    _prefix = 'ikev2-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Ikev2.ProfileNames.ProfileName.MatchIdentity.AddressSubs, self).__init__()

                        self.yang_name = "address-subs"
                        self.yang_parent_name = "match-identity"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("address-sub", ("address_sub", Ikev2.ProfileNames.ProfileName.MatchIdentity.AddressSubs.AddressSub))])
                        self._leafs = OrderedDict()

                        self.address_sub = YList(self)
                        self._segment_path = lambda: "address-subs"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ikev2.ProfileNames.ProfileName.MatchIdentity.AddressSubs, [], name, value)


                    class AddressSub(_Entity_):
                        """
                        Remote ip address for matching identity
                        
                        .. attribute:: address  (key)
                        
                        	Address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: address_sub_val
                        
                        	This indicates existence of remote ip address
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: mask
                        
                        	Mask
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ikev2-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Ikev2.ProfileNames.ProfileName.MatchIdentity.AddressSubs.AddressSub, self).__init__()

                            self.yang_name = "address-sub"
                            self.yang_parent_name = "address-subs"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['address']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('address', (YLeaf(YType.str, 'address'), ['str'])),
                                ('address_sub_val', (YLeaf(YType.empty, 'address-sub-val'), ['Empty'])),
                                ('mask', (YLeaf(YType.str, 'mask'), ['str'])),
                            ])
                            self.address = None
                            self.address_sub_val = None
                            self.mask = None
                            self._segment_path = lambda: "address-sub" + "[address='" + str(self.address) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ikev2.ProfileNames.ProfileName.MatchIdentity.AddressSubs.AddressSub, ['address', 'address_sub_val', 'mask'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ikev2_cfg as meta
                            return meta._meta_table['Ikev2.ProfileNames.ProfileName.MatchIdentity.AddressSubs.AddressSub']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ikev2_cfg as meta
                        return meta._meta_table['Ikev2.ProfileNames.ProfileName.MatchIdentity.AddressSubs']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ikev2_cfg as meta
                    return meta._meta_table['Ikev2.ProfileNames.ProfileName.MatchIdentity']['meta_info']


            class Dpd(_Entity_):
                """
                Enable IKEv2 liveliness for peers
                
                .. attribute:: interval
                
                	Interval(in sec)
                	**type**\: int
                
                	**range:** 10..3600
                
                .. attribute:: retry_time
                
                	Retry interval(in sec)
                	**type**\: int
                
                	**range:** 2..60
                
                

                """

                _prefix = 'ikev2-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Ikev2.ProfileNames.ProfileName.Dpd, self).__init__()

                    self.yang_name = "dpd"
                    self.yang_parent_name = "profile-name"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('interval', (YLeaf(YType.uint32, 'interval'), ['int'])),
                        ('retry_time', (YLeaf(YType.uint32, 'retry-time'), ['int'])),
                    ])
                    self.interval = None
                    self.retry_time = None
                    self._segment_path = lambda: "dpd"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ikev2.ProfileNames.ProfileName.Dpd, ['interval', 'retry_time'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ikev2_cfg as meta
                    return meta._meta_table['Ikev2.ProfileNames.ProfileName.Dpd']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ikev2_cfg as meta
                return meta._meta_table['Ikev2.ProfileNames.ProfileName']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ikev2_cfg as meta
            return meta._meta_table['Ikev2.ProfileNames']['meta_info']


    class PolicyNames(_Entity_):
        """
        Configure IKEv2 policies
        
        .. attribute:: policy_name
        
        	IKEv2 policy name
        	**type**\: list of  		 :py:class:`PolicyName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_cfg.Ikev2.PolicyNames.PolicyName>`
        
        

        """

        _prefix = 'ikev2-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Ikev2.PolicyNames, self).__init__()

            self.yang_name = "policy-names"
            self.yang_parent_name = "ikev2"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("policy-name", ("policy_name", Ikev2.PolicyNames.PolicyName))])
            self._leafs = OrderedDict()

            self.policy_name = YList(self)
            self._segment_path = lambda: "policy-names"
            self._absolute_path = lambda: "Cisco-IOS-XR-ikev2-cfg:ikev2/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ikev2.PolicyNames, [], name, value)


        class PolicyName(_Entity_):
            """
            IKEv2 policy name
            
            .. attribute:: name  (key)
            
            	Policy name
            	**type**\: str
            
            	**length:** 1..32
            
            .. attribute:: address_vals
            
            	Match a policy based on address
            	**type**\:  :py:class:`AddressVals <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_cfg.Ikev2.PolicyNames.PolicyName.AddressVals>`
            
            .. attribute:: proposal_in_policy
            
            	Proposal to use with configured policy
            	**type**\: str
            
            	**length:** 1..32
            
            .. attribute:: policy_sub
            
            	This indicates existence of policy
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'ikev2-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Ikev2.PolicyNames.PolicyName, self).__init__()

                self.yang_name = "policy-name"
                self.yang_parent_name = "policy-names"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['name']
                self._child_classes = OrderedDict([("address-vals", ("address_vals", Ikev2.PolicyNames.PolicyName.AddressVals))])
                self._leafs = OrderedDict([
                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                    ('proposal_in_policy', (YLeaf(YType.str, 'proposal-in-policy'), ['str'])),
                    ('policy_sub', (YLeaf(YType.empty, 'policy-sub'), ['Empty'])),
                ])
                self.name = None
                self.proposal_in_policy = None
                self.policy_sub = None

                self.address_vals = Ikev2.PolicyNames.PolicyName.AddressVals()
                self.address_vals.parent = self
                self._children_name_map["address_vals"] = "address-vals"
                self._segment_path = lambda: "policy-name" + "[name='" + str(self.name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ikev2-cfg:ikev2/policy-names/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ikev2.PolicyNames.PolicyName, ['name', 'proposal_in_policy', 'policy_sub'], name, value)


            class AddressVals(_Entity_):
                """
                Match a policy based on address
                
                .. attribute:: address_val
                
                	local address used to match policy
                	**type**\: list of  		 :py:class:`AddressVal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_cfg.Ikev2.PolicyNames.PolicyName.AddressVals.AddressVal>`
                
                

                """

                _prefix = 'ikev2-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Ikev2.PolicyNames.PolicyName.AddressVals, self).__init__()

                    self.yang_name = "address-vals"
                    self.yang_parent_name = "policy-name"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("address-val", ("address_val", Ikev2.PolicyNames.PolicyName.AddressVals.AddressVal))])
                    self._leafs = OrderedDict()

                    self.address_val = YList(self)
                    self._segment_path = lambda: "address-vals"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ikev2.PolicyNames.PolicyName.AddressVals, [], name, value)


                class AddressVal(_Entity_):
                    """
                    local address used to match policy
                    
                    .. attribute:: address  (key)
                    
                    	Address
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'ikev2-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Ikev2.PolicyNames.PolicyName.AddressVals.AddressVal, self).__init__()

                        self.yang_name = "address-val"
                        self.yang_parent_name = "address-vals"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['address']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('address', (YLeaf(YType.str, 'address'), ['str'])),
                        ])
                        self.address = None
                        self._segment_path = lambda: "address-val" + "[address='" + str(self.address) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ikev2.PolicyNames.PolicyName.AddressVals.AddressVal, ['address'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ikev2_cfg as meta
                        return meta._meta_table['Ikev2.PolicyNames.PolicyName.AddressVals.AddressVal']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ikev2_cfg as meta
                    return meta._meta_table['Ikev2.PolicyNames.PolicyName.AddressVals']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ikev2_cfg as meta
                return meta._meta_table['Ikev2.PolicyNames.PolicyName']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ikev2_cfg as meta
            return meta._meta_table['Ikev2.PolicyNames']['meta_info']


    class ProposalNames(_Entity_):
        """
        Configure IKEv2 proposals
        
        .. attribute:: proposal_name
        
        	IKEv2 proposal name
        	**type**\: list of  		 :py:class:`ProposalName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_cfg.Ikev2.ProposalNames.ProposalName>`
        
        

        """

        _prefix = 'ikev2-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Ikev2.ProposalNames, self).__init__()

            self.yang_name = "proposal-names"
            self.yang_parent_name = "ikev2"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("proposal-name", ("proposal_name", Ikev2.ProposalNames.ProposalName))])
            self._leafs = OrderedDict()

            self.proposal_name = YList(self)
            self._segment_path = lambda: "proposal-names"
            self._absolute_path = lambda: "Cisco-IOS-XR-ikev2-cfg:ikev2/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ikev2.ProposalNames, [], name, value)


        class ProposalName(_Entity_):
            """
            IKEv2 proposal name
            
            .. attribute:: name  (key)
            
            	Proposal name
            	**type**\: str
            
            	**length:** 1..32
            
            .. attribute:: prfses
            
            	Specify one or more transforms of prf
            	**type**\:  :py:class:`Prfses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_cfg.Ikev2.ProposalNames.ProposalName.Prfses>`
            
            .. attribute:: groups
            
            	Specify one or more transforms of group
            	**type**\:  :py:class:`Groups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_cfg.Ikev2.ProposalNames.ProposalName.Groups>`
            
            .. attribute:: integrities
            
            	Specify one or more transforms of integrity
            	**type**\:  :py:class:`Integrities <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_cfg.Ikev2.ProposalNames.ProposalName.Integrities>`
            
            .. attribute:: encryptions
            
            	Specify one or more transforms of encryption
            	**type**\:  :py:class:`Encryptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_cfg.Ikev2.ProposalNames.ProposalName.Encryptions>`
            
            .. attribute:: proposal_sub
            
            	This indicates existence of proposal
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'ikev2-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Ikev2.ProposalNames.ProposalName, self).__init__()

                self.yang_name = "proposal-name"
                self.yang_parent_name = "proposal-names"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['name']
                self._child_classes = OrderedDict([("prfses", ("prfses", Ikev2.ProposalNames.ProposalName.Prfses)), ("groups", ("groups", Ikev2.ProposalNames.ProposalName.Groups)), ("integrities", ("integrities", Ikev2.ProposalNames.ProposalName.Integrities)), ("encryptions", ("encryptions", Ikev2.ProposalNames.ProposalName.Encryptions))])
                self._leafs = OrderedDict([
                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                    ('proposal_sub', (YLeaf(YType.empty, 'proposal-sub'), ['Empty'])),
                ])
                self.name = None
                self.proposal_sub = None

                self.prfses = Ikev2.ProposalNames.ProposalName.Prfses()
                self.prfses.parent = self
                self._children_name_map["prfses"] = "prfses"

                self.groups = Ikev2.ProposalNames.ProposalName.Groups()
                self.groups.parent = self
                self._children_name_map["groups"] = "groups"

                self.integrities = Ikev2.ProposalNames.ProposalName.Integrities()
                self.integrities.parent = self
                self._children_name_map["integrities"] = "integrities"

                self.encryptions = Ikev2.ProposalNames.ProposalName.Encryptions()
                self.encryptions.parent = self
                self._children_name_map["encryptions"] = "encryptions"
                self._segment_path = lambda: "proposal-name" + "[name='" + str(self.name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ikev2-cfg:ikev2/proposal-names/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ikev2.ProposalNames.ProposalName, ['name', 'proposal_sub'], name, value)


            class Prfses(_Entity_):
                """
                Specify one or more transforms of prf
                
                .. attribute:: prfs
                
                	PRF Algorithm
                	**type**\: list of str
                
                	**length:** 1..8
                
                

                """

                _prefix = 'ikev2-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Ikev2.ProposalNames.ProposalName.Prfses, self).__init__()

                    self.yang_name = "prfses"
                    self.yang_parent_name = "proposal-name"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('prfs', (YLeafList(YType.str, 'prfs'), ['str'])),
                    ])
                    self.prfs = []
                    self._segment_path = lambda: "prfses"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ikev2.ProposalNames.ProposalName.Prfses, ['prfs'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ikev2_cfg as meta
                    return meta._meta_table['Ikev2.ProposalNames.ProposalName.Prfses']['meta_info']


            class Groups(_Entity_):
                """
                Specify one or more transforms of group
                
                .. attribute:: group
                
                	Encryption Algorithm
                	**type**\: list of str
                
                	**length:** 1..3
                
                

                """

                _prefix = 'ikev2-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Ikev2.ProposalNames.ProposalName.Groups, self).__init__()

                    self.yang_name = "groups"
                    self.yang_parent_name = "proposal-name"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('group', (YLeafList(YType.str, 'group'), ['str'])),
                    ])
                    self.group = []
                    self._segment_path = lambda: "groups"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ikev2.ProposalNames.ProposalName.Groups, ['group'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ikev2_cfg as meta
                    return meta._meta_table['Ikev2.ProposalNames.ProposalName.Groups']['meta_info']


            class Integrities(_Entity_):
                """
                Specify one or more transforms of integrity
                
                .. attribute:: integrity
                
                	Integrity Algorithm
                	**type**\: list of str
                
                	**length:** 1..8
                
                

                """

                _prefix = 'ikev2-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Ikev2.ProposalNames.ProposalName.Integrities, self).__init__()

                    self.yang_name = "integrities"
                    self.yang_parent_name = "proposal-name"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('integrity', (YLeafList(YType.str, 'integrity'), ['str'])),
                    ])
                    self.integrity = []
                    self._segment_path = lambda: "integrities"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ikev2.ProposalNames.ProposalName.Integrities, ['integrity'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ikev2_cfg as meta
                    return meta._meta_table['Ikev2.ProposalNames.ProposalName.Integrities']['meta_info']


            class Encryptions(_Entity_):
                """
                Specify one or more transforms of encryption
                
                .. attribute:: encryption
                
                	Encryption Algorithm
                	**type**\: list of str
                
                	**length:** 1..12
                
                

                """

                _prefix = 'ikev2-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Ikev2.ProposalNames.ProposalName.Encryptions, self).__init__()

                    self.yang_name = "encryptions"
                    self.yang_parent_name = "proposal-name"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('encryption', (YLeafList(YType.str, 'encryption'), ['str'])),
                    ])
                    self.encryption = []
                    self._segment_path = lambda: "encryptions"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ikev2.ProposalNames.ProposalName.Encryptions, ['encryption'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ikev2_cfg as meta
                    return meta._meta_table['Ikev2.ProposalNames.ProposalName.Encryptions']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ikev2_cfg as meta
                return meta._meta_table['Ikev2.ProposalNames.ProposalName']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ikev2_cfg as meta
            return meta._meta_table['Ikev2.ProposalNames']['meta_info']

    def clone_ptr(self):
        self._top_entity = Ikev2()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ikev2_cfg as meta
        return meta._meta_table['Ikev2']['meta_info']


