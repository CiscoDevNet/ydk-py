""" Cisco_IOS_XR_ipv4_vrrp_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv4\-vrrp package configuration.

This module contains definitions
for the following management objects\:
  vrrp\: VRRP configuration

This YANG module augments the
  Cisco\-IOS\-XR\-snmp\-agent\-cfg
module with configuration data.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class Vrrp(object):
    """
    VRRP configuration
    
    .. attribute:: interfaces
    
    	Interface configuration table
    	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces>`
    
    .. attribute:: logging
    
    	VRRP logging options
    	**type**\:   :py:class:`Logging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Logging>`
    
    

    """

    _prefix = 'ipv4-vrrp-cfg'
    _revision = '2016-12-16'

    def __init__(self):
        self.interfaces = Vrrp.Interfaces()
        self.interfaces.parent = self
        self.logging = Vrrp.Logging()
        self.logging.parent = self


    class Logging(object):
        """
        VRRP logging options
        
        .. attribute:: state_change_disable
        
        	VRRP state change IOS messages disable
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'ipv4-vrrp-cfg'
        _revision = '2016-12-16'

        def __init__(self):
            self.parent = None
            self.state_change_disable = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv4-vrrp-cfg:vrrp/Cisco-IOS-XR-ipv4-vrrp-cfg:logging'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.state_change_disable is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_cfg as meta
            return meta._meta_table['Vrrp.Logging']['meta_info']


    class Interfaces(object):
        """
        Interface configuration table
        
        .. attribute:: interface
        
        	The interface being configured
        	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface>`
        
        

        """

        _prefix = 'ipv4-vrrp-cfg'
        _revision = '2016-12-16'

        def __init__(self):
            self.parent = None
            self.interface = YList()
            self.interface.parent = self
            self.interface.name = 'interface'


        class Interface(object):
            """
            The interface being configured
            
            .. attribute:: interface_name  <key>
            
            	Interface name to configure
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: bfd
            
            	BFD configuration
            	**type**\:   :py:class:`Bfd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Bfd>`
            
            .. attribute:: delay
            
            	Minimum and Reload Delay
            	**type**\:   :py:class:`Delay <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Delay>`
            
            .. attribute:: ipv4
            
            	IPv4 VRRP configuration
            	**type**\:   :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4>`
            
            .. attribute:: ipv6
            
            	IPv6 VRRP configuration
            	**type**\:   :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv6>`
            
            .. attribute:: mac_refresh
            
            	VRRP Slave MAC\-refresh rate in seconds
            	**type**\:  int
            
            	**range:** 0..10000
            
            	**units**\: second
            
            	**default value**\: 60
            
            

            """

            _prefix = 'ipv4-vrrp-cfg'
            _revision = '2016-12-16'

            def __init__(self):
                self.parent = None
                self.interface_name = None
                self.bfd = Vrrp.Interfaces.Interface.Bfd()
                self.bfd.parent = self
                self.delay = Vrrp.Interfaces.Interface.Delay()
                self.delay.parent = self
                self.ipv4 = Vrrp.Interfaces.Interface.Ipv4()
                self.ipv4.parent = self
                self.ipv6 = Vrrp.Interfaces.Interface.Ipv6()
                self.ipv6.parent = self
                self.mac_refresh = None


            class Ipv6(object):
                """
                IPv6 VRRP configuration
                
                .. attribute:: slave_virtual_routers
                
                	The VRRP slave group configuration table
                	**type**\:   :py:class:`SlaveVirtualRouters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters>`
                
                .. attribute:: version3
                
                	Version 3 VRRP configuration
                	**type**\:   :py:class:`Version3 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv6.Version3>`
                
                

                """

                _prefix = 'ipv4-vrrp-cfg'
                _revision = '2016-12-16'

                def __init__(self):
                    self.parent = None
                    self.slave_virtual_routers = Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters()
                    self.slave_virtual_routers.parent = self
                    self.version3 = Vrrp.Interfaces.Interface.Ipv6.Version3()
                    self.version3.parent = self


                class Version3(object):
                    """
                    Version 3 VRRP configuration
                    
                    .. attribute:: virtual_routers
                    
                    	The VRRP virtual router configuration table
                    	**type**\:   :py:class:`VirtualRouters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters>`
                    
                    

                    """

                    _prefix = 'ipv4-vrrp-cfg'
                    _revision = '2016-12-16'

                    def __init__(self):
                        self.parent = None
                        self.virtual_routers = Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters()
                        self.virtual_routers.parent = self


                    class VirtualRouters(object):
                        """
                        The VRRP virtual router configuration table
                        
                        .. attribute:: virtual_router
                        
                        	The VRRP virtual router being configured
                        	**type**\: list of    :py:class:`VirtualRouter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter>`
                        
                        

                        """

                        _prefix = 'ipv4-vrrp-cfg'
                        _revision = '2016-12-16'

                        def __init__(self):
                            self.parent = None
                            self.virtual_router = YList()
                            self.virtual_router.parent = self
                            self.virtual_router.name = 'virtual_router'


                        class VirtualRouter(object):
                            """
                            The VRRP virtual router being configured
                            
                            .. attribute:: vr_id  <key>
                            
                            	VRID Virtual Router Identifier
                            	**type**\:  int
                            
                            	**range:** 1..255
                            
                            .. attribute:: accept_mode_disable
                            
                            	Disable Accept Mode for this virtual IPAddress
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: bfd
                            
                            	Enable use of Bidirectional Forwarding Detection for this IP
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: global_ipv6_addresses
                            
                            	The table of VRRP virtual global IPv6 addresses
                            	**type**\:   :py:class:`GlobalIpv6Addresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.GlobalIpv6Addresses>`
                            
                            .. attribute:: link_local_ipv6_address
                            
                            	The VRRP IPv6 virtual linklocal address
                            	**type**\:   :py:class:`LinkLocalIpv6Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.LinkLocalIpv6Address>`
                            
                            .. attribute:: preempt
                            
                            	Preempt Master router if higher priority
                            	**type**\:  int
                            
                            	**range:** 0..3600
                            
                            	**default value**\: 0
                            
                            .. attribute:: priority
                            
                            	Priority value
                            	**type**\:  int
                            
                            	**range:** 1..254
                            
                            	**default value**\: 100
                            
                            .. attribute:: session_name
                            
                            	VRRP Session Name
                            	**type**\:  str
                            
                            	**length:** 1..16
                            
                            .. attribute:: timer
                            
                            	Set advertisement timer
                            	**type**\:   :py:class:`Timer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.Timer>`
                            
                            .. attribute:: tracked_objects
                            
                            	Track an object, reducing priority if it goes down
                            	**type**\:   :py:class:`TrackedObjects <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.TrackedObjects>`
                            
                            .. attribute:: tracks
                            
                            	Track an item, reducing priority if it goes down
                            	**type**\:   :py:class:`Tracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.Tracks>`
                            
                            

                            """

                            _prefix = 'ipv4-vrrp-cfg'
                            _revision = '2016-12-16'

                            def __init__(self):
                                self.parent = None
                                self.vr_id = None
                                self.accept_mode_disable = None
                                self.bfd = None
                                self.global_ipv6_addresses = Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.GlobalIpv6Addresses()
                                self.global_ipv6_addresses.parent = self
                                self.link_local_ipv6_address = Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.LinkLocalIpv6Address()
                                self.link_local_ipv6_address.parent = self
                                self.preempt = None
                                self.priority = None
                                self.session_name = None
                                self.timer = Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.Timer()
                                self.timer.parent = self
                                self.tracked_objects = Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.TrackedObjects()
                                self.tracked_objects.parent = self
                                self.tracks = Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.Tracks()
                                self.tracks.parent = self


                            class GlobalIpv6Addresses(object):
                                """
                                The table of VRRP virtual global IPv6
                                addresses
                                
                                .. attribute:: global_ipv6_address
                                
                                	A VRRP virtual global IPv6 IP address
                                	**type**\: list of    :py:class:`GlobalIpv6Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.GlobalIpv6Addresses.GlobalIpv6Address>`
                                
                                

                                """

                                _prefix = 'ipv4-vrrp-cfg'
                                _revision = '2016-12-16'

                                def __init__(self):
                                    self.parent = None
                                    self.global_ipv6_address = YList()
                                    self.global_ipv6_address.parent = self
                                    self.global_ipv6_address.name = 'global_ipv6_address'


                                class GlobalIpv6Address(object):
                                    """
                                    A VRRP virtual global IPv6 IP address
                                    
                                    .. attribute:: ip_address  <key>
                                    
                                    	VRRP virtual global IPv6 address
                                    	**type**\: one of the below types:
                                    
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    
                                    ----
                                    	**type**\:  str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    
                                    ----
                                    

                                    """

                                    _prefix = 'ipv4-vrrp-cfg'
                                    _revision = '2016-12-16'

                                    def __init__(self):
                                        self.parent = None
                                        self.ip_address = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.ip_address is None:
                                            raise YPYModelError('Key property ip_address is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-vrrp-cfg:global-ipv6-address[Cisco-IOS-XR-ipv4-vrrp-cfg:ip-address = ' + str(self.ip_address) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.ip_address is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_cfg as meta
                                        return meta._meta_table['Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.GlobalIpv6Addresses.GlobalIpv6Address']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-vrrp-cfg:global-ipv6-addresses'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.global_ipv6_address is not None:
                                        for child_ref in self.global_ipv6_address:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_cfg as meta
                                    return meta._meta_table['Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.GlobalIpv6Addresses']['meta_info']


                            class Tracks(object):
                                """
                                Track an item, reducing priority if it
                                goes down
                                
                                .. attribute:: track
                                
                                	Object to be tracked
                                	**type**\: list of    :py:class:`Track <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.Tracks.Track>`
                                
                                

                                """

                                _prefix = 'ipv4-vrrp-cfg'
                                _revision = '2016-12-16'

                                def __init__(self):
                                    self.parent = None
                                    self.track = YList()
                                    self.track.parent = self
                                    self.track.name = 'track'


                                class Track(object):
                                    """
                                    Object to be tracked
                                    
                                    .. attribute:: interface_name  <key>
                                    
                                    	Object to be tracked, interface name for interfaces
                                    	**type**\:  str
                                    
                                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                    
                                    .. attribute:: priority
                                    
                                    	Priority decrement
                                    	**type**\:  int
                                    
                                    	**range:** 1..254
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'ipv4-vrrp-cfg'
                                    _revision = '2016-12-16'

                                    def __init__(self):
                                        self.parent = None
                                        self.interface_name = None
                                        self.priority = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.interface_name is None:
                                            raise YPYModelError('Key property interface_name is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-vrrp-cfg:track[Cisco-IOS-XR-ipv4-vrrp-cfg:interface-name = ' + str(self.interface_name) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.interface_name is not None:
                                            return True

                                        if self.priority is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_cfg as meta
                                        return meta._meta_table['Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.Tracks.Track']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-vrrp-cfg:tracks'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.track is not None:
                                        for child_ref in self.track:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_cfg as meta
                                    return meta._meta_table['Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.Tracks']['meta_info']


                            class Timer(object):
                                """
                                Set advertisement timer
                                
                                .. attribute:: advertisement_time_in_msec
                                
                                	Advertisement time in milliseconds
                                	**type**\:  int
                                
                                	**range:** 100..40950
                                
                                	**units**\: millisecond
                                
                                .. attribute:: advertisement_time_in_sec
                                
                                	Advertisement time in seconds
                                	**type**\:  int
                                
                                	**range:** 1..40
                                
                                	**units**\: second
                                
                                .. attribute:: forced
                                
                                	TRUE \- Force configured timer values to be used, required when configured in milliseconds
                                	**type**\:  bool
                                
                                	**default value**\: false
                                
                                .. attribute:: in_msec
                                
                                	TRUE \- Advertise time configured in milliseconds, FALSE \- Advertise time configured in seconds
                                	**type**\:  bool
                                
                                	**default value**\: false
                                
                                

                                """

                                _prefix = 'ipv4-vrrp-cfg'
                                _revision = '2016-12-16'

                                def __init__(self):
                                    self.parent = None
                                    self.advertisement_time_in_msec = None
                                    self.advertisement_time_in_sec = None
                                    self.forced = None
                                    self.in_msec = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-vrrp-cfg:timer'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.advertisement_time_in_msec is not None:
                                        return True

                                    if self.advertisement_time_in_sec is not None:
                                        return True

                                    if self.forced is not None:
                                        return True

                                    if self.in_msec is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_cfg as meta
                                    return meta._meta_table['Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.Timer']['meta_info']


                            class TrackedObjects(object):
                                """
                                Track an object, reducing priority if it
                                goes down
                                
                                .. attribute:: tracked_object
                                
                                	Object to be tracked
                                	**type**\: list of    :py:class:`TrackedObject <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.TrackedObjects.TrackedObject>`
                                
                                

                                """

                                _prefix = 'ipv4-vrrp-cfg'
                                _revision = '2016-12-16'

                                def __init__(self):
                                    self.parent = None
                                    self.tracked_object = YList()
                                    self.tracked_object.parent = self
                                    self.tracked_object.name = 'tracked_object'


                                class TrackedObject(object):
                                    """
                                    Object to be tracked
                                    
                                    .. attribute:: object_name  <key>
                                    
                                    	Object to be tracked, interface name for interfaces
                                    	**type**\:  str
                                    
                                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                    
                                    .. attribute:: priority_decrement
                                    
                                    	Priority decrement
                                    	**type**\:  int
                                    
                                    	**range:** 1..254
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'ipv4-vrrp-cfg'
                                    _revision = '2016-12-16'

                                    def __init__(self):
                                        self.parent = None
                                        self.object_name = None
                                        self.priority_decrement = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.object_name is None:
                                            raise YPYModelError('Key property object_name is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-vrrp-cfg:tracked-object[Cisco-IOS-XR-ipv4-vrrp-cfg:object-name = ' + str(self.object_name) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.object_name is not None:
                                            return True

                                        if self.priority_decrement is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_cfg as meta
                                        return meta._meta_table['Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.TrackedObjects.TrackedObject']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-vrrp-cfg:tracked-objects'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.tracked_object is not None:
                                        for child_ref in self.tracked_object:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_cfg as meta
                                    return meta._meta_table['Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.TrackedObjects']['meta_info']


                            class LinkLocalIpv6Address(object):
                                """
                                The VRRP IPv6 virtual linklocal address
                                
                                .. attribute:: auto_configure
                                
                                	TRUE if the virtual linklocal address is to be autoconfigured FALSE if an IPv6 virtual linklocal address is configured
                                	**type**\:  bool
                                
                                	**default value**\: false
                                
                                .. attribute:: ip_address
                                
                                	VRRP IPv6 virtual linklocal address
                                	**type**\: one of the below types:
                                
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                
                                ----
                                	**type**\:  str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                
                                ----
                                

                                """

                                _prefix = 'ipv4-vrrp-cfg'
                                _revision = '2016-12-16'

                                def __init__(self):
                                    self.parent = None
                                    self.auto_configure = None
                                    self.ip_address = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-vrrp-cfg:link-local-ipv6-address'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.auto_configure is not None:
                                        return True

                                    if self.ip_address is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_cfg as meta
                                    return meta._meta_table['Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.LinkLocalIpv6Address']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.vr_id is None:
                                    raise YPYModelError('Key property vr_id is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-vrrp-cfg:virtual-router[Cisco-IOS-XR-ipv4-vrrp-cfg:vr-id = ' + str(self.vr_id) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.vr_id is not None:
                                    return True

                                if self.accept_mode_disable is not None:
                                    return True

                                if self.bfd is not None:
                                    return True

                                if self.global_ipv6_addresses is not None and self.global_ipv6_addresses._has_data():
                                    return True

                                if self.link_local_ipv6_address is not None and self.link_local_ipv6_address._has_data():
                                    return True

                                if self.preempt is not None:
                                    return True

                                if self.priority is not None:
                                    return True

                                if self.session_name is not None:
                                    return True

                                if self.timer is not None and self.timer._has_data():
                                    return True

                                if self.tracked_objects is not None and self.tracked_objects._has_data():
                                    return True

                                if self.tracks is not None and self.tracks._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_cfg as meta
                                return meta._meta_table['Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-vrrp-cfg:virtual-routers'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.virtual_router is not None:
                                for child_ref in self.virtual_router:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_cfg as meta
                            return meta._meta_table['Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-vrrp-cfg:version3'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.virtual_routers is not None and self.virtual_routers._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_cfg as meta
                        return meta._meta_table['Vrrp.Interfaces.Interface.Ipv6.Version3']['meta_info']


                class SlaveVirtualRouters(object):
                    """
                    The VRRP slave group configuration table
                    
                    .. attribute:: slave_virtual_router
                    
                    	The VRRP slave being configured
                    	**type**\: list of    :py:class:`SlaveVirtualRouter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter>`
                    
                    

                    """

                    _prefix = 'ipv4-vrrp-cfg'
                    _revision = '2016-12-16'

                    def __init__(self):
                        self.parent = None
                        self.slave_virtual_router = YList()
                        self.slave_virtual_router.parent = self
                        self.slave_virtual_router.name = 'slave_virtual_router'


                    class SlaveVirtualRouter(object):
                        """
                        The VRRP slave being configured
                        
                        .. attribute:: slave_virtual_router_id  <key>
                        
                        	Virtual Router ID
                        	**type**\:  int
                        
                        	**range:** 1..255
                        
                        .. attribute:: accept_mode_disable
                        
                        	Disable Accept Mode for this virtual IPAddress
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: follow
                        
                        	VRRP Session name for this slave to follow
                        	**type**\:  str
                        
                        .. attribute:: global_ipv6_addresses
                        
                        	The table of VRRP virtual global IPv6 addresses
                        	**type**\:   :py:class:`GlobalIpv6Addresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter.GlobalIpv6Addresses>`
                        
                        .. attribute:: link_local_ipv6_address
                        
                        	The VRRP IPv6 virtual linklocal address
                        	**type**\:   :py:class:`LinkLocalIpv6Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter.LinkLocalIpv6Address>`
                        
                        

                        """

                        _prefix = 'ipv4-vrrp-cfg'
                        _revision = '2016-12-16'

                        def __init__(self):
                            self.parent = None
                            self.slave_virtual_router_id = None
                            self.accept_mode_disable = None
                            self.follow = None
                            self.global_ipv6_addresses = Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter.GlobalIpv6Addresses()
                            self.global_ipv6_addresses.parent = self
                            self.link_local_ipv6_address = Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter.LinkLocalIpv6Address()
                            self.link_local_ipv6_address.parent = self


                        class LinkLocalIpv6Address(object):
                            """
                            The VRRP IPv6 virtual linklocal address
                            
                            .. attribute:: auto_configure
                            
                            	TRUE if the virtual linklocal address is to be autoconfigured FALSE if an IPv6 virtual linklocal address is configured
                            	**type**\:  bool
                            
                            	**default value**\: false
                            
                            .. attribute:: ip_address
                            
                            	VRRP IPv6 virtual linklocal address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            

                            """

                            _prefix = 'ipv4-vrrp-cfg'
                            _revision = '2016-12-16'

                            def __init__(self):
                                self.parent = None
                                self.auto_configure = None
                                self.ip_address = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-vrrp-cfg:link-local-ipv6-address'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.auto_configure is not None:
                                    return True

                                if self.ip_address is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_cfg as meta
                                return meta._meta_table['Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter.LinkLocalIpv6Address']['meta_info']


                        class GlobalIpv6Addresses(object):
                            """
                            The table of VRRP virtual global IPv6
                            addresses
                            
                            .. attribute:: global_ipv6_address
                            
                            	A VRRP virtual global IPv6 IP address
                            	**type**\: list of    :py:class:`GlobalIpv6Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter.GlobalIpv6Addresses.GlobalIpv6Address>`
                            
                            

                            """

                            _prefix = 'ipv4-vrrp-cfg'
                            _revision = '2016-12-16'

                            def __init__(self):
                                self.parent = None
                                self.global_ipv6_address = YList()
                                self.global_ipv6_address.parent = self
                                self.global_ipv6_address.name = 'global_ipv6_address'


                            class GlobalIpv6Address(object):
                                """
                                A VRRP virtual global IPv6 IP address
                                
                                .. attribute:: ip_address  <key>
                                
                                	VRRP virtual global IPv6 address
                                	**type**\: one of the below types:
                                
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                
                                ----
                                	**type**\:  str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                
                                ----
                                

                                """

                                _prefix = 'ipv4-vrrp-cfg'
                                _revision = '2016-12-16'

                                def __init__(self):
                                    self.parent = None
                                    self.ip_address = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.ip_address is None:
                                        raise YPYModelError('Key property ip_address is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-vrrp-cfg:global-ipv6-address[Cisco-IOS-XR-ipv4-vrrp-cfg:ip-address = ' + str(self.ip_address) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.ip_address is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_cfg as meta
                                    return meta._meta_table['Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter.GlobalIpv6Addresses.GlobalIpv6Address']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-vrrp-cfg:global-ipv6-addresses'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.global_ipv6_address is not None:
                                    for child_ref in self.global_ipv6_address:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_cfg as meta
                                return meta._meta_table['Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter.GlobalIpv6Addresses']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.slave_virtual_router_id is None:
                                raise YPYModelError('Key property slave_virtual_router_id is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-vrrp-cfg:slave-virtual-router[Cisco-IOS-XR-ipv4-vrrp-cfg:slave-virtual-router-id = ' + str(self.slave_virtual_router_id) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.slave_virtual_router_id is not None:
                                return True

                            if self.accept_mode_disable is not None:
                                return True

                            if self.follow is not None:
                                return True

                            if self.global_ipv6_addresses is not None and self.global_ipv6_addresses._has_data():
                                return True

                            if self.link_local_ipv6_address is not None and self.link_local_ipv6_address._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_cfg as meta
                            return meta._meta_table['Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-vrrp-cfg:slave-virtual-routers'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.slave_virtual_router is not None:
                            for child_ref in self.slave_virtual_router:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_cfg as meta
                        return meta._meta_table['Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-vrrp-cfg:ipv6'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.slave_virtual_routers is not None and self.slave_virtual_routers._has_data():
                        return True

                    if self.version3 is not None and self.version3._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_cfg as meta
                    return meta._meta_table['Vrrp.Interfaces.Interface.Ipv6']['meta_info']


            class Delay(object):
                """
                Minimum and Reload Delay
                
                .. attribute:: min_delay
                
                	Minimum delay in seconds
                	**type**\:  int
                
                	**range:** 0..10000
                
                	**units**\: second
                
                .. attribute:: reload_delay
                
                	Reload delay in seconds
                	**type**\:  int
                
                	**range:** 0..10000
                
                	**units**\: second
                
                

                """

                _prefix = 'ipv4-vrrp-cfg'
                _revision = '2016-12-16'

                def __init__(self):
                    self.parent = None
                    self.min_delay = None
                    self.reload_delay = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-vrrp-cfg:delay'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.min_delay is not None:
                        return True

                    if self.reload_delay is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_cfg as meta
                    return meta._meta_table['Vrrp.Interfaces.Interface.Delay']['meta_info']


            class Ipv4(object):
                """
                IPv4 VRRP configuration
                
                .. attribute:: slave_virtual_routers
                
                	The VRRP slave group configuration table
                	**type**\:   :py:class:`SlaveVirtualRouters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters>`
                
                .. attribute:: version2
                
                	Version 2 VRRP configuration
                	**type**\:   :py:class:`Version2 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.Version2>`
                
                .. attribute:: version3
                
                	Version 3 VRRP configuration
                	**type**\:   :py:class:`Version3 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.Version3>`
                
                

                """

                _prefix = 'ipv4-vrrp-cfg'
                _revision = '2016-12-16'

                def __init__(self):
                    self.parent = None
                    self.slave_virtual_routers = Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters()
                    self.slave_virtual_routers.parent = self
                    self.version2 = Vrrp.Interfaces.Interface.Ipv4.Version2()
                    self.version2.parent = self
                    self.version3 = Vrrp.Interfaces.Interface.Ipv4.Version3()
                    self.version3.parent = self


                class Version3(object):
                    """
                    Version 3 VRRP configuration
                    
                    .. attribute:: virtual_routers
                    
                    	The VRRP virtual router configuration table
                    	**type**\:   :py:class:`VirtualRouters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters>`
                    
                    

                    """

                    _prefix = 'ipv4-vrrp-cfg'
                    _revision = '2016-12-16'

                    def __init__(self):
                        self.parent = None
                        self.virtual_routers = Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters()
                        self.virtual_routers.parent = self


                    class VirtualRouters(object):
                        """
                        The VRRP virtual router configuration table
                        
                        .. attribute:: virtual_router
                        
                        	The VRRP virtual router being configured
                        	**type**\: list of    :py:class:`VirtualRouter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter>`
                        
                        

                        """

                        _prefix = 'ipv4-vrrp-cfg'
                        _revision = '2016-12-16'

                        def __init__(self):
                            self.parent = None
                            self.virtual_router = YList()
                            self.virtual_router.parent = self
                            self.virtual_router.name = 'virtual_router'


                        class VirtualRouter(object):
                            """
                            The VRRP virtual router being configured
                            
                            .. attribute:: vr_id  <key>
                            
                            	VRID Virtual Router Identifier
                            	**type**\:  int
                            
                            	**range:** 1..255
                            
                            .. attribute:: accept_mode_disable
                            
                            	Disable Accept Mode for this virtual IPAddress
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: bfd
                            
                            	Enable use of Bidirectional Forwarding Detection for this IP
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: preempt
                            
                            	Preempt Master router if higher priority
                            	**type**\:  int
                            
                            	**range:** 0..3600
                            
                            	**default value**\: 0
                            
                            .. attribute:: primary_ipv4_address
                            
                            	The Primary VRRP IPv4 address
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: priority
                            
                            	Priority value
                            	**type**\:  int
                            
                            	**range:** 1..254
                            
                            	**default value**\: 100
                            
                            .. attribute:: secondary_ipv4_addresses
                            
                            	The table of VRRP secondary IPv4 addresses
                            	**type**\:   :py:class:`SecondaryIpv4Addresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses>`
                            
                            .. attribute:: session_name
                            
                            	VRRP Session Name
                            	**type**\:  str
                            
                            	**length:** 1..16
                            
                            .. attribute:: timer
                            
                            	Set advertisement timer
                            	**type**\:   :py:class:`Timer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.Timer>`
                            
                            .. attribute:: tracked_objects
                            
                            	Track an object, reducing priority if it goes down
                            	**type**\:   :py:class:`TrackedObjects <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.TrackedObjects>`
                            
                            .. attribute:: tracks
                            
                            	Track an item, reducing priority if it goes down
                            	**type**\:   :py:class:`Tracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.Tracks>`
                            
                            

                            """

                            _prefix = 'ipv4-vrrp-cfg'
                            _revision = '2016-12-16'

                            def __init__(self):
                                self.parent = None
                                self.vr_id = None
                                self.accept_mode_disable = None
                                self.bfd = None
                                self.preempt = None
                                self.primary_ipv4_address = None
                                self.priority = None
                                self.secondary_ipv4_addresses = Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses()
                                self.secondary_ipv4_addresses.parent = self
                                self.session_name = None
                                self.timer = Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.Timer()
                                self.timer.parent = self
                                self.tracked_objects = Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.TrackedObjects()
                                self.tracked_objects.parent = self
                                self.tracks = Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.Tracks()
                                self.tracks.parent = self


                            class Timer(object):
                                """
                                Set advertisement timer
                                
                                .. attribute:: advertisement_time_in_msec
                                
                                	Advertisement time in milliseconds
                                	**type**\:  int
                                
                                	**range:** 100..40950
                                
                                	**units**\: millisecond
                                
                                .. attribute:: advertisement_time_in_sec
                                
                                	Advertisement time in seconds
                                	**type**\:  int
                                
                                	**range:** 1..40
                                
                                	**units**\: second
                                
                                .. attribute:: forced
                                
                                	TRUE \- Force configured timer values to be used, required when configured in milliseconds
                                	**type**\:  bool
                                
                                	**default value**\: false
                                
                                .. attribute:: in_msec
                                
                                	TRUE \- Advertise time configured in milliseconds, FALSE \- Advertise time configured in seconds
                                	**type**\:  bool
                                
                                	**default value**\: false
                                
                                

                                """

                                _prefix = 'ipv4-vrrp-cfg'
                                _revision = '2016-12-16'

                                def __init__(self):
                                    self.parent = None
                                    self.advertisement_time_in_msec = None
                                    self.advertisement_time_in_sec = None
                                    self.forced = None
                                    self.in_msec = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-vrrp-cfg:timer'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.advertisement_time_in_msec is not None:
                                        return True

                                    if self.advertisement_time_in_sec is not None:
                                        return True

                                    if self.forced is not None:
                                        return True

                                    if self.in_msec is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_cfg as meta
                                    return meta._meta_table['Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.Timer']['meta_info']


                            class SecondaryIpv4Addresses(object):
                                """
                                The table of VRRP secondary IPv4 addresses
                                
                                .. attribute:: secondary_ipv4_address
                                
                                	A VRRP secondary IPv4 address
                                	**type**\: list of    :py:class:`SecondaryIpv4Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses.SecondaryIpv4Address>`
                                
                                

                                """

                                _prefix = 'ipv4-vrrp-cfg'
                                _revision = '2016-12-16'

                                def __init__(self):
                                    self.parent = None
                                    self.secondary_ipv4_address = YList()
                                    self.secondary_ipv4_address.parent = self
                                    self.secondary_ipv4_address.name = 'secondary_ipv4_address'


                                class SecondaryIpv4Address(object):
                                    """
                                    A VRRP secondary IPv4 address
                                    
                                    .. attribute:: ip_address  <key>
                                    
                                    	VRRP Secondary IPv4 address
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    

                                    """

                                    _prefix = 'ipv4-vrrp-cfg'
                                    _revision = '2016-12-16'

                                    def __init__(self):
                                        self.parent = None
                                        self.ip_address = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.ip_address is None:
                                            raise YPYModelError('Key property ip_address is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-vrrp-cfg:secondary-ipv4-address[Cisco-IOS-XR-ipv4-vrrp-cfg:ip-address = ' + str(self.ip_address) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.ip_address is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_cfg as meta
                                        return meta._meta_table['Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses.SecondaryIpv4Address']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-vrrp-cfg:secondary-ipv4-addresses'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.secondary_ipv4_address is not None:
                                        for child_ref in self.secondary_ipv4_address:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_cfg as meta
                                    return meta._meta_table['Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses']['meta_info']


                            class TrackedObjects(object):
                                """
                                Track an object, reducing priority if it
                                goes down
                                
                                .. attribute:: tracked_object
                                
                                	Object to be tracked
                                	**type**\: list of    :py:class:`TrackedObject <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.TrackedObjects.TrackedObject>`
                                
                                

                                """

                                _prefix = 'ipv4-vrrp-cfg'
                                _revision = '2016-12-16'

                                def __init__(self):
                                    self.parent = None
                                    self.tracked_object = YList()
                                    self.tracked_object.parent = self
                                    self.tracked_object.name = 'tracked_object'


                                class TrackedObject(object):
                                    """
                                    Object to be tracked
                                    
                                    .. attribute:: object_name  <key>
                                    
                                    	Object to be tracked, interface name for interfaces
                                    	**type**\:  str
                                    
                                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                    
                                    .. attribute:: priority_decrement
                                    
                                    	Priority decrement
                                    	**type**\:  int
                                    
                                    	**range:** 1..254
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'ipv4-vrrp-cfg'
                                    _revision = '2016-12-16'

                                    def __init__(self):
                                        self.parent = None
                                        self.object_name = None
                                        self.priority_decrement = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.object_name is None:
                                            raise YPYModelError('Key property object_name is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-vrrp-cfg:tracked-object[Cisco-IOS-XR-ipv4-vrrp-cfg:object-name = ' + str(self.object_name) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.object_name is not None:
                                            return True

                                        if self.priority_decrement is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_cfg as meta
                                        return meta._meta_table['Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.TrackedObjects.TrackedObject']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-vrrp-cfg:tracked-objects'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.tracked_object is not None:
                                        for child_ref in self.tracked_object:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_cfg as meta
                                    return meta._meta_table['Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.TrackedObjects']['meta_info']


                            class Tracks(object):
                                """
                                Track an item, reducing priority if it
                                goes down
                                
                                .. attribute:: track
                                
                                	Object to be tracked
                                	**type**\: list of    :py:class:`Track <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.Tracks.Track>`
                                
                                

                                """

                                _prefix = 'ipv4-vrrp-cfg'
                                _revision = '2016-12-16'

                                def __init__(self):
                                    self.parent = None
                                    self.track = YList()
                                    self.track.parent = self
                                    self.track.name = 'track'


                                class Track(object):
                                    """
                                    Object to be tracked
                                    
                                    .. attribute:: interface_name  <key>
                                    
                                    	Object to be tracked, interface name for interfaces
                                    	**type**\:  str
                                    
                                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                    
                                    .. attribute:: priority
                                    
                                    	Priority decrement
                                    	**type**\:  int
                                    
                                    	**range:** 1..254
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'ipv4-vrrp-cfg'
                                    _revision = '2016-12-16'

                                    def __init__(self):
                                        self.parent = None
                                        self.interface_name = None
                                        self.priority = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.interface_name is None:
                                            raise YPYModelError('Key property interface_name is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-vrrp-cfg:track[Cisco-IOS-XR-ipv4-vrrp-cfg:interface-name = ' + str(self.interface_name) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.interface_name is not None:
                                            return True

                                        if self.priority is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_cfg as meta
                                        return meta._meta_table['Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.Tracks.Track']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-vrrp-cfg:tracks'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.track is not None:
                                        for child_ref in self.track:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_cfg as meta
                                    return meta._meta_table['Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.Tracks']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.vr_id is None:
                                    raise YPYModelError('Key property vr_id is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-vrrp-cfg:virtual-router[Cisco-IOS-XR-ipv4-vrrp-cfg:vr-id = ' + str(self.vr_id) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.vr_id is not None:
                                    return True

                                if self.accept_mode_disable is not None:
                                    return True

                                if self.bfd is not None:
                                    return True

                                if self.preempt is not None:
                                    return True

                                if self.primary_ipv4_address is not None:
                                    return True

                                if self.priority is not None:
                                    return True

                                if self.secondary_ipv4_addresses is not None and self.secondary_ipv4_addresses._has_data():
                                    return True

                                if self.session_name is not None:
                                    return True

                                if self.timer is not None and self.timer._has_data():
                                    return True

                                if self.tracked_objects is not None and self.tracked_objects._has_data():
                                    return True

                                if self.tracks is not None and self.tracks._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_cfg as meta
                                return meta._meta_table['Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-vrrp-cfg:virtual-routers'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.virtual_router is not None:
                                for child_ref in self.virtual_router:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_cfg as meta
                            return meta._meta_table['Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-vrrp-cfg:version3'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.virtual_routers is not None and self.virtual_routers._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_cfg as meta
                        return meta._meta_table['Vrrp.Interfaces.Interface.Ipv4.Version3']['meta_info']


                class SlaveVirtualRouters(object):
                    """
                    The VRRP slave group configuration table
                    
                    .. attribute:: slave_virtual_router
                    
                    	The VRRP slave being configured
                    	**type**\: list of    :py:class:`SlaveVirtualRouter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters.SlaveVirtualRouter>`
                    
                    

                    """

                    _prefix = 'ipv4-vrrp-cfg'
                    _revision = '2016-12-16'

                    def __init__(self):
                        self.parent = None
                        self.slave_virtual_router = YList()
                        self.slave_virtual_router.parent = self
                        self.slave_virtual_router.name = 'slave_virtual_router'


                    class SlaveVirtualRouter(object):
                        """
                        The VRRP slave being configured
                        
                        .. attribute:: slave_virtual_router_id  <key>
                        
                        	Virtual Router ID
                        	**type**\:  int
                        
                        	**range:** 1..255
                        
                        .. attribute:: accept_mode_disable
                        
                        	Disable Accept Mode for this virtual IPAddress
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: follow
                        
                        	VRRP Session name for this slave to follow
                        	**type**\:  str
                        
                        .. attribute:: primary_ipv4_address
                        
                        	The Primary VRRP IPv4 address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: secondary_ipv4_addresses
                        
                        	The table of VRRP secondary IPv4 addresses
                        	**type**\:   :py:class:`SecondaryIpv4Addresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters.SlaveVirtualRouter.SecondaryIpv4Addresses>`
                        
                        

                        """

                        _prefix = 'ipv4-vrrp-cfg'
                        _revision = '2016-12-16'

                        def __init__(self):
                            self.parent = None
                            self.slave_virtual_router_id = None
                            self.accept_mode_disable = None
                            self.follow = None
                            self.primary_ipv4_address = None
                            self.secondary_ipv4_addresses = Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters.SlaveVirtualRouter.SecondaryIpv4Addresses()
                            self.secondary_ipv4_addresses.parent = self


                        class SecondaryIpv4Addresses(object):
                            """
                            The table of VRRP secondary IPv4 addresses
                            
                            .. attribute:: secondary_ipv4_address
                            
                            	A VRRP secondary IPv4 address
                            	**type**\: list of    :py:class:`SecondaryIpv4Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters.SlaveVirtualRouter.SecondaryIpv4Addresses.SecondaryIpv4Address>`
                            
                            

                            """

                            _prefix = 'ipv4-vrrp-cfg'
                            _revision = '2016-12-16'

                            def __init__(self):
                                self.parent = None
                                self.secondary_ipv4_address = YList()
                                self.secondary_ipv4_address.parent = self
                                self.secondary_ipv4_address.name = 'secondary_ipv4_address'


                            class SecondaryIpv4Address(object):
                                """
                                A VRRP secondary IPv4 address
                                
                                .. attribute:: ip_address  <key>
                                
                                	VRRP Secondary IPv4 address
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'ipv4-vrrp-cfg'
                                _revision = '2016-12-16'

                                def __init__(self):
                                    self.parent = None
                                    self.ip_address = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.ip_address is None:
                                        raise YPYModelError('Key property ip_address is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-vrrp-cfg:secondary-ipv4-address[Cisco-IOS-XR-ipv4-vrrp-cfg:ip-address = ' + str(self.ip_address) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.ip_address is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_cfg as meta
                                    return meta._meta_table['Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters.SlaveVirtualRouter.SecondaryIpv4Addresses.SecondaryIpv4Address']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-vrrp-cfg:secondary-ipv4-addresses'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.secondary_ipv4_address is not None:
                                    for child_ref in self.secondary_ipv4_address:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_cfg as meta
                                return meta._meta_table['Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters.SlaveVirtualRouter.SecondaryIpv4Addresses']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.slave_virtual_router_id is None:
                                raise YPYModelError('Key property slave_virtual_router_id is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-vrrp-cfg:slave-virtual-router[Cisco-IOS-XR-ipv4-vrrp-cfg:slave-virtual-router-id = ' + str(self.slave_virtual_router_id) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.slave_virtual_router_id is not None:
                                return True

                            if self.accept_mode_disable is not None:
                                return True

                            if self.follow is not None:
                                return True

                            if self.primary_ipv4_address is not None:
                                return True

                            if self.secondary_ipv4_addresses is not None and self.secondary_ipv4_addresses._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_cfg as meta
                            return meta._meta_table['Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters.SlaveVirtualRouter']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-vrrp-cfg:slave-virtual-routers'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.slave_virtual_router is not None:
                            for child_ref in self.slave_virtual_router:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_cfg as meta
                        return meta._meta_table['Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters']['meta_info']


                class Version2(object):
                    """
                    Version 2 VRRP configuration
                    
                    .. attribute:: virtual_routers
                    
                    	The VRRP virtual router configuration table
                    	**type**\:   :py:class:`VirtualRouters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters>`
                    
                    

                    """

                    _prefix = 'ipv4-vrrp-cfg'
                    _revision = '2016-12-16'

                    def __init__(self):
                        self.parent = None
                        self.virtual_routers = Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters()
                        self.virtual_routers.parent = self


                    class VirtualRouters(object):
                        """
                        The VRRP virtual router configuration table
                        
                        .. attribute:: virtual_router
                        
                        	The VRRP virtual router being configured
                        	**type**\: list of    :py:class:`VirtualRouter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter>`
                        
                        

                        """

                        _prefix = 'ipv4-vrrp-cfg'
                        _revision = '2016-12-16'

                        def __init__(self):
                            self.parent = None
                            self.virtual_router = YList()
                            self.virtual_router.parent = self
                            self.virtual_router.name = 'virtual_router'


                        class VirtualRouter(object):
                            """
                            The VRRP virtual router being configured
                            
                            .. attribute:: vr_id  <key>
                            
                            	VRID Virtual Router Identifier
                            	**type**\:  int
                            
                            	**range:** 1..255
                            
                            .. attribute:: accept_mode_disable
                            
                            	Disable Accept Mode for this virtual IPAddress
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: bfd
                            
                            	Enable use of Bidirectional Forwarding Detection for this IP
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: preempt
                            
                            	Preempt Master router if higher priority
                            	**type**\:  int
                            
                            	**range:** 0..3600
                            
                            	**default value**\: 0
                            
                            .. attribute:: primary_ipv4_address
                            
                            	The Primary VRRP IPv4 address
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: priority
                            
                            	Priority value
                            	**type**\:  int
                            
                            	**range:** 1..254
                            
                            	**default value**\: 100
                            
                            .. attribute:: secondary_ipv4_addresses
                            
                            	The table of VRRP secondary IPv4 addresses
                            	**type**\:   :py:class:`SecondaryIpv4Addresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses>`
                            
                            .. attribute:: session_name
                            
                            	VRRP Session Name
                            	**type**\:  str
                            
                            	**length:** 1..16
                            
                            .. attribute:: text_password
                            
                            	Authentication password, 8 chars max
                            	**type**\:  str
                            
                            .. attribute:: timer
                            
                            	Set advertisement timer
                            	**type**\:   :py:class:`Timer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.Timer>`
                            
                            .. attribute:: tracked_objects
                            
                            	Track an object, reducing priority if it goes down
                            	**type**\:   :py:class:`TrackedObjects <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.TrackedObjects>`
                            
                            .. attribute:: tracks
                            
                            	Track an item, reducing priority if it goes down
                            	**type**\:   :py:class:`Tracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.Tracks>`
                            
                            

                            """

                            _prefix = 'ipv4-vrrp-cfg'
                            _revision = '2016-12-16'

                            def __init__(self):
                                self.parent = None
                                self.vr_id = None
                                self.accept_mode_disable = None
                                self.bfd = None
                                self.preempt = None
                                self.primary_ipv4_address = None
                                self.priority = None
                                self.secondary_ipv4_addresses = Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses()
                                self.secondary_ipv4_addresses.parent = self
                                self.session_name = None
                                self.text_password = None
                                self.timer = Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.Timer()
                                self.timer.parent = self
                                self.tracked_objects = Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.TrackedObjects()
                                self.tracked_objects.parent = self
                                self.tracks = Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.Tracks()
                                self.tracks.parent = self


                            class Timer(object):
                                """
                                Set advertisement timer
                                
                                .. attribute:: advertisement_time_in_msec
                                
                                	Advertisement time in milliseconds
                                	**type**\:  int
                                
                                	**range:** 100..40950
                                
                                	**units**\: millisecond
                                
                                .. attribute:: advertisement_time_in_sec
                                
                                	Advertisement time in seconds
                                	**type**\:  int
                                
                                	**range:** 1..255
                                
                                	**units**\: second
                                
                                .. attribute:: forced
                                
                                	TRUE \- Force configured timer values to be used, required when configured in milliseconds
                                	**type**\:  bool
                                
                                	**default value**\: false
                                
                                .. attribute:: in_msec
                                
                                	TRUE \- Advertise time configured in milliseconds, FALSE \- Advertise time configured in seconds
                                	**type**\:  bool
                                
                                	**default value**\: false
                                
                                

                                """

                                _prefix = 'ipv4-vrrp-cfg'
                                _revision = '2016-12-16'

                                def __init__(self):
                                    self.parent = None
                                    self.advertisement_time_in_msec = None
                                    self.advertisement_time_in_sec = None
                                    self.forced = None
                                    self.in_msec = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-vrrp-cfg:timer'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.advertisement_time_in_msec is not None:
                                        return True

                                    if self.advertisement_time_in_sec is not None:
                                        return True

                                    if self.forced is not None:
                                        return True

                                    if self.in_msec is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_cfg as meta
                                    return meta._meta_table['Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.Timer']['meta_info']


                            class SecondaryIpv4Addresses(object):
                                """
                                The table of VRRP secondary IPv4 addresses
                                
                                .. attribute:: secondary_ipv4_address
                                
                                	A VRRP secondary IPv4 address
                                	**type**\: list of    :py:class:`SecondaryIpv4Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses.SecondaryIpv4Address>`
                                
                                

                                """

                                _prefix = 'ipv4-vrrp-cfg'
                                _revision = '2016-12-16'

                                def __init__(self):
                                    self.parent = None
                                    self.secondary_ipv4_address = YList()
                                    self.secondary_ipv4_address.parent = self
                                    self.secondary_ipv4_address.name = 'secondary_ipv4_address'


                                class SecondaryIpv4Address(object):
                                    """
                                    A VRRP secondary IPv4 address
                                    
                                    .. attribute:: ip_address  <key>
                                    
                                    	VRRP Secondary IPv4 address
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    

                                    """

                                    _prefix = 'ipv4-vrrp-cfg'
                                    _revision = '2016-12-16'

                                    def __init__(self):
                                        self.parent = None
                                        self.ip_address = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.ip_address is None:
                                            raise YPYModelError('Key property ip_address is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-vrrp-cfg:secondary-ipv4-address[Cisco-IOS-XR-ipv4-vrrp-cfg:ip-address = ' + str(self.ip_address) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.ip_address is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_cfg as meta
                                        return meta._meta_table['Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses.SecondaryIpv4Address']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-vrrp-cfg:secondary-ipv4-addresses'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.secondary_ipv4_address is not None:
                                        for child_ref in self.secondary_ipv4_address:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_cfg as meta
                                    return meta._meta_table['Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses']['meta_info']


                            class Tracks(object):
                                """
                                Track an item, reducing priority if it
                                goes down
                                
                                .. attribute:: track
                                
                                	Object to be tracked
                                	**type**\: list of    :py:class:`Track <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.Tracks.Track>`
                                
                                

                                """

                                _prefix = 'ipv4-vrrp-cfg'
                                _revision = '2016-12-16'

                                def __init__(self):
                                    self.parent = None
                                    self.track = YList()
                                    self.track.parent = self
                                    self.track.name = 'track'


                                class Track(object):
                                    """
                                    Object to be tracked
                                    
                                    .. attribute:: interface_name  <key>
                                    
                                    	Object to be tracked, interface name for interfaces
                                    	**type**\:  str
                                    
                                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                    
                                    .. attribute:: priority
                                    
                                    	Priority decrement
                                    	**type**\:  int
                                    
                                    	**range:** 1..254
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'ipv4-vrrp-cfg'
                                    _revision = '2016-12-16'

                                    def __init__(self):
                                        self.parent = None
                                        self.interface_name = None
                                        self.priority = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.interface_name is None:
                                            raise YPYModelError('Key property interface_name is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-vrrp-cfg:track[Cisco-IOS-XR-ipv4-vrrp-cfg:interface-name = ' + str(self.interface_name) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.interface_name is not None:
                                            return True

                                        if self.priority is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_cfg as meta
                                        return meta._meta_table['Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.Tracks.Track']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-vrrp-cfg:tracks'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.track is not None:
                                        for child_ref in self.track:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_cfg as meta
                                    return meta._meta_table['Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.Tracks']['meta_info']


                            class TrackedObjects(object):
                                """
                                Track an object, reducing priority if it
                                goes down
                                
                                .. attribute:: tracked_object
                                
                                	Object to be tracked
                                	**type**\: list of    :py:class:`TrackedObject <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.TrackedObjects.TrackedObject>`
                                
                                

                                """

                                _prefix = 'ipv4-vrrp-cfg'
                                _revision = '2016-12-16'

                                def __init__(self):
                                    self.parent = None
                                    self.tracked_object = YList()
                                    self.tracked_object.parent = self
                                    self.tracked_object.name = 'tracked_object'


                                class TrackedObject(object):
                                    """
                                    Object to be tracked
                                    
                                    .. attribute:: object_name  <key>
                                    
                                    	Object to be tracked, interface name for interfaces
                                    	**type**\:  str
                                    
                                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                    
                                    .. attribute:: priority_decrement
                                    
                                    	Priority decrement
                                    	**type**\:  int
                                    
                                    	**range:** 1..254
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'ipv4-vrrp-cfg'
                                    _revision = '2016-12-16'

                                    def __init__(self):
                                        self.parent = None
                                        self.object_name = None
                                        self.priority_decrement = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.object_name is None:
                                            raise YPYModelError('Key property object_name is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-vrrp-cfg:tracked-object[Cisco-IOS-XR-ipv4-vrrp-cfg:object-name = ' + str(self.object_name) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.object_name is not None:
                                            return True

                                        if self.priority_decrement is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_cfg as meta
                                        return meta._meta_table['Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.TrackedObjects.TrackedObject']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-vrrp-cfg:tracked-objects'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.tracked_object is not None:
                                        for child_ref in self.tracked_object:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_cfg as meta
                                    return meta._meta_table['Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.TrackedObjects']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.vr_id is None:
                                    raise YPYModelError('Key property vr_id is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-vrrp-cfg:virtual-router[Cisco-IOS-XR-ipv4-vrrp-cfg:vr-id = ' + str(self.vr_id) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.vr_id is not None:
                                    return True

                                if self.accept_mode_disable is not None:
                                    return True

                                if self.bfd is not None:
                                    return True

                                if self.preempt is not None:
                                    return True

                                if self.primary_ipv4_address is not None:
                                    return True

                                if self.priority is not None:
                                    return True

                                if self.secondary_ipv4_addresses is not None and self.secondary_ipv4_addresses._has_data():
                                    return True

                                if self.session_name is not None:
                                    return True

                                if self.text_password is not None:
                                    return True

                                if self.timer is not None and self.timer._has_data():
                                    return True

                                if self.tracked_objects is not None and self.tracked_objects._has_data():
                                    return True

                                if self.tracks is not None and self.tracks._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_cfg as meta
                                return meta._meta_table['Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-vrrp-cfg:virtual-routers'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.virtual_router is not None:
                                for child_ref in self.virtual_router:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_cfg as meta
                            return meta._meta_table['Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-vrrp-cfg:version2'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.virtual_routers is not None and self.virtual_routers._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_cfg as meta
                        return meta._meta_table['Vrrp.Interfaces.Interface.Ipv4.Version2']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-vrrp-cfg:ipv4'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.slave_virtual_routers is not None and self.slave_virtual_routers._has_data():
                        return True

                    if self.version2 is not None and self.version2._has_data():
                        return True

                    if self.version3 is not None and self.version3._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_cfg as meta
                    return meta._meta_table['Vrrp.Interfaces.Interface.Ipv4']['meta_info']


            class Bfd(object):
                """
                BFD configuration
                
                .. attribute:: detection_multiplier
                
                	Detection multiplier for BFD sessions created by vrrp
                	**type**\:  int
                
                	**range:** 2..50
                
                .. attribute:: interval
                
                	Hello interval for BFD sessions created by vrrp
                	**type**\:  int
                
                	**range:** 3..30000
                
                	**units**\: millisecond
                
                

                """

                _prefix = 'ipv4-vrrp-cfg'
                _revision = '2016-12-16'

                def __init__(self):
                    self.parent = None
                    self.detection_multiplier = None
                    self.interval = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-vrrp-cfg:bfd'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.detection_multiplier is not None:
                        return True

                    if self.interval is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_cfg as meta
                    return meta._meta_table['Vrrp.Interfaces.Interface.Bfd']['meta_info']

            @property
            def _common_path(self):
                if self.interface_name is None:
                    raise YPYModelError('Key property interface_name is None')

                return '/Cisco-IOS-XR-ipv4-vrrp-cfg:vrrp/Cisco-IOS-XR-ipv4-vrrp-cfg:interfaces/Cisco-IOS-XR-ipv4-vrrp-cfg:interface[Cisco-IOS-XR-ipv4-vrrp-cfg:interface-name = ' + str(self.interface_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.interface_name is not None:
                    return True

                if self.bfd is not None and self.bfd._has_data():
                    return True

                if self.delay is not None and self.delay._has_data():
                    return True

                if self.ipv4 is not None and self.ipv4._has_data():
                    return True

                if self.ipv6 is not None and self.ipv6._has_data():
                    return True

                if self.mac_refresh is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_cfg as meta
                return meta._meta_table['Vrrp.Interfaces.Interface']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv4-vrrp-cfg:vrrp/Cisco-IOS-XR-ipv4-vrrp-cfg:interfaces'

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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_cfg as meta
            return meta._meta_table['Vrrp.Interfaces']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ipv4-vrrp-cfg:vrrp'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.interfaces is not None and self.interfaces._has_data():
            return True

        if self.logging is not None and self.logging._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_cfg as meta
        return meta._meta_table['Vrrp']['meta_info']


