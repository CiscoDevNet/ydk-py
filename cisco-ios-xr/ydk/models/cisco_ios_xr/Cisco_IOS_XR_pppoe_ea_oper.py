""" Cisco_IOS_XR_pppoe_ea_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR pppoe\-ea package operational data.

This module contains definitions
for the following management objects\:
  pppoe\-ea\: PPPoE Ea data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class PppoeEa(Entity):
    """
    PPPoE Ea data
    
    .. attribute:: nodes
    
    	PPPOE\_EA list of nodes
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper.PppoeEa.Nodes>`
    
    

    """

    _prefix = 'pppoe-ea-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(PppoeEa, self).__init__()
        self._top_entity = None

        self.yang_name = "pppoe-ea"
        self.yang_parent_name = "Cisco-IOS-XR-pppoe-ea-oper"

        self.nodes = PppoeEa.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")


    class Nodes(Entity):
        """
        PPPOE\_EA list of nodes
        
        .. attribute:: node
        
        	PPPOE\-EA operational data for a particular node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper.PppoeEa.Nodes.Node>`
        
        

        """

        _prefix = 'pppoe-ea-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(PppoeEa.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "pppoe-ea"

            self.node = YList(self)

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
                        super(PppoeEa.Nodes, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(PppoeEa.Nodes, self).__setattr__(name, value)


        class Node(Entity):
            """
            PPPOE\-EA operational data for a particular node
            
            .. attribute:: node_name  <key>
            
            	Node name
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: interface_ids
            
            	PPPoE interface info
            	**type**\:   :py:class:`InterfaceIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper.PppoeEa.Nodes.Node.InterfaceIds>`
            
            .. attribute:: parent_interface_ids
            
            	PPPoE parent interface info
            	**type**\:   :py:class:`ParentInterfaceIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper.PppoeEa.Nodes.Node.ParentInterfaceIds>`
            
            

            """

            _prefix = 'pppoe-ea-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(PppoeEa.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"

                self.node_name = YLeaf(YType.str, "node-name")

                self.interface_ids = PppoeEa.Nodes.Node.InterfaceIds()
                self.interface_ids.parent = self
                self._children_name_map["interface_ids"] = "interface-ids"
                self._children_yang_names.add("interface-ids")

                self.parent_interface_ids = PppoeEa.Nodes.Node.ParentInterfaceIds()
                self.parent_interface_ids.parent = self
                self._children_name_map["parent_interface_ids"] = "parent-interface-ids"
                self._children_yang_names.add("parent-interface-ids")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("node_name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(PppoeEa.Nodes.Node, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(PppoeEa.Nodes.Node, self).__setattr__(name, value)


            class ParentInterfaceIds(Entity):
                """
                PPPoE parent interface info
                
                .. attribute:: parent_interface_id
                
                	PPPoE parent interface info
                	**type**\: list of    :py:class:`ParentInterfaceId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper.PppoeEa.Nodes.Node.ParentInterfaceIds.ParentInterfaceId>`
                
                

                """

                _prefix = 'pppoe-ea-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(PppoeEa.Nodes.Node.ParentInterfaceIds, self).__init__()

                    self.yang_name = "parent-interface-ids"
                    self.yang_parent_name = "node"

                    self.parent_interface_id = YList(self)

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
                                super(PppoeEa.Nodes.Node.ParentInterfaceIds, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(PppoeEa.Nodes.Node.ParentInterfaceIds, self).__setattr__(name, value)


                class ParentInterfaceId(Entity):
                    """
                    PPPoE parent interface info
                    
                    .. attribute:: parent_interface_name  <key>
                    
                    	Interface Name
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: interface
                    
                    	Interface
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: is_in_sync
                    
                    	Is in sync
                    	**type**\:  bool
                    
                    .. attribute:: srgv_mac
                    
                    	SRG VMac\-address
                    	**type**\:   :py:class:`SrgvMac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper.PppoeEa.Nodes.Node.ParentInterfaceIds.ParentInterfaceId.SrgvMac>`
                    
                    

                    """

                    _prefix = 'pppoe-ea-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(PppoeEa.Nodes.Node.ParentInterfaceIds.ParentInterfaceId, self).__init__()

                        self.yang_name = "parent-interface-id"
                        self.yang_parent_name = "parent-interface-ids"

                        self.parent_interface_name = YLeaf(YType.str, "parent-interface-name")

                        self.interface = YLeaf(YType.str, "interface")

                        self.is_in_sync = YLeaf(YType.boolean, "is-in-sync")

                        self.srgv_mac = PppoeEa.Nodes.Node.ParentInterfaceIds.ParentInterfaceId.SrgvMac()
                        self.srgv_mac.parent = self
                        self._children_name_map["srgv_mac"] = "srgv-mac"
                        self._children_yang_names.add("srgv-mac")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("parent_interface_name",
                                        "interface",
                                        "is_in_sync") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PppoeEa.Nodes.Node.ParentInterfaceIds.ParentInterfaceId, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PppoeEa.Nodes.Node.ParentInterfaceIds.ParentInterfaceId, self).__setattr__(name, value)


                    class SrgvMac(Entity):
                        """
                        SRG VMac\-address
                        
                        .. attribute:: macaddr
                        
                        	macaddr
                        	**type**\:  str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                        
                        

                        """

                        _prefix = 'pppoe-ea-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(PppoeEa.Nodes.Node.ParentInterfaceIds.ParentInterfaceId.SrgvMac, self).__init__()

                            self.yang_name = "srgv-mac"
                            self.yang_parent_name = "parent-interface-id"

                            self.macaddr = YLeaf(YType.str, "macaddr")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("macaddr") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(PppoeEa.Nodes.Node.ParentInterfaceIds.ParentInterfaceId.SrgvMac, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(PppoeEa.Nodes.Node.ParentInterfaceIds.ParentInterfaceId.SrgvMac, self).__setattr__(name, value)

                        def has_data(self):
                            return self.macaddr.is_set

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.macaddr.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "srgv-mac" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.macaddr.is_set or self.macaddr.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.macaddr.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "macaddr"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "macaddr"):
                                self.macaddr = value
                                self.macaddr.value_namespace = name_space
                                self.macaddr.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.parent_interface_name.is_set or
                            self.interface.is_set or
                            self.is_in_sync.is_set or
                            (self.srgv_mac is not None and self.srgv_mac.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.parent_interface_name.yfilter != YFilter.not_set or
                            self.interface.yfilter != YFilter.not_set or
                            self.is_in_sync.yfilter != YFilter.not_set or
                            (self.srgv_mac is not None and self.srgv_mac.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "parent-interface-id" + "[parent-interface-name='" + self.parent_interface_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.parent_interface_name.is_set or self.parent_interface_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.parent_interface_name.get_name_leafdata())
                        if (self.interface.is_set or self.interface.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface.get_name_leafdata())
                        if (self.is_in_sync.is_set or self.is_in_sync.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.is_in_sync.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "srgv-mac"):
                            if (self.srgv_mac is None):
                                self.srgv_mac = PppoeEa.Nodes.Node.ParentInterfaceIds.ParentInterfaceId.SrgvMac()
                                self.srgv_mac.parent = self
                                self._children_name_map["srgv_mac"] = "srgv-mac"
                            return self.srgv_mac

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "srgv-mac" or name == "parent-interface-name" or name == "interface" or name == "is-in-sync"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "parent-interface-name"):
                            self.parent_interface_name = value
                            self.parent_interface_name.value_namespace = name_space
                            self.parent_interface_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface"):
                            self.interface = value
                            self.interface.value_namespace = name_space
                            self.interface.value_namespace_prefix = name_space_prefix
                        if(value_path == "is-in-sync"):
                            self.is_in_sync = value
                            self.is_in_sync.value_namespace = name_space
                            self.is_in_sync.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.parent_interface_id:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.parent_interface_id:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "parent-interface-ids" + path_buffer

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

                    if (child_yang_name == "parent-interface-id"):
                        for c in self.parent_interface_id:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = PppoeEa.Nodes.Node.ParentInterfaceIds.ParentInterfaceId()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.parent_interface_id.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "parent-interface-id"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class InterfaceIds(Entity):
                """
                PPPoE interface info
                
                .. attribute:: interface_id
                
                	PPPoE interface info
                	**type**\: list of    :py:class:`InterfaceId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper.PppoeEa.Nodes.Node.InterfaceIds.InterfaceId>`
                
                

                """

                _prefix = 'pppoe-ea-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(PppoeEa.Nodes.Node.InterfaceIds, self).__init__()

                    self.yang_name = "interface-ids"
                    self.yang_parent_name = "node"

                    self.interface_id = YList(self)

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
                                super(PppoeEa.Nodes.Node.InterfaceIds, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(PppoeEa.Nodes.Node.InterfaceIds, self).__setattr__(name, value)


                class InterfaceId(Entity):
                    """
                    PPPoE interface info
                    
                    .. attribute:: interface_name  <key>
                    
                    	Interface Name
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: interface
                    
                    	Interface
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: is_in_sync
                    
                    	Is in sync
                    	**type**\:  bool
                    
                    .. attribute:: is_platform_created
                    
                    	Is Platform created
                    	**type**\:  bool
                    
                    .. attribute:: is_priority_set
                    
                    	Is Priority Set
                    	**type**\:  bool
                    
                    .. attribute:: local_mac
                    
                    	Local Mac\-address
                    	**type**\:   :py:class:`LocalMac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper.PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.LocalMac>`
                    
                    .. attribute:: parent_interface
                    
                    	Parent Interface
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: peer_mac
                    
                    	Peer Mac\-address
                    	**type**\:   :py:class:`PeerMac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper.PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.PeerMac>`
                    
                    .. attribute:: priority
                    
                    	Priority
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: session_id
                    
                    	Session ID
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: srgv_mac
                    
                    	SRG VMac\-address
                    	**type**\:   :py:class:`SrgvMac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper.PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.SrgvMac>`
                    
                    .. attribute:: vlanid
                    
                    	VLAN Ids
                    	**type**\:  list of int
                    
                    	**range:** 0..65535
                    
                    

                    """

                    _prefix = 'pppoe-ea-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(PppoeEa.Nodes.Node.InterfaceIds.InterfaceId, self).__init__()

                        self.yang_name = "interface-id"
                        self.yang_parent_name = "interface-ids"

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.interface = YLeaf(YType.str, "interface")

                        self.is_in_sync = YLeaf(YType.boolean, "is-in-sync")

                        self.is_platform_created = YLeaf(YType.boolean, "is-platform-created")

                        self.is_priority_set = YLeaf(YType.boolean, "is-priority-set")

                        self.parent_interface = YLeaf(YType.str, "parent-interface")

                        self.priority = YLeaf(YType.uint8, "priority")

                        self.session_id = YLeaf(YType.uint16, "session-id")

                        self.vlanid = YLeafList(YType.uint16, "vlanid")

                        self.local_mac = PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.LocalMac()
                        self.local_mac.parent = self
                        self._children_name_map["local_mac"] = "local-mac"
                        self._children_yang_names.add("local-mac")

                        self.peer_mac = PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.PeerMac()
                        self.peer_mac.parent = self
                        self._children_name_map["peer_mac"] = "peer-mac"
                        self._children_yang_names.add("peer-mac")

                        self.srgv_mac = PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.SrgvMac()
                        self.srgv_mac.parent = self
                        self._children_name_map["srgv_mac"] = "srgv-mac"
                        self._children_yang_names.add("srgv-mac")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("interface_name",
                                        "interface",
                                        "is_in_sync",
                                        "is_platform_created",
                                        "is_priority_set",
                                        "parent_interface",
                                        "priority",
                                        "session_id",
                                        "vlanid") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PppoeEa.Nodes.Node.InterfaceIds.InterfaceId, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PppoeEa.Nodes.Node.InterfaceIds.InterfaceId, self).__setattr__(name, value)


                    class PeerMac(Entity):
                        """
                        Peer Mac\-address
                        
                        .. attribute:: macaddr
                        
                        	macaddr
                        	**type**\:  str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                        
                        

                        """

                        _prefix = 'pppoe-ea-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.PeerMac, self).__init__()

                            self.yang_name = "peer-mac"
                            self.yang_parent_name = "interface-id"

                            self.macaddr = YLeaf(YType.str, "macaddr")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("macaddr") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.PeerMac, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.PeerMac, self).__setattr__(name, value)

                        def has_data(self):
                            return self.macaddr.is_set

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.macaddr.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "peer-mac" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.macaddr.is_set or self.macaddr.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.macaddr.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "macaddr"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "macaddr"):
                                self.macaddr = value
                                self.macaddr.value_namespace = name_space
                                self.macaddr.value_namespace_prefix = name_space_prefix


                    class LocalMac(Entity):
                        """
                        Local Mac\-address
                        
                        .. attribute:: macaddr
                        
                        	macaddr
                        	**type**\:  str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                        
                        

                        """

                        _prefix = 'pppoe-ea-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.LocalMac, self).__init__()

                            self.yang_name = "local-mac"
                            self.yang_parent_name = "interface-id"

                            self.macaddr = YLeaf(YType.str, "macaddr")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("macaddr") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.LocalMac, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.LocalMac, self).__setattr__(name, value)

                        def has_data(self):
                            return self.macaddr.is_set

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.macaddr.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "local-mac" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.macaddr.is_set or self.macaddr.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.macaddr.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "macaddr"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "macaddr"):
                                self.macaddr = value
                                self.macaddr.value_namespace = name_space
                                self.macaddr.value_namespace_prefix = name_space_prefix


                    class SrgvMac(Entity):
                        """
                        SRG VMac\-address
                        
                        .. attribute:: macaddr
                        
                        	macaddr
                        	**type**\:  str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                        
                        

                        """

                        _prefix = 'pppoe-ea-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.SrgvMac, self).__init__()

                            self.yang_name = "srgv-mac"
                            self.yang_parent_name = "interface-id"

                            self.macaddr = YLeaf(YType.str, "macaddr")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("macaddr") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.SrgvMac, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.SrgvMac, self).__setattr__(name, value)

                        def has_data(self):
                            return self.macaddr.is_set

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.macaddr.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "srgv-mac" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.macaddr.is_set or self.macaddr.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.macaddr.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "macaddr"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "macaddr"):
                                self.macaddr = value
                                self.macaddr.value_namespace = name_space
                                self.macaddr.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for leaf in self.vlanid.getYLeafs():
                            if (leaf.yfilter != YFilter.not_set):
                                return True
                        return (
                            self.interface_name.is_set or
                            self.interface.is_set or
                            self.is_in_sync.is_set or
                            self.is_platform_created.is_set or
                            self.is_priority_set.is_set or
                            self.parent_interface.is_set or
                            self.priority.is_set or
                            self.session_id.is_set or
                            (self.local_mac is not None and self.local_mac.has_data()) or
                            (self.peer_mac is not None and self.peer_mac.has_data()) or
                            (self.srgv_mac is not None and self.srgv_mac.has_data()))

                    def has_operation(self):
                        for leaf in self.vlanid.getYLeafs():
                            if (leaf.is_set):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.interface_name.yfilter != YFilter.not_set or
                            self.interface.yfilter != YFilter.not_set or
                            self.is_in_sync.yfilter != YFilter.not_set or
                            self.is_platform_created.yfilter != YFilter.not_set or
                            self.is_priority_set.yfilter != YFilter.not_set or
                            self.parent_interface.yfilter != YFilter.not_set or
                            self.priority.yfilter != YFilter.not_set or
                            self.session_id.yfilter != YFilter.not_set or
                            self.vlanid.yfilter != YFilter.not_set or
                            (self.local_mac is not None and self.local_mac.has_operation()) or
                            (self.peer_mac is not None and self.peer_mac.has_operation()) or
                            (self.srgv_mac is not None and self.srgv_mac.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "interface-id" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_name.get_name_leafdata())
                        if (self.interface.is_set or self.interface.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface.get_name_leafdata())
                        if (self.is_in_sync.is_set or self.is_in_sync.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.is_in_sync.get_name_leafdata())
                        if (self.is_platform_created.is_set or self.is_platform_created.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.is_platform_created.get_name_leafdata())
                        if (self.is_priority_set.is_set or self.is_priority_set.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.is_priority_set.get_name_leafdata())
                        if (self.parent_interface.is_set or self.parent_interface.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.parent_interface.get_name_leafdata())
                        if (self.priority.is_set or self.priority.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.priority.get_name_leafdata())
                        if (self.session_id.is_set or self.session_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.session_id.get_name_leafdata())

                        leaf_name_data.extend(self.vlanid.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "local-mac"):
                            if (self.local_mac is None):
                                self.local_mac = PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.LocalMac()
                                self.local_mac.parent = self
                                self._children_name_map["local_mac"] = "local-mac"
                            return self.local_mac

                        if (child_yang_name == "peer-mac"):
                            if (self.peer_mac is None):
                                self.peer_mac = PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.PeerMac()
                                self.peer_mac.parent = self
                                self._children_name_map["peer_mac"] = "peer-mac"
                            return self.peer_mac

                        if (child_yang_name == "srgv-mac"):
                            if (self.srgv_mac is None):
                                self.srgv_mac = PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.SrgvMac()
                                self.srgv_mac.parent = self
                                self._children_name_map["srgv_mac"] = "srgv-mac"
                            return self.srgv_mac

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "local-mac" or name == "peer-mac" or name == "srgv-mac" or name == "interface-name" or name == "interface" or name == "is-in-sync" or name == "is-platform-created" or name == "is-priority-set" or name == "parent-interface" or name == "priority" or name == "session-id" or name == "vlanid"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "interface-name"):
                            self.interface_name = value
                            self.interface_name.value_namespace = name_space
                            self.interface_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface"):
                            self.interface = value
                            self.interface.value_namespace = name_space
                            self.interface.value_namespace_prefix = name_space_prefix
                        if(value_path == "is-in-sync"):
                            self.is_in_sync = value
                            self.is_in_sync.value_namespace = name_space
                            self.is_in_sync.value_namespace_prefix = name_space_prefix
                        if(value_path == "is-platform-created"):
                            self.is_platform_created = value
                            self.is_platform_created.value_namespace = name_space
                            self.is_platform_created.value_namespace_prefix = name_space_prefix
                        if(value_path == "is-priority-set"):
                            self.is_priority_set = value
                            self.is_priority_set.value_namespace = name_space
                            self.is_priority_set.value_namespace_prefix = name_space_prefix
                        if(value_path == "parent-interface"):
                            self.parent_interface = value
                            self.parent_interface.value_namespace = name_space
                            self.parent_interface.value_namespace_prefix = name_space_prefix
                        if(value_path == "priority"):
                            self.priority = value
                            self.priority.value_namespace = name_space
                            self.priority.value_namespace_prefix = name_space_prefix
                        if(value_path == "session-id"):
                            self.session_id = value
                            self.session_id.value_namespace = name_space
                            self.session_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "vlanid"):
                            self.vlanid.append(value)

                def has_data(self):
                    for c in self.interface_id:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.interface_id:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "interface-ids" + path_buffer

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

                    if (child_yang_name == "interface-id"):
                        for c in self.interface_id:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = PppoeEa.Nodes.Node.InterfaceIds.InterfaceId()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.interface_id.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "interface-id"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.node_name.is_set or
                    (self.interface_ids is not None and self.interface_ids.has_data()) or
                    (self.parent_interface_ids is not None and self.parent_interface_ids.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.node_name.yfilter != YFilter.not_set or
                    (self.interface_ids is not None and self.interface_ids.has_operation()) or
                    (self.parent_interface_ids is not None and self.parent_interface_ids.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "node" + "[node-name='" + self.node_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-pppoe-ea-oper:pppoe-ea/nodes/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.node_name.is_set or self.node_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.node_name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "interface-ids"):
                    if (self.interface_ids is None):
                        self.interface_ids = PppoeEa.Nodes.Node.InterfaceIds()
                        self.interface_ids.parent = self
                        self._children_name_map["interface_ids"] = "interface-ids"
                    return self.interface_ids

                if (child_yang_name == "parent-interface-ids"):
                    if (self.parent_interface_ids is None):
                        self.parent_interface_ids = PppoeEa.Nodes.Node.ParentInterfaceIds()
                        self.parent_interface_ids.parent = self
                        self._children_name_map["parent_interface_ids"] = "parent-interface-ids"
                    return self.parent_interface_ids

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "interface-ids" or name == "parent-interface-ids" or name == "node-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "node-name"):
                    self.node_name = value
                    self.node_name.value_namespace = name_space
                    self.node_name.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.node:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.node:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "nodes" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-pppoe-ea-oper:pppoe-ea/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "node"):
                for c in self.node:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = PppoeEa.Nodes.Node()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.node.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "node"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (self.nodes is not None and self.nodes.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.nodes is not None and self.nodes.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-pppoe-ea-oper:pppoe-ea" + path_buffer

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

        if (child_yang_name == "nodes"):
            if (self.nodes is None):
                self.nodes = PppoeEa.Nodes()
                self.nodes.parent = self
                self._children_name_map["nodes"] = "nodes"
            return self.nodes

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "nodes"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = PppoeEa()
        return self._top_entity

