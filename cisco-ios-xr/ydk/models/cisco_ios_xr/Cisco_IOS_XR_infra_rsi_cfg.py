""" Cisco_IOS_XR_infra_rsi_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-rsi package configuration.

This module contains definitions
for the following management objects\:
  vrfs\: VRF configuration
  global\-af\: global af
  srlg\: srlg
  vrf\-groups\: vrf groups
  selective\-vrf\-download\: selective vrf download

This YANG module augments the
  Cisco\-IOS\-XR\-ifmgr\-cfg,
  Cisco\-IOS\-XR\-snmp\-agent\-cfg
modules with configuration data.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class SrlgPriority(Enum):
    """
    SrlgPriority

    Srlg priority

    .. data:: critical = 0

    	Critical

    .. data:: high = 1

    	High

    .. data:: default = 2

    	Default

    .. data:: low = 3

    	Low

    .. data:: very_low = 4

    	Very low

    """

    critical = Enum.YLeaf(0, "critical")

    high = Enum.YLeaf(1, "high")

    default = Enum.YLeaf(2, "default")

    low = Enum.YLeaf(3, "low")

    very_low = Enum.YLeaf(4, "very-low")


class VrfAddressFamily(Enum):
    """
    VrfAddressFamily

    Vrf address family

    .. data:: ipv4 = 1

    	IPv4

    .. data:: ipv6 = 2

    	IPv6

    """

    ipv4 = Enum.YLeaf(1, "ipv4")

    ipv6 = Enum.YLeaf(2, "ipv6")


class VrfSubAddressFamily(Enum):
    """
    VrfSubAddressFamily

    Vrf sub address family

    .. data:: unicast = 1

    	Unicast

    .. data:: multicast = 2

    	Multicast

    .. data:: flow_spec = 133

    	Flow spec

    """

    unicast = Enum.YLeaf(1, "unicast")

    multicast = Enum.YLeaf(2, "multicast")

    flow_spec = Enum.YLeaf(133, "flow-spec")



class Vrfs(Entity):
    """
    VRF configuration
    
    .. attribute:: vrf
    
    	VRF configuration
    	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf>`
    
    

    """

    _prefix = 'infra-rsi-cfg'
    _revision = '2016-12-19'

    def __init__(self):
        super(Vrfs, self).__init__()
        self._top_entity = None

        self.yang_name = "vrfs"
        self.yang_parent_name = "Cisco-IOS-XR-infra-rsi-cfg"

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
                    super(Vrfs, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(Vrfs, self).__setattr__(name, value)


    class Vrf(Entity):
        """
        VRF configuration
        
        .. attribute:: vrf_name  <key>
        
        	VRF name
        	**type**\:  str
        
        	**length:** 1..32
        
        .. attribute:: afs
        
        	VRF address family configuration
        	**type**\:   :py:class:`Afs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.Afs>`
        
        .. attribute:: create
        
        	VRF global configuration
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: description
        
        	A textual description of the VRF
        	**type**\:  str
        
        	**length:** 1..244
        
        .. attribute:: fallback_vrf
        
        	Fallback VRF
        	**type**\:  str
        
        	**length:** 1..32
        
        .. attribute:: mode_big
        
        	Configuration enable of big VRF
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: multicast_host
        
        	Multicast host stack configuration
        	**type**\:   :py:class:`MulticastHost <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.MulticastHost>`
        
        .. attribute:: remote_route_filter_disable
        
        	For disabling remote route filtering for this VRF on core\-facing card
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: vpn_id
        
        	VPN\-ID for the VRF
        	**type**\:   :py:class:`VpnId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.VpnId>`
        
        	**presence node**\: True
        
        

        """

        _prefix = 'infra-rsi-cfg'
        _revision = '2016-12-19'

        def __init__(self):
            super(Vrfs.Vrf, self).__init__()

            self.yang_name = "vrf"
            self.yang_parent_name = "vrfs"

            self.vrf_name = YLeaf(YType.str, "vrf-name")

            self.create = YLeaf(YType.empty, "create")

            self.description = YLeaf(YType.str, "description")

            self.fallback_vrf = YLeaf(YType.str, "fallback-vrf")

            self.mode_big = YLeaf(YType.empty, "mode-big")

            self.remote_route_filter_disable = YLeaf(YType.empty, "remote-route-filter-disable")

            self.afs = Vrfs.Vrf.Afs()
            self.afs.parent = self
            self._children_name_map["afs"] = "afs"
            self._children_yang_names.add("afs")

            self.multicast_host = Vrfs.Vrf.MulticastHost()
            self.multicast_host.parent = self
            self._children_name_map["multicast_host"] = "multicast-host"
            self._children_yang_names.add("multicast-host")

            self.vpn_id = None
            self._children_name_map["vpn_id"] = "vpn-id"
            self._children_yang_names.add("vpn-id")

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
                            "create",
                            "description",
                            "fallback_vrf",
                            "mode_big",
                            "remote_route_filter_disable") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Vrfs.Vrf, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Vrfs.Vrf, self).__setattr__(name, value)


        class VpnId(Entity):
            """
            VPN\-ID for the VRF
            
            .. attribute:: vpn_index
            
            	Index of VPNID Index
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**mandatory**\: True
            
            .. attribute:: vpn_oui
            
            	OUI of VPNID OUI
            	**type**\:  int
            
            	**range:** 0..16777215
            
            	**mandatory**\: True
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'infra-rsi-cfg'
            _revision = '2016-12-19'

            def __init__(self):
                super(Vrfs.Vrf.VpnId, self).__init__()

                self.yang_name = "vpn-id"
                self.yang_parent_name = "vrf"
                self.is_presence_container = True

                self.vpn_index = YLeaf(YType.uint32, "vpn-index")

                self.vpn_oui = YLeaf(YType.uint32, "vpn-oui")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("vpn_index",
                                "vpn_oui") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Vrfs.Vrf.VpnId, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Vrfs.Vrf.VpnId, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.vpn_index.is_set or
                    self.vpn_oui.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.vpn_index.yfilter != YFilter.not_set or
                    self.vpn_oui.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "vpn-id" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.vpn_index.is_set or self.vpn_index.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vpn_index.get_name_leafdata())
                if (self.vpn_oui.is_set or self.vpn_oui.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vpn_oui.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "vpn-index" or name == "vpn-oui"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "vpn-index"):
                    self.vpn_index = value
                    self.vpn_index.value_namespace = name_space
                    self.vpn_index.value_namespace_prefix = name_space_prefix
                if(value_path == "vpn-oui"):
                    self.vpn_oui = value
                    self.vpn_oui.value_namespace = name_space
                    self.vpn_oui.value_namespace_prefix = name_space_prefix


        class Afs(Entity):
            """
            VRF address family configuration
            
            .. attribute:: af
            
            	VRF address family configuration
            	**type**\: list of    :py:class:`Af <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.Afs.Af>`
            
            

            """

            _prefix = 'infra-rsi-cfg'
            _revision = '2016-12-19'

            def __init__(self):
                super(Vrfs.Vrf.Afs, self).__init__()

                self.yang_name = "afs"
                self.yang_parent_name = "vrf"

                self.af = YList(self)

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
                            super(Vrfs.Vrf.Afs, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Vrfs.Vrf.Afs, self).__setattr__(name, value)


            class Af(Entity):
                """
                VRF address family configuration
                
                .. attribute:: af_name  <key>
                
                	Address family
                	**type**\:   :py:class:`VrfAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.VrfAddressFamily>`
                
                .. attribute:: saf_name  <key>
                
                	Sub\-Address family
                	**type**\:   :py:class:`VrfSubAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.VrfSubAddressFamily>`
                
                .. attribute:: topology_name  <key>
                
                	Topology name
                	**type**\:  str
                
                	**length:** 1..244
                
                .. attribute:: bgp
                
                	BGP AF VRF config
                	**type**\:   :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.Afs.Af.Bgp>`
                
                .. attribute:: create
                
                	VRF configuration for a particular address family
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: maximum_prefix
                
                	Set maximum prefix limits
                	**type**\:   :py:class:`MaximumPrefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.Afs.Af.MaximumPrefix>`
                
                	**presence node**\: True
                
                

                """

                _prefix = 'infra-rsi-cfg'
                _revision = '2016-12-19'

                def __init__(self):
                    super(Vrfs.Vrf.Afs.Af, self).__init__()

                    self.yang_name = "af"
                    self.yang_parent_name = "afs"

                    self.af_name = YLeaf(YType.enumeration, "af-name")

                    self.saf_name = YLeaf(YType.enumeration, "saf-name")

                    self.topology_name = YLeaf(YType.str, "topology-name")

                    self.create = YLeaf(YType.empty, "create")

                    self.bgp = Vrfs.Vrf.Afs.Af.Bgp()
                    self.bgp.parent = self
                    self._children_name_map["bgp"] = "bgp"
                    self._children_yang_names.add("bgp")

                    self.maximum_prefix = None
                    self._children_name_map["maximum_prefix"] = "maximum-prefix"
                    self._children_yang_names.add("maximum-prefix")

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
                                    "saf_name",
                                    "topology_name",
                                    "create") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Vrfs.Vrf.Afs.Af, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Vrfs.Vrf.Afs.Af, self).__setattr__(name, value)


                class MaximumPrefix(Entity):
                    """
                    Set maximum prefix limits
                    
                    .. attribute:: mid_threshold
                    
                    	Mid\-threshold (% of maximum)
                    	**type**\:  int
                    
                    	**range:** 1..100
                    
                    .. attribute:: prefix_limit
                    
                    	Set table's maximum prefix limit
                    	**type**\:  int
                    
                    	**range:** 32..5000000
                    
                    	**mandatory**\: True
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ip-rib-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Vrfs.Vrf.Afs.Af.MaximumPrefix, self).__init__()

                        self.yang_name = "maximum-prefix"
                        self.yang_parent_name = "af"
                        self.is_presence_container = True

                        self.mid_threshold = YLeaf(YType.uint32, "mid-threshold")

                        self.prefix_limit = YLeaf(YType.uint32, "prefix-limit")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("mid_threshold",
                                        "prefix_limit") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Vrfs.Vrf.Afs.Af.MaximumPrefix, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Vrfs.Vrf.Afs.Af.MaximumPrefix, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.mid_threshold.is_set or
                            self.prefix_limit.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.mid_threshold.yfilter != YFilter.not_set or
                            self.prefix_limit.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "Cisco-IOS-XR-ip-rib-cfg:maximum-prefix" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.mid_threshold.is_set or self.mid_threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mid_threshold.get_name_leafdata())
                        if (self.prefix_limit.is_set or self.prefix_limit.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.prefix_limit.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "mid-threshold" or name == "prefix-limit"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "mid-threshold"):
                            self.mid_threshold = value
                            self.mid_threshold.value_namespace = name_space
                            self.mid_threshold.value_namespace_prefix = name_space_prefix
                        if(value_path == "prefix-limit"):
                            self.prefix_limit = value
                            self.prefix_limit.value_namespace = name_space
                            self.prefix_limit.value_namespace_prefix = name_space_prefix


                class Bgp(Entity):
                    """
                    BGP AF VRF config
                    
                    .. attribute:: export_route_policy
                    
                    	Route policy for export filtering
                    	**type**\:  str
                    
                    .. attribute:: export_route_targets
                    
                    	Export Route targets
                    	**type**\:   :py:class:`ExportRouteTargets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets>`
                    
                    .. attribute:: export_vrf_options
                    
                    	Export VRF options
                    	**type**\:   :py:class:`ExportVrfOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.Afs.Af.Bgp.ExportVrfOptions>`
                    
                    .. attribute:: global_to_vrf_import_route_policy
                    
                    	Route policy for global to vrf import filtering
                    	**type**\:   :py:class:`GlobalToVrfImportRoutePolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.Afs.Af.Bgp.GlobalToVrfImportRoutePolicy>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: import_route_policy
                    
                    	Route policy for import filtering
                    	**type**\:  str
                    
                    .. attribute:: import_route_targets
                    
                    	Import Route targets
                    	**type**\:   :py:class:`ImportRouteTargets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets>`
                    
                    .. attribute:: import_vrf_options
                    
                    	TRUE Enable advertising imported paths to PEsFALSE Disable advertising imported paths to PEs
                    	**type**\:  bool
                    
                    .. attribute:: vrf_to_global_export_route_policy
                    
                    	Route policy for vrf to global export filtering
                    	**type**\:   :py:class:`VrfToGlobalExportRoutePolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.Afs.Af.Bgp.VrfToGlobalExportRoutePolicy>`
                    
                    	**presence node**\: True
                    
                    

                    """

                    _prefix = 'ipv4-bgp-cfg'
                    _revision = '2015-08-27'

                    def __init__(self):
                        super(Vrfs.Vrf.Afs.Af.Bgp, self).__init__()

                        self.yang_name = "bgp"
                        self.yang_parent_name = "af"

                        self.export_route_policy = YLeaf(YType.str, "export-route-policy")

                        self.import_route_policy = YLeaf(YType.str, "import-route-policy")

                        self.import_vrf_options = YLeaf(YType.boolean, "import-vrf-options")

                        self.export_route_targets = Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets()
                        self.export_route_targets.parent = self
                        self._children_name_map["export_route_targets"] = "export-route-targets"
                        self._children_yang_names.add("export-route-targets")

                        self.export_vrf_options = Vrfs.Vrf.Afs.Af.Bgp.ExportVrfOptions()
                        self.export_vrf_options.parent = self
                        self._children_name_map["export_vrf_options"] = "export-vrf-options"
                        self._children_yang_names.add("export-vrf-options")

                        self.global_to_vrf_import_route_policy = None
                        self._children_name_map["global_to_vrf_import_route_policy"] = "global-to-vrf-import-route-policy"
                        self._children_yang_names.add("global-to-vrf-import-route-policy")

                        self.import_route_targets = Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets()
                        self.import_route_targets.parent = self
                        self._children_name_map["import_route_targets"] = "import-route-targets"
                        self._children_yang_names.add("import-route-targets")

                        self.vrf_to_global_export_route_policy = None
                        self._children_name_map["vrf_to_global_export_route_policy"] = "vrf-to-global-export-route-policy"
                        self._children_yang_names.add("vrf-to-global-export-route-policy")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("export_route_policy",
                                        "import_route_policy",
                                        "import_vrf_options") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Vrfs.Vrf.Afs.Af.Bgp, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Vrfs.Vrf.Afs.Af.Bgp, self).__setattr__(name, value)


                    class ImportRouteTargets(Entity):
                        """
                        Import Route targets
                        
                        .. attribute:: route_targets
                        
                        	Route target table
                        	**type**\:   :py:class:`RouteTargets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets>`
                        
                        

                        """

                        _prefix = 'ipv4-bgp-cfg'
                        _revision = '2015-08-27'

                        def __init__(self):
                            super(Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets, self).__init__()

                            self.yang_name = "import-route-targets"
                            self.yang_parent_name = "bgp"

                            self.route_targets = Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets()
                            self.route_targets.parent = self
                            self._children_name_map["route_targets"] = "route-targets"
                            self._children_yang_names.add("route-targets")


                        class RouteTargets(Entity):
                            """
                            Route target table
                            
                            .. attribute:: route_target
                            
                            	Route target
                            	**type**\: list of    :py:class:`RouteTarget <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets.RouteTarget>`
                            
                            

                            """

                            _prefix = 'ipv4-bgp-cfg'
                            _revision = '2015-08-27'

                            def __init__(self):
                                super(Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets, self).__init__()

                                self.yang_name = "route-targets"
                                self.yang_parent_name = "import-route-targets"

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
                                    if name in () and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets, self).__setattr__(name, value)


                            class RouteTarget(Entity):
                                """
                                Route target
                                
                                .. attribute:: type  <key>
                                
                                	Type of RT
                                	**type**\:   :py:class:`BgpVrfRouteTarget <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg.BgpVrfRouteTarget>`
                                
                                .. attribute:: as_or_four_byte_as
                                
                                	as or four byte as
                                	**type**\: list of    :py:class:`AsOrFourByteAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets.RouteTarget.AsOrFourByteAs>`
                                
                                .. attribute:: ipv4_address
                                
                                	ipv4 address
                                	**type**\: list of    :py:class:`Ipv4Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets.RouteTarget.Ipv4Address>`
                                
                                

                                """

                                _prefix = 'ipv4-bgp-cfg'
                                _revision = '2015-08-27'

                                def __init__(self):
                                    super(Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets.RouteTarget, self).__init__()

                                    self.yang_name = "route-target"
                                    self.yang_parent_name = "route-targets"

                                    self.type = YLeaf(YType.enumeration, "type")

                                    self.as_or_four_byte_as = YList(self)
                                    self.ipv4_address = YList(self)

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("type") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets.RouteTarget, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets.RouteTarget, self).__setattr__(name, value)


                                class AsOrFourByteAs(Entity):
                                    """
                                    as or four byte as
                                    
                                    .. attribute:: as_xx  <key>
                                    
                                    	AS number
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: as_  <key>
                                    
                                    	AS number
                                    	**type**\:  int
                                    
                                    	**range:** 1..4294967295
                                    
                                    .. attribute:: as_index  <key>
                                    
                                    	AS number Index
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: stitching_rt  <key>
                                    
                                    	Stitching RT
                                    	**type**\:  int
                                    
                                    	**range:** 0..1
                                    
                                    

                                    """

                                    _prefix = 'ipv4-bgp-cfg'
                                    _revision = '2015-08-27'

                                    def __init__(self):
                                        super(Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets.RouteTarget.AsOrFourByteAs, self).__init__()

                                        self.yang_name = "as-or-four-byte-as"
                                        self.yang_parent_name = "route-target"

                                        self.as_xx = YLeaf(YType.uint32, "as-xx")

                                        self.as_ = YLeaf(YType.uint32, "as")

                                        self.as_index = YLeaf(YType.uint32, "as-index")

                                        self.stitching_rt = YLeaf(YType.uint32, "stitching-rt")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("as_xx",
                                                        "as_",
                                                        "as_index",
                                                        "stitching_rt") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets.RouteTarget.AsOrFourByteAs, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets.RouteTarget.AsOrFourByteAs, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.as_xx.is_set or
                                            self.as_.is_set or
                                            self.as_index.is_set or
                                            self.stitching_rt.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.as_xx.yfilter != YFilter.not_set or
                                            self.as_.yfilter != YFilter.not_set or
                                            self.as_index.yfilter != YFilter.not_set or
                                            self.stitching_rt.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "as-or-four-byte-as" + "[as-xx='" + self.as_xx.get() + "']" + "[as='" + self.as_.get() + "']" + "[as-index='" + self.as_index.get() + "']" + "[stitching-rt='" + self.stitching_rt.get() + "']" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.as_xx.is_set or self.as_xx.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.as_xx.get_name_leafdata())
                                        if (self.as_.is_set or self.as_.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.as_.get_name_leafdata())
                                        if (self.as_index.is_set or self.as_index.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.as_index.get_name_leafdata())
                                        if (self.stitching_rt.is_set or self.stitching_rt.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.stitching_rt.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "as-xx" or name == "as" or name == "as-index" or name == "stitching-rt"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "as-xx"):
                                            self.as_xx = value
                                            self.as_xx.value_namespace = name_space
                                            self.as_xx.value_namespace_prefix = name_space_prefix
                                        if(value_path == "as"):
                                            self.as_ = value
                                            self.as_.value_namespace = name_space
                                            self.as_.value_namespace_prefix = name_space_prefix
                                        if(value_path == "as-index"):
                                            self.as_index = value
                                            self.as_index.value_namespace = name_space
                                            self.as_index.value_namespace_prefix = name_space_prefix
                                        if(value_path == "stitching-rt"):
                                            self.stitching_rt = value
                                            self.stitching_rt.value_namespace = name_space
                                            self.stitching_rt.value_namespace_prefix = name_space_prefix


                                class Ipv4Address(Entity):
                                    """
                                    ipv4 address
                                    
                                    .. attribute:: address  <key>
                                    
                                    	IP address
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: address_index  <key>
                                    
                                    	IP address Index
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: stitching_rt  <key>
                                    
                                    	Stitching RT
                                    	**type**\:  int
                                    
                                    	**range:** 0..1
                                    
                                    

                                    """

                                    _prefix = 'ipv4-bgp-cfg'
                                    _revision = '2015-08-27'

                                    def __init__(self):
                                        super(Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets.RouteTarget.Ipv4Address, self).__init__()

                                        self.yang_name = "ipv4-address"
                                        self.yang_parent_name = "route-target"

                                        self.address = YLeaf(YType.str, "address")

                                        self.address_index = YLeaf(YType.uint32, "address-index")

                                        self.stitching_rt = YLeaf(YType.uint32, "stitching-rt")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("address",
                                                        "address_index",
                                                        "stitching_rt") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets.RouteTarget.Ipv4Address, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets.RouteTarget.Ipv4Address, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.address.is_set or
                                            self.address_index.is_set or
                                            self.stitching_rt.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.address.yfilter != YFilter.not_set or
                                            self.address_index.yfilter != YFilter.not_set or
                                            self.stitching_rt.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "ipv4-address" + "[address='" + self.address.get() + "']" + "[address-index='" + self.address_index.get() + "']" + "[stitching-rt='" + self.stitching_rt.get() + "']" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.address.get_name_leafdata())
                                        if (self.address_index.is_set or self.address_index.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.address_index.get_name_leafdata())
                                        if (self.stitching_rt.is_set or self.stitching_rt.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.stitching_rt.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "address" or name == "address-index" or name == "stitching-rt"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "address"):
                                            self.address = value
                                            self.address.value_namespace = name_space
                                            self.address.value_namespace_prefix = name_space_prefix
                                        if(value_path == "address-index"):
                                            self.address_index = value
                                            self.address_index.value_namespace = name_space
                                            self.address_index.value_namespace_prefix = name_space_prefix
                                        if(value_path == "stitching-rt"):
                                            self.stitching_rt = value
                                            self.stitching_rt.value_namespace = name_space
                                            self.stitching_rt.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    for c in self.as_or_four_byte_as:
                                        if (c.has_data()):
                                            return True
                                    for c in self.ipv4_address:
                                        if (c.has_data()):
                                            return True
                                    return self.type.is_set

                                def has_operation(self):
                                    for c in self.as_or_four_byte_as:
                                        if (c.has_operation()):
                                            return True
                                    for c in self.ipv4_address:
                                        if (c.has_operation()):
                                            return True
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.type.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "route-target" + "[type='" + self.type.get() + "']" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.type.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "as-or-four-byte-as"):
                                        for c in self.as_or_four_byte_as:
                                            segment = c.get_segment_path()
                                            if (segment_path == segment):
                                                return c
                                        c = Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets.RouteTarget.AsOrFourByteAs()
                                        c.parent = self
                                        local_reference_key = "ydk::seg::%s" % segment_path
                                        self._local_refs[local_reference_key] = c
                                        self.as_or_four_byte_as.append(c)
                                        return c

                                    if (child_yang_name == "ipv4-address"):
                                        for c in self.ipv4_address:
                                            segment = c.get_segment_path()
                                            if (segment_path == segment):
                                                return c
                                        c = Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets.RouteTarget.Ipv4Address()
                                        c.parent = self
                                        local_reference_key = "ydk::seg::%s" % segment_path
                                        self._local_refs[local_reference_key] = c
                                        self.ipv4_address.append(c)
                                        return c

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "as-or-four-byte-as" or name == "ipv4-address" or name == "type"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "type"):
                                        self.type = value
                                        self.type.value_namespace = name_space
                                        self.type.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                for c in self.route_target:
                                    if (c.has_data()):
                                        return True
                                return False

                            def has_operation(self):
                                for c in self.route_target:
                                    if (c.has_operation()):
                                        return True
                                return self.yfilter != YFilter.not_set

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "route-targets" + path_buffer

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

                                if (child_yang_name == "route-target"):
                                    for c in self.route_target:
                                        segment = c.get_segment_path()
                                        if (segment_path == segment):
                                            return c
                                    c = Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets.RouteTarget()
                                    c.parent = self
                                    local_reference_key = "ydk::seg::%s" % segment_path
                                    self._local_refs[local_reference_key] = c
                                    self.route_target.append(c)
                                    return c

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "route-target"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass

                        def has_data(self):
                            return (self.route_targets is not None and self.route_targets.has_data())

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                (self.route_targets is not None and self.route_targets.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "import-route-targets" + path_buffer

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

                            if (child_yang_name == "route-targets"):
                                if (self.route_targets is None):
                                    self.route_targets = Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets()
                                    self.route_targets.parent = self
                                    self._children_name_map["route_targets"] = "route-targets"
                                return self.route_targets

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "route-targets"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass


                    class ExportRouteTargets(Entity):
                        """
                        Export Route targets
                        
                        .. attribute:: route_targets
                        
                        	Route target table
                        	**type**\:   :py:class:`RouteTargets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets>`
                        
                        

                        """

                        _prefix = 'ipv4-bgp-cfg'
                        _revision = '2015-08-27'

                        def __init__(self):
                            super(Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets, self).__init__()

                            self.yang_name = "export-route-targets"
                            self.yang_parent_name = "bgp"

                            self.route_targets = Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets()
                            self.route_targets.parent = self
                            self._children_name_map["route_targets"] = "route-targets"
                            self._children_yang_names.add("route-targets")


                        class RouteTargets(Entity):
                            """
                            Route target table
                            
                            .. attribute:: route_target
                            
                            	Route target
                            	**type**\: list of    :py:class:`RouteTarget <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets.RouteTarget>`
                            
                            

                            """

                            _prefix = 'ipv4-bgp-cfg'
                            _revision = '2015-08-27'

                            def __init__(self):
                                super(Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets, self).__init__()

                                self.yang_name = "route-targets"
                                self.yang_parent_name = "export-route-targets"

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
                                    if name in () and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets, self).__setattr__(name, value)


                            class RouteTarget(Entity):
                                """
                                Route target
                                
                                .. attribute:: type  <key>
                                
                                	Type of RT
                                	**type**\:   :py:class:`BgpVrfRouteTarget <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg.BgpVrfRouteTarget>`
                                
                                .. attribute:: as_or_four_byte_as
                                
                                	as or four byte as
                                	**type**\: list of    :py:class:`AsOrFourByteAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets.RouteTarget.AsOrFourByteAs>`
                                
                                .. attribute:: ipv4_address
                                
                                	ipv4 address
                                	**type**\: list of    :py:class:`Ipv4Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets.RouteTarget.Ipv4Address>`
                                
                                

                                """

                                _prefix = 'ipv4-bgp-cfg'
                                _revision = '2015-08-27'

                                def __init__(self):
                                    super(Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets.RouteTarget, self).__init__()

                                    self.yang_name = "route-target"
                                    self.yang_parent_name = "route-targets"

                                    self.type = YLeaf(YType.enumeration, "type")

                                    self.as_or_four_byte_as = YList(self)
                                    self.ipv4_address = YList(self)

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("type") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets.RouteTarget, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets.RouteTarget, self).__setattr__(name, value)


                                class AsOrFourByteAs(Entity):
                                    """
                                    as or four byte as
                                    
                                    .. attribute:: as_xx  <key>
                                    
                                    	AS number
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: as_  <key>
                                    
                                    	AS number
                                    	**type**\:  int
                                    
                                    	**range:** 1..4294967295
                                    
                                    .. attribute:: as_index  <key>
                                    
                                    	AS number Index
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: stitching_rt  <key>
                                    
                                    	Stitching RT
                                    	**type**\:  int
                                    
                                    	**range:** 0..1
                                    
                                    

                                    """

                                    _prefix = 'ipv4-bgp-cfg'
                                    _revision = '2015-08-27'

                                    def __init__(self):
                                        super(Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets.RouteTarget.AsOrFourByteAs, self).__init__()

                                        self.yang_name = "as-or-four-byte-as"
                                        self.yang_parent_name = "route-target"

                                        self.as_xx = YLeaf(YType.uint32, "as-xx")

                                        self.as_ = YLeaf(YType.uint32, "as")

                                        self.as_index = YLeaf(YType.uint32, "as-index")

                                        self.stitching_rt = YLeaf(YType.uint32, "stitching-rt")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("as_xx",
                                                        "as_",
                                                        "as_index",
                                                        "stitching_rt") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets.RouteTarget.AsOrFourByteAs, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets.RouteTarget.AsOrFourByteAs, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.as_xx.is_set or
                                            self.as_.is_set or
                                            self.as_index.is_set or
                                            self.stitching_rt.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.as_xx.yfilter != YFilter.not_set or
                                            self.as_.yfilter != YFilter.not_set or
                                            self.as_index.yfilter != YFilter.not_set or
                                            self.stitching_rt.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "as-or-four-byte-as" + "[as-xx='" + self.as_xx.get() + "']" + "[as='" + self.as_.get() + "']" + "[as-index='" + self.as_index.get() + "']" + "[stitching-rt='" + self.stitching_rt.get() + "']" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.as_xx.is_set or self.as_xx.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.as_xx.get_name_leafdata())
                                        if (self.as_.is_set or self.as_.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.as_.get_name_leafdata())
                                        if (self.as_index.is_set or self.as_index.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.as_index.get_name_leafdata())
                                        if (self.stitching_rt.is_set or self.stitching_rt.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.stitching_rt.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "as-xx" or name == "as" or name == "as-index" or name == "stitching-rt"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "as-xx"):
                                            self.as_xx = value
                                            self.as_xx.value_namespace = name_space
                                            self.as_xx.value_namespace_prefix = name_space_prefix
                                        if(value_path == "as"):
                                            self.as_ = value
                                            self.as_.value_namespace = name_space
                                            self.as_.value_namespace_prefix = name_space_prefix
                                        if(value_path == "as-index"):
                                            self.as_index = value
                                            self.as_index.value_namespace = name_space
                                            self.as_index.value_namespace_prefix = name_space_prefix
                                        if(value_path == "stitching-rt"):
                                            self.stitching_rt = value
                                            self.stitching_rt.value_namespace = name_space
                                            self.stitching_rt.value_namespace_prefix = name_space_prefix


                                class Ipv4Address(Entity):
                                    """
                                    ipv4 address
                                    
                                    .. attribute:: address  <key>
                                    
                                    	IP address
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: address_index  <key>
                                    
                                    	IP address Index
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: stitching_rt  <key>
                                    
                                    	Stitching RT
                                    	**type**\:  int
                                    
                                    	**range:** 0..1
                                    
                                    

                                    """

                                    _prefix = 'ipv4-bgp-cfg'
                                    _revision = '2015-08-27'

                                    def __init__(self):
                                        super(Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets.RouteTarget.Ipv4Address, self).__init__()

                                        self.yang_name = "ipv4-address"
                                        self.yang_parent_name = "route-target"

                                        self.address = YLeaf(YType.str, "address")

                                        self.address_index = YLeaf(YType.uint32, "address-index")

                                        self.stitching_rt = YLeaf(YType.uint32, "stitching-rt")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("address",
                                                        "address_index",
                                                        "stitching_rt") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets.RouteTarget.Ipv4Address, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets.RouteTarget.Ipv4Address, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.address.is_set or
                                            self.address_index.is_set or
                                            self.stitching_rt.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.address.yfilter != YFilter.not_set or
                                            self.address_index.yfilter != YFilter.not_set or
                                            self.stitching_rt.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "ipv4-address" + "[address='" + self.address.get() + "']" + "[address-index='" + self.address_index.get() + "']" + "[stitching-rt='" + self.stitching_rt.get() + "']" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.address.get_name_leafdata())
                                        if (self.address_index.is_set or self.address_index.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.address_index.get_name_leafdata())
                                        if (self.stitching_rt.is_set or self.stitching_rt.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.stitching_rt.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "address" or name == "address-index" or name == "stitching-rt"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "address"):
                                            self.address = value
                                            self.address.value_namespace = name_space
                                            self.address.value_namespace_prefix = name_space_prefix
                                        if(value_path == "address-index"):
                                            self.address_index = value
                                            self.address_index.value_namespace = name_space
                                            self.address_index.value_namespace_prefix = name_space_prefix
                                        if(value_path == "stitching-rt"):
                                            self.stitching_rt = value
                                            self.stitching_rt.value_namespace = name_space
                                            self.stitching_rt.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    for c in self.as_or_four_byte_as:
                                        if (c.has_data()):
                                            return True
                                    for c in self.ipv4_address:
                                        if (c.has_data()):
                                            return True
                                    return self.type.is_set

                                def has_operation(self):
                                    for c in self.as_or_four_byte_as:
                                        if (c.has_operation()):
                                            return True
                                    for c in self.ipv4_address:
                                        if (c.has_operation()):
                                            return True
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.type.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "route-target" + "[type='" + self.type.get() + "']" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.type.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "as-or-four-byte-as"):
                                        for c in self.as_or_four_byte_as:
                                            segment = c.get_segment_path()
                                            if (segment_path == segment):
                                                return c
                                        c = Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets.RouteTarget.AsOrFourByteAs()
                                        c.parent = self
                                        local_reference_key = "ydk::seg::%s" % segment_path
                                        self._local_refs[local_reference_key] = c
                                        self.as_or_four_byte_as.append(c)
                                        return c

                                    if (child_yang_name == "ipv4-address"):
                                        for c in self.ipv4_address:
                                            segment = c.get_segment_path()
                                            if (segment_path == segment):
                                                return c
                                        c = Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets.RouteTarget.Ipv4Address()
                                        c.parent = self
                                        local_reference_key = "ydk::seg::%s" % segment_path
                                        self._local_refs[local_reference_key] = c
                                        self.ipv4_address.append(c)
                                        return c

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "as-or-four-byte-as" or name == "ipv4-address" or name == "type"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "type"):
                                        self.type = value
                                        self.type.value_namespace = name_space
                                        self.type.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                for c in self.route_target:
                                    if (c.has_data()):
                                        return True
                                return False

                            def has_operation(self):
                                for c in self.route_target:
                                    if (c.has_operation()):
                                        return True
                                return self.yfilter != YFilter.not_set

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "route-targets" + path_buffer

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

                                if (child_yang_name == "route-target"):
                                    for c in self.route_target:
                                        segment = c.get_segment_path()
                                        if (segment_path == segment):
                                            return c
                                    c = Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets.RouteTarget()
                                    c.parent = self
                                    local_reference_key = "ydk::seg::%s" % segment_path
                                    self._local_refs[local_reference_key] = c
                                    self.route_target.append(c)
                                    return c

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "route-target"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass

                        def has_data(self):
                            return (self.route_targets is not None and self.route_targets.has_data())

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                (self.route_targets is not None and self.route_targets.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "export-route-targets" + path_buffer

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

                            if (child_yang_name == "route-targets"):
                                if (self.route_targets is None):
                                    self.route_targets = Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets()
                                    self.route_targets.parent = self
                                    self._children_name_map["route_targets"] = "route-targets"
                                return self.route_targets

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "route-targets"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass


                    class VrfToGlobalExportRoutePolicy(Entity):
                        """
                        Route policy for vrf to global export filtering
                        
                        .. attribute:: allow_imported_vpn
                        
                        	TRUE Enable imported VPN paths to be exported to Default VRF.FALSE Disable imported VPN paths to be exported to Default VRF
                        	**type**\:  bool
                        
                        .. attribute:: route_policy_name
                        
                        	Vrf to global export route policy
                        	**type**\:  str
                        
                        	**mandatory**\: True
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ipv4-bgp-cfg'
                        _revision = '2015-08-27'

                        def __init__(self):
                            super(Vrfs.Vrf.Afs.Af.Bgp.VrfToGlobalExportRoutePolicy, self).__init__()

                            self.yang_name = "vrf-to-global-export-route-policy"
                            self.yang_parent_name = "bgp"
                            self.is_presence_container = True

                            self.allow_imported_vpn = YLeaf(YType.boolean, "allow-imported-vpn")

                            self.route_policy_name = YLeaf(YType.str, "route-policy-name")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("allow_imported_vpn",
                                            "route_policy_name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Vrfs.Vrf.Afs.Af.Bgp.VrfToGlobalExportRoutePolicy, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Vrfs.Vrf.Afs.Af.Bgp.VrfToGlobalExportRoutePolicy, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.allow_imported_vpn.is_set or
                                self.route_policy_name.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.allow_imported_vpn.yfilter != YFilter.not_set or
                                self.route_policy_name.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "vrf-to-global-export-route-policy" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.allow_imported_vpn.is_set or self.allow_imported_vpn.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.allow_imported_vpn.get_name_leafdata())
                            if (self.route_policy_name.is_set or self.route_policy_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.route_policy_name.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "allow-imported-vpn" or name == "route-policy-name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "allow-imported-vpn"):
                                self.allow_imported_vpn = value
                                self.allow_imported_vpn.value_namespace = name_space
                                self.allow_imported_vpn.value_namespace_prefix = name_space_prefix
                            if(value_path == "route-policy-name"):
                                self.route_policy_name = value
                                self.route_policy_name.value_namespace = name_space
                                self.route_policy_name.value_namespace_prefix = name_space_prefix


                    class ExportVrfOptions(Entity):
                        """
                        Export VRF options
                        
                        .. attribute:: allow_imported_vpn
                        
                        	TRUE Enable imported VPN paths to be exported to non\-default VRFFALSE Disable imported VPN paths to be exported to non\-default VRF
                        	**type**\:  bool
                        
                        .. attribute:: import_stitching_rt
                        
                        	TRUE Use stitchng RTs to import extranet pathsFALSE Use regular RTs to import extranet paths
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'ipv4-bgp-cfg'
                        _revision = '2015-08-27'

                        def __init__(self):
                            super(Vrfs.Vrf.Afs.Af.Bgp.ExportVrfOptions, self).__init__()

                            self.yang_name = "export-vrf-options"
                            self.yang_parent_name = "bgp"

                            self.allow_imported_vpn = YLeaf(YType.boolean, "allow-imported-vpn")

                            self.import_stitching_rt = YLeaf(YType.boolean, "import-stitching-rt")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("allow_imported_vpn",
                                            "import_stitching_rt") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Vrfs.Vrf.Afs.Af.Bgp.ExportVrfOptions, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Vrfs.Vrf.Afs.Af.Bgp.ExportVrfOptions, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.allow_imported_vpn.is_set or
                                self.import_stitching_rt.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.allow_imported_vpn.yfilter != YFilter.not_set or
                                self.import_stitching_rt.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "export-vrf-options" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.allow_imported_vpn.is_set or self.allow_imported_vpn.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.allow_imported_vpn.get_name_leafdata())
                            if (self.import_stitching_rt.is_set or self.import_stitching_rt.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.import_stitching_rt.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "allow-imported-vpn" or name == "import-stitching-rt"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "allow-imported-vpn"):
                                self.allow_imported_vpn = value
                                self.allow_imported_vpn.value_namespace = name_space
                                self.allow_imported_vpn.value_namespace_prefix = name_space_prefix
                            if(value_path == "import-stitching-rt"):
                                self.import_stitching_rt = value
                                self.import_stitching_rt.value_namespace = name_space
                                self.import_stitching_rt.value_namespace_prefix = name_space_prefix


                    class GlobalToVrfImportRoutePolicy(Entity):
                        """
                        Route policy for global to vrf import filtering
                        
                        .. attribute:: advertise_as_vpn
                        
                        	TRUE Enable advertising imported paths to PEsFALSE Disable advertising imported paths to PEs
                        	**type**\:  bool
                        
                        .. attribute:: route_policy_name
                        
                        	Global to vrf import route policy
                        	**type**\:  str
                        
                        	**mandatory**\: True
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ipv4-bgp-cfg'
                        _revision = '2015-08-27'

                        def __init__(self):
                            super(Vrfs.Vrf.Afs.Af.Bgp.GlobalToVrfImportRoutePolicy, self).__init__()

                            self.yang_name = "global-to-vrf-import-route-policy"
                            self.yang_parent_name = "bgp"
                            self.is_presence_container = True

                            self.advertise_as_vpn = YLeaf(YType.boolean, "advertise-as-vpn")

                            self.route_policy_name = YLeaf(YType.str, "route-policy-name")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("advertise_as_vpn",
                                            "route_policy_name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Vrfs.Vrf.Afs.Af.Bgp.GlobalToVrfImportRoutePolicy, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Vrfs.Vrf.Afs.Af.Bgp.GlobalToVrfImportRoutePolicy, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.advertise_as_vpn.is_set or
                                self.route_policy_name.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.advertise_as_vpn.yfilter != YFilter.not_set or
                                self.route_policy_name.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "global-to-vrf-import-route-policy" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.advertise_as_vpn.is_set or self.advertise_as_vpn.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.advertise_as_vpn.get_name_leafdata())
                            if (self.route_policy_name.is_set or self.route_policy_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.route_policy_name.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "advertise-as-vpn" or name == "route-policy-name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "advertise-as-vpn"):
                                self.advertise_as_vpn = value
                                self.advertise_as_vpn.value_namespace = name_space
                                self.advertise_as_vpn.value_namespace_prefix = name_space_prefix
                            if(value_path == "route-policy-name"):
                                self.route_policy_name = value
                                self.route_policy_name.value_namespace = name_space
                                self.route_policy_name.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.export_route_policy.is_set or
                            self.import_route_policy.is_set or
                            self.import_vrf_options.is_set or
                            (self.export_route_targets is not None and self.export_route_targets.has_data()) or
                            (self.export_vrf_options is not None and self.export_vrf_options.has_data()) or
                            (self.import_route_targets is not None and self.import_route_targets.has_data()) or
                            (self.global_to_vrf_import_route_policy is not None) or
                            (self.vrf_to_global_export_route_policy is not None))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.export_route_policy.yfilter != YFilter.not_set or
                            self.import_route_policy.yfilter != YFilter.not_set or
                            self.import_vrf_options.yfilter != YFilter.not_set or
                            (self.export_route_targets is not None and self.export_route_targets.has_operation()) or
                            (self.export_vrf_options is not None and self.export_vrf_options.has_operation()) or
                            (self.global_to_vrf_import_route_policy is not None and self.global_to_vrf_import_route_policy.has_operation()) or
                            (self.import_route_targets is not None and self.import_route_targets.has_operation()) or
                            (self.vrf_to_global_export_route_policy is not None and self.vrf_to_global_export_route_policy.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "Cisco-IOS-XR-ipv4-bgp-cfg:bgp" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.export_route_policy.is_set or self.export_route_policy.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.export_route_policy.get_name_leafdata())
                        if (self.import_route_policy.is_set or self.import_route_policy.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.import_route_policy.get_name_leafdata())
                        if (self.import_vrf_options.is_set or self.import_vrf_options.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.import_vrf_options.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "export-route-targets"):
                            if (self.export_route_targets is None):
                                self.export_route_targets = Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets()
                                self.export_route_targets.parent = self
                                self._children_name_map["export_route_targets"] = "export-route-targets"
                            return self.export_route_targets

                        if (child_yang_name == "export-vrf-options"):
                            if (self.export_vrf_options is None):
                                self.export_vrf_options = Vrfs.Vrf.Afs.Af.Bgp.ExportVrfOptions()
                                self.export_vrf_options.parent = self
                                self._children_name_map["export_vrf_options"] = "export-vrf-options"
                            return self.export_vrf_options

                        if (child_yang_name == "global-to-vrf-import-route-policy"):
                            if (self.global_to_vrf_import_route_policy is None):
                                self.global_to_vrf_import_route_policy = Vrfs.Vrf.Afs.Af.Bgp.GlobalToVrfImportRoutePolicy()
                                self.global_to_vrf_import_route_policy.parent = self
                                self._children_name_map["global_to_vrf_import_route_policy"] = "global-to-vrf-import-route-policy"
                            return self.global_to_vrf_import_route_policy

                        if (child_yang_name == "import-route-targets"):
                            if (self.import_route_targets is None):
                                self.import_route_targets = Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets()
                                self.import_route_targets.parent = self
                                self._children_name_map["import_route_targets"] = "import-route-targets"
                            return self.import_route_targets

                        if (child_yang_name == "vrf-to-global-export-route-policy"):
                            if (self.vrf_to_global_export_route_policy is None):
                                self.vrf_to_global_export_route_policy = Vrfs.Vrf.Afs.Af.Bgp.VrfToGlobalExportRoutePolicy()
                                self.vrf_to_global_export_route_policy.parent = self
                                self._children_name_map["vrf_to_global_export_route_policy"] = "vrf-to-global-export-route-policy"
                            return self.vrf_to_global_export_route_policy

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "export-route-targets" or name == "export-vrf-options" or name == "global-to-vrf-import-route-policy" or name == "import-route-targets" or name == "vrf-to-global-export-route-policy" or name == "export-route-policy" or name == "import-route-policy" or name == "import-vrf-options"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "export-route-policy"):
                            self.export_route_policy = value
                            self.export_route_policy.value_namespace = name_space
                            self.export_route_policy.value_namespace_prefix = name_space_prefix
                        if(value_path == "import-route-policy"):
                            self.import_route_policy = value
                            self.import_route_policy.value_namespace = name_space
                            self.import_route_policy.value_namespace_prefix = name_space_prefix
                        if(value_path == "import-vrf-options"):
                            self.import_vrf_options = value
                            self.import_vrf_options.value_namespace = name_space
                            self.import_vrf_options.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.af_name.is_set or
                        self.saf_name.is_set or
                        self.topology_name.is_set or
                        self.create.is_set or
                        (self.bgp is not None and self.bgp.has_data()) or
                        (self.maximum_prefix is not None))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.af_name.yfilter != YFilter.not_set or
                        self.saf_name.yfilter != YFilter.not_set or
                        self.topology_name.yfilter != YFilter.not_set or
                        self.create.yfilter != YFilter.not_set or
                        (self.bgp is not None and self.bgp.has_operation()) or
                        (self.maximum_prefix is not None and self.maximum_prefix.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "af" + "[af-name='" + self.af_name.get() + "']" + "[saf-name='" + self.saf_name.get() + "']" + "[topology-name='" + self.topology_name.get() + "']" + path_buffer

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
                    if (self.saf_name.is_set or self.saf_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.saf_name.get_name_leafdata())
                    if (self.topology_name.is_set or self.topology_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.topology_name.get_name_leafdata())
                    if (self.create.is_set or self.create.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.create.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "bgp"):
                        if (self.bgp is None):
                            self.bgp = Vrfs.Vrf.Afs.Af.Bgp()
                            self.bgp.parent = self
                            self._children_name_map["bgp"] = "bgp"
                        return self.bgp

                    if (child_yang_name == "maximum-prefix"):
                        if (self.maximum_prefix is None):
                            self.maximum_prefix = Vrfs.Vrf.Afs.Af.MaximumPrefix()
                            self.maximum_prefix.parent = self
                            self._children_name_map["maximum_prefix"] = "maximum-prefix"
                        return self.maximum_prefix

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "bgp" or name == "maximum-prefix" or name == "af-name" or name == "saf-name" or name == "topology-name" or name == "create"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "af-name"):
                        self.af_name = value
                        self.af_name.value_namespace = name_space
                        self.af_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "saf-name"):
                        self.saf_name = value
                        self.saf_name.value_namespace = name_space
                        self.saf_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "topology-name"):
                        self.topology_name = value
                        self.topology_name.value_namespace = name_space
                        self.topology_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "create"):
                        self.create = value
                        self.create.value_namespace = name_space
                        self.create.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.af:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.af:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "afs" + path_buffer

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

                if (child_yang_name == "af"):
                    for c in self.af:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Vrfs.Vrf.Afs.Af()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.af.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "af"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class MulticastHost(Entity):
            """
            Multicast host stack configuration
            
            .. attribute:: ipv4
            
            	IPv4 configuration
            	**type**\:   :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.MulticastHost.Ipv4>`
            
            .. attribute:: ipv6
            
            	IPv6 configuration
            	**type**\:   :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.MulticastHost.Ipv6>`
            
            

            """

            _prefix = 'ip-iarm-vrf-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Vrfs.Vrf.MulticastHost, self).__init__()

                self.yang_name = "multicast-host"
                self.yang_parent_name = "vrf"

                self.ipv4 = Vrfs.Vrf.MulticastHost.Ipv4()
                self.ipv4.parent = self
                self._children_name_map["ipv4"] = "ipv4"
                self._children_yang_names.add("ipv4")

                self.ipv6 = Vrfs.Vrf.MulticastHost.Ipv6()
                self.ipv6.parent = self
                self._children_name_map["ipv6"] = "ipv6"
                self._children_yang_names.add("ipv6")


            class Ipv4(Entity):
                """
                IPv4 configuration
                
                .. attribute:: interface
                
                	Default multicast host interface name
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                

                """

                _prefix = 'ip-iarm-vrf-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Vrfs.Vrf.MulticastHost.Ipv4, self).__init__()

                    self.yang_name = "ipv4"
                    self.yang_parent_name = "multicast-host"

                    self.interface = YLeaf(YType.str, "interface")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("interface") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Vrfs.Vrf.MulticastHost.Ipv4, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Vrfs.Vrf.MulticastHost.Ipv4, self).__setattr__(name, value)

                def has_data(self):
                    return self.interface.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.interface.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "ipv4" + path_buffer

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

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "interface"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "interface"):
                        self.interface = value
                        self.interface.value_namespace = name_space
                        self.interface.value_namespace_prefix = name_space_prefix


            class Ipv6(Entity):
                """
                IPv6 configuration
                
                .. attribute:: interface
                
                	Default multicast host interface name
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                

                """

                _prefix = 'ip-iarm-vrf-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Vrfs.Vrf.MulticastHost.Ipv6, self).__init__()

                    self.yang_name = "ipv6"
                    self.yang_parent_name = "multicast-host"

                    self.interface = YLeaf(YType.str, "interface")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("interface") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Vrfs.Vrf.MulticastHost.Ipv6, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Vrfs.Vrf.MulticastHost.Ipv6, self).__setattr__(name, value)

                def has_data(self):
                    return self.interface.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.interface.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "ipv6" + path_buffer

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

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "interface"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "interface"):
                        self.interface = value
                        self.interface.value_namespace = name_space
                        self.interface.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    (self.ipv4 is not None and self.ipv4.has_data()) or
                    (self.ipv6 is not None and self.ipv6.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.ipv4 is not None and self.ipv4.has_operation()) or
                    (self.ipv6 is not None and self.ipv6.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "Cisco-IOS-XR-ip-iarm-vrf-cfg:multicast-host" + path_buffer

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

                if (child_yang_name == "ipv4"):
                    if (self.ipv4 is None):
                        self.ipv4 = Vrfs.Vrf.MulticastHost.Ipv4()
                        self.ipv4.parent = self
                        self._children_name_map["ipv4"] = "ipv4"
                    return self.ipv4

                if (child_yang_name == "ipv6"):
                    if (self.ipv6 is None):
                        self.ipv6 = Vrfs.Vrf.MulticastHost.Ipv6()
                        self.ipv6.parent = self
                        self._children_name_map["ipv6"] = "ipv6"
                    return self.ipv6

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ipv4" or name == "ipv6"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (
                self.vrf_name.is_set or
                self.create.is_set or
                self.description.is_set or
                self.fallback_vrf.is_set or
                self.mode_big.is_set or
                self.remote_route_filter_disable.is_set or
                (self.afs is not None and self.afs.has_data()) or
                (self.multicast_host is not None and self.multicast_host.has_data()) or
                (self.vpn_id is not None))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.vrf_name.yfilter != YFilter.not_set or
                self.create.yfilter != YFilter.not_set or
                self.description.yfilter != YFilter.not_set or
                self.fallback_vrf.yfilter != YFilter.not_set or
                self.mode_big.yfilter != YFilter.not_set or
                self.remote_route_filter_disable.yfilter != YFilter.not_set or
                (self.afs is not None and self.afs.has_operation()) or
                (self.multicast_host is not None and self.multicast_host.has_operation()) or
                (self.vpn_id is not None and self.vpn_id.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "vrf" + "[vrf-name='" + self.vrf_name.get() + "']" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-infra-rsi-cfg:vrfs/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                leaf_name_data.append(self.vrf_name.get_name_leafdata())
            if (self.create.is_set or self.create.yfilter != YFilter.not_set):
                leaf_name_data.append(self.create.get_name_leafdata())
            if (self.description.is_set or self.description.yfilter != YFilter.not_set):
                leaf_name_data.append(self.description.get_name_leafdata())
            if (self.fallback_vrf.is_set or self.fallback_vrf.yfilter != YFilter.not_set):
                leaf_name_data.append(self.fallback_vrf.get_name_leafdata())
            if (self.mode_big.is_set or self.mode_big.yfilter != YFilter.not_set):
                leaf_name_data.append(self.mode_big.get_name_leafdata())
            if (self.remote_route_filter_disable.is_set or self.remote_route_filter_disable.yfilter != YFilter.not_set):
                leaf_name_data.append(self.remote_route_filter_disable.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "afs"):
                if (self.afs is None):
                    self.afs = Vrfs.Vrf.Afs()
                    self.afs.parent = self
                    self._children_name_map["afs"] = "afs"
                return self.afs

            if (child_yang_name == "multicast-host"):
                if (self.multicast_host is None):
                    self.multicast_host = Vrfs.Vrf.MulticastHost()
                    self.multicast_host.parent = self
                    self._children_name_map["multicast_host"] = "multicast-host"
                return self.multicast_host

            if (child_yang_name == "vpn-id"):
                if (self.vpn_id is None):
                    self.vpn_id = Vrfs.Vrf.VpnId()
                    self.vpn_id.parent = self
                    self._children_name_map["vpn_id"] = "vpn-id"
                return self.vpn_id

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "afs" or name == "multicast-host" or name == "vpn-id" or name == "vrf-name" or name == "create" or name == "description" or name == "fallback-vrf" or name == "mode-big" or name == "remote-route-filter-disable"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "vrf-name"):
                self.vrf_name = value
                self.vrf_name.value_namespace = name_space
                self.vrf_name.value_namespace_prefix = name_space_prefix
            if(value_path == "create"):
                self.create = value
                self.create.value_namespace = name_space
                self.create.value_namespace_prefix = name_space_prefix
            if(value_path == "description"):
                self.description = value
                self.description.value_namespace = name_space
                self.description.value_namespace_prefix = name_space_prefix
            if(value_path == "fallback-vrf"):
                self.fallback_vrf = value
                self.fallback_vrf.value_namespace = name_space
                self.fallback_vrf.value_namespace_prefix = name_space_prefix
            if(value_path == "mode-big"):
                self.mode_big = value
                self.mode_big.value_namespace = name_space
                self.mode_big.value_namespace_prefix = name_space_prefix
            if(value_path == "remote-route-filter-disable"):
                self.remote_route_filter_disable = value
                self.remote_route_filter_disable.value_namespace = name_space
                self.remote_route_filter_disable.value_namespace_prefix = name_space_prefix

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
        path_buffer = "Cisco-IOS-XR-infra-rsi-cfg:vrfs" + path_buffer

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

        if (child_yang_name == "vrf"):
            for c in self.vrf:
                segment = c.get_segment_path()
                if (segment_path == segment):
                    return c
            c = Vrfs.Vrf()
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

    def clone_ptr(self):
        self._top_entity = Vrfs()
        return self._top_entity

class GlobalAf(Entity):
    """
    global af
    
    .. attribute:: afs
    
    	VRF address family configuration
    	**type**\:   :py:class:`Afs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.GlobalAf.Afs>`
    
    

    """

    _prefix = 'infra-rsi-cfg'
    _revision = '2016-12-19'

    def __init__(self):
        super(GlobalAf, self).__init__()
        self._top_entity = None

        self.yang_name = "global-af"
        self.yang_parent_name = "Cisco-IOS-XR-infra-rsi-cfg"

        self.afs = GlobalAf.Afs()
        self.afs.parent = self
        self._children_name_map["afs"] = "afs"
        self._children_yang_names.add("afs")


    class Afs(Entity):
        """
        VRF address family configuration
        
        .. attribute:: af
        
        	VRF address family configuration
        	**type**\: list of    :py:class:`Af <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.GlobalAf.Afs.Af>`
        
        

        """

        _prefix = 'infra-rsi-cfg'
        _revision = '2016-12-19'

        def __init__(self):
            super(GlobalAf.Afs, self).__init__()

            self.yang_name = "afs"
            self.yang_parent_name = "global-af"

            self.af = YList(self)

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
                        super(GlobalAf.Afs, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(GlobalAf.Afs, self).__setattr__(name, value)


        class Af(Entity):
            """
            VRF address family configuration
            
            .. attribute:: af_name  <key>
            
            	Address family
            	**type**\:   :py:class:`VrfAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.VrfAddressFamily>`
            
            .. attribute:: saf_name  <key>
            
            	Sub\-Address family
            	**type**\:   :py:class:`VrfSubAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.VrfSubAddressFamily>`
            
            .. attribute:: topology_name  <key>
            
            	Topology name
            	**type**\:  str
            
            	**length:** 1..244
            
            .. attribute:: create
            
            	VRF configuration for a particular address family
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'infra-rsi-cfg'
            _revision = '2016-12-19'

            def __init__(self):
                super(GlobalAf.Afs.Af, self).__init__()

                self.yang_name = "af"
                self.yang_parent_name = "afs"

                self.af_name = YLeaf(YType.enumeration, "af-name")

                self.saf_name = YLeaf(YType.enumeration, "saf-name")

                self.topology_name = YLeaf(YType.str, "topology-name")

                self.create = YLeaf(YType.empty, "create")

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
                                "saf_name",
                                "topology_name",
                                "create") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(GlobalAf.Afs.Af, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(GlobalAf.Afs.Af, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.af_name.is_set or
                    self.saf_name.is_set or
                    self.topology_name.is_set or
                    self.create.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.af_name.yfilter != YFilter.not_set or
                    self.saf_name.yfilter != YFilter.not_set or
                    self.topology_name.yfilter != YFilter.not_set or
                    self.create.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "af" + "[af-name='" + self.af_name.get() + "']" + "[saf-name='" + self.saf_name.get() + "']" + "[topology-name='" + self.topology_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-infra-rsi-cfg:global-af/afs/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.af_name.is_set or self.af_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.af_name.get_name_leafdata())
                if (self.saf_name.is_set or self.saf_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.saf_name.get_name_leafdata())
                if (self.topology_name.is_set or self.topology_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.topology_name.get_name_leafdata())
                if (self.create.is_set or self.create.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.create.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "af-name" or name == "saf-name" or name == "topology-name" or name == "create"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "af-name"):
                    self.af_name = value
                    self.af_name.value_namespace = name_space
                    self.af_name.value_namespace_prefix = name_space_prefix
                if(value_path == "saf-name"):
                    self.saf_name = value
                    self.saf_name.value_namespace = name_space
                    self.saf_name.value_namespace_prefix = name_space_prefix
                if(value_path == "topology-name"):
                    self.topology_name = value
                    self.topology_name.value_namespace = name_space
                    self.topology_name.value_namespace_prefix = name_space_prefix
                if(value_path == "create"):
                    self.create = value
                    self.create.value_namespace = name_space
                    self.create.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.af:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.af:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "afs" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-infra-rsi-cfg:global-af/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

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
                c = GlobalAf.Afs.Af()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.af.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "af"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (self.afs is not None and self.afs.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.afs is not None and self.afs.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-infra-rsi-cfg:global-af" + path_buffer

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

        if (child_yang_name == "afs"):
            if (self.afs is None):
                self.afs = GlobalAf.Afs()
                self.afs.parent = self
                self._children_name_map["afs"] = "afs"
            return self.afs

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "afs"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = GlobalAf()
        return self._top_entity

class Srlg(Entity):
    """
    srlg
    
    .. attribute:: enable
    
    	Enable SRLG
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: groups
    
    	Set of groups configured with SRLG
    	**type**\:   :py:class:`Groups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.Groups>`
    
    .. attribute:: inherit_nodes
    
    	Set of inherit nodes configured with SRLG
    	**type**\:   :py:class:`InheritNodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.InheritNodes>`
    
    .. attribute:: interfaces
    
    	Set of interfaces configured with SRLG
    	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.Interfaces>`
    
    .. attribute:: srlg_names
    
    	Set of SRLG name configuration
    	**type**\:   :py:class:`SrlgNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.SrlgNames>`
    
    

    """

    _prefix = 'infra-rsi-cfg'
    _revision = '2016-12-19'

    def __init__(self):
        super(Srlg, self).__init__()
        self._top_entity = None

        self.yang_name = "srlg"
        self.yang_parent_name = "Cisco-IOS-XR-infra-rsi-cfg"

        self.enable = YLeaf(YType.empty, "enable")

        self.groups = Srlg.Groups()
        self.groups.parent = self
        self._children_name_map["groups"] = "groups"
        self._children_yang_names.add("groups")

        self.inherit_nodes = Srlg.InheritNodes()
        self.inherit_nodes.parent = self
        self._children_name_map["inherit_nodes"] = "inherit-nodes"
        self._children_yang_names.add("inherit-nodes")

        self.interfaces = Srlg.Interfaces()
        self.interfaces.parent = self
        self._children_name_map["interfaces"] = "interfaces"
        self._children_yang_names.add("interfaces")

        self.srlg_names = Srlg.SrlgNames()
        self.srlg_names.parent = self
        self._children_name_map["srlg_names"] = "srlg-names"
        self._children_yang_names.add("srlg-names")

    def __setattr__(self, name, value):
        self._check_monkey_patching_error(name, value)
        with _handle_type_error():
            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                    "Please use list append or extend method."
                                    .format(value))
            if isinstance(value, Enum.YLeaf):
                value = value.name
            if name in ("enable") and name in self.__dict__:
                if isinstance(value, YLeaf):
                    self.__dict__[name].set(value.get())
                elif isinstance(value, YLeafList):
                    super(Srlg, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(Srlg, self).__setattr__(name, value)


    class Interfaces(Entity):
        """
        Set of interfaces configured with SRLG
        
        .. attribute:: interface
        
        	Interface configurations
        	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.Interfaces.Interface>`
        
        

        """

        _prefix = 'infra-rsi-cfg'
        _revision = '2016-12-19'

        def __init__(self):
            super(Srlg.Interfaces, self).__init__()

            self.yang_name = "interfaces"
            self.yang_parent_name = "srlg"

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
                        super(Srlg.Interfaces, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Srlg.Interfaces, self).__setattr__(name, value)


        class Interface(Entity):
            """
            Interface configurations
            
            .. attribute:: interface_name  <key>
            
            	Interface name
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: enable
            
            	Enable SRLG interface
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: include_optical
            
            	Include optical configuration for an interface
            	**type**\:   :py:class:`IncludeOptical <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.Interfaces.Interface.IncludeOptical>`
            
            .. attribute:: interface_group
            
            	Group configuration for an interface
            	**type**\:   :py:class:`InterfaceGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.Interfaces.Interface.InterfaceGroup>`
            
            .. attribute:: interface_srlg_names
            
            	SRLG Name configuration for an interface
            	**type**\:   :py:class:`InterfaceSrlgNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.Interfaces.Interface.InterfaceSrlgNames>`
            
            .. attribute:: values
            
            	SRLG Value configuration for an interface
            	**type**\:   :py:class:`Values <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.Interfaces.Interface.Values>`
            
            

            """

            _prefix = 'infra-rsi-cfg'
            _revision = '2016-12-19'

            def __init__(self):
                super(Srlg.Interfaces.Interface, self).__init__()

                self.yang_name = "interface"
                self.yang_parent_name = "interfaces"

                self.interface_name = YLeaf(YType.str, "interface-name")

                self.enable = YLeaf(YType.empty, "enable")

                self.include_optical = Srlg.Interfaces.Interface.IncludeOptical()
                self.include_optical.parent = self
                self._children_name_map["include_optical"] = "include-optical"
                self._children_yang_names.add("include-optical")

                self.interface_group = Srlg.Interfaces.Interface.InterfaceGroup()
                self.interface_group.parent = self
                self._children_name_map["interface_group"] = "interface-group"
                self._children_yang_names.add("interface-group")

                self.interface_srlg_names = Srlg.Interfaces.Interface.InterfaceSrlgNames()
                self.interface_srlg_names.parent = self
                self._children_name_map["interface_srlg_names"] = "interface-srlg-names"
                self._children_yang_names.add("interface-srlg-names")

                self.values = Srlg.Interfaces.Interface.Values()
                self.values.parent = self
                self._children_name_map["values"] = "values"
                self._children_yang_names.add("values")

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
                                "enable") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Srlg.Interfaces.Interface, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Srlg.Interfaces.Interface, self).__setattr__(name, value)


            class IncludeOptical(Entity):
                """
                Include optical configuration for an interface
                
                .. attribute:: enable
                
                	Enable SRLG interface include optical
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: priority
                
                	Priority for optical domain values
                	**type**\:   :py:class:`SrlgPriority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.SrlgPriority>`
                
                	**default value**\: default
                
                

                """

                _prefix = 'infra-rsi-cfg'
                _revision = '2016-12-19'

                def __init__(self):
                    super(Srlg.Interfaces.Interface.IncludeOptical, self).__init__()

                    self.yang_name = "include-optical"
                    self.yang_parent_name = "interface"

                    self.enable = YLeaf(YType.empty, "enable")

                    self.priority = YLeaf(YType.enumeration, "priority")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("enable",
                                    "priority") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Srlg.Interfaces.Interface.IncludeOptical, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Srlg.Interfaces.Interface.IncludeOptical, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.enable.is_set or
                        self.priority.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.enable.yfilter != YFilter.not_set or
                        self.priority.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "include-optical" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.enable.get_name_leafdata())
                    if (self.priority.is_set or self.priority.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.priority.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "enable" or name == "priority"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "enable"):
                        self.enable = value
                        self.enable.value_namespace = name_space
                        self.enable.value_namespace_prefix = name_space_prefix
                    if(value_path == "priority"):
                        self.priority = value
                        self.priority.value_namespace = name_space
                        self.priority.value_namespace_prefix = name_space_prefix


            class InterfaceGroup(Entity):
                """
                Group configuration for an interface
                
                .. attribute:: enable
                
                	Enable SRLG interface group submode
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: group_names
                
                	Set of group name under an interface
                	**type**\:   :py:class:`GroupNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.Interfaces.Interface.InterfaceGroup.GroupNames>`
                
                

                """

                _prefix = 'infra-rsi-cfg'
                _revision = '2016-12-19'

                def __init__(self):
                    super(Srlg.Interfaces.Interface.InterfaceGroup, self).__init__()

                    self.yang_name = "interface-group"
                    self.yang_parent_name = "interface"

                    self.enable = YLeaf(YType.empty, "enable")

                    self.group_names = Srlg.Interfaces.Interface.InterfaceGroup.GroupNames()
                    self.group_names.parent = self
                    self._children_name_map["group_names"] = "group-names"
                    self._children_yang_names.add("group-names")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("enable") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Srlg.Interfaces.Interface.InterfaceGroup, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Srlg.Interfaces.Interface.InterfaceGroup, self).__setattr__(name, value)


                class GroupNames(Entity):
                    """
                    Set of group name under an interface
                    
                    .. attribute:: group_name
                    
                    	Group name included under interface
                    	**type**\: list of    :py:class:`GroupName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.Interfaces.Interface.InterfaceGroup.GroupNames.GroupName>`
                    
                    

                    """

                    _prefix = 'infra-rsi-cfg'
                    _revision = '2016-12-19'

                    def __init__(self):
                        super(Srlg.Interfaces.Interface.InterfaceGroup.GroupNames, self).__init__()

                        self.yang_name = "group-names"
                        self.yang_parent_name = "interface-group"

                        self.group_name = YList(self)

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
                                    super(Srlg.Interfaces.Interface.InterfaceGroup.GroupNames, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Srlg.Interfaces.Interface.InterfaceGroup.GroupNames, self).__setattr__(name, value)


                    class GroupName(Entity):
                        """
                        Group name included under interface
                        
                        .. attribute:: group_name_index  <key>
                        
                        	Group name index
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: group_name
                        
                        	Group name
                        	**type**\:  str
                        
                        	**mandatory**\: True
                        
                        .. attribute:: srlg_priority
                        
                        	SRLG priority
                        	**type**\:   :py:class:`SrlgPriority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.SrlgPriority>`
                        
                        	**default value**\: default
                        
                        

                        """

                        _prefix = 'infra-rsi-cfg'
                        _revision = '2016-12-19'

                        def __init__(self):
                            super(Srlg.Interfaces.Interface.InterfaceGroup.GroupNames.GroupName, self).__init__()

                            self.yang_name = "group-name"
                            self.yang_parent_name = "group-names"

                            self.group_name_index = YLeaf(YType.uint32, "group-name-index")

                            self.group_name = YLeaf(YType.str, "group-name")

                            self.srlg_priority = YLeaf(YType.enumeration, "srlg-priority")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("group_name_index",
                                            "group_name",
                                            "srlg_priority") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Srlg.Interfaces.Interface.InterfaceGroup.GroupNames.GroupName, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Srlg.Interfaces.Interface.InterfaceGroup.GroupNames.GroupName, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.group_name_index.is_set or
                                self.group_name.is_set or
                                self.srlg_priority.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.group_name_index.yfilter != YFilter.not_set or
                                self.group_name.yfilter != YFilter.not_set or
                                self.srlg_priority.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "group-name" + "[group-name-index='" + self.group_name_index.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.group_name_index.is_set or self.group_name_index.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.group_name_index.get_name_leafdata())
                            if (self.group_name.is_set or self.group_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.group_name.get_name_leafdata())
                            if (self.srlg_priority.is_set or self.srlg_priority.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.srlg_priority.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "group-name-index" or name == "group-name" or name == "srlg-priority"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "group-name-index"):
                                self.group_name_index = value
                                self.group_name_index.value_namespace = name_space
                                self.group_name_index.value_namespace_prefix = name_space_prefix
                            if(value_path == "group-name"):
                                self.group_name = value
                                self.group_name.value_namespace = name_space
                                self.group_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "srlg-priority"):
                                self.srlg_priority = value
                                self.srlg_priority.value_namespace = name_space
                                self.srlg_priority.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.group_name:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.group_name:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "group-names" + path_buffer

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

                        if (child_yang_name == "group-name"):
                            for c in self.group_name:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Srlg.Interfaces.Interface.InterfaceGroup.GroupNames.GroupName()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.group_name.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "group-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        self.enable.is_set or
                        (self.group_names is not None and self.group_names.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.enable.yfilter != YFilter.not_set or
                        (self.group_names is not None and self.group_names.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "interface-group" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.enable.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "group-names"):
                        if (self.group_names is None):
                            self.group_names = Srlg.Interfaces.Interface.InterfaceGroup.GroupNames()
                            self.group_names.parent = self
                            self._children_name_map["group_names"] = "group-names"
                        return self.group_names

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "group-names" or name == "enable"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "enable"):
                        self.enable = value
                        self.enable.value_namespace = name_space
                        self.enable.value_namespace_prefix = name_space_prefix


            class Values(Entity):
                """
                SRLG Value configuration for an interface
                
                .. attribute:: value
                
                	SRLG value data
                	**type**\: list of    :py:class:`Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.Interfaces.Interface.Values.Value>`
                
                

                """

                _prefix = 'infra-rsi-cfg'
                _revision = '2016-12-19'

                def __init__(self):
                    super(Srlg.Interfaces.Interface.Values, self).__init__()

                    self.yang_name = "values"
                    self.yang_parent_name = "interface"

                    self.value = YList(self)

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
                                super(Srlg.Interfaces.Interface.Values, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Srlg.Interfaces.Interface.Values, self).__setattr__(name, value)


                class Value(Entity):
                    """
                    SRLG value data
                    
                    .. attribute:: srlg_index  <key>
                    
                    	SRLG index
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    .. attribute:: srlg_priority
                    
                    	SRLG priority
                    	**type**\:   :py:class:`SrlgPriority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.SrlgPriority>`
                    
                    	**default value**\: default
                    
                    .. attribute:: srlg_value
                    
                    	SRLG value
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**mandatory**\: True
                    
                    

                    """

                    _prefix = 'infra-rsi-cfg'
                    _revision = '2016-12-19'

                    def __init__(self):
                        super(Srlg.Interfaces.Interface.Values.Value, self).__init__()

                        self.yang_name = "value"
                        self.yang_parent_name = "values"

                        self.srlg_index = YLeaf(YType.uint32, "srlg-index")

                        self.srlg_priority = YLeaf(YType.enumeration, "srlg-priority")

                        self.srlg_value = YLeaf(YType.uint32, "srlg-value")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("srlg_index",
                                        "srlg_priority",
                                        "srlg_value") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Srlg.Interfaces.Interface.Values.Value, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Srlg.Interfaces.Interface.Values.Value, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.srlg_index.is_set or
                            self.srlg_priority.is_set or
                            self.srlg_value.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.srlg_index.yfilter != YFilter.not_set or
                            self.srlg_priority.yfilter != YFilter.not_set or
                            self.srlg_value.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "value" + "[srlg-index='" + self.srlg_index.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.srlg_index.is_set or self.srlg_index.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.srlg_index.get_name_leafdata())
                        if (self.srlg_priority.is_set or self.srlg_priority.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.srlg_priority.get_name_leafdata())
                        if (self.srlg_value.is_set or self.srlg_value.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.srlg_value.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "srlg-index" or name == "srlg-priority" or name == "srlg-value"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "srlg-index"):
                            self.srlg_index = value
                            self.srlg_index.value_namespace = name_space
                            self.srlg_index.value_namespace_prefix = name_space_prefix
                        if(value_path == "srlg-priority"):
                            self.srlg_priority = value
                            self.srlg_priority.value_namespace = name_space
                            self.srlg_priority.value_namespace_prefix = name_space_prefix
                        if(value_path == "srlg-value"):
                            self.srlg_value = value
                            self.srlg_value.value_namespace = name_space
                            self.srlg_value.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.value:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.value:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "values" + path_buffer

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

                    if (child_yang_name == "value"):
                        for c in self.value:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Srlg.Interfaces.Interface.Values.Value()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.value.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "value"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class InterfaceSrlgNames(Entity):
                """
                SRLG Name configuration for an interface
                
                .. attribute:: interface_srlg_name
                
                	SRLG name data
                	**type**\: list of    :py:class:`InterfaceSrlgName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.Interfaces.Interface.InterfaceSrlgNames.InterfaceSrlgName>`
                
                

                """

                _prefix = 'infra-rsi-cfg'
                _revision = '2016-12-19'

                def __init__(self):
                    super(Srlg.Interfaces.Interface.InterfaceSrlgNames, self).__init__()

                    self.yang_name = "interface-srlg-names"
                    self.yang_parent_name = "interface"

                    self.interface_srlg_name = YList(self)

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
                                super(Srlg.Interfaces.Interface.InterfaceSrlgNames, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Srlg.Interfaces.Interface.InterfaceSrlgNames, self).__setattr__(name, value)


                class InterfaceSrlgName(Entity):
                    """
                    SRLG name data
                    
                    .. attribute:: srlg_name  <key>
                    
                    	SRLG name
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    

                    """

                    _prefix = 'infra-rsi-cfg'
                    _revision = '2016-12-19'

                    def __init__(self):
                        super(Srlg.Interfaces.Interface.InterfaceSrlgNames.InterfaceSrlgName, self).__init__()

                        self.yang_name = "interface-srlg-name"
                        self.yang_parent_name = "interface-srlg-names"

                        self.srlg_name = YLeaf(YType.str, "srlg-name")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("srlg_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Srlg.Interfaces.Interface.InterfaceSrlgNames.InterfaceSrlgName, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Srlg.Interfaces.Interface.InterfaceSrlgNames.InterfaceSrlgName, self).__setattr__(name, value)

                    def has_data(self):
                        return self.srlg_name.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.srlg_name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "interface-srlg-name" + "[srlg-name='" + self.srlg_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.srlg_name.is_set or self.srlg_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.srlg_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "srlg-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "srlg-name"):
                            self.srlg_name = value
                            self.srlg_name.value_namespace = name_space
                            self.srlg_name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.interface_srlg_name:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.interface_srlg_name:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "interface-srlg-names" + path_buffer

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

                    if (child_yang_name == "interface-srlg-name"):
                        for c in self.interface_srlg_name:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Srlg.Interfaces.Interface.InterfaceSrlgNames.InterfaceSrlgName()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.interface_srlg_name.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "interface-srlg-name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.interface_name.is_set or
                    self.enable.is_set or
                    (self.include_optical is not None and self.include_optical.has_data()) or
                    (self.interface_group is not None and self.interface_group.has_data()) or
                    (self.interface_srlg_names is not None and self.interface_srlg_names.has_data()) or
                    (self.values is not None and self.values.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.interface_name.yfilter != YFilter.not_set or
                    self.enable.yfilter != YFilter.not_set or
                    (self.include_optical is not None and self.include_optical.has_operation()) or
                    (self.interface_group is not None and self.interface_group.has_operation()) or
                    (self.interface_srlg_names is not None and self.interface_srlg_names.has_operation()) or
                    (self.values is not None and self.values.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "interface" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-infra-rsi-cfg:srlg/interfaces/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.interface_name.get_name_leafdata())
                if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.enable.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "include-optical"):
                    if (self.include_optical is None):
                        self.include_optical = Srlg.Interfaces.Interface.IncludeOptical()
                        self.include_optical.parent = self
                        self._children_name_map["include_optical"] = "include-optical"
                    return self.include_optical

                if (child_yang_name == "interface-group"):
                    if (self.interface_group is None):
                        self.interface_group = Srlg.Interfaces.Interface.InterfaceGroup()
                        self.interface_group.parent = self
                        self._children_name_map["interface_group"] = "interface-group"
                    return self.interface_group

                if (child_yang_name == "interface-srlg-names"):
                    if (self.interface_srlg_names is None):
                        self.interface_srlg_names = Srlg.Interfaces.Interface.InterfaceSrlgNames()
                        self.interface_srlg_names.parent = self
                        self._children_name_map["interface_srlg_names"] = "interface-srlg-names"
                    return self.interface_srlg_names

                if (child_yang_name == "values"):
                    if (self.values is None):
                        self.values = Srlg.Interfaces.Interface.Values()
                        self.values.parent = self
                        self._children_name_map["values"] = "values"
                    return self.values

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "include-optical" or name == "interface-group" or name == "interface-srlg-names" or name == "values" or name == "interface-name" or name == "enable"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "interface-name"):
                    self.interface_name = value
                    self.interface_name.value_namespace = name_space
                    self.interface_name.value_namespace_prefix = name_space_prefix
                if(value_path == "enable"):
                    self.enable = value
                    self.enable.value_namespace = name_space
                    self.enable.value_namespace_prefix = name_space_prefix

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
                path_buffer = "Cisco-IOS-XR-infra-rsi-cfg:srlg/%s" % self.get_segment_path()
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
                c = Srlg.Interfaces.Interface()
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


    class SrlgNames(Entity):
        """
        Set of SRLG name configuration
        
        .. attribute:: srlg_name
        
        	SRLG name configuration
        	**type**\: list of    :py:class:`SrlgName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.SrlgNames.SrlgName>`
        
        

        """

        _prefix = 'infra-rsi-cfg'
        _revision = '2016-12-19'

        def __init__(self):
            super(Srlg.SrlgNames, self).__init__()

            self.yang_name = "srlg-names"
            self.yang_parent_name = "srlg"

            self.srlg_name = YList(self)

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
                        super(Srlg.SrlgNames, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Srlg.SrlgNames, self).__setattr__(name, value)


        class SrlgName(Entity):
            """
            SRLG name configuration
            
            .. attribute:: srlg_name  <key>
            
            	SRLG name
            	**type**\:  str
            
            	**length:** 1..64
            
            .. attribute:: srlg_value
            
            	SRLG value
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**mandatory**\: True
            
            

            """

            _prefix = 'infra-rsi-cfg'
            _revision = '2016-12-19'

            def __init__(self):
                super(Srlg.SrlgNames.SrlgName, self).__init__()

                self.yang_name = "srlg-name"
                self.yang_parent_name = "srlg-names"

                self.srlg_name = YLeaf(YType.str, "srlg-name")

                self.srlg_value = YLeaf(YType.uint32, "srlg-value")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("srlg_name",
                                "srlg_value") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Srlg.SrlgNames.SrlgName, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Srlg.SrlgNames.SrlgName, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.srlg_name.is_set or
                    self.srlg_value.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.srlg_name.yfilter != YFilter.not_set or
                    self.srlg_value.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "srlg-name" + "[srlg-name='" + self.srlg_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-infra-rsi-cfg:srlg/srlg-names/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.srlg_name.is_set or self.srlg_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.srlg_name.get_name_leafdata())
                if (self.srlg_value.is_set or self.srlg_value.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.srlg_value.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "srlg-name" or name == "srlg-value"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "srlg-name"):
                    self.srlg_name = value
                    self.srlg_name.value_namespace = name_space
                    self.srlg_name.value_namespace_prefix = name_space_prefix
                if(value_path == "srlg-value"):
                    self.srlg_value = value
                    self.srlg_value.value_namespace = name_space
                    self.srlg_value.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.srlg_name:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.srlg_name:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "srlg-names" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-infra-rsi-cfg:srlg/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "srlg-name"):
                for c in self.srlg_name:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Srlg.SrlgNames.SrlgName()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.srlg_name.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "srlg-name"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Groups(Entity):
        """
        Set of groups configured with SRLG
        
        .. attribute:: group
        
        	Group configurations
        	**type**\: list of    :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.Groups.Group>`
        
        

        """

        _prefix = 'infra-rsi-cfg'
        _revision = '2016-12-19'

        def __init__(self):
            super(Srlg.Groups, self).__init__()

            self.yang_name = "groups"
            self.yang_parent_name = "srlg"

            self.group = YList(self)

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
                        super(Srlg.Groups, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Srlg.Groups, self).__setattr__(name, value)


        class Group(Entity):
            """
            Group configurations
            
            .. attribute:: group_name  <key>
            
            	Group name
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: enable
            
            	Enable SRLG group
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: group_values
            
            	Set of SRLG values configured under a group
            	**type**\:   :py:class:`GroupValues <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.Groups.Group.GroupValues>`
            
            

            """

            _prefix = 'infra-rsi-cfg'
            _revision = '2016-12-19'

            def __init__(self):
                super(Srlg.Groups.Group, self).__init__()

                self.yang_name = "group"
                self.yang_parent_name = "groups"

                self.group_name = YLeaf(YType.str, "group-name")

                self.enable = YLeaf(YType.empty, "enable")

                self.group_values = Srlg.Groups.Group.GroupValues()
                self.group_values.parent = self
                self._children_name_map["group_values"] = "group-values"
                self._children_yang_names.add("group-values")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("group_name",
                                "enable") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Srlg.Groups.Group, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Srlg.Groups.Group, self).__setattr__(name, value)


            class GroupValues(Entity):
                """
                Set of SRLG values configured under a group
                
                .. attribute:: group_value
                
                	Group SRLG values with attribute
                	**type**\: list of    :py:class:`GroupValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.Groups.Group.GroupValues.GroupValue>`
                
                

                """

                _prefix = 'infra-rsi-cfg'
                _revision = '2016-12-19'

                def __init__(self):
                    super(Srlg.Groups.Group.GroupValues, self).__init__()

                    self.yang_name = "group-values"
                    self.yang_parent_name = "group"

                    self.group_value = YList(self)

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
                                super(Srlg.Groups.Group.GroupValues, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Srlg.Groups.Group.GroupValues, self).__setattr__(name, value)


                class GroupValue(Entity):
                    """
                    Group SRLG values with attribute
                    
                    .. attribute:: srlg_index  <key>
                    
                    	SRLG index
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    .. attribute:: srlg_priority
                    
                    	SRLG priority
                    	**type**\:   :py:class:`SrlgPriority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.SrlgPriority>`
                    
                    	**default value**\: default
                    
                    .. attribute:: srlg_value
                    
                    	SRLG value
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**mandatory**\: True
                    
                    

                    """

                    _prefix = 'infra-rsi-cfg'
                    _revision = '2016-12-19'

                    def __init__(self):
                        super(Srlg.Groups.Group.GroupValues.GroupValue, self).__init__()

                        self.yang_name = "group-value"
                        self.yang_parent_name = "group-values"

                        self.srlg_index = YLeaf(YType.uint32, "srlg-index")

                        self.srlg_priority = YLeaf(YType.enumeration, "srlg-priority")

                        self.srlg_value = YLeaf(YType.uint32, "srlg-value")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("srlg_index",
                                        "srlg_priority",
                                        "srlg_value") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Srlg.Groups.Group.GroupValues.GroupValue, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Srlg.Groups.Group.GroupValues.GroupValue, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.srlg_index.is_set or
                            self.srlg_priority.is_set or
                            self.srlg_value.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.srlg_index.yfilter != YFilter.not_set or
                            self.srlg_priority.yfilter != YFilter.not_set or
                            self.srlg_value.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "group-value" + "[srlg-index='" + self.srlg_index.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.srlg_index.is_set or self.srlg_index.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.srlg_index.get_name_leafdata())
                        if (self.srlg_priority.is_set or self.srlg_priority.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.srlg_priority.get_name_leafdata())
                        if (self.srlg_value.is_set or self.srlg_value.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.srlg_value.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "srlg-index" or name == "srlg-priority" or name == "srlg-value"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "srlg-index"):
                            self.srlg_index = value
                            self.srlg_index.value_namespace = name_space
                            self.srlg_index.value_namespace_prefix = name_space_prefix
                        if(value_path == "srlg-priority"):
                            self.srlg_priority = value
                            self.srlg_priority.value_namespace = name_space
                            self.srlg_priority.value_namespace_prefix = name_space_prefix
                        if(value_path == "srlg-value"):
                            self.srlg_value = value
                            self.srlg_value.value_namespace = name_space
                            self.srlg_value.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.group_value:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.group_value:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "group-values" + path_buffer

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

                    if (child_yang_name == "group-value"):
                        for c in self.group_value:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Srlg.Groups.Group.GroupValues.GroupValue()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.group_value.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "group-value"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.group_name.is_set or
                    self.enable.is_set or
                    (self.group_values is not None and self.group_values.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.group_name.yfilter != YFilter.not_set or
                    self.enable.yfilter != YFilter.not_set or
                    (self.group_values is not None and self.group_values.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "group" + "[group-name='" + self.group_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-infra-rsi-cfg:srlg/groups/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.group_name.is_set or self.group_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.group_name.get_name_leafdata())
                if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.enable.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "group-values"):
                    if (self.group_values is None):
                        self.group_values = Srlg.Groups.Group.GroupValues()
                        self.group_values.parent = self
                        self._children_name_map["group_values"] = "group-values"
                    return self.group_values

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "group-values" or name == "group-name" or name == "enable"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "group-name"):
                    self.group_name = value
                    self.group_name.value_namespace = name_space
                    self.group_name.value_namespace_prefix = name_space_prefix
                if(value_path == "enable"):
                    self.enable = value
                    self.enable.value_namespace = name_space
                    self.enable.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.group:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.group:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "groups" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-infra-rsi-cfg:srlg/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "group"):
                for c in self.group:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Srlg.Groups.Group()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.group.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "group"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class InheritNodes(Entity):
        """
        Set of inherit nodes configured with SRLG
        
        .. attribute:: inherit_node
        
        	Inherit node configurations
        	**type**\: list of    :py:class:`InheritNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.InheritNodes.InheritNode>`
        
        

        """

        _prefix = 'infra-rsi-cfg'
        _revision = '2016-12-19'

        def __init__(self):
            super(Srlg.InheritNodes, self).__init__()

            self.yang_name = "inherit-nodes"
            self.yang_parent_name = "srlg"

            self.inherit_node = YList(self)

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
                        super(Srlg.InheritNodes, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Srlg.InheritNodes, self).__setattr__(name, value)


        class InheritNode(Entity):
            """
            Inherit node configurations
            
            .. attribute:: inherit_node_name  <key>
            
            	The inherit node name
            	**type**\:  str
            
            	**pattern:** ((([a\-zA\-Z0\-9\_]\*\\d+)\|(\\\*))/){2}(([a\-zA\-Z0\-9\_]\*\\d+)\|(\\\*))
            
            .. attribute:: enable
            
            	Enable SRLG inherit node
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: inherit_node_values
            
            	Set of SRLG values configured under an inherit node
            	**type**\:   :py:class:`InheritNodeValues <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.InheritNodes.InheritNode.InheritNodeValues>`
            
            

            """

            _prefix = 'infra-rsi-cfg'
            _revision = '2016-12-19'

            def __init__(self):
                super(Srlg.InheritNodes.InheritNode, self).__init__()

                self.yang_name = "inherit-node"
                self.yang_parent_name = "inherit-nodes"

                self.inherit_node_name = YLeaf(YType.str, "inherit-node-name")

                self.enable = YLeaf(YType.empty, "enable")

                self.inherit_node_values = Srlg.InheritNodes.InheritNode.InheritNodeValues()
                self.inherit_node_values.parent = self
                self._children_name_map["inherit_node_values"] = "inherit-node-values"
                self._children_yang_names.add("inherit-node-values")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("inherit_node_name",
                                "enable") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Srlg.InheritNodes.InheritNode, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Srlg.InheritNodes.InheritNode, self).__setattr__(name, value)


            class InheritNodeValues(Entity):
                """
                Set of SRLG values configured under an inherit
                node
                
                .. attribute:: inherit_node_value
                
                	Inherit node SRLG value with attributes
                	**type**\: list of    :py:class:`InheritNodeValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.InheritNodes.InheritNode.InheritNodeValues.InheritNodeValue>`
                
                

                """

                _prefix = 'infra-rsi-cfg'
                _revision = '2016-12-19'

                def __init__(self):
                    super(Srlg.InheritNodes.InheritNode.InheritNodeValues, self).__init__()

                    self.yang_name = "inherit-node-values"
                    self.yang_parent_name = "inherit-node"

                    self.inherit_node_value = YList(self)

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
                                super(Srlg.InheritNodes.InheritNode.InheritNodeValues, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Srlg.InheritNodes.InheritNode.InheritNodeValues, self).__setattr__(name, value)


                class InheritNodeValue(Entity):
                    """
                    Inherit node SRLG value with attributes
                    
                    .. attribute:: srlg_index  <key>
                    
                    	SRLG index
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    .. attribute:: srlg_priority
                    
                    	SRLG priority
                    	**type**\:   :py:class:`SrlgPriority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.SrlgPriority>`
                    
                    	**default value**\: default
                    
                    .. attribute:: srlg_value
                    
                    	SRLG value
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**mandatory**\: True
                    
                    

                    """

                    _prefix = 'infra-rsi-cfg'
                    _revision = '2016-12-19'

                    def __init__(self):
                        super(Srlg.InheritNodes.InheritNode.InheritNodeValues.InheritNodeValue, self).__init__()

                        self.yang_name = "inherit-node-value"
                        self.yang_parent_name = "inherit-node-values"

                        self.srlg_index = YLeaf(YType.uint32, "srlg-index")

                        self.srlg_priority = YLeaf(YType.enumeration, "srlg-priority")

                        self.srlg_value = YLeaf(YType.uint32, "srlg-value")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("srlg_index",
                                        "srlg_priority",
                                        "srlg_value") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Srlg.InheritNodes.InheritNode.InheritNodeValues.InheritNodeValue, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Srlg.InheritNodes.InheritNode.InheritNodeValues.InheritNodeValue, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.srlg_index.is_set or
                            self.srlg_priority.is_set or
                            self.srlg_value.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.srlg_index.yfilter != YFilter.not_set or
                            self.srlg_priority.yfilter != YFilter.not_set or
                            self.srlg_value.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "inherit-node-value" + "[srlg-index='" + self.srlg_index.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.srlg_index.is_set or self.srlg_index.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.srlg_index.get_name_leafdata())
                        if (self.srlg_priority.is_set or self.srlg_priority.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.srlg_priority.get_name_leafdata())
                        if (self.srlg_value.is_set or self.srlg_value.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.srlg_value.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "srlg-index" or name == "srlg-priority" or name == "srlg-value"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "srlg-index"):
                            self.srlg_index = value
                            self.srlg_index.value_namespace = name_space
                            self.srlg_index.value_namespace_prefix = name_space_prefix
                        if(value_path == "srlg-priority"):
                            self.srlg_priority = value
                            self.srlg_priority.value_namespace = name_space
                            self.srlg_priority.value_namespace_prefix = name_space_prefix
                        if(value_path == "srlg-value"):
                            self.srlg_value = value
                            self.srlg_value.value_namespace = name_space
                            self.srlg_value.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.inherit_node_value:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.inherit_node_value:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "inherit-node-values" + path_buffer

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

                    if (child_yang_name == "inherit-node-value"):
                        for c in self.inherit_node_value:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Srlg.InheritNodes.InheritNode.InheritNodeValues.InheritNodeValue()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.inherit_node_value.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "inherit-node-value"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.inherit_node_name.is_set or
                    self.enable.is_set or
                    (self.inherit_node_values is not None and self.inherit_node_values.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.inherit_node_name.yfilter != YFilter.not_set or
                    self.enable.yfilter != YFilter.not_set or
                    (self.inherit_node_values is not None and self.inherit_node_values.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "inherit-node" + "[inherit-node-name='" + self.inherit_node_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-infra-rsi-cfg:srlg/inherit-nodes/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.inherit_node_name.is_set or self.inherit_node_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.inherit_node_name.get_name_leafdata())
                if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.enable.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "inherit-node-values"):
                    if (self.inherit_node_values is None):
                        self.inherit_node_values = Srlg.InheritNodes.InheritNode.InheritNodeValues()
                        self.inherit_node_values.parent = self
                        self._children_name_map["inherit_node_values"] = "inherit-node-values"
                    return self.inherit_node_values

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "inherit-node-values" or name == "inherit-node-name" or name == "enable"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "inherit-node-name"):
                    self.inherit_node_name = value
                    self.inherit_node_name.value_namespace = name_space
                    self.inherit_node_name.value_namespace_prefix = name_space_prefix
                if(value_path == "enable"):
                    self.enable = value
                    self.enable.value_namespace = name_space
                    self.enable.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.inherit_node:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.inherit_node:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "inherit-nodes" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-infra-rsi-cfg:srlg/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "inherit-node"):
                for c in self.inherit_node:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Srlg.InheritNodes.InheritNode()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.inherit_node.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "inherit-node"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            self.enable.is_set or
            (self.groups is not None and self.groups.has_data()) or
            (self.inherit_nodes is not None and self.inherit_nodes.has_data()) or
            (self.interfaces is not None and self.interfaces.has_data()) or
            (self.srlg_names is not None and self.srlg_names.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            self.enable.yfilter != YFilter.not_set or
            (self.groups is not None and self.groups.has_operation()) or
            (self.inherit_nodes is not None and self.inherit_nodes.has_operation()) or
            (self.interfaces is not None and self.interfaces.has_operation()) or
            (self.srlg_names is not None and self.srlg_names.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-infra-rsi-cfg:srlg" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()
        if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
            leaf_name_data.append(self.enable.get_name_leafdata())

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "groups"):
            if (self.groups is None):
                self.groups = Srlg.Groups()
                self.groups.parent = self
                self._children_name_map["groups"] = "groups"
            return self.groups

        if (child_yang_name == "inherit-nodes"):
            if (self.inherit_nodes is None):
                self.inherit_nodes = Srlg.InheritNodes()
                self.inherit_nodes.parent = self
                self._children_name_map["inherit_nodes"] = "inherit-nodes"
            return self.inherit_nodes

        if (child_yang_name == "interfaces"):
            if (self.interfaces is None):
                self.interfaces = Srlg.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"
            return self.interfaces

        if (child_yang_name == "srlg-names"):
            if (self.srlg_names is None):
                self.srlg_names = Srlg.SrlgNames()
                self.srlg_names.parent = self
                self._children_name_map["srlg_names"] = "srlg-names"
            return self.srlg_names

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "groups" or name == "inherit-nodes" or name == "interfaces" or name == "srlg-names" or name == "enable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        if(value_path == "enable"):
            self.enable = value
            self.enable.value_namespace = name_space
            self.enable.value_namespace_prefix = name_space_prefix

    def clone_ptr(self):
        self._top_entity = Srlg()
        return self._top_entity

class VrfGroups(Entity):
    """
    vrf groups
    
    .. attribute:: vrf_group
    
    	VRF group configuration
    	**type**\: list of    :py:class:`VrfGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.VrfGroups.VrfGroup>`
    
    

    """

    _prefix = 'infra-rsi-cfg'
    _revision = '2016-12-19'

    def __init__(self):
        super(VrfGroups, self).__init__()
        self._top_entity = None

        self.yang_name = "vrf-groups"
        self.yang_parent_name = "Cisco-IOS-XR-infra-rsi-cfg"

        self.vrf_group = YList(self)

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
                    super(VrfGroups, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(VrfGroups, self).__setattr__(name, value)


    class VrfGroup(Entity):
        """
        VRF group configuration
        
        .. attribute:: vrf_group_name  <key>
        
        	VRF group name
        	**type**\:  str
        
        	**length:** 1..32
        
        .. attribute:: enable
        
        	Enable VRF group
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: vrfs
        
        	Set of VRFs configured under a VRF group
        	**type**\:   :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.VrfGroups.VrfGroup.Vrfs>`
        
        

        """

        _prefix = 'infra-rsi-cfg'
        _revision = '2016-12-19'

        def __init__(self):
            super(VrfGroups.VrfGroup, self).__init__()

            self.yang_name = "vrf-group"
            self.yang_parent_name = "vrf-groups"

            self.vrf_group_name = YLeaf(YType.str, "vrf-group-name")

            self.enable = YLeaf(YType.empty, "enable")

            self.vrfs = VrfGroups.VrfGroup.Vrfs()
            self.vrfs.parent = self
            self._children_name_map["vrfs"] = "vrfs"
            self._children_yang_names.add("vrfs")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("vrf_group_name",
                            "enable") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(VrfGroups.VrfGroup, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(VrfGroups.VrfGroup, self).__setattr__(name, value)


        class Vrfs(Entity):
            """
            Set of VRFs configured under a VRF group
            
            .. attribute:: vrf
            
            	VRF configuration
            	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.VrfGroups.VrfGroup.Vrfs.Vrf>`
            
            

            """

            _prefix = 'infra-rsi-cfg'
            _revision = '2016-12-19'

            def __init__(self):
                super(VrfGroups.VrfGroup.Vrfs, self).__init__()

                self.yang_name = "vrfs"
                self.yang_parent_name = "vrf-group"

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
                            super(VrfGroups.VrfGroup.Vrfs, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(VrfGroups.VrfGroup.Vrfs, self).__setattr__(name, value)


            class Vrf(Entity):
                """
                VRF configuration
                
                .. attribute:: vrf_name  <key>
                
                	VRF name
                	**type**\:  str
                
                	**length:** 1..32
                
                

                """

                _prefix = 'infra-rsi-cfg'
                _revision = '2016-12-19'

                def __init__(self):
                    super(VrfGroups.VrfGroup.Vrfs.Vrf, self).__init__()

                    self.yang_name = "vrf"
                    self.yang_parent_name = "vrfs"

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
                        if name in ("vrf_name") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(VrfGroups.VrfGroup.Vrfs.Vrf, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(VrfGroups.VrfGroup.Vrfs.Vrf, self).__setattr__(name, value)

                def has_data(self):
                    return self.vrf_name.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.vrf_name.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "vrf" + "[vrf-name='" + self.vrf_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
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

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "vrf-name"):
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

                if (child_yang_name == "vrf"):
                    for c in self.vrf:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = VrfGroups.VrfGroup.Vrfs.Vrf()
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
                self.vrf_group_name.is_set or
                self.enable.is_set or
                (self.vrfs is not None and self.vrfs.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.vrf_group_name.yfilter != YFilter.not_set or
                self.enable.yfilter != YFilter.not_set or
                (self.vrfs is not None and self.vrfs.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "vrf-group" + "[vrf-group-name='" + self.vrf_group_name.get() + "']" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-infra-rsi-cfg:vrf-groups/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.vrf_group_name.is_set or self.vrf_group_name.yfilter != YFilter.not_set):
                leaf_name_data.append(self.vrf_group_name.get_name_leafdata())
            if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                leaf_name_data.append(self.enable.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "vrfs"):
                if (self.vrfs is None):
                    self.vrfs = VrfGroups.VrfGroup.Vrfs()
                    self.vrfs.parent = self
                    self._children_name_map["vrfs"] = "vrfs"
                return self.vrfs

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "vrfs" or name == "vrf-group-name" or name == "enable"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "vrf-group-name"):
                self.vrf_group_name = value
                self.vrf_group_name.value_namespace = name_space
                self.vrf_group_name.value_namespace_prefix = name_space_prefix
            if(value_path == "enable"):
                self.enable = value
                self.enable.value_namespace = name_space
                self.enable.value_namespace_prefix = name_space_prefix

    def has_data(self):
        for c in self.vrf_group:
            if (c.has_data()):
                return True
        return False

    def has_operation(self):
        for c in self.vrf_group:
            if (c.has_operation()):
                return True
        return self.yfilter != YFilter.not_set

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-infra-rsi-cfg:vrf-groups" + path_buffer

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

        if (child_yang_name == "vrf-group"):
            for c in self.vrf_group:
                segment = c.get_segment_path()
                if (segment_path == segment):
                    return c
            c = VrfGroups.VrfGroup()
            c.parent = self
            local_reference_key = "ydk::seg::%s" % segment_path
            self._local_refs[local_reference_key] = c
            self.vrf_group.append(c)
            return c

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "vrf-group"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = VrfGroups()
        return self._top_entity

class SelectiveVrfDownload(Entity):
    """
    selective vrf download
    
    .. attribute:: disable
    
    	Disable selective VRF download
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    

    """

    _prefix = 'infra-rsi-cfg'
    _revision = '2016-12-19'

    def __init__(self):
        super(SelectiveVrfDownload, self).__init__()
        self._top_entity = None

        self.yang_name = "selective-vrf-download"
        self.yang_parent_name = "Cisco-IOS-XR-infra-rsi-cfg"

        self.disable = YLeaf(YType.empty, "disable")

    def __setattr__(self, name, value):
        self._check_monkey_patching_error(name, value)
        with _handle_type_error():
            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                    "Please use list append or extend method."
                                    .format(value))
            if isinstance(value, Enum.YLeaf):
                value = value.name
            if name in ("disable") and name in self.__dict__:
                if isinstance(value, YLeaf):
                    self.__dict__[name].set(value.get())
                elif isinstance(value, YLeafList):
                    super(SelectiveVrfDownload, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(SelectiveVrfDownload, self).__setattr__(name, value)

    def has_data(self):
        return self.disable.is_set

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            self.disable.yfilter != YFilter.not_set)

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-infra-rsi-cfg:selective-vrf-download" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()
        if (self.disable.is_set or self.disable.yfilter != YFilter.not_set):
            leaf_name_data.append(self.disable.get_name_leafdata())

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "disable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        if(value_path == "disable"):
            self.disable = value
            self.disable.value_namespace = name_space
            self.disable.value_namespace_prefix = name_space_prefix

    def clone_ptr(self):
        self._top_entity = SelectiveVrfDownload()
        return self._top_entity

