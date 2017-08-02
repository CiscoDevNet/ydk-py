""" Cisco_IOS_XR_ip_pfilter_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-pfilter package operational data.

This module contains definitions
for the following management objects\:
  pfilter\-ma\: Root class of PfilterMa Oper schema

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class PfilterMa(Entity):
    """
    Root class of PfilterMa Oper schema
    
    .. attribute:: nodes
    
    	Node\-specific operational data
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_pfilter_oper.PfilterMa.Nodes>`
    
    

    """

    _prefix = 'ip-pfilter-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(PfilterMa, self).__init__()
        self._top_entity = None

        self.yang_name = "pfilter-ma"
        self.yang_parent_name = "Cisco-IOS-XR-ip-pfilter-oper"

        self.nodes = PfilterMa.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")


    class Nodes(Entity):
        """
        Node\-specific operational data
        
        .. attribute:: node
        
        	PfilterMa operational data for a particular node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_pfilter_oper.PfilterMa.Nodes.Node>`
        
        

        """

        _prefix = 'ip-pfilter-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(PfilterMa.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "pfilter-ma"

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
                        super(PfilterMa.Nodes, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(PfilterMa.Nodes, self).__setattr__(name, value)


        class Node(Entity):
            """
            PfilterMa operational data for a particular
            node
            
            .. attribute:: node_name  <key>
            
            	The node
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: process
            
            	Operational data for pfilter
            	**type**\:   :py:class:`Process <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_pfilter_oper.PfilterMa.Nodes.Node.Process>`
            
            

            """

            _prefix = 'ip-pfilter-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(PfilterMa.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"

                self.node_name = YLeaf(YType.str, "node-name")

                self.process = PfilterMa.Nodes.Node.Process()
                self.process.parent = self
                self._children_name_map["process"] = "process"
                self._children_yang_names.add("process")

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
                            super(PfilterMa.Nodes.Node, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(PfilterMa.Nodes.Node, self).__setattr__(name, value)


            class Process(Entity):
                """
                Operational data for pfilter
                
                .. attribute:: ipv4
                
                	Operational data for pfilter
                	**type**\:   :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_pfilter_oper.PfilterMa.Nodes.Node.Process.Ipv4>`
                
                .. attribute:: ipv6
                
                	Operational data for pfilter
                	**type**\:   :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_pfilter_oper.PfilterMa.Nodes.Node.Process.Ipv6>`
                
                

                """

                _prefix = 'ip-pfilter-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(PfilterMa.Nodes.Node.Process, self).__init__()

                    self.yang_name = "process"
                    self.yang_parent_name = "node"

                    self.ipv4 = PfilterMa.Nodes.Node.Process.Ipv4()
                    self.ipv4.parent = self
                    self._children_name_map["ipv4"] = "ipv4"
                    self._children_yang_names.add("ipv4")

                    self.ipv6 = PfilterMa.Nodes.Node.Process.Ipv6()
                    self.ipv6.parent = self
                    self._children_name_map["ipv6"] = "ipv6"
                    self._children_yang_names.add("ipv6")


                class Ipv6(Entity):
                    """
                    Operational data for pfilter
                    
                    .. attribute:: acl_info_table
                    
                    	Operational data for pfilter
                    	**type**\:   :py:class:`AclInfoTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_pfilter_oper.PfilterMa.Nodes.Node.Process.Ipv6.AclInfoTable>`
                    
                    

                    """

                    _prefix = 'ip-pfilter-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(PfilterMa.Nodes.Node.Process.Ipv6, self).__init__()

                        self.yang_name = "ipv6"
                        self.yang_parent_name = "process"

                        self.acl_info_table = PfilterMa.Nodes.Node.Process.Ipv6.AclInfoTable()
                        self.acl_info_table.parent = self
                        self._children_name_map["acl_info_table"] = "acl-info-table"
                        self._children_yang_names.add("acl-info-table")


                    class AclInfoTable(Entity):
                        """
                        Operational data for pfilter
                        
                        .. attribute:: interface_infos
                        
                        	Operational data for pfilter
                        	**type**\:   :py:class:`InterfaceInfos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_pfilter_oper.PfilterMa.Nodes.Node.Process.Ipv6.AclInfoTable.InterfaceInfos>`
                        
                        

                        """

                        _prefix = 'ip-pfilter-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(PfilterMa.Nodes.Node.Process.Ipv6.AclInfoTable, self).__init__()

                            self.yang_name = "acl-info-table"
                            self.yang_parent_name = "ipv6"

                            self.interface_infos = PfilterMa.Nodes.Node.Process.Ipv6.AclInfoTable.InterfaceInfos()
                            self.interface_infos.parent = self
                            self._children_name_map["interface_infos"] = "interface-infos"
                            self._children_yang_names.add("interface-infos")


                        class InterfaceInfos(Entity):
                            """
                            Operational data for pfilter
                            
                            .. attribute:: interface_info
                            
                            	Operational data for pfilter in bag
                            	**type**\: list of    :py:class:`InterfaceInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_pfilter_oper.PfilterMa.Nodes.Node.Process.Ipv6.AclInfoTable.InterfaceInfos.InterfaceInfo>`
                            
                            

                            """

                            _prefix = 'ip-pfilter-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(PfilterMa.Nodes.Node.Process.Ipv6.AclInfoTable.InterfaceInfos, self).__init__()

                                self.yang_name = "interface-infos"
                                self.yang_parent_name = "acl-info-table"

                                self.interface_info = YList(self)

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
                                            super(PfilterMa.Nodes.Node.Process.Ipv6.AclInfoTable.InterfaceInfos, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(PfilterMa.Nodes.Node.Process.Ipv6.AclInfoTable.InterfaceInfos, self).__setattr__(name, value)


                            class InterfaceInfo(Entity):
                                """
                                Operational data for pfilter in bag
                                
                                .. attribute:: interface_name  <key>
                                
                                	Name of the interface
                                	**type**\:  str
                                
                                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                
                                .. attribute:: acl_info
                                
                                	acl information
                                	**type**\:  str
                                
                                

                                """

                                _prefix = 'ip-pfilter-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PfilterMa.Nodes.Node.Process.Ipv6.AclInfoTable.InterfaceInfos.InterfaceInfo, self).__init__()

                                    self.yang_name = "interface-info"
                                    self.yang_parent_name = "interface-infos"

                                    self.interface_name = YLeaf(YType.str, "interface-name")

                                    self.acl_info = YLeaf(YType.str, "acl-info")

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
                                                    "acl_info") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(PfilterMa.Nodes.Node.Process.Ipv6.AclInfoTable.InterfaceInfos.InterfaceInfo, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(PfilterMa.Nodes.Node.Process.Ipv6.AclInfoTable.InterfaceInfos.InterfaceInfo, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.interface_name.is_set or
                                        self.acl_info.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.interface_name.yfilter != YFilter.not_set or
                                        self.acl_info.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "interface-info" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

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
                                    if (self.acl_info.is_set or self.acl_info.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.acl_info.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "interface-name" or name == "acl-info"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "interface-name"):
                                        self.interface_name = value
                                        self.interface_name.value_namespace = name_space
                                        self.interface_name.value_namespace_prefix = name_space_prefix
                                    if(value_path == "acl-info"):
                                        self.acl_info = value
                                        self.acl_info.value_namespace = name_space
                                        self.acl_info.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                for c in self.interface_info:
                                    if (c.has_data()):
                                        return True
                                return False

                            def has_operation(self):
                                for c in self.interface_info:
                                    if (c.has_operation()):
                                        return True
                                return self.yfilter != YFilter.not_set

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "interface-infos" + path_buffer

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

                                if (child_yang_name == "interface-info"):
                                    for c in self.interface_info:
                                        segment = c.get_segment_path()
                                        if (segment_path == segment):
                                            return c
                                    c = PfilterMa.Nodes.Node.Process.Ipv6.AclInfoTable.InterfaceInfos.InterfaceInfo()
                                    c.parent = self
                                    local_reference_key = "ydk::seg::%s" % segment_path
                                    self._local_refs[local_reference_key] = c
                                    self.interface_info.append(c)
                                    return c

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "interface-info"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass

                        def has_data(self):
                            return (self.interface_infos is not None and self.interface_infos.has_data())

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                (self.interface_infos is not None and self.interface_infos.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "acl-info-table" + path_buffer

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

                            if (child_yang_name == "interface-infos"):
                                if (self.interface_infos is None):
                                    self.interface_infos = PfilterMa.Nodes.Node.Process.Ipv6.AclInfoTable.InterfaceInfos()
                                    self.interface_infos.parent = self
                                    self._children_name_map["interface_infos"] = "interface-infos"
                                return self.interface_infos

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "interface-infos"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (self.acl_info_table is not None and self.acl_info_table.has_data())

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            (self.acl_info_table is not None and self.acl_info_table.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ipv6" + path_buffer

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

                        if (child_yang_name == "acl-info-table"):
                            if (self.acl_info_table is None):
                                self.acl_info_table = PfilterMa.Nodes.Node.Process.Ipv6.AclInfoTable()
                                self.acl_info_table.parent = self
                                self._children_name_map["acl_info_table"] = "acl-info-table"
                            return self.acl_info_table

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "acl-info-table"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class Ipv4(Entity):
                    """
                    Operational data for pfilter
                    
                    .. attribute:: acl_info_table
                    
                    	Operational data for pfilter
                    	**type**\:   :py:class:`AclInfoTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_pfilter_oper.PfilterMa.Nodes.Node.Process.Ipv4.AclInfoTable>`
                    
                    

                    """

                    _prefix = 'ip-pfilter-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(PfilterMa.Nodes.Node.Process.Ipv4, self).__init__()

                        self.yang_name = "ipv4"
                        self.yang_parent_name = "process"

                        self.acl_info_table = PfilterMa.Nodes.Node.Process.Ipv4.AclInfoTable()
                        self.acl_info_table.parent = self
                        self._children_name_map["acl_info_table"] = "acl-info-table"
                        self._children_yang_names.add("acl-info-table")


                    class AclInfoTable(Entity):
                        """
                        Operational data for pfilter
                        
                        .. attribute:: interface_infos
                        
                        	Operational data for pfilter
                        	**type**\:   :py:class:`InterfaceInfos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_pfilter_oper.PfilterMa.Nodes.Node.Process.Ipv4.AclInfoTable.InterfaceInfos>`
                        
                        

                        """

                        _prefix = 'ip-pfilter-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(PfilterMa.Nodes.Node.Process.Ipv4.AclInfoTable, self).__init__()

                            self.yang_name = "acl-info-table"
                            self.yang_parent_name = "ipv4"

                            self.interface_infos = PfilterMa.Nodes.Node.Process.Ipv4.AclInfoTable.InterfaceInfos()
                            self.interface_infos.parent = self
                            self._children_name_map["interface_infos"] = "interface-infos"
                            self._children_yang_names.add("interface-infos")


                        class InterfaceInfos(Entity):
                            """
                            Operational data for pfilter
                            
                            .. attribute:: interface_info
                            
                            	Operational data for pfilter in bag
                            	**type**\: list of    :py:class:`InterfaceInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_pfilter_oper.PfilterMa.Nodes.Node.Process.Ipv4.AclInfoTable.InterfaceInfos.InterfaceInfo>`
                            
                            

                            """

                            _prefix = 'ip-pfilter-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(PfilterMa.Nodes.Node.Process.Ipv4.AclInfoTable.InterfaceInfos, self).__init__()

                                self.yang_name = "interface-infos"
                                self.yang_parent_name = "acl-info-table"

                                self.interface_info = YList(self)

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
                                            super(PfilterMa.Nodes.Node.Process.Ipv4.AclInfoTable.InterfaceInfos, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(PfilterMa.Nodes.Node.Process.Ipv4.AclInfoTable.InterfaceInfos, self).__setattr__(name, value)


                            class InterfaceInfo(Entity):
                                """
                                Operational data for pfilter in bag
                                
                                .. attribute:: interface_name  <key>
                                
                                	Name of the interface
                                	**type**\:  str
                                
                                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                
                                .. attribute:: acl_info
                                
                                	acl information
                                	**type**\:  str
                                
                                

                                """

                                _prefix = 'ip-pfilter-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PfilterMa.Nodes.Node.Process.Ipv4.AclInfoTable.InterfaceInfos.InterfaceInfo, self).__init__()

                                    self.yang_name = "interface-info"
                                    self.yang_parent_name = "interface-infos"

                                    self.interface_name = YLeaf(YType.str, "interface-name")

                                    self.acl_info = YLeaf(YType.str, "acl-info")

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
                                                    "acl_info") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(PfilterMa.Nodes.Node.Process.Ipv4.AclInfoTable.InterfaceInfos.InterfaceInfo, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(PfilterMa.Nodes.Node.Process.Ipv4.AclInfoTable.InterfaceInfos.InterfaceInfo, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.interface_name.is_set or
                                        self.acl_info.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.interface_name.yfilter != YFilter.not_set or
                                        self.acl_info.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "interface-info" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

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
                                    if (self.acl_info.is_set or self.acl_info.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.acl_info.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "interface-name" or name == "acl-info"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "interface-name"):
                                        self.interface_name = value
                                        self.interface_name.value_namespace = name_space
                                        self.interface_name.value_namespace_prefix = name_space_prefix
                                    if(value_path == "acl-info"):
                                        self.acl_info = value
                                        self.acl_info.value_namespace = name_space
                                        self.acl_info.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                for c in self.interface_info:
                                    if (c.has_data()):
                                        return True
                                return False

                            def has_operation(self):
                                for c in self.interface_info:
                                    if (c.has_operation()):
                                        return True
                                return self.yfilter != YFilter.not_set

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "interface-infos" + path_buffer

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

                                if (child_yang_name == "interface-info"):
                                    for c in self.interface_info:
                                        segment = c.get_segment_path()
                                        if (segment_path == segment):
                                            return c
                                    c = PfilterMa.Nodes.Node.Process.Ipv4.AclInfoTable.InterfaceInfos.InterfaceInfo()
                                    c.parent = self
                                    local_reference_key = "ydk::seg::%s" % segment_path
                                    self._local_refs[local_reference_key] = c
                                    self.interface_info.append(c)
                                    return c

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "interface-info"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass

                        def has_data(self):
                            return (self.interface_infos is not None and self.interface_infos.has_data())

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                (self.interface_infos is not None and self.interface_infos.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "acl-info-table" + path_buffer

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

                            if (child_yang_name == "interface-infos"):
                                if (self.interface_infos is None):
                                    self.interface_infos = PfilterMa.Nodes.Node.Process.Ipv4.AclInfoTable.InterfaceInfos()
                                    self.interface_infos.parent = self
                                    self._children_name_map["interface_infos"] = "interface-infos"
                                return self.interface_infos

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "interface-infos"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (self.acl_info_table is not None and self.acl_info_table.has_data())

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            (self.acl_info_table is not None and self.acl_info_table.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ipv4" + path_buffer

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

                        if (child_yang_name == "acl-info-table"):
                            if (self.acl_info_table is None):
                                self.acl_info_table = PfilterMa.Nodes.Node.Process.Ipv4.AclInfoTable()
                                self.acl_info_table.parent = self
                                self._children_name_map["acl_info_table"] = "acl-info-table"
                            return self.acl_info_table

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "acl-info-table"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        (self.ipv4 is not None and self.ipv4.has_data()) or
                        (self.ipv6 is not None and self.ipv6.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.ipv4 is not None and self.ipv4.has_operation()) or
                        (self.ipv6 is not None and self.ipv6.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "process" + path_buffer

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

                    if (child_yang_name == "ipv4"):
                        if (self.ipv4 is None):
                            self.ipv4 = PfilterMa.Nodes.Node.Process.Ipv4()
                            self.ipv4.parent = self
                            self._children_name_map["ipv4"] = "ipv4"
                        return self.ipv4

                    if (child_yang_name == "ipv6"):
                        if (self.ipv6 is None):
                            self.ipv6 = PfilterMa.Nodes.Node.Process.Ipv6()
                            self.ipv6.parent = self
                            self._children_name_map["ipv6"] = "ipv6"
                        return self.ipv6

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "ipv4" or name == "ipv6"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.node_name.is_set or
                    (self.process is not None and self.process.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.node_name.yfilter != YFilter.not_set or
                    (self.process is not None and self.process.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "node" + "[node-name='" + self.node_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ip-pfilter-oper:pfilter-ma/nodes/%s" % self.get_segment_path()
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

                if (child_yang_name == "process"):
                    if (self.process is None):
                        self.process = PfilterMa.Nodes.Node.Process()
                        self.process.parent = self
                        self._children_name_map["process"] = "process"
                    return self.process

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "process" or name == "node-name"):
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
                path_buffer = "Cisco-IOS-XR-ip-pfilter-oper:pfilter-ma/%s" % self.get_segment_path()
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
                c = PfilterMa.Nodes.Node()
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
        path_buffer = "Cisco-IOS-XR-ip-pfilter-oper:pfilter-ma" + path_buffer

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
                self.nodes = PfilterMa.Nodes()
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
        self._top_entity = PfilterMa()
        return self._top_entity

