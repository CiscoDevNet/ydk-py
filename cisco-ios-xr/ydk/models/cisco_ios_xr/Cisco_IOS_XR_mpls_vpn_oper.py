""" Cisco_IOS_XR_mpls_vpn_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR mpls\-vpn package operational data.

This module contains definitions
for the following management objects\:
  l3vpn\: L3VPN operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
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

        self.invalid_vrfs = L3Vpn.InvalidVrfs()
        self.invalid_vrfs.parent = self
        self._children_name_map["invalid_vrfs"] = "invalid-vrfs"
        self._children_yang_names.add("invalid-vrfs")

        self.vrfs = L3Vpn.Vrfs()
        self.vrfs.parent = self
        self._children_name_map["vrfs"] = "vrfs"
        self._children_yang_names.add("vrfs")


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

            self.invalid_vrf = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(L3Vpn.InvalidVrfs, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(L3Vpn.InvalidVrfs, self).__setattr__(name, value)


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

                self.vrf_name = YLeaf(YType.str, "vrf-name")

                self.is_big_vrf = YLeaf(YType.boolean, "is-big-vrf")

                self.route_distinguisher = YLeaf(YType.str, "route-distinguisher")

                self.vrf_description = YLeaf(YType.str, "vrf-description")

                self.vrf_name_xr = YLeaf(YType.str, "vrf-name-xr")

                self.af = YList(self)
                self.interface = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("vrf_name",
                                "is_big_vrf",
                                "route_distinguisher",
                                "vrf_description",
                                "vrf_name_xr") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(L3Vpn.InvalidVrfs.InvalidVrf, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(L3Vpn.InvalidVrfs.InvalidVrf, self).__setattr__(name, value)


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

                    self.interface_name = YLeaf(YType.str, "interface-name")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("interface_name") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(L3Vpn.InvalidVrfs.InvalidVrf.Interface, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(L3Vpn.InvalidVrfs.InvalidVrf.Interface, self).__setattr__(name, value)

                def has_data(self):
                    return self.interface_name.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.interface_name.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "interface" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.interface_name.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "interface-name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "interface-name"):
                        self.interface_name = value
                        self.interface_name.value_namespace = name_space
                        self.interface_name.value_namespace_prefix = name_space_prefix


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

                    self.af_name = YLeaf(YType.enumeration, "af-name")

                    self.export_route_policy = YLeaf(YType.str, "export-route-policy")

                    self.import_route_policy = YLeaf(YType.str, "import-route-policy")

                    self.saf_name = YLeaf(YType.enumeration, "saf-name")

                    self.route_target = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("af_name",
                                    "export_route_policy",
                                    "import_route_policy",
                                    "saf_name") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(L3Vpn.InvalidVrfs.InvalidVrf.Af, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(L3Vpn.InvalidVrfs.InvalidVrf.Af, self).__setattr__(name, value)


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

                        self.af_name = YLeaf(YType.enumeration, "af-name")

                        self.route_target_type = YLeaf(YType.enumeration, "route-target-type")

                        self.route_target_value = YLeaf(YType.str, "route-target-value")

                        self.saf_name = YLeaf(YType.enumeration, "saf-name")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("af_name",
                                        "route_target_type",
                                        "route_target_value",
                                        "saf_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(L3Vpn.InvalidVrfs.InvalidVrf.Af.RouteTarget, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(L3Vpn.InvalidVrfs.InvalidVrf.Af.RouteTarget, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.af_name.is_set or
                            self.route_target_type.is_set or
                            self.route_target_value.is_set or
                            self.saf_name.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.af_name.yfilter != YFilter.not_set or
                            self.route_target_type.yfilter != YFilter.not_set or
                            self.route_target_value.yfilter != YFilter.not_set or
                            self.saf_name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "route-target" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.af_name.is_set or self.af_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.af_name.get_name_leafdata())
                        if (self.route_target_type.is_set or self.route_target_type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.route_target_type.get_name_leafdata())
                        if (self.route_target_value.is_set or self.route_target_value.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.route_target_value.get_name_leafdata())
                        if (self.saf_name.is_set or self.saf_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.saf_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "af-name" or name == "route-target-type" or name == "route-target-value" or name == "saf-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "af-name"):
                            self.af_name = value
                            self.af_name.value_namespace = name_space
                            self.af_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "route-target-type"):
                            self.route_target_type = value
                            self.route_target_type.value_namespace = name_space
                            self.route_target_type.value_namespace_prefix = name_space_prefix
                        if(value_path == "route-target-value"):
                            self.route_target_value = value
                            self.route_target_value.value_namespace = name_space
                            self.route_target_value.value_namespace_prefix = name_space_prefix
                        if(value_path == "saf-name"):
                            self.saf_name = value
                            self.saf_name.value_namespace = name_space
                            self.saf_name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.route_target:
                        if (c.has_data()):
                            return True
                    return (
                        self.af_name.is_set or
                        self.export_route_policy.is_set or
                        self.import_route_policy.is_set or
                        self.saf_name.is_set)

                def has_operation(self):
                    for c in self.route_target:
                        if (c.has_operation()):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.af_name.yfilter != YFilter.not_set or
                        self.export_route_policy.yfilter != YFilter.not_set or
                        self.import_route_policy.yfilter != YFilter.not_set or
                        self.saf_name.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "af" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.af_name.is_set or self.af_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.af_name.get_name_leafdata())
                    if (self.export_route_policy.is_set or self.export_route_policy.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.export_route_policy.get_name_leafdata())
                    if (self.import_route_policy.is_set or self.import_route_policy.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.import_route_policy.get_name_leafdata())
                    if (self.saf_name.is_set or self.saf_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.saf_name.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "route-target"):
                        for c in self.route_target:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = L3Vpn.InvalidVrfs.InvalidVrf.Af.RouteTarget()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.route_target.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "route-target" or name == "af-name" or name == "export-route-policy" or name == "import-route-policy" or name == "saf-name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "af-name"):
                        self.af_name = value
                        self.af_name.value_namespace = name_space
                        self.af_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "export-route-policy"):
                        self.export_route_policy = value
                        self.export_route_policy.value_namespace = name_space
                        self.export_route_policy.value_namespace_prefix = name_space_prefix
                    if(value_path == "import-route-policy"):
                        self.import_route_policy = value
                        self.import_route_policy.value_namespace = name_space
                        self.import_route_policy.value_namespace_prefix = name_space_prefix
                    if(value_path == "saf-name"):
                        self.saf_name = value
                        self.saf_name.value_namespace = name_space
                        self.saf_name.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.af:
                    if (c.has_data()):
                        return True
                for c in self.interface:
                    if (c.has_data()):
                        return True
                return (
                    self.vrf_name.is_set or
                    self.is_big_vrf.is_set or
                    self.route_distinguisher.is_set or
                    self.vrf_description.is_set or
                    self.vrf_name_xr.is_set)

            def has_operation(self):
                for c in self.af:
                    if (c.has_operation()):
                        return True
                for c in self.interface:
                    if (c.has_operation()):
                        return True
                return (
                    self.yfilter != YFilter.not_set or
                    self.vrf_name.yfilter != YFilter.not_set or
                    self.is_big_vrf.yfilter != YFilter.not_set or
                    self.route_distinguisher.yfilter != YFilter.not_set or
                    self.vrf_description.yfilter != YFilter.not_set or
                    self.vrf_name_xr.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "invalid-vrf" + "[vrf-name='" + self.vrf_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-mpls-vpn-oper:l3vpn/invalid-vrfs/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vrf_name.get_name_leafdata())
                if (self.is_big_vrf.is_set or self.is_big_vrf.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.is_big_vrf.get_name_leafdata())
                if (self.route_distinguisher.is_set or self.route_distinguisher.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.route_distinguisher.get_name_leafdata())
                if (self.vrf_description.is_set or self.vrf_description.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vrf_description.get_name_leafdata())
                if (self.vrf_name_xr.is_set or self.vrf_name_xr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vrf_name_xr.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "af"):
                    for c in self.af:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = L3Vpn.InvalidVrfs.InvalidVrf.Af()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.af.append(c)
                    return c

                if (child_yang_name == "interface"):
                    for c in self.interface:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = L3Vpn.InvalidVrfs.InvalidVrf.Interface()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.interface.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "af" or name == "interface" or name == "vrf-name" or name == "is-big-vrf" or name == "route-distinguisher" or name == "vrf-description" or name == "vrf-name-xr"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "vrf-name"):
                    self.vrf_name = value
                    self.vrf_name.value_namespace = name_space
                    self.vrf_name.value_namespace_prefix = name_space_prefix
                if(value_path == "is-big-vrf"):
                    self.is_big_vrf = value
                    self.is_big_vrf.value_namespace = name_space
                    self.is_big_vrf.value_namespace_prefix = name_space_prefix
                if(value_path == "route-distinguisher"):
                    self.route_distinguisher = value
                    self.route_distinguisher.value_namespace = name_space
                    self.route_distinguisher.value_namespace_prefix = name_space_prefix
                if(value_path == "vrf-description"):
                    self.vrf_description = value
                    self.vrf_description.value_namespace = name_space
                    self.vrf_description.value_namespace_prefix = name_space_prefix
                if(value_path == "vrf-name-xr"):
                    self.vrf_name_xr = value
                    self.vrf_name_xr.value_namespace = name_space
                    self.vrf_name_xr.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.invalid_vrf:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.invalid_vrf:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "invalid-vrfs" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-mpls-vpn-oper:l3vpn/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "invalid-vrf"):
                for c in self.invalid_vrf:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = L3Vpn.InvalidVrfs.InvalidVrf()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.invalid_vrf.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "invalid-vrf"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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

            self.vrf = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(L3Vpn.Vrfs, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(L3Vpn.Vrfs, self).__setattr__(name, value)


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

                self.vrf_name = YLeaf(YType.str, "vrf-name")

                self.is_big_vrf = YLeaf(YType.boolean, "is-big-vrf")

                self.route_distinguisher = YLeaf(YType.str, "route-distinguisher")

                self.vrf_description = YLeaf(YType.str, "vrf-description")

                self.vrf_name_xr = YLeaf(YType.str, "vrf-name-xr")

                self.af = YList(self)
                self.interface = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("vrf_name",
                                "is_big_vrf",
                                "route_distinguisher",
                                "vrf_description",
                                "vrf_name_xr") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(L3Vpn.Vrfs.Vrf, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(L3Vpn.Vrfs.Vrf, self).__setattr__(name, value)


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

                    self.interface_name = YLeaf(YType.str, "interface-name")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("interface_name") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(L3Vpn.Vrfs.Vrf.Interface, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(L3Vpn.Vrfs.Vrf.Interface, self).__setattr__(name, value)

                def has_data(self):
                    return self.interface_name.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.interface_name.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "interface" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.interface_name.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "interface-name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "interface-name"):
                        self.interface_name = value
                        self.interface_name.value_namespace = name_space
                        self.interface_name.value_namespace_prefix = name_space_prefix


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

                    self.af_name = YLeaf(YType.enumeration, "af-name")

                    self.export_route_policy = YLeaf(YType.str, "export-route-policy")

                    self.import_route_policy = YLeaf(YType.str, "import-route-policy")

                    self.saf_name = YLeaf(YType.enumeration, "saf-name")

                    self.route_target = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("af_name",
                                    "export_route_policy",
                                    "import_route_policy",
                                    "saf_name") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(L3Vpn.Vrfs.Vrf.Af, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(L3Vpn.Vrfs.Vrf.Af, self).__setattr__(name, value)


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

                        self.af_name = YLeaf(YType.enumeration, "af-name")

                        self.route_target_type = YLeaf(YType.enumeration, "route-target-type")

                        self.route_target_value = YLeaf(YType.str, "route-target-value")

                        self.saf_name = YLeaf(YType.enumeration, "saf-name")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("af_name",
                                        "route_target_type",
                                        "route_target_value",
                                        "saf_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(L3Vpn.Vrfs.Vrf.Af.RouteTarget, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(L3Vpn.Vrfs.Vrf.Af.RouteTarget, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.af_name.is_set or
                            self.route_target_type.is_set or
                            self.route_target_value.is_set or
                            self.saf_name.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.af_name.yfilter != YFilter.not_set or
                            self.route_target_type.yfilter != YFilter.not_set or
                            self.route_target_value.yfilter != YFilter.not_set or
                            self.saf_name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "route-target" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.af_name.is_set or self.af_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.af_name.get_name_leafdata())
                        if (self.route_target_type.is_set or self.route_target_type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.route_target_type.get_name_leafdata())
                        if (self.route_target_value.is_set or self.route_target_value.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.route_target_value.get_name_leafdata())
                        if (self.saf_name.is_set or self.saf_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.saf_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "af-name" or name == "route-target-type" or name == "route-target-value" or name == "saf-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "af-name"):
                            self.af_name = value
                            self.af_name.value_namespace = name_space
                            self.af_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "route-target-type"):
                            self.route_target_type = value
                            self.route_target_type.value_namespace = name_space
                            self.route_target_type.value_namespace_prefix = name_space_prefix
                        if(value_path == "route-target-value"):
                            self.route_target_value = value
                            self.route_target_value.value_namespace = name_space
                            self.route_target_value.value_namespace_prefix = name_space_prefix
                        if(value_path == "saf-name"):
                            self.saf_name = value
                            self.saf_name.value_namespace = name_space
                            self.saf_name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.route_target:
                        if (c.has_data()):
                            return True
                    return (
                        self.af_name.is_set or
                        self.export_route_policy.is_set or
                        self.import_route_policy.is_set or
                        self.saf_name.is_set)

                def has_operation(self):
                    for c in self.route_target:
                        if (c.has_operation()):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.af_name.yfilter != YFilter.not_set or
                        self.export_route_policy.yfilter != YFilter.not_set or
                        self.import_route_policy.yfilter != YFilter.not_set or
                        self.saf_name.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "af" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.af_name.is_set or self.af_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.af_name.get_name_leafdata())
                    if (self.export_route_policy.is_set or self.export_route_policy.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.export_route_policy.get_name_leafdata())
                    if (self.import_route_policy.is_set or self.import_route_policy.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.import_route_policy.get_name_leafdata())
                    if (self.saf_name.is_set or self.saf_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.saf_name.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "route-target"):
                        for c in self.route_target:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = L3Vpn.Vrfs.Vrf.Af.RouteTarget()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.route_target.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "route-target" or name == "af-name" or name == "export-route-policy" or name == "import-route-policy" or name == "saf-name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "af-name"):
                        self.af_name = value
                        self.af_name.value_namespace = name_space
                        self.af_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "export-route-policy"):
                        self.export_route_policy = value
                        self.export_route_policy.value_namespace = name_space
                        self.export_route_policy.value_namespace_prefix = name_space_prefix
                    if(value_path == "import-route-policy"):
                        self.import_route_policy = value
                        self.import_route_policy.value_namespace = name_space
                        self.import_route_policy.value_namespace_prefix = name_space_prefix
                    if(value_path == "saf-name"):
                        self.saf_name = value
                        self.saf_name.value_namespace = name_space
                        self.saf_name.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.af:
                    if (c.has_data()):
                        return True
                for c in self.interface:
                    if (c.has_data()):
                        return True
                return (
                    self.vrf_name.is_set or
                    self.is_big_vrf.is_set or
                    self.route_distinguisher.is_set or
                    self.vrf_description.is_set or
                    self.vrf_name_xr.is_set)

            def has_operation(self):
                for c in self.af:
                    if (c.has_operation()):
                        return True
                for c in self.interface:
                    if (c.has_operation()):
                        return True
                return (
                    self.yfilter != YFilter.not_set or
                    self.vrf_name.yfilter != YFilter.not_set or
                    self.is_big_vrf.yfilter != YFilter.not_set or
                    self.route_distinguisher.yfilter != YFilter.not_set or
                    self.vrf_description.yfilter != YFilter.not_set or
                    self.vrf_name_xr.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "vrf" + "[vrf-name='" + self.vrf_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-mpls-vpn-oper:l3vpn/vrfs/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vrf_name.get_name_leafdata())
                if (self.is_big_vrf.is_set or self.is_big_vrf.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.is_big_vrf.get_name_leafdata())
                if (self.route_distinguisher.is_set or self.route_distinguisher.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.route_distinguisher.get_name_leafdata())
                if (self.vrf_description.is_set or self.vrf_description.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vrf_description.get_name_leafdata())
                if (self.vrf_name_xr.is_set or self.vrf_name_xr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vrf_name_xr.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "af"):
                    for c in self.af:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = L3Vpn.Vrfs.Vrf.Af()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.af.append(c)
                    return c

                if (child_yang_name == "interface"):
                    for c in self.interface:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = L3Vpn.Vrfs.Vrf.Interface()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.interface.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "af" or name == "interface" or name == "vrf-name" or name == "is-big-vrf" or name == "route-distinguisher" or name == "vrf-description" or name == "vrf-name-xr"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "vrf-name"):
                    self.vrf_name = value
                    self.vrf_name.value_namespace = name_space
                    self.vrf_name.value_namespace_prefix = name_space_prefix
                if(value_path == "is-big-vrf"):
                    self.is_big_vrf = value
                    self.is_big_vrf.value_namespace = name_space
                    self.is_big_vrf.value_namespace_prefix = name_space_prefix
                if(value_path == "route-distinguisher"):
                    self.route_distinguisher = value
                    self.route_distinguisher.value_namespace = name_space
                    self.route_distinguisher.value_namespace_prefix = name_space_prefix
                if(value_path == "vrf-description"):
                    self.vrf_description = value
                    self.vrf_description.value_namespace = name_space
                    self.vrf_description.value_namespace_prefix = name_space_prefix
                if(value_path == "vrf-name-xr"):
                    self.vrf_name_xr = value
                    self.vrf_name_xr.value_namespace = name_space
                    self.vrf_name_xr.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.vrf:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.vrf:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "vrfs" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-mpls-vpn-oper:l3vpn/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "vrf"):
                for c in self.vrf:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = L3Vpn.Vrfs.Vrf()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.vrf.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "vrf"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.invalid_vrfs is not None and self.invalid_vrfs.has_data()) or
            (self.vrfs is not None and self.vrfs.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.invalid_vrfs is not None and self.invalid_vrfs.has_operation()) or
            (self.vrfs is not None and self.vrfs.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-mpls-vpn-oper:l3vpn" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "invalid-vrfs"):
            if (self.invalid_vrfs is None):
                self.invalid_vrfs = L3Vpn.InvalidVrfs()
                self.invalid_vrfs.parent = self
                self._children_name_map["invalid_vrfs"] = "invalid-vrfs"
            return self.invalid_vrfs

        if (child_yang_name == "vrfs"):
            if (self.vrfs is None):
                self.vrfs = L3Vpn.Vrfs()
                self.vrfs.parent = self
                self._children_name_map["vrfs"] = "vrfs"
            return self.vrfs

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "invalid-vrfs" or name == "vrfs"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = L3Vpn()
        return self._top_entity

