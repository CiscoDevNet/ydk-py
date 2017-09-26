""" Cisco_IOS_XR_mpls_vpn_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR mpls\-vpn package operational data.

This module contains definitions
for the following management objects\:
  l3vpn\: L3VPN operational data

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class MplsVpnAfi(Enum):
    """
    MplsVpnAfi

    Layer 3 VPN Address Family Type

    .. data:: ipv4 = 1

    	VRF IPv4 address family

    .. data:: ipv6 = 2

    	VRF IPv6 address family

    """

    ipv4 = Enum.YLeaf(1, "ipv4")

    ipv6 = Enum.YLeaf(2, "ipv6")


class MplsVpnRt(Enum):
    """
    MplsVpnRt

    Layer 3 VPN Route Target Type

    .. data:: import_ = 1

    	VRF Route Target Type Import

    .. data:: export = 2

    	VRF Route Target Type Export

    .. data:: both = 3

    	VRF Route Target Type Import and Export

    """

    import_ = Enum.YLeaf(1, "import")

    export = Enum.YLeaf(2, "export")

    both = Enum.YLeaf(3, "both")


class MplsVpnSafi(Enum):
    """
    MplsVpnSafi

    Layer 3 VPN Sub\-Address Family Type

    .. data:: unicast = 1

    	VRF Unicast sub-address family

    .. data:: multicast = 2

    	VRF Multicast sub-address family

    .. data:: flowspec = 133

    	VRF Flowspec sub-address family

    """

    unicast = Enum.YLeaf(1, "unicast")

    multicast = Enum.YLeaf(2, "multicast")

    flowspec = Enum.YLeaf(133, "flowspec")



class L3Vpn(Entity):
    """
    L3VPN operational data
    
    .. attribute:: invalid_vrfs
    
    	Invalid VRF Table (VRFs that are forward referenced)
    	**type**\:   :py:class:`InvalidVrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_vpn_oper.L3Vpn.InvalidVrfs>`
    
    .. attribute:: vrfs
    
    	VRF Table
    	**type**\:   :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_vpn_oper.L3Vpn.Vrfs>`
    
    

    """

    _prefix = 'mpls-vpn-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(L3Vpn, self).__init__()
        self._top_entity = None

        self.yang_name = "l3vpn"
        self.yang_parent_name = "Cisco-IOS-XR-mpls-vpn-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"invalid-vrfs" : ("invalid_vrfs", L3Vpn.InvalidVrfs), "vrfs" : ("vrfs", L3Vpn.Vrfs)}
        self._child_list_classes = {}

        self.invalid_vrfs = L3Vpn.InvalidVrfs()
        self.invalid_vrfs.parent = self
        self._children_name_map["invalid_vrfs"] = "invalid-vrfs"
        self._children_yang_names.add("invalid-vrfs")

        self.vrfs = L3Vpn.Vrfs()
        self.vrfs.parent = self
        self._children_name_map["vrfs"] = "vrfs"
        self._children_yang_names.add("vrfs")
        self._segment_path = lambda: "Cisco-IOS-XR-mpls-vpn-oper:l3vpn"


    class InvalidVrfs(Entity):
        """
        Invalid VRF Table (VRFs that are forward
        referenced)
        
        .. attribute:: invalid_vrf
        
        	Invalid VRF (VRF that is forward referenced)
        	**type**\: list of    :py:class:`InvalidVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_vpn_oper.L3Vpn.InvalidVrfs.InvalidVrf>`
        
        

        """

        _prefix = 'mpls-vpn-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(L3Vpn.InvalidVrfs, self).__init__()

            self.yang_name = "invalid-vrfs"
            self.yang_parent_name = "l3vpn"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"invalid-vrf" : ("invalid_vrf", L3Vpn.InvalidVrfs.InvalidVrf)}

            self.invalid_vrf = YList(self)
            self._segment_path = lambda: "invalid-vrfs"
            self._absolute_path = lambda: "Cisco-IOS-XR-mpls-vpn-oper:l3vpn/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(L3Vpn.InvalidVrfs, [], name, value)


        class InvalidVrf(Entity):
            """
            Invalid VRF (VRF that is forward referenced)
            
            .. attribute:: vrf_name  <key>
            
            	The Name for an invalid VRF
            	**type**\:  str
            
            .. attribute:: af
            
            	AF/SAF information
            	**type**\: list of    :py:class:`Af <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_vpn_oper.L3Vpn.InvalidVrfs.InvalidVrf.Af>`
            
            .. attribute:: interface
            
            	Interfaces in VRF
            	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_vpn_oper.L3Vpn.InvalidVrfs.InvalidVrf.Interface>`
            
            .. attribute:: is_big_vrf
            
            	VRF mode information
            	**type**\:  bool
            
            .. attribute:: route_distinguisher
            
            	Route Distinguisher
            	**type**\:  str
            
            .. attribute:: vrf_description
            
            	VRF Description
            	**type**\:  str
            
            .. attribute:: vrf_name_xr
            
            	VRF Name
            	**type**\:  str
            
            

            """

            _prefix = 'mpls-vpn-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(L3Vpn.InvalidVrfs.InvalidVrf, self).__init__()

                self.yang_name = "invalid-vrf"
                self.yang_parent_name = "invalid-vrfs"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"af" : ("af", L3Vpn.InvalidVrfs.InvalidVrf.Af), "interface" : ("interface", L3Vpn.InvalidVrfs.InvalidVrf.Interface)}

                self.vrf_name = YLeaf(YType.str, "vrf-name")

                self.is_big_vrf = YLeaf(YType.boolean, "is-big-vrf")

                self.route_distinguisher = YLeaf(YType.str, "route-distinguisher")

                self.vrf_description = YLeaf(YType.str, "vrf-description")

                self.vrf_name_xr = YLeaf(YType.str, "vrf-name-xr")

                self.af = YList(self)
                self.interface = YList(self)
                self._segment_path = lambda: "invalid-vrf" + "[vrf-name='" + self.vrf_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-mpls-vpn-oper:l3vpn/invalid-vrfs/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(L3Vpn.InvalidVrfs.InvalidVrf, ['vrf_name', 'is_big_vrf', 'route_distinguisher', 'vrf_description', 'vrf_name_xr'], name, value)


            class Af(Entity):
                """
                AF/SAF information
                
                .. attribute:: af_name
                
                	AF name
                	**type**\:   :py:class:`MplsVpnAfi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_vpn_oper.MplsVpnAfi>`
                
                .. attribute:: export_route_policy
                
                	Export Route Policy
                	**type**\:  str
                
                .. attribute:: import_route_policy
                
                	Import Route Policy
                	**type**\:  str
                
                .. attribute:: route_target
                
                	Route Targets
                	**type**\: list of    :py:class:`RouteTarget <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_vpn_oper.L3Vpn.InvalidVrfs.InvalidVrf.Af.RouteTarget>`
                
                .. attribute:: saf_name
                
                	SAF name
                	**type**\:   :py:class:`MplsVpnSafi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_vpn_oper.MplsVpnSafi>`
                
                

                """

                _prefix = 'mpls-vpn-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(L3Vpn.InvalidVrfs.InvalidVrf.Af, self).__init__()

                    self.yang_name = "af"
                    self.yang_parent_name = "invalid-vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"route-target" : ("route_target", L3Vpn.InvalidVrfs.InvalidVrf.Af.RouteTarget)}

                    self.af_name = YLeaf(YType.enumeration, "af-name")

                    self.export_route_policy = YLeaf(YType.str, "export-route-policy")

                    self.import_route_policy = YLeaf(YType.str, "import-route-policy")

                    self.saf_name = YLeaf(YType.enumeration, "saf-name")

                    self.route_target = YList(self)
                    self._segment_path = lambda: "af"

                def __setattr__(self, name, value):
                    self._perform_setattr(L3Vpn.InvalidVrfs.InvalidVrf.Af, ['af_name', 'export_route_policy', 'import_route_policy', 'saf_name'], name, value)


                class RouteTarget(Entity):
                    """
                    Route Targets
                    
                    .. attribute:: af_name
                    
                    	AF name
                    	**type**\:   :py:class:`MplsVpnAfi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_vpn_oper.MplsVpnAfi>`
                    
                    .. attribute:: route_target_type
                    
                    	Route Target Type
                    	**type**\:   :py:class:`MplsVpnRt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_vpn_oper.MplsVpnRt>`
                    
                    .. attribute:: route_target_value
                    
                    	Route Target Value
                    	**type**\:  str
                    
                    .. attribute:: saf_name
                    
                    	SAF name
                    	**type**\:   :py:class:`MplsVpnSafi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_vpn_oper.MplsVpnSafi>`
                    
                    

                    """

                    _prefix = 'mpls-vpn-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(L3Vpn.InvalidVrfs.InvalidVrf.Af.RouteTarget, self).__init__()

                        self.yang_name = "route-target"
                        self.yang_parent_name = "af"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.af_name = YLeaf(YType.enumeration, "af-name")

                        self.route_target_type = YLeaf(YType.enumeration, "route-target-type")

                        self.route_target_value = YLeaf(YType.str, "route-target-value")

                        self.saf_name = YLeaf(YType.enumeration, "saf-name")
                        self._segment_path = lambda: "route-target"

                    def __setattr__(self, name, value):
                        self._perform_setattr(L3Vpn.InvalidVrfs.InvalidVrf.Af.RouteTarget, ['af_name', 'route_target_type', 'route_target_value', 'saf_name'], name, value)


            class Interface(Entity):
                """
                Interfaces in VRF
                
                .. attribute:: interface_name
                
                	Interface Name
                	**type**\:  str
                
                

                """

                _prefix = 'mpls-vpn-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(L3Vpn.InvalidVrfs.InvalidVrf.Interface, self).__init__()

                    self.yang_name = "interface"
                    self.yang_parent_name = "invalid-vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.interface_name = YLeaf(YType.str, "interface-name")
                    self._segment_path = lambda: "interface"

                def __setattr__(self, name, value):
                    self._perform_setattr(L3Vpn.InvalidVrfs.InvalidVrf.Interface, ['interface_name'], name, value)


    class Vrfs(Entity):
        """
        VRF Table
        
        .. attribute:: vrf
        
        	VRF
        	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_vpn_oper.L3Vpn.Vrfs.Vrf>`
        
        

        """

        _prefix = 'mpls-vpn-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(L3Vpn.Vrfs, self).__init__()

            self.yang_name = "vrfs"
            self.yang_parent_name = "l3vpn"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"vrf" : ("vrf", L3Vpn.Vrfs.Vrf)}

            self.vrf = YList(self)
            self._segment_path = lambda: "vrfs"
            self._absolute_path = lambda: "Cisco-IOS-XR-mpls-vpn-oper:l3vpn/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(L3Vpn.Vrfs, [], name, value)


        class Vrf(Entity):
            """
            VRF
            
            .. attribute:: vrf_name  <key>
            
            	The Name for a VRF
            	**type**\:  str
            
            .. attribute:: af
            
            	AF/SAF information
            	**type**\: list of    :py:class:`Af <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_vpn_oper.L3Vpn.Vrfs.Vrf.Af>`
            
            .. attribute:: interface
            
            	Interfaces in VRF
            	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_vpn_oper.L3Vpn.Vrfs.Vrf.Interface>`
            
            .. attribute:: is_big_vrf
            
            	VRF mode information
            	**type**\:  bool
            
            .. attribute:: route_distinguisher
            
            	Route Distinguisher
            	**type**\:  str
            
            .. attribute:: vrf_description
            
            	VRF Description
            	**type**\:  str
            
            .. attribute:: vrf_name_xr
            
            	VRF Name
            	**type**\:  str
            
            

            """

            _prefix = 'mpls-vpn-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(L3Vpn.Vrfs.Vrf, self).__init__()

                self.yang_name = "vrf"
                self.yang_parent_name = "vrfs"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"af" : ("af", L3Vpn.Vrfs.Vrf.Af), "interface" : ("interface", L3Vpn.Vrfs.Vrf.Interface)}

                self.vrf_name = YLeaf(YType.str, "vrf-name")

                self.is_big_vrf = YLeaf(YType.boolean, "is-big-vrf")

                self.route_distinguisher = YLeaf(YType.str, "route-distinguisher")

                self.vrf_description = YLeaf(YType.str, "vrf-description")

                self.vrf_name_xr = YLeaf(YType.str, "vrf-name-xr")

                self.af = YList(self)
                self.interface = YList(self)
                self._segment_path = lambda: "vrf" + "[vrf-name='" + self.vrf_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-mpls-vpn-oper:l3vpn/vrfs/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(L3Vpn.Vrfs.Vrf, ['vrf_name', 'is_big_vrf', 'route_distinguisher', 'vrf_description', 'vrf_name_xr'], name, value)


            class Af(Entity):
                """
                AF/SAF information
                
                .. attribute:: af_name
                
                	AF name
                	**type**\:   :py:class:`MplsVpnAfi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_vpn_oper.MplsVpnAfi>`
                
                .. attribute:: export_route_policy
                
                	Export Route Policy
                	**type**\:  str
                
                .. attribute:: import_route_policy
                
                	Import Route Policy
                	**type**\:  str
                
                .. attribute:: route_target
                
                	Route Targets
                	**type**\: list of    :py:class:`RouteTarget <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_vpn_oper.L3Vpn.Vrfs.Vrf.Af.RouteTarget>`
                
                .. attribute:: saf_name
                
                	SAF name
                	**type**\:   :py:class:`MplsVpnSafi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_vpn_oper.MplsVpnSafi>`
                
                

                """

                _prefix = 'mpls-vpn-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(L3Vpn.Vrfs.Vrf.Af, self).__init__()

                    self.yang_name = "af"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"route-target" : ("route_target", L3Vpn.Vrfs.Vrf.Af.RouteTarget)}

                    self.af_name = YLeaf(YType.enumeration, "af-name")

                    self.export_route_policy = YLeaf(YType.str, "export-route-policy")

                    self.import_route_policy = YLeaf(YType.str, "import-route-policy")

                    self.saf_name = YLeaf(YType.enumeration, "saf-name")

                    self.route_target = YList(self)
                    self._segment_path = lambda: "af"

                def __setattr__(self, name, value):
                    self._perform_setattr(L3Vpn.Vrfs.Vrf.Af, ['af_name', 'export_route_policy', 'import_route_policy', 'saf_name'], name, value)


                class RouteTarget(Entity):
                    """
                    Route Targets
                    
                    .. attribute:: af_name
                    
                    	AF name
                    	**type**\:   :py:class:`MplsVpnAfi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_vpn_oper.MplsVpnAfi>`
                    
                    .. attribute:: route_target_type
                    
                    	Route Target Type
                    	**type**\:   :py:class:`MplsVpnRt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_vpn_oper.MplsVpnRt>`
                    
                    .. attribute:: route_target_value
                    
                    	Route Target Value
                    	**type**\:  str
                    
                    .. attribute:: saf_name
                    
                    	SAF name
                    	**type**\:   :py:class:`MplsVpnSafi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_vpn_oper.MplsVpnSafi>`
                    
                    

                    """

                    _prefix = 'mpls-vpn-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(L3Vpn.Vrfs.Vrf.Af.RouteTarget, self).__init__()

                        self.yang_name = "route-target"
                        self.yang_parent_name = "af"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.af_name = YLeaf(YType.enumeration, "af-name")

                        self.route_target_type = YLeaf(YType.enumeration, "route-target-type")

                        self.route_target_value = YLeaf(YType.str, "route-target-value")

                        self.saf_name = YLeaf(YType.enumeration, "saf-name")
                        self._segment_path = lambda: "route-target"

                    def __setattr__(self, name, value):
                        self._perform_setattr(L3Vpn.Vrfs.Vrf.Af.RouteTarget, ['af_name', 'route_target_type', 'route_target_value', 'saf_name'], name, value)


            class Interface(Entity):
                """
                Interfaces in VRF
                
                .. attribute:: interface_name
                
                	Interface Name
                	**type**\:  str
                
                

                """

                _prefix = 'mpls-vpn-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(L3Vpn.Vrfs.Vrf.Interface, self).__init__()

                    self.yang_name = "interface"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.interface_name = YLeaf(YType.str, "interface-name")
                    self._segment_path = lambda: "interface"

                def __setattr__(self, name, value):
                    self._perform_setattr(L3Vpn.Vrfs.Vrf.Interface, ['interface_name'], name, value)

    def clone_ptr(self):
        self._top_entity = L3Vpn()
        return self._top_entity

