""" Cisco_IOS_XR_ipv4_mfwd_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv4\-mfwd package configuration.

This module contains definitions
for the following management objects\:
  mfwd\: Multicast routing configuration

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
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
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"default-context" : ("default_context", Mfwd.DefaultContext), "vrfs" : ("vrfs", Mfwd.Vrfs)}
        self._child_list_classes = {}
        self.is_presence_container = True

        self.default_context = None
        self._children_name_map["default_context"] = "default-context"
        self._children_yang_names.add("default-context")

        self.vrfs = Mfwd.Vrfs()
        self.vrfs.parent = self
        self._children_name_map["vrfs"] = "vrfs"
        self._children_yang_names.add("vrfs")
        self._segment_path = lambda: "Cisco-IOS-XR-ipv4-mfwd-cfg:mfwd"


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
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"ipv4" : ("ipv4", Mfwd.DefaultContext.Ipv4), "ipv6" : ("ipv6", Mfwd.DefaultContext.Ipv6)}
            self._child_list_classes = {}
            self.is_presence_container = True

            self.ipv4 = Mfwd.DefaultContext.Ipv4()
            self.ipv4.parent = self
            self._children_name_map["ipv4"] = "ipv4"
            self._children_yang_names.add("ipv4")

            self.ipv6 = Mfwd.DefaultContext.Ipv6()
            self.ipv6.parent = self
            self._children_name_map["ipv6"] = "ipv6"
            self._children_yang_names.add("ipv6")
            self._segment_path = lambda: "default-context"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-mfwd-cfg:mfwd/%s" % self._segment_path()


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
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"interfaces" : ("interfaces", Mfwd.DefaultContext.Ipv4.Interfaces), "static-rpf-rules" : ("static_rpf_rules", Mfwd.DefaultContext.Ipv4.StaticRpfRules)}
                self._child_list_classes = {}

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
                self._segment_path = lambda: "ipv4"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-mfwd-cfg:mfwd/default-context/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Mfwd.DefaultContext.Ipv4, ['accounting', 'enable_on_all_interfaces', 'forwarding_latency', 'interface_inheritance_disable', 'log_traps', 'maximum_checking_disable', 'mofrr_lockout_timer_config', 'mofrr_loss_detection_timer_config', 'multicast_forwarding', 'out_of_memory_handling', 'rate_per_route'], name, value)


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
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"interface" : ("interface", Mfwd.DefaultContext.Ipv4.Interfaces.Interface)}

                    self.interface = YList(self)
                    self._segment_path = lambda: "interfaces"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-mfwd-cfg:mfwd/default-context/ipv4/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Mfwd.DefaultContext.Ipv4.Interfaces, [], name, value)


                class Interface(Entity):
                    """
                    The name of the interface
                    
                    .. attribute:: interface_name  <key>
                    
                    	Interface name
                    	**type**\:  str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
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
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.boundary = YLeaf(YType.str, "boundary")

                        self.enable_on_interface = YLeaf(YType.boolean, "enable-on-interface")

                        self.ttl_threshold = YLeaf(YType.uint32, "ttl-threshold")
                        self._segment_path = lambda: "interface" + "[interface-name='" + self.interface_name.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-mfwd-cfg:mfwd/default-context/ipv4/interfaces/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mfwd.DefaultContext.Ipv4.Interfaces.Interface, ['interface_name', 'boundary', 'enable_on_interface', 'ttl_threshold'], name, value)


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
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"static-rpf-rule" : ("static_rpf_rule", Mfwd.DefaultContext.Ipv4.StaticRpfRules.StaticRpfRule)}

                    self.static_rpf_rule = YList(self)
                    self._segment_path = lambda: "static-rpf-rules"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-mfwd-cfg:mfwd/default-context/ipv4/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Mfwd.DefaultContext.Ipv4.StaticRpfRules, [], name, value)


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
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
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
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.address = YLeaf(YType.str, "address")

                        self.prefix_mask = YLeaf(YType.uint32, "prefix-mask")

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.neighbor_address = YLeaf(YType.str, "neighbor-address")
                        self._segment_path = lambda: "static-rpf-rule" + "[address='" + self.address.get() + "']" + "[prefix-mask='" + self.prefix_mask.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-mfwd-cfg:mfwd/default-context/ipv4/static-rpf-rules/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mfwd.DefaultContext.Ipv4.StaticRpfRules.StaticRpfRule, ['address', 'prefix_mask', 'interface_name', 'neighbor_address'], name, value)


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
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"interfaces" : ("interfaces", Mfwd.DefaultContext.Ipv6.Interfaces), "static-rpf-rules" : ("static_rpf_rules", Mfwd.DefaultContext.Ipv6.StaticRpfRules)}
                self._child_list_classes = {}

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
                self._segment_path = lambda: "ipv6"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-mfwd-cfg:mfwd/default-context/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Mfwd.DefaultContext.Ipv6, ['accounting', 'enable_on_all_interfaces', 'forwarding_latency', 'interface_inheritance_disable', 'log_traps', 'maximum_checking_disable', 'mofrr_lockout_timer_config', 'mofrr_loss_detection_timer_config', 'multicast_forwarding', 'rate_per_route'], name, value)


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
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"interface" : ("interface", Mfwd.DefaultContext.Ipv6.Interfaces.Interface)}

                    self.interface = YList(self)
                    self._segment_path = lambda: "interfaces"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-mfwd-cfg:mfwd/default-context/ipv6/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Mfwd.DefaultContext.Ipv6.Interfaces, [], name, value)


                class Interface(Entity):
                    """
                    The name of the interface
                    
                    .. attribute:: interface_name  <key>
                    
                    	Interface name
                    	**type**\:  str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
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
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.boundary = YLeaf(YType.str, "boundary")

                        self.enable_on_interface = YLeaf(YType.boolean, "enable-on-interface")

                        self.ttl_threshold = YLeaf(YType.uint32, "ttl-threshold")
                        self._segment_path = lambda: "interface" + "[interface-name='" + self.interface_name.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-mfwd-cfg:mfwd/default-context/ipv6/interfaces/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mfwd.DefaultContext.Ipv6.Interfaces.Interface, ['interface_name', 'boundary', 'enable_on_interface', 'ttl_threshold'], name, value)


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
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"static-rpf-rule" : ("static_rpf_rule", Mfwd.DefaultContext.Ipv6.StaticRpfRules.StaticRpfRule)}

                    self.static_rpf_rule = YList(self)
                    self._segment_path = lambda: "static-rpf-rules"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-mfwd-cfg:mfwd/default-context/ipv6/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Mfwd.DefaultContext.Ipv6.StaticRpfRules, [], name, value)


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
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
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
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.address = YLeaf(YType.str, "address")

                        self.prefix_mask = YLeaf(YType.uint32, "prefix-mask")

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.neighbor_address = YLeaf(YType.str, "neighbor-address")
                        self._segment_path = lambda: "static-rpf-rule" + "[address='" + self.address.get() + "']" + "[prefix-mask='" + self.prefix_mask.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-mfwd-cfg:mfwd/default-context/ipv6/static-rpf-rules/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mfwd.DefaultContext.Ipv6.StaticRpfRules.StaticRpfRule, ['address', 'prefix_mask', 'interface_name', 'neighbor_address'], name, value)


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
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"vrf" : ("vrf", Mfwd.Vrfs.Vrf)}

            self.vrf = YList(self)
            self._segment_path = lambda: "vrfs"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-mfwd-cfg:mfwd/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Mfwd.Vrfs, [], name, value)


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
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"ipv4" : ("ipv4", Mfwd.Vrfs.Vrf.Ipv4), "ipv6" : ("ipv6", Mfwd.Vrfs.Vrf.Ipv6)}
                self._child_list_classes = {}

                self.vrf_name = YLeaf(YType.str, "vrf-name")

                self.ipv4 = Mfwd.Vrfs.Vrf.Ipv4()
                self.ipv4.parent = self
                self._children_name_map["ipv4"] = "ipv4"
                self._children_yang_names.add("ipv4")

                self.ipv6 = Mfwd.Vrfs.Vrf.Ipv6()
                self.ipv6.parent = self
                self._children_name_map["ipv6"] = "ipv6"
                self._children_yang_names.add("ipv6")
                self._segment_path = lambda: "vrf" + "[vrf-name='" + self.vrf_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-mfwd-cfg:mfwd/vrfs/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Mfwd.Vrfs.Vrf, ['vrf_name'], name, value)


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
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"interfaces" : ("interfaces", Mfwd.Vrfs.Vrf.Ipv4.Interfaces), "static-rpf-rules" : ("static_rpf_rules", Mfwd.Vrfs.Vrf.Ipv4.StaticRpfRules)}
                    self._child_list_classes = {}

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
                    self._segment_path = lambda: "ipv4"

                def __setattr__(self, name, value):
                    self._perform_setattr(Mfwd.Vrfs.Vrf.Ipv4, ['accounting', 'enable_on_all_interfaces', 'log_traps', 'multicast_forwarding', 'rate_per_route'], name, value)


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
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"interface" : ("interface", Mfwd.Vrfs.Vrf.Ipv4.Interfaces.Interface)}

                        self.interface = YList(self)
                        self._segment_path = lambda: "interfaces"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mfwd.Vrfs.Vrf.Ipv4.Interfaces, [], name, value)


                    class Interface(Entity):
                        """
                        The name of the interface
                        
                        .. attribute:: interface_name  <key>
                        
                        	Interface name
                        	**type**\:  str
                        
                        	**pattern:** [a\-zA\-Z0\-9./\-]+
                        
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
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.interface_name = YLeaf(YType.str, "interface-name")

                            self.boundary = YLeaf(YType.str, "boundary")

                            self.enable_on_interface = YLeaf(YType.boolean, "enable-on-interface")

                            self.ttl_threshold = YLeaf(YType.uint32, "ttl-threshold")
                            self._segment_path = lambda: "interface" + "[interface-name='" + self.interface_name.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mfwd.Vrfs.Vrf.Ipv4.Interfaces.Interface, ['interface_name', 'boundary', 'enable_on_interface', 'ttl_threshold'], name, value)


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
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"static-rpf-rule" : ("static_rpf_rule", Mfwd.Vrfs.Vrf.Ipv4.StaticRpfRules.StaticRpfRule)}

                        self.static_rpf_rule = YList(self)
                        self._segment_path = lambda: "static-rpf-rules"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mfwd.Vrfs.Vrf.Ipv4.StaticRpfRules, [], name, value)


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
                        
                        	**pattern:** [a\-zA\-Z0\-9./\-]+
                        
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
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.address = YLeaf(YType.str, "address")

                            self.prefix_mask = YLeaf(YType.uint32, "prefix-mask")

                            self.interface_name = YLeaf(YType.str, "interface-name")

                            self.neighbor_address = YLeaf(YType.str, "neighbor-address")
                            self._segment_path = lambda: "static-rpf-rule" + "[address='" + self.address.get() + "']" + "[prefix-mask='" + self.prefix_mask.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mfwd.Vrfs.Vrf.Ipv4.StaticRpfRules.StaticRpfRule, ['address', 'prefix_mask', 'interface_name', 'neighbor_address'], name, value)


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
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"interfaces" : ("interfaces", Mfwd.Vrfs.Vrf.Ipv6.Interfaces), "static-rpf-rules" : ("static_rpf_rules", Mfwd.Vrfs.Vrf.Ipv6.StaticRpfRules)}
                    self._child_list_classes = {}

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
                    self._segment_path = lambda: "ipv6"

                def __setattr__(self, name, value):
                    self._perform_setattr(Mfwd.Vrfs.Vrf.Ipv6, ['accounting', 'enable_on_all_interfaces', 'log_traps', 'multicast_forwarding', 'rate_per_route'], name, value)


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
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"interface" : ("interface", Mfwd.Vrfs.Vrf.Ipv6.Interfaces.Interface)}

                        self.interface = YList(self)
                        self._segment_path = lambda: "interfaces"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mfwd.Vrfs.Vrf.Ipv6.Interfaces, [], name, value)


                    class Interface(Entity):
                        """
                        The name of the interface
                        
                        .. attribute:: interface_name  <key>
                        
                        	Interface name
                        	**type**\:  str
                        
                        	**pattern:** [a\-zA\-Z0\-9./\-]+
                        
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
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.interface_name = YLeaf(YType.str, "interface-name")

                            self.boundary = YLeaf(YType.str, "boundary")

                            self.enable_on_interface = YLeaf(YType.boolean, "enable-on-interface")

                            self.ttl_threshold = YLeaf(YType.uint32, "ttl-threshold")
                            self._segment_path = lambda: "interface" + "[interface-name='" + self.interface_name.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mfwd.Vrfs.Vrf.Ipv6.Interfaces.Interface, ['interface_name', 'boundary', 'enable_on_interface', 'ttl_threshold'], name, value)


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
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"static-rpf-rule" : ("static_rpf_rule", Mfwd.Vrfs.Vrf.Ipv6.StaticRpfRules.StaticRpfRule)}

                        self.static_rpf_rule = YList(self)
                        self._segment_path = lambda: "static-rpf-rules"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mfwd.Vrfs.Vrf.Ipv6.StaticRpfRules, [], name, value)


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
                        
                        	**pattern:** [a\-zA\-Z0\-9./\-]+
                        
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
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.address = YLeaf(YType.str, "address")

                            self.prefix_mask = YLeaf(YType.uint32, "prefix-mask")

                            self.interface_name = YLeaf(YType.str, "interface-name")

                            self.neighbor_address = YLeaf(YType.str, "neighbor-address")
                            self._segment_path = lambda: "static-rpf-rule" + "[address='" + self.address.get() + "']" + "[prefix-mask='" + self.prefix_mask.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mfwd.Vrfs.Vrf.Ipv6.StaticRpfRules.StaticRpfRule, ['address', 'prefix_mask', 'interface_name', 'neighbor_address'], name, value)

    def clone_ptr(self):
        self._top_entity = Mfwd()
        return self._top_entity

