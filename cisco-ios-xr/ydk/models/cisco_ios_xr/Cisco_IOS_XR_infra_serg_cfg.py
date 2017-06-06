""" Cisco_IOS_XR_infra_serg_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-serg package configuration.

This module contains definitions
for the following management objects\:
  session\-redundancy\: Session Redundancy configuration

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class SergAddrFamilyEnum(Enum):
    """
    SergAddrFamilyEnum

    Serg addr family

    .. data:: ipv4 = 2

    	IPv4

    .. data:: ipv6 = 10

    	IPv6

    """

    ipv4 = 2

    ipv6 = 10


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_serg_cfg as meta
        return meta._meta_table['SergAddrFamilyEnum']


class SessionRedundancyGroupRoleEnum(Enum):
    """
    SessionRedundancyGroupRoleEnum

    Session redundancy group role

    .. data:: master = 1

    	Master Role

    .. data:: slave = 2

    	Slave Role

    """

    master = 1

    slave = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_serg_cfg as meta
        return meta._meta_table['SessionRedundancyGroupRoleEnum']



class SessionRedundancy(object):
    """
    Session Redundancy configuration
    
    .. attribute:: enable
    
    	Enable Session Redundancy configuration. Deletion of this object also causes deletion of all associated objects under SessionRedundancy
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: groups
    
    	Table of Group
    	**type**\:   :py:class:`Groups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_cfg.SessionRedundancy.Groups>`
    
    .. attribute:: hold_timer
    
    	Set hold time (in Minutes)
    	**type**\:  int
    
    	**range:** 1..65535
    
    	**units**\: minute
    
    .. attribute:: preferred_role
    
    	Set preferred role
    	**type**\:   :py:class:`SessionRedundancyGroupRoleEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_cfg.SessionRedundancyGroupRoleEnum>`
    
    .. attribute:: redundancy_disable
    
    	Disable
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: revertive_timer
    
    	None
    	**type**\:   :py:class:`RevertiveTimer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_cfg.SessionRedundancy.RevertiveTimer>`
    
    .. attribute:: source_interface
    
    	Source Interface for Redundancy Peer Communication
    	**type**\:  str
    
    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
    
    

    """

    _prefix = 'infra-serg-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.enable = None
        self.groups = SessionRedundancy.Groups()
        self.groups.parent = self
        self.hold_timer = None
        self.preferred_role = None
        self.redundancy_disable = None
        self.revertive_timer = SessionRedundancy.RevertiveTimer()
        self.revertive_timer.parent = self
        self.source_interface = None


    class Groups(object):
        """
        Table of Group
        
        .. attribute:: group
        
        	Redundancy Group configuration
        	**type**\: list of    :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_cfg.SessionRedundancy.Groups.Group>`
        
        

        """

        _prefix = 'infra-serg-cfg'
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
            
            .. attribute:: hold_timer
            
            	Set hold time (in Minutes)
            	**type**\:  int
            
            	**range:** 1..65535
            
            	**units**\: minute
            
            .. attribute:: interface_list
            
            	List of Interfaces for this Group
            	**type**\:   :py:class:`InterfaceList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_cfg.SessionRedundancy.Groups.Group.InterfaceList>`
            
            .. attribute:: peer
            
            	None
            	**type**\:   :py:class:`Peer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_cfg.SessionRedundancy.Groups.Group.Peer>`
            
            .. attribute:: preferred_role
            
            	Set preferred role
            	**type**\:   :py:class:`SessionRedundancyGroupRoleEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_cfg.SessionRedundancyGroupRoleEnum>`
            
            .. attribute:: redundancy_disable
            
            	Disable
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: revertive_timer
            
            	None
            	**type**\:   :py:class:`RevertiveTimer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_cfg.SessionRedundancy.Groups.Group.RevertiveTimer>`
            
            

            """

            _prefix = 'infra-serg-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.group_id = None
                self.access_tracking_object = None
                self.core_tracking_object = None
                self.description = None
                self.disable_tracking_object = None
                self.enable = None
                self.hold_timer = None
                self.interface_list = SessionRedundancy.Groups.Group.InterfaceList()
                self.interface_list.parent = self
                self.peer = SessionRedundancy.Groups.Group.Peer()
                self.peer.parent = self
                self.preferred_role = None
                self.redundancy_disable = None
                self.revertive_timer = SessionRedundancy.Groups.Group.RevertiveTimer()
                self.revertive_timer.parent = self


            class Peer(object):
                """
                None
                
                .. attribute:: ipaddress
                
                	IPv4 or IPv6 Address of SERG Peer
                	**type**\:   :py:class:`Ipaddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_cfg.SessionRedundancy.Groups.Group.Peer.Ipaddress>`
                
                

                """

                _prefix = 'infra-serg-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.ipaddress = SessionRedundancy.Groups.Group.Peer.Ipaddress()
                    self.ipaddress.parent = self


                class Ipaddress(object):
                    """
                    IPv4 or IPv6 Address of SERG Peer
                    
                    .. attribute:: address_family
                    
                    	Type of IPv4/IPv6 address
                    	**type**\:   :py:class:`SergAddrFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_cfg.SergAddrFamilyEnum>`
                    
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

                    _prefix = 'infra-serg-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.address_family = None
                        self.prefix_string = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-serg-cfg:ipaddress'

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
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_serg_cfg as meta
                        return meta._meta_table['SessionRedundancy.Groups.Group.Peer.Ipaddress']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-infra-serg-cfg:peer'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.ipaddress is not None and self.ipaddress._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_serg_cfg as meta
                    return meta._meta_table['SessionRedundancy.Groups.Group.Peer']['meta_info']


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

                _prefix = 'infra-serg-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.max_value = None
                    self.value = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-infra-serg-cfg:revertive-timer'

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
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_serg_cfg as meta
                    return meta._meta_table['SessionRedundancy.Groups.Group.RevertiveTimer']['meta_info']


            class InterfaceList(object):
                """
                List of Interfaces for this Group
                
                .. attribute:: enable
                
                	Enable List of Interfaces for this Group. Deletion of this object also causes deletion of all associated objects under InterfaceList 
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: interface_ranges
                
                	Table of InterfaceRange
                	**type**\:   :py:class:`InterfaceRanges <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_cfg.SessionRedundancy.Groups.Group.InterfaceList.InterfaceRanges>`
                
                .. attribute:: interfaces
                
                	Table of Interface
                	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_cfg.SessionRedundancy.Groups.Group.InterfaceList.Interfaces>`
                
                

                """

                _prefix = 'infra-serg-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.enable = None
                    self.interface_ranges = SessionRedundancy.Groups.Group.InterfaceList.InterfaceRanges()
                    self.interface_ranges.parent = self
                    self.interfaces = SessionRedundancy.Groups.Group.InterfaceList.Interfaces()
                    self.interfaces.parent = self


                class InterfaceRanges(object):
                    """
                    Table of InterfaceRange
                    
                    .. attribute:: interface_range
                    
                    	Interface for this Group
                    	**type**\: list of    :py:class:`InterfaceRange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_cfg.SessionRedundancy.Groups.Group.InterfaceList.InterfaceRanges.InterfaceRange>`
                    
                    

                    """

                    _prefix = 'infra-serg-cfg'
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

                        _prefix = 'infra-serg-cfg'
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

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-serg-cfg:interface-range[Cisco-IOS-XR-infra-serg-cfg:interface-name = ' + str(self.interface_name) + '][Cisco-IOS-XR-infra-serg-cfg:sub-interface-range-start = ' + str(self.sub_interface_range_start) + '][Cisco-IOS-XR-infra-serg-cfg:sub-interface-range-end = ' + str(self.sub_interface_range_end) + ']'

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
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_serg_cfg as meta
                            return meta._meta_table['SessionRedundancy.Groups.Group.InterfaceList.InterfaceRanges.InterfaceRange']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-serg-cfg:interface-ranges'

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
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_serg_cfg as meta
                        return meta._meta_table['SessionRedundancy.Groups.Group.InterfaceList.InterfaceRanges']['meta_info']


                class Interfaces(object):
                    """
                    Table of Interface
                    
                    .. attribute:: interface
                    
                    	Interface for this Group
                    	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_cfg.SessionRedundancy.Groups.Group.InterfaceList.Interfaces.Interface>`
                    
                    

                    """

                    _prefix = 'infra-serg-cfg'
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

                        _prefix = 'infra-serg-cfg'
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

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-serg-cfg:interface[Cisco-IOS-XR-infra-serg-cfg:interface-name = ' + str(self.interface_name) + ']'

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
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_serg_cfg as meta
                            return meta._meta_table['SessionRedundancy.Groups.Group.InterfaceList.Interfaces.Interface']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-serg-cfg:interfaces'

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
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_serg_cfg as meta
                        return meta._meta_table['SessionRedundancy.Groups.Group.InterfaceList.Interfaces']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-infra-serg-cfg:interface-list'

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
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_serg_cfg as meta
                    return meta._meta_table['SessionRedundancy.Groups.Group.InterfaceList']['meta_info']

            @property
            def _common_path(self):
                if self.group_id is None:
                    raise YPYModelError('Key property group_id is None')

                return '/Cisco-IOS-XR-infra-serg-cfg:session-redundancy/Cisco-IOS-XR-infra-serg-cfg:groups/Cisco-IOS-XR-infra-serg-cfg:group[Cisco-IOS-XR-infra-serg-cfg:group-id = ' + str(self.group_id) + ']'

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

                if self.hold_timer is not None:
                    return True

                if self.interface_list is not None and self.interface_list._has_data():
                    return True

                if self.peer is not None and self.peer._has_data():
                    return True

                if self.preferred_role is not None:
                    return True

                if self.redundancy_disable is not None:
                    return True

                if self.revertive_timer is not None and self.revertive_timer._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_serg_cfg as meta
                return meta._meta_table['SessionRedundancy.Groups.Group']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-serg-cfg:session-redundancy/Cisco-IOS-XR-infra-serg-cfg:groups'

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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_serg_cfg as meta
            return meta._meta_table['SessionRedundancy.Groups']['meta_info']


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

        _prefix = 'infra-serg-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.max_value = None
            self.value = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-serg-cfg:session-redundancy/Cisco-IOS-XR-infra-serg-cfg:revertive-timer'

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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_serg_cfg as meta
            return meta._meta_table['SessionRedundancy.RevertiveTimer']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-infra-serg-cfg:session-redundancy'

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

        if self.source_interface is not None:
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_serg_cfg as meta
        return meta._meta_table['SessionRedundancy']['meta_info']


