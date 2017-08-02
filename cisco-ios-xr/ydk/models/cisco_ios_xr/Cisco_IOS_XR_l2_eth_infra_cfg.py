""" Cisco_IOS_XR_l2_eth_infra_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR l2\-eth\-infra package configuration.

This module contains definitions
for the following management objects\:
  ethernet\-features\: Ethernet Features Configuration

This YANG module augments the
  Cisco\-IOS\-XR\-ifmgr\-cfg,
  Cisco\-IOS\-XR\-l2vpn\-cfg
modules with configuration data.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class EgressFiltering(Enum):
    """
    EgressFiltering

    Egress filtering

    .. data:: egress_filtering_type_strict = 1

    	Strict Egress Filtering

    .. data:: egress_filtering_type_disable = 2

    	Egress Filtering Disabled

    .. data:: egress_filtering_type_default = 3

    	Default Egress Filtering Behavior

    """

    egress_filtering_type_strict = Enum.YLeaf(1, "egress-filtering-type-strict")

    egress_filtering_type_disable = Enum.YLeaf(2, "egress-filtering-type-disable")

    egress_filtering_type_default = Enum.YLeaf(3, "egress-filtering-type-default")


class Filtering(Enum):
    """
    Filtering

    Filtering

    .. data:: filtering_type_dot1q = 0

    	C-Vlan ingress frame filtering (Table 8-1 of

    	802.1ad standard)

    .. data:: filtering_type_dot1ad = 1

    	S-Vlan ingress frame filtering (Table 8-2 of

    	802.1ad standard)

    """

    filtering_type_dot1q = Enum.YLeaf(0, "filtering-type-dot1q")

    filtering_type_dot1ad = Enum.YLeaf(1, "filtering-type-dot1ad")


class L2ProtocolMode(Enum):
    """
    L2ProtocolMode

    L2 protocol mode

    .. data:: forward = 0

    	Forward packets transparently

    .. data:: drop = 1

    	Drop the protocol's packets

    .. data:: tunnel = 2

    	Tunnel ingress frames, untunnel egress frames

    .. data:: reverse_tunnel = 3

    	Tunnel egress frames, untunnel ingress frames

    """

    forward = Enum.YLeaf(0, "forward")

    drop = Enum.YLeaf(1, "drop")

    tunnel = Enum.YLeaf(2, "tunnel")

    reverse_tunnel = Enum.YLeaf(3, "reverse-tunnel")


class L2ProtocolName(Enum):
    """
    L2ProtocolName

    L2 protocol name

    .. data:: cdp = 0

    	CDP

    .. data:: stp = 1

    	STP

    .. data:: vtp = 2

    	VTP

    .. data:: pvst = 3

    	PVST+

    .. data:: cpsv = 4

    	CDP, PVST+, STP, and VTP

    """

    cdp = Enum.YLeaf(0, "cdp")

    stp = Enum.YLeaf(1, "stp")

    vtp = Enum.YLeaf(2, "vtp")

    pvst = Enum.YLeaf(3, "pvst")

    cpsv = Enum.YLeaf(4, "cpsv")



class EthernetFeatures(Entity):
    """
    Ethernet Features Configuration
    
    .. attribute:: cfm
    
    	CFM global configuration
    	**type**\:   :py:class:`Cfm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.Cfm>`
    
    .. attribute:: egress_filtering
    
    	Egress Filtering Configuration
    	**type**\:   :py:class:`EgressFiltering <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.EgressFiltering>`
    
    .. attribute:: ether_link_oam
    
    	Ethernet Link OAM Global Configuration
    	**type**\:   :py:class:`EtherLinkOam <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.EtherLinkOam>`
    
    

    """

    _prefix = 'l2-eth-infra-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(EthernetFeatures, self).__init__()
        self._top_entity = None

        self.yang_name = "ethernet-features"
        self.yang_parent_name = "Cisco-IOS-XR-l2-eth-infra-cfg"

        self.cfm = EthernetFeatures.Cfm()
        self.cfm.parent = self
        self._children_name_map["cfm"] = "cfm"
        self._children_yang_names.add("cfm")

        self.egress_filtering = EthernetFeatures.EgressFiltering()
        self.egress_filtering.parent = self
        self._children_name_map["egress_filtering"] = "egress-filtering"
        self._children_yang_names.add("egress-filtering")

        self.ether_link_oam = EthernetFeatures.EtherLinkOam()
        self.ether_link_oam.parent = self
        self._children_name_map["ether_link_oam"] = "ether-link-oam"
        self._children_yang_names.add("ether-link-oam")


    class EgressFiltering(Entity):
        """
        Egress Filtering Configuration
        
        .. attribute:: egress_filtering_default_on
        
        	Whether Egress Filtering is on by default
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'l2-eth-infra-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(EthernetFeatures.EgressFiltering, self).__init__()

            self.yang_name = "egress-filtering"
            self.yang_parent_name = "ethernet-features"

            self.egress_filtering_default_on = YLeaf(YType.empty, "egress-filtering-default-on")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("egress_filtering_default_on") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(EthernetFeatures.EgressFiltering, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(EthernetFeatures.EgressFiltering, self).__setattr__(name, value)

        def has_data(self):
            return self.egress_filtering_default_on.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.egress_filtering_default_on.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "egress-filtering" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-l2-eth-infra-cfg:ethernet-features/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.egress_filtering_default_on.is_set or self.egress_filtering_default_on.yfilter != YFilter.not_set):
                leaf_name_data.append(self.egress_filtering_default_on.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "egress-filtering-default-on"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "egress-filtering-default-on"):
                self.egress_filtering_default_on = value
                self.egress_filtering_default_on.value_namespace = name_space
                self.egress_filtering_default_on.value_namespace_prefix = name_space_prefix


    class Cfm(Entity):
        """
        CFM global configuration
        
        .. attribute:: domains
        
        	Domain\-specific global configuration
        	**type**\:   :py:class:`Domains <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.Cfm.Domains>`
        
        .. attribute:: nv_satellite_sla_processing_disable
        
        	Disable processing of Ethernet SLA packets on nV Satellite devices
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: traceroute_cache
        
        	Traceroute Cache Configuration
        	**type**\:   :py:class:`TracerouteCache <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.Cfm.TracerouteCache>`
        
        

        """

        _prefix = 'ethernet-cfm-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(EthernetFeatures.Cfm, self).__init__()

            self.yang_name = "cfm"
            self.yang_parent_name = "ethernet-features"

            self.nv_satellite_sla_processing_disable = YLeaf(YType.empty, "nv-satellite-sla-processing-disable")

            self.domains = EthernetFeatures.Cfm.Domains()
            self.domains.parent = self
            self._children_name_map["domains"] = "domains"
            self._children_yang_names.add("domains")

            self.traceroute_cache = EthernetFeatures.Cfm.TracerouteCache()
            self.traceroute_cache.parent = self
            self._children_name_map["traceroute_cache"] = "traceroute-cache"
            self._children_yang_names.add("traceroute-cache")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("nv_satellite_sla_processing_disable") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(EthernetFeatures.Cfm, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(EthernetFeatures.Cfm, self).__setattr__(name, value)


        class TracerouteCache(Entity):
            """
            Traceroute Cache Configuration
            
            .. attribute:: cache_size
            
            	Cache Size limit (number of replies)
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            	**default value**\: 100
            
            .. attribute:: hold_time
            
            	Hold Time in minutes
            	**type**\:  int
            
            	**range:** 1..525600
            
            	**default value**\: 100
            
            

            """

            _prefix = 'ethernet-cfm-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(EthernetFeatures.Cfm.TracerouteCache, self).__init__()

                self.yang_name = "traceroute-cache"
                self.yang_parent_name = "cfm"

                self.cache_size = YLeaf(YType.uint32, "cache-size")

                self.hold_time = YLeaf(YType.uint32, "hold-time")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cache_size",
                                "hold_time") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(EthernetFeatures.Cfm.TracerouteCache, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(EthernetFeatures.Cfm.TracerouteCache, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cache_size.is_set or
                    self.hold_time.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cache_size.yfilter != YFilter.not_set or
                    self.hold_time.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "traceroute-cache" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-l2-eth-infra-cfg:ethernet-features/Cisco-IOS-XR-ethernet-cfm-cfg:cfm/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cache_size.is_set or self.cache_size.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cache_size.get_name_leafdata())
                if (self.hold_time.is_set or self.hold_time.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.hold_time.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cache-size" or name == "hold-time"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cache-size"):
                    self.cache_size = value
                    self.cache_size.value_namespace = name_space
                    self.cache_size.value_namespace_prefix = name_space_prefix
                if(value_path == "hold-time"):
                    self.hold_time = value
                    self.hold_time.value_namespace = name_space
                    self.hold_time.value_namespace_prefix = name_space_prefix


        class Domains(Entity):
            """
            Domain\-specific global configuration
            
            .. attribute:: domain
            
            	Configuration for a particular Maintenance Domain
            	**type**\: list of    :py:class:`Domain <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.Cfm.Domains.Domain>`
            
            

            """

            _prefix = 'ethernet-cfm-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(EthernetFeatures.Cfm.Domains, self).__init__()

                self.yang_name = "domains"
                self.yang_parent_name = "cfm"

                self.domain = YList(self)

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
                            super(EthernetFeatures.Cfm.Domains, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(EthernetFeatures.Cfm.Domains, self).__setattr__(name, value)


            class Domain(Entity):
                """
                Configuration for a particular Maintenance
                Domain
                
                .. attribute:: domain  <key>
                
                	Maintenance Domain
                	**type**\:  str
                
                	**length:** 1..79
                
                .. attribute:: domain_properties
                
                	Fundamental properties of the domain
                	**type**\:   :py:class:`DomainProperties <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.Cfm.Domains.Domain.DomainProperties>`
                
                .. attribute:: services
                
                	Service\-specific global configuration
                	**type**\:   :py:class:`Services <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.Cfm.Domains.Domain.Services>`
                
                

                """

                _prefix = 'ethernet-cfm-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(EthernetFeatures.Cfm.Domains.Domain, self).__init__()

                    self.yang_name = "domain"
                    self.yang_parent_name = "domains"

                    self.domain = YLeaf(YType.str, "domain")

                    self.domain_properties = EthernetFeatures.Cfm.Domains.Domain.DomainProperties()
                    self.domain_properties.parent = self
                    self._children_name_map["domain_properties"] = "domain-properties"
                    self._children_yang_names.add("domain-properties")

                    self.services = EthernetFeatures.Cfm.Domains.Domain.Services()
                    self.services.parent = self
                    self._children_name_map["services"] = "services"
                    self._children_yang_names.add("services")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("domain") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(EthernetFeatures.Cfm.Domains.Domain, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(EthernetFeatures.Cfm.Domains.Domain, self).__setattr__(name, value)


                class Services(Entity):
                    """
                    Service\-specific global configuration
                    
                    .. attribute:: service
                    
                    	Configuration for a particular Service (Maintenance Association)
                    	**type**\: list of    :py:class:`Service <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.Cfm.Domains.Domain.Services.Service>`
                    
                    

                    """

                    _prefix = 'ethernet-cfm-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(EthernetFeatures.Cfm.Domains.Domain.Services, self).__init__()

                        self.yang_name = "services"
                        self.yang_parent_name = "domain"

                        self.service = YList(self)

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
                                    super(EthernetFeatures.Cfm.Domains.Domain.Services, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(EthernetFeatures.Cfm.Domains.Domain.Services, self).__setattr__(name, value)


                    class Service(Entity):
                        """
                        Configuration for a particular Service
                        (Maintenance Association)
                        
                        .. attribute:: service  <key>
                        
                        	Service (Maintenance Association)
                        	**type**\:  str
                        
                        	**length:** 1..79
                        
                        .. attribute:: ais
                        
                        	Service specific AIS configuration
                        	**type**\:   :py:class:`Ais <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.Cfm.Domains.Domain.Services.Service.Ais>`
                        
                        .. attribute:: continuity_check_archive_hold_time
                        
                        	How long to store information for peer MEPs that have timed out
                        	**type**\:  int
                        
                        	**range:** 1..65535
                        
                        	**default value**\: 100
                        
                        .. attribute:: continuity_check_auto_traceroute
                        
                        	Automatically trigger a traceroute when a peer MEP times out
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: continuity_check_interval
                        
                        	Continuity Check Interval and Loss Threshold.  Configuring the interval enables Continuity Check
                        	**type**\:   :py:class:`ContinuityCheckInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.Cfm.Domains.Domain.Services.Service.ContinuityCheckInterval>`
                        
                        	**presence node**\: True
                        
                        .. attribute:: cross_check
                        
                        	Cross\-check configuration
                        	**type**\:   :py:class:`CrossCheck <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.Cfm.Domains.Domain.Services.Service.CrossCheck>`
                        
                        .. attribute:: efd2
                        
                        	Enable EFD to bring down ports when MEPs detect errors
                        	**type**\:   :py:class:`Efd2 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.Cfm.Domains.Domain.Services.Service.Efd2>`
                        
                        	**presence node**\: True
                        
                        .. attribute:: log_ais
                        
                        	Log receipt of AIS and LCK messages
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: log_continuity_check_errors
                        
                        	Log CCM Errors detected for peer MEPs
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: log_continuity_check_state_changes
                        
                        	Log peer MEPs state changes
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: log_cross_check_errors
                        
                        	Log Cross\-check Errors detected for peer MEPs
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: log_efd
                        
                        	Enable logging
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: maximum_meps
                        
                        	Limit on the number of MEPs in the service
                        	**type**\:  int
                        
                        	**range:** 2..8190
                        
                        	**default value**\: 100
                        
                        .. attribute:: mip_auto_creation
                        
                        	MIP Auto\-creation Policy
                        	**type**\:   :py:class:`MipAutoCreation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.Cfm.Domains.Domain.Services.Service.MipAutoCreation>`
                        
                        	**presence node**\: True
                        
                        .. attribute:: service_properties
                        
                        	Fundamental properties of the service (maintenance association)
                        	**type**\:   :py:class:`ServiceProperties <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.Cfm.Domains.Domain.Services.Service.ServiceProperties>`
                        
                        	**presence node**\: True
                        
                        .. attribute:: tags
                        
                        	The number of tags to use when sending CFM packets from up MEPs in this Service
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ethernet-cfm-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(EthernetFeatures.Cfm.Domains.Domain.Services.Service, self).__init__()

                            self.yang_name = "service"
                            self.yang_parent_name = "services"

                            self.service = YLeaf(YType.str, "service")

                            self.continuity_check_archive_hold_time = YLeaf(YType.uint32, "continuity-check-archive-hold-time")

                            self.continuity_check_auto_traceroute = YLeaf(YType.empty, "continuity-check-auto-traceroute")

                            self.log_ais = YLeaf(YType.empty, "log-ais")

                            self.log_continuity_check_errors = YLeaf(YType.empty, "log-continuity-check-errors")

                            self.log_continuity_check_state_changes = YLeaf(YType.empty, "log-continuity-check-state-changes")

                            self.log_cross_check_errors = YLeaf(YType.empty, "log-cross-check-errors")

                            self.log_efd = YLeaf(YType.empty, "log-efd")

                            self.maximum_meps = YLeaf(YType.uint32, "maximum-meps")

                            self.tags = YLeaf(YType.uint32, "tags")

                            self.ais = EthernetFeatures.Cfm.Domains.Domain.Services.Service.Ais()
                            self.ais.parent = self
                            self._children_name_map["ais"] = "ais"
                            self._children_yang_names.add("ais")

                            self.continuity_check_interval = None
                            self._children_name_map["continuity_check_interval"] = "continuity-check-interval"
                            self._children_yang_names.add("continuity-check-interval")

                            self.cross_check = EthernetFeatures.Cfm.Domains.Domain.Services.Service.CrossCheck()
                            self.cross_check.parent = self
                            self._children_name_map["cross_check"] = "cross-check"
                            self._children_yang_names.add("cross-check")

                            self.efd2 = None
                            self._children_name_map["efd2"] = "efd2"
                            self._children_yang_names.add("efd2")

                            self.mip_auto_creation = None
                            self._children_name_map["mip_auto_creation"] = "mip-auto-creation"
                            self._children_yang_names.add("mip-auto-creation")

                            self.service_properties = None
                            self._children_name_map["service_properties"] = "service-properties"
                            self._children_yang_names.add("service-properties")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("service",
                                            "continuity_check_archive_hold_time",
                                            "continuity_check_auto_traceroute",
                                            "log_ais",
                                            "log_continuity_check_errors",
                                            "log_continuity_check_state_changes",
                                            "log_cross_check_errors",
                                            "log_efd",
                                            "maximum_meps",
                                            "tags") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(EthernetFeatures.Cfm.Domains.Domain.Services.Service, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(EthernetFeatures.Cfm.Domains.Domain.Services.Service, self).__setattr__(name, value)


                        class Efd2(Entity):
                            """
                            Enable EFD to bring down ports when MEPs
                            detect errors
                            
                            .. attribute:: enable
                            
                            	Enable EFD
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            	**mandatory**\: True
                            
                            .. attribute:: protection_switching_enable
                            
                            	Enable protection switching notifications
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'ethernet-cfm-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(EthernetFeatures.Cfm.Domains.Domain.Services.Service.Efd2, self).__init__()

                                self.yang_name = "efd2"
                                self.yang_parent_name = "service"
                                self.is_presence_container = True

                                self.enable = YLeaf(YType.empty, "enable")

                                self.protection_switching_enable = YLeaf(YType.empty, "protection-switching-enable")

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
                                                "protection_switching_enable") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(EthernetFeatures.Cfm.Domains.Domain.Services.Service.Efd2, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(EthernetFeatures.Cfm.Domains.Domain.Services.Service.Efd2, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.enable.is_set or
                                    self.protection_switching_enable.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.enable.yfilter != YFilter.not_set or
                                    self.protection_switching_enable.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "efd2" + path_buffer

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
                                if (self.protection_switching_enable.is_set or self.protection_switching_enable.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.protection_switching_enable.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "enable" or name == "protection-switching-enable"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "enable"):
                                    self.enable = value
                                    self.enable.value_namespace = name_space
                                    self.enable.value_namespace_prefix = name_space_prefix
                                if(value_path == "protection-switching-enable"):
                                    self.protection_switching_enable = value
                                    self.protection_switching_enable.value_namespace = name_space
                                    self.protection_switching_enable.value_namespace_prefix = name_space_prefix


                        class ContinuityCheckInterval(Entity):
                            """
                            Continuity Check Interval and Loss
                            Threshold.  Configuring the interval
                            enables Continuity Check.
                            
                            .. attribute:: ccm_interval
                            
                            	CCM Interval
                            	**type**\:   :py:class:`CfmCcmInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_datatypes.CfmCcmInterval>`
                            
                            	**mandatory**\: True
                            
                            .. attribute:: loss_threshold
                            
                            	Loss Threshold (default 3)
                            	**type**\:  int
                            
                            	**range:** 2..255
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'ethernet-cfm-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(EthernetFeatures.Cfm.Domains.Domain.Services.Service.ContinuityCheckInterval, self).__init__()

                                self.yang_name = "continuity-check-interval"
                                self.yang_parent_name = "service"
                                self.is_presence_container = True

                                self.ccm_interval = YLeaf(YType.enumeration, "ccm-interval")

                                self.loss_threshold = YLeaf(YType.uint32, "loss-threshold")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("ccm_interval",
                                                "loss_threshold") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(EthernetFeatures.Cfm.Domains.Domain.Services.Service.ContinuityCheckInterval, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(EthernetFeatures.Cfm.Domains.Domain.Services.Service.ContinuityCheckInterval, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.ccm_interval.is_set or
                                    self.loss_threshold.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.ccm_interval.yfilter != YFilter.not_set or
                                    self.loss_threshold.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "continuity-check-interval" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.ccm_interval.is_set or self.ccm_interval.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ccm_interval.get_name_leafdata())
                                if (self.loss_threshold.is_set or self.loss_threshold.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.loss_threshold.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "ccm-interval" or name == "loss-threshold"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "ccm-interval"):
                                    self.ccm_interval = value
                                    self.ccm_interval.value_namespace = name_space
                                    self.ccm_interval.value_namespace_prefix = name_space_prefix
                                if(value_path == "loss-threshold"):
                                    self.loss_threshold = value
                                    self.loss_threshold.value_namespace = name_space
                                    self.loss_threshold.value_namespace_prefix = name_space_prefix


                        class MipAutoCreation(Entity):
                            """
                            MIP Auto\-creation Policy
                            
                            .. attribute:: ccm_learning_enable
                            
                            	Enable CCM Learning at MIPs in this service
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: mip_policy
                            
                            	MIP Auto\-creation Policy
                            	**type**\:   :py:class:`CfmMipPolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_cfg.CfmMipPolicy>`
                            
                            	**mandatory**\: True
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'ethernet-cfm-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(EthernetFeatures.Cfm.Domains.Domain.Services.Service.MipAutoCreation, self).__init__()

                                self.yang_name = "mip-auto-creation"
                                self.yang_parent_name = "service"
                                self.is_presence_container = True

                                self.ccm_learning_enable = YLeaf(YType.empty, "ccm-learning-enable")

                                self.mip_policy = YLeaf(YType.enumeration, "mip-policy")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("ccm_learning_enable",
                                                "mip_policy") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(EthernetFeatures.Cfm.Domains.Domain.Services.Service.MipAutoCreation, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(EthernetFeatures.Cfm.Domains.Domain.Services.Service.MipAutoCreation, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.ccm_learning_enable.is_set or
                                    self.mip_policy.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.ccm_learning_enable.yfilter != YFilter.not_set or
                                    self.mip_policy.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "mip-auto-creation" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.ccm_learning_enable.is_set or self.ccm_learning_enable.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ccm_learning_enable.get_name_leafdata())
                                if (self.mip_policy.is_set or self.mip_policy.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.mip_policy.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "ccm-learning-enable" or name == "mip-policy"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "ccm-learning-enable"):
                                    self.ccm_learning_enable = value
                                    self.ccm_learning_enable.value_namespace = name_space
                                    self.ccm_learning_enable.value_namespace_prefix = name_space_prefix
                                if(value_path == "mip-policy"):
                                    self.mip_policy = value
                                    self.mip_policy.value_namespace = name_space
                                    self.mip_policy.value_namespace_prefix = name_space_prefix


                        class Ais(Entity):
                            """
                            Service specific AIS configuration
                            
                            .. attribute:: transmission
                            
                            	AIS transmission configuration
                            	**type**\:   :py:class:`Transmission <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.Cfm.Domains.Domain.Services.Service.Ais.Transmission>`
                            
                            	**presence node**\: True
                            
                            

                            """

                            _prefix = 'ethernet-cfm-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(EthernetFeatures.Cfm.Domains.Domain.Services.Service.Ais, self).__init__()

                                self.yang_name = "ais"
                                self.yang_parent_name = "service"

                                self.transmission = None
                                self._children_name_map["transmission"] = "transmission"
                                self._children_yang_names.add("transmission")


                            class Transmission(Entity):
                                """
                                AIS transmission configuration
                                
                                .. attribute:: ais_interval
                                
                                	AIS Interval
                                	**type**\:   :py:class:`CfmAisInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_datatypes.CfmAisInterval>`
                                
                                .. attribute:: cos
                                
                                	Class of Service bits
                                	**type**\:  int
                                
                                	**range:** 0..7
                                
                                

                                This class is a :ref:`presence class<presence-class>`

                                """

                                _prefix = 'ethernet-cfm-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(EthernetFeatures.Cfm.Domains.Domain.Services.Service.Ais.Transmission, self).__init__()

                                    self.yang_name = "transmission"
                                    self.yang_parent_name = "ais"
                                    self.is_presence_container = True

                                    self.ais_interval = YLeaf(YType.enumeration, "ais-interval")

                                    self.cos = YLeaf(YType.uint32, "cos")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("ais_interval",
                                                    "cos") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(EthernetFeatures.Cfm.Domains.Domain.Services.Service.Ais.Transmission, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(EthernetFeatures.Cfm.Domains.Domain.Services.Service.Ais.Transmission, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.ais_interval.is_set or
                                        self.cos.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.ais_interval.yfilter != YFilter.not_set or
                                        self.cos.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "transmission" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.ais_interval.is_set or self.ais_interval.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.ais_interval.get_name_leafdata())
                                    if (self.cos.is_set or self.cos.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.cos.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "ais-interval" or name == "cos"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "ais-interval"):
                                        self.ais_interval = value
                                        self.ais_interval.value_namespace = name_space
                                        self.ais_interval.value_namespace_prefix = name_space_prefix
                                    if(value_path == "cos"):
                                        self.cos = value
                                        self.cos.value_namespace = name_space
                                        self.cos.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                return (self.transmission is not None)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    (self.transmission is not None and self.transmission.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "ais" + path_buffer

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

                                if (child_yang_name == "transmission"):
                                    if (self.transmission is None):
                                        self.transmission = EthernetFeatures.Cfm.Domains.Domain.Services.Service.Ais.Transmission()
                                        self.transmission.parent = self
                                        self._children_name_map["transmission"] = "transmission"
                                    return self.transmission

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "transmission"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass


                        class CrossCheck(Entity):
                            """
                            Cross\-check configuration
                            
                            .. attribute:: auto
                            
                            	Enable automatic MEP cross\-check
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: cross_check_meps
                            
                            	Cross\-check MEPs
                            	**type**\:   :py:class:`CrossCheckMeps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.Cfm.Domains.Domain.Services.Service.CrossCheck.CrossCheckMeps>`
                            
                            

                            """

                            _prefix = 'ethernet-cfm-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(EthernetFeatures.Cfm.Domains.Domain.Services.Service.CrossCheck, self).__init__()

                                self.yang_name = "cross-check"
                                self.yang_parent_name = "service"

                                self.auto = YLeaf(YType.empty, "auto")

                                self.cross_check_meps = EthernetFeatures.Cfm.Domains.Domain.Services.Service.CrossCheck.CrossCheckMeps()
                                self.cross_check_meps.parent = self
                                self._children_name_map["cross_check_meps"] = "cross-check-meps"
                                self._children_yang_names.add("cross-check-meps")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("auto") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(EthernetFeatures.Cfm.Domains.Domain.Services.Service.CrossCheck, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(EthernetFeatures.Cfm.Domains.Domain.Services.Service.CrossCheck, self).__setattr__(name, value)


                            class CrossCheckMeps(Entity):
                                """
                                Cross\-check MEPs
                                
                                .. attribute:: cross_check_mep
                                
                                	MEP ID and optional MAC Address for Cross\-check
                                	**type**\: list of    :py:class:`CrossCheckMep <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.Cfm.Domains.Domain.Services.Service.CrossCheck.CrossCheckMeps.CrossCheckMep>`
                                
                                

                                """

                                _prefix = 'ethernet-cfm-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(EthernetFeatures.Cfm.Domains.Domain.Services.Service.CrossCheck.CrossCheckMeps, self).__init__()

                                    self.yang_name = "cross-check-meps"
                                    self.yang_parent_name = "cross-check"

                                    self.cross_check_mep = YList(self)

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
                                                super(EthernetFeatures.Cfm.Domains.Domain.Services.Service.CrossCheck.CrossCheckMeps, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(EthernetFeatures.Cfm.Domains.Domain.Services.Service.CrossCheck.CrossCheckMeps, self).__setattr__(name, value)


                                class CrossCheckMep(Entity):
                                    """
                                    MEP ID and optional MAC Address for
                                    Cross\-check
                                    
                                    .. attribute:: mep_id  <key>
                                    
                                    	MEP ID
                                    	**type**\:  int
                                    
                                    	**range:** 1..8191
                                    
                                    .. attribute:: enable_mac_address
                                    
                                    	MAC Address is specified
                                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                    
                                    .. attribute:: mac_address
                                    
                                    	MAC Address
                                    	**type**\:  str
                                    
                                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                    
                                    

                                    """

                                    _prefix = 'ethernet-cfm-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(EthernetFeatures.Cfm.Domains.Domain.Services.Service.CrossCheck.CrossCheckMeps.CrossCheckMep, self).__init__()

                                        self.yang_name = "cross-check-mep"
                                        self.yang_parent_name = "cross-check-meps"

                                        self.mep_id = YLeaf(YType.uint32, "mep-id")

                                        self.enable_mac_address = YLeaf(YType.empty, "enable-mac-address")

                                        self.mac_address = YLeaf(YType.str, "mac-address")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("mep_id",
                                                        "enable_mac_address",
                                                        "mac_address") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(EthernetFeatures.Cfm.Domains.Domain.Services.Service.CrossCheck.CrossCheckMeps.CrossCheckMep, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(EthernetFeatures.Cfm.Domains.Domain.Services.Service.CrossCheck.CrossCheckMeps.CrossCheckMep, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.mep_id.is_set or
                                            self.enable_mac_address.is_set or
                                            self.mac_address.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.mep_id.yfilter != YFilter.not_set or
                                            self.enable_mac_address.yfilter != YFilter.not_set or
                                            self.mac_address.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "cross-check-mep" + "[mep-id='" + self.mep_id.get() + "']" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.mep_id.is_set or self.mep_id.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.mep_id.get_name_leafdata())
                                        if (self.enable_mac_address.is_set or self.enable_mac_address.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.enable_mac_address.get_name_leafdata())
                                        if (self.mac_address.is_set or self.mac_address.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.mac_address.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "mep-id" or name == "enable-mac-address" or name == "mac-address"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "mep-id"):
                                            self.mep_id = value
                                            self.mep_id.value_namespace = name_space
                                            self.mep_id.value_namespace_prefix = name_space_prefix
                                        if(value_path == "enable-mac-address"):
                                            self.enable_mac_address = value
                                            self.enable_mac_address.value_namespace = name_space
                                            self.enable_mac_address.value_namespace_prefix = name_space_prefix
                                        if(value_path == "mac-address"):
                                            self.mac_address = value
                                            self.mac_address.value_namespace = name_space
                                            self.mac_address.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    for c in self.cross_check_mep:
                                        if (c.has_data()):
                                            return True
                                    return False

                                def has_operation(self):
                                    for c in self.cross_check_mep:
                                        if (c.has_operation()):
                                            return True
                                    return self.yfilter != YFilter.not_set

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "cross-check-meps" + path_buffer

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

                                    if (child_yang_name == "cross-check-mep"):
                                        for c in self.cross_check_mep:
                                            segment = c.get_segment_path()
                                            if (segment_path == segment):
                                                return c
                                        c = EthernetFeatures.Cfm.Domains.Domain.Services.Service.CrossCheck.CrossCheckMeps.CrossCheckMep()
                                        c.parent = self
                                        local_reference_key = "ydk::seg::%s" % segment_path
                                        self._local_refs[local_reference_key] = c
                                        self.cross_check_mep.append(c)
                                        return c

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "cross-check-mep"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    pass

                            def has_data(self):
                                return (
                                    self.auto.is_set or
                                    (self.cross_check_meps is not None and self.cross_check_meps.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.auto.yfilter != YFilter.not_set or
                                    (self.cross_check_meps is not None and self.cross_check_meps.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "cross-check" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.auto.is_set or self.auto.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.auto.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "cross-check-meps"):
                                    if (self.cross_check_meps is None):
                                        self.cross_check_meps = EthernetFeatures.Cfm.Domains.Domain.Services.Service.CrossCheck.CrossCheckMeps()
                                        self.cross_check_meps.parent = self
                                        self._children_name_map["cross_check_meps"] = "cross-check-meps"
                                    return self.cross_check_meps

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "cross-check-meps" or name == "auto"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "auto"):
                                    self.auto = value
                                    self.auto.value_namespace = name_space
                                    self.auto.value_namespace_prefix = name_space_prefix


                        class ServiceProperties(Entity):
                            """
                            Fundamental properties of the service
                            (maintenance association)
                            
                            .. attribute:: ce_id
                            
                            	Local Customer Edge Identifier
                            	**type**\:  int
                            
                            	**range:** 1..16384
                            
                            .. attribute:: group_name
                            
                            	Bridge Group or Cross\-connect Group, if Service Type is BridgeDomain or CrossConnect
                            	**type**\:  str
                            
                            .. attribute:: remote_ce_id
                            
                            	Remote Customer Edge Identifier
                            	**type**\:  int
                            
                            	**range:** 1..16384
                            
                            .. attribute:: service_type
                            
                            	Type of Service
                            	**type**\:   :py:class:`CfmService <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_cfg.CfmService>`
                            
                            	**mandatory**\: True
                            
                            .. attribute:: short_ma_name_format
                            
                            	Short MA Name Format
                            	**type**\:   :py:class:`CfmShortMaNameFormat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_cfg.CfmShortMaNameFormat>`
                            
                            .. attribute:: short_ma_name_icc
                            
                            	ITU Carrier Code (ICC), if format is ICCBased
                            	**type**\:  str
                            
                            	**length:** 1..6
                            
                            .. attribute:: short_ma_name_number
                            
                            	Numeric Short MA Name, if format is VlanID or Number
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: short_ma_name_oui
                            
                            	VPN OUI, if Short MA Name format is VPN\_ID
                            	**type**\:  int
                            
                            	**range:** 0..16777215
                            
                            .. attribute:: short_ma_name_string
                            
                            	String Short MA Name, if format is String
                            	**type**\:  str
                            
                            	**length:** 1..45
                            
                            .. attribute:: short_ma_name_umc
                            
                            	Unique MEG ID Code (UMC), if format is ICCBased
                            	**type**\:  str
                            
                            	**length:** 1..12
                            
                            .. attribute:: short_ma_name_vpn_index
                            
                            	VPN Index, if Short MA Name format is VPN\_ID
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: switching_name
                            
                            	Bridge Domain or Cross\-connect name, if Service Type is BridgeDomain or CrossConnect
                            	**type**\:  str
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'ethernet-cfm-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(EthernetFeatures.Cfm.Domains.Domain.Services.Service.ServiceProperties, self).__init__()

                                self.yang_name = "service-properties"
                                self.yang_parent_name = "service"
                                self.is_presence_container = True

                                self.ce_id = YLeaf(YType.uint32, "ce-id")

                                self.group_name = YLeaf(YType.str, "group-name")

                                self.remote_ce_id = YLeaf(YType.uint32, "remote-ce-id")

                                self.service_type = YLeaf(YType.enumeration, "service-type")

                                self.short_ma_name_format = YLeaf(YType.enumeration, "short-ma-name-format")

                                self.short_ma_name_icc = YLeaf(YType.str, "short-ma-name-icc")

                                self.short_ma_name_number = YLeaf(YType.uint32, "short-ma-name-number")

                                self.short_ma_name_oui = YLeaf(YType.uint32, "short-ma-name-oui")

                                self.short_ma_name_string = YLeaf(YType.str, "short-ma-name-string")

                                self.short_ma_name_umc = YLeaf(YType.str, "short-ma-name-umc")

                                self.short_ma_name_vpn_index = YLeaf(YType.int32, "short-ma-name-vpn-index")

                                self.switching_name = YLeaf(YType.str, "switching-name")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("ce_id",
                                                "group_name",
                                                "remote_ce_id",
                                                "service_type",
                                                "short_ma_name_format",
                                                "short_ma_name_icc",
                                                "short_ma_name_number",
                                                "short_ma_name_oui",
                                                "short_ma_name_string",
                                                "short_ma_name_umc",
                                                "short_ma_name_vpn_index",
                                                "switching_name") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(EthernetFeatures.Cfm.Domains.Domain.Services.Service.ServiceProperties, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(EthernetFeatures.Cfm.Domains.Domain.Services.Service.ServiceProperties, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.ce_id.is_set or
                                    self.group_name.is_set or
                                    self.remote_ce_id.is_set or
                                    self.service_type.is_set or
                                    self.short_ma_name_format.is_set or
                                    self.short_ma_name_icc.is_set or
                                    self.short_ma_name_number.is_set or
                                    self.short_ma_name_oui.is_set or
                                    self.short_ma_name_string.is_set or
                                    self.short_ma_name_umc.is_set or
                                    self.short_ma_name_vpn_index.is_set or
                                    self.switching_name.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.ce_id.yfilter != YFilter.not_set or
                                    self.group_name.yfilter != YFilter.not_set or
                                    self.remote_ce_id.yfilter != YFilter.not_set or
                                    self.service_type.yfilter != YFilter.not_set or
                                    self.short_ma_name_format.yfilter != YFilter.not_set or
                                    self.short_ma_name_icc.yfilter != YFilter.not_set or
                                    self.short_ma_name_number.yfilter != YFilter.not_set or
                                    self.short_ma_name_oui.yfilter != YFilter.not_set or
                                    self.short_ma_name_string.yfilter != YFilter.not_set or
                                    self.short_ma_name_umc.yfilter != YFilter.not_set or
                                    self.short_ma_name_vpn_index.yfilter != YFilter.not_set or
                                    self.switching_name.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "service-properties" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.ce_id.is_set or self.ce_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ce_id.get_name_leafdata())
                                if (self.group_name.is_set or self.group_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.group_name.get_name_leafdata())
                                if (self.remote_ce_id.is_set or self.remote_ce_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.remote_ce_id.get_name_leafdata())
                                if (self.service_type.is_set or self.service_type.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.service_type.get_name_leafdata())
                                if (self.short_ma_name_format.is_set or self.short_ma_name_format.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.short_ma_name_format.get_name_leafdata())
                                if (self.short_ma_name_icc.is_set or self.short_ma_name_icc.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.short_ma_name_icc.get_name_leafdata())
                                if (self.short_ma_name_number.is_set or self.short_ma_name_number.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.short_ma_name_number.get_name_leafdata())
                                if (self.short_ma_name_oui.is_set or self.short_ma_name_oui.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.short_ma_name_oui.get_name_leafdata())
                                if (self.short_ma_name_string.is_set or self.short_ma_name_string.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.short_ma_name_string.get_name_leafdata())
                                if (self.short_ma_name_umc.is_set or self.short_ma_name_umc.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.short_ma_name_umc.get_name_leafdata())
                                if (self.short_ma_name_vpn_index.is_set or self.short_ma_name_vpn_index.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.short_ma_name_vpn_index.get_name_leafdata())
                                if (self.switching_name.is_set or self.switching_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.switching_name.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "ce-id" or name == "group-name" or name == "remote-ce-id" or name == "service-type" or name == "short-ma-name-format" or name == "short-ma-name-icc" or name == "short-ma-name-number" or name == "short-ma-name-oui" or name == "short-ma-name-string" or name == "short-ma-name-umc" or name == "short-ma-name-vpn-index" or name == "switching-name"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "ce-id"):
                                    self.ce_id = value
                                    self.ce_id.value_namespace = name_space
                                    self.ce_id.value_namespace_prefix = name_space_prefix
                                if(value_path == "group-name"):
                                    self.group_name = value
                                    self.group_name.value_namespace = name_space
                                    self.group_name.value_namespace_prefix = name_space_prefix
                                if(value_path == "remote-ce-id"):
                                    self.remote_ce_id = value
                                    self.remote_ce_id.value_namespace = name_space
                                    self.remote_ce_id.value_namespace_prefix = name_space_prefix
                                if(value_path == "service-type"):
                                    self.service_type = value
                                    self.service_type.value_namespace = name_space
                                    self.service_type.value_namespace_prefix = name_space_prefix
                                if(value_path == "short-ma-name-format"):
                                    self.short_ma_name_format = value
                                    self.short_ma_name_format.value_namespace = name_space
                                    self.short_ma_name_format.value_namespace_prefix = name_space_prefix
                                if(value_path == "short-ma-name-icc"):
                                    self.short_ma_name_icc = value
                                    self.short_ma_name_icc.value_namespace = name_space
                                    self.short_ma_name_icc.value_namespace_prefix = name_space_prefix
                                if(value_path == "short-ma-name-number"):
                                    self.short_ma_name_number = value
                                    self.short_ma_name_number.value_namespace = name_space
                                    self.short_ma_name_number.value_namespace_prefix = name_space_prefix
                                if(value_path == "short-ma-name-oui"):
                                    self.short_ma_name_oui = value
                                    self.short_ma_name_oui.value_namespace = name_space
                                    self.short_ma_name_oui.value_namespace_prefix = name_space_prefix
                                if(value_path == "short-ma-name-string"):
                                    self.short_ma_name_string = value
                                    self.short_ma_name_string.value_namespace = name_space
                                    self.short_ma_name_string.value_namespace_prefix = name_space_prefix
                                if(value_path == "short-ma-name-umc"):
                                    self.short_ma_name_umc = value
                                    self.short_ma_name_umc.value_namespace = name_space
                                    self.short_ma_name_umc.value_namespace_prefix = name_space_prefix
                                if(value_path == "short-ma-name-vpn-index"):
                                    self.short_ma_name_vpn_index = value
                                    self.short_ma_name_vpn_index.value_namespace = name_space
                                    self.short_ma_name_vpn_index.value_namespace_prefix = name_space_prefix
                                if(value_path == "switching-name"):
                                    self.switching_name = value
                                    self.switching_name.value_namespace = name_space
                                    self.switching_name.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                self.service.is_set or
                                self.continuity_check_archive_hold_time.is_set or
                                self.continuity_check_auto_traceroute.is_set or
                                self.log_ais.is_set or
                                self.log_continuity_check_errors.is_set or
                                self.log_continuity_check_state_changes.is_set or
                                self.log_cross_check_errors.is_set or
                                self.log_efd.is_set or
                                self.maximum_meps.is_set or
                                self.tags.is_set or
                                (self.ais is not None and self.ais.has_data()) or
                                (self.cross_check is not None and self.cross_check.has_data()) or
                                (self.continuity_check_interval is not None) or
                                (self.efd2 is not None) or
                                (self.mip_auto_creation is not None) or
                                (self.service_properties is not None))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.service.yfilter != YFilter.not_set or
                                self.continuity_check_archive_hold_time.yfilter != YFilter.not_set or
                                self.continuity_check_auto_traceroute.yfilter != YFilter.not_set or
                                self.log_ais.yfilter != YFilter.not_set or
                                self.log_continuity_check_errors.yfilter != YFilter.not_set or
                                self.log_continuity_check_state_changes.yfilter != YFilter.not_set or
                                self.log_cross_check_errors.yfilter != YFilter.not_set or
                                self.log_efd.yfilter != YFilter.not_set or
                                self.maximum_meps.yfilter != YFilter.not_set or
                                self.tags.yfilter != YFilter.not_set or
                                (self.ais is not None and self.ais.has_operation()) or
                                (self.continuity_check_interval is not None and self.continuity_check_interval.has_operation()) or
                                (self.cross_check is not None and self.cross_check.has_operation()) or
                                (self.efd2 is not None and self.efd2.has_operation()) or
                                (self.mip_auto_creation is not None and self.mip_auto_creation.has_operation()) or
                                (self.service_properties is not None and self.service_properties.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "service" + "[service='" + self.service.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.service.is_set or self.service.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.service.get_name_leafdata())
                            if (self.continuity_check_archive_hold_time.is_set or self.continuity_check_archive_hold_time.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.continuity_check_archive_hold_time.get_name_leafdata())
                            if (self.continuity_check_auto_traceroute.is_set or self.continuity_check_auto_traceroute.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.continuity_check_auto_traceroute.get_name_leafdata())
                            if (self.log_ais.is_set or self.log_ais.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.log_ais.get_name_leafdata())
                            if (self.log_continuity_check_errors.is_set or self.log_continuity_check_errors.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.log_continuity_check_errors.get_name_leafdata())
                            if (self.log_continuity_check_state_changes.is_set or self.log_continuity_check_state_changes.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.log_continuity_check_state_changes.get_name_leafdata())
                            if (self.log_cross_check_errors.is_set or self.log_cross_check_errors.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.log_cross_check_errors.get_name_leafdata())
                            if (self.log_efd.is_set or self.log_efd.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.log_efd.get_name_leafdata())
                            if (self.maximum_meps.is_set or self.maximum_meps.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.maximum_meps.get_name_leafdata())
                            if (self.tags.is_set or self.tags.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.tags.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "ais"):
                                if (self.ais is None):
                                    self.ais = EthernetFeatures.Cfm.Domains.Domain.Services.Service.Ais()
                                    self.ais.parent = self
                                    self._children_name_map["ais"] = "ais"
                                return self.ais

                            if (child_yang_name == "continuity-check-interval"):
                                if (self.continuity_check_interval is None):
                                    self.continuity_check_interval = EthernetFeatures.Cfm.Domains.Domain.Services.Service.ContinuityCheckInterval()
                                    self.continuity_check_interval.parent = self
                                    self._children_name_map["continuity_check_interval"] = "continuity-check-interval"
                                return self.continuity_check_interval

                            if (child_yang_name == "cross-check"):
                                if (self.cross_check is None):
                                    self.cross_check = EthernetFeatures.Cfm.Domains.Domain.Services.Service.CrossCheck()
                                    self.cross_check.parent = self
                                    self._children_name_map["cross_check"] = "cross-check"
                                return self.cross_check

                            if (child_yang_name == "efd2"):
                                if (self.efd2 is None):
                                    self.efd2 = EthernetFeatures.Cfm.Domains.Domain.Services.Service.Efd2()
                                    self.efd2.parent = self
                                    self._children_name_map["efd2"] = "efd2"
                                return self.efd2

                            if (child_yang_name == "mip-auto-creation"):
                                if (self.mip_auto_creation is None):
                                    self.mip_auto_creation = EthernetFeatures.Cfm.Domains.Domain.Services.Service.MipAutoCreation()
                                    self.mip_auto_creation.parent = self
                                    self._children_name_map["mip_auto_creation"] = "mip-auto-creation"
                                return self.mip_auto_creation

                            if (child_yang_name == "service-properties"):
                                if (self.service_properties is None):
                                    self.service_properties = EthernetFeatures.Cfm.Domains.Domain.Services.Service.ServiceProperties()
                                    self.service_properties.parent = self
                                    self._children_name_map["service_properties"] = "service-properties"
                                return self.service_properties

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "ais" or name == "continuity-check-interval" or name == "cross-check" or name == "efd2" or name == "mip-auto-creation" or name == "service-properties" or name == "service" or name == "continuity-check-archive-hold-time" or name == "continuity-check-auto-traceroute" or name == "log-ais" or name == "log-continuity-check-errors" or name == "log-continuity-check-state-changes" or name == "log-cross-check-errors" or name == "log-efd" or name == "maximum-meps" or name == "tags"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "service"):
                                self.service = value
                                self.service.value_namespace = name_space
                                self.service.value_namespace_prefix = name_space_prefix
                            if(value_path == "continuity-check-archive-hold-time"):
                                self.continuity_check_archive_hold_time = value
                                self.continuity_check_archive_hold_time.value_namespace = name_space
                                self.continuity_check_archive_hold_time.value_namespace_prefix = name_space_prefix
                            if(value_path == "continuity-check-auto-traceroute"):
                                self.continuity_check_auto_traceroute = value
                                self.continuity_check_auto_traceroute.value_namespace = name_space
                                self.continuity_check_auto_traceroute.value_namespace_prefix = name_space_prefix
                            if(value_path == "log-ais"):
                                self.log_ais = value
                                self.log_ais.value_namespace = name_space
                                self.log_ais.value_namespace_prefix = name_space_prefix
                            if(value_path == "log-continuity-check-errors"):
                                self.log_continuity_check_errors = value
                                self.log_continuity_check_errors.value_namespace = name_space
                                self.log_continuity_check_errors.value_namespace_prefix = name_space_prefix
                            if(value_path == "log-continuity-check-state-changes"):
                                self.log_continuity_check_state_changes = value
                                self.log_continuity_check_state_changes.value_namespace = name_space
                                self.log_continuity_check_state_changes.value_namespace_prefix = name_space_prefix
                            if(value_path == "log-cross-check-errors"):
                                self.log_cross_check_errors = value
                                self.log_cross_check_errors.value_namespace = name_space
                                self.log_cross_check_errors.value_namespace_prefix = name_space_prefix
                            if(value_path == "log-efd"):
                                self.log_efd = value
                                self.log_efd.value_namespace = name_space
                                self.log_efd.value_namespace_prefix = name_space_prefix
                            if(value_path == "maximum-meps"):
                                self.maximum_meps = value
                                self.maximum_meps.value_namespace = name_space
                                self.maximum_meps.value_namespace_prefix = name_space_prefix
                            if(value_path == "tags"):
                                self.tags = value
                                self.tags.value_namespace = name_space
                                self.tags.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.service:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.service:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "services" + path_buffer

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

                        if (child_yang_name == "service"):
                            for c in self.service:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = EthernetFeatures.Cfm.Domains.Domain.Services.Service()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.service.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "service"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class DomainProperties(Entity):
                    """
                    Fundamental properties of the domain
                    
                    .. attribute:: level
                    
                    	Maintenance Domain Level
                    	**type**\:  int
                    
                    	**range:** 0..7
                    
                    .. attribute:: mdid_format
                    
                    	Maintenance Domain ID Format
                    	**type**\:   :py:class:`CfmMdidFormat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_cfg.CfmMdidFormat>`
                    
                    .. attribute:: mdid_mac_address
                    
                    	MAC Address, if MDID Format is MACAddress
                    	**type**\:  str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: mdid_number
                    
                    	Unsigned 16\-bit Interger, if MDID Format is MACAddress
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: mdid_string
                    
                    	String MDID, if MDID format is String or DNSLike
                    	**type**\:  str
                    
                    	**length:** 1..43
                    
                    

                    """

                    _prefix = 'ethernet-cfm-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(EthernetFeatures.Cfm.Domains.Domain.DomainProperties, self).__init__()

                        self.yang_name = "domain-properties"
                        self.yang_parent_name = "domain"

                        self.level = YLeaf(YType.uint32, "level")

                        self.mdid_format = YLeaf(YType.enumeration, "mdid-format")

                        self.mdid_mac_address = YLeaf(YType.str, "mdid-mac-address")

                        self.mdid_number = YLeaf(YType.uint32, "mdid-number")

                        self.mdid_string = YLeaf(YType.str, "mdid-string")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("level",
                                        "mdid_format",
                                        "mdid_mac_address",
                                        "mdid_number",
                                        "mdid_string") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(EthernetFeatures.Cfm.Domains.Domain.DomainProperties, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(EthernetFeatures.Cfm.Domains.Domain.DomainProperties, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.level.is_set or
                            self.mdid_format.is_set or
                            self.mdid_mac_address.is_set or
                            self.mdid_number.is_set or
                            self.mdid_string.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.level.yfilter != YFilter.not_set or
                            self.mdid_format.yfilter != YFilter.not_set or
                            self.mdid_mac_address.yfilter != YFilter.not_set or
                            self.mdid_number.yfilter != YFilter.not_set or
                            self.mdid_string.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "domain-properties" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.level.is_set or self.level.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.level.get_name_leafdata())
                        if (self.mdid_format.is_set or self.mdid_format.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mdid_format.get_name_leafdata())
                        if (self.mdid_mac_address.is_set or self.mdid_mac_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mdid_mac_address.get_name_leafdata())
                        if (self.mdid_number.is_set or self.mdid_number.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mdid_number.get_name_leafdata())
                        if (self.mdid_string.is_set or self.mdid_string.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mdid_string.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "level" or name == "mdid-format" or name == "mdid-mac-address" or name == "mdid-number" or name == "mdid-string"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "level"):
                            self.level = value
                            self.level.value_namespace = name_space
                            self.level.value_namespace_prefix = name_space_prefix
                        if(value_path == "mdid-format"):
                            self.mdid_format = value
                            self.mdid_format.value_namespace = name_space
                            self.mdid_format.value_namespace_prefix = name_space_prefix
                        if(value_path == "mdid-mac-address"):
                            self.mdid_mac_address = value
                            self.mdid_mac_address.value_namespace = name_space
                            self.mdid_mac_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "mdid-number"):
                            self.mdid_number = value
                            self.mdid_number.value_namespace = name_space
                            self.mdid_number.value_namespace_prefix = name_space_prefix
                        if(value_path == "mdid-string"):
                            self.mdid_string = value
                            self.mdid_string.value_namespace = name_space
                            self.mdid_string.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.domain.is_set or
                        (self.domain_properties is not None and self.domain_properties.has_data()) or
                        (self.services is not None and self.services.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.domain.yfilter != YFilter.not_set or
                        (self.domain_properties is not None and self.domain_properties.has_operation()) or
                        (self.services is not None and self.services.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "domain" + "[domain='" + self.domain.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-l2-eth-infra-cfg:ethernet-features/Cisco-IOS-XR-ethernet-cfm-cfg:cfm/domains/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.domain.is_set or self.domain.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.domain.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "domain-properties"):
                        if (self.domain_properties is None):
                            self.domain_properties = EthernetFeatures.Cfm.Domains.Domain.DomainProperties()
                            self.domain_properties.parent = self
                            self._children_name_map["domain_properties"] = "domain-properties"
                        return self.domain_properties

                    if (child_yang_name == "services"):
                        if (self.services is None):
                            self.services = EthernetFeatures.Cfm.Domains.Domain.Services()
                            self.services.parent = self
                            self._children_name_map["services"] = "services"
                        return self.services

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "domain-properties" or name == "services" or name == "domain"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "domain"):
                        self.domain = value
                        self.domain.value_namespace = name_space
                        self.domain.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.domain:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.domain:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "domains" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-l2-eth-infra-cfg:ethernet-features/Cisco-IOS-XR-ethernet-cfm-cfg:cfm/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "domain"):
                    for c in self.domain:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = EthernetFeatures.Cfm.Domains.Domain()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.domain.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "domain"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (
                self.nv_satellite_sla_processing_disable.is_set or
                (self.domains is not None and self.domains.has_data()) or
                (self.traceroute_cache is not None and self.traceroute_cache.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.nv_satellite_sla_processing_disable.yfilter != YFilter.not_set or
                (self.domains is not None and self.domains.has_operation()) or
                (self.traceroute_cache is not None and self.traceroute_cache.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "Cisco-IOS-XR-ethernet-cfm-cfg:cfm" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-l2-eth-infra-cfg:ethernet-features/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.nv_satellite_sla_processing_disable.is_set or self.nv_satellite_sla_processing_disable.yfilter != YFilter.not_set):
                leaf_name_data.append(self.nv_satellite_sla_processing_disable.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "domains"):
                if (self.domains is None):
                    self.domains = EthernetFeatures.Cfm.Domains()
                    self.domains.parent = self
                    self._children_name_map["domains"] = "domains"
                return self.domains

            if (child_yang_name == "traceroute-cache"):
                if (self.traceroute_cache is None):
                    self.traceroute_cache = EthernetFeatures.Cfm.TracerouteCache()
                    self.traceroute_cache.parent = self
                    self._children_name_map["traceroute_cache"] = "traceroute-cache"
                return self.traceroute_cache

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "domains" or name == "traceroute-cache" or name == "nv-satellite-sla-processing-disable"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "nv-satellite-sla-processing-disable"):
                self.nv_satellite_sla_processing_disable = value
                self.nv_satellite_sla_processing_disable.value_namespace = name_space
                self.nv_satellite_sla_processing_disable.value_namespace_prefix = name_space_prefix


    class EtherLinkOam(Entity):
        """
        Ethernet Link OAM Global Configuration
        
        .. attribute:: profiles
        
        	Table of Ethernet Link OAM profiles
        	**type**\:   :py:class:`Profiles <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.EtherLinkOam.Profiles>`
        
        

        """

        _prefix = 'ethernet-link-oam-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(EthernetFeatures.EtherLinkOam, self).__init__()

            self.yang_name = "ether-link-oam"
            self.yang_parent_name = "ethernet-features"

            self.profiles = EthernetFeatures.EtherLinkOam.Profiles()
            self.profiles.parent = self
            self._children_name_map["profiles"] = "profiles"
            self._children_yang_names.add("profiles")


        class Profiles(Entity):
            """
            Table of Ethernet Link OAM profiles
            
            .. attribute:: profile
            
            	Name of the profile
            	**type**\: list of    :py:class:`Profile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.EtherLinkOam.Profiles.Profile>`
            
            

            """

            _prefix = 'ethernet-link-oam-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(EthernetFeatures.EtherLinkOam.Profiles, self).__init__()

                self.yang_name = "profiles"
                self.yang_parent_name = "ether-link-oam"

                self.profile = YList(self)

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
                            super(EthernetFeatures.EtherLinkOam.Profiles, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(EthernetFeatures.EtherLinkOam.Profiles, self).__setattr__(name, value)


            class Profile(Entity):
                """
                Name of the profile
                
                .. attribute:: profile  <key>
                
                	none
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: action
                
                	Configure action parameters
                	**type**\:   :py:class:`Action <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.EtherLinkOam.Profiles.Profile.Action>`
                
                .. attribute:: hello_interval
                
                	Possible Ethernet Link OAM hello intervals
                	**type**\:   :py:class:`EtherLinkOamHelloIntervalEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg.EtherLinkOamHelloIntervalEnum>`
                
                .. attribute:: link_monitoring
                
                	Configure link monitor parameters
                	**type**\:   :py:class:`LinkMonitoring <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring>`
                
                .. attribute:: mib_retrieval
                
                	Enable or disable MIB retrieval support
                	**type**\:  bool
                
                .. attribute:: mode
                
                	Set the OAM mode to passive
                	**type**\:   :py:class:`EtherLinkOamModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg.EtherLinkOamModeEnum>`
                
                .. attribute:: remote_loopback
                
                	Enable or disable remote loopback support
                	**type**\:  bool
                
                .. attribute:: require_remote
                
                	Configure remote requirement parameters
                	**type**\:   :py:class:`RequireRemote <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.EtherLinkOam.Profiles.Profile.RequireRemote>`
                
                .. attribute:: timeout
                
                	Connection timeout period in number of lost heartbeats
                	**type**\:  int
                
                	**range:** 2..30
                
                .. attribute:: udlf
                
                	Enable or disable uni\-directional link\-fault detection support
                	**type**\:  bool
                
                

                """

                _prefix = 'ethernet-link-oam-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(EthernetFeatures.EtherLinkOam.Profiles.Profile, self).__init__()

                    self.yang_name = "profile"
                    self.yang_parent_name = "profiles"

                    self.profile = YLeaf(YType.str, "profile")

                    self.hello_interval = YLeaf(YType.enumeration, "hello-interval")

                    self.mib_retrieval = YLeaf(YType.boolean, "mib-retrieval")

                    self.mode = YLeaf(YType.enumeration, "mode")

                    self.remote_loopback = YLeaf(YType.boolean, "remote-loopback")

                    self.timeout = YLeaf(YType.uint32, "timeout")

                    self.udlf = YLeaf(YType.boolean, "udlf")

                    self.action = EthernetFeatures.EtherLinkOam.Profiles.Profile.Action()
                    self.action.parent = self
                    self._children_name_map["action"] = "action"
                    self._children_yang_names.add("action")

                    self.link_monitoring = EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring()
                    self.link_monitoring.parent = self
                    self._children_name_map["link_monitoring"] = "link-monitoring"
                    self._children_yang_names.add("link-monitoring")

                    self.require_remote = EthernetFeatures.EtherLinkOam.Profiles.Profile.RequireRemote()
                    self.require_remote.parent = self
                    self._children_name_map["require_remote"] = "require-remote"
                    self._children_yang_names.add("require-remote")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("profile",
                                    "hello_interval",
                                    "mib_retrieval",
                                    "mode",
                                    "remote_loopback",
                                    "timeout",
                                    "udlf") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(EthernetFeatures.EtherLinkOam.Profiles.Profile, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(EthernetFeatures.EtherLinkOam.Profiles.Profile, self).__setattr__(name, value)


                class Action(Entity):
                    """
                    Configure action parameters
                    
                    .. attribute:: capabilities_conflict
                    
                    	Action to perform when a capabilities conflict occurs
                    	**type**\:   :py:class:`EtherLinkOamEventActionEnumEfd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg.EtherLinkOamEventActionEnumEfd>`
                    
                    .. attribute:: critical_event
                    
                    	Action to perform when a critical event occurs
                    	**type**\:   :py:class:`EtherLinkOamEventActionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg.EtherLinkOamEventActionEnum>`
                    
                    .. attribute:: discovery_timeout
                    
                    	Action to perform when discovery timeout occurs
                    	**type**\:   :py:class:`EtherLinkOamEventActionEnumEfd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg.EtherLinkOamEventActionEnumEfd>`
                    
                    .. attribute:: dying_gasp
                    
                    	Action to perform when a dying gasp occurs
                    	**type**\:   :py:class:`EtherLinkOamEventActionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg.EtherLinkOamEventActionEnum>`
                    
                    .. attribute:: high_threshold
                    
                    	Action to perform when a high\-threshold event occurs
                    	**type**\:   :py:class:`EtherLinkOamEventActionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg.EtherLinkOamEventActionEnum>`
                    
                    .. attribute:: link_fault
                    
                    	Action to perform when a link fault message is received
                    	**type**\:   :py:class:`EtherLinkOamEventActionEnumEfd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg.EtherLinkOamEventActionEnumEfd>`
                    
                    .. attribute:: remote_loopback
                    
                    	Action to perform when remote loopback is entered or exited
                    	**type**\:   :py:class:`EtherLinkOamEventActionPrimEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg.EtherLinkOamEventActionPrimEnum>`
                    
                    .. attribute:: session_down
                    
                    	Action to perform when a session goes down
                    	**type**\:   :py:class:`EtherLinkOamEventActionEnumEfd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg.EtherLinkOamEventActionEnumEfd>`
                    
                    .. attribute:: session_up
                    
                    	Action to perform when a session comes up
                    	**type**\:   :py:class:`EtherLinkOamEventActionPrimEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg.EtherLinkOamEventActionPrimEnum>`
                    
                    .. attribute:: wiring_conflict
                    
                    	Action to perform when a wiring conflict occurs
                    	**type**\:   :py:class:`EtherLinkOamEventActionEnumEfd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg.EtherLinkOamEventActionEnumEfd>`
                    
                    

                    """

                    _prefix = 'ethernet-link-oam-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(EthernetFeatures.EtherLinkOam.Profiles.Profile.Action, self).__init__()

                        self.yang_name = "action"
                        self.yang_parent_name = "profile"

                        self.capabilities_conflict = YLeaf(YType.enumeration, "capabilities-conflict")

                        self.critical_event = YLeaf(YType.enumeration, "critical-event")

                        self.discovery_timeout = YLeaf(YType.enumeration, "discovery-timeout")

                        self.dying_gasp = YLeaf(YType.enumeration, "dying-gasp")

                        self.high_threshold = YLeaf(YType.enumeration, "high-threshold")

                        self.link_fault = YLeaf(YType.enumeration, "link-fault")

                        self.remote_loopback = YLeaf(YType.enumeration, "remote-loopback")

                        self.session_down = YLeaf(YType.enumeration, "session-down")

                        self.session_up = YLeaf(YType.enumeration, "session-up")

                        self.wiring_conflict = YLeaf(YType.enumeration, "wiring-conflict")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("capabilities_conflict",
                                        "critical_event",
                                        "discovery_timeout",
                                        "dying_gasp",
                                        "high_threshold",
                                        "link_fault",
                                        "remote_loopback",
                                        "session_down",
                                        "session_up",
                                        "wiring_conflict") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(EthernetFeatures.EtherLinkOam.Profiles.Profile.Action, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(EthernetFeatures.EtherLinkOam.Profiles.Profile.Action, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.capabilities_conflict.is_set or
                            self.critical_event.is_set or
                            self.discovery_timeout.is_set or
                            self.dying_gasp.is_set or
                            self.high_threshold.is_set or
                            self.link_fault.is_set or
                            self.remote_loopback.is_set or
                            self.session_down.is_set or
                            self.session_up.is_set or
                            self.wiring_conflict.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.capabilities_conflict.yfilter != YFilter.not_set or
                            self.critical_event.yfilter != YFilter.not_set or
                            self.discovery_timeout.yfilter != YFilter.not_set or
                            self.dying_gasp.yfilter != YFilter.not_set or
                            self.high_threshold.yfilter != YFilter.not_set or
                            self.link_fault.yfilter != YFilter.not_set or
                            self.remote_loopback.yfilter != YFilter.not_set or
                            self.session_down.yfilter != YFilter.not_set or
                            self.session_up.yfilter != YFilter.not_set or
                            self.wiring_conflict.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "action" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.capabilities_conflict.is_set or self.capabilities_conflict.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.capabilities_conflict.get_name_leafdata())
                        if (self.critical_event.is_set or self.critical_event.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.critical_event.get_name_leafdata())
                        if (self.discovery_timeout.is_set or self.discovery_timeout.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.discovery_timeout.get_name_leafdata())
                        if (self.dying_gasp.is_set or self.dying_gasp.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.dying_gasp.get_name_leafdata())
                        if (self.high_threshold.is_set or self.high_threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.high_threshold.get_name_leafdata())
                        if (self.link_fault.is_set or self.link_fault.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.link_fault.get_name_leafdata())
                        if (self.remote_loopback.is_set or self.remote_loopback.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.remote_loopback.get_name_leafdata())
                        if (self.session_down.is_set or self.session_down.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.session_down.get_name_leafdata())
                        if (self.session_up.is_set or self.session_up.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.session_up.get_name_leafdata())
                        if (self.wiring_conflict.is_set or self.wiring_conflict.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.wiring_conflict.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "capabilities-conflict" or name == "critical-event" or name == "discovery-timeout" or name == "dying-gasp" or name == "high-threshold" or name == "link-fault" or name == "remote-loopback" or name == "session-down" or name == "session-up" or name == "wiring-conflict"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "capabilities-conflict"):
                            self.capabilities_conflict = value
                            self.capabilities_conflict.value_namespace = name_space
                            self.capabilities_conflict.value_namespace_prefix = name_space_prefix
                        if(value_path == "critical-event"):
                            self.critical_event = value
                            self.critical_event.value_namespace = name_space
                            self.critical_event.value_namespace_prefix = name_space_prefix
                        if(value_path == "discovery-timeout"):
                            self.discovery_timeout = value
                            self.discovery_timeout.value_namespace = name_space
                            self.discovery_timeout.value_namespace_prefix = name_space_prefix
                        if(value_path == "dying-gasp"):
                            self.dying_gasp = value
                            self.dying_gasp.value_namespace = name_space
                            self.dying_gasp.value_namespace_prefix = name_space_prefix
                        if(value_path == "high-threshold"):
                            self.high_threshold = value
                            self.high_threshold.value_namespace = name_space
                            self.high_threshold.value_namespace_prefix = name_space_prefix
                        if(value_path == "link-fault"):
                            self.link_fault = value
                            self.link_fault.value_namespace = name_space
                            self.link_fault.value_namespace_prefix = name_space_prefix
                        if(value_path == "remote-loopback"):
                            self.remote_loopback = value
                            self.remote_loopback.value_namespace = name_space
                            self.remote_loopback.value_namespace_prefix = name_space_prefix
                        if(value_path == "session-down"):
                            self.session_down = value
                            self.session_down.value_namespace = name_space
                            self.session_down.value_namespace_prefix = name_space_prefix
                        if(value_path == "session-up"):
                            self.session_up = value
                            self.session_up.value_namespace = name_space
                            self.session_up.value_namespace_prefix = name_space_prefix
                        if(value_path == "wiring-conflict"):
                            self.wiring_conflict = value
                            self.wiring_conflict.value_namespace = name_space
                            self.wiring_conflict.value_namespace_prefix = name_space_prefix


                class RequireRemote(Entity):
                    """
                    Configure remote requirement parameters
                    
                    .. attribute:: link_monitoring
                    
                    	Enable or disable link monitoring requirement
                    	**type**\:  bool
                    
                    .. attribute:: mib_retrieval
                    
                    	Enable or disable MIB retrieval requirement
                    	**type**\:  bool
                    
                    .. attribute:: mode
                    
                    	Possible required OAM modes
                    	**type**\:   :py:class:`EtherLinkOamRequireModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg.EtherLinkOamRequireModeEnum>`
                    
                    .. attribute:: remote_loopback
                    
                    	Enable or disable remote loopback requirement
                    	**type**\:  bool
                    
                    

                    """

                    _prefix = 'ethernet-link-oam-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(EthernetFeatures.EtherLinkOam.Profiles.Profile.RequireRemote, self).__init__()

                        self.yang_name = "require-remote"
                        self.yang_parent_name = "profile"

                        self.link_monitoring = YLeaf(YType.boolean, "link-monitoring")

                        self.mib_retrieval = YLeaf(YType.boolean, "mib-retrieval")

                        self.mode = YLeaf(YType.enumeration, "mode")

                        self.remote_loopback = YLeaf(YType.boolean, "remote-loopback")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("link_monitoring",
                                        "mib_retrieval",
                                        "mode",
                                        "remote_loopback") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(EthernetFeatures.EtherLinkOam.Profiles.Profile.RequireRemote, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(EthernetFeatures.EtherLinkOam.Profiles.Profile.RequireRemote, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.link_monitoring.is_set or
                            self.mib_retrieval.is_set or
                            self.mode.is_set or
                            self.remote_loopback.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.link_monitoring.yfilter != YFilter.not_set or
                            self.mib_retrieval.yfilter != YFilter.not_set or
                            self.mode.yfilter != YFilter.not_set or
                            self.remote_loopback.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "require-remote" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.link_monitoring.is_set or self.link_monitoring.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.link_monitoring.get_name_leafdata())
                        if (self.mib_retrieval.is_set or self.mib_retrieval.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mib_retrieval.get_name_leafdata())
                        if (self.mode.is_set or self.mode.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mode.get_name_leafdata())
                        if (self.remote_loopback.is_set or self.remote_loopback.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.remote_loopback.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "link-monitoring" or name == "mib-retrieval" or name == "mode" or name == "remote-loopback"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "link-monitoring"):
                            self.link_monitoring = value
                            self.link_monitoring.value_namespace = name_space
                            self.link_monitoring.value_namespace_prefix = name_space_prefix
                        if(value_path == "mib-retrieval"):
                            self.mib_retrieval = value
                            self.mib_retrieval.value_namespace = name_space
                            self.mib_retrieval.value_namespace_prefix = name_space_prefix
                        if(value_path == "mode"):
                            self.mode = value
                            self.mode.value_namespace = name_space
                            self.mode.value_namespace_prefix = name_space_prefix
                        if(value_path == "remote-loopback"):
                            self.remote_loopback = value
                            self.remote_loopback.value_namespace = name_space
                            self.remote_loopback.value_namespace_prefix = name_space_prefix


                class LinkMonitoring(Entity):
                    """
                    Configure link monitor parameters
                    
                    .. attribute:: frame
                    
                    	Frame event configuration
                    	**type**\:   :py:class:`Frame <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.Frame>`
                    
                    .. attribute:: frame_period
                    
                    	Frame\-period event configuration
                    	**type**\:   :py:class:`FramePeriod <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.FramePeriod>`
                    
                    .. attribute:: frame_seconds
                    
                    	Frame\-seconds event configuration
                    	**type**\:   :py:class:`FrameSeconds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.FrameSeconds>`
                    
                    .. attribute:: monitoring
                    
                    	Enable or disable monitoring
                    	**type**\:  bool
                    
                    .. attribute:: symbol_period
                    
                    	Symbol\-period event configuration
                    	**type**\:   :py:class:`SymbolPeriod <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.SymbolPeriod>`
                    
                    

                    """

                    _prefix = 'ethernet-link-oam-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring, self).__init__()

                        self.yang_name = "link-monitoring"
                        self.yang_parent_name = "profile"

                        self.monitoring = YLeaf(YType.boolean, "monitoring")

                        self.frame = EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.Frame()
                        self.frame.parent = self
                        self._children_name_map["frame"] = "frame"
                        self._children_yang_names.add("frame")

                        self.frame_period = EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.FramePeriod()
                        self.frame_period.parent = self
                        self._children_name_map["frame_period"] = "frame-period"
                        self._children_yang_names.add("frame-period")

                        self.frame_seconds = EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.FrameSeconds()
                        self.frame_seconds.parent = self
                        self._children_name_map["frame_seconds"] = "frame-seconds"
                        self._children_yang_names.add("frame-seconds")

                        self.symbol_period = EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.SymbolPeriod()
                        self.symbol_period.parent = self
                        self._children_name_map["symbol_period"] = "symbol-period"
                        self._children_yang_names.add("symbol-period")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("monitoring") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring, self).__setattr__(name, value)


                    class SymbolPeriod(Entity):
                        """
                        Symbol\-period event configuration
                        
                        .. attribute:: threshold
                        
                        	Threshold configuration for symbol\-period events
                        	**type**\:   :py:class:`Threshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.SymbolPeriod.Threshold>`
                        
                        .. attribute:: window
                        
                        	Window size configuration for symbol\-period events
                        	**type**\:   :py:class:`Window <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.SymbolPeriod.Window>`
                        
                        	**presence node**\: True
                        
                        

                        """

                        _prefix = 'ethernet-link-oam-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.SymbolPeriod, self).__init__()

                            self.yang_name = "symbol-period"
                            self.yang_parent_name = "link-monitoring"

                            self.threshold = EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.SymbolPeriod.Threshold()
                            self.threshold.parent = self
                            self._children_name_map["threshold"] = "threshold"
                            self._children_yang_names.add("threshold")

                            self.window = None
                            self._children_name_map["window"] = "window"
                            self._children_yang_names.add("window")


                        class Window(Entity):
                            """
                            Window size configuration for symbol\-period
                            events
                            
                            .. attribute:: multiplier
                            
                            	The multiplier to use for this window (only valid if 'Units' is Symbols and treated as 1 if unspecified)
                            	**type**\:   :py:class:`EtherLinkOamThresholdWindowMultiplierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg.EtherLinkOamThresholdWindowMultiplierEnum>`
                            
                            	**default value**\: none
                            
                            .. attribute:: units
                            
                            	Units to use for this window
                            	**type**\:   :py:class:`EtherLinkOamWindowUnitsSymbolsEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg.EtherLinkOamWindowUnitsSymbolsEnum>`
                            
                            	**mandatory**\: True
                            
                            .. attribute:: window
                            
                            	Size of the symbol\-period window
                            	**type**\:  int
                            
                            	**range:** 1..4294967295
                            
                            	**mandatory**\: True
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'ethernet-link-oam-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.SymbolPeriod.Window, self).__init__()

                                self.yang_name = "window"
                                self.yang_parent_name = "symbol-period"
                                self.is_presence_container = True

                                self.multiplier = YLeaf(YType.enumeration, "multiplier")

                                self.units = YLeaf(YType.enumeration, "units")

                                self.window = YLeaf(YType.uint32, "window")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("multiplier",
                                                "units",
                                                "window") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.SymbolPeriod.Window, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.SymbolPeriod.Window, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.multiplier.is_set or
                                    self.units.is_set or
                                    self.window.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.multiplier.yfilter != YFilter.not_set or
                                    self.units.yfilter != YFilter.not_set or
                                    self.window.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "window" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.multiplier.is_set or self.multiplier.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.multiplier.get_name_leafdata())
                                if (self.units.is_set or self.units.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.units.get_name_leafdata())
                                if (self.window.is_set or self.window.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.window.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "multiplier" or name == "units" or name == "window"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "multiplier"):
                                    self.multiplier = value
                                    self.multiplier.value_namespace = name_space
                                    self.multiplier.value_namespace_prefix = name_space_prefix
                                if(value_path == "units"):
                                    self.units = value
                                    self.units.value_namespace = name_space
                                    self.units.value_namespace_prefix = name_space_prefix
                                if(value_path == "window"):
                                    self.window = value
                                    self.window.value_namespace = name_space
                                    self.window.value_namespace_prefix = name_space_prefix


                        class Threshold(Entity):
                            """
                            Threshold configuration for symbol\-period
                            events
                            
                            .. attribute:: multiplier_high
                            
                            	The multiplier to use for the high threshold (only valid if 'Units' is Symbols and treated as 1 if unspecified)
                            	**type**\:   :py:class:`EtherLinkOamThresholdWindowMultiplierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg.EtherLinkOamThresholdWindowMultiplierEnum>`
                            
                            .. attribute:: multiplier_low
                            
                            	The multiplier to use for the low threshold (only valid if 'Units' is Symbols and treated as 1 if unspecified)
                            	**type**\:   :py:class:`EtherLinkOamThresholdWindowMultiplierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg.EtherLinkOamThresholdWindowMultiplierEnum>`
                            
                            	**default value**\: none
                            
                            .. attribute:: threshold_high
                            
                            	The high threshold for symbol\-period
                            	**type**\:  int
                            
                            	**range:** 1..4294967295
                            
                            .. attribute:: threshold_low
                            
                            	The low threshold for symbol\-period
                            	**type**\:  int
                            
                            	**range:** 1..4294967295
                            
                            	**default value**\: 1
                            
                            .. attribute:: units
                            
                            	The units to use for these thresholds
                            	**type**\:   :py:class:`EtherLinkOamThresholdUnitsSymbolsEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg.EtherLinkOamThresholdUnitsSymbolsEnum>`
                            
                            	**default value**\: symbols
                            
                            

                            """

                            _prefix = 'ethernet-link-oam-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.SymbolPeriod.Threshold, self).__init__()

                                self.yang_name = "threshold"
                                self.yang_parent_name = "symbol-period"

                                self.multiplier_high = YLeaf(YType.enumeration, "multiplier-high")

                                self.multiplier_low = YLeaf(YType.enumeration, "multiplier-low")

                                self.threshold_high = YLeaf(YType.uint32, "threshold-high")

                                self.threshold_low = YLeaf(YType.uint32, "threshold-low")

                                self.units = YLeaf(YType.enumeration, "units")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("multiplier_high",
                                                "multiplier_low",
                                                "threshold_high",
                                                "threshold_low",
                                                "units") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.SymbolPeriod.Threshold, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.SymbolPeriod.Threshold, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.multiplier_high.is_set or
                                    self.multiplier_low.is_set or
                                    self.threshold_high.is_set or
                                    self.threshold_low.is_set or
                                    self.units.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.multiplier_high.yfilter != YFilter.not_set or
                                    self.multiplier_low.yfilter != YFilter.not_set or
                                    self.threshold_high.yfilter != YFilter.not_set or
                                    self.threshold_low.yfilter != YFilter.not_set or
                                    self.units.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "threshold" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.multiplier_high.is_set or self.multiplier_high.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.multiplier_high.get_name_leafdata())
                                if (self.multiplier_low.is_set or self.multiplier_low.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.multiplier_low.get_name_leafdata())
                                if (self.threshold_high.is_set or self.threshold_high.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.threshold_high.get_name_leafdata())
                                if (self.threshold_low.is_set or self.threshold_low.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.threshold_low.get_name_leafdata())
                                if (self.units.is_set or self.units.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.units.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "multiplier-high" or name == "multiplier-low" or name == "threshold-high" or name == "threshold-low" or name == "units"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "multiplier-high"):
                                    self.multiplier_high = value
                                    self.multiplier_high.value_namespace = name_space
                                    self.multiplier_high.value_namespace_prefix = name_space_prefix
                                if(value_path == "multiplier-low"):
                                    self.multiplier_low = value
                                    self.multiplier_low.value_namespace = name_space
                                    self.multiplier_low.value_namespace_prefix = name_space_prefix
                                if(value_path == "threshold-high"):
                                    self.threshold_high = value
                                    self.threshold_high.value_namespace = name_space
                                    self.threshold_high.value_namespace_prefix = name_space_prefix
                                if(value_path == "threshold-low"):
                                    self.threshold_low = value
                                    self.threshold_low.value_namespace = name_space
                                    self.threshold_low.value_namespace_prefix = name_space_prefix
                                if(value_path == "units"):
                                    self.units = value
                                    self.units.value_namespace = name_space
                                    self.units.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                (self.threshold is not None and self.threshold.has_data()) or
                                (self.window is not None))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                (self.threshold is not None and self.threshold.has_operation()) or
                                (self.window is not None and self.window.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "symbol-period" + path_buffer

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

                            if (child_yang_name == "threshold"):
                                if (self.threshold is None):
                                    self.threshold = EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.SymbolPeriod.Threshold()
                                    self.threshold.parent = self
                                    self._children_name_map["threshold"] = "threshold"
                                return self.threshold

                            if (child_yang_name == "window"):
                                if (self.window is None):
                                    self.window = EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.SymbolPeriod.Window()
                                    self.window.parent = self
                                    self._children_name_map["window"] = "window"
                                return self.window

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "threshold" or name == "window"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass


                    class FramePeriod(Entity):
                        """
                        Frame\-period event configuration
                        
                        .. attribute:: threshold
                        
                        	Threshold configuration for frame\-period events
                        	**type**\:   :py:class:`Threshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.FramePeriod.Threshold>`
                        
                        .. attribute:: window
                        
                        	Window size configuration for frame\-period events
                        	**type**\:   :py:class:`Window <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.FramePeriod.Window>`
                        
                        	**presence node**\: True
                        
                        

                        """

                        _prefix = 'ethernet-link-oam-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.FramePeriod, self).__init__()

                            self.yang_name = "frame-period"
                            self.yang_parent_name = "link-monitoring"

                            self.threshold = EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.FramePeriod.Threshold()
                            self.threshold.parent = self
                            self._children_name_map["threshold"] = "threshold"
                            self._children_yang_names.add("threshold")

                            self.window = None
                            self._children_name_map["window"] = "window"
                            self._children_yang_names.add("window")


                        class Window(Entity):
                            """
                            Window size configuration for frame\-period
                            events
                            
                            .. attribute:: multiplier
                            
                            	The multiplier to use for this window (only valid if 'Units' is Frames and treated as 1 if unspecified)
                            	**type**\:   :py:class:`EtherLinkOamThresholdWindowMultiplierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg.EtherLinkOamThresholdWindowMultiplierEnum>`
                            
                            	**default value**\: none
                            
                            .. attribute:: units
                            
                            	The units to use for this window
                            	**type**\:   :py:class:`EtherLinkOamWindowUnitsFramesEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg.EtherLinkOamWindowUnitsFramesEnum>`
                            
                            	**mandatory**\: True
                            
                            .. attribute:: window
                            
                            	Size of the frame\-period window
                            	**type**\:  int
                            
                            	**range:** 1..4294967295
                            
                            	**mandatory**\: True
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'ethernet-link-oam-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.FramePeriod.Window, self).__init__()

                                self.yang_name = "window"
                                self.yang_parent_name = "frame-period"
                                self.is_presence_container = True

                                self.multiplier = YLeaf(YType.enumeration, "multiplier")

                                self.units = YLeaf(YType.enumeration, "units")

                                self.window = YLeaf(YType.uint32, "window")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("multiplier",
                                                "units",
                                                "window") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.FramePeriod.Window, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.FramePeriod.Window, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.multiplier.is_set or
                                    self.units.is_set or
                                    self.window.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.multiplier.yfilter != YFilter.not_set or
                                    self.units.yfilter != YFilter.not_set or
                                    self.window.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "window" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.multiplier.is_set or self.multiplier.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.multiplier.get_name_leafdata())
                                if (self.units.is_set or self.units.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.units.get_name_leafdata())
                                if (self.window.is_set or self.window.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.window.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "multiplier" or name == "units" or name == "window"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "multiplier"):
                                    self.multiplier = value
                                    self.multiplier.value_namespace = name_space
                                    self.multiplier.value_namespace_prefix = name_space_prefix
                                if(value_path == "units"):
                                    self.units = value
                                    self.units.value_namespace = name_space
                                    self.units.value_namespace_prefix = name_space_prefix
                                if(value_path == "window"):
                                    self.window = value
                                    self.window.value_namespace = name_space
                                    self.window.value_namespace_prefix = name_space_prefix


                        class Threshold(Entity):
                            """
                            Threshold configuration for frame\-period
                            events
                            
                            .. attribute:: multiplier_high
                            
                            	The multiplier to use for the high threshold (only valid if 'Units' is Frames and treated as 1 if unspecified)
                            	**type**\:   :py:class:`EtherLinkOamThresholdWindowMultiplierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg.EtherLinkOamThresholdWindowMultiplierEnum>`
                            
                            .. attribute:: multiplier_low
                            
                            	The multiplier to use for the low threshold (only valid if 'Units' is Frames and treated as 1 if unspecified)
                            	**type**\:   :py:class:`EtherLinkOamThresholdWindowMultiplierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg.EtherLinkOamThresholdWindowMultiplierEnum>`
                            
                            	**default value**\: none
                            
                            .. attribute:: threshold_high
                            
                            	The high threshold for frame\-period events
                            	**type**\:  int
                            
                            	**range:** 1..4294967295
                            
                            .. attribute:: threshold_low
                            
                            	The low threshold for frame\-period events
                            	**type**\:  int
                            
                            	**range:** 1..4294967295
                            
                            	**default value**\: 1
                            
                            .. attribute:: units
                            
                            	The units to use for these thresholds
                            	**type**\:   :py:class:`EtherLinkOamThresholdUnitsFramesEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg.EtherLinkOamThresholdUnitsFramesEnum>`
                            
                            	**default value**\: ppm
                            
                            

                            """

                            _prefix = 'ethernet-link-oam-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.FramePeriod.Threshold, self).__init__()

                                self.yang_name = "threshold"
                                self.yang_parent_name = "frame-period"

                                self.multiplier_high = YLeaf(YType.enumeration, "multiplier-high")

                                self.multiplier_low = YLeaf(YType.enumeration, "multiplier-low")

                                self.threshold_high = YLeaf(YType.uint32, "threshold-high")

                                self.threshold_low = YLeaf(YType.uint32, "threshold-low")

                                self.units = YLeaf(YType.enumeration, "units")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("multiplier_high",
                                                "multiplier_low",
                                                "threshold_high",
                                                "threshold_low",
                                                "units") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.FramePeriod.Threshold, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.FramePeriod.Threshold, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.multiplier_high.is_set or
                                    self.multiplier_low.is_set or
                                    self.threshold_high.is_set or
                                    self.threshold_low.is_set or
                                    self.units.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.multiplier_high.yfilter != YFilter.not_set or
                                    self.multiplier_low.yfilter != YFilter.not_set or
                                    self.threshold_high.yfilter != YFilter.not_set or
                                    self.threshold_low.yfilter != YFilter.not_set or
                                    self.units.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "threshold" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.multiplier_high.is_set or self.multiplier_high.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.multiplier_high.get_name_leafdata())
                                if (self.multiplier_low.is_set or self.multiplier_low.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.multiplier_low.get_name_leafdata())
                                if (self.threshold_high.is_set or self.threshold_high.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.threshold_high.get_name_leafdata())
                                if (self.threshold_low.is_set or self.threshold_low.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.threshold_low.get_name_leafdata())
                                if (self.units.is_set or self.units.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.units.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "multiplier-high" or name == "multiplier-low" or name == "threshold-high" or name == "threshold-low" or name == "units"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "multiplier-high"):
                                    self.multiplier_high = value
                                    self.multiplier_high.value_namespace = name_space
                                    self.multiplier_high.value_namespace_prefix = name_space_prefix
                                if(value_path == "multiplier-low"):
                                    self.multiplier_low = value
                                    self.multiplier_low.value_namespace = name_space
                                    self.multiplier_low.value_namespace_prefix = name_space_prefix
                                if(value_path == "threshold-high"):
                                    self.threshold_high = value
                                    self.threshold_high.value_namespace = name_space
                                    self.threshold_high.value_namespace_prefix = name_space_prefix
                                if(value_path == "threshold-low"):
                                    self.threshold_low = value
                                    self.threshold_low.value_namespace = name_space
                                    self.threshold_low.value_namespace_prefix = name_space_prefix
                                if(value_path == "units"):
                                    self.units = value
                                    self.units.value_namespace = name_space
                                    self.units.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                (self.threshold is not None and self.threshold.has_data()) or
                                (self.window is not None))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                (self.threshold is not None and self.threshold.has_operation()) or
                                (self.window is not None and self.window.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "frame-period" + path_buffer

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

                            if (child_yang_name == "threshold"):
                                if (self.threshold is None):
                                    self.threshold = EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.FramePeriod.Threshold()
                                    self.threshold.parent = self
                                    self._children_name_map["threshold"] = "threshold"
                                return self.threshold

                            if (child_yang_name == "window"):
                                if (self.window is None):
                                    self.window = EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.FramePeriod.Window()
                                    self.window.parent = self
                                    self._children_name_map["window"] = "window"
                                return self.window

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "threshold" or name == "window"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass


                    class FrameSeconds(Entity):
                        """
                        Frame\-seconds event configuration
                        
                        .. attribute:: threshold
                        
                        	Threshold configuration for frame\-seconds events
                        	**type**\:   :py:class:`Threshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.FrameSeconds.Threshold>`
                        
                        .. attribute:: window
                        
                        	Window size configuration for frame\-seconds events
                        	**type**\:  int
                        
                        	**range:** 10000..900000
                        
                        	**units**\: millisecond
                        
                        	**default value**\: 60000
                        
                        

                        """

                        _prefix = 'ethernet-link-oam-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.FrameSeconds, self).__init__()

                            self.yang_name = "frame-seconds"
                            self.yang_parent_name = "link-monitoring"

                            self.window = YLeaf(YType.uint32, "window")

                            self.threshold = EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.FrameSeconds.Threshold()
                            self.threshold.parent = self
                            self._children_name_map["threshold"] = "threshold"
                            self._children_yang_names.add("threshold")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("window") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.FrameSeconds, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.FrameSeconds, self).__setattr__(name, value)


                        class Threshold(Entity):
                            """
                            Threshold configuration for frame\-seconds
                            events
                            
                            .. attribute:: threshold_high
                            
                            	The high threshold for frame\-seconds events
                            	**type**\:  int
                            
                            	**range:** 1..900
                            
                            	**units**\: second
                            
                            .. attribute:: threshold_low
                            
                            	The low threshold for frame\-seconds events
                            	**type**\:  int
                            
                            	**range:** 1..900
                            
                            	**units**\: second
                            
                            	**default value**\: 1
                            
                            

                            """

                            _prefix = 'ethernet-link-oam-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.FrameSeconds.Threshold, self).__init__()

                                self.yang_name = "threshold"
                                self.yang_parent_name = "frame-seconds"

                                self.threshold_high = YLeaf(YType.uint32, "threshold-high")

                                self.threshold_low = YLeaf(YType.uint32, "threshold-low")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("threshold_high",
                                                "threshold_low") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.FrameSeconds.Threshold, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.FrameSeconds.Threshold, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.threshold_high.is_set or
                                    self.threshold_low.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.threshold_high.yfilter != YFilter.not_set or
                                    self.threshold_low.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "threshold" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.threshold_high.is_set or self.threshold_high.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.threshold_high.get_name_leafdata())
                                if (self.threshold_low.is_set or self.threshold_low.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.threshold_low.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "threshold-high" or name == "threshold-low"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "threshold-high"):
                                    self.threshold_high = value
                                    self.threshold_high.value_namespace = name_space
                                    self.threshold_high.value_namespace_prefix = name_space_prefix
                                if(value_path == "threshold-low"):
                                    self.threshold_low = value
                                    self.threshold_low.value_namespace = name_space
                                    self.threshold_low.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                self.window.is_set or
                                (self.threshold is not None and self.threshold.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.window.yfilter != YFilter.not_set or
                                (self.threshold is not None and self.threshold.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "frame-seconds" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.window.is_set or self.window.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.window.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "threshold"):
                                if (self.threshold is None):
                                    self.threshold = EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.FrameSeconds.Threshold()
                                    self.threshold.parent = self
                                    self._children_name_map["threshold"] = "threshold"
                                return self.threshold

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "threshold" or name == "window"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "window"):
                                self.window = value
                                self.window.value_namespace = name_space
                                self.window.value_namespace_prefix = name_space_prefix


                    class Frame(Entity):
                        """
                        Frame event configuration
                        
                        .. attribute:: threshold
                        
                        	Threshold configuration for frame events
                        	**type**\:   :py:class:`Threshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_cfg.EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.Frame.Threshold>`
                        
                        .. attribute:: window
                        
                        	Window size configuration for frame events
                        	**type**\:  int
                        
                        	**range:** 1000..60000
                        
                        	**units**\: millisecond
                        
                        	**default value**\: 1000
                        
                        

                        """

                        _prefix = 'ethernet-link-oam-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.Frame, self).__init__()

                            self.yang_name = "frame"
                            self.yang_parent_name = "link-monitoring"

                            self.window = YLeaf(YType.uint32, "window")

                            self.threshold = EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.Frame.Threshold()
                            self.threshold.parent = self
                            self._children_name_map["threshold"] = "threshold"
                            self._children_yang_names.add("threshold")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("window") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.Frame, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.Frame, self).__setattr__(name, value)


                        class Threshold(Entity):
                            """
                            Threshold configuration for frame events
                            
                            .. attribute:: multiplier_high
                            
                            	The multiplier to use for the high threshold (treated as 1 if unspecified)
                            	**type**\:   :py:class:`EtherLinkOamThresholdWindowMultiplierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg.EtherLinkOamThresholdWindowMultiplierEnum>`
                            
                            .. attribute:: multiplier_low
                            
                            	The multiplier to use for the low threshold (treated as 1 if unspecified)
                            	**type**\:   :py:class:`EtherLinkOamThresholdWindowMultiplierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg.EtherLinkOamThresholdWindowMultiplierEnum>`
                            
                            	**default value**\: none
                            
                            .. attribute:: threshold_high
                            
                            	The high threshold for frame events
                            	**type**\:  int
                            
                            	**range:** 1..4294967295
                            
                            .. attribute:: threshold_low
                            
                            	The low threshold for frame events
                            	**type**\:  int
                            
                            	**range:** 1..4294967295
                            
                            	**default value**\: 1
                            
                            

                            """

                            _prefix = 'ethernet-link-oam-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.Frame.Threshold, self).__init__()

                                self.yang_name = "threshold"
                                self.yang_parent_name = "frame"

                                self.multiplier_high = YLeaf(YType.enumeration, "multiplier-high")

                                self.multiplier_low = YLeaf(YType.enumeration, "multiplier-low")

                                self.threshold_high = YLeaf(YType.uint32, "threshold-high")

                                self.threshold_low = YLeaf(YType.uint32, "threshold-low")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("multiplier_high",
                                                "multiplier_low",
                                                "threshold_high",
                                                "threshold_low") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.Frame.Threshold, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.Frame.Threshold, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.multiplier_high.is_set or
                                    self.multiplier_low.is_set or
                                    self.threshold_high.is_set or
                                    self.threshold_low.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.multiplier_high.yfilter != YFilter.not_set or
                                    self.multiplier_low.yfilter != YFilter.not_set or
                                    self.threshold_high.yfilter != YFilter.not_set or
                                    self.threshold_low.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "threshold" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.multiplier_high.is_set or self.multiplier_high.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.multiplier_high.get_name_leafdata())
                                if (self.multiplier_low.is_set or self.multiplier_low.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.multiplier_low.get_name_leafdata())
                                if (self.threshold_high.is_set or self.threshold_high.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.threshold_high.get_name_leafdata())
                                if (self.threshold_low.is_set or self.threshold_low.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.threshold_low.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "multiplier-high" or name == "multiplier-low" or name == "threshold-high" or name == "threshold-low"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "multiplier-high"):
                                    self.multiplier_high = value
                                    self.multiplier_high.value_namespace = name_space
                                    self.multiplier_high.value_namespace_prefix = name_space_prefix
                                if(value_path == "multiplier-low"):
                                    self.multiplier_low = value
                                    self.multiplier_low.value_namespace = name_space
                                    self.multiplier_low.value_namespace_prefix = name_space_prefix
                                if(value_path == "threshold-high"):
                                    self.threshold_high = value
                                    self.threshold_high.value_namespace = name_space
                                    self.threshold_high.value_namespace_prefix = name_space_prefix
                                if(value_path == "threshold-low"):
                                    self.threshold_low = value
                                    self.threshold_low.value_namespace = name_space
                                    self.threshold_low.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                self.window.is_set or
                                (self.threshold is not None and self.threshold.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.window.yfilter != YFilter.not_set or
                                (self.threshold is not None and self.threshold.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "frame" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.window.is_set or self.window.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.window.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "threshold"):
                                if (self.threshold is None):
                                    self.threshold = EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.Frame.Threshold()
                                    self.threshold.parent = self
                                    self._children_name_map["threshold"] = "threshold"
                                return self.threshold

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "threshold" or name == "window"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "window"):
                                self.window = value
                                self.window.value_namespace = name_space
                                self.window.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.monitoring.is_set or
                            (self.frame is not None and self.frame.has_data()) or
                            (self.frame_period is not None and self.frame_period.has_data()) or
                            (self.frame_seconds is not None and self.frame_seconds.has_data()) or
                            (self.symbol_period is not None and self.symbol_period.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.monitoring.yfilter != YFilter.not_set or
                            (self.frame is not None and self.frame.has_operation()) or
                            (self.frame_period is not None and self.frame_period.has_operation()) or
                            (self.frame_seconds is not None and self.frame_seconds.has_operation()) or
                            (self.symbol_period is not None and self.symbol_period.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "link-monitoring" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.monitoring.is_set or self.monitoring.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.monitoring.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "frame"):
                            if (self.frame is None):
                                self.frame = EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.Frame()
                                self.frame.parent = self
                                self._children_name_map["frame"] = "frame"
                            return self.frame

                        if (child_yang_name == "frame-period"):
                            if (self.frame_period is None):
                                self.frame_period = EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.FramePeriod()
                                self.frame_period.parent = self
                                self._children_name_map["frame_period"] = "frame-period"
                            return self.frame_period

                        if (child_yang_name == "frame-seconds"):
                            if (self.frame_seconds is None):
                                self.frame_seconds = EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.FrameSeconds()
                                self.frame_seconds.parent = self
                                self._children_name_map["frame_seconds"] = "frame-seconds"
                            return self.frame_seconds

                        if (child_yang_name == "symbol-period"):
                            if (self.symbol_period is None):
                                self.symbol_period = EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring.SymbolPeriod()
                                self.symbol_period.parent = self
                                self._children_name_map["symbol_period"] = "symbol-period"
                            return self.symbol_period

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "frame" or name == "frame-period" or name == "frame-seconds" or name == "symbol-period" or name == "monitoring"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "monitoring"):
                            self.monitoring = value
                            self.monitoring.value_namespace = name_space
                            self.monitoring.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.profile.is_set or
                        self.hello_interval.is_set or
                        self.mib_retrieval.is_set or
                        self.mode.is_set or
                        self.remote_loopback.is_set or
                        self.timeout.is_set or
                        self.udlf.is_set or
                        (self.action is not None and self.action.has_data()) or
                        (self.link_monitoring is not None and self.link_monitoring.has_data()) or
                        (self.require_remote is not None and self.require_remote.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.profile.yfilter != YFilter.not_set or
                        self.hello_interval.yfilter != YFilter.not_set or
                        self.mib_retrieval.yfilter != YFilter.not_set or
                        self.mode.yfilter != YFilter.not_set or
                        self.remote_loopback.yfilter != YFilter.not_set or
                        self.timeout.yfilter != YFilter.not_set or
                        self.udlf.yfilter != YFilter.not_set or
                        (self.action is not None and self.action.has_operation()) or
                        (self.link_monitoring is not None and self.link_monitoring.has_operation()) or
                        (self.require_remote is not None and self.require_remote.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "profile" + "[profile='" + self.profile.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-l2-eth-infra-cfg:ethernet-features/Cisco-IOS-XR-ethernet-link-oam-cfg:ether-link-oam/profiles/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.profile.is_set or self.profile.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.profile.get_name_leafdata())
                    if (self.hello_interval.is_set or self.hello_interval.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.hello_interval.get_name_leafdata())
                    if (self.mib_retrieval.is_set or self.mib_retrieval.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.mib_retrieval.get_name_leafdata())
                    if (self.mode.is_set or self.mode.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.mode.get_name_leafdata())
                    if (self.remote_loopback.is_set or self.remote_loopback.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.remote_loopback.get_name_leafdata())
                    if (self.timeout.is_set or self.timeout.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.timeout.get_name_leafdata())
                    if (self.udlf.is_set or self.udlf.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.udlf.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "action"):
                        if (self.action is None):
                            self.action = EthernetFeatures.EtherLinkOam.Profiles.Profile.Action()
                            self.action.parent = self
                            self._children_name_map["action"] = "action"
                        return self.action

                    if (child_yang_name == "link-monitoring"):
                        if (self.link_monitoring is None):
                            self.link_monitoring = EthernetFeatures.EtherLinkOam.Profiles.Profile.LinkMonitoring()
                            self.link_monitoring.parent = self
                            self._children_name_map["link_monitoring"] = "link-monitoring"
                        return self.link_monitoring

                    if (child_yang_name == "require-remote"):
                        if (self.require_remote is None):
                            self.require_remote = EthernetFeatures.EtherLinkOam.Profiles.Profile.RequireRemote()
                            self.require_remote.parent = self
                            self._children_name_map["require_remote"] = "require-remote"
                        return self.require_remote

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "action" or name == "link-monitoring" or name == "require-remote" or name == "profile" or name == "hello-interval" or name == "mib-retrieval" or name == "mode" or name == "remote-loopback" or name == "timeout" or name == "udlf"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "profile"):
                        self.profile = value
                        self.profile.value_namespace = name_space
                        self.profile.value_namespace_prefix = name_space_prefix
                    if(value_path == "hello-interval"):
                        self.hello_interval = value
                        self.hello_interval.value_namespace = name_space
                        self.hello_interval.value_namespace_prefix = name_space_prefix
                    if(value_path == "mib-retrieval"):
                        self.mib_retrieval = value
                        self.mib_retrieval.value_namespace = name_space
                        self.mib_retrieval.value_namespace_prefix = name_space_prefix
                    if(value_path == "mode"):
                        self.mode = value
                        self.mode.value_namespace = name_space
                        self.mode.value_namespace_prefix = name_space_prefix
                    if(value_path == "remote-loopback"):
                        self.remote_loopback = value
                        self.remote_loopback.value_namespace = name_space
                        self.remote_loopback.value_namespace_prefix = name_space_prefix
                    if(value_path == "timeout"):
                        self.timeout = value
                        self.timeout.value_namespace = name_space
                        self.timeout.value_namespace_prefix = name_space_prefix
                    if(value_path == "udlf"):
                        self.udlf = value
                        self.udlf.value_namespace = name_space
                        self.udlf.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.profile:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.profile:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "profiles" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-l2-eth-infra-cfg:ethernet-features/Cisco-IOS-XR-ethernet-link-oam-cfg:ether-link-oam/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "profile"):
                    for c in self.profile:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = EthernetFeatures.EtherLinkOam.Profiles.Profile()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.profile.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "profile"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (self.profiles is not None and self.profiles.has_data())

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.profiles is not None and self.profiles.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "Cisco-IOS-XR-ethernet-link-oam-cfg:ether-link-oam" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-l2-eth-infra-cfg:ethernet-features/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "profiles"):
                if (self.profiles is None):
                    self.profiles = EthernetFeatures.EtherLinkOam.Profiles()
                    self.profiles.parent = self
                    self._children_name_map["profiles"] = "profiles"
                return self.profiles

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "profiles"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.cfm is not None and self.cfm.has_data()) or
            (self.egress_filtering is not None and self.egress_filtering.has_data()) or
            (self.ether_link_oam is not None and self.ether_link_oam.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.cfm is not None and self.cfm.has_operation()) or
            (self.egress_filtering is not None and self.egress_filtering.has_operation()) or
            (self.ether_link_oam is not None and self.ether_link_oam.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-l2-eth-infra-cfg:ethernet-features" + path_buffer

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

        if (child_yang_name == "cfm"):
            if (self.cfm is None):
                self.cfm = EthernetFeatures.Cfm()
                self.cfm.parent = self
                self._children_name_map["cfm"] = "cfm"
            return self.cfm

        if (child_yang_name == "egress-filtering"):
            if (self.egress_filtering is None):
                self.egress_filtering = EthernetFeatures.EgressFiltering()
                self.egress_filtering.parent = self
                self._children_name_map["egress_filtering"] = "egress-filtering"
            return self.egress_filtering

        if (child_yang_name == "ether-link-oam"):
            if (self.ether_link_oam is None):
                self.ether_link_oam = EthernetFeatures.EtherLinkOam()
                self.ether_link_oam.parent = self
                self._children_name_map["ether_link_oam"] = "ether-link-oam"
            return self.ether_link_oam

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "cfm" or name == "egress-filtering" or name == "ether-link-oam"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = EthernetFeatures()
        return self._top_entity

