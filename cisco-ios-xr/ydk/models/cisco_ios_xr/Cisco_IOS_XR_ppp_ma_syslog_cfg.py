""" Cisco_IOS_XR_ppp_ma_syslog_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ppp\-ma\-syslog package configuration.

This module contains definitions
for the following management objects\:
  ppp\: PPP configuration

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Ppp(Entity):
    """
    PPP configuration
    
    .. attribute:: syslog
    
    	syslog option for session status
    	**type**\:   :py:class:`Syslog <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_syslog_cfg.Ppp.Syslog>`
    
    

    """

    _prefix = 'ppp-ma-syslog-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(Ppp, self).__init__()
        self._top_entity = None

        self.yang_name = "ppp"
        self.yang_parent_name = "Cisco-IOS-XR-ppp-ma-syslog-cfg"

        self.syslog = Ppp.Syslog()
        self.syslog.parent = self
        self._children_name_map["syslog"] = "syslog"
        self._children_yang_names.add("syslog")


    class Syslog(Entity):
        """
        syslog option for session status
        
        .. attribute:: enable_session_status
        
        	Enable syslog for ppp session status
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'ppp-ma-syslog-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Ppp.Syslog, self).__init__()

            self.yang_name = "syslog"
            self.yang_parent_name = "ppp"

            self.enable_session_status = YLeaf(YType.empty, "enable-session-status")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("enable_session_status") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Ppp.Syslog, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Ppp.Syslog, self).__setattr__(name, value)

        def has_data(self):
            return self.enable_session_status.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.enable_session_status.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "syslog" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ppp-ma-syslog-cfg:ppp/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.enable_session_status.is_set or self.enable_session_status.yfilter != YFilter.not_set):
                leaf_name_data.append(self.enable_session_status.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "enable-session-status"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "enable-session-status"):
                self.enable_session_status = value
                self.enable_session_status.value_namespace = name_space
                self.enable_session_status.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (self.syslog is not None and self.syslog.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.syslog is not None and self.syslog.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-ppp-ma-syslog-cfg:ppp" + path_buffer

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

        if (child_yang_name == "syslog"):
            if (self.syslog is None):
                self.syslog = Ppp.Syslog()
                self.syslog.parent = self
                self._children_name_map["syslog"] = "syslog"
            return self.syslog

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "syslog"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Ppp()
        return self._top_entity

