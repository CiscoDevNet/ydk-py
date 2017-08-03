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
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class IccpMode(Enum):
    """
    IccpMode

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
        super(RedundancyGroupManager, self).__init__()
        self._top_entity = None

        self.yang_name = "redundancy-group-manager"
        self.yang_parent_name = "Cisco-IOS-XR-rgmgr-cfg"

        self.enable = YLeaf(YType.empty, "enable")

        self.aps = RedundancyGroupManager.Aps()
        self.aps.parent = self
        self._children_name_map["aps"] = "aps"
        self._children_yang_names.add("aps")

        self.iccp = RedundancyGroupManager.Iccp()
        self.iccp.parent = self
        self._children_name_map["iccp"] = "iccp"
        self._children_yang_names.add("iccp")

    def __setattr__(self, name, value):
        self._check_monkey_patching_error(name, value)
        with _handle_type_error():
            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                    "Please use list append or extend method."
                                    .format(value))
            if isinstance(value, Enum.YLeaf):
                value = value.name
            if name in ("enable") and name in self.__dict__:
                if isinstance(value, YLeaf):
                    self.__dict__[name].set(value.get())
                elif isinstance(value, YLeafList):
                    super(RedundancyGroupManager, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(RedundancyGroupManager, self).__setattr__(name, value)


    class Aps(Entity):
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
            super(RedundancyGroupManager.Aps, self).__init__()

            self.yang_name = "aps"
            self.yang_parent_name = "redundancy-group-manager"

            self.default_redundancy_group = RedundancyGroupManager.Aps.DefaultRedundancyGroup()
            self.default_redundancy_group.parent = self
            self._children_name_map["default_redundancy_group"] = "default-redundancy-group"
            self._children_yang_names.add("default-redundancy-group")

            self.groups = RedundancyGroupManager.Aps.Groups()
            self.groups.parent = self
            self._children_name_map["groups"] = "groups"
            self._children_yang_names.add("groups")


        class DefaultRedundancyGroup(Entity):
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
                super(RedundancyGroupManager.Aps.DefaultRedundancyGroup, self).__init__()

                self.yang_name = "default-redundancy-group"
                self.yang_parent_name = "aps"

                self.backup_interface_name = YLeaf(YType.str, "backup-interface-name")

                self.next_hop_address = YLeaf(YType.str, "next-hop-address")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("backup_interface_name",
                                "next_hop_address") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(RedundancyGroupManager.Aps.DefaultRedundancyGroup, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(RedundancyGroupManager.Aps.DefaultRedundancyGroup, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.backup_interface_name.is_set or
                    self.next_hop_address.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.backup_interface_name.yfilter != YFilter.not_set or
                    self.next_hop_address.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "default-redundancy-group" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-rgmgr-cfg:redundancy-group-manager/aps/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.backup_interface_name.is_set or self.backup_interface_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.backup_interface_name.get_name_leafdata())
                if (self.next_hop_address.is_set or self.next_hop_address.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.next_hop_address.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "backup-interface-name" or name == "next-hop-address"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "backup-interface-name"):
                    self.backup_interface_name = value
                    self.backup_interface_name.value_namespace = name_space
                    self.backup_interface_name.value_namespace_prefix = name_space_prefix
                if(value_path == "next-hop-address"):
                    self.next_hop_address = value
                    self.next_hop_address.value_namespace = name_space
                    self.next_hop_address.value_namespace_prefix = name_space_prefix


        class Groups(Entity):
            """
            Redundancy Group Table
            
            .. attribute:: group
            
            	Redundancy Group Configuration
            	**type**\: list of    :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_cfg.RedundancyGroupManager.Aps.Groups.Group>`
            
            

            """

            _prefix = 'rgmgr-cfg'
            _revision = '2015-07-30'

            def __init__(self):
                super(RedundancyGroupManager.Aps.Groups, self).__init__()

                self.yang_name = "groups"
                self.yang_parent_name = "aps"

                self.group = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in () and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(RedundancyGroupManager.Aps.Groups, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(RedundancyGroupManager.Aps.Groups, self).__setattr__(name, value)


            class Group(Entity):
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
                    super(RedundancyGroupManager.Aps.Groups.Group, self).__init__()

                    self.yang_name = "group"
                    self.yang_parent_name = "groups"

                    self.group_id = YLeaf(YType.uint32, "group-id")

                    self.controllers = RedundancyGroupManager.Aps.Groups.Group.Controllers()
                    self.controllers.parent = self
                    self._children_name_map["controllers"] = "controllers"
                    self._children_yang_names.add("controllers")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("group_id") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(RedundancyGroupManager.Aps.Groups.Group, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(RedundancyGroupManager.Aps.Groups.Group, self).__setattr__(name, value)


                class Controllers(Entity):
                    """
                    Controller configuration
                    
                    .. attribute:: controller
                    
                    	none
                    	**type**\: list of    :py:class:`Controller <ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_cfg.RedundancyGroupManager.Aps.Groups.Group.Controllers.Controller>`
                    
                    

                    """

                    _prefix = 'rgmgr-cfg'
                    _revision = '2015-07-30'

                    def __init__(self):
                        super(RedundancyGroupManager.Aps.Groups.Group.Controllers, self).__init__()

                        self.yang_name = "controllers"
                        self.yang_parent_name = "group"

                        self.controller = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in () and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(RedundancyGroupManager.Aps.Groups.Group.Controllers, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(RedundancyGroupManager.Aps.Groups.Group.Controllers, self).__setattr__(name, value)


                    class Controller(Entity):
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
                            super(RedundancyGroupManager.Aps.Groups.Group.Controllers.Controller, self).__init__()

                            self.yang_name = "controller"
                            self.yang_parent_name = "controllers"

                            self.controller_name = YLeaf(YType.str, "controller-name")

                            self.backup_interface_name = YLeaf(YType.str, "backup-interface-name")

                            self.next_hop_address = YLeaf(YType.str, "next-hop-address")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("controller_name",
                                            "backup_interface_name",
                                            "next_hop_address") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(RedundancyGroupManager.Aps.Groups.Group.Controllers.Controller, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(RedundancyGroupManager.Aps.Groups.Group.Controllers.Controller, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.controller_name.is_set or
                                self.backup_interface_name.is_set or
                                self.next_hop_address.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.controller_name.yfilter != YFilter.not_set or
                                self.backup_interface_name.yfilter != YFilter.not_set or
                                self.next_hop_address.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "controller" + "[controller-name='" + self.controller_name.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.controller_name.is_set or self.controller_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.controller_name.get_name_leafdata())
                            if (self.backup_interface_name.is_set or self.backup_interface_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.backup_interface_name.get_name_leafdata())
                            if (self.next_hop_address.is_set or self.next_hop_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.next_hop_address.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "controller-name" or name == "backup-interface-name" or name == "next-hop-address"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "controller-name"):
                                self.controller_name = value
                                self.controller_name.value_namespace = name_space
                                self.controller_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "backup-interface-name"):
                                self.backup_interface_name = value
                                self.backup_interface_name.value_namespace = name_space
                                self.backup_interface_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "next-hop-address"):
                                self.next_hop_address = value
                                self.next_hop_address.value_namespace = name_space
                                self.next_hop_address.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.controller:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.controller:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "controllers" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "controller"):
                            for c in self.controller:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = RedundancyGroupManager.Aps.Groups.Group.Controllers.Controller()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.controller.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "controller"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        self.group_id.is_set or
                        (self.controllers is not None and self.controllers.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.group_id.yfilter != YFilter.not_set or
                        (self.controllers is not None and self.controllers.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "group" + "[group-id='" + self.group_id.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-rgmgr-cfg:redundancy-group-manager/aps/groups/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.group_id.is_set or self.group_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.group_id.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "controllers"):
                        if (self.controllers is None):
                            self.controllers = RedundancyGroupManager.Aps.Groups.Group.Controllers()
                            self.controllers.parent = self
                            self._children_name_map["controllers"] = "controllers"
                        return self.controllers

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "controllers" or name == "group-id"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "group-id"):
                        self.group_id = value
                        self.group_id.value_namespace = name_space
                        self.group_id.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.group:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.group:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "groups" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-rgmgr-cfg:redundancy-group-manager/aps/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "group"):
                    for c in self.group:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = RedundancyGroupManager.Aps.Groups.Group()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.group.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "group"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (
                (self.default_redundancy_group is not None and self.default_redundancy_group.has_data()) or
                (self.groups is not None and self.groups.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.default_redundancy_group is not None and self.default_redundancy_group.has_operation()) or
                (self.groups is not None and self.groups.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "aps" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-rgmgr-cfg:redundancy-group-manager/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "default-redundancy-group"):
                if (self.default_redundancy_group is None):
                    self.default_redundancy_group = RedundancyGroupManager.Aps.DefaultRedundancyGroup()
                    self.default_redundancy_group.parent = self
                    self._children_name_map["default_redundancy_group"] = "default-redundancy-group"
                return self.default_redundancy_group

            if (child_yang_name == "groups"):
                if (self.groups is None):
                    self.groups = RedundancyGroupManager.Aps.Groups()
                    self.groups.parent = self
                    self._children_name_map["groups"] = "groups"
                return self.groups

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "default-redundancy-group" or name == "groups"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Iccp(Entity):
        """
        ICCP configuration
        
        .. attribute:: iccp_groups
        
        	Redundancy Group Table Configuration
        	**type**\:   :py:class:`IccpGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_cfg.RedundancyGroupManager.Iccp.IccpGroups>`
        
        

        """

        _prefix = 'rgmgr-cfg'
        _revision = '2015-07-30'

        def __init__(self):
            super(RedundancyGroupManager.Iccp, self).__init__()

            self.yang_name = "iccp"
            self.yang_parent_name = "redundancy-group-manager"

            self.iccp_groups = RedundancyGroupManager.Iccp.IccpGroups()
            self.iccp_groups.parent = self
            self._children_name_map["iccp_groups"] = "iccp-groups"
            self._children_yang_names.add("iccp-groups")


        class IccpGroups(Entity):
            """
            Redundancy Group Table Configuration
            
            .. attribute:: iccp_group
            
            	Redundancy Group Configuration
            	**type**\: list of    :py:class:`IccpGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_cfg.RedundancyGroupManager.Iccp.IccpGroups.IccpGroup>`
            
            

            """

            _prefix = 'rgmgr-cfg'
            _revision = '2015-07-30'

            def __init__(self):
                super(RedundancyGroupManager.Iccp.IccpGroups, self).__init__()

                self.yang_name = "iccp-groups"
                self.yang_parent_name = "iccp"

                self.iccp_group = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in () and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(RedundancyGroupManager.Iccp.IccpGroups, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(RedundancyGroupManager.Iccp.IccpGroups, self).__setattr__(name, value)


            class IccpGroup(Entity):
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
                	**type**\:   :py:class:`IccpMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_cfg.IccpMode>`
                
                .. attribute:: nv_satellite
                
                	nV Satellite configuration
                	**type**\:   :py:class:`NvSatellite <ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_cfg.RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.NvSatellite>`
                
                

                """

                _prefix = 'rgmgr-cfg'
                _revision = '2015-07-30'

                def __init__(self):
                    super(RedundancyGroupManager.Iccp.IccpGroups.IccpGroup, self).__init__()

                    self.yang_name = "iccp-group"
                    self.yang_parent_name = "iccp-groups"

                    self.group_number = YLeaf(YType.uint32, "group-number")

                    self.isolation_recovery_delay = YLeaf(YType.uint32, "isolation-recovery-delay")

                    self.mode = YLeaf(YType.enumeration, "mode")

                    self.backbones = RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Backbones()
                    self.backbones.parent = self
                    self._children_name_map["backbones"] = "backbones"
                    self._children_yang_names.add("backbones")

                    self.members = RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Members()
                    self.members.parent = self
                    self._children_name_map["members"] = "members"
                    self._children_yang_names.add("members")

                    self.mlacp = RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Mlacp()
                    self.mlacp.parent = self
                    self._children_name_map["mlacp"] = "mlacp"
                    self._children_yang_names.add("mlacp")

                    self.nv_satellite = RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.NvSatellite()
                    self.nv_satellite.parent = self
                    self._children_name_map["nv_satellite"] = "nv-satellite"
                    self._children_yang_names.add("nv-satellite")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("group_number",
                                    "isolation_recovery_delay",
                                    "mode") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(RedundancyGroupManager.Iccp.IccpGroups.IccpGroup, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(RedundancyGroupManager.Iccp.IccpGroups.IccpGroup, self).__setattr__(name, value)


                class Backbones(Entity):
                    """
                    ICCP backbone configuration
                    
                    .. attribute:: backbone
                    
                    	ICCP backbone interface configuration
                    	**type**\: list of    :py:class:`Backbone <ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_cfg.RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Backbones.Backbone>`
                    
                    

                    """

                    _prefix = 'rgmgr-cfg'
                    _revision = '2015-07-30'

                    def __init__(self):
                        super(RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Backbones, self).__init__()

                        self.yang_name = "backbones"
                        self.yang_parent_name = "iccp-group"

                        self.backbone = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in () and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Backbones, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Backbones, self).__setattr__(name, value)


                    class Backbone(Entity):
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
                            super(RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Backbones.Backbone, self).__init__()

                            self.yang_name = "backbone"
                            self.yang_parent_name = "backbones"

                            self.backbone_name = YLeaf(YType.str, "backbone-name")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("backbone_name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Backbones.Backbone, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Backbones.Backbone, self).__setattr__(name, value)

                        def has_data(self):
                            return self.backbone_name.is_set

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.backbone_name.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "backbone" + "[backbone-name='" + self.backbone_name.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.backbone_name.is_set or self.backbone_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.backbone_name.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "backbone-name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "backbone-name"):
                                self.backbone_name = value
                                self.backbone_name.value_namespace = name_space
                                self.backbone_name.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.backbone:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.backbone:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "backbones" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "backbone"):
                            for c in self.backbone:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Backbones.Backbone()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.backbone.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "backbone"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class Members(Entity):
                    """
                    ICCP member configuration
                    
                    .. attribute:: member
                    
                    	ICCP member configuration
                    	**type**\: list of    :py:class:`Member <ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_cfg.RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Members.Member>`
                    
                    

                    """

                    _prefix = 'rgmgr-cfg'
                    _revision = '2015-07-30'

                    def __init__(self):
                        super(RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Members, self).__init__()

                        self.yang_name = "members"
                        self.yang_parent_name = "iccp-group"

                        self.member = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in () and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Members, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Members, self).__setattr__(name, value)


                    class Member(Entity):
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
                            super(RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Members.Member, self).__init__()

                            self.yang_name = "member"
                            self.yang_parent_name = "members"

                            self.neighbor_address = YLeaf(YType.str, "neighbor-address")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("neighbor_address") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Members.Member, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Members.Member, self).__setattr__(name, value)

                        def has_data(self):
                            return self.neighbor_address.is_set

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.neighbor_address.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "member" + "[neighbor-address='" + self.neighbor_address.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.neighbor_address.is_set or self.neighbor_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.neighbor_address.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "neighbor-address"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "neighbor-address"):
                                self.neighbor_address = value
                                self.neighbor_address.value_namespace = name_space
                                self.neighbor_address.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.member:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.member:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "members" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "member"):
                            for c in self.member:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Members.Member()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.member.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "member"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class Mlacp(Entity):
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
                        super(RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Mlacp, self).__init__()

                        self.yang_name = "mlacp"
                        self.yang_parent_name = "iccp-group"

                        self.connect_timeout = YLeaf(YType.uint32, "connect-timeout")

                        self.node = YLeaf(YType.uint32, "node")

                        self.system_mac = YLeaf(YType.str, "system-mac")

                        self.system_priority = YLeaf(YType.uint32, "system-priority")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("connect_timeout",
                                        "node",
                                        "system_mac",
                                        "system_priority") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Mlacp, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Mlacp, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.connect_timeout.is_set or
                            self.node.is_set or
                            self.system_mac.is_set or
                            self.system_priority.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.connect_timeout.yfilter != YFilter.not_set or
                            self.node.yfilter != YFilter.not_set or
                            self.system_mac.yfilter != YFilter.not_set or
                            self.system_priority.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "Cisco-IOS-XR-bundlemgr-cfg:mlacp" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.connect_timeout.is_set or self.connect_timeout.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.connect_timeout.get_name_leafdata())
                        if (self.node.is_set or self.node.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.node.get_name_leafdata())
                        if (self.system_mac.is_set or self.system_mac.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.system_mac.get_name_leafdata())
                        if (self.system_priority.is_set or self.system_priority.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.system_priority.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "connect-timeout" or name == "node" or name == "system-mac" or name == "system-priority"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "connect-timeout"):
                            self.connect_timeout = value
                            self.connect_timeout.value_namespace = name_space
                            self.connect_timeout.value_namespace_prefix = name_space_prefix
                        if(value_path == "node"):
                            self.node = value
                            self.node.value_namespace = name_space
                            self.node.value_namespace_prefix = name_space_prefix
                        if(value_path == "system-mac"):
                            self.system_mac = value
                            self.system_mac.value_namespace = name_space
                            self.system_mac.value_namespace_prefix = name_space_prefix
                        if(value_path == "system-priority"):
                            self.system_priority = value
                            self.system_priority.value_namespace = name_space
                            self.system_priority.value_namespace_prefix = name_space_prefix


                class NvSatellite(Entity):
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
                        super(RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.NvSatellite, self).__init__()

                        self.yang_name = "nv-satellite"
                        self.yang_parent_name = "iccp-group"

                        self.system_mac = YLeaf(YType.str, "system-mac")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("system_mac") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.NvSatellite, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.NvSatellite, self).__setattr__(name, value)

                    def has_data(self):
                        return self.system_mac.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.system_mac.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "Cisco-IOS-XR-icpe-infra-cfg:nv-satellite" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.system_mac.is_set or self.system_mac.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.system_mac.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "system-mac"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "system-mac"):
                            self.system_mac = value
                            self.system_mac.value_namespace = name_space
                            self.system_mac.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.group_number.is_set or
                        self.isolation_recovery_delay.is_set or
                        self.mode.is_set or
                        (self.backbones is not None and self.backbones.has_data()) or
                        (self.members is not None and self.members.has_data()) or
                        (self.mlacp is not None and self.mlacp.has_data()) or
                        (self.nv_satellite is not None and self.nv_satellite.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.group_number.yfilter != YFilter.not_set or
                        self.isolation_recovery_delay.yfilter != YFilter.not_set or
                        self.mode.yfilter != YFilter.not_set or
                        (self.backbones is not None and self.backbones.has_operation()) or
                        (self.members is not None and self.members.has_operation()) or
                        (self.mlacp is not None and self.mlacp.has_operation()) or
                        (self.nv_satellite is not None and self.nv_satellite.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "iccp-group" + "[group-number='" + self.group_number.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-rgmgr-cfg:redundancy-group-manager/iccp/iccp-groups/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.group_number.is_set or self.group_number.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.group_number.get_name_leafdata())
                    if (self.isolation_recovery_delay.is_set or self.isolation_recovery_delay.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.isolation_recovery_delay.get_name_leafdata())
                    if (self.mode.is_set or self.mode.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.mode.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "backbones"):
                        if (self.backbones is None):
                            self.backbones = RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Backbones()
                            self.backbones.parent = self
                            self._children_name_map["backbones"] = "backbones"
                        return self.backbones

                    if (child_yang_name == "members"):
                        if (self.members is None):
                            self.members = RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Members()
                            self.members.parent = self
                            self._children_name_map["members"] = "members"
                        return self.members

                    if (child_yang_name == "mlacp"):
                        if (self.mlacp is None):
                            self.mlacp = RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Mlacp()
                            self.mlacp.parent = self
                            self._children_name_map["mlacp"] = "mlacp"
                        return self.mlacp

                    if (child_yang_name == "nv-satellite"):
                        if (self.nv_satellite is None):
                            self.nv_satellite = RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.NvSatellite()
                            self.nv_satellite.parent = self
                            self._children_name_map["nv_satellite"] = "nv-satellite"
                        return self.nv_satellite

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "backbones" or name == "members" or name == "mlacp" or name == "nv-satellite" or name == "group-number" or name == "isolation-recovery-delay" or name == "mode"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "group-number"):
                        self.group_number = value
                        self.group_number.value_namespace = name_space
                        self.group_number.value_namespace_prefix = name_space_prefix
                    if(value_path == "isolation-recovery-delay"):
                        self.isolation_recovery_delay = value
                        self.isolation_recovery_delay.value_namespace = name_space
                        self.isolation_recovery_delay.value_namespace_prefix = name_space_prefix
                    if(value_path == "mode"):
                        self.mode = value
                        self.mode.value_namespace = name_space
                        self.mode.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.iccp_group:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.iccp_group:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "iccp-groups" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-rgmgr-cfg:redundancy-group-manager/iccp/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "iccp-group"):
                    for c in self.iccp_group:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = RedundancyGroupManager.Iccp.IccpGroups.IccpGroup()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.iccp_group.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "iccp-group"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (self.iccp_groups is not None and self.iccp_groups.has_data())

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.iccp_groups is not None and self.iccp_groups.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "iccp" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-rgmgr-cfg:redundancy-group-manager/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "iccp-groups"):
                if (self.iccp_groups is None):
                    self.iccp_groups = RedundancyGroupManager.Iccp.IccpGroups()
                    self.iccp_groups.parent = self
                    self._children_name_map["iccp_groups"] = "iccp-groups"
                return self.iccp_groups

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "iccp-groups"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            self.enable.is_set or
            (self.aps is not None and self.aps.has_data()) or
            (self.iccp is not None and self.iccp.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            self.enable.yfilter != YFilter.not_set or
            (self.aps is not None and self.aps.has_operation()) or
            (self.iccp is not None and self.iccp.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-rgmgr-cfg:redundancy-group-manager" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()
        if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
            leaf_name_data.append(self.enable.get_name_leafdata())

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "aps"):
            if (self.aps is None):
                self.aps = RedundancyGroupManager.Aps()
                self.aps.parent = self
                self._children_name_map["aps"] = "aps"
            return self.aps

        if (child_yang_name == "iccp"):
            if (self.iccp is None):
                self.iccp = RedundancyGroupManager.Iccp()
                self.iccp.parent = self
                self._children_name_map["iccp"] = "iccp"
            return self.iccp

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "aps" or name == "iccp" or name == "enable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        if(value_path == "enable"):
            self.enable = value
            self.enable.value_namespace = name_space
            self.enable.value_namespace_prefix = name_space_prefix

    def clone_ptr(self):
        self._top_entity = RedundancyGroupManager()
        return self._top_entity

