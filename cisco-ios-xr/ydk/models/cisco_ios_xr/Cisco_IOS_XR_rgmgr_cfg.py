""" Cisco_IOS_XR_rgmgr_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR rgmgr package configuration.

This module contains definitions
for the following management objects\:
  redundancy\-group\-manager\: Redundancy Group Manager
    Configuration

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class IccpModeEnum(Enum):
    """
    IccpModeEnum

    Iccp mode

    .. data:: singleton = 1

    	Run the ICCP group in Singleton mode

    """

    singleton = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_rgmgr_cfg as meta
        return meta._meta_table['IccpModeEnum']



class RedundancyGroupManager(object):
    """
    Redundancy Group Manager Configuration
    
    .. attribute:: aps
    
    	MR\-APS groups
    	**type**\:   :py:class:`Aps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_cfg.RedundancyGroupManager.Aps>`
    
    .. attribute:: enable
    
    	Enable redundancy group manager
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: iccp
    
    	ICCP configuration
    	**type**\:   :py:class:`Iccp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_cfg.RedundancyGroupManager.Iccp>`
    
    

    """

    _prefix = 'rgmgr-cfg'
    _revision = '2015-07-30'

    def __init__(self):
        self.aps = RedundancyGroupManager.Aps()
        self.aps.parent = self
        self.enable = None
        self.iccp = RedundancyGroupManager.Iccp()
        self.iccp.parent = self


    class Aps(object):
        """
        MR\-APS groups
        
        .. attribute:: default_redundancy_group
        
        	Default SONET controller backup configuration
        	**type**\:   :py:class:`DefaultRedundancyGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_cfg.RedundancyGroupManager.Aps.DefaultRedundancyGroup>`
        
        .. attribute:: groups
        
        	Redundancy Group Table
        	**type**\:   :py:class:`Groups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_cfg.RedundancyGroupManager.Aps.Groups>`
        
        

        """

        _prefix = 'rgmgr-cfg'
        _revision = '2015-07-30'

        def __init__(self):
            self.parent = None
            self.default_redundancy_group = RedundancyGroupManager.Aps.DefaultRedundancyGroup()
            self.default_redundancy_group.parent = self
            self.groups = RedundancyGroupManager.Aps.Groups()
            self.groups.parent = self


        class DefaultRedundancyGroup(object):
            """
            Default SONET controller backup configuration
            
            .. attribute:: backup_interface_name
            
            	Backup interface name
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: next_hop_address
            
            	IPv4 address of remote peer
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            

            """

            _prefix = 'rgmgr-cfg'
            _revision = '2015-07-30'

            def __init__(self):
                self.parent = None
                self.backup_interface_name = None
                self.next_hop_address = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-rgmgr-cfg:redundancy-group-manager/Cisco-IOS-XR-rgmgr-cfg:aps/Cisco-IOS-XR-rgmgr-cfg:default-redundancy-group'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.backup_interface_name is not None:
                    return True

                if self.next_hop_address is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_rgmgr_cfg as meta
                return meta._meta_table['RedundancyGroupManager.Aps.DefaultRedundancyGroup']['meta_info']


        class Groups(object):
            """
            Redundancy Group Table
            
            .. attribute:: group
            
            	Redundancy Group Configuration
            	**type**\: list of    :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_cfg.RedundancyGroupManager.Aps.Groups.Group>`
            
            

            """

            _prefix = 'rgmgr-cfg'
            _revision = '2015-07-30'

            def __init__(self):
                self.parent = None
                self.group = YList()
                self.group.parent = self
                self.group.name = 'group'


            class Group(object):
                """
                Redundancy Group Configuration
                
                .. attribute:: group_id  <key>
                
                	The redundancy group ID
                	**type**\:  int
                
                	**range:** 1..32
                
                .. attribute:: controllers
                
                	Controller configuration
                	**type**\:   :py:class:`Controllers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_cfg.RedundancyGroupManager.Aps.Groups.Group.Controllers>`
                
                

                """

                _prefix = 'rgmgr-cfg'
                _revision = '2015-07-30'

                def __init__(self):
                    self.parent = None
                    self.group_id = None
                    self.controllers = RedundancyGroupManager.Aps.Groups.Group.Controllers()
                    self.controllers.parent = self


                class Controllers(object):
                    """
                    Controller configuration
                    
                    .. attribute:: controller
                    
                    	none
                    	**type**\: list of    :py:class:`Controller <ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_cfg.RedundancyGroupManager.Aps.Groups.Group.Controllers.Controller>`
                    
                    

                    """

                    _prefix = 'rgmgr-cfg'
                    _revision = '2015-07-30'

                    def __init__(self):
                        self.parent = None
                        self.controller = YList()
                        self.controller.parent = self
                        self.controller.name = 'controller'


                    class Controller(object):
                        """
                        none
                        
                        .. attribute:: controller_name  <key>
                        
                        	Controller Name
                        	**type**\:  str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        .. attribute:: backup_interface_name
                        
                        	Backup interface name
                        	**type**\:  str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        .. attribute:: next_hop_address
                        
                        	IPv4 address of remote peer
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'rgmgr-cfg'
                        _revision = '2015-07-30'

                        def __init__(self):
                            self.parent = None
                            self.controller_name = None
                            self.backup_interface_name = None
                            self.next_hop_address = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.controller_name is None:
                                raise YPYModelError('Key property controller_name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-rgmgr-cfg:controller[Cisco-IOS-XR-rgmgr-cfg:controller-name = ' + str(self.controller_name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.controller_name is not None:
                                return True

                            if self.backup_interface_name is not None:
                                return True

                            if self.next_hop_address is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_rgmgr_cfg as meta
                            return meta._meta_table['RedundancyGroupManager.Aps.Groups.Group.Controllers.Controller']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-rgmgr-cfg:controllers'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.controller is not None:
                            for child_ref in self.controller:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_rgmgr_cfg as meta
                        return meta._meta_table['RedundancyGroupManager.Aps.Groups.Group.Controllers']['meta_info']

                @property
                def _common_path(self):
                    if self.group_id is None:
                        raise YPYModelError('Key property group_id is None')

                    return '/Cisco-IOS-XR-rgmgr-cfg:redundancy-group-manager/Cisco-IOS-XR-rgmgr-cfg:aps/Cisco-IOS-XR-rgmgr-cfg:groups/Cisco-IOS-XR-rgmgr-cfg:group[Cisco-IOS-XR-rgmgr-cfg:group-id = ' + str(self.group_id) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.group_id is not None:
                        return True

                    if self.controllers is not None and self.controllers._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_rgmgr_cfg as meta
                    return meta._meta_table['RedundancyGroupManager.Aps.Groups.Group']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-rgmgr-cfg:redundancy-group-manager/Cisco-IOS-XR-rgmgr-cfg:aps/Cisco-IOS-XR-rgmgr-cfg:groups'

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
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_rgmgr_cfg as meta
                return meta._meta_table['RedundancyGroupManager.Aps.Groups']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-rgmgr-cfg:redundancy-group-manager/Cisco-IOS-XR-rgmgr-cfg:aps'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.default_redundancy_group is not None and self.default_redundancy_group._has_data():
                return True

            if self.groups is not None and self.groups._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_rgmgr_cfg as meta
            return meta._meta_table['RedundancyGroupManager.Aps']['meta_info']


    class Iccp(object):
        """
        ICCP configuration
        
        .. attribute:: iccp_groups
        
        	Redundancy Group Table Configuration
        	**type**\:   :py:class:`IccpGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_cfg.RedundancyGroupManager.Iccp.IccpGroups>`
        
        

        """

        _prefix = 'rgmgr-cfg'
        _revision = '2015-07-30'

        def __init__(self):
            self.parent = None
            self.iccp_groups = RedundancyGroupManager.Iccp.IccpGroups()
            self.iccp_groups.parent = self


        class IccpGroups(object):
            """
            Redundancy Group Table Configuration
            
            .. attribute:: iccp_group
            
            	Redundancy Group Configuration
            	**type**\: list of    :py:class:`IccpGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_cfg.RedundancyGroupManager.Iccp.IccpGroups.IccpGroup>`
            
            

            """

            _prefix = 'rgmgr-cfg'
            _revision = '2015-07-30'

            def __init__(self):
                self.parent = None
                self.iccp_group = YList()
                self.iccp_group.parent = self
                self.iccp_group.name = 'iccp_group'


            class IccpGroup(object):
                """
                Redundancy Group Configuration
                
                .. attribute:: group_number  <key>
                
                	The redundancy icc group number
                	**type**\:  int
                
                	**range:** 1..4294967295
                
                .. attribute:: backbones
                
                	ICCP backbone configuration
                	**type**\:   :py:class:`Backbones <ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_cfg.RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Backbones>`
                
                .. attribute:: isolation_recovery_delay
                
                	ICCP isolation recovery delay
                	**type**\:  int
                
                	**range:** 30..600
                
                	**units**\: second
                
                .. attribute:: members
                
                	ICCP member configuration
                	**type**\:   :py:class:`Members <ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_cfg.RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Members>`
                
                .. attribute:: mlacp
                
                	Multi\-chassis Link Aggregation Control Protocol commands
                	**type**\:   :py:class:`Mlacp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_cfg.RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Mlacp>`
                
                .. attribute:: mode
                
                	ICCP mode
                	**type**\:   :py:class:`IccpModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_cfg.IccpModeEnum>`
                
                .. attribute:: nv_satellite
                
                	nV Satellite configuration
                	**type**\:   :py:class:`NvSatellite <ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_cfg.RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.NvSatellite>`
                
                

                """

                _prefix = 'rgmgr-cfg'
                _revision = '2015-07-30'

                def __init__(self):
                    self.parent = None
                    self.group_number = None
                    self.backbones = RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Backbones()
                    self.backbones.parent = self
                    self.isolation_recovery_delay = None
                    self.members = RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Members()
                    self.members.parent = self
                    self.mlacp = RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Mlacp()
                    self.mlacp.parent = self
                    self.mode = None
                    self.nv_satellite = RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.NvSatellite()
                    self.nv_satellite.parent = self


                class Backbones(object):
                    """
                    ICCP backbone configuration
                    
                    .. attribute:: backbone
                    
                    	ICCP backbone interface configuration
                    	**type**\: list of    :py:class:`Backbone <ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_cfg.RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Backbones.Backbone>`
                    
                    

                    """

                    _prefix = 'rgmgr-cfg'
                    _revision = '2015-07-30'

                    def __init__(self):
                        self.parent = None
                        self.backbone = YList()
                        self.backbone.parent = self
                        self.backbone.name = 'backbone'


                    class Backbone(object):
                        """
                        ICCP backbone interface configuration
                        
                        .. attribute:: backbone_name  <key>
                        
                        	none
                        	**type**\:  str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        

                        """

                        _prefix = 'rgmgr-cfg'
                        _revision = '2015-07-30'

                        def __init__(self):
                            self.parent = None
                            self.backbone_name = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.backbone_name is None:
                                raise YPYModelError('Key property backbone_name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-rgmgr-cfg:backbone[Cisco-IOS-XR-rgmgr-cfg:backbone-name = ' + str(self.backbone_name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.backbone_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_rgmgr_cfg as meta
                            return meta._meta_table['RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Backbones.Backbone']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-rgmgr-cfg:backbones'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.backbone is not None:
                            for child_ref in self.backbone:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_rgmgr_cfg as meta
                        return meta._meta_table['RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Backbones']['meta_info']


                class Members(object):
                    """
                    ICCP member configuration
                    
                    .. attribute:: member
                    
                    	ICCP member configuration
                    	**type**\: list of    :py:class:`Member <ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_cfg.RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Members.Member>`
                    
                    

                    """

                    _prefix = 'rgmgr-cfg'
                    _revision = '2015-07-30'

                    def __init__(self):
                        self.parent = None
                        self.member = YList()
                        self.member.parent = self
                        self.member.name = 'member'


                    class Member(object):
                        """
                        ICCP member configuration
                        
                        .. attribute:: neighbor_address  <key>
                        
                        	Neighbor IP address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'rgmgr-cfg'
                        _revision = '2015-07-30'

                        def __init__(self):
                            self.parent = None
                            self.neighbor_address = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.neighbor_address is None:
                                raise YPYModelError('Key property neighbor_address is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-rgmgr-cfg:member[Cisco-IOS-XR-rgmgr-cfg:neighbor-address = ' + str(self.neighbor_address) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.neighbor_address is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_rgmgr_cfg as meta
                            return meta._meta_table['RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Members.Member']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-rgmgr-cfg:members'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.member is not None:
                            for child_ref in self.member:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_rgmgr_cfg as meta
                        return meta._meta_table['RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Members']['meta_info']


                class Mlacp(object):
                    """
                    Multi\-chassis Link Aggregation Control Protocol
                    commands
                    
                    .. attribute:: connect_timeout
                    
                    	Number of seconds to wait before assuming mLACP peer is down
                    	**type**\:  int
                    
                    	**range:** 0..65534
                    
                    .. attribute:: node
                    
                    	Unique identifier for this system in the ICCP Group
                    	**type**\:  int
                    
                    	**range:** 0..7
                    
                    .. attribute:: system_mac
                    
                    	Unique LACP identifier for this system
                    	**type**\:  str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: system_priority
                    
                    	Priority for this system. Lower value is higher priority
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    

                    """

                    _prefix = 'bundlemgr-cfg'
                    _revision = '2016-12-16'

                    def __init__(self):
                        self.parent = None
                        self.connect_timeout = None
                        self.node = None
                        self.system_mac = None
                        self.system_priority = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-bundlemgr-cfg:mlacp'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.connect_timeout is not None:
                            return True

                        if self.node is not None:
                            return True

                        if self.system_mac is not None:
                            return True

                        if self.system_priority is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_rgmgr_cfg as meta
                        return meta._meta_table['RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Mlacp']['meta_info']


                class NvSatellite(object):
                    """
                    nV Satellite configuration
                    
                    .. attribute:: system_mac
                    
                    	Optional identifier for this system
                    	**type**\:  str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    

                    """

                    _prefix = 'icpe-infra-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.system_mac = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-icpe-infra-cfg:nv-satellite'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.system_mac is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_rgmgr_cfg as meta
                        return meta._meta_table['RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.NvSatellite']['meta_info']

                @property
                def _common_path(self):
                    if self.group_number is None:
                        raise YPYModelError('Key property group_number is None')

                    return '/Cisco-IOS-XR-rgmgr-cfg:redundancy-group-manager/Cisco-IOS-XR-rgmgr-cfg:iccp/Cisco-IOS-XR-rgmgr-cfg:iccp-groups/Cisco-IOS-XR-rgmgr-cfg:iccp-group[Cisco-IOS-XR-rgmgr-cfg:group-number = ' + str(self.group_number) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.group_number is not None:
                        return True

                    if self.backbones is not None and self.backbones._has_data():
                        return True

                    if self.isolation_recovery_delay is not None:
                        return True

                    if self.members is not None and self.members._has_data():
                        return True

                    if self.mlacp is not None and self.mlacp._has_data():
                        return True

                    if self.mode is not None:
                        return True

                    if self.nv_satellite is not None and self.nv_satellite._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_rgmgr_cfg as meta
                    return meta._meta_table['RedundancyGroupManager.Iccp.IccpGroups.IccpGroup']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-rgmgr-cfg:redundancy-group-manager/Cisco-IOS-XR-rgmgr-cfg:iccp/Cisco-IOS-XR-rgmgr-cfg:iccp-groups'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.iccp_group is not None:
                    for child_ref in self.iccp_group:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_rgmgr_cfg as meta
                return meta._meta_table['RedundancyGroupManager.Iccp.IccpGroups']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-rgmgr-cfg:redundancy-group-manager/Cisco-IOS-XR-rgmgr-cfg:iccp'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.iccp_groups is not None and self.iccp_groups._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_rgmgr_cfg as meta
            return meta._meta_table['RedundancyGroupManager.Iccp']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-rgmgr-cfg:redundancy-group-manager'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.aps is not None and self.aps._has_data():
            return True

        if self.enable is not None:
            return True

        if self.iccp is not None and self.iccp._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_rgmgr_cfg as meta
        return meta._meta_table['RedundancyGroupManager']['meta_info']


