""" Cisco_IOS_XR_ppp_ma_ssrp_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ppp\-ma\-ssrp package configuration.

This module contains definitions
for the following management objects\:
  ssrp\: Shared plane SSRP configuration data

This YANG module augments the
  Cisco\-IOS\-XR\-config\-mda\-cfg,
  Cisco\-IOS\-XR\-ifmgr\-cfg
modules with configuration data.

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class Ssrp(Entity):
    """
    Shared plane SSRP configuration data
    
    .. attribute:: profiles
    
    	Table of SSRP Profiles
    	**type**\:  :py:class:`Profiles <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_ssrp_cfg.Ssrp.Profiles>`
    
    

    """

    _prefix = 'ppp-ma-ssrp-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(Ssrp, self).__init__()
        self._top_entity = None

        self.yang_name = "ssrp"
        self.yang_parent_name = "Cisco-IOS-XR-ppp-ma-ssrp-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("profiles", ("profiles", Ssrp.Profiles))])
        self._leafs = OrderedDict()

        self.profiles = Ssrp.Profiles()
        self.profiles.parent = self
        self._children_name_map["profiles"] = "profiles"
        self._segment_path = lambda: "Cisco-IOS-XR-ppp-ma-ssrp-cfg:ssrp"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Ssrp, [], name, value)


    class Profiles(Entity):
        """
        Table of SSRP Profiles
        
        .. attribute:: profile
        
        	SSRP Profile configuration
        	**type**\: list of  		 :py:class:`Profile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_ssrp_cfg.Ssrp.Profiles.Profile>`
        
        

        """

        _prefix = 'ppp-ma-ssrp-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Ssrp.Profiles, self).__init__()

            self.yang_name = "profiles"
            self.yang_parent_name = "ssrp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("profile", ("profile", Ssrp.Profiles.Profile))])
            self._leafs = OrderedDict()

            self.profile = YList(self)
            self._segment_path = lambda: "profiles"
            self._absolute_path = lambda: "Cisco-IOS-XR-ppp-ma-ssrp-cfg:ssrp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ssrp.Profiles, [], name, value)


        class Profile(Entity):
            """
            SSRP Profile configuration
            
            .. attribute:: name  (key)
            
            	The name of the profile
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: max_hops
            
            	This specifies the maximum number of hops for packets on the SSO channel
            	**type**\: int
            
            	**range:** 1..255
            
            .. attribute:: peer_ipv4_address
            
            	This specifies the remote end's IPv4\-address for the SSO channel
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            

            """

            _prefix = 'ppp-ma-ssrp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Ssrp.Profiles.Profile, self).__init__()

                self.yang_name = "profile"
                self.yang_parent_name = "profiles"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['name']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                    ('max_hops', (YLeaf(YType.uint32, 'max-hops'), ['int'])),
                    ('peer_ipv4_address', (YLeaf(YType.str, 'peer-ipv4-address'), ['str'])),
                ])
                self.name = None
                self.max_hops = None
                self.peer_ipv4_address = None
                self._segment_path = lambda: "profile" + "[name='" + str(self.name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ppp-ma-ssrp-cfg:ssrp/profiles/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ssrp.Profiles.Profile, ['name', 'max_hops', 'peer_ipv4_address'], name, value)

    def clone_ptr(self):
        self._top_entity = Ssrp()
        return self._top_entity

