""" Cisco_IOS_XR_pbr_vrf_policy_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR pbr\-vrf\-policy package configuration.

This module contains definitions
for the following management objects\:
  vrf\-policy\: VRF Policy PBR configuration

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class VrfPolicy(Entity):
    """
    VRF Policy PBR configuration
    
    .. attribute:: vrf
    
    	VRF Name
    	**type**\: list of  		 :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vrf_policy_cfg.VrfPolicy.Vrf>`
    
    

    """

    _prefix = 'pbr-vrf-policy-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(VrfPolicy, self).__init__()
        self._top_entity = None

        self.yang_name = "vrf-policy"
        self.yang_parent_name = "Cisco-IOS-XR-pbr-vrf-policy-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("vrf", ("vrf", VrfPolicy.Vrf))])
        self._leafs = OrderedDict()

        self.vrf = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-pbr-vrf-policy-cfg:vrf-policy"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(VrfPolicy, [], name, value)


    class Vrf(Entity):
        """
        VRF Name
        
        .. attribute:: vrf_name  (key)
        
        	VRF name
        	**type**\: str
        
        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
        
        .. attribute:: afi
        
        	address family
        	**type**\: list of  		 :py:class:`Afi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vrf_policy_cfg.VrfPolicy.Vrf.Afi>`
        
        

        """

        _prefix = 'pbr-vrf-policy-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(VrfPolicy.Vrf, self).__init__()

            self.yang_name = "vrf"
            self.yang_parent_name = "vrf-policy"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['vrf_name']
            self._child_classes = OrderedDict([("afi", ("afi", VrfPolicy.Vrf.Afi))])
            self._leafs = OrderedDict([
                ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
            ])
            self.vrf_name = None

            self.afi = YList(self)
            self._segment_path = lambda: "vrf" + "[vrf-name='" + str(self.vrf_name) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-pbr-vrf-policy-cfg:vrf-policy/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(VrfPolicy.Vrf, ['vrf_name'], name, value)


        class Afi(Entity):
            """
            address family
            
            .. attribute:: afi_type  (key)
            
            	AFI name
            	**type**\: str
            
            	**pattern:** (ipv4)\|(ipv6)
            
            .. attribute:: service_policy_in
            
            	Policy map name
            	**type**\: str
            
            

            """

            _prefix = 'pbr-vrf-policy-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(VrfPolicy.Vrf.Afi, self).__init__()

                self.yang_name = "afi"
                self.yang_parent_name = "vrf"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = ['afi_type']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('afi_type', (YLeaf(YType.str, 'afi-type'), ['str'])),
                    ('service_policy_in', (YLeaf(YType.str, 'service-policy-in'), ['str'])),
                ])
                self.afi_type = None
                self.service_policy_in = None
                self._segment_path = lambda: "afi" + "[afi-type='" + str(self.afi_type) + "']"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(VrfPolicy.Vrf.Afi, ['afi_type', 'service_policy_in'], name, value)

    def clone_ptr(self):
        self._top_entity = VrfPolicy()
        return self._top_entity

