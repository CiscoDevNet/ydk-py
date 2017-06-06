""" Cisco_IOS_XR_ipv4_mfwd_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv4\-mfwd package configuration.

This module contains definitions
for the following management objects\:
  mfwd\: Multicast routing configuration

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class AccountingModeEnum(Enum):
    """
    AccountingModeEnum

    Accounting mode

    .. data:: enable = 0

    	Enable per (S,G) accounting

    .. data:: forward_only_enable = 1

    	Enable per (S,G) forward-only accounting

    """

    enable = 0

    forward_only_enable = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_mfwd_cfg as meta
        return meta._meta_table['AccountingModeEnum']



class Mfwd(object):
    """
    Multicast routing configuration
    
    .. attribute:: default_context
    
    	Default Context
    	**type**\:   :py:class:`DefaultContext <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg.Mfwd.DefaultContext>`
    
    	**presence node**\: True
    
    .. attribute:: vrfs
    
    	VRF Table
    	**type**\:   :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg.Mfwd.Vrfs>`
    
    .. attribute:: _is_presence
    
    	Is present if this instance represents presence container else not
    	**type**\: bool
    
    

    This class is a :ref:`presence class<presence-class>`

    """

    _prefix = 'ipv4-mfwd-cfg'
    _revision = '2016-06-01'

    def __init__(self):
        self._is_presence = True
        self.default_context = None
        self.vrfs = Mfwd.Vrfs()
        self.vrfs.parent = self


    class DefaultContext(object):
        """
        Default Context
        
        .. attribute:: ipv4
        
        	IPV4 commands in the default context
        	**type**\:   :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg.Mfwd.DefaultContext.Ipv4>`
        
        .. attribute:: ipv6
        
        	IPV6 commands in the default context
        	**type**\:   :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg.Mfwd.DefaultContext.Ipv6>`
        
        .. attribute:: _is_presence
        
        	Is present if this instance represents presence container else not
        	**type**\: bool
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'ipv4-mfwd-cfg'
        _revision = '2016-06-01'

        def __init__(self):
            self.parent = None
            self._is_presence = True
            self.ipv4 = Mfwd.DefaultContext.Ipv4()
            self.ipv4.parent = self
            self.ipv6 = Mfwd.DefaultContext.Ipv6()
            self.ipv6.parent = self


        class Ipv6(object):
            """
            IPV6 commands in the default context
            
            .. attribute:: accounting
            
            	Per\-prefix accounting mode
            	**type**\:   :py:class:`AccountingModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg.AccountingModeEnum>`
            
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
                self.parent = None
                self.accounting = None
                self.enable_on_all_interfaces = None
                self.forwarding_latency = None
                self.interface_inheritance_disable = None
                self.interfaces = Mfwd.DefaultContext.Ipv6.Interfaces()
                self.interfaces.parent = self
                self.log_traps = None
                self.maximum_checking_disable = None
                self.mofrr_lockout_timer_config = None
                self.mofrr_loss_detection_timer_config = None
                self.multicast_forwarding = None
                self.rate_per_route = None
                self.static_rpf_rules = Mfwd.DefaultContext.Ipv6.StaticRpfRules()
                self.static_rpf_rules.parent = self


            class StaticRpfRules(object):
                """
                Configure a static RPF rule for a given prefix
                
                .. attribute:: static_rpf_rule
                
                	RPF prefix address and mask
                	**type**\: list of    :py:class:`StaticRpfRule <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg.Mfwd.DefaultContext.Ipv6.StaticRpfRules.StaticRpfRule>`
                
                

                """

                _prefix = 'ipv4-mfwd-cfg'
                _revision = '2016-06-01'

                def __init__(self):
                    self.parent = None
                    self.static_rpf_rule = YList()
                    self.static_rpf_rule.parent = self
                    self.static_rpf_rule.name = 'static_rpf_rule'


                class StaticRpfRule(object):
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
                        self.parent = None
                        self.address = None
                        self.prefix_mask = None
                        self.interface_name = None
                        self.neighbor_address = None

                    @property
                    def _common_path(self):
                        if self.address is None:
                            raise YPYModelError('Key property address is None')
                        if self.prefix_mask is None:
                            raise YPYModelError('Key property prefix_mask is None')

                        return '/Cisco-IOS-XR-ipv4-mfwd-cfg:mfwd/Cisco-IOS-XR-ipv4-mfwd-cfg:default-context/Cisco-IOS-XR-ipv4-mfwd-cfg:ipv6/Cisco-IOS-XR-ipv4-mfwd-cfg:static-rpf-rules/Cisco-IOS-XR-ipv4-mfwd-cfg:static-rpf-rule[Cisco-IOS-XR-ipv4-mfwd-cfg:address = ' + str(self.address) + '][Cisco-IOS-XR-ipv4-mfwd-cfg:prefix-mask = ' + str(self.prefix_mask) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.address is not None:
                            return True

                        if self.prefix_mask is not None:
                            return True

                        if self.interface_name is not None:
                            return True

                        if self.neighbor_address is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_mfwd_cfg as meta
                        return meta._meta_table['Mfwd.DefaultContext.Ipv6.StaticRpfRules.StaticRpfRule']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ipv4-mfwd-cfg:mfwd/Cisco-IOS-XR-ipv4-mfwd-cfg:default-context/Cisco-IOS-XR-ipv4-mfwd-cfg:ipv6/Cisco-IOS-XR-ipv4-mfwd-cfg:static-rpf-rules'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.static_rpf_rule is not None:
                        for child_ref in self.static_rpf_rule:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_mfwd_cfg as meta
                    return meta._meta_table['Mfwd.DefaultContext.Ipv6.StaticRpfRules']['meta_info']


            class Interfaces(object):
                """
                Interface\-level Configuration
                
                .. attribute:: interface
                
                	The name of the interface
                	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg.Mfwd.DefaultContext.Ipv6.Interfaces.Interface>`
                
                

                """

                _prefix = 'ipv4-mfwd-cfg'
                _revision = '2016-06-01'

                def __init__(self):
                    self.parent = None
                    self.interface = YList()
                    self.interface.parent = self
                    self.interface.name = 'interface'


                class Interface(object):
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
                        self.parent = None
                        self.interface_name = None
                        self.boundary = None
                        self.enable_on_interface = None
                        self.ttl_threshold = None

                    @property
                    def _common_path(self):
                        if self.interface_name is None:
                            raise YPYModelError('Key property interface_name is None')

                        return '/Cisco-IOS-XR-ipv4-mfwd-cfg:mfwd/Cisco-IOS-XR-ipv4-mfwd-cfg:default-context/Cisco-IOS-XR-ipv4-mfwd-cfg:ipv6/Cisco-IOS-XR-ipv4-mfwd-cfg:interfaces/Cisco-IOS-XR-ipv4-mfwd-cfg:interface[Cisco-IOS-XR-ipv4-mfwd-cfg:interface-name = ' + str(self.interface_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.interface_name is not None:
                            return True

                        if self.boundary is not None:
                            return True

                        if self.enable_on_interface is not None:
                            return True

                        if self.ttl_threshold is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_mfwd_cfg as meta
                        return meta._meta_table['Mfwd.DefaultContext.Ipv6.Interfaces.Interface']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ipv4-mfwd-cfg:mfwd/Cisco-IOS-XR-ipv4-mfwd-cfg:default-context/Cisco-IOS-XR-ipv4-mfwd-cfg:ipv6/Cisco-IOS-XR-ipv4-mfwd-cfg:interfaces'

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
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_mfwd_cfg as meta
                    return meta._meta_table['Mfwd.DefaultContext.Ipv6.Interfaces']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv4-mfwd-cfg:mfwd/Cisco-IOS-XR-ipv4-mfwd-cfg:default-context/Cisco-IOS-XR-ipv4-mfwd-cfg:ipv6'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.accounting is not None:
                    return True

                if self.enable_on_all_interfaces is not None:
                    return True

                if self.forwarding_latency is not None:
                    return True

                if self.interface_inheritance_disable is not None:
                    return True

                if self.interfaces is not None and self.interfaces._has_data():
                    return True

                if self.log_traps is not None:
                    return True

                if self.maximum_checking_disable is not None:
                    return True

                if self.mofrr_lockout_timer_config is not None:
                    return True

                if self.mofrr_loss_detection_timer_config is not None:
                    return True

                if self.multicast_forwarding is not None:
                    return True

                if self.rate_per_route is not None:
                    return True

                if self.static_rpf_rules is not None and self.static_rpf_rules._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_mfwd_cfg as meta
                return meta._meta_table['Mfwd.DefaultContext.Ipv6']['meta_info']


        class Ipv4(object):
            """
            IPV4 commands in the default context
            
            .. attribute:: accounting
            
            	Per\-prefix accounting mode
            	**type**\:   :py:class:`AccountingModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg.AccountingModeEnum>`
            
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
                self.parent = None
                self.accounting = None
                self.enable_on_all_interfaces = None
                self.forwarding_latency = None
                self.interface_inheritance_disable = None
                self.interfaces = Mfwd.DefaultContext.Ipv4.Interfaces()
                self.interfaces.parent = self
                self.log_traps = None
                self.maximum_checking_disable = None
                self.mofrr_lockout_timer_config = None
                self.mofrr_loss_detection_timer_config = None
                self.multicast_forwarding = None
                self.out_of_memory_handling = None
                self.rate_per_route = None
                self.static_rpf_rules = Mfwd.DefaultContext.Ipv4.StaticRpfRules()
                self.static_rpf_rules.parent = self


            class StaticRpfRules(object):
                """
                Configure a static RPF rule for a given prefix
                
                .. attribute:: static_rpf_rule
                
                	RPF prefix address and mask
                	**type**\: list of    :py:class:`StaticRpfRule <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg.Mfwd.DefaultContext.Ipv4.StaticRpfRules.StaticRpfRule>`
                
                

                """

                _prefix = 'ipv4-mfwd-cfg'
                _revision = '2016-06-01'

                def __init__(self):
                    self.parent = None
                    self.static_rpf_rule = YList()
                    self.static_rpf_rule.parent = self
                    self.static_rpf_rule.name = 'static_rpf_rule'


                class StaticRpfRule(object):
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
                        self.parent = None
                        self.address = None
                        self.prefix_mask = None
                        self.interface_name = None
                        self.neighbor_address = None

                    @property
                    def _common_path(self):
                        if self.address is None:
                            raise YPYModelError('Key property address is None')
                        if self.prefix_mask is None:
                            raise YPYModelError('Key property prefix_mask is None')

                        return '/Cisco-IOS-XR-ipv4-mfwd-cfg:mfwd/Cisco-IOS-XR-ipv4-mfwd-cfg:default-context/Cisco-IOS-XR-ipv4-mfwd-cfg:ipv4/Cisco-IOS-XR-ipv4-mfwd-cfg:static-rpf-rules/Cisco-IOS-XR-ipv4-mfwd-cfg:static-rpf-rule[Cisco-IOS-XR-ipv4-mfwd-cfg:address = ' + str(self.address) + '][Cisco-IOS-XR-ipv4-mfwd-cfg:prefix-mask = ' + str(self.prefix_mask) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.address is not None:
                            return True

                        if self.prefix_mask is not None:
                            return True

                        if self.interface_name is not None:
                            return True

                        if self.neighbor_address is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_mfwd_cfg as meta
                        return meta._meta_table['Mfwd.DefaultContext.Ipv4.StaticRpfRules.StaticRpfRule']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ipv4-mfwd-cfg:mfwd/Cisco-IOS-XR-ipv4-mfwd-cfg:default-context/Cisco-IOS-XR-ipv4-mfwd-cfg:ipv4/Cisco-IOS-XR-ipv4-mfwd-cfg:static-rpf-rules'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.static_rpf_rule is not None:
                        for child_ref in self.static_rpf_rule:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_mfwd_cfg as meta
                    return meta._meta_table['Mfwd.DefaultContext.Ipv4.StaticRpfRules']['meta_info']


            class Interfaces(object):
                """
                Interface\-level Configuration
                
                .. attribute:: interface
                
                	The name of the interface
                	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg.Mfwd.DefaultContext.Ipv4.Interfaces.Interface>`
                
                

                """

                _prefix = 'ipv4-mfwd-cfg'
                _revision = '2016-06-01'

                def __init__(self):
                    self.parent = None
                    self.interface = YList()
                    self.interface.parent = self
                    self.interface.name = 'interface'


                class Interface(object):
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
                        self.parent = None
                        self.interface_name = None
                        self.boundary = None
                        self.enable_on_interface = None
                        self.ttl_threshold = None

                    @property
                    def _common_path(self):
                        if self.interface_name is None:
                            raise YPYModelError('Key property interface_name is None')

                        return '/Cisco-IOS-XR-ipv4-mfwd-cfg:mfwd/Cisco-IOS-XR-ipv4-mfwd-cfg:default-context/Cisco-IOS-XR-ipv4-mfwd-cfg:ipv4/Cisco-IOS-XR-ipv4-mfwd-cfg:interfaces/Cisco-IOS-XR-ipv4-mfwd-cfg:interface[Cisco-IOS-XR-ipv4-mfwd-cfg:interface-name = ' + str(self.interface_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.interface_name is not None:
                            return True

                        if self.boundary is not None:
                            return True

                        if self.enable_on_interface is not None:
                            return True

                        if self.ttl_threshold is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_mfwd_cfg as meta
                        return meta._meta_table['Mfwd.DefaultContext.Ipv4.Interfaces.Interface']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ipv4-mfwd-cfg:mfwd/Cisco-IOS-XR-ipv4-mfwd-cfg:default-context/Cisco-IOS-XR-ipv4-mfwd-cfg:ipv4/Cisco-IOS-XR-ipv4-mfwd-cfg:interfaces'

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
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_mfwd_cfg as meta
                    return meta._meta_table['Mfwd.DefaultContext.Ipv4.Interfaces']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv4-mfwd-cfg:mfwd/Cisco-IOS-XR-ipv4-mfwd-cfg:default-context/Cisco-IOS-XR-ipv4-mfwd-cfg:ipv4'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.accounting is not None:
                    return True

                if self.enable_on_all_interfaces is not None:
                    return True

                if self.forwarding_latency is not None:
                    return True

                if self.interface_inheritance_disable is not None:
                    return True

                if self.interfaces is not None and self.interfaces._has_data():
                    return True

                if self.log_traps is not None:
                    return True

                if self.maximum_checking_disable is not None:
                    return True

                if self.mofrr_lockout_timer_config is not None:
                    return True

                if self.mofrr_loss_detection_timer_config is not None:
                    return True

                if self.multicast_forwarding is not None:
                    return True

                if self.out_of_memory_handling is not None:
                    return True

                if self.rate_per_route is not None:
                    return True

                if self.static_rpf_rules is not None and self.static_rpf_rules._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_mfwd_cfg as meta
                return meta._meta_table['Mfwd.DefaultContext.Ipv4']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv4-mfwd-cfg:mfwd/Cisco-IOS-XR-ipv4-mfwd-cfg:default-context'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self._is_presence:
                return True
            if self.ipv4 is not None and self.ipv4._has_data():
                return True

            if self.ipv6 is not None and self.ipv6._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_mfwd_cfg as meta
            return meta._meta_table['Mfwd.DefaultContext']['meta_info']


    class Vrfs(object):
        """
        VRF Table
        
        .. attribute:: vrf
        
        	VRF table names
        	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg.Mfwd.Vrfs.Vrf>`
        
        

        """

        _prefix = 'ipv4-mfwd-cfg'
        _revision = '2016-06-01'

        def __init__(self):
            self.parent = None
            self.vrf = YList()
            self.vrf.parent = self
            self.vrf.name = 'vrf'


        class Vrf(object):
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
                self.parent = None
                self.vrf_name = None
                self.ipv4 = Mfwd.Vrfs.Vrf.Ipv4()
                self.ipv4.parent = self
                self.ipv6 = Mfwd.Vrfs.Vrf.Ipv6()
                self.ipv6.parent = self


            class Ipv6(object):
                """
                VRF table for IPV6 commands
                
                .. attribute:: accounting
                
                	Per\-prefix accounting mode
                	**type**\:   :py:class:`AccountingModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg.AccountingModeEnum>`
                
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
                    self.parent = None
                    self.accounting = None
                    self.enable_on_all_interfaces = None
                    self.interfaces = Mfwd.Vrfs.Vrf.Ipv6.Interfaces()
                    self.interfaces.parent = self
                    self.log_traps = None
                    self.multicast_forwarding = None
                    self.rate_per_route = None
                    self.static_rpf_rules = Mfwd.Vrfs.Vrf.Ipv6.StaticRpfRules()
                    self.static_rpf_rules.parent = self


                class StaticRpfRules(object):
                    """
                    Configure a static RPF rule for a given prefix
                    
                    .. attribute:: static_rpf_rule
                    
                    	RPF prefix address and mask
                    	**type**\: list of    :py:class:`StaticRpfRule <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg.Mfwd.Vrfs.Vrf.Ipv6.StaticRpfRules.StaticRpfRule>`
                    
                    

                    """

                    _prefix = 'ipv4-mfwd-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        self.parent = None
                        self.static_rpf_rule = YList()
                        self.static_rpf_rule.parent = self
                        self.static_rpf_rule.name = 'static_rpf_rule'


                    class StaticRpfRule(object):
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
                            self.parent = None
                            self.address = None
                            self.prefix_mask = None
                            self.interface_name = None
                            self.neighbor_address = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.address is None:
                                raise YPYModelError('Key property address is None')
                            if self.prefix_mask is None:
                                raise YPYModelError('Key property prefix_mask is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-mfwd-cfg:static-rpf-rule[Cisco-IOS-XR-ipv4-mfwd-cfg:address = ' + str(self.address) + '][Cisco-IOS-XR-ipv4-mfwd-cfg:prefix-mask = ' + str(self.prefix_mask) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.address is not None:
                                return True

                            if self.prefix_mask is not None:
                                return True

                            if self.interface_name is not None:
                                return True

                            if self.neighbor_address is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_mfwd_cfg as meta
                            return meta._meta_table['Mfwd.Vrfs.Vrf.Ipv6.StaticRpfRules.StaticRpfRule']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-mfwd-cfg:static-rpf-rules'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.static_rpf_rule is not None:
                            for child_ref in self.static_rpf_rule:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_mfwd_cfg as meta
                        return meta._meta_table['Mfwd.Vrfs.Vrf.Ipv6.StaticRpfRules']['meta_info']


                class Interfaces(object):
                    """
                    Interface\-level Configuration
                    
                    .. attribute:: interface
                    
                    	The name of the interface
                    	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg.Mfwd.Vrfs.Vrf.Ipv6.Interfaces.Interface>`
                    
                    

                    """

                    _prefix = 'ipv4-mfwd-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        self.parent = None
                        self.interface = YList()
                        self.interface.parent = self
                        self.interface.name = 'interface'


                    class Interface(object):
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
                            self.parent = None
                            self.interface_name = None
                            self.boundary = None
                            self.enable_on_interface = None
                            self.ttl_threshold = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.interface_name is None:
                                raise YPYModelError('Key property interface_name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-mfwd-cfg:interface[Cisco-IOS-XR-ipv4-mfwd-cfg:interface-name = ' + str(self.interface_name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.interface_name is not None:
                                return True

                            if self.boundary is not None:
                                return True

                            if self.enable_on_interface is not None:
                                return True

                            if self.ttl_threshold is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_mfwd_cfg as meta
                            return meta._meta_table['Mfwd.Vrfs.Vrf.Ipv6.Interfaces.Interface']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-mfwd-cfg:interfaces'

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
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_mfwd_cfg as meta
                        return meta._meta_table['Mfwd.Vrfs.Vrf.Ipv6.Interfaces']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-mfwd-cfg:ipv6'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.accounting is not None:
                        return True

                    if self.enable_on_all_interfaces is not None:
                        return True

                    if self.interfaces is not None and self.interfaces._has_data():
                        return True

                    if self.log_traps is not None:
                        return True

                    if self.multicast_forwarding is not None:
                        return True

                    if self.rate_per_route is not None:
                        return True

                    if self.static_rpf_rules is not None and self.static_rpf_rules._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_mfwd_cfg as meta
                    return meta._meta_table['Mfwd.Vrfs.Vrf.Ipv6']['meta_info']


            class Ipv4(object):
                """
                VRF table for IPV4 commands
                
                .. attribute:: accounting
                
                	Per\-prefix accounting mode
                	**type**\:   :py:class:`AccountingModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg.AccountingModeEnum>`
                
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
                    self.parent = None
                    self.accounting = None
                    self.enable_on_all_interfaces = None
                    self.interfaces = Mfwd.Vrfs.Vrf.Ipv4.Interfaces()
                    self.interfaces.parent = self
                    self.log_traps = None
                    self.multicast_forwarding = None
                    self.rate_per_route = None
                    self.static_rpf_rules = Mfwd.Vrfs.Vrf.Ipv4.StaticRpfRules()
                    self.static_rpf_rules.parent = self


                class StaticRpfRules(object):
                    """
                    Configure a static RPF rule for a given prefix
                    
                    .. attribute:: static_rpf_rule
                    
                    	RPF prefix address and mask
                    	**type**\: list of    :py:class:`StaticRpfRule <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg.Mfwd.Vrfs.Vrf.Ipv4.StaticRpfRules.StaticRpfRule>`
                    
                    

                    """

                    _prefix = 'ipv4-mfwd-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        self.parent = None
                        self.static_rpf_rule = YList()
                        self.static_rpf_rule.parent = self
                        self.static_rpf_rule.name = 'static_rpf_rule'


                    class StaticRpfRule(object):
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
                            self.parent = None
                            self.address = None
                            self.prefix_mask = None
                            self.interface_name = None
                            self.neighbor_address = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.address is None:
                                raise YPYModelError('Key property address is None')
                            if self.prefix_mask is None:
                                raise YPYModelError('Key property prefix_mask is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-mfwd-cfg:static-rpf-rule[Cisco-IOS-XR-ipv4-mfwd-cfg:address = ' + str(self.address) + '][Cisco-IOS-XR-ipv4-mfwd-cfg:prefix-mask = ' + str(self.prefix_mask) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.address is not None:
                                return True

                            if self.prefix_mask is not None:
                                return True

                            if self.interface_name is not None:
                                return True

                            if self.neighbor_address is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_mfwd_cfg as meta
                            return meta._meta_table['Mfwd.Vrfs.Vrf.Ipv4.StaticRpfRules.StaticRpfRule']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-mfwd-cfg:static-rpf-rules'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.static_rpf_rule is not None:
                            for child_ref in self.static_rpf_rule:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_mfwd_cfg as meta
                        return meta._meta_table['Mfwd.Vrfs.Vrf.Ipv4.StaticRpfRules']['meta_info']


                class Interfaces(object):
                    """
                    Interface\-level Configuration
                    
                    .. attribute:: interface
                    
                    	The name of the interface
                    	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_mfwd_cfg.Mfwd.Vrfs.Vrf.Ipv4.Interfaces.Interface>`
                    
                    

                    """

                    _prefix = 'ipv4-mfwd-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        self.parent = None
                        self.interface = YList()
                        self.interface.parent = self
                        self.interface.name = 'interface'


                    class Interface(object):
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
                            self.parent = None
                            self.interface_name = None
                            self.boundary = None
                            self.enable_on_interface = None
                            self.ttl_threshold = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.interface_name is None:
                                raise YPYModelError('Key property interface_name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-mfwd-cfg:interface[Cisco-IOS-XR-ipv4-mfwd-cfg:interface-name = ' + str(self.interface_name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.interface_name is not None:
                                return True

                            if self.boundary is not None:
                                return True

                            if self.enable_on_interface is not None:
                                return True

                            if self.ttl_threshold is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_mfwd_cfg as meta
                            return meta._meta_table['Mfwd.Vrfs.Vrf.Ipv4.Interfaces.Interface']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-mfwd-cfg:interfaces'

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
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_mfwd_cfg as meta
                        return meta._meta_table['Mfwd.Vrfs.Vrf.Ipv4.Interfaces']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-mfwd-cfg:ipv4'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.accounting is not None:
                        return True

                    if self.enable_on_all_interfaces is not None:
                        return True

                    if self.interfaces is not None and self.interfaces._has_data():
                        return True

                    if self.log_traps is not None:
                        return True

                    if self.multicast_forwarding is not None:
                        return True

                    if self.rate_per_route is not None:
                        return True

                    if self.static_rpf_rules is not None and self.static_rpf_rules._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_mfwd_cfg as meta
                    return meta._meta_table['Mfwd.Vrfs.Vrf.Ipv4']['meta_info']

            @property
            def _common_path(self):
                if self.vrf_name is None:
                    raise YPYModelError('Key property vrf_name is None')

                return '/Cisco-IOS-XR-ipv4-mfwd-cfg:mfwd/Cisco-IOS-XR-ipv4-mfwd-cfg:vrfs/Cisco-IOS-XR-ipv4-mfwd-cfg:vrf[Cisco-IOS-XR-ipv4-mfwd-cfg:vrf-name = ' + str(self.vrf_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.vrf_name is not None:
                    return True

                if self.ipv4 is not None and self.ipv4._has_data():
                    return True

                if self.ipv6 is not None and self.ipv6._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_mfwd_cfg as meta
                return meta._meta_table['Mfwd.Vrfs.Vrf']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv4-mfwd-cfg:mfwd/Cisco-IOS-XR-ipv4-mfwd-cfg:vrfs'

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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_mfwd_cfg as meta
            return meta._meta_table['Mfwd.Vrfs']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ipv4-mfwd-cfg:mfwd'

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
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_mfwd_cfg as meta
        return meta._meta_table['Mfwd']['meta_info']


