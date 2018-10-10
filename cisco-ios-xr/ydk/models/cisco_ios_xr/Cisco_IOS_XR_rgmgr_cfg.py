""" Cisco_IOS_XR_rgmgr_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR rgmgr package configuration.

This module contains definitions
for the following management objects\:
  redundancy\-group\-manager\: Redundancy Group Manager
    Configuration

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class IccpMode(Enum):
    """
    IccpMode (Enum Class)

    Iccp mode

    .. data:: singleton = 1

    	Run the ICCP group in Singleton mode

    """

    singleton = Enum.YLeaf(1, "singleton")



class RedundancyGroupManager(Entity):
    """
    Redundancy Group Manager Configuration
    
    .. attribute:: aps
    
    	MR\-APS groups
    	**type**\:  :py:class:`Aps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_cfg.RedundancyGroupManager.Aps>`
    
    .. attribute:: iccp
    
    	ICCP configuration
    	**type**\:  :py:class:`Iccp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_cfg.RedundancyGroupManager.Iccp>`
    
    .. attribute:: enable
    
    	Enable redundancy group manager
    	**type**\: :py:class:`Empty<ydk.types.Empty>`
    
    

    """

    _prefix = 'rgmgr-cfg'
    _revision = '2017-08-01'

    def __init__(self):
        super(RedundancyGroupManager, self).__init__()
        self._top_entity = None

        self.yang_name = "redundancy-group-manager"
        self.yang_parent_name = "Cisco-IOS-XR-rgmgr-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("aps", ("aps", RedundancyGroupManager.Aps)), ("iccp", ("iccp", RedundancyGroupManager.Iccp))])
        self._leafs = OrderedDict([
            ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
        ])
        self.enable = None

        self.aps = RedundancyGroupManager.Aps()
        self.aps.parent = self
        self._children_name_map["aps"] = "aps"

        self.iccp = RedundancyGroupManager.Iccp()
        self.iccp.parent = self
        self._children_name_map["iccp"] = "iccp"
        self._segment_path = lambda: "Cisco-IOS-XR-rgmgr-cfg:redundancy-group-manager"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(RedundancyGroupManager, [u'enable'], name, value)


    class Aps(Entity):
        """
        MR\-APS groups
        
        .. attribute:: default_redundancy_group
        
        	Default SONET controller backup configuration
        	**type**\:  :py:class:`DefaultRedundancyGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_cfg.RedundancyGroupManager.Aps.DefaultRedundancyGroup>`
        
        .. attribute:: groups
        
        	Redundancy Group Table
        	**type**\:  :py:class:`Groups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_cfg.RedundancyGroupManager.Aps.Groups>`
        
        

        """

        _prefix = 'rgmgr-cfg'
        _revision = '2017-08-01'

        def __init__(self):
            super(RedundancyGroupManager.Aps, self).__init__()

            self.yang_name = "aps"
            self.yang_parent_name = "redundancy-group-manager"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("default-redundancy-group", ("default_redundancy_group", RedundancyGroupManager.Aps.DefaultRedundancyGroup)), ("groups", ("groups", RedundancyGroupManager.Aps.Groups))])
            self._leafs = OrderedDict()

            self.default_redundancy_group = RedundancyGroupManager.Aps.DefaultRedundancyGroup()
            self.default_redundancy_group.parent = self
            self._children_name_map["default_redundancy_group"] = "default-redundancy-group"

            self.groups = RedundancyGroupManager.Aps.Groups()
            self.groups.parent = self
            self._children_name_map["groups"] = "groups"
            self._segment_path = lambda: "aps"
            self._absolute_path = lambda: "Cisco-IOS-XR-rgmgr-cfg:redundancy-group-manager/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(RedundancyGroupManager.Aps, [], name, value)


        class DefaultRedundancyGroup(Entity):
            """
            Default SONET controller backup configuration
            
            .. attribute:: next_hop_address
            
            	IPv4 address of remote peer
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: backup_interface_name
            
            	Backup interface name
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
            
            

            """

            _prefix = 'rgmgr-cfg'
            _revision = '2017-08-01'

            def __init__(self):
                super(RedundancyGroupManager.Aps.DefaultRedundancyGroup, self).__init__()

                self.yang_name = "default-redundancy-group"
                self.yang_parent_name = "aps"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('next_hop_address', (YLeaf(YType.str, 'next-hop-address'), ['str'])),
                    ('backup_interface_name', (YLeaf(YType.str, 'backup-interface-name'), ['str'])),
                ])
                self.next_hop_address = None
                self.backup_interface_name = None
                self._segment_path = lambda: "default-redundancy-group"
                self._absolute_path = lambda: "Cisco-IOS-XR-rgmgr-cfg:redundancy-group-manager/aps/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(RedundancyGroupManager.Aps.DefaultRedundancyGroup, [u'next_hop_address', u'backup_interface_name'], name, value)


        class Groups(Entity):
            """
            Redundancy Group Table
            
            .. attribute:: group
            
            	Redundancy Group Configuration
            	**type**\: list of  		 :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_cfg.RedundancyGroupManager.Aps.Groups.Group>`
            
            

            """

            _prefix = 'rgmgr-cfg'
            _revision = '2017-08-01'

            def __init__(self):
                super(RedundancyGroupManager.Aps.Groups, self).__init__()

                self.yang_name = "groups"
                self.yang_parent_name = "aps"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("group", ("group", RedundancyGroupManager.Aps.Groups.Group))])
                self._leafs = OrderedDict()

                self.group = YList(self)
                self._segment_path = lambda: "groups"
                self._absolute_path = lambda: "Cisco-IOS-XR-rgmgr-cfg:redundancy-group-manager/aps/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(RedundancyGroupManager.Aps.Groups, [], name, value)


            class Group(Entity):
                """
                Redundancy Group Configuration
                
                .. attribute:: group_id  (key)
                
                	The redundancy group ID
                	**type**\: int
                
                	**range:** 1..32
                
                .. attribute:: controllers
                
                	Controller configuration
                	**type**\:  :py:class:`Controllers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_cfg.RedundancyGroupManager.Aps.Groups.Group.Controllers>`
                
                

                """

                _prefix = 'rgmgr-cfg'
                _revision = '2017-08-01'

                def __init__(self):
                    super(RedundancyGroupManager.Aps.Groups.Group, self).__init__()

                    self.yang_name = "group"
                    self.yang_parent_name = "groups"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['group_id']
                    self._child_classes = OrderedDict([("controllers", ("controllers", RedundancyGroupManager.Aps.Groups.Group.Controllers))])
                    self._leafs = OrderedDict([
                        ('group_id', (YLeaf(YType.uint32, 'group-id'), ['int'])),
                    ])
                    self.group_id = None

                    self.controllers = RedundancyGroupManager.Aps.Groups.Group.Controllers()
                    self.controllers.parent = self
                    self._children_name_map["controllers"] = "controllers"
                    self._segment_path = lambda: "group" + "[group-id='" + str(self.group_id) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-rgmgr-cfg:redundancy-group-manager/aps/groups/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(RedundancyGroupManager.Aps.Groups.Group, [u'group_id'], name, value)


                class Controllers(Entity):
                    """
                    Controller configuration
                    
                    .. attribute:: controller
                    
                    	none
                    	**type**\: list of  		 :py:class:`Controller <ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_cfg.RedundancyGroupManager.Aps.Groups.Group.Controllers.Controller>`
                    
                    

                    """

                    _prefix = 'rgmgr-cfg'
                    _revision = '2017-08-01'

                    def __init__(self):
                        super(RedundancyGroupManager.Aps.Groups.Group.Controllers, self).__init__()

                        self.yang_name = "controllers"
                        self.yang_parent_name = "group"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("controller", ("controller", RedundancyGroupManager.Aps.Groups.Group.Controllers.Controller))])
                        self._leafs = OrderedDict()

                        self.controller = YList(self)
                        self._segment_path = lambda: "controllers"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(RedundancyGroupManager.Aps.Groups.Group.Controllers, [], name, value)


                    class Controller(Entity):
                        """
                        none
                        
                        .. attribute:: controller_name  (key)
                        
                        	Controller Name
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        .. attribute:: next_hop_address
                        
                        	IPv4 address of remote peer
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: backup_interface_name
                        
                        	Backup interface name
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        

                        """

                        _prefix = 'rgmgr-cfg'
                        _revision = '2017-08-01'

                        def __init__(self):
                            super(RedundancyGroupManager.Aps.Groups.Group.Controllers.Controller, self).__init__()

                            self.yang_name = "controller"
                            self.yang_parent_name = "controllers"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['controller_name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('controller_name', (YLeaf(YType.str, 'controller-name'), ['str'])),
                                ('next_hop_address', (YLeaf(YType.str, 'next-hop-address'), ['str'])),
                                ('backup_interface_name', (YLeaf(YType.str, 'backup-interface-name'), ['str'])),
                            ])
                            self.controller_name = None
                            self.next_hop_address = None
                            self.backup_interface_name = None
                            self._segment_path = lambda: "controller" + "[controller-name='" + str(self.controller_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(RedundancyGroupManager.Aps.Groups.Group.Controllers.Controller, [u'controller_name', u'next_hop_address', u'backup_interface_name'], name, value)


    class Iccp(Entity):
        """
        ICCP configuration
        
        .. attribute:: iccp_groups
        
        	Redundancy Group Table Configuration
        	**type**\:  :py:class:`IccpGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_cfg.RedundancyGroupManager.Iccp.IccpGroups>`
        
        

        """

        _prefix = 'rgmgr-cfg'
        _revision = '2017-08-01'

        def __init__(self):
            super(RedundancyGroupManager.Iccp, self).__init__()

            self.yang_name = "iccp"
            self.yang_parent_name = "redundancy-group-manager"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("iccp-groups", ("iccp_groups", RedundancyGroupManager.Iccp.IccpGroups))])
            self._leafs = OrderedDict()

            self.iccp_groups = RedundancyGroupManager.Iccp.IccpGroups()
            self.iccp_groups.parent = self
            self._children_name_map["iccp_groups"] = "iccp-groups"
            self._segment_path = lambda: "iccp"
            self._absolute_path = lambda: "Cisco-IOS-XR-rgmgr-cfg:redundancy-group-manager/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(RedundancyGroupManager.Iccp, [], name, value)


        class IccpGroups(Entity):
            """
            Redundancy Group Table Configuration
            
            .. attribute:: iccp_group
            
            	Redundancy Group Configuration
            	**type**\: list of  		 :py:class:`IccpGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_cfg.RedundancyGroupManager.Iccp.IccpGroups.IccpGroup>`
            
            

            """

            _prefix = 'rgmgr-cfg'
            _revision = '2017-08-01'

            def __init__(self):
                super(RedundancyGroupManager.Iccp.IccpGroups, self).__init__()

                self.yang_name = "iccp-groups"
                self.yang_parent_name = "iccp"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("iccp-group", ("iccp_group", RedundancyGroupManager.Iccp.IccpGroups.IccpGroup))])
                self._leafs = OrderedDict()

                self.iccp_group = YList(self)
                self._segment_path = lambda: "iccp-groups"
                self._absolute_path = lambda: "Cisco-IOS-XR-rgmgr-cfg:redundancy-group-manager/iccp/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(RedundancyGroupManager.Iccp.IccpGroups, [], name, value)


            class IccpGroup(Entity):
                """
                Redundancy Group Configuration
                
                .. attribute:: group_number  (key)
                
                	The redundancy icc group number
                	**type**\: int
                
                	**range:** 1..4294967295
                
                .. attribute:: backbones
                
                	ICCP backbone configuration
                	**type**\:  :py:class:`Backbones <ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_cfg.RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Backbones>`
                
                .. attribute:: members
                
                	ICCP member configuration
                	**type**\:  :py:class:`Members <ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_cfg.RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Members>`
                
                .. attribute:: isolation_recovery_delay
                
                	ICCP isolation recovery delay
                	**type**\: int
                
                	**range:** 30..600
                
                	**units**\: second
                
                .. attribute:: mode
                
                	ICCP mode
                	**type**\:  :py:class:`IccpMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_cfg.IccpMode>`
                
                .. attribute:: mlacp
                
                	Multi\-chassis Link Aggregation Control Protocol commands
                	**type**\:  :py:class:`Mlacp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_cfg.RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Mlacp>`
                
                .. attribute:: nv_satellite
                
                	nV Satellite configuration
                	**type**\:  :py:class:`NvSatellite <ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_cfg.RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.NvSatellite>`
                
                

                """

                _prefix = 'rgmgr-cfg'
                _revision = '2017-08-01'

                def __init__(self):
                    super(RedundancyGroupManager.Iccp.IccpGroups.IccpGroup, self).__init__()

                    self.yang_name = "iccp-group"
                    self.yang_parent_name = "iccp-groups"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['group_number']
                    self._child_classes = OrderedDict([("backbones", ("backbones", RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Backbones)), ("members", ("members", RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Members)), ("Cisco-IOS-XR-bundlemgr-cfg:mlacp", ("mlacp", RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Mlacp)), ("Cisco-IOS-XR-icpe-infra-cfg:nv-satellite", ("nv_satellite", RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.NvSatellite))])
                    self._leafs = OrderedDict([
                        ('group_number', (YLeaf(YType.uint32, 'group-number'), ['int'])),
                        ('isolation_recovery_delay', (YLeaf(YType.uint32, 'isolation-recovery-delay'), ['int'])),
                        ('mode', (YLeaf(YType.enumeration, 'mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_cfg', 'IccpMode', '')])),
                    ])
                    self.group_number = None
                    self.isolation_recovery_delay = None
                    self.mode = None

                    self.backbones = RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Backbones()
                    self.backbones.parent = self
                    self._children_name_map["backbones"] = "backbones"

                    self.members = RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Members()
                    self.members.parent = self
                    self._children_name_map["members"] = "members"

                    self.mlacp = RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Mlacp()
                    self.mlacp.parent = self
                    self._children_name_map["mlacp"] = "Cisco-IOS-XR-bundlemgr-cfg:mlacp"

                    self.nv_satellite = RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.NvSatellite()
                    self.nv_satellite.parent = self
                    self._children_name_map["nv_satellite"] = "Cisco-IOS-XR-icpe-infra-cfg:nv-satellite"
                    self._segment_path = lambda: "iccp-group" + "[group-number='" + str(self.group_number) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-rgmgr-cfg:redundancy-group-manager/iccp/iccp-groups/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(RedundancyGroupManager.Iccp.IccpGroups.IccpGroup, [u'group_number', u'isolation_recovery_delay', u'mode'], name, value)


                class Backbones(Entity):
                    """
                    ICCP backbone configuration
                    
                    .. attribute:: backbone
                    
                    	ICCP backbone interface configuration
                    	**type**\: list of  		 :py:class:`Backbone <ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_cfg.RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Backbones.Backbone>`
                    
                    

                    """

                    _prefix = 'rgmgr-cfg'
                    _revision = '2017-08-01'

                    def __init__(self):
                        super(RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Backbones, self).__init__()

                        self.yang_name = "backbones"
                        self.yang_parent_name = "iccp-group"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("backbone", ("backbone", RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Backbones.Backbone))])
                        self._leafs = OrderedDict()

                        self.backbone = YList(self)
                        self._segment_path = lambda: "backbones"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Backbones, [], name, value)


                    class Backbone(Entity):
                        """
                        ICCP backbone interface configuration
                        
                        .. attribute:: backbone_name  (key)
                        
                        	none
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        

                        """

                        _prefix = 'rgmgr-cfg'
                        _revision = '2017-08-01'

                        def __init__(self):
                            super(RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Backbones.Backbone, self).__init__()

                            self.yang_name = "backbone"
                            self.yang_parent_name = "backbones"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['backbone_name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('backbone_name', (YLeaf(YType.str, 'backbone-name'), ['str'])),
                            ])
                            self.backbone_name = None
                            self._segment_path = lambda: "backbone" + "[backbone-name='" + str(self.backbone_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Backbones.Backbone, [u'backbone_name'], name, value)


                class Members(Entity):
                    """
                    ICCP member configuration
                    
                    .. attribute:: member
                    
                    	ICCP member configuration
                    	**type**\: list of  		 :py:class:`Member <ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_cfg.RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Members.Member>`
                    
                    

                    """

                    _prefix = 'rgmgr-cfg'
                    _revision = '2017-08-01'

                    def __init__(self):
                        super(RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Members, self).__init__()

                        self.yang_name = "members"
                        self.yang_parent_name = "iccp-group"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("member", ("member", RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Members.Member))])
                        self._leafs = OrderedDict()

                        self.member = YList(self)
                        self._segment_path = lambda: "members"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Members, [], name, value)


                    class Member(Entity):
                        """
                        ICCP member configuration
                        
                        .. attribute:: neighbor_address  (key)
                        
                        	Neighbor IP address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'rgmgr-cfg'
                        _revision = '2017-08-01'

                        def __init__(self):
                            super(RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Members.Member, self).__init__()

                            self.yang_name = "member"
                            self.yang_parent_name = "members"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['neighbor_address']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('neighbor_address', (YLeaf(YType.str, 'neighbor-address'), ['str'])),
                            ])
                            self.neighbor_address = None
                            self._segment_path = lambda: "member" + "[neighbor-address='" + str(self.neighbor_address) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Members.Member, [u'neighbor_address'], name, value)


                class Mlacp(Entity):
                    """
                    Multi\-chassis Link Aggregation Control Protocol
                    commands
                    
                    .. attribute:: connect_timeout
                    
                    	Number of seconds to wait before assuming mLACP peer is down
                    	**type**\: int
                    
                    	**range:** 0..65534
                    
                    .. attribute:: system_mac
                    
                    	Unique LACP identifier for this system
                    	**type**\: str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: node
                    
                    	Unique identifier for this system in the ICCP Group
                    	**type**\: int
                    
                    	**range:** 0..7
                    
                    .. attribute:: system_priority
                    
                    	Priority for this system. Lower value is higher priority
                    	**type**\: int
                    
                    	**range:** 1..65535
                    
                    

                    """

                    _prefix = 'bundlemgr-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Mlacp, self).__init__()

                        self.yang_name = "mlacp"
                        self.yang_parent_name = "iccp-group"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('connect_timeout', (YLeaf(YType.uint32, 'connect-timeout'), ['int'])),
                            ('system_mac', (YLeaf(YType.str, 'system-mac'), ['str'])),
                            ('node', (YLeaf(YType.uint32, 'node'), ['int'])),
                            ('system_priority', (YLeaf(YType.uint32, 'system-priority'), ['int'])),
                        ])
                        self.connect_timeout = None
                        self.system_mac = None
                        self.node = None
                        self.system_priority = None
                        self._segment_path = lambda: "Cisco-IOS-XR-bundlemgr-cfg:mlacp"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Mlacp, ['connect_timeout', 'system_mac', 'node', 'system_priority'], name, value)


                class NvSatellite(Entity):
                    """
                    nV Satellite configuration
                    
                    .. attribute:: system_mac
                    
                    	Optional identifier for this system
                    	**type**\: str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    

                    """

                    _prefix = 'icpe-infra-cfg'
                    _revision = '2017-09-30'

                    def __init__(self):
                        super(RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.NvSatellite, self).__init__()

                        self.yang_name = "nv-satellite"
                        self.yang_parent_name = "iccp-group"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('system_mac', (YLeaf(YType.str, 'system-mac'), ['str'])),
                        ])
                        self.system_mac = None
                        self._segment_path = lambda: "Cisco-IOS-XR-icpe-infra-cfg:nv-satellite"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.NvSatellite, [u'system_mac'], name, value)

    def clone_ptr(self):
        self._top_entity = RedundancyGroupManager()
        return self._top_entity

