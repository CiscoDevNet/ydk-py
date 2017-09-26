""" Cisco_IOS_XR_pbr_vrf_policy_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR pbr\-vrf\-policy package configuration.

This module contains definitions
for the following management objects\:
  vrf\-policy\: VRF Policy PBR configuration

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class VrfPolicy(Entity):
    """
    VRF Policy PBR configuration
    
    .. attribute:: vrf
    
    	VRF Name
    	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vrf_policy_cfg.VrfPolicy.Vrf>`
    
    

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
        self._child_container_classes = {}
        self._child_list_classes = {"vrf" : ("vrf", VrfPolicy.Vrf)}

        self.vrf = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-pbr-vrf-policy-cfg:vrf-policy"

    def __setattr__(self, name, value):
        self._perform_setattr(VrfPolicy, [], name, value)


    class Vrf(Entity):
        """
        VRF Name
        
        .. attribute:: vrf_name  <key>
        
        	VRF name
        	**type**\:  str
        
        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
        
        .. attribute:: afi
        
        	address family
        	**type**\: list of    :py:class:`Afi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vrf_policy_cfg.VrfPolicy.Vrf.Afi>`
        
        

        """

        _prefix = 'pbr-vrf-policy-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(VrfPolicy.Vrf, self).__init__()

            self.yang_name = "vrf"
            self.yang_parent_name = "vrf-policy"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"afi" : ("afi", VrfPolicy.Vrf.Afi)}

            self.vrf_name = YLeaf(YType.str, "vrf-name")

            self.afi = YList(self)
            self._segment_path = lambda: "vrf" + "[vrf-name='" + self.vrf_name.get() + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-pbr-vrf-policy-cfg:vrf-policy/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(VrfPolicy.Vrf, ['vrf_name'], name, value)


        class Afi(Entity):
            """
            address family
            
            .. attribute:: afi_type  <key>
            
            	AFI name
            	**type**\:  str
            
            	**pattern:** (ipv4)
            
            .. attribute:: service_policy_in
            
            	Policy map name
            	**type**\:  str
            
            

            """

            _prefix = 'pbr-vrf-policy-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(VrfPolicy.Vrf.Afi, self).__init__()

                self.yang_name = "afi"
                self.yang_parent_name = "vrf"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.afi_type = YLeaf(YType.str, "afi-type")

                self.service_policy_in = YLeaf(YType.str, "service-policy-in")
                self._segment_path = lambda: "afi" + "[afi-type='" + self.afi_type.get() + "']"

            def __setattr__(self, name, value):
                self._perform_setattr(VrfPolicy.Vrf.Afi, ['afi_type', 'service_policy_in'], name, value)

    def clone_ptr(self):
        self._top_entity = VrfPolicy()
        return self._top_entity

