""" Cisco_IOS_XR_ipv4_hsrp_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv4\-hsrp package configuration.

This module contains definitions
for the following management objects\:
  hsrp\: HSRP configuration

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



class HsrpLinklocalEnum(Enum):
    """
    HsrpLinklocalEnum

    Hsrp linklocal

    .. data:: manual = 0

    	Manual Linklocal address configuration

    .. data:: auto = 1

    	Automatic Linklocal address configuration

    .. data:: legacy = 2

    	Automatic legacy-compatible Linklocal address

    	configuration

    """

    manual = 0

    auto = 1

    legacy = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_cfg as meta
        return meta._meta_table['HsrpLinklocalEnum']



class Hsrp(object):
    """
    HSRP configuration
    
    .. attribute:: interfaces
    
    	Interface Table for HSRP configuration
    	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces>`
    
    .. attribute:: logging
    
    	HSRP logging options
    	**type**\:   :py:class:`Logging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Logging>`
    
    

    """

    _prefix = 'ipv4-hsrp-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.interfaces = Hsrp.Interfaces()
        self.interfaces.parent = self
        self.logging = Hsrp.Logging()
        self.logging.parent = self


    class Interfaces(object):
        """
        Interface Table for HSRP configuration
        
        .. attribute:: interface
        
        	Per\-interface HSRP configuration
        	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface>`
        
        

        """

        _prefix = 'ipv4-hsrp-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.interface = YList()
            self.interface.parent = self
            self.interface.name = 'interface'


        class Interface(object):
            """
            Per\-interface HSRP configuration
            
            .. attribute:: interface_name  <key>
            
            	Interface name
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: bfd
            
            	BFD configuration
            	**type**\:   :py:class:`Bfd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Bfd>`
            
            .. attribute:: delay
            
            	Minimum and Reload Delay
            	**type**\:   :py:class:`Delay <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Delay>`
            
            .. attribute:: ipv4
            
            	IPv4 HSRP configuration
            	**type**\:   :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4>`
            
            .. attribute:: ipv6
            
            	IPv6 HSRP configuration
            	**type**\:   :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv6>`
            
            .. attribute:: mac_refresh
            
            	HSRP MGO slave MAC refresh rate
            	**type**\:  int
            
            	**range:** 0..10000
            
            	**default value**\: 60
            
            .. attribute:: redirects_disable
            
            	Disable HSRP filtered ICMP redirects
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: use_bia
            
            	Use burned\-in address
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'ipv4-hsrp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.interface_name = None
                self.bfd = Hsrp.Interfaces.Interface.Bfd()
                self.bfd.parent = self
                self.delay = Hsrp.Interfaces.Interface.Delay()
                self.delay.parent = self
                self.ipv4 = Hsrp.Interfaces.Interface.Ipv4()
                self.ipv4.parent = self
                self.ipv6 = Hsrp.Interfaces.Interface.Ipv6()
                self.ipv6.parent = self
                self.mac_refresh = None
                self.redirects_disable = None
                self.use_bia = None


            class Ipv6(object):
                """
                IPv6 HSRP configuration
                
                .. attribute:: slave_groups
                
                	The HSRP slave group configuration table
                	**type**\:   :py:class:`SlaveGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv6.SlaveGroups>`
                
                .. attribute:: version2
                
                	Version 2 HSRP configuration
                	**type**\:   :py:class:`Version2 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv6.Version2>`
                
                

                """

                _prefix = 'ipv4-hsrp-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.slave_groups = Hsrp.Interfaces.Interface.Ipv6.SlaveGroups()
                    self.slave_groups.parent = self
                    self.version2 = Hsrp.Interfaces.Interface.Ipv6.Version2()
                    self.version2.parent = self


                class Version2(object):
                    """
                    Version 2 HSRP configuration
                    
                    .. attribute:: groups
                    
                    	The HSRP group configuration table
                    	**type**\:   :py:class:`Groups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv6.Version2.Groups>`
                    
                    

                    """

                    _prefix = 'ipv4-hsrp-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.groups = Hsrp.Interfaces.Interface.Ipv6.Version2.Groups()
                        self.groups.parent = self


                    class Groups(object):
                        """
                        The HSRP group configuration table
                        
                        .. attribute:: group
                        
                        	The HSRP group being configured
                        	**type**\: list of    :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group>`
                        
                        

                        """

                        _prefix = 'ipv4-hsrp-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.group = YList()
                            self.group.parent = self
                            self.group.name = 'group'


                        class Group(object):
                            """
                            The HSRP group being configured
                            
                            .. attribute:: group_number  <key>
                            
                            	HSRP group number
                            	**type**\:  int
                            
                            	**range:** 0..4095
                            
                            .. attribute:: bfd
                            
                            	Enable use of Bidirectional Forwarding Detection
                            	**type**\:   :py:class:`Bfd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.Bfd>`
                            
                            .. attribute:: global_ipv6_addresses
                            
                            	The table of HSRP virtual global IPv6 addresses
                            	**type**\:   :py:class:`GlobalIpv6Addresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.GlobalIpv6Addresses>`
                            
                            .. attribute:: link_local_ipv6_address
                            
                            	The HSRP IPv6 virtual linklocal address
                            	**type**\:   :py:class:`LinkLocalIpv6Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.LinkLocalIpv6Address>`
                            
                            .. attribute:: preempt
                            
                            	Force active if higher priority
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**default value**\: 0
                            
                            .. attribute:: priority
                            
                            	Priority value
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            	**default value**\: 100
                            
                            .. attribute:: session_name
                            
                            	HSRP Session name (for MGO)
                            	**type**\:  str
                            
                            	**length:** 1..16
                            
                            .. attribute:: timers
                            
                            	Hello and hold timers
                            	**type**\:   :py:class:`Timers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.Timers>`
                            
                            .. attribute:: tracked_interfaces
                            
                            	The HSRP tracked interface configuration table
                            	**type**\:   :py:class:`TrackedInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedInterfaces>`
                            
                            .. attribute:: tracked_objects
                            
                            	The HSRP tracked interface configuration table
                            	**type**\:   :py:class:`TrackedObjects <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedObjects>`
                            
                            .. attribute:: virtual_mac_address
                            
                            	HSRP MAC address
                            	**type**\:  str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            

                            """

                            _prefix = 'ipv4-hsrp-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.group_number = None
                                self.bfd = Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.Bfd()
                                self.bfd.parent = self
                                self.global_ipv6_addresses = Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.GlobalIpv6Addresses()
                                self.global_ipv6_addresses.parent = self
                                self.link_local_ipv6_address = Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.LinkLocalIpv6Address()
                                self.link_local_ipv6_address.parent = self
                                self.preempt = None
                                self.priority = None
                                self.session_name = None
                                self.timers = Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.Timers()
                                self.timers.parent = self
                                self.tracked_interfaces = Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedInterfaces()
                                self.tracked_interfaces.parent = self
                                self.tracked_objects = Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedObjects()
                                self.tracked_objects.parent = self
                                self.virtual_mac_address = None


                            class Bfd(object):
                                """
                                Enable use of Bidirectional Forwarding
                                Detection
                                
                                .. attribute:: address
                                
                                	Enable BFD for this remote IP
                                	**type**\:  str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: interface_name
                                
                                	Interface name to run BFD
                                	**type**\:  str
                                
                                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                
                                

                                """

                                _prefix = 'ipv4-hsrp-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.address = None
                                    self.interface_name = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-hsrp-cfg:bfd'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.address is not None:
                                        return True

                                    if self.interface_name is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_cfg as meta
                                    return meta._meta_table['Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.Bfd']['meta_info']


                            class TrackedInterfaces(object):
                                """
                                The HSRP tracked interface configuration
                                table
                                
                                .. attribute:: tracked_interface
                                
                                	Interface being tracked
                                	**type**\: list of    :py:class:`TrackedInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedInterfaces.TrackedInterface>`
                                
                                

                                """

                                _prefix = 'ipv4-hsrp-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.tracked_interface = YList()
                                    self.tracked_interface.parent = self
                                    self.tracked_interface.name = 'tracked_interface'


                                class TrackedInterface(object):
                                    """
                                    Interface being tracked
                                    
                                    .. attribute:: interface_name  <key>
                                    
                                    	Interface being tracked
                                    	**type**\:  str
                                    
                                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                    
                                    .. attribute:: priority_decrement
                                    
                                    	Priority decrement
                                    	**type**\:  int
                                    
                                    	**range:** 1..255
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'ipv4-hsrp-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.interface_name = None
                                        self.priority_decrement = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.interface_name is None:
                                            raise YPYModelError('Key property interface_name is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-hsrp-cfg:tracked-interface[Cisco-IOS-XR-ipv4-hsrp-cfg:interface-name = ' + str(self.interface_name) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.interface_name is not None:
                                            return True

                                        if self.priority_decrement is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_cfg as meta
                                        return meta._meta_table['Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedInterfaces.TrackedInterface']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-hsrp-cfg:tracked-interfaces'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.tracked_interface is not None:
                                        for child_ref in self.tracked_interface:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_cfg as meta
                                    return meta._meta_table['Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedInterfaces']['meta_info']


                            class TrackedObjects(object):
                                """
                                The HSRP tracked interface configuration
                                table
                                
                                .. attribute:: tracked_object
                                
                                	Object being tracked
                                	**type**\: list of    :py:class:`TrackedObject <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedObjects.TrackedObject>`
                                
                                

                                """

                                _prefix = 'ipv4-hsrp-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.tracked_object = YList()
                                    self.tracked_object.parent = self
                                    self.tracked_object.name = 'tracked_object'


                                class TrackedObject(object):
                                    """
                                    Object being tracked
                                    
                                    .. attribute:: object_name  <key>
                                    
                                    	Interface being tracked
                                    	**type**\:  str
                                    
                                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                    
                                    .. attribute:: priority_decrement
                                    
                                    	Priority decrement
                                    	**type**\:  int
                                    
                                    	**range:** 1..255
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'ipv4-hsrp-cfg'
                                    _revision = '2015-11-09'

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

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-hsrp-cfg:tracked-object[Cisco-IOS-XR-ipv4-hsrp-cfg:object-name = ' + str(self.object_name) + ']'

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
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_cfg as meta
                                        return meta._meta_table['Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedObjects.TrackedObject']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-hsrp-cfg:tracked-objects'

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
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_cfg as meta
                                    return meta._meta_table['Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedObjects']['meta_info']


                            class Timers(object):
                                """
                                Hello and hold timers
                                
                                .. attribute:: hello_msec
                                
                                	Hello time in msecs
                                	**type**\:  int
                                
                                	**range:** 100..3000
                                
                                	**units**\: millisecond
                                
                                .. attribute:: hello_msec_flag
                                
                                	TRUE \- Hello time configured in milliseconds, FALSE \- Hello time configured in seconds
                                	**type**\:  bool
                                
                                	**default value**\: false
                                
                                .. attribute:: hello_sec
                                
                                	Hello time in seconds
                                	**type**\:  int
                                
                                	**range:** 1..255
                                
                                	**units**\: second
                                
                                	**default value**\: 3
                                
                                .. attribute:: hold_msec
                                
                                	Hold time in msecs
                                	**type**\:  int
                                
                                	**range:** 100..3000
                                
                                	**units**\: millisecond
                                
                                .. attribute:: hold_msec_flag
                                
                                	TRUE \- Hold time configured in milliseconds, FALSE \- Hold time configured in seconds
                                	**type**\:  bool
                                
                                	**default value**\: false
                                
                                .. attribute:: hold_sec
                                
                                	Hold time in seconds
                                	**type**\:  int
                                
                                	**range:** 1..255
                                
                                	**units**\: second
                                
                                	**default value**\: 10
                                
                                

                                """

                                _prefix = 'ipv4-hsrp-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.hello_msec = None
                                    self.hello_msec_flag = None
                                    self.hello_sec = None
                                    self.hold_msec = None
                                    self.hold_msec_flag = None
                                    self.hold_sec = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-hsrp-cfg:timers'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.hello_msec is not None:
                                        return True

                                    if self.hello_msec_flag is not None:
                                        return True

                                    if self.hello_sec is not None:
                                        return True

                                    if self.hold_msec is not None:
                                        return True

                                    if self.hold_msec_flag is not None:
                                        return True

                                    if self.hold_sec is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_cfg as meta
                                    return meta._meta_table['Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.Timers']['meta_info']


                            class LinkLocalIpv6Address(object):
                                """
                                The HSRP IPv6 virtual linklocal address
                                
                                .. attribute:: address
                                
                                	HSRP IPv6 virtual linklocal address
                                	**type**\:  str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: auto_configure
                                
                                	Linklocal Configuration Type
                                	**type**\:   :py:class:`HsrpLinklocalEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.HsrpLinklocalEnum>`
                                
                                	**default value**\: manual
                                
                                

                                """

                                _prefix = 'ipv4-hsrp-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.address = None
                                    self.auto_configure = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-hsrp-cfg:link-local-ipv6-address'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.address is not None:
                                        return True

                                    if self.auto_configure is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_cfg as meta
                                    return meta._meta_table['Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.LinkLocalIpv6Address']['meta_info']


                            class GlobalIpv6Addresses(object):
                                """
                                The table of HSRP virtual global IPv6
                                addresses
                                
                                .. attribute:: global_ipv6_address
                                
                                	A HSRP virtual global IPv6 IP address
                                	**type**\: list of    :py:class:`GlobalIpv6Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.GlobalIpv6Addresses.GlobalIpv6Address>`
                                
                                

                                """

                                _prefix = 'ipv4-hsrp-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.global_ipv6_address = YList()
                                    self.global_ipv6_address.parent = self
                                    self.global_ipv6_address.name = 'global_ipv6_address'


                                class GlobalIpv6Address(object):
                                    """
                                    A HSRP virtual global IPv6 IP address
                                    
                                    .. attribute:: address  <key>
                                    
                                    	HSRP virtual global IPv6 address
                                    	**type**\:  str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    

                                    """

                                    _prefix = 'ipv4-hsrp-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.address = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.address is None:
                                            raise YPYModelError('Key property address is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-hsrp-cfg:global-ipv6-address[Cisco-IOS-XR-ipv4-hsrp-cfg:address = ' + str(self.address) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.address is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_cfg as meta
                                        return meta._meta_table['Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.GlobalIpv6Addresses.GlobalIpv6Address']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-hsrp-cfg:global-ipv6-addresses'

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
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_cfg as meta
                                    return meta._meta_table['Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.GlobalIpv6Addresses']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.group_number is None:
                                    raise YPYModelError('Key property group_number is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-hsrp-cfg:group[Cisco-IOS-XR-ipv4-hsrp-cfg:group-number = ' + str(self.group_number) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.group_number is not None:
                                    return True

                                if self.bfd is not None and self.bfd._has_data():
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

                                if self.timers is not None and self.timers._has_data():
                                    return True

                                if self.tracked_interfaces is not None and self.tracked_interfaces._has_data():
                                    return True

                                if self.tracked_objects is not None and self.tracked_objects._has_data():
                                    return True

                                if self.virtual_mac_address is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_cfg as meta
                                return meta._meta_table['Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-hsrp-cfg:groups'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.group is not None:
                                for child_ref in self.group:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_cfg as meta
                            return meta._meta_table['Hsrp.Interfaces.Interface.Ipv6.Version2.Groups']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-hsrp-cfg:version2'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.groups is not None and self.groups._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_cfg as meta
                        return meta._meta_table['Hsrp.Interfaces.Interface.Ipv6.Version2']['meta_info']


                class SlaveGroups(object):
                    """
                    The HSRP slave group configuration table
                    
                    .. attribute:: slave_group
                    
                    	The HSRP slave group being configured
                    	**type**\: list of    :py:class:`SlaveGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup>`
                    
                    

                    """

                    _prefix = 'ipv4-hsrp-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.slave_group = YList()
                        self.slave_group.parent = self
                        self.slave_group.name = 'slave_group'


                    class SlaveGroup(object):
                        """
                        The HSRP slave group being configured
                        
                        .. attribute:: slave_group_number  <key>
                        
                        	HSRP group number
                        	**type**\:  int
                        
                        	**range:** 0..4095
                        
                        .. attribute:: follow
                        
                        	HSRP Group name for this slave to follow
                        	**type**\:  str
                        
                        .. attribute:: global_ipv6_addresses
                        
                        	The table of HSRP virtual global IPv6 addresses
                        	**type**\:   :py:class:`GlobalIpv6Addresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup.GlobalIpv6Addresses>`
                        
                        .. attribute:: link_local_ipv6_address
                        
                        	The HSRP IPv6 virtual linklocal address
                        	**type**\:   :py:class:`LinkLocalIpv6Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup.LinkLocalIpv6Address>`
                        
                        .. attribute:: virtual_mac_address
                        
                        	HSRP MAC address
                        	**type**\:  str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        

                        """

                        _prefix = 'ipv4-hsrp-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.slave_group_number = None
                            self.follow = None
                            self.global_ipv6_addresses = Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup.GlobalIpv6Addresses()
                            self.global_ipv6_addresses.parent = self
                            self.link_local_ipv6_address = Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup.LinkLocalIpv6Address()
                            self.link_local_ipv6_address.parent = self
                            self.virtual_mac_address = None


                        class LinkLocalIpv6Address(object):
                            """
                            The HSRP IPv6 virtual linklocal address
                            
                            .. attribute:: address
                            
                            	HSRP IPv6 virtual linklocal address
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: auto_configure
                            
                            	Linklocal Configuration Type
                            	**type**\:   :py:class:`HsrpLinklocalEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.HsrpLinklocalEnum>`
                            
                            	**default value**\: manual
                            
                            

                            """

                            _prefix = 'ipv4-hsrp-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.address = None
                                self.auto_configure = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-hsrp-cfg:link-local-ipv6-address'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.address is not None:
                                    return True

                                if self.auto_configure is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_cfg as meta
                                return meta._meta_table['Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup.LinkLocalIpv6Address']['meta_info']


                        class GlobalIpv6Addresses(object):
                            """
                            The table of HSRP virtual global IPv6
                            addresses
                            
                            .. attribute:: global_ipv6_address
                            
                            	A HSRP virtual global IPv6 IP address
                            	**type**\: list of    :py:class:`GlobalIpv6Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup.GlobalIpv6Addresses.GlobalIpv6Address>`
                            
                            

                            """

                            _prefix = 'ipv4-hsrp-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.global_ipv6_address = YList()
                                self.global_ipv6_address.parent = self
                                self.global_ipv6_address.name = 'global_ipv6_address'


                            class GlobalIpv6Address(object):
                                """
                                A HSRP virtual global IPv6 IP address
                                
                                .. attribute:: address  <key>
                                
                                	HSRP virtual global IPv6 address
                                	**type**\:  str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'ipv4-hsrp-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.address = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.address is None:
                                        raise YPYModelError('Key property address is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-hsrp-cfg:global-ipv6-address[Cisco-IOS-XR-ipv4-hsrp-cfg:address = ' + str(self.address) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.address is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_cfg as meta
                                    return meta._meta_table['Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup.GlobalIpv6Addresses.GlobalIpv6Address']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-hsrp-cfg:global-ipv6-addresses'

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
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_cfg as meta
                                return meta._meta_table['Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup.GlobalIpv6Addresses']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.slave_group_number is None:
                                raise YPYModelError('Key property slave_group_number is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-hsrp-cfg:slave-group[Cisco-IOS-XR-ipv4-hsrp-cfg:slave-group-number = ' + str(self.slave_group_number) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.slave_group_number is not None:
                                return True

                            if self.follow is not None:
                                return True

                            if self.global_ipv6_addresses is not None and self.global_ipv6_addresses._has_data():
                                return True

                            if self.link_local_ipv6_address is not None and self.link_local_ipv6_address._has_data():
                                return True

                            if self.virtual_mac_address is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_cfg as meta
                            return meta._meta_table['Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-hsrp-cfg:slave-groups'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.slave_group is not None:
                            for child_ref in self.slave_group:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_cfg as meta
                        return meta._meta_table['Hsrp.Interfaces.Interface.Ipv6.SlaveGroups']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-hsrp-cfg:ipv6'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.slave_groups is not None and self.slave_groups._has_data():
                        return True

                    if self.version2 is not None and self.version2._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_cfg as meta
                    return meta._meta_table['Hsrp.Interfaces.Interface.Ipv6']['meta_info']


            class Bfd(object):
                """
                BFD configuration
                
                .. attribute:: detection_multiplier
                
                	Detection multiplier for BFD sessions created by hsrp
                	**type**\:  int
                
                	**range:** 2..50
                
                .. attribute:: interval
                
                	Hello interval for BFD sessions created by hsrp
                	**type**\:  int
                
                	**range:** 3..30000
                
                	**units**\: millisecond
                
                

                """

                _prefix = 'ipv4-hsrp-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.detection_multiplier = None
                    self.interval = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-hsrp-cfg:bfd'

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
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_cfg as meta
                    return meta._meta_table['Hsrp.Interfaces.Interface.Bfd']['meta_info']


            class Delay(object):
                """
                Minimum and Reload Delay
                
                .. attribute:: minimum_delay
                
                	Minimum delay in seconds
                	**type**\:  int
                
                	**range:** 0..10000
                
                	**units**\: second
                
                	**default value**\: 1
                
                .. attribute:: reload_delay
                
                	Reload delay in seconds
                	**type**\:  int
                
                	**range:** 0..10000
                
                	**units**\: second
                
                	**default value**\: 5
                
                

                """

                _prefix = 'ipv4-hsrp-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.minimum_delay = None
                    self.reload_delay = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-hsrp-cfg:delay'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.minimum_delay is not None:
                        return True

                    if self.reload_delay is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_cfg as meta
                    return meta._meta_table['Hsrp.Interfaces.Interface.Delay']['meta_info']


            class Ipv4(object):
                """
                IPv4 HSRP configuration
                
                .. attribute:: slave_groups
                
                	The HSRP slave group configuration table
                	**type**\:   :py:class:`SlaveGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.SlaveGroups>`
                
                .. attribute:: version1
                
                	Version 1 HSRP configuration
                	**type**\:   :py:class:`Version1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version1>`
                
                .. attribute:: version2
                
                	Version 2 HSRP configuration
                	**type**\:   :py:class:`Version2 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version2>`
                
                

                """

                _prefix = 'ipv4-hsrp-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.slave_groups = Hsrp.Interfaces.Interface.Ipv4.SlaveGroups()
                    self.slave_groups.parent = self
                    self.version1 = Hsrp.Interfaces.Interface.Ipv4.Version1()
                    self.version1.parent = self
                    self.version2 = Hsrp.Interfaces.Interface.Ipv4.Version2()
                    self.version2.parent = self


                class SlaveGroups(object):
                    """
                    The HSRP slave group configuration table
                    
                    .. attribute:: slave_group
                    
                    	The HSRP slave group being configured
                    	**type**\: list of    :py:class:`SlaveGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.SlaveGroups.SlaveGroup>`
                    
                    

                    """

                    _prefix = 'ipv4-hsrp-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.slave_group = YList()
                        self.slave_group.parent = self
                        self.slave_group.name = 'slave_group'


                    class SlaveGroup(object):
                        """
                        The HSRP slave group being configured
                        
                        .. attribute:: slave_group_number  <key>
                        
                        	HSRP group number
                        	**type**\:  int
                        
                        	**range:** 0..4095
                        
                        .. attribute:: follow
                        
                        	HSRP Group name for this slave to follow
                        	**type**\:  str
                        
                        .. attribute:: primary_ipv4_address
                        
                        	Primary HSRP IP address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: secondary_ipv4_addresses
                        
                        	Secondary HSRP IP address Table
                        	**type**\:   :py:class:`SecondaryIpv4Addresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.SlaveGroups.SlaveGroup.SecondaryIpv4Addresses>`
                        
                        .. attribute:: virtual_mac_address
                        
                        	HSRP MAC address
                        	**type**\:  str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        

                        """

                        _prefix = 'ipv4-hsrp-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.slave_group_number = None
                            self.follow = None
                            self.primary_ipv4_address = None
                            self.secondary_ipv4_addresses = Hsrp.Interfaces.Interface.Ipv4.SlaveGroups.SlaveGroup.SecondaryIpv4Addresses()
                            self.secondary_ipv4_addresses.parent = self
                            self.virtual_mac_address = None


                        class SecondaryIpv4Addresses(object):
                            """
                            Secondary HSRP IP address Table
                            
                            .. attribute:: secondary_ipv4_address
                            
                            	Secondary HSRP IP address
                            	**type**\: list of    :py:class:`SecondaryIpv4Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.SlaveGroups.SlaveGroup.SecondaryIpv4Addresses.SecondaryIpv4Address>`
                            
                            

                            """

                            _prefix = 'ipv4-hsrp-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.secondary_ipv4_address = YList()
                                self.secondary_ipv4_address.parent = self
                                self.secondary_ipv4_address.name = 'secondary_ipv4_address'


                            class SecondaryIpv4Address(object):
                                """
                                Secondary HSRP IP address
                                
                                .. attribute:: address  <key>
                                
                                	HSRP IP address
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'ipv4-hsrp-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.address = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.address is None:
                                        raise YPYModelError('Key property address is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-hsrp-cfg:secondary-ipv4-address[Cisco-IOS-XR-ipv4-hsrp-cfg:address = ' + str(self.address) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.address is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_cfg as meta
                                    return meta._meta_table['Hsrp.Interfaces.Interface.Ipv4.SlaveGroups.SlaveGroup.SecondaryIpv4Addresses.SecondaryIpv4Address']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-hsrp-cfg:secondary-ipv4-addresses'

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
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_cfg as meta
                                return meta._meta_table['Hsrp.Interfaces.Interface.Ipv4.SlaveGroups.SlaveGroup.SecondaryIpv4Addresses']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.slave_group_number is None:
                                raise YPYModelError('Key property slave_group_number is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-hsrp-cfg:slave-group[Cisco-IOS-XR-ipv4-hsrp-cfg:slave-group-number = ' + str(self.slave_group_number) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.slave_group_number is not None:
                                return True

                            if self.follow is not None:
                                return True

                            if self.primary_ipv4_address is not None:
                                return True

                            if self.secondary_ipv4_addresses is not None and self.secondary_ipv4_addresses._has_data():
                                return True

                            if self.virtual_mac_address is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_cfg as meta
                            return meta._meta_table['Hsrp.Interfaces.Interface.Ipv4.SlaveGroups.SlaveGroup']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-hsrp-cfg:slave-groups'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.slave_group is not None:
                            for child_ref in self.slave_group:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_cfg as meta
                        return meta._meta_table['Hsrp.Interfaces.Interface.Ipv4.SlaveGroups']['meta_info']


                class Version1(object):
                    """
                    Version 1 HSRP configuration
                    
                    .. attribute:: groups
                    
                    	The HSRP group configuration table
                    	**type**\:   :py:class:`Groups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version1.Groups>`
                    
                    

                    """

                    _prefix = 'ipv4-hsrp-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.groups = Hsrp.Interfaces.Interface.Ipv4.Version1.Groups()
                        self.groups.parent = self


                    class Groups(object):
                        """
                        The HSRP group configuration table
                        
                        .. attribute:: group
                        
                        	The HSRP group being configured
                        	**type**\: list of    :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group>`
                        
                        

                        """

                        _prefix = 'ipv4-hsrp-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.group = YList()
                            self.group.parent = self
                            self.group.name = 'group'


                        class Group(object):
                            """
                            The HSRP group being configured
                            
                            .. attribute:: group_number  <key>
                            
                            	HSRP group number
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: authentication
                            
                            	Authentication string
                            	**type**\:  str
                            
                            	**length:** 1..8
                            
                            	**default value**\: cisco
                            
                            .. attribute:: bfd
                            
                            	Enable use of Bidirectional Forwarding Detection
                            	**type**\:   :py:class:`Bfd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.Bfd>`
                            
                            .. attribute:: preempt
                            
                            	Force active if higher priority
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**default value**\: 0
                            
                            .. attribute:: primary_ipv4_address
                            
                            	Primary HSRP IP address
                            	**type**\:   :py:class:`PrimaryIpv4Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.PrimaryIpv4Address>`
                            
                            .. attribute:: priority
                            
                            	Priority value
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            	**default value**\: 100
                            
                            .. attribute:: secondary_ipv4_addresses
                            
                            	Secondary HSRP IP address Table
                            	**type**\:   :py:class:`SecondaryIpv4Addresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.SecondaryIpv4Addresses>`
                            
                            .. attribute:: session_name
                            
                            	HSRP Session name (for MGO)
                            	**type**\:  str
                            
                            	**length:** 1..16
                            
                            .. attribute:: timers
                            
                            	Hello and hold timers
                            	**type**\:   :py:class:`Timers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.Timers>`
                            
                            .. attribute:: tracked_interfaces
                            
                            	The HSRP tracked interface configuration table
                            	**type**\:   :py:class:`TrackedInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedInterfaces>`
                            
                            .. attribute:: tracked_objects
                            
                            	The HSRP tracked interface configuration table
                            	**type**\:   :py:class:`TrackedObjects <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedObjects>`
                            
                            .. attribute:: virtual_mac_address
                            
                            	HSRP MAC address
                            	**type**\:  str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            

                            """

                            _prefix = 'ipv4-hsrp-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.group_number = None
                                self.authentication = None
                                self.bfd = Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.Bfd()
                                self.bfd.parent = self
                                self.preempt = None
                                self.primary_ipv4_address = Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.PrimaryIpv4Address()
                                self.primary_ipv4_address.parent = self
                                self.priority = None
                                self.secondary_ipv4_addresses = Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.SecondaryIpv4Addresses()
                                self.secondary_ipv4_addresses.parent = self
                                self.session_name = None
                                self.timers = Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.Timers()
                                self.timers.parent = self
                                self.tracked_interfaces = Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedInterfaces()
                                self.tracked_interfaces.parent = self
                                self.tracked_objects = Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedObjects()
                                self.tracked_objects.parent = self
                                self.virtual_mac_address = None


                            class TrackedInterfaces(object):
                                """
                                The HSRP tracked interface configuration
                                table
                                
                                .. attribute:: tracked_interface
                                
                                	Interface being tracked
                                	**type**\: list of    :py:class:`TrackedInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedInterfaces.TrackedInterface>`
                                
                                

                                """

                                _prefix = 'ipv4-hsrp-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.tracked_interface = YList()
                                    self.tracked_interface.parent = self
                                    self.tracked_interface.name = 'tracked_interface'


                                class TrackedInterface(object):
                                    """
                                    Interface being tracked
                                    
                                    .. attribute:: interface_name  <key>
                                    
                                    	Interface being tracked
                                    	**type**\:  str
                                    
                                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                    
                                    .. attribute:: priority_decrement
                                    
                                    	Priority decrement
                                    	**type**\:  int
                                    
                                    	**range:** 1..255
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'ipv4-hsrp-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.interface_name = None
                                        self.priority_decrement = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.interface_name is None:
                                            raise YPYModelError('Key property interface_name is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-hsrp-cfg:tracked-interface[Cisco-IOS-XR-ipv4-hsrp-cfg:interface-name = ' + str(self.interface_name) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.interface_name is not None:
                                            return True

                                        if self.priority_decrement is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_cfg as meta
                                        return meta._meta_table['Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedInterfaces.TrackedInterface']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-hsrp-cfg:tracked-interfaces'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.tracked_interface is not None:
                                        for child_ref in self.tracked_interface:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_cfg as meta
                                    return meta._meta_table['Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedInterfaces']['meta_info']


                            class Bfd(object):
                                """
                                Enable use of Bidirectional Forwarding
                                Detection
                                
                                .. attribute:: address
                                
                                	Enable BFD for this remote IP
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: interface_name
                                
                                	Interface name to run BFD
                                	**type**\:  str
                                
                                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                
                                

                                """

                                _prefix = 'ipv4-hsrp-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.address = None
                                    self.interface_name = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-hsrp-cfg:bfd'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.address is not None:
                                        return True

                                    if self.interface_name is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_cfg as meta
                                    return meta._meta_table['Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.Bfd']['meta_info']


                            class TrackedObjects(object):
                                """
                                The HSRP tracked interface configuration
                                table
                                
                                .. attribute:: tracked_object
                                
                                	Object being tracked
                                	**type**\: list of    :py:class:`TrackedObject <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedObjects.TrackedObject>`
                                
                                

                                """

                                _prefix = 'ipv4-hsrp-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.tracked_object = YList()
                                    self.tracked_object.parent = self
                                    self.tracked_object.name = 'tracked_object'


                                class TrackedObject(object):
                                    """
                                    Object being tracked
                                    
                                    .. attribute:: object_name  <key>
                                    
                                    	Interface being tracked
                                    	**type**\:  str
                                    
                                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                    
                                    .. attribute:: priority_decrement
                                    
                                    	Priority decrement
                                    	**type**\:  int
                                    
                                    	**range:** 1..255
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'ipv4-hsrp-cfg'
                                    _revision = '2015-11-09'

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

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-hsrp-cfg:tracked-object[Cisco-IOS-XR-ipv4-hsrp-cfg:object-name = ' + str(self.object_name) + ']'

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
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_cfg as meta
                                        return meta._meta_table['Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedObjects.TrackedObject']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-hsrp-cfg:tracked-objects'

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
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_cfg as meta
                                    return meta._meta_table['Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedObjects']['meta_info']


                            class Timers(object):
                                """
                                Hello and hold timers
                                
                                .. attribute:: hello_msec
                                
                                	Hello time in msecs
                                	**type**\:  int
                                
                                	**range:** 100..3000
                                
                                	**units**\: millisecond
                                
                                .. attribute:: hello_msec_flag
                                
                                	TRUE \- Hello time configured in milliseconds, FALSE \- Hello time configured in seconds
                                	**type**\:  bool
                                
                                	**default value**\: false
                                
                                .. attribute:: hello_sec
                                
                                	Hello time in seconds
                                	**type**\:  int
                                
                                	**range:** 1..255
                                
                                	**units**\: second
                                
                                	**default value**\: 3
                                
                                .. attribute:: hold_msec
                                
                                	Hold time in msecs
                                	**type**\:  int
                                
                                	**range:** 100..3000
                                
                                	**units**\: millisecond
                                
                                .. attribute:: hold_msec_flag
                                
                                	TRUE \- Hold time configured in milliseconds, FALSE \- Hold time configured in seconds
                                	**type**\:  bool
                                
                                	**default value**\: false
                                
                                .. attribute:: hold_sec
                                
                                	Hold time in seconds
                                	**type**\:  int
                                
                                	**range:** 1..255
                                
                                	**units**\: second
                                
                                	**default value**\: 10
                                
                                

                                """

                                _prefix = 'ipv4-hsrp-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.hello_msec = None
                                    self.hello_msec_flag = None
                                    self.hello_sec = None
                                    self.hold_msec = None
                                    self.hold_msec_flag = None
                                    self.hold_sec = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-hsrp-cfg:timers'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.hello_msec is not None:
                                        return True

                                    if self.hello_msec_flag is not None:
                                        return True

                                    if self.hello_sec is not None:
                                        return True

                                    if self.hold_msec is not None:
                                        return True

                                    if self.hold_msec_flag is not None:
                                        return True

                                    if self.hold_sec is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_cfg as meta
                                    return meta._meta_table['Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.Timers']['meta_info']


                            class PrimaryIpv4Address(object):
                                """
                                Primary HSRP IP address
                                
                                .. attribute:: address
                                
                                	HSRP IP address
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: virtual_ip_learn
                                
                                	TRUE if the HSRP protocol is to learn the virtual IP address it is to use
                                	**type**\:  bool
                                
                                

                                """

                                _prefix = 'ipv4-hsrp-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.address = None
                                    self.virtual_ip_learn = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-hsrp-cfg:primary-ipv4-address'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.address is not None:
                                        return True

                                    if self.virtual_ip_learn is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_cfg as meta
                                    return meta._meta_table['Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.PrimaryIpv4Address']['meta_info']


                            class SecondaryIpv4Addresses(object):
                                """
                                Secondary HSRP IP address Table
                                
                                .. attribute:: secondary_ipv4_address
                                
                                	Secondary HSRP IP address
                                	**type**\: list of    :py:class:`SecondaryIpv4Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.SecondaryIpv4Addresses.SecondaryIpv4Address>`
                                
                                

                                """

                                _prefix = 'ipv4-hsrp-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.secondary_ipv4_address = YList()
                                    self.secondary_ipv4_address.parent = self
                                    self.secondary_ipv4_address.name = 'secondary_ipv4_address'


                                class SecondaryIpv4Address(object):
                                    """
                                    Secondary HSRP IP address
                                    
                                    .. attribute:: address  <key>
                                    
                                    	HSRP IP address
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    

                                    """

                                    _prefix = 'ipv4-hsrp-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.address = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.address is None:
                                            raise YPYModelError('Key property address is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-hsrp-cfg:secondary-ipv4-address[Cisco-IOS-XR-ipv4-hsrp-cfg:address = ' + str(self.address) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.address is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_cfg as meta
                                        return meta._meta_table['Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.SecondaryIpv4Addresses.SecondaryIpv4Address']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-hsrp-cfg:secondary-ipv4-addresses'

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
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_cfg as meta
                                    return meta._meta_table['Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.SecondaryIpv4Addresses']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.group_number is None:
                                    raise YPYModelError('Key property group_number is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-hsrp-cfg:group[Cisco-IOS-XR-ipv4-hsrp-cfg:group-number = ' + str(self.group_number) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.group_number is not None:
                                    return True

                                if self.authentication is not None:
                                    return True

                                if self.bfd is not None and self.bfd._has_data():
                                    return True

                                if self.preempt is not None:
                                    return True

                                if self.primary_ipv4_address is not None and self.primary_ipv4_address._has_data():
                                    return True

                                if self.priority is not None:
                                    return True

                                if self.secondary_ipv4_addresses is not None and self.secondary_ipv4_addresses._has_data():
                                    return True

                                if self.session_name is not None:
                                    return True

                                if self.timers is not None and self.timers._has_data():
                                    return True

                                if self.tracked_interfaces is not None and self.tracked_interfaces._has_data():
                                    return True

                                if self.tracked_objects is not None and self.tracked_objects._has_data():
                                    return True

                                if self.virtual_mac_address is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_cfg as meta
                                return meta._meta_table['Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-hsrp-cfg:groups'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.group is not None:
                                for child_ref in self.group:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_cfg as meta
                            return meta._meta_table['Hsrp.Interfaces.Interface.Ipv4.Version1.Groups']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-hsrp-cfg:version1'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.groups is not None and self.groups._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_cfg as meta
                        return meta._meta_table['Hsrp.Interfaces.Interface.Ipv4.Version1']['meta_info']


                class Version2(object):
                    """
                    Version 2 HSRP configuration
                    
                    .. attribute:: groups
                    
                    	The HSRP group configuration table
                    	**type**\:   :py:class:`Groups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version2.Groups>`
                    
                    

                    """

                    _prefix = 'ipv4-hsrp-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.groups = Hsrp.Interfaces.Interface.Ipv4.Version2.Groups()
                        self.groups.parent = self


                    class Groups(object):
                        """
                        The HSRP group configuration table
                        
                        .. attribute:: group
                        
                        	The HSRP group being configured
                        	**type**\: list of    :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group>`
                        
                        

                        """

                        _prefix = 'ipv4-hsrp-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.group = YList()
                            self.group.parent = self
                            self.group.name = 'group'


                        class Group(object):
                            """
                            The HSRP group being configured
                            
                            .. attribute:: group_number  <key>
                            
                            	HSRP group number
                            	**type**\:  int
                            
                            	**range:** 0..4095
                            
                            .. attribute:: bfd
                            
                            	Enable use of Bidirectional Forwarding Detection
                            	**type**\:   :py:class:`Bfd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.Bfd>`
                            
                            .. attribute:: preempt
                            
                            	Force active if higher priority
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**default value**\: 0
                            
                            .. attribute:: primary_ipv4_address
                            
                            	Primary HSRP IP address
                            	**type**\:   :py:class:`PrimaryIpv4Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.PrimaryIpv4Address>`
                            
                            .. attribute:: priority
                            
                            	Priority value
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            	**default value**\: 100
                            
                            .. attribute:: secondary_ipv4_addresses
                            
                            	Secondary HSRP IP address Table
                            	**type**\:   :py:class:`SecondaryIpv4Addresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.SecondaryIpv4Addresses>`
                            
                            .. attribute:: session_name
                            
                            	HSRP Session name (for MGO)
                            	**type**\:  str
                            
                            	**length:** 1..16
                            
                            .. attribute:: timers
                            
                            	Hello and hold timers
                            	**type**\:   :py:class:`Timers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.Timers>`
                            
                            .. attribute:: tracked_interfaces
                            
                            	The HSRP tracked interface configuration table
                            	**type**\:   :py:class:`TrackedInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedInterfaces>`
                            
                            .. attribute:: tracked_objects
                            
                            	The HSRP tracked interface configuration table
                            	**type**\:   :py:class:`TrackedObjects <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedObjects>`
                            
                            .. attribute:: virtual_mac_address
                            
                            	HSRP MAC address
                            	**type**\:  str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            

                            """

                            _prefix = 'ipv4-hsrp-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.group_number = None
                                self.bfd = Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.Bfd()
                                self.bfd.parent = self
                                self.preempt = None
                                self.primary_ipv4_address = Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.PrimaryIpv4Address()
                                self.primary_ipv4_address.parent = self
                                self.priority = None
                                self.secondary_ipv4_addresses = Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.SecondaryIpv4Addresses()
                                self.secondary_ipv4_addresses.parent = self
                                self.session_name = None
                                self.timers = Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.Timers()
                                self.timers.parent = self
                                self.tracked_interfaces = Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedInterfaces()
                                self.tracked_interfaces.parent = self
                                self.tracked_objects = Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedObjects()
                                self.tracked_objects.parent = self
                                self.virtual_mac_address = None


                            class SecondaryIpv4Addresses(object):
                                """
                                Secondary HSRP IP address Table
                                
                                .. attribute:: secondary_ipv4_address
                                
                                	Secondary HSRP IP address
                                	**type**\: list of    :py:class:`SecondaryIpv4Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.SecondaryIpv4Addresses.SecondaryIpv4Address>`
                                
                                

                                """

                                _prefix = 'ipv4-hsrp-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.secondary_ipv4_address = YList()
                                    self.secondary_ipv4_address.parent = self
                                    self.secondary_ipv4_address.name = 'secondary_ipv4_address'


                                class SecondaryIpv4Address(object):
                                    """
                                    Secondary HSRP IP address
                                    
                                    .. attribute:: address  <key>
                                    
                                    	HSRP IP address
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    

                                    """

                                    _prefix = 'ipv4-hsrp-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.address = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.address is None:
                                            raise YPYModelError('Key property address is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-hsrp-cfg:secondary-ipv4-address[Cisco-IOS-XR-ipv4-hsrp-cfg:address = ' + str(self.address) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.address is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_cfg as meta
                                        return meta._meta_table['Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.SecondaryIpv4Addresses.SecondaryIpv4Address']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-hsrp-cfg:secondary-ipv4-addresses'

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
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_cfg as meta
                                    return meta._meta_table['Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.SecondaryIpv4Addresses']['meta_info']


                            class Bfd(object):
                                """
                                Enable use of Bidirectional Forwarding
                                Detection
                                
                                .. attribute:: address
                                
                                	Enable BFD for this remote IP
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: interface_name
                                
                                	Interface name to run BFD
                                	**type**\:  str
                                
                                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                
                                

                                """

                                _prefix = 'ipv4-hsrp-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.address = None
                                    self.interface_name = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-hsrp-cfg:bfd'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.address is not None:
                                        return True

                                    if self.interface_name is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_cfg as meta
                                    return meta._meta_table['Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.Bfd']['meta_info']


                            class PrimaryIpv4Address(object):
                                """
                                Primary HSRP IP address
                                
                                .. attribute:: address
                                
                                	HSRP IP address
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: virtual_ip_learn
                                
                                	TRUE if the HSRP protocol is to learn the virtual IP address it is to use
                                	**type**\:  bool
                                
                                

                                """

                                _prefix = 'ipv4-hsrp-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.address = None
                                    self.virtual_ip_learn = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-hsrp-cfg:primary-ipv4-address'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.address is not None:
                                        return True

                                    if self.virtual_ip_learn is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_cfg as meta
                                    return meta._meta_table['Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.PrimaryIpv4Address']['meta_info']


                            class TrackedObjects(object):
                                """
                                The HSRP tracked interface configuration
                                table
                                
                                .. attribute:: tracked_object
                                
                                	Object being tracked
                                	**type**\: list of    :py:class:`TrackedObject <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedObjects.TrackedObject>`
                                
                                

                                """

                                _prefix = 'ipv4-hsrp-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.tracked_object = YList()
                                    self.tracked_object.parent = self
                                    self.tracked_object.name = 'tracked_object'


                                class TrackedObject(object):
                                    """
                                    Object being tracked
                                    
                                    .. attribute:: object_name  <key>
                                    
                                    	Interface being tracked
                                    	**type**\:  str
                                    
                                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                    
                                    .. attribute:: priority_decrement
                                    
                                    	Priority decrement
                                    	**type**\:  int
                                    
                                    	**range:** 1..255
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'ipv4-hsrp-cfg'
                                    _revision = '2015-11-09'

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

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-hsrp-cfg:tracked-object[Cisco-IOS-XR-ipv4-hsrp-cfg:object-name = ' + str(self.object_name) + ']'

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
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_cfg as meta
                                        return meta._meta_table['Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedObjects.TrackedObject']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-hsrp-cfg:tracked-objects'

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
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_cfg as meta
                                    return meta._meta_table['Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedObjects']['meta_info']


                            class TrackedInterfaces(object):
                                """
                                The HSRP tracked interface configuration
                                table
                                
                                .. attribute:: tracked_interface
                                
                                	Interface being tracked
                                	**type**\: list of    :py:class:`TrackedInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedInterfaces.TrackedInterface>`
                                
                                

                                """

                                _prefix = 'ipv4-hsrp-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.tracked_interface = YList()
                                    self.tracked_interface.parent = self
                                    self.tracked_interface.name = 'tracked_interface'


                                class TrackedInterface(object):
                                    """
                                    Interface being tracked
                                    
                                    .. attribute:: interface_name  <key>
                                    
                                    	Interface being tracked
                                    	**type**\:  str
                                    
                                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                    
                                    .. attribute:: priority_decrement
                                    
                                    	Priority decrement
                                    	**type**\:  int
                                    
                                    	**range:** 1..255
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'ipv4-hsrp-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.interface_name = None
                                        self.priority_decrement = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.interface_name is None:
                                            raise YPYModelError('Key property interface_name is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-hsrp-cfg:tracked-interface[Cisco-IOS-XR-ipv4-hsrp-cfg:interface-name = ' + str(self.interface_name) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.interface_name is not None:
                                            return True

                                        if self.priority_decrement is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_cfg as meta
                                        return meta._meta_table['Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedInterfaces.TrackedInterface']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-hsrp-cfg:tracked-interfaces'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.tracked_interface is not None:
                                        for child_ref in self.tracked_interface:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_cfg as meta
                                    return meta._meta_table['Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedInterfaces']['meta_info']


                            class Timers(object):
                                """
                                Hello and hold timers
                                
                                .. attribute:: hello_msec
                                
                                	Hello time in msecs
                                	**type**\:  int
                                
                                	**range:** 100..3000
                                
                                	**units**\: millisecond
                                
                                .. attribute:: hello_msec_flag
                                
                                	TRUE \- Hello time configured in milliseconds, FALSE \- Hello time configured in seconds
                                	**type**\:  bool
                                
                                	**default value**\: false
                                
                                .. attribute:: hello_sec
                                
                                	Hello time in seconds
                                	**type**\:  int
                                
                                	**range:** 1..255
                                
                                	**units**\: second
                                
                                	**default value**\: 3
                                
                                .. attribute:: hold_msec
                                
                                	Hold time in msecs
                                	**type**\:  int
                                
                                	**range:** 100..3000
                                
                                	**units**\: millisecond
                                
                                .. attribute:: hold_msec_flag
                                
                                	TRUE \- Hold time configured in milliseconds, FALSE \- Hold time configured in seconds
                                	**type**\:  bool
                                
                                	**default value**\: false
                                
                                .. attribute:: hold_sec
                                
                                	Hold time in seconds
                                	**type**\:  int
                                
                                	**range:** 1..255
                                
                                	**units**\: second
                                
                                	**default value**\: 10
                                
                                

                                """

                                _prefix = 'ipv4-hsrp-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.hello_msec = None
                                    self.hello_msec_flag = None
                                    self.hello_sec = None
                                    self.hold_msec = None
                                    self.hold_msec_flag = None
                                    self.hold_sec = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-hsrp-cfg:timers'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.hello_msec is not None:
                                        return True

                                    if self.hello_msec_flag is not None:
                                        return True

                                    if self.hello_sec is not None:
                                        return True

                                    if self.hold_msec is not None:
                                        return True

                                    if self.hold_msec_flag is not None:
                                        return True

                                    if self.hold_sec is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_cfg as meta
                                    return meta._meta_table['Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.Timers']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.group_number is None:
                                    raise YPYModelError('Key property group_number is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-hsrp-cfg:group[Cisco-IOS-XR-ipv4-hsrp-cfg:group-number = ' + str(self.group_number) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.group_number is not None:
                                    return True

                                if self.bfd is not None and self.bfd._has_data():
                                    return True

                                if self.preempt is not None:
                                    return True

                                if self.primary_ipv4_address is not None and self.primary_ipv4_address._has_data():
                                    return True

                                if self.priority is not None:
                                    return True

                                if self.secondary_ipv4_addresses is not None and self.secondary_ipv4_addresses._has_data():
                                    return True

                                if self.session_name is not None:
                                    return True

                                if self.timers is not None and self.timers._has_data():
                                    return True

                                if self.tracked_interfaces is not None and self.tracked_interfaces._has_data():
                                    return True

                                if self.tracked_objects is not None and self.tracked_objects._has_data():
                                    return True

                                if self.virtual_mac_address is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_cfg as meta
                                return meta._meta_table['Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-hsrp-cfg:groups'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.group is not None:
                                for child_ref in self.group:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_cfg as meta
                            return meta._meta_table['Hsrp.Interfaces.Interface.Ipv4.Version2.Groups']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-hsrp-cfg:version2'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.groups is not None and self.groups._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_cfg as meta
                        return meta._meta_table['Hsrp.Interfaces.Interface.Ipv4.Version2']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-hsrp-cfg:ipv4'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.slave_groups is not None and self.slave_groups._has_data():
                        return True

                    if self.version1 is not None and self.version1._has_data():
                        return True

                    if self.version2 is not None and self.version2._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_cfg as meta
                    return meta._meta_table['Hsrp.Interfaces.Interface.Ipv4']['meta_info']

            @property
            def _common_path(self):
                if self.interface_name is None:
                    raise YPYModelError('Key property interface_name is None')

                return '/Cisco-IOS-XR-ipv4-hsrp-cfg:hsrp/Cisco-IOS-XR-ipv4-hsrp-cfg:interfaces/Cisco-IOS-XR-ipv4-hsrp-cfg:interface[Cisco-IOS-XR-ipv4-hsrp-cfg:interface-name = ' + str(self.interface_name) + ']'

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

                if self.redirects_disable is not None:
                    return True

                if self.use_bia is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_cfg as meta
                return meta._meta_table['Hsrp.Interfaces.Interface']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv4-hsrp-cfg:hsrp/Cisco-IOS-XR-ipv4-hsrp-cfg:interfaces'

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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_cfg as meta
            return meta._meta_table['Hsrp.Interfaces']['meta_info']


    class Logging(object):
        """
        HSRP logging options
        
        .. attribute:: state_change_disable
        
        	HSRP state change IOS messages disable
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'ipv4-hsrp-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.state_change_disable = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv4-hsrp-cfg:hsrp/Cisco-IOS-XR-ipv4-hsrp-cfg:logging'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.state_change_disable is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_cfg as meta
            return meta._meta_table['Hsrp.Logging']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ipv4-hsrp-cfg:hsrp'

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
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_cfg as meta
        return meta._meta_table['Hsrp']['meta_info']


