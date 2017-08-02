""" Cisco_IOS_XR_syslog_act 

This module contains a collection of YANG definitions
for Cisco IOS\-XR action package configuration.

This module contains definitions
for the following management objects\:
syslog\: Global Syslog messaging data

Copyright (c) 2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Logmsg(Entity):
    """
    
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_syslog_act.Logmsg.Input>`
    
    

    """

    _prefix = 'syslog-act'
    _revision = '2016-04-17'

    def __init__(self):
        super(Logmsg, self).__init__()
        self._top_entity = None

        self.yang_name = "logmsg"
        self.yang_parent_name = "Cisco-IOS-XR-syslog-act"

        self.input = Logmsg.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")


    class Input(Entity):
        """
        
        
        .. attribute:: message
        
        	Message body
        	**type**\:  str
        
        	**mandatory**\: True
        
        .. attribute:: severity
        
        	Set serverity level
        	**type**\:   :py:class:`Severity <ydk.models.ietf.ietf_syslog_types.Severity>`
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'syslog-act'
        _revision = '2016-04-17'

        def __init__(self):
            super(Logmsg.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "logmsg"

            self.message = YLeaf(YType.str, "message")

            self.severity = YLeaf(YType.enumeration, "severity")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("message",
                            "severity") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Logmsg.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Logmsg.Input, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.message.is_set or
                self.severity.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.message.yfilter != YFilter.not_set or
                self.severity.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-syslog-act:logmsg/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.message.is_set or self.message.yfilter != YFilter.not_set):
                leaf_name_data.append(self.message.get_name_leafdata())
            if (self.severity.is_set or self.severity.yfilter != YFilter.not_set):
                leaf_name_data.append(self.severity.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "message" or name == "severity"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "message"):
                self.message = value
                self.message.value_namespace = name_space
                self.message.value_namespace_prefix = name_space_prefix
            if(value_path == "severity"):
                self.severity = value
                self.severity.value_namespace = name_space
                self.severity.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (self.input is not None and self.input.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.input is not None and self.input.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-syslog-act:logmsg" + path_buffer

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

        if (child_yang_name == "input"):
            if (self.input is None):
                self.input = Logmsg.Input()
                self.input.parent = self
                self._children_name_map["input"] = "input"
            return self.input

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "input"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Logmsg()
        return self._top_entity

