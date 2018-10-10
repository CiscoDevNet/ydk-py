""" Cisco_IOS_XR_ipv4_igmp_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv4\-igmp package configuration.

This module contains definitions
for the following management objects\:
  igmp\: IGMPconfiguration
  amt\: amt
  mld\: mld

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class IgmpFilter(Enum):
    """
    IgmpFilter (Enum Class)

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



class Igmp(Entity):
    """
    IGMPconfiguration
    
    .. attribute:: vrfs
    
    	VRF related configuration
    	**type**\:  :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.Vrfs>`
    
    .. attribute:: default_context
    
    	Default Context
    	**type**\:  :py:class:`DefaultContext <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext>`
    
    	**presence node**\: True
    
    

    """

    _prefix = 'ipv4-igmp-cfg'
    _revision = '2017-10-15'

    def __init__(self):
        super(Igmp, self).__init__()
        self._top_entity = None

        self.yang_name = "igmp"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-igmp-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("vrfs", ("vrfs", Igmp.Vrfs)), ("default-context", ("default_context", Igmp.DefaultContext))])
        self._leafs = OrderedDict()

        self.vrfs = Igmp.Vrfs()
        self.vrfs.parent = self
        self._children_name_map["vrfs"] = "vrfs"

        self.default_context = None
        self._children_name_map["default_context"] = "default-context"
        self._segment_path = lambda: "Cisco-IOS-XR-ipv4-igmp-cfg:igmp"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Igmp, [], name, value)


    class Vrfs(Entity):
        """
        VRF related configuration
        
        .. attribute:: vrf
        
        	Configuration for a particular vrf
        	**type**\: list of  		 :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.Vrfs.Vrf>`
        
        

        """

        _prefix = 'ipv4-igmp-cfg'
        _revision = '2017-10-15'

        def __init__(self):
            super(Igmp.Vrfs, self).__init__()

            self.yang_name = "vrfs"
            self.yang_parent_name = "igmp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("vrf", ("vrf", Igmp.Vrfs.Vrf))])
            self._leafs = OrderedDict()

            self.vrf = YList(self)
            self._segment_path = lambda: "vrfs"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-igmp-cfg:igmp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Igmp.Vrfs, [], name, value)


        class Vrf(Entity):
            """
            Configuration for a particular vrf
            
            .. attribute:: vrf_name  (key)
            
            	Name for this vrf
            	**type**\: str
            
            	**length:** 1..32
            
            .. attribute:: traffic
            
            	Configure IGMP Traffic variables
            	**type**\:  :py:class:`Traffic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.Vrfs.Vrf.Traffic>`
            
            .. attribute:: inheritable_defaults
            
            	Inheritable Defaults
            	**type**\:  :py:class:`InheritableDefaults <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.Vrfs.Vrf.InheritableDefaults>`
            
            .. attribute:: ssm_access_groups
            
            	IGMP Source specific mode
            	**type**\:  :py:class:`SsmAccessGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.Vrfs.Vrf.SsmAccessGroups>`
            
            .. attribute:: maximum
            
            	Configure IGMP State Limits
            	**type**\:  :py:class:`Maximum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.Vrfs.Vrf.Maximum>`
            
            .. attribute:: ssmdns_query_group
            
            	Enable SSM mapping using DNS Query
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: interfaces
            
            	Interface\-level configuration
            	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.Vrfs.Vrf.Interfaces>`
            
            .. attribute:: robustness
            
            	Configure IGMP Robustness variable
            	**type**\: int
            
            	**range:** 2..10
            
            	**default value**\: 2
            
            

            """

            _prefix = 'ipv4-igmp-cfg'
            _revision = '2017-10-15'

            def __init__(self):
                super(Igmp.Vrfs.Vrf, self).__init__()

                self.yang_name = "vrf"
                self.yang_parent_name = "vrfs"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['vrf_name']
                self._child_classes = OrderedDict([("traffic", ("traffic", Igmp.Vrfs.Vrf.Traffic)), ("inheritable-defaults", ("inheritable_defaults", Igmp.Vrfs.Vrf.InheritableDefaults)), ("ssm-access-groups", ("ssm_access_groups", Igmp.Vrfs.Vrf.SsmAccessGroups)), ("maximum", ("maximum", Igmp.Vrfs.Vrf.Maximum)), ("interfaces", ("interfaces", Igmp.Vrfs.Vrf.Interfaces))])
                self._leafs = OrderedDict([
                    ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                    ('ssmdns_query_group', (YLeaf(YType.empty, 'ssmdns-query-group'), ['Empty'])),
                    ('robustness', (YLeaf(YType.uint32, 'robustness'), ['int'])),
                ])
                self.vrf_name = None
                self.ssmdns_query_group = None
                self.robustness = None

                self.traffic = Igmp.Vrfs.Vrf.Traffic()
                self.traffic.parent = self
                self._children_name_map["traffic"] = "traffic"

                self.inheritable_defaults = Igmp.Vrfs.Vrf.InheritableDefaults()
                self.inheritable_defaults.parent = self
                self._children_name_map["inheritable_defaults"] = "inheritable-defaults"

                self.ssm_access_groups = Igmp.Vrfs.Vrf.SsmAccessGroups()
                self.ssm_access_groups.parent = self
                self._children_name_map["ssm_access_groups"] = "ssm-access-groups"

                self.maximum = Igmp.Vrfs.Vrf.Maximum()
                self.maximum.parent = self
                self._children_name_map["maximum"] = "maximum"

                self.interfaces = Igmp.Vrfs.Vrf.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"
                self._segment_path = lambda: "vrf" + "[vrf-name='" + str(self.vrf_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-igmp-cfg:igmp/vrfs/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Igmp.Vrfs.Vrf, ['vrf_name', 'ssmdns_query_group', 'robustness'], name, value)


            class Traffic(Entity):
                """
                Configure IGMP Traffic variables
                
                .. attribute:: profile
                
                	Configure the route\-policy profile
                	**type**\: str
                
                	**length:** 1..64
                
                

                """

                _prefix = 'ipv4-igmp-cfg'
                _revision = '2017-10-15'

                def __init__(self):
                    super(Igmp.Vrfs.Vrf.Traffic, self).__init__()

                    self.yang_name = "traffic"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('profile', (YLeaf(YType.str, 'profile'), ['str'])),
                    ])
                    self.profile = None
                    self._segment_path = lambda: "traffic"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Igmp.Vrfs.Vrf.Traffic, ['profile'], name, value)


            class InheritableDefaults(Entity):
                """
                Inheritable Defaults
                
                .. attribute:: maximum_groups_per_interface_oor
                
                	Configure maximum number of groups accepted per interface by this router
                	**type**\:  :py:class:`MaximumGroupsPerInterfaceOor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.Vrfs.Vrf.InheritableDefaults.MaximumGroupsPerInterfaceOor>`
                
                	**presence node**\: True
                
                .. attribute:: query_timeout
                
                	IGMP previous querier timeout
                	**type**\: int
                
                	**range:** 60..300
                
                	**units**\: second
                
                .. attribute:: access_group
                
                	Access list specifying access group range
                	**type**\: str
                
                	**length:** 1..64
                
                .. attribute:: query_max_response_time
                
                	Query response value in seconds
                	**type**\: int
                
                	**range:** 1..12
                
                	**units**\: second
                
                	**default value**\: 10
                
                .. attribute:: version
                
                	Version number
                	**type**\: int
                
                	**range:** 1..3
                
                	**default value**\: 3
                
                .. attribute:: router_enable
                
                	Enabled or disabled, when value is TRUE or FALSE respectively
                	**type**\: bool
                
                	**default value**\: true
                
                .. attribute:: query_interval
                
                	Query interval in seconds
                	**type**\: int
                
                	**range:** 1..3600
                
                	**units**\: second
                
                	**default value**\: 60
                
                .. attribute:: explicit_tracking
                
                	IGMPv3 explicit host tracking
                	**type**\:  :py:class:`ExplicitTracking <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.Vrfs.Vrf.InheritableDefaults.ExplicitTracking>`
                
                	**presence node**\: True
                
                

                """

                _prefix = 'ipv4-igmp-cfg'
                _revision = '2017-10-15'

                def __init__(self):
                    super(Igmp.Vrfs.Vrf.InheritableDefaults, self).__init__()

                    self.yang_name = "inheritable-defaults"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("maximum-groups-per-interface-oor", ("maximum_groups_per_interface_oor", Igmp.Vrfs.Vrf.InheritableDefaults.MaximumGroupsPerInterfaceOor)), ("explicit-tracking", ("explicit_tracking", Igmp.Vrfs.Vrf.InheritableDefaults.ExplicitTracking))])
                    self._leafs = OrderedDict([
                        ('query_timeout', (YLeaf(YType.uint32, 'query-timeout'), ['int'])),
                        ('access_group', (YLeaf(YType.str, 'access-group'), ['str'])),
                        ('query_max_response_time', (YLeaf(YType.uint32, 'query-max-response-time'), ['int'])),
                        ('version', (YLeaf(YType.uint32, 'version'), ['int'])),
                        ('router_enable', (YLeaf(YType.boolean, 'router-enable'), ['bool'])),
                        ('query_interval', (YLeaf(YType.uint32, 'query-interval'), ['int'])),
                    ])
                    self.query_timeout = None
                    self.access_group = None
                    self.query_max_response_time = None
                    self.version = None
                    self.router_enable = None
                    self.query_interval = None

                    self.maximum_groups_per_interface_oor = None
                    self._children_name_map["maximum_groups_per_interface_oor"] = "maximum-groups-per-interface-oor"

                    self.explicit_tracking = None
                    self._children_name_map["explicit_tracking"] = "explicit-tracking"
                    self._segment_path = lambda: "inheritable-defaults"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Igmp.Vrfs.Vrf.InheritableDefaults, ['query_timeout', 'access_group', 'query_max_response_time', 'version', 'router_enable', 'query_interval'], name, value)


                class MaximumGroupsPerInterfaceOor(Entity):
                    """
                    Configure maximum number of groups accepted per
                    interface by this router
                    
                    .. attribute:: maximum_groups
                    
                    	Maximum number of groups accepted per interface by this router
                    	**type**\: int
                    
                    	**range:** 1..40000
                    
                    	**mandatory**\: True
                    
                    .. attribute:: warning_threshold
                    
                    	 WarningThreshold for number of groups accepted per interface by this router
                    	**type**\: int
                    
                    	**range:** 1..40000
                    
                    	**default value**\: 25000
                    
                    .. attribute:: access_list_name
                    
                    	Access\-list to account for
                    	**type**\: str
                    
                    	**length:** 1..64
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-igmp-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Igmp.Vrfs.Vrf.InheritableDefaults.MaximumGroupsPerInterfaceOor, self).__init__()

                        self.yang_name = "maximum-groups-per-interface-oor"
                        self.yang_parent_name = "inheritable-defaults"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('maximum_groups', (YLeaf(YType.uint32, 'maximum-groups'), ['int'])),
                            ('warning_threshold', (YLeaf(YType.uint32, 'warning-threshold'), ['int'])),
                            ('access_list_name', (YLeaf(YType.str, 'access-list-name'), ['str'])),
                        ])
                        self.maximum_groups = None
                        self.warning_threshold = None
                        self.access_list_name = None
                        self._segment_path = lambda: "maximum-groups-per-interface-oor"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Igmp.Vrfs.Vrf.InheritableDefaults.MaximumGroupsPerInterfaceOor, ['maximum_groups', 'warning_threshold', 'access_list_name'], name, value)


                class ExplicitTracking(Entity):
                    """
                    IGMPv3 explicit host tracking
                    
                    .. attribute:: enable
                    
                    	Enabled or disabled, when value is TRUE or FALSE respectively
                    	**type**\: bool
                    
                    	**mandatory**\: True
                    
                    .. attribute:: access_list_name
                    
                    	Access list specifying tracking group range
                    	**type**\: str
                    
                    	**length:** 1..64
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-igmp-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Igmp.Vrfs.Vrf.InheritableDefaults.ExplicitTracking, self).__init__()

                        self.yang_name = "explicit-tracking"
                        self.yang_parent_name = "inheritable-defaults"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('enable', (YLeaf(YType.boolean, 'enable'), ['bool'])),
                            ('access_list_name', (YLeaf(YType.str, 'access-list-name'), ['str'])),
                        ])
                        self.enable = None
                        self.access_list_name = None
                        self._segment_path = lambda: "explicit-tracking"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Igmp.Vrfs.Vrf.InheritableDefaults.ExplicitTracking, ['enable', 'access_list_name'], name, value)


            class SsmAccessGroups(Entity):
                """
                IGMP Source specific mode
                
                .. attribute:: ssm_access_group
                
                	SSM static Access Group
                	**type**\: list of  		 :py:class:`SsmAccessGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.Vrfs.Vrf.SsmAccessGroups.SsmAccessGroup>`
                
                

                """

                _prefix = 'ipv4-igmp-cfg'
                _revision = '2017-10-15'

                def __init__(self):
                    super(Igmp.Vrfs.Vrf.SsmAccessGroups, self).__init__()

                    self.yang_name = "ssm-access-groups"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("ssm-access-group", ("ssm_access_group", Igmp.Vrfs.Vrf.SsmAccessGroups.SsmAccessGroup))])
                    self._leafs = OrderedDict()

                    self.ssm_access_group = YList(self)
                    self._segment_path = lambda: "ssm-access-groups"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Igmp.Vrfs.Vrf.SsmAccessGroups, [], name, value)


                class SsmAccessGroup(Entity):
                    """
                    SSM static Access Group
                    
                    .. attribute:: source_address  (key)
                    
                    	IP source address
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    		**type**\: str
                    
                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: access_list_name
                    
                    	Access list specifying access group
                    	**type**\: str
                    
                    	**length:** 1..64
                    
                    	**mandatory**\: True
                    
                    

                    """

                    _prefix = 'ipv4-igmp-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Igmp.Vrfs.Vrf.SsmAccessGroups.SsmAccessGroup, self).__init__()

                        self.yang_name = "ssm-access-group"
                        self.yang_parent_name = "ssm-access-groups"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['source_address']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('source_address', (YLeaf(YType.str, 'source-address'), ['str','str'])),
                            ('access_list_name', (YLeaf(YType.str, 'access-list-name'), ['str'])),
                        ])
                        self.source_address = None
                        self.access_list_name = None
                        self._segment_path = lambda: "ssm-access-group" + "[source-address='" + str(self.source_address) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Igmp.Vrfs.Vrf.SsmAccessGroups.SsmAccessGroup, ['source_address', 'access_list_name'], name, value)


            class Maximum(Entity):
                """
                Configure IGMP State Limits
                
                .. attribute:: maximum_groups
                
                	Configure maximum number of groups accepted by this router
                	**type**\: int
                
                	**range:** 1..75000
                
                	**default value**\: 50000
                
                

                """

                _prefix = 'ipv4-igmp-cfg'
                _revision = '2017-10-15'

                def __init__(self):
                    super(Igmp.Vrfs.Vrf.Maximum, self).__init__()

                    self.yang_name = "maximum"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('maximum_groups', (YLeaf(YType.uint32, 'maximum-groups'), ['int'])),
                    ])
                    self.maximum_groups = None
                    self._segment_path = lambda: "maximum"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Igmp.Vrfs.Vrf.Maximum, ['maximum_groups'], name, value)


            class Interfaces(Entity):
                """
                Interface\-level configuration
                
                .. attribute:: interface
                
                	The name of the interface
                	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.Vrfs.Vrf.Interfaces.Interface>`
                
                

                """

                _prefix = 'ipv4-igmp-cfg'
                _revision = '2017-10-15'

                def __init__(self):
                    super(Igmp.Vrfs.Vrf.Interfaces, self).__init__()

                    self.yang_name = "interfaces"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("interface", ("interface", Igmp.Vrfs.Vrf.Interfaces.Interface))])
                    self._leafs = OrderedDict()

                    self.interface = YList(self)
                    self._segment_path = lambda: "interfaces"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Igmp.Vrfs.Vrf.Interfaces, [], name, value)


                class Interface(Entity):
                    """
                    The name of the interface
                    
                    .. attribute:: interface_name  (key)
                    
                    	Name of the interface
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: join_groups
                    
                    	IGMP join multicast group
                    	**type**\:  :py:class:`JoinGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.Vrfs.Vrf.Interfaces.Interface.JoinGroups>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: static_group_group_addresses
                    
                    	IGMP static multicast group
                    	**type**\:  :py:class:`StaticGroupGroupAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses>`
                    
                    .. attribute:: maximum_groups_per_interface_oor
                    
                    	Configure maximum number of groups accepted per interface by this router
                    	**type**\:  :py:class:`MaximumGroupsPerInterfaceOor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.Vrfs.Vrf.Interfaces.Interface.MaximumGroupsPerInterfaceOor>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: query_timeout
                    
                    	IGMP previous querier timeout
                    	**type**\: int
                    
                    	**range:** 60..300
                    
                    	**units**\: second
                    
                    .. attribute:: access_group
                    
                    	Access list specifying access group range
                    	**type**\: str
                    
                    	**length:** 1..64
                    
                    .. attribute:: query_max_response_time
                    
                    	Query response value in seconds
                    	**type**\: int
                    
                    	**range:** 1..12
                    
                    	**units**\: second
                    
                    	**default value**\: 10
                    
                    .. attribute:: version
                    
                    	Version number
                    	**type**\: int
                    
                    	**range:** 1..3
                    
                    	**default value**\: 3
                    
                    .. attribute:: router_enable
                    
                    	Enabled or disabled, when value is TRUE or FALSE respectively
                    	**type**\: bool
                    
                    	**default value**\: true
                    
                    .. attribute:: query_interval
                    
                    	Query interval in seconds
                    	**type**\: int
                    
                    	**range:** 1..3600
                    
                    	**units**\: second
                    
                    	**default value**\: 60
                    
                    .. attribute:: explicit_tracking
                    
                    	IGMPv3 explicit host tracking
                    	**type**\:  :py:class:`ExplicitTracking <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.Vrfs.Vrf.Interfaces.Interface.ExplicitTracking>`
                    
                    	**presence node**\: True
                    
                    

                    """

                    _prefix = 'ipv4-igmp-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Igmp.Vrfs.Vrf.Interfaces.Interface, self).__init__()

                        self.yang_name = "interface"
                        self.yang_parent_name = "interfaces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['interface_name']
                        self._child_classes = OrderedDict([("join-groups", ("join_groups", Igmp.Vrfs.Vrf.Interfaces.Interface.JoinGroups)), ("static-group-group-addresses", ("static_group_group_addresses", Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses)), ("maximum-groups-per-interface-oor", ("maximum_groups_per_interface_oor", Igmp.Vrfs.Vrf.Interfaces.Interface.MaximumGroupsPerInterfaceOor)), ("explicit-tracking", ("explicit_tracking", Igmp.Vrfs.Vrf.Interfaces.Interface.ExplicitTracking))])
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                            ('query_timeout', (YLeaf(YType.uint32, 'query-timeout'), ['int'])),
                            ('access_group', (YLeaf(YType.str, 'access-group'), ['str'])),
                            ('query_max_response_time', (YLeaf(YType.uint32, 'query-max-response-time'), ['int'])),
                            ('version', (YLeaf(YType.uint32, 'version'), ['int'])),
                            ('router_enable', (YLeaf(YType.boolean, 'router-enable'), ['bool'])),
                            ('query_interval', (YLeaf(YType.uint32, 'query-interval'), ['int'])),
                        ])
                        self.interface_name = None
                        self.query_timeout = None
                        self.access_group = None
                        self.query_max_response_time = None
                        self.version = None
                        self.router_enable = None
                        self.query_interval = None

                        self.join_groups = None
                        self._children_name_map["join_groups"] = "join-groups"

                        self.static_group_group_addresses = Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses()
                        self.static_group_group_addresses.parent = self
                        self._children_name_map["static_group_group_addresses"] = "static-group-group-addresses"

                        self.maximum_groups_per_interface_oor = None
                        self._children_name_map["maximum_groups_per_interface_oor"] = "maximum-groups-per-interface-oor"

                        self.explicit_tracking = None
                        self._children_name_map["explicit_tracking"] = "explicit-tracking"
                        self._segment_path = lambda: "interface" + "[interface-name='" + str(self.interface_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Igmp.Vrfs.Vrf.Interfaces.Interface, ['interface_name', 'query_timeout', 'access_group', 'query_max_response_time', 'version', 'router_enable', 'query_interval'], name, value)


                    class JoinGroups(Entity):
                        """
                        IGMP join multicast group
                        
                        .. attribute:: join_group
                        
                        	IP group address and optional source address to include
                        	**type**\: list of  		 :py:class:`JoinGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.Vrfs.Vrf.Interfaces.Interface.JoinGroups.JoinGroup>`
                        
                        .. attribute:: join_group_source_address
                        
                        	IP group address and optional source address to include
                        	**type**\: list of  		 :py:class:`JoinGroupSourceAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.Vrfs.Vrf.Interfaces.Interface.JoinGroups.JoinGroupSourceAddress>`
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2017-10-15'

                        def __init__(self):
                            super(Igmp.Vrfs.Vrf.Interfaces.Interface.JoinGroups, self).__init__()

                            self.yang_name = "join-groups"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("join-group", ("join_group", Igmp.Vrfs.Vrf.Interfaces.Interface.JoinGroups.JoinGroup)), ("join-group-source-address", ("join_group_source_address", Igmp.Vrfs.Vrf.Interfaces.Interface.JoinGroups.JoinGroupSourceAddress))])
                            self.is_presence_container = True
                            self._leafs = OrderedDict()

                            self.join_group = YList(self)
                            self.join_group_source_address = YList(self)
                            self._segment_path = lambda: "join-groups"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Igmp.Vrfs.Vrf.Interfaces.Interface.JoinGroups, [], name, value)


                        class JoinGroup(Entity):
                            """
                            IP group address and optional source address
                            to include
                            
                            .. attribute:: group_address  (key)
                            
                            	IP group address
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            		**type**\: str
                            
                            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: mode
                            
                            	Filter mode
                            	**type**\:  :py:class:`IgmpFilter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.IgmpFilter>`
                            
                            	**mandatory**\: True
                            
                            

                            """

                            _prefix = 'ipv4-igmp-cfg'
                            _revision = '2017-10-15'

                            def __init__(self):
                                super(Igmp.Vrfs.Vrf.Interfaces.Interface.JoinGroups.JoinGroup, self).__init__()

                                self.yang_name = "join-group"
                                self.yang_parent_name = "join-groups"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['group_address']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('group_address', (YLeaf(YType.str, 'group-address'), ['str','str'])),
                                    ('mode', (YLeaf(YType.enumeration, 'mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'IgmpFilter', '')])),
                                ])
                                self.group_address = None
                                self.mode = None
                                self._segment_path = lambda: "join-group" + "[group-address='" + str(self.group_address) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Igmp.Vrfs.Vrf.Interfaces.Interface.JoinGroups.JoinGroup, ['group_address', 'mode'], name, value)


                        class JoinGroupSourceAddress(Entity):
                            """
                            IP group address and optional source address
                            to include
                            
                            .. attribute:: group_address  (key)
                            
                            	IP group address
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            		**type**\: str
                            
                            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: source_address  (key)
                            
                            	Optional IP source address
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            		**type**\: str
                            
                            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: mode
                            
                            	Filter mode
                            	**type**\:  :py:class:`IgmpFilter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.IgmpFilter>`
                            
                            	**mandatory**\: True
                            
                            

                            """

                            _prefix = 'ipv4-igmp-cfg'
                            _revision = '2017-10-15'

                            def __init__(self):
                                super(Igmp.Vrfs.Vrf.Interfaces.Interface.JoinGroups.JoinGroupSourceAddress, self).__init__()

                                self.yang_name = "join-group-source-address"
                                self.yang_parent_name = "join-groups"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['group_address','source_address']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('group_address', (YLeaf(YType.str, 'group-address'), ['str','str'])),
                                    ('source_address', (YLeaf(YType.str, 'source-address'), ['str','str'])),
                                    ('mode', (YLeaf(YType.enumeration, 'mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'IgmpFilter', '')])),
                                ])
                                self.group_address = None
                                self.source_address = None
                                self.mode = None
                                self._segment_path = lambda: "join-group-source-address" + "[group-address='" + str(self.group_address) + "']" + "[source-address='" + str(self.source_address) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Igmp.Vrfs.Vrf.Interfaces.Interface.JoinGroups.JoinGroupSourceAddress, ['group_address', 'source_address', 'mode'], name, value)


                    class StaticGroupGroupAddresses(Entity):
                        """
                        IGMP static multicast group
                        
                        .. attribute:: static_group_group_address
                        
                        	IP group address and optional source address to include
                        	**type**\: list of  		 :py:class:`StaticGroupGroupAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddress>`
                        
                        .. attribute:: static_group_group_address_source_address
                        
                        	IP group address and optional source address to include
                        	**type**\: list of  		 :py:class:`StaticGroupGroupAddressSourceAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddress>`
                        
                        .. attribute:: static_group_group_address_source_address_source_address_mask
                        
                        	IP group address and optional source address to include
                        	**type**\: list of  		 :py:class:`StaticGroupGroupAddressSourceAddressSourceAddressMask <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddressSourceAddressMask>`
                        
                        .. attribute:: static_group_group_address_group_address_mask
                        
                        	IP group address and optional source address to include
                        	**type**\: list of  		 :py:class:`StaticGroupGroupAddressGroupAddressMask <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMask>`
                        
                        .. attribute:: static_group_group_address_group_address_mask_source_address
                        
                        	IP group address and optional source address to include
                        	**type**\: list of  		 :py:class:`StaticGroupGroupAddressGroupAddressMaskSourceAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddress>`
                        
                        .. attribute:: static_group_group_address_group_address_mask_source_address_source_address_mask
                        
                        	IP group address and optional source address to include
                        	**type**\: list of  		 :py:class:`StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask>`
                        
                        

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2017-10-15'

                        def __init__(self):
                            super(Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses, self).__init__()

                            self.yang_name = "static-group-group-addresses"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("static-group-group-address", ("static_group_group_address", Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddress)), ("static-group-group-address-source-address", ("static_group_group_address_source_address", Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddress)), ("static-group-group-address-source-address-source-address-mask", ("static_group_group_address_source_address_source_address_mask", Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddressSourceAddressMask)), ("static-group-group-address-group-address-mask", ("static_group_group_address_group_address_mask", Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMask)), ("static-group-group-address-group-address-mask-source-address", ("static_group_group_address_group_address_mask_source_address", Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddress)), ("static-group-group-address-group-address-mask-source-address-source-address-mask", ("static_group_group_address_group_address_mask_source_address_source_address_mask", Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask))])
                            self._leafs = OrderedDict()

                            self.static_group_group_address = YList(self)
                            self.static_group_group_address_source_address = YList(self)
                            self.static_group_group_address_source_address_source_address_mask = YList(self)
                            self.static_group_group_address_group_address_mask = YList(self)
                            self.static_group_group_address_group_address_mask_source_address = YList(self)
                            self.static_group_group_address_group_address_mask_source_address_source_address_mask = YList(self)
                            self._segment_path = lambda: "static-group-group-addresses"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses, [], name, value)


                        class StaticGroupGroupAddress(Entity):
                            """
                            IP group address and optional source address
                            to include
                            
                            .. attribute:: group_address  (key)
                            
                            	IP group address
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            		**type**\: str
                            
                            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: group_count
                            
                            	Number of groups to join (do not set without GroupAddressMask)
                            	**type**\: int
                            
                            	**range:** 1..512
                            
                            	**default value**\: 1
                            
                            .. attribute:: source_count
                            
                            	Number of sources to join (do not set without SourceAddressMask)
                            	**type**\: int
                            
                            	**range:** 1..512
                            
                            	**default value**\: 1
                            
                            .. attribute:: suppress_report
                            
                            	Suppress reports
                            	**type**\: bool
                            
                            	**default value**\: false
                            
                            

                            """

                            _prefix = 'ipv4-igmp-cfg'
                            _revision = '2017-10-15'

                            def __init__(self):
                                super(Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddress, self).__init__()

                                self.yang_name = "static-group-group-address"
                                self.yang_parent_name = "static-group-group-addresses"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['group_address']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('group_address', (YLeaf(YType.str, 'group-address'), ['str','str'])),
                                    ('group_count', (YLeaf(YType.uint32, 'group-count'), ['int'])),
                                    ('source_count', (YLeaf(YType.uint32, 'source-count'), ['int'])),
                                    ('suppress_report', (YLeaf(YType.boolean, 'suppress-report'), ['bool'])),
                                ])
                                self.group_address = None
                                self.group_count = None
                                self.source_count = None
                                self.suppress_report = None
                                self._segment_path = lambda: "static-group-group-address" + "[group-address='" + str(self.group_address) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddress, ['group_address', 'group_count', 'source_count', 'suppress_report'], name, value)


                        class StaticGroupGroupAddressSourceAddress(Entity):
                            """
                            IP group address and optional source address
                            to include
                            
                            .. attribute:: group_address  (key)
                            
                            	IP group address
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            		**type**\: str
                            
                            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: source_address  (key)
                            
                            	IP source address
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            		**type**\: str
                            
                            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: group_count
                            
                            	Number of groups to join (do not set without GroupAddressMask)
                            	**type**\: int
                            
                            	**range:** 1..512
                            
                            	**default value**\: 1
                            
                            .. attribute:: source_count
                            
                            	Number of sources to join (do not set without SourceAddressMask)
                            	**type**\: int
                            
                            	**range:** 1..512
                            
                            	**default value**\: 1
                            
                            .. attribute:: suppress_report
                            
                            	Suppress reports
                            	**type**\: bool
                            
                            	**default value**\: false
                            
                            

                            """

                            _prefix = 'ipv4-igmp-cfg'
                            _revision = '2017-10-15'

                            def __init__(self):
                                super(Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddress, self).__init__()

                                self.yang_name = "static-group-group-address-source-address"
                                self.yang_parent_name = "static-group-group-addresses"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['group_address','source_address']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('group_address', (YLeaf(YType.str, 'group-address'), ['str','str'])),
                                    ('source_address', (YLeaf(YType.str, 'source-address'), ['str','str'])),
                                    ('group_count', (YLeaf(YType.uint32, 'group-count'), ['int'])),
                                    ('source_count', (YLeaf(YType.uint32, 'source-count'), ['int'])),
                                    ('suppress_report', (YLeaf(YType.boolean, 'suppress-report'), ['bool'])),
                                ])
                                self.group_address = None
                                self.source_address = None
                                self.group_count = None
                                self.source_count = None
                                self.suppress_report = None
                                self._segment_path = lambda: "static-group-group-address-source-address" + "[group-address='" + str(self.group_address) + "']" + "[source-address='" + str(self.source_address) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddress, ['group_address', 'source_address', 'group_count', 'source_count', 'suppress_report'], name, value)


                        class StaticGroupGroupAddressSourceAddressSourceAddressMask(Entity):
                            """
                            IP group address and optional source address
                            to include
                            
                            .. attribute:: group_address  (key)
                            
                            	IP group address
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            		**type**\: str
                            
                            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: source_address  (key)
                            
                            	IP source address
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            		**type**\: str
                            
                            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: source_address_mask  (key)
                            
                            	Mask for Source Address
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            		**type**\: str
                            
                            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: group_count
                            
                            	Number of groups to join (do not set without GroupAddressMask)
                            	**type**\: int
                            
                            	**range:** 1..512
                            
                            	**default value**\: 1
                            
                            .. attribute:: source_count
                            
                            	Number of sources to join (do not set without SourceAddressMask)
                            	**type**\: int
                            
                            	**range:** 1..512
                            
                            	**default value**\: 1
                            
                            .. attribute:: suppress_report
                            
                            	Suppress reports
                            	**type**\: bool
                            
                            	**default value**\: false
                            
                            

                            """

                            _prefix = 'ipv4-igmp-cfg'
                            _revision = '2017-10-15'

                            def __init__(self):
                                super(Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddressSourceAddressMask, self).__init__()

                                self.yang_name = "static-group-group-address-source-address-source-address-mask"
                                self.yang_parent_name = "static-group-group-addresses"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['group_address','source_address','source_address_mask']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('group_address', (YLeaf(YType.str, 'group-address'), ['str','str'])),
                                    ('source_address', (YLeaf(YType.str, 'source-address'), ['str','str'])),
                                    ('source_address_mask', (YLeaf(YType.str, 'source-address-mask'), ['str','str'])),
                                    ('group_count', (YLeaf(YType.uint32, 'group-count'), ['int'])),
                                    ('source_count', (YLeaf(YType.uint32, 'source-count'), ['int'])),
                                    ('suppress_report', (YLeaf(YType.boolean, 'suppress-report'), ['bool'])),
                                ])
                                self.group_address = None
                                self.source_address = None
                                self.source_address_mask = None
                                self.group_count = None
                                self.source_count = None
                                self.suppress_report = None
                                self._segment_path = lambda: "static-group-group-address-source-address-source-address-mask" + "[group-address='" + str(self.group_address) + "']" + "[source-address='" + str(self.source_address) + "']" + "[source-address-mask='" + str(self.source_address_mask) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddressSourceAddressMask, ['group_address', 'source_address', 'source_address_mask', 'group_count', 'source_count', 'suppress_report'], name, value)


                        class StaticGroupGroupAddressGroupAddressMask(Entity):
                            """
                            IP group address and optional source address
                            to include
                            
                            .. attribute:: group_address  (key)
                            
                            	IP group address
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            		**type**\: str
                            
                            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: group_address_mask  (key)
                            
                            	Mask for Group Address
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            		**type**\: str
                            
                            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: group_count
                            
                            	Number of groups to join (do not set without GroupAddressMask)
                            	**type**\: int
                            
                            	**range:** 1..512
                            
                            	**default value**\: 1
                            
                            .. attribute:: source_count
                            
                            	Number of sources to join (do not set without SourceAddressMask)
                            	**type**\: int
                            
                            	**range:** 1..512
                            
                            	**default value**\: 1
                            
                            .. attribute:: suppress_report
                            
                            	Suppress reports
                            	**type**\: bool
                            
                            	**default value**\: false
                            
                            

                            """

                            _prefix = 'ipv4-igmp-cfg'
                            _revision = '2017-10-15'

                            def __init__(self):
                                super(Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMask, self).__init__()

                                self.yang_name = "static-group-group-address-group-address-mask"
                                self.yang_parent_name = "static-group-group-addresses"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['group_address','group_address_mask']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('group_address', (YLeaf(YType.str, 'group-address'), ['str','str'])),
                                    ('group_address_mask', (YLeaf(YType.str, 'group-address-mask'), ['str','str'])),
                                    ('group_count', (YLeaf(YType.uint32, 'group-count'), ['int'])),
                                    ('source_count', (YLeaf(YType.uint32, 'source-count'), ['int'])),
                                    ('suppress_report', (YLeaf(YType.boolean, 'suppress-report'), ['bool'])),
                                ])
                                self.group_address = None
                                self.group_address_mask = None
                                self.group_count = None
                                self.source_count = None
                                self.suppress_report = None
                                self._segment_path = lambda: "static-group-group-address-group-address-mask" + "[group-address='" + str(self.group_address) + "']" + "[group-address-mask='" + str(self.group_address_mask) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMask, ['group_address', 'group_address_mask', 'group_count', 'source_count', 'suppress_report'], name, value)


                        class StaticGroupGroupAddressGroupAddressMaskSourceAddress(Entity):
                            """
                            IP group address and optional source address
                            to include
                            
                            .. attribute:: group_address  (key)
                            
                            	IP group address
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            		**type**\: str
                            
                            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: group_address_mask  (key)
                            
                            	Mask for Group Address
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            		**type**\: str
                            
                            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: source_address  (key)
                            
                            	IP source address
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            		**type**\: str
                            
                            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: group_count
                            
                            	Number of groups to join (do not set without GroupAddressMask)
                            	**type**\: int
                            
                            	**range:** 1..512
                            
                            	**default value**\: 1
                            
                            .. attribute:: source_count
                            
                            	Number of sources to join (do not set without SourceAddressMask)
                            	**type**\: int
                            
                            	**range:** 1..512
                            
                            	**default value**\: 1
                            
                            .. attribute:: suppress_report
                            
                            	Suppress reports
                            	**type**\: bool
                            
                            	**default value**\: false
                            
                            

                            """

                            _prefix = 'ipv4-igmp-cfg'
                            _revision = '2017-10-15'

                            def __init__(self):
                                super(Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddress, self).__init__()

                                self.yang_name = "static-group-group-address-group-address-mask-source-address"
                                self.yang_parent_name = "static-group-group-addresses"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['group_address','group_address_mask','source_address']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('group_address', (YLeaf(YType.str, 'group-address'), ['str','str'])),
                                    ('group_address_mask', (YLeaf(YType.str, 'group-address-mask'), ['str','str'])),
                                    ('source_address', (YLeaf(YType.str, 'source-address'), ['str','str'])),
                                    ('group_count', (YLeaf(YType.uint32, 'group-count'), ['int'])),
                                    ('source_count', (YLeaf(YType.uint32, 'source-count'), ['int'])),
                                    ('suppress_report', (YLeaf(YType.boolean, 'suppress-report'), ['bool'])),
                                ])
                                self.group_address = None
                                self.group_address_mask = None
                                self.source_address = None
                                self.group_count = None
                                self.source_count = None
                                self.suppress_report = None
                                self._segment_path = lambda: "static-group-group-address-group-address-mask-source-address" + "[group-address='" + str(self.group_address) + "']" + "[group-address-mask='" + str(self.group_address_mask) + "']" + "[source-address='" + str(self.source_address) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddress, ['group_address', 'group_address_mask', 'source_address', 'group_count', 'source_count', 'suppress_report'], name, value)


                        class StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask(Entity):
                            """
                            IP group address and optional source address
                            to include
                            
                            .. attribute:: group_address  (key)
                            
                            	IP group address
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            		**type**\: str
                            
                            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: group_address_mask  (key)
                            
                            	Mask for Group Address
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            		**type**\: str
                            
                            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: source_address  (key)
                            
                            	IP source address
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            		**type**\: str
                            
                            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: source_address_mask  (key)
                            
                            	Mask for Source Address
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            		**type**\: str
                            
                            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: group_count
                            
                            	Number of groups to join (do not set without GroupAddressMask)
                            	**type**\: int
                            
                            	**range:** 1..512
                            
                            	**default value**\: 1
                            
                            .. attribute:: source_count
                            
                            	Number of sources to join (do not set without SourceAddressMask)
                            	**type**\: int
                            
                            	**range:** 1..512
                            
                            	**default value**\: 1
                            
                            .. attribute:: suppress_report
                            
                            	Suppress reports
                            	**type**\: bool
                            
                            	**default value**\: false
                            
                            

                            """

                            _prefix = 'ipv4-igmp-cfg'
                            _revision = '2017-10-15'

                            def __init__(self):
                                super(Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask, self).__init__()

                                self.yang_name = "static-group-group-address-group-address-mask-source-address-source-address-mask"
                                self.yang_parent_name = "static-group-group-addresses"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['group_address','group_address_mask','source_address','source_address_mask']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('group_address', (YLeaf(YType.str, 'group-address'), ['str','str'])),
                                    ('group_address_mask', (YLeaf(YType.str, 'group-address-mask'), ['str','str'])),
                                    ('source_address', (YLeaf(YType.str, 'source-address'), ['str','str'])),
                                    ('source_address_mask', (YLeaf(YType.str, 'source-address-mask'), ['str','str'])),
                                    ('group_count', (YLeaf(YType.uint32, 'group-count'), ['int'])),
                                    ('source_count', (YLeaf(YType.uint32, 'source-count'), ['int'])),
                                    ('suppress_report', (YLeaf(YType.boolean, 'suppress-report'), ['bool'])),
                                ])
                                self.group_address = None
                                self.group_address_mask = None
                                self.source_address = None
                                self.source_address_mask = None
                                self.group_count = None
                                self.source_count = None
                                self.suppress_report = None
                                self._segment_path = lambda: "static-group-group-address-group-address-mask-source-address-source-address-mask" + "[group-address='" + str(self.group_address) + "']" + "[group-address-mask='" + str(self.group_address_mask) + "']" + "[source-address='" + str(self.source_address) + "']" + "[source-address-mask='" + str(self.source_address_mask) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask, ['group_address', 'group_address_mask', 'source_address', 'source_address_mask', 'group_count', 'source_count', 'suppress_report'], name, value)


                    class MaximumGroupsPerInterfaceOor(Entity):
                        """
                        Configure maximum number of groups accepted per
                        interface by this router
                        
                        .. attribute:: maximum_groups
                        
                        	Maximum number of groups accepted per interface by this router
                        	**type**\: int
                        
                        	**range:** 1..40000
                        
                        	**mandatory**\: True
                        
                        .. attribute:: warning_threshold
                        
                        	 WarningThreshold for number of groups accepted per interface by this router
                        	**type**\: int
                        
                        	**range:** 1..40000
                        
                        	**default value**\: 25000
                        
                        .. attribute:: access_list_name
                        
                        	Access\-list to account for
                        	**type**\: str
                        
                        	**length:** 1..64
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2017-10-15'

                        def __init__(self):
                            super(Igmp.Vrfs.Vrf.Interfaces.Interface.MaximumGroupsPerInterfaceOor, self).__init__()

                            self.yang_name = "maximum-groups-per-interface-oor"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('maximum_groups', (YLeaf(YType.uint32, 'maximum-groups'), ['int'])),
                                ('warning_threshold', (YLeaf(YType.uint32, 'warning-threshold'), ['int'])),
                                ('access_list_name', (YLeaf(YType.str, 'access-list-name'), ['str'])),
                            ])
                            self.maximum_groups = None
                            self.warning_threshold = None
                            self.access_list_name = None
                            self._segment_path = lambda: "maximum-groups-per-interface-oor"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Igmp.Vrfs.Vrf.Interfaces.Interface.MaximumGroupsPerInterfaceOor, ['maximum_groups', 'warning_threshold', 'access_list_name'], name, value)


                    class ExplicitTracking(Entity):
                        """
                        IGMPv3 explicit host tracking
                        
                        .. attribute:: enable
                        
                        	Enabled or disabled, when value is TRUE or FALSE respectively
                        	**type**\: bool
                        
                        	**mandatory**\: True
                        
                        .. attribute:: access_list_name
                        
                        	Access list specifying tracking group range
                        	**type**\: str
                        
                        	**length:** 1..64
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2017-10-15'

                        def __init__(self):
                            super(Igmp.Vrfs.Vrf.Interfaces.Interface.ExplicitTracking, self).__init__()

                            self.yang_name = "explicit-tracking"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('enable', (YLeaf(YType.boolean, 'enable'), ['bool'])),
                                ('access_list_name', (YLeaf(YType.str, 'access-list-name'), ['str'])),
                            ])
                            self.enable = None
                            self.access_list_name = None
                            self._segment_path = lambda: "explicit-tracking"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Igmp.Vrfs.Vrf.Interfaces.Interface.ExplicitTracking, ['enable', 'access_list_name'], name, value)


    class DefaultContext(Entity):
        """
        Default Context
        
        .. attribute:: nsf
        
        	Configure NSF specific options
        	**type**\:  :py:class:`Nsf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext.Nsf>`
        
        .. attribute:: unicast_qos_adjust
        
        	Configure IGMP QoS shapers for subscriber interfaces
        	**type**\:  :py:class:`UnicastQosAdjust <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext.UnicastQosAdjust>`
        
        .. attribute:: accounting
        
        	Configure IGMP accounting for logging join/leave records
        	**type**\:  :py:class:`Accounting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext.Accounting>`
        
        .. attribute:: traffic
        
        	Configure IGMP Traffic variables
        	**type**\:  :py:class:`Traffic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext.Traffic>`
        
        .. attribute:: inheritable_defaults
        
        	Inheritable Defaults
        	**type**\:  :py:class:`InheritableDefaults <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext.InheritableDefaults>`
        
        .. attribute:: ssm_access_groups
        
        	IGMP Source specific mode
        	**type**\:  :py:class:`SsmAccessGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext.SsmAccessGroups>`
        
        .. attribute:: maximum
        
        	Configure IGMP State Limits
        	**type**\:  :py:class:`Maximum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext.Maximum>`
        
        .. attribute:: ssmdns_query_group
        
        	Enable SSM mapping using DNS Query
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: interfaces
        
        	Interface\-level configuration
        	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext.Interfaces>`
        
        .. attribute:: robustness
        
        	Configure IGMP Robustness variable
        	**type**\: int
        
        	**range:** 2..10
        
        	**default value**\: 2
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'ipv4-igmp-cfg'
        _revision = '2017-10-15'

        def __init__(self):
            super(Igmp.DefaultContext, self).__init__()

            self.yang_name = "default-context"
            self.yang_parent_name = "igmp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("nsf", ("nsf", Igmp.DefaultContext.Nsf)), ("unicast-qos-adjust", ("unicast_qos_adjust", Igmp.DefaultContext.UnicastQosAdjust)), ("accounting", ("accounting", Igmp.DefaultContext.Accounting)), ("traffic", ("traffic", Igmp.DefaultContext.Traffic)), ("inheritable-defaults", ("inheritable_defaults", Igmp.DefaultContext.InheritableDefaults)), ("ssm-access-groups", ("ssm_access_groups", Igmp.DefaultContext.SsmAccessGroups)), ("maximum", ("maximum", Igmp.DefaultContext.Maximum)), ("interfaces", ("interfaces", Igmp.DefaultContext.Interfaces))])
            self.is_presence_container = True
            self._leafs = OrderedDict([
                ('ssmdns_query_group', (YLeaf(YType.empty, 'ssmdns-query-group'), ['Empty'])),
                ('robustness', (YLeaf(YType.uint32, 'robustness'), ['int'])),
            ])
            self.ssmdns_query_group = None
            self.robustness = None

            self.nsf = Igmp.DefaultContext.Nsf()
            self.nsf.parent = self
            self._children_name_map["nsf"] = "nsf"

            self.unicast_qos_adjust = Igmp.DefaultContext.UnicastQosAdjust()
            self.unicast_qos_adjust.parent = self
            self._children_name_map["unicast_qos_adjust"] = "unicast-qos-adjust"

            self.accounting = Igmp.DefaultContext.Accounting()
            self.accounting.parent = self
            self._children_name_map["accounting"] = "accounting"

            self.traffic = Igmp.DefaultContext.Traffic()
            self.traffic.parent = self
            self._children_name_map["traffic"] = "traffic"

            self.inheritable_defaults = Igmp.DefaultContext.InheritableDefaults()
            self.inheritable_defaults.parent = self
            self._children_name_map["inheritable_defaults"] = "inheritable-defaults"

            self.ssm_access_groups = Igmp.DefaultContext.SsmAccessGroups()
            self.ssm_access_groups.parent = self
            self._children_name_map["ssm_access_groups"] = "ssm-access-groups"

            self.maximum = Igmp.DefaultContext.Maximum()
            self.maximum.parent = self
            self._children_name_map["maximum"] = "maximum"

            self.interfaces = Igmp.DefaultContext.Interfaces()
            self.interfaces.parent = self
            self._children_name_map["interfaces"] = "interfaces"
            self._segment_path = lambda: "default-context"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-igmp-cfg:igmp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Igmp.DefaultContext, ['ssmdns_query_group', 'robustness'], name, value)


        class Nsf(Entity):
            """
            Configure NSF specific options
            
            .. attribute:: lifetime
            
            	Maximum time for IGMP NSF mode in seconds
            	**type**\: int
            
            	**range:** 10..3600
            
            	**units**\: second
            
            	**default value**\: 60
            
            

            """

            _prefix = 'ipv4-igmp-cfg'
            _revision = '2017-10-15'

            def __init__(self):
                super(Igmp.DefaultContext.Nsf, self).__init__()

                self.yang_name = "nsf"
                self.yang_parent_name = "default-context"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('lifetime', (YLeaf(YType.uint32, 'lifetime'), ['int'])),
                ])
                self.lifetime = None
                self._segment_path = lambda: "nsf"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-igmp-cfg:igmp/default-context/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Igmp.DefaultContext.Nsf, ['lifetime'], name, value)


        class UnicastQosAdjust(Entity):
            """
            Configure IGMP QoS shapers for subscriber
            interfaces
            
            .. attribute:: download_interval
            
            	Configure the QoS download interval (in milliseconds)
            	**type**\: int
            
            	**range:** 10..500
            
            	**units**\: millisecond
            
            	**default value**\: 100
            
            .. attribute:: adjustment_delay
            
            	Configure the QoS delay before programming (in seconds)
            	**type**\: int
            
            	**range:** 0..10
            
            	**units**\: second
            
            	**default value**\: 1
            
            .. attribute:: hold_off
            
            	Configure the QoS hold off time (in seconds)
            	**type**\: int
            
            	**range:** 5..1800
            
            	**units**\: second
            
            	**default value**\: 180
            
            

            """

            _prefix = 'ipv4-igmp-cfg'
            _revision = '2017-10-15'

            def __init__(self):
                super(Igmp.DefaultContext.UnicastQosAdjust, self).__init__()

                self.yang_name = "unicast-qos-adjust"
                self.yang_parent_name = "default-context"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('download_interval', (YLeaf(YType.uint32, 'download-interval'), ['int'])),
                    ('adjustment_delay', (YLeaf(YType.uint32, 'adjustment-delay'), ['int'])),
                    ('hold_off', (YLeaf(YType.uint32, 'hold-off'), ['int'])),
                ])
                self.download_interval = None
                self.adjustment_delay = None
                self.hold_off = None
                self._segment_path = lambda: "unicast-qos-adjust"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-igmp-cfg:igmp/default-context/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Igmp.DefaultContext.UnicastQosAdjust, ['download_interval', 'adjustment_delay', 'hold_off'], name, value)


        class Accounting(Entity):
            """
            Configure IGMP accounting for logging
            join/leave records
            
            .. attribute:: max_history
            
            	Configure IGMP accounting Maximum History setting
            	**type**\: int
            
            	**range:** 1..365
            
            	**units**\: day
            
            	**default value**\: 1
            
            

            """

            _prefix = 'ipv4-igmp-cfg'
            _revision = '2017-10-15'

            def __init__(self):
                super(Igmp.DefaultContext.Accounting, self).__init__()

                self.yang_name = "accounting"
                self.yang_parent_name = "default-context"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('max_history', (YLeaf(YType.uint32, 'max-history'), ['int'])),
                ])
                self.max_history = None
                self._segment_path = lambda: "accounting"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-igmp-cfg:igmp/default-context/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Igmp.DefaultContext.Accounting, ['max_history'], name, value)


        class Traffic(Entity):
            """
            Configure IGMP Traffic variables
            
            .. attribute:: profile
            
            	Configure the route\-policy profile
            	**type**\: str
            
            	**length:** 1..64
            
            

            """

            _prefix = 'ipv4-igmp-cfg'
            _revision = '2017-10-15'

            def __init__(self):
                super(Igmp.DefaultContext.Traffic, self).__init__()

                self.yang_name = "traffic"
                self.yang_parent_name = "default-context"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('profile', (YLeaf(YType.str, 'profile'), ['str'])),
                ])
                self.profile = None
                self._segment_path = lambda: "traffic"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-igmp-cfg:igmp/default-context/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Igmp.DefaultContext.Traffic, ['profile'], name, value)


        class InheritableDefaults(Entity):
            """
            Inheritable Defaults
            
            .. attribute:: maximum_groups_per_interface_oor
            
            	Configure maximum number of groups accepted per interface by this router
            	**type**\:  :py:class:`MaximumGroupsPerInterfaceOor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext.InheritableDefaults.MaximumGroupsPerInterfaceOor>`
            
            	**presence node**\: True
            
            .. attribute:: query_timeout
            
            	IGMP previous querier timeout
            	**type**\: int
            
            	**range:** 60..300
            
            	**units**\: second
            
            .. attribute:: access_group
            
            	Access list specifying access group range
            	**type**\: str
            
            	**length:** 1..64
            
            .. attribute:: query_max_response_time
            
            	Query response value in seconds
            	**type**\: int
            
            	**range:** 1..12
            
            	**units**\: second
            
            	**default value**\: 10
            
            .. attribute:: version
            
            	Version number
            	**type**\: int
            
            	**range:** 1..3
            
            	**default value**\: 3
            
            .. attribute:: router_enable
            
            	Enabled or disabled, when value is TRUE or FALSE respectively
            	**type**\: bool
            
            	**default value**\: true
            
            .. attribute:: query_interval
            
            	Query interval in seconds
            	**type**\: int
            
            	**range:** 1..3600
            
            	**units**\: second
            
            	**default value**\: 60
            
            .. attribute:: explicit_tracking
            
            	IGMPv3 explicit host tracking
            	**type**\:  :py:class:`ExplicitTracking <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext.InheritableDefaults.ExplicitTracking>`
            
            	**presence node**\: True
            
            

            """

            _prefix = 'ipv4-igmp-cfg'
            _revision = '2017-10-15'

            def __init__(self):
                super(Igmp.DefaultContext.InheritableDefaults, self).__init__()

                self.yang_name = "inheritable-defaults"
                self.yang_parent_name = "default-context"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("maximum-groups-per-interface-oor", ("maximum_groups_per_interface_oor", Igmp.DefaultContext.InheritableDefaults.MaximumGroupsPerInterfaceOor)), ("explicit-tracking", ("explicit_tracking", Igmp.DefaultContext.InheritableDefaults.ExplicitTracking))])
                self._leafs = OrderedDict([
                    ('query_timeout', (YLeaf(YType.uint32, 'query-timeout'), ['int'])),
                    ('access_group', (YLeaf(YType.str, 'access-group'), ['str'])),
                    ('query_max_response_time', (YLeaf(YType.uint32, 'query-max-response-time'), ['int'])),
                    ('version', (YLeaf(YType.uint32, 'version'), ['int'])),
                    ('router_enable', (YLeaf(YType.boolean, 'router-enable'), ['bool'])),
                    ('query_interval', (YLeaf(YType.uint32, 'query-interval'), ['int'])),
                ])
                self.query_timeout = None
                self.access_group = None
                self.query_max_response_time = None
                self.version = None
                self.router_enable = None
                self.query_interval = None

                self.maximum_groups_per_interface_oor = None
                self._children_name_map["maximum_groups_per_interface_oor"] = "maximum-groups-per-interface-oor"

                self.explicit_tracking = None
                self._children_name_map["explicit_tracking"] = "explicit-tracking"
                self._segment_path = lambda: "inheritable-defaults"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-igmp-cfg:igmp/default-context/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Igmp.DefaultContext.InheritableDefaults, ['query_timeout', 'access_group', 'query_max_response_time', 'version', 'router_enable', 'query_interval'], name, value)


            class MaximumGroupsPerInterfaceOor(Entity):
                """
                Configure maximum number of groups accepted per
                interface by this router
                
                .. attribute:: maximum_groups
                
                	Maximum number of groups accepted per interface by this router
                	**type**\: int
                
                	**range:** 1..40000
                
                	**mandatory**\: True
                
                .. attribute:: warning_threshold
                
                	 WarningThreshold for number of groups accepted per interface by this router
                	**type**\: int
                
                	**range:** 1..40000
                
                	**default value**\: 25000
                
                .. attribute:: access_list_name
                
                	Access\-list to account for
                	**type**\: str
                
                	**length:** 1..64
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'ipv4-igmp-cfg'
                _revision = '2017-10-15'

                def __init__(self):
                    super(Igmp.DefaultContext.InheritableDefaults.MaximumGroupsPerInterfaceOor, self).__init__()

                    self.yang_name = "maximum-groups-per-interface-oor"
                    self.yang_parent_name = "inheritable-defaults"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self.is_presence_container = True
                    self._leafs = OrderedDict([
                        ('maximum_groups', (YLeaf(YType.uint32, 'maximum-groups'), ['int'])),
                        ('warning_threshold', (YLeaf(YType.uint32, 'warning-threshold'), ['int'])),
                        ('access_list_name', (YLeaf(YType.str, 'access-list-name'), ['str'])),
                    ])
                    self.maximum_groups = None
                    self.warning_threshold = None
                    self.access_list_name = None
                    self._segment_path = lambda: "maximum-groups-per-interface-oor"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-igmp-cfg:igmp/default-context/inheritable-defaults/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Igmp.DefaultContext.InheritableDefaults.MaximumGroupsPerInterfaceOor, ['maximum_groups', 'warning_threshold', 'access_list_name'], name, value)


            class ExplicitTracking(Entity):
                """
                IGMPv3 explicit host tracking
                
                .. attribute:: enable
                
                	Enabled or disabled, when value is TRUE or FALSE respectively
                	**type**\: bool
                
                	**mandatory**\: True
                
                .. attribute:: access_list_name
                
                	Access list specifying tracking group range
                	**type**\: str
                
                	**length:** 1..64
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'ipv4-igmp-cfg'
                _revision = '2017-10-15'

                def __init__(self):
                    super(Igmp.DefaultContext.InheritableDefaults.ExplicitTracking, self).__init__()

                    self.yang_name = "explicit-tracking"
                    self.yang_parent_name = "inheritable-defaults"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self.is_presence_container = True
                    self._leafs = OrderedDict([
                        ('enable', (YLeaf(YType.boolean, 'enable'), ['bool'])),
                        ('access_list_name', (YLeaf(YType.str, 'access-list-name'), ['str'])),
                    ])
                    self.enable = None
                    self.access_list_name = None
                    self._segment_path = lambda: "explicit-tracking"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-igmp-cfg:igmp/default-context/inheritable-defaults/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Igmp.DefaultContext.InheritableDefaults.ExplicitTracking, ['enable', 'access_list_name'], name, value)


        class SsmAccessGroups(Entity):
            """
            IGMP Source specific mode
            
            .. attribute:: ssm_access_group
            
            	SSM static Access Group
            	**type**\: list of  		 :py:class:`SsmAccessGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext.SsmAccessGroups.SsmAccessGroup>`
            
            

            """

            _prefix = 'ipv4-igmp-cfg'
            _revision = '2017-10-15'

            def __init__(self):
                super(Igmp.DefaultContext.SsmAccessGroups, self).__init__()

                self.yang_name = "ssm-access-groups"
                self.yang_parent_name = "default-context"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("ssm-access-group", ("ssm_access_group", Igmp.DefaultContext.SsmAccessGroups.SsmAccessGroup))])
                self._leafs = OrderedDict()

                self.ssm_access_group = YList(self)
                self._segment_path = lambda: "ssm-access-groups"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-igmp-cfg:igmp/default-context/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Igmp.DefaultContext.SsmAccessGroups, [], name, value)


            class SsmAccessGroup(Entity):
                """
                SSM static Access Group
                
                .. attribute:: source_address  (key)
                
                	IP source address
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: access_list_name
                
                	Access list specifying access group
                	**type**\: str
                
                	**length:** 1..64
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'ipv4-igmp-cfg'
                _revision = '2017-10-15'

                def __init__(self):
                    super(Igmp.DefaultContext.SsmAccessGroups.SsmAccessGroup, self).__init__()

                    self.yang_name = "ssm-access-group"
                    self.yang_parent_name = "ssm-access-groups"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['source_address']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('source_address', (YLeaf(YType.str, 'source-address'), ['str','str'])),
                        ('access_list_name', (YLeaf(YType.str, 'access-list-name'), ['str'])),
                    ])
                    self.source_address = None
                    self.access_list_name = None
                    self._segment_path = lambda: "ssm-access-group" + "[source-address='" + str(self.source_address) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-igmp-cfg:igmp/default-context/ssm-access-groups/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Igmp.DefaultContext.SsmAccessGroups.SsmAccessGroup, ['source_address', 'access_list_name'], name, value)


        class Maximum(Entity):
            """
            Configure IGMP State Limits
            
            .. attribute:: maximum_groups
            
            	Configure maximum number of groups accepted by this router
            	**type**\: int
            
            	**range:** 1..75000
            
            	**default value**\: 50000
            
            

            """

            _prefix = 'ipv4-igmp-cfg'
            _revision = '2017-10-15'

            def __init__(self):
                super(Igmp.DefaultContext.Maximum, self).__init__()

                self.yang_name = "maximum"
                self.yang_parent_name = "default-context"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('maximum_groups', (YLeaf(YType.uint32, 'maximum-groups'), ['int'])),
                ])
                self.maximum_groups = None
                self._segment_path = lambda: "maximum"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-igmp-cfg:igmp/default-context/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Igmp.DefaultContext.Maximum, ['maximum_groups'], name, value)


        class Interfaces(Entity):
            """
            Interface\-level configuration
            
            .. attribute:: interface
            
            	The name of the interface
            	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext.Interfaces.Interface>`
            
            

            """

            _prefix = 'ipv4-igmp-cfg'
            _revision = '2017-10-15'

            def __init__(self):
                super(Igmp.DefaultContext.Interfaces, self).__init__()

                self.yang_name = "interfaces"
                self.yang_parent_name = "default-context"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("interface", ("interface", Igmp.DefaultContext.Interfaces.Interface))])
                self._leafs = OrderedDict()

                self.interface = YList(self)
                self._segment_path = lambda: "interfaces"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-igmp-cfg:igmp/default-context/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Igmp.DefaultContext.Interfaces, [], name, value)


            class Interface(Entity):
                """
                The name of the interface
                
                .. attribute:: interface_name  (key)
                
                	Name of the interface
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                .. attribute:: join_groups
                
                	IGMP join multicast group
                	**type**\:  :py:class:`JoinGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext.Interfaces.Interface.JoinGroups>`
                
                	**presence node**\: True
                
                .. attribute:: static_group_group_addresses
                
                	IGMP static multicast group
                	**type**\:  :py:class:`StaticGroupGroupAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses>`
                
                .. attribute:: maximum_groups_per_interface_oor
                
                	Configure maximum number of groups accepted per interface by this router
                	**type**\:  :py:class:`MaximumGroupsPerInterfaceOor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext.Interfaces.Interface.MaximumGroupsPerInterfaceOor>`
                
                	**presence node**\: True
                
                .. attribute:: query_timeout
                
                	IGMP previous querier timeout
                	**type**\: int
                
                	**range:** 60..300
                
                	**units**\: second
                
                .. attribute:: access_group
                
                	Access list specifying access group range
                	**type**\: str
                
                	**length:** 1..64
                
                .. attribute:: query_max_response_time
                
                	Query response value in seconds
                	**type**\: int
                
                	**range:** 1..12
                
                	**units**\: second
                
                	**default value**\: 10
                
                .. attribute:: version
                
                	Version number
                	**type**\: int
                
                	**range:** 1..3
                
                	**default value**\: 3
                
                .. attribute:: router_enable
                
                	Enabled or disabled, when value is TRUE or FALSE respectively
                	**type**\: bool
                
                	**default value**\: true
                
                .. attribute:: query_interval
                
                	Query interval in seconds
                	**type**\: int
                
                	**range:** 1..3600
                
                	**units**\: second
                
                	**default value**\: 60
                
                .. attribute:: explicit_tracking
                
                	IGMPv3 explicit host tracking
                	**type**\:  :py:class:`ExplicitTracking <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext.Interfaces.Interface.ExplicitTracking>`
                
                	**presence node**\: True
                
                

                """

                _prefix = 'ipv4-igmp-cfg'
                _revision = '2017-10-15'

                def __init__(self):
                    super(Igmp.DefaultContext.Interfaces.Interface, self).__init__()

                    self.yang_name = "interface"
                    self.yang_parent_name = "interfaces"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['interface_name']
                    self._child_classes = OrderedDict([("join-groups", ("join_groups", Igmp.DefaultContext.Interfaces.Interface.JoinGroups)), ("static-group-group-addresses", ("static_group_group_addresses", Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses)), ("maximum-groups-per-interface-oor", ("maximum_groups_per_interface_oor", Igmp.DefaultContext.Interfaces.Interface.MaximumGroupsPerInterfaceOor)), ("explicit-tracking", ("explicit_tracking", Igmp.DefaultContext.Interfaces.Interface.ExplicitTracking))])
                    self._leafs = OrderedDict([
                        ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                        ('query_timeout', (YLeaf(YType.uint32, 'query-timeout'), ['int'])),
                        ('access_group', (YLeaf(YType.str, 'access-group'), ['str'])),
                        ('query_max_response_time', (YLeaf(YType.uint32, 'query-max-response-time'), ['int'])),
                        ('version', (YLeaf(YType.uint32, 'version'), ['int'])),
                        ('router_enable', (YLeaf(YType.boolean, 'router-enable'), ['bool'])),
                        ('query_interval', (YLeaf(YType.uint32, 'query-interval'), ['int'])),
                    ])
                    self.interface_name = None
                    self.query_timeout = None
                    self.access_group = None
                    self.query_max_response_time = None
                    self.version = None
                    self.router_enable = None
                    self.query_interval = None

                    self.join_groups = None
                    self._children_name_map["join_groups"] = "join-groups"

                    self.static_group_group_addresses = Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses()
                    self.static_group_group_addresses.parent = self
                    self._children_name_map["static_group_group_addresses"] = "static-group-group-addresses"

                    self.maximum_groups_per_interface_oor = None
                    self._children_name_map["maximum_groups_per_interface_oor"] = "maximum-groups-per-interface-oor"

                    self.explicit_tracking = None
                    self._children_name_map["explicit_tracking"] = "explicit-tracking"
                    self._segment_path = lambda: "interface" + "[interface-name='" + str(self.interface_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-igmp-cfg:igmp/default-context/interfaces/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Igmp.DefaultContext.Interfaces.Interface, ['interface_name', 'query_timeout', 'access_group', 'query_max_response_time', 'version', 'router_enable', 'query_interval'], name, value)


                class JoinGroups(Entity):
                    """
                    IGMP join multicast group
                    
                    .. attribute:: join_group
                    
                    	IP group address and optional source address to include
                    	**type**\: list of  		 :py:class:`JoinGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext.Interfaces.Interface.JoinGroups.JoinGroup>`
                    
                    .. attribute:: join_group_source_address
                    
                    	IP group address and optional source address to include
                    	**type**\: list of  		 :py:class:`JoinGroupSourceAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext.Interfaces.Interface.JoinGroups.JoinGroupSourceAddress>`
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-igmp-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Igmp.DefaultContext.Interfaces.Interface.JoinGroups, self).__init__()

                        self.yang_name = "join-groups"
                        self.yang_parent_name = "interface"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("join-group", ("join_group", Igmp.DefaultContext.Interfaces.Interface.JoinGroups.JoinGroup)), ("join-group-source-address", ("join_group_source_address", Igmp.DefaultContext.Interfaces.Interface.JoinGroups.JoinGroupSourceAddress))])
                        self.is_presence_container = True
                        self._leafs = OrderedDict()

                        self.join_group = YList(self)
                        self.join_group_source_address = YList(self)
                        self._segment_path = lambda: "join-groups"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Igmp.DefaultContext.Interfaces.Interface.JoinGroups, [], name, value)


                    class JoinGroup(Entity):
                        """
                        IP group address and optional source address
                        to include
                        
                        .. attribute:: group_address  (key)
                        
                        	IP group address
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: mode
                        
                        	Filter mode
                        	**type**\:  :py:class:`IgmpFilter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.IgmpFilter>`
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2017-10-15'

                        def __init__(self):
                            super(Igmp.DefaultContext.Interfaces.Interface.JoinGroups.JoinGroup, self).__init__()

                            self.yang_name = "join-group"
                            self.yang_parent_name = "join-groups"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['group_address']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('group_address', (YLeaf(YType.str, 'group-address'), ['str','str'])),
                                ('mode', (YLeaf(YType.enumeration, 'mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'IgmpFilter', '')])),
                            ])
                            self.group_address = None
                            self.mode = None
                            self._segment_path = lambda: "join-group" + "[group-address='" + str(self.group_address) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Igmp.DefaultContext.Interfaces.Interface.JoinGroups.JoinGroup, ['group_address', 'mode'], name, value)


                    class JoinGroupSourceAddress(Entity):
                        """
                        IP group address and optional source address
                        to include
                        
                        .. attribute:: group_address  (key)
                        
                        	IP group address
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: source_address  (key)
                        
                        	Optional IP source address
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: mode
                        
                        	Filter mode
                        	**type**\:  :py:class:`IgmpFilter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.IgmpFilter>`
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2017-10-15'

                        def __init__(self):
                            super(Igmp.DefaultContext.Interfaces.Interface.JoinGroups.JoinGroupSourceAddress, self).__init__()

                            self.yang_name = "join-group-source-address"
                            self.yang_parent_name = "join-groups"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['group_address','source_address']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('group_address', (YLeaf(YType.str, 'group-address'), ['str','str'])),
                                ('source_address', (YLeaf(YType.str, 'source-address'), ['str','str'])),
                                ('mode', (YLeaf(YType.enumeration, 'mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'IgmpFilter', '')])),
                            ])
                            self.group_address = None
                            self.source_address = None
                            self.mode = None
                            self._segment_path = lambda: "join-group-source-address" + "[group-address='" + str(self.group_address) + "']" + "[source-address='" + str(self.source_address) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Igmp.DefaultContext.Interfaces.Interface.JoinGroups.JoinGroupSourceAddress, ['group_address', 'source_address', 'mode'], name, value)


                class StaticGroupGroupAddresses(Entity):
                    """
                    IGMP static multicast group
                    
                    .. attribute:: static_group_group_address
                    
                    	IP group address and optional source address to include
                    	**type**\: list of  		 :py:class:`StaticGroupGroupAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddress>`
                    
                    .. attribute:: static_group_group_address_source_address
                    
                    	IP group address and optional source address to include
                    	**type**\: list of  		 :py:class:`StaticGroupGroupAddressSourceAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddress>`
                    
                    .. attribute:: static_group_group_address_source_address_source_address_mask
                    
                    	IP group address and optional source address to include
                    	**type**\: list of  		 :py:class:`StaticGroupGroupAddressSourceAddressSourceAddressMask <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddressSourceAddressMask>`
                    
                    .. attribute:: static_group_group_address_group_address_mask
                    
                    	IP group address and optional source address to include
                    	**type**\: list of  		 :py:class:`StaticGroupGroupAddressGroupAddressMask <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMask>`
                    
                    .. attribute:: static_group_group_address_group_address_mask_source_address
                    
                    	IP group address and optional source address to include
                    	**type**\: list of  		 :py:class:`StaticGroupGroupAddressGroupAddressMaskSourceAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddress>`
                    
                    .. attribute:: static_group_group_address_group_address_mask_source_address_source_address_mask
                    
                    	IP group address and optional source address to include
                    	**type**\: list of  		 :py:class:`StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask>`
                    
                    

                    """

                    _prefix = 'ipv4-igmp-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses, self).__init__()

                        self.yang_name = "static-group-group-addresses"
                        self.yang_parent_name = "interface"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("static-group-group-address", ("static_group_group_address", Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddress)), ("static-group-group-address-source-address", ("static_group_group_address_source_address", Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddress)), ("static-group-group-address-source-address-source-address-mask", ("static_group_group_address_source_address_source_address_mask", Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddressSourceAddressMask)), ("static-group-group-address-group-address-mask", ("static_group_group_address_group_address_mask", Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMask)), ("static-group-group-address-group-address-mask-source-address", ("static_group_group_address_group_address_mask_source_address", Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddress)), ("static-group-group-address-group-address-mask-source-address-source-address-mask", ("static_group_group_address_group_address_mask_source_address_source_address_mask", Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask))])
                        self._leafs = OrderedDict()

                        self.static_group_group_address = YList(self)
                        self.static_group_group_address_source_address = YList(self)
                        self.static_group_group_address_source_address_source_address_mask = YList(self)
                        self.static_group_group_address_group_address_mask = YList(self)
                        self.static_group_group_address_group_address_mask_source_address = YList(self)
                        self.static_group_group_address_group_address_mask_source_address_source_address_mask = YList(self)
                        self._segment_path = lambda: "static-group-group-addresses"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses, [], name, value)


                    class StaticGroupGroupAddress(Entity):
                        """
                        IP group address and optional source address
                        to include
                        
                        .. attribute:: group_address  (key)
                        
                        	IP group address
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: group_count
                        
                        	Number of groups to join (do not set without GroupAddressMask)
                        	**type**\: int
                        
                        	**range:** 1..512
                        
                        	**default value**\: 1
                        
                        .. attribute:: source_count
                        
                        	Number of sources to join (do not set without SourceAddressMask)
                        	**type**\: int
                        
                        	**range:** 1..512
                        
                        	**default value**\: 1
                        
                        .. attribute:: suppress_report
                        
                        	Suppress reports
                        	**type**\: bool
                        
                        	**default value**\: false
                        
                        

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2017-10-15'

                        def __init__(self):
                            super(Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddress, self).__init__()

                            self.yang_name = "static-group-group-address"
                            self.yang_parent_name = "static-group-group-addresses"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['group_address']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('group_address', (YLeaf(YType.str, 'group-address'), ['str','str'])),
                                ('group_count', (YLeaf(YType.uint32, 'group-count'), ['int'])),
                                ('source_count', (YLeaf(YType.uint32, 'source-count'), ['int'])),
                                ('suppress_report', (YLeaf(YType.boolean, 'suppress-report'), ['bool'])),
                            ])
                            self.group_address = None
                            self.group_count = None
                            self.source_count = None
                            self.suppress_report = None
                            self._segment_path = lambda: "static-group-group-address" + "[group-address='" + str(self.group_address) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddress, ['group_address', 'group_count', 'source_count', 'suppress_report'], name, value)


                    class StaticGroupGroupAddressSourceAddress(Entity):
                        """
                        IP group address and optional source address
                        to include
                        
                        .. attribute:: group_address  (key)
                        
                        	IP group address
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: source_address  (key)
                        
                        	IP source address
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: group_count
                        
                        	Number of groups to join (do not set without GroupAddressMask)
                        	**type**\: int
                        
                        	**range:** 1..512
                        
                        	**default value**\: 1
                        
                        .. attribute:: source_count
                        
                        	Number of sources to join (do not set without SourceAddressMask)
                        	**type**\: int
                        
                        	**range:** 1..512
                        
                        	**default value**\: 1
                        
                        .. attribute:: suppress_report
                        
                        	Suppress reports
                        	**type**\: bool
                        
                        	**default value**\: false
                        
                        

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2017-10-15'

                        def __init__(self):
                            super(Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddress, self).__init__()

                            self.yang_name = "static-group-group-address-source-address"
                            self.yang_parent_name = "static-group-group-addresses"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['group_address','source_address']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('group_address', (YLeaf(YType.str, 'group-address'), ['str','str'])),
                                ('source_address', (YLeaf(YType.str, 'source-address'), ['str','str'])),
                                ('group_count', (YLeaf(YType.uint32, 'group-count'), ['int'])),
                                ('source_count', (YLeaf(YType.uint32, 'source-count'), ['int'])),
                                ('suppress_report', (YLeaf(YType.boolean, 'suppress-report'), ['bool'])),
                            ])
                            self.group_address = None
                            self.source_address = None
                            self.group_count = None
                            self.source_count = None
                            self.suppress_report = None
                            self._segment_path = lambda: "static-group-group-address-source-address" + "[group-address='" + str(self.group_address) + "']" + "[source-address='" + str(self.source_address) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddress, ['group_address', 'source_address', 'group_count', 'source_count', 'suppress_report'], name, value)


                    class StaticGroupGroupAddressSourceAddressSourceAddressMask(Entity):
                        """
                        IP group address and optional source address
                        to include
                        
                        .. attribute:: group_address  (key)
                        
                        	IP group address
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: source_address  (key)
                        
                        	IP source address
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: source_address_mask  (key)
                        
                        	Mask for Source Address
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: group_count
                        
                        	Number of groups to join (do not set without GroupAddressMask)
                        	**type**\: int
                        
                        	**range:** 1..512
                        
                        	**default value**\: 1
                        
                        .. attribute:: source_count
                        
                        	Number of sources to join (do not set without SourceAddressMask)
                        	**type**\: int
                        
                        	**range:** 1..512
                        
                        	**default value**\: 1
                        
                        .. attribute:: suppress_report
                        
                        	Suppress reports
                        	**type**\: bool
                        
                        	**default value**\: false
                        
                        

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2017-10-15'

                        def __init__(self):
                            super(Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddressSourceAddressMask, self).__init__()

                            self.yang_name = "static-group-group-address-source-address-source-address-mask"
                            self.yang_parent_name = "static-group-group-addresses"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['group_address','source_address','source_address_mask']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('group_address', (YLeaf(YType.str, 'group-address'), ['str','str'])),
                                ('source_address', (YLeaf(YType.str, 'source-address'), ['str','str'])),
                                ('source_address_mask', (YLeaf(YType.str, 'source-address-mask'), ['str','str'])),
                                ('group_count', (YLeaf(YType.uint32, 'group-count'), ['int'])),
                                ('source_count', (YLeaf(YType.uint32, 'source-count'), ['int'])),
                                ('suppress_report', (YLeaf(YType.boolean, 'suppress-report'), ['bool'])),
                            ])
                            self.group_address = None
                            self.source_address = None
                            self.source_address_mask = None
                            self.group_count = None
                            self.source_count = None
                            self.suppress_report = None
                            self._segment_path = lambda: "static-group-group-address-source-address-source-address-mask" + "[group-address='" + str(self.group_address) + "']" + "[source-address='" + str(self.source_address) + "']" + "[source-address-mask='" + str(self.source_address_mask) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddressSourceAddressMask, ['group_address', 'source_address', 'source_address_mask', 'group_count', 'source_count', 'suppress_report'], name, value)


                    class StaticGroupGroupAddressGroupAddressMask(Entity):
                        """
                        IP group address and optional source address
                        to include
                        
                        .. attribute:: group_address  (key)
                        
                        	IP group address
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: group_address_mask  (key)
                        
                        	Mask for Group Address
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: group_count
                        
                        	Number of groups to join (do not set without GroupAddressMask)
                        	**type**\: int
                        
                        	**range:** 1..512
                        
                        	**default value**\: 1
                        
                        .. attribute:: source_count
                        
                        	Number of sources to join (do not set without SourceAddressMask)
                        	**type**\: int
                        
                        	**range:** 1..512
                        
                        	**default value**\: 1
                        
                        .. attribute:: suppress_report
                        
                        	Suppress reports
                        	**type**\: bool
                        
                        	**default value**\: false
                        
                        

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2017-10-15'

                        def __init__(self):
                            super(Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMask, self).__init__()

                            self.yang_name = "static-group-group-address-group-address-mask"
                            self.yang_parent_name = "static-group-group-addresses"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['group_address','group_address_mask']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('group_address', (YLeaf(YType.str, 'group-address'), ['str','str'])),
                                ('group_address_mask', (YLeaf(YType.str, 'group-address-mask'), ['str','str'])),
                                ('group_count', (YLeaf(YType.uint32, 'group-count'), ['int'])),
                                ('source_count', (YLeaf(YType.uint32, 'source-count'), ['int'])),
                                ('suppress_report', (YLeaf(YType.boolean, 'suppress-report'), ['bool'])),
                            ])
                            self.group_address = None
                            self.group_address_mask = None
                            self.group_count = None
                            self.source_count = None
                            self.suppress_report = None
                            self._segment_path = lambda: "static-group-group-address-group-address-mask" + "[group-address='" + str(self.group_address) + "']" + "[group-address-mask='" + str(self.group_address_mask) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMask, ['group_address', 'group_address_mask', 'group_count', 'source_count', 'suppress_report'], name, value)


                    class StaticGroupGroupAddressGroupAddressMaskSourceAddress(Entity):
                        """
                        IP group address and optional source address
                        to include
                        
                        .. attribute:: group_address  (key)
                        
                        	IP group address
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: group_address_mask  (key)
                        
                        	Mask for Group Address
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: source_address  (key)
                        
                        	IP source address
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: group_count
                        
                        	Number of groups to join (do not set without GroupAddressMask)
                        	**type**\: int
                        
                        	**range:** 1..512
                        
                        	**default value**\: 1
                        
                        .. attribute:: source_count
                        
                        	Number of sources to join (do not set without SourceAddressMask)
                        	**type**\: int
                        
                        	**range:** 1..512
                        
                        	**default value**\: 1
                        
                        .. attribute:: suppress_report
                        
                        	Suppress reports
                        	**type**\: bool
                        
                        	**default value**\: false
                        
                        

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2017-10-15'

                        def __init__(self):
                            super(Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddress, self).__init__()

                            self.yang_name = "static-group-group-address-group-address-mask-source-address"
                            self.yang_parent_name = "static-group-group-addresses"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['group_address','group_address_mask','source_address']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('group_address', (YLeaf(YType.str, 'group-address'), ['str','str'])),
                                ('group_address_mask', (YLeaf(YType.str, 'group-address-mask'), ['str','str'])),
                                ('source_address', (YLeaf(YType.str, 'source-address'), ['str','str'])),
                                ('group_count', (YLeaf(YType.uint32, 'group-count'), ['int'])),
                                ('source_count', (YLeaf(YType.uint32, 'source-count'), ['int'])),
                                ('suppress_report', (YLeaf(YType.boolean, 'suppress-report'), ['bool'])),
                            ])
                            self.group_address = None
                            self.group_address_mask = None
                            self.source_address = None
                            self.group_count = None
                            self.source_count = None
                            self.suppress_report = None
                            self._segment_path = lambda: "static-group-group-address-group-address-mask-source-address" + "[group-address='" + str(self.group_address) + "']" + "[group-address-mask='" + str(self.group_address_mask) + "']" + "[source-address='" + str(self.source_address) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddress, ['group_address', 'group_address_mask', 'source_address', 'group_count', 'source_count', 'suppress_report'], name, value)


                    class StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask(Entity):
                        """
                        IP group address and optional source address
                        to include
                        
                        .. attribute:: group_address  (key)
                        
                        	IP group address
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: group_address_mask  (key)
                        
                        	Mask for Group Address
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: source_address  (key)
                        
                        	IP source address
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: source_address_mask  (key)
                        
                        	Mask for Source Address
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: group_count
                        
                        	Number of groups to join (do not set without GroupAddressMask)
                        	**type**\: int
                        
                        	**range:** 1..512
                        
                        	**default value**\: 1
                        
                        .. attribute:: source_count
                        
                        	Number of sources to join (do not set without SourceAddressMask)
                        	**type**\: int
                        
                        	**range:** 1..512
                        
                        	**default value**\: 1
                        
                        .. attribute:: suppress_report
                        
                        	Suppress reports
                        	**type**\: bool
                        
                        	**default value**\: false
                        
                        

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2017-10-15'

                        def __init__(self):
                            super(Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask, self).__init__()

                            self.yang_name = "static-group-group-address-group-address-mask-source-address-source-address-mask"
                            self.yang_parent_name = "static-group-group-addresses"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['group_address','group_address_mask','source_address','source_address_mask']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('group_address', (YLeaf(YType.str, 'group-address'), ['str','str'])),
                                ('group_address_mask', (YLeaf(YType.str, 'group-address-mask'), ['str','str'])),
                                ('source_address', (YLeaf(YType.str, 'source-address'), ['str','str'])),
                                ('source_address_mask', (YLeaf(YType.str, 'source-address-mask'), ['str','str'])),
                                ('group_count', (YLeaf(YType.uint32, 'group-count'), ['int'])),
                                ('source_count', (YLeaf(YType.uint32, 'source-count'), ['int'])),
                                ('suppress_report', (YLeaf(YType.boolean, 'suppress-report'), ['bool'])),
                            ])
                            self.group_address = None
                            self.group_address_mask = None
                            self.source_address = None
                            self.source_address_mask = None
                            self.group_count = None
                            self.source_count = None
                            self.suppress_report = None
                            self._segment_path = lambda: "static-group-group-address-group-address-mask-source-address-source-address-mask" + "[group-address='" + str(self.group_address) + "']" + "[group-address-mask='" + str(self.group_address_mask) + "']" + "[source-address='" + str(self.source_address) + "']" + "[source-address-mask='" + str(self.source_address_mask) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask, ['group_address', 'group_address_mask', 'source_address', 'source_address_mask', 'group_count', 'source_count', 'suppress_report'], name, value)


                class MaximumGroupsPerInterfaceOor(Entity):
                    """
                    Configure maximum number of groups accepted per
                    interface by this router
                    
                    .. attribute:: maximum_groups
                    
                    	Maximum number of groups accepted per interface by this router
                    	**type**\: int
                    
                    	**range:** 1..40000
                    
                    	**mandatory**\: True
                    
                    .. attribute:: warning_threshold
                    
                    	 WarningThreshold for number of groups accepted per interface by this router
                    	**type**\: int
                    
                    	**range:** 1..40000
                    
                    	**default value**\: 25000
                    
                    .. attribute:: access_list_name
                    
                    	Access\-list to account for
                    	**type**\: str
                    
                    	**length:** 1..64
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-igmp-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Igmp.DefaultContext.Interfaces.Interface.MaximumGroupsPerInterfaceOor, self).__init__()

                        self.yang_name = "maximum-groups-per-interface-oor"
                        self.yang_parent_name = "interface"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('maximum_groups', (YLeaf(YType.uint32, 'maximum-groups'), ['int'])),
                            ('warning_threshold', (YLeaf(YType.uint32, 'warning-threshold'), ['int'])),
                            ('access_list_name', (YLeaf(YType.str, 'access-list-name'), ['str'])),
                        ])
                        self.maximum_groups = None
                        self.warning_threshold = None
                        self.access_list_name = None
                        self._segment_path = lambda: "maximum-groups-per-interface-oor"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Igmp.DefaultContext.Interfaces.Interface.MaximumGroupsPerInterfaceOor, ['maximum_groups', 'warning_threshold', 'access_list_name'], name, value)


                class ExplicitTracking(Entity):
                    """
                    IGMPv3 explicit host tracking
                    
                    .. attribute:: enable
                    
                    	Enabled or disabled, when value is TRUE or FALSE respectively
                    	**type**\: bool
                    
                    	**mandatory**\: True
                    
                    .. attribute:: access_list_name
                    
                    	Access list specifying tracking group range
                    	**type**\: str
                    
                    	**length:** 1..64
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-igmp-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Igmp.DefaultContext.Interfaces.Interface.ExplicitTracking, self).__init__()

                        self.yang_name = "explicit-tracking"
                        self.yang_parent_name = "interface"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('enable', (YLeaf(YType.boolean, 'enable'), ['bool'])),
                            ('access_list_name', (YLeaf(YType.str, 'access-list-name'), ['str'])),
                        ])
                        self.enable = None
                        self.access_list_name = None
                        self._segment_path = lambda: "explicit-tracking"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Igmp.DefaultContext.Interfaces.Interface.ExplicitTracking, ['enable', 'access_list_name'], name, value)

    def clone_ptr(self):
        self._top_entity = Igmp()
        return self._top_entity

class Amt(Entity):
    """
    amt
    
    .. attribute:: relay_adv_add
    
    	Configure AMT Relay IPv4 Advertisement Address
    	**type**\:  :py:class:`RelayAdvAdd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Amt.RelayAdvAdd>`
    
    	**presence node**\: True
    
    .. attribute:: relay_anycast_prefix
    
    	Configure AMT Relay IPv4 Anycast\-Prefix
    	**type**\:  :py:class:`RelayAnycastPrefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Amt.RelayAnycastPrefix>`
    
    	**presence node**\: True
    
    .. attribute:: maximum_v4_route_gateway
    
    	Configure Maximum number of IPv4 route\-gateways (Tunnels)
    	**type**\: int
    
    	**range:** 1..4294967295
    
    .. attribute:: gateway_filter
    
    	Access list for Gateway Filter
    	**type**\: str
    
    	**length:** 1..64
    
    .. attribute:: maximum_v4_routes
    
    	Configure Maximum number of IPv4 Routes
    	**type**\: int
    
    	**range:** 1..4294967295
    
    .. attribute:: amttos
    
    	Configure AMT Relay TOS
    	**type**\: int
    
    	**range:** 1..255
    
    .. attribute:: amtttl
    
    	Configure AMT Relay TTL
    	**type**\: int
    
    	**range:** 1..255
    
    .. attribute:: maximum_v6_route_gateway
    
    	Configure Maximum number of IPv6 route\-gateways (Tunnels)
    	**type**\: int
    
    	**range:** 1..4294967295
    
    .. attribute:: maximum_gateway
    
    	Configure AMT maximum number of Gateways
    	**type**\: int
    
    	**range:** 1..4294967295
    
    .. attribute:: maximum_v6_routes
    
    	Configure Maximum number of IPv6 Routes
    	**type**\: int
    
    	**range:** 1..4294967295
    
    .. attribute:: amtqqic
    
    	Configure AMT QQIC value
    	**type**\: int
    
    	**range:** 1..4294967295
    
    .. attribute:: amtmtu
    
    	Configure AMT Relay MTU
    	**type**\: int
    
    	**range:** 100..65535
    
    

    """

    _prefix = 'ipv4-igmp-cfg'
    _revision = '2017-10-15'

    def __init__(self):
        super(Amt, self).__init__()
        self._top_entity = None

        self.yang_name = "amt"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-igmp-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("relay-adv-add", ("relay_adv_add", Amt.RelayAdvAdd)), ("relay-anycast-prefix", ("relay_anycast_prefix", Amt.RelayAnycastPrefix))])
        self._leafs = OrderedDict([
            ('maximum_v4_route_gateway', (YLeaf(YType.uint32, 'maximum-v4-route-gateway'), ['int'])),
            ('gateway_filter', (YLeaf(YType.str, 'gateway-filter'), ['str'])),
            ('maximum_v4_routes', (YLeaf(YType.uint32, 'maximum-v4-routes'), ['int'])),
            ('amttos', (YLeaf(YType.uint32, 'amttos'), ['int'])),
            ('amtttl', (YLeaf(YType.uint32, 'amtttl'), ['int'])),
            ('maximum_v6_route_gateway', (YLeaf(YType.uint32, 'maximum-v6-route-gateway'), ['int'])),
            ('maximum_gateway', (YLeaf(YType.uint32, 'maximum-gateway'), ['int'])),
            ('maximum_v6_routes', (YLeaf(YType.uint32, 'maximum-v6-routes'), ['int'])),
            ('amtqqic', (YLeaf(YType.uint32, 'amtqqic'), ['int'])),
            ('amtmtu', (YLeaf(YType.uint32, 'amtmtu'), ['int'])),
        ])
        self.maximum_v4_route_gateway = None
        self.gateway_filter = None
        self.maximum_v4_routes = None
        self.amttos = None
        self.amtttl = None
        self.maximum_v6_route_gateway = None
        self.maximum_gateway = None
        self.maximum_v6_routes = None
        self.amtqqic = None
        self.amtmtu = None

        self.relay_adv_add = None
        self._children_name_map["relay_adv_add"] = "relay-adv-add"

        self.relay_anycast_prefix = None
        self._children_name_map["relay_anycast_prefix"] = "relay-anycast-prefix"
        self._segment_path = lambda: "Cisco-IOS-XR-ipv4-igmp-cfg:amt"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Amt, ['maximum_v4_route_gateway', 'gateway_filter', 'maximum_v4_routes', 'amttos', 'amtttl', 'maximum_v6_route_gateway', 'maximum_gateway', 'maximum_v6_routes', 'amtqqic', 'amtmtu'], name, value)


    class RelayAdvAdd(Entity):
        """
        Configure AMT Relay IPv4 Advertisement Address
        
        .. attribute:: address
        
        	AMT Relay IPv4 Advertisement Address
        	**type**\: str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        	**mandatory**\: True
        
        .. attribute:: interface
        
        	Relay Advertisement Interface
        	**type**\: str
        
        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'ipv4-igmp-cfg'
        _revision = '2017-10-15'

        def __init__(self):
            super(Amt.RelayAdvAdd, self).__init__()

            self.yang_name = "relay-adv-add"
            self.yang_parent_name = "amt"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self.is_presence_container = True
            self._leafs = OrderedDict([
                ('address', (YLeaf(YType.str, 'address'), ['str'])),
                ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
            ])
            self.address = None
            self.interface = None
            self._segment_path = lambda: "relay-adv-add"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-igmp-cfg:amt/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Amt.RelayAdvAdd, ['address', 'interface'], name, value)


    class RelayAnycastPrefix(Entity):
        """
        Configure AMT Relay IPv4 Anycast\-Prefix
        
        .. attribute:: address
        
        	Anycast\-Prefix Address
        	**type**\: str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        	**mandatory**\: True
        
        .. attribute:: prefix_length
        
        	Mask Length for Anycast Prefix
        	**type**\: int
        
        	**range:** 1..32
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'ipv4-igmp-cfg'
        _revision = '2017-10-15'

        def __init__(self):
            super(Amt.RelayAnycastPrefix, self).__init__()

            self.yang_name = "relay-anycast-prefix"
            self.yang_parent_name = "amt"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self.is_presence_container = True
            self._leafs = OrderedDict([
                ('address', (YLeaf(YType.str, 'address'), ['str'])),
                ('prefix_length', (YLeaf(YType.uint32, 'prefix-length'), ['int'])),
            ])
            self.address = None
            self.prefix_length = None
            self._segment_path = lambda: "relay-anycast-prefix"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-igmp-cfg:amt/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Amt.RelayAnycastPrefix, ['address', 'prefix_length'], name, value)

    def clone_ptr(self):
        self._top_entity = Amt()
        return self._top_entity

class Mld(Entity):
    """
    mld
    
    .. attribute:: vrfs
    
    	VRF related configuration
    	**type**\:  :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.Vrfs>`
    
    .. attribute:: default_context
    
    	Default Context
    	**type**\:  :py:class:`DefaultContext <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext>`
    
    	**presence node**\: True
    
    

    """

    _prefix = 'ipv4-igmp-cfg'
    _revision = '2017-10-15'

    def __init__(self):
        super(Mld, self).__init__()
        self._top_entity = None

        self.yang_name = "mld"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-igmp-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("vrfs", ("vrfs", Mld.Vrfs)), ("default-context", ("default_context", Mld.DefaultContext))])
        self._leafs = OrderedDict()

        self.vrfs = Mld.Vrfs()
        self.vrfs.parent = self
        self._children_name_map["vrfs"] = "vrfs"

        self.default_context = None
        self._children_name_map["default_context"] = "default-context"
        self._segment_path = lambda: "Cisco-IOS-XR-ipv4-igmp-cfg:mld"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Mld, [], name, value)


    class Vrfs(Entity):
        """
        VRF related configuration
        
        .. attribute:: vrf
        
        	Configuration for a particular vrf
        	**type**\: list of  		 :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.Vrfs.Vrf>`
        
        

        """

        _prefix = 'ipv4-igmp-cfg'
        _revision = '2017-10-15'

        def __init__(self):
            super(Mld.Vrfs, self).__init__()

            self.yang_name = "vrfs"
            self.yang_parent_name = "mld"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("vrf", ("vrf", Mld.Vrfs.Vrf))])
            self._leafs = OrderedDict()

            self.vrf = YList(self)
            self._segment_path = lambda: "vrfs"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-igmp-cfg:mld/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Mld.Vrfs, [], name, value)


        class Vrf(Entity):
            """
            Configuration for a particular vrf
            
            .. attribute:: vrf_name  (key)
            
            	Name for this vrf
            	**type**\: str
            
            	**length:** 1..32
            
            .. attribute:: traffic
            
            	Configure IGMP Traffic variables
            	**type**\:  :py:class:`Traffic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.Vrfs.Vrf.Traffic>`
            
            .. attribute:: inheritable_defaults
            
            	Inheritable Defaults
            	**type**\:  :py:class:`InheritableDefaults <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.Vrfs.Vrf.InheritableDefaults>`
            
            .. attribute:: ssm_access_groups
            
            	IGMP Source specific mode
            	**type**\:  :py:class:`SsmAccessGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.Vrfs.Vrf.SsmAccessGroups>`
            
            .. attribute:: maximum
            
            	Configure IGMP State Limits
            	**type**\:  :py:class:`Maximum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.Vrfs.Vrf.Maximum>`
            
            .. attribute:: ssmdns_query_group
            
            	Enable SSM mapping using DNS Query
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: interfaces
            
            	Interface\-level configuration
            	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.Vrfs.Vrf.Interfaces>`
            
            .. attribute:: robustness
            
            	Configure IGMP Robustness variable
            	**type**\: int
            
            	**range:** 2..10
            
            	**default value**\: 2
            
            

            """

            _prefix = 'ipv4-igmp-cfg'
            _revision = '2017-10-15'

            def __init__(self):
                super(Mld.Vrfs.Vrf, self).__init__()

                self.yang_name = "vrf"
                self.yang_parent_name = "vrfs"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['vrf_name']
                self._child_classes = OrderedDict([("traffic", ("traffic", Mld.Vrfs.Vrf.Traffic)), ("inheritable-defaults", ("inheritable_defaults", Mld.Vrfs.Vrf.InheritableDefaults)), ("ssm-access-groups", ("ssm_access_groups", Mld.Vrfs.Vrf.SsmAccessGroups)), ("maximum", ("maximum", Mld.Vrfs.Vrf.Maximum)), ("interfaces", ("interfaces", Mld.Vrfs.Vrf.Interfaces))])
                self._leafs = OrderedDict([
                    ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                    ('ssmdns_query_group', (YLeaf(YType.empty, 'ssmdns-query-group'), ['Empty'])),
                    ('robustness', (YLeaf(YType.uint32, 'robustness'), ['int'])),
                ])
                self.vrf_name = None
                self.ssmdns_query_group = None
                self.robustness = None

                self.traffic = Mld.Vrfs.Vrf.Traffic()
                self.traffic.parent = self
                self._children_name_map["traffic"] = "traffic"

                self.inheritable_defaults = Mld.Vrfs.Vrf.InheritableDefaults()
                self.inheritable_defaults.parent = self
                self._children_name_map["inheritable_defaults"] = "inheritable-defaults"

                self.ssm_access_groups = Mld.Vrfs.Vrf.SsmAccessGroups()
                self.ssm_access_groups.parent = self
                self._children_name_map["ssm_access_groups"] = "ssm-access-groups"

                self.maximum = Mld.Vrfs.Vrf.Maximum()
                self.maximum.parent = self
                self._children_name_map["maximum"] = "maximum"

                self.interfaces = Mld.Vrfs.Vrf.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"
                self._segment_path = lambda: "vrf" + "[vrf-name='" + str(self.vrf_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-igmp-cfg:mld/vrfs/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Mld.Vrfs.Vrf, ['vrf_name', 'ssmdns_query_group', 'robustness'], name, value)


            class Traffic(Entity):
                """
                Configure IGMP Traffic variables
                
                .. attribute:: profile
                
                	Configure the route\-policy profile
                	**type**\: str
                
                	**length:** 1..64
                
                

                """

                _prefix = 'ipv4-igmp-cfg'
                _revision = '2017-10-15'

                def __init__(self):
                    super(Mld.Vrfs.Vrf.Traffic, self).__init__()

                    self.yang_name = "traffic"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('profile', (YLeaf(YType.str, 'profile'), ['str'])),
                    ])
                    self.profile = None
                    self._segment_path = lambda: "traffic"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Mld.Vrfs.Vrf.Traffic, ['profile'], name, value)


            class InheritableDefaults(Entity):
                """
                Inheritable Defaults
                
                .. attribute:: maximum_groups_per_interface_oor
                
                	Configure maximum number of groups accepted per interface by this router
                	**type**\:  :py:class:`MaximumGroupsPerInterfaceOor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.Vrfs.Vrf.InheritableDefaults.MaximumGroupsPerInterfaceOor>`
                
                	**presence node**\: True
                
                .. attribute:: query_timeout
                
                	IGMP previous querier timeout
                	**type**\: int
                
                	**range:** 60..300
                
                	**units**\: second
                
                .. attribute:: access_group
                
                	Access list specifying access group range
                	**type**\: str
                
                	**length:** 1..64
                
                .. attribute:: query_max_response_time
                
                	Query response value in seconds
                	**type**\: int
                
                	**range:** 1..12
                
                	**units**\: second
                
                	**default value**\: 10
                
                .. attribute:: version
                
                	Version number
                	**type**\: int
                
                	**range:** 1..3
                
                	**default value**\: 3
                
                .. attribute:: router_enable
                
                	Enabled or disabled, when value is TRUE or FALSE respectively
                	**type**\: bool
                
                	**default value**\: true
                
                .. attribute:: query_interval
                
                	Query interval in seconds
                	**type**\: int
                
                	**range:** 1..3600
                
                	**units**\: second
                
                	**default value**\: 60
                
                .. attribute:: explicit_tracking
                
                	IGMPv3 explicit host tracking
                	**type**\:  :py:class:`ExplicitTracking <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.Vrfs.Vrf.InheritableDefaults.ExplicitTracking>`
                
                	**presence node**\: True
                
                

                """

                _prefix = 'ipv4-igmp-cfg'
                _revision = '2017-10-15'

                def __init__(self):
                    super(Mld.Vrfs.Vrf.InheritableDefaults, self).__init__()

                    self.yang_name = "inheritable-defaults"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("maximum-groups-per-interface-oor", ("maximum_groups_per_interface_oor", Mld.Vrfs.Vrf.InheritableDefaults.MaximumGroupsPerInterfaceOor)), ("explicit-tracking", ("explicit_tracking", Mld.Vrfs.Vrf.InheritableDefaults.ExplicitTracking))])
                    self._leafs = OrderedDict([
                        ('query_timeout', (YLeaf(YType.uint32, 'query-timeout'), ['int'])),
                        ('access_group', (YLeaf(YType.str, 'access-group'), ['str'])),
                        ('query_max_response_time', (YLeaf(YType.uint32, 'query-max-response-time'), ['int'])),
                        ('version', (YLeaf(YType.uint32, 'version'), ['int'])),
                        ('router_enable', (YLeaf(YType.boolean, 'router-enable'), ['bool'])),
                        ('query_interval', (YLeaf(YType.uint32, 'query-interval'), ['int'])),
                    ])
                    self.query_timeout = None
                    self.access_group = None
                    self.query_max_response_time = None
                    self.version = None
                    self.router_enable = None
                    self.query_interval = None

                    self.maximum_groups_per_interface_oor = None
                    self._children_name_map["maximum_groups_per_interface_oor"] = "maximum-groups-per-interface-oor"

                    self.explicit_tracking = None
                    self._children_name_map["explicit_tracking"] = "explicit-tracking"
                    self._segment_path = lambda: "inheritable-defaults"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Mld.Vrfs.Vrf.InheritableDefaults, ['query_timeout', 'access_group', 'query_max_response_time', 'version', 'router_enable', 'query_interval'], name, value)


                class MaximumGroupsPerInterfaceOor(Entity):
                    """
                    Configure maximum number of groups accepted per
                    interface by this router
                    
                    .. attribute:: maximum_groups
                    
                    	Maximum number of groups accepted per interface by this router
                    	**type**\: int
                    
                    	**range:** 1..40000
                    
                    	**mandatory**\: True
                    
                    .. attribute:: warning_threshold
                    
                    	 WarningThreshold for number of groups accepted per interface by this router
                    	**type**\: int
                    
                    	**range:** 1..40000
                    
                    	**default value**\: 25000
                    
                    .. attribute:: access_list_name
                    
                    	Access\-list to account for
                    	**type**\: str
                    
                    	**length:** 1..64
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-igmp-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Mld.Vrfs.Vrf.InheritableDefaults.MaximumGroupsPerInterfaceOor, self).__init__()

                        self.yang_name = "maximum-groups-per-interface-oor"
                        self.yang_parent_name = "inheritable-defaults"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('maximum_groups', (YLeaf(YType.uint32, 'maximum-groups'), ['int'])),
                            ('warning_threshold', (YLeaf(YType.uint32, 'warning-threshold'), ['int'])),
                            ('access_list_name', (YLeaf(YType.str, 'access-list-name'), ['str'])),
                        ])
                        self.maximum_groups = None
                        self.warning_threshold = None
                        self.access_list_name = None
                        self._segment_path = lambda: "maximum-groups-per-interface-oor"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mld.Vrfs.Vrf.InheritableDefaults.MaximumGroupsPerInterfaceOor, ['maximum_groups', 'warning_threshold', 'access_list_name'], name, value)


                class ExplicitTracking(Entity):
                    """
                    IGMPv3 explicit host tracking
                    
                    .. attribute:: enable
                    
                    	Enabled or disabled, when value is TRUE or FALSE respectively
                    	**type**\: bool
                    
                    	**mandatory**\: True
                    
                    .. attribute:: access_list_name
                    
                    	Access list specifying tracking group range
                    	**type**\: str
                    
                    	**length:** 1..64
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-igmp-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Mld.Vrfs.Vrf.InheritableDefaults.ExplicitTracking, self).__init__()

                        self.yang_name = "explicit-tracking"
                        self.yang_parent_name = "inheritable-defaults"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('enable', (YLeaf(YType.boolean, 'enable'), ['bool'])),
                            ('access_list_name', (YLeaf(YType.str, 'access-list-name'), ['str'])),
                        ])
                        self.enable = None
                        self.access_list_name = None
                        self._segment_path = lambda: "explicit-tracking"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mld.Vrfs.Vrf.InheritableDefaults.ExplicitTracking, ['enable', 'access_list_name'], name, value)


            class SsmAccessGroups(Entity):
                """
                IGMP Source specific mode
                
                .. attribute:: ssm_access_group
                
                	SSM static Access Group
                	**type**\: list of  		 :py:class:`SsmAccessGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.Vrfs.Vrf.SsmAccessGroups.SsmAccessGroup>`
                
                

                """

                _prefix = 'ipv4-igmp-cfg'
                _revision = '2017-10-15'

                def __init__(self):
                    super(Mld.Vrfs.Vrf.SsmAccessGroups, self).__init__()

                    self.yang_name = "ssm-access-groups"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("ssm-access-group", ("ssm_access_group", Mld.Vrfs.Vrf.SsmAccessGroups.SsmAccessGroup))])
                    self._leafs = OrderedDict()

                    self.ssm_access_group = YList(self)
                    self._segment_path = lambda: "ssm-access-groups"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Mld.Vrfs.Vrf.SsmAccessGroups, [], name, value)


                class SsmAccessGroup(Entity):
                    """
                    SSM static Access Group
                    
                    .. attribute:: source_address  (key)
                    
                    	IP source address
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    		**type**\: str
                    
                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: access_list_name
                    
                    	Access list specifying access group
                    	**type**\: str
                    
                    	**length:** 1..64
                    
                    	**mandatory**\: True
                    
                    

                    """

                    _prefix = 'ipv4-igmp-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Mld.Vrfs.Vrf.SsmAccessGroups.SsmAccessGroup, self).__init__()

                        self.yang_name = "ssm-access-group"
                        self.yang_parent_name = "ssm-access-groups"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['source_address']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('source_address', (YLeaf(YType.str, 'source-address'), ['str','str'])),
                            ('access_list_name', (YLeaf(YType.str, 'access-list-name'), ['str'])),
                        ])
                        self.source_address = None
                        self.access_list_name = None
                        self._segment_path = lambda: "ssm-access-group" + "[source-address='" + str(self.source_address) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mld.Vrfs.Vrf.SsmAccessGroups.SsmAccessGroup, ['source_address', 'access_list_name'], name, value)


            class Maximum(Entity):
                """
                Configure IGMP State Limits
                
                .. attribute:: maximum_groups
                
                	Configure maximum number of groups accepted by this router
                	**type**\: int
                
                	**range:** 1..75000
                
                	**default value**\: 50000
                
                

                """

                _prefix = 'ipv4-igmp-cfg'
                _revision = '2017-10-15'

                def __init__(self):
                    super(Mld.Vrfs.Vrf.Maximum, self).__init__()

                    self.yang_name = "maximum"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('maximum_groups', (YLeaf(YType.uint32, 'maximum-groups'), ['int'])),
                    ])
                    self.maximum_groups = None
                    self._segment_path = lambda: "maximum"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Mld.Vrfs.Vrf.Maximum, ['maximum_groups'], name, value)


            class Interfaces(Entity):
                """
                Interface\-level configuration
                
                .. attribute:: interface
                
                	The name of the interface
                	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.Vrfs.Vrf.Interfaces.Interface>`
                
                

                """

                _prefix = 'ipv4-igmp-cfg'
                _revision = '2017-10-15'

                def __init__(self):
                    super(Mld.Vrfs.Vrf.Interfaces, self).__init__()

                    self.yang_name = "interfaces"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("interface", ("interface", Mld.Vrfs.Vrf.Interfaces.Interface))])
                    self._leafs = OrderedDict()

                    self.interface = YList(self)
                    self._segment_path = lambda: "interfaces"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Mld.Vrfs.Vrf.Interfaces, [], name, value)


                class Interface(Entity):
                    """
                    The name of the interface
                    
                    .. attribute:: interface_name  (key)
                    
                    	Name of the interface
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: join_groups
                    
                    	IGMP join multicast group
                    	**type**\:  :py:class:`JoinGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.Vrfs.Vrf.Interfaces.Interface.JoinGroups>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: static_group_group_addresses
                    
                    	IGMP static multicast group
                    	**type**\:  :py:class:`StaticGroupGroupAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses>`
                    
                    .. attribute:: maximum_groups_per_interface_oor
                    
                    	Configure maximum number of groups accepted per interface by this router
                    	**type**\:  :py:class:`MaximumGroupsPerInterfaceOor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.Vrfs.Vrf.Interfaces.Interface.MaximumGroupsPerInterfaceOor>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: query_timeout
                    
                    	IGMP previous querier timeout
                    	**type**\: int
                    
                    	**range:** 60..300
                    
                    	**units**\: second
                    
                    .. attribute:: access_group
                    
                    	Access list specifying access group range
                    	**type**\: str
                    
                    	**length:** 1..64
                    
                    .. attribute:: query_max_response_time
                    
                    	Query response value in seconds
                    	**type**\: int
                    
                    	**range:** 1..12
                    
                    	**units**\: second
                    
                    	**default value**\: 10
                    
                    .. attribute:: version
                    
                    	Version number
                    	**type**\: int
                    
                    	**range:** 1..3
                    
                    	**default value**\: 3
                    
                    .. attribute:: router_enable
                    
                    	Enabled or disabled, when value is TRUE or FALSE respectively
                    	**type**\: bool
                    
                    	**default value**\: true
                    
                    .. attribute:: query_interval
                    
                    	Query interval in seconds
                    	**type**\: int
                    
                    	**range:** 1..3600
                    
                    	**units**\: second
                    
                    	**default value**\: 60
                    
                    .. attribute:: explicit_tracking
                    
                    	IGMPv3 explicit host tracking
                    	**type**\:  :py:class:`ExplicitTracking <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.Vrfs.Vrf.Interfaces.Interface.ExplicitTracking>`
                    
                    	**presence node**\: True
                    
                    

                    """

                    _prefix = 'ipv4-igmp-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Mld.Vrfs.Vrf.Interfaces.Interface, self).__init__()

                        self.yang_name = "interface"
                        self.yang_parent_name = "interfaces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['interface_name']
                        self._child_classes = OrderedDict([("join-groups", ("join_groups", Mld.Vrfs.Vrf.Interfaces.Interface.JoinGroups)), ("static-group-group-addresses", ("static_group_group_addresses", Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses)), ("maximum-groups-per-interface-oor", ("maximum_groups_per_interface_oor", Mld.Vrfs.Vrf.Interfaces.Interface.MaximumGroupsPerInterfaceOor)), ("explicit-tracking", ("explicit_tracking", Mld.Vrfs.Vrf.Interfaces.Interface.ExplicitTracking))])
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                            ('query_timeout', (YLeaf(YType.uint32, 'query-timeout'), ['int'])),
                            ('access_group', (YLeaf(YType.str, 'access-group'), ['str'])),
                            ('query_max_response_time', (YLeaf(YType.uint32, 'query-max-response-time'), ['int'])),
                            ('version', (YLeaf(YType.uint32, 'version'), ['int'])),
                            ('router_enable', (YLeaf(YType.boolean, 'router-enable'), ['bool'])),
                            ('query_interval', (YLeaf(YType.uint32, 'query-interval'), ['int'])),
                        ])
                        self.interface_name = None
                        self.query_timeout = None
                        self.access_group = None
                        self.query_max_response_time = None
                        self.version = None
                        self.router_enable = None
                        self.query_interval = None

                        self.join_groups = None
                        self._children_name_map["join_groups"] = "join-groups"

                        self.static_group_group_addresses = Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses()
                        self.static_group_group_addresses.parent = self
                        self._children_name_map["static_group_group_addresses"] = "static-group-group-addresses"

                        self.maximum_groups_per_interface_oor = None
                        self._children_name_map["maximum_groups_per_interface_oor"] = "maximum-groups-per-interface-oor"

                        self.explicit_tracking = None
                        self._children_name_map["explicit_tracking"] = "explicit-tracking"
                        self._segment_path = lambda: "interface" + "[interface-name='" + str(self.interface_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mld.Vrfs.Vrf.Interfaces.Interface, ['interface_name', 'query_timeout', 'access_group', 'query_max_response_time', 'version', 'router_enable', 'query_interval'], name, value)


                    class JoinGroups(Entity):
                        """
                        IGMP join multicast group
                        
                        .. attribute:: join_group
                        
                        	IP group address and optional source address to include
                        	**type**\: list of  		 :py:class:`JoinGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.Vrfs.Vrf.Interfaces.Interface.JoinGroups.JoinGroup>`
                        
                        .. attribute:: join_group_source_address
                        
                        	IP group address and optional source address to include
                        	**type**\: list of  		 :py:class:`JoinGroupSourceAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.Vrfs.Vrf.Interfaces.Interface.JoinGroups.JoinGroupSourceAddress>`
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2017-10-15'

                        def __init__(self):
                            super(Mld.Vrfs.Vrf.Interfaces.Interface.JoinGroups, self).__init__()

                            self.yang_name = "join-groups"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("join-group", ("join_group", Mld.Vrfs.Vrf.Interfaces.Interface.JoinGroups.JoinGroup)), ("join-group-source-address", ("join_group_source_address", Mld.Vrfs.Vrf.Interfaces.Interface.JoinGroups.JoinGroupSourceAddress))])
                            self.is_presence_container = True
                            self._leafs = OrderedDict()

                            self.join_group = YList(self)
                            self.join_group_source_address = YList(self)
                            self._segment_path = lambda: "join-groups"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mld.Vrfs.Vrf.Interfaces.Interface.JoinGroups, [], name, value)


                        class JoinGroup(Entity):
                            """
                            IP group address and optional source address
                            to include
                            
                            .. attribute:: group_address  (key)
                            
                            	IP group address
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            		**type**\: str
                            
                            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: mode
                            
                            	Filter mode
                            	**type**\:  :py:class:`IgmpFilter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.IgmpFilter>`
                            
                            	**mandatory**\: True
                            
                            

                            """

                            _prefix = 'ipv4-igmp-cfg'
                            _revision = '2017-10-15'

                            def __init__(self):
                                super(Mld.Vrfs.Vrf.Interfaces.Interface.JoinGroups.JoinGroup, self).__init__()

                                self.yang_name = "join-group"
                                self.yang_parent_name = "join-groups"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['group_address']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('group_address', (YLeaf(YType.str, 'group-address'), ['str','str'])),
                                    ('mode', (YLeaf(YType.enumeration, 'mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'IgmpFilter', '')])),
                                ])
                                self.group_address = None
                                self.mode = None
                                self._segment_path = lambda: "join-group" + "[group-address='" + str(self.group_address) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mld.Vrfs.Vrf.Interfaces.Interface.JoinGroups.JoinGroup, ['group_address', 'mode'], name, value)


                        class JoinGroupSourceAddress(Entity):
                            """
                            IP group address and optional source address
                            to include
                            
                            .. attribute:: group_address  (key)
                            
                            	IP group address
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            		**type**\: str
                            
                            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: source_address  (key)
                            
                            	Optional IP source address
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            		**type**\: str
                            
                            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: mode
                            
                            	Filter mode
                            	**type**\:  :py:class:`IgmpFilter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.IgmpFilter>`
                            
                            	**mandatory**\: True
                            
                            

                            """

                            _prefix = 'ipv4-igmp-cfg'
                            _revision = '2017-10-15'

                            def __init__(self):
                                super(Mld.Vrfs.Vrf.Interfaces.Interface.JoinGroups.JoinGroupSourceAddress, self).__init__()

                                self.yang_name = "join-group-source-address"
                                self.yang_parent_name = "join-groups"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['group_address','source_address']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('group_address', (YLeaf(YType.str, 'group-address'), ['str','str'])),
                                    ('source_address', (YLeaf(YType.str, 'source-address'), ['str','str'])),
                                    ('mode', (YLeaf(YType.enumeration, 'mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'IgmpFilter', '')])),
                                ])
                                self.group_address = None
                                self.source_address = None
                                self.mode = None
                                self._segment_path = lambda: "join-group-source-address" + "[group-address='" + str(self.group_address) + "']" + "[source-address='" + str(self.source_address) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mld.Vrfs.Vrf.Interfaces.Interface.JoinGroups.JoinGroupSourceAddress, ['group_address', 'source_address', 'mode'], name, value)


                    class StaticGroupGroupAddresses(Entity):
                        """
                        IGMP static multicast group
                        
                        .. attribute:: static_group_group_address
                        
                        	IP group address and optional source address to include
                        	**type**\: list of  		 :py:class:`StaticGroupGroupAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddress>`
                        
                        .. attribute:: static_group_group_address_source_address
                        
                        	IP group address and optional source address to include
                        	**type**\: list of  		 :py:class:`StaticGroupGroupAddressSourceAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddress>`
                        
                        .. attribute:: static_group_group_address_source_address_source_address_mask
                        
                        	IP group address and optional source address to include
                        	**type**\: list of  		 :py:class:`StaticGroupGroupAddressSourceAddressSourceAddressMask <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddressSourceAddressMask>`
                        
                        .. attribute:: static_group_group_address_group_address_mask
                        
                        	IP group address and optional source address to include
                        	**type**\: list of  		 :py:class:`StaticGroupGroupAddressGroupAddressMask <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMask>`
                        
                        .. attribute:: static_group_group_address_group_address_mask_source_address
                        
                        	IP group address and optional source address to include
                        	**type**\: list of  		 :py:class:`StaticGroupGroupAddressGroupAddressMaskSourceAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddress>`
                        
                        .. attribute:: static_group_group_address_group_address_mask_source_address_source_address_mask
                        
                        	IP group address and optional source address to include
                        	**type**\: list of  		 :py:class:`StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask>`
                        
                        

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2017-10-15'

                        def __init__(self):
                            super(Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses, self).__init__()

                            self.yang_name = "static-group-group-addresses"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("static-group-group-address", ("static_group_group_address", Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddress)), ("static-group-group-address-source-address", ("static_group_group_address_source_address", Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddress)), ("static-group-group-address-source-address-source-address-mask", ("static_group_group_address_source_address_source_address_mask", Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddressSourceAddressMask)), ("static-group-group-address-group-address-mask", ("static_group_group_address_group_address_mask", Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMask)), ("static-group-group-address-group-address-mask-source-address", ("static_group_group_address_group_address_mask_source_address", Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddress)), ("static-group-group-address-group-address-mask-source-address-source-address-mask", ("static_group_group_address_group_address_mask_source_address_source_address_mask", Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask))])
                            self._leafs = OrderedDict()

                            self.static_group_group_address = YList(self)
                            self.static_group_group_address_source_address = YList(self)
                            self.static_group_group_address_source_address_source_address_mask = YList(self)
                            self.static_group_group_address_group_address_mask = YList(self)
                            self.static_group_group_address_group_address_mask_source_address = YList(self)
                            self.static_group_group_address_group_address_mask_source_address_source_address_mask = YList(self)
                            self._segment_path = lambda: "static-group-group-addresses"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses, [], name, value)


                        class StaticGroupGroupAddress(Entity):
                            """
                            IP group address and optional source address
                            to include
                            
                            .. attribute:: group_address  (key)
                            
                            	IP group address
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            		**type**\: str
                            
                            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: group_count
                            
                            	Number of groups to join (do not set without GroupAddressMask)
                            	**type**\: int
                            
                            	**range:** 1..512
                            
                            	**default value**\: 1
                            
                            .. attribute:: source_count
                            
                            	Number of sources to join (do not set without SourceAddressMask)
                            	**type**\: int
                            
                            	**range:** 1..512
                            
                            	**default value**\: 1
                            
                            .. attribute:: suppress_report
                            
                            	Suppress reports
                            	**type**\: bool
                            
                            	**default value**\: false
                            
                            

                            """

                            _prefix = 'ipv4-igmp-cfg'
                            _revision = '2017-10-15'

                            def __init__(self):
                                super(Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddress, self).__init__()

                                self.yang_name = "static-group-group-address"
                                self.yang_parent_name = "static-group-group-addresses"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['group_address']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('group_address', (YLeaf(YType.str, 'group-address'), ['str','str'])),
                                    ('group_count', (YLeaf(YType.uint32, 'group-count'), ['int'])),
                                    ('source_count', (YLeaf(YType.uint32, 'source-count'), ['int'])),
                                    ('suppress_report', (YLeaf(YType.boolean, 'suppress-report'), ['bool'])),
                                ])
                                self.group_address = None
                                self.group_count = None
                                self.source_count = None
                                self.suppress_report = None
                                self._segment_path = lambda: "static-group-group-address" + "[group-address='" + str(self.group_address) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddress, ['group_address', 'group_count', 'source_count', 'suppress_report'], name, value)


                        class StaticGroupGroupAddressSourceAddress(Entity):
                            """
                            IP group address and optional source address
                            to include
                            
                            .. attribute:: group_address  (key)
                            
                            	IP group address
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            		**type**\: str
                            
                            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: source_address  (key)
                            
                            	IP source address
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            		**type**\: str
                            
                            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: group_count
                            
                            	Number of groups to join (do not set without GroupAddressMask)
                            	**type**\: int
                            
                            	**range:** 1..512
                            
                            	**default value**\: 1
                            
                            .. attribute:: source_count
                            
                            	Number of sources to join (do not set without SourceAddressMask)
                            	**type**\: int
                            
                            	**range:** 1..512
                            
                            	**default value**\: 1
                            
                            .. attribute:: suppress_report
                            
                            	Suppress reports
                            	**type**\: bool
                            
                            	**default value**\: false
                            
                            

                            """

                            _prefix = 'ipv4-igmp-cfg'
                            _revision = '2017-10-15'

                            def __init__(self):
                                super(Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddress, self).__init__()

                                self.yang_name = "static-group-group-address-source-address"
                                self.yang_parent_name = "static-group-group-addresses"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['group_address','source_address']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('group_address', (YLeaf(YType.str, 'group-address'), ['str','str'])),
                                    ('source_address', (YLeaf(YType.str, 'source-address'), ['str','str'])),
                                    ('group_count', (YLeaf(YType.uint32, 'group-count'), ['int'])),
                                    ('source_count', (YLeaf(YType.uint32, 'source-count'), ['int'])),
                                    ('suppress_report', (YLeaf(YType.boolean, 'suppress-report'), ['bool'])),
                                ])
                                self.group_address = None
                                self.source_address = None
                                self.group_count = None
                                self.source_count = None
                                self.suppress_report = None
                                self._segment_path = lambda: "static-group-group-address-source-address" + "[group-address='" + str(self.group_address) + "']" + "[source-address='" + str(self.source_address) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddress, ['group_address', 'source_address', 'group_count', 'source_count', 'suppress_report'], name, value)


                        class StaticGroupGroupAddressSourceAddressSourceAddressMask(Entity):
                            """
                            IP group address and optional source address
                            to include
                            
                            .. attribute:: group_address  (key)
                            
                            	IP group address
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            		**type**\: str
                            
                            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: source_address  (key)
                            
                            	IP source address
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            		**type**\: str
                            
                            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: source_address_mask  (key)
                            
                            	Mask for Source Address
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            		**type**\: str
                            
                            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: group_count
                            
                            	Number of groups to join (do not set without GroupAddressMask)
                            	**type**\: int
                            
                            	**range:** 1..512
                            
                            	**default value**\: 1
                            
                            .. attribute:: source_count
                            
                            	Number of sources to join (do not set without SourceAddressMask)
                            	**type**\: int
                            
                            	**range:** 1..512
                            
                            	**default value**\: 1
                            
                            .. attribute:: suppress_report
                            
                            	Suppress reports
                            	**type**\: bool
                            
                            	**default value**\: false
                            
                            

                            """

                            _prefix = 'ipv4-igmp-cfg'
                            _revision = '2017-10-15'

                            def __init__(self):
                                super(Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddressSourceAddressMask, self).__init__()

                                self.yang_name = "static-group-group-address-source-address-source-address-mask"
                                self.yang_parent_name = "static-group-group-addresses"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['group_address','source_address','source_address_mask']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('group_address', (YLeaf(YType.str, 'group-address'), ['str','str'])),
                                    ('source_address', (YLeaf(YType.str, 'source-address'), ['str','str'])),
                                    ('source_address_mask', (YLeaf(YType.str, 'source-address-mask'), ['str','str'])),
                                    ('group_count', (YLeaf(YType.uint32, 'group-count'), ['int'])),
                                    ('source_count', (YLeaf(YType.uint32, 'source-count'), ['int'])),
                                    ('suppress_report', (YLeaf(YType.boolean, 'suppress-report'), ['bool'])),
                                ])
                                self.group_address = None
                                self.source_address = None
                                self.source_address_mask = None
                                self.group_count = None
                                self.source_count = None
                                self.suppress_report = None
                                self._segment_path = lambda: "static-group-group-address-source-address-source-address-mask" + "[group-address='" + str(self.group_address) + "']" + "[source-address='" + str(self.source_address) + "']" + "[source-address-mask='" + str(self.source_address_mask) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddressSourceAddressMask, ['group_address', 'source_address', 'source_address_mask', 'group_count', 'source_count', 'suppress_report'], name, value)


                        class StaticGroupGroupAddressGroupAddressMask(Entity):
                            """
                            IP group address and optional source address
                            to include
                            
                            .. attribute:: group_address  (key)
                            
                            	IP group address
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            		**type**\: str
                            
                            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: group_address_mask  (key)
                            
                            	Mask for Group Address
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            		**type**\: str
                            
                            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: group_count
                            
                            	Number of groups to join (do not set without GroupAddressMask)
                            	**type**\: int
                            
                            	**range:** 1..512
                            
                            	**default value**\: 1
                            
                            .. attribute:: source_count
                            
                            	Number of sources to join (do not set without SourceAddressMask)
                            	**type**\: int
                            
                            	**range:** 1..512
                            
                            	**default value**\: 1
                            
                            .. attribute:: suppress_report
                            
                            	Suppress reports
                            	**type**\: bool
                            
                            	**default value**\: false
                            
                            

                            """

                            _prefix = 'ipv4-igmp-cfg'
                            _revision = '2017-10-15'

                            def __init__(self):
                                super(Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMask, self).__init__()

                                self.yang_name = "static-group-group-address-group-address-mask"
                                self.yang_parent_name = "static-group-group-addresses"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['group_address','group_address_mask']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('group_address', (YLeaf(YType.str, 'group-address'), ['str','str'])),
                                    ('group_address_mask', (YLeaf(YType.str, 'group-address-mask'), ['str','str'])),
                                    ('group_count', (YLeaf(YType.uint32, 'group-count'), ['int'])),
                                    ('source_count', (YLeaf(YType.uint32, 'source-count'), ['int'])),
                                    ('suppress_report', (YLeaf(YType.boolean, 'suppress-report'), ['bool'])),
                                ])
                                self.group_address = None
                                self.group_address_mask = None
                                self.group_count = None
                                self.source_count = None
                                self.suppress_report = None
                                self._segment_path = lambda: "static-group-group-address-group-address-mask" + "[group-address='" + str(self.group_address) + "']" + "[group-address-mask='" + str(self.group_address_mask) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMask, ['group_address', 'group_address_mask', 'group_count', 'source_count', 'suppress_report'], name, value)


                        class StaticGroupGroupAddressGroupAddressMaskSourceAddress(Entity):
                            """
                            IP group address and optional source address
                            to include
                            
                            .. attribute:: group_address  (key)
                            
                            	IP group address
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            		**type**\: str
                            
                            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: group_address_mask  (key)
                            
                            	Mask for Group Address
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            		**type**\: str
                            
                            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: source_address  (key)
                            
                            	IP source address
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            		**type**\: str
                            
                            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: group_count
                            
                            	Number of groups to join (do not set without GroupAddressMask)
                            	**type**\: int
                            
                            	**range:** 1..512
                            
                            	**default value**\: 1
                            
                            .. attribute:: source_count
                            
                            	Number of sources to join (do not set without SourceAddressMask)
                            	**type**\: int
                            
                            	**range:** 1..512
                            
                            	**default value**\: 1
                            
                            .. attribute:: suppress_report
                            
                            	Suppress reports
                            	**type**\: bool
                            
                            	**default value**\: false
                            
                            

                            """

                            _prefix = 'ipv4-igmp-cfg'
                            _revision = '2017-10-15'

                            def __init__(self):
                                super(Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddress, self).__init__()

                                self.yang_name = "static-group-group-address-group-address-mask-source-address"
                                self.yang_parent_name = "static-group-group-addresses"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['group_address','group_address_mask','source_address']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('group_address', (YLeaf(YType.str, 'group-address'), ['str','str'])),
                                    ('group_address_mask', (YLeaf(YType.str, 'group-address-mask'), ['str','str'])),
                                    ('source_address', (YLeaf(YType.str, 'source-address'), ['str','str'])),
                                    ('group_count', (YLeaf(YType.uint32, 'group-count'), ['int'])),
                                    ('source_count', (YLeaf(YType.uint32, 'source-count'), ['int'])),
                                    ('suppress_report', (YLeaf(YType.boolean, 'suppress-report'), ['bool'])),
                                ])
                                self.group_address = None
                                self.group_address_mask = None
                                self.source_address = None
                                self.group_count = None
                                self.source_count = None
                                self.suppress_report = None
                                self._segment_path = lambda: "static-group-group-address-group-address-mask-source-address" + "[group-address='" + str(self.group_address) + "']" + "[group-address-mask='" + str(self.group_address_mask) + "']" + "[source-address='" + str(self.source_address) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddress, ['group_address', 'group_address_mask', 'source_address', 'group_count', 'source_count', 'suppress_report'], name, value)


                        class StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask(Entity):
                            """
                            IP group address and optional source address
                            to include
                            
                            .. attribute:: group_address  (key)
                            
                            	IP group address
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            		**type**\: str
                            
                            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: group_address_mask  (key)
                            
                            	Mask for Group Address
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            		**type**\: str
                            
                            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: source_address  (key)
                            
                            	IP source address
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            		**type**\: str
                            
                            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: source_address_mask  (key)
                            
                            	Mask for Source Address
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            		**type**\: str
                            
                            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: group_count
                            
                            	Number of groups to join (do not set without GroupAddressMask)
                            	**type**\: int
                            
                            	**range:** 1..512
                            
                            	**default value**\: 1
                            
                            .. attribute:: source_count
                            
                            	Number of sources to join (do not set without SourceAddressMask)
                            	**type**\: int
                            
                            	**range:** 1..512
                            
                            	**default value**\: 1
                            
                            .. attribute:: suppress_report
                            
                            	Suppress reports
                            	**type**\: bool
                            
                            	**default value**\: false
                            
                            

                            """

                            _prefix = 'ipv4-igmp-cfg'
                            _revision = '2017-10-15'

                            def __init__(self):
                                super(Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask, self).__init__()

                                self.yang_name = "static-group-group-address-group-address-mask-source-address-source-address-mask"
                                self.yang_parent_name = "static-group-group-addresses"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['group_address','group_address_mask','source_address','source_address_mask']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('group_address', (YLeaf(YType.str, 'group-address'), ['str','str'])),
                                    ('group_address_mask', (YLeaf(YType.str, 'group-address-mask'), ['str','str'])),
                                    ('source_address', (YLeaf(YType.str, 'source-address'), ['str','str'])),
                                    ('source_address_mask', (YLeaf(YType.str, 'source-address-mask'), ['str','str'])),
                                    ('group_count', (YLeaf(YType.uint32, 'group-count'), ['int'])),
                                    ('source_count', (YLeaf(YType.uint32, 'source-count'), ['int'])),
                                    ('suppress_report', (YLeaf(YType.boolean, 'suppress-report'), ['bool'])),
                                ])
                                self.group_address = None
                                self.group_address_mask = None
                                self.source_address = None
                                self.source_address_mask = None
                                self.group_count = None
                                self.source_count = None
                                self.suppress_report = None
                                self._segment_path = lambda: "static-group-group-address-group-address-mask-source-address-source-address-mask" + "[group-address='" + str(self.group_address) + "']" + "[group-address-mask='" + str(self.group_address_mask) + "']" + "[source-address='" + str(self.source_address) + "']" + "[source-address-mask='" + str(self.source_address_mask) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask, ['group_address', 'group_address_mask', 'source_address', 'source_address_mask', 'group_count', 'source_count', 'suppress_report'], name, value)


                    class MaximumGroupsPerInterfaceOor(Entity):
                        """
                        Configure maximum number of groups accepted per
                        interface by this router
                        
                        .. attribute:: maximum_groups
                        
                        	Maximum number of groups accepted per interface by this router
                        	**type**\: int
                        
                        	**range:** 1..40000
                        
                        	**mandatory**\: True
                        
                        .. attribute:: warning_threshold
                        
                        	 WarningThreshold for number of groups accepted per interface by this router
                        	**type**\: int
                        
                        	**range:** 1..40000
                        
                        	**default value**\: 25000
                        
                        .. attribute:: access_list_name
                        
                        	Access\-list to account for
                        	**type**\: str
                        
                        	**length:** 1..64
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2017-10-15'

                        def __init__(self):
                            super(Mld.Vrfs.Vrf.Interfaces.Interface.MaximumGroupsPerInterfaceOor, self).__init__()

                            self.yang_name = "maximum-groups-per-interface-oor"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('maximum_groups', (YLeaf(YType.uint32, 'maximum-groups'), ['int'])),
                                ('warning_threshold', (YLeaf(YType.uint32, 'warning-threshold'), ['int'])),
                                ('access_list_name', (YLeaf(YType.str, 'access-list-name'), ['str'])),
                            ])
                            self.maximum_groups = None
                            self.warning_threshold = None
                            self.access_list_name = None
                            self._segment_path = lambda: "maximum-groups-per-interface-oor"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mld.Vrfs.Vrf.Interfaces.Interface.MaximumGroupsPerInterfaceOor, ['maximum_groups', 'warning_threshold', 'access_list_name'], name, value)


                    class ExplicitTracking(Entity):
                        """
                        IGMPv3 explicit host tracking
                        
                        .. attribute:: enable
                        
                        	Enabled or disabled, when value is TRUE or FALSE respectively
                        	**type**\: bool
                        
                        	**mandatory**\: True
                        
                        .. attribute:: access_list_name
                        
                        	Access list specifying tracking group range
                        	**type**\: str
                        
                        	**length:** 1..64
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2017-10-15'

                        def __init__(self):
                            super(Mld.Vrfs.Vrf.Interfaces.Interface.ExplicitTracking, self).__init__()

                            self.yang_name = "explicit-tracking"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('enable', (YLeaf(YType.boolean, 'enable'), ['bool'])),
                                ('access_list_name', (YLeaf(YType.str, 'access-list-name'), ['str'])),
                            ])
                            self.enable = None
                            self.access_list_name = None
                            self._segment_path = lambda: "explicit-tracking"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mld.Vrfs.Vrf.Interfaces.Interface.ExplicitTracking, ['enable', 'access_list_name'], name, value)


    class DefaultContext(Entity):
        """
        Default Context
        
        .. attribute:: nsf
        
        	Configure NSF specific options
        	**type**\:  :py:class:`Nsf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext.Nsf>`
        
        .. attribute:: unicast_qos_adjust
        
        	Configure IGMP QoS shapers for subscriber interfaces
        	**type**\:  :py:class:`UnicastQosAdjust <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext.UnicastQosAdjust>`
        
        .. attribute:: accounting
        
        	Configure IGMP accounting for logging join/leave records
        	**type**\:  :py:class:`Accounting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext.Accounting>`
        
        .. attribute:: traffic
        
        	Configure IGMP Traffic variables
        	**type**\:  :py:class:`Traffic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext.Traffic>`
        
        .. attribute:: inheritable_defaults
        
        	Inheritable Defaults
        	**type**\:  :py:class:`InheritableDefaults <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext.InheritableDefaults>`
        
        .. attribute:: ssm_access_groups
        
        	IGMP Source specific mode
        	**type**\:  :py:class:`SsmAccessGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext.SsmAccessGroups>`
        
        .. attribute:: maximum
        
        	Configure IGMP State Limits
        	**type**\:  :py:class:`Maximum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext.Maximum>`
        
        .. attribute:: ssmdns_query_group
        
        	Enable SSM mapping using DNS Query
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: interfaces
        
        	Interface\-level configuration
        	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext.Interfaces>`
        
        .. attribute:: robustness
        
        	Configure IGMP Robustness variable
        	**type**\: int
        
        	**range:** 2..10
        
        	**default value**\: 2
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'ipv4-igmp-cfg'
        _revision = '2017-10-15'

        def __init__(self):
            super(Mld.DefaultContext, self).__init__()

            self.yang_name = "default-context"
            self.yang_parent_name = "mld"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("nsf", ("nsf", Mld.DefaultContext.Nsf)), ("unicast-qos-adjust", ("unicast_qos_adjust", Mld.DefaultContext.UnicastQosAdjust)), ("accounting", ("accounting", Mld.DefaultContext.Accounting)), ("traffic", ("traffic", Mld.DefaultContext.Traffic)), ("inheritable-defaults", ("inheritable_defaults", Mld.DefaultContext.InheritableDefaults)), ("ssm-access-groups", ("ssm_access_groups", Mld.DefaultContext.SsmAccessGroups)), ("maximum", ("maximum", Mld.DefaultContext.Maximum)), ("interfaces", ("interfaces", Mld.DefaultContext.Interfaces))])
            self.is_presence_container = True
            self._leafs = OrderedDict([
                ('ssmdns_query_group', (YLeaf(YType.empty, 'ssmdns-query-group'), ['Empty'])),
                ('robustness', (YLeaf(YType.uint32, 'robustness'), ['int'])),
            ])
            self.ssmdns_query_group = None
            self.robustness = None

            self.nsf = Mld.DefaultContext.Nsf()
            self.nsf.parent = self
            self._children_name_map["nsf"] = "nsf"

            self.unicast_qos_adjust = Mld.DefaultContext.UnicastQosAdjust()
            self.unicast_qos_adjust.parent = self
            self._children_name_map["unicast_qos_adjust"] = "unicast-qos-adjust"

            self.accounting = Mld.DefaultContext.Accounting()
            self.accounting.parent = self
            self._children_name_map["accounting"] = "accounting"

            self.traffic = Mld.DefaultContext.Traffic()
            self.traffic.parent = self
            self._children_name_map["traffic"] = "traffic"

            self.inheritable_defaults = Mld.DefaultContext.InheritableDefaults()
            self.inheritable_defaults.parent = self
            self._children_name_map["inheritable_defaults"] = "inheritable-defaults"

            self.ssm_access_groups = Mld.DefaultContext.SsmAccessGroups()
            self.ssm_access_groups.parent = self
            self._children_name_map["ssm_access_groups"] = "ssm-access-groups"

            self.maximum = Mld.DefaultContext.Maximum()
            self.maximum.parent = self
            self._children_name_map["maximum"] = "maximum"

            self.interfaces = Mld.DefaultContext.Interfaces()
            self.interfaces.parent = self
            self._children_name_map["interfaces"] = "interfaces"
            self._segment_path = lambda: "default-context"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-igmp-cfg:mld/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Mld.DefaultContext, ['ssmdns_query_group', 'robustness'], name, value)


        class Nsf(Entity):
            """
            Configure NSF specific options
            
            .. attribute:: lifetime
            
            	Maximum time for IGMP NSF mode in seconds
            	**type**\: int
            
            	**range:** 10..3600
            
            	**units**\: second
            
            	**default value**\: 60
            
            

            """

            _prefix = 'ipv4-igmp-cfg'
            _revision = '2017-10-15'

            def __init__(self):
                super(Mld.DefaultContext.Nsf, self).__init__()

                self.yang_name = "nsf"
                self.yang_parent_name = "default-context"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('lifetime', (YLeaf(YType.uint32, 'lifetime'), ['int'])),
                ])
                self.lifetime = None
                self._segment_path = lambda: "nsf"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-igmp-cfg:mld/default-context/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Mld.DefaultContext.Nsf, ['lifetime'], name, value)


        class UnicastQosAdjust(Entity):
            """
            Configure IGMP QoS shapers for subscriber
            interfaces
            
            .. attribute:: download_interval
            
            	Configure the QoS download interval (in milliseconds)
            	**type**\: int
            
            	**range:** 10..500
            
            	**units**\: millisecond
            
            	**default value**\: 100
            
            .. attribute:: adjustment_delay
            
            	Configure the QoS delay before programming (in seconds)
            	**type**\: int
            
            	**range:** 0..10
            
            	**units**\: second
            
            	**default value**\: 1
            
            .. attribute:: hold_off
            
            	Configure the QoS hold off time (in seconds)
            	**type**\: int
            
            	**range:** 5..1800
            
            	**units**\: second
            
            	**default value**\: 180
            
            

            """

            _prefix = 'ipv4-igmp-cfg'
            _revision = '2017-10-15'

            def __init__(self):
                super(Mld.DefaultContext.UnicastQosAdjust, self).__init__()

                self.yang_name = "unicast-qos-adjust"
                self.yang_parent_name = "default-context"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('download_interval', (YLeaf(YType.uint32, 'download-interval'), ['int'])),
                    ('adjustment_delay', (YLeaf(YType.uint32, 'adjustment-delay'), ['int'])),
                    ('hold_off', (YLeaf(YType.uint32, 'hold-off'), ['int'])),
                ])
                self.download_interval = None
                self.adjustment_delay = None
                self.hold_off = None
                self._segment_path = lambda: "unicast-qos-adjust"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-igmp-cfg:mld/default-context/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Mld.DefaultContext.UnicastQosAdjust, ['download_interval', 'adjustment_delay', 'hold_off'], name, value)


        class Accounting(Entity):
            """
            Configure IGMP accounting for logging
            join/leave records
            
            .. attribute:: max_history
            
            	Configure IGMP accounting Maximum History setting
            	**type**\: int
            
            	**range:** 1..365
            
            	**units**\: day
            
            	**default value**\: 1
            
            

            """

            _prefix = 'ipv4-igmp-cfg'
            _revision = '2017-10-15'

            def __init__(self):
                super(Mld.DefaultContext.Accounting, self).__init__()

                self.yang_name = "accounting"
                self.yang_parent_name = "default-context"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('max_history', (YLeaf(YType.uint32, 'max-history'), ['int'])),
                ])
                self.max_history = None
                self._segment_path = lambda: "accounting"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-igmp-cfg:mld/default-context/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Mld.DefaultContext.Accounting, ['max_history'], name, value)


        class Traffic(Entity):
            """
            Configure IGMP Traffic variables
            
            .. attribute:: profile
            
            	Configure the route\-policy profile
            	**type**\: str
            
            	**length:** 1..64
            
            

            """

            _prefix = 'ipv4-igmp-cfg'
            _revision = '2017-10-15'

            def __init__(self):
                super(Mld.DefaultContext.Traffic, self).__init__()

                self.yang_name = "traffic"
                self.yang_parent_name = "default-context"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('profile', (YLeaf(YType.str, 'profile'), ['str'])),
                ])
                self.profile = None
                self._segment_path = lambda: "traffic"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-igmp-cfg:mld/default-context/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Mld.DefaultContext.Traffic, ['profile'], name, value)


        class InheritableDefaults(Entity):
            """
            Inheritable Defaults
            
            .. attribute:: maximum_groups_per_interface_oor
            
            	Configure maximum number of groups accepted per interface by this router
            	**type**\:  :py:class:`MaximumGroupsPerInterfaceOor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext.InheritableDefaults.MaximumGroupsPerInterfaceOor>`
            
            	**presence node**\: True
            
            .. attribute:: query_timeout
            
            	IGMP previous querier timeout
            	**type**\: int
            
            	**range:** 60..300
            
            	**units**\: second
            
            .. attribute:: access_group
            
            	Access list specifying access group range
            	**type**\: str
            
            	**length:** 1..64
            
            .. attribute:: query_max_response_time
            
            	Query response value in seconds
            	**type**\: int
            
            	**range:** 1..12
            
            	**units**\: second
            
            	**default value**\: 10
            
            .. attribute:: version
            
            	Version number
            	**type**\: int
            
            	**range:** 1..3
            
            	**default value**\: 3
            
            .. attribute:: router_enable
            
            	Enabled or disabled, when value is TRUE or FALSE respectively
            	**type**\: bool
            
            	**default value**\: true
            
            .. attribute:: query_interval
            
            	Query interval in seconds
            	**type**\: int
            
            	**range:** 1..3600
            
            	**units**\: second
            
            	**default value**\: 60
            
            .. attribute:: explicit_tracking
            
            	IGMPv3 explicit host tracking
            	**type**\:  :py:class:`ExplicitTracking <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext.InheritableDefaults.ExplicitTracking>`
            
            	**presence node**\: True
            
            

            """

            _prefix = 'ipv4-igmp-cfg'
            _revision = '2017-10-15'

            def __init__(self):
                super(Mld.DefaultContext.InheritableDefaults, self).__init__()

                self.yang_name = "inheritable-defaults"
                self.yang_parent_name = "default-context"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("maximum-groups-per-interface-oor", ("maximum_groups_per_interface_oor", Mld.DefaultContext.InheritableDefaults.MaximumGroupsPerInterfaceOor)), ("explicit-tracking", ("explicit_tracking", Mld.DefaultContext.InheritableDefaults.ExplicitTracking))])
                self._leafs = OrderedDict([
                    ('query_timeout', (YLeaf(YType.uint32, 'query-timeout'), ['int'])),
                    ('access_group', (YLeaf(YType.str, 'access-group'), ['str'])),
                    ('query_max_response_time', (YLeaf(YType.uint32, 'query-max-response-time'), ['int'])),
                    ('version', (YLeaf(YType.uint32, 'version'), ['int'])),
                    ('router_enable', (YLeaf(YType.boolean, 'router-enable'), ['bool'])),
                    ('query_interval', (YLeaf(YType.uint32, 'query-interval'), ['int'])),
                ])
                self.query_timeout = None
                self.access_group = None
                self.query_max_response_time = None
                self.version = None
                self.router_enable = None
                self.query_interval = None

                self.maximum_groups_per_interface_oor = None
                self._children_name_map["maximum_groups_per_interface_oor"] = "maximum-groups-per-interface-oor"

                self.explicit_tracking = None
                self._children_name_map["explicit_tracking"] = "explicit-tracking"
                self._segment_path = lambda: "inheritable-defaults"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-igmp-cfg:mld/default-context/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Mld.DefaultContext.InheritableDefaults, ['query_timeout', 'access_group', 'query_max_response_time', 'version', 'router_enable', 'query_interval'], name, value)


            class MaximumGroupsPerInterfaceOor(Entity):
                """
                Configure maximum number of groups accepted per
                interface by this router
                
                .. attribute:: maximum_groups
                
                	Maximum number of groups accepted per interface by this router
                	**type**\: int
                
                	**range:** 1..40000
                
                	**mandatory**\: True
                
                .. attribute:: warning_threshold
                
                	 WarningThreshold for number of groups accepted per interface by this router
                	**type**\: int
                
                	**range:** 1..40000
                
                	**default value**\: 25000
                
                .. attribute:: access_list_name
                
                	Access\-list to account for
                	**type**\: str
                
                	**length:** 1..64
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'ipv4-igmp-cfg'
                _revision = '2017-10-15'

                def __init__(self):
                    super(Mld.DefaultContext.InheritableDefaults.MaximumGroupsPerInterfaceOor, self).__init__()

                    self.yang_name = "maximum-groups-per-interface-oor"
                    self.yang_parent_name = "inheritable-defaults"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self.is_presence_container = True
                    self._leafs = OrderedDict([
                        ('maximum_groups', (YLeaf(YType.uint32, 'maximum-groups'), ['int'])),
                        ('warning_threshold', (YLeaf(YType.uint32, 'warning-threshold'), ['int'])),
                        ('access_list_name', (YLeaf(YType.str, 'access-list-name'), ['str'])),
                    ])
                    self.maximum_groups = None
                    self.warning_threshold = None
                    self.access_list_name = None
                    self._segment_path = lambda: "maximum-groups-per-interface-oor"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-igmp-cfg:mld/default-context/inheritable-defaults/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Mld.DefaultContext.InheritableDefaults.MaximumGroupsPerInterfaceOor, ['maximum_groups', 'warning_threshold', 'access_list_name'], name, value)


            class ExplicitTracking(Entity):
                """
                IGMPv3 explicit host tracking
                
                .. attribute:: enable
                
                	Enabled or disabled, when value is TRUE or FALSE respectively
                	**type**\: bool
                
                	**mandatory**\: True
                
                .. attribute:: access_list_name
                
                	Access list specifying tracking group range
                	**type**\: str
                
                	**length:** 1..64
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'ipv4-igmp-cfg'
                _revision = '2017-10-15'

                def __init__(self):
                    super(Mld.DefaultContext.InheritableDefaults.ExplicitTracking, self).__init__()

                    self.yang_name = "explicit-tracking"
                    self.yang_parent_name = "inheritable-defaults"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self.is_presence_container = True
                    self._leafs = OrderedDict([
                        ('enable', (YLeaf(YType.boolean, 'enable'), ['bool'])),
                        ('access_list_name', (YLeaf(YType.str, 'access-list-name'), ['str'])),
                    ])
                    self.enable = None
                    self.access_list_name = None
                    self._segment_path = lambda: "explicit-tracking"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-igmp-cfg:mld/default-context/inheritable-defaults/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Mld.DefaultContext.InheritableDefaults.ExplicitTracking, ['enable', 'access_list_name'], name, value)


        class SsmAccessGroups(Entity):
            """
            IGMP Source specific mode
            
            .. attribute:: ssm_access_group
            
            	SSM static Access Group
            	**type**\: list of  		 :py:class:`SsmAccessGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext.SsmAccessGroups.SsmAccessGroup>`
            
            

            """

            _prefix = 'ipv4-igmp-cfg'
            _revision = '2017-10-15'

            def __init__(self):
                super(Mld.DefaultContext.SsmAccessGroups, self).__init__()

                self.yang_name = "ssm-access-groups"
                self.yang_parent_name = "default-context"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("ssm-access-group", ("ssm_access_group", Mld.DefaultContext.SsmAccessGroups.SsmAccessGroup))])
                self._leafs = OrderedDict()

                self.ssm_access_group = YList(self)
                self._segment_path = lambda: "ssm-access-groups"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-igmp-cfg:mld/default-context/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Mld.DefaultContext.SsmAccessGroups, [], name, value)


            class SsmAccessGroup(Entity):
                """
                SSM static Access Group
                
                .. attribute:: source_address  (key)
                
                	IP source address
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: access_list_name
                
                	Access list specifying access group
                	**type**\: str
                
                	**length:** 1..64
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'ipv4-igmp-cfg'
                _revision = '2017-10-15'

                def __init__(self):
                    super(Mld.DefaultContext.SsmAccessGroups.SsmAccessGroup, self).__init__()

                    self.yang_name = "ssm-access-group"
                    self.yang_parent_name = "ssm-access-groups"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['source_address']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('source_address', (YLeaf(YType.str, 'source-address'), ['str','str'])),
                        ('access_list_name', (YLeaf(YType.str, 'access-list-name'), ['str'])),
                    ])
                    self.source_address = None
                    self.access_list_name = None
                    self._segment_path = lambda: "ssm-access-group" + "[source-address='" + str(self.source_address) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-igmp-cfg:mld/default-context/ssm-access-groups/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Mld.DefaultContext.SsmAccessGroups.SsmAccessGroup, ['source_address', 'access_list_name'], name, value)


        class Maximum(Entity):
            """
            Configure IGMP State Limits
            
            .. attribute:: maximum_groups
            
            	Configure maximum number of groups accepted by this router
            	**type**\: int
            
            	**range:** 1..75000
            
            	**default value**\: 50000
            
            

            """

            _prefix = 'ipv4-igmp-cfg'
            _revision = '2017-10-15'

            def __init__(self):
                super(Mld.DefaultContext.Maximum, self).__init__()

                self.yang_name = "maximum"
                self.yang_parent_name = "default-context"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('maximum_groups', (YLeaf(YType.uint32, 'maximum-groups'), ['int'])),
                ])
                self.maximum_groups = None
                self._segment_path = lambda: "maximum"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-igmp-cfg:mld/default-context/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Mld.DefaultContext.Maximum, ['maximum_groups'], name, value)


        class Interfaces(Entity):
            """
            Interface\-level configuration
            
            .. attribute:: interface
            
            	The name of the interface
            	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext.Interfaces.Interface>`
            
            

            """

            _prefix = 'ipv4-igmp-cfg'
            _revision = '2017-10-15'

            def __init__(self):
                super(Mld.DefaultContext.Interfaces, self).__init__()

                self.yang_name = "interfaces"
                self.yang_parent_name = "default-context"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("interface", ("interface", Mld.DefaultContext.Interfaces.Interface))])
                self._leafs = OrderedDict()

                self.interface = YList(self)
                self._segment_path = lambda: "interfaces"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-igmp-cfg:mld/default-context/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Mld.DefaultContext.Interfaces, [], name, value)


            class Interface(Entity):
                """
                The name of the interface
                
                .. attribute:: interface_name  (key)
                
                	Name of the interface
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                .. attribute:: join_groups
                
                	IGMP join multicast group
                	**type**\:  :py:class:`JoinGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext.Interfaces.Interface.JoinGroups>`
                
                	**presence node**\: True
                
                .. attribute:: static_group_group_addresses
                
                	IGMP static multicast group
                	**type**\:  :py:class:`StaticGroupGroupAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses>`
                
                .. attribute:: maximum_groups_per_interface_oor
                
                	Configure maximum number of groups accepted per interface by this router
                	**type**\:  :py:class:`MaximumGroupsPerInterfaceOor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext.Interfaces.Interface.MaximumGroupsPerInterfaceOor>`
                
                	**presence node**\: True
                
                .. attribute:: query_timeout
                
                	IGMP previous querier timeout
                	**type**\: int
                
                	**range:** 60..300
                
                	**units**\: second
                
                .. attribute:: access_group
                
                	Access list specifying access group range
                	**type**\: str
                
                	**length:** 1..64
                
                .. attribute:: query_max_response_time
                
                	Query response value in seconds
                	**type**\: int
                
                	**range:** 1..12
                
                	**units**\: second
                
                	**default value**\: 10
                
                .. attribute:: version
                
                	Version number
                	**type**\: int
                
                	**range:** 1..3
                
                	**default value**\: 3
                
                .. attribute:: router_enable
                
                	Enabled or disabled, when value is TRUE or FALSE respectively
                	**type**\: bool
                
                	**default value**\: true
                
                .. attribute:: query_interval
                
                	Query interval in seconds
                	**type**\: int
                
                	**range:** 1..3600
                
                	**units**\: second
                
                	**default value**\: 60
                
                .. attribute:: explicit_tracking
                
                	IGMPv3 explicit host tracking
                	**type**\:  :py:class:`ExplicitTracking <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext.Interfaces.Interface.ExplicitTracking>`
                
                	**presence node**\: True
                
                

                """

                _prefix = 'ipv4-igmp-cfg'
                _revision = '2017-10-15'

                def __init__(self):
                    super(Mld.DefaultContext.Interfaces.Interface, self).__init__()

                    self.yang_name = "interface"
                    self.yang_parent_name = "interfaces"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['interface_name']
                    self._child_classes = OrderedDict([("join-groups", ("join_groups", Mld.DefaultContext.Interfaces.Interface.JoinGroups)), ("static-group-group-addresses", ("static_group_group_addresses", Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses)), ("maximum-groups-per-interface-oor", ("maximum_groups_per_interface_oor", Mld.DefaultContext.Interfaces.Interface.MaximumGroupsPerInterfaceOor)), ("explicit-tracking", ("explicit_tracking", Mld.DefaultContext.Interfaces.Interface.ExplicitTracking))])
                    self._leafs = OrderedDict([
                        ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                        ('query_timeout', (YLeaf(YType.uint32, 'query-timeout'), ['int'])),
                        ('access_group', (YLeaf(YType.str, 'access-group'), ['str'])),
                        ('query_max_response_time', (YLeaf(YType.uint32, 'query-max-response-time'), ['int'])),
                        ('version', (YLeaf(YType.uint32, 'version'), ['int'])),
                        ('router_enable', (YLeaf(YType.boolean, 'router-enable'), ['bool'])),
                        ('query_interval', (YLeaf(YType.uint32, 'query-interval'), ['int'])),
                    ])
                    self.interface_name = None
                    self.query_timeout = None
                    self.access_group = None
                    self.query_max_response_time = None
                    self.version = None
                    self.router_enable = None
                    self.query_interval = None

                    self.join_groups = None
                    self._children_name_map["join_groups"] = "join-groups"

                    self.static_group_group_addresses = Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses()
                    self.static_group_group_addresses.parent = self
                    self._children_name_map["static_group_group_addresses"] = "static-group-group-addresses"

                    self.maximum_groups_per_interface_oor = None
                    self._children_name_map["maximum_groups_per_interface_oor"] = "maximum-groups-per-interface-oor"

                    self.explicit_tracking = None
                    self._children_name_map["explicit_tracking"] = "explicit-tracking"
                    self._segment_path = lambda: "interface" + "[interface-name='" + str(self.interface_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-igmp-cfg:mld/default-context/interfaces/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Mld.DefaultContext.Interfaces.Interface, ['interface_name', 'query_timeout', 'access_group', 'query_max_response_time', 'version', 'router_enable', 'query_interval'], name, value)


                class JoinGroups(Entity):
                    """
                    IGMP join multicast group
                    
                    .. attribute:: join_group
                    
                    	IP group address and optional source address to include
                    	**type**\: list of  		 :py:class:`JoinGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext.Interfaces.Interface.JoinGroups.JoinGroup>`
                    
                    .. attribute:: join_group_source_address
                    
                    	IP group address and optional source address to include
                    	**type**\: list of  		 :py:class:`JoinGroupSourceAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext.Interfaces.Interface.JoinGroups.JoinGroupSourceAddress>`
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-igmp-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Mld.DefaultContext.Interfaces.Interface.JoinGroups, self).__init__()

                        self.yang_name = "join-groups"
                        self.yang_parent_name = "interface"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("join-group", ("join_group", Mld.DefaultContext.Interfaces.Interface.JoinGroups.JoinGroup)), ("join-group-source-address", ("join_group_source_address", Mld.DefaultContext.Interfaces.Interface.JoinGroups.JoinGroupSourceAddress))])
                        self.is_presence_container = True
                        self._leafs = OrderedDict()

                        self.join_group = YList(self)
                        self.join_group_source_address = YList(self)
                        self._segment_path = lambda: "join-groups"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mld.DefaultContext.Interfaces.Interface.JoinGroups, [], name, value)


                    class JoinGroup(Entity):
                        """
                        IP group address and optional source address
                        to include
                        
                        .. attribute:: group_address  (key)
                        
                        	IP group address
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: mode
                        
                        	Filter mode
                        	**type**\:  :py:class:`IgmpFilter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.IgmpFilter>`
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2017-10-15'

                        def __init__(self):
                            super(Mld.DefaultContext.Interfaces.Interface.JoinGroups.JoinGroup, self).__init__()

                            self.yang_name = "join-group"
                            self.yang_parent_name = "join-groups"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['group_address']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('group_address', (YLeaf(YType.str, 'group-address'), ['str','str'])),
                                ('mode', (YLeaf(YType.enumeration, 'mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'IgmpFilter', '')])),
                            ])
                            self.group_address = None
                            self.mode = None
                            self._segment_path = lambda: "join-group" + "[group-address='" + str(self.group_address) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mld.DefaultContext.Interfaces.Interface.JoinGroups.JoinGroup, ['group_address', 'mode'], name, value)


                    class JoinGroupSourceAddress(Entity):
                        """
                        IP group address and optional source address
                        to include
                        
                        .. attribute:: group_address  (key)
                        
                        	IP group address
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: source_address  (key)
                        
                        	Optional IP source address
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: mode
                        
                        	Filter mode
                        	**type**\:  :py:class:`IgmpFilter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.IgmpFilter>`
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2017-10-15'

                        def __init__(self):
                            super(Mld.DefaultContext.Interfaces.Interface.JoinGroups.JoinGroupSourceAddress, self).__init__()

                            self.yang_name = "join-group-source-address"
                            self.yang_parent_name = "join-groups"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['group_address','source_address']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('group_address', (YLeaf(YType.str, 'group-address'), ['str','str'])),
                                ('source_address', (YLeaf(YType.str, 'source-address'), ['str','str'])),
                                ('mode', (YLeaf(YType.enumeration, 'mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'IgmpFilter', '')])),
                            ])
                            self.group_address = None
                            self.source_address = None
                            self.mode = None
                            self._segment_path = lambda: "join-group-source-address" + "[group-address='" + str(self.group_address) + "']" + "[source-address='" + str(self.source_address) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mld.DefaultContext.Interfaces.Interface.JoinGroups.JoinGroupSourceAddress, ['group_address', 'source_address', 'mode'], name, value)


                class StaticGroupGroupAddresses(Entity):
                    """
                    IGMP static multicast group
                    
                    .. attribute:: static_group_group_address
                    
                    	IP group address and optional source address to include
                    	**type**\: list of  		 :py:class:`StaticGroupGroupAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddress>`
                    
                    .. attribute:: static_group_group_address_source_address
                    
                    	IP group address and optional source address to include
                    	**type**\: list of  		 :py:class:`StaticGroupGroupAddressSourceAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddress>`
                    
                    .. attribute:: static_group_group_address_source_address_source_address_mask
                    
                    	IP group address and optional source address to include
                    	**type**\: list of  		 :py:class:`StaticGroupGroupAddressSourceAddressSourceAddressMask <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddressSourceAddressMask>`
                    
                    .. attribute:: static_group_group_address_group_address_mask
                    
                    	IP group address and optional source address to include
                    	**type**\: list of  		 :py:class:`StaticGroupGroupAddressGroupAddressMask <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMask>`
                    
                    .. attribute:: static_group_group_address_group_address_mask_source_address
                    
                    	IP group address and optional source address to include
                    	**type**\: list of  		 :py:class:`StaticGroupGroupAddressGroupAddressMaskSourceAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddress>`
                    
                    .. attribute:: static_group_group_address_group_address_mask_source_address_source_address_mask
                    
                    	IP group address and optional source address to include
                    	**type**\: list of  		 :py:class:`StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask>`
                    
                    

                    """

                    _prefix = 'ipv4-igmp-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses, self).__init__()

                        self.yang_name = "static-group-group-addresses"
                        self.yang_parent_name = "interface"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("static-group-group-address", ("static_group_group_address", Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddress)), ("static-group-group-address-source-address", ("static_group_group_address_source_address", Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddress)), ("static-group-group-address-source-address-source-address-mask", ("static_group_group_address_source_address_source_address_mask", Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddressSourceAddressMask)), ("static-group-group-address-group-address-mask", ("static_group_group_address_group_address_mask", Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMask)), ("static-group-group-address-group-address-mask-source-address", ("static_group_group_address_group_address_mask_source_address", Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddress)), ("static-group-group-address-group-address-mask-source-address-source-address-mask", ("static_group_group_address_group_address_mask_source_address_source_address_mask", Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask))])
                        self._leafs = OrderedDict()

                        self.static_group_group_address = YList(self)
                        self.static_group_group_address_source_address = YList(self)
                        self.static_group_group_address_source_address_source_address_mask = YList(self)
                        self.static_group_group_address_group_address_mask = YList(self)
                        self.static_group_group_address_group_address_mask_source_address = YList(self)
                        self.static_group_group_address_group_address_mask_source_address_source_address_mask = YList(self)
                        self._segment_path = lambda: "static-group-group-addresses"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses, [], name, value)


                    class StaticGroupGroupAddress(Entity):
                        """
                        IP group address and optional source address
                        to include
                        
                        .. attribute:: group_address  (key)
                        
                        	IP group address
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: group_count
                        
                        	Number of groups to join (do not set without GroupAddressMask)
                        	**type**\: int
                        
                        	**range:** 1..512
                        
                        	**default value**\: 1
                        
                        .. attribute:: source_count
                        
                        	Number of sources to join (do not set without SourceAddressMask)
                        	**type**\: int
                        
                        	**range:** 1..512
                        
                        	**default value**\: 1
                        
                        .. attribute:: suppress_report
                        
                        	Suppress reports
                        	**type**\: bool
                        
                        	**default value**\: false
                        
                        

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2017-10-15'

                        def __init__(self):
                            super(Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddress, self).__init__()

                            self.yang_name = "static-group-group-address"
                            self.yang_parent_name = "static-group-group-addresses"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['group_address']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('group_address', (YLeaf(YType.str, 'group-address'), ['str','str'])),
                                ('group_count', (YLeaf(YType.uint32, 'group-count'), ['int'])),
                                ('source_count', (YLeaf(YType.uint32, 'source-count'), ['int'])),
                                ('suppress_report', (YLeaf(YType.boolean, 'suppress-report'), ['bool'])),
                            ])
                            self.group_address = None
                            self.group_count = None
                            self.source_count = None
                            self.suppress_report = None
                            self._segment_path = lambda: "static-group-group-address" + "[group-address='" + str(self.group_address) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddress, ['group_address', 'group_count', 'source_count', 'suppress_report'], name, value)


                    class StaticGroupGroupAddressSourceAddress(Entity):
                        """
                        IP group address and optional source address
                        to include
                        
                        .. attribute:: group_address  (key)
                        
                        	IP group address
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: source_address  (key)
                        
                        	IP source address
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: group_count
                        
                        	Number of groups to join (do not set without GroupAddressMask)
                        	**type**\: int
                        
                        	**range:** 1..512
                        
                        	**default value**\: 1
                        
                        .. attribute:: source_count
                        
                        	Number of sources to join (do not set without SourceAddressMask)
                        	**type**\: int
                        
                        	**range:** 1..512
                        
                        	**default value**\: 1
                        
                        .. attribute:: suppress_report
                        
                        	Suppress reports
                        	**type**\: bool
                        
                        	**default value**\: false
                        
                        

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2017-10-15'

                        def __init__(self):
                            super(Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddress, self).__init__()

                            self.yang_name = "static-group-group-address-source-address"
                            self.yang_parent_name = "static-group-group-addresses"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['group_address','source_address']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('group_address', (YLeaf(YType.str, 'group-address'), ['str','str'])),
                                ('source_address', (YLeaf(YType.str, 'source-address'), ['str','str'])),
                                ('group_count', (YLeaf(YType.uint32, 'group-count'), ['int'])),
                                ('source_count', (YLeaf(YType.uint32, 'source-count'), ['int'])),
                                ('suppress_report', (YLeaf(YType.boolean, 'suppress-report'), ['bool'])),
                            ])
                            self.group_address = None
                            self.source_address = None
                            self.group_count = None
                            self.source_count = None
                            self.suppress_report = None
                            self._segment_path = lambda: "static-group-group-address-source-address" + "[group-address='" + str(self.group_address) + "']" + "[source-address='" + str(self.source_address) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddress, ['group_address', 'source_address', 'group_count', 'source_count', 'suppress_report'], name, value)


                    class StaticGroupGroupAddressSourceAddressSourceAddressMask(Entity):
                        """
                        IP group address and optional source address
                        to include
                        
                        .. attribute:: group_address  (key)
                        
                        	IP group address
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: source_address  (key)
                        
                        	IP source address
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: source_address_mask  (key)
                        
                        	Mask for Source Address
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: group_count
                        
                        	Number of groups to join (do not set without GroupAddressMask)
                        	**type**\: int
                        
                        	**range:** 1..512
                        
                        	**default value**\: 1
                        
                        .. attribute:: source_count
                        
                        	Number of sources to join (do not set without SourceAddressMask)
                        	**type**\: int
                        
                        	**range:** 1..512
                        
                        	**default value**\: 1
                        
                        .. attribute:: suppress_report
                        
                        	Suppress reports
                        	**type**\: bool
                        
                        	**default value**\: false
                        
                        

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2017-10-15'

                        def __init__(self):
                            super(Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddressSourceAddressMask, self).__init__()

                            self.yang_name = "static-group-group-address-source-address-source-address-mask"
                            self.yang_parent_name = "static-group-group-addresses"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['group_address','source_address','source_address_mask']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('group_address', (YLeaf(YType.str, 'group-address'), ['str','str'])),
                                ('source_address', (YLeaf(YType.str, 'source-address'), ['str','str'])),
                                ('source_address_mask', (YLeaf(YType.str, 'source-address-mask'), ['str','str'])),
                                ('group_count', (YLeaf(YType.uint32, 'group-count'), ['int'])),
                                ('source_count', (YLeaf(YType.uint32, 'source-count'), ['int'])),
                                ('suppress_report', (YLeaf(YType.boolean, 'suppress-report'), ['bool'])),
                            ])
                            self.group_address = None
                            self.source_address = None
                            self.source_address_mask = None
                            self.group_count = None
                            self.source_count = None
                            self.suppress_report = None
                            self._segment_path = lambda: "static-group-group-address-source-address-source-address-mask" + "[group-address='" + str(self.group_address) + "']" + "[source-address='" + str(self.source_address) + "']" + "[source-address-mask='" + str(self.source_address_mask) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddressSourceAddressMask, ['group_address', 'source_address', 'source_address_mask', 'group_count', 'source_count', 'suppress_report'], name, value)


                    class StaticGroupGroupAddressGroupAddressMask(Entity):
                        """
                        IP group address and optional source address
                        to include
                        
                        .. attribute:: group_address  (key)
                        
                        	IP group address
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: group_address_mask  (key)
                        
                        	Mask for Group Address
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: group_count
                        
                        	Number of groups to join (do not set without GroupAddressMask)
                        	**type**\: int
                        
                        	**range:** 1..512
                        
                        	**default value**\: 1
                        
                        .. attribute:: source_count
                        
                        	Number of sources to join (do not set without SourceAddressMask)
                        	**type**\: int
                        
                        	**range:** 1..512
                        
                        	**default value**\: 1
                        
                        .. attribute:: suppress_report
                        
                        	Suppress reports
                        	**type**\: bool
                        
                        	**default value**\: false
                        
                        

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2017-10-15'

                        def __init__(self):
                            super(Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMask, self).__init__()

                            self.yang_name = "static-group-group-address-group-address-mask"
                            self.yang_parent_name = "static-group-group-addresses"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['group_address','group_address_mask']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('group_address', (YLeaf(YType.str, 'group-address'), ['str','str'])),
                                ('group_address_mask', (YLeaf(YType.str, 'group-address-mask'), ['str','str'])),
                                ('group_count', (YLeaf(YType.uint32, 'group-count'), ['int'])),
                                ('source_count', (YLeaf(YType.uint32, 'source-count'), ['int'])),
                                ('suppress_report', (YLeaf(YType.boolean, 'suppress-report'), ['bool'])),
                            ])
                            self.group_address = None
                            self.group_address_mask = None
                            self.group_count = None
                            self.source_count = None
                            self.suppress_report = None
                            self._segment_path = lambda: "static-group-group-address-group-address-mask" + "[group-address='" + str(self.group_address) + "']" + "[group-address-mask='" + str(self.group_address_mask) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMask, ['group_address', 'group_address_mask', 'group_count', 'source_count', 'suppress_report'], name, value)


                    class StaticGroupGroupAddressGroupAddressMaskSourceAddress(Entity):
                        """
                        IP group address and optional source address
                        to include
                        
                        .. attribute:: group_address  (key)
                        
                        	IP group address
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: group_address_mask  (key)
                        
                        	Mask for Group Address
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: source_address  (key)
                        
                        	IP source address
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: group_count
                        
                        	Number of groups to join (do not set without GroupAddressMask)
                        	**type**\: int
                        
                        	**range:** 1..512
                        
                        	**default value**\: 1
                        
                        .. attribute:: source_count
                        
                        	Number of sources to join (do not set without SourceAddressMask)
                        	**type**\: int
                        
                        	**range:** 1..512
                        
                        	**default value**\: 1
                        
                        .. attribute:: suppress_report
                        
                        	Suppress reports
                        	**type**\: bool
                        
                        	**default value**\: false
                        
                        

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2017-10-15'

                        def __init__(self):
                            super(Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddress, self).__init__()

                            self.yang_name = "static-group-group-address-group-address-mask-source-address"
                            self.yang_parent_name = "static-group-group-addresses"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['group_address','group_address_mask','source_address']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('group_address', (YLeaf(YType.str, 'group-address'), ['str','str'])),
                                ('group_address_mask', (YLeaf(YType.str, 'group-address-mask'), ['str','str'])),
                                ('source_address', (YLeaf(YType.str, 'source-address'), ['str','str'])),
                                ('group_count', (YLeaf(YType.uint32, 'group-count'), ['int'])),
                                ('source_count', (YLeaf(YType.uint32, 'source-count'), ['int'])),
                                ('suppress_report', (YLeaf(YType.boolean, 'suppress-report'), ['bool'])),
                            ])
                            self.group_address = None
                            self.group_address_mask = None
                            self.source_address = None
                            self.group_count = None
                            self.source_count = None
                            self.suppress_report = None
                            self._segment_path = lambda: "static-group-group-address-group-address-mask-source-address" + "[group-address='" + str(self.group_address) + "']" + "[group-address-mask='" + str(self.group_address_mask) + "']" + "[source-address='" + str(self.source_address) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddress, ['group_address', 'group_address_mask', 'source_address', 'group_count', 'source_count', 'suppress_report'], name, value)


                    class StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask(Entity):
                        """
                        IP group address and optional source address
                        to include
                        
                        .. attribute:: group_address  (key)
                        
                        	IP group address
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: group_address_mask  (key)
                        
                        	Mask for Group Address
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: source_address  (key)
                        
                        	IP source address
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: source_address_mask  (key)
                        
                        	Mask for Source Address
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: group_count
                        
                        	Number of groups to join (do not set without GroupAddressMask)
                        	**type**\: int
                        
                        	**range:** 1..512
                        
                        	**default value**\: 1
                        
                        .. attribute:: source_count
                        
                        	Number of sources to join (do not set without SourceAddressMask)
                        	**type**\: int
                        
                        	**range:** 1..512
                        
                        	**default value**\: 1
                        
                        .. attribute:: suppress_report
                        
                        	Suppress reports
                        	**type**\: bool
                        
                        	**default value**\: false
                        
                        

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2017-10-15'

                        def __init__(self):
                            super(Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask, self).__init__()

                            self.yang_name = "static-group-group-address-group-address-mask-source-address-source-address-mask"
                            self.yang_parent_name = "static-group-group-addresses"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['group_address','group_address_mask','source_address','source_address_mask']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('group_address', (YLeaf(YType.str, 'group-address'), ['str','str'])),
                                ('group_address_mask', (YLeaf(YType.str, 'group-address-mask'), ['str','str'])),
                                ('source_address', (YLeaf(YType.str, 'source-address'), ['str','str'])),
                                ('source_address_mask', (YLeaf(YType.str, 'source-address-mask'), ['str','str'])),
                                ('group_count', (YLeaf(YType.uint32, 'group-count'), ['int'])),
                                ('source_count', (YLeaf(YType.uint32, 'source-count'), ['int'])),
                                ('suppress_report', (YLeaf(YType.boolean, 'suppress-report'), ['bool'])),
                            ])
                            self.group_address = None
                            self.group_address_mask = None
                            self.source_address = None
                            self.source_address_mask = None
                            self.group_count = None
                            self.source_count = None
                            self.suppress_report = None
                            self._segment_path = lambda: "static-group-group-address-group-address-mask-source-address-source-address-mask" + "[group-address='" + str(self.group_address) + "']" + "[group-address-mask='" + str(self.group_address_mask) + "']" + "[source-address='" + str(self.source_address) + "']" + "[source-address-mask='" + str(self.source_address_mask) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask, ['group_address', 'group_address_mask', 'source_address', 'source_address_mask', 'group_count', 'source_count', 'suppress_report'], name, value)


                class MaximumGroupsPerInterfaceOor(Entity):
                    """
                    Configure maximum number of groups accepted per
                    interface by this router
                    
                    .. attribute:: maximum_groups
                    
                    	Maximum number of groups accepted per interface by this router
                    	**type**\: int
                    
                    	**range:** 1..40000
                    
                    	**mandatory**\: True
                    
                    .. attribute:: warning_threshold
                    
                    	 WarningThreshold for number of groups accepted per interface by this router
                    	**type**\: int
                    
                    	**range:** 1..40000
                    
                    	**default value**\: 25000
                    
                    .. attribute:: access_list_name
                    
                    	Access\-list to account for
                    	**type**\: str
                    
                    	**length:** 1..64
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-igmp-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Mld.DefaultContext.Interfaces.Interface.MaximumGroupsPerInterfaceOor, self).__init__()

                        self.yang_name = "maximum-groups-per-interface-oor"
                        self.yang_parent_name = "interface"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('maximum_groups', (YLeaf(YType.uint32, 'maximum-groups'), ['int'])),
                            ('warning_threshold', (YLeaf(YType.uint32, 'warning-threshold'), ['int'])),
                            ('access_list_name', (YLeaf(YType.str, 'access-list-name'), ['str'])),
                        ])
                        self.maximum_groups = None
                        self.warning_threshold = None
                        self.access_list_name = None
                        self._segment_path = lambda: "maximum-groups-per-interface-oor"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mld.DefaultContext.Interfaces.Interface.MaximumGroupsPerInterfaceOor, ['maximum_groups', 'warning_threshold', 'access_list_name'], name, value)


                class ExplicitTracking(Entity):
                    """
                    IGMPv3 explicit host tracking
                    
                    .. attribute:: enable
                    
                    	Enabled or disabled, when value is TRUE or FALSE respectively
                    	**type**\: bool
                    
                    	**mandatory**\: True
                    
                    .. attribute:: access_list_name
                    
                    	Access list specifying tracking group range
                    	**type**\: str
                    
                    	**length:** 1..64
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-igmp-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Mld.DefaultContext.Interfaces.Interface.ExplicitTracking, self).__init__()

                        self.yang_name = "explicit-tracking"
                        self.yang_parent_name = "interface"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('enable', (YLeaf(YType.boolean, 'enable'), ['bool'])),
                            ('access_list_name', (YLeaf(YType.str, 'access-list-name'), ['str'])),
                        ])
                        self.enable = None
                        self.access_list_name = None
                        self._segment_path = lambda: "explicit-tracking"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mld.DefaultContext.Interfaces.Interface.ExplicitTracking, ['enable', 'access_list_name'], name, value)

    def clone_ptr(self):
        self._top_entity = Mld()
        return self._top_entity

