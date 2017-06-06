""" Cisco_IOS_XR_ipv4_igmp_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv4\-igmp package configuration.

This module contains definitions
for the following management objects\:
  igmp\: IGMPconfiguration
  amt\: amt
  mld\: mld

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class IgmpFilterEnum(Enum):
    """
    IgmpFilterEnum

    Igmp filter

    .. data:: include = 0

    	Include

    .. data:: exclude = 1

    	Exclude

    .. data:: star_g = 2

    	StarG

    """

    include = 0

    exclude = 1

    star_g = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
        return meta._meta_table['IgmpFilterEnum']



class Igmp(object):
    """
    IGMPconfiguration
    
    .. attribute:: default_context
    
    	Default Context
    	**type**\:   :py:class:`DefaultContext <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext>`
    
    	**presence node**\: True
    
    .. attribute:: vrfs
    
    	VRF related configuration
    	**type**\:   :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.Vrfs>`
    
    .. attribute:: _is_presence
    
    	Is present if this instance represents presence container else not
    	**type**\: bool
    
    

    This class is a :ref:`presence class<presence-class>`

    """

    _prefix = 'ipv4-igmp-cfg'
    _revision = '2016-10-10'

    def __init__(self):
        self._is_presence = True
        self.default_context = None
        self.vrfs = Igmp.Vrfs()
        self.vrfs.parent = self


    class Vrfs(object):
        """
        VRF related configuration
        
        .. attribute:: vrf
        
        	Configuration for a particular vrf
        	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.Vrfs.Vrf>`
        
        

        """

        _prefix = 'ipv4-igmp-cfg'
        _revision = '2016-10-10'

        def __init__(self):
            self.parent = None
            self.vrf = YList()
            self.vrf.parent = self
            self.vrf.name = 'vrf'


        class Vrf(object):
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
                self.parent = None
                self.vrf_name = None
                self.inheritable_defaults = Igmp.Vrfs.Vrf.InheritableDefaults()
                self.inheritable_defaults.parent = self
                self.interfaces = Igmp.Vrfs.Vrf.Interfaces()
                self.interfaces.parent = self
                self.maximum = Igmp.Vrfs.Vrf.Maximum()
                self.maximum.parent = self
                self.robustness = None
                self.ssm_access_groups = Igmp.Vrfs.Vrf.SsmAccessGroups()
                self.ssm_access_groups.parent = self
                self.ssmdns_query_group = None
                self.traffic = Igmp.Vrfs.Vrf.Traffic()
                self.traffic.parent = self


            class Traffic(object):
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
                    self.parent = None
                    self.profile = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-igmp-cfg:traffic'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.profile is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                    return meta._meta_table['Igmp.Vrfs.Vrf.Traffic']['meta_info']


            class InheritableDefaults(object):
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
                    self.parent = None
                    self.access_group = None
                    self.explicit_tracking = None
                    self.maximum_groups_per_interface_oor = None
                    self.query_interval = None
                    self.query_max_response_time = None
                    self.query_timeout = None
                    self.router_enable = None
                    self.version = None


                class MaximumGroupsPerInterfaceOor(object):
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
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-igmp-cfg'
                    _revision = '2016-10-10'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.access_list_name = None
                        self.maximum_groups = None
                        self.warning_threshold = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-igmp-cfg:maximum-groups-per-interface-oor'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self._is_presence:
                            return True
                        if self.access_list_name is not None:
                            return True

                        if self.maximum_groups is not None:
                            return True

                        if self.warning_threshold is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                        return meta._meta_table['Igmp.Vrfs.Vrf.InheritableDefaults.MaximumGroupsPerInterfaceOor']['meta_info']


                class ExplicitTracking(object):
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
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-igmp-cfg'
                    _revision = '2016-10-10'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.access_list_name = None
                        self.enable = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-igmp-cfg:explicit-tracking'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self._is_presence:
                            return True
                        if self.access_list_name is not None:
                            return True

                        if self.enable is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                        return meta._meta_table['Igmp.Vrfs.Vrf.InheritableDefaults.ExplicitTracking']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-igmp-cfg:inheritable-defaults'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.access_group is not None:
                        return True

                    if self.explicit_tracking is not None and self.explicit_tracking._has_data():
                        return True

                    if self.maximum_groups_per_interface_oor is not None and self.maximum_groups_per_interface_oor._has_data():
                        return True

                    if self.query_interval is not None:
                        return True

                    if self.query_max_response_time is not None:
                        return True

                    if self.query_timeout is not None:
                        return True

                    if self.router_enable is not None:
                        return True

                    if self.version is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                    return meta._meta_table['Igmp.Vrfs.Vrf.InheritableDefaults']['meta_info']


            class SsmAccessGroups(object):
                """
                IGMP Source specific mode
                
                .. attribute:: ssm_access_group
                
                	SSM static Access Group
                	**type**\: list of    :py:class:`SsmAccessGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.Vrfs.Vrf.SsmAccessGroups.SsmAccessGroup>`
                
                

                """

                _prefix = 'ipv4-igmp-cfg'
                _revision = '2016-10-10'

                def __init__(self):
                    self.parent = None
                    self.ssm_access_group = YList()
                    self.ssm_access_group.parent = self
                    self.ssm_access_group.name = 'ssm_access_group'


                class SsmAccessGroup(object):
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
                        self.parent = None
                        self.source_address = None
                        self.access_list_name = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.source_address is None:
                            raise YPYModelError('Key property source_address is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-igmp-cfg:ssm-access-group[Cisco-IOS-XR-ipv4-igmp-cfg:source-address = ' + str(self.source_address) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.source_address is not None:
                            return True

                        if self.access_list_name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                        return meta._meta_table['Igmp.Vrfs.Vrf.SsmAccessGroups.SsmAccessGroup']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-igmp-cfg:ssm-access-groups'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.ssm_access_group is not None:
                        for child_ref in self.ssm_access_group:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                    return meta._meta_table['Igmp.Vrfs.Vrf.SsmAccessGroups']['meta_info']


            class Maximum(object):
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
                    self.parent = None
                    self.maximum_groups = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-igmp-cfg:maximum'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.maximum_groups is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                    return meta._meta_table['Igmp.Vrfs.Vrf.Maximum']['meta_info']


            class Interfaces(object):
                """
                Interface\-level configuration
                
                .. attribute:: interface
                
                	The name of the interface
                	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.Vrfs.Vrf.Interfaces.Interface>`
                
                

                """

                _prefix = 'ipv4-igmp-cfg'
                _revision = '2016-10-10'

                def __init__(self):
                    self.parent = None
                    self.interface = YList()
                    self.interface.parent = self
                    self.interface.name = 'interface'


                class Interface(object):
                    """
                    The name of the interface
                    
                    .. attribute:: interface_name  <key>
                    
                    	Name of the interface
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
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
                        self.parent = None
                        self.interface_name = None
                        self.access_group = None
                        self.explicit_tracking = None
                        self.join_groups = None
                        self.maximum_groups_per_interface_oor = None
                        self.query_interval = None
                        self.query_max_response_time = None
                        self.query_timeout = None
                        self.router_enable = None
                        self.static_group_group_addresses = Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses()
                        self.static_group_group_addresses.parent = self
                        self.version = None


                    class JoinGroups(object):
                        """
                        IGMP join multicast group
                        
                        .. attribute:: join_group
                        
                        	IP group address and optional source address to include
                        	**type**\: list of    :py:class:`JoinGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.Vrfs.Vrf.Interfaces.Interface.JoinGroups.JoinGroup>`
                        
                        .. attribute:: join_group_source_address
                        
                        	IP group address and optional source address to include
                        	**type**\: list of    :py:class:`JoinGroupSourceAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.Vrfs.Vrf.Interfaces.Interface.JoinGroups.JoinGroupSourceAddress>`
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2016-10-10'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.join_group = YList()
                            self.join_group.parent = self
                            self.join_group.name = 'join_group'
                            self.join_group_source_address = YList()
                            self.join_group_source_address.parent = self
                            self.join_group_source_address.name = 'join_group_source_address'


                        class JoinGroup(object):
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
                            	**type**\:   :py:class:`IgmpFilterEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.IgmpFilterEnum>`
                            
                            	**mandatory**\: True
                            
                            

                            """

                            _prefix = 'ipv4-igmp-cfg'
                            _revision = '2016-10-10'

                            def __init__(self):
                                self.parent = None
                                self.group_address = None
                                self.mode = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.group_address is None:
                                    raise YPYModelError('Key property group_address is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-igmp-cfg:join-group[Cisco-IOS-XR-ipv4-igmp-cfg:group-address = ' + str(self.group_address) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.group_address is not None:
                                    return True

                                if self.mode is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                                return meta._meta_table['Igmp.Vrfs.Vrf.Interfaces.Interface.JoinGroups.JoinGroup']['meta_info']


                        class JoinGroupSourceAddress(object):
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
                            	**type**\:   :py:class:`IgmpFilterEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.IgmpFilterEnum>`
                            
                            	**mandatory**\: True
                            
                            

                            """

                            _prefix = 'ipv4-igmp-cfg'
                            _revision = '2016-10-10'

                            def __init__(self):
                                self.parent = None
                                self.group_address = None
                                self.source_address = None
                                self.mode = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.group_address is None:
                                    raise YPYModelError('Key property group_address is None')
                                if self.source_address is None:
                                    raise YPYModelError('Key property source_address is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-igmp-cfg:join-group-source-address[Cisco-IOS-XR-ipv4-igmp-cfg:group-address = ' + str(self.group_address) + '][Cisco-IOS-XR-ipv4-igmp-cfg:source-address = ' + str(self.source_address) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.group_address is not None:
                                    return True

                                if self.source_address is not None:
                                    return True

                                if self.mode is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                                return meta._meta_table['Igmp.Vrfs.Vrf.Interfaces.Interface.JoinGroups.JoinGroupSourceAddress']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-igmp-cfg:join-groups'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.join_group is not None:
                                for child_ref in self.join_group:
                                    if child_ref._has_data():
                                        return True

                            if self.join_group_source_address is not None:
                                for child_ref in self.join_group_source_address:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                            return meta._meta_table['Igmp.Vrfs.Vrf.Interfaces.Interface.JoinGroups']['meta_info']


                    class StaticGroupGroupAddresses(object):
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
                            self.parent = None
                            self.static_group_group_address = YList()
                            self.static_group_group_address.parent = self
                            self.static_group_group_address.name = 'static_group_group_address'
                            self.static_group_group_address_group_address_mask = YList()
                            self.static_group_group_address_group_address_mask.parent = self
                            self.static_group_group_address_group_address_mask.name = 'static_group_group_address_group_address_mask'
                            self.static_group_group_address_group_address_mask_source_address = YList()
                            self.static_group_group_address_group_address_mask_source_address.parent = self
                            self.static_group_group_address_group_address_mask_source_address.name = 'static_group_group_address_group_address_mask_source_address'
                            self.static_group_group_address_group_address_mask_source_address_source_address_mask = YList()
                            self.static_group_group_address_group_address_mask_source_address_source_address_mask.parent = self
                            self.static_group_group_address_group_address_mask_source_address_source_address_mask.name = 'static_group_group_address_group_address_mask_source_address_source_address_mask'
                            self.static_group_group_address_source_address = YList()
                            self.static_group_group_address_source_address.parent = self
                            self.static_group_group_address_source_address.name = 'static_group_group_address_source_address'
                            self.static_group_group_address_source_address_source_address_mask = YList()
                            self.static_group_group_address_source_address_source_address_mask.parent = self
                            self.static_group_group_address_source_address_source_address_mask.name = 'static_group_group_address_source_address_source_address_mask'


                        class StaticGroupGroupAddress(object):
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
                                self.parent = None
                                self.group_address = None
                                self.group_count = None
                                self.source_count = None
                                self.suppress_report = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.group_address is None:
                                    raise YPYModelError('Key property group_address is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-igmp-cfg:static-group-group-address[Cisco-IOS-XR-ipv4-igmp-cfg:group-address = ' + str(self.group_address) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.group_address is not None:
                                    return True

                                if self.group_count is not None:
                                    return True

                                if self.source_count is not None:
                                    return True

                                if self.suppress_report is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                                return meta._meta_table['Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddress']['meta_info']


                        class StaticGroupGroupAddressSourceAddress(object):
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
                                self.parent = None
                                self.group_address = None
                                self.source_address = None
                                self.group_count = None
                                self.source_count = None
                                self.suppress_report = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.group_address is None:
                                    raise YPYModelError('Key property group_address is None')
                                if self.source_address is None:
                                    raise YPYModelError('Key property source_address is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-igmp-cfg:static-group-group-address-source-address[Cisco-IOS-XR-ipv4-igmp-cfg:group-address = ' + str(self.group_address) + '][Cisco-IOS-XR-ipv4-igmp-cfg:source-address = ' + str(self.source_address) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.group_address is not None:
                                    return True

                                if self.source_address is not None:
                                    return True

                                if self.group_count is not None:
                                    return True

                                if self.source_count is not None:
                                    return True

                                if self.suppress_report is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                                return meta._meta_table['Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddress']['meta_info']


                        class StaticGroupGroupAddressSourceAddressSourceAddressMask(object):
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
                                self.parent = None
                                self.group_address = None
                                self.source_address = None
                                self.source_address_mask = None
                                self.group_count = None
                                self.source_count = None
                                self.suppress_report = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.group_address is None:
                                    raise YPYModelError('Key property group_address is None')
                                if self.source_address is None:
                                    raise YPYModelError('Key property source_address is None')
                                if self.source_address_mask is None:
                                    raise YPYModelError('Key property source_address_mask is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-igmp-cfg:static-group-group-address-source-address-source-address-mask[Cisco-IOS-XR-ipv4-igmp-cfg:group-address = ' + str(self.group_address) + '][Cisco-IOS-XR-ipv4-igmp-cfg:source-address = ' + str(self.source_address) + '][Cisco-IOS-XR-ipv4-igmp-cfg:source-address-mask = ' + str(self.source_address_mask) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.group_address is not None:
                                    return True

                                if self.source_address is not None:
                                    return True

                                if self.source_address_mask is not None:
                                    return True

                                if self.group_count is not None:
                                    return True

                                if self.source_count is not None:
                                    return True

                                if self.suppress_report is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                                return meta._meta_table['Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddressSourceAddressMask']['meta_info']


                        class StaticGroupGroupAddressGroupAddressMask(object):
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
                                self.parent = None
                                self.group_address = None
                                self.group_address_mask = None
                                self.group_count = None
                                self.source_count = None
                                self.suppress_report = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.group_address is None:
                                    raise YPYModelError('Key property group_address is None')
                                if self.group_address_mask is None:
                                    raise YPYModelError('Key property group_address_mask is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-igmp-cfg:static-group-group-address-group-address-mask[Cisco-IOS-XR-ipv4-igmp-cfg:group-address = ' + str(self.group_address) + '][Cisco-IOS-XR-ipv4-igmp-cfg:group-address-mask = ' + str(self.group_address_mask) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.group_address is not None:
                                    return True

                                if self.group_address_mask is not None:
                                    return True

                                if self.group_count is not None:
                                    return True

                                if self.source_count is not None:
                                    return True

                                if self.suppress_report is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                                return meta._meta_table['Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMask']['meta_info']


                        class StaticGroupGroupAddressGroupAddressMaskSourceAddress(object):
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
                                self.parent = None
                                self.group_address = None
                                self.group_address_mask = None
                                self.source_address = None
                                self.group_count = None
                                self.source_count = None
                                self.suppress_report = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.group_address is None:
                                    raise YPYModelError('Key property group_address is None')
                                if self.group_address_mask is None:
                                    raise YPYModelError('Key property group_address_mask is None')
                                if self.source_address is None:
                                    raise YPYModelError('Key property source_address is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-igmp-cfg:static-group-group-address-group-address-mask-source-address[Cisco-IOS-XR-ipv4-igmp-cfg:group-address = ' + str(self.group_address) + '][Cisco-IOS-XR-ipv4-igmp-cfg:group-address-mask = ' + str(self.group_address_mask) + '][Cisco-IOS-XR-ipv4-igmp-cfg:source-address = ' + str(self.source_address) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.group_address is not None:
                                    return True

                                if self.group_address_mask is not None:
                                    return True

                                if self.source_address is not None:
                                    return True

                                if self.group_count is not None:
                                    return True

                                if self.source_count is not None:
                                    return True

                                if self.suppress_report is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                                return meta._meta_table['Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddress']['meta_info']


                        class StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask(object):
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
                                self.parent = None
                                self.group_address = None
                                self.group_address_mask = None
                                self.source_address = None
                                self.source_address_mask = None
                                self.group_count = None
                                self.source_count = None
                                self.suppress_report = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.group_address is None:
                                    raise YPYModelError('Key property group_address is None')
                                if self.group_address_mask is None:
                                    raise YPYModelError('Key property group_address_mask is None')
                                if self.source_address is None:
                                    raise YPYModelError('Key property source_address is None')
                                if self.source_address_mask is None:
                                    raise YPYModelError('Key property source_address_mask is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-igmp-cfg:static-group-group-address-group-address-mask-source-address-source-address-mask[Cisco-IOS-XR-ipv4-igmp-cfg:group-address = ' + str(self.group_address) + '][Cisco-IOS-XR-ipv4-igmp-cfg:group-address-mask = ' + str(self.group_address_mask) + '][Cisco-IOS-XR-ipv4-igmp-cfg:source-address = ' + str(self.source_address) + '][Cisco-IOS-XR-ipv4-igmp-cfg:source-address-mask = ' + str(self.source_address_mask) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.group_address is not None:
                                    return True

                                if self.group_address_mask is not None:
                                    return True

                                if self.source_address is not None:
                                    return True

                                if self.source_address_mask is not None:
                                    return True

                                if self.group_count is not None:
                                    return True

                                if self.source_count is not None:
                                    return True

                                if self.suppress_report is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                                return meta._meta_table['Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-igmp-cfg:static-group-group-addresses'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.static_group_group_address is not None:
                                for child_ref in self.static_group_group_address:
                                    if child_ref._has_data():
                                        return True

                            if self.static_group_group_address_group_address_mask is not None:
                                for child_ref in self.static_group_group_address_group_address_mask:
                                    if child_ref._has_data():
                                        return True

                            if self.static_group_group_address_group_address_mask_source_address is not None:
                                for child_ref in self.static_group_group_address_group_address_mask_source_address:
                                    if child_ref._has_data():
                                        return True

                            if self.static_group_group_address_group_address_mask_source_address_source_address_mask is not None:
                                for child_ref in self.static_group_group_address_group_address_mask_source_address_source_address_mask:
                                    if child_ref._has_data():
                                        return True

                            if self.static_group_group_address_source_address is not None:
                                for child_ref in self.static_group_group_address_source_address:
                                    if child_ref._has_data():
                                        return True

                            if self.static_group_group_address_source_address_source_address_mask is not None:
                                for child_ref in self.static_group_group_address_source_address_source_address_mask:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                            return meta._meta_table['Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses']['meta_info']


                    class MaximumGroupsPerInterfaceOor(object):
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
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2016-10-10'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.access_list_name = None
                            self.maximum_groups = None
                            self.warning_threshold = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-igmp-cfg:maximum-groups-per-interface-oor'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.access_list_name is not None:
                                return True

                            if self.maximum_groups is not None:
                                return True

                            if self.warning_threshold is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                            return meta._meta_table['Igmp.Vrfs.Vrf.Interfaces.Interface.MaximumGroupsPerInterfaceOor']['meta_info']


                    class ExplicitTracking(object):
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
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2016-10-10'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.access_list_name = None
                            self.enable = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-igmp-cfg:explicit-tracking'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.access_list_name is not None:
                                return True

                            if self.enable is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                            return meta._meta_table['Igmp.Vrfs.Vrf.Interfaces.Interface.ExplicitTracking']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.interface_name is None:
                            raise YPYModelError('Key property interface_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-igmp-cfg:interface[Cisco-IOS-XR-ipv4-igmp-cfg:interface-name = ' + str(self.interface_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.interface_name is not None:
                            return True

                        if self.access_group is not None:
                            return True

                        if self.explicit_tracking is not None and self.explicit_tracking._has_data():
                            return True

                        if self.join_groups is not None and self.join_groups._has_data():
                            return True

                        if self.maximum_groups_per_interface_oor is not None and self.maximum_groups_per_interface_oor._has_data():
                            return True

                        if self.query_interval is not None:
                            return True

                        if self.query_max_response_time is not None:
                            return True

                        if self.query_timeout is not None:
                            return True

                        if self.router_enable is not None:
                            return True

                        if self.static_group_group_addresses is not None and self.static_group_group_addresses._has_data():
                            return True

                        if self.version is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                        return meta._meta_table['Igmp.Vrfs.Vrf.Interfaces.Interface']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-igmp-cfg:interfaces'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.interface is not None:
                        for child_ref in self.interface:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                    return meta._meta_table['Igmp.Vrfs.Vrf.Interfaces']['meta_info']

            @property
            def _common_path(self):
                if self.vrf_name is None:
                    raise YPYModelError('Key property vrf_name is None')

                return '/Cisco-IOS-XR-ipv4-igmp-cfg:igmp/Cisco-IOS-XR-ipv4-igmp-cfg:vrfs/Cisco-IOS-XR-ipv4-igmp-cfg:vrf[Cisco-IOS-XR-ipv4-igmp-cfg:vrf-name = ' + str(self.vrf_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.vrf_name is not None:
                    return True

                if self.inheritable_defaults is not None and self.inheritable_defaults._has_data():
                    return True

                if self.interfaces is not None and self.interfaces._has_data():
                    return True

                if self.maximum is not None and self.maximum._has_data():
                    return True

                if self.robustness is not None:
                    return True

                if self.ssm_access_groups is not None and self.ssm_access_groups._has_data():
                    return True

                if self.ssmdns_query_group is not None:
                    return True

                if self.traffic is not None and self.traffic._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                return meta._meta_table['Igmp.Vrfs.Vrf']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv4-igmp-cfg:igmp/Cisco-IOS-XR-ipv4-igmp-cfg:vrfs'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.vrf is not None:
                for child_ref in self.vrf:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
            return meta._meta_table['Igmp.Vrfs']['meta_info']


    class DefaultContext(object):
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
        
        .. attribute:: _is_presence
        
        	Is present if this instance represents presence container else not
        	**type**\: bool
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'ipv4-igmp-cfg'
        _revision = '2016-10-10'

        def __init__(self):
            self.parent = None
            self._is_presence = True
            self.accounting = Igmp.DefaultContext.Accounting()
            self.accounting.parent = self
            self.inheritable_defaults = Igmp.DefaultContext.InheritableDefaults()
            self.inheritable_defaults.parent = self
            self.interfaces = Igmp.DefaultContext.Interfaces()
            self.interfaces.parent = self
            self.maximum = Igmp.DefaultContext.Maximum()
            self.maximum.parent = self
            self.nsf = Igmp.DefaultContext.Nsf()
            self.nsf.parent = self
            self.robustness = None
            self.ssm_access_groups = Igmp.DefaultContext.SsmAccessGroups()
            self.ssm_access_groups.parent = self
            self.ssmdns_query_group = None
            self.traffic = Igmp.DefaultContext.Traffic()
            self.traffic.parent = self
            self.unicast_qos_adjust = Igmp.DefaultContext.UnicastQosAdjust()
            self.unicast_qos_adjust.parent = self


        class Nsf(object):
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
                self.parent = None
                self.lifetime = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv4-igmp-cfg:igmp/Cisco-IOS-XR-ipv4-igmp-cfg:default-context/Cisco-IOS-XR-ipv4-igmp-cfg:nsf'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.lifetime is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                return meta._meta_table['Igmp.DefaultContext.Nsf']['meta_info']


        class UnicastQosAdjust(object):
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
                self.parent = None
                self.adjustment_delay = None
                self.download_interval = None
                self.hold_off = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv4-igmp-cfg:igmp/Cisco-IOS-XR-ipv4-igmp-cfg:default-context/Cisco-IOS-XR-ipv4-igmp-cfg:unicast-qos-adjust'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.adjustment_delay is not None:
                    return True

                if self.download_interval is not None:
                    return True

                if self.hold_off is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                return meta._meta_table['Igmp.DefaultContext.UnicastQosAdjust']['meta_info']


        class Accounting(object):
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
                self.parent = None
                self.max_history = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv4-igmp-cfg:igmp/Cisco-IOS-XR-ipv4-igmp-cfg:default-context/Cisco-IOS-XR-ipv4-igmp-cfg:accounting'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.max_history is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                return meta._meta_table['Igmp.DefaultContext.Accounting']['meta_info']


        class Traffic(object):
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
                self.parent = None
                self.profile = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv4-igmp-cfg:igmp/Cisco-IOS-XR-ipv4-igmp-cfg:default-context/Cisco-IOS-XR-ipv4-igmp-cfg:traffic'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.profile is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                return meta._meta_table['Igmp.DefaultContext.Traffic']['meta_info']


        class InheritableDefaults(object):
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
                self.parent = None
                self.access_group = None
                self.explicit_tracking = None
                self.maximum_groups_per_interface_oor = None
                self.query_interval = None
                self.query_max_response_time = None
                self.query_timeout = None
                self.router_enable = None
                self.version = None


            class MaximumGroupsPerInterfaceOor(object):
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
                
                .. attribute:: _is_presence
                
                	Is present if this instance represents presence container else not
                	**type**\: bool
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'ipv4-igmp-cfg'
                _revision = '2016-10-10'

                def __init__(self):
                    self.parent = None
                    self._is_presence = True
                    self.access_list_name = None
                    self.maximum_groups = None
                    self.warning_threshold = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ipv4-igmp-cfg:igmp/Cisco-IOS-XR-ipv4-igmp-cfg:default-context/Cisco-IOS-XR-ipv4-igmp-cfg:inheritable-defaults/Cisco-IOS-XR-ipv4-igmp-cfg:maximum-groups-per-interface-oor'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self._is_presence:
                        return True
                    if self.access_list_name is not None:
                        return True

                    if self.maximum_groups is not None:
                        return True

                    if self.warning_threshold is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                    return meta._meta_table['Igmp.DefaultContext.InheritableDefaults.MaximumGroupsPerInterfaceOor']['meta_info']


            class ExplicitTracking(object):
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
                
                .. attribute:: _is_presence
                
                	Is present if this instance represents presence container else not
                	**type**\: bool
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'ipv4-igmp-cfg'
                _revision = '2016-10-10'

                def __init__(self):
                    self.parent = None
                    self._is_presence = True
                    self.access_list_name = None
                    self.enable = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ipv4-igmp-cfg:igmp/Cisco-IOS-XR-ipv4-igmp-cfg:default-context/Cisco-IOS-XR-ipv4-igmp-cfg:inheritable-defaults/Cisco-IOS-XR-ipv4-igmp-cfg:explicit-tracking'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self._is_presence:
                        return True
                    if self.access_list_name is not None:
                        return True

                    if self.enable is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                    return meta._meta_table['Igmp.DefaultContext.InheritableDefaults.ExplicitTracking']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv4-igmp-cfg:igmp/Cisco-IOS-XR-ipv4-igmp-cfg:default-context/Cisco-IOS-XR-ipv4-igmp-cfg:inheritable-defaults'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.access_group is not None:
                    return True

                if self.explicit_tracking is not None and self.explicit_tracking._has_data():
                    return True

                if self.maximum_groups_per_interface_oor is not None and self.maximum_groups_per_interface_oor._has_data():
                    return True

                if self.query_interval is not None:
                    return True

                if self.query_max_response_time is not None:
                    return True

                if self.query_timeout is not None:
                    return True

                if self.router_enable is not None:
                    return True

                if self.version is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                return meta._meta_table['Igmp.DefaultContext.InheritableDefaults']['meta_info']


        class SsmAccessGroups(object):
            """
            IGMP Source specific mode
            
            .. attribute:: ssm_access_group
            
            	SSM static Access Group
            	**type**\: list of    :py:class:`SsmAccessGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext.SsmAccessGroups.SsmAccessGroup>`
            
            

            """

            _prefix = 'ipv4-igmp-cfg'
            _revision = '2016-10-10'

            def __init__(self):
                self.parent = None
                self.ssm_access_group = YList()
                self.ssm_access_group.parent = self
                self.ssm_access_group.name = 'ssm_access_group'


            class SsmAccessGroup(object):
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
                    self.parent = None
                    self.source_address = None
                    self.access_list_name = None

                @property
                def _common_path(self):
                    if self.source_address is None:
                        raise YPYModelError('Key property source_address is None')

                    return '/Cisco-IOS-XR-ipv4-igmp-cfg:igmp/Cisco-IOS-XR-ipv4-igmp-cfg:default-context/Cisco-IOS-XR-ipv4-igmp-cfg:ssm-access-groups/Cisco-IOS-XR-ipv4-igmp-cfg:ssm-access-group[Cisco-IOS-XR-ipv4-igmp-cfg:source-address = ' + str(self.source_address) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.source_address is not None:
                        return True

                    if self.access_list_name is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                    return meta._meta_table['Igmp.DefaultContext.SsmAccessGroups.SsmAccessGroup']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv4-igmp-cfg:igmp/Cisco-IOS-XR-ipv4-igmp-cfg:default-context/Cisco-IOS-XR-ipv4-igmp-cfg:ssm-access-groups'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.ssm_access_group is not None:
                    for child_ref in self.ssm_access_group:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                return meta._meta_table['Igmp.DefaultContext.SsmAccessGroups']['meta_info']


        class Maximum(object):
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
                self.parent = None
                self.maximum_groups = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv4-igmp-cfg:igmp/Cisco-IOS-XR-ipv4-igmp-cfg:default-context/Cisco-IOS-XR-ipv4-igmp-cfg:maximum'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.maximum_groups is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                return meta._meta_table['Igmp.DefaultContext.Maximum']['meta_info']


        class Interfaces(object):
            """
            Interface\-level configuration
            
            .. attribute:: interface
            
            	The name of the interface
            	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext.Interfaces.Interface>`
            
            

            """

            _prefix = 'ipv4-igmp-cfg'
            _revision = '2016-10-10'

            def __init__(self):
                self.parent = None
                self.interface = YList()
                self.interface.parent = self
                self.interface.name = 'interface'


            class Interface(object):
                """
                The name of the interface
                
                .. attribute:: interface_name  <key>
                
                	Name of the interface
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
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
                    self.parent = None
                    self.interface_name = None
                    self.access_group = None
                    self.explicit_tracking = None
                    self.join_groups = None
                    self.maximum_groups_per_interface_oor = None
                    self.query_interval = None
                    self.query_max_response_time = None
                    self.query_timeout = None
                    self.router_enable = None
                    self.static_group_group_addresses = Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses()
                    self.static_group_group_addresses.parent = self
                    self.version = None


                class JoinGroups(object):
                    """
                    IGMP join multicast group
                    
                    .. attribute:: join_group
                    
                    	IP group address and optional source address to include
                    	**type**\: list of    :py:class:`JoinGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext.Interfaces.Interface.JoinGroups.JoinGroup>`
                    
                    .. attribute:: join_group_source_address
                    
                    	IP group address and optional source address to include
                    	**type**\: list of    :py:class:`JoinGroupSourceAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Igmp.DefaultContext.Interfaces.Interface.JoinGroups.JoinGroupSourceAddress>`
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-igmp-cfg'
                    _revision = '2016-10-10'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.join_group = YList()
                        self.join_group.parent = self
                        self.join_group.name = 'join_group'
                        self.join_group_source_address = YList()
                        self.join_group_source_address.parent = self
                        self.join_group_source_address.name = 'join_group_source_address'


                    class JoinGroup(object):
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
                        	**type**\:   :py:class:`IgmpFilterEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.IgmpFilterEnum>`
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2016-10-10'

                        def __init__(self):
                            self.parent = None
                            self.group_address = None
                            self.mode = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.group_address is None:
                                raise YPYModelError('Key property group_address is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-igmp-cfg:join-group[Cisco-IOS-XR-ipv4-igmp-cfg:group-address = ' + str(self.group_address) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.group_address is not None:
                                return True

                            if self.mode is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                            return meta._meta_table['Igmp.DefaultContext.Interfaces.Interface.JoinGroups.JoinGroup']['meta_info']


                    class JoinGroupSourceAddress(object):
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
                        	**type**\:   :py:class:`IgmpFilterEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.IgmpFilterEnum>`
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2016-10-10'

                        def __init__(self):
                            self.parent = None
                            self.group_address = None
                            self.source_address = None
                            self.mode = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.group_address is None:
                                raise YPYModelError('Key property group_address is None')
                            if self.source_address is None:
                                raise YPYModelError('Key property source_address is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-igmp-cfg:join-group-source-address[Cisco-IOS-XR-ipv4-igmp-cfg:group-address = ' + str(self.group_address) + '][Cisco-IOS-XR-ipv4-igmp-cfg:source-address = ' + str(self.source_address) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.group_address is not None:
                                return True

                            if self.source_address is not None:
                                return True

                            if self.mode is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                            return meta._meta_table['Igmp.DefaultContext.Interfaces.Interface.JoinGroups.JoinGroupSourceAddress']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-igmp-cfg:join-groups'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self._is_presence:
                            return True
                        if self.join_group is not None:
                            for child_ref in self.join_group:
                                if child_ref._has_data():
                                    return True

                        if self.join_group_source_address is not None:
                            for child_ref in self.join_group_source_address:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                        return meta._meta_table['Igmp.DefaultContext.Interfaces.Interface.JoinGroups']['meta_info']


                class StaticGroupGroupAddresses(object):
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
                        self.parent = None
                        self.static_group_group_address = YList()
                        self.static_group_group_address.parent = self
                        self.static_group_group_address.name = 'static_group_group_address'
                        self.static_group_group_address_group_address_mask = YList()
                        self.static_group_group_address_group_address_mask.parent = self
                        self.static_group_group_address_group_address_mask.name = 'static_group_group_address_group_address_mask'
                        self.static_group_group_address_group_address_mask_source_address = YList()
                        self.static_group_group_address_group_address_mask_source_address.parent = self
                        self.static_group_group_address_group_address_mask_source_address.name = 'static_group_group_address_group_address_mask_source_address'
                        self.static_group_group_address_group_address_mask_source_address_source_address_mask = YList()
                        self.static_group_group_address_group_address_mask_source_address_source_address_mask.parent = self
                        self.static_group_group_address_group_address_mask_source_address_source_address_mask.name = 'static_group_group_address_group_address_mask_source_address_source_address_mask'
                        self.static_group_group_address_source_address = YList()
                        self.static_group_group_address_source_address.parent = self
                        self.static_group_group_address_source_address.name = 'static_group_group_address_source_address'
                        self.static_group_group_address_source_address_source_address_mask = YList()
                        self.static_group_group_address_source_address_source_address_mask.parent = self
                        self.static_group_group_address_source_address_source_address_mask.name = 'static_group_group_address_source_address_source_address_mask'


                    class StaticGroupGroupAddress(object):
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
                            self.parent = None
                            self.group_address = None
                            self.group_count = None
                            self.source_count = None
                            self.suppress_report = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.group_address is None:
                                raise YPYModelError('Key property group_address is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-igmp-cfg:static-group-group-address[Cisco-IOS-XR-ipv4-igmp-cfg:group-address = ' + str(self.group_address) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.group_address is not None:
                                return True

                            if self.group_count is not None:
                                return True

                            if self.source_count is not None:
                                return True

                            if self.suppress_report is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                            return meta._meta_table['Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddress']['meta_info']


                    class StaticGroupGroupAddressSourceAddress(object):
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
                            self.parent = None
                            self.group_address = None
                            self.source_address = None
                            self.group_count = None
                            self.source_count = None
                            self.suppress_report = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.group_address is None:
                                raise YPYModelError('Key property group_address is None')
                            if self.source_address is None:
                                raise YPYModelError('Key property source_address is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-igmp-cfg:static-group-group-address-source-address[Cisco-IOS-XR-ipv4-igmp-cfg:group-address = ' + str(self.group_address) + '][Cisco-IOS-XR-ipv4-igmp-cfg:source-address = ' + str(self.source_address) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.group_address is not None:
                                return True

                            if self.source_address is not None:
                                return True

                            if self.group_count is not None:
                                return True

                            if self.source_count is not None:
                                return True

                            if self.suppress_report is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                            return meta._meta_table['Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddress']['meta_info']


                    class StaticGroupGroupAddressSourceAddressSourceAddressMask(object):
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
                            self.parent = None
                            self.group_address = None
                            self.source_address = None
                            self.source_address_mask = None
                            self.group_count = None
                            self.source_count = None
                            self.suppress_report = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.group_address is None:
                                raise YPYModelError('Key property group_address is None')
                            if self.source_address is None:
                                raise YPYModelError('Key property source_address is None')
                            if self.source_address_mask is None:
                                raise YPYModelError('Key property source_address_mask is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-igmp-cfg:static-group-group-address-source-address-source-address-mask[Cisco-IOS-XR-ipv4-igmp-cfg:group-address = ' + str(self.group_address) + '][Cisco-IOS-XR-ipv4-igmp-cfg:source-address = ' + str(self.source_address) + '][Cisco-IOS-XR-ipv4-igmp-cfg:source-address-mask = ' + str(self.source_address_mask) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.group_address is not None:
                                return True

                            if self.source_address is not None:
                                return True

                            if self.source_address_mask is not None:
                                return True

                            if self.group_count is not None:
                                return True

                            if self.source_count is not None:
                                return True

                            if self.suppress_report is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                            return meta._meta_table['Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddressSourceAddressMask']['meta_info']


                    class StaticGroupGroupAddressGroupAddressMask(object):
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
                            self.parent = None
                            self.group_address = None
                            self.group_address_mask = None
                            self.group_count = None
                            self.source_count = None
                            self.suppress_report = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.group_address is None:
                                raise YPYModelError('Key property group_address is None')
                            if self.group_address_mask is None:
                                raise YPYModelError('Key property group_address_mask is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-igmp-cfg:static-group-group-address-group-address-mask[Cisco-IOS-XR-ipv4-igmp-cfg:group-address = ' + str(self.group_address) + '][Cisco-IOS-XR-ipv4-igmp-cfg:group-address-mask = ' + str(self.group_address_mask) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.group_address is not None:
                                return True

                            if self.group_address_mask is not None:
                                return True

                            if self.group_count is not None:
                                return True

                            if self.source_count is not None:
                                return True

                            if self.suppress_report is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                            return meta._meta_table['Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMask']['meta_info']


                    class StaticGroupGroupAddressGroupAddressMaskSourceAddress(object):
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
                            self.parent = None
                            self.group_address = None
                            self.group_address_mask = None
                            self.source_address = None
                            self.group_count = None
                            self.source_count = None
                            self.suppress_report = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.group_address is None:
                                raise YPYModelError('Key property group_address is None')
                            if self.group_address_mask is None:
                                raise YPYModelError('Key property group_address_mask is None')
                            if self.source_address is None:
                                raise YPYModelError('Key property source_address is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-igmp-cfg:static-group-group-address-group-address-mask-source-address[Cisco-IOS-XR-ipv4-igmp-cfg:group-address = ' + str(self.group_address) + '][Cisco-IOS-XR-ipv4-igmp-cfg:group-address-mask = ' + str(self.group_address_mask) + '][Cisco-IOS-XR-ipv4-igmp-cfg:source-address = ' + str(self.source_address) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.group_address is not None:
                                return True

                            if self.group_address_mask is not None:
                                return True

                            if self.source_address is not None:
                                return True

                            if self.group_count is not None:
                                return True

                            if self.source_count is not None:
                                return True

                            if self.suppress_report is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                            return meta._meta_table['Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddress']['meta_info']


                    class StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask(object):
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
                            self.parent = None
                            self.group_address = None
                            self.group_address_mask = None
                            self.source_address = None
                            self.source_address_mask = None
                            self.group_count = None
                            self.source_count = None
                            self.suppress_report = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.group_address is None:
                                raise YPYModelError('Key property group_address is None')
                            if self.group_address_mask is None:
                                raise YPYModelError('Key property group_address_mask is None')
                            if self.source_address is None:
                                raise YPYModelError('Key property source_address is None')
                            if self.source_address_mask is None:
                                raise YPYModelError('Key property source_address_mask is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-igmp-cfg:static-group-group-address-group-address-mask-source-address-source-address-mask[Cisco-IOS-XR-ipv4-igmp-cfg:group-address = ' + str(self.group_address) + '][Cisco-IOS-XR-ipv4-igmp-cfg:group-address-mask = ' + str(self.group_address_mask) + '][Cisco-IOS-XR-ipv4-igmp-cfg:source-address = ' + str(self.source_address) + '][Cisco-IOS-XR-ipv4-igmp-cfg:source-address-mask = ' + str(self.source_address_mask) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.group_address is not None:
                                return True

                            if self.group_address_mask is not None:
                                return True

                            if self.source_address is not None:
                                return True

                            if self.source_address_mask is not None:
                                return True

                            if self.group_count is not None:
                                return True

                            if self.source_count is not None:
                                return True

                            if self.suppress_report is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                            return meta._meta_table['Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-igmp-cfg:static-group-group-addresses'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.static_group_group_address is not None:
                            for child_ref in self.static_group_group_address:
                                if child_ref._has_data():
                                    return True

                        if self.static_group_group_address_group_address_mask is not None:
                            for child_ref in self.static_group_group_address_group_address_mask:
                                if child_ref._has_data():
                                    return True

                        if self.static_group_group_address_group_address_mask_source_address is not None:
                            for child_ref in self.static_group_group_address_group_address_mask_source_address:
                                if child_ref._has_data():
                                    return True

                        if self.static_group_group_address_group_address_mask_source_address_source_address_mask is not None:
                            for child_ref in self.static_group_group_address_group_address_mask_source_address_source_address_mask:
                                if child_ref._has_data():
                                    return True

                        if self.static_group_group_address_source_address is not None:
                            for child_ref in self.static_group_group_address_source_address:
                                if child_ref._has_data():
                                    return True

                        if self.static_group_group_address_source_address_source_address_mask is not None:
                            for child_ref in self.static_group_group_address_source_address_source_address_mask:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                        return meta._meta_table['Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses']['meta_info']


                class MaximumGroupsPerInterfaceOor(object):
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
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-igmp-cfg'
                    _revision = '2016-10-10'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.access_list_name = None
                        self.maximum_groups = None
                        self.warning_threshold = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-igmp-cfg:maximum-groups-per-interface-oor'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self._is_presence:
                            return True
                        if self.access_list_name is not None:
                            return True

                        if self.maximum_groups is not None:
                            return True

                        if self.warning_threshold is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                        return meta._meta_table['Igmp.DefaultContext.Interfaces.Interface.MaximumGroupsPerInterfaceOor']['meta_info']


                class ExplicitTracking(object):
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
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-igmp-cfg'
                    _revision = '2016-10-10'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.access_list_name = None
                        self.enable = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-igmp-cfg:explicit-tracking'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self._is_presence:
                            return True
                        if self.access_list_name is not None:
                            return True

                        if self.enable is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                        return meta._meta_table['Igmp.DefaultContext.Interfaces.Interface.ExplicitTracking']['meta_info']

                @property
                def _common_path(self):
                    if self.interface_name is None:
                        raise YPYModelError('Key property interface_name is None')

                    return '/Cisco-IOS-XR-ipv4-igmp-cfg:igmp/Cisco-IOS-XR-ipv4-igmp-cfg:default-context/Cisco-IOS-XR-ipv4-igmp-cfg:interfaces/Cisco-IOS-XR-ipv4-igmp-cfg:interface[Cisco-IOS-XR-ipv4-igmp-cfg:interface-name = ' + str(self.interface_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.interface_name is not None:
                        return True

                    if self.access_group is not None:
                        return True

                    if self.explicit_tracking is not None and self.explicit_tracking._has_data():
                        return True

                    if self.join_groups is not None and self.join_groups._has_data():
                        return True

                    if self.maximum_groups_per_interface_oor is not None and self.maximum_groups_per_interface_oor._has_data():
                        return True

                    if self.query_interval is not None:
                        return True

                    if self.query_max_response_time is not None:
                        return True

                    if self.query_timeout is not None:
                        return True

                    if self.router_enable is not None:
                        return True

                    if self.static_group_group_addresses is not None and self.static_group_group_addresses._has_data():
                        return True

                    if self.version is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                    return meta._meta_table['Igmp.DefaultContext.Interfaces.Interface']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv4-igmp-cfg:igmp/Cisco-IOS-XR-ipv4-igmp-cfg:default-context/Cisco-IOS-XR-ipv4-igmp-cfg:interfaces'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.interface is not None:
                    for child_ref in self.interface:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                return meta._meta_table['Igmp.DefaultContext.Interfaces']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv4-igmp-cfg:igmp/Cisco-IOS-XR-ipv4-igmp-cfg:default-context'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self._is_presence:
                return True
            if self.accounting is not None and self.accounting._has_data():
                return True

            if self.inheritable_defaults is not None and self.inheritable_defaults._has_data():
                return True

            if self.interfaces is not None and self.interfaces._has_data():
                return True

            if self.maximum is not None and self.maximum._has_data():
                return True

            if self.nsf is not None and self.nsf._has_data():
                return True

            if self.robustness is not None:
                return True

            if self.ssm_access_groups is not None and self.ssm_access_groups._has_data():
                return True

            if self.ssmdns_query_group is not None:
                return True

            if self.traffic is not None and self.traffic._has_data():
                return True

            if self.unicast_qos_adjust is not None and self.unicast_qos_adjust._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
            return meta._meta_table['Igmp.DefaultContext']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ipv4-igmp-cfg:igmp'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self._is_presence:
            return True
        if self.default_context is not None and self.default_context._has_data():
            return True

        if self.vrfs is not None and self.vrfs._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
        return meta._meta_table['Igmp']['meta_info']


class Amt(object):
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
        self.amtmtu = None
        self.amtqqic = None
        self.amttos = None
        self.amtttl = None
        self.gateway_filter = None
        self.maximum_gateway = None
        self.maximum_v4_route_gateway = None
        self.maximum_v4_routes = None
        self.maximum_v6_route_gateway = None
        self.maximum_v6_routes = None
        self.relay_adv_add = None
        self.relay_anycast_prefix = None


    class RelayAdvAdd(object):
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
        
        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
        
        .. attribute:: _is_presence
        
        	Is present if this instance represents presence container else not
        	**type**\: bool
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'ipv4-igmp-cfg'
        _revision = '2016-10-10'

        def __init__(self):
            self.parent = None
            self._is_presence = True
            self.address = None
            self.interface = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv4-igmp-cfg:amt/Cisco-IOS-XR-ipv4-igmp-cfg:relay-adv-add'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self._is_presence:
                return True
            if self.address is not None:
                return True

            if self.interface is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
            return meta._meta_table['Amt.RelayAdvAdd']['meta_info']


    class RelayAnycastPrefix(object):
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
        
        .. attribute:: _is_presence
        
        	Is present if this instance represents presence container else not
        	**type**\: bool
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'ipv4-igmp-cfg'
        _revision = '2016-10-10'

        def __init__(self):
            self.parent = None
            self._is_presence = True
            self.address = None
            self.prefix_length = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv4-igmp-cfg:amt/Cisco-IOS-XR-ipv4-igmp-cfg:relay-anycast-prefix'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self._is_presence:
                return True
            if self.address is not None:
                return True

            if self.prefix_length is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
            return meta._meta_table['Amt.RelayAnycastPrefix']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ipv4-igmp-cfg:amt'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.amtmtu is not None:
            return True

        if self.amtqqic is not None:
            return True

        if self.amttos is not None:
            return True

        if self.amtttl is not None:
            return True

        if self.gateway_filter is not None:
            return True

        if self.maximum_gateway is not None:
            return True

        if self.maximum_v4_route_gateway is not None:
            return True

        if self.maximum_v4_routes is not None:
            return True

        if self.maximum_v6_route_gateway is not None:
            return True

        if self.maximum_v6_routes is not None:
            return True

        if self.relay_adv_add is not None and self.relay_adv_add._has_data():
            return True

        if self.relay_anycast_prefix is not None and self.relay_anycast_prefix._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
        return meta._meta_table['Amt']['meta_info']


class Mld(object):
    """
    mld
    
    .. attribute:: default_context
    
    	Default Context
    	**type**\:   :py:class:`DefaultContext <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext>`
    
    	**presence node**\: True
    
    .. attribute:: vrfs
    
    	VRF related configuration
    	**type**\:   :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.Vrfs>`
    
    .. attribute:: _is_presence
    
    	Is present if this instance represents presence container else not
    	**type**\: bool
    
    

    This class is a :ref:`presence class<presence-class>`

    """

    _prefix = 'ipv4-igmp-cfg'
    _revision = '2016-10-10'

    def __init__(self):
        self._is_presence = True
        self.default_context = None
        self.vrfs = Mld.Vrfs()
        self.vrfs.parent = self


    class Vrfs(object):
        """
        VRF related configuration
        
        .. attribute:: vrf
        
        	Configuration for a particular vrf
        	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.Vrfs.Vrf>`
        
        

        """

        _prefix = 'ipv4-igmp-cfg'
        _revision = '2016-10-10'

        def __init__(self):
            self.parent = None
            self.vrf = YList()
            self.vrf.parent = self
            self.vrf.name = 'vrf'


        class Vrf(object):
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
                self.parent = None
                self.vrf_name = None
                self.inheritable_defaults = Mld.Vrfs.Vrf.InheritableDefaults()
                self.inheritable_defaults.parent = self
                self.interfaces = Mld.Vrfs.Vrf.Interfaces()
                self.interfaces.parent = self
                self.maximum = Mld.Vrfs.Vrf.Maximum()
                self.maximum.parent = self
                self.robustness = None
                self.ssm_access_groups = Mld.Vrfs.Vrf.SsmAccessGroups()
                self.ssm_access_groups.parent = self
                self.ssmdns_query_group = None
                self.traffic = Mld.Vrfs.Vrf.Traffic()
                self.traffic.parent = self


            class Traffic(object):
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
                    self.parent = None
                    self.profile = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-igmp-cfg:traffic'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.profile is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                    return meta._meta_table['Mld.Vrfs.Vrf.Traffic']['meta_info']


            class InheritableDefaults(object):
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
                    self.parent = None
                    self.access_group = None
                    self.explicit_tracking = None
                    self.maximum_groups_per_interface_oor = None
                    self.query_interval = None
                    self.query_max_response_time = None
                    self.query_timeout = None
                    self.router_enable = None
                    self.version = None


                class MaximumGroupsPerInterfaceOor(object):
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
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-igmp-cfg'
                    _revision = '2016-10-10'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.access_list_name = None
                        self.maximum_groups = None
                        self.warning_threshold = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-igmp-cfg:maximum-groups-per-interface-oor'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self._is_presence:
                            return True
                        if self.access_list_name is not None:
                            return True

                        if self.maximum_groups is not None:
                            return True

                        if self.warning_threshold is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                        return meta._meta_table['Mld.Vrfs.Vrf.InheritableDefaults.MaximumGroupsPerInterfaceOor']['meta_info']


                class ExplicitTracking(object):
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
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-igmp-cfg'
                    _revision = '2016-10-10'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.access_list_name = None
                        self.enable = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-igmp-cfg:explicit-tracking'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self._is_presence:
                            return True
                        if self.access_list_name is not None:
                            return True

                        if self.enable is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                        return meta._meta_table['Mld.Vrfs.Vrf.InheritableDefaults.ExplicitTracking']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-igmp-cfg:inheritable-defaults'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.access_group is not None:
                        return True

                    if self.explicit_tracking is not None and self.explicit_tracking._has_data():
                        return True

                    if self.maximum_groups_per_interface_oor is not None and self.maximum_groups_per_interface_oor._has_data():
                        return True

                    if self.query_interval is not None:
                        return True

                    if self.query_max_response_time is not None:
                        return True

                    if self.query_timeout is not None:
                        return True

                    if self.router_enable is not None:
                        return True

                    if self.version is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                    return meta._meta_table['Mld.Vrfs.Vrf.InheritableDefaults']['meta_info']


            class SsmAccessGroups(object):
                """
                IGMP Source specific mode
                
                .. attribute:: ssm_access_group
                
                	SSM static Access Group
                	**type**\: list of    :py:class:`SsmAccessGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.Vrfs.Vrf.SsmAccessGroups.SsmAccessGroup>`
                
                

                """

                _prefix = 'ipv4-igmp-cfg'
                _revision = '2016-10-10'

                def __init__(self):
                    self.parent = None
                    self.ssm_access_group = YList()
                    self.ssm_access_group.parent = self
                    self.ssm_access_group.name = 'ssm_access_group'


                class SsmAccessGroup(object):
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
                        self.parent = None
                        self.source_address = None
                        self.access_list_name = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.source_address is None:
                            raise YPYModelError('Key property source_address is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-igmp-cfg:ssm-access-group[Cisco-IOS-XR-ipv4-igmp-cfg:source-address = ' + str(self.source_address) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.source_address is not None:
                            return True

                        if self.access_list_name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                        return meta._meta_table['Mld.Vrfs.Vrf.SsmAccessGroups.SsmAccessGroup']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-igmp-cfg:ssm-access-groups'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.ssm_access_group is not None:
                        for child_ref in self.ssm_access_group:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                    return meta._meta_table['Mld.Vrfs.Vrf.SsmAccessGroups']['meta_info']


            class Maximum(object):
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
                    self.parent = None
                    self.maximum_groups = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-igmp-cfg:maximum'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.maximum_groups is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                    return meta._meta_table['Mld.Vrfs.Vrf.Maximum']['meta_info']


            class Interfaces(object):
                """
                Interface\-level configuration
                
                .. attribute:: interface
                
                	The name of the interface
                	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.Vrfs.Vrf.Interfaces.Interface>`
                
                

                """

                _prefix = 'ipv4-igmp-cfg'
                _revision = '2016-10-10'

                def __init__(self):
                    self.parent = None
                    self.interface = YList()
                    self.interface.parent = self
                    self.interface.name = 'interface'


                class Interface(object):
                    """
                    The name of the interface
                    
                    .. attribute:: interface_name  <key>
                    
                    	Name of the interface
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
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
                        self.parent = None
                        self.interface_name = None
                        self.access_group = None
                        self.explicit_tracking = None
                        self.join_groups = None
                        self.maximum_groups_per_interface_oor = None
                        self.query_interval = None
                        self.query_max_response_time = None
                        self.query_timeout = None
                        self.router_enable = None
                        self.static_group_group_addresses = Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses()
                        self.static_group_group_addresses.parent = self
                        self.version = None


                    class JoinGroups(object):
                        """
                        IGMP join multicast group
                        
                        .. attribute:: join_group
                        
                        	IP group address and optional source address to include
                        	**type**\: list of    :py:class:`JoinGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.Vrfs.Vrf.Interfaces.Interface.JoinGroups.JoinGroup>`
                        
                        .. attribute:: join_group_source_address
                        
                        	IP group address and optional source address to include
                        	**type**\: list of    :py:class:`JoinGroupSourceAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.Vrfs.Vrf.Interfaces.Interface.JoinGroups.JoinGroupSourceAddress>`
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2016-10-10'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.join_group = YList()
                            self.join_group.parent = self
                            self.join_group.name = 'join_group'
                            self.join_group_source_address = YList()
                            self.join_group_source_address.parent = self
                            self.join_group_source_address.name = 'join_group_source_address'


                        class JoinGroup(object):
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
                            	**type**\:   :py:class:`IgmpFilterEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.IgmpFilterEnum>`
                            
                            	**mandatory**\: True
                            
                            

                            """

                            _prefix = 'ipv4-igmp-cfg'
                            _revision = '2016-10-10'

                            def __init__(self):
                                self.parent = None
                                self.group_address = None
                                self.mode = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.group_address is None:
                                    raise YPYModelError('Key property group_address is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-igmp-cfg:join-group[Cisco-IOS-XR-ipv4-igmp-cfg:group-address = ' + str(self.group_address) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.group_address is not None:
                                    return True

                                if self.mode is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                                return meta._meta_table['Mld.Vrfs.Vrf.Interfaces.Interface.JoinGroups.JoinGroup']['meta_info']


                        class JoinGroupSourceAddress(object):
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
                            	**type**\:   :py:class:`IgmpFilterEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.IgmpFilterEnum>`
                            
                            	**mandatory**\: True
                            
                            

                            """

                            _prefix = 'ipv4-igmp-cfg'
                            _revision = '2016-10-10'

                            def __init__(self):
                                self.parent = None
                                self.group_address = None
                                self.source_address = None
                                self.mode = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.group_address is None:
                                    raise YPYModelError('Key property group_address is None')
                                if self.source_address is None:
                                    raise YPYModelError('Key property source_address is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-igmp-cfg:join-group-source-address[Cisco-IOS-XR-ipv4-igmp-cfg:group-address = ' + str(self.group_address) + '][Cisco-IOS-XR-ipv4-igmp-cfg:source-address = ' + str(self.source_address) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.group_address is not None:
                                    return True

                                if self.source_address is not None:
                                    return True

                                if self.mode is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                                return meta._meta_table['Mld.Vrfs.Vrf.Interfaces.Interface.JoinGroups.JoinGroupSourceAddress']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-igmp-cfg:join-groups'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.join_group is not None:
                                for child_ref in self.join_group:
                                    if child_ref._has_data():
                                        return True

                            if self.join_group_source_address is not None:
                                for child_ref in self.join_group_source_address:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                            return meta._meta_table['Mld.Vrfs.Vrf.Interfaces.Interface.JoinGroups']['meta_info']


                    class StaticGroupGroupAddresses(object):
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
                            self.parent = None
                            self.static_group_group_address = YList()
                            self.static_group_group_address.parent = self
                            self.static_group_group_address.name = 'static_group_group_address'
                            self.static_group_group_address_group_address_mask = YList()
                            self.static_group_group_address_group_address_mask.parent = self
                            self.static_group_group_address_group_address_mask.name = 'static_group_group_address_group_address_mask'
                            self.static_group_group_address_group_address_mask_source_address = YList()
                            self.static_group_group_address_group_address_mask_source_address.parent = self
                            self.static_group_group_address_group_address_mask_source_address.name = 'static_group_group_address_group_address_mask_source_address'
                            self.static_group_group_address_group_address_mask_source_address_source_address_mask = YList()
                            self.static_group_group_address_group_address_mask_source_address_source_address_mask.parent = self
                            self.static_group_group_address_group_address_mask_source_address_source_address_mask.name = 'static_group_group_address_group_address_mask_source_address_source_address_mask'
                            self.static_group_group_address_source_address = YList()
                            self.static_group_group_address_source_address.parent = self
                            self.static_group_group_address_source_address.name = 'static_group_group_address_source_address'
                            self.static_group_group_address_source_address_source_address_mask = YList()
                            self.static_group_group_address_source_address_source_address_mask.parent = self
                            self.static_group_group_address_source_address_source_address_mask.name = 'static_group_group_address_source_address_source_address_mask'


                        class StaticGroupGroupAddress(object):
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
                                self.parent = None
                                self.group_address = None
                                self.group_count = None
                                self.source_count = None
                                self.suppress_report = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.group_address is None:
                                    raise YPYModelError('Key property group_address is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-igmp-cfg:static-group-group-address[Cisco-IOS-XR-ipv4-igmp-cfg:group-address = ' + str(self.group_address) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.group_address is not None:
                                    return True

                                if self.group_count is not None:
                                    return True

                                if self.source_count is not None:
                                    return True

                                if self.suppress_report is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                                return meta._meta_table['Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddress']['meta_info']


                        class StaticGroupGroupAddressSourceAddress(object):
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
                                self.parent = None
                                self.group_address = None
                                self.source_address = None
                                self.group_count = None
                                self.source_count = None
                                self.suppress_report = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.group_address is None:
                                    raise YPYModelError('Key property group_address is None')
                                if self.source_address is None:
                                    raise YPYModelError('Key property source_address is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-igmp-cfg:static-group-group-address-source-address[Cisco-IOS-XR-ipv4-igmp-cfg:group-address = ' + str(self.group_address) + '][Cisco-IOS-XR-ipv4-igmp-cfg:source-address = ' + str(self.source_address) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.group_address is not None:
                                    return True

                                if self.source_address is not None:
                                    return True

                                if self.group_count is not None:
                                    return True

                                if self.source_count is not None:
                                    return True

                                if self.suppress_report is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                                return meta._meta_table['Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddress']['meta_info']


                        class StaticGroupGroupAddressSourceAddressSourceAddressMask(object):
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
                                self.parent = None
                                self.group_address = None
                                self.source_address = None
                                self.source_address_mask = None
                                self.group_count = None
                                self.source_count = None
                                self.suppress_report = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.group_address is None:
                                    raise YPYModelError('Key property group_address is None')
                                if self.source_address is None:
                                    raise YPYModelError('Key property source_address is None')
                                if self.source_address_mask is None:
                                    raise YPYModelError('Key property source_address_mask is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-igmp-cfg:static-group-group-address-source-address-source-address-mask[Cisco-IOS-XR-ipv4-igmp-cfg:group-address = ' + str(self.group_address) + '][Cisco-IOS-XR-ipv4-igmp-cfg:source-address = ' + str(self.source_address) + '][Cisco-IOS-XR-ipv4-igmp-cfg:source-address-mask = ' + str(self.source_address_mask) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.group_address is not None:
                                    return True

                                if self.source_address is not None:
                                    return True

                                if self.source_address_mask is not None:
                                    return True

                                if self.group_count is not None:
                                    return True

                                if self.source_count is not None:
                                    return True

                                if self.suppress_report is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                                return meta._meta_table['Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddressSourceAddressMask']['meta_info']


                        class StaticGroupGroupAddressGroupAddressMask(object):
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
                                self.parent = None
                                self.group_address = None
                                self.group_address_mask = None
                                self.group_count = None
                                self.source_count = None
                                self.suppress_report = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.group_address is None:
                                    raise YPYModelError('Key property group_address is None')
                                if self.group_address_mask is None:
                                    raise YPYModelError('Key property group_address_mask is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-igmp-cfg:static-group-group-address-group-address-mask[Cisco-IOS-XR-ipv4-igmp-cfg:group-address = ' + str(self.group_address) + '][Cisco-IOS-XR-ipv4-igmp-cfg:group-address-mask = ' + str(self.group_address_mask) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.group_address is not None:
                                    return True

                                if self.group_address_mask is not None:
                                    return True

                                if self.group_count is not None:
                                    return True

                                if self.source_count is not None:
                                    return True

                                if self.suppress_report is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                                return meta._meta_table['Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMask']['meta_info']


                        class StaticGroupGroupAddressGroupAddressMaskSourceAddress(object):
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
                                self.parent = None
                                self.group_address = None
                                self.group_address_mask = None
                                self.source_address = None
                                self.group_count = None
                                self.source_count = None
                                self.suppress_report = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.group_address is None:
                                    raise YPYModelError('Key property group_address is None')
                                if self.group_address_mask is None:
                                    raise YPYModelError('Key property group_address_mask is None')
                                if self.source_address is None:
                                    raise YPYModelError('Key property source_address is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-igmp-cfg:static-group-group-address-group-address-mask-source-address[Cisco-IOS-XR-ipv4-igmp-cfg:group-address = ' + str(self.group_address) + '][Cisco-IOS-XR-ipv4-igmp-cfg:group-address-mask = ' + str(self.group_address_mask) + '][Cisco-IOS-XR-ipv4-igmp-cfg:source-address = ' + str(self.source_address) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.group_address is not None:
                                    return True

                                if self.group_address_mask is not None:
                                    return True

                                if self.source_address is not None:
                                    return True

                                if self.group_count is not None:
                                    return True

                                if self.source_count is not None:
                                    return True

                                if self.suppress_report is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                                return meta._meta_table['Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddress']['meta_info']


                        class StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask(object):
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
                                self.parent = None
                                self.group_address = None
                                self.group_address_mask = None
                                self.source_address = None
                                self.source_address_mask = None
                                self.group_count = None
                                self.source_count = None
                                self.suppress_report = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.group_address is None:
                                    raise YPYModelError('Key property group_address is None')
                                if self.group_address_mask is None:
                                    raise YPYModelError('Key property group_address_mask is None')
                                if self.source_address is None:
                                    raise YPYModelError('Key property source_address is None')
                                if self.source_address_mask is None:
                                    raise YPYModelError('Key property source_address_mask is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-igmp-cfg:static-group-group-address-group-address-mask-source-address-source-address-mask[Cisco-IOS-XR-ipv4-igmp-cfg:group-address = ' + str(self.group_address) + '][Cisco-IOS-XR-ipv4-igmp-cfg:group-address-mask = ' + str(self.group_address_mask) + '][Cisco-IOS-XR-ipv4-igmp-cfg:source-address = ' + str(self.source_address) + '][Cisco-IOS-XR-ipv4-igmp-cfg:source-address-mask = ' + str(self.source_address_mask) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.group_address is not None:
                                    return True

                                if self.group_address_mask is not None:
                                    return True

                                if self.source_address is not None:
                                    return True

                                if self.source_address_mask is not None:
                                    return True

                                if self.group_count is not None:
                                    return True

                                if self.source_count is not None:
                                    return True

                                if self.suppress_report is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                                return meta._meta_table['Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-igmp-cfg:static-group-group-addresses'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.static_group_group_address is not None:
                                for child_ref in self.static_group_group_address:
                                    if child_ref._has_data():
                                        return True

                            if self.static_group_group_address_group_address_mask is not None:
                                for child_ref in self.static_group_group_address_group_address_mask:
                                    if child_ref._has_data():
                                        return True

                            if self.static_group_group_address_group_address_mask_source_address is not None:
                                for child_ref in self.static_group_group_address_group_address_mask_source_address:
                                    if child_ref._has_data():
                                        return True

                            if self.static_group_group_address_group_address_mask_source_address_source_address_mask is not None:
                                for child_ref in self.static_group_group_address_group_address_mask_source_address_source_address_mask:
                                    if child_ref._has_data():
                                        return True

                            if self.static_group_group_address_source_address is not None:
                                for child_ref in self.static_group_group_address_source_address:
                                    if child_ref._has_data():
                                        return True

                            if self.static_group_group_address_source_address_source_address_mask is not None:
                                for child_ref in self.static_group_group_address_source_address_source_address_mask:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                            return meta._meta_table['Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses']['meta_info']


                    class MaximumGroupsPerInterfaceOor(object):
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
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2016-10-10'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.access_list_name = None
                            self.maximum_groups = None
                            self.warning_threshold = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-igmp-cfg:maximum-groups-per-interface-oor'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.access_list_name is not None:
                                return True

                            if self.maximum_groups is not None:
                                return True

                            if self.warning_threshold is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                            return meta._meta_table['Mld.Vrfs.Vrf.Interfaces.Interface.MaximumGroupsPerInterfaceOor']['meta_info']


                    class ExplicitTracking(object):
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
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2016-10-10'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.access_list_name = None
                            self.enable = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-igmp-cfg:explicit-tracking'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.access_list_name is not None:
                                return True

                            if self.enable is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                            return meta._meta_table['Mld.Vrfs.Vrf.Interfaces.Interface.ExplicitTracking']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.interface_name is None:
                            raise YPYModelError('Key property interface_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-igmp-cfg:interface[Cisco-IOS-XR-ipv4-igmp-cfg:interface-name = ' + str(self.interface_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.interface_name is not None:
                            return True

                        if self.access_group is not None:
                            return True

                        if self.explicit_tracking is not None and self.explicit_tracking._has_data():
                            return True

                        if self.join_groups is not None and self.join_groups._has_data():
                            return True

                        if self.maximum_groups_per_interface_oor is not None and self.maximum_groups_per_interface_oor._has_data():
                            return True

                        if self.query_interval is not None:
                            return True

                        if self.query_max_response_time is not None:
                            return True

                        if self.query_timeout is not None:
                            return True

                        if self.router_enable is not None:
                            return True

                        if self.static_group_group_addresses is not None and self.static_group_group_addresses._has_data():
                            return True

                        if self.version is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                        return meta._meta_table['Mld.Vrfs.Vrf.Interfaces.Interface']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-igmp-cfg:interfaces'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.interface is not None:
                        for child_ref in self.interface:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                    return meta._meta_table['Mld.Vrfs.Vrf.Interfaces']['meta_info']

            @property
            def _common_path(self):
                if self.vrf_name is None:
                    raise YPYModelError('Key property vrf_name is None')

                return '/Cisco-IOS-XR-ipv4-igmp-cfg:mld/Cisco-IOS-XR-ipv4-igmp-cfg:vrfs/Cisco-IOS-XR-ipv4-igmp-cfg:vrf[Cisco-IOS-XR-ipv4-igmp-cfg:vrf-name = ' + str(self.vrf_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.vrf_name is not None:
                    return True

                if self.inheritable_defaults is not None and self.inheritable_defaults._has_data():
                    return True

                if self.interfaces is not None and self.interfaces._has_data():
                    return True

                if self.maximum is not None and self.maximum._has_data():
                    return True

                if self.robustness is not None:
                    return True

                if self.ssm_access_groups is not None and self.ssm_access_groups._has_data():
                    return True

                if self.ssmdns_query_group is not None:
                    return True

                if self.traffic is not None and self.traffic._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                return meta._meta_table['Mld.Vrfs.Vrf']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv4-igmp-cfg:mld/Cisco-IOS-XR-ipv4-igmp-cfg:vrfs'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.vrf is not None:
                for child_ref in self.vrf:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
            return meta._meta_table['Mld.Vrfs']['meta_info']


    class DefaultContext(object):
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
        
        .. attribute:: _is_presence
        
        	Is present if this instance represents presence container else not
        	**type**\: bool
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'ipv4-igmp-cfg'
        _revision = '2016-10-10'

        def __init__(self):
            self.parent = None
            self._is_presence = True
            self.accounting = Mld.DefaultContext.Accounting()
            self.accounting.parent = self
            self.inheritable_defaults = Mld.DefaultContext.InheritableDefaults()
            self.inheritable_defaults.parent = self
            self.interfaces = Mld.DefaultContext.Interfaces()
            self.interfaces.parent = self
            self.maximum = Mld.DefaultContext.Maximum()
            self.maximum.parent = self
            self.nsf = Mld.DefaultContext.Nsf()
            self.nsf.parent = self
            self.robustness = None
            self.ssm_access_groups = Mld.DefaultContext.SsmAccessGroups()
            self.ssm_access_groups.parent = self
            self.ssmdns_query_group = None
            self.traffic = Mld.DefaultContext.Traffic()
            self.traffic.parent = self
            self.unicast_qos_adjust = Mld.DefaultContext.UnicastQosAdjust()
            self.unicast_qos_adjust.parent = self


        class Nsf(object):
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
                self.parent = None
                self.lifetime = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv4-igmp-cfg:mld/Cisco-IOS-XR-ipv4-igmp-cfg:default-context/Cisco-IOS-XR-ipv4-igmp-cfg:nsf'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.lifetime is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                return meta._meta_table['Mld.DefaultContext.Nsf']['meta_info']


        class UnicastQosAdjust(object):
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
                self.parent = None
                self.adjustment_delay = None
                self.download_interval = None
                self.hold_off = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv4-igmp-cfg:mld/Cisco-IOS-XR-ipv4-igmp-cfg:default-context/Cisco-IOS-XR-ipv4-igmp-cfg:unicast-qos-adjust'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.adjustment_delay is not None:
                    return True

                if self.download_interval is not None:
                    return True

                if self.hold_off is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                return meta._meta_table['Mld.DefaultContext.UnicastQosAdjust']['meta_info']


        class Accounting(object):
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
                self.parent = None
                self.max_history = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv4-igmp-cfg:mld/Cisco-IOS-XR-ipv4-igmp-cfg:default-context/Cisco-IOS-XR-ipv4-igmp-cfg:accounting'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.max_history is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                return meta._meta_table['Mld.DefaultContext.Accounting']['meta_info']


        class Traffic(object):
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
                self.parent = None
                self.profile = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv4-igmp-cfg:mld/Cisco-IOS-XR-ipv4-igmp-cfg:default-context/Cisco-IOS-XR-ipv4-igmp-cfg:traffic'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.profile is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                return meta._meta_table['Mld.DefaultContext.Traffic']['meta_info']


        class InheritableDefaults(object):
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
                self.parent = None
                self.access_group = None
                self.explicit_tracking = None
                self.maximum_groups_per_interface_oor = None
                self.query_interval = None
                self.query_max_response_time = None
                self.query_timeout = None
                self.router_enable = None
                self.version = None


            class MaximumGroupsPerInterfaceOor(object):
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
                
                .. attribute:: _is_presence
                
                	Is present if this instance represents presence container else not
                	**type**\: bool
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'ipv4-igmp-cfg'
                _revision = '2016-10-10'

                def __init__(self):
                    self.parent = None
                    self._is_presence = True
                    self.access_list_name = None
                    self.maximum_groups = None
                    self.warning_threshold = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ipv4-igmp-cfg:mld/Cisco-IOS-XR-ipv4-igmp-cfg:default-context/Cisco-IOS-XR-ipv4-igmp-cfg:inheritable-defaults/Cisco-IOS-XR-ipv4-igmp-cfg:maximum-groups-per-interface-oor'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self._is_presence:
                        return True
                    if self.access_list_name is not None:
                        return True

                    if self.maximum_groups is not None:
                        return True

                    if self.warning_threshold is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                    return meta._meta_table['Mld.DefaultContext.InheritableDefaults.MaximumGroupsPerInterfaceOor']['meta_info']


            class ExplicitTracking(object):
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
                
                .. attribute:: _is_presence
                
                	Is present if this instance represents presence container else not
                	**type**\: bool
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'ipv4-igmp-cfg'
                _revision = '2016-10-10'

                def __init__(self):
                    self.parent = None
                    self._is_presence = True
                    self.access_list_name = None
                    self.enable = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ipv4-igmp-cfg:mld/Cisco-IOS-XR-ipv4-igmp-cfg:default-context/Cisco-IOS-XR-ipv4-igmp-cfg:inheritable-defaults/Cisco-IOS-XR-ipv4-igmp-cfg:explicit-tracking'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self._is_presence:
                        return True
                    if self.access_list_name is not None:
                        return True

                    if self.enable is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                    return meta._meta_table['Mld.DefaultContext.InheritableDefaults.ExplicitTracking']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv4-igmp-cfg:mld/Cisco-IOS-XR-ipv4-igmp-cfg:default-context/Cisco-IOS-XR-ipv4-igmp-cfg:inheritable-defaults'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.access_group is not None:
                    return True

                if self.explicit_tracking is not None and self.explicit_tracking._has_data():
                    return True

                if self.maximum_groups_per_interface_oor is not None and self.maximum_groups_per_interface_oor._has_data():
                    return True

                if self.query_interval is not None:
                    return True

                if self.query_max_response_time is not None:
                    return True

                if self.query_timeout is not None:
                    return True

                if self.router_enable is not None:
                    return True

                if self.version is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                return meta._meta_table['Mld.DefaultContext.InheritableDefaults']['meta_info']


        class SsmAccessGroups(object):
            """
            IGMP Source specific mode
            
            .. attribute:: ssm_access_group
            
            	SSM static Access Group
            	**type**\: list of    :py:class:`SsmAccessGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext.SsmAccessGroups.SsmAccessGroup>`
            
            

            """

            _prefix = 'ipv4-igmp-cfg'
            _revision = '2016-10-10'

            def __init__(self):
                self.parent = None
                self.ssm_access_group = YList()
                self.ssm_access_group.parent = self
                self.ssm_access_group.name = 'ssm_access_group'


            class SsmAccessGroup(object):
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
                    self.parent = None
                    self.source_address = None
                    self.access_list_name = None

                @property
                def _common_path(self):
                    if self.source_address is None:
                        raise YPYModelError('Key property source_address is None')

                    return '/Cisco-IOS-XR-ipv4-igmp-cfg:mld/Cisco-IOS-XR-ipv4-igmp-cfg:default-context/Cisco-IOS-XR-ipv4-igmp-cfg:ssm-access-groups/Cisco-IOS-XR-ipv4-igmp-cfg:ssm-access-group[Cisco-IOS-XR-ipv4-igmp-cfg:source-address = ' + str(self.source_address) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.source_address is not None:
                        return True

                    if self.access_list_name is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                    return meta._meta_table['Mld.DefaultContext.SsmAccessGroups.SsmAccessGroup']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv4-igmp-cfg:mld/Cisco-IOS-XR-ipv4-igmp-cfg:default-context/Cisco-IOS-XR-ipv4-igmp-cfg:ssm-access-groups'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.ssm_access_group is not None:
                    for child_ref in self.ssm_access_group:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                return meta._meta_table['Mld.DefaultContext.SsmAccessGroups']['meta_info']


        class Maximum(object):
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
                self.parent = None
                self.maximum_groups = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv4-igmp-cfg:mld/Cisco-IOS-XR-ipv4-igmp-cfg:default-context/Cisco-IOS-XR-ipv4-igmp-cfg:maximum'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.maximum_groups is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                return meta._meta_table['Mld.DefaultContext.Maximum']['meta_info']


        class Interfaces(object):
            """
            Interface\-level configuration
            
            .. attribute:: interface
            
            	The name of the interface
            	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext.Interfaces.Interface>`
            
            

            """

            _prefix = 'ipv4-igmp-cfg'
            _revision = '2016-10-10'

            def __init__(self):
                self.parent = None
                self.interface = YList()
                self.interface.parent = self
                self.interface.name = 'interface'


            class Interface(object):
                """
                The name of the interface
                
                .. attribute:: interface_name  <key>
                
                	Name of the interface
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
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
                    self.parent = None
                    self.interface_name = None
                    self.access_group = None
                    self.explicit_tracking = None
                    self.join_groups = None
                    self.maximum_groups_per_interface_oor = None
                    self.query_interval = None
                    self.query_max_response_time = None
                    self.query_timeout = None
                    self.router_enable = None
                    self.static_group_group_addresses = Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses()
                    self.static_group_group_addresses.parent = self
                    self.version = None


                class JoinGroups(object):
                    """
                    IGMP join multicast group
                    
                    .. attribute:: join_group
                    
                    	IP group address and optional source address to include
                    	**type**\: list of    :py:class:`JoinGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext.Interfaces.Interface.JoinGroups.JoinGroup>`
                    
                    .. attribute:: join_group_source_address
                    
                    	IP group address and optional source address to include
                    	**type**\: list of    :py:class:`JoinGroupSourceAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.Mld.DefaultContext.Interfaces.Interface.JoinGroups.JoinGroupSourceAddress>`
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-igmp-cfg'
                    _revision = '2016-10-10'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.join_group = YList()
                        self.join_group.parent = self
                        self.join_group.name = 'join_group'
                        self.join_group_source_address = YList()
                        self.join_group_source_address.parent = self
                        self.join_group_source_address.name = 'join_group_source_address'


                    class JoinGroup(object):
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
                        	**type**\:   :py:class:`IgmpFilterEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.IgmpFilterEnum>`
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2016-10-10'

                        def __init__(self):
                            self.parent = None
                            self.group_address = None
                            self.mode = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.group_address is None:
                                raise YPYModelError('Key property group_address is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-igmp-cfg:join-group[Cisco-IOS-XR-ipv4-igmp-cfg:group-address = ' + str(self.group_address) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.group_address is not None:
                                return True

                            if self.mode is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                            return meta._meta_table['Mld.DefaultContext.Interfaces.Interface.JoinGroups.JoinGroup']['meta_info']


                    class JoinGroupSourceAddress(object):
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
                        	**type**\:   :py:class:`IgmpFilterEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg.IgmpFilterEnum>`
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'ipv4-igmp-cfg'
                        _revision = '2016-10-10'

                        def __init__(self):
                            self.parent = None
                            self.group_address = None
                            self.source_address = None
                            self.mode = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.group_address is None:
                                raise YPYModelError('Key property group_address is None')
                            if self.source_address is None:
                                raise YPYModelError('Key property source_address is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-igmp-cfg:join-group-source-address[Cisco-IOS-XR-ipv4-igmp-cfg:group-address = ' + str(self.group_address) + '][Cisco-IOS-XR-ipv4-igmp-cfg:source-address = ' + str(self.source_address) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.group_address is not None:
                                return True

                            if self.source_address is not None:
                                return True

                            if self.mode is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                            return meta._meta_table['Mld.DefaultContext.Interfaces.Interface.JoinGroups.JoinGroupSourceAddress']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-igmp-cfg:join-groups'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self._is_presence:
                            return True
                        if self.join_group is not None:
                            for child_ref in self.join_group:
                                if child_ref._has_data():
                                    return True

                        if self.join_group_source_address is not None:
                            for child_ref in self.join_group_source_address:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                        return meta._meta_table['Mld.DefaultContext.Interfaces.Interface.JoinGroups']['meta_info']


                class StaticGroupGroupAddresses(object):
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
                        self.parent = None
                        self.static_group_group_address = YList()
                        self.static_group_group_address.parent = self
                        self.static_group_group_address.name = 'static_group_group_address'
                        self.static_group_group_address_group_address_mask = YList()
                        self.static_group_group_address_group_address_mask.parent = self
                        self.static_group_group_address_group_address_mask.name = 'static_group_group_address_group_address_mask'
                        self.static_group_group_address_group_address_mask_source_address = YList()
                        self.static_group_group_address_group_address_mask_source_address.parent = self
                        self.static_group_group_address_group_address_mask_source_address.name = 'static_group_group_address_group_address_mask_source_address'
                        self.static_group_group_address_group_address_mask_source_address_source_address_mask = YList()
                        self.static_group_group_address_group_address_mask_source_address_source_address_mask.parent = self
                        self.static_group_group_address_group_address_mask_source_address_source_address_mask.name = 'static_group_group_address_group_address_mask_source_address_source_address_mask'
                        self.static_group_group_address_source_address = YList()
                        self.static_group_group_address_source_address.parent = self
                        self.static_group_group_address_source_address.name = 'static_group_group_address_source_address'
                        self.static_group_group_address_source_address_source_address_mask = YList()
                        self.static_group_group_address_source_address_source_address_mask.parent = self
                        self.static_group_group_address_source_address_source_address_mask.name = 'static_group_group_address_source_address_source_address_mask'


                    class StaticGroupGroupAddress(object):
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
                            self.parent = None
                            self.group_address = None
                            self.group_count = None
                            self.source_count = None
                            self.suppress_report = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.group_address is None:
                                raise YPYModelError('Key property group_address is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-igmp-cfg:static-group-group-address[Cisco-IOS-XR-ipv4-igmp-cfg:group-address = ' + str(self.group_address) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.group_address is not None:
                                return True

                            if self.group_count is not None:
                                return True

                            if self.source_count is not None:
                                return True

                            if self.suppress_report is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                            return meta._meta_table['Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddress']['meta_info']


                    class StaticGroupGroupAddressSourceAddress(object):
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
                            self.parent = None
                            self.group_address = None
                            self.source_address = None
                            self.group_count = None
                            self.source_count = None
                            self.suppress_report = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.group_address is None:
                                raise YPYModelError('Key property group_address is None')
                            if self.source_address is None:
                                raise YPYModelError('Key property source_address is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-igmp-cfg:static-group-group-address-source-address[Cisco-IOS-XR-ipv4-igmp-cfg:group-address = ' + str(self.group_address) + '][Cisco-IOS-XR-ipv4-igmp-cfg:source-address = ' + str(self.source_address) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.group_address is not None:
                                return True

                            if self.source_address is not None:
                                return True

                            if self.group_count is not None:
                                return True

                            if self.source_count is not None:
                                return True

                            if self.suppress_report is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                            return meta._meta_table['Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddress']['meta_info']


                    class StaticGroupGroupAddressSourceAddressSourceAddressMask(object):
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
                            self.parent = None
                            self.group_address = None
                            self.source_address = None
                            self.source_address_mask = None
                            self.group_count = None
                            self.source_count = None
                            self.suppress_report = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.group_address is None:
                                raise YPYModelError('Key property group_address is None')
                            if self.source_address is None:
                                raise YPYModelError('Key property source_address is None')
                            if self.source_address_mask is None:
                                raise YPYModelError('Key property source_address_mask is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-igmp-cfg:static-group-group-address-source-address-source-address-mask[Cisco-IOS-XR-ipv4-igmp-cfg:group-address = ' + str(self.group_address) + '][Cisco-IOS-XR-ipv4-igmp-cfg:source-address = ' + str(self.source_address) + '][Cisco-IOS-XR-ipv4-igmp-cfg:source-address-mask = ' + str(self.source_address_mask) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.group_address is not None:
                                return True

                            if self.source_address is not None:
                                return True

                            if self.source_address_mask is not None:
                                return True

                            if self.group_count is not None:
                                return True

                            if self.source_count is not None:
                                return True

                            if self.suppress_report is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                            return meta._meta_table['Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddressSourceAddressMask']['meta_info']


                    class StaticGroupGroupAddressGroupAddressMask(object):
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
                            self.parent = None
                            self.group_address = None
                            self.group_address_mask = None
                            self.group_count = None
                            self.source_count = None
                            self.suppress_report = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.group_address is None:
                                raise YPYModelError('Key property group_address is None')
                            if self.group_address_mask is None:
                                raise YPYModelError('Key property group_address_mask is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-igmp-cfg:static-group-group-address-group-address-mask[Cisco-IOS-XR-ipv4-igmp-cfg:group-address = ' + str(self.group_address) + '][Cisco-IOS-XR-ipv4-igmp-cfg:group-address-mask = ' + str(self.group_address_mask) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.group_address is not None:
                                return True

                            if self.group_address_mask is not None:
                                return True

                            if self.group_count is not None:
                                return True

                            if self.source_count is not None:
                                return True

                            if self.suppress_report is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                            return meta._meta_table['Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMask']['meta_info']


                    class StaticGroupGroupAddressGroupAddressMaskSourceAddress(object):
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
                            self.parent = None
                            self.group_address = None
                            self.group_address_mask = None
                            self.source_address = None
                            self.group_count = None
                            self.source_count = None
                            self.suppress_report = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.group_address is None:
                                raise YPYModelError('Key property group_address is None')
                            if self.group_address_mask is None:
                                raise YPYModelError('Key property group_address_mask is None')
                            if self.source_address is None:
                                raise YPYModelError('Key property source_address is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-igmp-cfg:static-group-group-address-group-address-mask-source-address[Cisco-IOS-XR-ipv4-igmp-cfg:group-address = ' + str(self.group_address) + '][Cisco-IOS-XR-ipv4-igmp-cfg:group-address-mask = ' + str(self.group_address_mask) + '][Cisco-IOS-XR-ipv4-igmp-cfg:source-address = ' + str(self.source_address) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.group_address is not None:
                                return True

                            if self.group_address_mask is not None:
                                return True

                            if self.source_address is not None:
                                return True

                            if self.group_count is not None:
                                return True

                            if self.source_count is not None:
                                return True

                            if self.suppress_report is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                            return meta._meta_table['Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddress']['meta_info']


                    class StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask(object):
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
                            self.parent = None
                            self.group_address = None
                            self.group_address_mask = None
                            self.source_address = None
                            self.source_address_mask = None
                            self.group_count = None
                            self.source_count = None
                            self.suppress_report = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.group_address is None:
                                raise YPYModelError('Key property group_address is None')
                            if self.group_address_mask is None:
                                raise YPYModelError('Key property group_address_mask is None')
                            if self.source_address is None:
                                raise YPYModelError('Key property source_address is None')
                            if self.source_address_mask is None:
                                raise YPYModelError('Key property source_address_mask is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-igmp-cfg:static-group-group-address-group-address-mask-source-address-source-address-mask[Cisco-IOS-XR-ipv4-igmp-cfg:group-address = ' + str(self.group_address) + '][Cisco-IOS-XR-ipv4-igmp-cfg:group-address-mask = ' + str(self.group_address_mask) + '][Cisco-IOS-XR-ipv4-igmp-cfg:source-address = ' + str(self.source_address) + '][Cisco-IOS-XR-ipv4-igmp-cfg:source-address-mask = ' + str(self.source_address_mask) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.group_address is not None:
                                return True

                            if self.group_address_mask is not None:
                                return True

                            if self.source_address is not None:
                                return True

                            if self.source_address_mask is not None:
                                return True

                            if self.group_count is not None:
                                return True

                            if self.source_count is not None:
                                return True

                            if self.suppress_report is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                            return meta._meta_table['Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-igmp-cfg:static-group-group-addresses'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.static_group_group_address is not None:
                            for child_ref in self.static_group_group_address:
                                if child_ref._has_data():
                                    return True

                        if self.static_group_group_address_group_address_mask is not None:
                            for child_ref in self.static_group_group_address_group_address_mask:
                                if child_ref._has_data():
                                    return True

                        if self.static_group_group_address_group_address_mask_source_address is not None:
                            for child_ref in self.static_group_group_address_group_address_mask_source_address:
                                if child_ref._has_data():
                                    return True

                        if self.static_group_group_address_group_address_mask_source_address_source_address_mask is not None:
                            for child_ref in self.static_group_group_address_group_address_mask_source_address_source_address_mask:
                                if child_ref._has_data():
                                    return True

                        if self.static_group_group_address_source_address is not None:
                            for child_ref in self.static_group_group_address_source_address:
                                if child_ref._has_data():
                                    return True

                        if self.static_group_group_address_source_address_source_address_mask is not None:
                            for child_ref in self.static_group_group_address_source_address_source_address_mask:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                        return meta._meta_table['Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses']['meta_info']


                class MaximumGroupsPerInterfaceOor(object):
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
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-igmp-cfg'
                    _revision = '2016-10-10'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.access_list_name = None
                        self.maximum_groups = None
                        self.warning_threshold = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-igmp-cfg:maximum-groups-per-interface-oor'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self._is_presence:
                            return True
                        if self.access_list_name is not None:
                            return True

                        if self.maximum_groups is not None:
                            return True

                        if self.warning_threshold is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                        return meta._meta_table['Mld.DefaultContext.Interfaces.Interface.MaximumGroupsPerInterfaceOor']['meta_info']


                class ExplicitTracking(object):
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
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-igmp-cfg'
                    _revision = '2016-10-10'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.access_list_name = None
                        self.enable = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-igmp-cfg:explicit-tracking'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self._is_presence:
                            return True
                        if self.access_list_name is not None:
                            return True

                        if self.enable is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                        return meta._meta_table['Mld.DefaultContext.Interfaces.Interface.ExplicitTracking']['meta_info']

                @property
                def _common_path(self):
                    if self.interface_name is None:
                        raise YPYModelError('Key property interface_name is None')

                    return '/Cisco-IOS-XR-ipv4-igmp-cfg:mld/Cisco-IOS-XR-ipv4-igmp-cfg:default-context/Cisco-IOS-XR-ipv4-igmp-cfg:interfaces/Cisco-IOS-XR-ipv4-igmp-cfg:interface[Cisco-IOS-XR-ipv4-igmp-cfg:interface-name = ' + str(self.interface_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.interface_name is not None:
                        return True

                    if self.access_group is not None:
                        return True

                    if self.explicit_tracking is not None and self.explicit_tracking._has_data():
                        return True

                    if self.join_groups is not None and self.join_groups._has_data():
                        return True

                    if self.maximum_groups_per_interface_oor is not None and self.maximum_groups_per_interface_oor._has_data():
                        return True

                    if self.query_interval is not None:
                        return True

                    if self.query_max_response_time is not None:
                        return True

                    if self.query_timeout is not None:
                        return True

                    if self.router_enable is not None:
                        return True

                    if self.static_group_group_addresses is not None and self.static_group_group_addresses._has_data():
                        return True

                    if self.version is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                    return meta._meta_table['Mld.DefaultContext.Interfaces.Interface']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv4-igmp-cfg:mld/Cisco-IOS-XR-ipv4-igmp-cfg:default-context/Cisco-IOS-XR-ipv4-igmp-cfg:interfaces'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.interface is not None:
                    for child_ref in self.interface:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
                return meta._meta_table['Mld.DefaultContext.Interfaces']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv4-igmp-cfg:mld/Cisco-IOS-XR-ipv4-igmp-cfg:default-context'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self._is_presence:
                return True
            if self.accounting is not None and self.accounting._has_data():
                return True

            if self.inheritable_defaults is not None and self.inheritable_defaults._has_data():
                return True

            if self.interfaces is not None and self.interfaces._has_data():
                return True

            if self.maximum is not None and self.maximum._has_data():
                return True

            if self.nsf is not None and self.nsf._has_data():
                return True

            if self.robustness is not None:
                return True

            if self.ssm_access_groups is not None and self.ssm_access_groups._has_data():
                return True

            if self.ssmdns_query_group is not None:
                return True

            if self.traffic is not None and self.traffic._has_data():
                return True

            if self.unicast_qos_adjust is not None and self.unicast_qos_adjust._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
            return meta._meta_table['Mld.DefaultContext']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ipv4-igmp-cfg:mld'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self._is_presence:
            return True
        if self.default_context is not None and self.default_context._has_data():
            return True

        if self.vrfs is not None and self.vrfs._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_cfg as meta
        return meta._meta_table['Mld']['meta_info']


