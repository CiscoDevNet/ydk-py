""" Cisco_IOS_XR_ipv4_mfwd_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv4\-mfwd package configuration.

This module contains definitions
for the following management objects\:
  mfwd\: Multicast routing configuration

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class AccountingMode(Enum):
    """
    AccountingMode

    Accounting mode

    .. data:: enable = 0

    	Enable per (S,G) accounting

    .. data:: forward_only_enable = 1

    	Enable per (S,G) forward-only accounting

    """

    enable = Enum.YLeaf(0, "enable")

    forward_only_enable = Enum.YLeaf(1, "forward-only-enable")



class Mfwd(Entity):
    """
    Multicast routing configuration
    
    .. attribute:: default_context
    
    	Default Context
    	**type**\:   :py:class:`DefaultContext <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg.Mfwd.DefaultContext>`
    
    	**presence node**\: True
    
    .. attribute:: vrfs
    
    	VRF Table
    	**type**\:   :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg.Mfwd.Vrfs>`
    
    

    This class is a :ref:`presence class<presence-class>`

    """

    _prefix = 'ipv4-mfwd-cfg'
    _revision = '2016-06-01'

    def __init__(self):
        super(Mfwd, self).__init__()
        self._top_entity = None

        self.yang_name = "mfwd"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-mfwd-cfg"
        self.is_presence_container = True

        self.default_context = None
        self._children_name_map["default_context"] = "default-context"
        self._children_yang_names.add("default-context")

        self.vrfs = Mfwd.Vrfs()
        self.vrfs.parent = self
        self._children_name_map["vrfs"] = "vrfs"
        self._children_yang_names.add("vrfs")


    class DefaultContext(Entity):
        """
        Default Context
        
        .. attribute:: ipv4
        
        	IPV4 commands in the default context
        	**type**\:   :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg.Mfwd.DefaultContext.Ipv4>`
        
        .. attribute:: ipv6
        
        	IPV6 commands in the default context
        	**type**\:   :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg.Mfwd.DefaultContext.Ipv6>`
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'ipv4-mfwd-cfg'
        _revision = '2016-06-01'

        def __init__(self):
            super(Mfwd.DefaultContext, self).__init__()

            self.yang_name = "default-context"
            self.yang_parent_name = "mfwd"
            self.is_presence_container = True

            self.ipv4 = Mfwd.DefaultContext.Ipv4()
            self.ipv4.parent = self
            self._children_name_map["ipv4"] = "ipv4"
            self._children_yang_names.add("ipv4")

            self.ipv6 = Mfwd.DefaultContext.Ipv6()
            self.ipv6.parent = self
            self._children_name_map["ipv6"] = "ipv6"
            self._children_yang_names.add("ipv6")


        class Ipv6(Entity):
            """
            IPV6 commands in the default context
            
            .. attribute:: accounting
            
            	Per\-prefix accounting mode
            	**type**\:   :py:class:`AccountingMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg.AccountingMode>`
            
            .. attribute:: enable_on_all_interfaces
            
            	Configure all interfaces for multicast routing and forwarding
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: forwarding_latency
            
            	Knob to delay traffic being forwarded on a route
            	**type**\:  int
            
            	**range:** 5..500
            
            	**units**\: millisecond
            
            .. attribute:: interface_inheritance_disable
            
            	Disable interface inheritance configuration
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: interfaces
            
            	Interface\-level Configuration
            	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg.Mfwd.DefaultContext.Ipv6.Interfaces>`
            
            .. attribute:: log_traps
            
            	Enable logging trap event
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: maximum_checking_disable
            
            	Disable state limit maximum checking
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: mofrr_lockout_timer_config
            
            	Mofrr Lockout timer value
            	**type**\:  int
            
            	**range:** 1..3600
            
            .. attribute:: mofrr_loss_detection_timer_config
            
            	Mofrr Loss Detection timer value
            	**type**\:  int
            
            	**range:** 1..3600
            
            .. attribute:: multicast_forwarding
            
            	Enable IP multicast routing and forwarding
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: rate_per_route
            
            	Enable per (S,G) rate calculation
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: static_rpf_rules
            
            	Configure a static RPF rule for a given prefix
            	**type**\:   :py:class:`StaticRpfRules <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg.Mfwd.DefaultContext.Ipv6.StaticRpfRules>`
            
            

            """

            _prefix = 'ipv4-mfwd-cfg'
            _revision = '2016-06-01'

            def __init__(self):
                super(Mfwd.DefaultContext.Ipv6, self).__init__()

                self.yang_name = "ipv6"
                self.yang_parent_name = "default-context"

                self.accounting = YLeaf(YType.enumeration, "accounting")

                self.enable_on_all_interfaces = YLeaf(YType.empty, "enable-on-all-interfaces")

                self.forwarding_latency = YLeaf(YType.uint32, "forwarding-latency")

                self.interface_inheritance_disable = YLeaf(YType.empty, "interface-inheritance-disable")

                self.log_traps = YLeaf(YType.empty, "log-traps")

                self.maximum_checking_disable = YLeaf(YType.empty, "maximum-checking-disable")

                self.mofrr_lockout_timer_config = YLeaf(YType.uint32, "mofrr-lockout-timer-config")

                self.mofrr_loss_detection_timer_config = YLeaf(YType.uint32, "mofrr-loss-detection-timer-config")

                self.multicast_forwarding = YLeaf(YType.empty, "multicast-forwarding")

                self.rate_per_route = YLeaf(YType.empty, "rate-per-route")

                self.interfaces = Mfwd.DefaultContext.Ipv6.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"
                self._children_yang_names.add("interfaces")

                self.static_rpf_rules = Mfwd.DefaultContext.Ipv6.StaticRpfRules()
                self.static_rpf_rules.parent = self
                self._children_name_map["static_rpf_rules"] = "static-rpf-rules"
                self._children_yang_names.add("static-rpf-rules")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("accounting",
                                "enable_on_all_interfaces",
                                "forwarding_latency",
                                "interface_inheritance_disable",
                                "log_traps",
                                "maximum_checking_disable",
                                "mofrr_lockout_timer_config",
                                "mofrr_loss_detection_timer_config",
                                "multicast_forwarding",
                                "rate_per_route") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Mfwd.DefaultContext.Ipv6, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Mfwd.DefaultContext.Ipv6, self).__setattr__(name, value)


            class StaticRpfRules(Entity):
                """
                Configure a static RPF rule for a given prefix
                
                .. attribute:: static_rpf_rule
                
                	RPF prefix address and mask
                	**type**\: list of    :py:class:`StaticRpfRule <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg.Mfwd.DefaultContext.Ipv6.StaticRpfRules.StaticRpfRule>`
                
                

                """

                _prefix = 'ipv4-mfwd-cfg'
                _revision = '2016-06-01'

                def __init__(self):
                    super(Mfwd.DefaultContext.Ipv6.StaticRpfRules, self).__init__()

                    self.yang_name = "static-rpf-rules"
                    self.yang_parent_name = "ipv6"

                    self.static_rpf_rule = YList(self)

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
                                super(Mfwd.DefaultContext.Ipv6.StaticRpfRules, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Mfwd.DefaultContext.Ipv6.StaticRpfRules, self).__setattr__(name, value)


                class StaticRpfRule(Entity):
                    """
                    RPF prefix address and mask
                    
                    .. attribute:: address  <key>
                    
                    	IP address of the RPF prefix
                    	**type**\: one of the below types:
                    
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    .. attribute:: prefix_mask  <key>
                    
                    	Prefix mask of the RPF Prefix
                    	**type**\:  int
                    
                    	**range:** 0..128
                    
                    .. attribute:: interface_name
                    
                    	The name of the RPF interface
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    	**mandatory**\: True
                    
                    .. attribute:: neighbor_address
                    
                    	Neighbor address of the RPF Prefix
                    	**type**\: one of the below types:
                    
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    	**mandatory**\: True
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    	**mandatory**\: True
                    
                    
                    ----
                    

                    """

                    _prefix = 'ipv4-mfwd-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        super(Mfwd.DefaultContext.Ipv6.StaticRpfRules.StaticRpfRule, self).__init__()

                        self.yang_name = "static-rpf-rule"
                        self.yang_parent_name = "static-rpf-rules"

                        self.address = YLeaf(YType.str, "address")

                        self.prefix_mask = YLeaf(YType.uint32, "prefix-mask")

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.neighbor_address = YLeaf(YType.str, "neighbor-address")

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
                                        "prefix_mask",
                                        "interface_name",
                                        "neighbor_address") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Mfwd.DefaultContext.Ipv6.StaticRpfRules.StaticRpfRule, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Mfwd.DefaultContext.Ipv6.StaticRpfRules.StaticRpfRule, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.address.is_set or
                            self.prefix_mask.is_set or
                            self.interface_name.is_set or
                            self.neighbor_address.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.address.yfilter != YFilter.not_set or
                            self.prefix_mask.yfilter != YFilter.not_set or
                            self.interface_name.yfilter != YFilter.not_set or
                            self.neighbor_address.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "static-rpf-rule" + "[address='" + self.address.get() + "']" + "[prefix-mask='" + self.prefix_mask.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-ipv4-mfwd-cfg:mfwd/default-context/ipv6/static-rpf-rules/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.address.get_name_leafdata())
                        if (self.prefix_mask.is_set or self.prefix_mask.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.prefix_mask.get_name_leafdata())
                        if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_name.get_name_leafdata())
                        if (self.neighbor_address.is_set or self.neighbor_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.neighbor_address.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "address" or name == "prefix-mask" or name == "interface-name" or name == "neighbor-address"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "address"):
                            self.address = value
                            self.address.value_namespace = name_space
                            self.address.value_namespace_prefix = name_space_prefix
                        if(value_path == "prefix-mask"):
                            self.prefix_mask = value
                            self.prefix_mask.value_namespace = name_space
                            self.prefix_mask.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface-name"):
                            self.interface_name = value
                            self.interface_name.value_namespace = name_space
                            self.interface_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "neighbor-address"):
                            self.neighbor_address = value
                            self.neighbor_address.value_namespace = name_space
                            self.neighbor_address.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.static_rpf_rule:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.static_rpf_rule:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "static-rpf-rules" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ipv4-mfwd-cfg:mfwd/default-context/ipv6/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "static-rpf-rule"):
                        for c in self.static_rpf_rule:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Mfwd.DefaultContext.Ipv6.StaticRpfRules.StaticRpfRule()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.static_rpf_rule.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "static-rpf-rule"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Interfaces(Entity):
                """
                Interface\-level Configuration
                
                .. attribute:: interface
                
                	The name of the interface
                	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg.Mfwd.DefaultContext.Ipv6.Interfaces.Interface>`
                
                

                """

                _prefix = 'ipv4-mfwd-cfg'
                _revision = '2016-06-01'

                def __init__(self):
                    super(Mfwd.DefaultContext.Ipv6.Interfaces, self).__init__()

                    self.yang_name = "interfaces"
                    self.yang_parent_name = "ipv6"

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
                                super(Mfwd.DefaultContext.Ipv6.Interfaces, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Mfwd.DefaultContext.Ipv6.Interfaces, self).__setattr__(name, value)


                class Interface(Entity):
                    """
                    The name of the interface
                    
                    .. attribute:: interface_name  <key>
                    
                    	Interface name
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: boundary
                    
                    	Boundary for administratively scoped multicast addresses
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    .. attribute:: enable_on_interface
                    
                    	Enable or disable IP multicast on the interface
                    	**type**\:  bool
                    
                    .. attribute:: ttl_threshold
                    
                    	TTL threshold for multicast packets
                    	**type**\:  int
                    
                    	**range:** 1..255
                    
                    

                    """

                    _prefix = 'ipv4-mfwd-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        super(Mfwd.DefaultContext.Ipv6.Interfaces.Interface, self).__init__()

                        self.yang_name = "interface"
                        self.yang_parent_name = "interfaces"

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.boundary = YLeaf(YType.str, "boundary")

                        self.enable_on_interface = YLeaf(YType.boolean, "enable-on-interface")

                        self.ttl_threshold = YLeaf(YType.uint32, "ttl-threshold")

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
                                        "boundary",
                                        "enable_on_interface",
                                        "ttl_threshold") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Mfwd.DefaultContext.Ipv6.Interfaces.Interface, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Mfwd.DefaultContext.Ipv6.Interfaces.Interface, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.interface_name.is_set or
                            self.boundary.is_set or
                            self.enable_on_interface.is_set or
                            self.ttl_threshold.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.interface_name.yfilter != YFilter.not_set or
                            self.boundary.yfilter != YFilter.not_set or
                            self.enable_on_interface.yfilter != YFilter.not_set or
                            self.ttl_threshold.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "interface" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-ipv4-mfwd-cfg:mfwd/default-context/ipv6/interfaces/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_name.get_name_leafdata())
                        if (self.boundary.is_set or self.boundary.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.boundary.get_name_leafdata())
                        if (self.enable_on_interface.is_set or self.enable_on_interface.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.enable_on_interface.get_name_leafdata())
                        if (self.ttl_threshold.is_set or self.ttl_threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ttl_threshold.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "interface-name" or name == "boundary" or name == "enable-on-interface" or name == "ttl-threshold"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "interface-name"):
                            self.interface_name = value
                            self.interface_name.value_namespace = name_space
                            self.interface_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "boundary"):
                            self.boundary = value
                            self.boundary.value_namespace = name_space
                            self.boundary.value_namespace_prefix = name_space_prefix
                        if(value_path == "enable-on-interface"):
                            self.enable_on_interface = value
                            self.enable_on_interface.value_namespace = name_space
                            self.enable_on_interface.value_namespace_prefix = name_space_prefix
                        if(value_path == "ttl-threshold"):
                            self.ttl_threshold = value
                            self.ttl_threshold.value_namespace = name_space
                            self.ttl_threshold.value_namespace_prefix = name_space_prefix

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
                        path_buffer = "Cisco-IOS-XR-ipv4-mfwd-cfg:mfwd/default-context/ipv6/%s" % self.get_segment_path()
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
                        c = Mfwd.DefaultContext.Ipv6.Interfaces.Interface()
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

            def has_data(self):
                return (
                    self.accounting.is_set or
                    self.enable_on_all_interfaces.is_set or
                    self.forwarding_latency.is_set or
                    self.interface_inheritance_disable.is_set or
                    self.log_traps.is_set or
                    self.maximum_checking_disable.is_set or
                    self.mofrr_lockout_timer_config.is_set or
                    self.mofrr_loss_detection_timer_config.is_set or
                    self.multicast_forwarding.is_set or
                    self.rate_per_route.is_set or
                    (self.interfaces is not None and self.interfaces.has_data()) or
                    (self.static_rpf_rules is not None and self.static_rpf_rules.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.accounting.yfilter != YFilter.not_set or
                    self.enable_on_all_interfaces.yfilter != YFilter.not_set or
                    self.forwarding_latency.yfilter != YFilter.not_set or
                    self.interface_inheritance_disable.yfilter != YFilter.not_set or
                    self.log_traps.yfilter != YFilter.not_set or
                    self.maximum_checking_disable.yfilter != YFilter.not_set or
                    self.mofrr_lockout_timer_config.yfilter != YFilter.not_set or
                    self.mofrr_loss_detection_timer_config.yfilter != YFilter.not_set or
                    self.multicast_forwarding.yfilter != YFilter.not_set or
                    self.rate_per_route.yfilter != YFilter.not_set or
                    (self.interfaces is not None and self.interfaces.has_operation()) or
                    (self.static_rpf_rules is not None and self.static_rpf_rules.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ipv6" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ipv4-mfwd-cfg:mfwd/default-context/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.accounting.is_set or self.accounting.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.accounting.get_name_leafdata())
                if (self.enable_on_all_interfaces.is_set or self.enable_on_all_interfaces.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.enable_on_all_interfaces.get_name_leafdata())
                if (self.forwarding_latency.is_set or self.forwarding_latency.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.forwarding_latency.get_name_leafdata())
                if (self.interface_inheritance_disable.is_set or self.interface_inheritance_disable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.interface_inheritance_disable.get_name_leafdata())
                if (self.log_traps.is_set or self.log_traps.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.log_traps.get_name_leafdata())
                if (self.maximum_checking_disable.is_set or self.maximum_checking_disable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.maximum_checking_disable.get_name_leafdata())
                if (self.mofrr_lockout_timer_config.is_set or self.mofrr_lockout_timer_config.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mofrr_lockout_timer_config.get_name_leafdata())
                if (self.mofrr_loss_detection_timer_config.is_set or self.mofrr_loss_detection_timer_config.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mofrr_loss_detection_timer_config.get_name_leafdata())
                if (self.multicast_forwarding.is_set or self.multicast_forwarding.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.multicast_forwarding.get_name_leafdata())
                if (self.rate_per_route.is_set or self.rate_per_route.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rate_per_route.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "interfaces"):
                    if (self.interfaces is None):
                        self.interfaces = Mfwd.DefaultContext.Ipv6.Interfaces()
                        self.interfaces.parent = self
                        self._children_name_map["interfaces"] = "interfaces"
                    return self.interfaces

                if (child_yang_name == "static-rpf-rules"):
                    if (self.static_rpf_rules is None):
                        self.static_rpf_rules = Mfwd.DefaultContext.Ipv6.StaticRpfRules()
                        self.static_rpf_rules.parent = self
                        self._children_name_map["static_rpf_rules"] = "static-rpf-rules"
                    return self.static_rpf_rules

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "interfaces" or name == "static-rpf-rules" or name == "accounting" or name == "enable-on-all-interfaces" or name == "forwarding-latency" or name == "interface-inheritance-disable" or name == "log-traps" or name == "maximum-checking-disable" or name == "mofrr-lockout-timer-config" or name == "mofrr-loss-detection-timer-config" or name == "multicast-forwarding" or name == "rate-per-route"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "accounting"):
                    self.accounting = value
                    self.accounting.value_namespace = name_space
                    self.accounting.value_namespace_prefix = name_space_prefix
                if(value_path == "enable-on-all-interfaces"):
                    self.enable_on_all_interfaces = value
                    self.enable_on_all_interfaces.value_namespace = name_space
                    self.enable_on_all_interfaces.value_namespace_prefix = name_space_prefix
                if(value_path == "forwarding-latency"):
                    self.forwarding_latency = value
                    self.forwarding_latency.value_namespace = name_space
                    self.forwarding_latency.value_namespace_prefix = name_space_prefix
                if(value_path == "interface-inheritance-disable"):
                    self.interface_inheritance_disable = value
                    self.interface_inheritance_disable.value_namespace = name_space
                    self.interface_inheritance_disable.value_namespace_prefix = name_space_prefix
                if(value_path == "log-traps"):
                    self.log_traps = value
                    self.log_traps.value_namespace = name_space
                    self.log_traps.value_namespace_prefix = name_space_prefix
                if(value_path == "maximum-checking-disable"):
                    self.maximum_checking_disable = value
                    self.maximum_checking_disable.value_namespace = name_space
                    self.maximum_checking_disable.value_namespace_prefix = name_space_prefix
                if(value_path == "mofrr-lockout-timer-config"):
                    self.mofrr_lockout_timer_config = value
                    self.mofrr_lockout_timer_config.value_namespace = name_space
                    self.mofrr_lockout_timer_config.value_namespace_prefix = name_space_prefix
                if(value_path == "mofrr-loss-detection-timer-config"):
                    self.mofrr_loss_detection_timer_config = value
                    self.mofrr_loss_detection_timer_config.value_namespace = name_space
                    self.mofrr_loss_detection_timer_config.value_namespace_prefix = name_space_prefix
                if(value_path == "multicast-forwarding"):
                    self.multicast_forwarding = value
                    self.multicast_forwarding.value_namespace = name_space
                    self.multicast_forwarding.value_namespace_prefix = name_space_prefix
                if(value_path == "rate-per-route"):
                    self.rate_per_route = value
                    self.rate_per_route.value_namespace = name_space
                    self.rate_per_route.value_namespace_prefix = name_space_prefix


        class Ipv4(Entity):
            """
            IPV4 commands in the default context
            
            .. attribute:: accounting
            
            	Per\-prefix accounting mode
            	**type**\:   :py:class:`AccountingMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg.AccountingMode>`
            
            .. attribute:: enable_on_all_interfaces
            
            	Configure all interfaces for multicast routing and forwarding
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: forwarding_latency
            
            	Knob to delay traffic being forwarded on a route
            	**type**\:  int
            
            	**range:** 5..500
            
            	**units**\: millisecond
            
            .. attribute:: interface_inheritance_disable
            
            	Disable interface inheritance configuration
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: interfaces
            
            	Interface\-level Configuration
            	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg.Mfwd.DefaultContext.Ipv4.Interfaces>`
            
            .. attribute:: log_traps
            
            	Enable logging trap event
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: maximum_checking_disable
            
            	Disable state limit maximum checking
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: mofrr_lockout_timer_config
            
            	Mofrr Lockout timer value
            	**type**\:  int
            
            	**range:** 1..3600
            
            .. attribute:: mofrr_loss_detection_timer_config
            
            	Mofrr Loss Detection timer value
            	**type**\:  int
            
            	**range:** 1..3600
            
            .. attribute:: multicast_forwarding
            
            	Enable IP multicast routing and forwarding
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: out_of_memory_handling
            
            	Enable out\-of\-memory handling
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: rate_per_route
            
            	Enable per (S,G) rate calculation
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: static_rpf_rules
            
            	Configure a static RPF rule for a given prefix
            	**type**\:   :py:class:`StaticRpfRules <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg.Mfwd.DefaultContext.Ipv4.StaticRpfRules>`
            
            

            """

            _prefix = 'ipv4-mfwd-cfg'
            _revision = '2016-06-01'

            def __init__(self):
                super(Mfwd.DefaultContext.Ipv4, self).__init__()

                self.yang_name = "ipv4"
                self.yang_parent_name = "default-context"

                self.accounting = YLeaf(YType.enumeration, "accounting")

                self.enable_on_all_interfaces = YLeaf(YType.empty, "enable-on-all-interfaces")

                self.forwarding_latency = YLeaf(YType.uint32, "forwarding-latency")

                self.interface_inheritance_disable = YLeaf(YType.empty, "interface-inheritance-disable")

                self.log_traps = YLeaf(YType.empty, "log-traps")

                self.maximum_checking_disable = YLeaf(YType.empty, "maximum-checking-disable")

                self.mofrr_lockout_timer_config = YLeaf(YType.uint32, "mofrr-lockout-timer-config")

                self.mofrr_loss_detection_timer_config = YLeaf(YType.uint32, "mofrr-loss-detection-timer-config")

                self.multicast_forwarding = YLeaf(YType.empty, "multicast-forwarding")

                self.out_of_memory_handling = YLeaf(YType.empty, "out-of-memory-handling")

                self.rate_per_route = YLeaf(YType.empty, "rate-per-route")

                self.interfaces = Mfwd.DefaultContext.Ipv4.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"
                self._children_yang_names.add("interfaces")

                self.static_rpf_rules = Mfwd.DefaultContext.Ipv4.StaticRpfRules()
                self.static_rpf_rules.parent = self
                self._children_name_map["static_rpf_rules"] = "static-rpf-rules"
                self._children_yang_names.add("static-rpf-rules")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("accounting",
                                "enable_on_all_interfaces",
                                "forwarding_latency",
                                "interface_inheritance_disable",
                                "log_traps",
                                "maximum_checking_disable",
                                "mofrr_lockout_timer_config",
                                "mofrr_loss_detection_timer_config",
                                "multicast_forwarding",
                                "out_of_memory_handling",
                                "rate_per_route") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Mfwd.DefaultContext.Ipv4, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Mfwd.DefaultContext.Ipv4, self).__setattr__(name, value)


            class StaticRpfRules(Entity):
                """
                Configure a static RPF rule for a given prefix
                
                .. attribute:: static_rpf_rule
                
                	RPF prefix address and mask
                	**type**\: list of    :py:class:`StaticRpfRule <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg.Mfwd.DefaultContext.Ipv4.StaticRpfRules.StaticRpfRule>`
                
                

                """

                _prefix = 'ipv4-mfwd-cfg'
                _revision = '2016-06-01'

                def __init__(self):
                    super(Mfwd.DefaultContext.Ipv4.StaticRpfRules, self).__init__()

                    self.yang_name = "static-rpf-rules"
                    self.yang_parent_name = "ipv4"

                    self.static_rpf_rule = YList(self)

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
                                super(Mfwd.DefaultContext.Ipv4.StaticRpfRules, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Mfwd.DefaultContext.Ipv4.StaticRpfRules, self).__setattr__(name, value)


                class StaticRpfRule(Entity):
                    """
                    RPF prefix address and mask
                    
                    .. attribute:: address  <key>
                    
                    	IP address of the RPF prefix
                    	**type**\: one of the below types:
                    
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    .. attribute:: prefix_mask  <key>
                    
                    	Prefix mask of the RPF Prefix
                    	**type**\:  int
                    
                    	**range:** 0..128
                    
                    .. attribute:: interface_name
                    
                    	The name of the RPF interface
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    	**mandatory**\: True
                    
                    .. attribute:: neighbor_address
                    
                    	Neighbor address of the RPF Prefix
                    	**type**\: one of the below types:
                    
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    	**mandatory**\: True
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    	**mandatory**\: True
                    
                    
                    ----
                    

                    """

                    _prefix = 'ipv4-mfwd-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        super(Mfwd.DefaultContext.Ipv4.StaticRpfRules.StaticRpfRule, self).__init__()

                        self.yang_name = "static-rpf-rule"
                        self.yang_parent_name = "static-rpf-rules"

                        self.address = YLeaf(YType.str, "address")

                        self.prefix_mask = YLeaf(YType.uint32, "prefix-mask")

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.neighbor_address = YLeaf(YType.str, "neighbor-address")

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
                                        "prefix_mask",
                                        "interface_name",
                                        "neighbor_address") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Mfwd.DefaultContext.Ipv4.StaticRpfRules.StaticRpfRule, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Mfwd.DefaultContext.Ipv4.StaticRpfRules.StaticRpfRule, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.address.is_set or
                            self.prefix_mask.is_set or
                            self.interface_name.is_set or
                            self.neighbor_address.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.address.yfilter != YFilter.not_set or
                            self.prefix_mask.yfilter != YFilter.not_set or
                            self.interface_name.yfilter != YFilter.not_set or
                            self.neighbor_address.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "static-rpf-rule" + "[address='" + self.address.get() + "']" + "[prefix-mask='" + self.prefix_mask.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-ipv4-mfwd-cfg:mfwd/default-context/ipv4/static-rpf-rules/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.address.get_name_leafdata())
                        if (self.prefix_mask.is_set or self.prefix_mask.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.prefix_mask.get_name_leafdata())
                        if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_name.get_name_leafdata())
                        if (self.neighbor_address.is_set or self.neighbor_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.neighbor_address.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "address" or name == "prefix-mask" or name == "interface-name" or name == "neighbor-address"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "address"):
                            self.address = value
                            self.address.value_namespace = name_space
                            self.address.value_namespace_prefix = name_space_prefix
                        if(value_path == "prefix-mask"):
                            self.prefix_mask = value
                            self.prefix_mask.value_namespace = name_space
                            self.prefix_mask.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface-name"):
                            self.interface_name = value
                            self.interface_name.value_namespace = name_space
                            self.interface_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "neighbor-address"):
                            self.neighbor_address = value
                            self.neighbor_address.value_namespace = name_space
                            self.neighbor_address.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.static_rpf_rule:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.static_rpf_rule:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "static-rpf-rules" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ipv4-mfwd-cfg:mfwd/default-context/ipv4/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "static-rpf-rule"):
                        for c in self.static_rpf_rule:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Mfwd.DefaultContext.Ipv4.StaticRpfRules.StaticRpfRule()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.static_rpf_rule.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "static-rpf-rule"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Interfaces(Entity):
                """
                Interface\-level Configuration
                
                .. attribute:: interface
                
                	The name of the interface
                	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg.Mfwd.DefaultContext.Ipv4.Interfaces.Interface>`
                
                

                """

                _prefix = 'ipv4-mfwd-cfg'
                _revision = '2016-06-01'

                def __init__(self):
                    super(Mfwd.DefaultContext.Ipv4.Interfaces, self).__init__()

                    self.yang_name = "interfaces"
                    self.yang_parent_name = "ipv4"

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
                                super(Mfwd.DefaultContext.Ipv4.Interfaces, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Mfwd.DefaultContext.Ipv4.Interfaces, self).__setattr__(name, value)


                class Interface(Entity):
                    """
                    The name of the interface
                    
                    .. attribute:: interface_name  <key>
                    
                    	Interface name
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: boundary
                    
                    	Boundary for administratively scoped multicast addresses
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    .. attribute:: enable_on_interface
                    
                    	Enable or disable IP multicast on the interface
                    	**type**\:  bool
                    
                    .. attribute:: ttl_threshold
                    
                    	TTL threshold for multicast packets
                    	**type**\:  int
                    
                    	**range:** 1..255
                    
                    

                    """

                    _prefix = 'ipv4-mfwd-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        super(Mfwd.DefaultContext.Ipv4.Interfaces.Interface, self).__init__()

                        self.yang_name = "interface"
                        self.yang_parent_name = "interfaces"

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.boundary = YLeaf(YType.str, "boundary")

                        self.enable_on_interface = YLeaf(YType.boolean, "enable-on-interface")

                        self.ttl_threshold = YLeaf(YType.uint32, "ttl-threshold")

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
                                        "boundary",
                                        "enable_on_interface",
                                        "ttl_threshold") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Mfwd.DefaultContext.Ipv4.Interfaces.Interface, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Mfwd.DefaultContext.Ipv4.Interfaces.Interface, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.interface_name.is_set or
                            self.boundary.is_set or
                            self.enable_on_interface.is_set or
                            self.ttl_threshold.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.interface_name.yfilter != YFilter.not_set or
                            self.boundary.yfilter != YFilter.not_set or
                            self.enable_on_interface.yfilter != YFilter.not_set or
                            self.ttl_threshold.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "interface" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-ipv4-mfwd-cfg:mfwd/default-context/ipv4/interfaces/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_name.get_name_leafdata())
                        if (self.boundary.is_set or self.boundary.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.boundary.get_name_leafdata())
                        if (self.enable_on_interface.is_set or self.enable_on_interface.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.enable_on_interface.get_name_leafdata())
                        if (self.ttl_threshold.is_set or self.ttl_threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ttl_threshold.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "interface-name" or name == "boundary" or name == "enable-on-interface" or name == "ttl-threshold"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "interface-name"):
                            self.interface_name = value
                            self.interface_name.value_namespace = name_space
                            self.interface_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "boundary"):
                            self.boundary = value
                            self.boundary.value_namespace = name_space
                            self.boundary.value_namespace_prefix = name_space_prefix
                        if(value_path == "enable-on-interface"):
                            self.enable_on_interface = value
                            self.enable_on_interface.value_namespace = name_space
                            self.enable_on_interface.value_namespace_prefix = name_space_prefix
                        if(value_path == "ttl-threshold"):
                            self.ttl_threshold = value
                            self.ttl_threshold.value_namespace = name_space
                            self.ttl_threshold.value_namespace_prefix = name_space_prefix

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
                        path_buffer = "Cisco-IOS-XR-ipv4-mfwd-cfg:mfwd/default-context/ipv4/%s" % self.get_segment_path()
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
                        c = Mfwd.DefaultContext.Ipv4.Interfaces.Interface()
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

            def has_data(self):
                return (
                    self.accounting.is_set or
                    self.enable_on_all_interfaces.is_set or
                    self.forwarding_latency.is_set or
                    self.interface_inheritance_disable.is_set or
                    self.log_traps.is_set or
                    self.maximum_checking_disable.is_set or
                    self.mofrr_lockout_timer_config.is_set or
                    self.mofrr_loss_detection_timer_config.is_set or
                    self.multicast_forwarding.is_set or
                    self.out_of_memory_handling.is_set or
                    self.rate_per_route.is_set or
                    (self.interfaces is not None and self.interfaces.has_data()) or
                    (self.static_rpf_rules is not None and self.static_rpf_rules.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.accounting.yfilter != YFilter.not_set or
                    self.enable_on_all_interfaces.yfilter != YFilter.not_set or
                    self.forwarding_latency.yfilter != YFilter.not_set or
                    self.interface_inheritance_disable.yfilter != YFilter.not_set or
                    self.log_traps.yfilter != YFilter.not_set or
                    self.maximum_checking_disable.yfilter != YFilter.not_set or
                    self.mofrr_lockout_timer_config.yfilter != YFilter.not_set or
                    self.mofrr_loss_detection_timer_config.yfilter != YFilter.not_set or
                    self.multicast_forwarding.yfilter != YFilter.not_set or
                    self.out_of_memory_handling.yfilter != YFilter.not_set or
                    self.rate_per_route.yfilter != YFilter.not_set or
                    (self.interfaces is not None and self.interfaces.has_operation()) or
                    (self.static_rpf_rules is not None and self.static_rpf_rules.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ipv4" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ipv4-mfwd-cfg:mfwd/default-context/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.accounting.is_set or self.accounting.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.accounting.get_name_leafdata())
                if (self.enable_on_all_interfaces.is_set or self.enable_on_all_interfaces.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.enable_on_all_interfaces.get_name_leafdata())
                if (self.forwarding_latency.is_set or self.forwarding_latency.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.forwarding_latency.get_name_leafdata())
                if (self.interface_inheritance_disable.is_set or self.interface_inheritance_disable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.interface_inheritance_disable.get_name_leafdata())
                if (self.log_traps.is_set or self.log_traps.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.log_traps.get_name_leafdata())
                if (self.maximum_checking_disable.is_set or self.maximum_checking_disable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.maximum_checking_disable.get_name_leafdata())
                if (self.mofrr_lockout_timer_config.is_set or self.mofrr_lockout_timer_config.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mofrr_lockout_timer_config.get_name_leafdata())
                if (self.mofrr_loss_detection_timer_config.is_set or self.mofrr_loss_detection_timer_config.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mofrr_loss_detection_timer_config.get_name_leafdata())
                if (self.multicast_forwarding.is_set or self.multicast_forwarding.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.multicast_forwarding.get_name_leafdata())
                if (self.out_of_memory_handling.is_set or self.out_of_memory_handling.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.out_of_memory_handling.get_name_leafdata())
                if (self.rate_per_route.is_set or self.rate_per_route.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rate_per_route.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "interfaces"):
                    if (self.interfaces is None):
                        self.interfaces = Mfwd.DefaultContext.Ipv4.Interfaces()
                        self.interfaces.parent = self
                        self._children_name_map["interfaces"] = "interfaces"
                    return self.interfaces

                if (child_yang_name == "static-rpf-rules"):
                    if (self.static_rpf_rules is None):
                        self.static_rpf_rules = Mfwd.DefaultContext.Ipv4.StaticRpfRules()
                        self.static_rpf_rules.parent = self
                        self._children_name_map["static_rpf_rules"] = "static-rpf-rules"
                    return self.static_rpf_rules

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "interfaces" or name == "static-rpf-rules" or name == "accounting" or name == "enable-on-all-interfaces" or name == "forwarding-latency" or name == "interface-inheritance-disable" or name == "log-traps" or name == "maximum-checking-disable" or name == "mofrr-lockout-timer-config" or name == "mofrr-loss-detection-timer-config" or name == "multicast-forwarding" or name == "out-of-memory-handling" or name == "rate-per-route"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "accounting"):
                    self.accounting = value
                    self.accounting.value_namespace = name_space
                    self.accounting.value_namespace_prefix = name_space_prefix
                if(value_path == "enable-on-all-interfaces"):
                    self.enable_on_all_interfaces = value
                    self.enable_on_all_interfaces.value_namespace = name_space
                    self.enable_on_all_interfaces.value_namespace_prefix = name_space_prefix
                if(value_path == "forwarding-latency"):
                    self.forwarding_latency = value
                    self.forwarding_latency.value_namespace = name_space
                    self.forwarding_latency.value_namespace_prefix = name_space_prefix
                if(value_path == "interface-inheritance-disable"):
                    self.interface_inheritance_disable = value
                    self.interface_inheritance_disable.value_namespace = name_space
                    self.interface_inheritance_disable.value_namespace_prefix = name_space_prefix
                if(value_path == "log-traps"):
                    self.log_traps = value
                    self.log_traps.value_namespace = name_space
                    self.log_traps.value_namespace_prefix = name_space_prefix
                if(value_path == "maximum-checking-disable"):
                    self.maximum_checking_disable = value
                    self.maximum_checking_disable.value_namespace = name_space
                    self.maximum_checking_disable.value_namespace_prefix = name_space_prefix
                if(value_path == "mofrr-lockout-timer-config"):
                    self.mofrr_lockout_timer_config = value
                    self.mofrr_lockout_timer_config.value_namespace = name_space
                    self.mofrr_lockout_timer_config.value_namespace_prefix = name_space_prefix
                if(value_path == "mofrr-loss-detection-timer-config"):
                    self.mofrr_loss_detection_timer_config = value
                    self.mofrr_loss_detection_timer_config.value_namespace = name_space
                    self.mofrr_loss_detection_timer_config.value_namespace_prefix = name_space_prefix
                if(value_path == "multicast-forwarding"):
                    self.multicast_forwarding = value
                    self.multicast_forwarding.value_namespace = name_space
                    self.multicast_forwarding.value_namespace_prefix = name_space_prefix
                if(value_path == "out-of-memory-handling"):
                    self.out_of_memory_handling = value
                    self.out_of_memory_handling.value_namespace = name_space
                    self.out_of_memory_handling.value_namespace_prefix = name_space_prefix
                if(value_path == "rate-per-route"):
                    self.rate_per_route = value
                    self.rate_per_route.value_namespace = name_space
                    self.rate_per_route.value_namespace_prefix = name_space_prefix

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
            path_buffer = "default-context" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ipv4-mfwd-cfg:mfwd/%s" % self.get_segment_path()
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
                    self.ipv4 = Mfwd.DefaultContext.Ipv4()
                    self.ipv4.parent = self
                    self._children_name_map["ipv4"] = "ipv4"
                return self.ipv4

            if (child_yang_name == "ipv6"):
                if (self.ipv6 is None):
                    self.ipv6 = Mfwd.DefaultContext.Ipv6()
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


    class Vrfs(Entity):
        """
        VRF Table
        
        .. attribute:: vrf
        
        	VRF table names
        	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg.Mfwd.Vrfs.Vrf>`
        
        

        """

        _prefix = 'ipv4-mfwd-cfg'
        _revision = '2016-06-01'

        def __init__(self):
            super(Mfwd.Vrfs, self).__init__()

            self.yang_name = "vrfs"
            self.yang_parent_name = "mfwd"

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
                        super(Mfwd.Vrfs, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Mfwd.Vrfs, self).__setattr__(name, value)


        class Vrf(Entity):
            """
            VRF table names
            
            .. attribute:: vrf_name  <key>
            
            	VRF Name
            	**type**\:  str
            
            	**length:** 1..32
            
            .. attribute:: ipv4
            
            	VRF table for IPV4 commands
            	**type**\:   :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg.Mfwd.Vrfs.Vrf.Ipv4>`
            
            .. attribute:: ipv6
            
            	VRF table for IPV6 commands
            	**type**\:   :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg.Mfwd.Vrfs.Vrf.Ipv6>`
            
            

            """

            _prefix = 'ipv4-mfwd-cfg'
            _revision = '2016-06-01'

            def __init__(self):
                super(Mfwd.Vrfs.Vrf, self).__init__()

                self.yang_name = "vrf"
                self.yang_parent_name = "vrfs"

                self.vrf_name = YLeaf(YType.str, "vrf-name")

                self.ipv4 = Mfwd.Vrfs.Vrf.Ipv4()
                self.ipv4.parent = self
                self._children_name_map["ipv4"] = "ipv4"
                self._children_yang_names.add("ipv4")

                self.ipv6 = Mfwd.Vrfs.Vrf.Ipv6()
                self.ipv6.parent = self
                self._children_name_map["ipv6"] = "ipv6"
                self._children_yang_names.add("ipv6")

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
                            super(Mfwd.Vrfs.Vrf, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Mfwd.Vrfs.Vrf, self).__setattr__(name, value)


            class Ipv6(Entity):
                """
                VRF table for IPV6 commands
                
                .. attribute:: accounting
                
                	Per\-prefix accounting mode
                	**type**\:   :py:class:`AccountingMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg.AccountingMode>`
                
                .. attribute:: enable_on_all_interfaces
                
                	Configure all interfaces for multicast routing and forwarding
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: interfaces
                
                	Interface\-level Configuration
                	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg.Mfwd.Vrfs.Vrf.Ipv6.Interfaces>`
                
                .. attribute:: log_traps
                
                	Enable logging trap event
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: multicast_forwarding
                
                	Enable IP multicast routing and forwarding
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: rate_per_route
                
                	Enable per (S,G) rate calculation
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: static_rpf_rules
                
                	Configure a static RPF rule for a given prefix
                	**type**\:   :py:class:`StaticRpfRules <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg.Mfwd.Vrfs.Vrf.Ipv6.StaticRpfRules>`
                
                

                """

                _prefix = 'ipv4-mfwd-cfg'
                _revision = '2016-06-01'

                def __init__(self):
                    super(Mfwd.Vrfs.Vrf.Ipv6, self).__init__()

                    self.yang_name = "ipv6"
                    self.yang_parent_name = "vrf"

                    self.accounting = YLeaf(YType.enumeration, "accounting")

                    self.enable_on_all_interfaces = YLeaf(YType.empty, "enable-on-all-interfaces")

                    self.log_traps = YLeaf(YType.empty, "log-traps")

                    self.multicast_forwarding = YLeaf(YType.empty, "multicast-forwarding")

                    self.rate_per_route = YLeaf(YType.empty, "rate-per-route")

                    self.interfaces = Mfwd.Vrfs.Vrf.Ipv6.Interfaces()
                    self.interfaces.parent = self
                    self._children_name_map["interfaces"] = "interfaces"
                    self._children_yang_names.add("interfaces")

                    self.static_rpf_rules = Mfwd.Vrfs.Vrf.Ipv6.StaticRpfRules()
                    self.static_rpf_rules.parent = self
                    self._children_name_map["static_rpf_rules"] = "static-rpf-rules"
                    self._children_yang_names.add("static-rpf-rules")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("accounting",
                                    "enable_on_all_interfaces",
                                    "log_traps",
                                    "multicast_forwarding",
                                    "rate_per_route") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Mfwd.Vrfs.Vrf.Ipv6, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Mfwd.Vrfs.Vrf.Ipv6, self).__setattr__(name, value)


                class StaticRpfRules(Entity):
                    """
                    Configure a static RPF rule for a given prefix
                    
                    .. attribute:: static_rpf_rule
                    
                    	RPF prefix address and mask
                    	**type**\: list of    :py:class:`StaticRpfRule <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg.Mfwd.Vrfs.Vrf.Ipv6.StaticRpfRules.StaticRpfRule>`
                    
                    

                    """

                    _prefix = 'ipv4-mfwd-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        super(Mfwd.Vrfs.Vrf.Ipv6.StaticRpfRules, self).__init__()

                        self.yang_name = "static-rpf-rules"
                        self.yang_parent_name = "ipv6"

                        self.static_rpf_rule = YList(self)

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
                                    super(Mfwd.Vrfs.Vrf.Ipv6.StaticRpfRules, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Mfwd.Vrfs.Vrf.Ipv6.StaticRpfRules, self).__setattr__(name, value)


                    class StaticRpfRule(Entity):
                        """
                        RPF prefix address and mask
                        
                        .. attribute:: address  <key>
                        
                        	IP address of the RPF prefix
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: prefix_mask  <key>
                        
                        	Prefix mask of the RPF Prefix
                        	**type**\:  int
                        
                        	**range:** 0..128
                        
                        .. attribute:: interface_name
                        
                        	The name of the RPF interface
                        	**type**\:  str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        	**mandatory**\: True
                        
                        .. attribute:: neighbor_address
                        
                        	Neighbor address of the RPF Prefix
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        	**mandatory**\: True
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        	**mandatory**\: True
                        
                        
                        ----
                        

                        """

                        _prefix = 'ipv4-mfwd-cfg'
                        _revision = '2016-06-01'

                        def __init__(self):
                            super(Mfwd.Vrfs.Vrf.Ipv6.StaticRpfRules.StaticRpfRule, self).__init__()

                            self.yang_name = "static-rpf-rule"
                            self.yang_parent_name = "static-rpf-rules"

                            self.address = YLeaf(YType.str, "address")

                            self.prefix_mask = YLeaf(YType.uint32, "prefix-mask")

                            self.interface_name = YLeaf(YType.str, "interface-name")

                            self.neighbor_address = YLeaf(YType.str, "neighbor-address")

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
                                            "prefix_mask",
                                            "interface_name",
                                            "neighbor_address") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Mfwd.Vrfs.Vrf.Ipv6.StaticRpfRules.StaticRpfRule, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Mfwd.Vrfs.Vrf.Ipv6.StaticRpfRules.StaticRpfRule, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.address.is_set or
                                self.prefix_mask.is_set or
                                self.interface_name.is_set or
                                self.neighbor_address.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.address.yfilter != YFilter.not_set or
                                self.prefix_mask.yfilter != YFilter.not_set or
                                self.interface_name.yfilter != YFilter.not_set or
                                self.neighbor_address.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "static-rpf-rule" + "[address='" + self.address.get() + "']" + "[prefix-mask='" + self.prefix_mask.get() + "']" + path_buffer

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
                            if (self.prefix_mask.is_set or self.prefix_mask.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.prefix_mask.get_name_leafdata())
                            if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.interface_name.get_name_leafdata())
                            if (self.neighbor_address.is_set or self.neighbor_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.neighbor_address.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "address" or name == "prefix-mask" or name == "interface-name" or name == "neighbor-address"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "address"):
                                self.address = value
                                self.address.value_namespace = name_space
                                self.address.value_namespace_prefix = name_space_prefix
                            if(value_path == "prefix-mask"):
                                self.prefix_mask = value
                                self.prefix_mask.value_namespace = name_space
                                self.prefix_mask.value_namespace_prefix = name_space_prefix
                            if(value_path == "interface-name"):
                                self.interface_name = value
                                self.interface_name.value_namespace = name_space
                                self.interface_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "neighbor-address"):
                                self.neighbor_address = value
                                self.neighbor_address.value_namespace = name_space
                                self.neighbor_address.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.static_rpf_rule:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.static_rpf_rule:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "static-rpf-rules" + path_buffer

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

                        if (child_yang_name == "static-rpf-rule"):
                            for c in self.static_rpf_rule:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Mfwd.Vrfs.Vrf.Ipv6.StaticRpfRules.StaticRpfRule()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.static_rpf_rule.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "static-rpf-rule"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class Interfaces(Entity):
                    """
                    Interface\-level Configuration
                    
                    .. attribute:: interface
                    
                    	The name of the interface
                    	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg.Mfwd.Vrfs.Vrf.Ipv6.Interfaces.Interface>`
                    
                    

                    """

                    _prefix = 'ipv4-mfwd-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        super(Mfwd.Vrfs.Vrf.Ipv6.Interfaces, self).__init__()

                        self.yang_name = "interfaces"
                        self.yang_parent_name = "ipv6"

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
                                    super(Mfwd.Vrfs.Vrf.Ipv6.Interfaces, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Mfwd.Vrfs.Vrf.Ipv6.Interfaces, self).__setattr__(name, value)


                    class Interface(Entity):
                        """
                        The name of the interface
                        
                        .. attribute:: interface_name  <key>
                        
                        	Interface name
                        	**type**\:  str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        .. attribute:: boundary
                        
                        	Boundary for administratively scoped multicast addresses
                        	**type**\:  str
                        
                        	**length:** 1..64
                        
                        .. attribute:: enable_on_interface
                        
                        	Enable or disable IP multicast on the interface
                        	**type**\:  bool
                        
                        .. attribute:: ttl_threshold
                        
                        	TTL threshold for multicast packets
                        	**type**\:  int
                        
                        	**range:** 1..255
                        
                        

                        """

                        _prefix = 'ipv4-mfwd-cfg'
                        _revision = '2016-06-01'

                        def __init__(self):
                            super(Mfwd.Vrfs.Vrf.Ipv6.Interfaces.Interface, self).__init__()

                            self.yang_name = "interface"
                            self.yang_parent_name = "interfaces"

                            self.interface_name = YLeaf(YType.str, "interface-name")

                            self.boundary = YLeaf(YType.str, "boundary")

                            self.enable_on_interface = YLeaf(YType.boolean, "enable-on-interface")

                            self.ttl_threshold = YLeaf(YType.uint32, "ttl-threshold")

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
                                            "boundary",
                                            "enable_on_interface",
                                            "ttl_threshold") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Mfwd.Vrfs.Vrf.Ipv6.Interfaces.Interface, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Mfwd.Vrfs.Vrf.Ipv6.Interfaces.Interface, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.interface_name.is_set or
                                self.boundary.is_set or
                                self.enable_on_interface.is_set or
                                self.ttl_threshold.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.interface_name.yfilter != YFilter.not_set or
                                self.boundary.yfilter != YFilter.not_set or
                                self.enable_on_interface.yfilter != YFilter.not_set or
                                self.ttl_threshold.yfilter != YFilter.not_set)

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
                            if (self.boundary.is_set or self.boundary.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.boundary.get_name_leafdata())
                            if (self.enable_on_interface.is_set or self.enable_on_interface.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.enable_on_interface.get_name_leafdata())
                            if (self.ttl_threshold.is_set or self.ttl_threshold.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ttl_threshold.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "interface-name" or name == "boundary" or name == "enable-on-interface" or name == "ttl-threshold"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "interface-name"):
                                self.interface_name = value
                                self.interface_name.value_namespace = name_space
                                self.interface_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "boundary"):
                                self.boundary = value
                                self.boundary.value_namespace = name_space
                                self.boundary.value_namespace_prefix = name_space_prefix
                            if(value_path == "enable-on-interface"):
                                self.enable_on_interface = value
                                self.enable_on_interface.value_namespace = name_space
                                self.enable_on_interface.value_namespace_prefix = name_space_prefix
                            if(value_path == "ttl-threshold"):
                                self.ttl_threshold = value
                                self.ttl_threshold.value_namespace = name_space
                                self.ttl_threshold.value_namespace_prefix = name_space_prefix

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
                            c = Mfwd.Vrfs.Vrf.Ipv6.Interfaces.Interface()
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

                def has_data(self):
                    return (
                        self.accounting.is_set or
                        self.enable_on_all_interfaces.is_set or
                        self.log_traps.is_set or
                        self.multicast_forwarding.is_set or
                        self.rate_per_route.is_set or
                        (self.interfaces is not None and self.interfaces.has_data()) or
                        (self.static_rpf_rules is not None and self.static_rpf_rules.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.accounting.yfilter != YFilter.not_set or
                        self.enable_on_all_interfaces.yfilter != YFilter.not_set or
                        self.log_traps.yfilter != YFilter.not_set or
                        self.multicast_forwarding.yfilter != YFilter.not_set or
                        self.rate_per_route.yfilter != YFilter.not_set or
                        (self.interfaces is not None and self.interfaces.has_operation()) or
                        (self.static_rpf_rules is not None and self.static_rpf_rules.has_operation()))

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
                    if (self.accounting.is_set or self.accounting.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.accounting.get_name_leafdata())
                    if (self.enable_on_all_interfaces.is_set or self.enable_on_all_interfaces.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.enable_on_all_interfaces.get_name_leafdata())
                    if (self.log_traps.is_set or self.log_traps.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.log_traps.get_name_leafdata())
                    if (self.multicast_forwarding.is_set or self.multicast_forwarding.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.multicast_forwarding.get_name_leafdata())
                    if (self.rate_per_route.is_set or self.rate_per_route.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rate_per_route.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "interfaces"):
                        if (self.interfaces is None):
                            self.interfaces = Mfwd.Vrfs.Vrf.Ipv6.Interfaces()
                            self.interfaces.parent = self
                            self._children_name_map["interfaces"] = "interfaces"
                        return self.interfaces

                    if (child_yang_name == "static-rpf-rules"):
                        if (self.static_rpf_rules is None):
                            self.static_rpf_rules = Mfwd.Vrfs.Vrf.Ipv6.StaticRpfRules()
                            self.static_rpf_rules.parent = self
                            self._children_name_map["static_rpf_rules"] = "static-rpf-rules"
                        return self.static_rpf_rules

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "interfaces" or name == "static-rpf-rules" or name == "accounting" or name == "enable-on-all-interfaces" or name == "log-traps" or name == "multicast-forwarding" or name == "rate-per-route"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "accounting"):
                        self.accounting = value
                        self.accounting.value_namespace = name_space
                        self.accounting.value_namespace_prefix = name_space_prefix
                    if(value_path == "enable-on-all-interfaces"):
                        self.enable_on_all_interfaces = value
                        self.enable_on_all_interfaces.value_namespace = name_space
                        self.enable_on_all_interfaces.value_namespace_prefix = name_space_prefix
                    if(value_path == "log-traps"):
                        self.log_traps = value
                        self.log_traps.value_namespace = name_space
                        self.log_traps.value_namespace_prefix = name_space_prefix
                    if(value_path == "multicast-forwarding"):
                        self.multicast_forwarding = value
                        self.multicast_forwarding.value_namespace = name_space
                        self.multicast_forwarding.value_namespace_prefix = name_space_prefix
                    if(value_path == "rate-per-route"):
                        self.rate_per_route = value
                        self.rate_per_route.value_namespace = name_space
                        self.rate_per_route.value_namespace_prefix = name_space_prefix


            class Ipv4(Entity):
                """
                VRF table for IPV4 commands
                
                .. attribute:: accounting
                
                	Per\-prefix accounting mode
                	**type**\:   :py:class:`AccountingMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg.AccountingMode>`
                
                .. attribute:: enable_on_all_interfaces
                
                	Configure all interfaces for multicast routing and forwarding
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: interfaces
                
                	Interface\-level Configuration
                	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg.Mfwd.Vrfs.Vrf.Ipv4.Interfaces>`
                
                .. attribute:: log_traps
                
                	Enable logging trap event
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: multicast_forwarding
                
                	Enable IP multicast routing and forwarding
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: rate_per_route
                
                	Enable per (S,G) rate calculation
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: static_rpf_rules
                
                	Configure a static RPF rule for a given prefix
                	**type**\:   :py:class:`StaticRpfRules <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg.Mfwd.Vrfs.Vrf.Ipv4.StaticRpfRules>`
                
                

                """

                _prefix = 'ipv4-mfwd-cfg'
                _revision = '2016-06-01'

                def __init__(self):
                    super(Mfwd.Vrfs.Vrf.Ipv4, self).__init__()

                    self.yang_name = "ipv4"
                    self.yang_parent_name = "vrf"

                    self.accounting = YLeaf(YType.enumeration, "accounting")

                    self.enable_on_all_interfaces = YLeaf(YType.empty, "enable-on-all-interfaces")

                    self.log_traps = YLeaf(YType.empty, "log-traps")

                    self.multicast_forwarding = YLeaf(YType.empty, "multicast-forwarding")

                    self.rate_per_route = YLeaf(YType.empty, "rate-per-route")

                    self.interfaces = Mfwd.Vrfs.Vrf.Ipv4.Interfaces()
                    self.interfaces.parent = self
                    self._children_name_map["interfaces"] = "interfaces"
                    self._children_yang_names.add("interfaces")

                    self.static_rpf_rules = Mfwd.Vrfs.Vrf.Ipv4.StaticRpfRules()
                    self.static_rpf_rules.parent = self
                    self._children_name_map["static_rpf_rules"] = "static-rpf-rules"
                    self._children_yang_names.add("static-rpf-rules")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("accounting",
                                    "enable_on_all_interfaces",
                                    "log_traps",
                                    "multicast_forwarding",
                                    "rate_per_route") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Mfwd.Vrfs.Vrf.Ipv4, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Mfwd.Vrfs.Vrf.Ipv4, self).__setattr__(name, value)


                class StaticRpfRules(Entity):
                    """
                    Configure a static RPF rule for a given prefix
                    
                    .. attribute:: static_rpf_rule
                    
                    	RPF prefix address and mask
                    	**type**\: list of    :py:class:`StaticRpfRule <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg.Mfwd.Vrfs.Vrf.Ipv4.StaticRpfRules.StaticRpfRule>`
                    
                    

                    """

                    _prefix = 'ipv4-mfwd-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        super(Mfwd.Vrfs.Vrf.Ipv4.StaticRpfRules, self).__init__()

                        self.yang_name = "static-rpf-rules"
                        self.yang_parent_name = "ipv4"

                        self.static_rpf_rule = YList(self)

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
                                    super(Mfwd.Vrfs.Vrf.Ipv4.StaticRpfRules, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Mfwd.Vrfs.Vrf.Ipv4.StaticRpfRules, self).__setattr__(name, value)


                    class StaticRpfRule(Entity):
                        """
                        RPF prefix address and mask
                        
                        .. attribute:: address  <key>
                        
                        	IP address of the RPF prefix
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: prefix_mask  <key>
                        
                        	Prefix mask of the RPF Prefix
                        	**type**\:  int
                        
                        	**range:** 0..128
                        
                        .. attribute:: interface_name
                        
                        	The name of the RPF interface
                        	**type**\:  str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        	**mandatory**\: True
                        
                        .. attribute:: neighbor_address
                        
                        	Neighbor address of the RPF Prefix
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        	**mandatory**\: True
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        	**mandatory**\: True
                        
                        
                        ----
                        

                        """

                        _prefix = 'ipv4-mfwd-cfg'
                        _revision = '2016-06-01'

                        def __init__(self):
                            super(Mfwd.Vrfs.Vrf.Ipv4.StaticRpfRules.StaticRpfRule, self).__init__()

                            self.yang_name = "static-rpf-rule"
                            self.yang_parent_name = "static-rpf-rules"

                            self.address = YLeaf(YType.str, "address")

                            self.prefix_mask = YLeaf(YType.uint32, "prefix-mask")

                            self.interface_name = YLeaf(YType.str, "interface-name")

                            self.neighbor_address = YLeaf(YType.str, "neighbor-address")

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
                                            "prefix_mask",
                                            "interface_name",
                                            "neighbor_address") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Mfwd.Vrfs.Vrf.Ipv4.StaticRpfRules.StaticRpfRule, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Mfwd.Vrfs.Vrf.Ipv4.StaticRpfRules.StaticRpfRule, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.address.is_set or
                                self.prefix_mask.is_set or
                                self.interface_name.is_set or
                                self.neighbor_address.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.address.yfilter != YFilter.not_set or
                                self.prefix_mask.yfilter != YFilter.not_set or
                                self.interface_name.yfilter != YFilter.not_set or
                                self.neighbor_address.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "static-rpf-rule" + "[address='" + self.address.get() + "']" + "[prefix-mask='" + self.prefix_mask.get() + "']" + path_buffer

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
                            if (self.prefix_mask.is_set or self.prefix_mask.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.prefix_mask.get_name_leafdata())
                            if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.interface_name.get_name_leafdata())
                            if (self.neighbor_address.is_set or self.neighbor_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.neighbor_address.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "address" or name == "prefix-mask" or name == "interface-name" or name == "neighbor-address"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "address"):
                                self.address = value
                                self.address.value_namespace = name_space
                                self.address.value_namespace_prefix = name_space_prefix
                            if(value_path == "prefix-mask"):
                                self.prefix_mask = value
                                self.prefix_mask.value_namespace = name_space
                                self.prefix_mask.value_namespace_prefix = name_space_prefix
                            if(value_path == "interface-name"):
                                self.interface_name = value
                                self.interface_name.value_namespace = name_space
                                self.interface_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "neighbor-address"):
                                self.neighbor_address = value
                                self.neighbor_address.value_namespace = name_space
                                self.neighbor_address.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.static_rpf_rule:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.static_rpf_rule:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "static-rpf-rules" + path_buffer

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

                        if (child_yang_name == "static-rpf-rule"):
                            for c in self.static_rpf_rule:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Mfwd.Vrfs.Vrf.Ipv4.StaticRpfRules.StaticRpfRule()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.static_rpf_rule.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "static-rpf-rule"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class Interfaces(Entity):
                    """
                    Interface\-level Configuration
                    
                    .. attribute:: interface
                    
                    	The name of the interface
                    	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg.Mfwd.Vrfs.Vrf.Ipv4.Interfaces.Interface>`
                    
                    

                    """

                    _prefix = 'ipv4-mfwd-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        super(Mfwd.Vrfs.Vrf.Ipv4.Interfaces, self).__init__()

                        self.yang_name = "interfaces"
                        self.yang_parent_name = "ipv4"

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
                                    super(Mfwd.Vrfs.Vrf.Ipv4.Interfaces, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Mfwd.Vrfs.Vrf.Ipv4.Interfaces, self).__setattr__(name, value)


                    class Interface(Entity):
                        """
                        The name of the interface
                        
                        .. attribute:: interface_name  <key>
                        
                        	Interface name
                        	**type**\:  str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        .. attribute:: boundary
                        
                        	Boundary for administratively scoped multicast addresses
                        	**type**\:  str
                        
                        	**length:** 1..64
                        
                        .. attribute:: enable_on_interface
                        
                        	Enable or disable IP multicast on the interface
                        	**type**\:  bool
                        
                        .. attribute:: ttl_threshold
                        
                        	TTL threshold for multicast packets
                        	**type**\:  int
                        
                        	**range:** 1..255
                        
                        

                        """

                        _prefix = 'ipv4-mfwd-cfg'
                        _revision = '2016-06-01'

                        def __init__(self):
                            super(Mfwd.Vrfs.Vrf.Ipv4.Interfaces.Interface, self).__init__()

                            self.yang_name = "interface"
                            self.yang_parent_name = "interfaces"

                            self.interface_name = YLeaf(YType.str, "interface-name")

                            self.boundary = YLeaf(YType.str, "boundary")

                            self.enable_on_interface = YLeaf(YType.boolean, "enable-on-interface")

                            self.ttl_threshold = YLeaf(YType.uint32, "ttl-threshold")

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
                                            "boundary",
                                            "enable_on_interface",
                                            "ttl_threshold") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Mfwd.Vrfs.Vrf.Ipv4.Interfaces.Interface, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Mfwd.Vrfs.Vrf.Ipv4.Interfaces.Interface, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.interface_name.is_set or
                                self.boundary.is_set or
                                self.enable_on_interface.is_set or
                                self.ttl_threshold.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.interface_name.yfilter != YFilter.not_set or
                                self.boundary.yfilter != YFilter.not_set or
                                self.enable_on_interface.yfilter != YFilter.not_set or
                                self.ttl_threshold.yfilter != YFilter.not_set)

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
                            if (self.boundary.is_set or self.boundary.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.boundary.get_name_leafdata())
                            if (self.enable_on_interface.is_set or self.enable_on_interface.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.enable_on_interface.get_name_leafdata())
                            if (self.ttl_threshold.is_set or self.ttl_threshold.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ttl_threshold.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "interface-name" or name == "boundary" or name == "enable-on-interface" or name == "ttl-threshold"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "interface-name"):
                                self.interface_name = value
                                self.interface_name.value_namespace = name_space
                                self.interface_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "boundary"):
                                self.boundary = value
                                self.boundary.value_namespace = name_space
                                self.boundary.value_namespace_prefix = name_space_prefix
                            if(value_path == "enable-on-interface"):
                                self.enable_on_interface = value
                                self.enable_on_interface.value_namespace = name_space
                                self.enable_on_interface.value_namespace_prefix = name_space_prefix
                            if(value_path == "ttl-threshold"):
                                self.ttl_threshold = value
                                self.ttl_threshold.value_namespace = name_space
                                self.ttl_threshold.value_namespace_prefix = name_space_prefix

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
                            c = Mfwd.Vrfs.Vrf.Ipv4.Interfaces.Interface()
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

                def has_data(self):
                    return (
                        self.accounting.is_set or
                        self.enable_on_all_interfaces.is_set or
                        self.log_traps.is_set or
                        self.multicast_forwarding.is_set or
                        self.rate_per_route.is_set or
                        (self.interfaces is not None and self.interfaces.has_data()) or
                        (self.static_rpf_rules is not None and self.static_rpf_rules.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.accounting.yfilter != YFilter.not_set or
                        self.enable_on_all_interfaces.yfilter != YFilter.not_set or
                        self.log_traps.yfilter != YFilter.not_set or
                        self.multicast_forwarding.yfilter != YFilter.not_set or
                        self.rate_per_route.yfilter != YFilter.not_set or
                        (self.interfaces is not None and self.interfaces.has_operation()) or
                        (self.static_rpf_rules is not None and self.static_rpf_rules.has_operation()))

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
                    if (self.accounting.is_set or self.accounting.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.accounting.get_name_leafdata())
                    if (self.enable_on_all_interfaces.is_set or self.enable_on_all_interfaces.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.enable_on_all_interfaces.get_name_leafdata())
                    if (self.log_traps.is_set or self.log_traps.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.log_traps.get_name_leafdata())
                    if (self.multicast_forwarding.is_set or self.multicast_forwarding.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.multicast_forwarding.get_name_leafdata())
                    if (self.rate_per_route.is_set or self.rate_per_route.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rate_per_route.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "interfaces"):
                        if (self.interfaces is None):
                            self.interfaces = Mfwd.Vrfs.Vrf.Ipv4.Interfaces()
                            self.interfaces.parent = self
                            self._children_name_map["interfaces"] = "interfaces"
                        return self.interfaces

                    if (child_yang_name == "static-rpf-rules"):
                        if (self.static_rpf_rules is None):
                            self.static_rpf_rules = Mfwd.Vrfs.Vrf.Ipv4.StaticRpfRules()
                            self.static_rpf_rules.parent = self
                            self._children_name_map["static_rpf_rules"] = "static-rpf-rules"
                        return self.static_rpf_rules

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "interfaces" or name == "static-rpf-rules" or name == "accounting" or name == "enable-on-all-interfaces" or name == "log-traps" or name == "multicast-forwarding" or name == "rate-per-route"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "accounting"):
                        self.accounting = value
                        self.accounting.value_namespace = name_space
                        self.accounting.value_namespace_prefix = name_space_prefix
                    if(value_path == "enable-on-all-interfaces"):
                        self.enable_on_all_interfaces = value
                        self.enable_on_all_interfaces.value_namespace = name_space
                        self.enable_on_all_interfaces.value_namespace_prefix = name_space_prefix
                    if(value_path == "log-traps"):
                        self.log_traps = value
                        self.log_traps.value_namespace = name_space
                        self.log_traps.value_namespace_prefix = name_space_prefix
                    if(value_path == "multicast-forwarding"):
                        self.multicast_forwarding = value
                        self.multicast_forwarding.value_namespace = name_space
                        self.multicast_forwarding.value_namespace_prefix = name_space_prefix
                    if(value_path == "rate-per-route"):
                        self.rate_per_route = value
                        self.rate_per_route.value_namespace = name_space
                        self.rate_per_route.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.vrf_name.is_set or
                    (self.ipv4 is not None and self.ipv4.has_data()) or
                    (self.ipv6 is not None and self.ipv6.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.vrf_name.yfilter != YFilter.not_set or
                    (self.ipv4 is not None and self.ipv4.has_operation()) or
                    (self.ipv6 is not None and self.ipv6.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "vrf" + "[vrf-name='" + self.vrf_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ipv4-mfwd-cfg:mfwd/vrfs/%s" % self.get_segment_path()
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

                if (child_yang_name == "ipv4"):
                    if (self.ipv4 is None):
                        self.ipv4 = Mfwd.Vrfs.Vrf.Ipv4()
                        self.ipv4.parent = self
                        self._children_name_map["ipv4"] = "ipv4"
                    return self.ipv4

                if (child_yang_name == "ipv6"):
                    if (self.ipv6 is None):
                        self.ipv6 = Mfwd.Vrfs.Vrf.Ipv6()
                        self.ipv6.parent = self
                        self._children_name_map["ipv6"] = "ipv6"
                    return self.ipv6

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ipv4" or name == "ipv6" or name == "vrf-name"):
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
                path_buffer = "Cisco-IOS-XR-ipv4-mfwd-cfg:mfwd/%s" % self.get_segment_path()
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
                c = Mfwd.Vrfs.Vrf()
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
            (self.vrfs is not None and self.vrfs.has_data()) or
            (self.default_context is not None))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.default_context is not None and self.default_context.has_operation()) or
            (self.vrfs is not None and self.vrfs.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-ipv4-mfwd-cfg:mfwd" + path_buffer

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

        if (child_yang_name == "default-context"):
            if (self.default_context is None):
                self.default_context = Mfwd.DefaultContext()
                self.default_context.parent = self
                self._children_name_map["default_context"] = "default-context"
            return self.default_context

        if (child_yang_name == "vrfs"):
            if (self.vrfs is None):
                self.vrfs = Mfwd.Vrfs()
                self.vrfs.parent = self
                self._children_name_map["vrfs"] = "vrfs"
            return self.vrfs

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "default-context" or name == "vrfs"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Mfwd()
        return self._top_entity

