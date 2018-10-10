""" Cisco_IOS_XR_ipv4_mfwd_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv4\-mfwd package configuration.

This module contains definitions
for the following management objects\:
  mfwd\: Multicast routing configuration

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class AccountingMode(Enum):
    """
    AccountingMode (Enum Class)

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
    	**type**\:  :py:class:`DefaultContext <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg.Mfwd.DefaultContext>`
    
    .. attribute:: vrfs
    
    	VRF Table
    	**type**\:  :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg.Mfwd.Vrfs>`
    
    

    """

    _prefix = 'ipv4-mfwd-cfg'
    _revision = '2017-10-15'

    def __init__(self):
        super(Mfwd, self).__init__()
        self._top_entity = None

        self.yang_name = "mfwd"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-mfwd-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("default-context", ("default_context", Mfwd.DefaultContext)), ("vrfs", ("vrfs", Mfwd.Vrfs))])
        self._leafs = OrderedDict()

        self.default_context = Mfwd.DefaultContext()
        self.default_context.parent = self
        self._children_name_map["default_context"] = "default-context"

        self.vrfs = Mfwd.Vrfs()
        self.vrfs.parent = self
        self._children_name_map["vrfs"] = "vrfs"
        self._segment_path = lambda: "Cisco-IOS-XR-ipv4-mfwd-cfg:mfwd"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Mfwd, [], name, value)


    class DefaultContext(Entity):
        """
        Default Context
        
        .. attribute:: ipv6
        
        	IPV6 commands in the default context
        	**type**\:  :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg.Mfwd.DefaultContext.Ipv6>`
        
        .. attribute:: ipv4
        
        	IPV4 commands in the default context
        	**type**\:  :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg.Mfwd.DefaultContext.Ipv4>`
        
        

        """

        _prefix = 'ipv4-mfwd-cfg'
        _revision = '2017-10-15'

        def __init__(self):
            super(Mfwd.DefaultContext, self).__init__()

            self.yang_name = "default-context"
            self.yang_parent_name = "mfwd"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ipv6", ("ipv6", Mfwd.DefaultContext.Ipv6)), ("ipv4", ("ipv4", Mfwd.DefaultContext.Ipv4))])
            self._leafs = OrderedDict()

            self.ipv6 = Mfwd.DefaultContext.Ipv6()
            self.ipv6.parent = self
            self._children_name_map["ipv6"] = "ipv6"

            self.ipv4 = Mfwd.DefaultContext.Ipv4()
            self.ipv4.parent = self
            self._children_name_map["ipv4"] = "ipv4"
            self._segment_path = lambda: "default-context"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-mfwd-cfg:mfwd/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Mfwd.DefaultContext, [], name, value)


        class Ipv6(Entity):
            """
            IPV6 commands in the default context
            
            .. attribute:: enable_on_all_interfaces
            
            	Configure all interfaces for multicast routing and forwarding
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: maximum_checking_disable
            
            	Disable state limit maximum checking
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: rate_per_route
            
            	Enable per (S,G) rate calculation
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: interface_inheritance_disable
            
            	Disable interface inheritance configuration
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: static_rpf_rules
            
            	Configure a static RPF rule for a given prefix
            	**type**\:  :py:class:`StaticRpfRules <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg.Mfwd.DefaultContext.Ipv6.StaticRpfRules>`
            
            .. attribute:: mofrr_lockout_timer_config
            
            	Mofrr Lockout timer value
            	**type**\: int
            
            	**range:** 1..3600
            
            .. attribute:: forwarding_latency
            
            	Knob to delay traffic being forwarded on a route
            	**type**\: int
            
            	**range:** 5..500
            
            	**units**\: millisecond
            
            .. attribute:: mofrr_loss_detection_timer_config
            
            	Mofrr Loss Detection timer value
            	**type**\: int
            
            	**range:** 1..3600
            
            .. attribute:: interfaces
            
            	Interface\-level Configuration
            	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg.Mfwd.DefaultContext.Ipv6.Interfaces>`
            
            .. attribute:: multicast_forwarding
            
            	Enable IP multicast routing and forwarding
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: log_traps
            
            	Enable logging trap event
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: accounting
            
            	Per\-prefix accounting mode
            	**type**\:  :py:class:`AccountingMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg.AccountingMode>`
            
            

            """

            _prefix = 'ipv4-mfwd-cfg'
            _revision = '2017-10-15'

            def __init__(self):
                super(Mfwd.DefaultContext.Ipv6, self).__init__()

                self.yang_name = "ipv6"
                self.yang_parent_name = "default-context"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("static-rpf-rules", ("static_rpf_rules", Mfwd.DefaultContext.Ipv6.StaticRpfRules)), ("interfaces", ("interfaces", Mfwd.DefaultContext.Ipv6.Interfaces))])
                self._leafs = OrderedDict([
                    ('enable_on_all_interfaces', (YLeaf(YType.empty, 'enable-on-all-interfaces'), ['Empty'])),
                    ('maximum_checking_disable', (YLeaf(YType.empty, 'maximum-checking-disable'), ['Empty'])),
                    ('rate_per_route', (YLeaf(YType.empty, 'rate-per-route'), ['Empty'])),
                    ('interface_inheritance_disable', (YLeaf(YType.empty, 'interface-inheritance-disable'), ['Empty'])),
                    ('mofrr_lockout_timer_config', (YLeaf(YType.uint32, 'mofrr-lockout-timer-config'), ['int'])),
                    ('forwarding_latency', (YLeaf(YType.uint32, 'forwarding-latency'), ['int'])),
                    ('mofrr_loss_detection_timer_config', (YLeaf(YType.uint32, 'mofrr-loss-detection-timer-config'), ['int'])),
                    ('multicast_forwarding', (YLeaf(YType.empty, 'multicast-forwarding'), ['Empty'])),
                    ('log_traps', (YLeaf(YType.empty, 'log-traps'), ['Empty'])),
                    ('accounting', (YLeaf(YType.enumeration, 'accounting'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg', 'AccountingMode', '')])),
                ])
                self.enable_on_all_interfaces = None
                self.maximum_checking_disable = None
                self.rate_per_route = None
                self.interface_inheritance_disable = None
                self.mofrr_lockout_timer_config = None
                self.forwarding_latency = None
                self.mofrr_loss_detection_timer_config = None
                self.multicast_forwarding = None
                self.log_traps = None
                self.accounting = None

                self.static_rpf_rules = Mfwd.DefaultContext.Ipv6.StaticRpfRules()
                self.static_rpf_rules.parent = self
                self._children_name_map["static_rpf_rules"] = "static-rpf-rules"

                self.interfaces = Mfwd.DefaultContext.Ipv6.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"
                self._segment_path = lambda: "ipv6"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-mfwd-cfg:mfwd/default-context/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Mfwd.DefaultContext.Ipv6, ['enable_on_all_interfaces', 'maximum_checking_disable', 'rate_per_route', 'interface_inheritance_disable', 'mofrr_lockout_timer_config', 'forwarding_latency', 'mofrr_loss_detection_timer_config', 'multicast_forwarding', 'log_traps', 'accounting'], name, value)


            class StaticRpfRules(Entity):
                """
                Configure a static RPF rule for a given prefix
                
                .. attribute:: static_rpf_rule
                
                	RPF prefix address and mask
                	**type**\: list of  		 :py:class:`StaticRpfRule <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg.Mfwd.DefaultContext.Ipv6.StaticRpfRules.StaticRpfRule>`
                
                

                """

                _prefix = 'ipv4-mfwd-cfg'
                _revision = '2017-10-15'

                def __init__(self):
                    super(Mfwd.DefaultContext.Ipv6.StaticRpfRules, self).__init__()

                    self.yang_name = "static-rpf-rules"
                    self.yang_parent_name = "ipv6"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("static-rpf-rule", ("static_rpf_rule", Mfwd.DefaultContext.Ipv6.StaticRpfRules.StaticRpfRule))])
                    self._leafs = OrderedDict()

                    self.static_rpf_rule = YList(self)
                    self._segment_path = lambda: "static-rpf-rules"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-mfwd-cfg:mfwd/default-context/ipv6/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Mfwd.DefaultContext.Ipv6.StaticRpfRules, [], name, value)


                class StaticRpfRule(Entity):
                    """
                    RPF prefix address and mask
                    
                    .. attribute:: address  (key)
                    
                    	IP address of the RPF prefix
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    		**type**\: str
                    
                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: prefix_mask  (key)
                    
                    	Prefix mask of the RPF Prefix
                    	**type**\: int
                    
                    	**range:** 0..128
                    
                    .. attribute:: neighbor_address
                    
                    	Neighbor address of the RPF Prefix
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    		**type**\: str
                    
                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    	**mandatory**\: True
                    
                    .. attribute:: interface_name
                    
                    	The name of the RPF interface
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    	**mandatory**\: True
                    
                    

                    """

                    _prefix = 'ipv4-mfwd-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Mfwd.DefaultContext.Ipv6.StaticRpfRules.StaticRpfRule, self).__init__()

                        self.yang_name = "static-rpf-rule"
                        self.yang_parent_name = "static-rpf-rules"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['address','prefix_mask']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('address', (YLeaf(YType.str, 'address'), ['str','str'])),
                            ('prefix_mask', (YLeaf(YType.uint32, 'prefix-mask'), ['int'])),
                            ('neighbor_address', (YLeaf(YType.str, 'neighbor-address'), ['str','str'])),
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                        ])
                        self.address = None
                        self.prefix_mask = None
                        self.neighbor_address = None
                        self.interface_name = None
                        self._segment_path = lambda: "static-rpf-rule" + "[address='" + str(self.address) + "']" + "[prefix-mask='" + str(self.prefix_mask) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-mfwd-cfg:mfwd/default-context/ipv6/static-rpf-rules/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mfwd.DefaultContext.Ipv6.StaticRpfRules.StaticRpfRule, ['address', 'prefix_mask', 'neighbor_address', 'interface_name'], name, value)


            class Interfaces(Entity):
                """
                Interface\-level Configuration
                
                .. attribute:: interface
                
                	The name of the interface
                	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg.Mfwd.DefaultContext.Ipv6.Interfaces.Interface>`
                
                

                """

                _prefix = 'ipv4-mfwd-cfg'
                _revision = '2017-10-15'

                def __init__(self):
                    super(Mfwd.DefaultContext.Ipv6.Interfaces, self).__init__()

                    self.yang_name = "interfaces"
                    self.yang_parent_name = "ipv6"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("interface", ("interface", Mfwd.DefaultContext.Ipv6.Interfaces.Interface))])
                    self._leafs = OrderedDict()

                    self.interface = YList(self)
                    self._segment_path = lambda: "interfaces"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-mfwd-cfg:mfwd/default-context/ipv6/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Mfwd.DefaultContext.Ipv6.Interfaces, [], name, value)


                class Interface(Entity):
                    """
                    The name of the interface
                    
                    .. attribute:: interface_name  (key)
                    
                    	Interface name
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: ttl_threshold
                    
                    	TTL threshold for multicast packets
                    	**type**\: int
                    
                    	**range:** 1..255
                    
                    .. attribute:: enable_on_interface
                    
                    	Enable or disable IP multicast on the interface
                    	**type**\: bool
                    
                    .. attribute:: boundary
                    
                    	Boundary for administratively scoped multicast addresses
                    	**type**\: str
                    
                    	**length:** 1..64
                    
                    

                    """

                    _prefix = 'ipv4-mfwd-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Mfwd.DefaultContext.Ipv6.Interfaces.Interface, self).__init__()

                        self.yang_name = "interface"
                        self.yang_parent_name = "interfaces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['interface_name']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                            ('ttl_threshold', (YLeaf(YType.uint32, 'ttl-threshold'), ['int'])),
                            ('enable_on_interface', (YLeaf(YType.boolean, 'enable-on-interface'), ['bool'])),
                            ('boundary', (YLeaf(YType.str, 'boundary'), ['str'])),
                        ])
                        self.interface_name = None
                        self.ttl_threshold = None
                        self.enable_on_interface = None
                        self.boundary = None
                        self._segment_path = lambda: "interface" + "[interface-name='" + str(self.interface_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-mfwd-cfg:mfwd/default-context/ipv6/interfaces/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mfwd.DefaultContext.Ipv6.Interfaces.Interface, ['interface_name', 'ttl_threshold', 'enable_on_interface', 'boundary'], name, value)


        class Ipv4(Entity):
            """
            IPV4 commands in the default context
            
            .. attribute:: out_of_memory_handling
            
            	Enable out\-of\-memory handling
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: enable_on_all_interfaces
            
            	Configure all interfaces for multicast routing and forwarding
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: maximum_checking_disable
            
            	Disable state limit maximum checking
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: rate_per_route
            
            	Enable per (S,G) rate calculation
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: interface_inheritance_disable
            
            	Disable interface inheritance configuration
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: static_rpf_rules
            
            	Configure a static RPF rule for a given prefix
            	**type**\:  :py:class:`StaticRpfRules <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg.Mfwd.DefaultContext.Ipv4.StaticRpfRules>`
            
            .. attribute:: mofrr_lockout_timer_config
            
            	Mofrr Lockout timer value
            	**type**\: int
            
            	**range:** 1..3600
            
            .. attribute:: forwarding_latency
            
            	Knob to delay traffic being forwarded on a route
            	**type**\: int
            
            	**range:** 5..500
            
            	**units**\: millisecond
            
            .. attribute:: mofrr_loss_detection_timer_config
            
            	Mofrr Loss Detection timer value
            	**type**\: int
            
            	**range:** 1..3600
            
            .. attribute:: interfaces
            
            	Interface\-level Configuration
            	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg.Mfwd.DefaultContext.Ipv4.Interfaces>`
            
            .. attribute:: multicast_forwarding
            
            	Enable IP multicast routing and forwarding
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: log_traps
            
            	Enable logging trap event
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: accounting
            
            	Per\-prefix accounting mode
            	**type**\:  :py:class:`AccountingMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg.AccountingMode>`
            
            

            """

            _prefix = 'ipv4-mfwd-cfg'
            _revision = '2017-10-15'

            def __init__(self):
                super(Mfwd.DefaultContext.Ipv4, self).__init__()

                self.yang_name = "ipv4"
                self.yang_parent_name = "default-context"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("static-rpf-rules", ("static_rpf_rules", Mfwd.DefaultContext.Ipv4.StaticRpfRules)), ("interfaces", ("interfaces", Mfwd.DefaultContext.Ipv4.Interfaces))])
                self._leafs = OrderedDict([
                    ('out_of_memory_handling', (YLeaf(YType.empty, 'out-of-memory-handling'), ['Empty'])),
                    ('enable_on_all_interfaces', (YLeaf(YType.empty, 'enable-on-all-interfaces'), ['Empty'])),
                    ('maximum_checking_disable', (YLeaf(YType.empty, 'maximum-checking-disable'), ['Empty'])),
                    ('rate_per_route', (YLeaf(YType.empty, 'rate-per-route'), ['Empty'])),
                    ('interface_inheritance_disable', (YLeaf(YType.empty, 'interface-inheritance-disable'), ['Empty'])),
                    ('mofrr_lockout_timer_config', (YLeaf(YType.uint32, 'mofrr-lockout-timer-config'), ['int'])),
                    ('forwarding_latency', (YLeaf(YType.uint32, 'forwarding-latency'), ['int'])),
                    ('mofrr_loss_detection_timer_config', (YLeaf(YType.uint32, 'mofrr-loss-detection-timer-config'), ['int'])),
                    ('multicast_forwarding', (YLeaf(YType.empty, 'multicast-forwarding'), ['Empty'])),
                    ('log_traps', (YLeaf(YType.empty, 'log-traps'), ['Empty'])),
                    ('accounting', (YLeaf(YType.enumeration, 'accounting'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg', 'AccountingMode', '')])),
                ])
                self.out_of_memory_handling = None
                self.enable_on_all_interfaces = None
                self.maximum_checking_disable = None
                self.rate_per_route = None
                self.interface_inheritance_disable = None
                self.mofrr_lockout_timer_config = None
                self.forwarding_latency = None
                self.mofrr_loss_detection_timer_config = None
                self.multicast_forwarding = None
                self.log_traps = None
                self.accounting = None

                self.static_rpf_rules = Mfwd.DefaultContext.Ipv4.StaticRpfRules()
                self.static_rpf_rules.parent = self
                self._children_name_map["static_rpf_rules"] = "static-rpf-rules"

                self.interfaces = Mfwd.DefaultContext.Ipv4.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"
                self._segment_path = lambda: "ipv4"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-mfwd-cfg:mfwd/default-context/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Mfwd.DefaultContext.Ipv4, ['out_of_memory_handling', 'enable_on_all_interfaces', 'maximum_checking_disable', 'rate_per_route', 'interface_inheritance_disable', 'mofrr_lockout_timer_config', 'forwarding_latency', 'mofrr_loss_detection_timer_config', 'multicast_forwarding', 'log_traps', 'accounting'], name, value)


            class StaticRpfRules(Entity):
                """
                Configure a static RPF rule for a given prefix
                
                .. attribute:: static_rpf_rule
                
                	RPF prefix address and mask
                	**type**\: list of  		 :py:class:`StaticRpfRule <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg.Mfwd.DefaultContext.Ipv4.StaticRpfRules.StaticRpfRule>`
                
                

                """

                _prefix = 'ipv4-mfwd-cfg'
                _revision = '2017-10-15'

                def __init__(self):
                    super(Mfwd.DefaultContext.Ipv4.StaticRpfRules, self).__init__()

                    self.yang_name = "static-rpf-rules"
                    self.yang_parent_name = "ipv4"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("static-rpf-rule", ("static_rpf_rule", Mfwd.DefaultContext.Ipv4.StaticRpfRules.StaticRpfRule))])
                    self._leafs = OrderedDict()

                    self.static_rpf_rule = YList(self)
                    self._segment_path = lambda: "static-rpf-rules"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-mfwd-cfg:mfwd/default-context/ipv4/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Mfwd.DefaultContext.Ipv4.StaticRpfRules, [], name, value)


                class StaticRpfRule(Entity):
                    """
                    RPF prefix address and mask
                    
                    .. attribute:: address  (key)
                    
                    	IP address of the RPF prefix
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    		**type**\: str
                    
                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: prefix_mask  (key)
                    
                    	Prefix mask of the RPF Prefix
                    	**type**\: int
                    
                    	**range:** 0..128
                    
                    .. attribute:: neighbor_address
                    
                    	Neighbor address of the RPF Prefix
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    		**type**\: str
                    
                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    	**mandatory**\: True
                    
                    .. attribute:: interface_name
                    
                    	The name of the RPF interface
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    	**mandatory**\: True
                    
                    

                    """

                    _prefix = 'ipv4-mfwd-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Mfwd.DefaultContext.Ipv4.StaticRpfRules.StaticRpfRule, self).__init__()

                        self.yang_name = "static-rpf-rule"
                        self.yang_parent_name = "static-rpf-rules"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['address','prefix_mask']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('address', (YLeaf(YType.str, 'address'), ['str','str'])),
                            ('prefix_mask', (YLeaf(YType.uint32, 'prefix-mask'), ['int'])),
                            ('neighbor_address', (YLeaf(YType.str, 'neighbor-address'), ['str','str'])),
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                        ])
                        self.address = None
                        self.prefix_mask = None
                        self.neighbor_address = None
                        self.interface_name = None
                        self._segment_path = lambda: "static-rpf-rule" + "[address='" + str(self.address) + "']" + "[prefix-mask='" + str(self.prefix_mask) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-mfwd-cfg:mfwd/default-context/ipv4/static-rpf-rules/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mfwd.DefaultContext.Ipv4.StaticRpfRules.StaticRpfRule, ['address', 'prefix_mask', 'neighbor_address', 'interface_name'], name, value)


            class Interfaces(Entity):
                """
                Interface\-level Configuration
                
                .. attribute:: interface
                
                	The name of the interface
                	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg.Mfwd.DefaultContext.Ipv4.Interfaces.Interface>`
                
                

                """

                _prefix = 'ipv4-mfwd-cfg'
                _revision = '2017-10-15'

                def __init__(self):
                    super(Mfwd.DefaultContext.Ipv4.Interfaces, self).__init__()

                    self.yang_name = "interfaces"
                    self.yang_parent_name = "ipv4"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("interface", ("interface", Mfwd.DefaultContext.Ipv4.Interfaces.Interface))])
                    self._leafs = OrderedDict()

                    self.interface = YList(self)
                    self._segment_path = lambda: "interfaces"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-mfwd-cfg:mfwd/default-context/ipv4/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Mfwd.DefaultContext.Ipv4.Interfaces, [], name, value)


                class Interface(Entity):
                    """
                    The name of the interface
                    
                    .. attribute:: interface_name  (key)
                    
                    	Interface name
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: ttl_threshold
                    
                    	TTL threshold for multicast packets
                    	**type**\: int
                    
                    	**range:** 1..255
                    
                    .. attribute:: enable_on_interface
                    
                    	Enable or disable IP multicast on the interface
                    	**type**\: bool
                    
                    .. attribute:: boundary
                    
                    	Boundary for administratively scoped multicast addresses
                    	**type**\: str
                    
                    	**length:** 1..64
                    
                    

                    """

                    _prefix = 'ipv4-mfwd-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Mfwd.DefaultContext.Ipv4.Interfaces.Interface, self).__init__()

                        self.yang_name = "interface"
                        self.yang_parent_name = "interfaces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['interface_name']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                            ('ttl_threshold', (YLeaf(YType.uint32, 'ttl-threshold'), ['int'])),
                            ('enable_on_interface', (YLeaf(YType.boolean, 'enable-on-interface'), ['bool'])),
                            ('boundary', (YLeaf(YType.str, 'boundary'), ['str'])),
                        ])
                        self.interface_name = None
                        self.ttl_threshold = None
                        self.enable_on_interface = None
                        self.boundary = None
                        self._segment_path = lambda: "interface" + "[interface-name='" + str(self.interface_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-mfwd-cfg:mfwd/default-context/ipv4/interfaces/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mfwd.DefaultContext.Ipv4.Interfaces.Interface, ['interface_name', 'ttl_threshold', 'enable_on_interface', 'boundary'], name, value)


    class Vrfs(Entity):
        """
        VRF Table
        
        .. attribute:: vrf
        
        	VRF table names
        	**type**\: list of  		 :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg.Mfwd.Vrfs.Vrf>`
        
        

        """

        _prefix = 'ipv4-mfwd-cfg'
        _revision = '2017-10-15'

        def __init__(self):
            super(Mfwd.Vrfs, self).__init__()

            self.yang_name = "vrfs"
            self.yang_parent_name = "mfwd"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("vrf", ("vrf", Mfwd.Vrfs.Vrf))])
            self._leafs = OrderedDict()

            self.vrf = YList(self)
            self._segment_path = lambda: "vrfs"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-mfwd-cfg:mfwd/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Mfwd.Vrfs, [], name, value)


        class Vrf(Entity):
            """
            VRF table names
            
            .. attribute:: vrf_name  (key)
            
            	VRF Name
            	**type**\: str
            
            	**length:** 1..32
            
            .. attribute:: ipv6
            
            	VRF table for IPV6 commands
            	**type**\:  :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg.Mfwd.Vrfs.Vrf.Ipv6>`
            
            .. attribute:: ipv4
            
            	VRF table for IPV4 commands
            	**type**\:  :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg.Mfwd.Vrfs.Vrf.Ipv4>`
            
            

            """

            _prefix = 'ipv4-mfwd-cfg'
            _revision = '2017-10-15'

            def __init__(self):
                super(Mfwd.Vrfs.Vrf, self).__init__()

                self.yang_name = "vrf"
                self.yang_parent_name = "vrfs"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['vrf_name']
                self._child_classes = OrderedDict([("ipv6", ("ipv6", Mfwd.Vrfs.Vrf.Ipv6)), ("ipv4", ("ipv4", Mfwd.Vrfs.Vrf.Ipv4))])
                self._leafs = OrderedDict([
                    ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                ])
                self.vrf_name = None

                self.ipv6 = Mfwd.Vrfs.Vrf.Ipv6()
                self.ipv6.parent = self
                self._children_name_map["ipv6"] = "ipv6"

                self.ipv4 = Mfwd.Vrfs.Vrf.Ipv4()
                self.ipv4.parent = self
                self._children_name_map["ipv4"] = "ipv4"
                self._segment_path = lambda: "vrf" + "[vrf-name='" + str(self.vrf_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-mfwd-cfg:mfwd/vrfs/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Mfwd.Vrfs.Vrf, ['vrf_name'], name, value)


            class Ipv6(Entity):
                """
                VRF table for IPV6 commands
                
                .. attribute:: enable_on_all_interfaces
                
                	Configure all interfaces for multicast routing and forwarding
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: rate_per_route
                
                	Enable per (S,G) rate calculation
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: static_rpf_rules
                
                	Configure a static RPF rule for a given prefix
                	**type**\:  :py:class:`StaticRpfRules <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg.Mfwd.Vrfs.Vrf.Ipv6.StaticRpfRules>`
                
                .. attribute:: interfaces
                
                	Interface\-level Configuration
                	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg.Mfwd.Vrfs.Vrf.Ipv6.Interfaces>`
                
                .. attribute:: multicast_forwarding
                
                	Enable IP multicast routing and forwarding
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: log_traps
                
                	Enable logging trap event
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: accounting
                
                	Per\-prefix accounting mode
                	**type**\:  :py:class:`AccountingMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg.AccountingMode>`
                
                

                """

                _prefix = 'ipv4-mfwd-cfg'
                _revision = '2017-10-15'

                def __init__(self):
                    super(Mfwd.Vrfs.Vrf.Ipv6, self).__init__()

                    self.yang_name = "ipv6"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("static-rpf-rules", ("static_rpf_rules", Mfwd.Vrfs.Vrf.Ipv6.StaticRpfRules)), ("interfaces", ("interfaces", Mfwd.Vrfs.Vrf.Ipv6.Interfaces))])
                    self._leafs = OrderedDict([
                        ('enable_on_all_interfaces', (YLeaf(YType.empty, 'enable-on-all-interfaces'), ['Empty'])),
                        ('rate_per_route', (YLeaf(YType.empty, 'rate-per-route'), ['Empty'])),
                        ('multicast_forwarding', (YLeaf(YType.empty, 'multicast-forwarding'), ['Empty'])),
                        ('log_traps', (YLeaf(YType.empty, 'log-traps'), ['Empty'])),
                        ('accounting', (YLeaf(YType.enumeration, 'accounting'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg', 'AccountingMode', '')])),
                    ])
                    self.enable_on_all_interfaces = None
                    self.rate_per_route = None
                    self.multicast_forwarding = None
                    self.log_traps = None
                    self.accounting = None

                    self.static_rpf_rules = Mfwd.Vrfs.Vrf.Ipv6.StaticRpfRules()
                    self.static_rpf_rules.parent = self
                    self._children_name_map["static_rpf_rules"] = "static-rpf-rules"

                    self.interfaces = Mfwd.Vrfs.Vrf.Ipv6.Interfaces()
                    self.interfaces.parent = self
                    self._children_name_map["interfaces"] = "interfaces"
                    self._segment_path = lambda: "ipv6"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Mfwd.Vrfs.Vrf.Ipv6, ['enable_on_all_interfaces', 'rate_per_route', 'multicast_forwarding', 'log_traps', 'accounting'], name, value)


                class StaticRpfRules(Entity):
                    """
                    Configure a static RPF rule for a given prefix
                    
                    .. attribute:: static_rpf_rule
                    
                    	RPF prefix address and mask
                    	**type**\: list of  		 :py:class:`StaticRpfRule <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg.Mfwd.Vrfs.Vrf.Ipv6.StaticRpfRules.StaticRpfRule>`
                    
                    

                    """

                    _prefix = 'ipv4-mfwd-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Mfwd.Vrfs.Vrf.Ipv6.StaticRpfRules, self).__init__()

                        self.yang_name = "static-rpf-rules"
                        self.yang_parent_name = "ipv6"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("static-rpf-rule", ("static_rpf_rule", Mfwd.Vrfs.Vrf.Ipv6.StaticRpfRules.StaticRpfRule))])
                        self._leafs = OrderedDict()

                        self.static_rpf_rule = YList(self)
                        self._segment_path = lambda: "static-rpf-rules"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mfwd.Vrfs.Vrf.Ipv6.StaticRpfRules, [], name, value)


                    class StaticRpfRule(Entity):
                        """
                        RPF prefix address and mask
                        
                        .. attribute:: address  (key)
                        
                        	IP address of the RPF prefix
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: prefix_mask  (key)
                        
                        	Prefix mask of the RPF Prefix
                        	**type**\: int
                        
                        	**range:** 0..128
                        
                        .. attribute:: neighbor_address
                        
                        	Neighbor address of the RPF Prefix
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        	**mandatory**\: True
                        
                        .. attribute:: interface_name
                        
                        	The name of the RPF interface
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'ipv4-mfwd-cfg'
                        _revision = '2017-10-15'

                        def __init__(self):
                            super(Mfwd.Vrfs.Vrf.Ipv6.StaticRpfRules.StaticRpfRule, self).__init__()

                            self.yang_name = "static-rpf-rule"
                            self.yang_parent_name = "static-rpf-rules"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['address','prefix_mask']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('address', (YLeaf(YType.str, 'address'), ['str','str'])),
                                ('prefix_mask', (YLeaf(YType.uint32, 'prefix-mask'), ['int'])),
                                ('neighbor_address', (YLeaf(YType.str, 'neighbor-address'), ['str','str'])),
                                ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                            ])
                            self.address = None
                            self.prefix_mask = None
                            self.neighbor_address = None
                            self.interface_name = None
                            self._segment_path = lambda: "static-rpf-rule" + "[address='" + str(self.address) + "']" + "[prefix-mask='" + str(self.prefix_mask) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mfwd.Vrfs.Vrf.Ipv6.StaticRpfRules.StaticRpfRule, ['address', 'prefix_mask', 'neighbor_address', 'interface_name'], name, value)


                class Interfaces(Entity):
                    """
                    Interface\-level Configuration
                    
                    .. attribute:: interface
                    
                    	The name of the interface
                    	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg.Mfwd.Vrfs.Vrf.Ipv6.Interfaces.Interface>`
                    
                    

                    """

                    _prefix = 'ipv4-mfwd-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Mfwd.Vrfs.Vrf.Ipv6.Interfaces, self).__init__()

                        self.yang_name = "interfaces"
                        self.yang_parent_name = "ipv6"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("interface", ("interface", Mfwd.Vrfs.Vrf.Ipv6.Interfaces.Interface))])
                        self._leafs = OrderedDict()

                        self.interface = YList(self)
                        self._segment_path = lambda: "interfaces"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mfwd.Vrfs.Vrf.Ipv6.Interfaces, [], name, value)


                    class Interface(Entity):
                        """
                        The name of the interface
                        
                        .. attribute:: interface_name  (key)
                        
                        	Interface name
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        .. attribute:: ttl_threshold
                        
                        	TTL threshold for multicast packets
                        	**type**\: int
                        
                        	**range:** 1..255
                        
                        .. attribute:: enable_on_interface
                        
                        	Enable or disable IP multicast on the interface
                        	**type**\: bool
                        
                        .. attribute:: boundary
                        
                        	Boundary for administratively scoped multicast addresses
                        	**type**\: str
                        
                        	**length:** 1..64
                        
                        

                        """

                        _prefix = 'ipv4-mfwd-cfg'
                        _revision = '2017-10-15'

                        def __init__(self):
                            super(Mfwd.Vrfs.Vrf.Ipv6.Interfaces.Interface, self).__init__()

                            self.yang_name = "interface"
                            self.yang_parent_name = "interfaces"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['interface_name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                ('ttl_threshold', (YLeaf(YType.uint32, 'ttl-threshold'), ['int'])),
                                ('enable_on_interface', (YLeaf(YType.boolean, 'enable-on-interface'), ['bool'])),
                                ('boundary', (YLeaf(YType.str, 'boundary'), ['str'])),
                            ])
                            self.interface_name = None
                            self.ttl_threshold = None
                            self.enable_on_interface = None
                            self.boundary = None
                            self._segment_path = lambda: "interface" + "[interface-name='" + str(self.interface_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mfwd.Vrfs.Vrf.Ipv6.Interfaces.Interface, ['interface_name', 'ttl_threshold', 'enable_on_interface', 'boundary'], name, value)


            class Ipv4(Entity):
                """
                VRF table for IPV4 commands
                
                .. attribute:: enable_on_all_interfaces
                
                	Configure all interfaces for multicast routing and forwarding
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: rate_per_route
                
                	Enable per (S,G) rate calculation
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: static_rpf_rules
                
                	Configure a static RPF rule for a given prefix
                	**type**\:  :py:class:`StaticRpfRules <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg.Mfwd.Vrfs.Vrf.Ipv4.StaticRpfRules>`
                
                .. attribute:: interfaces
                
                	Interface\-level Configuration
                	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg.Mfwd.Vrfs.Vrf.Ipv4.Interfaces>`
                
                .. attribute:: multicast_forwarding
                
                	Enable IP multicast routing and forwarding
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: log_traps
                
                	Enable logging trap event
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: accounting
                
                	Per\-prefix accounting mode
                	**type**\:  :py:class:`AccountingMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg.AccountingMode>`
                
                

                """

                _prefix = 'ipv4-mfwd-cfg'
                _revision = '2017-10-15'

                def __init__(self):
                    super(Mfwd.Vrfs.Vrf.Ipv4, self).__init__()

                    self.yang_name = "ipv4"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("static-rpf-rules", ("static_rpf_rules", Mfwd.Vrfs.Vrf.Ipv4.StaticRpfRules)), ("interfaces", ("interfaces", Mfwd.Vrfs.Vrf.Ipv4.Interfaces))])
                    self._leafs = OrderedDict([
                        ('enable_on_all_interfaces', (YLeaf(YType.empty, 'enable-on-all-interfaces'), ['Empty'])),
                        ('rate_per_route', (YLeaf(YType.empty, 'rate-per-route'), ['Empty'])),
                        ('multicast_forwarding', (YLeaf(YType.empty, 'multicast-forwarding'), ['Empty'])),
                        ('log_traps', (YLeaf(YType.empty, 'log-traps'), ['Empty'])),
                        ('accounting', (YLeaf(YType.enumeration, 'accounting'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg', 'AccountingMode', '')])),
                    ])
                    self.enable_on_all_interfaces = None
                    self.rate_per_route = None
                    self.multicast_forwarding = None
                    self.log_traps = None
                    self.accounting = None

                    self.static_rpf_rules = Mfwd.Vrfs.Vrf.Ipv4.StaticRpfRules()
                    self.static_rpf_rules.parent = self
                    self._children_name_map["static_rpf_rules"] = "static-rpf-rules"

                    self.interfaces = Mfwd.Vrfs.Vrf.Ipv4.Interfaces()
                    self.interfaces.parent = self
                    self._children_name_map["interfaces"] = "interfaces"
                    self._segment_path = lambda: "ipv4"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Mfwd.Vrfs.Vrf.Ipv4, ['enable_on_all_interfaces', 'rate_per_route', 'multicast_forwarding', 'log_traps', 'accounting'], name, value)


                class StaticRpfRules(Entity):
                    """
                    Configure a static RPF rule for a given prefix
                    
                    .. attribute:: static_rpf_rule
                    
                    	RPF prefix address and mask
                    	**type**\: list of  		 :py:class:`StaticRpfRule <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg.Mfwd.Vrfs.Vrf.Ipv4.StaticRpfRules.StaticRpfRule>`
                    
                    

                    """

                    _prefix = 'ipv4-mfwd-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Mfwd.Vrfs.Vrf.Ipv4.StaticRpfRules, self).__init__()

                        self.yang_name = "static-rpf-rules"
                        self.yang_parent_name = "ipv4"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("static-rpf-rule", ("static_rpf_rule", Mfwd.Vrfs.Vrf.Ipv4.StaticRpfRules.StaticRpfRule))])
                        self._leafs = OrderedDict()

                        self.static_rpf_rule = YList(self)
                        self._segment_path = lambda: "static-rpf-rules"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mfwd.Vrfs.Vrf.Ipv4.StaticRpfRules, [], name, value)


                    class StaticRpfRule(Entity):
                        """
                        RPF prefix address and mask
                        
                        .. attribute:: address  (key)
                        
                        	IP address of the RPF prefix
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: prefix_mask  (key)
                        
                        	Prefix mask of the RPF Prefix
                        	**type**\: int
                        
                        	**range:** 0..128
                        
                        .. attribute:: neighbor_address
                        
                        	Neighbor address of the RPF Prefix
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        	**mandatory**\: True
                        
                        .. attribute:: interface_name
                        
                        	The name of the RPF interface
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'ipv4-mfwd-cfg'
                        _revision = '2017-10-15'

                        def __init__(self):
                            super(Mfwd.Vrfs.Vrf.Ipv4.StaticRpfRules.StaticRpfRule, self).__init__()

                            self.yang_name = "static-rpf-rule"
                            self.yang_parent_name = "static-rpf-rules"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['address','prefix_mask']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('address', (YLeaf(YType.str, 'address'), ['str','str'])),
                                ('prefix_mask', (YLeaf(YType.uint32, 'prefix-mask'), ['int'])),
                                ('neighbor_address', (YLeaf(YType.str, 'neighbor-address'), ['str','str'])),
                                ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                            ])
                            self.address = None
                            self.prefix_mask = None
                            self.neighbor_address = None
                            self.interface_name = None
                            self._segment_path = lambda: "static-rpf-rule" + "[address='" + str(self.address) + "']" + "[prefix-mask='" + str(self.prefix_mask) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mfwd.Vrfs.Vrf.Ipv4.StaticRpfRules.StaticRpfRule, ['address', 'prefix_mask', 'neighbor_address', 'interface_name'], name, value)


                class Interfaces(Entity):
                    """
                    Interface\-level Configuration
                    
                    .. attribute:: interface
                    
                    	The name of the interface
                    	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg.Mfwd.Vrfs.Vrf.Ipv4.Interfaces.Interface>`
                    
                    

                    """

                    _prefix = 'ipv4-mfwd-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Mfwd.Vrfs.Vrf.Ipv4.Interfaces, self).__init__()

                        self.yang_name = "interfaces"
                        self.yang_parent_name = "ipv4"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("interface", ("interface", Mfwd.Vrfs.Vrf.Ipv4.Interfaces.Interface))])
                        self._leafs = OrderedDict()

                        self.interface = YList(self)
                        self._segment_path = lambda: "interfaces"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mfwd.Vrfs.Vrf.Ipv4.Interfaces, [], name, value)


                    class Interface(Entity):
                        """
                        The name of the interface
                        
                        .. attribute:: interface_name  (key)
                        
                        	Interface name
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        .. attribute:: ttl_threshold
                        
                        	TTL threshold for multicast packets
                        	**type**\: int
                        
                        	**range:** 1..255
                        
                        .. attribute:: enable_on_interface
                        
                        	Enable or disable IP multicast on the interface
                        	**type**\: bool
                        
                        .. attribute:: boundary
                        
                        	Boundary for administratively scoped multicast addresses
                        	**type**\: str
                        
                        	**length:** 1..64
                        
                        

                        """

                        _prefix = 'ipv4-mfwd-cfg'
                        _revision = '2017-10-15'

                        def __init__(self):
                            super(Mfwd.Vrfs.Vrf.Ipv4.Interfaces.Interface, self).__init__()

                            self.yang_name = "interface"
                            self.yang_parent_name = "interfaces"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['interface_name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                ('ttl_threshold', (YLeaf(YType.uint32, 'ttl-threshold'), ['int'])),
                                ('enable_on_interface', (YLeaf(YType.boolean, 'enable-on-interface'), ['bool'])),
                                ('boundary', (YLeaf(YType.str, 'boundary'), ['str'])),
                            ])
                            self.interface_name = None
                            self.ttl_threshold = None
                            self.enable_on_interface = None
                            self.boundary = None
                            self._segment_path = lambda: "interface" + "[interface-name='" + str(self.interface_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mfwd.Vrfs.Vrf.Ipv4.Interfaces.Interface, ['interface_name', 'ttl_threshold', 'enable_on_interface', 'boundary'], name, value)

    def clone_ptr(self):
        self._top_entity = Mfwd()
        return self._top_entity

