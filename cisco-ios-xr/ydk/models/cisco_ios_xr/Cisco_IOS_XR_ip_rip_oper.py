""" Cisco_IOS_XR_ip_rip_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-rip package operational data.

This module contains definitions
for the following management objects\:
  rip\: RIP operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class InterfaceState(Enum):
    """
    InterfaceState

    Interface state

    .. data:: interface_none = 0

    	Interface does not exist

    .. data:: interface_down = 1

    	Interface exists but IP is down

    .. data:: interface_up = 2

    	Interface exists and IP is up

    .. data:: interface_unknown = 3

    	Unknown state

    """

    interface_none = Enum.YLeaf(0, "interface-none")

    interface_down = Enum.YLeaf(1, "interface-down")

    interface_up = Enum.YLeaf(2, "interface-up")

    interface_unknown = Enum.YLeaf(3, "interface-unknown")


class RipRouteOrigin(Enum):
    """
    RipRouteOrigin

    Rip route origin

    .. data:: rip_rt_org_runover = 0

    	configured 'network'

    .. data:: rip_rt_org_redist = 1

    	redistributed

    .. data:: rip_rt_org_auto_summary = 2

    	auto summary

    .. data:: rip_rt_org_rip = 3

    	learned via RIP

    .. data:: rip_rt_org_intsummary = 4

    	interface summary-address

    .. data:: rip_rt_org_unused = 5

    	route stay in for triggered rip

    """

    rip_rt_org_runover = Enum.YLeaf(0, "rip-rt-org-runover")

    rip_rt_org_redist = Enum.YLeaf(1, "rip-rt-org-redist")

    rip_rt_org_auto_summary = Enum.YLeaf(2, "rip-rt-org-auto-summary")

    rip_rt_org_rip = Enum.YLeaf(3, "rip-rt-org-rip")

    rip_rt_org_intsummary = Enum.YLeaf(4, "rip-rt-org-intsummary")

    rip_rt_org_unused = Enum.YLeaf(5, "rip-rt-org-unused")



class Rip(Entity):
    """
    RIP operational data
    
    .. attribute:: default_vrf
    
    	RIP operational data for Default VRF
    	**type**\:   :py:class:`DefaultVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.DefaultVrf>`
    
    .. attribute:: protocol
    
    	Protocol operational data
    	**type**\:   :py:class:`Protocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Protocol>`
    
    .. attribute:: vrfs
    
    	VRF related operational data
    	**type**\:   :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Vrfs>`
    
    

    """

    _prefix = 'ip-rip-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Rip, self).__init__()
        self._top_entity = None

        self.yang_name = "rip"
        self.yang_parent_name = "Cisco-IOS-XR-ip-rip-oper"

        self.default_vrf = Rip.DefaultVrf()
        self.default_vrf.parent = self
        self._children_name_map["default_vrf"] = "default-vrf"
        self._children_yang_names.add("default-vrf")

        self.protocol = Rip.Protocol()
        self.protocol.parent = self
        self._children_name_map["protocol"] = "protocol"
        self._children_yang_names.add("protocol")

        self.vrfs = Rip.Vrfs()
        self.vrfs.parent = self
        self._children_name_map["vrfs"] = "vrfs"
        self._children_yang_names.add("vrfs")


    class Vrfs(Entity):
        """
        VRF related operational data
        
        .. attribute:: vrf
        
        	Operational data for a particular VRF
        	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Vrfs.Vrf>`
        
        

        """

        _prefix = 'ip-rip-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Rip.Vrfs, self).__init__()

            self.yang_name = "vrfs"
            self.yang_parent_name = "rip"

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
                        super(Rip.Vrfs, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Rip.Vrfs, self).__setattr__(name, value)


        class Vrf(Entity):
            """
            Operational data for a particular VRF
            
            .. attribute:: vrf_name  <key>
            
            	Name of the VRF
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: configuration
            
            	RIP global configuration
            	**type**\:   :py:class:`Configuration <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Vrfs.Vrf.Configuration>`
            
            .. attribute:: global_
            
            	Global Information 
            	**type**\:   :py:class:`Global_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Vrfs.Vrf.Global_>`
            
            .. attribute:: interfaces
            
            	RIP interfaces
            	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Vrfs.Vrf.Interfaces>`
            
            .. attribute:: routes
            
            	RIP route database
            	**type**\:   :py:class:`Routes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Vrfs.Vrf.Routes>`
            
            .. attribute:: statistics
            
            	RIP statistics information
            	**type**\:   :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Vrfs.Vrf.Statistics>`
            
            

            """

            _prefix = 'ip-rip-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Rip.Vrfs.Vrf, self).__init__()

                self.yang_name = "vrf"
                self.yang_parent_name = "vrfs"

                self.vrf_name = YLeaf(YType.str, "vrf-name")

                self.configuration = Rip.Vrfs.Vrf.Configuration()
                self.configuration.parent = self
                self._children_name_map["configuration"] = "configuration"
                self._children_yang_names.add("configuration")

                self.global_ = Rip.Vrfs.Vrf.Global_()
                self.global_.parent = self
                self._children_name_map["global_"] = "global"
                self._children_yang_names.add("global")

                self.interfaces = Rip.Vrfs.Vrf.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"
                self._children_yang_names.add("interfaces")

                self.routes = Rip.Vrfs.Vrf.Routes()
                self.routes.parent = self
                self._children_name_map["routes"] = "routes"
                self._children_yang_names.add("routes")

                self.statistics = Rip.Vrfs.Vrf.Statistics()
                self.statistics.parent = self
                self._children_name_map["statistics"] = "statistics"
                self._children_yang_names.add("statistics")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("vrf_name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Rip.Vrfs.Vrf, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Rip.Vrfs.Vrf, self).__setattr__(name, value)


            class Routes(Entity):
                """
                RIP route database
                
                .. attribute:: route
                
                	A route in the RIP database
                	**type**\: list of    :py:class:`Route <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Vrfs.Vrf.Routes.Route>`
                
                

                """

                _prefix = 'ip-rip-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rip.Vrfs.Vrf.Routes, self).__init__()

                    self.yang_name = "routes"
                    self.yang_parent_name = "vrf"

                    self.route = YList(self)

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
                                super(Rip.Vrfs.Vrf.Routes, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Rip.Vrfs.Vrf.Routes, self).__setattr__(name, value)


                class Route(Entity):
                    """
                    A route in the RIP database
                    
                    .. attribute:: active
                    
                    	Active route indicator
                    	**type**\:  bool
                    
                    .. attribute:: attributes
                    
                    	RIB supplied route attributes
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: bgp_count
                    
                    	Hop count for this route
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: destination_address
                    
                    	Destination IP Address for this route
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: distance
                    
                    	Route administrative distance
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: hold_down
                    
                    	Indicates whether route is in holddown
                    	**type**\:  bool
                    
                    .. attribute:: path_origin
                    
                    	Where this route was learnt
                    	**type**\:   :py:class:`RipRouteOrigin <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.RipRouteOrigin>`
                    
                    .. attribute:: paths
                    
                    	The paths for this route
                    	**type**\: list of    :py:class:`Paths <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Vrfs.Vrf.Routes.Route.Paths>`
                    
                    .. attribute:: prefix
                    
                    	Network prefix
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: prefix_length
                    
                    	Prefix length
                    	**type**\:  int
                    
                    	**range:** 0..32
                    
                    .. attribute:: prefix_length_xr
                    
                    	Prefix length of IP address
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: route_summary
                    
                    	Summary route placeholder indicator
                    	**type**\:  bool
                    
                    .. attribute:: route_tag
                    
                    	Generic route information
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: route_type
                    
                    	Type of this route
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: version
                    
                    	RIB supplied version number
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'ip-rip-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Rip.Vrfs.Vrf.Routes.Route, self).__init__()

                        self.yang_name = "route"
                        self.yang_parent_name = "routes"

                        self.active = YLeaf(YType.boolean, "active")

                        self.attributes = YLeaf(YType.uint32, "attributes")

                        self.bgp_count = YLeaf(YType.uint16, "bgp-count")

                        self.destination_address = YLeaf(YType.str, "destination-address")

                        self.distance = YLeaf(YType.uint16, "distance")

                        self.hold_down = YLeaf(YType.boolean, "hold-down")

                        self.path_origin = YLeaf(YType.enumeration, "path-origin")

                        self.prefix = YLeaf(YType.str, "prefix")

                        self.prefix_length = YLeaf(YType.uint32, "prefix-length")

                        self.prefix_length_xr = YLeaf(YType.uint32, "prefix-length-xr")

                        self.route_summary = YLeaf(YType.boolean, "route-summary")

                        self.route_tag = YLeaf(YType.uint16, "route-tag")

                        self.route_type = YLeaf(YType.uint16, "route-type")

                        self.version = YLeaf(YType.uint8, "version")

                        self.paths = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("active",
                                        "attributes",
                                        "bgp_count",
                                        "destination_address",
                                        "distance",
                                        "hold_down",
                                        "path_origin",
                                        "prefix",
                                        "prefix_length",
                                        "prefix_length_xr",
                                        "route_summary",
                                        "route_tag",
                                        "route_type",
                                        "version") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Rip.Vrfs.Vrf.Routes.Route, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Rip.Vrfs.Vrf.Routes.Route, self).__setattr__(name, value)


                    class Paths(Entity):
                        """
                        The paths for this route
                        
                        .. attribute:: interface
                        
                        	Interface
                        	**type**\:  str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        .. attribute:: is_permanent
                        
                        	Permanent indicator
                        	**type**\:  bool
                        
                        .. attribute:: metric
                        
                        	Metric
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: next_hop_address
                        
                        	Next hop address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: source_address
                        
                        	Source address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: tag
                        
                        	Tag
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: uptime
                        
                        	Up time
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ip-rip-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Rip.Vrfs.Vrf.Routes.Route.Paths, self).__init__()

                            self.yang_name = "paths"
                            self.yang_parent_name = "route"

                            self.interface = YLeaf(YType.str, "interface")

                            self.is_permanent = YLeaf(YType.boolean, "is-permanent")

                            self.metric = YLeaf(YType.uint16, "metric")

                            self.next_hop_address = YLeaf(YType.str, "next-hop-address")

                            self.source_address = YLeaf(YType.str, "source-address")

                            self.tag = YLeaf(YType.uint16, "tag")

                            self.uptime = YLeaf(YType.uint32, "uptime")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("interface",
                                            "is_permanent",
                                            "metric",
                                            "next_hop_address",
                                            "source_address",
                                            "tag",
                                            "uptime") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Rip.Vrfs.Vrf.Routes.Route.Paths, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Rip.Vrfs.Vrf.Routes.Route.Paths, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.interface.is_set or
                                self.is_permanent.is_set or
                                self.metric.is_set or
                                self.next_hop_address.is_set or
                                self.source_address.is_set or
                                self.tag.is_set or
                                self.uptime.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.interface.yfilter != YFilter.not_set or
                                self.is_permanent.yfilter != YFilter.not_set or
                                self.metric.yfilter != YFilter.not_set or
                                self.next_hop_address.yfilter != YFilter.not_set or
                                self.source_address.yfilter != YFilter.not_set or
                                self.tag.yfilter != YFilter.not_set or
                                self.uptime.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "paths" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.interface.is_set or self.interface.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.interface.get_name_leafdata())
                            if (self.is_permanent.is_set or self.is_permanent.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_permanent.get_name_leafdata())
                            if (self.metric.is_set or self.metric.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.metric.get_name_leafdata())
                            if (self.next_hop_address.is_set or self.next_hop_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.next_hop_address.get_name_leafdata())
                            if (self.source_address.is_set or self.source_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.source_address.get_name_leafdata())
                            if (self.tag.is_set or self.tag.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.tag.get_name_leafdata())
                            if (self.uptime.is_set or self.uptime.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.uptime.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "interface" or name == "is-permanent" or name == "metric" or name == "next-hop-address" or name == "source-address" or name == "tag" or name == "uptime"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "interface"):
                                self.interface = value
                                self.interface.value_namespace = name_space
                                self.interface.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-permanent"):
                                self.is_permanent = value
                                self.is_permanent.value_namespace = name_space
                                self.is_permanent.value_namespace_prefix = name_space_prefix
                            if(value_path == "metric"):
                                self.metric = value
                                self.metric.value_namespace = name_space
                                self.metric.value_namespace_prefix = name_space_prefix
                            if(value_path == "next-hop-address"):
                                self.next_hop_address = value
                                self.next_hop_address.value_namespace = name_space
                                self.next_hop_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "source-address"):
                                self.source_address = value
                                self.source_address.value_namespace = name_space
                                self.source_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "tag"):
                                self.tag = value
                                self.tag.value_namespace = name_space
                                self.tag.value_namespace_prefix = name_space_prefix
                            if(value_path == "uptime"):
                                self.uptime = value
                                self.uptime.value_namespace = name_space
                                self.uptime.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.paths:
                            if (c.has_data()):
                                return True
                        return (
                            self.active.is_set or
                            self.attributes.is_set or
                            self.bgp_count.is_set or
                            self.destination_address.is_set or
                            self.distance.is_set or
                            self.hold_down.is_set or
                            self.path_origin.is_set or
                            self.prefix.is_set or
                            self.prefix_length.is_set or
                            self.prefix_length_xr.is_set or
                            self.route_summary.is_set or
                            self.route_tag.is_set or
                            self.route_type.is_set or
                            self.version.is_set)

                    def has_operation(self):
                        for c in self.paths:
                            if (c.has_operation()):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.active.yfilter != YFilter.not_set or
                            self.attributes.yfilter != YFilter.not_set or
                            self.bgp_count.yfilter != YFilter.not_set or
                            self.destination_address.yfilter != YFilter.not_set or
                            self.distance.yfilter != YFilter.not_set or
                            self.hold_down.yfilter != YFilter.not_set or
                            self.path_origin.yfilter != YFilter.not_set or
                            self.prefix.yfilter != YFilter.not_set or
                            self.prefix_length.yfilter != YFilter.not_set or
                            self.prefix_length_xr.yfilter != YFilter.not_set or
                            self.route_summary.yfilter != YFilter.not_set or
                            self.route_tag.yfilter != YFilter.not_set or
                            self.route_type.yfilter != YFilter.not_set or
                            self.version.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "route" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.active.is_set or self.active.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.active.get_name_leafdata())
                        if (self.attributes.is_set or self.attributes.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.attributes.get_name_leafdata())
                        if (self.bgp_count.is_set or self.bgp_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.bgp_count.get_name_leafdata())
                        if (self.destination_address.is_set or self.destination_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.destination_address.get_name_leafdata())
                        if (self.distance.is_set or self.distance.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.distance.get_name_leafdata())
                        if (self.hold_down.is_set or self.hold_down.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.hold_down.get_name_leafdata())
                        if (self.path_origin.is_set or self.path_origin.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.path_origin.get_name_leafdata())
                        if (self.prefix.is_set or self.prefix.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.prefix.get_name_leafdata())
                        if (self.prefix_length.is_set or self.prefix_length.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.prefix_length.get_name_leafdata())
                        if (self.prefix_length_xr.is_set or self.prefix_length_xr.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.prefix_length_xr.get_name_leafdata())
                        if (self.route_summary.is_set or self.route_summary.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.route_summary.get_name_leafdata())
                        if (self.route_tag.is_set or self.route_tag.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.route_tag.get_name_leafdata())
                        if (self.route_type.is_set or self.route_type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.route_type.get_name_leafdata())
                        if (self.version.is_set or self.version.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.version.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "paths"):
                            for c in self.paths:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Rip.Vrfs.Vrf.Routes.Route.Paths()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.paths.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "paths" or name == "active" or name == "attributes" or name == "bgp-count" or name == "destination-address" or name == "distance" or name == "hold-down" or name == "path-origin" or name == "prefix" or name == "prefix-length" or name == "prefix-length-xr" or name == "route-summary" or name == "route-tag" or name == "route-type" or name == "version"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "active"):
                            self.active = value
                            self.active.value_namespace = name_space
                            self.active.value_namespace_prefix = name_space_prefix
                        if(value_path == "attributes"):
                            self.attributes = value
                            self.attributes.value_namespace = name_space
                            self.attributes.value_namespace_prefix = name_space_prefix
                        if(value_path == "bgp-count"):
                            self.bgp_count = value
                            self.bgp_count.value_namespace = name_space
                            self.bgp_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "destination-address"):
                            self.destination_address = value
                            self.destination_address.value_namespace = name_space
                            self.destination_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "distance"):
                            self.distance = value
                            self.distance.value_namespace = name_space
                            self.distance.value_namespace_prefix = name_space_prefix
                        if(value_path == "hold-down"):
                            self.hold_down = value
                            self.hold_down.value_namespace = name_space
                            self.hold_down.value_namespace_prefix = name_space_prefix
                        if(value_path == "path-origin"):
                            self.path_origin = value
                            self.path_origin.value_namespace = name_space
                            self.path_origin.value_namespace_prefix = name_space_prefix
                        if(value_path == "prefix"):
                            self.prefix = value
                            self.prefix.value_namespace = name_space
                            self.prefix.value_namespace_prefix = name_space_prefix
                        if(value_path == "prefix-length"):
                            self.prefix_length = value
                            self.prefix_length.value_namespace = name_space
                            self.prefix_length.value_namespace_prefix = name_space_prefix
                        if(value_path == "prefix-length-xr"):
                            self.prefix_length_xr = value
                            self.prefix_length_xr.value_namespace = name_space
                            self.prefix_length_xr.value_namespace_prefix = name_space_prefix
                        if(value_path == "route-summary"):
                            self.route_summary = value
                            self.route_summary.value_namespace = name_space
                            self.route_summary.value_namespace_prefix = name_space_prefix
                        if(value_path == "route-tag"):
                            self.route_tag = value
                            self.route_tag.value_namespace = name_space
                            self.route_tag.value_namespace_prefix = name_space_prefix
                        if(value_path == "route-type"):
                            self.route_type = value
                            self.route_type.value_namespace = name_space
                            self.route_type.value_namespace_prefix = name_space_prefix
                        if(value_path == "version"):
                            self.version = value
                            self.version.value_namespace = name_space
                            self.version.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.route:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.route:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "routes" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "route"):
                        for c in self.route:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Rip.Vrfs.Vrf.Routes.Route()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.route.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "route"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Configuration(Entity):
                """
                RIP global configuration
                
                .. attribute:: active
                
                	VRF active indicator
                	**type**\:  bool
                
                .. attribute:: auto_summarize
                
                	Auto\-summarization indicator
                	**type**\:  bool
                
                .. attribute:: default_metric
                
                	Default metric for RIP routes
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: flash_threshold
                
                	Flash update threshold
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: flush_timer
                
                	Flush timer
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: hold_down_timer
                
                	Holddown timer
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: input_q_length
                
                	Length of the input queue
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: invalid_timer
                
                	Invalid timer
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: maximum_paths
                
                	Maximum number of paths a route can have
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: multicast_address
                
                	Use broadcast/multicast address indicator
                	**type**\:  bool
                
                .. attribute:: next_update_time
                
                	Time left for next update
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: nsf_life_time
                
                	NSF life time
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: nsf_status
                
                	NSF Enable status
                	**type**\:  bool
                
                .. attribute:: oom_flags
                
                	Out\-of\-memory status flags
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: rip_version
                
                	Version of RIP configured
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: triggered_rip
                
                	Triggered RIP enabled indicator
                	**type**\:  bool
                
                .. attribute:: update_timer
                
                	Update timer
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: validation_indicator
                
                	Incoming packet source validation indicator
                	**type**\:  bool
                
                .. attribute:: vr_fised_socket
                
                	VRF added to socket indicator
                	**type**\:  bool
                
                

                """

                _prefix = 'ip-rip-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rip.Vrfs.Vrf.Configuration, self).__init__()

                    self.yang_name = "configuration"
                    self.yang_parent_name = "vrf"

                    self.active = YLeaf(YType.boolean, "active")

                    self.auto_summarize = YLeaf(YType.boolean, "auto-summarize")

                    self.default_metric = YLeaf(YType.uint8, "default-metric")

                    self.flash_threshold = YLeaf(YType.uint8, "flash-threshold")

                    self.flush_timer = YLeaf(YType.uint32, "flush-timer")

                    self.hold_down_timer = YLeaf(YType.uint32, "hold-down-timer")

                    self.input_q_length = YLeaf(YType.uint16, "input-q-length")

                    self.invalid_timer = YLeaf(YType.uint32, "invalid-timer")

                    self.maximum_paths = YLeaf(YType.uint8, "maximum-paths")

                    self.multicast_address = YLeaf(YType.boolean, "multicast-address")

                    self.next_update_time = YLeaf(YType.uint32, "next-update-time")

                    self.nsf_life_time = YLeaf(YType.uint32, "nsf-life-time")

                    self.nsf_status = YLeaf(YType.boolean, "nsf-status")

                    self.oom_flags = YLeaf(YType.uint32, "oom-flags")

                    self.rip_version = YLeaf(YType.int32, "rip-version")

                    self.triggered_rip = YLeaf(YType.boolean, "triggered-rip")

                    self.update_timer = YLeaf(YType.uint32, "update-timer")

                    self.validation_indicator = YLeaf(YType.boolean, "validation-indicator")

                    self.vr_fised_socket = YLeaf(YType.boolean, "vr-fised-socket")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("active",
                                    "auto_summarize",
                                    "default_metric",
                                    "flash_threshold",
                                    "flush_timer",
                                    "hold_down_timer",
                                    "input_q_length",
                                    "invalid_timer",
                                    "maximum_paths",
                                    "multicast_address",
                                    "next_update_time",
                                    "nsf_life_time",
                                    "nsf_status",
                                    "oom_flags",
                                    "rip_version",
                                    "triggered_rip",
                                    "update_timer",
                                    "validation_indicator",
                                    "vr_fised_socket") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Rip.Vrfs.Vrf.Configuration, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Rip.Vrfs.Vrf.Configuration, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.active.is_set or
                        self.auto_summarize.is_set or
                        self.default_metric.is_set or
                        self.flash_threshold.is_set or
                        self.flush_timer.is_set or
                        self.hold_down_timer.is_set or
                        self.input_q_length.is_set or
                        self.invalid_timer.is_set or
                        self.maximum_paths.is_set or
                        self.multicast_address.is_set or
                        self.next_update_time.is_set or
                        self.nsf_life_time.is_set or
                        self.nsf_status.is_set or
                        self.oom_flags.is_set or
                        self.rip_version.is_set or
                        self.triggered_rip.is_set or
                        self.update_timer.is_set or
                        self.validation_indicator.is_set or
                        self.vr_fised_socket.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.active.yfilter != YFilter.not_set or
                        self.auto_summarize.yfilter != YFilter.not_set or
                        self.default_metric.yfilter != YFilter.not_set or
                        self.flash_threshold.yfilter != YFilter.not_set or
                        self.flush_timer.yfilter != YFilter.not_set or
                        self.hold_down_timer.yfilter != YFilter.not_set or
                        self.input_q_length.yfilter != YFilter.not_set or
                        self.invalid_timer.yfilter != YFilter.not_set or
                        self.maximum_paths.yfilter != YFilter.not_set or
                        self.multicast_address.yfilter != YFilter.not_set or
                        self.next_update_time.yfilter != YFilter.not_set or
                        self.nsf_life_time.yfilter != YFilter.not_set or
                        self.nsf_status.yfilter != YFilter.not_set or
                        self.oom_flags.yfilter != YFilter.not_set or
                        self.rip_version.yfilter != YFilter.not_set or
                        self.triggered_rip.yfilter != YFilter.not_set or
                        self.update_timer.yfilter != YFilter.not_set or
                        self.validation_indicator.yfilter != YFilter.not_set or
                        self.vr_fised_socket.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "configuration" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.active.is_set or self.active.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.active.get_name_leafdata())
                    if (self.auto_summarize.is_set or self.auto_summarize.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.auto_summarize.get_name_leafdata())
                    if (self.default_metric.is_set or self.default_metric.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.default_metric.get_name_leafdata())
                    if (self.flash_threshold.is_set or self.flash_threshold.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.flash_threshold.get_name_leafdata())
                    if (self.flush_timer.is_set or self.flush_timer.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.flush_timer.get_name_leafdata())
                    if (self.hold_down_timer.is_set or self.hold_down_timer.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.hold_down_timer.get_name_leafdata())
                    if (self.input_q_length.is_set or self.input_q_length.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.input_q_length.get_name_leafdata())
                    if (self.invalid_timer.is_set or self.invalid_timer.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.invalid_timer.get_name_leafdata())
                    if (self.maximum_paths.is_set or self.maximum_paths.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.maximum_paths.get_name_leafdata())
                    if (self.multicast_address.is_set or self.multicast_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.multicast_address.get_name_leafdata())
                    if (self.next_update_time.is_set or self.next_update_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.next_update_time.get_name_leafdata())
                    if (self.nsf_life_time.is_set or self.nsf_life_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.nsf_life_time.get_name_leafdata())
                    if (self.nsf_status.is_set or self.nsf_status.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.nsf_status.get_name_leafdata())
                    if (self.oom_flags.is_set or self.oom_flags.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.oom_flags.get_name_leafdata())
                    if (self.rip_version.is_set or self.rip_version.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rip_version.get_name_leafdata())
                    if (self.triggered_rip.is_set or self.triggered_rip.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.triggered_rip.get_name_leafdata())
                    if (self.update_timer.is_set or self.update_timer.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.update_timer.get_name_leafdata())
                    if (self.validation_indicator.is_set or self.validation_indicator.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.validation_indicator.get_name_leafdata())
                    if (self.vr_fised_socket.is_set or self.vr_fised_socket.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.vr_fised_socket.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "active" or name == "auto-summarize" or name == "default-metric" or name == "flash-threshold" or name == "flush-timer" or name == "hold-down-timer" or name == "input-q-length" or name == "invalid-timer" or name == "maximum-paths" or name == "multicast-address" or name == "next-update-time" or name == "nsf-life-time" or name == "nsf-status" or name == "oom-flags" or name == "rip-version" or name == "triggered-rip" or name == "update-timer" or name == "validation-indicator" or name == "vr-fised-socket"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "active"):
                        self.active = value
                        self.active.value_namespace = name_space
                        self.active.value_namespace_prefix = name_space_prefix
                    if(value_path == "auto-summarize"):
                        self.auto_summarize = value
                        self.auto_summarize.value_namespace = name_space
                        self.auto_summarize.value_namespace_prefix = name_space_prefix
                    if(value_path == "default-metric"):
                        self.default_metric = value
                        self.default_metric.value_namespace = name_space
                        self.default_metric.value_namespace_prefix = name_space_prefix
                    if(value_path == "flash-threshold"):
                        self.flash_threshold = value
                        self.flash_threshold.value_namespace = name_space
                        self.flash_threshold.value_namespace_prefix = name_space_prefix
                    if(value_path == "flush-timer"):
                        self.flush_timer = value
                        self.flush_timer.value_namespace = name_space
                        self.flush_timer.value_namespace_prefix = name_space_prefix
                    if(value_path == "hold-down-timer"):
                        self.hold_down_timer = value
                        self.hold_down_timer.value_namespace = name_space
                        self.hold_down_timer.value_namespace_prefix = name_space_prefix
                    if(value_path == "input-q-length"):
                        self.input_q_length = value
                        self.input_q_length.value_namespace = name_space
                        self.input_q_length.value_namespace_prefix = name_space_prefix
                    if(value_path == "invalid-timer"):
                        self.invalid_timer = value
                        self.invalid_timer.value_namespace = name_space
                        self.invalid_timer.value_namespace_prefix = name_space_prefix
                    if(value_path == "maximum-paths"):
                        self.maximum_paths = value
                        self.maximum_paths.value_namespace = name_space
                        self.maximum_paths.value_namespace_prefix = name_space_prefix
                    if(value_path == "multicast-address"):
                        self.multicast_address = value
                        self.multicast_address.value_namespace = name_space
                        self.multicast_address.value_namespace_prefix = name_space_prefix
                    if(value_path == "next-update-time"):
                        self.next_update_time = value
                        self.next_update_time.value_namespace = name_space
                        self.next_update_time.value_namespace_prefix = name_space_prefix
                    if(value_path == "nsf-life-time"):
                        self.nsf_life_time = value
                        self.nsf_life_time.value_namespace = name_space
                        self.nsf_life_time.value_namespace_prefix = name_space_prefix
                    if(value_path == "nsf-status"):
                        self.nsf_status = value
                        self.nsf_status.value_namespace = name_space
                        self.nsf_status.value_namespace_prefix = name_space_prefix
                    if(value_path == "oom-flags"):
                        self.oom_flags = value
                        self.oom_flags.value_namespace = name_space
                        self.oom_flags.value_namespace_prefix = name_space_prefix
                    if(value_path == "rip-version"):
                        self.rip_version = value
                        self.rip_version.value_namespace = name_space
                        self.rip_version.value_namespace_prefix = name_space_prefix
                    if(value_path == "triggered-rip"):
                        self.triggered_rip = value
                        self.triggered_rip.value_namespace = name_space
                        self.triggered_rip.value_namespace_prefix = name_space_prefix
                    if(value_path == "update-timer"):
                        self.update_timer = value
                        self.update_timer.value_namespace = name_space
                        self.update_timer.value_namespace_prefix = name_space_prefix
                    if(value_path == "validation-indicator"):
                        self.validation_indicator = value
                        self.validation_indicator.value_namespace = name_space
                        self.validation_indicator.value_namespace_prefix = name_space_prefix
                    if(value_path == "vr-fised-socket"):
                        self.vr_fised_socket = value
                        self.vr_fised_socket.value_namespace = name_space
                        self.vr_fised_socket.value_namespace_prefix = name_space_prefix


            class Statistics(Entity):
                """
                RIP statistics information
                
                .. attribute:: discarded_packets
                
                	Total discarded packets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: discarded_routes
                
                	Total discarded routes
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: path_count
                
                	Number of paths allocated
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: path_malloc_failures
                
                	Number of failures to allocate memory for a path
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: periodic_updates
                
                	Number of periodic RIP updates
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: query_responses
                
                	Number of RIP queries responded to
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: received_packets
                
                	Total packets received
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: rib_updates
                
                	Number of route updates to RIB made by RIP
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: route_count
                
                	Number of routes allocated
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: route_malloc_failures
                
                	Number of failures to allocate memory for a route
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: sent_message_failures
                
                	Number of message send failures
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: sent_messages
                
                	Number of messages sent
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: standby_packets_received
                
                	Packets rx in SRP
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ip-rip-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rip.Vrfs.Vrf.Statistics, self).__init__()

                    self.yang_name = "statistics"
                    self.yang_parent_name = "vrf"

                    self.discarded_packets = YLeaf(YType.uint32, "discarded-packets")

                    self.discarded_routes = YLeaf(YType.uint32, "discarded-routes")

                    self.path_count = YLeaf(YType.uint32, "path-count")

                    self.path_malloc_failures = YLeaf(YType.uint32, "path-malloc-failures")

                    self.periodic_updates = YLeaf(YType.uint32, "periodic-updates")

                    self.query_responses = YLeaf(YType.uint32, "query-responses")

                    self.received_packets = YLeaf(YType.uint32, "received-packets")

                    self.rib_updates = YLeaf(YType.uint32, "rib-updates")

                    self.route_count = YLeaf(YType.uint32, "route-count")

                    self.route_malloc_failures = YLeaf(YType.uint32, "route-malloc-failures")

                    self.sent_message_failures = YLeaf(YType.uint32, "sent-message-failures")

                    self.sent_messages = YLeaf(YType.uint32, "sent-messages")

                    self.standby_packets_received = YLeaf(YType.uint32, "standby-packets-received")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("discarded_packets",
                                    "discarded_routes",
                                    "path_count",
                                    "path_malloc_failures",
                                    "periodic_updates",
                                    "query_responses",
                                    "received_packets",
                                    "rib_updates",
                                    "route_count",
                                    "route_malloc_failures",
                                    "sent_message_failures",
                                    "sent_messages",
                                    "standby_packets_received") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Rip.Vrfs.Vrf.Statistics, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Rip.Vrfs.Vrf.Statistics, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.discarded_packets.is_set or
                        self.discarded_routes.is_set or
                        self.path_count.is_set or
                        self.path_malloc_failures.is_set or
                        self.periodic_updates.is_set or
                        self.query_responses.is_set or
                        self.received_packets.is_set or
                        self.rib_updates.is_set or
                        self.route_count.is_set or
                        self.route_malloc_failures.is_set or
                        self.sent_message_failures.is_set or
                        self.sent_messages.is_set or
                        self.standby_packets_received.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.discarded_packets.yfilter != YFilter.not_set or
                        self.discarded_routes.yfilter != YFilter.not_set or
                        self.path_count.yfilter != YFilter.not_set or
                        self.path_malloc_failures.yfilter != YFilter.not_set or
                        self.periodic_updates.yfilter != YFilter.not_set or
                        self.query_responses.yfilter != YFilter.not_set or
                        self.received_packets.yfilter != YFilter.not_set or
                        self.rib_updates.yfilter != YFilter.not_set or
                        self.route_count.yfilter != YFilter.not_set or
                        self.route_malloc_failures.yfilter != YFilter.not_set or
                        self.sent_message_failures.yfilter != YFilter.not_set or
                        self.sent_messages.yfilter != YFilter.not_set or
                        self.standby_packets_received.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "statistics" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.discarded_packets.is_set or self.discarded_packets.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.discarded_packets.get_name_leafdata())
                    if (self.discarded_routes.is_set or self.discarded_routes.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.discarded_routes.get_name_leafdata())
                    if (self.path_count.is_set or self.path_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.path_count.get_name_leafdata())
                    if (self.path_malloc_failures.is_set or self.path_malloc_failures.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.path_malloc_failures.get_name_leafdata())
                    if (self.periodic_updates.is_set or self.periodic_updates.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.periodic_updates.get_name_leafdata())
                    if (self.query_responses.is_set or self.query_responses.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.query_responses.get_name_leafdata())
                    if (self.received_packets.is_set or self.received_packets.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.received_packets.get_name_leafdata())
                    if (self.rib_updates.is_set or self.rib_updates.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rib_updates.get_name_leafdata())
                    if (self.route_count.is_set or self.route_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.route_count.get_name_leafdata())
                    if (self.route_malloc_failures.is_set or self.route_malloc_failures.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.route_malloc_failures.get_name_leafdata())
                    if (self.sent_message_failures.is_set or self.sent_message_failures.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.sent_message_failures.get_name_leafdata())
                    if (self.sent_messages.is_set or self.sent_messages.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.sent_messages.get_name_leafdata())
                    if (self.standby_packets_received.is_set or self.standby_packets_received.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.standby_packets_received.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "discarded-packets" or name == "discarded-routes" or name == "path-count" or name == "path-malloc-failures" or name == "periodic-updates" or name == "query-responses" or name == "received-packets" or name == "rib-updates" or name == "route-count" or name == "route-malloc-failures" or name == "sent-message-failures" or name == "sent-messages" or name == "standby-packets-received"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "discarded-packets"):
                        self.discarded_packets = value
                        self.discarded_packets.value_namespace = name_space
                        self.discarded_packets.value_namespace_prefix = name_space_prefix
                    if(value_path == "discarded-routes"):
                        self.discarded_routes = value
                        self.discarded_routes.value_namespace = name_space
                        self.discarded_routes.value_namespace_prefix = name_space_prefix
                    if(value_path == "path-count"):
                        self.path_count = value
                        self.path_count.value_namespace = name_space
                        self.path_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "path-malloc-failures"):
                        self.path_malloc_failures = value
                        self.path_malloc_failures.value_namespace = name_space
                        self.path_malloc_failures.value_namespace_prefix = name_space_prefix
                    if(value_path == "periodic-updates"):
                        self.periodic_updates = value
                        self.periodic_updates.value_namespace = name_space
                        self.periodic_updates.value_namespace_prefix = name_space_prefix
                    if(value_path == "query-responses"):
                        self.query_responses = value
                        self.query_responses.value_namespace = name_space
                        self.query_responses.value_namespace_prefix = name_space_prefix
                    if(value_path == "received-packets"):
                        self.received_packets = value
                        self.received_packets.value_namespace = name_space
                        self.received_packets.value_namespace_prefix = name_space_prefix
                    if(value_path == "rib-updates"):
                        self.rib_updates = value
                        self.rib_updates.value_namespace = name_space
                        self.rib_updates.value_namespace_prefix = name_space_prefix
                    if(value_path == "route-count"):
                        self.route_count = value
                        self.route_count.value_namespace = name_space
                        self.route_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "route-malloc-failures"):
                        self.route_malloc_failures = value
                        self.route_malloc_failures.value_namespace = name_space
                        self.route_malloc_failures.value_namespace_prefix = name_space_prefix
                    if(value_path == "sent-message-failures"):
                        self.sent_message_failures = value
                        self.sent_message_failures.value_namespace = name_space
                        self.sent_message_failures.value_namespace_prefix = name_space_prefix
                    if(value_path == "sent-messages"):
                        self.sent_messages = value
                        self.sent_messages.value_namespace = name_space
                        self.sent_messages.value_namespace_prefix = name_space_prefix
                    if(value_path == "standby-packets-received"):
                        self.standby_packets_received = value
                        self.standby_packets_received.value_namespace = name_space
                        self.standby_packets_received.value_namespace_prefix = name_space_prefix


            class Interfaces(Entity):
                """
                RIP interfaces
                
                .. attribute:: interface
                
                	Information about a particular RIP interface
                	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Vrfs.Vrf.Interfaces.Interface>`
                
                

                """

                _prefix = 'ip-rip-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rip.Vrfs.Vrf.Interfaces, self).__init__()

                    self.yang_name = "interfaces"
                    self.yang_parent_name = "vrf"

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
                        if name in () and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Rip.Vrfs.Vrf.Interfaces, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Rip.Vrfs.Vrf.Interfaces, self).__setattr__(name, value)


                class Interface(Entity):
                    """
                    Information about a particular RIP interface
                    
                    .. attribute:: interface_name  <key>
                    
                    	Interface name
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: accept_metric
                    
                    	Accept routes of metric 0 indicator
                    	**type**\:  bool
                    
                    .. attribute:: auth_key_md5
                    
                    	Authentication key programmed with MD5 algorithm
                    	**type**\:  bool
                    
                    .. attribute:: auth_key_send_id
                    
                    	Current active Send Authentication Key Id
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: auth_keychain
                    
                    	Authentication Keychain Name
                    	**type**\:  str
                    
                    .. attribute:: auth_mode
                    
                    	Authentication Mode
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: destination_address
                    
                    	IP Address of this interface
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: if_handle
                    
                    	Interface handle
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: interface
                    
                    	Interface name
                    	**type**\:  str
                    
                    .. attribute:: is_passive_interface
                    
                    	Passive interface indicator
                    	**type**\:  bool
                    
                    .. attribute:: join_status
                    
                    	Multicast group join status
                    	**type**\:  bool
                    
                    .. attribute:: lpts_state
                    
                    	LPTSState
                    	**type**\:  bool
                    
                    .. attribute:: metric_cost
                    
                    	Cost added to routes through this interface
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: multicast_address
                    
                    	Use broadcast address for v2 packets
                    	**type**\:  bool
                    
                    .. attribute:: neighbor_address
                    
                    	Interface's triggered RIP neighbor
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: oom_flags
                    
                    	Out\-of\-memory status flags
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: pkt_accepted_valid_auth
                    
                    	Packets accepted with valid authentication data
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: pkt_drop_invalid_auth
                    
                    	Packets dropped due to invalid authentication data
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: pkt_drop_no_auth
                    
                    	Packets dropped due to missing authentication data
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: pkt_drop_wrong_kc
                    
                    	Packets dropped due to wrong keychain configured
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: poison_horizon
                    
                    	Poisoned reverse enabled indicator
                    	**type**\:  bool
                    
                    .. attribute:: prefix_length
                    
                    	Prefix length of the IP address
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: receive_version
                    
                    	Versions that the interface will recieve
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rip_enabled
                    
                    	Whether RIP is enabled on this interface
                    	**type**\:  bool
                    
                    .. attribute:: rip_peer
                    
                    	Neighbors on this interface
                    	**type**\: list of    :py:class:`RipPeer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Vrfs.Vrf.Interfaces.Interface.RipPeer>`
                    
                    .. attribute:: rip_summary
                    
                    	User defined summary addresses
                    	**type**\: list of    :py:class:`RipSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Vrfs.Vrf.Interfaces.Interface.RipSummary>`
                    
                    .. attribute:: send_auth_key_exists
                    
                    	Authentication send key exists
                    	**type**\:  bool
                    
                    .. attribute:: send_version
                    
                    	Versions that the interface is sending
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: split_horizon
                    
                    	Split horizon enabled indicator
                    	**type**\:  bool
                    
                    .. attribute:: state
                    
                    	Current state of the interface
                    	**type**\:   :py:class:`InterfaceState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.InterfaceState>`
                    
                    .. attribute:: total_pkt_recvd
                    
                    	Total packets received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: triggered_rip
                    
                    	Triggered RIP enabled indicator
                    	**type**\:  bool
                    
                    

                    """

                    _prefix = 'ip-rip-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Rip.Vrfs.Vrf.Interfaces.Interface, self).__init__()

                        self.yang_name = "interface"
                        self.yang_parent_name = "interfaces"

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.accept_metric = YLeaf(YType.boolean, "accept-metric")

                        self.auth_key_md5 = YLeaf(YType.boolean, "auth-key-md5")

                        self.auth_key_send_id = YLeaf(YType.uint64, "auth-key-send-id")

                        self.auth_keychain = YLeaf(YType.str, "auth-keychain")

                        self.auth_mode = YLeaf(YType.uint32, "auth-mode")

                        self.destination_address = YLeaf(YType.str, "destination-address")

                        self.if_handle = YLeaf(YType.str, "if-handle")

                        self.interface = YLeaf(YType.str, "interface")

                        self.is_passive_interface = YLeaf(YType.boolean, "is-passive-interface")

                        self.join_status = YLeaf(YType.boolean, "join-status")

                        self.lpts_state = YLeaf(YType.boolean, "lpts-state")

                        self.metric_cost = YLeaf(YType.uint32, "metric-cost")

                        self.multicast_address = YLeaf(YType.boolean, "multicast-address")

                        self.neighbor_address = YLeaf(YType.str, "neighbor-address")

                        self.oom_flags = YLeaf(YType.uint32, "oom-flags")

                        self.pkt_accepted_valid_auth = YLeaf(YType.uint32, "pkt-accepted-valid-auth")

                        self.pkt_drop_invalid_auth = YLeaf(YType.uint32, "pkt-drop-invalid-auth")

                        self.pkt_drop_no_auth = YLeaf(YType.uint32, "pkt-drop-no-auth")

                        self.pkt_drop_wrong_kc = YLeaf(YType.uint32, "pkt-drop-wrong-kc")

                        self.poison_horizon = YLeaf(YType.boolean, "poison-horizon")

                        self.prefix_length = YLeaf(YType.uint32, "prefix-length")

                        self.receive_version = YLeaf(YType.uint32, "receive-version")

                        self.rip_enabled = YLeaf(YType.boolean, "rip-enabled")

                        self.send_auth_key_exists = YLeaf(YType.boolean, "send-auth-key-exists")

                        self.send_version = YLeaf(YType.uint32, "send-version")

                        self.split_horizon = YLeaf(YType.boolean, "split-horizon")

                        self.state = YLeaf(YType.enumeration, "state")

                        self.total_pkt_recvd = YLeaf(YType.uint32, "total-pkt-recvd")

                        self.triggered_rip = YLeaf(YType.boolean, "triggered-rip")

                        self.rip_peer = YList(self)
                        self.rip_summary = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("interface_name",
                                        "accept_metric",
                                        "auth_key_md5",
                                        "auth_key_send_id",
                                        "auth_keychain",
                                        "auth_mode",
                                        "destination_address",
                                        "if_handle",
                                        "interface",
                                        "is_passive_interface",
                                        "join_status",
                                        "lpts_state",
                                        "metric_cost",
                                        "multicast_address",
                                        "neighbor_address",
                                        "oom_flags",
                                        "pkt_accepted_valid_auth",
                                        "pkt_drop_invalid_auth",
                                        "pkt_drop_no_auth",
                                        "pkt_drop_wrong_kc",
                                        "poison_horizon",
                                        "prefix_length",
                                        "receive_version",
                                        "rip_enabled",
                                        "send_auth_key_exists",
                                        "send_version",
                                        "split_horizon",
                                        "state",
                                        "total_pkt_recvd",
                                        "triggered_rip") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Rip.Vrfs.Vrf.Interfaces.Interface, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Rip.Vrfs.Vrf.Interfaces.Interface, self).__setattr__(name, value)


                    class RipSummary(Entity):
                        """
                        User defined summary addresses
                        
                        .. attribute:: metric
                        
                        	Summary metric
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: next_hop_address
                        
                        	Summary address next hop
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: prefix
                        
                        	Summary address prefix
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: prefix_length
                        
                        	Summary address prefix length
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ip-rip-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Rip.Vrfs.Vrf.Interfaces.Interface.RipSummary, self).__init__()

                            self.yang_name = "rip-summary"
                            self.yang_parent_name = "interface"

                            self.metric = YLeaf(YType.int32, "metric")

                            self.next_hop_address = YLeaf(YType.str, "next-hop-address")

                            self.prefix = YLeaf(YType.str, "prefix")

                            self.prefix_length = YLeaf(YType.uint32, "prefix-length")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("metric",
                                            "next_hop_address",
                                            "prefix",
                                            "prefix_length") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Rip.Vrfs.Vrf.Interfaces.Interface.RipSummary, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Rip.Vrfs.Vrf.Interfaces.Interface.RipSummary, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.metric.is_set or
                                self.next_hop_address.is_set or
                                self.prefix.is_set or
                                self.prefix_length.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.metric.yfilter != YFilter.not_set or
                                self.next_hop_address.yfilter != YFilter.not_set or
                                self.prefix.yfilter != YFilter.not_set or
                                self.prefix_length.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "rip-summary" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.metric.is_set or self.metric.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.metric.get_name_leafdata())
                            if (self.next_hop_address.is_set or self.next_hop_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.next_hop_address.get_name_leafdata())
                            if (self.prefix.is_set or self.prefix.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.prefix.get_name_leafdata())
                            if (self.prefix_length.is_set or self.prefix_length.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.prefix_length.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "metric" or name == "next-hop-address" or name == "prefix" or name == "prefix-length"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "metric"):
                                self.metric = value
                                self.metric.value_namespace = name_space
                                self.metric.value_namespace_prefix = name_space_prefix
                            if(value_path == "next-hop-address"):
                                self.next_hop_address = value
                                self.next_hop_address.value_namespace = name_space
                                self.next_hop_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "prefix"):
                                self.prefix = value
                                self.prefix.value_namespace = name_space
                                self.prefix.value_namespace_prefix = name_space_prefix
                            if(value_path == "prefix-length"):
                                self.prefix_length = value
                                self.prefix_length.value_namespace = name_space
                                self.prefix_length.value_namespace_prefix = name_space_prefix


                    class RipPeer(Entity):
                        """
                        Neighbors on this interface
                        
                        .. attribute:: discarded_peer_packets
                        
                        	Discarded packets from this peer
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: discarded_peer_routes
                        
                        	Discarded routes from this peer
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: peer_address
                        
                        	IP Address of this peer
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: peer_uptime
                        
                        	Uptime of this peer
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: peer_version
                        
                        	RIP version for this peer
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        

                        """

                        _prefix = 'ip-rip-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Rip.Vrfs.Vrf.Interfaces.Interface.RipPeer, self).__init__()

                            self.yang_name = "rip-peer"
                            self.yang_parent_name = "interface"

                            self.discarded_peer_packets = YLeaf(YType.uint32, "discarded-peer-packets")

                            self.discarded_peer_routes = YLeaf(YType.uint32, "discarded-peer-routes")

                            self.peer_address = YLeaf(YType.str, "peer-address")

                            self.peer_uptime = YLeaf(YType.uint32, "peer-uptime")

                            self.peer_version = YLeaf(YType.uint8, "peer-version")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("discarded_peer_packets",
                                            "discarded_peer_routes",
                                            "peer_address",
                                            "peer_uptime",
                                            "peer_version") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Rip.Vrfs.Vrf.Interfaces.Interface.RipPeer, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Rip.Vrfs.Vrf.Interfaces.Interface.RipPeer, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.discarded_peer_packets.is_set or
                                self.discarded_peer_routes.is_set or
                                self.peer_address.is_set or
                                self.peer_uptime.is_set or
                                self.peer_version.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.discarded_peer_packets.yfilter != YFilter.not_set or
                                self.discarded_peer_routes.yfilter != YFilter.not_set or
                                self.peer_address.yfilter != YFilter.not_set or
                                self.peer_uptime.yfilter != YFilter.not_set or
                                self.peer_version.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "rip-peer" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.discarded_peer_packets.is_set or self.discarded_peer_packets.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.discarded_peer_packets.get_name_leafdata())
                            if (self.discarded_peer_routes.is_set or self.discarded_peer_routes.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.discarded_peer_routes.get_name_leafdata())
                            if (self.peer_address.is_set or self.peer_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.peer_address.get_name_leafdata())
                            if (self.peer_uptime.is_set or self.peer_uptime.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.peer_uptime.get_name_leafdata())
                            if (self.peer_version.is_set or self.peer_version.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.peer_version.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "discarded-peer-packets" or name == "discarded-peer-routes" or name == "peer-address" or name == "peer-uptime" or name == "peer-version"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "discarded-peer-packets"):
                                self.discarded_peer_packets = value
                                self.discarded_peer_packets.value_namespace = name_space
                                self.discarded_peer_packets.value_namespace_prefix = name_space_prefix
                            if(value_path == "discarded-peer-routes"):
                                self.discarded_peer_routes = value
                                self.discarded_peer_routes.value_namespace = name_space
                                self.discarded_peer_routes.value_namespace_prefix = name_space_prefix
                            if(value_path == "peer-address"):
                                self.peer_address = value
                                self.peer_address.value_namespace = name_space
                                self.peer_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "peer-uptime"):
                                self.peer_uptime = value
                                self.peer_uptime.value_namespace = name_space
                                self.peer_uptime.value_namespace_prefix = name_space_prefix
                            if(value_path == "peer-version"):
                                self.peer_version = value
                                self.peer_version.value_namespace = name_space
                                self.peer_version.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.rip_peer:
                            if (c.has_data()):
                                return True
                        for c in self.rip_summary:
                            if (c.has_data()):
                                return True
                        return (
                            self.interface_name.is_set or
                            self.accept_metric.is_set or
                            self.auth_key_md5.is_set or
                            self.auth_key_send_id.is_set or
                            self.auth_keychain.is_set or
                            self.auth_mode.is_set or
                            self.destination_address.is_set or
                            self.if_handle.is_set or
                            self.interface.is_set or
                            self.is_passive_interface.is_set or
                            self.join_status.is_set or
                            self.lpts_state.is_set or
                            self.metric_cost.is_set or
                            self.multicast_address.is_set or
                            self.neighbor_address.is_set or
                            self.oom_flags.is_set or
                            self.pkt_accepted_valid_auth.is_set or
                            self.pkt_drop_invalid_auth.is_set or
                            self.pkt_drop_no_auth.is_set or
                            self.pkt_drop_wrong_kc.is_set or
                            self.poison_horizon.is_set or
                            self.prefix_length.is_set or
                            self.receive_version.is_set or
                            self.rip_enabled.is_set or
                            self.send_auth_key_exists.is_set or
                            self.send_version.is_set or
                            self.split_horizon.is_set or
                            self.state.is_set or
                            self.total_pkt_recvd.is_set or
                            self.triggered_rip.is_set)

                    def has_operation(self):
                        for c in self.rip_peer:
                            if (c.has_operation()):
                                return True
                        for c in self.rip_summary:
                            if (c.has_operation()):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.interface_name.yfilter != YFilter.not_set or
                            self.accept_metric.yfilter != YFilter.not_set or
                            self.auth_key_md5.yfilter != YFilter.not_set or
                            self.auth_key_send_id.yfilter != YFilter.not_set or
                            self.auth_keychain.yfilter != YFilter.not_set or
                            self.auth_mode.yfilter != YFilter.not_set or
                            self.destination_address.yfilter != YFilter.not_set or
                            self.if_handle.yfilter != YFilter.not_set or
                            self.interface.yfilter != YFilter.not_set or
                            self.is_passive_interface.yfilter != YFilter.not_set or
                            self.join_status.yfilter != YFilter.not_set or
                            self.lpts_state.yfilter != YFilter.not_set or
                            self.metric_cost.yfilter != YFilter.not_set or
                            self.multicast_address.yfilter != YFilter.not_set or
                            self.neighbor_address.yfilter != YFilter.not_set or
                            self.oom_flags.yfilter != YFilter.not_set or
                            self.pkt_accepted_valid_auth.yfilter != YFilter.not_set or
                            self.pkt_drop_invalid_auth.yfilter != YFilter.not_set or
                            self.pkt_drop_no_auth.yfilter != YFilter.not_set or
                            self.pkt_drop_wrong_kc.yfilter != YFilter.not_set or
                            self.poison_horizon.yfilter != YFilter.not_set or
                            self.prefix_length.yfilter != YFilter.not_set or
                            self.receive_version.yfilter != YFilter.not_set or
                            self.rip_enabled.yfilter != YFilter.not_set or
                            self.send_auth_key_exists.yfilter != YFilter.not_set or
                            self.send_version.yfilter != YFilter.not_set or
                            self.split_horizon.yfilter != YFilter.not_set or
                            self.state.yfilter != YFilter.not_set or
                            self.total_pkt_recvd.yfilter != YFilter.not_set or
                            self.triggered_rip.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "interface" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

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
                        if (self.accept_metric.is_set or self.accept_metric.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.accept_metric.get_name_leafdata())
                        if (self.auth_key_md5.is_set or self.auth_key_md5.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.auth_key_md5.get_name_leafdata())
                        if (self.auth_key_send_id.is_set or self.auth_key_send_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.auth_key_send_id.get_name_leafdata())
                        if (self.auth_keychain.is_set or self.auth_keychain.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.auth_keychain.get_name_leafdata())
                        if (self.auth_mode.is_set or self.auth_mode.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.auth_mode.get_name_leafdata())
                        if (self.destination_address.is_set or self.destination_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.destination_address.get_name_leafdata())
                        if (self.if_handle.is_set or self.if_handle.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.if_handle.get_name_leafdata())
                        if (self.interface.is_set or self.interface.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface.get_name_leafdata())
                        if (self.is_passive_interface.is_set or self.is_passive_interface.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.is_passive_interface.get_name_leafdata())
                        if (self.join_status.is_set or self.join_status.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.join_status.get_name_leafdata())
                        if (self.lpts_state.is_set or self.lpts_state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.lpts_state.get_name_leafdata())
                        if (self.metric_cost.is_set or self.metric_cost.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.metric_cost.get_name_leafdata())
                        if (self.multicast_address.is_set or self.multicast_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.multicast_address.get_name_leafdata())
                        if (self.neighbor_address.is_set or self.neighbor_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.neighbor_address.get_name_leafdata())
                        if (self.oom_flags.is_set or self.oom_flags.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.oom_flags.get_name_leafdata())
                        if (self.pkt_accepted_valid_auth.is_set or self.pkt_accepted_valid_auth.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pkt_accepted_valid_auth.get_name_leafdata())
                        if (self.pkt_drop_invalid_auth.is_set or self.pkt_drop_invalid_auth.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pkt_drop_invalid_auth.get_name_leafdata())
                        if (self.pkt_drop_no_auth.is_set or self.pkt_drop_no_auth.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pkt_drop_no_auth.get_name_leafdata())
                        if (self.pkt_drop_wrong_kc.is_set or self.pkt_drop_wrong_kc.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pkt_drop_wrong_kc.get_name_leafdata())
                        if (self.poison_horizon.is_set or self.poison_horizon.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.poison_horizon.get_name_leafdata())
                        if (self.prefix_length.is_set or self.prefix_length.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.prefix_length.get_name_leafdata())
                        if (self.receive_version.is_set or self.receive_version.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.receive_version.get_name_leafdata())
                        if (self.rip_enabled.is_set or self.rip_enabled.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.rip_enabled.get_name_leafdata())
                        if (self.send_auth_key_exists.is_set or self.send_auth_key_exists.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.send_auth_key_exists.get_name_leafdata())
                        if (self.send_version.is_set or self.send_version.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.send_version.get_name_leafdata())
                        if (self.split_horizon.is_set or self.split_horizon.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.split_horizon.get_name_leafdata())
                        if (self.state.is_set or self.state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.state.get_name_leafdata())
                        if (self.total_pkt_recvd.is_set or self.total_pkt_recvd.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.total_pkt_recvd.get_name_leafdata())
                        if (self.triggered_rip.is_set or self.triggered_rip.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.triggered_rip.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "rip-peer"):
                            for c in self.rip_peer:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Rip.Vrfs.Vrf.Interfaces.Interface.RipPeer()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.rip_peer.append(c)
                            return c

                        if (child_yang_name == "rip-summary"):
                            for c in self.rip_summary:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Rip.Vrfs.Vrf.Interfaces.Interface.RipSummary()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.rip_summary.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "rip-peer" or name == "rip-summary" or name == "interface-name" or name == "accept-metric" or name == "auth-key-md5" or name == "auth-key-send-id" or name == "auth-keychain" or name == "auth-mode" or name == "destination-address" or name == "if-handle" or name == "interface" or name == "is-passive-interface" or name == "join-status" or name == "lpts-state" or name == "metric-cost" or name == "multicast-address" or name == "neighbor-address" or name == "oom-flags" or name == "pkt-accepted-valid-auth" or name == "pkt-drop-invalid-auth" or name == "pkt-drop-no-auth" or name == "pkt-drop-wrong-kc" or name == "poison-horizon" or name == "prefix-length" or name == "receive-version" or name == "rip-enabled" or name == "send-auth-key-exists" or name == "send-version" or name == "split-horizon" or name == "state" or name == "total-pkt-recvd" or name == "triggered-rip"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "interface-name"):
                            self.interface_name = value
                            self.interface_name.value_namespace = name_space
                            self.interface_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "accept-metric"):
                            self.accept_metric = value
                            self.accept_metric.value_namespace = name_space
                            self.accept_metric.value_namespace_prefix = name_space_prefix
                        if(value_path == "auth-key-md5"):
                            self.auth_key_md5 = value
                            self.auth_key_md5.value_namespace = name_space
                            self.auth_key_md5.value_namespace_prefix = name_space_prefix
                        if(value_path == "auth-key-send-id"):
                            self.auth_key_send_id = value
                            self.auth_key_send_id.value_namespace = name_space
                            self.auth_key_send_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "auth-keychain"):
                            self.auth_keychain = value
                            self.auth_keychain.value_namespace = name_space
                            self.auth_keychain.value_namespace_prefix = name_space_prefix
                        if(value_path == "auth-mode"):
                            self.auth_mode = value
                            self.auth_mode.value_namespace = name_space
                            self.auth_mode.value_namespace_prefix = name_space_prefix
                        if(value_path == "destination-address"):
                            self.destination_address = value
                            self.destination_address.value_namespace = name_space
                            self.destination_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "if-handle"):
                            self.if_handle = value
                            self.if_handle.value_namespace = name_space
                            self.if_handle.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface"):
                            self.interface = value
                            self.interface.value_namespace = name_space
                            self.interface.value_namespace_prefix = name_space_prefix
                        if(value_path == "is-passive-interface"):
                            self.is_passive_interface = value
                            self.is_passive_interface.value_namespace = name_space
                            self.is_passive_interface.value_namespace_prefix = name_space_prefix
                        if(value_path == "join-status"):
                            self.join_status = value
                            self.join_status.value_namespace = name_space
                            self.join_status.value_namespace_prefix = name_space_prefix
                        if(value_path == "lpts-state"):
                            self.lpts_state = value
                            self.lpts_state.value_namespace = name_space
                            self.lpts_state.value_namespace_prefix = name_space_prefix
                        if(value_path == "metric-cost"):
                            self.metric_cost = value
                            self.metric_cost.value_namespace = name_space
                            self.metric_cost.value_namespace_prefix = name_space_prefix
                        if(value_path == "multicast-address"):
                            self.multicast_address = value
                            self.multicast_address.value_namespace = name_space
                            self.multicast_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "neighbor-address"):
                            self.neighbor_address = value
                            self.neighbor_address.value_namespace = name_space
                            self.neighbor_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "oom-flags"):
                            self.oom_flags = value
                            self.oom_flags.value_namespace = name_space
                            self.oom_flags.value_namespace_prefix = name_space_prefix
                        if(value_path == "pkt-accepted-valid-auth"):
                            self.pkt_accepted_valid_auth = value
                            self.pkt_accepted_valid_auth.value_namespace = name_space
                            self.pkt_accepted_valid_auth.value_namespace_prefix = name_space_prefix
                        if(value_path == "pkt-drop-invalid-auth"):
                            self.pkt_drop_invalid_auth = value
                            self.pkt_drop_invalid_auth.value_namespace = name_space
                            self.pkt_drop_invalid_auth.value_namespace_prefix = name_space_prefix
                        if(value_path == "pkt-drop-no-auth"):
                            self.pkt_drop_no_auth = value
                            self.pkt_drop_no_auth.value_namespace = name_space
                            self.pkt_drop_no_auth.value_namespace_prefix = name_space_prefix
                        if(value_path == "pkt-drop-wrong-kc"):
                            self.pkt_drop_wrong_kc = value
                            self.pkt_drop_wrong_kc.value_namespace = name_space
                            self.pkt_drop_wrong_kc.value_namespace_prefix = name_space_prefix
                        if(value_path == "poison-horizon"):
                            self.poison_horizon = value
                            self.poison_horizon.value_namespace = name_space
                            self.poison_horizon.value_namespace_prefix = name_space_prefix
                        if(value_path == "prefix-length"):
                            self.prefix_length = value
                            self.prefix_length.value_namespace = name_space
                            self.prefix_length.value_namespace_prefix = name_space_prefix
                        if(value_path == "receive-version"):
                            self.receive_version = value
                            self.receive_version.value_namespace = name_space
                            self.receive_version.value_namespace_prefix = name_space_prefix
                        if(value_path == "rip-enabled"):
                            self.rip_enabled = value
                            self.rip_enabled.value_namespace = name_space
                            self.rip_enabled.value_namespace_prefix = name_space_prefix
                        if(value_path == "send-auth-key-exists"):
                            self.send_auth_key_exists = value
                            self.send_auth_key_exists.value_namespace = name_space
                            self.send_auth_key_exists.value_namespace_prefix = name_space_prefix
                        if(value_path == "send-version"):
                            self.send_version = value
                            self.send_version.value_namespace = name_space
                            self.send_version.value_namespace_prefix = name_space_prefix
                        if(value_path == "split-horizon"):
                            self.split_horizon = value
                            self.split_horizon.value_namespace = name_space
                            self.split_horizon.value_namespace_prefix = name_space_prefix
                        if(value_path == "state"):
                            self.state = value
                            self.state.value_namespace = name_space
                            self.state.value_namespace_prefix = name_space_prefix
                        if(value_path == "total-pkt-recvd"):
                            self.total_pkt_recvd = value
                            self.total_pkt_recvd.value_namespace = name_space
                            self.total_pkt_recvd.value_namespace_prefix = name_space_prefix
                        if(value_path == "triggered-rip"):
                            self.triggered_rip = value
                            self.triggered_rip.value_namespace = name_space
                            self.triggered_rip.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.interface:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.interface:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "interfaces" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "interface"):
                        for c in self.interface:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Rip.Vrfs.Vrf.Interfaces.Interface()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.interface.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "interface"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Global_(Entity):
                """
                Global Information 
                
                .. attribute:: interface_summary
                
                	List of Interfaces configured
                	**type**\: list of    :py:class:`InterfaceSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Vrfs.Vrf.Global_.InterfaceSummary>`
                
                .. attribute:: vrf_summary
                
                	VRF summary data
                	**type**\:   :py:class:`VrfSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Vrfs.Vrf.Global_.VrfSummary>`
                
                

                """

                _prefix = 'ip-rip-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rip.Vrfs.Vrf.Global_, self).__init__()

                    self.yang_name = "global"
                    self.yang_parent_name = "vrf"

                    self.vrf_summary = Rip.Vrfs.Vrf.Global_.VrfSummary()
                    self.vrf_summary.parent = self
                    self._children_name_map["vrf_summary"] = "vrf-summary"
                    self._children_yang_names.add("vrf-summary")

                    self.interface_summary = YList(self)

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
                                super(Rip.Vrfs.Vrf.Global_, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Rip.Vrfs.Vrf.Global_, self).__setattr__(name, value)


                class VrfSummary(Entity):
                    """
                    VRF summary data
                    
                    .. attribute:: active
                    
                    	VRF Active indicator
                    	**type**\:  bool
                    
                    .. attribute:: active_interface_count
                    
                    	Number of active interfaces
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: flush_timer
                    
                    	Flush timer
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: hold_down_timer
                    
                    	Holddown timer
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: interface_configured_count
                    
                    	Number of interfaces configured
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: invalid_timer
                    
                    	Invalid timer
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: next_update_time
                    
                    	Time left for next update
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: oom_flags
                    
                    	Current OOM flags
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: path_count
                    
                    	Number of paths allocated
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: route_count
                    
                    	Number of routes allocated
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: update_timer
                    
                    	Update timer
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: vrf_name
                    
                    	VRF Name
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'ip-rip-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Rip.Vrfs.Vrf.Global_.VrfSummary, self).__init__()

                        self.yang_name = "vrf-summary"
                        self.yang_parent_name = "global"

                        self.active = YLeaf(YType.boolean, "active")

                        self.active_interface_count = YLeaf(YType.uint32, "active-interface-count")

                        self.flush_timer = YLeaf(YType.uint32, "flush-timer")

                        self.hold_down_timer = YLeaf(YType.uint32, "hold-down-timer")

                        self.interface_configured_count = YLeaf(YType.uint32, "interface-configured-count")

                        self.invalid_timer = YLeaf(YType.uint32, "invalid-timer")

                        self.next_update_time = YLeaf(YType.uint32, "next-update-time")

                        self.oom_flags = YLeaf(YType.uint32, "oom-flags")

                        self.path_count = YLeaf(YType.uint32, "path-count")

                        self.route_count = YLeaf(YType.uint32, "route-count")

                        self.update_timer = YLeaf(YType.uint32, "update-timer")

                        self.vrf_name = YLeaf(YType.str, "vrf-name")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("active",
                                        "active_interface_count",
                                        "flush_timer",
                                        "hold_down_timer",
                                        "interface_configured_count",
                                        "invalid_timer",
                                        "next_update_time",
                                        "oom_flags",
                                        "path_count",
                                        "route_count",
                                        "update_timer",
                                        "vrf_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Rip.Vrfs.Vrf.Global_.VrfSummary, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Rip.Vrfs.Vrf.Global_.VrfSummary, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.active.is_set or
                            self.active_interface_count.is_set or
                            self.flush_timer.is_set or
                            self.hold_down_timer.is_set or
                            self.interface_configured_count.is_set or
                            self.invalid_timer.is_set or
                            self.next_update_time.is_set or
                            self.oom_flags.is_set or
                            self.path_count.is_set or
                            self.route_count.is_set or
                            self.update_timer.is_set or
                            self.vrf_name.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.active.yfilter != YFilter.not_set or
                            self.active_interface_count.yfilter != YFilter.not_set or
                            self.flush_timer.yfilter != YFilter.not_set or
                            self.hold_down_timer.yfilter != YFilter.not_set or
                            self.interface_configured_count.yfilter != YFilter.not_set or
                            self.invalid_timer.yfilter != YFilter.not_set or
                            self.next_update_time.yfilter != YFilter.not_set or
                            self.oom_flags.yfilter != YFilter.not_set or
                            self.path_count.yfilter != YFilter.not_set or
                            self.route_count.yfilter != YFilter.not_set or
                            self.update_timer.yfilter != YFilter.not_set or
                            self.vrf_name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "vrf-summary" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.active.is_set or self.active.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.active.get_name_leafdata())
                        if (self.active_interface_count.is_set or self.active_interface_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.active_interface_count.get_name_leafdata())
                        if (self.flush_timer.is_set or self.flush_timer.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.flush_timer.get_name_leafdata())
                        if (self.hold_down_timer.is_set or self.hold_down_timer.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.hold_down_timer.get_name_leafdata())
                        if (self.interface_configured_count.is_set or self.interface_configured_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_configured_count.get_name_leafdata())
                        if (self.invalid_timer.is_set or self.invalid_timer.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.invalid_timer.get_name_leafdata())
                        if (self.next_update_time.is_set or self.next_update_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.next_update_time.get_name_leafdata())
                        if (self.oom_flags.is_set or self.oom_flags.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.oom_flags.get_name_leafdata())
                        if (self.path_count.is_set or self.path_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.path_count.get_name_leafdata())
                        if (self.route_count.is_set or self.route_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.route_count.get_name_leafdata())
                        if (self.update_timer.is_set or self.update_timer.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.update_timer.get_name_leafdata())
                        if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vrf_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "active" or name == "active-interface-count" or name == "flush-timer" or name == "hold-down-timer" or name == "interface-configured-count" or name == "invalid-timer" or name == "next-update-time" or name == "oom-flags" or name == "path-count" or name == "route-count" or name == "update-timer" or name == "vrf-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "active"):
                            self.active = value
                            self.active.value_namespace = name_space
                            self.active.value_namespace_prefix = name_space_prefix
                        if(value_path == "active-interface-count"):
                            self.active_interface_count = value
                            self.active_interface_count.value_namespace = name_space
                            self.active_interface_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "flush-timer"):
                            self.flush_timer = value
                            self.flush_timer.value_namespace = name_space
                            self.flush_timer.value_namespace_prefix = name_space_prefix
                        if(value_path == "hold-down-timer"):
                            self.hold_down_timer = value
                            self.hold_down_timer.value_namespace = name_space
                            self.hold_down_timer.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface-configured-count"):
                            self.interface_configured_count = value
                            self.interface_configured_count.value_namespace = name_space
                            self.interface_configured_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "invalid-timer"):
                            self.invalid_timer = value
                            self.invalid_timer.value_namespace = name_space
                            self.invalid_timer.value_namespace_prefix = name_space_prefix
                        if(value_path == "next-update-time"):
                            self.next_update_time = value
                            self.next_update_time.value_namespace = name_space
                            self.next_update_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "oom-flags"):
                            self.oom_flags = value
                            self.oom_flags.value_namespace = name_space
                            self.oom_flags.value_namespace_prefix = name_space_prefix
                        if(value_path == "path-count"):
                            self.path_count = value
                            self.path_count.value_namespace = name_space
                            self.path_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "route-count"):
                            self.route_count = value
                            self.route_count.value_namespace = name_space
                            self.route_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "update-timer"):
                            self.update_timer = value
                            self.update_timer.value_namespace = name_space
                            self.update_timer.value_namespace_prefix = name_space_prefix
                        if(value_path == "vrf-name"):
                            self.vrf_name = value
                            self.vrf_name.value_namespace = name_space
                            self.vrf_name.value_namespace_prefix = name_space_prefix


                class InterfaceSummary(Entity):
                    """
                    List of Interfaces configured
                    
                    .. attribute:: destination_address
                    
                    	IP address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: enabled
                    
                    	RIP enabled indicator
                    	**type**\:  bool
                    
                    .. attribute:: interface_name
                    
                    	Interface name
                    	**type**\:  str
                    
                    .. attribute:: neighbor_count
                    
                    	Number of neighbors seen
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: oom_flags
                    
                    	Current OOM flags
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: prefix_length
                    
                    	Prefix length of IP address
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: receive_version
                    
                    	RIP versions this interface will receive
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: send_version
                    
                    	RIP versions this interface sends out
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: state
                    
                    	Interface state
                    	**type**\:   :py:class:`InterfaceState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.InterfaceState>`
                    
                    

                    """

                    _prefix = 'ip-rip-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Rip.Vrfs.Vrf.Global_.InterfaceSummary, self).__init__()

                        self.yang_name = "interface-summary"
                        self.yang_parent_name = "global"

                        self.destination_address = YLeaf(YType.str, "destination-address")

                        self.enabled = YLeaf(YType.boolean, "enabled")

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.neighbor_count = YLeaf(YType.uint32, "neighbor-count")

                        self.oom_flags = YLeaf(YType.uint32, "oom-flags")

                        self.prefix_length = YLeaf(YType.uint32, "prefix-length")

                        self.receive_version = YLeaf(YType.uint32, "receive-version")

                        self.send_version = YLeaf(YType.uint32, "send-version")

                        self.state = YLeaf(YType.enumeration, "state")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("destination_address",
                                        "enabled",
                                        "interface_name",
                                        "neighbor_count",
                                        "oom_flags",
                                        "prefix_length",
                                        "receive_version",
                                        "send_version",
                                        "state") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Rip.Vrfs.Vrf.Global_.InterfaceSummary, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Rip.Vrfs.Vrf.Global_.InterfaceSummary, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.destination_address.is_set or
                            self.enabled.is_set or
                            self.interface_name.is_set or
                            self.neighbor_count.is_set or
                            self.oom_flags.is_set or
                            self.prefix_length.is_set or
                            self.receive_version.is_set or
                            self.send_version.is_set or
                            self.state.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.destination_address.yfilter != YFilter.not_set or
                            self.enabled.yfilter != YFilter.not_set or
                            self.interface_name.yfilter != YFilter.not_set or
                            self.neighbor_count.yfilter != YFilter.not_set or
                            self.oom_flags.yfilter != YFilter.not_set or
                            self.prefix_length.yfilter != YFilter.not_set or
                            self.receive_version.yfilter != YFilter.not_set or
                            self.send_version.yfilter != YFilter.not_set or
                            self.state.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "interface-summary" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.destination_address.is_set or self.destination_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.destination_address.get_name_leafdata())
                        if (self.enabled.is_set or self.enabled.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.enabled.get_name_leafdata())
                        if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_name.get_name_leafdata())
                        if (self.neighbor_count.is_set or self.neighbor_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.neighbor_count.get_name_leafdata())
                        if (self.oom_flags.is_set or self.oom_flags.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.oom_flags.get_name_leafdata())
                        if (self.prefix_length.is_set or self.prefix_length.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.prefix_length.get_name_leafdata())
                        if (self.receive_version.is_set or self.receive_version.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.receive_version.get_name_leafdata())
                        if (self.send_version.is_set or self.send_version.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.send_version.get_name_leafdata())
                        if (self.state.is_set or self.state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.state.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "destination-address" or name == "enabled" or name == "interface-name" or name == "neighbor-count" or name == "oom-flags" or name == "prefix-length" or name == "receive-version" or name == "send-version" or name == "state"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "destination-address"):
                            self.destination_address = value
                            self.destination_address.value_namespace = name_space
                            self.destination_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "enabled"):
                            self.enabled = value
                            self.enabled.value_namespace = name_space
                            self.enabled.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface-name"):
                            self.interface_name = value
                            self.interface_name.value_namespace = name_space
                            self.interface_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "neighbor-count"):
                            self.neighbor_count = value
                            self.neighbor_count.value_namespace = name_space
                            self.neighbor_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "oom-flags"):
                            self.oom_flags = value
                            self.oom_flags.value_namespace = name_space
                            self.oom_flags.value_namespace_prefix = name_space_prefix
                        if(value_path == "prefix-length"):
                            self.prefix_length = value
                            self.prefix_length.value_namespace = name_space
                            self.prefix_length.value_namespace_prefix = name_space_prefix
                        if(value_path == "receive-version"):
                            self.receive_version = value
                            self.receive_version.value_namespace = name_space
                            self.receive_version.value_namespace_prefix = name_space_prefix
                        if(value_path == "send-version"):
                            self.send_version = value
                            self.send_version.value_namespace = name_space
                            self.send_version.value_namespace_prefix = name_space_prefix
                        if(value_path == "state"):
                            self.state = value
                            self.state.value_namespace = name_space
                            self.state.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.interface_summary:
                        if (c.has_data()):
                            return True
                    return (self.vrf_summary is not None and self.vrf_summary.has_data())

                def has_operation(self):
                    for c in self.interface_summary:
                        if (c.has_operation()):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.vrf_summary is not None and self.vrf_summary.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "global" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "interface-summary"):
                        for c in self.interface_summary:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Rip.Vrfs.Vrf.Global_.InterfaceSummary()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.interface_summary.append(c)
                        return c

                    if (child_yang_name == "vrf-summary"):
                        if (self.vrf_summary is None):
                            self.vrf_summary = Rip.Vrfs.Vrf.Global_.VrfSummary()
                            self.vrf_summary.parent = self
                            self._children_name_map["vrf_summary"] = "vrf-summary"
                        return self.vrf_summary

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "interface-summary" or name == "vrf-summary"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.vrf_name.is_set or
                    (self.configuration is not None and self.configuration.has_data()) or
                    (self.global_ is not None and self.global_.has_data()) or
                    (self.interfaces is not None and self.interfaces.has_data()) or
                    (self.routes is not None and self.routes.has_data()) or
                    (self.statistics is not None and self.statistics.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.vrf_name.yfilter != YFilter.not_set or
                    (self.configuration is not None and self.configuration.has_operation()) or
                    (self.global_ is not None and self.global_.has_operation()) or
                    (self.interfaces is not None and self.interfaces.has_operation()) or
                    (self.routes is not None and self.routes.has_operation()) or
                    (self.statistics is not None and self.statistics.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "vrf" + "[vrf-name='" + self.vrf_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ip-rip-oper:rip/vrfs/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vrf_name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "configuration"):
                    if (self.configuration is None):
                        self.configuration = Rip.Vrfs.Vrf.Configuration()
                        self.configuration.parent = self
                        self._children_name_map["configuration"] = "configuration"
                    return self.configuration

                if (child_yang_name == "global"):
                    if (self.global_ is None):
                        self.global_ = Rip.Vrfs.Vrf.Global_()
                        self.global_.parent = self
                        self._children_name_map["global_"] = "global"
                    return self.global_

                if (child_yang_name == "interfaces"):
                    if (self.interfaces is None):
                        self.interfaces = Rip.Vrfs.Vrf.Interfaces()
                        self.interfaces.parent = self
                        self._children_name_map["interfaces"] = "interfaces"
                    return self.interfaces

                if (child_yang_name == "routes"):
                    if (self.routes is None):
                        self.routes = Rip.Vrfs.Vrf.Routes()
                        self.routes.parent = self
                        self._children_name_map["routes"] = "routes"
                    return self.routes

                if (child_yang_name == "statistics"):
                    if (self.statistics is None):
                        self.statistics = Rip.Vrfs.Vrf.Statistics()
                        self.statistics.parent = self
                        self._children_name_map["statistics"] = "statistics"
                    return self.statistics

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "configuration" or name == "global" or name == "interfaces" or name == "routes" or name == "statistics" or name == "vrf-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "vrf-name"):
                    self.vrf_name = value
                    self.vrf_name.value_namespace = name_space
                    self.vrf_name.value_namespace_prefix = name_space_prefix

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
                path_buffer = "Cisco-IOS-XR-ip-rip-oper:rip/%s" % self.get_segment_path()
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
                c = Rip.Vrfs.Vrf()
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


    class Protocol(Entity):
        """
        Protocol operational data
        
        .. attribute:: default_vrf
        
        	RIP operational data for Default VRF
        	**type**\:   :py:class:`DefaultVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Protocol.DefaultVrf>`
        
        .. attribute:: process
        
        	RIP global process 
        	**type**\:   :py:class:`Process <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Protocol.Process>`
        
        

        """

        _prefix = 'ip-rip-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Rip.Protocol, self).__init__()

            self.yang_name = "protocol"
            self.yang_parent_name = "rip"

            self.default_vrf = Rip.Protocol.DefaultVrf()
            self.default_vrf.parent = self
            self._children_name_map["default_vrf"] = "default-vrf"
            self._children_yang_names.add("default-vrf")

            self.process = Rip.Protocol.Process()
            self.process.parent = self
            self._children_name_map["process"] = "process"
            self._children_yang_names.add("process")


        class Process(Entity):
            """
            RIP global process 
            
            .. attribute:: current_oom_state
            
            	Current OOM state
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: path_count
            
            	Number of paths allocated
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: route_count
            
            	Number of routes allocated
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: socket_descriptor
            
            	Socket descriptior
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: vrf_active_count
            
            	Number of active VRFs
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: vrf_config_count
            
            	Number of VRFs configured
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: vrf_summary
            
            	List of VRFs configured
            	**type**\: list of    :py:class:`VrfSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Protocol.Process.VrfSummary>`
            
            

            """

            _prefix = 'ip-rip-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Rip.Protocol.Process, self).__init__()

                self.yang_name = "process"
                self.yang_parent_name = "protocol"

                self.current_oom_state = YLeaf(YType.int32, "current-oom-state")

                self.path_count = YLeaf(YType.uint32, "path-count")

                self.route_count = YLeaf(YType.uint32, "route-count")

                self.socket_descriptor = YLeaf(YType.int32, "socket-descriptor")

                self.vrf_active_count = YLeaf(YType.uint32, "vrf-active-count")

                self.vrf_config_count = YLeaf(YType.uint32, "vrf-config-count")

                self.vrf_summary = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("current_oom_state",
                                "path_count",
                                "route_count",
                                "socket_descriptor",
                                "vrf_active_count",
                                "vrf_config_count") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Rip.Protocol.Process, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Rip.Protocol.Process, self).__setattr__(name, value)


            class VrfSummary(Entity):
                """
                List of VRFs configured
                
                .. attribute:: active
                
                	VRF Active indicator
                	**type**\:  bool
                
                .. attribute:: active_interface_count
                
                	Number of active interfaces
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: flush_timer
                
                	Flush timer
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: hold_down_timer
                
                	Holddown timer
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: interface_configured_count
                
                	Number of interfaces configured
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: invalid_timer
                
                	Invalid timer
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: next_update_time
                
                	Time left for next update
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: oom_flags
                
                	Current OOM flags
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: path_count
                
                	Number of paths allocated
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: route_count
                
                	Number of routes allocated
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: update_timer
                
                	Update timer
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: vrf_name
                
                	VRF Name
                	**type**\:  str
                
                

                """

                _prefix = 'ip-rip-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rip.Protocol.Process.VrfSummary, self).__init__()

                    self.yang_name = "vrf-summary"
                    self.yang_parent_name = "process"

                    self.active = YLeaf(YType.boolean, "active")

                    self.active_interface_count = YLeaf(YType.uint32, "active-interface-count")

                    self.flush_timer = YLeaf(YType.uint32, "flush-timer")

                    self.hold_down_timer = YLeaf(YType.uint32, "hold-down-timer")

                    self.interface_configured_count = YLeaf(YType.uint32, "interface-configured-count")

                    self.invalid_timer = YLeaf(YType.uint32, "invalid-timer")

                    self.next_update_time = YLeaf(YType.uint32, "next-update-time")

                    self.oom_flags = YLeaf(YType.uint32, "oom-flags")

                    self.path_count = YLeaf(YType.uint32, "path-count")

                    self.route_count = YLeaf(YType.uint32, "route-count")

                    self.update_timer = YLeaf(YType.uint32, "update-timer")

                    self.vrf_name = YLeaf(YType.str, "vrf-name")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("active",
                                    "active_interface_count",
                                    "flush_timer",
                                    "hold_down_timer",
                                    "interface_configured_count",
                                    "invalid_timer",
                                    "next_update_time",
                                    "oom_flags",
                                    "path_count",
                                    "route_count",
                                    "update_timer",
                                    "vrf_name") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Rip.Protocol.Process.VrfSummary, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Rip.Protocol.Process.VrfSummary, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.active.is_set or
                        self.active_interface_count.is_set or
                        self.flush_timer.is_set or
                        self.hold_down_timer.is_set or
                        self.interface_configured_count.is_set or
                        self.invalid_timer.is_set or
                        self.next_update_time.is_set or
                        self.oom_flags.is_set or
                        self.path_count.is_set or
                        self.route_count.is_set or
                        self.update_timer.is_set or
                        self.vrf_name.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.active.yfilter != YFilter.not_set or
                        self.active_interface_count.yfilter != YFilter.not_set or
                        self.flush_timer.yfilter != YFilter.not_set or
                        self.hold_down_timer.yfilter != YFilter.not_set or
                        self.interface_configured_count.yfilter != YFilter.not_set or
                        self.invalid_timer.yfilter != YFilter.not_set or
                        self.next_update_time.yfilter != YFilter.not_set or
                        self.oom_flags.yfilter != YFilter.not_set or
                        self.path_count.yfilter != YFilter.not_set or
                        self.route_count.yfilter != YFilter.not_set or
                        self.update_timer.yfilter != YFilter.not_set or
                        self.vrf_name.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "vrf-summary" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ip-rip-oper:rip/protocol/process/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.active.is_set or self.active.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.active.get_name_leafdata())
                    if (self.active_interface_count.is_set or self.active_interface_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.active_interface_count.get_name_leafdata())
                    if (self.flush_timer.is_set or self.flush_timer.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.flush_timer.get_name_leafdata())
                    if (self.hold_down_timer.is_set or self.hold_down_timer.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.hold_down_timer.get_name_leafdata())
                    if (self.interface_configured_count.is_set or self.interface_configured_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.interface_configured_count.get_name_leafdata())
                    if (self.invalid_timer.is_set or self.invalid_timer.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.invalid_timer.get_name_leafdata())
                    if (self.next_update_time.is_set or self.next_update_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.next_update_time.get_name_leafdata())
                    if (self.oom_flags.is_set or self.oom_flags.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.oom_flags.get_name_leafdata())
                    if (self.path_count.is_set or self.path_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.path_count.get_name_leafdata())
                    if (self.route_count.is_set or self.route_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.route_count.get_name_leafdata())
                    if (self.update_timer.is_set or self.update_timer.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.update_timer.get_name_leafdata())
                    if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.vrf_name.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "active" or name == "active-interface-count" or name == "flush-timer" or name == "hold-down-timer" or name == "interface-configured-count" or name == "invalid-timer" or name == "next-update-time" or name == "oom-flags" or name == "path-count" or name == "route-count" or name == "update-timer" or name == "vrf-name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "active"):
                        self.active = value
                        self.active.value_namespace = name_space
                        self.active.value_namespace_prefix = name_space_prefix
                    if(value_path == "active-interface-count"):
                        self.active_interface_count = value
                        self.active_interface_count.value_namespace = name_space
                        self.active_interface_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "flush-timer"):
                        self.flush_timer = value
                        self.flush_timer.value_namespace = name_space
                        self.flush_timer.value_namespace_prefix = name_space_prefix
                    if(value_path == "hold-down-timer"):
                        self.hold_down_timer = value
                        self.hold_down_timer.value_namespace = name_space
                        self.hold_down_timer.value_namespace_prefix = name_space_prefix
                    if(value_path == "interface-configured-count"):
                        self.interface_configured_count = value
                        self.interface_configured_count.value_namespace = name_space
                        self.interface_configured_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "invalid-timer"):
                        self.invalid_timer = value
                        self.invalid_timer.value_namespace = name_space
                        self.invalid_timer.value_namespace_prefix = name_space_prefix
                    if(value_path == "next-update-time"):
                        self.next_update_time = value
                        self.next_update_time.value_namespace = name_space
                        self.next_update_time.value_namespace_prefix = name_space_prefix
                    if(value_path == "oom-flags"):
                        self.oom_flags = value
                        self.oom_flags.value_namespace = name_space
                        self.oom_flags.value_namespace_prefix = name_space_prefix
                    if(value_path == "path-count"):
                        self.path_count = value
                        self.path_count.value_namespace = name_space
                        self.path_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "route-count"):
                        self.route_count = value
                        self.route_count.value_namespace = name_space
                        self.route_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "update-timer"):
                        self.update_timer = value
                        self.update_timer.value_namespace = name_space
                        self.update_timer.value_namespace_prefix = name_space_prefix
                    if(value_path == "vrf-name"):
                        self.vrf_name = value
                        self.vrf_name.value_namespace = name_space
                        self.vrf_name.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.vrf_summary:
                    if (c.has_data()):
                        return True
                return (
                    self.current_oom_state.is_set or
                    self.path_count.is_set or
                    self.route_count.is_set or
                    self.socket_descriptor.is_set or
                    self.vrf_active_count.is_set or
                    self.vrf_config_count.is_set)

            def has_operation(self):
                for c in self.vrf_summary:
                    if (c.has_operation()):
                        return True
                return (
                    self.yfilter != YFilter.not_set or
                    self.current_oom_state.yfilter != YFilter.not_set or
                    self.path_count.yfilter != YFilter.not_set or
                    self.route_count.yfilter != YFilter.not_set or
                    self.socket_descriptor.yfilter != YFilter.not_set or
                    self.vrf_active_count.yfilter != YFilter.not_set or
                    self.vrf_config_count.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "process" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ip-rip-oper:rip/protocol/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.current_oom_state.is_set or self.current_oom_state.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.current_oom_state.get_name_leafdata())
                if (self.path_count.is_set or self.path_count.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.path_count.get_name_leafdata())
                if (self.route_count.is_set or self.route_count.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.route_count.get_name_leafdata())
                if (self.socket_descriptor.is_set or self.socket_descriptor.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.socket_descriptor.get_name_leafdata())
                if (self.vrf_active_count.is_set or self.vrf_active_count.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vrf_active_count.get_name_leafdata())
                if (self.vrf_config_count.is_set or self.vrf_config_count.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vrf_config_count.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "vrf-summary"):
                    for c in self.vrf_summary:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Rip.Protocol.Process.VrfSummary()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.vrf_summary.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "vrf-summary" or name == "current-oom-state" or name == "path-count" or name == "route-count" or name == "socket-descriptor" or name == "vrf-active-count" or name == "vrf-config-count"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "current-oom-state"):
                    self.current_oom_state = value
                    self.current_oom_state.value_namespace = name_space
                    self.current_oom_state.value_namespace_prefix = name_space_prefix
                if(value_path == "path-count"):
                    self.path_count = value
                    self.path_count.value_namespace = name_space
                    self.path_count.value_namespace_prefix = name_space_prefix
                if(value_path == "route-count"):
                    self.route_count = value
                    self.route_count.value_namespace = name_space
                    self.route_count.value_namespace_prefix = name_space_prefix
                if(value_path == "socket-descriptor"):
                    self.socket_descriptor = value
                    self.socket_descriptor.value_namespace = name_space
                    self.socket_descriptor.value_namespace_prefix = name_space_prefix
                if(value_path == "vrf-active-count"):
                    self.vrf_active_count = value
                    self.vrf_active_count.value_namespace = name_space
                    self.vrf_active_count.value_namespace_prefix = name_space_prefix
                if(value_path == "vrf-config-count"):
                    self.vrf_config_count = value
                    self.vrf_config_count.value_namespace = name_space
                    self.vrf_config_count.value_namespace_prefix = name_space_prefix


        class DefaultVrf(Entity):
            """
            RIP operational data for Default VRF
            
            .. attribute:: configuration
            
            	RIP global configuration
            	**type**\:   :py:class:`Configuration <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Protocol.DefaultVrf.Configuration>`
            
            .. attribute:: global_
            
            	Global Information 
            	**type**\:   :py:class:`Global_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Protocol.DefaultVrf.Global_>`
            
            .. attribute:: interfaces
            
            	RIP interfaces
            	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Protocol.DefaultVrf.Interfaces>`
            
            .. attribute:: routes
            
            	RIP route database
            	**type**\:   :py:class:`Routes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Protocol.DefaultVrf.Routes>`
            
            .. attribute:: statistics
            
            	RIP statistics information
            	**type**\:   :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Protocol.DefaultVrf.Statistics>`
            
            

            """

            _prefix = 'ip-rip-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Rip.Protocol.DefaultVrf, self).__init__()

                self.yang_name = "default-vrf"
                self.yang_parent_name = "protocol"

                self.configuration = Rip.Protocol.DefaultVrf.Configuration()
                self.configuration.parent = self
                self._children_name_map["configuration"] = "configuration"
                self._children_yang_names.add("configuration")

                self.global_ = Rip.Protocol.DefaultVrf.Global_()
                self.global_.parent = self
                self._children_name_map["global_"] = "global"
                self._children_yang_names.add("global")

                self.interfaces = Rip.Protocol.DefaultVrf.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"
                self._children_yang_names.add("interfaces")

                self.routes = Rip.Protocol.DefaultVrf.Routes()
                self.routes.parent = self
                self._children_name_map["routes"] = "routes"
                self._children_yang_names.add("routes")

                self.statistics = Rip.Protocol.DefaultVrf.Statistics()
                self.statistics.parent = self
                self._children_name_map["statistics"] = "statistics"
                self._children_yang_names.add("statistics")


            class Routes(Entity):
                """
                RIP route database
                
                .. attribute:: route
                
                	A route in the RIP database
                	**type**\: list of    :py:class:`Route <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Protocol.DefaultVrf.Routes.Route>`
                
                

                """

                _prefix = 'ip-rip-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rip.Protocol.DefaultVrf.Routes, self).__init__()

                    self.yang_name = "routes"
                    self.yang_parent_name = "default-vrf"

                    self.route = YList(self)

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
                                super(Rip.Protocol.DefaultVrf.Routes, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Rip.Protocol.DefaultVrf.Routes, self).__setattr__(name, value)


                class Route(Entity):
                    """
                    A route in the RIP database
                    
                    .. attribute:: active
                    
                    	Active route indicator
                    	**type**\:  bool
                    
                    .. attribute:: attributes
                    
                    	RIB supplied route attributes
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: bgp_count
                    
                    	Hop count for this route
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: destination_address
                    
                    	Destination IP Address for this route
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: distance
                    
                    	Route administrative distance
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: hold_down
                    
                    	Indicates whether route is in holddown
                    	**type**\:  bool
                    
                    .. attribute:: path_origin
                    
                    	Where this route was learnt
                    	**type**\:   :py:class:`RipRouteOrigin <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.RipRouteOrigin>`
                    
                    .. attribute:: paths
                    
                    	The paths for this route
                    	**type**\: list of    :py:class:`Paths <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Protocol.DefaultVrf.Routes.Route.Paths>`
                    
                    .. attribute:: prefix
                    
                    	Network prefix
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: prefix_length
                    
                    	Prefix length
                    	**type**\:  int
                    
                    	**range:** 0..32
                    
                    .. attribute:: prefix_length_xr
                    
                    	Prefix length of IP address
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: route_summary
                    
                    	Summary route placeholder indicator
                    	**type**\:  bool
                    
                    .. attribute:: route_tag
                    
                    	Generic route information
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: route_type
                    
                    	Type of this route
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: version
                    
                    	RIB supplied version number
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'ip-rip-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Rip.Protocol.DefaultVrf.Routes.Route, self).__init__()

                        self.yang_name = "route"
                        self.yang_parent_name = "routes"

                        self.active = YLeaf(YType.boolean, "active")

                        self.attributes = YLeaf(YType.uint32, "attributes")

                        self.bgp_count = YLeaf(YType.uint16, "bgp-count")

                        self.destination_address = YLeaf(YType.str, "destination-address")

                        self.distance = YLeaf(YType.uint16, "distance")

                        self.hold_down = YLeaf(YType.boolean, "hold-down")

                        self.path_origin = YLeaf(YType.enumeration, "path-origin")

                        self.prefix = YLeaf(YType.str, "prefix")

                        self.prefix_length = YLeaf(YType.uint32, "prefix-length")

                        self.prefix_length_xr = YLeaf(YType.uint32, "prefix-length-xr")

                        self.route_summary = YLeaf(YType.boolean, "route-summary")

                        self.route_tag = YLeaf(YType.uint16, "route-tag")

                        self.route_type = YLeaf(YType.uint16, "route-type")

                        self.version = YLeaf(YType.uint8, "version")

                        self.paths = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("active",
                                        "attributes",
                                        "bgp_count",
                                        "destination_address",
                                        "distance",
                                        "hold_down",
                                        "path_origin",
                                        "prefix",
                                        "prefix_length",
                                        "prefix_length_xr",
                                        "route_summary",
                                        "route_tag",
                                        "route_type",
                                        "version") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Rip.Protocol.DefaultVrf.Routes.Route, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Rip.Protocol.DefaultVrf.Routes.Route, self).__setattr__(name, value)


                    class Paths(Entity):
                        """
                        The paths for this route
                        
                        .. attribute:: interface
                        
                        	Interface
                        	**type**\:  str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        .. attribute:: is_permanent
                        
                        	Permanent indicator
                        	**type**\:  bool
                        
                        .. attribute:: metric
                        
                        	Metric
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: next_hop_address
                        
                        	Next hop address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: source_address
                        
                        	Source address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: tag
                        
                        	Tag
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: uptime
                        
                        	Up time
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ip-rip-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Rip.Protocol.DefaultVrf.Routes.Route.Paths, self).__init__()

                            self.yang_name = "paths"
                            self.yang_parent_name = "route"

                            self.interface = YLeaf(YType.str, "interface")

                            self.is_permanent = YLeaf(YType.boolean, "is-permanent")

                            self.metric = YLeaf(YType.uint16, "metric")

                            self.next_hop_address = YLeaf(YType.str, "next-hop-address")

                            self.source_address = YLeaf(YType.str, "source-address")

                            self.tag = YLeaf(YType.uint16, "tag")

                            self.uptime = YLeaf(YType.uint32, "uptime")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("interface",
                                            "is_permanent",
                                            "metric",
                                            "next_hop_address",
                                            "source_address",
                                            "tag",
                                            "uptime") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Rip.Protocol.DefaultVrf.Routes.Route.Paths, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Rip.Protocol.DefaultVrf.Routes.Route.Paths, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.interface.is_set or
                                self.is_permanent.is_set or
                                self.metric.is_set or
                                self.next_hop_address.is_set or
                                self.source_address.is_set or
                                self.tag.is_set or
                                self.uptime.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.interface.yfilter != YFilter.not_set or
                                self.is_permanent.yfilter != YFilter.not_set or
                                self.metric.yfilter != YFilter.not_set or
                                self.next_hop_address.yfilter != YFilter.not_set or
                                self.source_address.yfilter != YFilter.not_set or
                                self.tag.yfilter != YFilter.not_set or
                                self.uptime.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "paths" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                path_buffer = "Cisco-IOS-XR-ip-rip-oper:rip/protocol/default-vrf/routes/route/%s" % self.get_segment_path()
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.interface.is_set or self.interface.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.interface.get_name_leafdata())
                            if (self.is_permanent.is_set or self.is_permanent.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_permanent.get_name_leafdata())
                            if (self.metric.is_set or self.metric.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.metric.get_name_leafdata())
                            if (self.next_hop_address.is_set or self.next_hop_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.next_hop_address.get_name_leafdata())
                            if (self.source_address.is_set or self.source_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.source_address.get_name_leafdata())
                            if (self.tag.is_set or self.tag.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.tag.get_name_leafdata())
                            if (self.uptime.is_set or self.uptime.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.uptime.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "interface" or name == "is-permanent" or name == "metric" or name == "next-hop-address" or name == "source-address" or name == "tag" or name == "uptime"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "interface"):
                                self.interface = value
                                self.interface.value_namespace = name_space
                                self.interface.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-permanent"):
                                self.is_permanent = value
                                self.is_permanent.value_namespace = name_space
                                self.is_permanent.value_namespace_prefix = name_space_prefix
                            if(value_path == "metric"):
                                self.metric = value
                                self.metric.value_namespace = name_space
                                self.metric.value_namespace_prefix = name_space_prefix
                            if(value_path == "next-hop-address"):
                                self.next_hop_address = value
                                self.next_hop_address.value_namespace = name_space
                                self.next_hop_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "source-address"):
                                self.source_address = value
                                self.source_address.value_namespace = name_space
                                self.source_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "tag"):
                                self.tag = value
                                self.tag.value_namespace = name_space
                                self.tag.value_namespace_prefix = name_space_prefix
                            if(value_path == "uptime"):
                                self.uptime = value
                                self.uptime.value_namespace = name_space
                                self.uptime.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.paths:
                            if (c.has_data()):
                                return True
                        return (
                            self.active.is_set or
                            self.attributes.is_set or
                            self.bgp_count.is_set or
                            self.destination_address.is_set or
                            self.distance.is_set or
                            self.hold_down.is_set or
                            self.path_origin.is_set or
                            self.prefix.is_set or
                            self.prefix_length.is_set or
                            self.prefix_length_xr.is_set or
                            self.route_summary.is_set or
                            self.route_tag.is_set or
                            self.route_type.is_set or
                            self.version.is_set)

                    def has_operation(self):
                        for c in self.paths:
                            if (c.has_operation()):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.active.yfilter != YFilter.not_set or
                            self.attributes.yfilter != YFilter.not_set or
                            self.bgp_count.yfilter != YFilter.not_set or
                            self.destination_address.yfilter != YFilter.not_set or
                            self.distance.yfilter != YFilter.not_set or
                            self.hold_down.yfilter != YFilter.not_set or
                            self.path_origin.yfilter != YFilter.not_set or
                            self.prefix.yfilter != YFilter.not_set or
                            self.prefix_length.yfilter != YFilter.not_set or
                            self.prefix_length_xr.yfilter != YFilter.not_set or
                            self.route_summary.yfilter != YFilter.not_set or
                            self.route_tag.yfilter != YFilter.not_set or
                            self.route_type.yfilter != YFilter.not_set or
                            self.version.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "route" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-ip-rip-oper:rip/protocol/default-vrf/routes/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.active.is_set or self.active.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.active.get_name_leafdata())
                        if (self.attributes.is_set or self.attributes.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.attributes.get_name_leafdata())
                        if (self.bgp_count.is_set or self.bgp_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.bgp_count.get_name_leafdata())
                        if (self.destination_address.is_set or self.destination_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.destination_address.get_name_leafdata())
                        if (self.distance.is_set or self.distance.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.distance.get_name_leafdata())
                        if (self.hold_down.is_set or self.hold_down.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.hold_down.get_name_leafdata())
                        if (self.path_origin.is_set or self.path_origin.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.path_origin.get_name_leafdata())
                        if (self.prefix.is_set or self.prefix.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.prefix.get_name_leafdata())
                        if (self.prefix_length.is_set or self.prefix_length.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.prefix_length.get_name_leafdata())
                        if (self.prefix_length_xr.is_set or self.prefix_length_xr.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.prefix_length_xr.get_name_leafdata())
                        if (self.route_summary.is_set or self.route_summary.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.route_summary.get_name_leafdata())
                        if (self.route_tag.is_set or self.route_tag.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.route_tag.get_name_leafdata())
                        if (self.route_type.is_set or self.route_type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.route_type.get_name_leafdata())
                        if (self.version.is_set or self.version.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.version.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "paths"):
                            for c in self.paths:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Rip.Protocol.DefaultVrf.Routes.Route.Paths()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.paths.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "paths" or name == "active" or name == "attributes" or name == "bgp-count" or name == "destination-address" or name == "distance" or name == "hold-down" or name == "path-origin" or name == "prefix" or name == "prefix-length" or name == "prefix-length-xr" or name == "route-summary" or name == "route-tag" or name == "route-type" or name == "version"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "active"):
                            self.active = value
                            self.active.value_namespace = name_space
                            self.active.value_namespace_prefix = name_space_prefix
                        if(value_path == "attributes"):
                            self.attributes = value
                            self.attributes.value_namespace = name_space
                            self.attributes.value_namespace_prefix = name_space_prefix
                        if(value_path == "bgp-count"):
                            self.bgp_count = value
                            self.bgp_count.value_namespace = name_space
                            self.bgp_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "destination-address"):
                            self.destination_address = value
                            self.destination_address.value_namespace = name_space
                            self.destination_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "distance"):
                            self.distance = value
                            self.distance.value_namespace = name_space
                            self.distance.value_namespace_prefix = name_space_prefix
                        if(value_path == "hold-down"):
                            self.hold_down = value
                            self.hold_down.value_namespace = name_space
                            self.hold_down.value_namespace_prefix = name_space_prefix
                        if(value_path == "path-origin"):
                            self.path_origin = value
                            self.path_origin.value_namespace = name_space
                            self.path_origin.value_namespace_prefix = name_space_prefix
                        if(value_path == "prefix"):
                            self.prefix = value
                            self.prefix.value_namespace = name_space
                            self.prefix.value_namespace_prefix = name_space_prefix
                        if(value_path == "prefix-length"):
                            self.prefix_length = value
                            self.prefix_length.value_namespace = name_space
                            self.prefix_length.value_namespace_prefix = name_space_prefix
                        if(value_path == "prefix-length-xr"):
                            self.prefix_length_xr = value
                            self.prefix_length_xr.value_namespace = name_space
                            self.prefix_length_xr.value_namespace_prefix = name_space_prefix
                        if(value_path == "route-summary"):
                            self.route_summary = value
                            self.route_summary.value_namespace = name_space
                            self.route_summary.value_namespace_prefix = name_space_prefix
                        if(value_path == "route-tag"):
                            self.route_tag = value
                            self.route_tag.value_namespace = name_space
                            self.route_tag.value_namespace_prefix = name_space_prefix
                        if(value_path == "route-type"):
                            self.route_type = value
                            self.route_type.value_namespace = name_space
                            self.route_type.value_namespace_prefix = name_space_prefix
                        if(value_path == "version"):
                            self.version = value
                            self.version.value_namespace = name_space
                            self.version.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.route:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.route:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "routes" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ip-rip-oper:rip/protocol/default-vrf/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "route"):
                        for c in self.route:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Rip.Protocol.DefaultVrf.Routes.Route()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.route.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "route"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Configuration(Entity):
                """
                RIP global configuration
                
                .. attribute:: active
                
                	VRF active indicator
                	**type**\:  bool
                
                .. attribute:: auto_summarize
                
                	Auto\-summarization indicator
                	**type**\:  bool
                
                .. attribute:: default_metric
                
                	Default metric for RIP routes
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: flash_threshold
                
                	Flash update threshold
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: flush_timer
                
                	Flush timer
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: hold_down_timer
                
                	Holddown timer
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: input_q_length
                
                	Length of the input queue
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: invalid_timer
                
                	Invalid timer
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: maximum_paths
                
                	Maximum number of paths a route can have
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: multicast_address
                
                	Use broadcast/multicast address indicator
                	**type**\:  bool
                
                .. attribute:: next_update_time
                
                	Time left for next update
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: nsf_life_time
                
                	NSF life time
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: nsf_status
                
                	NSF Enable status
                	**type**\:  bool
                
                .. attribute:: oom_flags
                
                	Out\-of\-memory status flags
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: rip_version
                
                	Version of RIP configured
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: triggered_rip
                
                	Triggered RIP enabled indicator
                	**type**\:  bool
                
                .. attribute:: update_timer
                
                	Update timer
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: validation_indicator
                
                	Incoming packet source validation indicator
                	**type**\:  bool
                
                .. attribute:: vr_fised_socket
                
                	VRF added to socket indicator
                	**type**\:  bool
                
                

                """

                _prefix = 'ip-rip-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rip.Protocol.DefaultVrf.Configuration, self).__init__()

                    self.yang_name = "configuration"
                    self.yang_parent_name = "default-vrf"

                    self.active = YLeaf(YType.boolean, "active")

                    self.auto_summarize = YLeaf(YType.boolean, "auto-summarize")

                    self.default_metric = YLeaf(YType.uint8, "default-metric")

                    self.flash_threshold = YLeaf(YType.uint8, "flash-threshold")

                    self.flush_timer = YLeaf(YType.uint32, "flush-timer")

                    self.hold_down_timer = YLeaf(YType.uint32, "hold-down-timer")

                    self.input_q_length = YLeaf(YType.uint16, "input-q-length")

                    self.invalid_timer = YLeaf(YType.uint32, "invalid-timer")

                    self.maximum_paths = YLeaf(YType.uint8, "maximum-paths")

                    self.multicast_address = YLeaf(YType.boolean, "multicast-address")

                    self.next_update_time = YLeaf(YType.uint32, "next-update-time")

                    self.nsf_life_time = YLeaf(YType.uint32, "nsf-life-time")

                    self.nsf_status = YLeaf(YType.boolean, "nsf-status")

                    self.oom_flags = YLeaf(YType.uint32, "oom-flags")

                    self.rip_version = YLeaf(YType.int32, "rip-version")

                    self.triggered_rip = YLeaf(YType.boolean, "triggered-rip")

                    self.update_timer = YLeaf(YType.uint32, "update-timer")

                    self.validation_indicator = YLeaf(YType.boolean, "validation-indicator")

                    self.vr_fised_socket = YLeaf(YType.boolean, "vr-fised-socket")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("active",
                                    "auto_summarize",
                                    "default_metric",
                                    "flash_threshold",
                                    "flush_timer",
                                    "hold_down_timer",
                                    "input_q_length",
                                    "invalid_timer",
                                    "maximum_paths",
                                    "multicast_address",
                                    "next_update_time",
                                    "nsf_life_time",
                                    "nsf_status",
                                    "oom_flags",
                                    "rip_version",
                                    "triggered_rip",
                                    "update_timer",
                                    "validation_indicator",
                                    "vr_fised_socket") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Rip.Protocol.DefaultVrf.Configuration, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Rip.Protocol.DefaultVrf.Configuration, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.active.is_set or
                        self.auto_summarize.is_set or
                        self.default_metric.is_set or
                        self.flash_threshold.is_set or
                        self.flush_timer.is_set or
                        self.hold_down_timer.is_set or
                        self.input_q_length.is_set or
                        self.invalid_timer.is_set or
                        self.maximum_paths.is_set or
                        self.multicast_address.is_set or
                        self.next_update_time.is_set or
                        self.nsf_life_time.is_set or
                        self.nsf_status.is_set or
                        self.oom_flags.is_set or
                        self.rip_version.is_set or
                        self.triggered_rip.is_set or
                        self.update_timer.is_set or
                        self.validation_indicator.is_set or
                        self.vr_fised_socket.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.active.yfilter != YFilter.not_set or
                        self.auto_summarize.yfilter != YFilter.not_set or
                        self.default_metric.yfilter != YFilter.not_set or
                        self.flash_threshold.yfilter != YFilter.not_set or
                        self.flush_timer.yfilter != YFilter.not_set or
                        self.hold_down_timer.yfilter != YFilter.not_set or
                        self.input_q_length.yfilter != YFilter.not_set or
                        self.invalid_timer.yfilter != YFilter.not_set or
                        self.maximum_paths.yfilter != YFilter.not_set or
                        self.multicast_address.yfilter != YFilter.not_set or
                        self.next_update_time.yfilter != YFilter.not_set or
                        self.nsf_life_time.yfilter != YFilter.not_set or
                        self.nsf_status.yfilter != YFilter.not_set or
                        self.oom_flags.yfilter != YFilter.not_set or
                        self.rip_version.yfilter != YFilter.not_set or
                        self.triggered_rip.yfilter != YFilter.not_set or
                        self.update_timer.yfilter != YFilter.not_set or
                        self.validation_indicator.yfilter != YFilter.not_set or
                        self.vr_fised_socket.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "configuration" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ip-rip-oper:rip/protocol/default-vrf/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.active.is_set or self.active.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.active.get_name_leafdata())
                    if (self.auto_summarize.is_set or self.auto_summarize.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.auto_summarize.get_name_leafdata())
                    if (self.default_metric.is_set or self.default_metric.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.default_metric.get_name_leafdata())
                    if (self.flash_threshold.is_set or self.flash_threshold.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.flash_threshold.get_name_leafdata())
                    if (self.flush_timer.is_set or self.flush_timer.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.flush_timer.get_name_leafdata())
                    if (self.hold_down_timer.is_set or self.hold_down_timer.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.hold_down_timer.get_name_leafdata())
                    if (self.input_q_length.is_set or self.input_q_length.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.input_q_length.get_name_leafdata())
                    if (self.invalid_timer.is_set or self.invalid_timer.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.invalid_timer.get_name_leafdata())
                    if (self.maximum_paths.is_set or self.maximum_paths.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.maximum_paths.get_name_leafdata())
                    if (self.multicast_address.is_set or self.multicast_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.multicast_address.get_name_leafdata())
                    if (self.next_update_time.is_set or self.next_update_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.next_update_time.get_name_leafdata())
                    if (self.nsf_life_time.is_set or self.nsf_life_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.nsf_life_time.get_name_leafdata())
                    if (self.nsf_status.is_set or self.nsf_status.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.nsf_status.get_name_leafdata())
                    if (self.oom_flags.is_set or self.oom_flags.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.oom_flags.get_name_leafdata())
                    if (self.rip_version.is_set or self.rip_version.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rip_version.get_name_leafdata())
                    if (self.triggered_rip.is_set or self.triggered_rip.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.triggered_rip.get_name_leafdata())
                    if (self.update_timer.is_set or self.update_timer.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.update_timer.get_name_leafdata())
                    if (self.validation_indicator.is_set or self.validation_indicator.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.validation_indicator.get_name_leafdata())
                    if (self.vr_fised_socket.is_set or self.vr_fised_socket.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.vr_fised_socket.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "active" or name == "auto-summarize" or name == "default-metric" or name == "flash-threshold" or name == "flush-timer" or name == "hold-down-timer" or name == "input-q-length" or name == "invalid-timer" or name == "maximum-paths" or name == "multicast-address" or name == "next-update-time" or name == "nsf-life-time" or name == "nsf-status" or name == "oom-flags" or name == "rip-version" or name == "triggered-rip" or name == "update-timer" or name == "validation-indicator" or name == "vr-fised-socket"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "active"):
                        self.active = value
                        self.active.value_namespace = name_space
                        self.active.value_namespace_prefix = name_space_prefix
                    if(value_path == "auto-summarize"):
                        self.auto_summarize = value
                        self.auto_summarize.value_namespace = name_space
                        self.auto_summarize.value_namespace_prefix = name_space_prefix
                    if(value_path == "default-metric"):
                        self.default_metric = value
                        self.default_metric.value_namespace = name_space
                        self.default_metric.value_namespace_prefix = name_space_prefix
                    if(value_path == "flash-threshold"):
                        self.flash_threshold = value
                        self.flash_threshold.value_namespace = name_space
                        self.flash_threshold.value_namespace_prefix = name_space_prefix
                    if(value_path == "flush-timer"):
                        self.flush_timer = value
                        self.flush_timer.value_namespace = name_space
                        self.flush_timer.value_namespace_prefix = name_space_prefix
                    if(value_path == "hold-down-timer"):
                        self.hold_down_timer = value
                        self.hold_down_timer.value_namespace = name_space
                        self.hold_down_timer.value_namespace_prefix = name_space_prefix
                    if(value_path == "input-q-length"):
                        self.input_q_length = value
                        self.input_q_length.value_namespace = name_space
                        self.input_q_length.value_namespace_prefix = name_space_prefix
                    if(value_path == "invalid-timer"):
                        self.invalid_timer = value
                        self.invalid_timer.value_namespace = name_space
                        self.invalid_timer.value_namespace_prefix = name_space_prefix
                    if(value_path == "maximum-paths"):
                        self.maximum_paths = value
                        self.maximum_paths.value_namespace = name_space
                        self.maximum_paths.value_namespace_prefix = name_space_prefix
                    if(value_path == "multicast-address"):
                        self.multicast_address = value
                        self.multicast_address.value_namespace = name_space
                        self.multicast_address.value_namespace_prefix = name_space_prefix
                    if(value_path == "next-update-time"):
                        self.next_update_time = value
                        self.next_update_time.value_namespace = name_space
                        self.next_update_time.value_namespace_prefix = name_space_prefix
                    if(value_path == "nsf-life-time"):
                        self.nsf_life_time = value
                        self.nsf_life_time.value_namespace = name_space
                        self.nsf_life_time.value_namespace_prefix = name_space_prefix
                    if(value_path == "nsf-status"):
                        self.nsf_status = value
                        self.nsf_status.value_namespace = name_space
                        self.nsf_status.value_namespace_prefix = name_space_prefix
                    if(value_path == "oom-flags"):
                        self.oom_flags = value
                        self.oom_flags.value_namespace = name_space
                        self.oom_flags.value_namespace_prefix = name_space_prefix
                    if(value_path == "rip-version"):
                        self.rip_version = value
                        self.rip_version.value_namespace = name_space
                        self.rip_version.value_namespace_prefix = name_space_prefix
                    if(value_path == "triggered-rip"):
                        self.triggered_rip = value
                        self.triggered_rip.value_namespace = name_space
                        self.triggered_rip.value_namespace_prefix = name_space_prefix
                    if(value_path == "update-timer"):
                        self.update_timer = value
                        self.update_timer.value_namespace = name_space
                        self.update_timer.value_namespace_prefix = name_space_prefix
                    if(value_path == "validation-indicator"):
                        self.validation_indicator = value
                        self.validation_indicator.value_namespace = name_space
                        self.validation_indicator.value_namespace_prefix = name_space_prefix
                    if(value_path == "vr-fised-socket"):
                        self.vr_fised_socket = value
                        self.vr_fised_socket.value_namespace = name_space
                        self.vr_fised_socket.value_namespace_prefix = name_space_prefix


            class Statistics(Entity):
                """
                RIP statistics information
                
                .. attribute:: discarded_packets
                
                	Total discarded packets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: discarded_routes
                
                	Total discarded routes
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: path_count
                
                	Number of paths allocated
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: path_malloc_failures
                
                	Number of failures to allocate memory for a path
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: periodic_updates
                
                	Number of periodic RIP updates
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: query_responses
                
                	Number of RIP queries responded to
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: received_packets
                
                	Total packets received
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: rib_updates
                
                	Number of route updates to RIB made by RIP
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: route_count
                
                	Number of routes allocated
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: route_malloc_failures
                
                	Number of failures to allocate memory for a route
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: sent_message_failures
                
                	Number of message send failures
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: sent_messages
                
                	Number of messages sent
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: standby_packets_received
                
                	Packets rx in SRP
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ip-rip-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rip.Protocol.DefaultVrf.Statistics, self).__init__()

                    self.yang_name = "statistics"
                    self.yang_parent_name = "default-vrf"

                    self.discarded_packets = YLeaf(YType.uint32, "discarded-packets")

                    self.discarded_routes = YLeaf(YType.uint32, "discarded-routes")

                    self.path_count = YLeaf(YType.uint32, "path-count")

                    self.path_malloc_failures = YLeaf(YType.uint32, "path-malloc-failures")

                    self.periodic_updates = YLeaf(YType.uint32, "periodic-updates")

                    self.query_responses = YLeaf(YType.uint32, "query-responses")

                    self.received_packets = YLeaf(YType.uint32, "received-packets")

                    self.rib_updates = YLeaf(YType.uint32, "rib-updates")

                    self.route_count = YLeaf(YType.uint32, "route-count")

                    self.route_malloc_failures = YLeaf(YType.uint32, "route-malloc-failures")

                    self.sent_message_failures = YLeaf(YType.uint32, "sent-message-failures")

                    self.sent_messages = YLeaf(YType.uint32, "sent-messages")

                    self.standby_packets_received = YLeaf(YType.uint32, "standby-packets-received")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("discarded_packets",
                                    "discarded_routes",
                                    "path_count",
                                    "path_malloc_failures",
                                    "periodic_updates",
                                    "query_responses",
                                    "received_packets",
                                    "rib_updates",
                                    "route_count",
                                    "route_malloc_failures",
                                    "sent_message_failures",
                                    "sent_messages",
                                    "standby_packets_received") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Rip.Protocol.DefaultVrf.Statistics, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Rip.Protocol.DefaultVrf.Statistics, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.discarded_packets.is_set or
                        self.discarded_routes.is_set or
                        self.path_count.is_set or
                        self.path_malloc_failures.is_set or
                        self.periodic_updates.is_set or
                        self.query_responses.is_set or
                        self.received_packets.is_set or
                        self.rib_updates.is_set or
                        self.route_count.is_set or
                        self.route_malloc_failures.is_set or
                        self.sent_message_failures.is_set or
                        self.sent_messages.is_set or
                        self.standby_packets_received.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.discarded_packets.yfilter != YFilter.not_set or
                        self.discarded_routes.yfilter != YFilter.not_set or
                        self.path_count.yfilter != YFilter.not_set or
                        self.path_malloc_failures.yfilter != YFilter.not_set or
                        self.periodic_updates.yfilter != YFilter.not_set or
                        self.query_responses.yfilter != YFilter.not_set or
                        self.received_packets.yfilter != YFilter.not_set or
                        self.rib_updates.yfilter != YFilter.not_set or
                        self.route_count.yfilter != YFilter.not_set or
                        self.route_malloc_failures.yfilter != YFilter.not_set or
                        self.sent_message_failures.yfilter != YFilter.not_set or
                        self.sent_messages.yfilter != YFilter.not_set or
                        self.standby_packets_received.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "statistics" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ip-rip-oper:rip/protocol/default-vrf/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.discarded_packets.is_set or self.discarded_packets.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.discarded_packets.get_name_leafdata())
                    if (self.discarded_routes.is_set or self.discarded_routes.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.discarded_routes.get_name_leafdata())
                    if (self.path_count.is_set or self.path_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.path_count.get_name_leafdata())
                    if (self.path_malloc_failures.is_set or self.path_malloc_failures.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.path_malloc_failures.get_name_leafdata())
                    if (self.periodic_updates.is_set or self.periodic_updates.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.periodic_updates.get_name_leafdata())
                    if (self.query_responses.is_set or self.query_responses.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.query_responses.get_name_leafdata())
                    if (self.received_packets.is_set or self.received_packets.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.received_packets.get_name_leafdata())
                    if (self.rib_updates.is_set or self.rib_updates.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rib_updates.get_name_leafdata())
                    if (self.route_count.is_set or self.route_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.route_count.get_name_leafdata())
                    if (self.route_malloc_failures.is_set or self.route_malloc_failures.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.route_malloc_failures.get_name_leafdata())
                    if (self.sent_message_failures.is_set or self.sent_message_failures.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.sent_message_failures.get_name_leafdata())
                    if (self.sent_messages.is_set or self.sent_messages.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.sent_messages.get_name_leafdata())
                    if (self.standby_packets_received.is_set or self.standby_packets_received.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.standby_packets_received.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "discarded-packets" or name == "discarded-routes" or name == "path-count" or name == "path-malloc-failures" or name == "periodic-updates" or name == "query-responses" or name == "received-packets" or name == "rib-updates" or name == "route-count" or name == "route-malloc-failures" or name == "sent-message-failures" or name == "sent-messages" or name == "standby-packets-received"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "discarded-packets"):
                        self.discarded_packets = value
                        self.discarded_packets.value_namespace = name_space
                        self.discarded_packets.value_namespace_prefix = name_space_prefix
                    if(value_path == "discarded-routes"):
                        self.discarded_routes = value
                        self.discarded_routes.value_namespace = name_space
                        self.discarded_routes.value_namespace_prefix = name_space_prefix
                    if(value_path == "path-count"):
                        self.path_count = value
                        self.path_count.value_namespace = name_space
                        self.path_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "path-malloc-failures"):
                        self.path_malloc_failures = value
                        self.path_malloc_failures.value_namespace = name_space
                        self.path_malloc_failures.value_namespace_prefix = name_space_prefix
                    if(value_path == "periodic-updates"):
                        self.periodic_updates = value
                        self.periodic_updates.value_namespace = name_space
                        self.periodic_updates.value_namespace_prefix = name_space_prefix
                    if(value_path == "query-responses"):
                        self.query_responses = value
                        self.query_responses.value_namespace = name_space
                        self.query_responses.value_namespace_prefix = name_space_prefix
                    if(value_path == "received-packets"):
                        self.received_packets = value
                        self.received_packets.value_namespace = name_space
                        self.received_packets.value_namespace_prefix = name_space_prefix
                    if(value_path == "rib-updates"):
                        self.rib_updates = value
                        self.rib_updates.value_namespace = name_space
                        self.rib_updates.value_namespace_prefix = name_space_prefix
                    if(value_path == "route-count"):
                        self.route_count = value
                        self.route_count.value_namespace = name_space
                        self.route_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "route-malloc-failures"):
                        self.route_malloc_failures = value
                        self.route_malloc_failures.value_namespace = name_space
                        self.route_malloc_failures.value_namespace_prefix = name_space_prefix
                    if(value_path == "sent-message-failures"):
                        self.sent_message_failures = value
                        self.sent_message_failures.value_namespace = name_space
                        self.sent_message_failures.value_namespace_prefix = name_space_prefix
                    if(value_path == "sent-messages"):
                        self.sent_messages = value
                        self.sent_messages.value_namespace = name_space
                        self.sent_messages.value_namespace_prefix = name_space_prefix
                    if(value_path == "standby-packets-received"):
                        self.standby_packets_received = value
                        self.standby_packets_received.value_namespace = name_space
                        self.standby_packets_received.value_namespace_prefix = name_space_prefix


            class Interfaces(Entity):
                """
                RIP interfaces
                
                .. attribute:: interface
                
                	Information about a particular RIP interface
                	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Protocol.DefaultVrf.Interfaces.Interface>`
                
                

                """

                _prefix = 'ip-rip-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rip.Protocol.DefaultVrf.Interfaces, self).__init__()

                    self.yang_name = "interfaces"
                    self.yang_parent_name = "default-vrf"

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
                        if name in () and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Rip.Protocol.DefaultVrf.Interfaces, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Rip.Protocol.DefaultVrf.Interfaces, self).__setattr__(name, value)


                class Interface(Entity):
                    """
                    Information about a particular RIP interface
                    
                    .. attribute:: interface_name  <key>
                    
                    	Interface name
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: accept_metric
                    
                    	Accept routes of metric 0 indicator
                    	**type**\:  bool
                    
                    .. attribute:: auth_key_md5
                    
                    	Authentication key programmed with MD5 algorithm
                    	**type**\:  bool
                    
                    .. attribute:: auth_key_send_id
                    
                    	Current active Send Authentication Key Id
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: auth_keychain
                    
                    	Authentication Keychain Name
                    	**type**\:  str
                    
                    .. attribute:: auth_mode
                    
                    	Authentication Mode
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: destination_address
                    
                    	IP Address of this interface
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: if_handle
                    
                    	Interface handle
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: interface
                    
                    	Interface name
                    	**type**\:  str
                    
                    .. attribute:: is_passive_interface
                    
                    	Passive interface indicator
                    	**type**\:  bool
                    
                    .. attribute:: join_status
                    
                    	Multicast group join status
                    	**type**\:  bool
                    
                    .. attribute:: lpts_state
                    
                    	LPTSState
                    	**type**\:  bool
                    
                    .. attribute:: metric_cost
                    
                    	Cost added to routes through this interface
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: multicast_address
                    
                    	Use broadcast address for v2 packets
                    	**type**\:  bool
                    
                    .. attribute:: neighbor_address
                    
                    	Interface's triggered RIP neighbor
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: oom_flags
                    
                    	Out\-of\-memory status flags
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: pkt_accepted_valid_auth
                    
                    	Packets accepted with valid authentication data
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: pkt_drop_invalid_auth
                    
                    	Packets dropped due to invalid authentication data
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: pkt_drop_no_auth
                    
                    	Packets dropped due to missing authentication data
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: pkt_drop_wrong_kc
                    
                    	Packets dropped due to wrong keychain configured
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: poison_horizon
                    
                    	Poisoned reverse enabled indicator
                    	**type**\:  bool
                    
                    .. attribute:: prefix_length
                    
                    	Prefix length of the IP address
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: receive_version
                    
                    	Versions that the interface will recieve
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rip_enabled
                    
                    	Whether RIP is enabled on this interface
                    	**type**\:  bool
                    
                    .. attribute:: rip_peer
                    
                    	Neighbors on this interface
                    	**type**\: list of    :py:class:`RipPeer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Protocol.DefaultVrf.Interfaces.Interface.RipPeer>`
                    
                    .. attribute:: rip_summary
                    
                    	User defined summary addresses
                    	**type**\: list of    :py:class:`RipSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Protocol.DefaultVrf.Interfaces.Interface.RipSummary>`
                    
                    .. attribute:: send_auth_key_exists
                    
                    	Authentication send key exists
                    	**type**\:  bool
                    
                    .. attribute:: send_version
                    
                    	Versions that the interface is sending
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: split_horizon
                    
                    	Split horizon enabled indicator
                    	**type**\:  bool
                    
                    .. attribute:: state
                    
                    	Current state of the interface
                    	**type**\:   :py:class:`InterfaceState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.InterfaceState>`
                    
                    .. attribute:: total_pkt_recvd
                    
                    	Total packets received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: triggered_rip
                    
                    	Triggered RIP enabled indicator
                    	**type**\:  bool
                    
                    

                    """

                    _prefix = 'ip-rip-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Rip.Protocol.DefaultVrf.Interfaces.Interface, self).__init__()

                        self.yang_name = "interface"
                        self.yang_parent_name = "interfaces"

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.accept_metric = YLeaf(YType.boolean, "accept-metric")

                        self.auth_key_md5 = YLeaf(YType.boolean, "auth-key-md5")

                        self.auth_key_send_id = YLeaf(YType.uint64, "auth-key-send-id")

                        self.auth_keychain = YLeaf(YType.str, "auth-keychain")

                        self.auth_mode = YLeaf(YType.uint32, "auth-mode")

                        self.destination_address = YLeaf(YType.str, "destination-address")

                        self.if_handle = YLeaf(YType.str, "if-handle")

                        self.interface = YLeaf(YType.str, "interface")

                        self.is_passive_interface = YLeaf(YType.boolean, "is-passive-interface")

                        self.join_status = YLeaf(YType.boolean, "join-status")

                        self.lpts_state = YLeaf(YType.boolean, "lpts-state")

                        self.metric_cost = YLeaf(YType.uint32, "metric-cost")

                        self.multicast_address = YLeaf(YType.boolean, "multicast-address")

                        self.neighbor_address = YLeaf(YType.str, "neighbor-address")

                        self.oom_flags = YLeaf(YType.uint32, "oom-flags")

                        self.pkt_accepted_valid_auth = YLeaf(YType.uint32, "pkt-accepted-valid-auth")

                        self.pkt_drop_invalid_auth = YLeaf(YType.uint32, "pkt-drop-invalid-auth")

                        self.pkt_drop_no_auth = YLeaf(YType.uint32, "pkt-drop-no-auth")

                        self.pkt_drop_wrong_kc = YLeaf(YType.uint32, "pkt-drop-wrong-kc")

                        self.poison_horizon = YLeaf(YType.boolean, "poison-horizon")

                        self.prefix_length = YLeaf(YType.uint32, "prefix-length")

                        self.receive_version = YLeaf(YType.uint32, "receive-version")

                        self.rip_enabled = YLeaf(YType.boolean, "rip-enabled")

                        self.send_auth_key_exists = YLeaf(YType.boolean, "send-auth-key-exists")

                        self.send_version = YLeaf(YType.uint32, "send-version")

                        self.split_horizon = YLeaf(YType.boolean, "split-horizon")

                        self.state = YLeaf(YType.enumeration, "state")

                        self.total_pkt_recvd = YLeaf(YType.uint32, "total-pkt-recvd")

                        self.triggered_rip = YLeaf(YType.boolean, "triggered-rip")

                        self.rip_peer = YList(self)
                        self.rip_summary = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("interface_name",
                                        "accept_metric",
                                        "auth_key_md5",
                                        "auth_key_send_id",
                                        "auth_keychain",
                                        "auth_mode",
                                        "destination_address",
                                        "if_handle",
                                        "interface",
                                        "is_passive_interface",
                                        "join_status",
                                        "lpts_state",
                                        "metric_cost",
                                        "multicast_address",
                                        "neighbor_address",
                                        "oom_flags",
                                        "pkt_accepted_valid_auth",
                                        "pkt_drop_invalid_auth",
                                        "pkt_drop_no_auth",
                                        "pkt_drop_wrong_kc",
                                        "poison_horizon",
                                        "prefix_length",
                                        "receive_version",
                                        "rip_enabled",
                                        "send_auth_key_exists",
                                        "send_version",
                                        "split_horizon",
                                        "state",
                                        "total_pkt_recvd",
                                        "triggered_rip") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Rip.Protocol.DefaultVrf.Interfaces.Interface, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Rip.Protocol.DefaultVrf.Interfaces.Interface, self).__setattr__(name, value)


                    class RipSummary(Entity):
                        """
                        User defined summary addresses
                        
                        .. attribute:: metric
                        
                        	Summary metric
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: next_hop_address
                        
                        	Summary address next hop
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: prefix
                        
                        	Summary address prefix
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: prefix_length
                        
                        	Summary address prefix length
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ip-rip-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Rip.Protocol.DefaultVrf.Interfaces.Interface.RipSummary, self).__init__()

                            self.yang_name = "rip-summary"
                            self.yang_parent_name = "interface"

                            self.metric = YLeaf(YType.int32, "metric")

                            self.next_hop_address = YLeaf(YType.str, "next-hop-address")

                            self.prefix = YLeaf(YType.str, "prefix")

                            self.prefix_length = YLeaf(YType.uint32, "prefix-length")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("metric",
                                            "next_hop_address",
                                            "prefix",
                                            "prefix_length") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Rip.Protocol.DefaultVrf.Interfaces.Interface.RipSummary, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Rip.Protocol.DefaultVrf.Interfaces.Interface.RipSummary, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.metric.is_set or
                                self.next_hop_address.is_set or
                                self.prefix.is_set or
                                self.prefix_length.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.metric.yfilter != YFilter.not_set or
                                self.next_hop_address.yfilter != YFilter.not_set or
                                self.prefix.yfilter != YFilter.not_set or
                                self.prefix_length.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "rip-summary" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.metric.is_set or self.metric.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.metric.get_name_leafdata())
                            if (self.next_hop_address.is_set or self.next_hop_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.next_hop_address.get_name_leafdata())
                            if (self.prefix.is_set or self.prefix.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.prefix.get_name_leafdata())
                            if (self.prefix_length.is_set or self.prefix_length.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.prefix_length.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "metric" or name == "next-hop-address" or name == "prefix" or name == "prefix-length"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "metric"):
                                self.metric = value
                                self.metric.value_namespace = name_space
                                self.metric.value_namespace_prefix = name_space_prefix
                            if(value_path == "next-hop-address"):
                                self.next_hop_address = value
                                self.next_hop_address.value_namespace = name_space
                                self.next_hop_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "prefix"):
                                self.prefix = value
                                self.prefix.value_namespace = name_space
                                self.prefix.value_namespace_prefix = name_space_prefix
                            if(value_path == "prefix-length"):
                                self.prefix_length = value
                                self.prefix_length.value_namespace = name_space
                                self.prefix_length.value_namespace_prefix = name_space_prefix


                    class RipPeer(Entity):
                        """
                        Neighbors on this interface
                        
                        .. attribute:: discarded_peer_packets
                        
                        	Discarded packets from this peer
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: discarded_peer_routes
                        
                        	Discarded routes from this peer
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: peer_address
                        
                        	IP Address of this peer
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: peer_uptime
                        
                        	Uptime of this peer
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: peer_version
                        
                        	RIP version for this peer
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        

                        """

                        _prefix = 'ip-rip-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Rip.Protocol.DefaultVrf.Interfaces.Interface.RipPeer, self).__init__()

                            self.yang_name = "rip-peer"
                            self.yang_parent_name = "interface"

                            self.discarded_peer_packets = YLeaf(YType.uint32, "discarded-peer-packets")

                            self.discarded_peer_routes = YLeaf(YType.uint32, "discarded-peer-routes")

                            self.peer_address = YLeaf(YType.str, "peer-address")

                            self.peer_uptime = YLeaf(YType.uint32, "peer-uptime")

                            self.peer_version = YLeaf(YType.uint8, "peer-version")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("discarded_peer_packets",
                                            "discarded_peer_routes",
                                            "peer_address",
                                            "peer_uptime",
                                            "peer_version") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Rip.Protocol.DefaultVrf.Interfaces.Interface.RipPeer, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Rip.Protocol.DefaultVrf.Interfaces.Interface.RipPeer, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.discarded_peer_packets.is_set or
                                self.discarded_peer_routes.is_set or
                                self.peer_address.is_set or
                                self.peer_uptime.is_set or
                                self.peer_version.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.discarded_peer_packets.yfilter != YFilter.not_set or
                                self.discarded_peer_routes.yfilter != YFilter.not_set or
                                self.peer_address.yfilter != YFilter.not_set or
                                self.peer_uptime.yfilter != YFilter.not_set or
                                self.peer_version.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "rip-peer" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.discarded_peer_packets.is_set or self.discarded_peer_packets.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.discarded_peer_packets.get_name_leafdata())
                            if (self.discarded_peer_routes.is_set or self.discarded_peer_routes.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.discarded_peer_routes.get_name_leafdata())
                            if (self.peer_address.is_set or self.peer_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.peer_address.get_name_leafdata())
                            if (self.peer_uptime.is_set or self.peer_uptime.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.peer_uptime.get_name_leafdata())
                            if (self.peer_version.is_set or self.peer_version.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.peer_version.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "discarded-peer-packets" or name == "discarded-peer-routes" or name == "peer-address" or name == "peer-uptime" or name == "peer-version"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "discarded-peer-packets"):
                                self.discarded_peer_packets = value
                                self.discarded_peer_packets.value_namespace = name_space
                                self.discarded_peer_packets.value_namespace_prefix = name_space_prefix
                            if(value_path == "discarded-peer-routes"):
                                self.discarded_peer_routes = value
                                self.discarded_peer_routes.value_namespace = name_space
                                self.discarded_peer_routes.value_namespace_prefix = name_space_prefix
                            if(value_path == "peer-address"):
                                self.peer_address = value
                                self.peer_address.value_namespace = name_space
                                self.peer_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "peer-uptime"):
                                self.peer_uptime = value
                                self.peer_uptime.value_namespace = name_space
                                self.peer_uptime.value_namespace_prefix = name_space_prefix
                            if(value_path == "peer-version"):
                                self.peer_version = value
                                self.peer_version.value_namespace = name_space
                                self.peer_version.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.rip_peer:
                            if (c.has_data()):
                                return True
                        for c in self.rip_summary:
                            if (c.has_data()):
                                return True
                        return (
                            self.interface_name.is_set or
                            self.accept_metric.is_set or
                            self.auth_key_md5.is_set or
                            self.auth_key_send_id.is_set or
                            self.auth_keychain.is_set or
                            self.auth_mode.is_set or
                            self.destination_address.is_set or
                            self.if_handle.is_set or
                            self.interface.is_set or
                            self.is_passive_interface.is_set or
                            self.join_status.is_set or
                            self.lpts_state.is_set or
                            self.metric_cost.is_set or
                            self.multicast_address.is_set or
                            self.neighbor_address.is_set or
                            self.oom_flags.is_set or
                            self.pkt_accepted_valid_auth.is_set or
                            self.pkt_drop_invalid_auth.is_set or
                            self.pkt_drop_no_auth.is_set or
                            self.pkt_drop_wrong_kc.is_set or
                            self.poison_horizon.is_set or
                            self.prefix_length.is_set or
                            self.receive_version.is_set or
                            self.rip_enabled.is_set or
                            self.send_auth_key_exists.is_set or
                            self.send_version.is_set or
                            self.split_horizon.is_set or
                            self.state.is_set or
                            self.total_pkt_recvd.is_set or
                            self.triggered_rip.is_set)

                    def has_operation(self):
                        for c in self.rip_peer:
                            if (c.has_operation()):
                                return True
                        for c in self.rip_summary:
                            if (c.has_operation()):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.interface_name.yfilter != YFilter.not_set or
                            self.accept_metric.yfilter != YFilter.not_set or
                            self.auth_key_md5.yfilter != YFilter.not_set or
                            self.auth_key_send_id.yfilter != YFilter.not_set or
                            self.auth_keychain.yfilter != YFilter.not_set or
                            self.auth_mode.yfilter != YFilter.not_set or
                            self.destination_address.yfilter != YFilter.not_set or
                            self.if_handle.yfilter != YFilter.not_set or
                            self.interface.yfilter != YFilter.not_set or
                            self.is_passive_interface.yfilter != YFilter.not_set or
                            self.join_status.yfilter != YFilter.not_set or
                            self.lpts_state.yfilter != YFilter.not_set or
                            self.metric_cost.yfilter != YFilter.not_set or
                            self.multicast_address.yfilter != YFilter.not_set or
                            self.neighbor_address.yfilter != YFilter.not_set or
                            self.oom_flags.yfilter != YFilter.not_set or
                            self.pkt_accepted_valid_auth.yfilter != YFilter.not_set or
                            self.pkt_drop_invalid_auth.yfilter != YFilter.not_set or
                            self.pkt_drop_no_auth.yfilter != YFilter.not_set or
                            self.pkt_drop_wrong_kc.yfilter != YFilter.not_set or
                            self.poison_horizon.yfilter != YFilter.not_set or
                            self.prefix_length.yfilter != YFilter.not_set or
                            self.receive_version.yfilter != YFilter.not_set or
                            self.rip_enabled.yfilter != YFilter.not_set or
                            self.send_auth_key_exists.yfilter != YFilter.not_set or
                            self.send_version.yfilter != YFilter.not_set or
                            self.split_horizon.yfilter != YFilter.not_set or
                            self.state.yfilter != YFilter.not_set or
                            self.total_pkt_recvd.yfilter != YFilter.not_set or
                            self.triggered_rip.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "interface" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-ip-rip-oper:rip/protocol/default-vrf/interfaces/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_name.get_name_leafdata())
                        if (self.accept_metric.is_set or self.accept_metric.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.accept_metric.get_name_leafdata())
                        if (self.auth_key_md5.is_set or self.auth_key_md5.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.auth_key_md5.get_name_leafdata())
                        if (self.auth_key_send_id.is_set or self.auth_key_send_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.auth_key_send_id.get_name_leafdata())
                        if (self.auth_keychain.is_set or self.auth_keychain.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.auth_keychain.get_name_leafdata())
                        if (self.auth_mode.is_set or self.auth_mode.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.auth_mode.get_name_leafdata())
                        if (self.destination_address.is_set or self.destination_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.destination_address.get_name_leafdata())
                        if (self.if_handle.is_set or self.if_handle.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.if_handle.get_name_leafdata())
                        if (self.interface.is_set or self.interface.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface.get_name_leafdata())
                        if (self.is_passive_interface.is_set or self.is_passive_interface.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.is_passive_interface.get_name_leafdata())
                        if (self.join_status.is_set or self.join_status.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.join_status.get_name_leafdata())
                        if (self.lpts_state.is_set or self.lpts_state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.lpts_state.get_name_leafdata())
                        if (self.metric_cost.is_set or self.metric_cost.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.metric_cost.get_name_leafdata())
                        if (self.multicast_address.is_set or self.multicast_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.multicast_address.get_name_leafdata())
                        if (self.neighbor_address.is_set or self.neighbor_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.neighbor_address.get_name_leafdata())
                        if (self.oom_flags.is_set or self.oom_flags.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.oom_flags.get_name_leafdata())
                        if (self.pkt_accepted_valid_auth.is_set or self.pkt_accepted_valid_auth.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pkt_accepted_valid_auth.get_name_leafdata())
                        if (self.pkt_drop_invalid_auth.is_set or self.pkt_drop_invalid_auth.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pkt_drop_invalid_auth.get_name_leafdata())
                        if (self.pkt_drop_no_auth.is_set or self.pkt_drop_no_auth.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pkt_drop_no_auth.get_name_leafdata())
                        if (self.pkt_drop_wrong_kc.is_set or self.pkt_drop_wrong_kc.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pkt_drop_wrong_kc.get_name_leafdata())
                        if (self.poison_horizon.is_set or self.poison_horizon.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.poison_horizon.get_name_leafdata())
                        if (self.prefix_length.is_set or self.prefix_length.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.prefix_length.get_name_leafdata())
                        if (self.receive_version.is_set or self.receive_version.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.receive_version.get_name_leafdata())
                        if (self.rip_enabled.is_set or self.rip_enabled.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.rip_enabled.get_name_leafdata())
                        if (self.send_auth_key_exists.is_set or self.send_auth_key_exists.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.send_auth_key_exists.get_name_leafdata())
                        if (self.send_version.is_set or self.send_version.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.send_version.get_name_leafdata())
                        if (self.split_horizon.is_set or self.split_horizon.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.split_horizon.get_name_leafdata())
                        if (self.state.is_set or self.state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.state.get_name_leafdata())
                        if (self.total_pkt_recvd.is_set or self.total_pkt_recvd.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.total_pkt_recvd.get_name_leafdata())
                        if (self.triggered_rip.is_set or self.triggered_rip.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.triggered_rip.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "rip-peer"):
                            for c in self.rip_peer:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Rip.Protocol.DefaultVrf.Interfaces.Interface.RipPeer()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.rip_peer.append(c)
                            return c

                        if (child_yang_name == "rip-summary"):
                            for c in self.rip_summary:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Rip.Protocol.DefaultVrf.Interfaces.Interface.RipSummary()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.rip_summary.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "rip-peer" or name == "rip-summary" or name == "interface-name" or name == "accept-metric" or name == "auth-key-md5" or name == "auth-key-send-id" or name == "auth-keychain" or name == "auth-mode" or name == "destination-address" or name == "if-handle" or name == "interface" or name == "is-passive-interface" or name == "join-status" or name == "lpts-state" or name == "metric-cost" or name == "multicast-address" or name == "neighbor-address" or name == "oom-flags" or name == "pkt-accepted-valid-auth" or name == "pkt-drop-invalid-auth" or name == "pkt-drop-no-auth" or name == "pkt-drop-wrong-kc" or name == "poison-horizon" or name == "prefix-length" or name == "receive-version" or name == "rip-enabled" or name == "send-auth-key-exists" or name == "send-version" or name == "split-horizon" or name == "state" or name == "total-pkt-recvd" or name == "triggered-rip"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "interface-name"):
                            self.interface_name = value
                            self.interface_name.value_namespace = name_space
                            self.interface_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "accept-metric"):
                            self.accept_metric = value
                            self.accept_metric.value_namespace = name_space
                            self.accept_metric.value_namespace_prefix = name_space_prefix
                        if(value_path == "auth-key-md5"):
                            self.auth_key_md5 = value
                            self.auth_key_md5.value_namespace = name_space
                            self.auth_key_md5.value_namespace_prefix = name_space_prefix
                        if(value_path == "auth-key-send-id"):
                            self.auth_key_send_id = value
                            self.auth_key_send_id.value_namespace = name_space
                            self.auth_key_send_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "auth-keychain"):
                            self.auth_keychain = value
                            self.auth_keychain.value_namespace = name_space
                            self.auth_keychain.value_namespace_prefix = name_space_prefix
                        if(value_path == "auth-mode"):
                            self.auth_mode = value
                            self.auth_mode.value_namespace = name_space
                            self.auth_mode.value_namespace_prefix = name_space_prefix
                        if(value_path == "destination-address"):
                            self.destination_address = value
                            self.destination_address.value_namespace = name_space
                            self.destination_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "if-handle"):
                            self.if_handle = value
                            self.if_handle.value_namespace = name_space
                            self.if_handle.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface"):
                            self.interface = value
                            self.interface.value_namespace = name_space
                            self.interface.value_namespace_prefix = name_space_prefix
                        if(value_path == "is-passive-interface"):
                            self.is_passive_interface = value
                            self.is_passive_interface.value_namespace = name_space
                            self.is_passive_interface.value_namespace_prefix = name_space_prefix
                        if(value_path == "join-status"):
                            self.join_status = value
                            self.join_status.value_namespace = name_space
                            self.join_status.value_namespace_prefix = name_space_prefix
                        if(value_path == "lpts-state"):
                            self.lpts_state = value
                            self.lpts_state.value_namespace = name_space
                            self.lpts_state.value_namespace_prefix = name_space_prefix
                        if(value_path == "metric-cost"):
                            self.metric_cost = value
                            self.metric_cost.value_namespace = name_space
                            self.metric_cost.value_namespace_prefix = name_space_prefix
                        if(value_path == "multicast-address"):
                            self.multicast_address = value
                            self.multicast_address.value_namespace = name_space
                            self.multicast_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "neighbor-address"):
                            self.neighbor_address = value
                            self.neighbor_address.value_namespace = name_space
                            self.neighbor_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "oom-flags"):
                            self.oom_flags = value
                            self.oom_flags.value_namespace = name_space
                            self.oom_flags.value_namespace_prefix = name_space_prefix
                        if(value_path == "pkt-accepted-valid-auth"):
                            self.pkt_accepted_valid_auth = value
                            self.pkt_accepted_valid_auth.value_namespace = name_space
                            self.pkt_accepted_valid_auth.value_namespace_prefix = name_space_prefix
                        if(value_path == "pkt-drop-invalid-auth"):
                            self.pkt_drop_invalid_auth = value
                            self.pkt_drop_invalid_auth.value_namespace = name_space
                            self.pkt_drop_invalid_auth.value_namespace_prefix = name_space_prefix
                        if(value_path == "pkt-drop-no-auth"):
                            self.pkt_drop_no_auth = value
                            self.pkt_drop_no_auth.value_namespace = name_space
                            self.pkt_drop_no_auth.value_namespace_prefix = name_space_prefix
                        if(value_path == "pkt-drop-wrong-kc"):
                            self.pkt_drop_wrong_kc = value
                            self.pkt_drop_wrong_kc.value_namespace = name_space
                            self.pkt_drop_wrong_kc.value_namespace_prefix = name_space_prefix
                        if(value_path == "poison-horizon"):
                            self.poison_horizon = value
                            self.poison_horizon.value_namespace = name_space
                            self.poison_horizon.value_namespace_prefix = name_space_prefix
                        if(value_path == "prefix-length"):
                            self.prefix_length = value
                            self.prefix_length.value_namespace = name_space
                            self.prefix_length.value_namespace_prefix = name_space_prefix
                        if(value_path == "receive-version"):
                            self.receive_version = value
                            self.receive_version.value_namespace = name_space
                            self.receive_version.value_namespace_prefix = name_space_prefix
                        if(value_path == "rip-enabled"):
                            self.rip_enabled = value
                            self.rip_enabled.value_namespace = name_space
                            self.rip_enabled.value_namespace_prefix = name_space_prefix
                        if(value_path == "send-auth-key-exists"):
                            self.send_auth_key_exists = value
                            self.send_auth_key_exists.value_namespace = name_space
                            self.send_auth_key_exists.value_namespace_prefix = name_space_prefix
                        if(value_path == "send-version"):
                            self.send_version = value
                            self.send_version.value_namespace = name_space
                            self.send_version.value_namespace_prefix = name_space_prefix
                        if(value_path == "split-horizon"):
                            self.split_horizon = value
                            self.split_horizon.value_namespace = name_space
                            self.split_horizon.value_namespace_prefix = name_space_prefix
                        if(value_path == "state"):
                            self.state = value
                            self.state.value_namespace = name_space
                            self.state.value_namespace_prefix = name_space_prefix
                        if(value_path == "total-pkt-recvd"):
                            self.total_pkt_recvd = value
                            self.total_pkt_recvd.value_namespace = name_space
                            self.total_pkt_recvd.value_namespace_prefix = name_space_prefix
                        if(value_path == "triggered-rip"):
                            self.triggered_rip = value
                            self.triggered_rip.value_namespace = name_space
                            self.triggered_rip.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.interface:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.interface:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "interfaces" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ip-rip-oper:rip/protocol/default-vrf/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "interface"):
                        for c in self.interface:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Rip.Protocol.DefaultVrf.Interfaces.Interface()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.interface.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "interface"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Global_(Entity):
                """
                Global Information 
                
                .. attribute:: interface_summary
                
                	List of Interfaces configured
                	**type**\: list of    :py:class:`InterfaceSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Protocol.DefaultVrf.Global_.InterfaceSummary>`
                
                .. attribute:: vrf_summary
                
                	VRF summary data
                	**type**\:   :py:class:`VrfSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Protocol.DefaultVrf.Global_.VrfSummary>`
                
                

                """

                _prefix = 'ip-rip-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rip.Protocol.DefaultVrf.Global_, self).__init__()

                    self.yang_name = "global"
                    self.yang_parent_name = "default-vrf"

                    self.vrf_summary = Rip.Protocol.DefaultVrf.Global_.VrfSummary()
                    self.vrf_summary.parent = self
                    self._children_name_map["vrf_summary"] = "vrf-summary"
                    self._children_yang_names.add("vrf-summary")

                    self.interface_summary = YList(self)

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
                                super(Rip.Protocol.DefaultVrf.Global_, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Rip.Protocol.DefaultVrf.Global_, self).__setattr__(name, value)


                class VrfSummary(Entity):
                    """
                    VRF summary data
                    
                    .. attribute:: active
                    
                    	VRF Active indicator
                    	**type**\:  bool
                    
                    .. attribute:: active_interface_count
                    
                    	Number of active interfaces
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: flush_timer
                    
                    	Flush timer
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: hold_down_timer
                    
                    	Holddown timer
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: interface_configured_count
                    
                    	Number of interfaces configured
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: invalid_timer
                    
                    	Invalid timer
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: next_update_time
                    
                    	Time left for next update
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: oom_flags
                    
                    	Current OOM flags
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: path_count
                    
                    	Number of paths allocated
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: route_count
                    
                    	Number of routes allocated
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: update_timer
                    
                    	Update timer
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: vrf_name
                    
                    	VRF Name
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'ip-rip-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Rip.Protocol.DefaultVrf.Global_.VrfSummary, self).__init__()

                        self.yang_name = "vrf-summary"
                        self.yang_parent_name = "global"

                        self.active = YLeaf(YType.boolean, "active")

                        self.active_interface_count = YLeaf(YType.uint32, "active-interface-count")

                        self.flush_timer = YLeaf(YType.uint32, "flush-timer")

                        self.hold_down_timer = YLeaf(YType.uint32, "hold-down-timer")

                        self.interface_configured_count = YLeaf(YType.uint32, "interface-configured-count")

                        self.invalid_timer = YLeaf(YType.uint32, "invalid-timer")

                        self.next_update_time = YLeaf(YType.uint32, "next-update-time")

                        self.oom_flags = YLeaf(YType.uint32, "oom-flags")

                        self.path_count = YLeaf(YType.uint32, "path-count")

                        self.route_count = YLeaf(YType.uint32, "route-count")

                        self.update_timer = YLeaf(YType.uint32, "update-timer")

                        self.vrf_name = YLeaf(YType.str, "vrf-name")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("active",
                                        "active_interface_count",
                                        "flush_timer",
                                        "hold_down_timer",
                                        "interface_configured_count",
                                        "invalid_timer",
                                        "next_update_time",
                                        "oom_flags",
                                        "path_count",
                                        "route_count",
                                        "update_timer",
                                        "vrf_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Rip.Protocol.DefaultVrf.Global_.VrfSummary, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Rip.Protocol.DefaultVrf.Global_.VrfSummary, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.active.is_set or
                            self.active_interface_count.is_set or
                            self.flush_timer.is_set or
                            self.hold_down_timer.is_set or
                            self.interface_configured_count.is_set or
                            self.invalid_timer.is_set or
                            self.next_update_time.is_set or
                            self.oom_flags.is_set or
                            self.path_count.is_set or
                            self.route_count.is_set or
                            self.update_timer.is_set or
                            self.vrf_name.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.active.yfilter != YFilter.not_set or
                            self.active_interface_count.yfilter != YFilter.not_set or
                            self.flush_timer.yfilter != YFilter.not_set or
                            self.hold_down_timer.yfilter != YFilter.not_set or
                            self.interface_configured_count.yfilter != YFilter.not_set or
                            self.invalid_timer.yfilter != YFilter.not_set or
                            self.next_update_time.yfilter != YFilter.not_set or
                            self.oom_flags.yfilter != YFilter.not_set or
                            self.path_count.yfilter != YFilter.not_set or
                            self.route_count.yfilter != YFilter.not_set or
                            self.update_timer.yfilter != YFilter.not_set or
                            self.vrf_name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "vrf-summary" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-ip-rip-oper:rip/protocol/default-vrf/global/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.active.is_set or self.active.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.active.get_name_leafdata())
                        if (self.active_interface_count.is_set or self.active_interface_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.active_interface_count.get_name_leafdata())
                        if (self.flush_timer.is_set or self.flush_timer.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.flush_timer.get_name_leafdata())
                        if (self.hold_down_timer.is_set or self.hold_down_timer.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.hold_down_timer.get_name_leafdata())
                        if (self.interface_configured_count.is_set or self.interface_configured_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_configured_count.get_name_leafdata())
                        if (self.invalid_timer.is_set or self.invalid_timer.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.invalid_timer.get_name_leafdata())
                        if (self.next_update_time.is_set or self.next_update_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.next_update_time.get_name_leafdata())
                        if (self.oom_flags.is_set or self.oom_flags.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.oom_flags.get_name_leafdata())
                        if (self.path_count.is_set or self.path_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.path_count.get_name_leafdata())
                        if (self.route_count.is_set or self.route_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.route_count.get_name_leafdata())
                        if (self.update_timer.is_set or self.update_timer.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.update_timer.get_name_leafdata())
                        if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vrf_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "active" or name == "active-interface-count" or name == "flush-timer" or name == "hold-down-timer" or name == "interface-configured-count" or name == "invalid-timer" or name == "next-update-time" or name == "oom-flags" or name == "path-count" or name == "route-count" or name == "update-timer" or name == "vrf-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "active"):
                            self.active = value
                            self.active.value_namespace = name_space
                            self.active.value_namespace_prefix = name_space_prefix
                        if(value_path == "active-interface-count"):
                            self.active_interface_count = value
                            self.active_interface_count.value_namespace = name_space
                            self.active_interface_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "flush-timer"):
                            self.flush_timer = value
                            self.flush_timer.value_namespace = name_space
                            self.flush_timer.value_namespace_prefix = name_space_prefix
                        if(value_path == "hold-down-timer"):
                            self.hold_down_timer = value
                            self.hold_down_timer.value_namespace = name_space
                            self.hold_down_timer.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface-configured-count"):
                            self.interface_configured_count = value
                            self.interface_configured_count.value_namespace = name_space
                            self.interface_configured_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "invalid-timer"):
                            self.invalid_timer = value
                            self.invalid_timer.value_namespace = name_space
                            self.invalid_timer.value_namespace_prefix = name_space_prefix
                        if(value_path == "next-update-time"):
                            self.next_update_time = value
                            self.next_update_time.value_namespace = name_space
                            self.next_update_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "oom-flags"):
                            self.oom_flags = value
                            self.oom_flags.value_namespace = name_space
                            self.oom_flags.value_namespace_prefix = name_space_prefix
                        if(value_path == "path-count"):
                            self.path_count = value
                            self.path_count.value_namespace = name_space
                            self.path_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "route-count"):
                            self.route_count = value
                            self.route_count.value_namespace = name_space
                            self.route_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "update-timer"):
                            self.update_timer = value
                            self.update_timer.value_namespace = name_space
                            self.update_timer.value_namespace_prefix = name_space_prefix
                        if(value_path == "vrf-name"):
                            self.vrf_name = value
                            self.vrf_name.value_namespace = name_space
                            self.vrf_name.value_namespace_prefix = name_space_prefix


                class InterfaceSummary(Entity):
                    """
                    List of Interfaces configured
                    
                    .. attribute:: destination_address
                    
                    	IP address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: enabled
                    
                    	RIP enabled indicator
                    	**type**\:  bool
                    
                    .. attribute:: interface_name
                    
                    	Interface name
                    	**type**\:  str
                    
                    .. attribute:: neighbor_count
                    
                    	Number of neighbors seen
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: oom_flags
                    
                    	Current OOM flags
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: prefix_length
                    
                    	Prefix length of IP address
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: receive_version
                    
                    	RIP versions this interface will receive
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: send_version
                    
                    	RIP versions this interface sends out
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: state
                    
                    	Interface state
                    	**type**\:   :py:class:`InterfaceState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.InterfaceState>`
                    
                    

                    """

                    _prefix = 'ip-rip-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Rip.Protocol.DefaultVrf.Global_.InterfaceSummary, self).__init__()

                        self.yang_name = "interface-summary"
                        self.yang_parent_name = "global"

                        self.destination_address = YLeaf(YType.str, "destination-address")

                        self.enabled = YLeaf(YType.boolean, "enabled")

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.neighbor_count = YLeaf(YType.uint32, "neighbor-count")

                        self.oom_flags = YLeaf(YType.uint32, "oom-flags")

                        self.prefix_length = YLeaf(YType.uint32, "prefix-length")

                        self.receive_version = YLeaf(YType.uint32, "receive-version")

                        self.send_version = YLeaf(YType.uint32, "send-version")

                        self.state = YLeaf(YType.enumeration, "state")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("destination_address",
                                        "enabled",
                                        "interface_name",
                                        "neighbor_count",
                                        "oom_flags",
                                        "prefix_length",
                                        "receive_version",
                                        "send_version",
                                        "state") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Rip.Protocol.DefaultVrf.Global_.InterfaceSummary, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Rip.Protocol.DefaultVrf.Global_.InterfaceSummary, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.destination_address.is_set or
                            self.enabled.is_set or
                            self.interface_name.is_set or
                            self.neighbor_count.is_set or
                            self.oom_flags.is_set or
                            self.prefix_length.is_set or
                            self.receive_version.is_set or
                            self.send_version.is_set or
                            self.state.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.destination_address.yfilter != YFilter.not_set or
                            self.enabled.yfilter != YFilter.not_set or
                            self.interface_name.yfilter != YFilter.not_set or
                            self.neighbor_count.yfilter != YFilter.not_set or
                            self.oom_flags.yfilter != YFilter.not_set or
                            self.prefix_length.yfilter != YFilter.not_set or
                            self.receive_version.yfilter != YFilter.not_set or
                            self.send_version.yfilter != YFilter.not_set or
                            self.state.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "interface-summary" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-ip-rip-oper:rip/protocol/default-vrf/global/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.destination_address.is_set or self.destination_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.destination_address.get_name_leafdata())
                        if (self.enabled.is_set or self.enabled.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.enabled.get_name_leafdata())
                        if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_name.get_name_leafdata())
                        if (self.neighbor_count.is_set or self.neighbor_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.neighbor_count.get_name_leafdata())
                        if (self.oom_flags.is_set or self.oom_flags.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.oom_flags.get_name_leafdata())
                        if (self.prefix_length.is_set or self.prefix_length.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.prefix_length.get_name_leafdata())
                        if (self.receive_version.is_set or self.receive_version.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.receive_version.get_name_leafdata())
                        if (self.send_version.is_set or self.send_version.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.send_version.get_name_leafdata())
                        if (self.state.is_set or self.state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.state.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "destination-address" or name == "enabled" or name == "interface-name" or name == "neighbor-count" or name == "oom-flags" or name == "prefix-length" or name == "receive-version" or name == "send-version" or name == "state"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "destination-address"):
                            self.destination_address = value
                            self.destination_address.value_namespace = name_space
                            self.destination_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "enabled"):
                            self.enabled = value
                            self.enabled.value_namespace = name_space
                            self.enabled.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface-name"):
                            self.interface_name = value
                            self.interface_name.value_namespace = name_space
                            self.interface_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "neighbor-count"):
                            self.neighbor_count = value
                            self.neighbor_count.value_namespace = name_space
                            self.neighbor_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "oom-flags"):
                            self.oom_flags = value
                            self.oom_flags.value_namespace = name_space
                            self.oom_flags.value_namespace_prefix = name_space_prefix
                        if(value_path == "prefix-length"):
                            self.prefix_length = value
                            self.prefix_length.value_namespace = name_space
                            self.prefix_length.value_namespace_prefix = name_space_prefix
                        if(value_path == "receive-version"):
                            self.receive_version = value
                            self.receive_version.value_namespace = name_space
                            self.receive_version.value_namespace_prefix = name_space_prefix
                        if(value_path == "send-version"):
                            self.send_version = value
                            self.send_version.value_namespace = name_space
                            self.send_version.value_namespace_prefix = name_space_prefix
                        if(value_path == "state"):
                            self.state = value
                            self.state.value_namespace = name_space
                            self.state.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.interface_summary:
                        if (c.has_data()):
                            return True
                    return (self.vrf_summary is not None and self.vrf_summary.has_data())

                def has_operation(self):
                    for c in self.interface_summary:
                        if (c.has_operation()):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.vrf_summary is not None and self.vrf_summary.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "global" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ip-rip-oper:rip/protocol/default-vrf/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "interface-summary"):
                        for c in self.interface_summary:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Rip.Protocol.DefaultVrf.Global_.InterfaceSummary()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.interface_summary.append(c)
                        return c

                    if (child_yang_name == "vrf-summary"):
                        if (self.vrf_summary is None):
                            self.vrf_summary = Rip.Protocol.DefaultVrf.Global_.VrfSummary()
                            self.vrf_summary.parent = self
                            self._children_name_map["vrf_summary"] = "vrf-summary"
                        return self.vrf_summary

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "interface-summary" or name == "vrf-summary"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    (self.configuration is not None and self.configuration.has_data()) or
                    (self.global_ is not None and self.global_.has_data()) or
                    (self.interfaces is not None and self.interfaces.has_data()) or
                    (self.routes is not None and self.routes.has_data()) or
                    (self.statistics is not None and self.statistics.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.configuration is not None and self.configuration.has_operation()) or
                    (self.global_ is not None and self.global_.has_operation()) or
                    (self.interfaces is not None and self.interfaces.has_operation()) or
                    (self.routes is not None and self.routes.has_operation()) or
                    (self.statistics is not None and self.statistics.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "default-vrf" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ip-rip-oper:rip/protocol/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "configuration"):
                    if (self.configuration is None):
                        self.configuration = Rip.Protocol.DefaultVrf.Configuration()
                        self.configuration.parent = self
                        self._children_name_map["configuration"] = "configuration"
                    return self.configuration

                if (child_yang_name == "global"):
                    if (self.global_ is None):
                        self.global_ = Rip.Protocol.DefaultVrf.Global_()
                        self.global_.parent = self
                        self._children_name_map["global_"] = "global"
                    return self.global_

                if (child_yang_name == "interfaces"):
                    if (self.interfaces is None):
                        self.interfaces = Rip.Protocol.DefaultVrf.Interfaces()
                        self.interfaces.parent = self
                        self._children_name_map["interfaces"] = "interfaces"
                    return self.interfaces

                if (child_yang_name == "routes"):
                    if (self.routes is None):
                        self.routes = Rip.Protocol.DefaultVrf.Routes()
                        self.routes.parent = self
                        self._children_name_map["routes"] = "routes"
                    return self.routes

                if (child_yang_name == "statistics"):
                    if (self.statistics is None):
                        self.statistics = Rip.Protocol.DefaultVrf.Statistics()
                        self.statistics.parent = self
                        self._children_name_map["statistics"] = "statistics"
                    return self.statistics

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "configuration" or name == "global" or name == "interfaces" or name == "routes" or name == "statistics"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (
                (self.default_vrf is not None and self.default_vrf.has_data()) or
                (self.process is not None and self.process.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.default_vrf is not None and self.default_vrf.has_operation()) or
                (self.process is not None and self.process.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "protocol" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ip-rip-oper:rip/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "default-vrf"):
                if (self.default_vrf is None):
                    self.default_vrf = Rip.Protocol.DefaultVrf()
                    self.default_vrf.parent = self
                    self._children_name_map["default_vrf"] = "default-vrf"
                return self.default_vrf

            if (child_yang_name == "process"):
                if (self.process is None):
                    self.process = Rip.Protocol.Process()
                    self.process.parent = self
                    self._children_name_map["process"] = "process"
                return self.process

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "default-vrf" or name == "process"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class DefaultVrf(Entity):
        """
        RIP operational data for Default VRF
        
        .. attribute:: configuration
        
        	RIP global configuration
        	**type**\:   :py:class:`Configuration <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.DefaultVrf.Configuration>`
        
        .. attribute:: global_
        
        	Global Information 
        	**type**\:   :py:class:`Global_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.DefaultVrf.Global_>`
        
        .. attribute:: interfaces
        
        	RIP interfaces
        	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.DefaultVrf.Interfaces>`
        
        .. attribute:: routes
        
        	RIP route database
        	**type**\:   :py:class:`Routes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.DefaultVrf.Routes>`
        
        .. attribute:: statistics
        
        	RIP statistics information
        	**type**\:   :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.DefaultVrf.Statistics>`
        
        

        """

        _prefix = 'ip-rip-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Rip.DefaultVrf, self).__init__()

            self.yang_name = "default-vrf"
            self.yang_parent_name = "rip"

            self.configuration = Rip.DefaultVrf.Configuration()
            self.configuration.parent = self
            self._children_name_map["configuration"] = "configuration"
            self._children_yang_names.add("configuration")

            self.global_ = Rip.DefaultVrf.Global_()
            self.global_.parent = self
            self._children_name_map["global_"] = "global"
            self._children_yang_names.add("global")

            self.interfaces = Rip.DefaultVrf.Interfaces()
            self.interfaces.parent = self
            self._children_name_map["interfaces"] = "interfaces"
            self._children_yang_names.add("interfaces")

            self.routes = Rip.DefaultVrf.Routes()
            self.routes.parent = self
            self._children_name_map["routes"] = "routes"
            self._children_yang_names.add("routes")

            self.statistics = Rip.DefaultVrf.Statistics()
            self.statistics.parent = self
            self._children_name_map["statistics"] = "statistics"
            self._children_yang_names.add("statistics")


        class Routes(Entity):
            """
            RIP route database
            
            .. attribute:: route
            
            	A route in the RIP database
            	**type**\: list of    :py:class:`Route <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.DefaultVrf.Routes.Route>`
            
            

            """

            _prefix = 'ip-rip-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Rip.DefaultVrf.Routes, self).__init__()

                self.yang_name = "routes"
                self.yang_parent_name = "default-vrf"

                self.route = YList(self)

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
                            super(Rip.DefaultVrf.Routes, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Rip.DefaultVrf.Routes, self).__setattr__(name, value)


            class Route(Entity):
                """
                A route in the RIP database
                
                .. attribute:: active
                
                	Active route indicator
                	**type**\:  bool
                
                .. attribute:: attributes
                
                	RIB supplied route attributes
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: bgp_count
                
                	Hop count for this route
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: destination_address
                
                	Destination IP Address for this route
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: distance
                
                	Route administrative distance
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: hold_down
                
                	Indicates whether route is in holddown
                	**type**\:  bool
                
                .. attribute:: path_origin
                
                	Where this route was learnt
                	**type**\:   :py:class:`RipRouteOrigin <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.RipRouteOrigin>`
                
                .. attribute:: paths
                
                	The paths for this route
                	**type**\: list of    :py:class:`Paths <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.DefaultVrf.Routes.Route.Paths>`
                
                .. attribute:: prefix
                
                	Network prefix
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: prefix_length
                
                	Prefix length
                	**type**\:  int
                
                	**range:** 0..32
                
                .. attribute:: prefix_length_xr
                
                	Prefix length of IP address
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: route_summary
                
                	Summary route placeholder indicator
                	**type**\:  bool
                
                .. attribute:: route_tag
                
                	Generic route information
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: route_type
                
                	Type of this route
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: version
                
                	RIB supplied version number
                	**type**\:  int
                
                	**range:** 0..255
                
                

                """

                _prefix = 'ip-rip-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rip.DefaultVrf.Routes.Route, self).__init__()

                    self.yang_name = "route"
                    self.yang_parent_name = "routes"

                    self.active = YLeaf(YType.boolean, "active")

                    self.attributes = YLeaf(YType.uint32, "attributes")

                    self.bgp_count = YLeaf(YType.uint16, "bgp-count")

                    self.destination_address = YLeaf(YType.str, "destination-address")

                    self.distance = YLeaf(YType.uint16, "distance")

                    self.hold_down = YLeaf(YType.boolean, "hold-down")

                    self.path_origin = YLeaf(YType.enumeration, "path-origin")

                    self.prefix = YLeaf(YType.str, "prefix")

                    self.prefix_length = YLeaf(YType.uint32, "prefix-length")

                    self.prefix_length_xr = YLeaf(YType.uint32, "prefix-length-xr")

                    self.route_summary = YLeaf(YType.boolean, "route-summary")

                    self.route_tag = YLeaf(YType.uint16, "route-tag")

                    self.route_type = YLeaf(YType.uint16, "route-type")

                    self.version = YLeaf(YType.uint8, "version")

                    self.paths = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("active",
                                    "attributes",
                                    "bgp_count",
                                    "destination_address",
                                    "distance",
                                    "hold_down",
                                    "path_origin",
                                    "prefix",
                                    "prefix_length",
                                    "prefix_length_xr",
                                    "route_summary",
                                    "route_tag",
                                    "route_type",
                                    "version") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Rip.DefaultVrf.Routes.Route, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Rip.DefaultVrf.Routes.Route, self).__setattr__(name, value)


                class Paths(Entity):
                    """
                    The paths for this route
                    
                    .. attribute:: interface
                    
                    	Interface
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: is_permanent
                    
                    	Permanent indicator
                    	**type**\:  bool
                    
                    .. attribute:: metric
                    
                    	Metric
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: next_hop_address
                    
                    	Next hop address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: source_address
                    
                    	Source address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: tag
                    
                    	Tag
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: uptime
                    
                    	Up time
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ip-rip-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Rip.DefaultVrf.Routes.Route.Paths, self).__init__()

                        self.yang_name = "paths"
                        self.yang_parent_name = "route"

                        self.interface = YLeaf(YType.str, "interface")

                        self.is_permanent = YLeaf(YType.boolean, "is-permanent")

                        self.metric = YLeaf(YType.uint16, "metric")

                        self.next_hop_address = YLeaf(YType.str, "next-hop-address")

                        self.source_address = YLeaf(YType.str, "source-address")

                        self.tag = YLeaf(YType.uint16, "tag")

                        self.uptime = YLeaf(YType.uint32, "uptime")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("interface",
                                        "is_permanent",
                                        "metric",
                                        "next_hop_address",
                                        "source_address",
                                        "tag",
                                        "uptime") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Rip.DefaultVrf.Routes.Route.Paths, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Rip.DefaultVrf.Routes.Route.Paths, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.interface.is_set or
                            self.is_permanent.is_set or
                            self.metric.is_set or
                            self.next_hop_address.is_set or
                            self.source_address.is_set or
                            self.tag.is_set or
                            self.uptime.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.interface.yfilter != YFilter.not_set or
                            self.is_permanent.yfilter != YFilter.not_set or
                            self.metric.yfilter != YFilter.not_set or
                            self.next_hop_address.yfilter != YFilter.not_set or
                            self.source_address.yfilter != YFilter.not_set or
                            self.tag.yfilter != YFilter.not_set or
                            self.uptime.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "paths" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-ip-rip-oper:rip/default-vrf/routes/route/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.interface.is_set or self.interface.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface.get_name_leafdata())
                        if (self.is_permanent.is_set or self.is_permanent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.is_permanent.get_name_leafdata())
                        if (self.metric.is_set or self.metric.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.metric.get_name_leafdata())
                        if (self.next_hop_address.is_set or self.next_hop_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.next_hop_address.get_name_leafdata())
                        if (self.source_address.is_set or self.source_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.source_address.get_name_leafdata())
                        if (self.tag.is_set or self.tag.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tag.get_name_leafdata())
                        if (self.uptime.is_set or self.uptime.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.uptime.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "interface" or name == "is-permanent" or name == "metric" or name == "next-hop-address" or name == "source-address" or name == "tag" or name == "uptime"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "interface"):
                            self.interface = value
                            self.interface.value_namespace = name_space
                            self.interface.value_namespace_prefix = name_space_prefix
                        if(value_path == "is-permanent"):
                            self.is_permanent = value
                            self.is_permanent.value_namespace = name_space
                            self.is_permanent.value_namespace_prefix = name_space_prefix
                        if(value_path == "metric"):
                            self.metric = value
                            self.metric.value_namespace = name_space
                            self.metric.value_namespace_prefix = name_space_prefix
                        if(value_path == "next-hop-address"):
                            self.next_hop_address = value
                            self.next_hop_address.value_namespace = name_space
                            self.next_hop_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "source-address"):
                            self.source_address = value
                            self.source_address.value_namespace = name_space
                            self.source_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "tag"):
                            self.tag = value
                            self.tag.value_namespace = name_space
                            self.tag.value_namespace_prefix = name_space_prefix
                        if(value_path == "uptime"):
                            self.uptime = value
                            self.uptime.value_namespace = name_space
                            self.uptime.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.paths:
                        if (c.has_data()):
                            return True
                    return (
                        self.active.is_set or
                        self.attributes.is_set or
                        self.bgp_count.is_set or
                        self.destination_address.is_set or
                        self.distance.is_set or
                        self.hold_down.is_set or
                        self.path_origin.is_set or
                        self.prefix.is_set or
                        self.prefix_length.is_set or
                        self.prefix_length_xr.is_set or
                        self.route_summary.is_set or
                        self.route_tag.is_set or
                        self.route_type.is_set or
                        self.version.is_set)

                def has_operation(self):
                    for c in self.paths:
                        if (c.has_operation()):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.active.yfilter != YFilter.not_set or
                        self.attributes.yfilter != YFilter.not_set or
                        self.bgp_count.yfilter != YFilter.not_set or
                        self.destination_address.yfilter != YFilter.not_set or
                        self.distance.yfilter != YFilter.not_set or
                        self.hold_down.yfilter != YFilter.not_set or
                        self.path_origin.yfilter != YFilter.not_set or
                        self.prefix.yfilter != YFilter.not_set or
                        self.prefix_length.yfilter != YFilter.not_set or
                        self.prefix_length_xr.yfilter != YFilter.not_set or
                        self.route_summary.yfilter != YFilter.not_set or
                        self.route_tag.yfilter != YFilter.not_set or
                        self.route_type.yfilter != YFilter.not_set or
                        self.version.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "route" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ip-rip-oper:rip/default-vrf/routes/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.active.is_set or self.active.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.active.get_name_leafdata())
                    if (self.attributes.is_set or self.attributes.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.attributes.get_name_leafdata())
                    if (self.bgp_count.is_set or self.bgp_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bgp_count.get_name_leafdata())
                    if (self.destination_address.is_set or self.destination_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.destination_address.get_name_leafdata())
                    if (self.distance.is_set or self.distance.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.distance.get_name_leafdata())
                    if (self.hold_down.is_set or self.hold_down.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.hold_down.get_name_leafdata())
                    if (self.path_origin.is_set or self.path_origin.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.path_origin.get_name_leafdata())
                    if (self.prefix.is_set or self.prefix.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.prefix.get_name_leafdata())
                    if (self.prefix_length.is_set or self.prefix_length.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.prefix_length.get_name_leafdata())
                    if (self.prefix_length_xr.is_set or self.prefix_length_xr.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.prefix_length_xr.get_name_leafdata())
                    if (self.route_summary.is_set or self.route_summary.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.route_summary.get_name_leafdata())
                    if (self.route_tag.is_set or self.route_tag.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.route_tag.get_name_leafdata())
                    if (self.route_type.is_set or self.route_type.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.route_type.get_name_leafdata())
                    if (self.version.is_set or self.version.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.version.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "paths"):
                        for c in self.paths:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Rip.DefaultVrf.Routes.Route.Paths()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.paths.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "paths" or name == "active" or name == "attributes" or name == "bgp-count" or name == "destination-address" or name == "distance" or name == "hold-down" or name == "path-origin" or name == "prefix" or name == "prefix-length" or name == "prefix-length-xr" or name == "route-summary" or name == "route-tag" or name == "route-type" or name == "version"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "active"):
                        self.active = value
                        self.active.value_namespace = name_space
                        self.active.value_namespace_prefix = name_space_prefix
                    if(value_path == "attributes"):
                        self.attributes = value
                        self.attributes.value_namespace = name_space
                        self.attributes.value_namespace_prefix = name_space_prefix
                    if(value_path == "bgp-count"):
                        self.bgp_count = value
                        self.bgp_count.value_namespace = name_space
                        self.bgp_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "destination-address"):
                        self.destination_address = value
                        self.destination_address.value_namespace = name_space
                        self.destination_address.value_namespace_prefix = name_space_prefix
                    if(value_path == "distance"):
                        self.distance = value
                        self.distance.value_namespace = name_space
                        self.distance.value_namespace_prefix = name_space_prefix
                    if(value_path == "hold-down"):
                        self.hold_down = value
                        self.hold_down.value_namespace = name_space
                        self.hold_down.value_namespace_prefix = name_space_prefix
                    if(value_path == "path-origin"):
                        self.path_origin = value
                        self.path_origin.value_namespace = name_space
                        self.path_origin.value_namespace_prefix = name_space_prefix
                    if(value_path == "prefix"):
                        self.prefix = value
                        self.prefix.value_namespace = name_space
                        self.prefix.value_namespace_prefix = name_space_prefix
                    if(value_path == "prefix-length"):
                        self.prefix_length = value
                        self.prefix_length.value_namespace = name_space
                        self.prefix_length.value_namespace_prefix = name_space_prefix
                    if(value_path == "prefix-length-xr"):
                        self.prefix_length_xr = value
                        self.prefix_length_xr.value_namespace = name_space
                        self.prefix_length_xr.value_namespace_prefix = name_space_prefix
                    if(value_path == "route-summary"):
                        self.route_summary = value
                        self.route_summary.value_namespace = name_space
                        self.route_summary.value_namespace_prefix = name_space_prefix
                    if(value_path == "route-tag"):
                        self.route_tag = value
                        self.route_tag.value_namespace = name_space
                        self.route_tag.value_namespace_prefix = name_space_prefix
                    if(value_path == "route-type"):
                        self.route_type = value
                        self.route_type.value_namespace = name_space
                        self.route_type.value_namespace_prefix = name_space_prefix
                    if(value_path == "version"):
                        self.version = value
                        self.version.value_namespace = name_space
                        self.version.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.route:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.route:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "routes" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ip-rip-oper:rip/default-vrf/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "route"):
                    for c in self.route:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Rip.DefaultVrf.Routes.Route()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.route.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "route"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class Configuration(Entity):
            """
            RIP global configuration
            
            .. attribute:: active
            
            	VRF active indicator
            	**type**\:  bool
            
            .. attribute:: auto_summarize
            
            	Auto\-summarization indicator
            	**type**\:  bool
            
            .. attribute:: default_metric
            
            	Default metric for RIP routes
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: flash_threshold
            
            	Flash update threshold
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: flush_timer
            
            	Flush timer
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: hold_down_timer
            
            	Holddown timer
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: input_q_length
            
            	Length of the input queue
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: invalid_timer
            
            	Invalid timer
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: maximum_paths
            
            	Maximum number of paths a route can have
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: multicast_address
            
            	Use broadcast/multicast address indicator
            	**type**\:  bool
            
            .. attribute:: next_update_time
            
            	Time left for next update
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nsf_life_time
            
            	NSF life time
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nsf_status
            
            	NSF Enable status
            	**type**\:  bool
            
            .. attribute:: oom_flags
            
            	Out\-of\-memory status flags
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rip_version
            
            	Version of RIP configured
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: triggered_rip
            
            	Triggered RIP enabled indicator
            	**type**\:  bool
            
            .. attribute:: update_timer
            
            	Update timer
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: validation_indicator
            
            	Incoming packet source validation indicator
            	**type**\:  bool
            
            .. attribute:: vr_fised_socket
            
            	VRF added to socket indicator
            	**type**\:  bool
            
            

            """

            _prefix = 'ip-rip-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Rip.DefaultVrf.Configuration, self).__init__()

                self.yang_name = "configuration"
                self.yang_parent_name = "default-vrf"

                self.active = YLeaf(YType.boolean, "active")

                self.auto_summarize = YLeaf(YType.boolean, "auto-summarize")

                self.default_metric = YLeaf(YType.uint8, "default-metric")

                self.flash_threshold = YLeaf(YType.uint8, "flash-threshold")

                self.flush_timer = YLeaf(YType.uint32, "flush-timer")

                self.hold_down_timer = YLeaf(YType.uint32, "hold-down-timer")

                self.input_q_length = YLeaf(YType.uint16, "input-q-length")

                self.invalid_timer = YLeaf(YType.uint32, "invalid-timer")

                self.maximum_paths = YLeaf(YType.uint8, "maximum-paths")

                self.multicast_address = YLeaf(YType.boolean, "multicast-address")

                self.next_update_time = YLeaf(YType.uint32, "next-update-time")

                self.nsf_life_time = YLeaf(YType.uint32, "nsf-life-time")

                self.nsf_status = YLeaf(YType.boolean, "nsf-status")

                self.oom_flags = YLeaf(YType.uint32, "oom-flags")

                self.rip_version = YLeaf(YType.int32, "rip-version")

                self.triggered_rip = YLeaf(YType.boolean, "triggered-rip")

                self.update_timer = YLeaf(YType.uint32, "update-timer")

                self.validation_indicator = YLeaf(YType.boolean, "validation-indicator")

                self.vr_fised_socket = YLeaf(YType.boolean, "vr-fised-socket")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("active",
                                "auto_summarize",
                                "default_metric",
                                "flash_threshold",
                                "flush_timer",
                                "hold_down_timer",
                                "input_q_length",
                                "invalid_timer",
                                "maximum_paths",
                                "multicast_address",
                                "next_update_time",
                                "nsf_life_time",
                                "nsf_status",
                                "oom_flags",
                                "rip_version",
                                "triggered_rip",
                                "update_timer",
                                "validation_indicator",
                                "vr_fised_socket") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Rip.DefaultVrf.Configuration, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Rip.DefaultVrf.Configuration, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.active.is_set or
                    self.auto_summarize.is_set or
                    self.default_metric.is_set or
                    self.flash_threshold.is_set or
                    self.flush_timer.is_set or
                    self.hold_down_timer.is_set or
                    self.input_q_length.is_set or
                    self.invalid_timer.is_set or
                    self.maximum_paths.is_set or
                    self.multicast_address.is_set or
                    self.next_update_time.is_set or
                    self.nsf_life_time.is_set or
                    self.nsf_status.is_set or
                    self.oom_flags.is_set or
                    self.rip_version.is_set or
                    self.triggered_rip.is_set or
                    self.update_timer.is_set or
                    self.validation_indicator.is_set or
                    self.vr_fised_socket.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.active.yfilter != YFilter.not_set or
                    self.auto_summarize.yfilter != YFilter.not_set or
                    self.default_metric.yfilter != YFilter.not_set or
                    self.flash_threshold.yfilter != YFilter.not_set or
                    self.flush_timer.yfilter != YFilter.not_set or
                    self.hold_down_timer.yfilter != YFilter.not_set or
                    self.input_q_length.yfilter != YFilter.not_set or
                    self.invalid_timer.yfilter != YFilter.not_set or
                    self.maximum_paths.yfilter != YFilter.not_set or
                    self.multicast_address.yfilter != YFilter.not_set or
                    self.next_update_time.yfilter != YFilter.not_set or
                    self.nsf_life_time.yfilter != YFilter.not_set or
                    self.nsf_status.yfilter != YFilter.not_set or
                    self.oom_flags.yfilter != YFilter.not_set or
                    self.rip_version.yfilter != YFilter.not_set or
                    self.triggered_rip.yfilter != YFilter.not_set or
                    self.update_timer.yfilter != YFilter.not_set or
                    self.validation_indicator.yfilter != YFilter.not_set or
                    self.vr_fised_socket.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "configuration" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ip-rip-oper:rip/default-vrf/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.active.is_set or self.active.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.active.get_name_leafdata())
                if (self.auto_summarize.is_set or self.auto_summarize.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.auto_summarize.get_name_leafdata())
                if (self.default_metric.is_set or self.default_metric.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.default_metric.get_name_leafdata())
                if (self.flash_threshold.is_set or self.flash_threshold.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.flash_threshold.get_name_leafdata())
                if (self.flush_timer.is_set or self.flush_timer.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.flush_timer.get_name_leafdata())
                if (self.hold_down_timer.is_set or self.hold_down_timer.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.hold_down_timer.get_name_leafdata())
                if (self.input_q_length.is_set or self.input_q_length.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.input_q_length.get_name_leafdata())
                if (self.invalid_timer.is_set or self.invalid_timer.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.invalid_timer.get_name_leafdata())
                if (self.maximum_paths.is_set or self.maximum_paths.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.maximum_paths.get_name_leafdata())
                if (self.multicast_address.is_set or self.multicast_address.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.multicast_address.get_name_leafdata())
                if (self.next_update_time.is_set or self.next_update_time.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.next_update_time.get_name_leafdata())
                if (self.nsf_life_time.is_set or self.nsf_life_time.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nsf_life_time.get_name_leafdata())
                if (self.nsf_status.is_set or self.nsf_status.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nsf_status.get_name_leafdata())
                if (self.oom_flags.is_set or self.oom_flags.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.oom_flags.get_name_leafdata())
                if (self.rip_version.is_set or self.rip_version.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rip_version.get_name_leafdata())
                if (self.triggered_rip.is_set or self.triggered_rip.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.triggered_rip.get_name_leafdata())
                if (self.update_timer.is_set or self.update_timer.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.update_timer.get_name_leafdata())
                if (self.validation_indicator.is_set or self.validation_indicator.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.validation_indicator.get_name_leafdata())
                if (self.vr_fised_socket.is_set or self.vr_fised_socket.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vr_fised_socket.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "active" or name == "auto-summarize" or name == "default-metric" or name == "flash-threshold" or name == "flush-timer" or name == "hold-down-timer" or name == "input-q-length" or name == "invalid-timer" or name == "maximum-paths" or name == "multicast-address" or name == "next-update-time" or name == "nsf-life-time" or name == "nsf-status" or name == "oom-flags" or name == "rip-version" or name == "triggered-rip" or name == "update-timer" or name == "validation-indicator" or name == "vr-fised-socket"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "active"):
                    self.active = value
                    self.active.value_namespace = name_space
                    self.active.value_namespace_prefix = name_space_prefix
                if(value_path == "auto-summarize"):
                    self.auto_summarize = value
                    self.auto_summarize.value_namespace = name_space
                    self.auto_summarize.value_namespace_prefix = name_space_prefix
                if(value_path == "default-metric"):
                    self.default_metric = value
                    self.default_metric.value_namespace = name_space
                    self.default_metric.value_namespace_prefix = name_space_prefix
                if(value_path == "flash-threshold"):
                    self.flash_threshold = value
                    self.flash_threshold.value_namespace = name_space
                    self.flash_threshold.value_namespace_prefix = name_space_prefix
                if(value_path == "flush-timer"):
                    self.flush_timer = value
                    self.flush_timer.value_namespace = name_space
                    self.flush_timer.value_namespace_prefix = name_space_prefix
                if(value_path == "hold-down-timer"):
                    self.hold_down_timer = value
                    self.hold_down_timer.value_namespace = name_space
                    self.hold_down_timer.value_namespace_prefix = name_space_prefix
                if(value_path == "input-q-length"):
                    self.input_q_length = value
                    self.input_q_length.value_namespace = name_space
                    self.input_q_length.value_namespace_prefix = name_space_prefix
                if(value_path == "invalid-timer"):
                    self.invalid_timer = value
                    self.invalid_timer.value_namespace = name_space
                    self.invalid_timer.value_namespace_prefix = name_space_prefix
                if(value_path == "maximum-paths"):
                    self.maximum_paths = value
                    self.maximum_paths.value_namespace = name_space
                    self.maximum_paths.value_namespace_prefix = name_space_prefix
                if(value_path == "multicast-address"):
                    self.multicast_address = value
                    self.multicast_address.value_namespace = name_space
                    self.multicast_address.value_namespace_prefix = name_space_prefix
                if(value_path == "next-update-time"):
                    self.next_update_time = value
                    self.next_update_time.value_namespace = name_space
                    self.next_update_time.value_namespace_prefix = name_space_prefix
                if(value_path == "nsf-life-time"):
                    self.nsf_life_time = value
                    self.nsf_life_time.value_namespace = name_space
                    self.nsf_life_time.value_namespace_prefix = name_space_prefix
                if(value_path == "nsf-status"):
                    self.nsf_status = value
                    self.nsf_status.value_namespace = name_space
                    self.nsf_status.value_namespace_prefix = name_space_prefix
                if(value_path == "oom-flags"):
                    self.oom_flags = value
                    self.oom_flags.value_namespace = name_space
                    self.oom_flags.value_namespace_prefix = name_space_prefix
                if(value_path == "rip-version"):
                    self.rip_version = value
                    self.rip_version.value_namespace = name_space
                    self.rip_version.value_namespace_prefix = name_space_prefix
                if(value_path == "triggered-rip"):
                    self.triggered_rip = value
                    self.triggered_rip.value_namespace = name_space
                    self.triggered_rip.value_namespace_prefix = name_space_prefix
                if(value_path == "update-timer"):
                    self.update_timer = value
                    self.update_timer.value_namespace = name_space
                    self.update_timer.value_namespace_prefix = name_space_prefix
                if(value_path == "validation-indicator"):
                    self.validation_indicator = value
                    self.validation_indicator.value_namespace = name_space
                    self.validation_indicator.value_namespace_prefix = name_space_prefix
                if(value_path == "vr-fised-socket"):
                    self.vr_fised_socket = value
                    self.vr_fised_socket.value_namespace = name_space
                    self.vr_fised_socket.value_namespace_prefix = name_space_prefix


        class Statistics(Entity):
            """
            RIP statistics information
            
            .. attribute:: discarded_packets
            
            	Total discarded packets
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: discarded_routes
            
            	Total discarded routes
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: path_count
            
            	Number of paths allocated
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: path_malloc_failures
            
            	Number of failures to allocate memory for a path
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: periodic_updates
            
            	Number of periodic RIP updates
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: query_responses
            
            	Number of RIP queries responded to
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: received_packets
            
            	Total packets received
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rib_updates
            
            	Number of route updates to RIB made by RIP
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: route_count
            
            	Number of routes allocated
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: route_malloc_failures
            
            	Number of failures to allocate memory for a route
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sent_message_failures
            
            	Number of message send failures
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sent_messages
            
            	Number of messages sent
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: standby_packets_received
            
            	Packets rx in SRP
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'ip-rip-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Rip.DefaultVrf.Statistics, self).__init__()

                self.yang_name = "statistics"
                self.yang_parent_name = "default-vrf"

                self.discarded_packets = YLeaf(YType.uint32, "discarded-packets")

                self.discarded_routes = YLeaf(YType.uint32, "discarded-routes")

                self.path_count = YLeaf(YType.uint32, "path-count")

                self.path_malloc_failures = YLeaf(YType.uint32, "path-malloc-failures")

                self.periodic_updates = YLeaf(YType.uint32, "periodic-updates")

                self.query_responses = YLeaf(YType.uint32, "query-responses")

                self.received_packets = YLeaf(YType.uint32, "received-packets")

                self.rib_updates = YLeaf(YType.uint32, "rib-updates")

                self.route_count = YLeaf(YType.uint32, "route-count")

                self.route_malloc_failures = YLeaf(YType.uint32, "route-malloc-failures")

                self.sent_message_failures = YLeaf(YType.uint32, "sent-message-failures")

                self.sent_messages = YLeaf(YType.uint32, "sent-messages")

                self.standby_packets_received = YLeaf(YType.uint32, "standby-packets-received")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("discarded_packets",
                                "discarded_routes",
                                "path_count",
                                "path_malloc_failures",
                                "periodic_updates",
                                "query_responses",
                                "received_packets",
                                "rib_updates",
                                "route_count",
                                "route_malloc_failures",
                                "sent_message_failures",
                                "sent_messages",
                                "standby_packets_received") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Rip.DefaultVrf.Statistics, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Rip.DefaultVrf.Statistics, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.discarded_packets.is_set or
                    self.discarded_routes.is_set or
                    self.path_count.is_set or
                    self.path_malloc_failures.is_set or
                    self.periodic_updates.is_set or
                    self.query_responses.is_set or
                    self.received_packets.is_set or
                    self.rib_updates.is_set or
                    self.route_count.is_set or
                    self.route_malloc_failures.is_set or
                    self.sent_message_failures.is_set or
                    self.sent_messages.is_set or
                    self.standby_packets_received.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.discarded_packets.yfilter != YFilter.not_set or
                    self.discarded_routes.yfilter != YFilter.not_set or
                    self.path_count.yfilter != YFilter.not_set or
                    self.path_malloc_failures.yfilter != YFilter.not_set or
                    self.periodic_updates.yfilter != YFilter.not_set or
                    self.query_responses.yfilter != YFilter.not_set or
                    self.received_packets.yfilter != YFilter.not_set or
                    self.rib_updates.yfilter != YFilter.not_set or
                    self.route_count.yfilter != YFilter.not_set or
                    self.route_malloc_failures.yfilter != YFilter.not_set or
                    self.sent_message_failures.yfilter != YFilter.not_set or
                    self.sent_messages.yfilter != YFilter.not_set or
                    self.standby_packets_received.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "statistics" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ip-rip-oper:rip/default-vrf/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.discarded_packets.is_set or self.discarded_packets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.discarded_packets.get_name_leafdata())
                if (self.discarded_routes.is_set or self.discarded_routes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.discarded_routes.get_name_leafdata())
                if (self.path_count.is_set or self.path_count.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.path_count.get_name_leafdata())
                if (self.path_malloc_failures.is_set or self.path_malloc_failures.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.path_malloc_failures.get_name_leafdata())
                if (self.periodic_updates.is_set or self.periodic_updates.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.periodic_updates.get_name_leafdata())
                if (self.query_responses.is_set or self.query_responses.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.query_responses.get_name_leafdata())
                if (self.received_packets.is_set or self.received_packets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.received_packets.get_name_leafdata())
                if (self.rib_updates.is_set or self.rib_updates.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rib_updates.get_name_leafdata())
                if (self.route_count.is_set or self.route_count.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.route_count.get_name_leafdata())
                if (self.route_malloc_failures.is_set or self.route_malloc_failures.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.route_malloc_failures.get_name_leafdata())
                if (self.sent_message_failures.is_set or self.sent_message_failures.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sent_message_failures.get_name_leafdata())
                if (self.sent_messages.is_set or self.sent_messages.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sent_messages.get_name_leafdata())
                if (self.standby_packets_received.is_set or self.standby_packets_received.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.standby_packets_received.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "discarded-packets" or name == "discarded-routes" or name == "path-count" or name == "path-malloc-failures" or name == "periodic-updates" or name == "query-responses" or name == "received-packets" or name == "rib-updates" or name == "route-count" or name == "route-malloc-failures" or name == "sent-message-failures" or name == "sent-messages" or name == "standby-packets-received"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "discarded-packets"):
                    self.discarded_packets = value
                    self.discarded_packets.value_namespace = name_space
                    self.discarded_packets.value_namespace_prefix = name_space_prefix
                if(value_path == "discarded-routes"):
                    self.discarded_routes = value
                    self.discarded_routes.value_namespace = name_space
                    self.discarded_routes.value_namespace_prefix = name_space_prefix
                if(value_path == "path-count"):
                    self.path_count = value
                    self.path_count.value_namespace = name_space
                    self.path_count.value_namespace_prefix = name_space_prefix
                if(value_path == "path-malloc-failures"):
                    self.path_malloc_failures = value
                    self.path_malloc_failures.value_namespace = name_space
                    self.path_malloc_failures.value_namespace_prefix = name_space_prefix
                if(value_path == "periodic-updates"):
                    self.periodic_updates = value
                    self.periodic_updates.value_namespace = name_space
                    self.periodic_updates.value_namespace_prefix = name_space_prefix
                if(value_path == "query-responses"):
                    self.query_responses = value
                    self.query_responses.value_namespace = name_space
                    self.query_responses.value_namespace_prefix = name_space_prefix
                if(value_path == "received-packets"):
                    self.received_packets = value
                    self.received_packets.value_namespace = name_space
                    self.received_packets.value_namespace_prefix = name_space_prefix
                if(value_path == "rib-updates"):
                    self.rib_updates = value
                    self.rib_updates.value_namespace = name_space
                    self.rib_updates.value_namespace_prefix = name_space_prefix
                if(value_path == "route-count"):
                    self.route_count = value
                    self.route_count.value_namespace = name_space
                    self.route_count.value_namespace_prefix = name_space_prefix
                if(value_path == "route-malloc-failures"):
                    self.route_malloc_failures = value
                    self.route_malloc_failures.value_namespace = name_space
                    self.route_malloc_failures.value_namespace_prefix = name_space_prefix
                if(value_path == "sent-message-failures"):
                    self.sent_message_failures = value
                    self.sent_message_failures.value_namespace = name_space
                    self.sent_message_failures.value_namespace_prefix = name_space_prefix
                if(value_path == "sent-messages"):
                    self.sent_messages = value
                    self.sent_messages.value_namespace = name_space
                    self.sent_messages.value_namespace_prefix = name_space_prefix
                if(value_path == "standby-packets-received"):
                    self.standby_packets_received = value
                    self.standby_packets_received.value_namespace = name_space
                    self.standby_packets_received.value_namespace_prefix = name_space_prefix


        class Interfaces(Entity):
            """
            RIP interfaces
            
            .. attribute:: interface
            
            	Information about a particular RIP interface
            	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.DefaultVrf.Interfaces.Interface>`
            
            

            """

            _prefix = 'ip-rip-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Rip.DefaultVrf.Interfaces, self).__init__()

                self.yang_name = "interfaces"
                self.yang_parent_name = "default-vrf"

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
                    if name in () and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Rip.DefaultVrf.Interfaces, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Rip.DefaultVrf.Interfaces, self).__setattr__(name, value)


            class Interface(Entity):
                """
                Information about a particular RIP interface
                
                .. attribute:: interface_name  <key>
                
                	Interface name
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: accept_metric
                
                	Accept routes of metric 0 indicator
                	**type**\:  bool
                
                .. attribute:: auth_key_md5
                
                	Authentication key programmed with MD5 algorithm
                	**type**\:  bool
                
                .. attribute:: auth_key_send_id
                
                	Current active Send Authentication Key Id
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: auth_keychain
                
                	Authentication Keychain Name
                	**type**\:  str
                
                .. attribute:: auth_mode
                
                	Authentication Mode
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: destination_address
                
                	IP Address of this interface
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: if_handle
                
                	Interface handle
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: interface
                
                	Interface name
                	**type**\:  str
                
                .. attribute:: is_passive_interface
                
                	Passive interface indicator
                	**type**\:  bool
                
                .. attribute:: join_status
                
                	Multicast group join status
                	**type**\:  bool
                
                .. attribute:: lpts_state
                
                	LPTSState
                	**type**\:  bool
                
                .. attribute:: metric_cost
                
                	Cost added to routes through this interface
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: multicast_address
                
                	Use broadcast address for v2 packets
                	**type**\:  bool
                
                .. attribute:: neighbor_address
                
                	Interface's triggered RIP neighbor
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: oom_flags
                
                	Out\-of\-memory status flags
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pkt_accepted_valid_auth
                
                	Packets accepted with valid authentication data
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pkt_drop_invalid_auth
                
                	Packets dropped due to invalid authentication data
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pkt_drop_no_auth
                
                	Packets dropped due to missing authentication data
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pkt_drop_wrong_kc
                
                	Packets dropped due to wrong keychain configured
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: poison_horizon
                
                	Poisoned reverse enabled indicator
                	**type**\:  bool
                
                .. attribute:: prefix_length
                
                	Prefix length of the IP address
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: receive_version
                
                	Versions that the interface will recieve
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: rip_enabled
                
                	Whether RIP is enabled on this interface
                	**type**\:  bool
                
                .. attribute:: rip_peer
                
                	Neighbors on this interface
                	**type**\: list of    :py:class:`RipPeer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.DefaultVrf.Interfaces.Interface.RipPeer>`
                
                .. attribute:: rip_summary
                
                	User defined summary addresses
                	**type**\: list of    :py:class:`RipSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.DefaultVrf.Interfaces.Interface.RipSummary>`
                
                .. attribute:: send_auth_key_exists
                
                	Authentication send key exists
                	**type**\:  bool
                
                .. attribute:: send_version
                
                	Versions that the interface is sending
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: split_horizon
                
                	Split horizon enabled indicator
                	**type**\:  bool
                
                .. attribute:: state
                
                	Current state of the interface
                	**type**\:   :py:class:`InterfaceState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.InterfaceState>`
                
                .. attribute:: total_pkt_recvd
                
                	Total packets received
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: triggered_rip
                
                	Triggered RIP enabled indicator
                	**type**\:  bool
                
                

                """

                _prefix = 'ip-rip-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rip.DefaultVrf.Interfaces.Interface, self).__init__()

                    self.yang_name = "interface"
                    self.yang_parent_name = "interfaces"

                    self.interface_name = YLeaf(YType.str, "interface-name")

                    self.accept_metric = YLeaf(YType.boolean, "accept-metric")

                    self.auth_key_md5 = YLeaf(YType.boolean, "auth-key-md5")

                    self.auth_key_send_id = YLeaf(YType.uint64, "auth-key-send-id")

                    self.auth_keychain = YLeaf(YType.str, "auth-keychain")

                    self.auth_mode = YLeaf(YType.uint32, "auth-mode")

                    self.destination_address = YLeaf(YType.str, "destination-address")

                    self.if_handle = YLeaf(YType.str, "if-handle")

                    self.interface = YLeaf(YType.str, "interface")

                    self.is_passive_interface = YLeaf(YType.boolean, "is-passive-interface")

                    self.join_status = YLeaf(YType.boolean, "join-status")

                    self.lpts_state = YLeaf(YType.boolean, "lpts-state")

                    self.metric_cost = YLeaf(YType.uint32, "metric-cost")

                    self.multicast_address = YLeaf(YType.boolean, "multicast-address")

                    self.neighbor_address = YLeaf(YType.str, "neighbor-address")

                    self.oom_flags = YLeaf(YType.uint32, "oom-flags")

                    self.pkt_accepted_valid_auth = YLeaf(YType.uint32, "pkt-accepted-valid-auth")

                    self.pkt_drop_invalid_auth = YLeaf(YType.uint32, "pkt-drop-invalid-auth")

                    self.pkt_drop_no_auth = YLeaf(YType.uint32, "pkt-drop-no-auth")

                    self.pkt_drop_wrong_kc = YLeaf(YType.uint32, "pkt-drop-wrong-kc")

                    self.poison_horizon = YLeaf(YType.boolean, "poison-horizon")

                    self.prefix_length = YLeaf(YType.uint32, "prefix-length")

                    self.receive_version = YLeaf(YType.uint32, "receive-version")

                    self.rip_enabled = YLeaf(YType.boolean, "rip-enabled")

                    self.send_auth_key_exists = YLeaf(YType.boolean, "send-auth-key-exists")

                    self.send_version = YLeaf(YType.uint32, "send-version")

                    self.split_horizon = YLeaf(YType.boolean, "split-horizon")

                    self.state = YLeaf(YType.enumeration, "state")

                    self.total_pkt_recvd = YLeaf(YType.uint32, "total-pkt-recvd")

                    self.triggered_rip = YLeaf(YType.boolean, "triggered-rip")

                    self.rip_peer = YList(self)
                    self.rip_summary = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("interface_name",
                                    "accept_metric",
                                    "auth_key_md5",
                                    "auth_key_send_id",
                                    "auth_keychain",
                                    "auth_mode",
                                    "destination_address",
                                    "if_handle",
                                    "interface",
                                    "is_passive_interface",
                                    "join_status",
                                    "lpts_state",
                                    "metric_cost",
                                    "multicast_address",
                                    "neighbor_address",
                                    "oom_flags",
                                    "pkt_accepted_valid_auth",
                                    "pkt_drop_invalid_auth",
                                    "pkt_drop_no_auth",
                                    "pkt_drop_wrong_kc",
                                    "poison_horizon",
                                    "prefix_length",
                                    "receive_version",
                                    "rip_enabled",
                                    "send_auth_key_exists",
                                    "send_version",
                                    "split_horizon",
                                    "state",
                                    "total_pkt_recvd",
                                    "triggered_rip") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Rip.DefaultVrf.Interfaces.Interface, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Rip.DefaultVrf.Interfaces.Interface, self).__setattr__(name, value)


                class RipSummary(Entity):
                    """
                    User defined summary addresses
                    
                    .. attribute:: metric
                    
                    	Summary metric
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: next_hop_address
                    
                    	Summary address next hop
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: prefix
                    
                    	Summary address prefix
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: prefix_length
                    
                    	Summary address prefix length
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ip-rip-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Rip.DefaultVrf.Interfaces.Interface.RipSummary, self).__init__()

                        self.yang_name = "rip-summary"
                        self.yang_parent_name = "interface"

                        self.metric = YLeaf(YType.int32, "metric")

                        self.next_hop_address = YLeaf(YType.str, "next-hop-address")

                        self.prefix = YLeaf(YType.str, "prefix")

                        self.prefix_length = YLeaf(YType.uint32, "prefix-length")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("metric",
                                        "next_hop_address",
                                        "prefix",
                                        "prefix_length") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Rip.DefaultVrf.Interfaces.Interface.RipSummary, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Rip.DefaultVrf.Interfaces.Interface.RipSummary, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.metric.is_set or
                            self.next_hop_address.is_set or
                            self.prefix.is_set or
                            self.prefix_length.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.metric.yfilter != YFilter.not_set or
                            self.next_hop_address.yfilter != YFilter.not_set or
                            self.prefix.yfilter != YFilter.not_set or
                            self.prefix_length.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "rip-summary" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.metric.is_set or self.metric.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.metric.get_name_leafdata())
                        if (self.next_hop_address.is_set or self.next_hop_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.next_hop_address.get_name_leafdata())
                        if (self.prefix.is_set or self.prefix.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.prefix.get_name_leafdata())
                        if (self.prefix_length.is_set or self.prefix_length.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.prefix_length.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "metric" or name == "next-hop-address" or name == "prefix" or name == "prefix-length"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "metric"):
                            self.metric = value
                            self.metric.value_namespace = name_space
                            self.metric.value_namespace_prefix = name_space_prefix
                        if(value_path == "next-hop-address"):
                            self.next_hop_address = value
                            self.next_hop_address.value_namespace = name_space
                            self.next_hop_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "prefix"):
                            self.prefix = value
                            self.prefix.value_namespace = name_space
                            self.prefix.value_namespace_prefix = name_space_prefix
                        if(value_path == "prefix-length"):
                            self.prefix_length = value
                            self.prefix_length.value_namespace = name_space
                            self.prefix_length.value_namespace_prefix = name_space_prefix


                class RipPeer(Entity):
                    """
                    Neighbors on this interface
                    
                    .. attribute:: discarded_peer_packets
                    
                    	Discarded packets from this peer
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: discarded_peer_routes
                    
                    	Discarded routes from this peer
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: peer_address
                    
                    	IP Address of this peer
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: peer_uptime
                    
                    	Uptime of this peer
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: peer_version
                    
                    	RIP version for this peer
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'ip-rip-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Rip.DefaultVrf.Interfaces.Interface.RipPeer, self).__init__()

                        self.yang_name = "rip-peer"
                        self.yang_parent_name = "interface"

                        self.discarded_peer_packets = YLeaf(YType.uint32, "discarded-peer-packets")

                        self.discarded_peer_routes = YLeaf(YType.uint32, "discarded-peer-routes")

                        self.peer_address = YLeaf(YType.str, "peer-address")

                        self.peer_uptime = YLeaf(YType.uint32, "peer-uptime")

                        self.peer_version = YLeaf(YType.uint8, "peer-version")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("discarded_peer_packets",
                                        "discarded_peer_routes",
                                        "peer_address",
                                        "peer_uptime",
                                        "peer_version") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Rip.DefaultVrf.Interfaces.Interface.RipPeer, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Rip.DefaultVrf.Interfaces.Interface.RipPeer, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.discarded_peer_packets.is_set or
                            self.discarded_peer_routes.is_set or
                            self.peer_address.is_set or
                            self.peer_uptime.is_set or
                            self.peer_version.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.discarded_peer_packets.yfilter != YFilter.not_set or
                            self.discarded_peer_routes.yfilter != YFilter.not_set or
                            self.peer_address.yfilter != YFilter.not_set or
                            self.peer_uptime.yfilter != YFilter.not_set or
                            self.peer_version.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "rip-peer" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.discarded_peer_packets.is_set or self.discarded_peer_packets.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.discarded_peer_packets.get_name_leafdata())
                        if (self.discarded_peer_routes.is_set or self.discarded_peer_routes.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.discarded_peer_routes.get_name_leafdata())
                        if (self.peer_address.is_set or self.peer_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.peer_address.get_name_leafdata())
                        if (self.peer_uptime.is_set or self.peer_uptime.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.peer_uptime.get_name_leafdata())
                        if (self.peer_version.is_set or self.peer_version.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.peer_version.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "discarded-peer-packets" or name == "discarded-peer-routes" or name == "peer-address" or name == "peer-uptime" or name == "peer-version"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "discarded-peer-packets"):
                            self.discarded_peer_packets = value
                            self.discarded_peer_packets.value_namespace = name_space
                            self.discarded_peer_packets.value_namespace_prefix = name_space_prefix
                        if(value_path == "discarded-peer-routes"):
                            self.discarded_peer_routes = value
                            self.discarded_peer_routes.value_namespace = name_space
                            self.discarded_peer_routes.value_namespace_prefix = name_space_prefix
                        if(value_path == "peer-address"):
                            self.peer_address = value
                            self.peer_address.value_namespace = name_space
                            self.peer_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "peer-uptime"):
                            self.peer_uptime = value
                            self.peer_uptime.value_namespace = name_space
                            self.peer_uptime.value_namespace_prefix = name_space_prefix
                        if(value_path == "peer-version"):
                            self.peer_version = value
                            self.peer_version.value_namespace = name_space
                            self.peer_version.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.rip_peer:
                        if (c.has_data()):
                            return True
                    for c in self.rip_summary:
                        if (c.has_data()):
                            return True
                    return (
                        self.interface_name.is_set or
                        self.accept_metric.is_set or
                        self.auth_key_md5.is_set or
                        self.auth_key_send_id.is_set or
                        self.auth_keychain.is_set or
                        self.auth_mode.is_set or
                        self.destination_address.is_set or
                        self.if_handle.is_set or
                        self.interface.is_set or
                        self.is_passive_interface.is_set or
                        self.join_status.is_set or
                        self.lpts_state.is_set or
                        self.metric_cost.is_set or
                        self.multicast_address.is_set or
                        self.neighbor_address.is_set or
                        self.oom_flags.is_set or
                        self.pkt_accepted_valid_auth.is_set or
                        self.pkt_drop_invalid_auth.is_set or
                        self.pkt_drop_no_auth.is_set or
                        self.pkt_drop_wrong_kc.is_set or
                        self.poison_horizon.is_set or
                        self.prefix_length.is_set or
                        self.receive_version.is_set or
                        self.rip_enabled.is_set or
                        self.send_auth_key_exists.is_set or
                        self.send_version.is_set or
                        self.split_horizon.is_set or
                        self.state.is_set or
                        self.total_pkt_recvd.is_set or
                        self.triggered_rip.is_set)

                def has_operation(self):
                    for c in self.rip_peer:
                        if (c.has_operation()):
                            return True
                    for c in self.rip_summary:
                        if (c.has_operation()):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.interface_name.yfilter != YFilter.not_set or
                        self.accept_metric.yfilter != YFilter.not_set or
                        self.auth_key_md5.yfilter != YFilter.not_set or
                        self.auth_key_send_id.yfilter != YFilter.not_set or
                        self.auth_keychain.yfilter != YFilter.not_set or
                        self.auth_mode.yfilter != YFilter.not_set or
                        self.destination_address.yfilter != YFilter.not_set or
                        self.if_handle.yfilter != YFilter.not_set or
                        self.interface.yfilter != YFilter.not_set or
                        self.is_passive_interface.yfilter != YFilter.not_set or
                        self.join_status.yfilter != YFilter.not_set or
                        self.lpts_state.yfilter != YFilter.not_set or
                        self.metric_cost.yfilter != YFilter.not_set or
                        self.multicast_address.yfilter != YFilter.not_set or
                        self.neighbor_address.yfilter != YFilter.not_set or
                        self.oom_flags.yfilter != YFilter.not_set or
                        self.pkt_accepted_valid_auth.yfilter != YFilter.not_set or
                        self.pkt_drop_invalid_auth.yfilter != YFilter.not_set or
                        self.pkt_drop_no_auth.yfilter != YFilter.not_set or
                        self.pkt_drop_wrong_kc.yfilter != YFilter.not_set or
                        self.poison_horizon.yfilter != YFilter.not_set or
                        self.prefix_length.yfilter != YFilter.not_set or
                        self.receive_version.yfilter != YFilter.not_set or
                        self.rip_enabled.yfilter != YFilter.not_set or
                        self.send_auth_key_exists.yfilter != YFilter.not_set or
                        self.send_version.yfilter != YFilter.not_set or
                        self.split_horizon.yfilter != YFilter.not_set or
                        self.state.yfilter != YFilter.not_set or
                        self.total_pkt_recvd.yfilter != YFilter.not_set or
                        self.triggered_rip.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "interface" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ip-rip-oper:rip/default-vrf/interfaces/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.interface_name.get_name_leafdata())
                    if (self.accept_metric.is_set or self.accept_metric.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.accept_metric.get_name_leafdata())
                    if (self.auth_key_md5.is_set or self.auth_key_md5.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.auth_key_md5.get_name_leafdata())
                    if (self.auth_key_send_id.is_set or self.auth_key_send_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.auth_key_send_id.get_name_leafdata())
                    if (self.auth_keychain.is_set or self.auth_keychain.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.auth_keychain.get_name_leafdata())
                    if (self.auth_mode.is_set or self.auth_mode.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.auth_mode.get_name_leafdata())
                    if (self.destination_address.is_set or self.destination_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.destination_address.get_name_leafdata())
                    if (self.if_handle.is_set or self.if_handle.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.if_handle.get_name_leafdata())
                    if (self.interface.is_set or self.interface.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.interface.get_name_leafdata())
                    if (self.is_passive_interface.is_set or self.is_passive_interface.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.is_passive_interface.get_name_leafdata())
                    if (self.join_status.is_set or self.join_status.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.join_status.get_name_leafdata())
                    if (self.lpts_state.is_set or self.lpts_state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.lpts_state.get_name_leafdata())
                    if (self.metric_cost.is_set or self.metric_cost.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.metric_cost.get_name_leafdata())
                    if (self.multicast_address.is_set or self.multicast_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.multicast_address.get_name_leafdata())
                    if (self.neighbor_address.is_set or self.neighbor_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.neighbor_address.get_name_leafdata())
                    if (self.oom_flags.is_set or self.oom_flags.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.oom_flags.get_name_leafdata())
                    if (self.pkt_accepted_valid_auth.is_set or self.pkt_accepted_valid_auth.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.pkt_accepted_valid_auth.get_name_leafdata())
                    if (self.pkt_drop_invalid_auth.is_set or self.pkt_drop_invalid_auth.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.pkt_drop_invalid_auth.get_name_leafdata())
                    if (self.pkt_drop_no_auth.is_set or self.pkt_drop_no_auth.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.pkt_drop_no_auth.get_name_leafdata())
                    if (self.pkt_drop_wrong_kc.is_set or self.pkt_drop_wrong_kc.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.pkt_drop_wrong_kc.get_name_leafdata())
                    if (self.poison_horizon.is_set or self.poison_horizon.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.poison_horizon.get_name_leafdata())
                    if (self.prefix_length.is_set or self.prefix_length.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.prefix_length.get_name_leafdata())
                    if (self.receive_version.is_set or self.receive_version.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.receive_version.get_name_leafdata())
                    if (self.rip_enabled.is_set or self.rip_enabled.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rip_enabled.get_name_leafdata())
                    if (self.send_auth_key_exists.is_set or self.send_auth_key_exists.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.send_auth_key_exists.get_name_leafdata())
                    if (self.send_version.is_set or self.send_version.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.send_version.get_name_leafdata())
                    if (self.split_horizon.is_set or self.split_horizon.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.split_horizon.get_name_leafdata())
                    if (self.state.is_set or self.state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.state.get_name_leafdata())
                    if (self.total_pkt_recvd.is_set or self.total_pkt_recvd.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.total_pkt_recvd.get_name_leafdata())
                    if (self.triggered_rip.is_set or self.triggered_rip.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.triggered_rip.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "rip-peer"):
                        for c in self.rip_peer:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Rip.DefaultVrf.Interfaces.Interface.RipPeer()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.rip_peer.append(c)
                        return c

                    if (child_yang_name == "rip-summary"):
                        for c in self.rip_summary:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Rip.DefaultVrf.Interfaces.Interface.RipSummary()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.rip_summary.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "rip-peer" or name == "rip-summary" or name == "interface-name" or name == "accept-metric" or name == "auth-key-md5" or name == "auth-key-send-id" or name == "auth-keychain" or name == "auth-mode" or name == "destination-address" or name == "if-handle" or name == "interface" or name == "is-passive-interface" or name == "join-status" or name == "lpts-state" or name == "metric-cost" or name == "multicast-address" or name == "neighbor-address" or name == "oom-flags" or name == "pkt-accepted-valid-auth" or name == "pkt-drop-invalid-auth" or name == "pkt-drop-no-auth" or name == "pkt-drop-wrong-kc" or name == "poison-horizon" or name == "prefix-length" or name == "receive-version" or name == "rip-enabled" or name == "send-auth-key-exists" or name == "send-version" or name == "split-horizon" or name == "state" or name == "total-pkt-recvd" or name == "triggered-rip"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "interface-name"):
                        self.interface_name = value
                        self.interface_name.value_namespace = name_space
                        self.interface_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "accept-metric"):
                        self.accept_metric = value
                        self.accept_metric.value_namespace = name_space
                        self.accept_metric.value_namespace_prefix = name_space_prefix
                    if(value_path == "auth-key-md5"):
                        self.auth_key_md5 = value
                        self.auth_key_md5.value_namespace = name_space
                        self.auth_key_md5.value_namespace_prefix = name_space_prefix
                    if(value_path == "auth-key-send-id"):
                        self.auth_key_send_id = value
                        self.auth_key_send_id.value_namespace = name_space
                        self.auth_key_send_id.value_namespace_prefix = name_space_prefix
                    if(value_path == "auth-keychain"):
                        self.auth_keychain = value
                        self.auth_keychain.value_namespace = name_space
                        self.auth_keychain.value_namespace_prefix = name_space_prefix
                    if(value_path == "auth-mode"):
                        self.auth_mode = value
                        self.auth_mode.value_namespace = name_space
                        self.auth_mode.value_namespace_prefix = name_space_prefix
                    if(value_path == "destination-address"):
                        self.destination_address = value
                        self.destination_address.value_namespace = name_space
                        self.destination_address.value_namespace_prefix = name_space_prefix
                    if(value_path == "if-handle"):
                        self.if_handle = value
                        self.if_handle.value_namespace = name_space
                        self.if_handle.value_namespace_prefix = name_space_prefix
                    if(value_path == "interface"):
                        self.interface = value
                        self.interface.value_namespace = name_space
                        self.interface.value_namespace_prefix = name_space_prefix
                    if(value_path == "is-passive-interface"):
                        self.is_passive_interface = value
                        self.is_passive_interface.value_namespace = name_space
                        self.is_passive_interface.value_namespace_prefix = name_space_prefix
                    if(value_path == "join-status"):
                        self.join_status = value
                        self.join_status.value_namespace = name_space
                        self.join_status.value_namespace_prefix = name_space_prefix
                    if(value_path == "lpts-state"):
                        self.lpts_state = value
                        self.lpts_state.value_namespace = name_space
                        self.lpts_state.value_namespace_prefix = name_space_prefix
                    if(value_path == "metric-cost"):
                        self.metric_cost = value
                        self.metric_cost.value_namespace = name_space
                        self.metric_cost.value_namespace_prefix = name_space_prefix
                    if(value_path == "multicast-address"):
                        self.multicast_address = value
                        self.multicast_address.value_namespace = name_space
                        self.multicast_address.value_namespace_prefix = name_space_prefix
                    if(value_path == "neighbor-address"):
                        self.neighbor_address = value
                        self.neighbor_address.value_namespace = name_space
                        self.neighbor_address.value_namespace_prefix = name_space_prefix
                    if(value_path == "oom-flags"):
                        self.oom_flags = value
                        self.oom_flags.value_namespace = name_space
                        self.oom_flags.value_namespace_prefix = name_space_prefix
                    if(value_path == "pkt-accepted-valid-auth"):
                        self.pkt_accepted_valid_auth = value
                        self.pkt_accepted_valid_auth.value_namespace = name_space
                        self.pkt_accepted_valid_auth.value_namespace_prefix = name_space_prefix
                    if(value_path == "pkt-drop-invalid-auth"):
                        self.pkt_drop_invalid_auth = value
                        self.pkt_drop_invalid_auth.value_namespace = name_space
                        self.pkt_drop_invalid_auth.value_namespace_prefix = name_space_prefix
                    if(value_path == "pkt-drop-no-auth"):
                        self.pkt_drop_no_auth = value
                        self.pkt_drop_no_auth.value_namespace = name_space
                        self.pkt_drop_no_auth.value_namespace_prefix = name_space_prefix
                    if(value_path == "pkt-drop-wrong-kc"):
                        self.pkt_drop_wrong_kc = value
                        self.pkt_drop_wrong_kc.value_namespace = name_space
                        self.pkt_drop_wrong_kc.value_namespace_prefix = name_space_prefix
                    if(value_path == "poison-horizon"):
                        self.poison_horizon = value
                        self.poison_horizon.value_namespace = name_space
                        self.poison_horizon.value_namespace_prefix = name_space_prefix
                    if(value_path == "prefix-length"):
                        self.prefix_length = value
                        self.prefix_length.value_namespace = name_space
                        self.prefix_length.value_namespace_prefix = name_space_prefix
                    if(value_path == "receive-version"):
                        self.receive_version = value
                        self.receive_version.value_namespace = name_space
                        self.receive_version.value_namespace_prefix = name_space_prefix
                    if(value_path == "rip-enabled"):
                        self.rip_enabled = value
                        self.rip_enabled.value_namespace = name_space
                        self.rip_enabled.value_namespace_prefix = name_space_prefix
                    if(value_path == "send-auth-key-exists"):
                        self.send_auth_key_exists = value
                        self.send_auth_key_exists.value_namespace = name_space
                        self.send_auth_key_exists.value_namespace_prefix = name_space_prefix
                    if(value_path == "send-version"):
                        self.send_version = value
                        self.send_version.value_namespace = name_space
                        self.send_version.value_namespace_prefix = name_space_prefix
                    if(value_path == "split-horizon"):
                        self.split_horizon = value
                        self.split_horizon.value_namespace = name_space
                        self.split_horizon.value_namespace_prefix = name_space_prefix
                    if(value_path == "state"):
                        self.state = value
                        self.state.value_namespace = name_space
                        self.state.value_namespace_prefix = name_space_prefix
                    if(value_path == "total-pkt-recvd"):
                        self.total_pkt_recvd = value
                        self.total_pkt_recvd.value_namespace = name_space
                        self.total_pkt_recvd.value_namespace_prefix = name_space_prefix
                    if(value_path == "triggered-rip"):
                        self.triggered_rip = value
                        self.triggered_rip.value_namespace = name_space
                        self.triggered_rip.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.interface:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.interface:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "interfaces" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ip-rip-oper:rip/default-vrf/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "interface"):
                    for c in self.interface:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Rip.DefaultVrf.Interfaces.Interface()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.interface.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "interface"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class Global_(Entity):
            """
            Global Information 
            
            .. attribute:: interface_summary
            
            	List of Interfaces configured
            	**type**\: list of    :py:class:`InterfaceSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.DefaultVrf.Global_.InterfaceSummary>`
            
            .. attribute:: vrf_summary
            
            	VRF summary data
            	**type**\:   :py:class:`VrfSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.DefaultVrf.Global_.VrfSummary>`
            
            

            """

            _prefix = 'ip-rip-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Rip.DefaultVrf.Global_, self).__init__()

                self.yang_name = "global"
                self.yang_parent_name = "default-vrf"

                self.vrf_summary = Rip.DefaultVrf.Global_.VrfSummary()
                self.vrf_summary.parent = self
                self._children_name_map["vrf_summary"] = "vrf-summary"
                self._children_yang_names.add("vrf-summary")

                self.interface_summary = YList(self)

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
                            super(Rip.DefaultVrf.Global_, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Rip.DefaultVrf.Global_, self).__setattr__(name, value)


            class VrfSummary(Entity):
                """
                VRF summary data
                
                .. attribute:: active
                
                	VRF Active indicator
                	**type**\:  bool
                
                .. attribute:: active_interface_count
                
                	Number of active interfaces
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: flush_timer
                
                	Flush timer
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: hold_down_timer
                
                	Holddown timer
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: interface_configured_count
                
                	Number of interfaces configured
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: invalid_timer
                
                	Invalid timer
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: next_update_time
                
                	Time left for next update
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: oom_flags
                
                	Current OOM flags
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: path_count
                
                	Number of paths allocated
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: route_count
                
                	Number of routes allocated
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: update_timer
                
                	Update timer
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: vrf_name
                
                	VRF Name
                	**type**\:  str
                
                

                """

                _prefix = 'ip-rip-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rip.DefaultVrf.Global_.VrfSummary, self).__init__()

                    self.yang_name = "vrf-summary"
                    self.yang_parent_name = "global"

                    self.active = YLeaf(YType.boolean, "active")

                    self.active_interface_count = YLeaf(YType.uint32, "active-interface-count")

                    self.flush_timer = YLeaf(YType.uint32, "flush-timer")

                    self.hold_down_timer = YLeaf(YType.uint32, "hold-down-timer")

                    self.interface_configured_count = YLeaf(YType.uint32, "interface-configured-count")

                    self.invalid_timer = YLeaf(YType.uint32, "invalid-timer")

                    self.next_update_time = YLeaf(YType.uint32, "next-update-time")

                    self.oom_flags = YLeaf(YType.uint32, "oom-flags")

                    self.path_count = YLeaf(YType.uint32, "path-count")

                    self.route_count = YLeaf(YType.uint32, "route-count")

                    self.update_timer = YLeaf(YType.uint32, "update-timer")

                    self.vrf_name = YLeaf(YType.str, "vrf-name")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("active",
                                    "active_interface_count",
                                    "flush_timer",
                                    "hold_down_timer",
                                    "interface_configured_count",
                                    "invalid_timer",
                                    "next_update_time",
                                    "oom_flags",
                                    "path_count",
                                    "route_count",
                                    "update_timer",
                                    "vrf_name") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Rip.DefaultVrf.Global_.VrfSummary, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Rip.DefaultVrf.Global_.VrfSummary, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.active.is_set or
                        self.active_interface_count.is_set or
                        self.flush_timer.is_set or
                        self.hold_down_timer.is_set or
                        self.interface_configured_count.is_set or
                        self.invalid_timer.is_set or
                        self.next_update_time.is_set or
                        self.oom_flags.is_set or
                        self.path_count.is_set or
                        self.route_count.is_set or
                        self.update_timer.is_set or
                        self.vrf_name.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.active.yfilter != YFilter.not_set or
                        self.active_interface_count.yfilter != YFilter.not_set or
                        self.flush_timer.yfilter != YFilter.not_set or
                        self.hold_down_timer.yfilter != YFilter.not_set or
                        self.interface_configured_count.yfilter != YFilter.not_set or
                        self.invalid_timer.yfilter != YFilter.not_set or
                        self.next_update_time.yfilter != YFilter.not_set or
                        self.oom_flags.yfilter != YFilter.not_set or
                        self.path_count.yfilter != YFilter.not_set or
                        self.route_count.yfilter != YFilter.not_set or
                        self.update_timer.yfilter != YFilter.not_set or
                        self.vrf_name.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "vrf-summary" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ip-rip-oper:rip/default-vrf/global/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.active.is_set or self.active.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.active.get_name_leafdata())
                    if (self.active_interface_count.is_set or self.active_interface_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.active_interface_count.get_name_leafdata())
                    if (self.flush_timer.is_set or self.flush_timer.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.flush_timer.get_name_leafdata())
                    if (self.hold_down_timer.is_set or self.hold_down_timer.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.hold_down_timer.get_name_leafdata())
                    if (self.interface_configured_count.is_set or self.interface_configured_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.interface_configured_count.get_name_leafdata())
                    if (self.invalid_timer.is_set or self.invalid_timer.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.invalid_timer.get_name_leafdata())
                    if (self.next_update_time.is_set or self.next_update_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.next_update_time.get_name_leafdata())
                    if (self.oom_flags.is_set or self.oom_flags.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.oom_flags.get_name_leafdata())
                    if (self.path_count.is_set or self.path_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.path_count.get_name_leafdata())
                    if (self.route_count.is_set or self.route_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.route_count.get_name_leafdata())
                    if (self.update_timer.is_set or self.update_timer.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.update_timer.get_name_leafdata())
                    if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.vrf_name.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "active" or name == "active-interface-count" or name == "flush-timer" or name == "hold-down-timer" or name == "interface-configured-count" or name == "invalid-timer" or name == "next-update-time" or name == "oom-flags" or name == "path-count" or name == "route-count" or name == "update-timer" or name == "vrf-name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "active"):
                        self.active = value
                        self.active.value_namespace = name_space
                        self.active.value_namespace_prefix = name_space_prefix
                    if(value_path == "active-interface-count"):
                        self.active_interface_count = value
                        self.active_interface_count.value_namespace = name_space
                        self.active_interface_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "flush-timer"):
                        self.flush_timer = value
                        self.flush_timer.value_namespace = name_space
                        self.flush_timer.value_namespace_prefix = name_space_prefix
                    if(value_path == "hold-down-timer"):
                        self.hold_down_timer = value
                        self.hold_down_timer.value_namespace = name_space
                        self.hold_down_timer.value_namespace_prefix = name_space_prefix
                    if(value_path == "interface-configured-count"):
                        self.interface_configured_count = value
                        self.interface_configured_count.value_namespace = name_space
                        self.interface_configured_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "invalid-timer"):
                        self.invalid_timer = value
                        self.invalid_timer.value_namespace = name_space
                        self.invalid_timer.value_namespace_prefix = name_space_prefix
                    if(value_path == "next-update-time"):
                        self.next_update_time = value
                        self.next_update_time.value_namespace = name_space
                        self.next_update_time.value_namespace_prefix = name_space_prefix
                    if(value_path == "oom-flags"):
                        self.oom_flags = value
                        self.oom_flags.value_namespace = name_space
                        self.oom_flags.value_namespace_prefix = name_space_prefix
                    if(value_path == "path-count"):
                        self.path_count = value
                        self.path_count.value_namespace = name_space
                        self.path_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "route-count"):
                        self.route_count = value
                        self.route_count.value_namespace = name_space
                        self.route_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "update-timer"):
                        self.update_timer = value
                        self.update_timer.value_namespace = name_space
                        self.update_timer.value_namespace_prefix = name_space_prefix
                    if(value_path == "vrf-name"):
                        self.vrf_name = value
                        self.vrf_name.value_namespace = name_space
                        self.vrf_name.value_namespace_prefix = name_space_prefix


            class InterfaceSummary(Entity):
                """
                List of Interfaces configured
                
                .. attribute:: destination_address
                
                	IP address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: enabled
                
                	RIP enabled indicator
                	**type**\:  bool
                
                .. attribute:: interface_name
                
                	Interface name
                	**type**\:  str
                
                .. attribute:: neighbor_count
                
                	Number of neighbors seen
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: oom_flags
                
                	Current OOM flags
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: prefix_length
                
                	Prefix length of IP address
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: receive_version
                
                	RIP versions this interface will receive
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: send_version
                
                	RIP versions this interface sends out
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: state
                
                	Interface state
                	**type**\:   :py:class:`InterfaceState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.InterfaceState>`
                
                

                """

                _prefix = 'ip-rip-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rip.DefaultVrf.Global_.InterfaceSummary, self).__init__()

                    self.yang_name = "interface-summary"
                    self.yang_parent_name = "global"

                    self.destination_address = YLeaf(YType.str, "destination-address")

                    self.enabled = YLeaf(YType.boolean, "enabled")

                    self.interface_name = YLeaf(YType.str, "interface-name")

                    self.neighbor_count = YLeaf(YType.uint32, "neighbor-count")

                    self.oom_flags = YLeaf(YType.uint32, "oom-flags")

                    self.prefix_length = YLeaf(YType.uint32, "prefix-length")

                    self.receive_version = YLeaf(YType.uint32, "receive-version")

                    self.send_version = YLeaf(YType.uint32, "send-version")

                    self.state = YLeaf(YType.enumeration, "state")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("destination_address",
                                    "enabled",
                                    "interface_name",
                                    "neighbor_count",
                                    "oom_flags",
                                    "prefix_length",
                                    "receive_version",
                                    "send_version",
                                    "state") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Rip.DefaultVrf.Global_.InterfaceSummary, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Rip.DefaultVrf.Global_.InterfaceSummary, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.destination_address.is_set or
                        self.enabled.is_set or
                        self.interface_name.is_set or
                        self.neighbor_count.is_set or
                        self.oom_flags.is_set or
                        self.prefix_length.is_set or
                        self.receive_version.is_set or
                        self.send_version.is_set or
                        self.state.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.destination_address.yfilter != YFilter.not_set or
                        self.enabled.yfilter != YFilter.not_set or
                        self.interface_name.yfilter != YFilter.not_set or
                        self.neighbor_count.yfilter != YFilter.not_set or
                        self.oom_flags.yfilter != YFilter.not_set or
                        self.prefix_length.yfilter != YFilter.not_set or
                        self.receive_version.yfilter != YFilter.not_set or
                        self.send_version.yfilter != YFilter.not_set or
                        self.state.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "interface-summary" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ip-rip-oper:rip/default-vrf/global/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.destination_address.is_set or self.destination_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.destination_address.get_name_leafdata())
                    if (self.enabled.is_set or self.enabled.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.enabled.get_name_leafdata())
                    if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.interface_name.get_name_leafdata())
                    if (self.neighbor_count.is_set or self.neighbor_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.neighbor_count.get_name_leafdata())
                    if (self.oom_flags.is_set or self.oom_flags.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.oom_flags.get_name_leafdata())
                    if (self.prefix_length.is_set or self.prefix_length.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.prefix_length.get_name_leafdata())
                    if (self.receive_version.is_set or self.receive_version.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.receive_version.get_name_leafdata())
                    if (self.send_version.is_set or self.send_version.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.send_version.get_name_leafdata())
                    if (self.state.is_set or self.state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.state.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "destination-address" or name == "enabled" or name == "interface-name" or name == "neighbor-count" or name == "oom-flags" or name == "prefix-length" or name == "receive-version" or name == "send-version" or name == "state"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "destination-address"):
                        self.destination_address = value
                        self.destination_address.value_namespace = name_space
                        self.destination_address.value_namespace_prefix = name_space_prefix
                    if(value_path == "enabled"):
                        self.enabled = value
                        self.enabled.value_namespace = name_space
                        self.enabled.value_namespace_prefix = name_space_prefix
                    if(value_path == "interface-name"):
                        self.interface_name = value
                        self.interface_name.value_namespace = name_space
                        self.interface_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "neighbor-count"):
                        self.neighbor_count = value
                        self.neighbor_count.value_namespace = name_space
                        self.neighbor_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "oom-flags"):
                        self.oom_flags = value
                        self.oom_flags.value_namespace = name_space
                        self.oom_flags.value_namespace_prefix = name_space_prefix
                    if(value_path == "prefix-length"):
                        self.prefix_length = value
                        self.prefix_length.value_namespace = name_space
                        self.prefix_length.value_namespace_prefix = name_space_prefix
                    if(value_path == "receive-version"):
                        self.receive_version = value
                        self.receive_version.value_namespace = name_space
                        self.receive_version.value_namespace_prefix = name_space_prefix
                    if(value_path == "send-version"):
                        self.send_version = value
                        self.send_version.value_namespace = name_space
                        self.send_version.value_namespace_prefix = name_space_prefix
                    if(value_path == "state"):
                        self.state = value
                        self.state.value_namespace = name_space
                        self.state.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.interface_summary:
                    if (c.has_data()):
                        return True
                return (self.vrf_summary is not None and self.vrf_summary.has_data())

            def has_operation(self):
                for c in self.interface_summary:
                    if (c.has_operation()):
                        return True
                return (
                    self.yfilter != YFilter.not_set or
                    (self.vrf_summary is not None and self.vrf_summary.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "global" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ip-rip-oper:rip/default-vrf/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "interface-summary"):
                    for c in self.interface_summary:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Rip.DefaultVrf.Global_.InterfaceSummary()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.interface_summary.append(c)
                    return c

                if (child_yang_name == "vrf-summary"):
                    if (self.vrf_summary is None):
                        self.vrf_summary = Rip.DefaultVrf.Global_.VrfSummary()
                        self.vrf_summary.parent = self
                        self._children_name_map["vrf_summary"] = "vrf-summary"
                    return self.vrf_summary

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "interface-summary" or name == "vrf-summary"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (
                (self.configuration is not None and self.configuration.has_data()) or
                (self.global_ is not None and self.global_.has_data()) or
                (self.interfaces is not None and self.interfaces.has_data()) or
                (self.routes is not None and self.routes.has_data()) or
                (self.statistics is not None and self.statistics.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.configuration is not None and self.configuration.has_operation()) or
                (self.global_ is not None and self.global_.has_operation()) or
                (self.interfaces is not None and self.interfaces.has_operation()) or
                (self.routes is not None and self.routes.has_operation()) or
                (self.statistics is not None and self.statistics.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "default-vrf" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ip-rip-oper:rip/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "configuration"):
                if (self.configuration is None):
                    self.configuration = Rip.DefaultVrf.Configuration()
                    self.configuration.parent = self
                    self._children_name_map["configuration"] = "configuration"
                return self.configuration

            if (child_yang_name == "global"):
                if (self.global_ is None):
                    self.global_ = Rip.DefaultVrf.Global_()
                    self.global_.parent = self
                    self._children_name_map["global_"] = "global"
                return self.global_

            if (child_yang_name == "interfaces"):
                if (self.interfaces is None):
                    self.interfaces = Rip.DefaultVrf.Interfaces()
                    self.interfaces.parent = self
                    self._children_name_map["interfaces"] = "interfaces"
                return self.interfaces

            if (child_yang_name == "routes"):
                if (self.routes is None):
                    self.routes = Rip.DefaultVrf.Routes()
                    self.routes.parent = self
                    self._children_name_map["routes"] = "routes"
                return self.routes

            if (child_yang_name == "statistics"):
                if (self.statistics is None):
                    self.statistics = Rip.DefaultVrf.Statistics()
                    self.statistics.parent = self
                    self._children_name_map["statistics"] = "statistics"
                return self.statistics

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "configuration" or name == "global" or name == "interfaces" or name == "routes" or name == "statistics"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.default_vrf is not None and self.default_vrf.has_data()) or
            (self.protocol is not None and self.protocol.has_data()) or
            (self.vrfs is not None and self.vrfs.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.default_vrf is not None and self.default_vrf.has_operation()) or
            (self.protocol is not None and self.protocol.has_operation()) or
            (self.vrfs is not None and self.vrfs.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-ip-rip-oper:rip" + path_buffer

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

        if (child_yang_name == "default-vrf"):
            if (self.default_vrf is None):
                self.default_vrf = Rip.DefaultVrf()
                self.default_vrf.parent = self
                self._children_name_map["default_vrf"] = "default-vrf"
            return self.default_vrf

        if (child_yang_name == "protocol"):
            if (self.protocol is None):
                self.protocol = Rip.Protocol()
                self.protocol.parent = self
                self._children_name_map["protocol"] = "protocol"
            return self.protocol

        if (child_yang_name == "vrfs"):
            if (self.vrfs is None):
                self.vrfs = Rip.Vrfs()
                self.vrfs.parent = self
                self._children_name_map["vrfs"] = "vrfs"
            return self.vrfs

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "default-vrf" or name == "protocol" or name == "vrfs"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Rip()
        return self._top_entity

