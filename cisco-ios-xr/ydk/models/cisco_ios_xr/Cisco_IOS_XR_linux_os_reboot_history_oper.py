""" Cisco_IOS_XR_linux_os_reboot_history_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR linux\-os\-reboot\-history package operational data.

This module contains definitions
for the following management objects\:
  reboot\-history\: Reboot History information

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class RebootHistory(Entity):
    """
    Reboot History information
    
    .. attribute:: node
    
    	Node ID
    	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_linux_os_reboot_history_oper.RebootHistory.Node>`
    
    

    """

    _prefix = 'linux-os-reboot-history-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(RebootHistory, self).__init__()
        self._top_entity = None

        self.yang_name = "reboot-history"
        self.yang_parent_name = "Cisco-IOS-XR-linux-os-reboot-history-oper"

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
                    super(RebootHistory, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(RebootHistory, self).__setattr__(name, value)


    class Node(Entity):
        """
        Node ID
        
        .. attribute:: node_name  <key>
        
        	Node name
        	**type**\:  str
        
        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
        
        .. attribute:: reboot_history
        
        	Last Reboots
        	**type**\: list of    :py:class:`RebootHistory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_linux_os_reboot_history_oper.RebootHistory.Node.RebootHistory>`
        
        

        """

        _prefix = 'linux-os-reboot-history-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(RebootHistory.Node, self).__init__()

            self.yang_name = "node"
            self.yang_parent_name = "reboot-history"

            self.node_name = YLeaf(YType.str, "node-name")

            self.reboot_history = YList(self)

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
                        super(RebootHistory.Node, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(RebootHistory.Node, self).__setattr__(name, value)


        class RebootHistory(Entity):
            """
            Last Reboots
            
            .. attribute:: cause_code
            
            	Cause code for reboot
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: no
            
            	Number count
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: reason
            
            	Reason for reboot
            	**type**\:  str
            
            .. attribute:: time
            
            	Time of reboot
            	**type**\:  str
            
            

            """

            _prefix = 'linux-os-reboot-history-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(RebootHistory.Node.RebootHistory, self).__init__()

                self.yang_name = "reboot-history"
                self.yang_parent_name = "node"

                self.cause_code = YLeaf(YType.uint32, "cause-code")

                self.no = YLeaf(YType.uint32, "no")

                self.reason = YLeaf(YType.str, "reason")

                self.time = YLeaf(YType.str, "time")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cause_code",
                                "no",
                                "reason",
                                "time") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(RebootHistory.Node.RebootHistory, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(RebootHistory.Node.RebootHistory, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cause_code.is_set or
                    self.no.is_set or
                    self.reason.is_set or
                    self.time.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cause_code.yfilter != YFilter.not_set or
                    self.no.yfilter != YFilter.not_set or
                    self.reason.yfilter != YFilter.not_set or
                    self.time.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "reboot-history" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cause_code.is_set or self.cause_code.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cause_code.get_name_leafdata())
                if (self.no.is_set or self.no.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.no.get_name_leafdata())
                if (self.reason.is_set or self.reason.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.reason.get_name_leafdata())
                if (self.time.is_set or self.time.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.time.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cause-code" or name == "no" or name == "reason" or name == "time"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cause-code"):
                    self.cause_code = value
                    self.cause_code.value_namespace = name_space
                    self.cause_code.value_namespace_prefix = name_space_prefix
                if(value_path == "no"):
                    self.no = value
                    self.no.value_namespace = name_space
                    self.no.value_namespace_prefix = name_space_prefix
                if(value_path == "reason"):
                    self.reason = value
                    self.reason.value_namespace = name_space
                    self.reason.value_namespace_prefix = name_space_prefix
                if(value_path == "time"):
                    self.time = value
                    self.time.value_namespace = name_space
                    self.time.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.reboot_history:
                if (c.has_data()):
                    return True
            return self.node_name.is_set

        def has_operation(self):
            for c in self.reboot_history:
                if (c.has_operation()):
                    return True
            return (
                self.yfilter != YFilter.not_set or
                self.node_name.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "node" + "[node-name='" + self.node_name.get() + "']" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-linux-os-reboot-history-oper:reboot-history/%s" % self.get_segment_path()
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

            if (child_yang_name == "reboot-history"):
                for c in self.reboot_history:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = RebootHistory.Node.RebootHistory()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.reboot_history.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "reboot-history" or name == "node-name"):
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
        path_buffer = "Cisco-IOS-XR-linux-os-reboot-history-oper:reboot-history" + path_buffer

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

        if (child_yang_name == "node"):
            for c in self.node:
                segment = c.get_segment_path()
                if (segment_path == segment):
                    return c
            c = RebootHistory.Node()
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

    def clone_ptr(self):
        self._top_entity = RebootHistory()
        return self._top_entity

