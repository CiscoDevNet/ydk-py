""" Cisco_IOS_XR_rgmgr_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR rgmgr package operational data.

This module contains definitions
for the following management objects\:
  redundancy\-group\-manager\: Redundancy group manager operational
    data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class RedundancyGroupManager(Entity):
    """
    Redundancy group manager operational data
    
    .. attribute:: controllers
    
    	Redundancy group manager data
    	**type**\:   :py:class:`Controllers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_oper.RedundancyGroupManager.Controllers>`
    
    

    """

    _prefix = 'rgmgr-oper'
    _revision = '2015-01-07'

    def __init__(self):
        super(RedundancyGroupManager, self).__init__()
        self._top_entity = None

        self.yang_name = "redundancy-group-manager"
        self.yang_parent_name = "Cisco-IOS-XR-rgmgr-oper"

        self.controllers = RedundancyGroupManager.Controllers()
        self.controllers.parent = self
        self._children_name_map["controllers"] = "controllers"
        self._children_yang_names.add("controllers")


    class Controllers(Entity):
        """
        Redundancy group manager data
        
        .. attribute:: controller
        
        	Display redundancy group by controller name
        	**type**\: list of    :py:class:`Controller <ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_oper.RedundancyGroupManager.Controllers.Controller>`
        
        

        """

        _prefix = 'rgmgr-oper'
        _revision = '2015-01-07'

        def __init__(self):
            super(RedundancyGroupManager.Controllers, self).__init__()

            self.yang_name = "controllers"
            self.yang_parent_name = "redundancy-group-manager"

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
                        super(RedundancyGroupManager.Controllers, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(RedundancyGroupManager.Controllers, self).__setattr__(name, value)


        class Controller(Entity):
            """
            Display redundancy group by controller name
            
            .. attribute:: controller_name  <key>
            
            	Controller name
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: backup_interface_handle
            
            	Backup interface handle
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: backup_interface_name
            
            	Backup interface name
            	**type**\:  str
            
            	**length:** 0..64
            
            .. attribute:: backup_interface_next_hop_ip_address
            
            	Backup interface next hop IP address
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: controller_handle
            
            	Handle of controller being backed up
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: controller_name_xr
            
            	Name of controller being backed up
            	**type**\:  str
            
            	**length:** 0..64
            
            .. attribute:: inter_chassis_group_state
            
            	Configured interchassis redundancy group state
            	**type**\:  str
            
            	**length:** 0..64
            
            .. attribute:: multi_router_aps_group_number
            
            	Configured interchassis redundancy group number
            	**type**\:  str
            
            	**length:** 0..64
            
            

            """

            _prefix = 'rgmgr-oper'
            _revision = '2015-01-07'

            def __init__(self):
                super(RedundancyGroupManager.Controllers.Controller, self).__init__()

                self.yang_name = "controller"
                self.yang_parent_name = "controllers"

                self.controller_name = YLeaf(YType.str, "controller-name")

                self.backup_interface_handle = YLeaf(YType.str, "backup-interface-handle")

                self.backup_interface_name = YLeaf(YType.str, "backup-interface-name")

                self.backup_interface_next_hop_ip_address = YLeaf(YType.str, "backup-interface-next-hop-ip-address")

                self.controller_handle = YLeaf(YType.str, "controller-handle")

                self.controller_name_xr = YLeaf(YType.str, "controller-name-xr")

                self.inter_chassis_group_state = YLeaf(YType.str, "inter-chassis-group-state")

                self.multi_router_aps_group_number = YLeaf(YType.str, "multi-router-aps-group-number")

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
                                "backup_interface_handle",
                                "backup_interface_name",
                                "backup_interface_next_hop_ip_address",
                                "controller_handle",
                                "controller_name_xr",
                                "inter_chassis_group_state",
                                "multi_router_aps_group_number") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(RedundancyGroupManager.Controllers.Controller, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(RedundancyGroupManager.Controllers.Controller, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.controller_name.is_set or
                    self.backup_interface_handle.is_set or
                    self.backup_interface_name.is_set or
                    self.backup_interface_next_hop_ip_address.is_set or
                    self.controller_handle.is_set or
                    self.controller_name_xr.is_set or
                    self.inter_chassis_group_state.is_set or
                    self.multi_router_aps_group_number.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.controller_name.yfilter != YFilter.not_set or
                    self.backup_interface_handle.yfilter != YFilter.not_set or
                    self.backup_interface_name.yfilter != YFilter.not_set or
                    self.backup_interface_next_hop_ip_address.yfilter != YFilter.not_set or
                    self.controller_handle.yfilter != YFilter.not_set or
                    self.controller_name_xr.yfilter != YFilter.not_set or
                    self.inter_chassis_group_state.yfilter != YFilter.not_set or
                    self.multi_router_aps_group_number.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "controller" + "[controller-name='" + self.controller_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-rgmgr-oper:redundancy-group-manager/controllers/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.controller_name.is_set or self.controller_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.controller_name.get_name_leafdata())
                if (self.backup_interface_handle.is_set or self.backup_interface_handle.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.backup_interface_handle.get_name_leafdata())
                if (self.backup_interface_name.is_set or self.backup_interface_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.backup_interface_name.get_name_leafdata())
                if (self.backup_interface_next_hop_ip_address.is_set or self.backup_interface_next_hop_ip_address.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.backup_interface_next_hop_ip_address.get_name_leafdata())
                if (self.controller_handle.is_set or self.controller_handle.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.controller_handle.get_name_leafdata())
                if (self.controller_name_xr.is_set or self.controller_name_xr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.controller_name_xr.get_name_leafdata())
                if (self.inter_chassis_group_state.is_set or self.inter_chassis_group_state.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.inter_chassis_group_state.get_name_leafdata())
                if (self.multi_router_aps_group_number.is_set or self.multi_router_aps_group_number.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.multi_router_aps_group_number.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "controller-name" or name == "backup-interface-handle" or name == "backup-interface-name" or name == "backup-interface-next-hop-ip-address" or name == "controller-handle" or name == "controller-name-xr" or name == "inter-chassis-group-state" or name == "multi-router-aps-group-number"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "controller-name"):
                    self.controller_name = value
                    self.controller_name.value_namespace = name_space
                    self.controller_name.value_namespace_prefix = name_space_prefix
                if(value_path == "backup-interface-handle"):
                    self.backup_interface_handle = value
                    self.backup_interface_handle.value_namespace = name_space
                    self.backup_interface_handle.value_namespace_prefix = name_space_prefix
                if(value_path == "backup-interface-name"):
                    self.backup_interface_name = value
                    self.backup_interface_name.value_namespace = name_space
                    self.backup_interface_name.value_namespace_prefix = name_space_prefix
                if(value_path == "backup-interface-next-hop-ip-address"):
                    self.backup_interface_next_hop_ip_address = value
                    self.backup_interface_next_hop_ip_address.value_namespace = name_space
                    self.backup_interface_next_hop_ip_address.value_namespace_prefix = name_space_prefix
                if(value_path == "controller-handle"):
                    self.controller_handle = value
                    self.controller_handle.value_namespace = name_space
                    self.controller_handle.value_namespace_prefix = name_space_prefix
                if(value_path == "controller-name-xr"):
                    self.controller_name_xr = value
                    self.controller_name_xr.value_namespace = name_space
                    self.controller_name_xr.value_namespace_prefix = name_space_prefix
                if(value_path == "inter-chassis-group-state"):
                    self.inter_chassis_group_state = value
                    self.inter_chassis_group_state.value_namespace = name_space
                    self.inter_chassis_group_state.value_namespace_prefix = name_space_prefix
                if(value_path == "multi-router-aps-group-number"):
                    self.multi_router_aps_group_number = value
                    self.multi_router_aps_group_number.value_namespace = name_space
                    self.multi_router_aps_group_number.value_namespace_prefix = name_space_prefix

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
                path_buffer = "Cisco-IOS-XR-rgmgr-oper:redundancy-group-manager/%s" % self.get_segment_path()
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
                c = RedundancyGroupManager.Controllers.Controller()
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
        return (self.controllers is not None and self.controllers.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.controllers is not None and self.controllers.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-rgmgr-oper:redundancy-group-manager" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "controllers"):
            if (self.controllers is None):
                self.controllers = RedundancyGroupManager.Controllers()
                self.controllers.parent = self
                self._children_name_map["controllers"] = "controllers"
            return self.controllers

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "controllers"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = RedundancyGroupManager()
        return self._top_entity

