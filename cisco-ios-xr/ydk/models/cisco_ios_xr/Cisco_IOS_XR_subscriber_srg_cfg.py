""" Cisco_IOS_XR_subscriber_srg_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR subscriber\-srg package configuration.

This module contains definitions
for the following management objects\:
  subscriber\-redundancy\: Subscriber Redundancy configuration

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class SrgAddrFamilyEnum(Enum):
    """
    SrgAddrFamilyEnum

    Srg addr family

    .. data:: ipv4 = 2

    	IPv4

    .. data:: ipv6 = 10

    	IPv6

    """

    ipv4 = 2

    ipv6 = 10


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_srg_cfg as meta
        return meta._meta_table['SrgAddrFamilyEnum']


class SubscriberRedundancyGroupRoleEnum(Enum):
    """
    SubscriberRedundancyGroupRoleEnum

    Subscriber redundancy group role

    .. data:: master = 1

    	Master Role

    .. data:: slave = 2

    	Slave Role

    """

    master = 1

    slave = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_srg_cfg as meta
        return meta._meta_table['SubscriberRedundancyGroupRoleEnum']


class SubscriberRedundancyGroupSlaveModeEnum(Enum):
    """
    SubscriberRedundancyGroupSlaveModeEnum

    Subscriber redundancy group slave mode

    .. data:: warm = 1

    	Warm Mode

    .. data:: hot = 2

    	Hot Mode

    """

    warm = 1

    hot = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_srg_cfg as meta
        return meta._meta_table['SubscriberRedundancyGroupSlaveModeEnum']



class SubscriberRedundancy(object):
    """
    Subscriber Redundancy configuration
    
    .. attribute:: enable
    
    	Enable Subscriber Redundancy configuration. Deletion of this object also causes deletion of all associated objects under SubscriberRedundancy
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: groups
    
    	Table of Group
    	**type**\:   :py:class:`Groups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg.SubscriberRedundancy.Groups>`
    
    .. attribute:: hold_timer
    
    	Set hold time (in Minutes)
    	**type**\:  int
    
    	**range:** 1..65535
    
    	**units**\: minute
    
    .. attribute:: preferred_role
    
    	Set preferred role
    	**type**\:   :py:class:`SubscriberRedundancyGroupRoleEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg.SubscriberRedundancyGroupRoleEnum>`
    
    .. attribute:: redundancy_disable
    
    	Disable
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: revertive_timer
    
    	None
    	**type**\:   :py:class:`RevertiveTimer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg.SubscriberRedundancy.RevertiveTimer>`
    
    .. attribute:: slave_mode
    
    	Set slave
    	**type**\:   :py:class:`SubscriberRedundancyGroupSlaveModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg.SubscriberRedundancyGroupSlaveModeEnum>`
    
    .. attribute:: source_interface
    
    	Source Interface for Redundancy Peer Communication
    	**type**\:  str
    
    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
    
    .. attribute:: virtual_mac_prefix
    
    	Virtual MAC Prefix for Subscriber Redundancy
    	**type**\:  str
    
    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
    
    

    """

    _prefix = 'subscriber-srg-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.enable = None
        self.groups = SubscriberRedundancy.Groups()
        self.groups.parent = self
        self.hold_timer = None
        self.preferred_role = None
        self.redundancy_disable = None
        self.revertive_timer = SubscriberRedundancy.RevertiveTimer()
        self.revertive_timer.parent = self
        self.slave_mode = None
        self.source_interface = None
        self.virtual_mac_prefix = None


    class Groups(object):
        """
        Table of Group
        
        .. attribute:: group
        
        	Redundancy Group configuration
        	**type**\: list of    :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg.SubscriberRedundancy.Groups.Group>`
        
        

        """

        _prefix = 'subscriber-srg-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.group = YList()
            self.group.parent = self
            self.group.name = 'group'


        class Group(object):
            """
            Redundancy Group configuration
            
            .. attribute:: group_id  <key>
            
            	Group ID
            	**type**\:  int
            
            	**range:** 1..500
            
            .. attribute:: access_tracking_object
            
            	Access Tracking Object for this Group
            	**type**\:  str
            
            .. attribute:: core_tracking_object
            
            	Core Tracking Object for this Group
            	**type**\:  str
            
            .. attribute:: description
            
            	Description for this Group
            	**type**\:  str
            
            .. attribute:: disable_tracking_object
            
            	Disable Tracking Object for this Group
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: enable
            
            	Enable Redundancy Group configuration. Deletion of this object also causes deletion of all associated objects under Group
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: enable_fast_switchover
            
            	Enable fast switchover for this Group
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: hold_timer
            
            	Set hold time (in Minutes)
            	**type**\:  int
            
            	**range:** 1..65535
            
            	**units**\: minute
            
            .. attribute:: interface_list
            
            	List of Interfaces for this Group
            	**type**\:   :py:class:`InterfaceList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg.SubscriberRedundancy.Groups.Group.InterfaceList>`
            
            .. attribute:: l2tp_source_ip_address
            
            	Enter an IP address
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: peer
            
            	None
            	**type**\:   :py:class:`Peer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg.SubscriberRedundancy.Groups.Group.Peer>`
            
            .. attribute:: preferred_role
            
            	Set preferred role
            	**type**\:   :py:class:`SubscriberRedundancyGroupRoleEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg.SubscriberRedundancyGroupRoleEnum>`
            
            .. attribute:: redundancy_disable
            
            	Disable
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: revertive_timer
            
            	None
            	**type**\:   :py:class:`RevertiveTimer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg.SubscriberRedundancy.Groups.Group.RevertiveTimer>`
            
            .. attribute:: slave_mode
            
            	Set Slave Mode
            	**type**\:   :py:class:`SubscriberRedundancyGroupSlaveModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg.SubscriberRedundancyGroupSlaveModeEnum>`
            
            .. attribute:: state_control_route
            
            	None
            	**type**\:   :py:class:`StateControlRoute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg.SubscriberRedundancy.Groups.Group.StateControlRoute>`
            
            .. attribute:: virtual_mac
            
            	Virtual MAC Address for this Group
            	**type**\:   :py:class:`VirtualMac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg.SubscriberRedundancy.Groups.Group.VirtualMac>`
            
            

            """

            _prefix = 'subscriber-srg-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.group_id = None
                self.access_tracking_object = None
                self.core_tracking_object = None
                self.description = None
                self.disable_tracking_object = None
                self.enable = None
                self.enable_fast_switchover = None
                self.hold_timer = None
                self.interface_list = SubscriberRedundancy.Groups.Group.InterfaceList()
                self.interface_list.parent = self
                self.l2tp_source_ip_address = None
                self.peer = SubscriberRedundancy.Groups.Group.Peer()
                self.peer.parent = self
                self.preferred_role = None
                self.redundancy_disable = None
                self.revertive_timer = SubscriberRedundancy.Groups.Group.RevertiveTimer()
                self.revertive_timer.parent = self
                self.slave_mode = None
                self.state_control_route = SubscriberRedundancy.Groups.Group.StateControlRoute()
                self.state_control_route.parent = self
                self.virtual_mac = SubscriberRedundancy.Groups.Group.VirtualMac()
                self.virtual_mac.parent = self


            class InterfaceList(object):
                """
                List of Interfaces for this Group
                
                .. attribute:: enable
                
                	Enable List of Interfaces for this Group. Deletion of this object also causes deletion of all associated objects under InterfaceList 
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: interface_ranges
                
                	Table of InterfaceRange
                	**type**\:   :py:class:`InterfaceRanges <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg.SubscriberRedundancy.Groups.Group.InterfaceList.InterfaceRanges>`
                
                .. attribute:: interfaces
                
                	Table of Interface
                	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg.SubscriberRedundancy.Groups.Group.InterfaceList.Interfaces>`
                
                

                """

                _prefix = 'subscriber-srg-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.enable = None
                    self.interface_ranges = SubscriberRedundancy.Groups.Group.InterfaceList.InterfaceRanges()
                    self.interface_ranges.parent = self
                    self.interfaces = SubscriberRedundancy.Groups.Group.InterfaceList.Interfaces()
                    self.interfaces.parent = self


                class Interfaces(object):
                    """
                    Table of Interface
                    
                    .. attribute:: interface
                    
                    	Interface for this Group
                    	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg.SubscriberRedundancy.Groups.Group.InterfaceList.Interfaces.Interface>`
                    
                    

                    """

                    _prefix = 'subscriber-srg-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.interface = YList()
                        self.interface.parent = self
                        self.interface.name = 'interface'


                    class Interface(object):
                        """
                        Interface for this Group
                        
                        .. attribute:: interface_name  <key>
                        
                        	Interface name
                        	**type**\:  str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        .. attribute:: interface_id
                        
                        	Interface Id for the interface
                        	**type**\:  int
                        
                        	**range:** 1..65535
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'subscriber-srg-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.interface_name = None
                            self.interface_id = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.interface_name is None:
                                raise YPYModelError('Key property interface_name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-subscriber-srg-cfg:interface[Cisco-IOS-XR-subscriber-srg-cfg:interface-name = ' + str(self.interface_name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.interface_name is not None:
                                return True

                            if self.interface_id is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_srg_cfg as meta
                            return meta._meta_table['SubscriberRedundancy.Groups.Group.InterfaceList.Interfaces.Interface']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-subscriber-srg-cfg:interfaces'

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
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_srg_cfg as meta
                        return meta._meta_table['SubscriberRedundancy.Groups.Group.InterfaceList.Interfaces']['meta_info']


                class InterfaceRanges(object):
                    """
                    Table of InterfaceRange
                    
                    .. attribute:: interface_range
                    
                    	Interface for this Group
                    	**type**\: list of    :py:class:`InterfaceRange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg.SubscriberRedundancy.Groups.Group.InterfaceList.InterfaceRanges.InterfaceRange>`
                    
                    

                    """

                    _prefix = 'subscriber-srg-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.interface_range = YList()
                        self.interface_range.parent = self
                        self.interface_range.name = 'interface_range'


                    class InterfaceRange(object):
                        """
                        Interface for this Group
                        
                        .. attribute:: interface_name  <key>
                        
                        	Interface name
                        	**type**\:  str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        .. attribute:: sub_interface_range_start  <key>
                        
                        	Sub Interface Start Range
                        	**type**\:  int
                        
                        	**range:** 0..2147483647
                        
                        .. attribute:: sub_interface_range_end  <key>
                        
                        	Sub Interface End Range
                        	**type**\:  int
                        
                        	**range:** 0..2147483647
                        
                        .. attribute:: interface_id_range_end
                        
                        	Interface ID End Range
                        	**type**\:  int
                        
                        	**range:** 1..65535
                        
                        .. attribute:: interface_id_range_start
                        
                        	Interface ID Start Range
                        	**type**\:  int
                        
                        	**range:** 1..65535
                        
                        

                        """

                        _prefix = 'subscriber-srg-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.interface_name = None
                            self.sub_interface_range_start = None
                            self.sub_interface_range_end = None
                            self.interface_id_range_end = None
                            self.interface_id_range_start = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.interface_name is None:
                                raise YPYModelError('Key property interface_name is None')
                            if self.sub_interface_range_start is None:
                                raise YPYModelError('Key property sub_interface_range_start is None')
                            if self.sub_interface_range_end is None:
                                raise YPYModelError('Key property sub_interface_range_end is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-subscriber-srg-cfg:interface-range[Cisco-IOS-XR-subscriber-srg-cfg:interface-name = ' + str(self.interface_name) + '][Cisco-IOS-XR-subscriber-srg-cfg:sub-interface-range-start = ' + str(self.sub_interface_range_start) + '][Cisco-IOS-XR-subscriber-srg-cfg:sub-interface-range-end = ' + str(self.sub_interface_range_end) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.interface_name is not None:
                                return True

                            if self.sub_interface_range_start is not None:
                                return True

                            if self.sub_interface_range_end is not None:
                                return True

                            if self.interface_id_range_end is not None:
                                return True

                            if self.interface_id_range_start is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_srg_cfg as meta
                            return meta._meta_table['SubscriberRedundancy.Groups.Group.InterfaceList.InterfaceRanges.InterfaceRange']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-subscriber-srg-cfg:interface-ranges'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.interface_range is not None:
                            for child_ref in self.interface_range:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_srg_cfg as meta
                        return meta._meta_table['SubscriberRedundancy.Groups.Group.InterfaceList.InterfaceRanges']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-subscriber-srg-cfg:interface-list'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.enable is not None:
                        return True

                    if self.interface_ranges is not None and self.interface_ranges._has_data():
                        return True

                    if self.interfaces is not None and self.interfaces._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_srg_cfg as meta
                    return meta._meta_table['SubscriberRedundancy.Groups.Group.InterfaceList']['meta_info']


            class Peer(object):
                """
                None
                
                .. attribute:: ipaddress
                
                	IPv4 or IPv6 Address of SRG Peer
                	**type**\:   :py:class:`Ipaddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg.SubscriberRedundancy.Groups.Group.Peer.Ipaddress>`
                
                .. attribute:: route_add_disable
                
                	Set Route add disable
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'subscriber-srg-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.ipaddress = SubscriberRedundancy.Groups.Group.Peer.Ipaddress()
                    self.ipaddress.parent = self
                    self.route_add_disable = None


                class Ipaddress(object):
                    """
                    IPv4 or IPv6 Address of SRG Peer
                    
                    .. attribute:: address_family
                    
                    	Type of IPv4/IPv6 address
                    	**type**\:   :py:class:`SrgAddrFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg.SrgAddrFamilyEnum>`
                    
                    .. attribute:: prefix_string
                    
                    	IPv4/IPv6 address
                    	**type**\: one of the below types:
                    
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    

                    """

                    _prefix = 'subscriber-srg-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.address_family = None
                        self.prefix_string = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-subscriber-srg-cfg:ipaddress'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.address_family is not None:
                            return True

                        if self.prefix_string is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_srg_cfg as meta
                        return meta._meta_table['SubscriberRedundancy.Groups.Group.Peer.Ipaddress']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-subscriber-srg-cfg:peer'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.ipaddress is not None and self.ipaddress._has_data():
                        return True

                    if self.route_add_disable is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_srg_cfg as meta
                    return meta._meta_table['SubscriberRedundancy.Groups.Group.Peer']['meta_info']


            class RevertiveTimer(object):
                """
                None
                
                .. attribute:: max_value
                
                	Value of MAX Revertive Timer
                	**type**\:  int
                
                	**range:** 1..65535
                
                .. attribute:: value
                
                	Value of revertive time in minutes
                	**type**\:  int
                
                	**range:** 1..65535
                
                	**units**\: minute
                
                

                """

                _prefix = 'subscriber-srg-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.max_value = None
                    self.value = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-subscriber-srg-cfg:revertive-timer'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.max_value is not None:
                        return True

                    if self.value is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_srg_cfg as meta
                    return meta._meta_table['SubscriberRedundancy.Groups.Group.RevertiveTimer']['meta_info']


            class VirtualMac(object):
                """
                Virtual MAC Address for this Group
                
                .. attribute:: address
                
                	Virtual MAC Address for this Group
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: disable
                
                	Disable Virtual MAC Address for this Group
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'subscriber-srg-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.address = None
                    self.disable = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-subscriber-srg-cfg:virtual-mac'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.address is not None:
                        return True

                    if self.disable is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_srg_cfg as meta
                    return meta._meta_table['SubscriberRedundancy.Groups.Group.VirtualMac']['meta_info']


            class StateControlRoute(object):
                """
                None
                
                .. attribute:: ipv4_route
                
                	None
                	**type**\:   :py:class:`Ipv4Route <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg.SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv4Route>`
                
                .. attribute:: ipv6_route
                
                	None
                	**type**\:   :py:class:`Ipv6Route <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg.SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route>`
                
                

                """

                _prefix = 'subscriber-srg-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.ipv4_route = SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv4Route()
                    self.ipv4_route.parent = self
                    self.ipv6_route = SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route()
                    self.ipv6_route.parent = self


                class Ipv4Route(object):
                    """
                    None
                    
                    .. attribute:: address_family
                    
                    	Type of IPv4 address with prefix\-length
                    	**type**\:   :py:class:`SrgAddrFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg.SrgAddrFamilyEnum>`
                    
                    .. attribute:: prefix_length
                    
                    	Prefix of the IP Address
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: prefix_string
                    
                    	IPv4 address with prefix\-length
                    	**type**\: one of the below types:
                    
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    .. attribute:: value
                    
                    	Tag value
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    

                    """

                    _prefix = 'subscriber-srg-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.address_family = None
                        self.prefix_length = None
                        self.prefix_string = None
                        self.value = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-subscriber-srg-cfg:ipv4-route'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.address_family is not None:
                            return True

                        if self.prefix_length is not None:
                            return True

                        if self.prefix_string is not None:
                            return True

                        if self.value is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_srg_cfg as meta
                        return meta._meta_table['SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv4Route']['meta_info']


                class Ipv6Route(object):
                    """
                    None
                    
                    .. attribute:: ipv6na_route
                    
                    	None
                    	**type**\:   :py:class:`Ipv6NaRoute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg.SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route.Ipv6NaRoute>`
                    
                    .. attribute:: ipv6pd_route
                    
                    	None
                    	**type**\:   :py:class:`Ipv6PdRoute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg.SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route.Ipv6PdRoute>`
                    
                    

                    """

                    _prefix = 'subscriber-srg-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.ipv6na_route = SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route.Ipv6NaRoute()
                        self.ipv6na_route.parent = self
                        self.ipv6pd_route = SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route.Ipv6PdRoute()
                        self.ipv6pd_route.parent = self


                    class Ipv6NaRoute(object):
                        """
                        None
                        
                        .. attribute:: address_family
                        
                        	Type of IPv6 address with prefix\-length
                        	**type**\:   :py:class:`SrgAddrFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg.SrgAddrFamilyEnum>`
                        
                        .. attribute:: prefix_length
                        
                        	Prefix of the IP Address
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: prefix_string
                        
                        	IPv6 address with prefix\-length
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: value
                        
                        	Tag value
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        

                        """

                        _prefix = 'subscriber-srg-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.address_family = None
                            self.prefix_length = None
                            self.prefix_string = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-subscriber-srg-cfg:ipv6na-route'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.address_family is not None:
                                return True

                            if self.prefix_length is not None:
                                return True

                            if self.prefix_string is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_srg_cfg as meta
                            return meta._meta_table['SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route.Ipv6NaRoute']['meta_info']


                    class Ipv6PdRoute(object):
                        """
                        None
                        
                        .. attribute:: address_family
                        
                        	Type of IPv6 address with prefix\-length
                        	**type**\:   :py:class:`SrgAddrFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg.SrgAddrFamilyEnum>`
                        
                        .. attribute:: prefix_length
                        
                        	Prefix of the IP Address
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: prefix_string
                        
                        	IPv6 address with prefix\-length
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: value
                        
                        	Tag value
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        

                        """

                        _prefix = 'subscriber-srg-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.address_family = None
                            self.prefix_length = None
                            self.prefix_string = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-subscriber-srg-cfg:ipv6pd-route'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.address_family is not None:
                                return True

                            if self.prefix_length is not None:
                                return True

                            if self.prefix_string is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_srg_cfg as meta
                            return meta._meta_table['SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route.Ipv6PdRoute']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-subscriber-srg-cfg:ipv6-route'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.ipv6na_route is not None and self.ipv6na_route._has_data():
                            return True

                        if self.ipv6pd_route is not None and self.ipv6pd_route._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_srg_cfg as meta
                        return meta._meta_table['SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-subscriber-srg-cfg:state-control-route'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.ipv4_route is not None and self.ipv4_route._has_data():
                        return True

                    if self.ipv6_route is not None and self.ipv6_route._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_srg_cfg as meta
                    return meta._meta_table['SubscriberRedundancy.Groups.Group.StateControlRoute']['meta_info']

            @property
            def _common_path(self):
                if self.group_id is None:
                    raise YPYModelError('Key property group_id is None')

                return '/Cisco-IOS-XR-subscriber-srg-cfg:subscriber-redundancy/Cisco-IOS-XR-subscriber-srg-cfg:groups/Cisco-IOS-XR-subscriber-srg-cfg:group[Cisco-IOS-XR-subscriber-srg-cfg:group-id = ' + str(self.group_id) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.group_id is not None:
                    return True

                if self.access_tracking_object is not None:
                    return True

                if self.core_tracking_object is not None:
                    return True

                if self.description is not None:
                    return True

                if self.disable_tracking_object is not None:
                    return True

                if self.enable is not None:
                    return True

                if self.enable_fast_switchover is not None:
                    return True

                if self.hold_timer is not None:
                    return True

                if self.interface_list is not None and self.interface_list._has_data():
                    return True

                if self.l2tp_source_ip_address is not None:
                    return True

                if self.peer is not None and self.peer._has_data():
                    return True

                if self.preferred_role is not None:
                    return True

                if self.redundancy_disable is not None:
                    return True

                if self.revertive_timer is not None and self.revertive_timer._has_data():
                    return True

                if self.slave_mode is not None:
                    return True

                if self.state_control_route is not None and self.state_control_route._has_data():
                    return True

                if self.virtual_mac is not None and self.virtual_mac._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_srg_cfg as meta
                return meta._meta_table['SubscriberRedundancy.Groups.Group']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-subscriber-srg-cfg:subscriber-redundancy/Cisco-IOS-XR-subscriber-srg-cfg:groups'

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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_srg_cfg as meta
            return meta._meta_table['SubscriberRedundancy.Groups']['meta_info']


    class RevertiveTimer(object):
        """
        None
        
        .. attribute:: max_value
        
        	Value of MAX Revertive Timer
        	**type**\:  int
        
        	**range:** 1..65535
        
        .. attribute:: value
        
        	Value of revertive time in minutes
        	**type**\:  int
        
        	**range:** 1..65535
        
        	**units**\: minute
        
        

        """

        _prefix = 'subscriber-srg-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.max_value = None
            self.value = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-subscriber-srg-cfg:subscriber-redundancy/Cisco-IOS-XR-subscriber-srg-cfg:revertive-timer'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.max_value is not None:
                return True

            if self.value is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_srg_cfg as meta
            return meta._meta_table['SubscriberRedundancy.RevertiveTimer']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-subscriber-srg-cfg:subscriber-redundancy'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.enable is not None:
            return True

        if self.groups is not None and self.groups._has_data():
            return True

        if self.hold_timer is not None:
            return True

        if self.preferred_role is not None:
            return True

        if self.redundancy_disable is not None:
            return True

        if self.revertive_timer is not None and self.revertive_timer._has_data():
            return True

        if self.slave_mode is not None:
            return True

        if self.source_interface is not None:
            return True

        if self.virtual_mac_prefix is not None:
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_srg_cfg as meta
        return meta._meta_table['SubscriberRedundancy']['meta_info']


