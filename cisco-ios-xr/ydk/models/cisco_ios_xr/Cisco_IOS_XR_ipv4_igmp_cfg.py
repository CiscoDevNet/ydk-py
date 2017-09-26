""" Cisco_IOS_XR_ipv4_igmp_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv4\-igmp package configuration.

This module contains definitions
for the following management objects\:
  igmp\: IGMPconfiguration
  amt\: amt
  mld\: mld

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class IgmpFilter(Enum):
    """
    IgmpFilter

    Igmp filter

    .. data:: include = 0

    	Include

    .. data:: exclude = 1

    	Exclude

    .. data:: star_g = 2

    	StarG

    """

    include = Enum.YLeaf(0, "include")

    exclude = Enum.YLeaf(1, "exclude")

    star_g = Enum.YLeaf(2, "star-g")



class Amt(Entity):
    """
    amt
    
    .. attribute:: amtmtu
    
    	Configure AMT Relay MTU
    	**type**\:  int
    
    	**range:** 100..65535
    
    .. attribute:: amtqqic
    
    	Configure AMT QQIC value
    	**type**\:  int
    
    	**range:** 1..4294967295
    
    .. attribute:: amttos
    
    	Configure AMT Relay TOS
    	**type**\:  int
    
    	**range:** 1..255
    
    .. attribute:: amtttl
    
    	Configure AMT Relay TTL
    	**type**\:  int
    
    	**range:** 1..255
    
    .. attribute:: gateway_filter
    
    	Access list for Gateway Filter
    	**type**\:  str
    
    	**length:** 1..64
    
    .. attribute:: maximum_gateway
    
    	Configure AMT maximum number of Gateways
    	**type**\:  int
    
    	**range:** 1..4294967295
    
    .. attribute:: maximum_v4_route_gateway
    
    	Configure Maximum number of IPv4 route\-gateways (Tunnels)
    	**type**\:  int
    
    	**range:** 1..4294967295
    
    .. attribute:: maximum_v4_routes
    
    	Configure Maximum number of IPv4 Routes
    	**type**\:  int
    
    	**range:** 1..4294967295
    
    .. attribute:: maximum_v6_route_gateway
    
    	Configure Maximum number of IPv6 route\-gateways (Tunnels)
    	**type**\:  int
    
    	**range:** 1..4294967295
    
    .. attribute:: maximum_v6_routes
    
    	Configure Maximum number of IPv6 Routes
    	**type**\:  int
    
    	**range:** 1..4294967295
    
    .. attribute:: relay_adv_add
    
    	Configure AMT Relay IPv4 Advertisement Address
    	**type**\:   :py:class:`RelayAdvAdd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Amt.RelayAdvAdd>`
    
    	**presence node**\: True
    
    .. attribute:: relay_anycast_prefix
    
    	Configure AMT Relay IPv4 Anycast\-Prefix
    	**type**\:   :py:class:`RelayAnycastPrefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Amt.RelayAnycastPrefix>`
    
    	**presence node**\: True
    
    

    """

    _prefix = 'ipv4-igmp-cfg'
    _revision = '2016-10-10'

    def __init__(self):
        super(Amt, self).__init__()
        self._top_entity = None

        self.yang_name = "amt"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-igmp-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"relay-adv-add" : ("relay_adv_add", Amt.RelayAdvAdd), "relay-anycast-prefix" : ("relay_anycast_prefix", Amt.RelayAnycastPrefix)}
        self._child_list_classes = {}

        self.amtmtu = YLeaf(YType.uint32, "amtmtu")

        self.amtqqic = YLeaf(YType.uint32, "amtqqic")

        self.amttos = YLeaf(YType.uint32, "amttos")

        self.amtttl = YLeaf(YType.uint32, "amtttl")

        self.gateway_filter = YLeaf(YType.str, "gateway-filter")

        self.maximum_gateway = YLeaf(YType.uint32, "maximum-gateway")

        self.maximum_v4_route_gateway = YLeaf(YType.uint32, "maximum-v4-route-gateway")

        self.maximum_v4_routes = YLeaf(YType.uint32, "maximum-v4-routes")

        self.maximum_v6_route_gateway = YLeaf(YType.uint32, "maximum-v6-route-gateway")

        self.maximum_v6_routes = YLeaf(YType.uint32, "maximum-v6-routes")

        self.relay_adv_add = None
        self._children_name_map["relay_adv_add"] = "relay-adv-add"
        self._children_yang_names.add("relay-adv-add")

        self.relay_anycast_prefix = None
        self._children_name_map["relay_anycast_prefix"] = "relay-anycast-prefix"
        self._children_yang_names.add("relay-anycast-prefix")
        self._segment_path = lambda: "Cisco-IOS-XR-ipv4-igmp-cfg:amt"

    def __setattr__(self, name, value):
        self._perform_setattr(Amt, ['amtmtu', 'amtqqic', 'amttos', 'amtttl', 'gateway_filter', 'maximum_gateway', 'maximum_v4_route_gateway', 'maximum_v4_routes', 'maximum_v6_route_gateway', 'maximum_v6_routes'], name, value)


    class RelayAdvAdd(Entity):
        """
        Configure AMT Relay IPv4 Advertisement Address
        
        .. attribute:: address
        
        	AMT Relay IPv4 Advertisement Address
        	**type**\:  str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        	**mandatory**\: True
        
        .. attribute:: interface
        
        	Relay Advertisement Interface
        	**type**\:  str
        
        	**pattern:** [a\-zA\-Z0\-9./\-]+
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'ipv4-igmp-cfg'
        _revision = '2016-10-10'

        def __init__(self):
            super(Amt.RelayAdvAdd, self).__init__()

            self.yang_name = "relay-adv-add"
            self.yang_parent_name = "amt"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}
            self.is_presence_container = True

            self.address = YLeaf(YType.str, "address")

            self.interface = YLeaf(YType.str, "interface")
            self._segment_path = lambda: "relay-adv-add"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-igmp-cfg:amt/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Amt.RelayAdvAdd, ['address', 'interface'], name, value)


    class RelayAnycastPrefix(Entity):
        """
        Configure AMT Relay IPv4 Anycast\-Prefix
        
        .. attribute:: address
        
        	Anycast\-Prefix Address
        	**type**\:  str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        	**mandatory**\: True
        
        .. attribute:: prefix_length
        
        	Mask Length for Anycast Prefix
        	**type**\:  int
        
        	**range:** 1..32
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'ipv4-igmp-cfg'
        _revision = '2016-10-10'

        def __init__(self):
            super(Amt.RelayAnycastPrefix, self).__init__()

            self.yang_name = "relay-anycast-prefix"
            self.yang_parent_name = "amt"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}
            self.is_presence_container = True

            self.address = YLeaf(YType.str, "address")

            self.prefix_length = YLeaf(YType.uint32, "prefix-length")
            self._segment_path = lambda: "relay-anycast-prefix"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-igmp-cfg:amt/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Amt.RelayAnycastPrefix, ['address', 'prefix_length'], name, value)

    def clone_ptr(self):
        self._top_entity = Amt()
        return self._top_entity

class Igmp(Entity):
    """
    IGMPconfiguration
    
    .. attribute:: default_context
    
    	Default Context
    	**type**\:   :py:class:`DefaultContext <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext>`
    
    	**presence node**\: True
    
    .. attribute:: vrfs
    
    	VRF related configuration
    	**type**\:   :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.Vrfs>`
    
    

    This class is a :ref:`presence class<presence-class>`

    """

    _prefix = 'ipv4-igmp-cfg'
    _revision = '2016-10-10'

    def __init__(self):
        super(Igmp, self).__init__()
        self._top_entity = None

        self.yang_name = "igmp"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-igmp-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"default-context" : ("default_context", Igmp.DefaultContext), "vrfs" : ("vrfs", Igmp.Vrfs)}
        self._child_list_classes = {}
        self.is_presence_container = True

        self.default_context = None
        self._children_name_map["default_context"] = "default-context"
        self._children_yang_names.add("default-context")

        self.vrfs = Igmp.Vrfs()
        self.vrfs.parent = self
        self._children_name_map["vrfs"] = "vrfs"
        self._children_yang_names.add("vrfs")
        self._segment_path = lambda: "Cisco-IOS-XR-ipv4-igmp-cfg:igmp"


    class DefaultContext(Entity):
        """
        Default Context
        
        .. attribute:: accounting
        
        	Configure IGMP accounting for logging join/leave records
        	**type**\:   :py:class:`Accounting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext.Accounting>`
        
        .. attribute:: inheritable_defaults
        
        	Inheritable Defaults
        	**type**\:   :py:class:`InheritableDefaults <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext.InheritableDefaults>`
        
        .. attribute:: interfaces
        
        	Interface\-level configuration
        	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext.Interfaces>`
        
        .. attribute:: maximum
        
        	Configure IGMP State Limits
        	**type**\:   :py:class:`Maximum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext.Maximum>`
        
        .. attribute:: nsf
        
        	Configure NSF specific options
        	**type**\:   :py:class:`Nsf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext.Nsf>`
        
        .. attribute:: robustness
        
        	Configure IGMP Robustness variable
        	**type**\:  int
        
        	**range:** 2..10
        
        	**default value**\: 2
        
        .. attribute:: ssm_access_groups
        
        	IGMP Source specific mode
        	**type**\:   :py:class:`SsmAccessGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext.SsmAccessGroups>`
        
        .. attribute:: ssmdns_query_group
        
        	Enable SSM mapping using DNS Query
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: traffic
        
        	Configure IGMP Traffic variables
        	**type**\:   :py:class:`Traffic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext.Traffic>`
        
        .. attribute:: unicast_qos_adjust
        
        	Configure IGMP QoS shapers for subscriber interfaces
        	**type**\:   :py:class:`UnicastQosAdjust <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext.UnicastQosAdjust>`
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'ipv4-igmp-cfg'
        _revision = '2016-10-10'

        def __init__(self):
            super(Igmp.DefaultContext, self).__init__()

            self.yang_name = "default-context"
            self.yang_parent_name = "igmp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"accounting" : ("accounting", Igmp.DefaultContext.Accounting), "inheritable-defaults" : ("inheritable_defaults", Igmp.DefaultContext.InheritableDefaults), "interfaces" : ("interfaces", Igmp.DefaultContext.Interfaces), "maximum" : ("maximum", Igmp.DefaultContext.Maximum), "nsf" : ("nsf", Igmp.DefaultContext.Nsf), "ssm-access-groups" : ("ssm_access_groups", Igmp.DefaultContext.SsmAccessGroups), "traffic" : ("traffic", Igmp.DefaultContext.Traffic), "unicast-qos-adjust" : ("unicast_qos_adjust", Igmp.DefaultContext.UnicastQosAdjust)}
            self._child_list_classes = {}
            self.is_presence_container = True

            self.robustness = YLeaf(YType.uint32, "robustness")

            self.ssmdns_query_group = YLeaf(YType.empty, "ssmdns-query-group")

            self.accounting = Igmp.DefaultContext.Accounting()
            self.accounting.parent = self
            self._children_name_map["accounting"] = "accounting"
            self._children_yang_names.add("accounting")

            self.inheritable_defaults = Igmp.DefaultContext.InheritableDefaults()
            self.inheritable_defaults.parent = self
            self._children_name_map["inheritable_defaults"] = "inheritable-defaults"
            self._children_yang_names.add("inheritable-defaults")

            self.interfaces = Igmp.DefaultContext.Interfaces()
            self.interfaces.parent = self
            self._children_name_map["interfaces"] = "interfaces"
            self._children_yang_names.add("interfaces")

            self.maximum = Igmp.DefaultContext.Maximum()
            self.maximum.parent = self
            self._children_name_map["maximum"] = "maximum"
            self._children_yang_names.add("maximum")

            self.nsf = Igmp.DefaultContext.Nsf()
            self.nsf.parent = self
            self._children_name_map["nsf"] = "nsf"
            self._children_yang_names.add("nsf")

            self.ssm_access_groups = Igmp.DefaultContext.SsmAccessGroups()
            self.ssm_access_groups.parent = self
            self._children_name_map["ssm_access_groups"] = "ssm-access-groups"
            self._children_yang_names.add("ssm-access-groups")

            self.traffic = Igmp.DefaultContext.Traffic()
            self.traffic.parent = self
            self._children_name_map["traffic"] = "traffic"
            self._children_yang_names.add("traffic")

            self.unicast_qos_adjust = Igmp.DefaultContext.UnicastQosAdjust()
            self.unicast_qos_adjust.parent = self
            self._children_name_map["unicast_qos_adjust"] = "unicast-qos-adjust"
            self._children_yang_names.add("unicast-qos-adjust")
            self._segment_path = lambda: "default-context"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-igmp-cfg:igmp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Igmp.DefaultContext, ['robustness', 'ssmdns_query_group'], name, value)


        class Accounting(Entity):
            """
            Configure IGMP accounting for logging
            join/leave records
            
            .. attribute:: max_history
            
            	Configure IGMP accounting Maximum History setting
            	**type**\:  int
            
            	**range:** 0..365
            
            	**units**\: day
            
            	**default value**\: 0
            
            

            """

            _prefix = 'ipv4-igmp-cfg'
            _revision = '2016-10-10'

            def __init__(self):
                super(Igmp.DefaultContext.Accounting, self).__init__()

                self.yang_name = "accounting"
                self.yang_parent_name = "default-context"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.max_history = YLeaf(YType.uint32, "max-history")
                self._segment_path = lambda: "accounting"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-igmp-cfg:igmp/default-context/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Igmp.DefaultContext.Accounting, ['max_history'], name, value)


        class InheritableDefaults(Entity):
            """
            Inheritable Defaults
            
            .. attribute:: access_group
            
            	Access list specifying access group range
            	**type**\:  str
            
            	**length:** 1..64
            
            .. attribute:: explicit_tracking
            
            	IGMPv3 explicit host tracking
            	**type**\:   :py:class:`ExplicitTracking <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext.InheritableDefaults.ExplicitTracking>`
            
            	**presence node**\: True
            
            .. attribute:: maximum_groups_per_interface_oor
            
            	Configure maximum number of groups accepted per interface by this router
            	**type**\:   :py:class:`MaximumGroupsPerInterfaceOor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext.InheritableDefaults.MaximumGroupsPerInterfaceOor>`
            
            	**presence node**\: True
            
            .. attribute:: query_interval
            
            	Query interval in seconds
            	**type**\:  int
            
            	**range:** 1..3600
            
            	**units**\: second
            
            	**default value**\: 60
            
            .. attribute:: query_max_response_time
            
            	Query response value in seconds
            	**type**\:  int
            
            	**range:** 1..12
            
            	**units**\: second
            
            	**default value**\: 10
            
            .. attribute:: query_timeout
            
            	IGMP previous querier timeout
            	**type**\:  int
            
            	**range:** 60..300
            
            	**units**\: second
            
            .. attribute:: router_enable
            
            	Enabled or disabled, when value is TRUE or FALSE respectively
            	**type**\:  bool
            
            	**default value**\: true
            
            .. attribute:: version
            
            	Version number
            	**type**\:  int
            
            	**range:** 1..3
            
            	**default value**\: 3
            
            

            """

            _prefix = 'ipv4-igmp-cfg'
            _revision = '2016-10-10'

            def __init__(self):
                super(Igmp.DefaultContext.InheritableDefaults, self).__init__()

                self.yang_name = "inheritable-defaults"
                self.yang_parent_name = "default-context"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"explicit-tracking" : ("explicit_tracking", Igmp.DefaultContext.InheritableDefaults.ExplicitTracking), "maximum-groups-per-interface-oor" : ("maximum_groups_per_interface_oor", Igmp.DefaultContext.InheritableDefaults.MaximumGroupsPerInterfaceOor)}
                self._child_list_classes = {}

                self.access_group = YLeaf(YType.str, "access-group")

                self.query_interval = YLeaf(YType.uint32, "query-interval")

                self.query_max_response_time = YLeaf(YType.uint32, "query-max-response-time")

                self.query_timeout = YLeaf(YType.uint32, "query-timeout")

                self.router_enable = YLeaf(YType.boolean, "router-enable")

                self.version = YLeaf(YType.uint32, "version")

                self.explicit_tracking = None
                self._children_name_map["explicit_tracking"] = "explicit-tracking"
                self._children_yang_names.add("explicit-tracking")

                self.maximum_groups_per_interface_oor = None
                self._children_name_map["maximum_groups_per_interface_oor"] = "maximum-groups-per-interface-oor"
                self._children_yang_names.add("maximum-groups-per-interface-oor")
                self._segment_path = lambda: "inheritable-defaults"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-igmp-cfg:igmp/default-context/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Igmp.DefaultContext.InheritableDefaults, ['access_group', 'query_interval', 'query_max_response_time', 'query_timeout', 'router_enable', 'version'], name, value)


            class ExplicitTracking(Entity):
                """
                IGMPv3 explicit host tracking
                
                .. attribute:: access_list_name
                
                	Access list specifying tracking group range
                	**type**\:  str
                
                	**length:** 1..64
                
                .. attribute:: enable
                
                	Enabled or disabled, when value is TRUE or FALSE respectively
                	**type**\:  bool
                
                	**mandatory**\: True
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'ipv4-igmp-cfg'
                _revision = '2016-10-10'

                def __init__(self):
                    super(Igmp.DefaultContext.InheritableDefaults.ExplicitTracking, self).__init__()

                    self.yang_name = "explicit-tracking"
                    self.yang_parent_name = "inheritable-defaults"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}
                    self.is_presence_container = True

                    self.access_list_name = YLeaf(YType.str, "access-list-name")

                    self.enable = YLeaf(YType.boolean, "enable")
                    self._segment_path = lambda: "explicit-tracking"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-igmp-cfg:igmp/default-context/inheritable-defaults/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Igmp.DefaultContext.InheritableDefaults.ExplicitTracking, ['access_list_name', 'enable'], name, value)


            class MaximumGroupsPerInterfaceOor(Entity):
                """
                Configure maximum number of groups accepted per
                interface by this router
                
                .. attribute:: access_list_name
                
                	Access\-list to account for
                	**type**\:  str
                
                	**length:** 1..64
                
                .. attribute:: maximum_groups
                
                	Maximum number of groups accepted per interface by this router
                	**type**\:  int
                
                	**range:** 1..40000
                
                	**mandatory**\: True
                
                .. attribute:: warning_threshold
                
                	 WarningThreshold for number of groups accepted per interface by this router
                	**type**\:  int
                
                	**range:** 1..40000
                
                	**default value**\: 25000
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'ipv4-igmp-cfg'
                _revision = '2016-10-10'

                def __init__(self):
                    super(Igmp.DefaultContext.InheritableDefaults.MaximumGroupsPerInterfaceOor, self).__init__()

                    self.yang_name = "maximum-groups-per-interface-oor"
                    self.yang_parent_name = "inheritable-defaults"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}
                    self.is_presence_container = True

                    self.access_list_name = YLeaf(YType.str, "access-list-name")

                    self.maximum_groups = YLeaf(YType.uint32, "maximum-groups")

                    self.warning_threshold = YLeaf(YType.uint32, "warning-threshold")
                    self._segment_path = lambda: "maximum-groups-per-interface-oor"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-igmp-cfg:igmp/default-context/inheritable-defaults/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Igmp.DefaultContext.InheritableDefaults.MaximumGroupsPerInterfaceOor, ['access_list_name', 'maximum_groups', 'warning_threshold'], name, value)


        class Interfaces(Entity):
            """
            Interface\-level configuration
            
            .. attribute:: interface
            
            	The name of the interface
            	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext.Interfaces.Interface>`
            
            

            """

            _prefix = 'ipv4-igmp-cfg'
            _revision = '2016-10-10'

            def __init__(self):
                super(Igmp.DefaultContext.Interfaces, self).__init__()

                self.yang_name = "interfaces"
                self.yang_parent_name = "default-context"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"interface" : ("interface", Igmp.DefaultContext.Interfaces.Interface)}

                self.interface = YList(self)
                self._segment_path = lambda: "interfaces"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-igmp-cfg:igmp/default-context/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Igmp.DefaultContext.Interfaces, [], name, value)


            class Interface(Entity):
                """
                The name of the interface
                
                .. attribute:: interface_name  <key>
                
                	Name of the interface
                	**type**\:  str
                
                	**pattern:** [a\-zA\-Z0\-9./\-]+
                
                .. attribute:: access_group
                
                	Access list specifying access group range
                	**type**\:  str
                
                	**length:** 1..64
                
                .. attribute:: explicit_tracking
                
                	IGMPv3 explicit host tracking
                	**type**\:   :py:class:`ExplicitTracking <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext.Interfaces.Interface.ExplicitTracking>`
                
                	**presence node**\: True
                
                .. attribute:: join_groups
                
                	IGMP join multicast group
                	**type**\:   :py:class:`JoinGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext.Interfaces.Interface.JoinGroups>`
                
                	**presence node**\: True
                
                .. attribute:: maximum_groups_per_interface_oor
                
                	Configure maximum number of groups accepted per interface by this router
                	**type**\:   :py:class:`MaximumGroupsPerInterfaceOor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext.Interfaces.Interface.MaximumGroupsPerInterfaceOor>`
                
                	**presence node**\: True
                
                .. attribute:: query_interval
                
                	Query interval in seconds
                	**type**\:  int
                
                	**range:** 1..3600
                
                	**units**\: second
                
                	**default value**\: 60
                
                .. attribute:: query_max_response_time
                
                	Query response value in seconds
                	**type**\:  int
                
                	**range:** 1..12
                
                	**units**\: second
                
                	**default value**\: 10
                
                .. attribute:: query_timeout
                
                	IGMP previous querier timeout
                	**type**\:  int
                
                	**range:** 60..300
                
                	**units**\: second
                
                .. attribute:: router_enable
                
                	Enabled or disabled, when value is TRUE or FALSE respectively
                	**type**\:  bool
                
                	**default value**\: true
                
                .. attribute:: static_group_group_addresses
                
                	IGMP static multicast group
                	**type**\:   :py:class:`StaticGroupGroupAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses>`
                
                .. attribute:: version
                
                	Version number
                	**type**\:  int
                
                	**range:** 1..3
                
                	**default value**\: 3
                
                

                """

                _prefix = 'ipv4-igmp-cfg'
                _revision = '2016-10-10'

                def __init__(self):
                    super(Igmp.DefaultContext.Interfaces.Interface, self).__init__()

                    self.yang_name = "interface"
                    self.yang_parent_name = "interfaces"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"explicit-tracking" : ("explicit_tracking", Igmp.DefaultContext.Interfaces.Interface.ExplicitTracking), "join-groups" : ("join_groups", Igmp.DefaultContext.Interfaces.Interface.JoinGroups), "maximum-groups-per-interface-oor" : ("maximum_groups_per_interface_oor", Igmp.DefaultContext.Interfaces.Interface.MaximumGroupsPerInterfaceOor), "static-group-group-addresses" : ("static_group_group_addresses", Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses)}
                    self._child_list_classes = {}

                    self.interface_name = YLeaf(YType.str, "interface-name")

                    self.access_group = YLeaf(YType.str, "access-group")

                    self.query_interval = YLeaf(YType.uint32, "query-interval")

                    self.query_max_response_time = YLeaf(YType.uint32, "query-max-response-time")

                    self.query_timeout = YLeaf(YType.uint32, "query-timeout")

                    self.router_enable = YLeaf(YType.boolean, "router-enable")

                    self.version = YLeaf(YType.uint32, "version")

                    self.explicit_tracking = None
                    self._children_name_map["explicit_tracking"] = "explicit-tracking"
                    self._children_yang_names.add("explicit-tracking")

                    self.join_groups = None
                    self._children_name_map["join_groups"] = "join-groups"
                    self._children_yang_names.add("join-groups")

                    self.maximum_groups_per_interface_oor = None
                    self._children_name_map["maximum_groups_per_interface_oor"] = "maximum-groups-per-interface-oor"
                    self._children_yang_names.add("maximum-groups-per-interface-oor")

                    self.static_group_group_addresses = Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses()
                    self.static_group_group_addresses.parent = self
                    self._children_name_map["static_group_group_addresses"] = "static-group-group-addresses"
                    self._children_yang_names.add("static-group-group-addresses")
                    self._segment_path = lambda: "interface" + "[interface-name='" + self.interface_name.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-igmp-cfg:igmp/default-context/interfaces/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Igmp.DefaultContext.Interfaces.Interface, ['interface_name', 'access_group', 'query_interval', 'query_max_response_time', 'query_timeout', 'router_enable', 'version'], name, value)


                class ExplicitTracking(Entity):
                    """
                    IGMPv3 explicit host tracking
                    
                    .. attribute:: access_list_name
                    
                    	Access list specifying tracking group range
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    .. attribute:: enable
                    
                    	Enabled or disabled, when value is TRUE or FALSE respectively
                    	**type**\:  bool
                    
                    	**mandatory**\: True
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-igmp-cfg'
                    _revision = '2016-10-10'

                    def __init__(self):
                        super(Igmp.DefaultContext.Interfaces.Interface.ExplicitTracking, self).__init__()

                        self.yang_name = "explicit-tracking"
                        self.yang_parent_name = "interface"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}
                        self.is_presence_container = True

                        self.access_list_name = YLeaf(YType.str, "access-list-name")

                        self.enable = YLeaf(YType.boolean, "enable")
                        self._segment_path = lambda: "explicit-tracking"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Igmp.DefaultContext.Interfaces.Interface.ExplicitTracking, ['access_list_name', 'enable'], name, value)


                class JoinGroups(Entity):
                    """
                    IGMP join multicast group
                    
                    .. attribute:: join_group
                    
                    	IP group address and optional source address to include
                    	**type**\: list of    :py:class:`JoinGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext.Interfaces.Interface.JoinGroups.JoinGroup>`
                    
                    .. attribute:: join_group_source_address
                    
                    	IP group address and optional source address to include
                    	**type**\: list of    :py:class:`JoinGroupSourceAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext.Interfaces.Interface.JoinGroups.JoinGroupSourceAddress>`
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-igmp-cfg'
                    _revision = '2016-10-10'

                    def __init__(self):
                        super(Igmp.DefaultContext.Interfaces.Interface.JoinGroups, self).__init__()

                        self.yang_name = "join-groups"
                        self.yang_parent_name = "interface"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"join-group" : ("join_group", Igmp.DefaultContext.Interfaces.Interface.JoinGroups.JoinGroup), "join-group-source-address" : ("join_group_source_address", Igmp.DefaultContext.Interfaces.Interface.JoinGroups.JoinGroupSourceAddress)}
                        self.is_presence_container = True

                        self.join_group = YList(self)
                        self.join_group_source_address = YList(self)
                        self._segment_path = lambda: "join-groups"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Igmp.DefaultContext.Interfaces.Interface.JoinGroups, [], name, value)


                    class JoinGroup(Entity):
                        """
                        IP group address and optional source address
                        to include
                        
                        .. attribute:: group_address  <key>
                        
                        	IP group address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: mode
                        
                        	Filter mode
                        	**type**\:   :py:class:`IgmpFilter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.IgmpFilter>`
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2016-10-10'

                        def __init__(self):
                            super(Igmp.DefaultContext.Interfaces.Interface.JoinGroups.JoinGroup, self).__init__()

                            self.yang_name = "join-group"
                            self.yang_parent_name = "join-groups"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.group_address = YLeaf(YType.str, "group-address")

                            self.mode = YLeaf(YType.enumeration, "mode")
                            self._segment_path = lambda: "join-group" + "[group-address='" + self.group_address.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Igmp.DefaultContext.Interfaces.Interface.JoinGroups.JoinGroup, ['group_address', 'mode'], name, value)


                    class JoinGroupSourceAddress(Entity):
                        """
                        IP group address and optional source address
                        to include
                        
                        .. attribute:: group_address  <key>
                        
                        	IP group address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: source_address  <key>
                        
                        	Optional IP source address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: mode
                        
                        	Filter mode
                        	**type**\:   :py:class:`IgmpFilter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.IgmpFilter>`
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2016-10-10'

                        def __init__(self):
                            super(Igmp.DefaultContext.Interfaces.Interface.JoinGroups.JoinGroupSourceAddress, self).__init__()

                            self.yang_name = "join-group-source-address"
                            self.yang_parent_name = "join-groups"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.group_address = YLeaf(YType.str, "group-address")

                            self.source_address = YLeaf(YType.str, "source-address")

                            self.mode = YLeaf(YType.enumeration, "mode")
                            self._segment_path = lambda: "join-group-source-address" + "[group-address='" + self.group_address.get() + "']" + "[source-address='" + self.source_address.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Igmp.DefaultContext.Interfaces.Interface.JoinGroups.JoinGroupSourceAddress, ['group_address', 'source_address', 'mode'], name, value)


                class MaximumGroupsPerInterfaceOor(Entity):
                    """
                    Configure maximum number of groups accepted per
                    interface by this router
                    
                    .. attribute:: access_list_name
                    
                    	Access\-list to account for
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    .. attribute:: maximum_groups
                    
                    	Maximum number of groups accepted per interface by this router
                    	**type**\:  int
                    
                    	**range:** 1..40000
                    
                    	**mandatory**\: True
                    
                    .. attribute:: warning_threshold
                    
                    	 WarningThreshold for number of groups accepted per interface by this router
                    	**type**\:  int
                    
                    	**range:** 1..40000
                    
                    	**default value**\: 25000
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-igmp-cfg'
                    _revision = '2016-10-10'

                    def __init__(self):
                        super(Igmp.DefaultContext.Interfaces.Interface.MaximumGroupsPerInterfaceOor, self).__init__()

                        self.yang_name = "maximum-groups-per-interface-oor"
                        self.yang_parent_name = "interface"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}
                        self.is_presence_container = True

                        self.access_list_name = YLeaf(YType.str, "access-list-name")

                        self.maximum_groups = YLeaf(YType.uint32, "maximum-groups")

                        self.warning_threshold = YLeaf(YType.uint32, "warning-threshold")
                        self._segment_path = lambda: "maximum-groups-per-interface-oor"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Igmp.DefaultContext.Interfaces.Interface.MaximumGroupsPerInterfaceOor, ['access_list_name', 'maximum_groups', 'warning_threshold'], name, value)


                class StaticGroupGroupAddresses(Entity):
                    """
                    IGMP static multicast group
                    
                    .. attribute:: static_group_group_address
                    
                    	IP group address and optional source address to include
                    	**type**\: list of    :py:class:`StaticGroupGroupAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddress>`
                    
                    .. attribute:: static_group_group_address_group_address_mask
                    
                    	IP group address and optional source address to include
                    	**type**\: list of    :py:class:`StaticGroupGroupAddressGroupAddressMask <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMask>`
                    
                    .. attribute:: static_group_group_address_group_address_mask_source_address
                    
                    	IP group address and optional source address to include
                    	**type**\: list of    :py:class:`StaticGroupGroupAddressGroupAddressMaskSourceAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddress>`
                    
                    .. attribute:: static_group_group_address_group_address_mask_source_address_source_address_mask
                    
                    	IP group address and optional source address to include
                    	**type**\: list of    :py:class:`StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask>`
                    
                    .. attribute:: static_group_group_address_source_address
                    
                    	IP group address and optional source address to include
                    	**type**\: list of    :py:class:`StaticGroupGroupAddressSourceAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddress>`
                    
                    .. attribute:: static_group_group_address_source_address_source_address_mask
                    
                    	IP group address and optional source address to include
                    	**type**\: list of    :py:class:`StaticGroupGroupAddressSourceAddressSourceAddressMask <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddressSourceAddressMask>`
                    
                    

                    """

                    _prefix = 'ipv4-igmp-cfg'
                    _revision = '2016-10-10'

                    def __init__(self):
                        super(Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses, self).__init__()

                        self.yang_name = "static-group-group-addresses"
                        self.yang_parent_name = "interface"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"static-group-group-address" : ("static_group_group_address", Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddress), "static-group-group-address-group-address-mask" : ("static_group_group_address_group_address_mask", Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMask), "static-group-group-address-group-address-mask-source-address" : ("static_group_group_address_group_address_mask_source_address", Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddress), "static-group-group-address-group-address-mask-source-address-source-address-mask" : ("static_group_group_address_group_address_mask_source_address_source_address_mask", Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask), "static-group-group-address-source-address" : ("static_group_group_address_source_address", Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddress), "static-group-group-address-source-address-source-address-mask" : ("static_group_group_address_source_address_source_address_mask", Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddressSourceAddressMask)}

                        self.static_group_group_address = YList(self)
                        self.static_group_group_address_group_address_mask = YList(self)
                        self.static_group_group_address_group_address_mask_source_address = YList(self)
                        self.static_group_group_address_group_address_mask_source_address_source_address_mask = YList(self)
                        self.static_group_group_address_source_address = YList(self)
                        self.static_group_group_address_source_address_source_address_mask = YList(self)
                        self._segment_path = lambda: "static-group-group-addresses"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses, [], name, value)


                    class StaticGroupGroupAddress(Entity):
                        """
                        IP group address and optional source address
                        to include
                        
                        .. attribute:: group_address  <key>
                        
                        	IP group address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: group_count
                        
                        	Number of groups to join (do not set without GroupAddressMask)
                        	**type**\:  int
                        
                        	**range:** 1..512
                        
                        	**default value**\: 1
                        
                        .. attribute:: source_count
                        
                        	Number of sources to join (do not set without SourceAddressMask)
                        	**type**\:  int
                        
                        	**range:** 1..512
                        
                        	**default value**\: 1
                        
                        .. attribute:: suppress_report
                        
                        	Suppress reports
                        	**type**\:  bool
                        
                        	**default value**\: false
                        
                        

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2016-10-10'

                        def __init__(self):
                            super(Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddress, self).__init__()

                            self.yang_name = "static-group-group-address"
                            self.yang_parent_name = "static-group-group-addresses"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.group_address = YLeaf(YType.str, "group-address")

                            self.group_count = YLeaf(YType.uint32, "group-count")

                            self.source_count = YLeaf(YType.uint32, "source-count")

                            self.suppress_report = YLeaf(YType.boolean, "suppress-report")
                            self._segment_path = lambda: "static-group-group-address" + "[group-address='" + self.group_address.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddress, ['group_address', 'group_count', 'source_count', 'suppress_report'], name, value)


                    class StaticGroupGroupAddressGroupAddressMask(Entity):
                        """
                        IP group address and optional source address
                        to include
                        
                        .. attribute:: group_address  <key>
                        
                        	IP group address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: group_address_mask  <key>
                        
                        	Mask for Group Address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: group_count
                        
                        	Number of groups to join (do not set without GroupAddressMask)
                        	**type**\:  int
                        
                        	**range:** 1..512
                        
                        	**default value**\: 1
                        
                        .. attribute:: source_count
                        
                        	Number of sources to join (do not set without SourceAddressMask)
                        	**type**\:  int
                        
                        	**range:** 1..512
                        
                        	**default value**\: 1
                        
                        .. attribute:: suppress_report
                        
                        	Suppress reports
                        	**type**\:  bool
                        
                        	**default value**\: false
                        
                        

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2016-10-10'

                        def __init__(self):
                            super(Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMask, self).__init__()

                            self.yang_name = "static-group-group-address-group-address-mask"
                            self.yang_parent_name = "static-group-group-addresses"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.group_address = YLeaf(YType.str, "group-address")

                            self.group_address_mask = YLeaf(YType.str, "group-address-mask")

                            self.group_count = YLeaf(YType.uint32, "group-count")

                            self.source_count = YLeaf(YType.uint32, "source-count")

                            self.suppress_report = YLeaf(YType.boolean, "suppress-report")
                            self._segment_path = lambda: "static-group-group-address-group-address-mask" + "[group-address='" + self.group_address.get() + "']" + "[group-address-mask='" + self.group_address_mask.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMask, ['group_address', 'group_address_mask', 'group_count', 'source_count', 'suppress_report'], name, value)


                    class StaticGroupGroupAddressGroupAddressMaskSourceAddress(Entity):
                        """
                        IP group address and optional source address
                        to include
                        
                        .. attribute:: group_address  <key>
                        
                        	IP group address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: group_address_mask  <key>
                        
                        	Mask for Group Address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: source_address  <key>
                        
                        	IP source address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: group_count
                        
                        	Number of groups to join (do not set without GroupAddressMask)
                        	**type**\:  int
                        
                        	**range:** 1..512
                        
                        	**default value**\: 1
                        
                        .. attribute:: source_count
                        
                        	Number of sources to join (do not set without SourceAddressMask)
                        	**type**\:  int
                        
                        	**range:** 1..512
                        
                        	**default value**\: 1
                        
                        .. attribute:: suppress_report
                        
                        	Suppress reports
                        	**type**\:  bool
                        
                        	**default value**\: false
                        
                        

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2016-10-10'

                        def __init__(self):
                            super(Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddress, self).__init__()

                            self.yang_name = "static-group-group-address-group-address-mask-source-address"
                            self.yang_parent_name = "static-group-group-addresses"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.group_address = YLeaf(YType.str, "group-address")

                            self.group_address_mask = YLeaf(YType.str, "group-address-mask")

                            self.source_address = YLeaf(YType.str, "source-address")

                            self.group_count = YLeaf(YType.uint32, "group-count")

                            self.source_count = YLeaf(YType.uint32, "source-count")

                            self.suppress_report = YLeaf(YType.boolean, "suppress-report")
                            self._segment_path = lambda: "static-group-group-address-group-address-mask-source-address" + "[group-address='" + self.group_address.get() + "']" + "[group-address-mask='" + self.group_address_mask.get() + "']" + "[source-address='" + self.source_address.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddress, ['group_address', 'group_address_mask', 'source_address', 'group_count', 'source_count', 'suppress_report'], name, value)


                    class StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask(Entity):
                        """
                        IP group address and optional source address
                        to include
                        
                        .. attribute:: group_address  <key>
                        
                        	IP group address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: group_address_mask  <key>
                        
                        	Mask for Group Address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: source_address  <key>
                        
                        	IP source address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: source_address_mask  <key>
                        
                        	Mask for Source Address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: group_count
                        
                        	Number of groups to join (do not set without GroupAddressMask)
                        	**type**\:  int
                        
                        	**range:** 1..512
                        
                        	**default value**\: 1
                        
                        .. attribute:: source_count
                        
                        	Number of sources to join (do not set without SourceAddressMask)
                        	**type**\:  int
                        
                        	**range:** 1..512
                        
                        	**default value**\: 1
                        
                        .. attribute:: suppress_report
                        
                        	Suppress reports
                        	**type**\:  bool
                        
                        	**default value**\: false
                        
                        

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2016-10-10'

                        def __init__(self):
                            super(Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask, self).__init__()

                            self.yang_name = "static-group-group-address-group-address-mask-source-address-source-address-mask"
                            self.yang_parent_name = "static-group-group-addresses"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.group_address = YLeaf(YType.str, "group-address")

                            self.group_address_mask = YLeaf(YType.str, "group-address-mask")

                            self.source_address = YLeaf(YType.str, "source-address")

                            self.source_address_mask = YLeaf(YType.str, "source-address-mask")

                            self.group_count = YLeaf(YType.uint32, "group-count")

                            self.source_count = YLeaf(YType.uint32, "source-count")

                            self.suppress_report = YLeaf(YType.boolean, "suppress-report")
                            self._segment_path = lambda: "static-group-group-address-group-address-mask-source-address-source-address-mask" + "[group-address='" + self.group_address.get() + "']" + "[group-address-mask='" + self.group_address_mask.get() + "']" + "[source-address='" + self.source_address.get() + "']" + "[source-address-mask='" + self.source_address_mask.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask, ['group_address', 'group_address_mask', 'source_address', 'source_address_mask', 'group_count', 'source_count', 'suppress_report'], name, value)


                    class StaticGroupGroupAddressSourceAddress(Entity):
                        """
                        IP group address and optional source address
                        to include
                        
                        .. attribute:: group_address  <key>
                        
                        	IP group address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: source_address  <key>
                        
                        	IP source address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: group_count
                        
                        	Number of groups to join (do not set without GroupAddressMask)
                        	**type**\:  int
                        
                        	**range:** 1..512
                        
                        	**default value**\: 1
                        
                        .. attribute:: source_count
                        
                        	Number of sources to join (do not set without SourceAddressMask)
                        	**type**\:  int
                        
                        	**range:** 1..512
                        
                        	**default value**\: 1
                        
                        .. attribute:: suppress_report
                        
                        	Suppress reports
                        	**type**\:  bool
                        
                        	**default value**\: false
                        
                        

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2016-10-10'

                        def __init__(self):
                            super(Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddress, self).__init__()

                            self.yang_name = "static-group-group-address-source-address"
                            self.yang_parent_name = "static-group-group-addresses"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.group_address = YLeaf(YType.str, "group-address")

                            self.source_address = YLeaf(YType.str, "source-address")

                            self.group_count = YLeaf(YType.uint32, "group-count")

                            self.source_count = YLeaf(YType.uint32, "source-count")

                            self.suppress_report = YLeaf(YType.boolean, "suppress-report")
                            self._segment_path = lambda: "static-group-group-address-source-address" + "[group-address='" + self.group_address.get() + "']" + "[source-address='" + self.source_address.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddress, ['group_address', 'source_address', 'group_count', 'source_count', 'suppress_report'], name, value)


                    class StaticGroupGroupAddressSourceAddressSourceAddressMask(Entity):
                        """
                        IP group address and optional source address
                        to include
                        
                        .. attribute:: group_address  <key>
                        
                        	IP group address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: source_address  <key>
                        
                        	IP source address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: source_address_mask  <key>
                        
                        	Mask for Source Address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: group_count
                        
                        	Number of groups to join (do not set without GroupAddressMask)
                        	**type**\:  int
                        
                        	**range:** 1..512
                        
                        	**default value**\: 1
                        
                        .. attribute:: source_count
                        
                        	Number of sources to join (do not set without SourceAddressMask)
                        	**type**\:  int
                        
                        	**range:** 1..512
                        
                        	**default value**\: 1
                        
                        .. attribute:: suppress_report
                        
                        	Suppress reports
                        	**type**\:  bool
                        
                        	**default value**\: false
                        
                        

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2016-10-10'

                        def __init__(self):
                            super(Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddressSourceAddressMask, self).__init__()

                            self.yang_name = "static-group-group-address-source-address-source-address-mask"
                            self.yang_parent_name = "static-group-group-addresses"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.group_address = YLeaf(YType.str, "group-address")

                            self.source_address = YLeaf(YType.str, "source-address")

                            self.source_address_mask = YLeaf(YType.str, "source-address-mask")

                            self.group_count = YLeaf(YType.uint32, "group-count")

                            self.source_count = YLeaf(YType.uint32, "source-count")

                            self.suppress_report = YLeaf(YType.boolean, "suppress-report")
                            self._segment_path = lambda: "static-group-group-address-source-address-source-address-mask" + "[group-address='" + self.group_address.get() + "']" + "[source-address='" + self.source_address.get() + "']" + "[source-address-mask='" + self.source_address_mask.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddressSourceAddressMask, ['group_address', 'source_address', 'source_address_mask', 'group_count', 'source_count', 'suppress_report'], name, value)


        class Maximum(Entity):
            """
            Configure IGMP State Limits
            
            .. attribute:: maximum_groups
            
            	Configure maximum number of groups accepted by this router
            	**type**\:  int
            
            	**range:** 1..75000
            
            	**default value**\: 50000
            
            

            """

            _prefix = 'ipv4-igmp-cfg'
            _revision = '2016-10-10'

            def __init__(self):
                super(Igmp.DefaultContext.Maximum, self).__init__()

                self.yang_name = "maximum"
                self.yang_parent_name = "default-context"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.maximum_groups = YLeaf(YType.uint32, "maximum-groups")
                self._segment_path = lambda: "maximum"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-igmp-cfg:igmp/default-context/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Igmp.DefaultContext.Maximum, ['maximum_groups'], name, value)


        class Nsf(Entity):
            """
            Configure NSF specific options
            
            .. attribute:: lifetime
            
            	Maximum time for IGMP NSF mode in seconds
            	**type**\:  int
            
            	**range:** 10..3600
            
            	**units**\: second
            
            	**default value**\: 60
            
            

            """

            _prefix = 'ipv4-igmp-cfg'
            _revision = '2016-10-10'

            def __init__(self):
                super(Igmp.DefaultContext.Nsf, self).__init__()

                self.yang_name = "nsf"
                self.yang_parent_name = "default-context"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.lifetime = YLeaf(YType.uint32, "lifetime")
                self._segment_path = lambda: "nsf"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-igmp-cfg:igmp/default-context/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Igmp.DefaultContext.Nsf, ['lifetime'], name, value)


        class SsmAccessGroups(Entity):
            """
            IGMP Source specific mode
            
            .. attribute:: ssm_access_group
            
            	SSM static Access Group
            	**type**\: list of    :py:class:`SsmAccessGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext.SsmAccessGroups.SsmAccessGroup>`
            
            

            """

            _prefix = 'ipv4-igmp-cfg'
            _revision = '2016-10-10'

            def __init__(self):
                super(Igmp.DefaultContext.SsmAccessGroups, self).__init__()

                self.yang_name = "ssm-access-groups"
                self.yang_parent_name = "default-context"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"ssm-access-group" : ("ssm_access_group", Igmp.DefaultContext.SsmAccessGroups.SsmAccessGroup)}

                self.ssm_access_group = YList(self)
                self._segment_path = lambda: "ssm-access-groups"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-igmp-cfg:igmp/default-context/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Igmp.DefaultContext.SsmAccessGroups, [], name, value)


            class SsmAccessGroup(Entity):
                """
                SSM static Access Group
                
                .. attribute:: source_address  <key>
                
                	IP source address
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                
                ----
                .. attribute:: access_list_name
                
                	Access list specifying access group
                	**type**\:  str
                
                	**length:** 1..64
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'ipv4-igmp-cfg'
                _revision = '2016-10-10'

                def __init__(self):
                    super(Igmp.DefaultContext.SsmAccessGroups.SsmAccessGroup, self).__init__()

                    self.yang_name = "ssm-access-group"
                    self.yang_parent_name = "ssm-access-groups"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.source_address = YLeaf(YType.str, "source-address")

                    self.access_list_name = YLeaf(YType.str, "access-list-name")
                    self._segment_path = lambda: "ssm-access-group" + "[source-address='" + self.source_address.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-igmp-cfg:igmp/default-context/ssm-access-groups/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Igmp.DefaultContext.SsmAccessGroups.SsmAccessGroup, ['source_address', 'access_list_name'], name, value)


        class Traffic(Entity):
            """
            Configure IGMP Traffic variables
            
            .. attribute:: profile
            
            	Configure the route\-policy profile
            	**type**\:  str
            
            	**length:** 1..64
            
            

            """

            _prefix = 'ipv4-igmp-cfg'
            _revision = '2016-10-10'

            def __init__(self):
                super(Igmp.DefaultContext.Traffic, self).__init__()

                self.yang_name = "traffic"
                self.yang_parent_name = "default-context"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.profile = YLeaf(YType.str, "profile")
                self._segment_path = lambda: "traffic"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-igmp-cfg:igmp/default-context/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Igmp.DefaultContext.Traffic, ['profile'], name, value)


        class UnicastQosAdjust(Entity):
            """
            Configure IGMP QoS shapers for subscriber
            interfaces
            
            .. attribute:: adjustment_delay
            
            	Configure the QoS delay before programming (in seconds)
            	**type**\:  int
            
            	**range:** 0..10
            
            	**units**\: second
            
            	**default value**\: 1
            
            .. attribute:: download_interval
            
            	Configure the QoS download interval (in milliseconds)
            	**type**\:  int
            
            	**range:** 10..500
            
            	**units**\: millisecond
            
            	**default value**\: 100
            
            .. attribute:: hold_off
            
            	Configure the QoS hold off time (in seconds)
            	**type**\:  int
            
            	**range:** 5..1800
            
            	**units**\: second
            
            	**default value**\: 180
            
            

            """

            _prefix = 'ipv4-igmp-cfg'
            _revision = '2016-10-10'

            def __init__(self):
                super(Igmp.DefaultContext.UnicastQosAdjust, self).__init__()

                self.yang_name = "unicast-qos-adjust"
                self.yang_parent_name = "default-context"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.adjustment_delay = YLeaf(YType.uint32, "adjustment-delay")

                self.download_interval = YLeaf(YType.uint32, "download-interval")

                self.hold_off = YLeaf(YType.uint32, "hold-off")
                self._segment_path = lambda: "unicast-qos-adjust"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-igmp-cfg:igmp/default-context/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Igmp.DefaultContext.UnicastQosAdjust, ['adjustment_delay', 'download_interval', 'hold_off'], name, value)


    class Vrfs(Entity):
        """
        VRF related configuration
        
        .. attribute:: vrf
        
        	Configuration for a particular vrf
        	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.Vrfs.Vrf>`
        
        

        """

        _prefix = 'ipv4-igmp-cfg'
        _revision = '2016-10-10'

        def __init__(self):
            super(Igmp.Vrfs, self).__init__()

            self.yang_name = "vrfs"
            self.yang_parent_name = "igmp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"vrf" : ("vrf", Igmp.Vrfs.Vrf)}

            self.vrf = YList(self)
            self._segment_path = lambda: "vrfs"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-igmp-cfg:igmp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Igmp.Vrfs, [], name, value)


        class Vrf(Entity):
            """
            Configuration for a particular vrf
            
            .. attribute:: vrf_name  <key>
            
            	Name for this vrf
            	**type**\:  str
            
            	**length:** 1..32
            
            .. attribute:: inheritable_defaults
            
            	Inheritable Defaults
            	**type**\:   :py:class:`InheritableDefaults <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.Vrfs.Vrf.InheritableDefaults>`
            
            .. attribute:: interfaces
            
            	Interface\-level configuration
            	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.Vrfs.Vrf.Interfaces>`
            
            .. attribute:: maximum
            
            	Configure IGMP State Limits
            	**type**\:   :py:class:`Maximum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.Vrfs.Vrf.Maximum>`
            
            .. attribute:: robustness
            
            	Configure IGMP Robustness variable
            	**type**\:  int
            
            	**range:** 2..10
            
            	**default value**\: 2
            
            .. attribute:: ssm_access_groups
            
            	IGMP Source specific mode
            	**type**\:   :py:class:`SsmAccessGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.Vrfs.Vrf.SsmAccessGroups>`
            
            .. attribute:: ssmdns_query_group
            
            	Enable SSM mapping using DNS Query
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: traffic
            
            	Configure IGMP Traffic variables
            	**type**\:   :py:class:`Traffic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.Vrfs.Vrf.Traffic>`
            
            

            """

            _prefix = 'ipv4-igmp-cfg'
            _revision = '2016-10-10'

            def __init__(self):
                super(Igmp.Vrfs.Vrf, self).__init__()

                self.yang_name = "vrf"
                self.yang_parent_name = "vrfs"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"inheritable-defaults" : ("inheritable_defaults", Igmp.Vrfs.Vrf.InheritableDefaults), "interfaces" : ("interfaces", Igmp.Vrfs.Vrf.Interfaces), "maximum" : ("maximum", Igmp.Vrfs.Vrf.Maximum), "ssm-access-groups" : ("ssm_access_groups", Igmp.Vrfs.Vrf.SsmAccessGroups), "traffic" : ("traffic", Igmp.Vrfs.Vrf.Traffic)}
                self._child_list_classes = {}

                self.vrf_name = YLeaf(YType.str, "vrf-name")

                self.robustness = YLeaf(YType.uint32, "robustness")

                self.ssmdns_query_group = YLeaf(YType.empty, "ssmdns-query-group")

                self.inheritable_defaults = Igmp.Vrfs.Vrf.InheritableDefaults()
                self.inheritable_defaults.parent = self
                self._children_name_map["inheritable_defaults"] = "inheritable-defaults"
                self._children_yang_names.add("inheritable-defaults")

                self.interfaces = Igmp.Vrfs.Vrf.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"
                self._children_yang_names.add("interfaces")

                self.maximum = Igmp.Vrfs.Vrf.Maximum()
                self.maximum.parent = self
                self._children_name_map["maximum"] = "maximum"
                self._children_yang_names.add("maximum")

                self.ssm_access_groups = Igmp.Vrfs.Vrf.SsmAccessGroups()
                self.ssm_access_groups.parent = self
                self._children_name_map["ssm_access_groups"] = "ssm-access-groups"
                self._children_yang_names.add("ssm-access-groups")

                self.traffic = Igmp.Vrfs.Vrf.Traffic()
                self.traffic.parent = self
                self._children_name_map["traffic"] = "traffic"
                self._children_yang_names.add("traffic")
                self._segment_path = lambda: "vrf" + "[vrf-name='" + self.vrf_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-igmp-cfg:igmp/vrfs/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Igmp.Vrfs.Vrf, ['vrf_name', 'robustness', 'ssmdns_query_group'], name, value)


            class InheritableDefaults(Entity):
                """
                Inheritable Defaults
                
                .. attribute:: access_group
                
                	Access list specifying access group range
                	**type**\:  str
                
                	**length:** 1..64
                
                .. attribute:: explicit_tracking
                
                	IGMPv3 explicit host tracking
                	**type**\:   :py:class:`ExplicitTracking <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.Vrfs.Vrf.InheritableDefaults.ExplicitTracking>`
                
                	**presence node**\: True
                
                .. attribute:: maximum_groups_per_interface_oor
                
                	Configure maximum number of groups accepted per interface by this router
                	**type**\:   :py:class:`MaximumGroupsPerInterfaceOor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.Vrfs.Vrf.InheritableDefaults.MaximumGroupsPerInterfaceOor>`
                
                	**presence node**\: True
                
                .. attribute:: query_interval
                
                	Query interval in seconds
                	**type**\:  int
                
                	**range:** 1..3600
                
                	**units**\: second
                
                	**default value**\: 60
                
                .. attribute:: query_max_response_time
                
                	Query response value in seconds
                	**type**\:  int
                
                	**range:** 1..12
                
                	**units**\: second
                
                	**default value**\: 10
                
                .. attribute:: query_timeout
                
                	IGMP previous querier timeout
                	**type**\:  int
                
                	**range:** 60..300
                
                	**units**\: second
                
                .. attribute:: router_enable
                
                	Enabled or disabled, when value is TRUE or FALSE respectively
                	**type**\:  bool
                
                	**default value**\: true
                
                .. attribute:: version
                
                	Version number
                	**type**\:  int
                
                	**range:** 1..3
                
                	**default value**\: 3
                
                

                """

                _prefix = 'ipv4-igmp-cfg'
                _revision = '2016-10-10'

                def __init__(self):
                    super(Igmp.Vrfs.Vrf.InheritableDefaults, self).__init__()

                    self.yang_name = "inheritable-defaults"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"explicit-tracking" : ("explicit_tracking", Igmp.Vrfs.Vrf.InheritableDefaults.ExplicitTracking), "maximum-groups-per-interface-oor" : ("maximum_groups_per_interface_oor", Igmp.Vrfs.Vrf.InheritableDefaults.MaximumGroupsPerInterfaceOor)}
                    self._child_list_classes = {}

                    self.access_group = YLeaf(YType.str, "access-group")

                    self.query_interval = YLeaf(YType.uint32, "query-interval")

                    self.query_max_response_time = YLeaf(YType.uint32, "query-max-response-time")

                    self.query_timeout = YLeaf(YType.uint32, "query-timeout")

                    self.router_enable = YLeaf(YType.boolean, "router-enable")

                    self.version = YLeaf(YType.uint32, "version")

                    self.explicit_tracking = None
                    self._children_name_map["explicit_tracking"] = "explicit-tracking"
                    self._children_yang_names.add("explicit-tracking")

                    self.maximum_groups_per_interface_oor = None
                    self._children_name_map["maximum_groups_per_interface_oor"] = "maximum-groups-per-interface-oor"
                    self._children_yang_names.add("maximum-groups-per-interface-oor")
                    self._segment_path = lambda: "inheritable-defaults"

                def __setattr__(self, name, value):
                    self._perform_setattr(Igmp.Vrfs.Vrf.InheritableDefaults, ['access_group', 'query_interval', 'query_max_response_time', 'query_timeout', 'router_enable', 'version'], name, value)


                class ExplicitTracking(Entity):
                    """
                    IGMPv3 explicit host tracking
                    
                    .. attribute:: access_list_name
                    
                    	Access list specifying tracking group range
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    .. attribute:: enable
                    
                    	Enabled or disabled, when value is TRUE or FALSE respectively
                    	**type**\:  bool
                    
                    	**mandatory**\: True
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-igmp-cfg'
                    _revision = '2016-10-10'

                    def __init__(self):
                        super(Igmp.Vrfs.Vrf.InheritableDefaults.ExplicitTracking, self).__init__()

                        self.yang_name = "explicit-tracking"
                        self.yang_parent_name = "inheritable-defaults"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}
                        self.is_presence_container = True

                        self.access_list_name = YLeaf(YType.str, "access-list-name")

                        self.enable = YLeaf(YType.boolean, "enable")
                        self._segment_path = lambda: "explicit-tracking"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Igmp.Vrfs.Vrf.InheritableDefaults.ExplicitTracking, ['access_list_name', 'enable'], name, value)


                class MaximumGroupsPerInterfaceOor(Entity):
                    """
                    Configure maximum number of groups accepted per
                    interface by this router
                    
                    .. attribute:: access_list_name
                    
                    	Access\-list to account for
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    .. attribute:: maximum_groups
                    
                    	Maximum number of groups accepted per interface by this router
                    	**type**\:  int
                    
                    	**range:** 1..40000
                    
                    	**mandatory**\: True
                    
                    .. attribute:: warning_threshold
                    
                    	 WarningThreshold for number of groups accepted per interface by this router
                    	**type**\:  int
                    
                    	**range:** 1..40000
                    
                    	**default value**\: 25000
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-igmp-cfg'
                    _revision = '2016-10-10'

                    def __init__(self):
                        super(Igmp.Vrfs.Vrf.InheritableDefaults.MaximumGroupsPerInterfaceOor, self).__init__()

                        self.yang_name = "maximum-groups-per-interface-oor"
                        self.yang_parent_name = "inheritable-defaults"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}
                        self.is_presence_container = True

                        self.access_list_name = YLeaf(YType.str, "access-list-name")

                        self.maximum_groups = YLeaf(YType.uint32, "maximum-groups")

                        self.warning_threshold = YLeaf(YType.uint32, "warning-threshold")
                        self._segment_path = lambda: "maximum-groups-per-interface-oor"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Igmp.Vrfs.Vrf.InheritableDefaults.MaximumGroupsPerInterfaceOor, ['access_list_name', 'maximum_groups', 'warning_threshold'], name, value)


            class Interfaces(Entity):
                """
                Interface\-level configuration
                
                .. attribute:: interface
                
                	The name of the interface
                	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.Vrfs.Vrf.Interfaces.Interface>`
                
                

                """

                _prefix = 'ipv4-igmp-cfg'
                _revision = '2016-10-10'

                def __init__(self):
                    super(Igmp.Vrfs.Vrf.Interfaces, self).__init__()

                    self.yang_name = "interfaces"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"interface" : ("interface", Igmp.Vrfs.Vrf.Interfaces.Interface)}

                    self.interface = YList(self)
                    self._segment_path = lambda: "interfaces"

                def __setattr__(self, name, value):
                    self._perform_setattr(Igmp.Vrfs.Vrf.Interfaces, [], name, value)


                class Interface(Entity):
                    """
                    The name of the interface
                    
                    .. attribute:: interface_name  <key>
                    
                    	Name of the interface
                    	**type**\:  str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
                    .. attribute:: access_group
                    
                    	Access list specifying access group range
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    .. attribute:: explicit_tracking
                    
                    	IGMPv3 explicit host tracking
                    	**type**\:   :py:class:`ExplicitTracking <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.Vrfs.Vrf.Interfaces.Interface.ExplicitTracking>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: join_groups
                    
                    	IGMP join multicast group
                    	**type**\:   :py:class:`JoinGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.Vrfs.Vrf.Interfaces.Interface.JoinGroups>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: maximum_groups_per_interface_oor
                    
                    	Configure maximum number of groups accepted per interface by this router
                    	**type**\:   :py:class:`MaximumGroupsPerInterfaceOor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.Vrfs.Vrf.Interfaces.Interface.MaximumGroupsPerInterfaceOor>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: query_interval
                    
                    	Query interval in seconds
                    	**type**\:  int
                    
                    	**range:** 1..3600
                    
                    	**units**\: second
                    
                    	**default value**\: 60
                    
                    .. attribute:: query_max_response_time
                    
                    	Query response value in seconds
                    	**type**\:  int
                    
                    	**range:** 1..12
                    
                    	**units**\: second
                    
                    	**default value**\: 10
                    
                    .. attribute:: query_timeout
                    
                    	IGMP previous querier timeout
                    	**type**\:  int
                    
                    	**range:** 60..300
                    
                    	**units**\: second
                    
                    .. attribute:: router_enable
                    
                    	Enabled or disabled, when value is TRUE or FALSE respectively
                    	**type**\:  bool
                    
                    	**default value**\: true
                    
                    .. attribute:: static_group_group_addresses
                    
                    	IGMP static multicast group
                    	**type**\:   :py:class:`StaticGroupGroupAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses>`
                    
                    .. attribute:: version
                    
                    	Version number
                    	**type**\:  int
                    
                    	**range:** 1..3
                    
                    	**default value**\: 3
                    
                    

                    """

                    _prefix = 'ipv4-igmp-cfg'
                    _revision = '2016-10-10'

                    def __init__(self):
                        super(Igmp.Vrfs.Vrf.Interfaces.Interface, self).__init__()

                        self.yang_name = "interface"
                        self.yang_parent_name = "interfaces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"explicit-tracking" : ("explicit_tracking", Igmp.Vrfs.Vrf.Interfaces.Interface.ExplicitTracking), "join-groups" : ("join_groups", Igmp.Vrfs.Vrf.Interfaces.Interface.JoinGroups), "maximum-groups-per-interface-oor" : ("maximum_groups_per_interface_oor", Igmp.Vrfs.Vrf.Interfaces.Interface.MaximumGroupsPerInterfaceOor), "static-group-group-addresses" : ("static_group_group_addresses", Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses)}
                        self._child_list_classes = {}

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.access_group = YLeaf(YType.str, "access-group")

                        self.query_interval = YLeaf(YType.uint32, "query-interval")

                        self.query_max_response_time = YLeaf(YType.uint32, "query-max-response-time")

                        self.query_timeout = YLeaf(YType.uint32, "query-timeout")

                        self.router_enable = YLeaf(YType.boolean, "router-enable")

                        self.version = YLeaf(YType.uint32, "version")

                        self.explicit_tracking = None
                        self._children_name_map["explicit_tracking"] = "explicit-tracking"
                        self._children_yang_names.add("explicit-tracking")

                        self.join_groups = None
                        self._children_name_map["join_groups"] = "join-groups"
                        self._children_yang_names.add("join-groups")

                        self.maximum_groups_per_interface_oor = None
                        self._children_name_map["maximum_groups_per_interface_oor"] = "maximum-groups-per-interface-oor"
                        self._children_yang_names.add("maximum-groups-per-interface-oor")

                        self.static_group_group_addresses = Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses()
                        self.static_group_group_addresses.parent = self
                        self._children_name_map["static_group_group_addresses"] = "static-group-group-addresses"
                        self._children_yang_names.add("static-group-group-addresses")
                        self._segment_path = lambda: "interface" + "[interface-name='" + self.interface_name.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Igmp.Vrfs.Vrf.Interfaces.Interface, ['interface_name', 'access_group', 'query_interval', 'query_max_response_time', 'query_timeout', 'router_enable', 'version'], name, value)


                    class ExplicitTracking(Entity):
                        """
                        IGMPv3 explicit host tracking
                        
                        .. attribute:: access_list_name
                        
                        	Access list specifying tracking group range
                        	**type**\:  str
                        
                        	**length:** 1..64
                        
                        .. attribute:: enable
                        
                        	Enabled or disabled, when value is TRUE or FALSE respectively
                        	**type**\:  bool
                        
                        	**mandatory**\: True
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2016-10-10'

                        def __init__(self):
                            super(Igmp.Vrfs.Vrf.Interfaces.Interface.ExplicitTracking, self).__init__()

                            self.yang_name = "explicit-tracking"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}
                            self.is_presence_container = True

                            self.access_list_name = YLeaf(YType.str, "access-list-name")

                            self.enable = YLeaf(YType.boolean, "enable")
                            self._segment_path = lambda: "explicit-tracking"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Igmp.Vrfs.Vrf.Interfaces.Interface.ExplicitTracking, ['access_list_name', 'enable'], name, value)


                    class JoinGroups(Entity):
                        """
                        IGMP join multicast group
                        
                        .. attribute:: join_group
                        
                        	IP group address and optional source address to include
                        	**type**\: list of    :py:class:`JoinGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.Vrfs.Vrf.Interfaces.Interface.JoinGroups.JoinGroup>`
                        
                        .. attribute:: join_group_source_address
                        
                        	IP group address and optional source address to include
                        	**type**\: list of    :py:class:`JoinGroupSourceAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.Vrfs.Vrf.Interfaces.Interface.JoinGroups.JoinGroupSourceAddress>`
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2016-10-10'

                        def __init__(self):
                            super(Igmp.Vrfs.Vrf.Interfaces.Interface.JoinGroups, self).__init__()

                            self.yang_name = "join-groups"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"join-group" : ("join_group", Igmp.Vrfs.Vrf.Interfaces.Interface.JoinGroups.JoinGroup), "join-group-source-address" : ("join_group_source_address", Igmp.Vrfs.Vrf.Interfaces.Interface.JoinGroups.JoinGroupSourceAddress)}
                            self.is_presence_container = True

                            self.join_group = YList(self)
                            self.join_group_source_address = YList(self)
                            self._segment_path = lambda: "join-groups"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Igmp.Vrfs.Vrf.Interfaces.Interface.JoinGroups, [], name, value)


                        class JoinGroup(Entity):
                            """
                            IP group address and optional source address
                            to include
                            
                            .. attribute:: group_address  <key>
                            
                            	IP group address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: mode
                            
                            	Filter mode
                            	**type**\:   :py:class:`IgmpFilter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.IgmpFilter>`
                            
                            	**mandatory**\: True
                            
                            

                            """

                            _prefix = 'ipv4-igmp-cfg'
                            _revision = '2016-10-10'

                            def __init__(self):
                                super(Igmp.Vrfs.Vrf.Interfaces.Interface.JoinGroups.JoinGroup, self).__init__()

                                self.yang_name = "join-group"
                                self.yang_parent_name = "join-groups"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.group_address = YLeaf(YType.str, "group-address")

                                self.mode = YLeaf(YType.enumeration, "mode")
                                self._segment_path = lambda: "join-group" + "[group-address='" + self.group_address.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Igmp.Vrfs.Vrf.Interfaces.Interface.JoinGroups.JoinGroup, ['group_address', 'mode'], name, value)


                        class JoinGroupSourceAddress(Entity):
                            """
                            IP group address and optional source address
                            to include
                            
                            .. attribute:: group_address  <key>
                            
                            	IP group address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: source_address  <key>
                            
                            	Optional IP source address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: mode
                            
                            	Filter mode
                            	**type**\:   :py:class:`IgmpFilter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.IgmpFilter>`
                            
                            	**mandatory**\: True
                            
                            

                            """

                            _prefix = 'ipv4-igmp-cfg'
                            _revision = '2016-10-10'

                            def __init__(self):
                                super(Igmp.Vrfs.Vrf.Interfaces.Interface.JoinGroups.JoinGroupSourceAddress, self).__init__()

                                self.yang_name = "join-group-source-address"
                                self.yang_parent_name = "join-groups"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.group_address = YLeaf(YType.str, "group-address")

                                self.source_address = YLeaf(YType.str, "source-address")

                                self.mode = YLeaf(YType.enumeration, "mode")
                                self._segment_path = lambda: "join-group-source-address" + "[group-address='" + self.group_address.get() + "']" + "[source-address='" + self.source_address.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Igmp.Vrfs.Vrf.Interfaces.Interface.JoinGroups.JoinGroupSourceAddress, ['group_address', 'source_address', 'mode'], name, value)


                    class MaximumGroupsPerInterfaceOor(Entity):
                        """
                        Configure maximum number of groups accepted per
                        interface by this router
                        
                        .. attribute:: access_list_name
                        
                        	Access\-list to account for
                        	**type**\:  str
                        
                        	**length:** 1..64
                        
                        .. attribute:: maximum_groups
                        
                        	Maximum number of groups accepted per interface by this router
                        	**type**\:  int
                        
                        	**range:** 1..40000
                        
                        	**mandatory**\: True
                        
                        .. attribute:: warning_threshold
                        
                        	 WarningThreshold for number of groups accepted per interface by this router
                        	**type**\:  int
                        
                        	**range:** 1..40000
                        
                        	**default value**\: 25000
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2016-10-10'

                        def __init__(self):
                            super(Igmp.Vrfs.Vrf.Interfaces.Interface.MaximumGroupsPerInterfaceOor, self).__init__()

                            self.yang_name = "maximum-groups-per-interface-oor"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}
                            self.is_presence_container = True

                            self.access_list_name = YLeaf(YType.str, "access-list-name")

                            self.maximum_groups = YLeaf(YType.uint32, "maximum-groups")

                            self.warning_threshold = YLeaf(YType.uint32, "warning-threshold")
                            self._segment_path = lambda: "maximum-groups-per-interface-oor"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Igmp.Vrfs.Vrf.Interfaces.Interface.MaximumGroupsPerInterfaceOor, ['access_list_name', 'maximum_groups', 'warning_threshold'], name, value)


                    class StaticGroupGroupAddresses(Entity):
                        """
                        IGMP static multicast group
                        
                        .. attribute:: static_group_group_address
                        
                        	IP group address and optional source address to include
                        	**type**\: list of    :py:class:`StaticGroupGroupAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddress>`
                        
                        .. attribute:: static_group_group_address_group_address_mask
                        
                        	IP group address and optional source address to include
                        	**type**\: list of    :py:class:`StaticGroupGroupAddressGroupAddressMask <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMask>`
                        
                        .. attribute:: static_group_group_address_group_address_mask_source_address
                        
                        	IP group address and optional source address to include
                        	**type**\: list of    :py:class:`StaticGroupGroupAddressGroupAddressMaskSourceAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddress>`
                        
                        .. attribute:: static_group_group_address_group_address_mask_source_address_source_address_mask
                        
                        	IP group address and optional source address to include
                        	**type**\: list of    :py:class:`StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask>`
                        
                        .. attribute:: static_group_group_address_source_address
                        
                        	IP group address and optional source address to include
                        	**type**\: list of    :py:class:`StaticGroupGroupAddressSourceAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddress>`
                        
                        .. attribute:: static_group_group_address_source_address_source_address_mask
                        
                        	IP group address and optional source address to include
                        	**type**\: list of    :py:class:`StaticGroupGroupAddressSourceAddressSourceAddressMask <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddressSourceAddressMask>`
                        
                        

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2016-10-10'

                        def __init__(self):
                            super(Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses, self).__init__()

                            self.yang_name = "static-group-group-addresses"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"static-group-group-address" : ("static_group_group_address", Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddress), "static-group-group-address-group-address-mask" : ("static_group_group_address_group_address_mask", Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMask), "static-group-group-address-group-address-mask-source-address" : ("static_group_group_address_group_address_mask_source_address", Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddress), "static-group-group-address-group-address-mask-source-address-source-address-mask" : ("static_group_group_address_group_address_mask_source_address_source_address_mask", Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask), "static-group-group-address-source-address" : ("static_group_group_address_source_address", Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddress), "static-group-group-address-source-address-source-address-mask" : ("static_group_group_address_source_address_source_address_mask", Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddressSourceAddressMask)}

                            self.static_group_group_address = YList(self)
                            self.static_group_group_address_group_address_mask = YList(self)
                            self.static_group_group_address_group_address_mask_source_address = YList(self)
                            self.static_group_group_address_group_address_mask_source_address_source_address_mask = YList(self)
                            self.static_group_group_address_source_address = YList(self)
                            self.static_group_group_address_source_address_source_address_mask = YList(self)
                            self._segment_path = lambda: "static-group-group-addresses"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses, [], name, value)


                        class StaticGroupGroupAddress(Entity):
                            """
                            IP group address and optional source address
                            to include
                            
                            .. attribute:: group_address  <key>
                            
                            	IP group address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: group_count
                            
                            	Number of groups to join (do not set without GroupAddressMask)
                            	**type**\:  int
                            
                            	**range:** 1..512
                            
                            	**default value**\: 1
                            
                            .. attribute:: source_count
                            
                            	Number of sources to join (do not set without SourceAddressMask)
                            	**type**\:  int
                            
                            	**range:** 1..512
                            
                            	**default value**\: 1
                            
                            .. attribute:: suppress_report
                            
                            	Suppress reports
                            	**type**\:  bool
                            
                            	**default value**\: false
                            
                            

                            """

                            _prefix = 'ipv4-igmp-cfg'
                            _revision = '2016-10-10'

                            def __init__(self):
                                super(Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddress, self).__init__()

                                self.yang_name = "static-group-group-address"
                                self.yang_parent_name = "static-group-group-addresses"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.group_address = YLeaf(YType.str, "group-address")

                                self.group_count = YLeaf(YType.uint32, "group-count")

                                self.source_count = YLeaf(YType.uint32, "source-count")

                                self.suppress_report = YLeaf(YType.boolean, "suppress-report")
                                self._segment_path = lambda: "static-group-group-address" + "[group-address='" + self.group_address.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddress, ['group_address', 'group_count', 'source_count', 'suppress_report'], name, value)


                        class StaticGroupGroupAddressGroupAddressMask(Entity):
                            """
                            IP group address and optional source address
                            to include
                            
                            .. attribute:: group_address  <key>
                            
                            	IP group address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: group_address_mask  <key>
                            
                            	Mask for Group Address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: group_count
                            
                            	Number of groups to join (do not set without GroupAddressMask)
                            	**type**\:  int
                            
                            	**range:** 1..512
                            
                            	**default value**\: 1
                            
                            .. attribute:: source_count
                            
                            	Number of sources to join (do not set without SourceAddressMask)
                            	**type**\:  int
                            
                            	**range:** 1..512
                            
                            	**default value**\: 1
                            
                            .. attribute:: suppress_report
                            
                            	Suppress reports
                            	**type**\:  bool
                            
                            	**default value**\: false
                            
                            

                            """

                            _prefix = 'ipv4-igmp-cfg'
                            _revision = '2016-10-10'

                            def __init__(self):
                                super(Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMask, self).__init__()

                                self.yang_name = "static-group-group-address-group-address-mask"
                                self.yang_parent_name = "static-group-group-addresses"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.group_address = YLeaf(YType.str, "group-address")

                                self.group_address_mask = YLeaf(YType.str, "group-address-mask")

                                self.group_count = YLeaf(YType.uint32, "group-count")

                                self.source_count = YLeaf(YType.uint32, "source-count")

                                self.suppress_report = YLeaf(YType.boolean, "suppress-report")
                                self._segment_path = lambda: "static-group-group-address-group-address-mask" + "[group-address='" + self.group_address.get() + "']" + "[group-address-mask='" + self.group_address_mask.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMask, ['group_address', 'group_address_mask', 'group_count', 'source_count', 'suppress_report'], name, value)


                        class StaticGroupGroupAddressGroupAddressMaskSourceAddress(Entity):
                            """
                            IP group address and optional source address
                            to include
                            
                            .. attribute:: group_address  <key>
                            
                            	IP group address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: group_address_mask  <key>
                            
                            	Mask for Group Address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: source_address  <key>
                            
                            	IP source address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: group_count
                            
                            	Number of groups to join (do not set without GroupAddressMask)
                            	**type**\:  int
                            
                            	**range:** 1..512
                            
                            	**default value**\: 1
                            
                            .. attribute:: source_count
                            
                            	Number of sources to join (do not set without SourceAddressMask)
                            	**type**\:  int
                            
                            	**range:** 1..512
                            
                            	**default value**\: 1
                            
                            .. attribute:: suppress_report
                            
                            	Suppress reports
                            	**type**\:  bool
                            
                            	**default value**\: false
                            
                            

                            """

                            _prefix = 'ipv4-igmp-cfg'
                            _revision = '2016-10-10'

                            def __init__(self):
                                super(Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddress, self).__init__()

                                self.yang_name = "static-group-group-address-group-address-mask-source-address"
                                self.yang_parent_name = "static-group-group-addresses"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.group_address = YLeaf(YType.str, "group-address")

                                self.group_address_mask = YLeaf(YType.str, "group-address-mask")

                                self.source_address = YLeaf(YType.str, "source-address")

                                self.group_count = YLeaf(YType.uint32, "group-count")

                                self.source_count = YLeaf(YType.uint32, "source-count")

                                self.suppress_report = YLeaf(YType.boolean, "suppress-report")
                                self._segment_path = lambda: "static-group-group-address-group-address-mask-source-address" + "[group-address='" + self.group_address.get() + "']" + "[group-address-mask='" + self.group_address_mask.get() + "']" + "[source-address='" + self.source_address.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddress, ['group_address', 'group_address_mask', 'source_address', 'group_count', 'source_count', 'suppress_report'], name, value)


                        class StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask(Entity):
                            """
                            IP group address and optional source address
                            to include
                            
                            .. attribute:: group_address  <key>
                            
                            	IP group address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: group_address_mask  <key>
                            
                            	Mask for Group Address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: source_address  <key>
                            
                            	IP source address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: source_address_mask  <key>
                            
                            	Mask for Source Address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: group_count
                            
                            	Number of groups to join (do not set without GroupAddressMask)
                            	**type**\:  int
                            
                            	**range:** 1..512
                            
                            	**default value**\: 1
                            
                            .. attribute:: source_count
                            
                            	Number of sources to join (do not set without SourceAddressMask)
                            	**type**\:  int
                            
                            	**range:** 1..512
                            
                            	**default value**\: 1
                            
                            .. attribute:: suppress_report
                            
                            	Suppress reports
                            	**type**\:  bool
                            
                            	**default value**\: false
                            
                            

                            """

                            _prefix = 'ipv4-igmp-cfg'
                            _revision = '2016-10-10'

                            def __init__(self):
                                super(Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask, self).__init__()

                                self.yang_name = "static-group-group-address-group-address-mask-source-address-source-address-mask"
                                self.yang_parent_name = "static-group-group-addresses"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.group_address = YLeaf(YType.str, "group-address")

                                self.group_address_mask = YLeaf(YType.str, "group-address-mask")

                                self.source_address = YLeaf(YType.str, "source-address")

                                self.source_address_mask = YLeaf(YType.str, "source-address-mask")

                                self.group_count = YLeaf(YType.uint32, "group-count")

                                self.source_count = YLeaf(YType.uint32, "source-count")

                                self.suppress_report = YLeaf(YType.boolean, "suppress-report")
                                self._segment_path = lambda: "static-group-group-address-group-address-mask-source-address-source-address-mask" + "[group-address='" + self.group_address.get() + "']" + "[group-address-mask='" + self.group_address_mask.get() + "']" + "[source-address='" + self.source_address.get() + "']" + "[source-address-mask='" + self.source_address_mask.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask, ['group_address', 'group_address_mask', 'source_address', 'source_address_mask', 'group_count', 'source_count', 'suppress_report'], name, value)


                        class StaticGroupGroupAddressSourceAddress(Entity):
                            """
                            IP group address and optional source address
                            to include
                            
                            .. attribute:: group_address  <key>
                            
                            	IP group address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: source_address  <key>
                            
                            	IP source address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: group_count
                            
                            	Number of groups to join (do not set without GroupAddressMask)
                            	**type**\:  int
                            
                            	**range:** 1..512
                            
                            	**default value**\: 1
                            
                            .. attribute:: source_count
                            
                            	Number of sources to join (do not set without SourceAddressMask)
                            	**type**\:  int
                            
                            	**range:** 1..512
                            
                            	**default value**\: 1
                            
                            .. attribute:: suppress_report
                            
                            	Suppress reports
                            	**type**\:  bool
                            
                            	**default value**\: false
                            
                            

                            """

                            _prefix = 'ipv4-igmp-cfg'
                            _revision = '2016-10-10'

                            def __init__(self):
                                super(Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddress, self).__init__()

                                self.yang_name = "static-group-group-address-source-address"
                                self.yang_parent_name = "static-group-group-addresses"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.group_address = YLeaf(YType.str, "group-address")

                                self.source_address = YLeaf(YType.str, "source-address")

                                self.group_count = YLeaf(YType.uint32, "group-count")

                                self.source_count = YLeaf(YType.uint32, "source-count")

                                self.suppress_report = YLeaf(YType.boolean, "suppress-report")
                                self._segment_path = lambda: "static-group-group-address-source-address" + "[group-address='" + self.group_address.get() + "']" + "[source-address='" + self.source_address.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddress, ['group_address', 'source_address', 'group_count', 'source_count', 'suppress_report'], name, value)


                        class StaticGroupGroupAddressSourceAddressSourceAddressMask(Entity):
                            """
                            IP group address and optional source address
                            to include
                            
                            .. attribute:: group_address  <key>
                            
                            	IP group address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: source_address  <key>
                            
                            	IP source address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: source_address_mask  <key>
                            
                            	Mask for Source Address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: group_count
                            
                            	Number of groups to join (do not set without GroupAddressMask)
                            	**type**\:  int
                            
                            	**range:** 1..512
                            
                            	**default value**\: 1
                            
                            .. attribute:: source_count
                            
                            	Number of sources to join (do not set without SourceAddressMask)
                            	**type**\:  int
                            
                            	**range:** 1..512
                            
                            	**default value**\: 1
                            
                            .. attribute:: suppress_report
                            
                            	Suppress reports
                            	**type**\:  bool
                            
                            	**default value**\: false
                            
                            

                            """

                            _prefix = 'ipv4-igmp-cfg'
                            _revision = '2016-10-10'

                            def __init__(self):
                                super(Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddressSourceAddressMask, self).__init__()

                                self.yang_name = "static-group-group-address-source-address-source-address-mask"
                                self.yang_parent_name = "static-group-group-addresses"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.group_address = YLeaf(YType.str, "group-address")

                                self.source_address = YLeaf(YType.str, "source-address")

                                self.source_address_mask = YLeaf(YType.str, "source-address-mask")

                                self.group_count = YLeaf(YType.uint32, "group-count")

                                self.source_count = YLeaf(YType.uint32, "source-count")

                                self.suppress_report = YLeaf(YType.boolean, "suppress-report")
                                self._segment_path = lambda: "static-group-group-address-source-address-source-address-mask" + "[group-address='" + self.group_address.get() + "']" + "[source-address='" + self.source_address.get() + "']" + "[source-address-mask='" + self.source_address_mask.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddressSourceAddressMask, ['group_address', 'source_address', 'source_address_mask', 'group_count', 'source_count', 'suppress_report'], name, value)


            class Maximum(Entity):
                """
                Configure IGMP State Limits
                
                .. attribute:: maximum_groups
                
                	Configure maximum number of groups accepted by this router
                	**type**\:  int
                
                	**range:** 1..75000
                
                	**default value**\: 50000
                
                

                """

                _prefix = 'ipv4-igmp-cfg'
                _revision = '2016-10-10'

                def __init__(self):
                    super(Igmp.Vrfs.Vrf.Maximum, self).__init__()

                    self.yang_name = "maximum"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.maximum_groups = YLeaf(YType.uint32, "maximum-groups")
                    self._segment_path = lambda: "maximum"

                def __setattr__(self, name, value):
                    self._perform_setattr(Igmp.Vrfs.Vrf.Maximum, ['maximum_groups'], name, value)


            class SsmAccessGroups(Entity):
                """
                IGMP Source specific mode
                
                .. attribute:: ssm_access_group
                
                	SSM static Access Group
                	**type**\: list of    :py:class:`SsmAccessGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.Vrfs.Vrf.SsmAccessGroups.SsmAccessGroup>`
                
                

                """

                _prefix = 'ipv4-igmp-cfg'
                _revision = '2016-10-10'

                def __init__(self):
                    super(Igmp.Vrfs.Vrf.SsmAccessGroups, self).__init__()

                    self.yang_name = "ssm-access-groups"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"ssm-access-group" : ("ssm_access_group", Igmp.Vrfs.Vrf.SsmAccessGroups.SsmAccessGroup)}

                    self.ssm_access_group = YList(self)
                    self._segment_path = lambda: "ssm-access-groups"

                def __setattr__(self, name, value):
                    self._perform_setattr(Igmp.Vrfs.Vrf.SsmAccessGroups, [], name, value)


                class SsmAccessGroup(Entity):
                    """
                    SSM static Access Group
                    
                    .. attribute:: source_address  <key>
                    
                    	IP source address
                    	**type**\: one of the below types:
                    
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    .. attribute:: access_list_name
                    
                    	Access list specifying access group
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    	**mandatory**\: True
                    
                    

                    """

                    _prefix = 'ipv4-igmp-cfg'
                    _revision = '2016-10-10'

                    def __init__(self):
                        super(Igmp.Vrfs.Vrf.SsmAccessGroups.SsmAccessGroup, self).__init__()

                        self.yang_name = "ssm-access-group"
                        self.yang_parent_name = "ssm-access-groups"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.source_address = YLeaf(YType.str, "source-address")

                        self.access_list_name = YLeaf(YType.str, "access-list-name")
                        self._segment_path = lambda: "ssm-access-group" + "[source-address='" + self.source_address.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Igmp.Vrfs.Vrf.SsmAccessGroups.SsmAccessGroup, ['source_address', 'access_list_name'], name, value)


            class Traffic(Entity):
                """
                Configure IGMP Traffic variables
                
                .. attribute:: profile
                
                	Configure the route\-policy profile
                	**type**\:  str
                
                	**length:** 1..64
                
                

                """

                _prefix = 'ipv4-igmp-cfg'
                _revision = '2016-10-10'

                def __init__(self):
                    super(Igmp.Vrfs.Vrf.Traffic, self).__init__()

                    self.yang_name = "traffic"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.profile = YLeaf(YType.str, "profile")
                    self._segment_path = lambda: "traffic"

                def __setattr__(self, name, value):
                    self._perform_setattr(Igmp.Vrfs.Vrf.Traffic, ['profile'], name, value)

    def clone_ptr(self):
        self._top_entity = Igmp()
        return self._top_entity

class Mld(Entity):
    """
    mld
    
    .. attribute:: default_context
    
    	Default Context
    	**type**\:   :py:class:`DefaultContext <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext>`
    
    	**presence node**\: True
    
    .. attribute:: vrfs
    
    	VRF related configuration
    	**type**\:   :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.Vrfs>`
    
    

    This class is a :ref:`presence class<presence-class>`

    """

    _prefix = 'ipv4-igmp-cfg'
    _revision = '2016-10-10'

    def __init__(self):
        super(Mld, self).__init__()
        self._top_entity = None

        self.yang_name = "mld"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-igmp-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"default-context" : ("default_context", Mld.DefaultContext), "vrfs" : ("vrfs", Mld.Vrfs)}
        self._child_list_classes = {}
        self.is_presence_container = True

        self.default_context = None
        self._children_name_map["default_context"] = "default-context"
        self._children_yang_names.add("default-context")

        self.vrfs = Mld.Vrfs()
        self.vrfs.parent = self
        self._children_name_map["vrfs"] = "vrfs"
        self._children_yang_names.add("vrfs")
        self._segment_path = lambda: "Cisco-IOS-XR-ipv4-igmp-cfg:mld"


    class DefaultContext(Entity):
        """
        Default Context
        
        .. attribute:: accounting
        
        	Configure IGMP accounting for logging join/leave records
        	**type**\:   :py:class:`Accounting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext.Accounting>`
        
        .. attribute:: inheritable_defaults
        
        	Inheritable Defaults
        	**type**\:   :py:class:`InheritableDefaults <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext.InheritableDefaults>`
        
        .. attribute:: interfaces
        
        	Interface\-level configuration
        	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext.Interfaces>`
        
        .. attribute:: maximum
        
        	Configure IGMP State Limits
        	**type**\:   :py:class:`Maximum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext.Maximum>`
        
        .. attribute:: nsf
        
        	Configure NSF specific options
        	**type**\:   :py:class:`Nsf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext.Nsf>`
        
        .. attribute:: robustness
        
        	Configure IGMP Robustness variable
        	**type**\:  int
        
        	**range:** 2..10
        
        	**default value**\: 2
        
        .. attribute:: ssm_access_groups
        
        	IGMP Source specific mode
        	**type**\:   :py:class:`SsmAccessGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext.SsmAccessGroups>`
        
        .. attribute:: ssmdns_query_group
        
        	Enable SSM mapping using DNS Query
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: traffic
        
        	Configure IGMP Traffic variables
        	**type**\:   :py:class:`Traffic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext.Traffic>`
        
        .. attribute:: unicast_qos_adjust
        
        	Configure IGMP QoS shapers for subscriber interfaces
        	**type**\:   :py:class:`UnicastQosAdjust <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext.UnicastQosAdjust>`
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'ipv4-igmp-cfg'
        _revision = '2016-10-10'

        def __init__(self):
            super(Mld.DefaultContext, self).__init__()

            self.yang_name = "default-context"
            self.yang_parent_name = "mld"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"accounting" : ("accounting", Mld.DefaultContext.Accounting), "inheritable-defaults" : ("inheritable_defaults", Mld.DefaultContext.InheritableDefaults), "interfaces" : ("interfaces", Mld.DefaultContext.Interfaces), "maximum" : ("maximum", Mld.DefaultContext.Maximum), "nsf" : ("nsf", Mld.DefaultContext.Nsf), "ssm-access-groups" : ("ssm_access_groups", Mld.DefaultContext.SsmAccessGroups), "traffic" : ("traffic", Mld.DefaultContext.Traffic), "unicast-qos-adjust" : ("unicast_qos_adjust", Mld.DefaultContext.UnicastQosAdjust)}
            self._child_list_classes = {}
            self.is_presence_container = True

            self.robustness = YLeaf(YType.uint32, "robustness")

            self.ssmdns_query_group = YLeaf(YType.empty, "ssmdns-query-group")

            self.accounting = Mld.DefaultContext.Accounting()
            self.accounting.parent = self
            self._children_name_map["accounting"] = "accounting"
            self._children_yang_names.add("accounting")

            self.inheritable_defaults = Mld.DefaultContext.InheritableDefaults()
            self.inheritable_defaults.parent = self
            self._children_name_map["inheritable_defaults"] = "inheritable-defaults"
            self._children_yang_names.add("inheritable-defaults")

            self.interfaces = Mld.DefaultContext.Interfaces()
            self.interfaces.parent = self
            self._children_name_map["interfaces"] = "interfaces"
            self._children_yang_names.add("interfaces")

            self.maximum = Mld.DefaultContext.Maximum()
            self.maximum.parent = self
            self._children_name_map["maximum"] = "maximum"
            self._children_yang_names.add("maximum")

            self.nsf = Mld.DefaultContext.Nsf()
            self.nsf.parent = self
            self._children_name_map["nsf"] = "nsf"
            self._children_yang_names.add("nsf")

            self.ssm_access_groups = Mld.DefaultContext.SsmAccessGroups()
            self.ssm_access_groups.parent = self
            self._children_name_map["ssm_access_groups"] = "ssm-access-groups"
            self._children_yang_names.add("ssm-access-groups")

            self.traffic = Mld.DefaultContext.Traffic()
            self.traffic.parent = self
            self._children_name_map["traffic"] = "traffic"
            self._children_yang_names.add("traffic")

            self.unicast_qos_adjust = Mld.DefaultContext.UnicastQosAdjust()
            self.unicast_qos_adjust.parent = self
            self._children_name_map["unicast_qos_adjust"] = "unicast-qos-adjust"
            self._children_yang_names.add("unicast-qos-adjust")
            self._segment_path = lambda: "default-context"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-igmp-cfg:mld/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Mld.DefaultContext, ['robustness', 'ssmdns_query_group'], name, value)


        class Accounting(Entity):
            """
            Configure IGMP accounting for logging
            join/leave records
            
            .. attribute:: max_history
            
            	Configure IGMP accounting Maximum History setting
            	**type**\:  int
            
            	**range:** 0..365
            
            	**units**\: day
            
            	**default value**\: 0
            
            

            """

            _prefix = 'ipv4-igmp-cfg'
            _revision = '2016-10-10'

            def __init__(self):
                super(Mld.DefaultContext.Accounting, self).__init__()

                self.yang_name = "accounting"
                self.yang_parent_name = "default-context"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.max_history = YLeaf(YType.uint32, "max-history")
                self._segment_path = lambda: "accounting"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-igmp-cfg:mld/default-context/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Mld.DefaultContext.Accounting, ['max_history'], name, value)


        class InheritableDefaults(Entity):
            """
            Inheritable Defaults
            
            .. attribute:: access_group
            
            	Access list specifying access group range
            	**type**\:  str
            
            	**length:** 1..64
            
            .. attribute:: explicit_tracking
            
            	IGMPv3 explicit host tracking
            	**type**\:   :py:class:`ExplicitTracking <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext.InheritableDefaults.ExplicitTracking>`
            
            	**presence node**\: True
            
            .. attribute:: maximum_groups_per_interface_oor
            
            	Configure maximum number of groups accepted per interface by this router
            	**type**\:   :py:class:`MaximumGroupsPerInterfaceOor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext.InheritableDefaults.MaximumGroupsPerInterfaceOor>`
            
            	**presence node**\: True
            
            .. attribute:: query_interval
            
            	Query interval in seconds
            	**type**\:  int
            
            	**range:** 1..3600
            
            	**units**\: second
            
            	**default value**\: 60
            
            .. attribute:: query_max_response_time
            
            	Query response value in seconds
            	**type**\:  int
            
            	**range:** 1..12
            
            	**units**\: second
            
            	**default value**\: 10
            
            .. attribute:: query_timeout
            
            	IGMP previous querier timeout
            	**type**\:  int
            
            	**range:** 60..300
            
            	**units**\: second
            
            .. attribute:: router_enable
            
            	Enabled or disabled, when value is TRUE or FALSE respectively
            	**type**\:  bool
            
            	**default value**\: true
            
            .. attribute:: version
            
            	Version number
            	**type**\:  int
            
            	**range:** 1..3
            
            	**default value**\: 3
            
            

            """

            _prefix = 'ipv4-igmp-cfg'
            _revision = '2016-10-10'

            def __init__(self):
                super(Mld.DefaultContext.InheritableDefaults, self).__init__()

                self.yang_name = "inheritable-defaults"
                self.yang_parent_name = "default-context"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"explicit-tracking" : ("explicit_tracking", Mld.DefaultContext.InheritableDefaults.ExplicitTracking), "maximum-groups-per-interface-oor" : ("maximum_groups_per_interface_oor", Mld.DefaultContext.InheritableDefaults.MaximumGroupsPerInterfaceOor)}
                self._child_list_classes = {}

                self.access_group = YLeaf(YType.str, "access-group")

                self.query_interval = YLeaf(YType.uint32, "query-interval")

                self.query_max_response_time = YLeaf(YType.uint32, "query-max-response-time")

                self.query_timeout = YLeaf(YType.uint32, "query-timeout")

                self.router_enable = YLeaf(YType.boolean, "router-enable")

                self.version = YLeaf(YType.uint32, "version")

                self.explicit_tracking = None
                self._children_name_map["explicit_tracking"] = "explicit-tracking"
                self._children_yang_names.add("explicit-tracking")

                self.maximum_groups_per_interface_oor = None
                self._children_name_map["maximum_groups_per_interface_oor"] = "maximum-groups-per-interface-oor"
                self._children_yang_names.add("maximum-groups-per-interface-oor")
                self._segment_path = lambda: "inheritable-defaults"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-igmp-cfg:mld/default-context/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Mld.DefaultContext.InheritableDefaults, ['access_group', 'query_interval', 'query_max_response_time', 'query_timeout', 'router_enable', 'version'], name, value)


            class ExplicitTracking(Entity):
                """
                IGMPv3 explicit host tracking
                
                .. attribute:: access_list_name
                
                	Access list specifying tracking group range
                	**type**\:  str
                
                	**length:** 1..64
                
                .. attribute:: enable
                
                	Enabled or disabled, when value is TRUE or FALSE respectively
                	**type**\:  bool
                
                	**mandatory**\: True
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'ipv4-igmp-cfg'
                _revision = '2016-10-10'

                def __init__(self):
                    super(Mld.DefaultContext.InheritableDefaults.ExplicitTracking, self).__init__()

                    self.yang_name = "explicit-tracking"
                    self.yang_parent_name = "inheritable-defaults"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}
                    self.is_presence_container = True

                    self.access_list_name = YLeaf(YType.str, "access-list-name")

                    self.enable = YLeaf(YType.boolean, "enable")
                    self._segment_path = lambda: "explicit-tracking"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-igmp-cfg:mld/default-context/inheritable-defaults/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Mld.DefaultContext.InheritableDefaults.ExplicitTracking, ['access_list_name', 'enable'], name, value)


            class MaximumGroupsPerInterfaceOor(Entity):
                """
                Configure maximum number of groups accepted per
                interface by this router
                
                .. attribute:: access_list_name
                
                	Access\-list to account for
                	**type**\:  str
                
                	**length:** 1..64
                
                .. attribute:: maximum_groups
                
                	Maximum number of groups accepted per interface by this router
                	**type**\:  int
                
                	**range:** 1..40000
                
                	**mandatory**\: True
                
                .. attribute:: warning_threshold
                
                	 WarningThreshold for number of groups accepted per interface by this router
                	**type**\:  int
                
                	**range:** 1..40000
                
                	**default value**\: 25000
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'ipv4-igmp-cfg'
                _revision = '2016-10-10'

                def __init__(self):
                    super(Mld.DefaultContext.InheritableDefaults.MaximumGroupsPerInterfaceOor, self).__init__()

                    self.yang_name = "maximum-groups-per-interface-oor"
                    self.yang_parent_name = "inheritable-defaults"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}
                    self.is_presence_container = True

                    self.access_list_name = YLeaf(YType.str, "access-list-name")

                    self.maximum_groups = YLeaf(YType.uint32, "maximum-groups")

                    self.warning_threshold = YLeaf(YType.uint32, "warning-threshold")
                    self._segment_path = lambda: "maximum-groups-per-interface-oor"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-igmp-cfg:mld/default-context/inheritable-defaults/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Mld.DefaultContext.InheritableDefaults.MaximumGroupsPerInterfaceOor, ['access_list_name', 'maximum_groups', 'warning_threshold'], name, value)


        class Interfaces(Entity):
            """
            Interface\-level configuration
            
            .. attribute:: interface
            
            	The name of the interface
            	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext.Interfaces.Interface>`
            
            

            """

            _prefix = 'ipv4-igmp-cfg'
            _revision = '2016-10-10'

            def __init__(self):
                super(Mld.DefaultContext.Interfaces, self).__init__()

                self.yang_name = "interfaces"
                self.yang_parent_name = "default-context"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"interface" : ("interface", Mld.DefaultContext.Interfaces.Interface)}

                self.interface = YList(self)
                self._segment_path = lambda: "interfaces"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-igmp-cfg:mld/default-context/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Mld.DefaultContext.Interfaces, [], name, value)


            class Interface(Entity):
                """
                The name of the interface
                
                .. attribute:: interface_name  <key>
                
                	Name of the interface
                	**type**\:  str
                
                	**pattern:** [a\-zA\-Z0\-9./\-]+
                
                .. attribute:: access_group
                
                	Access list specifying access group range
                	**type**\:  str
                
                	**length:** 1..64
                
                .. attribute:: explicit_tracking
                
                	IGMPv3 explicit host tracking
                	**type**\:   :py:class:`ExplicitTracking <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext.Interfaces.Interface.ExplicitTracking>`
                
                	**presence node**\: True
                
                .. attribute:: join_groups
                
                	IGMP join multicast group
                	**type**\:   :py:class:`JoinGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext.Interfaces.Interface.JoinGroups>`
                
                	**presence node**\: True
                
                .. attribute:: maximum_groups_per_interface_oor
                
                	Configure maximum number of groups accepted per interface by this router
                	**type**\:   :py:class:`MaximumGroupsPerInterfaceOor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext.Interfaces.Interface.MaximumGroupsPerInterfaceOor>`
                
                	**presence node**\: True
                
                .. attribute:: query_interval
                
                	Query interval in seconds
                	**type**\:  int
                
                	**range:** 1..3600
                
                	**units**\: second
                
                	**default value**\: 60
                
                .. attribute:: query_max_response_time
                
                	Query response value in seconds
                	**type**\:  int
                
                	**range:** 1..12
                
                	**units**\: second
                
                	**default value**\: 10
                
                .. attribute:: query_timeout
                
                	IGMP previous querier timeout
                	**type**\:  int
                
                	**range:** 60..300
                
                	**units**\: second
                
                .. attribute:: router_enable
                
                	Enabled or disabled, when value is TRUE or FALSE respectively
                	**type**\:  bool
                
                	**default value**\: true
                
                .. attribute:: static_group_group_addresses
                
                	IGMP static multicast group
                	**type**\:   :py:class:`StaticGroupGroupAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses>`
                
                .. attribute:: version
                
                	Version number
                	**type**\:  int
                
                	**range:** 1..3
                
                	**default value**\: 3
                
                

                """

                _prefix = 'ipv4-igmp-cfg'
                _revision = '2016-10-10'

                def __init__(self):
                    super(Mld.DefaultContext.Interfaces.Interface, self).__init__()

                    self.yang_name = "interface"
                    self.yang_parent_name = "interfaces"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"explicit-tracking" : ("explicit_tracking", Mld.DefaultContext.Interfaces.Interface.ExplicitTracking), "join-groups" : ("join_groups", Mld.DefaultContext.Interfaces.Interface.JoinGroups), "maximum-groups-per-interface-oor" : ("maximum_groups_per_interface_oor", Mld.DefaultContext.Interfaces.Interface.MaximumGroupsPerInterfaceOor), "static-group-group-addresses" : ("static_group_group_addresses", Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses)}
                    self._child_list_classes = {}

                    self.interface_name = YLeaf(YType.str, "interface-name")

                    self.access_group = YLeaf(YType.str, "access-group")

                    self.query_interval = YLeaf(YType.uint32, "query-interval")

                    self.query_max_response_time = YLeaf(YType.uint32, "query-max-response-time")

                    self.query_timeout = YLeaf(YType.uint32, "query-timeout")

                    self.router_enable = YLeaf(YType.boolean, "router-enable")

                    self.version = YLeaf(YType.uint32, "version")

                    self.explicit_tracking = None
                    self._children_name_map["explicit_tracking"] = "explicit-tracking"
                    self._children_yang_names.add("explicit-tracking")

                    self.join_groups = None
                    self._children_name_map["join_groups"] = "join-groups"
                    self._children_yang_names.add("join-groups")

                    self.maximum_groups_per_interface_oor = None
                    self._children_name_map["maximum_groups_per_interface_oor"] = "maximum-groups-per-interface-oor"
                    self._children_yang_names.add("maximum-groups-per-interface-oor")

                    self.static_group_group_addresses = Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses()
                    self.static_group_group_addresses.parent = self
                    self._children_name_map["static_group_group_addresses"] = "static-group-group-addresses"
                    self._children_yang_names.add("static-group-group-addresses")
                    self._segment_path = lambda: "interface" + "[interface-name='" + self.interface_name.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-igmp-cfg:mld/default-context/interfaces/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Mld.DefaultContext.Interfaces.Interface, ['interface_name', 'access_group', 'query_interval', 'query_max_response_time', 'query_timeout', 'router_enable', 'version'], name, value)


                class ExplicitTracking(Entity):
                    """
                    IGMPv3 explicit host tracking
                    
                    .. attribute:: access_list_name
                    
                    	Access list specifying tracking group range
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    .. attribute:: enable
                    
                    	Enabled or disabled, when value is TRUE or FALSE respectively
                    	**type**\:  bool
                    
                    	**mandatory**\: True
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-igmp-cfg'
                    _revision = '2016-10-10'

                    def __init__(self):
                        super(Mld.DefaultContext.Interfaces.Interface.ExplicitTracking, self).__init__()

                        self.yang_name = "explicit-tracking"
                        self.yang_parent_name = "interface"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}
                        self.is_presence_container = True

                        self.access_list_name = YLeaf(YType.str, "access-list-name")

                        self.enable = YLeaf(YType.boolean, "enable")
                        self._segment_path = lambda: "explicit-tracking"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mld.DefaultContext.Interfaces.Interface.ExplicitTracking, ['access_list_name', 'enable'], name, value)


                class JoinGroups(Entity):
                    """
                    IGMP join multicast group
                    
                    .. attribute:: join_group
                    
                    	IP group address and optional source address to include
                    	**type**\: list of    :py:class:`JoinGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext.Interfaces.Interface.JoinGroups.JoinGroup>`
                    
                    .. attribute:: join_group_source_address
                    
                    	IP group address and optional source address to include
                    	**type**\: list of    :py:class:`JoinGroupSourceAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext.Interfaces.Interface.JoinGroups.JoinGroupSourceAddress>`
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-igmp-cfg'
                    _revision = '2016-10-10'

                    def __init__(self):
                        super(Mld.DefaultContext.Interfaces.Interface.JoinGroups, self).__init__()

                        self.yang_name = "join-groups"
                        self.yang_parent_name = "interface"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"join-group" : ("join_group", Mld.DefaultContext.Interfaces.Interface.JoinGroups.JoinGroup), "join-group-source-address" : ("join_group_source_address", Mld.DefaultContext.Interfaces.Interface.JoinGroups.JoinGroupSourceAddress)}
                        self.is_presence_container = True

                        self.join_group = YList(self)
                        self.join_group_source_address = YList(self)
                        self._segment_path = lambda: "join-groups"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mld.DefaultContext.Interfaces.Interface.JoinGroups, [], name, value)


                    class JoinGroup(Entity):
                        """
                        IP group address and optional source address
                        to include
                        
                        .. attribute:: group_address  <key>
                        
                        	IP group address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: mode
                        
                        	Filter mode
                        	**type**\:   :py:class:`IgmpFilter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.IgmpFilter>`
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2016-10-10'

                        def __init__(self):
                            super(Mld.DefaultContext.Interfaces.Interface.JoinGroups.JoinGroup, self).__init__()

                            self.yang_name = "join-group"
                            self.yang_parent_name = "join-groups"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.group_address = YLeaf(YType.str, "group-address")

                            self.mode = YLeaf(YType.enumeration, "mode")
                            self._segment_path = lambda: "join-group" + "[group-address='" + self.group_address.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mld.DefaultContext.Interfaces.Interface.JoinGroups.JoinGroup, ['group_address', 'mode'], name, value)


                    class JoinGroupSourceAddress(Entity):
                        """
                        IP group address and optional source address
                        to include
                        
                        .. attribute:: group_address  <key>
                        
                        	IP group address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: source_address  <key>
                        
                        	Optional IP source address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: mode
                        
                        	Filter mode
                        	**type**\:   :py:class:`IgmpFilter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.IgmpFilter>`
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2016-10-10'

                        def __init__(self):
                            super(Mld.DefaultContext.Interfaces.Interface.JoinGroups.JoinGroupSourceAddress, self).__init__()

                            self.yang_name = "join-group-source-address"
                            self.yang_parent_name = "join-groups"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.group_address = YLeaf(YType.str, "group-address")

                            self.source_address = YLeaf(YType.str, "source-address")

                            self.mode = YLeaf(YType.enumeration, "mode")
                            self._segment_path = lambda: "join-group-source-address" + "[group-address='" + self.group_address.get() + "']" + "[source-address='" + self.source_address.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mld.DefaultContext.Interfaces.Interface.JoinGroups.JoinGroupSourceAddress, ['group_address', 'source_address', 'mode'], name, value)


                class MaximumGroupsPerInterfaceOor(Entity):
                    """
                    Configure maximum number of groups accepted per
                    interface by this router
                    
                    .. attribute:: access_list_name
                    
                    	Access\-list to account for
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    .. attribute:: maximum_groups
                    
                    	Maximum number of groups accepted per interface by this router
                    	**type**\:  int
                    
                    	**range:** 1..40000
                    
                    	**mandatory**\: True
                    
                    .. attribute:: warning_threshold
                    
                    	 WarningThreshold for number of groups accepted per interface by this router
                    	**type**\:  int
                    
                    	**range:** 1..40000
                    
                    	**default value**\: 25000
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-igmp-cfg'
                    _revision = '2016-10-10'

                    def __init__(self):
                        super(Mld.DefaultContext.Interfaces.Interface.MaximumGroupsPerInterfaceOor, self).__init__()

                        self.yang_name = "maximum-groups-per-interface-oor"
                        self.yang_parent_name = "interface"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}
                        self.is_presence_container = True

                        self.access_list_name = YLeaf(YType.str, "access-list-name")

                        self.maximum_groups = YLeaf(YType.uint32, "maximum-groups")

                        self.warning_threshold = YLeaf(YType.uint32, "warning-threshold")
                        self._segment_path = lambda: "maximum-groups-per-interface-oor"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mld.DefaultContext.Interfaces.Interface.MaximumGroupsPerInterfaceOor, ['access_list_name', 'maximum_groups', 'warning_threshold'], name, value)


                class StaticGroupGroupAddresses(Entity):
                    """
                    IGMP static multicast group
                    
                    .. attribute:: static_group_group_address
                    
                    	IP group address and optional source address to include
                    	**type**\: list of    :py:class:`StaticGroupGroupAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddress>`
                    
                    .. attribute:: static_group_group_address_group_address_mask
                    
                    	IP group address and optional source address to include
                    	**type**\: list of    :py:class:`StaticGroupGroupAddressGroupAddressMask <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMask>`
                    
                    .. attribute:: static_group_group_address_group_address_mask_source_address
                    
                    	IP group address and optional source address to include
                    	**type**\: list of    :py:class:`StaticGroupGroupAddressGroupAddressMaskSourceAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddress>`
                    
                    .. attribute:: static_group_group_address_group_address_mask_source_address_source_address_mask
                    
                    	IP group address and optional source address to include
                    	**type**\: list of    :py:class:`StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask>`
                    
                    .. attribute:: static_group_group_address_source_address
                    
                    	IP group address and optional source address to include
                    	**type**\: list of    :py:class:`StaticGroupGroupAddressSourceAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddress>`
                    
                    .. attribute:: static_group_group_address_source_address_source_address_mask
                    
                    	IP group address and optional source address to include
                    	**type**\: list of    :py:class:`StaticGroupGroupAddressSourceAddressSourceAddressMask <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddressSourceAddressMask>`
                    
                    

                    """

                    _prefix = 'ipv4-igmp-cfg'
                    _revision = '2016-10-10'

                    def __init__(self):
                        super(Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses, self).__init__()

                        self.yang_name = "static-group-group-addresses"
                        self.yang_parent_name = "interface"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"static-group-group-address" : ("static_group_group_address", Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddress), "static-group-group-address-group-address-mask" : ("static_group_group_address_group_address_mask", Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMask), "static-group-group-address-group-address-mask-source-address" : ("static_group_group_address_group_address_mask_source_address", Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddress), "static-group-group-address-group-address-mask-source-address-source-address-mask" : ("static_group_group_address_group_address_mask_source_address_source_address_mask", Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask), "static-group-group-address-source-address" : ("static_group_group_address_source_address", Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddress), "static-group-group-address-source-address-source-address-mask" : ("static_group_group_address_source_address_source_address_mask", Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddressSourceAddressMask)}

                        self.static_group_group_address = YList(self)
                        self.static_group_group_address_group_address_mask = YList(self)
                        self.static_group_group_address_group_address_mask_source_address = YList(self)
                        self.static_group_group_address_group_address_mask_source_address_source_address_mask = YList(self)
                        self.static_group_group_address_source_address = YList(self)
                        self.static_group_group_address_source_address_source_address_mask = YList(self)
                        self._segment_path = lambda: "static-group-group-addresses"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses, [], name, value)


                    class StaticGroupGroupAddress(Entity):
                        """
                        IP group address and optional source address
                        to include
                        
                        .. attribute:: group_address  <key>
                        
                        	IP group address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: group_count
                        
                        	Number of groups to join (do not set without GroupAddressMask)
                        	**type**\:  int
                        
                        	**range:** 1..512
                        
                        	**default value**\: 1
                        
                        .. attribute:: source_count
                        
                        	Number of sources to join (do not set without SourceAddressMask)
                        	**type**\:  int
                        
                        	**range:** 1..512
                        
                        	**default value**\: 1
                        
                        .. attribute:: suppress_report
                        
                        	Suppress reports
                        	**type**\:  bool
                        
                        	**default value**\: false
                        
                        

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2016-10-10'

                        def __init__(self):
                            super(Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddress, self).__init__()

                            self.yang_name = "static-group-group-address"
                            self.yang_parent_name = "static-group-group-addresses"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.group_address = YLeaf(YType.str, "group-address")

                            self.group_count = YLeaf(YType.uint32, "group-count")

                            self.source_count = YLeaf(YType.uint32, "source-count")

                            self.suppress_report = YLeaf(YType.boolean, "suppress-report")
                            self._segment_path = lambda: "static-group-group-address" + "[group-address='" + self.group_address.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddress, ['group_address', 'group_count', 'source_count', 'suppress_report'], name, value)


                    class StaticGroupGroupAddressGroupAddressMask(Entity):
                        """
                        IP group address and optional source address
                        to include
                        
                        .. attribute:: group_address  <key>
                        
                        	IP group address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: group_address_mask  <key>
                        
                        	Mask for Group Address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: group_count
                        
                        	Number of groups to join (do not set without GroupAddressMask)
                        	**type**\:  int
                        
                        	**range:** 1..512
                        
                        	**default value**\: 1
                        
                        .. attribute:: source_count
                        
                        	Number of sources to join (do not set without SourceAddressMask)
                        	**type**\:  int
                        
                        	**range:** 1..512
                        
                        	**default value**\: 1
                        
                        .. attribute:: suppress_report
                        
                        	Suppress reports
                        	**type**\:  bool
                        
                        	**default value**\: false
                        
                        

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2016-10-10'

                        def __init__(self):
                            super(Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMask, self).__init__()

                            self.yang_name = "static-group-group-address-group-address-mask"
                            self.yang_parent_name = "static-group-group-addresses"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.group_address = YLeaf(YType.str, "group-address")

                            self.group_address_mask = YLeaf(YType.str, "group-address-mask")

                            self.group_count = YLeaf(YType.uint32, "group-count")

                            self.source_count = YLeaf(YType.uint32, "source-count")

                            self.suppress_report = YLeaf(YType.boolean, "suppress-report")
                            self._segment_path = lambda: "static-group-group-address-group-address-mask" + "[group-address='" + self.group_address.get() + "']" + "[group-address-mask='" + self.group_address_mask.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMask, ['group_address', 'group_address_mask', 'group_count', 'source_count', 'suppress_report'], name, value)


                    class StaticGroupGroupAddressGroupAddressMaskSourceAddress(Entity):
                        """
                        IP group address and optional source address
                        to include
                        
                        .. attribute:: group_address  <key>
                        
                        	IP group address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: group_address_mask  <key>
                        
                        	Mask for Group Address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: source_address  <key>
                        
                        	IP source address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: group_count
                        
                        	Number of groups to join (do not set without GroupAddressMask)
                        	**type**\:  int
                        
                        	**range:** 1..512
                        
                        	**default value**\: 1
                        
                        .. attribute:: source_count
                        
                        	Number of sources to join (do not set without SourceAddressMask)
                        	**type**\:  int
                        
                        	**range:** 1..512
                        
                        	**default value**\: 1
                        
                        .. attribute:: suppress_report
                        
                        	Suppress reports
                        	**type**\:  bool
                        
                        	**default value**\: false
                        
                        

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2016-10-10'

                        def __init__(self):
                            super(Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddress, self).__init__()

                            self.yang_name = "static-group-group-address-group-address-mask-source-address"
                            self.yang_parent_name = "static-group-group-addresses"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.group_address = YLeaf(YType.str, "group-address")

                            self.group_address_mask = YLeaf(YType.str, "group-address-mask")

                            self.source_address = YLeaf(YType.str, "source-address")

                            self.group_count = YLeaf(YType.uint32, "group-count")

                            self.source_count = YLeaf(YType.uint32, "source-count")

                            self.suppress_report = YLeaf(YType.boolean, "suppress-report")
                            self._segment_path = lambda: "static-group-group-address-group-address-mask-source-address" + "[group-address='" + self.group_address.get() + "']" + "[group-address-mask='" + self.group_address_mask.get() + "']" + "[source-address='" + self.source_address.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddress, ['group_address', 'group_address_mask', 'source_address', 'group_count', 'source_count', 'suppress_report'], name, value)


                    class StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask(Entity):
                        """
                        IP group address and optional source address
                        to include
                        
                        .. attribute:: group_address  <key>
                        
                        	IP group address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: group_address_mask  <key>
                        
                        	Mask for Group Address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: source_address  <key>
                        
                        	IP source address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: source_address_mask  <key>
                        
                        	Mask for Source Address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: group_count
                        
                        	Number of groups to join (do not set without GroupAddressMask)
                        	**type**\:  int
                        
                        	**range:** 1..512
                        
                        	**default value**\: 1
                        
                        .. attribute:: source_count
                        
                        	Number of sources to join (do not set without SourceAddressMask)
                        	**type**\:  int
                        
                        	**range:** 1..512
                        
                        	**default value**\: 1
                        
                        .. attribute:: suppress_report
                        
                        	Suppress reports
                        	**type**\:  bool
                        
                        	**default value**\: false
                        
                        

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2016-10-10'

                        def __init__(self):
                            super(Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask, self).__init__()

                            self.yang_name = "static-group-group-address-group-address-mask-source-address-source-address-mask"
                            self.yang_parent_name = "static-group-group-addresses"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.group_address = YLeaf(YType.str, "group-address")

                            self.group_address_mask = YLeaf(YType.str, "group-address-mask")

                            self.source_address = YLeaf(YType.str, "source-address")

                            self.source_address_mask = YLeaf(YType.str, "source-address-mask")

                            self.group_count = YLeaf(YType.uint32, "group-count")

                            self.source_count = YLeaf(YType.uint32, "source-count")

                            self.suppress_report = YLeaf(YType.boolean, "suppress-report")
                            self._segment_path = lambda: "static-group-group-address-group-address-mask-source-address-source-address-mask" + "[group-address='" + self.group_address.get() + "']" + "[group-address-mask='" + self.group_address_mask.get() + "']" + "[source-address='" + self.source_address.get() + "']" + "[source-address-mask='" + self.source_address_mask.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask, ['group_address', 'group_address_mask', 'source_address', 'source_address_mask', 'group_count', 'source_count', 'suppress_report'], name, value)


                    class StaticGroupGroupAddressSourceAddress(Entity):
                        """
                        IP group address and optional source address
                        to include
                        
                        .. attribute:: group_address  <key>
                        
                        	IP group address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: source_address  <key>
                        
                        	IP source address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: group_count
                        
                        	Number of groups to join (do not set without GroupAddressMask)
                        	**type**\:  int
                        
                        	**range:** 1..512
                        
                        	**default value**\: 1
                        
                        .. attribute:: source_count
                        
                        	Number of sources to join (do not set without SourceAddressMask)
                        	**type**\:  int
                        
                        	**range:** 1..512
                        
                        	**default value**\: 1
                        
                        .. attribute:: suppress_report
                        
                        	Suppress reports
                        	**type**\:  bool
                        
                        	**default value**\: false
                        
                        

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2016-10-10'

                        def __init__(self):
                            super(Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddress, self).__init__()

                            self.yang_name = "static-group-group-address-source-address"
                            self.yang_parent_name = "static-group-group-addresses"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.group_address = YLeaf(YType.str, "group-address")

                            self.source_address = YLeaf(YType.str, "source-address")

                            self.group_count = YLeaf(YType.uint32, "group-count")

                            self.source_count = YLeaf(YType.uint32, "source-count")

                            self.suppress_report = YLeaf(YType.boolean, "suppress-report")
                            self._segment_path = lambda: "static-group-group-address-source-address" + "[group-address='" + self.group_address.get() + "']" + "[source-address='" + self.source_address.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddress, ['group_address', 'source_address', 'group_count', 'source_count', 'suppress_report'], name, value)


                    class StaticGroupGroupAddressSourceAddressSourceAddressMask(Entity):
                        """
                        IP group address and optional source address
                        to include
                        
                        .. attribute:: group_address  <key>
                        
                        	IP group address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: source_address  <key>
                        
                        	IP source address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: source_address_mask  <key>
                        
                        	Mask for Source Address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: group_count
                        
                        	Number of groups to join (do not set without GroupAddressMask)
                        	**type**\:  int
                        
                        	**range:** 1..512
                        
                        	**default value**\: 1
                        
                        .. attribute:: source_count
                        
                        	Number of sources to join (do not set without SourceAddressMask)
                        	**type**\:  int
                        
                        	**range:** 1..512
                        
                        	**default value**\: 1
                        
                        .. attribute:: suppress_report
                        
                        	Suppress reports
                        	**type**\:  bool
                        
                        	**default value**\: false
                        
                        

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2016-10-10'

                        def __init__(self):
                            super(Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddressSourceAddressMask, self).__init__()

                            self.yang_name = "static-group-group-address-source-address-source-address-mask"
                            self.yang_parent_name = "static-group-group-addresses"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.group_address = YLeaf(YType.str, "group-address")

                            self.source_address = YLeaf(YType.str, "source-address")

                            self.source_address_mask = YLeaf(YType.str, "source-address-mask")

                            self.group_count = YLeaf(YType.uint32, "group-count")

                            self.source_count = YLeaf(YType.uint32, "source-count")

                            self.suppress_report = YLeaf(YType.boolean, "suppress-report")
                            self._segment_path = lambda: "static-group-group-address-source-address-source-address-mask" + "[group-address='" + self.group_address.get() + "']" + "[source-address='" + self.source_address.get() + "']" + "[source-address-mask='" + self.source_address_mask.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddressSourceAddressMask, ['group_address', 'source_address', 'source_address_mask', 'group_count', 'source_count', 'suppress_report'], name, value)


        class Maximum(Entity):
            """
            Configure IGMP State Limits
            
            .. attribute:: maximum_groups
            
            	Configure maximum number of groups accepted by this router
            	**type**\:  int
            
            	**range:** 1..75000
            
            	**default value**\: 50000
            
            

            """

            _prefix = 'ipv4-igmp-cfg'
            _revision = '2016-10-10'

            def __init__(self):
                super(Mld.DefaultContext.Maximum, self).__init__()

                self.yang_name = "maximum"
                self.yang_parent_name = "default-context"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.maximum_groups = YLeaf(YType.uint32, "maximum-groups")
                self._segment_path = lambda: "maximum"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-igmp-cfg:mld/default-context/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Mld.DefaultContext.Maximum, ['maximum_groups'], name, value)


        class Nsf(Entity):
            """
            Configure NSF specific options
            
            .. attribute:: lifetime
            
            	Maximum time for IGMP NSF mode in seconds
            	**type**\:  int
            
            	**range:** 10..3600
            
            	**units**\: second
            
            	**default value**\: 60
            
            

            """

            _prefix = 'ipv4-igmp-cfg'
            _revision = '2016-10-10'

            def __init__(self):
                super(Mld.DefaultContext.Nsf, self).__init__()

                self.yang_name = "nsf"
                self.yang_parent_name = "default-context"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.lifetime = YLeaf(YType.uint32, "lifetime")
                self._segment_path = lambda: "nsf"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-igmp-cfg:mld/default-context/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Mld.DefaultContext.Nsf, ['lifetime'], name, value)


        class SsmAccessGroups(Entity):
            """
            IGMP Source specific mode
            
            .. attribute:: ssm_access_group
            
            	SSM static Access Group
            	**type**\: list of    :py:class:`SsmAccessGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext.SsmAccessGroups.SsmAccessGroup>`
            
            

            """

            _prefix = 'ipv4-igmp-cfg'
            _revision = '2016-10-10'

            def __init__(self):
                super(Mld.DefaultContext.SsmAccessGroups, self).__init__()

                self.yang_name = "ssm-access-groups"
                self.yang_parent_name = "default-context"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"ssm-access-group" : ("ssm_access_group", Mld.DefaultContext.SsmAccessGroups.SsmAccessGroup)}

                self.ssm_access_group = YList(self)
                self._segment_path = lambda: "ssm-access-groups"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-igmp-cfg:mld/default-context/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Mld.DefaultContext.SsmAccessGroups, [], name, value)


            class SsmAccessGroup(Entity):
                """
                SSM static Access Group
                
                .. attribute:: source_address  <key>
                
                	IP source address
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                
                ----
                .. attribute:: access_list_name
                
                	Access list specifying access group
                	**type**\:  str
                
                	**length:** 1..64
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'ipv4-igmp-cfg'
                _revision = '2016-10-10'

                def __init__(self):
                    super(Mld.DefaultContext.SsmAccessGroups.SsmAccessGroup, self).__init__()

                    self.yang_name = "ssm-access-group"
                    self.yang_parent_name = "ssm-access-groups"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.source_address = YLeaf(YType.str, "source-address")

                    self.access_list_name = YLeaf(YType.str, "access-list-name")
                    self._segment_path = lambda: "ssm-access-group" + "[source-address='" + self.source_address.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-igmp-cfg:mld/default-context/ssm-access-groups/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Mld.DefaultContext.SsmAccessGroups.SsmAccessGroup, ['source_address', 'access_list_name'], name, value)


        class Traffic(Entity):
            """
            Configure IGMP Traffic variables
            
            .. attribute:: profile
            
            	Configure the route\-policy profile
            	**type**\:  str
            
            	**length:** 1..64
            
            

            """

            _prefix = 'ipv4-igmp-cfg'
            _revision = '2016-10-10'

            def __init__(self):
                super(Mld.DefaultContext.Traffic, self).__init__()

                self.yang_name = "traffic"
                self.yang_parent_name = "default-context"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.profile = YLeaf(YType.str, "profile")
                self._segment_path = lambda: "traffic"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-igmp-cfg:mld/default-context/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Mld.DefaultContext.Traffic, ['profile'], name, value)


        class UnicastQosAdjust(Entity):
            """
            Configure IGMP QoS shapers for subscriber
            interfaces
            
            .. attribute:: adjustment_delay
            
            	Configure the QoS delay before programming (in seconds)
            	**type**\:  int
            
            	**range:** 0..10
            
            	**units**\: second
            
            	**default value**\: 1
            
            .. attribute:: download_interval
            
            	Configure the QoS download interval (in milliseconds)
            	**type**\:  int
            
            	**range:** 10..500
            
            	**units**\: millisecond
            
            	**default value**\: 100
            
            .. attribute:: hold_off
            
            	Configure the QoS hold off time (in seconds)
            	**type**\:  int
            
            	**range:** 5..1800
            
            	**units**\: second
            
            	**default value**\: 180
            
            

            """

            _prefix = 'ipv4-igmp-cfg'
            _revision = '2016-10-10'

            def __init__(self):
                super(Mld.DefaultContext.UnicastQosAdjust, self).__init__()

                self.yang_name = "unicast-qos-adjust"
                self.yang_parent_name = "default-context"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.adjustment_delay = YLeaf(YType.uint32, "adjustment-delay")

                self.download_interval = YLeaf(YType.uint32, "download-interval")

                self.hold_off = YLeaf(YType.uint32, "hold-off")
                self._segment_path = lambda: "unicast-qos-adjust"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-igmp-cfg:mld/default-context/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Mld.DefaultContext.UnicastQosAdjust, ['adjustment_delay', 'download_interval', 'hold_off'], name, value)


    class Vrfs(Entity):
        """
        VRF related configuration
        
        .. attribute:: vrf
        
        	Configuration for a particular vrf
        	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.Vrfs.Vrf>`
        
        

        """

        _prefix = 'ipv4-igmp-cfg'
        _revision = '2016-10-10'

        def __init__(self):
            super(Mld.Vrfs, self).__init__()

            self.yang_name = "vrfs"
            self.yang_parent_name = "mld"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"vrf" : ("vrf", Mld.Vrfs.Vrf)}

            self.vrf = YList(self)
            self._segment_path = lambda: "vrfs"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-igmp-cfg:mld/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Mld.Vrfs, [], name, value)


        class Vrf(Entity):
            """
            Configuration for a particular vrf
            
            .. attribute:: vrf_name  <key>
            
            	Name for this vrf
            	**type**\:  str
            
            	**length:** 1..32
            
            .. attribute:: inheritable_defaults
            
            	Inheritable Defaults
            	**type**\:   :py:class:`InheritableDefaults <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.Vrfs.Vrf.InheritableDefaults>`
            
            .. attribute:: interfaces
            
            	Interface\-level configuration
            	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.Vrfs.Vrf.Interfaces>`
            
            .. attribute:: maximum
            
            	Configure IGMP State Limits
            	**type**\:   :py:class:`Maximum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.Vrfs.Vrf.Maximum>`
            
            .. attribute:: robustness
            
            	Configure IGMP Robustness variable
            	**type**\:  int
            
            	**range:** 2..10
            
            	**default value**\: 2
            
            .. attribute:: ssm_access_groups
            
            	IGMP Source specific mode
            	**type**\:   :py:class:`SsmAccessGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.Vrfs.Vrf.SsmAccessGroups>`
            
            .. attribute:: ssmdns_query_group
            
            	Enable SSM mapping using DNS Query
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: traffic
            
            	Configure IGMP Traffic variables
            	**type**\:   :py:class:`Traffic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.Vrfs.Vrf.Traffic>`
            
            

            """

            _prefix = 'ipv4-igmp-cfg'
            _revision = '2016-10-10'

            def __init__(self):
                super(Mld.Vrfs.Vrf, self).__init__()

                self.yang_name = "vrf"
                self.yang_parent_name = "vrfs"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"inheritable-defaults" : ("inheritable_defaults", Mld.Vrfs.Vrf.InheritableDefaults), "interfaces" : ("interfaces", Mld.Vrfs.Vrf.Interfaces), "maximum" : ("maximum", Mld.Vrfs.Vrf.Maximum), "ssm-access-groups" : ("ssm_access_groups", Mld.Vrfs.Vrf.SsmAccessGroups), "traffic" : ("traffic", Mld.Vrfs.Vrf.Traffic)}
                self._child_list_classes = {}

                self.vrf_name = YLeaf(YType.str, "vrf-name")

                self.robustness = YLeaf(YType.uint32, "robustness")

                self.ssmdns_query_group = YLeaf(YType.empty, "ssmdns-query-group")

                self.inheritable_defaults = Mld.Vrfs.Vrf.InheritableDefaults()
                self.inheritable_defaults.parent = self
                self._children_name_map["inheritable_defaults"] = "inheritable-defaults"
                self._children_yang_names.add("inheritable-defaults")

                self.interfaces = Mld.Vrfs.Vrf.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"
                self._children_yang_names.add("interfaces")

                self.maximum = Mld.Vrfs.Vrf.Maximum()
                self.maximum.parent = self
                self._children_name_map["maximum"] = "maximum"
                self._children_yang_names.add("maximum")

                self.ssm_access_groups = Mld.Vrfs.Vrf.SsmAccessGroups()
                self.ssm_access_groups.parent = self
                self._children_name_map["ssm_access_groups"] = "ssm-access-groups"
                self._children_yang_names.add("ssm-access-groups")

                self.traffic = Mld.Vrfs.Vrf.Traffic()
                self.traffic.parent = self
                self._children_name_map["traffic"] = "traffic"
                self._children_yang_names.add("traffic")
                self._segment_path = lambda: "vrf" + "[vrf-name='" + self.vrf_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-igmp-cfg:mld/vrfs/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Mld.Vrfs.Vrf, ['vrf_name', 'robustness', 'ssmdns_query_group'], name, value)


            class InheritableDefaults(Entity):
                """
                Inheritable Defaults
                
                .. attribute:: access_group
                
                	Access list specifying access group range
                	**type**\:  str
                
                	**length:** 1..64
                
                .. attribute:: explicit_tracking
                
                	IGMPv3 explicit host tracking
                	**type**\:   :py:class:`ExplicitTracking <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.Vrfs.Vrf.InheritableDefaults.ExplicitTracking>`
                
                	**presence node**\: True
                
                .. attribute:: maximum_groups_per_interface_oor
                
                	Configure maximum number of groups accepted per interface by this router
                	**type**\:   :py:class:`MaximumGroupsPerInterfaceOor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.Vrfs.Vrf.InheritableDefaults.MaximumGroupsPerInterfaceOor>`
                
                	**presence node**\: True
                
                .. attribute:: query_interval
                
                	Query interval in seconds
                	**type**\:  int
                
                	**range:** 1..3600
                
                	**units**\: second
                
                	**default value**\: 60
                
                .. attribute:: query_max_response_time
                
                	Query response value in seconds
                	**type**\:  int
                
                	**range:** 1..12
                
                	**units**\: second
                
                	**default value**\: 10
                
                .. attribute:: query_timeout
                
                	IGMP previous querier timeout
                	**type**\:  int
                
                	**range:** 60..300
                
                	**units**\: second
                
                .. attribute:: router_enable
                
                	Enabled or disabled, when value is TRUE or FALSE respectively
                	**type**\:  bool
                
                	**default value**\: true
                
                .. attribute:: version
                
                	Version number
                	**type**\:  int
                
                	**range:** 1..3
                
                	**default value**\: 3
                
                

                """

                _prefix = 'ipv4-igmp-cfg'
                _revision = '2016-10-10'

                def __init__(self):
                    super(Mld.Vrfs.Vrf.InheritableDefaults, self).__init__()

                    self.yang_name = "inheritable-defaults"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"explicit-tracking" : ("explicit_tracking", Mld.Vrfs.Vrf.InheritableDefaults.ExplicitTracking), "maximum-groups-per-interface-oor" : ("maximum_groups_per_interface_oor", Mld.Vrfs.Vrf.InheritableDefaults.MaximumGroupsPerInterfaceOor)}
                    self._child_list_classes = {}

                    self.access_group = YLeaf(YType.str, "access-group")

                    self.query_interval = YLeaf(YType.uint32, "query-interval")

                    self.query_max_response_time = YLeaf(YType.uint32, "query-max-response-time")

                    self.query_timeout = YLeaf(YType.uint32, "query-timeout")

                    self.router_enable = YLeaf(YType.boolean, "router-enable")

                    self.version = YLeaf(YType.uint32, "version")

                    self.explicit_tracking = None
                    self._children_name_map["explicit_tracking"] = "explicit-tracking"
                    self._children_yang_names.add("explicit-tracking")

                    self.maximum_groups_per_interface_oor = None
                    self._children_name_map["maximum_groups_per_interface_oor"] = "maximum-groups-per-interface-oor"
                    self._children_yang_names.add("maximum-groups-per-interface-oor")
                    self._segment_path = lambda: "inheritable-defaults"

                def __setattr__(self, name, value):
                    self._perform_setattr(Mld.Vrfs.Vrf.InheritableDefaults, ['access_group', 'query_interval', 'query_max_response_time', 'query_timeout', 'router_enable', 'version'], name, value)


                class ExplicitTracking(Entity):
                    """
                    IGMPv3 explicit host tracking
                    
                    .. attribute:: access_list_name
                    
                    	Access list specifying tracking group range
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    .. attribute:: enable
                    
                    	Enabled or disabled, when value is TRUE or FALSE respectively
                    	**type**\:  bool
                    
                    	**mandatory**\: True
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-igmp-cfg'
                    _revision = '2016-10-10'

                    def __init__(self):
                        super(Mld.Vrfs.Vrf.InheritableDefaults.ExplicitTracking, self).__init__()

                        self.yang_name = "explicit-tracking"
                        self.yang_parent_name = "inheritable-defaults"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}
                        self.is_presence_container = True

                        self.access_list_name = YLeaf(YType.str, "access-list-name")

                        self.enable = YLeaf(YType.boolean, "enable")
                        self._segment_path = lambda: "explicit-tracking"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mld.Vrfs.Vrf.InheritableDefaults.ExplicitTracking, ['access_list_name', 'enable'], name, value)


                class MaximumGroupsPerInterfaceOor(Entity):
                    """
                    Configure maximum number of groups accepted per
                    interface by this router
                    
                    .. attribute:: access_list_name
                    
                    	Access\-list to account for
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    .. attribute:: maximum_groups
                    
                    	Maximum number of groups accepted per interface by this router
                    	**type**\:  int
                    
                    	**range:** 1..40000
                    
                    	**mandatory**\: True
                    
                    .. attribute:: warning_threshold
                    
                    	 WarningThreshold for number of groups accepted per interface by this router
                    	**type**\:  int
                    
                    	**range:** 1..40000
                    
                    	**default value**\: 25000
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-igmp-cfg'
                    _revision = '2016-10-10'

                    def __init__(self):
                        super(Mld.Vrfs.Vrf.InheritableDefaults.MaximumGroupsPerInterfaceOor, self).__init__()

                        self.yang_name = "maximum-groups-per-interface-oor"
                        self.yang_parent_name = "inheritable-defaults"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}
                        self.is_presence_container = True

                        self.access_list_name = YLeaf(YType.str, "access-list-name")

                        self.maximum_groups = YLeaf(YType.uint32, "maximum-groups")

                        self.warning_threshold = YLeaf(YType.uint32, "warning-threshold")
                        self._segment_path = lambda: "maximum-groups-per-interface-oor"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mld.Vrfs.Vrf.InheritableDefaults.MaximumGroupsPerInterfaceOor, ['access_list_name', 'maximum_groups', 'warning_threshold'], name, value)


            class Interfaces(Entity):
                """
                Interface\-level configuration
                
                .. attribute:: interface
                
                	The name of the interface
                	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.Vrfs.Vrf.Interfaces.Interface>`
                
                

                """

                _prefix = 'ipv4-igmp-cfg'
                _revision = '2016-10-10'

                def __init__(self):
                    super(Mld.Vrfs.Vrf.Interfaces, self).__init__()

                    self.yang_name = "interfaces"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"interface" : ("interface", Mld.Vrfs.Vrf.Interfaces.Interface)}

                    self.interface = YList(self)
                    self._segment_path = lambda: "interfaces"

                def __setattr__(self, name, value):
                    self._perform_setattr(Mld.Vrfs.Vrf.Interfaces, [], name, value)


                class Interface(Entity):
                    """
                    The name of the interface
                    
                    .. attribute:: interface_name  <key>
                    
                    	Name of the interface
                    	**type**\:  str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
                    .. attribute:: access_group
                    
                    	Access list specifying access group range
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    .. attribute:: explicit_tracking
                    
                    	IGMPv3 explicit host tracking
                    	**type**\:   :py:class:`ExplicitTracking <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.Vrfs.Vrf.Interfaces.Interface.ExplicitTracking>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: join_groups
                    
                    	IGMP join multicast group
                    	**type**\:   :py:class:`JoinGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.Vrfs.Vrf.Interfaces.Interface.JoinGroups>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: maximum_groups_per_interface_oor
                    
                    	Configure maximum number of groups accepted per interface by this router
                    	**type**\:   :py:class:`MaximumGroupsPerInterfaceOor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.Vrfs.Vrf.Interfaces.Interface.MaximumGroupsPerInterfaceOor>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: query_interval
                    
                    	Query interval in seconds
                    	**type**\:  int
                    
                    	**range:** 1..3600
                    
                    	**units**\: second
                    
                    	**default value**\: 60
                    
                    .. attribute:: query_max_response_time
                    
                    	Query response value in seconds
                    	**type**\:  int
                    
                    	**range:** 1..12
                    
                    	**units**\: second
                    
                    	**default value**\: 10
                    
                    .. attribute:: query_timeout
                    
                    	IGMP previous querier timeout
                    	**type**\:  int
                    
                    	**range:** 60..300
                    
                    	**units**\: second
                    
                    .. attribute:: router_enable
                    
                    	Enabled or disabled, when value is TRUE or FALSE respectively
                    	**type**\:  bool
                    
                    	**default value**\: true
                    
                    .. attribute:: static_group_group_addresses
                    
                    	IGMP static multicast group
                    	**type**\:   :py:class:`StaticGroupGroupAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses>`
                    
                    .. attribute:: version
                    
                    	Version number
                    	**type**\:  int
                    
                    	**range:** 1..3
                    
                    	**default value**\: 3
                    
                    

                    """

                    _prefix = 'ipv4-igmp-cfg'
                    _revision = '2016-10-10'

                    def __init__(self):
                        super(Mld.Vrfs.Vrf.Interfaces.Interface, self).__init__()

                        self.yang_name = "interface"
                        self.yang_parent_name = "interfaces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"explicit-tracking" : ("explicit_tracking", Mld.Vrfs.Vrf.Interfaces.Interface.ExplicitTracking), "join-groups" : ("join_groups", Mld.Vrfs.Vrf.Interfaces.Interface.JoinGroups), "maximum-groups-per-interface-oor" : ("maximum_groups_per_interface_oor", Mld.Vrfs.Vrf.Interfaces.Interface.MaximumGroupsPerInterfaceOor), "static-group-group-addresses" : ("static_group_group_addresses", Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses)}
                        self._child_list_classes = {}

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.access_group = YLeaf(YType.str, "access-group")

                        self.query_interval = YLeaf(YType.uint32, "query-interval")

                        self.query_max_response_time = YLeaf(YType.uint32, "query-max-response-time")

                        self.query_timeout = YLeaf(YType.uint32, "query-timeout")

                        self.router_enable = YLeaf(YType.boolean, "router-enable")

                        self.version = YLeaf(YType.uint32, "version")

                        self.explicit_tracking = None
                        self._children_name_map["explicit_tracking"] = "explicit-tracking"
                        self._children_yang_names.add("explicit-tracking")

                        self.join_groups = None
                        self._children_name_map["join_groups"] = "join-groups"
                        self._children_yang_names.add("join-groups")

                        self.maximum_groups_per_interface_oor = None
                        self._children_name_map["maximum_groups_per_interface_oor"] = "maximum-groups-per-interface-oor"
                        self._children_yang_names.add("maximum-groups-per-interface-oor")

                        self.static_group_group_addresses = Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses()
                        self.static_group_group_addresses.parent = self
                        self._children_name_map["static_group_group_addresses"] = "static-group-group-addresses"
                        self._children_yang_names.add("static-group-group-addresses")
                        self._segment_path = lambda: "interface" + "[interface-name='" + self.interface_name.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mld.Vrfs.Vrf.Interfaces.Interface, ['interface_name', 'access_group', 'query_interval', 'query_max_response_time', 'query_timeout', 'router_enable', 'version'], name, value)


                    class ExplicitTracking(Entity):
                        """
                        IGMPv3 explicit host tracking
                        
                        .. attribute:: access_list_name
                        
                        	Access list specifying tracking group range
                        	**type**\:  str
                        
                        	**length:** 1..64
                        
                        .. attribute:: enable
                        
                        	Enabled or disabled, when value is TRUE or FALSE respectively
                        	**type**\:  bool
                        
                        	**mandatory**\: True
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2016-10-10'

                        def __init__(self):
                            super(Mld.Vrfs.Vrf.Interfaces.Interface.ExplicitTracking, self).__init__()

                            self.yang_name = "explicit-tracking"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}
                            self.is_presence_container = True

                            self.access_list_name = YLeaf(YType.str, "access-list-name")

                            self.enable = YLeaf(YType.boolean, "enable")
                            self._segment_path = lambda: "explicit-tracking"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mld.Vrfs.Vrf.Interfaces.Interface.ExplicitTracking, ['access_list_name', 'enable'], name, value)


                    class JoinGroups(Entity):
                        """
                        IGMP join multicast group
                        
                        .. attribute:: join_group
                        
                        	IP group address and optional source address to include
                        	**type**\: list of    :py:class:`JoinGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.Vrfs.Vrf.Interfaces.Interface.JoinGroups.JoinGroup>`
                        
                        .. attribute:: join_group_source_address
                        
                        	IP group address and optional source address to include
                        	**type**\: list of    :py:class:`JoinGroupSourceAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.Vrfs.Vrf.Interfaces.Interface.JoinGroups.JoinGroupSourceAddress>`
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2016-10-10'

                        def __init__(self):
                            super(Mld.Vrfs.Vrf.Interfaces.Interface.JoinGroups, self).__init__()

                            self.yang_name = "join-groups"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"join-group" : ("join_group", Mld.Vrfs.Vrf.Interfaces.Interface.JoinGroups.JoinGroup), "join-group-source-address" : ("join_group_source_address", Mld.Vrfs.Vrf.Interfaces.Interface.JoinGroups.JoinGroupSourceAddress)}
                            self.is_presence_container = True

                            self.join_group = YList(self)
                            self.join_group_source_address = YList(self)
                            self._segment_path = lambda: "join-groups"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mld.Vrfs.Vrf.Interfaces.Interface.JoinGroups, [], name, value)


                        class JoinGroup(Entity):
                            """
                            IP group address and optional source address
                            to include
                            
                            .. attribute:: group_address  <key>
                            
                            	IP group address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: mode
                            
                            	Filter mode
                            	**type**\:   :py:class:`IgmpFilter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.IgmpFilter>`
                            
                            	**mandatory**\: True
                            
                            

                            """

                            _prefix = 'ipv4-igmp-cfg'
                            _revision = '2016-10-10'

                            def __init__(self):
                                super(Mld.Vrfs.Vrf.Interfaces.Interface.JoinGroups.JoinGroup, self).__init__()

                                self.yang_name = "join-group"
                                self.yang_parent_name = "join-groups"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.group_address = YLeaf(YType.str, "group-address")

                                self.mode = YLeaf(YType.enumeration, "mode")
                                self._segment_path = lambda: "join-group" + "[group-address='" + self.group_address.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mld.Vrfs.Vrf.Interfaces.Interface.JoinGroups.JoinGroup, ['group_address', 'mode'], name, value)


                        class JoinGroupSourceAddress(Entity):
                            """
                            IP group address and optional source address
                            to include
                            
                            .. attribute:: group_address  <key>
                            
                            	IP group address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: source_address  <key>
                            
                            	Optional IP source address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: mode
                            
                            	Filter mode
                            	**type**\:   :py:class:`IgmpFilter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.IgmpFilter>`
                            
                            	**mandatory**\: True
                            
                            

                            """

                            _prefix = 'ipv4-igmp-cfg'
                            _revision = '2016-10-10'

                            def __init__(self):
                                super(Mld.Vrfs.Vrf.Interfaces.Interface.JoinGroups.JoinGroupSourceAddress, self).__init__()

                                self.yang_name = "join-group-source-address"
                                self.yang_parent_name = "join-groups"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.group_address = YLeaf(YType.str, "group-address")

                                self.source_address = YLeaf(YType.str, "source-address")

                                self.mode = YLeaf(YType.enumeration, "mode")
                                self._segment_path = lambda: "join-group-source-address" + "[group-address='" + self.group_address.get() + "']" + "[source-address='" + self.source_address.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mld.Vrfs.Vrf.Interfaces.Interface.JoinGroups.JoinGroupSourceAddress, ['group_address', 'source_address', 'mode'], name, value)


                    class MaximumGroupsPerInterfaceOor(Entity):
                        """
                        Configure maximum number of groups accepted per
                        interface by this router
                        
                        .. attribute:: access_list_name
                        
                        	Access\-list to account for
                        	**type**\:  str
                        
                        	**length:** 1..64
                        
                        .. attribute:: maximum_groups
                        
                        	Maximum number of groups accepted per interface by this router
                        	**type**\:  int
                        
                        	**range:** 1..40000
                        
                        	**mandatory**\: True
                        
                        .. attribute:: warning_threshold
                        
                        	 WarningThreshold for number of groups accepted per interface by this router
                        	**type**\:  int
                        
                        	**range:** 1..40000
                        
                        	**default value**\: 25000
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2016-10-10'

                        def __init__(self):
                            super(Mld.Vrfs.Vrf.Interfaces.Interface.MaximumGroupsPerInterfaceOor, self).__init__()

                            self.yang_name = "maximum-groups-per-interface-oor"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}
                            self.is_presence_container = True

                            self.access_list_name = YLeaf(YType.str, "access-list-name")

                            self.maximum_groups = YLeaf(YType.uint32, "maximum-groups")

                            self.warning_threshold = YLeaf(YType.uint32, "warning-threshold")
                            self._segment_path = lambda: "maximum-groups-per-interface-oor"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mld.Vrfs.Vrf.Interfaces.Interface.MaximumGroupsPerInterfaceOor, ['access_list_name', 'maximum_groups', 'warning_threshold'], name, value)


                    class StaticGroupGroupAddresses(Entity):
                        """
                        IGMP static multicast group
                        
                        .. attribute:: static_group_group_address
                        
                        	IP group address and optional source address to include
                        	**type**\: list of    :py:class:`StaticGroupGroupAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddress>`
                        
                        .. attribute:: static_group_group_address_group_address_mask
                        
                        	IP group address and optional source address to include
                        	**type**\: list of    :py:class:`StaticGroupGroupAddressGroupAddressMask <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMask>`
                        
                        .. attribute:: static_group_group_address_group_address_mask_source_address
                        
                        	IP group address and optional source address to include
                        	**type**\: list of    :py:class:`StaticGroupGroupAddressGroupAddressMaskSourceAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddress>`
                        
                        .. attribute:: static_group_group_address_group_address_mask_source_address_source_address_mask
                        
                        	IP group address and optional source address to include
                        	**type**\: list of    :py:class:`StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask>`
                        
                        .. attribute:: static_group_group_address_source_address
                        
                        	IP group address and optional source address to include
                        	**type**\: list of    :py:class:`StaticGroupGroupAddressSourceAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddress>`
                        
                        .. attribute:: static_group_group_address_source_address_source_address_mask
                        
                        	IP group address and optional source address to include
                        	**type**\: list of    :py:class:`StaticGroupGroupAddressSourceAddressSourceAddressMask <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddressSourceAddressMask>`
                        
                        

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2016-10-10'

                        def __init__(self):
                            super(Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses, self).__init__()

                            self.yang_name = "static-group-group-addresses"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"static-group-group-address" : ("static_group_group_address", Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddress), "static-group-group-address-group-address-mask" : ("static_group_group_address_group_address_mask", Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMask), "static-group-group-address-group-address-mask-source-address" : ("static_group_group_address_group_address_mask_source_address", Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddress), "static-group-group-address-group-address-mask-source-address-source-address-mask" : ("static_group_group_address_group_address_mask_source_address_source_address_mask", Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask), "static-group-group-address-source-address" : ("static_group_group_address_source_address", Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddress), "static-group-group-address-source-address-source-address-mask" : ("static_group_group_address_source_address_source_address_mask", Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddressSourceAddressMask)}

                            self.static_group_group_address = YList(self)
                            self.static_group_group_address_group_address_mask = YList(self)
                            self.static_group_group_address_group_address_mask_source_address = YList(self)
                            self.static_group_group_address_group_address_mask_source_address_source_address_mask = YList(self)
                            self.static_group_group_address_source_address = YList(self)
                            self.static_group_group_address_source_address_source_address_mask = YList(self)
                            self._segment_path = lambda: "static-group-group-addresses"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses, [], name, value)


                        class StaticGroupGroupAddress(Entity):
                            """
                            IP group address and optional source address
                            to include
                            
                            .. attribute:: group_address  <key>
                            
                            	IP group address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: group_count
                            
                            	Number of groups to join (do not set without GroupAddressMask)
                            	**type**\:  int
                            
                            	**range:** 1..512
                            
                            	**default value**\: 1
                            
                            .. attribute:: source_count
                            
                            	Number of sources to join (do not set without SourceAddressMask)
                            	**type**\:  int
                            
                            	**range:** 1..512
                            
                            	**default value**\: 1
                            
                            .. attribute:: suppress_report
                            
                            	Suppress reports
                            	**type**\:  bool
                            
                            	**default value**\: false
                            
                            

                            """

                            _prefix = 'ipv4-igmp-cfg'
                            _revision = '2016-10-10'

                            def __init__(self):
                                super(Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddress, self).__init__()

                                self.yang_name = "static-group-group-address"
                                self.yang_parent_name = "static-group-group-addresses"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.group_address = YLeaf(YType.str, "group-address")

                                self.group_count = YLeaf(YType.uint32, "group-count")

                                self.source_count = YLeaf(YType.uint32, "source-count")

                                self.suppress_report = YLeaf(YType.boolean, "suppress-report")
                                self._segment_path = lambda: "static-group-group-address" + "[group-address='" + self.group_address.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddress, ['group_address', 'group_count', 'source_count', 'suppress_report'], name, value)


                        class StaticGroupGroupAddressGroupAddressMask(Entity):
                            """
                            IP group address and optional source address
                            to include
                            
                            .. attribute:: group_address  <key>
                            
                            	IP group address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: group_address_mask  <key>
                            
                            	Mask for Group Address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: group_count
                            
                            	Number of groups to join (do not set without GroupAddressMask)
                            	**type**\:  int
                            
                            	**range:** 1..512
                            
                            	**default value**\: 1
                            
                            .. attribute:: source_count
                            
                            	Number of sources to join (do not set without SourceAddressMask)
                            	**type**\:  int
                            
                            	**range:** 1..512
                            
                            	**default value**\: 1
                            
                            .. attribute:: suppress_report
                            
                            	Suppress reports
                            	**type**\:  bool
                            
                            	**default value**\: false
                            
                            

                            """

                            _prefix = 'ipv4-igmp-cfg'
                            _revision = '2016-10-10'

                            def __init__(self):
                                super(Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMask, self).__init__()

                                self.yang_name = "static-group-group-address-group-address-mask"
                                self.yang_parent_name = "static-group-group-addresses"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.group_address = YLeaf(YType.str, "group-address")

                                self.group_address_mask = YLeaf(YType.str, "group-address-mask")

                                self.group_count = YLeaf(YType.uint32, "group-count")

                                self.source_count = YLeaf(YType.uint32, "source-count")

                                self.suppress_report = YLeaf(YType.boolean, "suppress-report")
                                self._segment_path = lambda: "static-group-group-address-group-address-mask" + "[group-address='" + self.group_address.get() + "']" + "[group-address-mask='" + self.group_address_mask.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMask, ['group_address', 'group_address_mask', 'group_count', 'source_count', 'suppress_report'], name, value)


                        class StaticGroupGroupAddressGroupAddressMaskSourceAddress(Entity):
                            """
                            IP group address and optional source address
                            to include
                            
                            .. attribute:: group_address  <key>
                            
                            	IP group address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: group_address_mask  <key>
                            
                            	Mask for Group Address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: source_address  <key>
                            
                            	IP source address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: group_count
                            
                            	Number of groups to join (do not set without GroupAddressMask)
                            	**type**\:  int
                            
                            	**range:** 1..512
                            
                            	**default value**\: 1
                            
                            .. attribute:: source_count
                            
                            	Number of sources to join (do not set without SourceAddressMask)
                            	**type**\:  int
                            
                            	**range:** 1..512
                            
                            	**default value**\: 1
                            
                            .. attribute:: suppress_report
                            
                            	Suppress reports
                            	**type**\:  bool
                            
                            	**default value**\: false
                            
                            

                            """

                            _prefix = 'ipv4-igmp-cfg'
                            _revision = '2016-10-10'

                            def __init__(self):
                                super(Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddress, self).__init__()

                                self.yang_name = "static-group-group-address-group-address-mask-source-address"
                                self.yang_parent_name = "static-group-group-addresses"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.group_address = YLeaf(YType.str, "group-address")

                                self.group_address_mask = YLeaf(YType.str, "group-address-mask")

                                self.source_address = YLeaf(YType.str, "source-address")

                                self.group_count = YLeaf(YType.uint32, "group-count")

                                self.source_count = YLeaf(YType.uint32, "source-count")

                                self.suppress_report = YLeaf(YType.boolean, "suppress-report")
                                self._segment_path = lambda: "static-group-group-address-group-address-mask-source-address" + "[group-address='" + self.group_address.get() + "']" + "[group-address-mask='" + self.group_address_mask.get() + "']" + "[source-address='" + self.source_address.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddress, ['group_address', 'group_address_mask', 'source_address', 'group_count', 'source_count', 'suppress_report'], name, value)


                        class StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask(Entity):
                            """
                            IP group address and optional source address
                            to include
                            
                            .. attribute:: group_address  <key>
                            
                            	IP group address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: group_address_mask  <key>
                            
                            	Mask for Group Address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: source_address  <key>
                            
                            	IP source address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: source_address_mask  <key>
                            
                            	Mask for Source Address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: group_count
                            
                            	Number of groups to join (do not set without GroupAddressMask)
                            	**type**\:  int
                            
                            	**range:** 1..512
                            
                            	**default value**\: 1
                            
                            .. attribute:: source_count
                            
                            	Number of sources to join (do not set without SourceAddressMask)
                            	**type**\:  int
                            
                            	**range:** 1..512
                            
                            	**default value**\: 1
                            
                            .. attribute:: suppress_report
                            
                            	Suppress reports
                            	**type**\:  bool
                            
                            	**default value**\: false
                            
                            

                            """

                            _prefix = 'ipv4-igmp-cfg'
                            _revision = '2016-10-10'

                            def __init__(self):
                                super(Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask, self).__init__()

                                self.yang_name = "static-group-group-address-group-address-mask-source-address-source-address-mask"
                                self.yang_parent_name = "static-group-group-addresses"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.group_address = YLeaf(YType.str, "group-address")

                                self.group_address_mask = YLeaf(YType.str, "group-address-mask")

                                self.source_address = YLeaf(YType.str, "source-address")

                                self.source_address_mask = YLeaf(YType.str, "source-address-mask")

                                self.group_count = YLeaf(YType.uint32, "group-count")

                                self.source_count = YLeaf(YType.uint32, "source-count")

                                self.suppress_report = YLeaf(YType.boolean, "suppress-report")
                                self._segment_path = lambda: "static-group-group-address-group-address-mask-source-address-source-address-mask" + "[group-address='" + self.group_address.get() + "']" + "[group-address-mask='" + self.group_address_mask.get() + "']" + "[source-address='" + self.source_address.get() + "']" + "[source-address-mask='" + self.source_address_mask.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask, ['group_address', 'group_address_mask', 'source_address', 'source_address_mask', 'group_count', 'source_count', 'suppress_report'], name, value)


                        class StaticGroupGroupAddressSourceAddress(Entity):
                            """
                            IP group address and optional source address
                            to include
                            
                            .. attribute:: group_address  <key>
                            
                            	IP group address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: source_address  <key>
                            
                            	IP source address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: group_count
                            
                            	Number of groups to join (do not set without GroupAddressMask)
                            	**type**\:  int
                            
                            	**range:** 1..512
                            
                            	**default value**\: 1
                            
                            .. attribute:: source_count
                            
                            	Number of sources to join (do not set without SourceAddressMask)
                            	**type**\:  int
                            
                            	**range:** 1..512
                            
                            	**default value**\: 1
                            
                            .. attribute:: suppress_report
                            
                            	Suppress reports
                            	**type**\:  bool
                            
                            	**default value**\: false
                            
                            

                            """

                            _prefix = 'ipv4-igmp-cfg'
                            _revision = '2016-10-10'

                            def __init__(self):
                                super(Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddress, self).__init__()

                                self.yang_name = "static-group-group-address-source-address"
                                self.yang_parent_name = "static-group-group-addresses"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.group_address = YLeaf(YType.str, "group-address")

                                self.source_address = YLeaf(YType.str, "source-address")

                                self.group_count = YLeaf(YType.uint32, "group-count")

                                self.source_count = YLeaf(YType.uint32, "source-count")

                                self.suppress_report = YLeaf(YType.boolean, "suppress-report")
                                self._segment_path = lambda: "static-group-group-address-source-address" + "[group-address='" + self.group_address.get() + "']" + "[source-address='" + self.source_address.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddress, ['group_address', 'source_address', 'group_count', 'source_count', 'suppress_report'], name, value)


                        class StaticGroupGroupAddressSourceAddressSourceAddressMask(Entity):
                            """
                            IP group address and optional source address
                            to include
                            
                            .. attribute:: group_address  <key>
                            
                            	IP group address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: source_address  <key>
                            
                            	IP source address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: source_address_mask  <key>
                            
                            	Mask for Source Address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: group_count
                            
                            	Number of groups to join (do not set without GroupAddressMask)
                            	**type**\:  int
                            
                            	**range:** 1..512
                            
                            	**default value**\: 1
                            
                            .. attribute:: source_count
                            
                            	Number of sources to join (do not set without SourceAddressMask)
                            	**type**\:  int
                            
                            	**range:** 1..512
                            
                            	**default value**\: 1
                            
                            .. attribute:: suppress_report
                            
                            	Suppress reports
                            	**type**\:  bool
                            
                            	**default value**\: false
                            
                            

                            """

                            _prefix = 'ipv4-igmp-cfg'
                            _revision = '2016-10-10'

                            def __init__(self):
                                super(Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddressSourceAddressMask, self).__init__()

                                self.yang_name = "static-group-group-address-source-address-source-address-mask"
                                self.yang_parent_name = "static-group-group-addresses"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.group_address = YLeaf(YType.str, "group-address")

                                self.source_address = YLeaf(YType.str, "source-address")

                                self.source_address_mask = YLeaf(YType.str, "source-address-mask")

                                self.group_count = YLeaf(YType.uint32, "group-count")

                                self.source_count = YLeaf(YType.uint32, "source-count")

                                self.suppress_report = YLeaf(YType.boolean, "suppress-report")
                                self._segment_path = lambda: "static-group-group-address-source-address-source-address-mask" + "[group-address='" + self.group_address.get() + "']" + "[source-address='" + self.source_address.get() + "']" + "[source-address-mask='" + self.source_address_mask.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddressSourceAddressMask, ['group_address', 'source_address', 'source_address_mask', 'group_count', 'source_count', 'suppress_report'], name, value)


            class Maximum(Entity):
                """
                Configure IGMP State Limits
                
                .. attribute:: maximum_groups
                
                	Configure maximum number of groups accepted by this router
                	**type**\:  int
                
                	**range:** 1..75000
                
                	**default value**\: 50000
                
                

                """

                _prefix = 'ipv4-igmp-cfg'
                _revision = '2016-10-10'

                def __init__(self):
                    super(Mld.Vrfs.Vrf.Maximum, self).__init__()

                    self.yang_name = "maximum"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.maximum_groups = YLeaf(YType.uint32, "maximum-groups")
                    self._segment_path = lambda: "maximum"

                def __setattr__(self, name, value):
                    self._perform_setattr(Mld.Vrfs.Vrf.Maximum, ['maximum_groups'], name, value)


            class SsmAccessGroups(Entity):
                """
                IGMP Source specific mode
                
                .. attribute:: ssm_access_group
                
                	SSM static Access Group
                	**type**\: list of    :py:class:`SsmAccessGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.Vrfs.Vrf.SsmAccessGroups.SsmAccessGroup>`
                
                

                """

                _prefix = 'ipv4-igmp-cfg'
                _revision = '2016-10-10'

                def __init__(self):
                    super(Mld.Vrfs.Vrf.SsmAccessGroups, self).__init__()

                    self.yang_name = "ssm-access-groups"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"ssm-access-group" : ("ssm_access_group", Mld.Vrfs.Vrf.SsmAccessGroups.SsmAccessGroup)}

                    self.ssm_access_group = YList(self)
                    self._segment_path = lambda: "ssm-access-groups"

                def __setattr__(self, name, value):
                    self._perform_setattr(Mld.Vrfs.Vrf.SsmAccessGroups, [], name, value)


                class SsmAccessGroup(Entity):
                    """
                    SSM static Access Group
                    
                    .. attribute:: source_address  <key>
                    
                    	IP source address
                    	**type**\: one of the below types:
                    
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    .. attribute:: access_list_name
                    
                    	Access list specifying access group
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    	**mandatory**\: True
                    
                    

                    """

                    _prefix = 'ipv4-igmp-cfg'
                    _revision = '2016-10-10'

                    def __init__(self):
                        super(Mld.Vrfs.Vrf.SsmAccessGroups.SsmAccessGroup, self).__init__()

                        self.yang_name = "ssm-access-group"
                        self.yang_parent_name = "ssm-access-groups"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.source_address = YLeaf(YType.str, "source-address")

                        self.access_list_name = YLeaf(YType.str, "access-list-name")
                        self._segment_path = lambda: "ssm-access-group" + "[source-address='" + self.source_address.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mld.Vrfs.Vrf.SsmAccessGroups.SsmAccessGroup, ['source_address', 'access_list_name'], name, value)


            class Traffic(Entity):
                """
                Configure IGMP Traffic variables
                
                .. attribute:: profile
                
                	Configure the route\-policy profile
                	**type**\:  str
                
                	**length:** 1..64
                
                

                """

                _prefix = 'ipv4-igmp-cfg'
                _revision = '2016-10-10'

                def __init__(self):
                    super(Mld.Vrfs.Vrf.Traffic, self).__init__()

                    self.yang_name = "traffic"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.profile = YLeaf(YType.str, "profile")
                    self._segment_path = lambda: "traffic"

                def __setattr__(self, name, value):
                    self._perform_setattr(Mld.Vrfs.Vrf.Traffic, ['profile'], name, value)

    def clone_ptr(self):
        self._top_entity = Mld()
        return self._top_entity

